#!/usr/bin/env node
// Configurable adversarial harness for prompt safety evaluation
// Scans prompts for prohibited patterns based on safety_class and configurable rules.
const fs = require('fs');
const path = require('path');

const promptsDir = fs.existsSync(path.join(process.cwd(), 'prompts')) ? 'prompts' : 'Prompts';
const indexPath = path.join(process.cwd(), promptsDir, 'index.json');
const mdPath = path.join(process.cwd(), promptsDir, 'Tem-Prompts.md');
const patternsPath = path.join(process.cwd(), 'guardrails', 'patterns.json');
const outDir = path.join(process.cwd(), 'eval-results');
fs.mkdirSync(outDir, { recursive: true });

// Load configuration files
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
const md = fs.readFileSync(mdPath, 'utf8');
const patternsConfig = JSON.parse(fs.readFileSync(patternsPath, 'utf8'));

const findings = [];
const warnings = [];

// Normalize guardrail config to support both legacy and new schemas
function materializeConfig(cfg) {
  if (cfg.patterns && cfg.safety_class_rules) {
    return cfg; // already in new format
  }
  const legacy = cfg.classes || {};
  const ro = (legacy['read-only'] && legacy['read-only'].prohibited) || [];
  const adv = (legacy['advisory'] && legacy['advisory'].prohibited) || [];
  const merged = [...ro, ...adv].map((p) => ({
    pattern: p.pattern,
    description: p.description || p.id || 'prohibited',
    severity: p.severity || 'medium',
    category: p.category || 'general'
  }));
  return {
    version: cfg.version || '1.0.0',
    patterns: {
      prohibited_for_non_lab: merged,
      informational: []
    },
    safety_class_rules: {
      'read-only': { check_patterns: ['prohibited_for_non_lab', 'informational'], fail_on_prohibited: true, fail_on_informational: false },
      'advisory': { check_patterns: ['prohibited_for_non_lab', 'informational'], fail_on_prohibited: true, fail_on_informational: false },
      'lab-only': { check_patterns: ['informational'], fail_on_prohibited: false, fail_on_informational: false }
    }
  };
}

const mat = materializeConfig(patternsConfig);

// Extract patterns based on configuration
function getCompiledPatterns(patternType) {
  return (mat.patterns[patternType] || []).map(p => ({
    regex: new RegExp(p.pattern, 'gi'),
    description: p.description,
    severity: p.severity,
    category: p.category,
    pattern: p.pattern
  }));
}

const prohibitedPatterns = getCompiledPatterns('prohibited_for_non_lab');
const informationalPatterns = getCompiledPatterns('informational');

// Process each prompt
for (const p of index.prompts) {
  const anchor = p.anchor.replace(/^#/, '');

  // Robust section matching across different formatting
  const headingRe = new RegExp(`^#{2,6}\\s+[^\\n]*\\{#${anchor}\\}[\\s\\S]*?(?=^#{2,6}\\s+|$)`, 'm');
  const enumeratedRe = new RegExp(`^\\s*\\d+[\\)\\.]\\s+[^\\n]*\\{#${anchor}\\}[\\s\\S]*?(?=^\\s*\\d+[\\)\\.]|$)`, 'm');

  let match = md.match(headingRe) || md.match(enumeratedRe);
  const section = match ? match[0] : '';

  if (!section) {
    warnings.push({
      id: p.id,
      title: p.title,
      issue: 'section_not_found',
      message: `Could not find section for anchor ${p.anchor}`
    });
    continue;
  }

  // Get safety class rules
  const safetyRules = mat.safety_class_rules[p.safety_class];
  if (!safetyRules) {
    warnings.push({
      id: p.id,
      title: p.title,
      issue: 'unknown_safety_class',
      message: `Unknown safety class: ${p.safety_class}`
    });
    continue;
  }

  // Severity threshold + per-prompt allowlist
  const order = { low: 1, medium: 2, high: 3 };
  const thresholds = (patternsConfig.severity_thresholds || {});
  const threshold = thresholds[p.safety_class] || 'high';
  const minRank = threshold === 'off' ? Infinity : (order[threshold] || 3);
  const allowlist = ((patternsConfig.per_prompt_allowlist || {})[p.id]) || [];

  // Check prohibited patterns
  if (safetyRules.check_patterns.includes('prohibited_for_non_lab')) {
    prohibitedPatterns.forEach((pattern) => {
      const matches = [...section.matchAll(pattern.regex)];
      matches.forEach(match => {
        if (allowlist.includes(pattern.description) || allowlist.includes(pattern.pattern)) return;
        const sevRank = order[(pattern.severity || 'high').toLowerCase()] || 3;
        const finding = {
          id: p.id,
          title: p.title,
          issue: 'prohibited_pattern',
          pattern: pattern.pattern,
          description: pattern.description,
          severity: pattern.severity,
          category: pattern.category,
          matched_text: match[0],
          safety_class: p.safety_class,
          should_fail: safetyRules.fail_on_prohibited && sevRank >= minRank
        };

        if (finding.should_fail) {
          findings.push(finding);
        } else {
          warnings.push(finding);
        }
      });
    });
  }

  // Check informational patterns
  if (safetyRules.check_patterns.includes('informational')) {
    informationalPatterns.forEach((pattern) => {
      const matches = [...section.matchAll(pattern.regex)];
      matches.forEach(match => {
        const finding = {
          id: p.id,
          title: p.title,
          issue: 'informational_pattern',
          pattern: pattern.pattern,
          description: pattern.description,
          severity: pattern.severity,
          category: pattern.category,
          matched_text: match[0],
          safety_class: p.safety_class,
          should_fail: safetyRules.fail_on_informational
        };

        if (safetyRules.fail_on_informational) {
          findings.push(finding);
        } else {
          warnings.push(finding);
        }
      });
    });
  }
}

// Generate comprehensive results
const result = {
  status: findings.length === 0 ? 'passed' : 'failed',
  timestamp: new Date().toISOString(),
  summary: {
    total_prompts: index.prompts.length,
    findings_count: findings.length,
    warnings_count: warnings.length,
    patterns_config_version: mat.version
  },
  findings,
  warnings,
  passed: findings.length === 0
};

// Write results
fs.writeFileSync(path.join(outDir, 'adversarial-results.json'), JSON.stringify(result, null, 2));

// Optional debug
if (process.env.DEBUG_ADV === '1') {
  const missed = warnings.filter(w => w.issue === 'section_not_found').length;
  console.log(`[adversarial] prompts=${index.prompts.length} missed=${missed}`);
}

// Log summary
console.log(`\nAdversarial Evaluation Summary:`);
console.log(`- Total prompts evaluated: ${result.summary.total_prompts}`);
console.log(`- Blocking findings: ${result.summary.findings_count}`);
console.log(`- Warnings: ${result.summary.warnings_count}`);

if (warnings.length > 0) {
  console.log(`\nWarnings (non-blocking):`);
  warnings.forEach(w => {
    console.log(`  - ${w.id}: ${w.issue} - ${w.message || w.description}`);
  });
}

if (!result.passed) {
  console.error(`\nBlocking findings detected:`);
  findings.forEach(f => {
    console.error(`  - ${f.id} (${f.safety_class}): ${f.description}`);
    console.error(`    Pattern: ${f.pattern}`);
    console.error(`    Matched: "${f.matched_text}"`);
  });
  process.exit(1);
}

console.log('\n✅ Adversarial evaluations passed - no blocking issues found.');

#!/usr/bin/env node
// ROE Token Compliance Checker
// Validates that lab-only prompts have appropriate ROE token requirements
const fs = require('fs');
const path = require('path');

const promptsDir = fs.existsSync(path.join(process.cwd(), 'prompts')) ? 'prompts' : 'Prompts';
const indexPath = path.join(process.cwd(), promptsDir, 'index.json');
const outDir = path.join(process.cwd(), 'eval-results');
fs.mkdirSync(outDir, { recursive: true });

// Load catalog
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

const issues = [];
const warnings = [];

// ROE compliance rules
const roeRules = {
  'lab-only': {
    requires_roe_token: true, // Should be true for lab-only prompts
    min_risk_level: 'medium', // Minimum risk level
    min_authorization: 'security_team' // Minimum authorization level
  },
  'advisory': {
    requires_roe_token: false, // Optional for advisory
    min_risk_level: 'low',
    min_authorization: 'supervisor'
  },
  'read-only': {
    requires_roe_token: false, // Not required for read-only
    min_risk_level: 'low',
    min_authorization: 'none'
  }
};

const riskLevels = ['low', 'medium', 'high', 'critical'];
const authLevels = ['none', 'supervisor', 'security_team', 'executive'];

function getRiskLevelIndex(level) {
  return riskLevels.indexOf(level);
}

function getAuthLevelIndex(level) {
  return authLevels.indexOf(level);
}

// Check each prompt for ROE compliance
index.prompts.forEach(prompt => {
  const rules = roeRules[prompt.safety_class];
  if (!rules) {
    warnings.push({
      type: 'unknown_safety_class',
      id: prompt.id,
      safety_class: prompt.safety_class,
      message: `Unknown safety class: ${prompt.safety_class}`
    });
    return;
  }

  // Check ROE token requirement
  const hasRoeToken = prompt.requires_roe_token === true;
  if (rules.requires_roe_token && !hasRoeToken) {
    issues.push({
      type: 'missing_roe_token',
      id: prompt.id,
      title: prompt.title,
      safety_class: prompt.safety_class,
      message: `${prompt.safety_class} prompts must set requires_roe_token: true`
    });
  }

  // Check risk level
  const riskLevel = prompt.risk_level;
  if (riskLevel) {
    const minRiskIndex = getRiskLevelIndex(rules.min_risk_level);
    const promptRiskIndex = getRiskLevelIndex(riskLevel);

    if (promptRiskIndex < minRiskIndex) {
      warnings.push({
        type: 'insufficient_risk_level',
        id: prompt.id,
        title: prompt.title,
        safety_class: prompt.safety_class,
        current_risk: riskLevel,
        minimum_risk: rules.min_risk_level,
        message: `Risk level "${riskLevel}" may be too low for ${prompt.safety_class} (minimum: ${rules.min_risk_level})`
      });
    }
  } else if (prompt.safety_class === 'lab-only') {
    warnings.push({
      type: 'missing_risk_level',
      id: prompt.id,
      title: prompt.title,
      safety_class: prompt.safety_class,
      message: `${prompt.safety_class} prompts should specify risk_level`
    });
  }

  // Check authorization level
  const authLevel = prompt.authorization_level;
  if (authLevel) {
    const minAuthIndex = getAuthLevelIndex(rules.min_authorization);
    const promptAuthIndex = getAuthLevelIndex(authLevel);

    if (promptAuthIndex < minAuthIndex) {
      warnings.push({
        type: 'insufficient_authorization',
        id: prompt.id,
        title: prompt.title,
        safety_class: prompt.safety_class,
        current_auth: authLevel,
        minimum_auth: rules.min_authorization,
        message: `Authorization level "${authLevel}" may be too low for ${prompt.safety_class} (minimum: ${rules.min_authorization})`
      });
    }
  } else if (prompt.safety_class !== 'read-only') {
    warnings.push({
      type: 'missing_authorization_level',
      id: prompt.id,
      title: prompt.title,
      safety_class: prompt.safety_class,
      message: `${prompt.safety_class} prompts should specify authorization_level`
    });
  }
});

// Generate results
const result = {
  status: issues.length === 0 ? 'passed' : 'failed',
  timestamp: new Date().toISOString(),
  summary: {
    total_prompts: index.prompts.length,
    lab_only_prompts: index.prompts.filter(p => p.safety_class === 'lab-only').length,
    roe_compliant: index.prompts.filter(p => p.requires_roe_token === true).length,
    compliance_issues: issues.length,
    warnings: warnings.length
  },
  compliance_rules: roeRules,
  issues,
  warnings,
  passed: issues.length === 0
};

// Write results
fs.writeFileSync(path.join(outDir, 'roe-compliance-results.json'), JSON.stringify(result, null, 2));

// Log output
console.log(`\nROE Token Compliance Check:`);
console.log(`- Total prompts: ${result.summary.total_prompts}`);
console.log(`- Lab-only prompts: ${result.summary.lab_only_prompts}`);
console.log(`- ROE-compliant prompts: ${result.summary.roe_compliant}`);
console.log(`- Compliance issues: ${result.summary.compliance_issues}`);
console.log(`- Warnings: ${result.summary.warnings}`);

if (issues.length > 0) {
  console.error(`\nCompliance issues (blocking):`);
  issues.forEach(issue => {
    console.error(`  - ${issue.id}: ${issue.message}`);
  });
}

if (warnings.length > 0) {
  console.log(`\nWarnings (non-blocking):`);
  warnings.forEach(warning => {
    console.log(`  - ${warning.id}: ${warning.message}`);
  });
}

if (!result.passed) {
  console.error(`\n❌ ROE compliance check failed - ${issues.length} issues found`);
  process.exit(1);
}

console.log(`\n✅ ROE compliance check passed`);

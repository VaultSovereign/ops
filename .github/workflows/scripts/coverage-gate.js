#!/usr/bin/env node
/**
 * Coverage Gate: ensure every prompt section in prompts/Tem-Prompts.md
 * has a corresponding entry in prompts/index.json (by anchor), and vice versa.
 *
 * Intent: Only validate actual prompt sections, not meta headers like
 * "Sources Ledger" or "Footnotes". Prompt sections are identified by explicit
 * anchors on headings (e.g., `## Title {#anchor}`) or by enumerated rows
 * (`1) Title {#anchor}`).
 */
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
let overrideOut = null;
let threshold = null;
for (let i = 0; i < args.length; i += 1) {
  const arg = args[i];
  if (arg === '--threshold') {
    const next = args[i + 1];
    const parsed = parseFloat(next);
    if (!Number.isFinite(parsed)) {
      console.error(`Invalid threshold value: ${next}`);
      process.exit(2);
    }
    threshold = parsed;
    i += 1;
    continue;
  }
  if (!overrideOut) {
    overrideOut = arg;
  }
}

const cwd = process.cwd();
const promptsDir = fs.existsSync(path.join(cwd, 'prompts')) ? 'prompts' : 'Prompts';
const mdPath = path.join(cwd, promptsDir, 'Tem-Prompts.md');
const indexPath = path.join(cwd, promptsDir, 'index.json');
const outDir = path.join(cwd, 'eval-results');
fs.mkdirSync(outDir, { recursive: true });
const outPath = overrideOut
  ? path.resolve(cwd, overrideOut)
  : path.join(outDir, 'coverage-results.json');
fs.mkdirSync(path.dirname(outPath), { recursive: true });

const slugify = (s) =>
  s
    .toLowerCase()
    .replace(/[^\w\s-]/g, '') // drop punctuation
    .trim()
    .replace(/\s+/g, '-') // spaces -> dashes
    .replace(/-+/g, '-'); // collapse

const md = fs.readFileSync(mdPath, 'utf8');
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

// 1) Collect sections that could map to a prompt (require explicit anchors)
const explicitSections = [];
for (const line of md.split(/\r?\n/)) {
  let m = line.match(/^(#{2,6})\s+(.+?)\s*(?:\{#([A-Za-z0-9._:-]+)\})?\s*$/);
  if (m) {
    const titleText = m[2].trim();
    const explicit = m[3] ? `#${m[3]}`.toLowerCase() : null;
    if (explicit) {
      explicitSections.push({ title: titleText, anchor: explicit });
    }
    continue;
  }

  // Support legacy enumerated style with explicit anchors
  m = line.match(/^\s*\d+[\)\.]\s+(.+?)\s*(?:\{#([A-Za-z0-9._:-]+)\})?\s*$/);
  if (m) {
    const titleText = m[1].trim();
    const explicit = m[2] ? `#${m[2]}`.toLowerCase() : null;
    if (explicit) {
      explicitSections.push({ title: titleText, anchor: explicit });
    }
  }
}

// 2) Collect anchors from index.json
const indexArr = Array.isArray(index) ? index : (index.prompts || []);
const indexedAnchors = new Set(indexArr.map((e) => (e.anchor || '').trim().toLowerCase()).filter(Boolean));

// 3) Compute diffs across explicit sections
const mdAnchorSet = new Set(explicitSections.map((s) => s.anchor));
const missingInIndex = [...mdAnchorSet]
  .filter((a) => !indexedAnchors.has(a))
  .map((a) => explicitSections.find((s) => s.anchor === a));
const extraInIndex = indexArr.filter((e) => e.anchor && !mdAnchorSet.has(e.anchor.toLowerCase()));

// 4) Build machine-readable result
const result = {
  status: missingInIndex.length || extraInIndex.length ? 'failed' : 'passed',
  timestamp: new Date().toISOString(),
  summary: {
    markdown_prompt_sections: explicitSections.length,
    catalog_entries: indexArr.length,
    missing_entries: missingInIndex.length,
    extra_entries: extraInIndex.length,
    coverage_percentage: explicitSections.length
      ? Math.round(((explicitSections.length - missingInIndex.length) / explicitSections.length) * 100)
      : 100
  },
  issues: {
    missing_in_index: missingInIndex,
    extra_in_index: extraInIndex
  },
  passed: !(missingInIndex.length || extraInIndex.length)
};

fs.writeFileSync(outPath, JSON.stringify(result, null, 2));

// Optional debug
if (process.env.DEBUG_COVERAGE === '1') {
  console.log(`[coverage] sections_detected=${explicitSections.length} index_entries=${indexArr.length}`);
  console.log(`[coverage] sample_sections=` + explicitSections.slice(0, 3).map((s) => s.anchor).join(', '));
}

// 5) Human-readable output + exit code
const coveragePct = result.summary.coverage_percentage;

if (!result.passed) {
  console.error('❌ Coverage gate failed.');
  if (missingInIndex.length) {
    console.error('\nPrompt sections missing in prompts/index.json:');
    missingInIndex.forEach((s) => console.error(`  - ${s.title}  (${s.anchor})`));
  }
  if (extraInIndex.length) {
    console.error('\nCatalog entries without matching prompt section in Tem-Prompts.md:');
    extraInIndex.forEach((e) => console.error(`  - ${e.title}  (${e.anchor})`));
  }
  process.exit(1);
}

if (threshold !== null && coveragePct < threshold) {
  console.error(
    `❌ Coverage gate below threshold: required ${threshold}% | actual ${coveragePct}%`
  );
  process.exit(1);
}

console.log('✅ Coverage gate passed: prompts catalog matches enumerated sections.');

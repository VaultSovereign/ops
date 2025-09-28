#!/usr/bin/env node
// Footer Gate with minimal variant + exceptions
const fs = require('fs');
const path = require('path');

const root = process.cwd();
const args = process.argv.slice(2);
const startDir = args.find(a=>!a.startsWith('--')) ? path.resolve(root, args.find(a=>!a.startsWith('--'))) : root;
const changedOnly = args.includes('--changed');

const FULL_FOOTER_ONE_LINE = '© VaultMesh — Earth’s Civilization Ledger • TEM';
const FULL_FOOTER_TWO_LINE_RE = /©\s*VaultMesh\s*—\s*Earth[’']s\s*Civilization\s*Ledger\s*\n?\s*•\s*TEM/i;
const MINIMAL_FOOTER = '© VaultMesh • TEM';
const MINIMAL_DIRECTIVE_RE = /<!--\s*vaultmesh:footer=minimal\s*-->/i;

function readConfig() {
  const cfgPath = path.join(root, 'docs', 'footer.config.json');
  try {
    let txt = fs.readFileSync(cfgPath, 'utf8');
    // strip // and /* */ comments
    txt = txt.replace(/\/\*[\s\S]*?\*\//g, '').replace(/(^|\n)\s*\/\/.*(?=\n|$)/g, '$1');
    const cfg = JSON.parse(txt);
    return cfg && cfg.ignore_globs ? cfg : { ignore_globs: [] };
  } catch {
    return { ignore_globs: [] };
  }
}

const cfg = readConfig();

// Basic glob matcher (supports **, *, ?)
function globToRegExp(glob) {
  const esc = (s) => s.replace(/[.+^${}()|[\]\\]/g, '\\$&');
  let re = '^' + glob.split('**').map(part => esc(part).replace(/\\\*/g, '[^/]*').replace(/\\\?/g, '.')).join('(?:.*)') + '$';
  return new RegExp(re);
}

const ignoreGlobs = (cfg.ignore_globs || []).map(g => globToRegExp(g));

function isIgnored(relPath) {
  return ignoreGlobs.some(rx => rx.test(relPath));
}

function* walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    const rel = p.replace(root + path.sep, '');
    if (rel.startsWith('.git')) continue;
    if (e.isDirectory()) {
      if (rel === '.github' || rel.startsWith('node_modules') || rel.startsWith('vendor') || rel.startsWith('dist') || rel.startsWith('build')) continue;
      if (isIgnored(rel + '/')) continue;
      yield* walk(p);
    } else if (e.isFile() && e.name.endsWith('.md')) {
      if (!isIgnored(rel)) yield p;
    }
  }
}

function tail(content, nLines = 60) {
  const lines = content.split(/\r?\n/);
  return lines.slice(-nLines).join('\n');
}

function hasFullFooter(s) {
  return s.includes(FULL_FOOTER_ONE_LINE) || FULL_FOOTER_TWO_LINE_RE.test(s);
}

function hasMinimalFooter(s) {
  return s.includes(MINIMAL_FOOTER);
}

const failures = [];
const checked = [];
// Collect files to check
let candidates = [];
if (changedOnly) {
  try {
    const base = process.env.GITHUB_BASE_REF || process.env.BASE_REF || 'HEAD~1';
    const { execSync } = require('child_process');
    const out = execSync(`git diff --name-only ${base}...HEAD`, { encoding: 'utf8' });
    candidates = out.split(/\r?\n/).filter(f => f.endsWith('.md')).map(f => path.join(root, f));
  } catch (e) {
    // fallback to full walk
    candidates = Array.from(walk(startDir));
  }
} else {
  candidates = Array.from(walk(startDir));
}

for (const file of candidates) {
  const rel = file.replace(root + path.sep, '');
  const content = fs.readFileSync(file, 'utf8');
  const scope = tail(content, 80);
  const allowMinimal = MINIMAL_DIRECTIVE_RE.test(content);

  const ok = hasFullFooter(scope) || (allowMinimal && hasMinimalFooter(scope));
  if (!ok) {
    failures.push({ file: rel, allowMinimal });
  }
  checked.push(rel);
}

if (failures.length) {
  console.error('Footer gate failed for the following files:');
  for (const f of failures) {
    console.error(' - ' + f.file + (f.allowMinimal ? ' (minimal allowed)' : ''));
  }
  console.error('\nRequired footer (full):\n');
  console.error('<p align="center"><sub>© VaultMesh — Earth’s Civilization Ledger • TEM</sub></p>');
  console.error('\nOptional minimal variant (only if directive is present anywhere in file):\n');
  console.error('<!-- vaultmesh:footer=minimal -->');
  console.error('<p align="center"><sub>© VaultMesh • TEM</sub></p>');
  process.exit(1);
}

console.log(`✅ Footer check passed for ${checked.length} file(s).`);

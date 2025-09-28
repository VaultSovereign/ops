#!/usr/bin/env node
/**
 * Generates docs/index.md from prompts/index.json
 * Safe to run on PR; recommended to run on default branch via PR automation.
 */
const fs = require('fs');
const path = require('path');

const idxPath = path.join(process.cwd(), 'prompts', 'index.json');
const idxRaw = JSON.parse(fs.readFileSync(idxPath, 'utf8'));
const idx = Array.isArray(idxRaw) ? idxRaw : idxRaw.prompts || [];

// Tools index (optional)
let tools = [];
try {
  const toolsPath = path.join(process.cwd(), 'tools', 'index.json');
  const toolsRaw = JSON.parse(fs.readFileSync(toolsPath, 'utf8'));
  tools = toolsRaw.tools || [];
} catch (_) {
  tools = [];
}

const rows = idx
  .slice()
  .sort((a, b) => (a.title || '').localeCompare(b.title || ''))
  .map((e) => {
    const link = `${e.path}${e.anchor ? e.anchor : ''}`;
    const tags = (e.tags || []).join(', ');
    return `| \`${e.id}\` | [${e.title}](${link}) | ${e.safety_class || ''} | ${tags} | ${e.owner || ''} |`;
  })
  .join('\n');

const toolsRows = tools
  .slice()
  .sort((a, b) => (a.title || '').localeCompare(b.title || ''))
  .map((t) => {
    const tags = (t.tags || []).join(', ');
    return `| \`${t.id}\` | [${t.title}](${t.path}) | ${tags} |`;
  })
  .join('\n');

const toolsSection = tools.length
  ? `\n## Tools\n\n| ID | Title | Tags |\n|---|---|---|\n${toolsRows}\n`
  : '';

const footer = `\n— VaultMesh · Earth’s Civilization Ledger —\n© Vault Sovereign · https://vaultmesh.example/\n`;

const body = `# VaultMesh TEM — Prompt Index

> Auto-generated from \`prompts/index.json\`. Do not edit manually.

| ID | Title | Safety | Tags | Owner |
|---|---|---|---|---|
${rows}
${toolsSection}
${footer}`;

const outDir = path.join(process.cwd(), 'docs');
fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, 'index.md'), body, 'utf8');

console.log('✅ Generated docs/index.md');

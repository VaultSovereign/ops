# Repository Guidelines

## Scope
VaultMesh TEM Ops is an operational repository for Mine with a security‑first posture. It includes prompts, runbooks, tools/matrices, guardrails, and governance. Treat prompts and catalogs as APIs; treat runbooks and tools as production ops assets.

## Project Structure & Module Organization
- `prompts/` — TEM grimoire (`Tem-Prompts.md`), catalog (`index.json`), schema.
- `runbooks/` — Operational procedures (incidents, daily ops), scoped and actionable.
- `guides/` & `templates/` — How‑tos and document templates (inherit standard footer).
- `tools/` — Operational matrices (`Tool‑Matrix.md`, `Lawful‑Intercept‑Matrix.md`) + `index.json`.
- `guardrails/` — Safety policy, patterns, mappings to OWASP LLM + NIST SSDF.
- `docs/` — Auto‑generated index and automation docs (footer config lives here).
- `.github/workflows/` — CI gates (lint, schemas, coverage, evals, docs, badges).

## Build, Test, and Development Commands
- Validate catalogs:
  - `npx --yes ajv-cli@5 validate -s prompts/index.schema.json -d prompts/index.json`
  - `npx --yes ajv-cli@5 validate -s tools/index.schema.json -d tools/index.json`
- Coverage gate: `node .github/workflows/scripts/coverage-gate.js` (anchors ↔ catalog)
- Adversarial evals: `node .github/workflows/scripts/adversarial-evals.js` (thresholds + allowlist)
- Docs index: `node .github/workflows/scripts/generate-docs-index.js`
- Footer gate: `node .github/workflows/scripts/footer-check.js [--changed]`

## Coding Style & Naming Conventions
- Prompts: include purpose, inputs, outputs, safety class; ids in kebab‑case (e.g., `recon-assistant`).
- Headings use stable anchors `{#id}` referenced in catalogs.
- Markdown lint via `markdownlint-cli2` (CI); keep sections scannable and concise.

## Testing Guidelines (Gates)
- Schemas (AJV), Coverage gate (content/catalog lockstep), Adversarial evals (guardrails/patterns.json), Footer presence (full or minimal with `<!-- vaultmesh:footer=minimal -->`).

## Commit & Pull Request Guidelines
- Commits: concise, imperative (e.g., `docs: refresh index`, `runbooks: add triage checklist`).
- PRs: update catalogs when adding/modifying prompts/tools; bump `CHANGELOG.md` for schema/output changes; pass all CI gates.
- Use PR template; CODEOWNERS enforce review for guardrails/workflows.

## Security & Ops Notes
- Private vuln reporting: see `SECURITY.md`.
- No secrets or weaponized payloads; offensive content is pseudocode‑only and lab‑scoped.
- Lawful use: tools/runbooks must include scope, consent, and assumptions.

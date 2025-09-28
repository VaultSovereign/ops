# Repository Guidelines

## Project Structure & Module Organization
- `docs/`: Public documentation, CI, and badge configs (see `docs/index.md`, `docs/footer.config.json`).
- `guides/`, `runbooks/`, `tools/`, `templates/`: Operational knowledge, playbooks, tool indexes, and content templates.
- `prompts/`: Prompt libraries and schemas (`prompts/index.json`, `prompts/index.schema.json`).
- `guardrails/`: Policy and pattern definitions that CI validates.
- `scripts/`: Small utilities used locally and in CI (Python + Bash).
- `eval-results/`: JSON outputs consumed by coverage and ROE gates.
- `.github/`: Issue/PR templates and CI scripts under `.github/workflows/scripts/`.

## Build, Test, and Development Commands
- Aggregate validation suite: `make check` (schema, markdown, footer, guardrails)
- Regenerate docs index: `make docs:index`
- Coverage + adversarial evals: `make evals` (`COVERAGE_THRESHOLD` env overrides 80%)
- ROE-only gate (manual): `make roe`
- Badge refresh: `make badges`
- Prompt metadata placeholder: `make prompts:sync`
- PR auto-summary (requires `GITHUB_TOKEN` + PR context): `make pr:summary`
- Create a new note: `bash scripts/new_note.sh "Title" path/dir`
- MCP knowledge summon (example): `python scripts/mcp_knowledge_summon.py --config templates/mcp-summon.config.json`

## Coding Style & Naming Conventions
- Markdown: Use clear headings, one H1 per file, include required footer block per `docs/footer.config.json`.
- Filenames: Knowledge articles use Title Case (spaces allowed), scripts use `snake_case.py` or `kebab-case.sh`.
- JSON: 2-space indent, valid against `*.schema.json` when present.
- Python: PEP 8 (4 spaces), small focused scripts; JavaScript: Node 18+, prefer ES modules if editing CI scripts.

## Testing Guidelines
- No unit test suite; validate via CI utilities:
  - Update `eval-results/*.json` and run coverage/ROE gates locally (see commands above).
  - For JSON changes, validate against associated schema files.

## Commit & Pull Request Guidelines
- Commits: Imperative present tense; prefer Conventional Commits (e.g., `feat:`, `fix:`) for changelog clarity.
- PRs must include: concise description, linked issues, impacted paths, and screenshots/GIFs for documentation UX changes.
- Before opening a PR: regenerate docs index, run footer check, and run coverage/ROE gates if applicable.

## Security & Configuration Tips
- Do not commit secrets or sensitive identifiers. Avoid PII in `eval-results/` and examples.
- Changes to `guardrails/` require a brief rationale and a link to policy context.

## Agent-Specific Instructions
- Prefer minimal diffs; adhere to these guidelines for any file you modify.
- When editing JSON or Markdown, also update related indexes and run local checks shown above.


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/

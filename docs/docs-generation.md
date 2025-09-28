# Docs Generation

- Source of truth: `prompts/index.json`
- Generator: `.github/workflows/scripts/generate-docs-index.js`
- Output: `docs/index.md` (auto-PR on push to default branch)

## Tools Section

- Optional catalog: `tools/index.json`
- The generator appends a Tools table when this file exists.

## Extending

- Add new sections (e.g., Guardrails) by reading more catalogs in the generator and appending tables.
- Keep outputs deterministic to avoid noisy PRs.

______________________________________________________________________

— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · <https://vaultmesh.example/>

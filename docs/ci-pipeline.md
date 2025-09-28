# CI Pipeline

Workflow: `/.github/workflows/evals.yml`

Triggers

- push to default branches (main/master)
- pull_request
- workflow_dispatch (badges job)

Stages

- Markdown Lint: `markdownlint-cli2`
- Schema Validation: `ajv-cli` validates `prompts/index.json`
- ROE Compliance: `roe-compliance.js` enforces `requires_roe_token` for lab-only
- Coverage Gate: ensures `prompts/Tem-Prompts.md` ↔ `prompts/index.json` anchors match
- Adversarial Evals: scans content vs `guardrails/patterns.json`
- Docs Job (push only): generates `docs/index.md` and opens PR

Local runs

````text
# From repo root
npx --yes ajv-cli@5 validate -s prompts/index.schema.json -d prompts/index.json
node .github/workflows/scripts/coverage-gate.js
node .github/workflows/scripts/roe-compliance.js
node .github/workflows/scripts/adversarial-evals.js
node .github/workflows/scripts/generate-docs-index.js
```text

______________________________________________________________________

— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · <https://vaultmesh.example/>
````

______________________________________________________________________

<p align="center"><sub>© VaultMesh - Earth's Civilization Ledger • TEM</sub></p>

— VaultMesh · Earth's Civilization Ledger —
© Vault Sovereign · <https://vaultmesh.example/>

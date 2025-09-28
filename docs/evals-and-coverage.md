# Evals and Coverage

## Adversarial Evaluations
- Config-driven patterns: `guardrails/patterns.json`
- Script: `.github/workflows/scripts/adversarial-evals.js`
- Blocks non-lab prompts if prohibited patterns appear.
- Outputs: `eval-results/adversarial-results.json`

## Coverage Gate
- Script: `.github/workflows/scripts/coverage-gate.js`
- Compares anchors in `prompts/Tem-Prompts.md` against catalog entries in `prompts/index.json`.
- Accepts explicit anchors `{#anchor}` or slugified headers.
- Fails CI if mismatched.

## ROE Compliance
- Script: `.github/workflows/scripts/roe-compliance.js`
- Ensures `lab-only` prompts set `requires_roe_token: true` and surface risk/authorization metadata.
- Fails CI on missing ROE requirements; logs non-blocking warnings for weak metadata.

## Local Debug
```
node .github/workflows/scripts/adversarial-evals.js || true
node .github/workflows/scripts/coverage-gate.js || true
jq . eval-results/adversarial-results.json 2>/dev/null || true
```

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


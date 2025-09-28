# Contributing

Thanks for helping improve the TEM Prompt Library.

## How to Contribute
1. Fork the repo and create a feature branch.
2. Make changes with focused commits.
3. Update `prompts/index.json` for any new/changed prompts.
4. Run local checks:
   - `npx --yes markdownlint-cli2 **/*.md`
   - `npx --yes ajv-cli@5 validate -s prompts/index.schema.json -d prompts/index.json`
5. Update `CHANGELOG.md`.
6. Open a PR and fill out the checklist.

## Security
Do not include secrets, tokens, or weaponized payloads. Report vulnerabilities via Private vulnerability reporting or email in `SECURITY.md`.

## Style
- Treat prompts as code: include purpose, inputs, outputs, and safety notes.
- Prefer structured outputs (JSON/YAML) and tags.

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


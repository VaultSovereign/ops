# Badges and Supply Chain Signals

## OpenSSF Scorecards
- Badge and viewer driven off repo coordinates.
- Updater: `.github/workflows/scripts/update-badges.js`
- Run via `workflow_dispatch` with env: `REPO_OWNER`, `REPO_NAME`, `OSSF_BP_ID`.

## OpenSSF Best Practices
- Register project to get an ID.
- Replace placeholder ID in README or run the updater.

## Recommendations
- Enable branch protection with required checks.
- Keep Actions minimal-permission and pin action versions.
- Periodically review CI logs and eval artifacts.

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


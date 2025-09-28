# Signals System (Draft)

Purpose: Define a weighted signaling model to inform governance without replacing due process.

## Model

- Signal: `{ id, title, description, source, weight, epoch, scope, tags }`
- Weight: 0.0–1.0 (source reputation × recency × verification)
- Epochs: daily, weekly, monthly, quarterly; anchored to UTC boundaries
- Scope: repo, program, federation

## Process

- Collection: proposals/issues/discussions produce signals
- Verification: provenance and supporting evidence linked
- Aggregation: rolling weighted means and trend deltas per tag/scope
- Publication: weekly digest in `docs/digests/` and artifact in CI

## Artifacts

- JSON feed: `signals/*.json` (append‑only by epoch)
- Schema: `docs/schemas/signal.schema.json` (AJV‑valid)
- Digest: `docs/digests/YYYY‑WW.md`

## Open Questions

- Reputation model (who assigns, decay rate)
- Federation merge rules (conflict, quorum)

______________________________________________________________________

<p align="center"><sub>© VaultMesh — Earth’s Civilization Ledger • TEM</sub></p>

______________________________________________________________________

<p align="center"><sub>© VaultMesh - Earth's Civilization Ledger • TEM</sub></p>

— VaultMesh · Earth's Civilization Ledger —
© Vault Sovereign · <https://vaultmesh.example/>

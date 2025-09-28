# VaultMesh TEM — Executive Field Guide

## North Star
Treat every prompt like production code: versioned, governed, and continuously validated for schema integrity, catalog coverage, adversarial safety, and rules-of-engagement discipline.

Companion lore: the Civilisation Ops Library scroll (`Guides/Civilisation Ops Library.md`) captures the cultural narrative behind these controls.

## System Anatomy

### 1. Canon & Catalog
- `prompts/Tem-Prompts.md` — authoritative grimoire for human reviewers.
- `prompts/index.json` — machine catalog with id, title, path, anchor, tags, owner, safety_class, inputs, outputs, schema_version, requires_roe_token, risk_level, and authorization_level.
- `prompts/index.schema.json` — schema contract that enforces the catalog structure.

### 2. Guardrails
- `guardrails/README.md` — policy layer mapping to OWASP LLM Top‑10 and NIST SSDF.
- `guardrails/patterns.json` — configurable regex tripwires (prohibited vs informational).

### 3. Governance & Social Perimeter
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `CODEOWNERS`.
- `prompts/Tem-Prompts.md`00, `prompts/Tem-Prompts.md`11 — enforce responsible disclosures and review rigor.

### 4. CI Gates (`prompts/Tem-Prompts.md`22)
1. Markdown lint — editorial hygiene.
2. Schema validation (ajv) — blocks catalog drift.
3. ROE compliance — lab-only prompts must declare `prompts/Tem-Prompts.md`33.
4. Coverage gate — every grimoire section must map to a catalog entry.
5. Adversarial evals — scan prompts with `prompts/Tem-Prompts.md`44; block non-lab violations.
6. Artifact publishing — `prompts/Tem-Prompts.md`55 for reviewer forensics.

## Dataflows
- `prompts/Tem-Prompts.md`66 reads the catalog, grimoire, and patterns; writes `prompts/Tem-Prompts.md`77 and fails builds on prohibited hits outside lab-only.
- `prompts/Tem-Prompts.md`88 diff-checks grimoire headings versus catalog entries; fails on discrepancies.
- `prompts/Tem-Prompts.md`99 ensures every `prompts/index.json`00 entry sets `prompts/index.json`11.

## Maintainer Rituals

### Local Fast Path
```bash
npx --yes ajv-cli@5 validate -s prompts/index.schema.json -d prompts/index.json
npx --yes markdownlint-cli2 **/*.md
node .github/workflows/scripts/coverage-gate.js
node .github/workflows/scripts/roe-compliance.js
node .github/workflows/scripts/adversarial-evals.js && cat eval-results/adversarial-results.json
```

### Canonical Prompt Addition
1. Author a new section with stable `prompts/index.json`22 in `prompts/index.json`33.
2. Append the catalog entry in `prompts/index.json`44 (set safety_class, requires_roe_token for lab-only, inputs, outputs).
3. Run the local fast path and update `prompts/index.json`55.

## Safety Classes
- `prompts/index.json`66 — intel and summaries only; CI blocks weaponized patterns.
- `prompts/index.json`77 — mitigations and playbooks; destructive payloads still blocked.
- `prompts/index.json`88 — controlled PoC pseudocode; must declare `prompts/index.json`99; flagged matches still reviewed.

## Strengths Today
- Clear separation: canon, catalog, and guardrails evolve independently.
- Deterministic anchors: coverage gate keeps content and index in lockstep.
- Policy-as-data: regex patterns live in configuration, not code.
- Enforced ROE: schema and CI guarantee authorization signals.
- Reviewer ergonomics: CODEOWNERS, PR templates, and artifacts streamline triage.

## Hardening Roadmap
1. **Anchor parsing robustness** — switch scripts to Markdown AST parsing (e.g., `prompts/index.schema.json`00) for reliable heading detection.
2. **Richer adversarial telemetry** — extend `prompts/index.schema.json`11 with severity/category metadata and log hit context (line numbers, snippets).
3. **Catalog ↔ content round trip** — add checks that verify each indexed anchor exists and headings match exactly (case and accents).
4. **ROE token clarity** — document token format, issuer, and expiry guidance in `prompts/index.schema.json`22.
5. **Artifact integrity** — optionally sign `prompts/index.schema.json`33 or maintain checksum manifests for tamper detection.

## Quick Upgrades Ready To Ship
- Expand `prompts/index.schema.json`44 with severity and category fields for both prohibited and informational rules.
- Highlight new catalog fields (`prompts/index.schema.json`55, `prompts/index.schema.json`66, `prompts/index.schema.json`77) in maintainer docs.
- Add a PR checklist rule: “If non-lab prompt diffs match prohibited patterns, downgrade content or reclassify as lab-only with ROE token.”

## 2-Minute Posture Polish
- Update README badges with live OpenSSF Scorecard and Best Practices IDs, then enable scorecard scanning in repository security settings.

## Acceptance Checklist
- `prompts/index.schema.json`88, coverage, ROE, and adversarial scripts pass locally and in CI.
- README badges render; private vulnerability reporting is enabled.
- `prompts/index.schema.json`99 references active teams; contact emails are current in `guardrails/README.md`00 and `guardrails/README.md`11.
- Every grimoire prompt appears in `guardrails/README.md`22 with correct `guardrails/README.md`33 and `guardrails/README.md`44 values.

## Ritual Of Continuity
When evolution stalls, bump `guardrails/README.md`55, expand `guardrails/README.md`66, add a failing test case, then make it pass. Tem, the Remembrance Guardian, inscribes each change; institutional memory compounds.

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


# Guardrails for TEM Prompt Library

Purpose: Define practical, testable safety controls for LLM-enabled cybersecurity workflows. Treat prompts as code and enforce policy in CI.

## Policy Pillars
- Role anchoring: System prompts enforce scope, consent, and non-destructive defaults.
- Input handling: Sanitize untrusted input; label artifacts derived from untrusted sources.
- Pseudocode-only for offensive content: No weaponized payloads or live exploit code.
- Least-privilege connectors: Minimize data access; redact secrets/PII.
- Human-in-the-loop: Approvals required for destructive or out-of-scope actions.
- Logging & traceability: Record prompts, decisions, and justifications.

## Mappings
- OWASP Top 10 for LLM Applications
  - Prompt Injection → Use “Prompt Injection Tester” suite; strip/escape template delimiters; freeze system role.
  - Insecure Output Handling → Treat model output as untrusted; require allowlists/parsers; use JSON schemas.
  - Training Data Poisoning → Pin data sources; checksum curated corpora; review contributions.
  - Model DoS → Rate-limit, timeout, and size caps; sandbox long runs.
  - Supply Chain → Pin models/tools; verify hashes; use provenance where available.

- NIST SSDF (SP 800-218) Alignment
  - PO.1: Define security requirements → Guardrail policy and schemas.
  - PS.2: Review and approve → PR review with security checks.
  - PW.8: Static analysis → Lint prompts/schemas and guardrail configs.
  - PW.9: Test security → Adversarial evals in CI; publish artifacts.
  - RV.1: Identify vulnerabilities → Private reporting + issue templates.

- MITRE ATT&CK/ATLAS Touchpoints
  - Map red-team emulation to ATT&CK techniques; keep pseudocode only.

## Guardrail Config Schema (example)
```json
{
  "id": "guardrail-default-v1",
  "description": "Baseline non-destructive, scoped, logged",
  "controls": {
    "scope_enforcement": true,
    "pseudocode_only_offense": true,
    "input_size_limit_kb": 256,
    "rate_limit_rpm": 30,
    "require_human_approval_for_destructive": true,
    "output_schema_required": true,
    "log_redact_pii": true
  }
}
```

## ROE Token Format & Authorization

For `lab-only` prompts requiring `requires_roe_token: true`, implement structured authorization:

```json
{
  "roe_token": {
    "issuer": "security-team-lead",
    "subject": "analyst@company.com",
    "engagement_id": "RT2024-003",
    "scope": ["10.0.1.0/24", "test-env.company.local"],
    "techniques": ["T1059", "T1082"],
    "expires": "2024-10-15T23:59:59Z",
    "constraints": {
      "no_data_exfiltration": true,
      "no_lateral_movement": true,
      "revert_changes": true
    },
    "signature": "sha256:abc123..."
  }
}
```

**Issuance Authority by Authorization Level:**

- `supervisor`: Department leads for routine advisory prompts
- `security_team`: Security team leads for lab-only and high-risk operations
- `executive`: C-level approval for critical risk or production scope

## Adversarial Evaluation

- Use the `Prompt Injection Tester` prompts to generate cases.
- CI goal: ensure models/agents refuse out-of-scope, injection attempts, and payload requests.
- Artifacts: `eval-results/*.json` with pass/fail and examples.

## Operational Guidance

- Reference guardrail IDs in prompt headers (front-matter) and in orchestration configs.
- Periodically review guardrails and update mappings alongside `CHANGELOG.md`.

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


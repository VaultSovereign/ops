# VaultMesh TEM — Security-Grade Prompt Library

<!-- Populate real badges when the repository slug is public
[![OpenSSF Best Practices](https://www.bestpractices.coreinfrastructure.org/projects/badge?id=YOUR_ID)](https://www.bestpractices.coreinfrastructure.org/projects/YOUR_ID)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/YOUR_ORG/YOUR_REPO/badge)](https://securityscorecards.dev/viewer/?uri=github.com/YOUR_ORG/YOUR_REPO)
[![GitHub release](https://img.shields.io/github/v/release/YOUR_ORG/YOUR_REPO)](https://github.com/YOUR_ORG/YOUR_REPO/releases)
[![CI Status](https://github.com/YOUR_ORG/YOUR_REPO/workflows/Lint,%20Schemas,%20and%20Adversarial%20Evals/badge.svg)](https://github.com/YOUR_ORG/YOUR_REPO/actions)
-->
[![SPDX License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

> **A security-grade prompt library treated like code: governed, testable, and auditable.**

VaultMesh TEM is a collection of parameterized cybersecurity AI prompts with enterprise-grade governance, safety controls, and automated validation. Each prompt behaves like an API with versioning, safety classifications, and adversarial testing.

## Repository Highlights

- **16 Production-Ready Prompts**: Reconnaissance, vulnerability analysis, incident response, red team emulation, and more
- **Safety Classifications**: `read-only`, `advisory`, and `lab-only` with corresponding guardrails
- **Automated Validation**: Schema validation and adversarial pattern detection in CI/CD
- **Governance Framework**: Security reporting, code ownership, and contribution workflows
- **Structured Catalog**: Machine-readable prompt index with inputs, outputs, and metadata

## Quick Start

### Using a Prompt

1. Browse the [prompt catalog](prompts/index.json) or [grimoire](prompts/Tem-Prompts.md)
2. Replace `{{placeholders}}` with your parameters
3. Ensure you have appropriate authorization for the prompt's safety class

```bash
# Example: Validate the catalog
npx --yes ajv-cli@5 validate -s prompts/index.schema.json -d prompts/index.json

# Run local adversarial checks
node .github/workflows/scripts/adversarial-evals.js
```

### Contributing a New Prompt

1. Add your prompt section to [`prompts/Tem-Prompts.md`](prompts/Tem-Prompts.md)
2. Register it in [`prompts/index.json`](prompts/index.json) with appropriate safety class
3. Update [`CHANGELOG.md`](CHANGELOG.md) with semver bump
4. Submit PR (automated checks will validate schema conformance and safety)

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for detailed workflow.

For a one-page overview, see the Executive Field Guide: [Guides/Executive Field Guide.md](Guides/Executive%20Field%20Guide.md). For the lore-rich Civilisation Ops Library scroll, visit [Guides/Civilisation Ops Library.md](Guides/Civilisation%20Ops%20Library.md).

## Repository Architecture

```text
.
├── prompts/
│   ├── Tem-Prompts.md           # Human-readable TEM prompt grimoire
│   ├── index.json               # Machine-readable catalog (16 prompts)
│   └── index.schema.json        # JSON schema for catalog validation
├── guardrails/
│   ├── README.md                # Policy framework (OWASP LLM, NIST SSDF)
│   └── patterns.json            # Configurable adversarial patterns
├── .github/
│   ├── workflows/
│   │   ├── evals.yml            # CI: lint → schema → ROE → coverage → adversarial
│   │   └── scripts/
│   │       └── adversarial-evals.js  # Automated safety scanning
│   ├── ISSUE_TEMPLATE/          # Bug, feature, security reporting
│   └── PULL_REQUEST_TEMPLATE.md # Review checklist
├── Templates/                   # Prompt, runbook, persona templates
├── Guides/                      # Documentation and workflow guides
└── governance files             # SECURITY.md, CODEOWNERS, etc.
```

## Operational Kits

- Tool Matrix Scroll — Open‑Source Listening & Forensic Kit: `tools/Tool-Matrix.md`
- Lawful Intercept Matrix — Who / What / Oversight: `tools/Lawful-Intercept-Matrix.md`

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/

- Ritual Cite — Auto-footnote engraver and Sources Ledger: [Scripts/ritual_cite.md](Scripts/ritual_cite.md) · Script: [Scripts/ritual_cite.py](Scripts/ritual_cite.py)

## Why Prompt Libraries Matter

A prompt library is a curated, structured collection of reusable prompts for AI systems. Organizing prompts by task, role, or output type creates durable institutional knowledge and keeps interactions predictable. Well-governed libraries consistently:

- Reduce redundant prompt authoring by recycling vetted instructions
- Maintain tone, structure, and safety expectations across teams
- Accelerate onboarding through documented, versioned exemplars
- Support experimentation without sacrificing policy compliance

Industry references (for example, the UF Business Library[^ufb] and AICamp 2025 analysis[^aicamp]) describe prompt libraries as centralized catalogs of tested prompts that teams can share across departments. Reported outcomes include double-digit productivity gains and faster adoption when organizations converge on a common library.


## Safety and Governance Model

### Safety Classifications

| Class | Description | Validation | Use Cases |
|-------|-------------|------------|-----------|
| `advisory`00 | Non-destructive analysis and recommendations | Strict pattern blocking | Risk assessment, log analysis, code review |
| `advisory`11 | Guidance with potential operational impact | Moderate restrictions | Incident response, vulnerability enumeration |
| `advisory`22 | Offensive/experimental content | Informational warnings only | Red team emulation, exploit research |

### Automated Safety Checks

- **Schema Validation**: Ensures catalog consistency and completeness
- **Adversarial Scanning**: Blocks weaponized patterns outside lab environments
- **Coverage Gate**: Validates 1:1 mapping between catalog and content
- **Security Reporting**: Private disclosure channel with SLA commitments

### Governance Framework

- **Human-in-the-Loop**: Required approvals for destructive actions
- **Audit Trail**: All prompts, actions, and justifications logged
- **Scope Validation**: Automated out-of-scope detection and escalation
- **Data Minimization**: PII redaction and least-privilege connectors

## Prompt Inventory

| ID | Title | Safety Class | Tags |
|----|-------|--------------|------|
| `advisory`33 | Reconnaissance Assistant | read-only | osint, dns, inventory |
| `advisory`44 | Vulnerability Enumerator | advisory | cve, misconfig, mitigation |
| `advisory`55 | Exploit Generator (PoC Sketch) | lab-only | exploit, poc, redteam |
| `advisory`66 | Incident Responder | advisory | triage, forensics, recovery |
| `advisory`77 | Log Analyzer | read-only | logs, anomalies, detection |
| `advisory`88 | Red-Team Emulation | lab-only | attack, ttp, simulation |
| `advisory`99 | Threat Intelligence Summarizer | read-only | intel, ioc, advisories |
| `lab-only`00 | Prompt Injection Tester | lab-only | jailbreak, guardrails |
| `lab-only`11 | AI Guardrail Checker | read-only | authz, policy, logging |
| `lab-only`22 | Code Security Reviewer | read-only | secrets, crypto, injection |
| `lab-only`33 | Social Engineering Strategist | advisory | awareness, training |
| `lab-only`44 | CTF Challenge Designer | read-only | ctf, walkthrough, hints |
| `lab-only`55 | Risk Assessment Calculator | read-only | risk, scoring, controls |
| `lab-only`66 | Tool Hints & OSINT Recipes | advisory | tools, osint, ethics |
| `lab-only`77 | Defensive Advisor | read-only | defense, hardening, compliance |
| `lab-only`88 | LLM Guardrails & Operational Controls | read-only | governance, policy, citations |

*Complete details in [`lab-only`99](prompts/index.json)*

## Development Workflow

### Local Development

```bash
# Clone and setup
git clone <repo-url>
cd vaultmesh-tem

# Validate changes locally
npm run lint                     # Markdown linting
npm run validate-schema          # JSON schema validation
npm run adversarial-check        # Safety pattern scanning
npm run test-coverage            # Catalog-content coverage

# Add new prompt
# 1. Edit prompts/Tem-Prompts.md
# 2. Update prompts/index.json
# 3. Update CHANGELOG.md
# 4. Run validation suite
```

## MCP Interfaces & Automation

VaultMesh TEM surfaces key operations through Model Context Protocol (MCP[^mcp]) interfaces so agent-centric clients can trigger validations and knowledge workflows safely.

- Run the stdio server with `python -m scripts.ops_mcp --stdio` to expose repo automations as MCP tools. Tool metadata lives in [`tools/index.json`](tools/index.json) under `mcp_tools`.
- Knowledge summons are available via [`scripts/mcp_knowledge_summon.py`](scripts/mcp_knowledge_summon.py), configurable with [`templates/mcp-summon.config.json`](templates/mcp-summon.config.json). See [`docs/mcp-knowledge-summon-blueprint.md`](docs/mcp-knowledge-summon-blueprint.md) for the full pattern.
- Agent surfaces (e.g., Claude Desktop, VS Code MCP clients) can initialize against the stdio endpoint to list tools such as `prompts.validate`, `knowledge.summon`, and `guardrails.validate` before invoking them with policy-aligned arguments.

[^mcp]: Model Context Protocol (MCP) — https://modelcontextprotocol.io/

### CI/CD Pipeline

1. **Lint Check**: Markdown formatting and style
2. **Schema Validation**: Catalog structure and completeness
3. **ROE Compliance**: Lab-only prompts require `{{placeholders}}`00
4. **Coverage Gate**: Ensures anchors in `{{placeholders}}`11 match `{{placeholders}}`22
5. **Adversarial Evaluation**: Safety pattern detection based on classification
6. **Artifact Generation**: Evaluation results for reviewer download

### Review Requirements

- [ ] Schema validates successfully
- [ ] Safety class appropriate for content
- [ ] Guardrails alignment verified
- [ ] CHANGELOG.md updated with semver
- [ ] No adversarial patterns outside lab-only class

## Security and Compliance

### Security Reporting

Report security vulnerabilities privately via:

- GitHub Security Advisory (preferred)
- Email: <security@placeholder.com>
- Response SLA: 48 hours acknowledgment, 7 days initial assessment

### Compliance Mappings

- **OWASP LLM Top 10**: Prompt injection, data leakage, model theft prevention
- **NIST SSDF**: Secure software development framework integration
- **ISO 27001**: Information security management alignment
- **SOC 2**: Trust services criteria for availability and security

See [`{{placeholders}}`33](guardrails/README.md) for detailed policy framework.

## Operator Access Best Practices

Keep your macOS operator `{{placeholders}}`44 opinionated so production credentials stay scoped and predictable. The fragment below sets safe defaults, establishes host entries, and documents the intent behind each toggle.

```sshconfig
# ---------- Shared defaults (safe Mac operator stance) ----------
Host 91.98.124.11
  HostName 91.98.124.11
  User root

Host *
  AddKeysToAgent yes
  UseKeychain yes   # macOS stores passphrases
  IgnoreUnknown UseKeychain,Include,ProxyJump
  IdentityFile ~/.ssh/vaultmesh_master   # primary operator key
  IdentitiesOnly yes # don't spray other keys
  ForwardAgent no    # default OFF (opt-in per host)
  ServerAliveInterval 30
  ServerAliveCountMax 3
  TCPKeepAlive yes
  HashKnownHosts yes
  PreferredAuthentications publickey
  CanonicalizeHostname yes
  ControlMaster auto
  ControlPersist 10m
  ControlPath ~/.ssh/cm-%C # short, portable

# ---------- Home / LAN nodes ----------
Host ai-node brain
  User vaultop
  StrictHostKeyChecking accept-new # TOFU, refuse changes later
  ForwardAgent no # keep off on LAN

Host ai-node
  HostName 192.168.0.42

Host brain
  HostName 192.168.0.40

# ---------- DEV node (Hetzner) ----------
Host forge
  HostName 91.98.83.252
  User vaultop
  IdentityFile ~/.ssh/vaultmesh_master
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
  ServerAliveInterval 30
  ServerAliveCountMax 3
  # If you use a bastion, uncomment:
  # ProxyJump bastion
  # ForwardAgent yes            # ONLY if the remote needs your agent

# ---------- PROD anchor (Hetzner) ----------
Host core-01
  HostName 91.98.124.11
  User vaultop
  IdentityFile ~/.ssh/vaultmesh_master
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
  ServerAliveInterval 30
  ServerAliveCountMax 3

# ---------- Tunnel for VaultMesh web access ----------
Host vm-funnel
  HostName 91.98.124.11
  User vaultop
  IdentityFile ~/.ssh/vaultmesh_master
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
  ServerAliveInterval 30
  ServerAliveCountMax 3
  ExitOnForwardFailure yes
  LocalForward 8800 localhost:3081
  LocalForward 8801 localhost:80

# ---------- Tunnel target (for autossh) ----------
Host dev-server-1
  HostName 91.98.83.252
  User vaultop
  IdentityFile ~/.ssh/vaultmesh_master
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new

# ---------- Bastion (optional, if you have one) ----------
# Host bastion
#   HostName bastion.vaultmesh.net
#   User vaultsovereign
#   IdentityFile ~/.ssh/vaultmesh_master
#   IdentitiesOnly yes
#   StrictHostKeyChecking accept-new
#   ForwardAgent yes           # narrowly enabled
```

## Contributing

We welcome contributions! Please see our:

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Prompt Template](Templates/Prompt Template.md)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **MITRE ATT&CK** framework for TTP classification
- **OWASP** for LLM security guidance
- **NIST** for cybersecurity frameworks
- **FIRST** for incident response standards

---

**Important**: All offensive prompts are for authorized educational and testing purposes only. Users are responsible for complying with applicable laws and obtaining authorization before use.


## Sources Ledger

| Domain | Citations |
|---|---|
| aicamp.ai | 1 |
| guides.uflib.ufl.edu | 1 |

---

### 📝 Footnotes

[^ufb]: *UF Business Library* → [https://guides.uflib.ufl.edu/AI/PromptLibraries](https://guides.uflib.ufl.edu/AI/PromptLibraries)
[^aicamp]: *AICamp 2025* → [https://www.aicamp.ai/event/eventdetails/W2025030311](https://www.aicamp.ai/event/eventdetails/W2025030311)

---

## 📚 Sources & References

| 🌐 **Domain** | 📖 **Citations** |
|:---|:---:|
| `aicamp.ai` | **1** |
| `guides.uflib.ufl.edu` | **1** |
*Total: **2** citations across **2** domains*

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/

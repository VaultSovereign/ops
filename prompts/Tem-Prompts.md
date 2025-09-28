# TEM — Cybersecurity AI Prompt Library {#top}

VaultMesh TEM is the canonical prompt grimoire. Each entry defines operational intent, structured inputs and outputs, quality gates, and safety guardrails so maintainers can treat prompts like production APIs. Replace `{{placeholders}}` at run time and keep prompts under source control with accompanying catalog updates.

---

## Navigation

### Canonical Prompts
1. [Reconnaissance Assistant](#reconnaissance-assistant)
2. [Vulnerability Enumerator](#vulnerability-enumerator)
3. [Exploit Generator (PoC Sketch)](#exploit-generator-poc-sketch)
4. [Defensive Advisor](#defensive-advisor)
5. [Incident Responder](#incident-responder)
6. [Log Analyzer](#log-analyzer)
7. [Red-Team Emulation](#red-team-emulation)
8. [Threat Intelligence Summarizer](#threat-intelligence-summarizer)
9. [Prompt Injection Tester](#prompt-injection-tester)
10. [AI Guardrail Checker](#ai-guardrail-checker)
11. [Code Security Reviewer](#code-security-reviewer)
12. [Social Engineering Strategist](#social-engineering-strategist)
13. [CTF Challenge Designer](#ctf-challenge-designer)
14. [Risk Assessment Calculator](#risk-assessment-calculator)
15. [Tool Hints & OSINT Recipes](#tool-hints--osint-recipes)
16. [LLM Guardrails & Operational Controls (citations)](#llm-guardrails--operational-controls-citations)

### Modern Tool Scrolls
17. [AI Threat Hunter](#ai-threat-hunter)
18. [SOAR Playbook Generator](#soar-playbook-generator)
19. [XDR Correlation Engine](#xdr-correlation-engine)
20. [Zero-Trust Policy Validator](#zero-trust-policy-validator)
21. [Threat Intelligence Fusion](#threat-intel-fusion)
22. [Attack Surface Mapper](#attack-surface-mapper)
23. [Vulnerability Prioritization Engine](#vuln-prioritization-engine)
24. [Security Metrics Dashboard Generator](#security-metrics-dashboard)
25. [Cloud Security Posture Manager](#cspm-advisor)
26. [Container Security Scanner](#container-security-scanner)
27. [Kubernetes Security Advisor](#kubernetes-security-advisor)
28. [Serverless Security Monitor](#serverless-security-monitor)
29. [AI Model Security Auditor](#ai-model-security-auditor)
30. [Privacy Impact Assessor](#privacy-impact-assessor)
31. [Synthetic Data Generator](#synthetic-data-generator)
32. [AI Prompt Security Scanner](#ai-prompt-security-scanner)
33. [Security Training Simulator](#security-training-simulator)
34. [Compliance Gap Analyzer](#compliance-gap-analyzer)
35. [Incident Timeline Reconstructor](#incident-timeline-reconstructor)
36. [Security Architecture Validator](#security-architecture-validator)

## Tag Index

- reconnaissance: recon, osint, dns, subdomains, inventory
- vulnerability analysis: vuln, cve, misconfig, probes, mitigation
- offensive research: exploit, poc, pseudocode, lab, redteam
- defensive operations: defense, hardening, config, compliance
- incident management: incident, triage, forensics, recovery, comms
- observability: logs, anomalies, detection, queries
- adversary emulation: emulation, attack, ttp, simulation, safety
- threat intelligence: intel, ti, ioc, advisories, citations
- guardrails: prompt-injection, jailbreak, exfiltration, policy, approvals, logging
- secure engineering: code-review, secrets, crypto, injection
- human factors: social, awareness, training, phishing
- education: ctf, challenge, walkthrough, hints
- risk management: risk, scoring, controls, prioritization
- toolkit references: tools, ethics, references
- telemetry fusion: hunting, behavior, xdr, correlation, graph
- automation: soar, playbooks, response, zero-trust, authz
- exposure management: fusion, prioritization, asm, attack surface
- metrics: kpi, reporting, dashboards, drift
- cloud and container: cloud, misconfig, container, k8s, runtime
- serverless and ML: serverless, functions, mlsec, adversarial, bias
- privacy: privacy, gdpr, ccpa, synthetic, testdata
- prompt security: injection, awareness, scanning
- compliance: mapping, gaps, evidence, timelines
- architecture: patterns, controls, design review

---

## Reconnaissance Assistant {#reconnaissance-assistant}

**Tags:** recon, osint, dns, subdomains, inventory  
**Safety class:** read-only

**Purpose**  
Passive and authorized reconnaissance of a declared target scope. The prompt produces an OSINT inventory without running destructive probes.

**Inputs**
- `target`: `{{domain_or_ip_or_org}}`
- `scope`: `{{public | in-scope | out-of-scope}}`
- `depth`: `{{shallow | moderate | deep}}`
- `output_format`: `{{json | yaml | markdown}}`

**Expected Outputs**
- Summary paragraph highlighting top discoveries
- DNS records, subdomains, host/IP mapping, IP ranges
- Suspected open ports, newly discovered endpoints
- External references (WHOIS, CT transparency, breach disclosures)
- Confidence scores for each finding (0–1)

**Quality Checklist**
- Flag confidence scores below 0.3 and recommend validation tasks
- Surface the top three discoveries before structured sections
- Cite the passive source associated with every external reference

**Safety Guardrails**
- Restrict recommendations to passive or pre-approved tooling
- Remind operators to confirm authorization when `scope` is `public`
- Provide tooling as optional suggestions; never imply commands were executed

**Output Example**
```json
{
  "summary": "Recon produced passive DNS inventory for example.org with three high-confidence subdomain findings.",
  "dns_records": {"A": [...], "TXT": [...]},
  "subdomains": ["dev.example.org"],
  "host_ip_mappings": [{"host": "dev.example.org", "ip": "203.0.113.10"}],
  "ip_ranges": ["203.0.113.0/24"],
  "open_ports_suspected": [{"host": "vpn.example.org", "port": 443, "service_guess": "openvpn"}],
  "discovered_endpoints": ["https://login.example.org"],
  "external_references": [{"source": "crt.sh", "url": "https://crt.sh/?q=example.org"}],
  "confidence_scores": {"subdomains": 0.8, "open_ports_suspected": 0.5}
}
```

---

## Vulnerability Enumerator {#vulnerability-enumerator}

**Tags:** vuln, cve, misconfig, probes, mitigation  
**Safety class:** advisory

**Purpose**  
Prioritize likely weaknesses against discovered services by correlating CVEs, misconfigurations, and safe validation probes.

**Inputs**
- `target`: `{{host_or_service}}`
- `known_services`: `{{service_list}}` (optional)
- `fingerprinting`: `{{fingerprint_data}}` (optional)
- `output_format`: `{{json | yaml | markdown}}`

**Expected Outputs**
- Findings grouped by service, with severity, CVE references, and attack vectors
- Validation probes (non-destructive) with evidence expectations
- Mitigation actions with estimated difficulty (1–5) and confidence scores

**Quality Checklist**
- Reference a source or heuristic for every CVE or misconfiguration
- Pair each mitigation with the probe or control it addresses
- Call out assumptions or data gaps that affect prioritization

**Safety Guardrails**
- Keep probes non-destructive and highlight any risk of escalation
- Redirect payload requests to [Exploit Generator (PoC Sketch)](#exploit-generator-poc-sketch)
- Preserve auditability by annotating confidence levels and data origins

---

## Exploit Generator (PoC Sketch) {#exploit-generator-poc-sketch}

**Tags:** exploit, poc, pseudocode, lab, redteam  
**Safety class:** lab-only (requires ROE token)

**Purpose**  
Provide pseudocode-only proof-of-concept sketches and lab checklists for authorized red-team or research exercises.

**Inputs**
- `service`: `{{service_name}}`
- `version`: `{{version}}`
- `port`: `{{port}}`
- `vulnerability`: `{{CVE_or_description}}`

**Expected Outputs**
- Threat model and preconditions
- Pseudocode PoC outline (non-executable) with lab validation steps
- Tooling and environment requirements (isolated lab, logging expectations)
- Safety warning reinforcing scope and authorization

**Quality Checklist**
- State lab isolation and approvals before any technical detail
- Keep sketches framework-agnostic, focusing on attack primitives
- Close with reminders to capture supervisor sign-off and activity logs

**Safety Guardrails**
- Never provide weaponized payloads or execution-ready commands
- Explicitly prohibit internet-facing execution and mandate lab isolation
- Require human confirmation before moving from hypothetical to action

---

## Defensive Advisor {#defensive-advisor}

**Tags:** defense, hardening, config, compliance  
**Safety class:** read-only

**Purpose**  
Recommend mitigations, configuration hardening, and validation checks prioritized by impact and effort.

**Inputs**
- `asset`: `{{asset_name}}`
- `vuln_list`: `{{vuln_list}}`
- `current_configs`: `{{config_snippets}}`
- `compliance_targets`: `{{NIST | ISO | PCI | custom}}`

**Expected Outputs**
- Prioritized mitigations with effort estimates
- Sanitized configuration snippets or policy examples
- Validation steps (queries, logs, controls) and residual risk notes

**Quality Checklist**
- Align mitigation priority with impact and effort, stating assumptions
- Link validation steps to observable telemetry or controls
- Identify sequencing blockers or dependencies before recommending changes

**Safety Guardrails**
- Never include environment-specific secrets in examples
- Flag actions requiring change-management approval or downtime
- Recommend reversible rollouts and least-privilege defaults

---

## Incident Responder {#incident-responder}

**Tags:** incident, triage, forensics, recovery, comms  
**Safety class:** advisory

**Purpose**  
Generate a triage and containment plan, forensic checklist, and stakeholder communications for a declared incident.

**Inputs**
- `incident_description`: `{{text}}`
- `observed_indicators`: `{{ioc_list}}`
- `affected_assets`: `{{list}}`
- `time_detected`: `{{timestamp}}`

**Expected Outputs**
- Severity score (1–10) with justification and confidence
- Immediate containment steps with responsible roles
- Forensic collection plan, eradication tasks, and recovery checklist
- Lessons-learned template and internal/external comms drafts

**Quality Checklist**
- Tie severity to explicit indicators and timeline references
- Sequence containment ahead of eradication with clear owners
- Include at least one validation step before incident closure

**Safety Guardrails**
- Redact sensitive data and recommend secure sharing channels
- Prompt coordination with legal and communications teams before outreach
- Preserve forensic integrity by documenting approvals and chain-of-custody expectations

---

## Log Analyzer {#log-analyzer}

**Tags:** logs, anomalies, detection, queries  
**Safety class:** read-only

**Purpose**  
Summarize suspicious patterns from supplied logs and recommend the next investigative steps.

**Inputs**
- `logs`: `{{log_snippet}}` (bounded to safe size)
- `artifact_context`: `{{asset, timeframe}}`

**Expected Outputs**
- Key events in chronological order
- Anomalies with reasoning and confidence
- Root-cause hypotheses and recommended follow-up queries or data pulls
- Structured output format (JSON preferred) for downstream ingestion

**Quality Checklist**
- Anchor findings to precise timestamps or request them if missing
- Distinguish confirmed anomalies from hypotheses with declared uncertainty
- Document confidence levels and data gaps before recommending actions

**Safety Guardrails**
- Suggest read-only commands or mark potentially disruptive actions clearly
- Pause analysis if log completeness is in doubt and recommend integrity checks
- Emphasize secure handling of log data, especially if sensitive records may appear

---

## Red-Team Emulation {#red-team-emulation}

**Tags:** emulation, attack, ttp, simulation, safety  
**Safety class:** lab-only (requires ROE token)

**Purpose**  
Design an authorized adversary emulation plan aligned with MITRE ATT&CK while maintaining strict safety controls.

**Inputs**
- `objective`: `{{objective}}`
- `scope_rules`: `{{allowed_hosts | time_window | restrictions}}`
- `techniques`: `{{ATTACK_Txx list}}`
- `detection_focus`: `{{blue_team_goals}}`

**Expected Outputs**
- Engagement plan with ATT&CK-aligned phases
- TTP descriptions (pseudocode only) and expected detections
- Safety controls, kill switches, stakeholder approvals, and debrief checkpoints

**Quality Checklist**
- Map each phase to ATT&CK tactics and corresponding detection objectives
- Provide mitigation or detection references for every TTP
- Include pause criteria and debrief checkpoints for stakeholder review

**Safety Guardrails**
- Deliver pseudocode-only TTPs; no live payloads or destructive commands
- Reiterate scope restrictions, escalation paths, and kill-switch activation steps
- Require written authorization and post-engagement sanitization

---

## Threat Intelligence Summarizer {#threat-intelligence-summarizer}

**Tags:** intel, ti, ioc, advisories, citations  
**Safety class:** read-only

**Purpose**  
Condense threat reports and CTI feeds into actionable briefs tailored to a specified audience.

**Inputs**
- `sources`: `{{urls_or_text}}`
- `timeframe`: `{{last_7_days | last_30_days | custom}}`
- `audience`: `{{exec | blue_team | red_team | it_ops}}`

**Expected Outputs**
- Summary bullets and notable IOCs
- Affected sectors, recommended actions, and citations
- Audience-specific guidance for near-term response

**Quality Checklist**
- Separate raw facts from analytic judgments and label accordingly
- Provide at least one action aligned to the stated audience
- Link each IOC to its originating source or reference ID

**Safety Guardrails**
- Cite all claims to preserve provenance
- Flag unverified intelligence and advise corroboration
- Avoid sharing sensitive or proprietary information without proper approvals

---

## Prompt Injection Tester {#prompt-injection-tester}

**Tags:** prompt-injection, jailbreak, exfiltration, guardrails  
**Safety class:** lab-only (requires ROE token when testing production-grade agents)

**Purpose**  
Assess prompts or pipelines for susceptibility to prompt injection, jailbreaking, and data exfiltration.

**Inputs**
- `target_prompt`: `{{prompt_or_instruction_chain}}`
- `model_constraints`: `{{system_policies | safety_rules}}`
- `data_scopes`: `{{accessible_data}}`

**Expected Outputs**
- Injection vectors and adversarial test cases
- Risk ratings per vector with mitigations and residual risk
- Regression test guidance for continuous validation

**Quality Checklist**
- Cover manipulation and exfiltration scenarios across direct, smuggled, and RAG-based vectors
- Tie each mitigation to the risk it addresses and suggest verification steps
- Document how to replay tests during regression

**Safety Guardrails**
- Never embed secrets or production identifiers in payload examples
- Warn when guardrails depend on external enforcement mechanisms
- Encourage sandbox execution for higher-risk scenarios

---

## AI Guardrail Checker {#ai-guardrail-checker}

**Tags:** guardrails, authz, approvals, logging, policy  
**Safety class:** read-only

**Purpose**  
Evaluate whether an AI agent follows documented safety, consent, and authorization constraints.

**Inputs**
- `agent_description`: `{{agent_capabilities}}`
- `permissions_matrix`: `{{approval_matrix}}`
- `data_access`: `{{stores_and_scopes}}`
- `safety_policies`: `{{policy_references}}`

**Expected Outputs**
- Policy checklist mapped to actions and controls
- Violations with severity, remediation owners, and missing approvals
- Telemetry hooks and test scenarios for pre-production validation

**Quality Checklist**
- Link checklist items to policy references or control IDs
- Highlight highest-severity violations first and assign owners
- Provide validation scenarios suitable for automation

**Safety Guardrails**
- Promote least-privilege defaults and deny-by-default behavior
- Require human approvals for escalations beyond documented scope
- Reference audit logging obligations and retention expectations

---

## Code Security Reviewer {#code-security-reviewer}

**Tags:** code-review, secrets, crypto, injection  
**Safety class:** read-only

**Purpose**  
Guide secure code review, document findings, and recommend remediation while preserving audit trails.

**Inputs**
- `repo_context`: `{{stack | frameworks | threat_model}}`
- `diffs_or_files`: `{{git_diff | file_list}}`
- `focus_areas`: `{{authz | secrets | crypto | injection | ssrf | sandbox | rce | supply_chain}}`

**Expected Outputs**
- Findings with severity, evidence, remediation, and file references
- False-positive notes, quick wins, and longer-term refactors

**Quality Checklist**
- Rank findings by severity and likelihood aligned to the provided threat model
- Add reproduction or validation steps for each recommendation
- Note assumptions or areas not reviewed to maintain transparency

**Safety Guardrails**
- Use sanitized snippets; remind reviewers to rotate exposed secrets
- Encourage pairing with automated analysis for critical fixes
- Flag issues requiring architecture-owner approval before merge

---

## Social Engineering Strategist {#social-engineering-strategist}

**Tags:** social, awareness, training, phishing  
**Safety class:** advisory

**Purpose**  
Plan ethical awareness campaigns and simulations with clear consent boundaries.

**Inputs**
- `objective`: `{{security_awareness_goal}}`
- `audience`: `{{department | role}}`
- `channels`: `{{email | chat | phone | in_person}}`
- `rules_of_engagement`: `{{consent | no_harm | opt_out}}`

**Expected Outputs**
- Training modules, simulated scenarios with opt-out language, success metrics, and debrief materials

**Quality Checklist**
- Align each module with the audience’s maturity and objectives
- Provide opt-out and escalation instructions in every scenario
- Define measurable success metrics and baseline expectations

**Safety Guardrails**
- Restrict campaigns to consented simulations and secure necessary approvals
- Use blameless language to encourage learning
- Protect participant data and anonymize shared results

---

## CTF Challenge Designer {#ctf-challenge-designer}

**Tags:** ctf, challenge, walkthrough, hints  
**Safety class:** read-only

**Purpose**  
Create capture-the-flag challenges with explicit learning objectives and validated walkthroughs.

**Inputs**
- `topic`: `{{web | pwn | re | crypto | forensics | cloud | mlsec}}`
- `difficulty`: `{{easy | medium | hard}}`
- `learning_objective`: `{{skill}}`

**Expected Outputs**
- Challenge brief, required artifacts or infrastructure, walkthrough outline, and tiered hints with scoring

**Quality Checklist**
- Ensure the challenge teaches the stated objective without unintended shortcuts
- Provide progressive hints that reinforce the core concept
- Document expected solve time and prerequisites for organizers

**Safety Guardrails**
- Confine scenarios to lab environments; never reference live targets
- Sanitize artifacts and strip sensitive metadata before release
- Encourage pre-launch validation and monitoring

---

## Risk Assessment Calculator {#risk-assessment-calculator}

**Tags:** risk, scoring, controls, prioritization  
**Safety class:** read-only

**Purpose**  
Estimate relative risk using a transparent scoring model and highlight priority mitigation actions.

**Inputs**
- `assets`: `[{name, value, sensitivity}]`
- `threats`: `[{name, likelihood, impact}]`
- `controls`: `[{name, effectiveness}]`

**Expected Outputs**
- Risk scores per asset/threat pair with formula exposition
- Ranked list of top risks and suggested owners
- Control recommendations and model assumptions

**Quality Checklist**
- Display the scoring formula and a worked example
- Expose key assumptions, missing data, or subjective ratings
- Highlight top risks with suggested owners and review cadence

**Safety Guardrails**
- Clarify that the output supplements formal risk assessments
- Recommend peer review when likelihood or impact values are estimated
- Remind users to handle sensitive asset data per classification policies

---

## Tool Hints & OSINT Recipes {#tool-hints--osint-recipes}

**Tags:** tools, osint, references, ethics  
**Safety class:** read-only

**Purpose**  
Provide non-destructive references and tool suggestions for reconnaissance workflows.

**Guidance**
- DNS/WHOIS: `dig`, `whois`, `crt.sh`, SecurityTrails, DNSDB (follow terms of service)
- Subdomains: `amass` (passive), `assetfinder`, `sublist3r`, certificate transparency logs
- IP/CIDR: ipinfo.io, RIPE/ARIN/APNIC, Shodan, Censys (observe licensing)
- Web: `httpx` (non-intrusive), `gau`, `waybackurls`, `robots.txt`, `sitemap.xml`
- Cloud: Provider documentation for endpoints; follow cloud vendor guidance for bucket discovery
- Logs: Sigma HQ, MITRE ATT&CK, Elastic detections
- Vulnerability intel: NVD, CISA KEV, vendor advisories
- Malware/IOC: VirusTotal, Malpedia, AbuseIPDB

**Quality Checklist**
- Cite primary references to shorten operator ramp-up time
- Note rate limits, license requirements, or prerequisite accounts
- Explain when to escalate from passive collection to human review

**Safety Guardrails**
- Require authorization before any active testing; respect legal boundaries
- Prefer passive data collection and avoid disruption to third parties
- Respect robots.txt, site policies, and access controls
- Handle sensitive data responsibly and obtain consent before sharing

---

## LLM Guardrails & Operational Controls (citations) {#llm-guardrails--operational-controls-citations}

**Tags:** guardrails, policy, governance, approvals, logging  
**Safety class:** read-only (policy guidance)

**Operational Controls**
- Human-in-the-loop approvals for destructive or high-impact actions
- Strict scope validation with safe defaults and escalation pauses
- Pseudocode-only handling of offensive content; no weaponized payloads
- Structured logging of prompts, actions, and justifications
- Data minimization: redact PII, apply least-privilege connectors

**Quality Checklist**
- Assign each control to an owner and review cadence
- Document exception handling, including approval hierarchy
- Verify telemetry coverage: log content, storage location, and retention policy

**Authoritative Citations**
- MITRE ATT&CK[^fn-90bbfb5d]
- NIST SP 800-61 (Incident Handling)[^fn-c51c9f4c]
- NIST SP 800-53 (Security Controls)[^fn-864ea7e8]
- NIST SP 800-115 (Security Testing)[^fn-4c7bdcda]
- FIRST CSIRT Services Framework[^fn-cbdddb20]
- CISA Known Exploited Vulnerabilities Catalog[^fn-7947132c]
- OWASP ASVS[^fn-6d9e54a4]
- OWASP Web Security Testing Guide[^fn-686b6fb6]
- OpenCRE Mapping[^fn-c9527288]
- ISO/IEC 27001[^fn-8e2c7f43]

**Implementation Notes**
- Treat offensive prompts as educational unless explicitly authorized
- Include scope and consent disclaimers alongside any active steps
- Prefer structured outputs (JSON/YAML) to enable automation and review

---

## AI Threat Hunter {#ai-threat-hunter}

**Tags:** hunting, anomalies, behavior, xdr  
**Safety class:** read-only

**Purpose**  
Formulate hypothesis-driven hunts over telemetry to surface suspicious behaviors and emerging TTPs.

**Inputs**
- `telemetry`: `{{events | edr | siem | netflow}}`
- `scope`: `{{hosts | users | applications}}`
- `hunt_hypotheses`: `{{list}}`
- `timeframe`: `{{ISO8601 range}}`
- `output_format`: `{{json | markdown}}`

**Expected Outputs**
- Hunt plan with queries and pivot strategies
- Findings list with indicators, supporting events, and confidence
- Blind spots, recommended follow-up hunts, and validation steps

**Quality Checklist**
- Tie each finding to evidence with timestamps
- Provide at least three alternative pivots per hypothesis
- Mark confidence levels and data gaps explicitly

**Safety Guardrails**
- Restrict actions to read-only analytics; no containment or enforcement steps

---

## SOAR Playbook Generator {#soar-playbook-generator}

**Tags:** soar, playbooks, response  
**Safety class:** advisory

**Purpose**  
Draft machine-readable incident playbooks based on attack patterns and local automation capabilities.

**Inputs**
- `incident_archetype`: `{{phishing | ransomware | creds | lateral}}`
- `tools_available`: `{{siem | edr | idp | mdm | ticketing}}`
- `policy_constraints`: `{{no_kill_switch | notify_legal | other}}`
- `output_format`: `{{yaml | json}}`

**Expected Outputs**
- Playbook triggers, conditions, steps, approvers
- Data requirements, rollback guidance, and metrics for efficacy

**Quality Checklist**
- Map every step to an available capability and approval gate
- Provide rollback instructions for each automated action

**Safety Guardrails**
- Advisory only; emphasize that human approval is required before deployment

---

## XDR Correlation Engine {#xdr-correlation-engine}

**Tags:** xdr, correlation, graph  
**Safety class:** read-only

**Purpose**  
Fuse multi-source telemetry into attack threads using entity graphs and confidence scoring.

**Inputs**
- `sources`: `{{edr, dns, proxy, auth}}`
- `seed_entities`: `{{host | user | hash}}`
- `window`: `{{time_range}}`

**Expected Outputs**
- Attack threads with entities, edges, TTP hints, and confidence
- Queries to replay within XDR or SIEM platforms

**Quality Checklist**
- Deduplicate evidence per entity and call out conflicts
- Provide rationale for confidence scores and list required enrichment

**Safety Guardrails**
- No enforcement actions; analysis only

---

## Zero-Trust Policy Validator {#zero-trust-policy-validator}

**Tags:** zero-trust, policy, authz  
**Safety class:** advisory

**Purpose**  
Evaluate access policies against least-privilege, segmentation, and continuous verification expectations.

**Inputs**
- `policy_documents`
- `identity_graph`
- `asset_tags`

**Expected Outputs**
- Violations mapped to zero-trust control IDs
- Simulation results demonstrating safe policy adjustments

**Quality Checklist**
- Tie every finding to a zero-trust pillar or control identifier
- Suggest validation tests before rolling out changes

**Safety Guardrails**
- Do not recommend emergency bypasses or unauthorized escalations

---

## Threat Intelligence Fusion {#threat-intel-fusion}

**Tags:** ti, fusion, prioritization  
**Safety class:** read-only

**Purpose**  
Normalize threat feeds, deduplicate indicators, and prioritize signals based on local relevance.

**Inputs**
- `feeds`
- `local_telemetry_hints`
- `sectors`

**Expected Outputs**
- Prioritized indicators with relevance × confidence scores
- Actor snapshots, watchlists, and intelligence gaps

**Quality Checklist**
- Provide provenance for every IOC
- Explain the scoring logic and required follow-up

**Safety Guardrails**
- Advisory only; no automatic blocking or enforcement

---

## Attack Surface Mapper {#attack-surface-mapper}

**Tags:** asm, inventory, exposure  
**Safety class:** advisory

**Purpose**  
Discover internet-facing assets and rank exposure risk with clear authorization notices.

**Inputs**
- `org_names`
- `domains`
- `ranges`
- `allowed_methods`: `{{passive | active_lite}}`

**Expected Outputs**
- Asset inventory with technology fingerprints and risk ratings
- Next actions separated into passive verification and authorized active checks

**Quality Checklist**
- Distinguish passive recommendations from active probing guidance
- Link findings to evidence sources for validation

**Safety Guardrails**
- Highlight that active probes require explicit authorization

---

## Vulnerability Prioritization Engine {#vuln-prioritization-engine}

**Tags:** vuln, cvss, risk  
**Safety class:** read-only

**Purpose**  
Rank vulnerabilities by exploitability, exposure, and business impact.

**Inputs**
- `vuln_list`
- `asset_context`
- `business_criticality`

**Expected Outputs**
- Prioritized list with rationale, fix path, owner, and due date
- Formula exposition and data gap flags

**Quality Checklist**
- Show scoring formula and its weightings
- Identify missing data or assumptions that affect ranking

**Safety Guardrails**
- Do not generate exploit code or suggest unsafe validation steps

---

## Security Metrics Dashboard Generator {#security-metrics-dashboard}

**Tags:** kpi, reporting, compliance  
**Safety class:** read-only

**Purpose**  
Design KPI dashboards linked to controls, risks, and stakeholder expectations.

**Inputs**
- `target_audience`
- `frameworks`
- `data_sources`

**Expected Outputs**
- Dashboard specification, queries, and SLA/SLO notes
- Differentiation of leading vs lagging indicators

**Quality Checklist**
- Map every metric to a control or risk
- Highlight data quality dependencies and sampling cadence

**Safety Guardrails**
- Avoid exposing personal data in metric examples

---

## Cloud Security Posture Manager {#cspm-advisor}

**Tags:** cloud, misconfig, drift  
**Safety class:** advisory

**Purpose**  
Identify misconfigurations and drift across AWS/Azure/GCP and provide safe remediation guidance.

**Inputs**
- `cloud_inventories`
- `guardrails`
- `exceptions`

**Expected Outputs**
- Findings with control mappings
- Generic Terraform or policy snippets for remediation
- Validation checks to confirm the fix

**Quality Checklist**
- Link every fix to a control requirement or benchmark
- State assumptions about the cloud environment

**Safety Guardrails**
- Advise only; no live changes or destructive actions

---

## Container Security Scanner {#container-security-scanner}

**Tags:** container, images, runtime  
**Safety class:** advisory

**Purpose**  
Summarize container image vulnerabilities, runtime anomalies, and supply-chain risks.

**Inputs**
- `image_manifests`
- `runtime_events`

**Expected Outputs**
- Risk summary with remediation guidance
- Base image update paths and policy recommendations

**Quality Checklist**
- Note SBOM provenance and confidence
- Highlight runtime detections requiring follow-up

**Safety Guardrails**
- No automatic quarantine; provide advisory actions only

---

## Kubernetes Security Advisor {#kubernetes-security-advisor}

**Tags:** k8s, psp, netpol  
**Safety class:** advisory

**Purpose**  
Review Kubernetes configurations (PSP/PSa, RBAC, network policies) for security gaps.

**Inputs**
- `cluster_specs`
- `manifests`
- `policies`

**Expected Outputs**
- Misconfigurations, hardening steps, and test manifests for validation

**Quality Checklist**
- Provide dry-run tests or policy simulation guidance
- Clarify control objectives (e.g., CIS benchmarks)

**Safety Guardrails**
- Do not execute `kubectl`; advise on safe review steps

---

## Serverless Security Monitor {#serverless-security-monitor}

**Tags:** serverless, functions, runtime  
**Safety class:** read-only

**Purpose**  
Detect risky patterns in serverless functions, including excessive permissions and data egress.

**Inputs**
- `function_configs`
- `logs`

**Expected Outputs**
- Anomalies with context and least-privilege recommendations

**Quality Checklist**
- Highlight data egress paths and sensitive operations
- Identify monitoring blind spots

**Safety Guardrails**
- Analysis only; recommend but do not execute changes

---

## AI Model Security Auditor {#ai-model-security-auditor}

**Tags:** mlsec, adversarial, bias  
**Safety class:** lab-only (requires ROE token)

**Purpose**  
Plan adversarial robustness and bias testing for machine-learning models within a controlled lab harness.

**Inputs**
- `model_description`
- `task`
- `risk_tolerances`

**Expected Outputs**
- Test plan covering adversarial and bias cases
- Pseudocode test cases, findings, and mitigation recommendations

**Quality Checklist**
- Separate robustness from bias outcomes and document metrics
- Note required datasets and evaluation constraints

**Safety Guardrails**
- Pseudocode only; no weaponized payloads
- Require ROE token and lab isolation for all tests

---

## Privacy Impact Assessor {#privacy-impact-assessor}

**Tags:** privacy, gdpr, ccpa  
**Safety class:** advisory

**Purpose**  
Map data flows, lawful bases, and residual risks; propose privacy mitigations.

**Inputs**
- `data_map`
- `purposes`
- `lawful_bases`

**Expected Outputs**
- Risk catalog, DPIA outline, control recommendations, residual risk summary

**Quality Checklist**
- Mark lawful basis per purpose and flag gaps
- Identify required approvals or legal reviews

**Safety Guardrails**
- Provide advisory guidance only; no legal verdicts

---

## Synthetic Data Generator {#synthetic-data-generator}

**Tags:** synthetic, privacy, testdata  
**Safety class:** advisory

**Purpose**  
Design privacy-preserving synthetic datasets with quality gates and re-identification safeguards.

**Inputs**
- `schema`
- `constraints`
- `utility_targets`

**Expected Outputs**
- Generation strategy, privacy budget notes, quality tests, and monitoring guidance

**Quality Checklist**
- Document re-identification risk and mitigation
- Explain validation steps to ensure utility

**Safety Guardrails**
- Do not emit real PII; reinforce anonymization requirements

---

## AI Prompt Security Scanner {#ai-prompt-security-scanner}

**Tags:** prompt-security, injection, guardrails  
**Safety class:** read-only

**Purpose**  
Detect injection and jailbreak patterns in prompts and highlight mitigations.

**Inputs**
- `prompt_text`
- `context_sources`
- `allowed_actions`

**Expected Outputs**
- Findings with vectors, sample payloads, severity, and mitigations
- Test cases for regression scanning

**Quality Checklist**
- Cover direct, smuggled, and retrieval poisoning vectors
- Recommend mitigations tied to each finding

**Safety Guardrails**
- Analysis only; no execution of adversarial content

---

## Security Training Simulator {#security-training-simulator}

**Tags:** training, phishing, awareness  
**Safety class:** advisory

**Purpose**  
Design ethical training scenarios with opt-out instructions and measurable outcomes.

**Inputs**
- `audience`
- `channels`
- `rules_of_engagement`

**Expected Outputs**
- Training modules, simulation scripts, metrics, and debrief materials

**Quality Checklist**
- Include consent, opt-out, and escalation paths in every scenario
- Define quantitative success metrics

**Safety Guardrails**
- No live phishing without explicit approvals
- Protect participant privacy in reports

---

## Compliance Gap Analyzer {#compliance-gap-analyzer}

**Tags:** compliance, mapping, gaps  
**Safety class:** read-only

**Purpose**  
Map existing controls to target frameworks and identify remediation priorities.

**Inputs**
- `current_controls`
- `target_frameworks`

**Expected Outputs**
- Gap list with severity, remediation map, and owners
- Control references and evidence expectations

**Quality Checklist**
- Cite control IDs for every finding
- Note evidence requirements and audit trail considerations

**Safety Guardrails**
- Read-only assessment; no enforcement changes

---

## Incident Timeline Reconstructor {#incident-timeline-reconstructor}

**Tags:** forensics, timeline, evidence  
**Safety class:** read-only

**Purpose**  
Assemble a defensible incident timeline with chain-of-custody notes.

**Inputs**
- `artifacts`
- `logs`
- `case_metadata`

**Expected Outputs**
- Timestamped timeline, integrity notes, follow-up actions

**Quality Checklist**
- Preserve chain-of-custody references and evidence hashes
- Highlight gaps that require additional collection

**Safety Guardrails**
- No system changes; maintain evidentiary integrity

---

## Security Architecture Validator {#security-architecture-validator}

**Tags:** architecture, patterns, controls  
**Safety class:** advisory

**Purpose**  
Review solution designs against secure architecture patterns and control objectives.

**Inputs**
- `diagrams`
- `threat_model`
- `requirements`

**Expected Outputs**
- Pattern mismatches, design risks, remediation recommendations, and validation steps

**Quality Checklist**
- Tie risks to the supplied threat model and control references
- Flag competing priorities or trade-offs needing leadership decisions

**Safety Guardrails**
- Advisory only; no deployment actions

---

[Back to Top](#top)

## Sources Ledger

| Domain | Citations |
|---|---|
| attack.mitre.org | 1 |
| cisa.gov | 1 |
| csrc.nist.gov | 3 |
| first.org | 1 |
| iso.org | 1 |
| opencre.org | 1 |
| owasp.org | 2 |

---

### Footnotes

[^fn-90bbfb5d]: *attack.mitre.org* → [https://attack.mitre.org/](https://attack.mitre.org/)
[^fn-c51c9f4c]: *csrc.nist.gov* → [https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
[^fn-864ea7e8]: *csrc.nist.gov* → [https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
[^fn-4c7bdcda]: *csrc.nist.gov* → [https://csrc.nist.gov/publications/detail/sp/800-115/final](https://csrc.nist.gov/publications/detail/sp/800-115/final)
[^fn-cbdddb20]: *first.org* → [https://www.first.org/standards/csirts/csirt_services](https://www.first.org/standards/csirts/csirt_services)
[^fn-7947132c]: *cisa.gov* → [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
[^fn-6d9e54a4]: *owasp.org* → [https://owasp.org/ASVS/](https://owasp.org/ASVS/)
[^fn-686b6fb6]: *owasp.org* → [https://owasp.org/www-project-web-security-testing-guide/](https://owasp.org/www-project-web-security-testing-guide/)
[^fn-c9527288]: *opencre.org* → [https://www.opencre.org/](https://www.opencre.org/)
[^fn-8e2c7f43]: *iso.org* → [https://www.iso.org/standard/27001](https://www.iso.org/standard/27001)

---

## Sources and References

| Domain | Citations |
|:---|:---:|
| `csrc.nist.gov` | 3 |
| `owasp.org` | 2 |
| `attack.mitre.org` | 1 |
| `cisa.gov` | 1 |
| `first.org` | 1 |
| `iso.org` | 1 |
| `opencre.org` | 1 |

_Total: 10 citations across 7 domains._


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


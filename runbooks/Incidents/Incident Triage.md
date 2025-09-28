---
title: Incident Triage
created: 2024-03-01
updated: {{date:YYYY-MM-DD}}
tags: [runbook, incident]
service: cross-team
owner: incident commander
impact: high
---

# Summary
First-hour sequence for responding to a high-impact incident.

# Preconditions
- Incident commander on-call rotation in place.
- Communications channels (Slack, Zoom, Status Page) ready.

# Trigger
Triggered when PagerDuty raises a SEV-1 or SEV-2 alert or customer-facing outage is reported.

# Steps
1. Acknowledge the alert and claim IC role.
2. Spin up incident channel and invite functional leads.
3. Assign roles: operations, communications, subject-matter experts.
4. Collect initial impact summary within 10 minutes.
5. Set investigation cadence (every 15 minutes) and communicate updates.
6. Decide mitigation path or rollback; document commands used.

# Recovery / Rollback
Capture rollback plans in real time; confirm they are executed and documented before ending the incident.

# Validation
Ensure systems return to baseline metrics and customer impact is resolved.

# Contacts
- Primary: incident commander
- Escalation: CTO / duty executive

# References
- [[Runbooks/Operations/Daily System Check]]
- Public status page checklist

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


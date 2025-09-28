---
title: Daily Systems Check
created: 2024-03-01
updated: {{date:YYYY-MM-DD}}
tags: [runbook, operations]
service: core-ops
owner: on-call engineer
impact: medium
---

# Summary
A lightweight checklist to confirm critical services and dashboards look healthy at the start of each day.

# Preconditions
- Access to observability dashboards (Grafana, Kibana).
- PagerDuty or incident alerting system online.

# Trigger
Run once every morning before business hours begin.

# Steps
1. Review overnight alerts; confirm any open incidents have active owners.
2. Check service dashboards for error rate spikes > 5%.
3. Verify queued jobs backlog is below agreed threshold.
4. Update the status channel with a quick health summary.

# Recovery / Rollback
If any indicators breach thresholds, escalate via PagerDuty and consult the relevant incident runbook.

# Validation
Confirm all checks are green and there are no unacknowledged incidents in the queue.

# Contacts
- Primary: on-call
- Escalation: engineering manager

# References
- [[Runbooks/Incidents/Incident Triage]]
- Team dashboards bookmarks

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


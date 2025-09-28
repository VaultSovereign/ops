# Prompt Patterns

Common repeatable structures you can reuse:

## CRISP Framework
1. **Context** — what the assistant needs to know.
2. **Request** — the explicit task.
3. **Intent** — the why behind the task.
4. **Style** — tone, formatting, or constraints.
5. **Post-processing** — checks, follow-ups, or validation.

## Role + Steps + Check
```
You are <role>
Follow these steps:
1. ...
2. ...
3. ...
Return: <format expectations>
Double-check: <quality bar>
```

## Chain of Thought Guardrails
```
Think step-by-step before answering. Use scratchpad reasoning in <reasoning></reasoning> tags. Output the final answer outside of those tags.
```

## Red-Team Prompt
```
Find gaps, risks, or failure modes in these instructions. Rate severity (1-5) and suggest mitigations.
```

Tag prompts that use these patterns with `#pattern` for quick filtering.

## Quality + Safety Companion Blocks
Layer these blocks onto any pattern to clarify expectations:

### Quality Checklist
- List the top signals that confirm a strong answer.
- Call out common mistakes or omissions to double-check.
- Tie checklist items to evidence or validation steps when possible.

### Safety Guardrails
- Spell out prohibited actions, escalation triggers, and approval flows.
- Reference relevant policies or runbooks (e.g., `[[Runbooks/Incident Response]]`).
- Reinforce consent, scope, and logging requirements for sensitive tasks.

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


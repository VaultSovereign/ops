# MCP Knowledge Summon — Blueprint & Automation {#top}

**Tags:** mcp, knowledge, automation, context, guardrails\
**Safety class:** read-only (advisory when executing with providers)

**Purpose**\
A practical pattern to "summon" curated knowledge into AI workflows using an MCP-style connector layer with reproducible guardrails and policy alignment.

> *Model Context Protocol (MCP) standardizes how tools expose context to models. This blueprint mirrors that approach locally with filesystem connectors, ranking algorithms, and safety controls.*

______________________________________________________________________

## Architecture Overview

- **Connectors**: Adapters that fetch and normalize text content
  - Filesystem (Markdown, text) — *included in script*
  - Git (commit messages, diffs) — *future enhancement*
  - Web (cached scrapes) — *future enhancement*
  - Vector store (semantic recall) — *future enhancement*
- **Ranker**: Keyword overlap scoring (pluggable for embeddings)
- **Prompt Builder**: System guardrails + user query + cited snippets
- **Providers**: OpenAI or Anthropic integration (optional; dry-run default)

## Flow Diagram

```text
Query → Connectors → Ranking → Context Assembly → Provider → Output
```

______________________________________________________________________

## Usage Patterns

### Inputs

- `query`: `{{natural_language_question}}`
- `config`: `{{config_file_path}}` (optional)
- `sources`: `{{directory_list}}` (optional override)
- `max_files`: `{{integer}}` (default: 20)
- `max_chars`: `{{integer}}` (default: 4000)
- `provider`: `{{openai | anthropic}}` (optional)
- `model`: `{{model_name}}` (optional)
- `dry_run`: `{{boolean}}` (default: true)

### Expected Outputs

- Context assembly with source citations
- Ranked content snippets with relevance scores
- Provider response (when `--execute` flag used)
- Audit trail in `eval-results/knowledge-summon/` (when `--out` specified)

### Command Examples

```bash
# Dry-run exploration (safe, no network calls)
python3 scripts/mcp_knowledge_summon.py \
  --query "Map our incident response playbooks to hardening steps" \
  --config templates/mcp-summon.config.json \
  --dry-run

# Targeted source search
python3 scripts/mcp_knowledge_summon.py \
  --query "OSINT recon guardrails for red-team emulation" \
  --sources guides docs prompts \
  --max-files 12 --max-chars 2400 --dry-run

# Execute with provider (requires API key)
python3 scripts/mcp_knowledge_summon.py \
  --query "Draft an IR runbook outline based on our library" \
  --config templates/mcp-summon.config.json \
  --provider openai --model gpt-4o-mini \
  --execute --out eval-results/knowledge-summon/ir-draft.md
```text

______________________________________________________________________

## MCP Server Integration

**Purpose**\
Expose knowledge summoning through the ops MCP stdio server for programmatic orchestration by agent clients.

## 

```bash
python -m scripts.ops_mcp --stdio
```text

## 

1. Send `initialize` handshake
1. Call `list_tools` to discover `knowledge.summon`
1. Invoke with JSON-RPC 2.0 protocol

## 

```json
{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "call_tool",
  "params": {
    "name": "knowledge.summon",
    "arguments": {
      "query": "Summon PCI DSS runbooks",
      "dry_run": true
    }
  }
}
```text

## 

- Server executes `make docs:summon` wrapper
- Uses repo defaults from `templates/mcp-summon.config.json`
- Tool metadata in `tools/index.json` under `mcp_tools` section

______________________________________________________________________

## Safety & Governance Framework

## 

- **Read-only**: Default mode for context assembly and analysis
- **Advisory**: When executing with AI providers (requires explicit `--execute`)

## 

- **Minimization**: Enforce `--max-files` and `--max-chars` limits
- **PII Handling**: Strip sensitive data per classification policies
- **Citations**: Always include source paths for provenance
- **Audit Trail**: Persist inputs/outputs to `eval-results/knowledge-summon/`

## 

- Validate config schema before execution
- Confirm source authorization and access permissions
- Review output for sensitive data before sharing
- Document query intent and expected outcomes

## 

- Default to dry-run mode; require explicit `--execute` for provider calls
- Restrict to pre-approved source directories
- Enable Sources Ledger via `scripts/ritual_cite.py` post-processing
- Log all operations for security review

______________________________________________________________________

## Configuration Schema

## 

```json
{
  "provider": "openai",
  "model": "gpt-4o-mini", 
  "pre_prompt": "You are a safety-graded assistant...",
  "guardrails": { 
    "safety_class": "read-only", 
    "block_patterns": [] 
  },
  "sources": [
    { 
      "type": "filesystem", 
      "include": ["guides/**/*.md", "docs/**/*.md", "prompts/**/*.md"], 
      "exclude": ["**/node_modules/**"] 
    }
  ]
}
```text

## 

- **OpenAI**: Set `OPENAI_API_KEY`; models: `gpt-4o-mini`, `o1-mini`
- **Anthropic**: Set `ANTHROPIC_API_KEY`; models: `claude-3-5-sonnet`
- **Execution**: Opt-in via `--execute`; otherwise assembles payload and prints plan

______________________________________________________________________

## Extension Points

## 

- **Git Integration**: Track file changes, weight recent commits higher
- **Web Scraping**: Pre-approved cached mirrors only (no live scraping in CI)
- **Vector Search**: Local embedding index (`sqlite + faiss`) for semantic recall

## 

- Semantic similarity scoring via embeddings
- Recency weighting for time-sensitive queries
- Authority scoring based on source reputation

______________________________________________________________________

— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · <https://vaultmesh.example/>
````

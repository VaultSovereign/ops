# Ritual Cite — Auto-footnote Engraver & Sources Ledger

**Purpose**
Convert bare URLs and placeholder links (`[source](https://…)`, `[ref](https://…)`, `[*](https://…)`) into stable footnotes, then append a Sources Ledger summarizing citations by domain. Code and fenced blocks are preserved.

**Script**: `Scripts/ritual_cite.py`  
**Dependencies**: Python 3.9+ (no external packages)

## Usage

```bash
# Dry run — show diffs only
python Scripts/ritual_cite.py "Guides/**/*.md"

# Write changes in-place
python Scripts/ritual_cite.py "Guides/**/*.md" --write
```

Examples
- [^fn-0620d248] → `[^fn-xxxxxxxx]` with `[^fn-xxxxxxxx]: example.com — https://www.example.com/page`
- `[source](https://archive.example.org/item)` → `[^fn-yyyyyyyy]` with `[^fn-yyyyyyyy]: source — https://archive.example.org/item`

### CI Integration (Optional)

#### pre-commit

```bash
cat > .git/hooks/pre-commit <<'SH'
#!/usr/bin/env bash
set -e
CHANGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.md$' || true)
[ -z "$CHANGED" ] && exit 0
python Scripts/ritual_cite.py $CHANGED --write
git add $CHANGED
SH
chmod +x .git/hooks/pre-commit
```

#### GitHub Actions (preview sweep)

```yaml
name: Ritual Cite
on:
  pull_request:
    paths: ["**/*.md"]
jobs:
  cite:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python Scripts/ritual_cite.py "Guides/**/*.md"
```

### Notes
- Footnote IDs are hash-based and stable across runs.
- Existing footnotes are preserved and de-duplicated.
- If you want page titles, add a separate optional fetch step (kept off by default for determinism).

---

## Footnote Scaffold for “Why Prompt Libraries Matter”

> Drop these markers beside the claims, then run Ritual Cite once real links are added.

```markdown
Industry references (for example, the UF Business Library[^ufb] and AICamp 2025 analysis[^aicamp]) …

```


## Sources Ledger

| Domain | Citations |
|---|---|
| example.com | 1 |

---

### 📝 Footnotes

[^ufb]: *UF Business Library* → [<ADD_URL>](<ADD_URL>)
[^aicamp]: *AICamp 2025* → [<ADD_URL>](<ADD_URL>)
[^fn-0620d248]: *example.com* → [https://www.example.com/page](https://www.example.com/page)

---

## 📚 Sources & References

**1** citation from **example.com**


---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/


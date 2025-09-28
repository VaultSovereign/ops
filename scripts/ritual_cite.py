# -*- coding: utf-8 -*-
"""
ritual_cite.py — VaultMesh Markdown ritual to auto-format citations into footnotes
and maintain a Sources Ledger.

USAGE:
    python ritual_cite.py path/to/file.md [more/files.md] --write
    python ritual_cite.py docs/**/*.md             # dry run (shows planned changes)
    python ritual_cite.py --help
"""
import re, argparse, sys, pathlib, hashlib
from collections import OrderedDict, defaultdict

PROTECTED_TOKEN = "§§CODE§§"

# Heuristic patterns
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')
BARE_URL_RE = re.compile(r'(?<!\()(?<!\])(?<!\))\bhttps?://[^\s\)]+')
FOOTNOTE_DEF_RE = re.compile(r'^\[\^([^\]]+)\]\:\s*(.*)$')
CODE_SPAN_RE = re.compile(r'`[^`]*`')
CODE_BLOCK_FENCE_RE = re.compile(r'(^|\n)```[\s\S]*?```', re.MULTILINE)

PLACEHOLDER_TEXTS = {"source","ref","reference","citation","link","here","*","**","***","????","todo","TODO"}

def normalize_domain(url: str) -> str:
    from urllib.parse import urlparse
    netloc = urlparse(url).netloc.lower()
    return netloc.lstrip("www.")

def short_id(url: str) -> str:
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return f"fn-{h}"

def protect_code(text: str):
    # Protect fenced blocks
    fenced = []
    def repl_block(m):
        fenced.append(m.group(0))
        return f"\n{PROTECTED_TOKEN}{len(fenced)-1}\n"
    text = CODE_BLOCK_FENCE_RE.sub(repl_block, text)

    # Protect inline code
    inline = []
    def repl_span(m):
        inline.append(m.group(0))
        return f"{PROTECTED_TOKEN}i{len(inline)-1}"
    text = CODE_SPAN_RE.sub(repl_span, text)
    return text, fenced, inline

def unprotect_code(text: str, fenced, inline):
    # Restore inline first (unique tokens)
    for i, seg in enumerate(inline):
        text = text.replace(f"{PROTECTED_TOKEN}i{i}", seg)
    # Restore fenced blocks
    for i, seg in enumerate(fenced):
        text = text.replace(f"\n{PROTECTED_TOKEN}{i}\n", seg)
    return text

def extract_existing_footnotes(lines):
    footnotes = OrderedDict()
    new_lines = []
    for line in lines:
        m = FOOTNOTE_DEF_RE.match(line.strip())
        if m:
            key, rest = m.group(1), m.group(2)
            footnotes[key] = rest
            # omit from main content; we'll re-append in normalized position
            continue
        new_lines.append(line)
    return new_lines, footnotes

def build_ledger(footnotes):
    counts = defaultdict(int)
    for body in footnotes.values():
        m = re.search(r'(https?://\S+)', body)
        if m:
            counts[normalize_domain(m.group(1))] += 1
    if not counts:
        return ""
    
    # Enhanced styling with better typography
    header = "---\n\n## 📚 Sources & References\n\n"
    
    if len(counts) == 1:
        domain, count = next(iter(counts.items()))
        citation_text = "citation" if count == 1 else "citations"
        return f"{header}**{count}** {citation_text} from **{domain}**\n\n"
    
    # Multiple domains - use enhanced table with emojis and better alignment
    table_header = "| 🌐 **Domain** | 📖 **Citations** |\n|:---|:---:|\n"
    rows = "\n".join(f"| `{d}` | **{n}** |" for d, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])))
    
    total = sum(counts.values())
    total_text = f"\n*Total: **{total}** citations across **{len(counts)}** domains*\n\n"
    
    return header + table_header + rows + total_text

def transform(content, path):
    # Separate YAML front matter if present
    yaml_front = ""
    if content.startswith("---\n"):
        parts = content.split("\n---\n", 1)
        if len(parts) == 2:
            yaml_front = parts[0] + "\n---\n"
            content = parts[1]

    # Extract and remove footnote definitions; we will rebuild
    lines = content.splitlines(keepends=True)
    body_lines, existing = extract_existing_footnotes(lines)
    body = "".join(body_lines)

    # Protect code blocks/spans
    protected, fenced, inline = protect_code(body)

    # Mapping URL -> footnote key
    url2key = {}
    # Start with existing where URL is present
    for k,v in existing.items():
        m = re.search(r'(https?://\S+)', v)
        if m:
            url2key[m.group(1)] = k

    planned_defs = OrderedDict(existing)

    # 1) Convert placeholder-style markdown links to footnotes
    def repl_link(m):
        text, url = m.group(1), m.group(2)
        if text.strip().lower() in PLACEHOLDER_TEXTS or text.strip().startswith("placeholder"):
            key = url2key.get(url) or short_id(url)
            url2key[url] = key
            planned_defs.setdefault(key, f"{text.strip() or 'Source'} — {url}")
            return f"[^{key}]"
        else:
            return m.group(0)

    protected = MD_LINK_RE.sub(repl_link, protected)

    # 2) Convert bare URLs to footnotes
    def repl_bare(m):
        url = m.group(0).rstrip(".,);]")
        key = url2key.get(url) or short_id(url)
        url2key[url] = key
        planned_defs.setdefault(key, f"{normalize_domain(url)} — {url}")
        return f"[^{key}]"
    protected = BARE_URL_RE.sub(repl_bare, protected)

    # Restore code
    transformed_body = unprotect_code(protected, fenced, inline)

    # Normalize spacing: ensure single trailing newline
    transformed_body = transformed_body.rstrip() + "\n"

    # Compose enhanced footnotes block with better formatting
    if planned_defs:
        # Add section separator and header for footnotes
        footnotes_header = "---\n\n### 📝 Footnotes\n\n"
        footnote_lines = []
        
        for k, v in planned_defs.items():
            # Enhanced footnote formatting with better typography
            if " — " in v:
                title, url = v.split(" — ", 1)
                # Clean up title and make it look better
                if title.strip() in PLACEHOLDER_TEXTS or "Source" in title:
                    clean_domain = normalize_domain(url)
                    footnote_lines.append(f"[^{k}]: **{clean_domain.title()}** → [{url}]({url})")
                else:
                    footnote_lines.append(f"[^{k}]: *{title.strip()}* → [{url}]({url})")
            else:
                footnote_lines.append(f"[^{k}]: {v}")
        
        foot_block = footnotes_header + "\n".join(footnote_lines) + "\n\n"
    else:
        foot_block = ""

    # Attach footnotes then ledger with proper spacing
    ledger = build_ledger(planned_defs)
    pieces = [yaml_front, transformed_body]
    
    if foot_block:
        # Ensure proper spacing before footnotes section
        if not transformed_body.endswith("\n\n"):
            pieces.append("\n")
        pieces.append(foot_block)
    
    if ledger:
        # Add sources ledger with proper spacing
        pieces.append(ledger)

    result = "".join(pieces)
    return result

def main():
    ap = argparse.ArgumentParser(description="Auto-format citations in Markdown files into footnotes with a Sources Ledger.")
    ap.add_argument("paths", nargs="*", help="Markdown files or glob patterns")
    ap.add_argument("--write", action="store_true", help="Write changes in place")
    args = ap.parse_args()

    if not args.paths:
        print("No paths provided.", file=sys.stderr)
        sys.exit(1)

    any_changes = False
    for p in args.paths:
        for path in pathlib.Path().glob(p):
            if not path.is_file() or path.suffix.lower() != ".md":
                continue
            original = path.read_text(encoding="utf-8")
            updated = transform(original, path)
            if updated != original:
                any_changes = True
                if args.write:
                    path.write_text(updated, encoding="utf-8")
                    print(f"✨ updated: {path}")
                else:
                    print(f"--- PLAN for {path} ---")
                    import difflib
                    diff = difflib.unified_diff(
                        original.splitlines(), updated.splitlines(),
                        fromfile=f"{path}", tofile=f"{path} (ritual)",
                        lineterm=""
                    )
                    preview = "\n".join(list(diff)[:200])
                    print(preview)
            else:
                print(f"✓ no change: {path}")

    if not any_changes and not args.write:
        print("No changes planned.")

if __name__ == "__main__":
    main()

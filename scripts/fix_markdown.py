#!/usr/bin/env python3
"""Auto-fix common markdown lint issues: bare URLs and unlabeled fences."""

import re
import sys
from pathlib import Path

DOCS = Path("docs")

def fix_bare_urls(text: str) -> str:
    """Wrap bare URLs in angle brackets to fix MD034."""
    # Match URLs not already in parentheses or angle brackets
    return re.sub(r'(?<!\()(?<!<)(https?://[^\s)>\]]+)', r'<\1>', text)

def fix_unlabeled_fences(text: str) -> str:
    """Add 'text' language to unlabeled fenced code blocks."""
    def tag_fence(match):
        fence, lang = match.group(1), match.group(2)
        return f"{fence}text\n" if not lang.strip() else match.group(0)
    
    return re.sub(r"(^```)([^\n]*)\n", tag_fence, text, flags=re.MULTILINE)

def main():
    """Process all markdown files in docs directory."""
    if not DOCS.exists():
        print("[fix_markdown] docs directory not found")
        return 1
    
    fixed = 0
    for path in DOCS.rglob("*.md"):
        try:
            original_text = path.read_text(encoding="utf-8")
            fixed_text = original_text
            
            # Apply fixes
            fixed_text = fix_bare_urls(fixed_text)
            fixed_text = fix_unlabeled_fences(fixed_text)
            
            # Write back if changed
            if fixed_text != original_text:
                path.write_text(fixed_text, encoding="utf-8")
                fixed += 1
                print(f"[fix_markdown] fixed {path}")
                
        except Exception as e:
            print(f"[fix_markdown] error processing {path}: {e}", file=sys.stderr)
    
    print(f"[fix_markdown] updated {fixed} file(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())

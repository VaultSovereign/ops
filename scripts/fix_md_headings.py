#!/usr/bin/env python3
"""Fix MD036: Convert emphasis-as-headings to proper markdown headings."""

import re
import sys
from pathlib import Path

DOCS = Path("docs")

# Patterns for emphasis that should be headings
H1 = re.compile(r"^\s*(\*\*|__|_)([^*_].+?)\1\s*$")
H2 = re.compile(r"^\s*(#+)?\s*(\*\*|__|_)([^*_].+?)\2\s*$")

def main():
    """Process all markdown files to fix emphasis-as-headings."""
    if not DOCS.exists():
        print("[fix_md_headings] docs directory not found")
        return 1
    
    updated = 0
    
    for path in DOCS.rglob("*.md"):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
            out = []
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                
                # If it's the very first non-empty line → H1
                if stripped and (not any(l.strip() for l in lines[:i])):
                    match = H1.match(stripped) or H2.match(stripped)
                    if match:
                        title = (match.group(2) if match.lastindex == 3 else match.group(1)).strip("*_ ").strip()
                        out.append(f"# {title}")
                        continue
                
                # Otherwise convert emphasized line flanked by blanks into H2
                if i > 0 and i < len(lines) - 1:
                    if not lines[i-1].strip() and not lines[i+1].strip():
                        match = H1.match(stripped) or H2.match(stripped)
                        if match:
                            title = (match.group(2) if match.lastindex == 3 else match.group(1)).strip("*_ ").strip()
                            out.append(f"## {title}")
                            continue
                
                out.append(line)
            
            new_content = "\n".join(out)
            original_content = "\n".join(lines)
            
            if new_content != original_content:
                path.write_text(new_content, encoding="utf-8")
                updated += 1
                print(f"[fix_md_headings] fixed {path}")
                
        except Exception as e:
            print(f"[fix_md_headings] error processing {path}: {e}", file=sys.stderr)
    
    print(f"[fix_md_headings] updated {updated} file(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())

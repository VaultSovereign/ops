#!/usr/bin/env python3
"""
Generate docs/index.md listing major docs (excluding digests index).
"""
import os
import sys
from glob import glob


def main():
    """Generate documentation index."""
    # Find all markdown files in docs
    docs_files = sorted([
        path for path in glob('docs/**/*.md', recursive=True)
        if os.path.basename(path) != 'index.md'
    ])
    
    # Build index content
    lines = ["# Documentation Index\n"]
    
    for path in docs_files:
        # Skip digest files for main index
        if '/digests/' in path:
            continue
        
        # Create relative link
        relative_path = path.split('/', 1)[1]  # Remove 'docs/' prefix
        lines.append(f"- [{relative_path}]({path})")
    
    # Write index file
    output_path = 'docs/index.md'
    os.makedirs('docs', exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
    
    print(f"✅ Wrote {output_path}")
    return 0


if __name__ == '__main__':
    sys.exit(main())


#!/usr/bin/env python3
"""
Ensure standard footer is present across docs/*.md files.
Idempotent (won't duplicate). Skips digests.
"""
import os
import sys
from glob import glob


FOOTER = "\n— VaultMesh · Earth's Civilization Ledger —\n© Vault Sovereign · https://vaultmesh.example/\n"


def ensure_footer(path):
    """Add footer to file if not present. Returns True if modified."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if footer already exists
    if 'VaultMesh · Earth\'s Civilization Ledger' in content:
        return False
    
    # Add footer
    with open(path, 'a', encoding='utf-8') as f:
        f.write(FOOTER)
    
    return True


def main():
    """Ensure footer across all documentation files."""
    # Find all markdown files in docs (excluding digests)
    files = sorted([
        path for path in glob('docs/**/*.md', recursive=True) 
        if '/digests/' not in path
    ])
    
    changed_count = 0
    for filepath in files:
        if ensure_footer(filepath):
            changed_count += 1
    
    print(f"Footer ensured in {changed_count} files.")
    return 0


if __name__ == '__main__':
    sys.exit(main())

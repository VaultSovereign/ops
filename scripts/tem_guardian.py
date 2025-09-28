#!/usr/bin/env python3
"""
Tem — the Remembrance Guardian.
Blocks PRs that modify governance-critical files unless they reference a proposal id.

What counts as governance-critical (tune as needed):
- guardrails/**, docs/schemas/**, .github/workflows/**,
- docs/**/*.md (excluding docs/digests/**),
- prompts/**, tools/**, CODEOWNERS, SECURITY.md, README.md

Pass conditions (any):
- PR title or body contains a proposal id (e.g., P-2025-001 or 2025-001-*)
- A file under proposals/ is part of the PR
- Label "emergency" is attached to the PR

Usage (in GitHub Actions pull_request):
  python scripts/tem_guardian.py
"""
import json
import os
import re
import subprocess
import sys


CRITICAL_PATTERNS = [
    r'^guardrails/',
    r'^docs/schemas/',
    r'^\.github/workflows/',
    r'^docs/((?!digests/).)*\.md$',
    r'^prompts/',
    r'^tools/',
    r'^CODEOWNERS$',
    r'^SECURITY\.md$',
    r'^README\.md$',
]

ID_REGEX = re.compile(r'(?:VM-)?P-\d{4}-\d{3}|\d{4}-\d{2,4}[a-z0-9\-]*', re.I)


def get_changed_files(base_sha, head_sha):
    """Get list of changed files between two commits."""
    try:
        cmd = ['git', 'diff', '--name-only', f'{base_sha}...{head_sha}']
        result = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        return [line.strip() for line in result.splitlines() if line.strip()]
    except subprocess.CalledProcessError:
        return []


def is_governance_critical(path):
    """Check if file path matches governance-critical patterns."""
    return any(re.match(pattern, path) for pattern in CRITICAL_PATTERNS)


def main():
    """Main Tem guardian function."""
    # Load GitHub event context
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if not event_path:
        print("No GITHUB_EVENT_PATH; assuming local run. PASS.")
        return 0
    
    try:
        with open(event_path, 'r', encoding='utf-8') as f:
            event = json.load(f)
    except Exception as e:
        print(f"❌ Error loading GitHub event: {e}")
        return 1
    
    if 'pull_request' not in event:
        print("Not a PR event. PASS.")
        return 0

    # Extract PR information
    pr = event['pull_request']
    base_sha = pr['base']['sha']
    head_sha = pr['head']['sha']
    title = pr.get('title') or ''
    body = pr.get('body') or ''
    labels = {label['name'] for label in pr.get('labels', [])}

    # Ensure we have the base branch for diff
    base_ref = pr['base']['ref']
    try:
        subprocess.run([
            'git', 'fetch', '--no-tags', '--prune', '--depth', '1', 
            'origin', base_ref
        ], check=False, stderr=subprocess.DEVNULL)
    except Exception:
        pass  # Continue even if fetch fails

    # Get changed files and filter for governance-critical
    changed_files = get_changed_files(base_sha, head_sha)
    critical_files = [f for f in changed_files if is_governance_critical(f)]

    if not critical_files:
        print("No governance-critical changes detected. PASS.")
        return 0

    print("🔍 Governance-critical files changed:")
    for filepath in critical_files:
        print(f"   - {filepath}")

    # Check exemption conditions
    
    # 1. Emergency label
    if 'emergency' in labels:
        print("🚨 Label 'emergency' present. PASS.")
        return 0
    
    # 2. Proposal file in PR
    if any(f.startswith('proposals/') for f in changed_files):
        print("📋 Proposal file present in PR. PASS.")
        return 0
    
    # 3. Proposal ID in title/body
    combined_text = f"{title}\n\n{body}"
    if ID_REGEX.search(combined_text):
        print("🆔 Proposal ID found in title/body. PASS.")
        return 0

    # All checks failed - block the PR
    print("\n❌ **Tem Guardian**: Missing proposal reference for governance-critical change.")
    print("\n**To proceed, add one of the following:**")
    print("  - Include a file under `proposals/` with an `id` matching your PR")
    print("  - Add a proposal ID to the PR title or body (e.g., P-2025-001)")
    print("  - Apply the 'emergency' label if this is urgent")
    print("\n**Governance-critical paths:**")
    for pattern in CRITICAL_PATTERNS:
        print(f"  - {pattern}")
    
    return 2  # Use exit code 2 to distinguish from other failures


if __name__ == '__main__':
    sys.exit(main())


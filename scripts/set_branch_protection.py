#!/usr/bin/env python3
"""Enable branch protection on the default branch with required status checks."""

from __future__ import annotations

import json
import os
import sys

import requests

API_ROOT = "https://api.github.com"
REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
BRANCH = os.environ.get("BRANCH", "main")

if not REPO or not TOKEN:
    print("[protect] Missing GITHUB_REPOSITORY or GITHUB_TOKEN", file=sys.stderr)
    sys.exit(1)

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}

BODY = {
    "required_status_checks": {
        "strict": False,
        "contexts": ["validate"],
    },
    "enforce_admins": True,
    "required_pull_request_reviews": {
        "required_approving_review_count": 1,
    },
    "restrictions": None,
}

url = f"{API_ROOT}/repos/{REPO}/branches/{BRANCH}/protection"
response = requests.put(url, headers=HEADERS, json=BODY, timeout=15)

if response.status_code >= 400:
    print("[protect] Failed to update branch protection:", response.status_code, response.text, file=sys.stderr)
    sys.exit(1)

print(f"[protect] Branch protection updated for {REPO}:{BRANCH}")

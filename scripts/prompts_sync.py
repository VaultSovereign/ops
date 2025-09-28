#!/usr/bin/env python3
"""Normalize prompts/index.json entries with required metadata fields."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


def main() -> int:
    index_path = Path("prompts/index.json")
    if not index_path.exists():
        print("[prompts] WARN: prompts/index.json not found; skipping")
        return 0

    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[prompts] ERROR: failed to parse {index_path}: {exc}")
        return 1

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        print("[prompts] WARN: prompts/index.json missing 'prompts' array; skipping")
        return 0

    today = date.today().isoformat()
    changed = 0
    for item in prompts:
        if not isinstance(item, dict):
            continue
        before = item.copy()
        tags = item.get("tags") or []
        primary_tag = tags[0] if tags else "general"
        item.setdefault("domain", primary_tag)
        item.setdefault("eval_tag", "none")
        summary = item.get("summary")
        if not isinstance(summary, str) or not summary.strip():
            item["summary"] = "TBD"
        last_reviewed = item.get("last_reviewed")
        if not isinstance(last_reviewed, str) or not last_reviewed.strip():
            item["last_reviewed"] = today
        if not isinstance(item.get("links"), list):
            item["links"] = []
        if before != item:
            changed += 1

    if changed:
        index_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"[prompts] normalized {changed} prompt entries")
    else:
        print("[prompts] no-op (metadata already normalized)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

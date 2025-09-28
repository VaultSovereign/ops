#!/usr/bin/env python3
"""Validate prompt metadata contract within prompts/index.json."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

REQUIRED_FIELDS = ["owner", "domain", "eval_tag", "summary", "last_reviewed", "links"]
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_links(root: Path, ident: str, links: list[str]) -> list[str]:
    errors: list[str] = []
    for target in links:
        if not isinstance(target, str):
            errors.append(f"{ident} link entry must be string (got {type(target).__name__})")
            continue
        if "://" in target:
            continue
        candidate = target.split("#", 1)[0]
        if not candidate:
            continue
        if not (root / candidate).exists():
            errors.append(f"{ident} link target not found: {target}")
    return errors


def main() -> int:
    root = Path(".").resolve()
    index_path = root / "prompts" / "index.json"
    if not index_path.exists():
        print("[prompts] WARN: prompts/index.json not found; skipping lint")
        return 0

    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[prompts] ERROR: failed to parse prompts/index.json: {exc}")
        return 1

    prompts = data.get("prompts")
    if not prompts:
        print("[prompts] WARN: no prompt entries found")
        return 0

    errors: list[str] = []

    for item in prompts:
        if not isinstance(item, dict):
            errors.append("prompt entry is not an object")
            continue
        ident = item.get("id") or item.get("title") or "<unknown>"
        path_value = item.get("path")
        if path_value:
            if not (root / path_value).exists():
                errors.append(f"{ident} references missing path {path_value}")
        for field in REQUIRED_FIELDS:
            if field not in item:
                errors.append(f"{ident} missing required field '{field}'")
                continue
            value = item[field]
            if field == "summary":
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{ident} summary must be a non-empty string")
            elif field == "last_reviewed":
                if not isinstance(value, str) or not DATE_PATTERN.match(value.strip()):
                    errors.append(f"{ident} last_reviewed must be YYYY-MM-DD (got {value!r})")
                else:
                    try:
                        datetime.strptime(value.strip(), "%Y-%m-%d")
                    except ValueError:
                        errors.append(f"{ident} last_reviewed is not a valid date ({value})")
            elif field == "links":
                if not isinstance(value, list):
                    errors.append(f"{ident} links must be a list")
                else:
                    errors.extend(validate_links(root, ident, value))

    if errors:
        print("[prompts] FAILED with the following issues:")
        for message in errors:
            print(f" - {message}")
        return 1

    print("[prompts] OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

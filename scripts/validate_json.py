#!/usr/bin/env python3
"""Validate repository JSON catalogs against their schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Callable

from jsonschema import Draft7Validator


def load(path: str) -> dict | None:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"[json] WARN missing {path}")
        return None


def validate(schema_path: str, data_path: str, *, draft: Callable = Draft7Validator) -> bool:
    schema = load(schema_path)
    data = load(data_path)
    if schema is None or data is None:
        return True
    validator = draft(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if not errors:
        print(f"[json] OK {data_path}")
        return True
    for err in errors:
        location = ".".join(str(p) for p in err.path) or "<root>"
        print(f"[json] ERROR {data_path} :: {location} :: {err.message}")
    return False


def main() -> int:
    ok = True
    ok &= validate("prompts/index.schema.json", "prompts/index.json", draft=Draft7Validator)
    ok &= validate("tools/index.schema.json", "tools/index.json", draft=Draft7Validator)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

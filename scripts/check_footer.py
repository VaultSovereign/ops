#!/usr/bin/env python3
"""Hardened footer compliance gate for VaultMesh markdown assets."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable


REQUIRED_FOOTER = (
    "— VaultMesh · Earth’s Civilization Ledger —\n"
    "© Vault Sovereign · https://vaultmesh.example/\n"
)

FOOTER_LINE_RE = re.compile(r"^— VaultMesh · Earth’s Civilization Ledger —$", re.M)
LINK_RE = re.compile(r"https?://", re.I)

IGNORE_DIRS = {".git", ".github", "node_modules", ".obsidian"}


def iter_markdown(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() == ".md":
            if any(part in IGNORE_DIRS for part in path.parts):
                continue
            yield path
        elif path.is_dir():
            for candidate in path.rglob("*.md"):
                if any(part in IGNORE_DIRS for part in candidate.parts):
                    continue
                yield candidate


def has_required_footer(text: str) -> bool:
    return bool(FOOTER_LINE_RE.search(text))


def tail_has_link(text: str, tail_lines: int = 20) -> bool:
    lines = text.splitlines()[-tail_lines:]
    return any(LINK_RE.search(line) for line in lines)


def main(argv: list[str]) -> int:
    targets = [Path(arg) for arg in argv[1:]] or [Path("docs")]

    missing_footer: list[Path] = []
    footer_without_link: list[Path] = []

    for md_file in iter_markdown(targets):
        try:
            content = md_file.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"[footer] WARN unable to read {md_file}: {exc}")
            continue

        if not has_required_footer(content):
            missing_footer.append(md_file)
            continue

        if not tail_has_link(content):
            footer_without_link.append(md_file)

    if missing_footer or footer_without_link:
        if missing_footer:
            print("[footer] missing footer block:")
            for path in missing_footer:
                print(f" - {path}")
        if footer_without_link:
            print("[footer] footer present but tail lacks link:")
            for path in footer_without_link:
                print(f" - {path}")
        print(
            "\nRequired footer block (append verbatim):\n"
            f"{REQUIRED_FOOTER}"
        )
        return 1

    print("[footer] OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
"""Generate docs/summon.md from repo activity, TODOs, and prompt metadata."""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

CONFIG_PATH = Path("templates/mcp-summon.config.json")
OUTPUT_PATH = Path("docs/summon.md")
RECENT_WINDOW_DAYS = 7
STALE_AFTER_DAYS = 90
FOOTER = (
    "— VaultMesh · Earth’s Civilization Ledger —\n"
    "© Vault Sovereign · https://vaultmesh.example/\n"
)
PLACEHOLDER_SUMMARY_PATTERNS = ("tbd", "todo", "tba", "pending")


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"[summon] invalid config JSON: {exc}") from exc


def gather_source_files(config: dict) -> List[Path]:
    includes: List[str] = []
    excludes: List[str] = []
    for source in config.get("sources", []):
        if source.get("type") == "filesystem":
            includes.extend(source.get("include", []))
            excludes.extend(source.get("exclude", []))
    if not includes:
        includes = ["docs/**/*.md", "guides/**/*.md", "prompts/**/*.md"]

    files: List[Path] = []
    seen: set[Path] = set()
    for pattern in includes:
        for match in Path().glob(pattern):
            if match.is_dir():
                continue
            if any(match.match(ex) for ex in excludes):
                continue
            if match.suffix.lower() not in {".md", ".txt"}:
                continue
            normalized = match.resolve()
            if normalized in seen:
                continue
            seen.add(normalized)
            files.append(normalized)
    return sorted(files)


def slugify(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def extract_headings_and_links(files: Sequence[Path]) -> Tuple[List[Tuple[Path, str]], List[Tuple[str, str, Path]]]:
    heading_entries: List[Tuple[Path, str]] = []
    link_entries: List[Tuple[str, str, Path]] = []
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rel_path = path.relative_to(Path.cwd())
        for line in text.splitlines():
            if line.startswith("#"):
                heading = line.lstrip("#").strip()
                if heading:
                    heading_entries.append((rel_path, heading))
            for match in link_pattern.finditer(line):
                link_text, target = match.groups()
                link_entries.append((link_text.strip(), target.strip(), rel_path))
    return heading_entries, link_entries


def git_shortlog(days: int) -> str:
    try:
        result = subprocess.run(
            ["git", "shortlog", "HEAD", f"--since={days}.days"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "No repository activity detected."

    output = result.stdout.strip()
    return output or "No commits in the selected window."


def gather_todos(files: Sequence[Path], limit: int = 30) -> List[Tuple[Path, int, str]]:
    todo_re = re.compile(r"\b(TODO|FIXME)\b", re.IGNORECASE)
    results: List[Tuple[Path, int, str]] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            if todo_re.search(line):
                snippet = line.strip()
                results.append((path.relative_to(Path.cwd()), idx, snippet))
                if len(results) >= limit:
                    return results
    return results


def analyze_prompts(stale_after_days: int) -> Tuple[int, List[Tuple[str, str]], List[Tuple[str, str]]]:
    index_path = Path("prompts/index.json")
    if not index_path.exists():
        return 0, [], []

    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0, [], []

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        return 0, [], []

    total = len(prompts)
    missing_summary: List[Tuple[str, str]] = []
    stale_review: List[Tuple[str, str]] = []
    today = datetime.utcnow().date()
    stale_delta = timedelta(days=stale_after_days)

    for prompt in prompts:
        if not isinstance(prompt, dict):
            continue
        ident = prompt.get("id") or prompt.get("title") or "<unknown>"
        summary = prompt.get("summary", "")
        if not isinstance(summary, str) or not summary.strip() or summary.strip().lower() in PLACEHOLDER_SUMMARY_PATTERNS:
            missing_summary.append((ident, str(prompt.get("path", ""))))
        last_reviewed = prompt.get("last_reviewed")
        if isinstance(last_reviewed, str):
            try:
                reviewed_date = datetime.strptime(last_reviewed, "%Y-%m-%d").date()
            except ValueError:
                stale_review.append((ident, last_reviewed))
                continue
            if today - reviewed_date > stale_delta:
                stale_review.append((ident, last_reviewed))
        else:
            stale_review.append((ident, str(last_reviewed)))

    return total, missing_summary, stale_review


def format_todo_section(todos: Sequence[Tuple[Path, int, str]]) -> str:
    if not todos:
        return "- None found."
    lines = []
    for path, line_no, snippet in todos:
        lines.append(f"- `{path}:{line_no}` — {snippet}")
    return "\n".join(lines)


def format_prompt_section(total: int, missing: Sequence[Tuple[str, str]], stale: Sequence[Tuple[str, str]]) -> str:
    lines = [f"- Total prompts: {total}"]
    lines.append(f"- Missing summaries: {len(missing)}")
    lines.append(f"- Stale last_reviewed (> {STALE_AFTER_DAYS} days): {len(stale)}")
    if missing:
        lines.append("\n**Prompts missing summaries**")
        for ident, path in missing[:20]:
            lines.append(f"- {ident} ({path})")
    if stale:
        lines.append("\n**Prompts needing review**")
        for ident, stamp in stale[:20]:
            lines.append(f"- {ident} (last reviewed {stamp})")
    return "\n".join(lines)


def format_headings_section(headings: Sequence[Tuple[Path, str]]) -> str:
    if not headings:
        return "- No headings discovered in configured sources."
    lines: List[str] = []
    for path, heading in headings[:50]:
        anchor = slugify(heading)
        lines.append(f"- [{heading}]({path}#{anchor})")
    if len(headings) > 50:
        lines.append(f"- …and {len(headings) - 50} more headings")
    return "\n".join(lines)


def format_links_section(links: Sequence[Tuple[str, str, Path]]) -> str:
    if not links:
        return "- No links discovered in configured sources."
    lines: List[str] = []
    for text, target, path in links[:50]:
        display = text or target
        lines.append(f"- [{display}]({target}) — `{path}`")
    if len(links) > 50:
        lines.append(f"- …and {len(links) - 50} more links")
    return "\n".join(lines)


def build_report(
    generated_at: datetime,
    shortlog: str,
    todos: Sequence[Tuple[Path, int, str]],
    prompt_stats: Tuple[int, Sequence[Tuple[str, str]], Sequence[Tuple[str, str]]],
    headings: Sequence[Tuple[Path, str]],
    links: Sequence[Tuple[str, str, Path]],
) -> str:
    total, missing, stale = prompt_stats
    report = [
        "# VaultMesh Knowledge Summon",
        "",
        f"Generated: {generated_at.strftime('%Y-%m-%d %H:%M:%S')} UTC",
        "",
        "## Recent changes (last 7 days)",
        "",
        "```",
        shortlog.strip() or "No commits in the selected window.",
        "```",
        "",
        "## Open TODO / FIXME",
        "",
        format_todo_section(todos),
        "",
        "## Prompt coverage",
        "",
        format_prompt_section(total, missing, stale),
        "",
        "## Source headings",
        "",
        format_headings_section(headings),
        "",
        "## Discovered links",
        "",
        format_links_section(links),
        "",
        FOOTER.strip(),
        "",
    ]
    return "\n".join(report) + "\n"


def main() -> int:
    config = load_config(CONFIG_PATH)
    files = gather_source_files(config)
    headings, links = extract_headings_and_links(files)
    shortlog = git_shortlog(RECENT_WINDOW_DAYS)
    todos = gather_todos(files)
    prompt_stats = analyze_prompts(STALE_AFTER_DAYS)
    generated_at = datetime.utcnow()

    content = build_report(generated_at, shortlog, todos, prompt_stats, headings, links)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT_PATH.exists():
        current = OUTPUT_PATH.read_text(encoding="utf-8")
        if current == content:
            print("[summon] no-op (docs/summon.md already current)")
            return 0

    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print("[summon] wrote docs/summon.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

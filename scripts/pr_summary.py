#!/usr/bin/env python3
"""Create or update the VaultMesh PR summary comment with rich impact details."""

from __future__ import annotations

import json
import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from xml.etree import ElementTree as ET

import requests

API_ROOT = "https://api.github.com"
SUMMARY_TAG = "<!-- vaultmesh-pr-summary -->"
EVAL_RESULTS_DIR = Path("eval-results")
PROMPT_INDEX_PATH = Path("prompts/index.json")
MAX_DIFFSTAT_ROWS = 10
MAX_SECTION_ITEMS = 15


PARSER = argparse.ArgumentParser(description="VaultMesh PR summary generator")
PARSER.add_argument("--no-post", action="store_true", help="Preview only; do not post comment or labels")
CLI_ARGS = PARSER.parse_args()


def cov_badge(pct: Optional[float]) -> str:
    if pct is None:
        return "N/A"
    if pct < 60:
        badge = "🟥"
    elif pct < 80:
        badge = "🟧"
    elif pct < 90:
        badge = "🟨"
    else:
        badge = "🟩"
    return f"{badge} {pct:.1f}%"


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"[pr-summary] Missing environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def github_request(method: str, path: str, *, token: str, json_body: Optional[dict] = None, params: Optional[dict] = None) -> dict | list:
    url = f"{API_ROOT}{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }
    response = requests.request(method, url, headers=headers, json=json_body, params=params)
    if response.status_code >= 400:
        raise RuntimeError(f"GitHub API error {response.status_code}: {response.text}")
    if response.text:
        return response.json()
    return {}


def resolve_pr_number() -> str:
    if pr := os.environ.get("PR_NUMBER"):
        return pr

    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).exists():
        payload = json.loads(Path(event_path).read_text(encoding="utf-8"))
        number = payload.get("pull_request", {}).get("number")
        if number:
            return str(number)

    print("[pr-summary] Unable to determine PR number", file=sys.stderr)
    sys.exit(1)


def fetch_changed_files(repo: str, pr_number: str, token: str) -> List[Dict]:
    files: List[Dict] = []
    page = 1
    while True:
        chunk = github_request(
            "GET",
            f"/repos/{repo}/pulls/{pr_number}/files",
            token=token,
            params={"per_page": 100, "page": page},
        )
        if not chunk:
            break
        files.extend(chunk)
        page += 1
    return files


def collect_area_impacts(changed: Sequence[Dict]) -> Tuple[Dict[str, List[str]], set[str]]:
    impacts = {"docs": [], "prompts": [], "ops_mcp": [], "schema": []}
    labels: set[str] = set()
    for item in changed:
        path = item["filename"]
        if path.startswith("docs/"):
            impacts["docs"].append(path)
            labels.add("area:docs")
        if path.startswith("prompts/"):
            impacts["prompts"].append(path)
            labels.add("area:prompts")
        if path.startswith("scripts/ops_mcp/"):
            impacts["ops_mcp"].append(path)
            labels.add("ops:mcp")
        if path.endswith(".schema.json"):
            impacts["schema"].append(path)
            labels.add("type:schema")
    return impacts, labels


def load_eval_metrics() -> Tuple[Optional[float], Optional[str], Optional[Dict]]:
    coverage_pct: Optional[float] = None
    coverage_note: Optional[str] = None
    adversarial_summary: Optional[Dict] = None

    for candidate in [EVAL_RESULTS_DIR / "coverage-results.json", EVAL_RESULTS_DIR / "coverage.json"]:
        if not candidate.exists():
            continue
        try:
            data = json.loads(candidate.read_text())
        except Exception as exc:  # noqa: BLE001
            coverage_note = f"Failed to parse {candidate.name}: {exc}"
            break
        if isinstance(data, dict):
            total = data.get("total") or {}
            lines = total.get("lines") if isinstance(total, dict) else {}
            if isinstance(lines, dict) and isinstance(lines.get("pct"), (int, float)):
                coverage_pct = float(lines["pct"])
            if coverage_pct is None and isinstance(data.get("coverage"), (int, float)):
                val = float(data["coverage"])
                coverage_pct = val * 100 if val <= 1.0 else val
            if coverage_pct is None and isinstance(data.get("line_rate"), (int, float)):
                val = float(data["line_rate"])
                coverage_pct = val * 100 if val <= 1.0 else val
            if coverage_pct is None and isinstance(data.get("summary"), dict):
                summary = data["summary"]
                if isinstance(summary.get("coverage_percentage"), (int, float)):
                    coverage_pct = float(summary["coverage_percentage"])
        elif isinstance(data, (int, float)):
            coverage_pct = float(data) * 100 if data <= 1.0 else float(data)
        coverage_note = str(candidate)
        break

    for path in EVAL_RESULTS_DIR.glob("adversarial*.json"):
        try:
            data = json.loads(path.read_text())
        except Exception:  # noqa: BLE001
            continue
        passed = data.get("passed") or data.get("ok") or 0
        failed = data.get("failed") or data.get("errors") or 0
        total = data.get("total") or (passed + failed)
        adversarial_summary = {
            "file": str(path),
            "passed": passed,
            "failed": failed,
            "total": total,
        }
        break

    return coverage_pct, coverage_note, adversarial_summary


def build_diffstat(changed: Sequence[Dict], limit: int = MAX_DIFFSTAT_ROWS) -> str:
    rows = sorted(
        (
            {
                "filename": item["filename"],
                "additions": item.get("additions", 0) or 0,
                "deletions": item.get("deletions", 0) or 0,
                "changes": item.get("changes")
                if item.get("changes") is not None
                else (item.get("additions", 0) or 0) + (item.get("deletions", 0) or 0),
            }
            for item in changed
        ),
        key=lambda row: row["changes"],
        reverse=True,
    )

    top = rows[:limit]
    if not top:
        return "_no diffstat available_"

    lines = ["| file | + | - | ± changes |", "|---|---:|---:|---:|"]
    for row in top:
        lines.append(
            f"| `{row['filename']}` | {row['additions']} | {row['deletions']} | {row['changes']} |"
        )
    return "\n".join(lines)


def section_list(items: Sequence[str], limit: int = MAX_SECTION_ITEMS) -> str:
    if not items:
        return "- _none_"
    preview = list(items)[:limit]
    return "\n".join(f"- `{item}`" for item in preview)


def inline_list(items: Sequence[str]) -> str:
    if not items:
        return "- _none_"
    return "- " + ", ".join(sorted(items))


def load_prompt_entries() -> List[dict]:
    if not PROMPT_INDEX_PATH.exists():
        return []
    try:
        data = json.loads(PROMPT_INDEX_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    prompts = data.get("prompts")
    return prompts if isinstance(prompts, list) else []


def slugify_label(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower())
    slug = slug.strip("-")
    return slug or "unknown"


def prompts_by_id(entries: Sequence[dict]) -> Dict[str, dict]:
    mapping: Dict[str, dict] = {}
    for entry in entries:
        if isinstance(entry, dict):
            ident = entry.get("id") or entry.get("title")
            if ident:
                mapping[str(ident)] = entry
    return mapping


def extract_ids_from_patch(patch: Optional[str]) -> set[str]:
    if not patch:
        return set()
    ids: set[str] = set()
    for line in patch.splitlines():
        if not line.startswith(("+", "-")):
            continue
        match = re.search(r'"id"\s*:\s*"([^"]+)"', line)
        if match:
            ids.add(match.group(1))
    return ids


def collect_prompt_impacts(changed: Sequence[Dict], prompt_entries: Sequence[dict]) -> Tuple[set[str], set[str], set[str], List[Tuple[str, List[str]]]]:
    prompt_map = prompts_by_id(prompt_entries)
    impacted_ids: set[str] = set()
    impacted_owners: set[str] = set()
    impacted_domains: set[str] = set()

    for item in changed:
        path = item["filename"]
        if not path.startswith("prompts/"):
            continue
        if path.endswith("index.json"):
            ids = extract_ids_from_patch(item.get("patch"))
            if not ids:
                ids = set(prompt_map.keys())
            for ident in ids:
                entry = prompt_map.get(ident)
                if not entry:
                    continue
                impacted_ids.add(ident)
                owner = entry.get("owner")
                domain = entry.get("domain")
                if owner:
                    impacted_owners.add(str(owner))
                if domain:
                    impacted_domains.add(str(domain))
            continue

        if not path.endswith(".json") or path.endswith(".schema.json"):
            continue

        file_path = Path(path)
        if not file_path.exists():
            continue
        try:
            metadata = json.loads(file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        ident = metadata.get("id") or metadata.get("title") or file_path.stem
        owner = metadata.get("owner")
        domain = metadata.get("domain")
        if ident:
            impacted_ids.add(str(ident))
        if owner:
            impacted_owners.add(str(owner))
        if domain:
            impacted_domains.add(str(domain))

    doc_link_map: Dict[str, set[str]] = {}
    for entry in prompt_entries:
        if not isinstance(entry, dict):
            continue
        ident = entry.get("id") or entry.get("title")
        if not ident:
            continue
        for link in entry.get("links", []) or []:
            if not isinstance(link, str):
                continue
            target = link.split("#", 1)[0]
            variations = {
                target,
                target.lstrip("./"),
                target.lstrip("../"),
            }
            for candidate in variations:
                if candidate:
                    doc_link_map.setdefault(candidate, set()).add(str(ident))

    related_doc_prompts: List[Tuple[str, List[str]]] = []
    docs_changed = [item["filename"] for item in changed if item["filename"].startswith("docs/")]
    for doc_path in docs_changed:
        matches: set[str] = set()
        variations = {
            doc_path,
            doc_path.lstrip("./"),
            doc_path.lstrip("../"),
        }
        for candidate in variations:
            matches.update(doc_link_map.get(candidate, set()))
        if matches:
            related_doc_prompts.append((doc_path, sorted(matches)))

    return impacted_ids, impacted_owners, impacted_domains, related_doc_prompts


def format_related_prompts(related: Sequence[Tuple[str, Sequence[str]]]) -> str:
    if not related:
        return "- _none_"
    lines: List[str] = []
    for doc_path, prompts in related:
        lines.append(f"- `{doc_path}` → {', '.join(prompts)}")
    return "\n".join(lines)


def format_impacted_prompts(impacted_ids: Sequence[str], prompt_map: Dict[str, dict]) -> str:
    if not impacted_ids:
        return "- _none_"
    lines: List[str] = []
    for ident in sorted(impacted_ids):
        meta = prompt_map.get(ident, {})
        owner = meta.get("owner", "n/a")
        domain = meta.get("domain", "n/a")
        lines.append(f"- `{ident}` — owner: {owner}, domain: {domain}")
    return "\n".join(lines)


def collect_junit_summary() -> str:
    for path in Path(".").rglob("junit*.xml"):
        try:
            root = ET.parse(path).getroot()
        except Exception:  # noqa: BLE001
            continue

        suites = list(root) if root.tag == "testsuites" else [root]
        tests = failures = errors = skipped = 0
        for suite in suites:
            tests += int(suite.attrib.get("tests", 0) or 0)
            failures += int(suite.attrib.get("failures", 0) or 0)
            errors += int(suite.attrib.get("errors", 0) or 0)
            skipped += int(suite.attrib.get("skipped", 0) or 0)

        if tests == 0:
            passed = tests
        else:
            passed = max(tests - failures - errors - skipped, 0)

        return f"{passed}/{tests} passed, {failures} failed, {errors} errors, {skipped} skipped  _(source: {path})_"

    return "N/A"


def build_summary_body(
    changed: Sequence[Dict],
    impacts: Dict[str, List[str]],
    coverage_pct: Optional[float],
    coverage_note: Optional[str],
    adversarial_summary: Optional[Dict],
    diffstat_md: str,
    owners: Sequence[str],
    domains: Sequence[str],
    related_docs_md: str,
    impacted_prompts_md: str,
    junit_md: str,
) -> str:
    added = sum(1 for f in changed if f["status"] == "added")
    modified = sum(1 for f in changed if f["status"] == "modified")
    removed = sum(1 for f in changed if f["status"] == "removed")
    additions = sum(f.get("additions", 0) for f in changed)
    deletions = sum(f.get("deletions", 0) for f in changed)

    if coverage_pct is not None:
        coverage_line = cov_badge(coverage_pct)
        if coverage_note:
            coverage_line += f"  _(source: {coverage_note})_"
    else:
        coverage_line = coverage_note or "N/A"

    adversarial_md = "N/A"
    if adversarial_summary:
        passed = adversarial_summary.get("passed", 0)
        total = adversarial_summary.get("total", 0)
        failed = adversarial_summary.get("failed", 0)
        source = adversarial_summary.get("file")
        adversarial_md = f"{passed}/{total} passed, {failed} failed"
        if source:
            adversarial_md += f"  _(source: {source})_"

    quality_block = (
        "**Quality Signals**  \n"
        f"- Coverage: {coverage_line}  \n"
        f"- Adversarial: {adversarial_md}  \n"
        f"- Tests: {junit_md}"
    )

    return (
        f"{SUMMARY_TAG}\n"
        f"### PR Summary — VaultMesh Auto\n\n"
        f"**Files**: +{added} / ~{modified} / -{removed}  \n"
        f"**Lines**: +{additions} / -{deletions}\n\n"
        f"{quality_block}\n\n"
        f"**Impacted areas**  \n"
        f"- docs: {len(impacts['docs'])}  \n"
        f"- prompts: {len(impacts['prompts'])}  \n"
        f"- ops_mcp: {len(impacts['ops_mcp'])}  \n"
        f"- schema: {len(impacts['schema'])}\n\n"
        f"**Impacted owners**  \n{inline_list(owners)}\n\n"
        f"**Impacted domains**  \n{inline_list(domains)}\n\n"
        f"**Related prompts from docs**  \n{related_docs_md}\n\n"
        f"<details><summary>Impacted prompt metadata</summary>\n\n{impacted_prompts_md}\n\n</details>\n\n"
        f"<details><summary>Top diffstat ({min(len(changed), MAX_DIFFSTAT_ROWS)})</summary>\n\n{diffstat_md}\n\n</details>\n\n"
        f"<details><summary>Changed docs</summary>\n\n{section_list(impacts['docs'])}\n\n</details>\n\n"
        f"<details><summary>Changed prompts</summary>\n\n{section_list(impacts['prompts'])}\n\n</details>\n\n"
        f"<details><summary>Changed ops_mcp</summary>\n\n{section_list(impacts['ops_mcp'])}\n\n</details>\n\n"
        f"<details><summary>Changed schema files</summary>\n\n{section_list(impacts['schema'])}\n\n</details>\n\n"
        f"### Artifacts\n{artifacts_md}\n\n"
        f"{head_tag}"
    )


def upsert_comment(
    repo: str,
    pr_number: str,
    body: str,
    token: str,
    labels: Sequence[str],
    head_sha: Optional[str],
) -> None:
    comments = github_request("GET", f"/repos/{repo}/issues/{pr_number}/comments", token=token)
    prev_comment = None
    same_head = False

    for comment in comments:
        existing_body = comment.get("body", "")
        if existing_body.startswith(SUMMARY_TAG):
            prev_comment = comment
            if head_sha and f"<!-- head:{head_sha} -->" in existing_body:
                same_head = True
            break

    if same_head:
        print("[pr-summary] No-op: same HEAD SHA, skipping comment update.")
        return

    if prev_comment:
        github_request(
            "PATCH",
            f"/repos/{repo}/issues/comments/{prev_comment['id']}",
            token=token,
            json_body={"body": body},
        )
        print("[pr-summary] Updated existing summary comment.")
    else:
        github_request(
            "POST",
            f"/repos/{repo}/issues/{pr_number}/comments",
            token=token,
            json_body={"body": body},
        )
        print("[pr-summary] Posted new summary comment.")

    if labels:
        github_request(
            "POST",
            f"/repos/{repo}/issues/{pr_number}/labels",
            token=token,
            json_body={"labels": sorted(set(labels))},
        )
        print("[pr-summary] Applied labels: ", ", ".join(sorted(set(labels))))
    else:
        print("[pr-summary] No labels inferred.")


def main() -> int:
    repo = require_env("GITHUB_REPOSITORY")
    token = require_env("GITHUB_TOKEN")
    pr_number = resolve_pr_number()

    raw_files = fetch_changed_files(repo, pr_number, token)
    if not raw_files:
        print("[pr-summary] No file changes detected.")
        return 0

    changed = [
        {
            "filename": f["filename"],
            "status": f["status"],
            "additions": f.get("additions", 0),
            "deletions": f.get("deletions", 0),
            "changes": f.get("changes", f.get("additions", 0) + f.get("deletions", 0)),
            "sha": f.get("sha"),
            "patch": f.get("patch"),
        }
        for f in raw_files
    ]

    impacts, labels = collect_area_impacts(changed)
    coverage_pct, coverage_note, adversarial_summary = load_eval_metrics()
    diffstat_md = build_diffstat(changed)
    junit_md = collect_junit_summary()

    prompt_entries = load_prompt_entries()
    impacted_ids, impacted_owners, impacted_domains, related_doc_prompts = collect_prompt_impacts(changed, prompt_entries)
    prompt_map = prompts_by_id(prompt_entries)

    owner_labels = {f"owner:{slugify_label(owner)}" for owner in impacted_owners}
    domain_labels = {f"domain:{slugify_label(domain)}" for domain in impacted_domains}
    labels.update(owner_labels)
    labels.update(domain_labels)

    related_docs_md = format_related_prompts(related_doc_prompts)

    impacted_prompts_md = format_impacted_prompts(sorted(impacted_ids), prompt_map)

    run_id = os.environ.get("GITHUB_RUN_ID")
    run_url = f"https://github.com/{repo}/actions/runs/{run_id}" if run_id else None
    
    # GitHub Pages base URL for reports
    pages_base = f"https://{repo.split('/')[0].lower()}.github.io/{repo.split('/')[1]}"
    
    artifact_lines: List[str] = []
    if run_url:
        artifact_lines.append(f"- Actions run: {run_url}")
    
    # Add GitHub Pages links for HTML reports
    artifact_lines.append(f"- 📊 [Coverage Report]({pages_base}/coverage/)")
    artifact_lines.append(f"- 🛡️ [Adversarial Analysis]({pages_base}/adversarial/)")
    artifact_lines.append(f"- 📋 [JUnit Results]({pages_base}/junit/)")
    
    # Legacy artifact detection
    for candidate in [
        "coverage/index.html",
        "eval-results/html/index.html", 
        "eval-results/coverage/index.html",
    ]:
        candidate_path = Path(candidate)
        if candidate_path.exists():
            artifact_lines.append(f"- {candidate_path.as_posix()}")
    
    artifacts_md = "\n".join(artifact_lines) if artifact_lines else "- _none detected_"

    head_sha = os.environ.get("GITHUB_SHA")
    head_tag = f"<!-- head:{head_sha} -->" if head_sha else ""

    body = build_summary_body(
        changed,
        impacts,
        coverage_pct,
        coverage_note,
        adversarial_summary,
        diffstat_md,
        sorted(impacted_owners),
        sorted(impacted_domains),
        related_docs_md,
        impacted_prompts_md,
        junit_md,
        artifacts_md,
        head_tag,
    )

    if CLI_ARGS.no_post:
        print(body)
        return 0

    upsert_comment(repo, pr_number, body, token, sorted(labels), head_sha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

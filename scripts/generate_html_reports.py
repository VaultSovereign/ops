#!/usr/bin/env python3
"""Generate HTML reports for coverage, adversarial, and JUnit results."""

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def generate_coverage_html():
    """Generate coverage HTML report."""
    reports_dir = Path("reports-html/coverage")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    # Check for existing HTML reports first
    html_sources = [
        Path("coverage/index.html"),
        Path("eval-results/html/index.html"), 
        Path("eval-results/coverage/index.html")
    ]
    
    for source in html_sources:
        if source.exists():
            target = reports_dir / "index.html"
            target.write_text(source.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
            print(f"[reports] copied {source}")
            return
    
    # Fallback: generate minimal HTML from JSON
    data = {}
    json_sources = [
        "eval-results/coverage-results.json",
        "eval-results/coverage.json"
    ]
    
    for source in json_sources:
        path = Path(source)
        if path.exists():
            try:
                data = json.loads(path.read_text())
                break
            except Exception:
                continue
    
    pct = None
    if isinstance(data, dict):
        total = data.get("total") or {}
        lines = total.get("lines") if isinstance(total, dict) else {}
        if isinstance(lines, dict) and isinstance(lines.get("pct"), (int, float)):
            pct = float(lines["pct"])
        elif isinstance(data.get("coverage"), (int, float)):
            val = float(data["coverage"])
            pct = val * 100 if val <= 1.0 else val
        elif isinstance(data.get("line_rate"), (int, float)):
            val = float(data["line_rate"])
            pct = val * 100 if val <= 1.0 else val
    elif isinstance(data, (int, float)):
        pct = float(data) * 100 if data <= 1.0 else float(data)
    
    html = f"""<!doctype html>
<html><head>
<meta charset="utf-8">
<title>Coverage Report</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 2rem; }}
.metric {{ font-size: 2rem; color: {'#22c55e' if pct and pct >= 80 else '#ef4444' if pct else '#6b7280'}; }}
</style>
</head><body>
<h1>Coverage Report</h1>
<p>Total coverage: <span class="metric"><strong>{pct if pct is not None else 'N/A'}{'%' if pct is not None else ''}</strong></span></p>
<p><em>Provide a real HTML report in <code>coverage/index.html</code> or <code>eval-results/html/index.html</code> to replace this stub.</em></p>
</body></html>"""
    
    (reports_dir / "index.html").write_text(html, encoding="utf-8")
    print("[reports] generated minimal coverage HTML")


def generate_adversarial_html():
    """Generate adversarial analysis HTML report."""
    reports_dir = Path("reports-html/adversarial")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    summary = None
    for path in sorted(Path("eval-results").glob("adversarial*.json")):
        try:
            data = json.loads(path.read_text())
            passed = data.get("passed") or data.get("ok") or 0
            failed = data.get("failed") or data.get("errors") or 0
            total = data.get("total") or (passed + failed)
            summary = {
                "file": str(path),
                "passed": passed,
                "failed": failed,
                "total": total
            }
            break
        except Exception:
            continue
    
    html = """<!doctype html>
<html><head>
<meta charset="utf-8">
<title>Adversarial Analysis</title>
<style>
body { font-family: system-ui, sans-serif; margin: 2rem; }
.metric { font-size: 1.5rem; }
.passed { color: #22c55e; }
.failed { color: #ef4444; }
</style>
</head><body>
<h1>🛡️ Adversarial Analysis</h1>
"""
    
    if summary:
        pass_rate = (summary["passed"] / summary["total"] * 100) if summary["total"] > 0 else 0
        html += f"""
<p class="metric">Results: <span class="passed"><strong>{summary['passed']}/{summary['total']} passed</strong></span>
{f', <span class="failed">{summary["failed"]} failed</span>' if summary["failed"] > 0 else ''}</p>
<p>Pass rate: <strong>{pass_rate:.1f}%</strong></p>
<p><em>Source: {summary['file']}</em></p>
"""
    else:
        html += "<p>No adversarial results found.</p>"
    
    html += "</body></html>"
    
    (reports_dir / "index.html").write_text(html, encoding="utf-8")
    print("[reports] adversarial HTML written")


def generate_junit_html():
    """Generate JUnit results HTML report."""
    reports_dir = Path("reports-html/junit")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    junit_path = Path("junit.xml")
    if junit_path.exists():
        try:
            root = ET.parse(junit_path).getroot()
            suites = list(root) if root.tag == "testsuites" else [root]
            
            tests = failures = errors = skipped = 0
            for suite in suites:
                tests += int(suite.attrib.get("tests", 0) or 0)
                failures += int(suite.attrib.get("failures", 0) or 0)
                errors += int(suite.attrib.get("errors", 0) or 0)
                skipped += int(suite.attrib.get("skipped", 0) or 0)
            
            passed = max(tests - failures - errors - skipped, 0)
            pass_rate = (passed / tests * 100) if tests > 0 else 0
            
            html = f"""<!doctype html>
<html><head>
<meta charset="utf-8">
<title>JUnit Results</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 2rem; }}
.metric {{ font-size: 1.5rem; }}
.passed {{ color: #22c55e; }}
.failed {{ color: #ef4444; }}
.skipped {{ color: #f59e0b; }}
</style>
</head><body>
<h1>📋 JUnit Results</h1>
<p class="metric">
<span class="passed"><strong>{passed}/{tests} passed</strong></span>
{f', <span class="failed">{failures} failed</span>' if failures > 0 else ''}
{f', <span class="failed">{errors} errors</span>' if errors > 0 else ''}
{f', <span class="skipped">{skipped} skipped</span>' if skipped > 0 else ''}
</p>
<p>Pass rate: <strong>{pass_rate:.1f}%</strong></p>
<p><em>Source: junit.xml</em></p>
</body></html>"""
            
        except Exception as e:
            html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>JUnit Results</title></head><body>
<h1>📋 JUnit Results</h1>
<p>Error parsing junit.xml: {e}</p>
</body></html>"""
    else:
        html = """<!doctype html>
<html><head><meta charset="utf-8"><title>JUnit Results</title></head><body>
<h1>📋 JUnit Results</h1>
<p>No junit.xml found.</p>
</body></html>"""
    
    (reports_dir / "index.html").write_text(html, encoding="utf-8")
    print("[reports] junit HTML written")


def main():
    """Generate HTML reports based on command line argument."""
    if len(sys.argv) != 2:
        print("Usage: python generate_html_reports.py <coverage|adversarial|junit>")
        sys.exit(1)
    
    report_type = sys.argv[1]
    
    if report_type == "coverage":
        generate_coverage_html()
    elif report_type == "adversarial":
        generate_adversarial_html()
    elif report_type == "junit":
        generate_junit_html()
    else:
        print(f"Unknown report type: {report_type}")
        sys.exit(1)


if __name__ == "__main__":
    main()

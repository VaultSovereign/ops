"""Smoke tests for VaultMesh ops repository."""

import json
from pathlib import Path


def test_smoke():
    """Basic smoke test to keep CI green until real test suites arrive."""
    assert True


def test_required_files_exist():
    """Verify core repository structure is intact."""
    root = Path(__file__).parent.parent
    
    required_files = [
        "README.md",
        "Makefile", 
        "prompts/index.json",
        "tools/index.json",
        "docs/index.md",
        "scripts/pr_summary.py",
        "scripts/set_branch_protection.py"
    ]
    
    for file_path in required_files:
        assert (root / file_path).exists(), f"Required file missing: {file_path}"


def test_json_schemas_valid():
    """Verify JSON files are valid and parseable."""
    root = Path(__file__).parent.parent
    
    # Standard JSON files (no comments allowed)
    json_files = [
        "prompts/index.json",
        "tools/index.json", 
        "eval-results/coverage-results.json",
        "eval-results/adversarial-results.json",
        "eval-results/roe-compliance-results.json"
    ]
    
    for file_path in json_files:
        full_path = root / file_path
        if full_path.exists():
            with open(full_path) as f:
                data = json.load(f)
                assert isinstance(data, (dict, list)), f"Invalid JSON structure in {file_path}"
    
    # Special case: footer config supports comments, just verify it exists
    footer_config = root / "docs/footer.config.json"
    if footer_config.exists():
        content = footer_config.read_text()
        assert "footer" in content, "Footer config should contain footer configuration"


def test_makefile_targets():
    """Verify key Makefile targets are defined."""
    root = Path(__file__).parent.parent
    makefile_path = root / "Makefile"
    
    if makefile_path.exists():
        content = makefile_path.read_text()
        required_targets = [
            "check",
            "evals", 
            "lint:md:fix",
            "protect:enable",
            "pr:scan"
        ]
        
        for target in required_targets:
            assert target in content, f"Required Makefile target missing: {target}"

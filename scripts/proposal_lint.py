#!/usr/bin/env python3
"""
Proposal linter for VaultMesh.

Validates:
- proposals/*.{yml,yaml,json,md} against docs/schemas/proposal.schema.json
- filename contains the proposal `id`
- id formatting (flexible, but encourages stable patterns)
- required fields & friendly error messages

Usage:
  python scripts/proposal_lint.py --schema docs/schemas/proposal.schema.json --strict
"""
import argparse
import json
import os
import re
import sys
from glob import glob


ID_PATTERNS = [
    r'(?:VM-)?P-\d{4}-\d{3}',     # e.g., P-2025-001 or VM-P-2025-001
    r'\d{4}-\d{2,4}[a-z0-9\-]*',  # e.g., 2025-001, 2025-001-something
]


def load_yaml_or_json(path):
    """Load YAML, JSON, or Markdown with frontmatter."""
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if path.endswith('.md'):
        # extract YAML front-matter if present
        if text.lstrip().startswith('---'):
            parts = text.split('---', 2)
            if len(parts) >= 3:
                import yaml  # lazy import
                return yaml.safe_load(parts[1]) or {}
        # else try JSON block fence ```json ... ```
        match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
        if match:
            return json.loads(match.group(1))
        return {}
    
    if path.endswith(('.yml', '.yaml')):
        import yaml
        return yaml.safe_load(text) or {}
    
    return json.loads(text)


def load_schema(schema_path):
    """Load JSON schema from file."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_schema(obj, schema):
    """Validate object against JSON schema."""
    from jsonschema import Draft202012Validator
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(obj), key=lambda e: e.path)
    return errors


def find_id(obj, default=''):
    """Extract proposal ID from object."""
    if isinstance(obj, dict):
        return (obj.get('id') or 
                obj.get('proposal_id') or 
                (obj.get('metadata') or {}).get('id') or 
                default)
    return default


def filename_contains_id(fname, pid):
    """Check if filename contains the proposal ID."""
    if not pid:
        return False
    base = os.path.basename(fname)
    return pid in base


def looks_like_id(pid):
    """Check if string matches expected ID patterns."""
    return any(re.fullmatch(p, pid or '', flags=re.I) for p in ID_PATTERNS)


def main():
    """Main proposal linter function."""
    parser = argparse.ArgumentParser(description="VaultMesh proposal linter")
    parser.add_argument('--schema', required=True, help="Path to proposal schema")
    parser.add_argument('--strict', action='store_true', help='Fail on warnings')
    args = parser.parse_args()

    # Find all proposal files
    files = sorted([
        *glob('proposals/*.yml'), 
        *glob('proposals/*.yaml'),
        *glob('proposals/*.json'), 
        *glob('proposals/*.md')
    ])

    if not files:
        print("No proposals found under proposals/. OK.")
        return 0

    # Load schema
    try:
        schema = load_schema(args.schema)
    except FileNotFoundError:
        print(f"❌ Schema file not found: {args.schema}")
        return 1
    except Exception as e:
        print(f"❌ Error loading schema: {e}")
        return 1

    failures = 0
    warnings = 0
    valid_proposals = []

    # Validate each proposal
    for filepath in files:
        try:
            obj = load_yaml_or_json(filepath)
        except Exception as e:
            print(f"❌ {filepath}: cannot parse ({e})")
            failures += 1
            continue

        pid = find_id(obj, '')
        errors = []
        
        # Check for ID presence and format
        if not pid:
            errors.append("missing `id`")
        else:
            if not filename_contains_id(filepath, pid):
                errors.append(f"filename does not contain id `{pid}`")
            if not looks_like_id(pid):
                warnings += 1
                print(f"⚠️ {filepath}: id `{pid}` is non-standard; "
                      f"recommend P-YYYY-NNN or YYYY-NNN")
        
        # Schema validation
        schema_errors = validate_schema(obj, schema)
        if schema_errors:
            for error in schema_errors:
                path = "$" + "".join([
                    f"[{repr(p)}]" if isinstance(p, int) else f".{p}" 
                    for p in error.path
                ])
                errors.append(f"{path}: {error.message}")

        # Report results
        if errors:
            failures += 1
            print(f"❌ {filepath}:")
            for error in errors:
                print(f"   - {error}")
        else:
            title = obj.get('title', '(untitled)')
            status = obj.get('status', '(no status)')
            valid_proposals.append((filepath, pid, title, status))

    # Summary of valid proposals
    if valid_proposals:
        print("\n✅ Valid proposals:")
        for filepath, pid, title, status in valid_proposals:
            print(f"  - {pid} · {title} · {status} ({filepath})")

    # Final result
    if failures or (warnings and args.strict):
        result = 'FAIL' if failures else 'WARN(strict)'
        print(f"\nResult: {result} — failures={failures} warnings={warnings}")
        return 1
    
    print(f"\nResult: PASS — failures={failures} warnings={warnings}")
    return 0


if __name__ == '__main__':
    sys.exit(main())


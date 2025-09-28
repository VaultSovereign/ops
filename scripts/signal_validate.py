#!/usr/bin/env python3
"""
Validate signals/*.json against docs/schemas/signal.schema.json (if present).
Accepts partial records; warns for missing weight/timestamp.
"""
import argparse
import json
import os
import sys
from glob import glob
from datetime import datetime, timezone


def load_schema(path):
    """Load JSON schema, return None if not found."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"❌ Error loading schema {path}: {e}")
        return None


def validate_against_schema(obj, schema):
    """Validate object against schema, return list of errors."""
    if not schema:
        return []
    
    try:
        from jsonschema import Draft202012Validator
        validator = Draft202012Validator(schema)
        return list(validator.iter_errors(obj))
    except ImportError:
        print("⚠️ jsonschema not available, skipping schema validation")
        return []


def main():
    """Main signals validator function."""
    parser = argparse.ArgumentParser(description="VaultMesh signals validator")
    parser.add_argument('--schema', default='docs/schemas/signal.schema.json',
                       help="Path to signal schema")
    args = parser.parse_args()

    # Load schema if available
    schema = load_schema(args.schema)
    if not schema:
        print(f"⚠️ Schema not found at {args.schema}, proceeding without validation")

    # Find signal files
    files = sorted(glob('signals/*.json'))
    if not files:
        print("No signals/*.json found. OK.")
        return 0

    failures = 0
    
    # Validate each signal file
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                obj = json.load(f)
        except Exception as e:
            print(f"❌ {filepath}: parse error: {e}")
            failures += 1
            continue

        # Schema validation
        errors = validate_against_schema(obj, schema)
        if errors:
            print(f"❌ {filepath}:")
            for error in errors:
                path = "$" + "".join([
                    f"[{repr(p)}]" if isinstance(p, int) else f".{p}" 
                    for p in error.path
                ])
                print(f"   - {path}: {error.message}")
            failures += 1
        else:
            # Show valid signal info
            signal_id = obj.get('id') or '(no id)'
            weight = obj.get('weight', 1)
            timestamp = obj.get('timestamp') or '(no timestamp)'
            print(f"✅ {filepath}: id={signal_id} weight={weight} ts={timestamp}")

    # Final result
    result = "FAIL" if failures else "PASS"
    print(f"\nResult: {result}")
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())


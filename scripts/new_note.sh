#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<USAGE
Usage: $(basename "$0") <prompt|runbook|persona> "Title" [Subfolder]
Creates a new note from the corresponding template and drops it in the right folder.
USAGE
  exit 1
}

if [ $# -lt 2 ]; then
  usage
fi

TYPE=$1
TITLE=$2
SUBDIR=${3:-}
TODAY=$(date +%F)

case $TYPE in
  prompt)
    TEMPLATE="Templates/Prompt Template.md"
    BASE_DIR="Prompts"
    DEFAULT_SUBDIR="Workflows"
    PLACEHOLDER="title: Prompt Name"
    ;;
  runbook)
    TEMPLATE="Templates/Runbook Template.md"
    BASE_DIR="Runbooks"
    DEFAULT_SUBDIR="Operations"
    PLACEHOLDER="title: Runbook Name"
    ;;
  persona)
    TEMPLATE="Templates/Persona Template.md"
    BASE_DIR="Prompts"
    DEFAULT_SUBDIR="Personas"
    PLACEHOLDER="title: Persona Name"
    ;;
  *)
    echo "Unknown type: $TYPE" >&2
    usage
    ;;
esac

TARGET_DIR="$BASE_DIR/${SUBDIR:-$DEFAULT_SUBDIR}"
mkdir -p "$TARGET_DIR"

NOTE_PATH="$TARGET_DIR/$TITLE.md"

if [ -e "$NOTE_PATH" ]; then
  echo "Note already exists: $NOTE_PATH" >&2
  exit 1
fi

if [ ! -f "$TEMPLATE" ]; then
  echo "Missing template: $TEMPLATE" >&2
  exit 1
fi

python3 - "$TEMPLATE" "$NOTE_PATH" "$PLACEHOLDER" "$TITLE" "$TODAY" <<'PY'
import sys
from pathlib import Path

template_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
placeholder = sys.argv[3]
title = sys.argv[4]
date = sys.argv[5]

content = template_path.read_text()
content = content.replace(placeholder, f"title: {title}", 1)
content = content.replace("created: {{date:YYYY-MM-DD}}", f"created: {date}", 1)
content = content.replace("updated: {{date:YYYY-MM-DD}}", f"updated: {date}", 1)
output_path.write_text(content)
PY

echo "Created $NOTE_PATH"

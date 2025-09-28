"""Simple registry that reads MCP tool metadata from tools/index.json."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


TOOLS_PATH = Path("tools/index.json")


class ToolRegistry:
    """Loads tool definitions used by the ops MCP server."""

    def __init__(self) -> None:
        self._tools: List[Dict[str, Any]] = []
        self.reload()

    def reload(self) -> None:
        """Reload tool metadata from tools/index.json when available."""

        if not TOOLS_PATH.exists():
            self._tools = []
            return
        try:
            raw = json.loads(TOOLS_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            self._tools = []
            return

        # Prefer dedicated mcp_tools section; fall back to legacy shape if needed.
        tools = raw.get("mcp_tools") or raw.get("tools") or []
        normalized: List[Dict[str, Any]] = []
        for entry in tools:
            if not isinstance(entry, dict):
                continue
            if "name" not in entry and "id" in entry:
                entry = dict(entry)
                entry["name"] = entry["id"]
            if "command" not in entry:
                # skip legacy entries without command metadata
                continue
            normalized.append(entry)
        self._tools = normalized

    def list_tools(self) -> List[Dict[str, Any]]:
        return list(self._tools)

    def find(self, name: str) -> Optional[Dict[str, Any]]:
        for tool in self._tools:
            if tool.get("name") == name:
                return tool
        return None


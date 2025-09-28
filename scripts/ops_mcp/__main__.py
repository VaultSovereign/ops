"""Minimal stdio loop to expose repo automation as MCP-style tools."""

from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
from typing import Any, Dict

from jsonschema import ValidationError
from jsonschema import validate as js_validate

from .tool_registry import ToolRegistry


REGISTRY = ToolRegistry()


def _respond(msg_id: Any, *, result: Any = None, error: Dict[str, Any] | None = None) -> None:
    payload: Dict[str, Any] = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        payload["error"] = error
    else:
        payload["result"] = result
    sys.stdout.write(json.dumps(payload) + "\n")
    sys.stdout.flush()


def _capabilities() -> Dict[str, Any]:
    return {
        "server": "ops_mcp",
        "version": "0.1.0",
        "tools": REGISTRY.list_tools(),
    }


def _call_tool(name: str, arguments: Dict[str, Any] | None) -> Dict[str, Any]:
    tool = REGISTRY.find(name)
    if not tool:
        return {"ok": False, "error": f"Unknown tool: {name}"}

    command = tool.get("command")
    if not command:
        return {"ok": False, "error": f"Tool missing command: {name}"}

    args = arguments or {}
    schema = (tool.get("parameters") or {}).get("schema")
    if schema is not None:
        try:
            js_validate(instance=args, schema=schema)
        except ValidationError as exc:
            return {"ok": False, "error": f"Argument validation failed: {exc.message}"}

    env = None
    env_map = tool.get("env_map") or {}
    cli_args: Dict[str, Any] = {}
    for key, val in args.items():
        if key in env_map:
            if env is None:
                env = os.environ.copy()
            env[env_map[key]] = str(val)
        else:
            cli_args[key] = val

    extra = " ".join(f"--{key} {shlex.quote(str(val))}" for key, val in cli_args.items())
    full_command = f"{command} {extra}".strip()

    try:
        output = subprocess.check_output(
            full_command,
            shell=True,
            cwd=".",
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
        )
        return {"ok": True, "output": output}
    except subprocess.CalledProcessError as exc:  # pragma: no cover - interactive surface
        return {"ok": False, "code": exc.returncode, "output": exc.output}


def run() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                request = json.loads(line)
            except json.JSONDecodeError as err:
                _respond(None, error={"code": -32700, "message": f"Parse error: {err}"})
                continue

            message_id = request.get("id")
            method = request.get("method")
            params = request.get("params") or {}

            if method == "initialize":
                REGISTRY.reload()
                _respond(message_id, result=_capabilities())
            elif method == "list_tools":
                _respond(message_id, result=REGISTRY.list_tools())
            elif method == "call_tool":
                tool_name = params.get("name")
                result = _call_tool(tool_name, params.get("arguments"))
                _respond(message_id, result=result)
            else:
                _respond(message_id, error={"code": -32601, "message": f"Unknown method: {method}"})
    else:
        print("ops_mcp ready. Launch with 'python -m scripts.ops_mcp --stdio' for stdio mode.")


if __name__ == "__main__":
    run()

"""Ops MCP server bootstrap."""


def run_stdio() -> None:
    """Entry point used by scripts invoking the server via stdio."""

    from .__main__ import run

    run()


__all__ = ["run_stdio"]

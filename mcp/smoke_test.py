#!/usr/bin/env python3
"""Smoke test the profile MCP server through its stdio JSON-RPC interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


SERVER = Path(__file__).with_name("profile_server.py")


def request(proc: subprocess.Popen[str], message_id: int, method: str, params: dict[str, Any] | None = None) -> Any:
    assert proc.stdin is not None
    assert proc.stdout is not None

    message: dict[str, Any] = {"jsonrpc": "2.0", "id": message_id, "method": method}
    if params is not None:
        message["params"] = params

    proc.stdin.write(json.dumps(message) + "\n")
    proc.stdin.flush()

    line = proc.stdout.readline()
    if not line:
        raise RuntimeError(f"No response for {method}")

    response = json.loads(line)
    if "error" in response:
        raise RuntimeError(f"{method} failed: {response['error']}")
    return response["result"]


def notify(proc: subprocess.Popen[str], method: str) -> None:
    assert proc.stdin is not None
    proc.stdin.write(json.dumps({"jsonrpc": "2.0", "method": method}) + "\n")
    proc.stdin.flush()


def main() -> int:
    proc = subprocess.Popen(
        [sys.executable, str(SERVER)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        init = request(proc, 1, "initialize", {"protocolVersion": "2025-11-25"})
        assert init["serverInfo"]["name"] == "dragutin-profile"
        notify(proc, "notifications/initialized")

        resources = request(proc, 2, "resources/list")["resources"]
        uris = {item["uri"] for item in resources}
        assert "dragutin://profile/summary" in uris
        assert "dragutin://profile/homepage" in uris
        assert "dragutin://profile/pokedex" in uris

        templates = request(proc, 3, "resources/templates/list")["resourceTemplates"]
        assert templates == []

        summary = request(proc, 4, "resources/read", {"uri": "dragutin://profile/summary"})
        assert "Dragutin Oreški" in summary["contents"][0]["text"]

        prompts = request(proc, 5, "prompts/list")["prompts"]
        assert prompts[0]["name"] == "answer_profile_question"

        prompt = request(
            proc,
            6,
            "prompts/get",
            {
                "name": "answer_profile_question",
                "arguments": {"question": "What is Dragutin doing now?"},
            },
        )
        assert prompt["messages"][0]["role"] == "user"

        tools = request(proc, 7, "tools/list")["tools"]
        assert tools == []

        print("MCP smoke test passed")
        return 0
    finally:
        if proc.stdin:
            proc.stdin.close()
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())

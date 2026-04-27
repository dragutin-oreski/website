#!/usr/bin/env python3
"""Read-only MCP stdio server for Dragutin Oreški's public profile context."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_VERSION = "2025-11-25"


RESOURCE_FILES = {
    "dragutin://profile/llms": {
        "path": ROOT / "llms.txt",
        "name": "llms",
        "title": "LLMs.txt",
        "description": "Curated agent-readable overview of Dragutin Oreški's public website.",
        "mimeType": "text/markdown",
    },
    "dragutin://profile/homepage": {
        "path": ROOT / "index.html.md",
        "name": "homepage-markdown",
        "title": "Homepage Markdown",
        "description": "LLM-readable Markdown mirror of the homepage/profile.",
        "mimeType": "text/markdown",
    },
    "dragutin://profile/pokedex": {
        "path": ROOT / "side-projects" / "pokedex" / "index.html.md",
        "name": "pokedex-markdown",
        "title": "Pokedex Markdown",
        "description": "LLM-readable Markdown mirror of the Pokedex side project.",
        "mimeType": "text/markdown",
    },
    "dragutin://profile/sitemap": {
        "path": ROOT / "sitemap.xml",
        "name": "sitemap",
        "title": "Sitemap",
        "description": "XML sitemap for the public website.",
        "mimeType": "application/xml",
    },
    "dragutin://profile/robots": {
        "path": ROOT / "robots.txt",
        "name": "robots",
        "title": "Robots.txt",
        "description": "Crawler policy and sitemap pointer.",
        "mimeType": "text/plain",
    },
}


SUMMARY = """# Dragutin Oreški

Dragutin Oreški is an AI Engineer based in Zagreb. His public site focuses on data-driven AI systems, private/local agents, RAG, multi-agent workflows, evaluation, observability, and practical AI learning materials.

Current public context:

- Lead AI Engineer at QED Code since December 2024.
- Lecturer at Algebra Bernays in April 2026 for a 60-hour course on AI benefits and risks.
- Creator of UI Suputnik, a Croatian-language course companion for introductory AI concepts.
- Builder of the Pokedex side project, a handheld Raspberry Pi object-recognition device.

Public links:

- Homepage: https://dragutinoreski.com/
- LLMs.txt: https://dragutinoreski.com/llms.txt
- UI Suputnik: https://dragutinoreski.com/courses/ui-suputnik/
- Pokedex: https://dragutinoreski.com/side-projects/pokedex/
- GitHub: https://github.com/dragutin-oreski
- LinkedIn: https://www.linkedin.com/in/dragutinoreski
- Email: mailto:dragutin.oreski@gmail.com
"""


def respond(message_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def error(message_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "error": {"code": code, "message": message}}


def list_resources() -> dict[str, Any]:
    resources = [
        {
            "uri": "dragutin://profile/summary",
            "name": "profile-summary",
            "title": "Profile Summary",
            "description": "Short public profile summary for Dragutin Oreški.",
            "mimeType": "text/markdown",
        }
    ]
    for uri, metadata in RESOURCE_FILES.items():
        resources.append(
            {
                "uri": uri,
                "name": metadata["name"],
                "title": metadata["title"],
                "description": metadata["description"],
                "mimeType": metadata["mimeType"],
            }
        )
    return {"resources": resources}


def read_resource(uri: str) -> dict[str, Any]:
    if uri == "dragutin://profile/summary":
        return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": SUMMARY}]}

    metadata = RESOURCE_FILES.get(uri)
    if not metadata:
        raise KeyError(f"Unknown resource URI: {uri}")

    path = metadata["path"]
    text = path.read_text(encoding="utf-8")
    return {"contents": [{"uri": uri, "mimeType": metadata["mimeType"], "text": text}]}


def list_prompts() -> dict[str, Any]:
    return {
        "prompts": [
            {
                "name": "answer_profile_question",
                "title": "Answer Profile Question",
                "description": "Answer questions about Dragutin Oreški using only public website resources.",
                "arguments": [
                    {
                        "name": "question",
                        "description": "The profile, work, project, or contact question to answer.",
                        "required": True,
                    }
                ],
            }
        ]
    }


def get_prompt(params: dict[str, Any] | None) -> dict[str, Any]:
    arguments = (params or {}).get("arguments", {})
    question = arguments.get("question", "Summarize Dragutin Oreški's public profile.")
    text = (
        "Use the dragutin://profile resources to answer the question. "
        "Stay grounded in public site content. Do not infer private client details or unstated credentials.\n\n"
        f"Question: {question}"
    )
    return {
        "description": "Grounded public-profile question answering prompt.",
        "messages": [{"role": "user", "content": {"type": "text", "text": text}}],
    }


def handle(message: dict[str, Any]) -> dict[str, Any] | None:
    message_id = message.get("id")
    method = message.get("method")
    params = message.get("params") or {}

    if method == "notifications/initialized":
        return None
    if method == "initialize":
        return respond(
            message_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"resources": {}, "prompts": {}, "tools": {}},
                "serverInfo": {"name": "dragutin-profile", "version": "0.1.0"},
            },
        )
    if method == "ping":
        return respond(message_id, {})
    if method == "resources/list":
        return respond(message_id, list_resources())
    if method == "resources/read":
        try:
            return respond(message_id, read_resource(params["uri"]))
        except KeyError as exc:
            return error(message_id, -32602, str(exc))
    if method == "prompts/list":
        return respond(message_id, list_prompts())
    if method == "prompts/get":
        if params.get("name") != "answer_profile_question":
            return error(message_id, -32602, f"Unknown prompt: {params.get('name')}")
        return respond(message_id, get_prompt(params))
    if method == "tools/list":
        return respond(message_id, {"tools": []})

    return error(message_id, -32601, f"Method not found: {method}")


def main() -> int:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
            response = handle(message)
        except Exception as exc:  # Keep protocol errors visible to clients.
            response = error(None, -32603, str(exc))
        if response is not None:
            print(json.dumps(response, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

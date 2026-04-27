# Dragutin Profile MCP Server

This directory contains a small read-only MCP stdio server for Dragutin Oreški's public profile/site context.

It is intended for local agent clients that support MCP, such as Claude Desktop, Claude Code, Cursor, or other MCP-compatible tools.

## What It Exposes

- Public profile summary.
- `llms.txt`.
- Homepage Markdown mirror.
- Pokedex Markdown mirror.
- `sitemap.xml`.
- `robots.txt`.

It exposes resources and one prompt. It does not expose tools and cannot mutate files or call external APIs.

## Local Usage

Configure your MCP client to run:

```json
{
  "mcpServers": {
    "dragutin-profile": {
      "command": "python3",
      "args": ["/path/to/website/mcp/profile_server.py"]
    }
  }
}
```

Replace `/path/to/website` with the absolute path to this repository checkout.

## Remote MCP Note

This website is deployed with GitHub Pages. GitHub Pages can serve static files, but it cannot run the bidirectional JSON-RPC server required for a remote MCP endpoint.

To make this available as a remote MCP server, deploy an HTTP version of this server to a runtime such as Cloudflare Workers, Fly.io, Render, or another server host, then publish or document the remote endpoint.

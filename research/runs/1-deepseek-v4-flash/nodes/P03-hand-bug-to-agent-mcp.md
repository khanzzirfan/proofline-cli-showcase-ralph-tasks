---
id: P03
title: "People want to hand a captured bug straight to an agent, usually over MCP"
who: developers, QA
tools: [Claude Code, Cursor, Windsurf, BugDump, FlowLens, TraceBug, openjam]
status: verified
---
## Pain
Capturing the bug is not the end; the report must reach the agent. Users want one link or
action that hands a full browser report (console, network, replay, recording) to Claude Code,
Cursor or Windsurf so the agent can start fixing. Today that hand-off is manual or needs a
local server, and most tools that do it are cloud SaaS.

## Evidence
- https://news.ycombinator.com/item?id=46047931 (hn, 2025-11-25, verified): "Show HN: A better way to handoff web bugs to AI agents" pointing at github.com/magentic/flowlens-mcp-server — 5 points.
- https://bugdump.com/blog/ai-agent-screen-recording-frames-mcp (blog, verified): the widget "already returns a signed link to the recording" and ships a `get_recording_frames` MCP tool so "Claude read it over MCP".
- https://tracebug.dev/blog/jam-dev-alternatives (blog/vendor, 2026-07-30, verified): "the bug report's most important reader in 2026 often isn't a human … TraceBug ships a local MCP server (`npx tracebug mcp`) so Claude Code, Cursor, or Windsurf can read the full report". Vendor, so weak.
- https://github.com/search?q=bug+report+mcp+agent&type=repositories (repo discovery, verified via GitHub API): several small projects do this — `UseVynix/vynix-mcp` (10★), `chriswu727/argus` (7★), `BugTraceAI/BugTraceAI-CLI` (183★).

## How users want it fixed
- One link or one command that opens the captured report in the agent over MCP (FlowLens, TraceBug, Faylee).
- Local-first so answers do not leave the machine.

## Workarounds people use today
- Export a ZIP, unzip, paste `report.md`; or run a third-party MCP server.

## Session Recorder angle
Session Recorder files issues/exports a ZIP but has no agent hand-off or MCP server. A local MCP
server is too big and a security risk (see P05), so the small version is the clipboard copy in P02.
Repos like openjam/pointa show rivals already ship agent hand-off. No open PR overlaps.

## Scores
frequency: 4  severity: 3  fit: 4  smallness: 3  novelty: 3

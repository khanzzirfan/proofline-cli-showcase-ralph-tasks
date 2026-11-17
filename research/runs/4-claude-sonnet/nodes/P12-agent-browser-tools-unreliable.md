---
id: P12
title: "The agent's built-in browser tool says it is connected, then isn't there"
who: developers
tools: [Cursor, Codex, Claude in Chrome, Roo Code]
status: verified
---
## Pain
Even the tools meant to give agents a browser fail often: tools missing from the toolset, "browser host unavailable", extension not connecting, console tool returning unreadable data. Users lose the visual loop and go back to manual pasting.
## Evidence
- https://github.com/openai/codex/issues/57641 (github-issue, 2026-10-28, verified, from listing): CLI @Browser fails with "The browser access host is unavailable". 42 reactions, 53 comments.
- https://github.com/openai/codex/issues/39136 (github-issue, 2026-08-18, verified, from listing): built-in browser plugin initialization fails. 44 reactions, 82 comments.
- https://github.com/anthropics/claude-code/issues/20298 (github-issue, 2026-01-23, verified, from listing): Claude in Chrome extension not connecting to the CLI. 41 reactions, 51 comments.
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (forum, 2026-02-20, verified): console and network tools return "Unsupported content type metadata". 260 views.
## How users want it fixed
- Fix the tools (vendor bugs); staff call it a known regression.
## Workarounds people use today
- Reinstall, switch to Playwright MCP, paste manually.
## Session Recorder angle
Supports the case for a recorder that does not depend on the agent's browser: a file/clipboard hand-off works on any agent. Nothing to build for this pain directly.
## Scores
frequency: 5  severity: 3  fit: 2  smallness: 1  novelty: 3

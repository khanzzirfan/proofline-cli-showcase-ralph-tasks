---
id: P05
title: “The browser tool is configured, but the agent still can’t use it”
who: developers, agent users
tools: [Claude Code Chrome MCP, Cursor Browser Automation]
status: partly-verified
---
## Pain
Browser integration can fail at the connection or tool-availability layer, even when the extension is installed or browser automation appears enabled. Users then repeat setup, restart tools, or downgrade versions before they can provide browser context.
## Evidence
- https://github.com/anthropics/claude-code/issues/21371 (github-issue, 2026-01-28, verified): `tabs_context_mcp` repeatedly reports the extension is not connected despite installation; 79 reactions, 40 comments; closed as duplicate of connection issues.
- https://forum.cursor.com/t/agent-can-t-access-browser-automation-tools-navigate-click-screenshot-even-though-browser-capabilities-page-lists-them-and-browser-automation-is-connected/148651 (forum, date unknown, unverified): web fetch returned the page title only; the report body and claimed symptom could not be checked.
- https://forum.cursor.com/t/browser-screenshot-tool-now-missing/145855 (forum, date unknown, unverified): web fetch returned the page title only; the reported missing screenshot capability could not be checked.
## How users want it fixed
- Make browser connection and listed tool availability work consistently; the issue report’s expected behavior is available tab information: https://github.com/anthropics/claude-code/issues/21371.
## Workarounds people use today
- Restart Chrome, reinstall/toggle the extension, rerun the connection command, or downgrade the CLI; multiple attempts and downgrading are documented in #21371.
## Session Recorder angle
A portable ZIP avoids reliance on live browser MCP setup, and a one-click agent handoff might reduce integration fragility. Avoid implementing an MCP server as an assumed small change; no overlap with current open PRs identified.
## Scores
frequency: 3  severity: 3  fit: 4  smallness: 4  novelty: 4

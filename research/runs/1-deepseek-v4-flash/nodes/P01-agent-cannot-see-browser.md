---
id: P01
title: "My agent can't see the browser: it can't read the console, network tab or live DOM"
who: developers
tools: [Cursor, Claude Code, Chrome DevTools MCP, Copilot agent mode]
status: partly-verified
---
## Pain
Coding agents edit code but cannot observe what the running app does. Developers want the
agent to read the live browser console, network requests and DOM so it can debug frontend
bugs instead of guessing. Cursor's in-IDE browser exposes the data but the agent cannot
consume it; Claude Code has no way to see a running app at all.

## Evidence
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "Today the workarounds are screenshots, paste, WebFetch (no auth, no JS), or driving headless Playwright via Bash" — 76 reactions, +1:55, 7 comments.
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): requests "browser view / browser tools in Claude Code cloud sessions" — 8 reactions, +1:8, 3 comments, now closed.
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): "Add browser rendering / DOM inspection capability to Claude Code" — 1 reaction, 5 comments, closed.
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (forum, unverified: title loads, body JS-rendered so quote is from the search snippet): browser_console_messages "return a response in an unprocessable format".
- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 (forum, unverified: title loads, body JS-rendered): "I asked agent to inspect network requests, it made a few attempts and concluded that it cant access network requests."
- https://developer.chrome.com/blog/devtools-for-agents-v1 (vendor-doc, 2026-05-19, verified): "They can generate a complex web app, but they cannot observe its behavior or inspect its output in a live browser." Weak vendor evidence, but it is the Chrome team stating the gap and shipping a fix.

## How users want it fixed
- Give the agent a read path into the browser the user already has open (shared tab), with
  user control over what is shared — claude-code#57034 asks to reuse VS Code's browser-sharing API.
- Structured console + network tools rather than raw unsupported payloads — cursor forum threads above.

## Workarounds people use today
- Screenshots and paste; WebFetch (no auth, no JS); headless Playwright driven over Bash (claude-code#57034).
- Chrome DevTools MCP / Cursor "Browser Tab" mode (forum thread: "enabling Chrome DevTools MCP seems to help").

## Session Recorder angle
Session Recorder already captures console, exceptions and network from a real tab and writes them into
`report.md`. That is exactly the evidence the agent cannot otherwise get. The extension cannot stream
live into the agent, but it can hand over the captured console/network on the clipboard or in the ZIP.
No open PR overlaps directly (this node is about handing over evidence, not capturing it).

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 4  novelty: 3

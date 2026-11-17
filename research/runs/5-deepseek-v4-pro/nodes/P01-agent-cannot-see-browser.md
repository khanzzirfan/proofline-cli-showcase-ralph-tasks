---
id: P01
title: The agent can't see the browser (console, network, DOM), so it guesses at frontend bugs
who: developers
tools: [Claude Code, Cursor, Copilot coding agent, Codex]
status: verified
---
## Pain
Coding agents read source files but cannot see the page a user actually runs: no rendered DOM, no console errors, no network requests, no UI state. For frontend and browser bugs the agent therefore guesses, changes a line, and claims success without ever looking at the result. This is the most frequently repeated complaint across agent issue trackers and blogs.

## Evidence
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "no way for Claude to see a running app the user has open... workarounds are screenshots, paste, WebFetch (no auth, no JS), or driving headless Playwright via Bash" — 76 reactions, 7 comments
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): "Claude Code currently has no built-in way to render HTML/JS output in a real browser, inspect the resulting DOM, or verify visual output" — 1 reaction
- https://reposquare.com/claude-code-browser-access/ (blog, 2026-10-31, verified): "Claude Code fixed a broken page fully 3 times out of 10 without one, and 9 out of 9 with a browser."
- https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc (blog, verified): "When Claude Code or Cursor fixes a front-end bug, it is usually guessing. It reads your source, but it cannot see the page."

## How users want it fixed
- A browser tool/MCP so the agent can render, click, read console and network, and screenshot: https://github.com/anthropics/claude-code/issues/52907
- VS Code browser-sharing so Claude can validate web UI changes in one turn: https://github.com/anthropics/claude-code/issues/57034

## Workarounds people use today
- Screenshot and paste; WebFetch; headless Playwright via Bash; Chrome DevTools MCP; Claude in Chrome (`claude --chrome`).

## Session Recorder angle
Session Recorder already captures console, exceptions, network, clicks, screenshots and the rendered page — exactly the context the agent is missing. The gap is handing that recorded context to the agent, not capturing it. Open PRs #29 (browser/OS/viewport) and #32 (HAR export) touch adjacent data; no PR turns the full recorded session into agent-consumable context.

## Scores
frequency: 5  severity: 4  fit: 4  smallness: 3  novelty: 2

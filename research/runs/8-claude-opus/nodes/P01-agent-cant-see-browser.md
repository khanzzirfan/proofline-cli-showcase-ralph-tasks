---
id: P01
title: "My coding agent can't see the running app: no page, console or network"
who: developers, agent users
tools: [Claude Code, Cursor, Copilot agent mode, chrome-devtools-mcp]
status: verified
---
## Pain
Coding agents read source code but not the page the user is looking at. For front-end bugs they guess, because they cannot see the rendered UI, console errors or network calls. Built-in browser tools exist (Cursor browser, Claude in Chrome) but break often, and cloud sessions have no browser at all.
## Evidence
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "There's no way for Claude to see a running app the user has open, even when the user wants to share it." 76 reactions, 7 comments
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "I end up reviewing the PR blind or pulling the branch locally, which defeats the point of delegating." 8 reactions, 3 comments
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): "Claude itself remains blind to what it just produced, which breaks the feedback loop on every iteration." 1 reaction, 5 comments
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (forum, 2026-02-20, verified): "they return a response in an unprocessable format (Unsupported content type “metadata”)" 4 posts, 260 views; staff confirmed bug
- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 (forum, 2026-02-08, verified): "it made a few attempts and concluded that it cant access network requests." 3 likes, 177 views
- https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc (blog, verified): "it is usually guessing. It reads your source, but it cannot see the page, the console errors or the network calls."
- https://news.ycombinator.com/item?id=47390817 (hn, 2026-03-15, verified): "Chrome DevTools MCP (2025)" story; 604 points, 234 comments (demand signal)
## How users want it fixed
- Let the agent read tabs the user explicitly shares: DOM, screenshots, console, navigation (https://github.com/anthropics/claude-code/issues/57034).
- Browser tools in cloud sessions so the agent can confirm a fix (https://github.com/anthropics/claude-code/issues/75632).
## Workarounds people use today
- chrome-devtools-mcp, Playwright MCP, Claude in Chrome; screenshots and paste; headless Playwright via Bash (listed in #57034).
## Session Recorder angle
Session Recorder captures exactly this context (console, network, screenshots, DOM-anchored clicks) from the user's real browser and writes it into `report.md`. It does not give the agent live access (out of scope in PLAN.md). Its value is a frozen, complete snapshot handed over once. No open PR targets the hand-off itself.
## Scores
frequency: 5  severity: 4  fit: 4  smallness: 2  novelty: 2

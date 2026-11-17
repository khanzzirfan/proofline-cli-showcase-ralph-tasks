---
id: P13
title: "The agent's browser isn't logged in, so it can't reach the bug"
who: developers
tools: [chrome-devtools-mcp, Playwright MCP, Claude Code WebFetch]
status: verified
---
## Pain
Bugs live behind login, feature flags and real data. Agent-driven browsers start as fresh profiles, so users fight with cookies, storage state and remote debugging to reuse their session, and worry about giving the agent their real account.
## Evidence
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/140 (github-issue, 2025-09-25, verified): "I want to be able to connect to an existing Chrome session in an opened browser with zero configuration work." 61 reactions, 29 comments
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/825 (github-issue, 2026-01-24, verified via API): "Feature request: Allow persisting remote debugging permission approval" (title) 32 reactions, 21 comments
- https://github.com/microsoft/playwright-mcp/issues/403 (github-issue, 2025-05-12, verified via API): "Support to attach cookies to browser context" (title) 5 reactions
- https://github.com/microsoft/playwright-mcp/issues/1388 (github-issue, 2026-02-10, verified via API): "--storage-state flag does not apply cookies to browser context" (title) 2 reactions, 5 comments
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, verified): "screenshots, paste, WebFetch (no auth, no JS), or driving headless Playwright via Bash"
- https://news.ycombinator.com/item?id=46130602 (hn, 2025-12-03, verified via Algolia): "I Solved Chrome DevTools MCP's Authentication Gap" 5 points, 2 comments
## How users want it fixed
- Attach to the user's open, logged-in Chrome with one confirmation (#140).
## Workarounds people use today
- Dedicated Chrome profile (https://news.ycombinator.com/item?id=47391195), storage-state files, playwriter extension.
## Session Recorder angle
Not in section 5. A built-in strength: the recorder runs in the user's real, logged-in browser, so it captures bugs the agent's browser cannot reach. Storage capture is #41 (open). Little to add beyond saying "session was authenticated as role X" in the report.
## Scores
frequency: 3  severity: 3  fit: 3  smallness: 3  novelty: 1

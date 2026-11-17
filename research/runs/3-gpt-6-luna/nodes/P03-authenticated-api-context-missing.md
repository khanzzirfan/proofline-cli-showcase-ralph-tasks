---
id: P03
title: “The agent invents API behavior because my browser session is elsewhere”
who: developers
tools: [Claude Code, Cursor, Chrome DevTools MCP, Playwright MCP]
status: verified
---
## Pain
An agent operating in a terminal may not have the user’s authenticated browser session or the actual requests/responses from it. It may guess response shapes or receive 401 errors, forcing a separate context transfer or login setup.
## Evidence
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 (blog, date unknown, verified): “It read the frontend source, found the URLs, and invented the response shapes. Then it tried `curl` from the terminal and got a 401” (first-person, promotional tool comparison).
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): says WebFetch cannot reach authenticated internal tools and proposes reusing the running browser session (1 reaction).
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): identifies unauthenticated WebFetch/headless-browser limitations as workarounds (8 reactions, 9 comments).
## How users want it fixed
- Provide controlled access to the existing authenticated browser or recorded traffic: https://github.com/anthropics/claude-code/issues/52907.
- Let the agent inspect recorded request/response evidence: https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705.
## Workarounds people use today
- Copy a cURL request and response after removing sensitive headers.
- Configure browser MCP or use a local MCP to query previously recorded traffic.
## Session Recorder angle
Captured network evidence is already exported; ensure ZIP handoff clearly preserves it and names referenced request bodies. Open PR #43 covers Copy as cURL and #32 HAR export; avoid those specific implementations.
## Scores
frequency: 3  severity: 4  fit: 5  smallness: 4  novelty: 3

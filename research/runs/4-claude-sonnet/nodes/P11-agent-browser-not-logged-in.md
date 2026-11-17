---
id: P11
title: "The agent's browser isn't my logged-in session, so it can't reach the buggy page"
who: developers
tools: [Chrome DevTools MCP, Playwright MCP, Claude Code]
status: verified
---
## Pain
Bugs live behind a login, with real data and cookies. Agent-controlled browsers start clean, so the agent cannot get to the broken state. Attaching to the user's real Chrome needs flags, prompts or fails.
## Evidence
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/140 (github-issue, 2025-09-25, verified): wants to "connect to an existing Chrome session in an opened browser with zero configuration work". 61 reactions (58 +1), 29 comments.
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/825 (github-issue, 2026-01-24, verified, from listing): allow persisting the remote debugging permission approval. 32 reactions, 21 comments.
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): workarounds today include "WebFetch (no auth, no JS)". 76 reactions.
- https://github.com/microsoft/playwright-mcp/issues/403 (github-issue, 2025-05-12, verified, from listing): attach cookies to the browser context. 5 reactions.
## How users want it fixed
- Connect to the user's existing session with one consent prompt (cdt#140).
## Workarounds people use today
- Debug port flags; saved auth state files; copy cookies by hand (risky).
## Session Recorder angle
A recording already comes from the user's real, logged-in tab, so the agent does not need auth to see the bug. Note for the report: say which user state (role, feature flags) was active. Open PR #41 (storage snapshot) and #29 (env) overlap. Low novelty.
## Scores
frequency: 4  severity: 3  fit: 3  smallness: 2  novelty: 1

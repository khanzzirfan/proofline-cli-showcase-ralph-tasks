---
id: P07
title: “A code change or passing test doesn’t show me the UI fix worked”
who: developers, QA, product
tools: [Claude Code, Cursor, coding agents]
status: verified
---
## Pain
A frontend fix needs evidence from the rendered page, but users report being left to inspect it manually or review a PR “blind.” UI state, layout and browser errors are not proven by an edit alone.
## Evidence
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): describes “manual loop” of switching browser, eyeballing, screenshotting and describing the problem again (1 reaction).
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): asks for edit/reload/verify iteration with browser state; 76 reactions, 7 comments.
- https://news.ycombinator.com/item?id=45293848 (hn, 2025-09-18, verified): commenter says a crawler cannot infer expected behavior without specific assertions and acceptance criteria (2 points, 2 comments).
## How users want it fixed
- Let the agent inspect and verify the actual rendered app after changes: https://github.com/anthropics/claude-code/issues/57034.
- Include checks grounded in intended behavior, rather than treating all clickable paths as success criteria: https://news.ycombinator.com/item?id=45293848.
## Workarounds people use today
- Run the app and inspect it manually, use Playwright/browser MCP, or write explicit assertions.
## Session Recorder angle
The extension can show captured before/after evidence and timeline, but cannot verify a later code fix automatically. A lightweight report handoff can instruct the agent to use the captured failure as a validation target. No open extension PR directly overlaps.
## Scores
frequency: 4  severity: 4  fit: 4  smallness: 4  novelty: 4

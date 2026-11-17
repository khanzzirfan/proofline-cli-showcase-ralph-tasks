---
id: P03
title: "I found the bug, now give my agent the exact context in one step"
who: developers, QA
tools: [Claude Code, Cursor, Codex, opencode, MCP]
status: verified
---
## Pain
People who already found the bug want to hand the agent the exact evidence, not make it reproduce from nothing. Today every step is manual: export, unzip, paste, add a prompt. Several small tools appeared in 2025-2026 just to remove this step, which shows demand.
## Evidence
- https://news.ycombinator.com/item?id=46047931 (hn, 2025-11-25, verified): FlowLens author: "What I actually want is a way to hand the agent the exact context I just saw." 5 points, 2 comments (vendor, weak).
- https://news.ycombinator.com/item?id=48795580 (hn, 2026-07-05, verified): Show HN Heckle, "Send a bug's full browser context to your coding agent". 6 points, 3 comments.
- https://www.producthunt.com/products/flowlens-ai-native-bug-reports (product-hunt, 2025, unverified on re-check: HTTP 403, vendor): "No more praying your agent can reproduce an issue, or dumping console logs and screenshots into chat." 132 upvotes.
- https://www.producthunt.com/products/markupr (product-hunt, 2026, unverified on re-check: HTTP 403, vendor): "AI coding agents are blind. When you find a bug, you context-switch into writing mode" 3 upvotes.
- https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj (review/listing, 2026-11-10, verified, vendor copy): "No more screenshot, switch apps, find the file, drag it in and explain it all again." 6 users.
## How users want it fixed
- One link or one paste (MCP or clipboard) with a built-in prompt; local-first (FlowLens PH: "everything runs locally").
## Workarounds people use today
- Export a ZIP, unzip, paste report, write a prompt each time; Jam MCP, FlowLens, Heckle.
## Session Recorder angle
Best fit. The extension only copies issue Markdown (`copyIssue`); docs/report-format.md has a "Suggested prompt" that the user must copy by hand. A "Copy for coding agent" action (prompt + trimmed report.md on the clipboard) is small. No open PR does it (#22 was closed). Avoid MCP server (too large, security risk).
## Scores
frequency: 3  severity: 3  fit: 5  smallness: 5  novelty: 5

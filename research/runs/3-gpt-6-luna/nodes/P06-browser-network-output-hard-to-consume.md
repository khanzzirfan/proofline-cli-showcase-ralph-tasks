---
id: P06
title: “The agent’s browser tools return data it can’t use”
who: developers, agent users
tools: [Cursor Browser Automation, Chrome DevTools MCP]
status: partly-verified
---
## Pain
Even when browser tools exist, their network or console output may be unavailable to the agent or returned in a form it cannot process. In that case, the feature is nominally connected but does not deliver usable diagnostic context.
## Evidence
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (forum, date unknown, unverified): web fetch returned the page title only; the reported error and details could not be checked.
- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 (forum, date unknown, unverified): web fetch returned the page title only; the reported Network-tab issue could not be checked.
- https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc (blog, date unknown, verified): explains structured network requests, screenshots and console stack traces as necessary debugging inputs (tutorial, promotional).
## How users want it fixed
- Provide structured browser inspection with network requests, screenshots and console details: https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc (vendor-authored tutorial; this is a proposed fix, not evidence of prevalence). 
## Workarounds people use today
- Copy a request as cURL/HAR or set up a separate Chrome DevTools MCP server.
## Session Recorder angle
The report already structures requests in Markdown and ZIP assets. An agent handoff that puts the narrative first and preserves linked bodies may help; #32 HAR export and #43 Copy as cURL are open overlaps to avoid.
## Scores
frequency: 2  severity: 3  fit: 4  smallness: 4  novelty: 3

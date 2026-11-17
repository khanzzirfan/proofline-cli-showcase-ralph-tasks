---
id: P03
title: "I want to hand the bug straight to the agent instead of retyping it"
who: developers, QA, product
tools: [claude-code, cursor, opencode, codex, jam, flowlens, darnly, faylee]
status: verified
---
## Pain
The bottleneck is not capture, it is *transfer*. The reporter has found the bug and already
has the evidence; the agent still has to be told about it. People want a single action that
pushes a structured bug report into the agent they use, ideally over MCP, rather than a
sequence of unzip, paste and copy-the-prompt steps.

## Evidence
- https://news.ycombinator.com/item?id=46047931 (hn, verified): "most tools optimize for agent-led exploration... But in many cases, I've already found the bug myself. What I actually want is a way to hand the agent the exact context I just saw - without retyping steps, copying logs, or hoping it can reproduce the behavior." (signal: 5 points, 1 comment; FlowLens, open source MCP server + Chrome extension)
- https://news.ycombinator.com/item?id=45909113 (hn, verified): "it detects bugs in your website in production from real user sessions, an llm clusters them by severity and it provides the complete context of the issue that you can copy-paste into your coding agent to fix it in one go" (signal: 5 points, 0 comments)
- https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 (forum, 2026-10-13, verified): "A customer says the discount button doesn't work. You open Cursor, but the report doesn't tell you what they clicked, what the browser logged, or which request failed." (signal: 1 post, 36 views)
- https://news.ycombinator.com/item?id=48795580 (hn, verified): "Show HN: Heckle – Send a bug's full browser context to your coding agent" (signal: 6 points, 2 comments)
- https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc&per_page=20 (github-repo-search, verified): 54 repositories built for the same handoff — BugTraceAI-CLI (183 stars), vynix-mcp (10), hearback (9), argus (7), Webvizio/mcp (6), ui-debugger-mcp (2) (signal: star counts as listed)

## How users want it fixed
- The mechanism named most often is an MCP server the agent can query: FlowLens "captures browser context and lets coding agents inspect it as structured, queryable data" (https://news.ycombinator.com/item?id=46047931).
- AnnotateFix asks for the same via MCP: "Its MCP tools make report..." (https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630).
- Some want it without MCP: "a way to hand the agent the exact context I just saw - without retyping steps, copying logs" (https://news.ycombinator.com/item?id=46047931).

## Workarounds people use today
- Copy-paste the console and the steps into the chat (https://news.ycombinator.com/item?id=48795580).
- Use a third-party Chrome extension plus its own MCP server (FlowLens, AnnotateFix, Heckle).
- File a GitHub issue and let a cloud agent pick it up (Copilot, Jules, Codex, OpenHands — see notes pain 4).

## Session Recorder angle
The extension already files a GitHub issue and exports a ZIP with `report.md`; the missing
piece is the *push into the agent*. A local MCP server is too big and too risky (notes
option C), but a "copy for agent" plus an "open in agent" style handoff is a clean PR.
Overlapping open PRs: #48 (labels and assignees when filing) partly covers the issue-side;
#24 (Linear issues) covers another tracker. No open PR covers the clipboard handoff.

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 4  novelty: 2
pain_score: 16  pick_score: 30

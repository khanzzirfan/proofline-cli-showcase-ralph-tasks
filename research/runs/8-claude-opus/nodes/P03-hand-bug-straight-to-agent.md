---
id: P03
title: "I already found the bug; let me hand the agent exactly what I saw"
who: developers, QA, product
tools: [FlowLens, Jam MCP, Darnly, Heckle, Vynix, Webvizio, Playwright MCP]
status: verified
---
## Pain
Most browser tools let the agent explore on its own. But often a human has already reproduced the bug and wants to pass that exact session (steps, logs, requests) to the agent without retyping. A wave of small tools appeared in 2025-2026 to do this, mostly over MCP.
## Evidence
- https://news.ycombinator.com/item?id=46047931 (hn, 2025-11-25, verified): "What I actually want is a way to hand the agent the exact context I just saw - without retyping steps, copying logs, or hoping it can reproduce the behavior." 5 points, 2 comments
- https://github.com/microsoft/playwright-mcp/issues/734 (github-issue, 2025-07-22, verified): "The trace only shows what the mcp server did through the tools the mcp server has." 6 reactions, 6 comments (user wants their own actions recorded)
- https://jam.dev/docs/jam-mcp (vendor-doc, weak, verified): "Paste a Jam link and your agent reads the video, logs, and requests."
- https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj (review page, verified): "Point at a bug, say what you expected, and your AI coding agent fixes it." 6 users, no ratings (weak)
- https://github.com/UseVynix/vynix-mcp (github-repo, verified via API): "Give AI coding agents access to your visual feedback and bug reports." 10 stars
- https://github.com/rbsriram/heckle (github-repo, verified): "The live QA co-pilot for agentic development. Talk at your app. Ship better code." Show HN https://news.ycombinator.com/item?id=48795580 (verified): "Send a bug's full browser context to your coding agent" 6 points
## How users want it fixed
- Structured, queryable recording handed to the agent over MCP (FlowLens, Jam MCP).
- One link or one command in the agent (Darnly `/darnly`, Jam link paste).
## Workarounds people use today
- Jam + Jam MCP (account, hosted), FlowLens (MCP + extension), manual `report.md` paste.
## Session Recorder angle
Session Recorder is this category, minus the last step. A local MCP server was judged too big and risky (notes, option C). A small step is a single "Copy for agent" output, or a `prompt.md` / `AGENTS`-style instruction file inside the ZIP. No open PR overlaps. Related but separate: P15 (agent replays the recorded steps as a script); P03 is about handing over the evidence.
## Scores
frequency: 3  severity: 3  fit: 5  smallness: 4  novelty: 4

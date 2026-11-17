---
id: P15
title: "Let the agent replay the steps I recorded instead of re-exploring"
who: developers, QA
tools: [Playwright MCP, Claude Code]
status: verified
---
## Pain
Agents re-discover the same flow on every run (log in, navigate, click), burning tokens and sometimes taking a different path than the human did. Users want human actions recorded as a script or trace the agent can replay to reproduce and later re-verify.
## Evidence
- https://github.com/microsoft/playwright-mcp/issues/734 (github-issue, 2025-07-22, verified): "The trace only shows what the mcp server did through the tools the mcp server has." 6 reactions, 6 comments
- https://github.com/microsoft/playwright-mcp/issues/280 (github-issue, 2025-04-28, verified): "is there a way to \"save\" the actions or steps the AI performed and rerun them automatically" 1 reaction, 3 comments
- https://github.com/microsoft/playwright-mcp/issues/1645 (github-issue, 2026-06-08, verified): "it re-evaluates accessibility snapshots and re-reasons about identical steps every time. That burns tokens and adds latency" 2 comments
- https://github.com/microsoft/playwright-mcp/issues/123 (github-issue, 2025-04-02, verified via API): "allow running the prompt based flow with codegen enable to capture the automated test code" (title) 16 reactions, 7 comments
- https://overreacted.io/how-to-fix-any-bug/ (blog, verified): "a reliable way to tell whether the bug is still happening. It’s “the test”."
## How users want it fixed
- Record human actions into a trace/script (#734); macro record and replay (#1645).
## Workarounds people use today
- Playwright codegen by hand; agent-written tests.
## Session Recorder angle
Not in section 5. The extension records clicks and inputs with selectors, so it could emit a replay script. But PR #22 (Playwright repro test in ZIP) was closed by its author as too large, so this is low novelty and not small.
Not merged with P03: P03 is about handing the agent the evidence; this node is about the agent replaying the human's steps (script or trace).
## Scores
frequency: 2  severity: 3  fit: 4  smallness: 1  novelty: 1

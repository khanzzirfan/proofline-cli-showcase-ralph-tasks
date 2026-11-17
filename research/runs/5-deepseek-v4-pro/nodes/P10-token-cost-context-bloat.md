---
id: P10
title: Browser evidence burns tokens and the context window — console/snapshots are too verbose
who: developers
tools: [chrome-devtools-mcp, playwright-mcp, Claude Code]
status: verified
---
## Pain
Handing browser context to an agent is expensive: raw console messages, page snapshots and MCP tool output flood the context window and raise token cost. Users want the evidence trimmed to a summary the agent can drill into.

## Evidence
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/171 (github-issue, 2025-09-26, verified): "list_console_message TOO VERBOSE TOO MUCH TOKENS" — 1 reaction, 3 comments
- https://github.com/microsoft/playwright-mcp/issues/889 (github-issue, 2025-08-14, verified): "Control and limit the size of the output of each tool" — 13 reactions, 15 comments
- https://news.ycombinator.com/item?id=46047931 (hn, verified): "token efficiency. Instead of dumping raw logs into the context window, the agent starts with a summary"

## How users want it fixed
- Tool output size limits and the ability to omit page snapshot/console: https://github.com/microsoft/playwright-mcp/issues/889

## Workarounds people use today
- Summarize first, drill down on demand (FlowLens); omit console/snapshot options; verbosity trim levels.

## Session Recorder angle
The extension already ships four deterministic trim levels (L0–L3) and a summary-first report — this pain is largely solved internally, so it is a lower-value new PR. Open PR #32 (HAR) and existing trimming work overlap.

## Scores
frequency: 3  severity: 4  fit: 3  smallness: 3  novelty: 2

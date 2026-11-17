---
id: P03
title: Users want to hand a bug straight to an agent, often over MCP or one link
who: developers, QA
tools: [Claude Code, Codex, Cursor, opencode]
status: verified
---
## Pain
The reporter has already reproduced the bug and captured the context; what they lack is a way to hand that exact context to a coding agent without retyping steps, copying logs, or hoping the agent can reproduce it. A whole category of tools (Heckle, FlowLens, Faylee, Jam MCP) exists to bridge this hand-off, usually over MCP or a shareable link.

## Evidence
- https://news.ycombinator.com/item?id=46047931 (hn, verified): "What I actually want is a way to hand the agent the exact context I just saw - without retyping steps, copying logs, or hoping it can reproduce the behavior."
- https://vibehacker.com/news/faylee-turns-a-bug-report-into-one-link-your-coding-agent-can-open-over-mcp-and- (news, 2026-10-31, verified): "its MCP server lets Claude Code, Codex, Cursor or OpenCode pull any moment, fix the code and comment back on the recording."
- https://news.ycombinator.com/item?id=48795580 (hn, verified): "Send a bug's full browser context to your coding agent"

## How users want it fixed
- An MCP server the agent can query for the recording: https://vibehacker.com/news/faylee-turns-a-bug-report-into-one-link-your-coding-agent-can-open-over-mcp-and-
- A local zip plus an MCP the agent explores with tools: https://news.ycombinator.com/item?id=46047931

## Workarounds people use today
- FlowLens (zip + MCP), Faylee (one link + MCP), Jam MCP, Heckle, Darnly.

## Session Recorder angle
The extension already exports a `report.md` ZIP the agent can read, but handing it over is manual (unzip, paste, copy the prompt). A lightweight hand-off (clipboard or an instructions block) closes the loop. MCP is flagged as "too big / security risk" in the notes; the clipboard/instructions path is the safe slice.

## Scores
frequency: 4  severity: 4  fit: 3  smallness: 2  novelty: 4

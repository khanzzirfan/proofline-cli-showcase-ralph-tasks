---
id: P06
title: "A fake error or bug report can hijack the agent that reads it"
who: developers, security teams
tools: [Sentry MCP, Claude Code, Cursor, browser MCPs]
status: verified
---
## Pain
Agents treat error reports and logs as trusted. Any text a page or an attacker can write into captured evidence (console messages, response bodies, error events) can carry instructions that the agent follows. Bug reports from the browser are exactly this kind of attacker-reachable text.
## Evidence
- https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/ (blog, 2026, verified): "hijacks AI coding agents into running attacker-controlled code on a developer’s machine, triggered by a single fake error report"
- Same page: "the Sentry MCP server (which returns this data to AI agents as trusted system output)"
- https://news.ycombinator.com/item?id=48507994 (hn, 2026-06-12, verified): "A Fake Bug Report Hijacks Your AI Coding Agent – and Nothing Catches It" 4 points
- https://news.ycombinator.com/item?id=47391875 (hn comment, verified): "I wouldn't cut loose an agent that's at risk of prompt injection w/ unscoped access to my primary Google account."
## How users want it fixed
- Mark log and telemetry content as untrusted data; harden agent configs (tenetsecurity "agent-jackstop").
## Workarounds people use today
- Separate browser profiles; agent config rules; human review before the agent acts.
## Session Recorder angle
Not in section 5 of the notes. The extension already tells its own AI summary model that evidence is untrusted (`lib/sharing/summary.ts`), but `report.md` and filed issues carry no such guard. A small PR: an "untrusted evidence" preamble in `report.md`/issue body, plus fencing of page-controlled text. No open PR overlaps (redaction PRs remove secrets, not instructions).
## Scores
frequency: 2  severity: 4  fit: 4  smallness: 5  novelty: 5

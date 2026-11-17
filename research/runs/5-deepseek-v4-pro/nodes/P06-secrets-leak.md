---
id: P06
title: Secrets and credentials leak into agent context and MCP configs
who: developers, security
tools: [Claude Code, Cursor, Copilot, MCP servers]
status: verified
---
## Pain
Coding agents and their MCP servers store and send credentials (API keys, tokens, cookies, customer data) across config files, prompts, logs and browser evidence. Screenshots and session recordings can accidentally contain tokens, emails and card numbers. This is a security and trust risk when handing bug reports to agents.

## Evidence
- https://blog.gitguardian.com/ai-coding-agents-credential-security/ (blog, 2026-09, verified): "24,008 unique secrets in public MCP configuration files, 2,117 of them valid, plus a 3.2% leak rate in Claude Code-assisted commits."
- https://www.browseract.com/blog/github-copilot-browser-automation (blog, verified): "The unsafe workaround is to paste credentials or cookies into the prompt. Do not do that."
- https://blog.sandbase.ai/multimodal-coding-agents-screenshot-to-fix-2026/ (blog, verified): "Do not send screenshots containing customer data, tokens, internal URLs... without redaction."

## How users want it fixed
- Redact tokens, cookies, cards and customer data before any report/recording is uploaded or handed to an agent: https://vibehacker.com/news/faylee-turns-a-bug-report-into-one-link-your-coding-agent-can-open-over-mcp-and-

## Workarounds people use today
- Faylee redacts before upload; secret scanners (GitGuardian); separate test browser profiles.

## Session Recorder angle
The extension already redacts by default (auth/cookie/API keys) at capture time. Open PRs #38, #42, #37, #44, #31 all expand redaction — this is a crowded area, so a new PR here has low novelty.

## Scores
frequency: 3  severity: 5  fit: 3  smallness: 3  novelty: 1

---
id: P10
title: “Copying browser requests can leak credentials into an agent prompt”
who: developers, QA, security-conscious teams
tools: [Claude Code, Cursor, DevTools, MCP tools]
status: verified
---
## Pain
Manual cURL/HAR sharing can carry cookies, authorization headers, URL tokens, custom API keys or body data into an agent conversation. Default sanitization does not necessarily remove every sensitive field.
## Evidence
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 (blog, date unknown, verified): warns “Copy as cURL includes your headers, so tokens go straight into the chat unless you remove them”; also describes HAR fields beyond standard cookie stripping (promotional, specific security caveat).
- https://www.infosecurity-magazine.com/news/chrome-extension-ai-engine-act-mcp/ (blog, 2025-04-25, verified): researchers found a Chrome extension could access an unauthenticated local MCP service and its exposed tools; security reporting, not an agent bug report.
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): suggests reuse of the existing authenticated session because WebFetch cannot access protected internal apps (1 reaction).
## How users want it fixed
- Remove Cookie/Authorization before sharing and redact tokens/custom headers from browser data: https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705.
- Keep agent/browser data sharing under user control: https://github.com/anthropics/claude-code/issues/57034.
## Workarounds people use today
- Manually clean cURL headers; use sanitized HAR cautiously; prefer local-only/read-only capture tooling when applicable.
## Session Recorder angle
Redaction is already a core capability and multiple open PRs address it (#42, #38, #37, #31), so a new generic redaction feature is not novel. Avoid exposing captured report data through an unauthenticated local MCP server.
## Scores
frequency: 3  severity: 5  fit: 4  smallness: 2  novelty: 1

---
id: P13
title: “A local agent bridge can expose more browser or machine data than intended”
who: developers, security-conscious teams
tools: [Chrome extensions, MCP servers, coding agents]
status: verified
---
## Pain
Connecting a browser extension or agent to a local MCP service can create a security boundary problem if local services lack authentication or expose privileged tools. A convenience bridge may grant more access than intended.
## Evidence
- https://www.infosecurity-magazine.com/news/chrome-extension-ai-engine-act-mcp/ (blog, 2025-04-25, verified): security researchers reported an extension could access an unauthenticated MCP server’s exposed filesystem tools; secondary reporting of research.
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 (blog, date unknown, verified): describes its recorded-traffic MCP as local and read-only, and explicitly notes nested JSON redaction limits (promotional, but direct caveat).
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): asks that tab sharing remain explicitly user-controlled (76 reactions, 7 comments).
## How users want it fixed
- Keep sharing opt-in and scoped to explicitly selected browser content: https://github.com/anthropics/claude-code/issues/57034.
- Prefer read-only data access with explicit limits: https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705.
## Workarounds people use today
- Use offline ZIP export and review evidence before attaching it; avoid exposing unauthenticated local tools.
## Session Recorder angle
The extension currently packages local evidence instead of hosting a local MCP endpoint. This argues against treating an MCP server as a small, low-risk feature. No current PR directly overlaps, but existing privacy/redaction PRs (#42, #38, #37, #31) must not be duplicated.
## Scores
frequency: 2  severity: 5  fit: 3  smallness: 2  novelty: 2

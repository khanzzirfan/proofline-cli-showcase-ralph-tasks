---
id: P05
title: "Logs and sessions I hand to agents carry secrets and tokens"
who: developers, security-minded teams
tools: [Claude Code, Playwright MCP, chrome-devtools-mcp]
status: verified
---
## Pain
Evidence given to agents (env files, console logs, cookies, transcripts) holds credentials. Users worry about secrets in agent context, and cloud sessions have no safe way to pass them.
## Evidence
- https://github.com/anthropics/claude-code/issues/32733 (github-issue, 2026-03-10, verified): "The environment variables field in the environment settings dialog explicitly warns: \"don't add secrets or credentials.\"" 217 reactions, 12 comments
- https://github.com/anthropics/claude-code/issues/401 (github-issue, 2025-03-08, verified): "it had loaded my projects `.env` file into its bash env." 54 reactions, 64 comments
- https://dev.to/skyestrela/stop-asking-ai-coding-agents-to-fix-vague-bugs-4ji6 (blog, verified): "Remove secrets and personal data before putting logs into an agent context."
- https://bug0.com/blog/playwright-mcp-cli-secret-redaction-2026 (vendor blog, weak, verified): "Playwright MCP and CLI now redact secrets from console logs"
- https://news.ycombinator.com/item?id=47391801 (hn comment, verified): "Even just stealing the auth cookie is pretty serious in terms of damage it could do."
## How users want it fixed
- Secret injection that never lands in agent-visible text (#32733); redaction at capture or write time (bug0 blog).
## Workarounds people use today
- Separate Chrome profiles, manual scrubbing, Playwright redaction.
## Session Recorder angle
Heavily covered already: #31, #37, #38, #42, #44 all add redaction. Nothing new to add in one PR.
## Scores
frequency: 4  severity: 4  fit: 3  smallness: 2  novelty: 0

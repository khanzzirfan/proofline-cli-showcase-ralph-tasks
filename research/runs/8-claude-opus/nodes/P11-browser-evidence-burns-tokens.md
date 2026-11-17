---
id: P11
title: "Browser tools flood the agent's context and burn tokens"
who: developers, agent users paying for tokens
tools: [chrome-devtools-mcp, Playwright MCP, Claude Code, Copilot]
status: verified
---
## Pain
Live browser tools return whole accessibility trees, console dumps and tool schemas on every call. Context fills, compaction fires, and bills grow. Users want only the relevant slice of evidence.
## Evidence
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/171 (github-issue, 2025-09-26, verified): "when copying directly from browser console its only 8k tokens. when using list_console_messages tool its 40k tokens." 1 reaction, 3 comments
- https://github.com/microsoft/playwright-mcp/issues/1216 (github-issue, 2025-11-20, verified): "console messages and the entire accessibility tree for the page are returned in the response every time" 3 reactions, 3 comments
- https://github.com/microsoft/playwright-mcp/issues/806 (github-issue, 2025-08-01, verified): "every action will return long content include tab information, console log and page content" 9 reactions, 3 comments
- https://github.com/microsoft/playwright-mcp/issues/1290 (github-issue, 2025-12-29, verified): "The default MCP tool list consumes 14.4k tokens in Claude Code." 2 reactions
- https://github.com/microsoft/playwright-mcp/issues/395 (github-issue, 2025-05-10, verified via API): "the snapshot length is too long, add pagination to it" (title) 14 reactions, 8 comments
- https://news.ycombinator.com/item?id=47391926 (hn comment on 604-point story, verified): "I've been using the DevTools MCP for months now, but it's extremely token heavy."
- https://news.ycombinator.com/item?id=47391877 (hn comment, verified): "Note that this is a mega token guzzler in case you're paying for your own tokens!"
- https://dev.to/creatman/playwright-mcp-burns-15m-tokens-cli-does-it-in-27k-so-i-built-the-skill-that-splits-the-phases-50j7 (blog, verified): "watched it burn through tokens like there was no tomorrow. Then /compact fired at 18% text context."
## How users want it fixed
- Options to omit snapshot and console, paginate, cap output size (playwright-mcp #1216, #395, #889).
- Dump to disk and let the agent query what it needs (HN 47391775, 47392937).
## Workarounds people use today
- Playwright CLI + skills, wrappers that write to disk, jq filtering.
## Session Recorder angle
A strength already: trim levels L0-L3 and token estimates (`lib/export/trimmer.ts`, `tokens.ts`) produce a bounded report. Little new to build; can be stated as positioning. A per-section token count in `report.md` header is a tiny add.
## Scores
frequency: 4  severity: 3  fit: 3  smallness: 4  novelty: 1

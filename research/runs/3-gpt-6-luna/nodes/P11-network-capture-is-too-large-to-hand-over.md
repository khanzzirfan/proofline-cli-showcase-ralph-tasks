---
id: P11
title: “A full browser network dump wastes agent context on noise”
who: developers, agent users
tools: [Claude Code, Cursor, Chrome DevTools MCP]
status: partly-verified
---
## Pain
A short browser session can produce hundreds of network entries, many of them static assets, while agents have finite context and tool-call budgets. Users need focused failures and related payloads rather than an unfiltered dump.
## Evidence
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 (blog, date unknown, verified): “A HAR of a few minutes of clicking has hundreds of entries. That's a lot of context spent on images and scripts.” (first-person tool author, promotional).
- https://github.com/rbsriram/heckle (github-issue, date unknown, verified): describes starting the agent with a summary and allowing drill-down to individual events, specifically citing token efficiency (3 stars, self-promotional).
- https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc (blog, date unknown, verified): recommends browser inspection against specific failing flows, not general capture (tutorial, promotional).
## How users want it fixed
- Summarize errors/failed requests first, then let the agent drill into selected evidence: https://github.com/rbsriram/heckle.
- Collapse noise and retain relevant requests in reports: https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705.
## Workarounds people use today
- Export only a request or use compact summaries/recorded-session search instead of pasting a whole HAR.
## Session Recorder angle
The extension already has deterministic trim levels, event prioritization, dedupe and token estimates. New capture/trim work likely overlaps existing functionality; consider making the compact report the default agent handoff rather than adding another trimming system.
## Scores
frequency: 2  severity: 3  fit: 4  smallness: 4  novelty: 2

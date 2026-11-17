---
id: P10
title: "Browser tools dump huge snapshots, HAR and logs that burn my tokens"
who: developers
tools: [Playwright MCP, Chrome DevTools MCP, Claude Code]
status: verified
---
## Pain
Raw page snapshots, HAR files and console dumps fill the context window. Users pay in tokens and the model gets worse as the context fills. They ask for limits, pagination and summaries.
## Evidence
- https://github.com/microsoft/playwright-mcp/issues/889 (github-issue, 2025-08-14, verified): token use "multiplied by 6 solving the same task" between two versions. 13 reactions, 15 comments.
- https://github.com/microsoft/playwright-mcp/issues/395 (github-issue, 2025-05-10, verified): snapshot "too long for some website, resulting the LLM token reach limit error". 14 reactions, 8 comments.
- https://github.com/microsoft/playwright-mcp/issues/806 (github-issue, 2025-08-01, verified, from search listing): "Easy to reach token limit". 9 reactions.
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 (blog, verified, weak): a HAR with "hundreds of entries" wastes context on images and scripts.
## How users want it fixed
- Verbosity levels and output limits (pw-mcp#889); pagination (pw-mcp#395).
## Workarounds people use today
- Hand-trimmed HAR; filtered console; ask for only errors.
## Session Recorder angle
Already addressed: four deterministic trim levels (L0-L3, about 150k/50k/15k tokens). Gap: the user has to choose and does not see the token estimate. A token estimate per level in the export dialog could help; check if it exists. Overlaps nothing in the open PRs, but the pain is mostly met.
## Scores
frequency: 3  severity: 3  fit: 3  smallness: 4  novelty: 2

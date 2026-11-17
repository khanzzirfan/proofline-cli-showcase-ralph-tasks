---
id: P13
title: "The evidence is too big and nobody knows what it will cost to feed it to the agent"
who: developers
tools: [Claude Code, Codex, Playwright MCP, chrome-devtools-mcp]
status: verified
---
## Pain
A recording produces a large artifact and the cost of handing it over is invisible. Images are the expensive part:
each screenshot is a base64 blob in the tool response, and one screenshot alone can push a request over a limit that
the user believes they have room for. People hit "context limit reached" at 25% usage and cannot tell why, then
guess which level of detail to export and re-export when the agent asks for more.

## Evidence
- https://github.com/anthropics/claude-code/issues/21230 (github-issue, 2026-01-27, verified): "Context limit reached" with "50k/200k tokens (25%)" — signal: 1 👍, 3 comments, closed as a duplicate of #9152; the body carries a full per-category token breakdown and notes the MCP response was base64
- https://github.com/openai/codex/issues/31040 (github-issue, 2026-07-03, verified): "macOS: compaction checkpoints re-embed screenshots until rollout hits 3.9 GB" — signal: 4 👍, 4 comments, still open
- https://github.com/anthropics/claude-code/issues/9152 (github-issue, 2025-10-08, verified): "[BUG] Claude Code MCP - Image responses token exceeds 25000 tokens" — signal: 3 comments, closed; the canonical duplicate of #21230
- https://github.com/anthropics/claude-code/issues/5385 (github-issue, 2025-08-08, verified): "[CRITICAL] Context auto-compact stuck at 0% - Tool Unusable" — signal: 12 reactions (12 👍), 98 comments, closed; context-window background rather than evidence-size specific
- https://github.com/anthropics/claude-code/issues/62063 (github-issue, 2026-05-24, verified): "Claude Code defaults to 1M context on fresh session with no workaround on Pro plan" — signal: 44 reactions (44 👍), 63 comments, closed; context-window background rather than evidence-size specific

## How users want it fixed
- State the token cost of the evidence before the agent receives it
  (https://github.com/anthropics/claude-code/issues/21230, verified — the reporter built the breakdown by hand).
- Export at the level the question actually needs, and re-export surgically rather than re-dumping
  (https://github.com/anthropics/claude-code/issues/21230, verified).

## Workarounds people use today
- Trim by hand: crop and downscale before pasting — the reporter notes the scaled image was "~5-7KB, ~1900 tokens"
  and still tripped the limit
  (https://github.com/anthropics/claude-code/issues/21230, verified).
- Use `imageResponses: 'omit'` for MCP servers that return large images
  (https://github.com/anthropics/claude-code/issues/21230, verified).

## Session Recorder angle
The extension has already solved most of this: four deterministic trim levels (L0 full, L1 standard ≈150k tokens,
L2 compact ≈50k, L3 minimal ≈15k), a token estimator (`lib/export/tokens.ts`, chars/4) and an asset manifest.
`docs/report-format.md` also tells the reader to start at L2 and escalate surgically.
So the novelty here is close to zero — only an *agent-calibrated default* (a level chosen for the target agent, or a
per-request token estimate next to the level picker) is still open. Nothing in the open PR list covers it, but the
underlying capability exists, so this node scores low on novelty by construction.

## Scores
frequency: 3  severity: 4  fit: 4  smallness: 3  novelty: 1

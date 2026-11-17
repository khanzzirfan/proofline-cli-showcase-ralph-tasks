---
id: P08
title: "One oversized or corrupt screenshot breaks the whole agent conversation"
who: developers
tools: [Claude Code, Playwright MCP]
status: verified
---
## Pain
A screenshot over the API size limit stays in history, so every later message fails with a 400 error. The only way out is a new chat and lost context. Screenshot tools can also return corrupt images that cause the same permanent error.
## Evidence
- https://github.com/anthropics/claude-code/issues/13480 (github-issue, 2025-12-09, verified): oversized image "causing all subsequent requests to fail" even for text messages. 90 reactions (90 +1), 111 comments.
- https://github.com/anthropics/claude-code/issues/2939 (github-issue, 2025-07-03, verified, from search listing): image over the size limit causes persistent request failure. 63 reactions, 39 comments.
- https://github.com/microsoft/playwright-mcp/issues/1211 (github-issue, 2025-11-19, verified, from search listing): screenshot tool returns corrupted image data causing a permanent API 400. 6 reactions, 30 comments.
## How users want it fixed
- Validate image size at paste time and reject or downscale (cc#13480 Option A).
## Workarounds people use today
- Start a new session; resize screenshots before pasting.
## Session Recorder angle
Real and fixable on our side: screenshots in the ZIP can be large (retina full page). Exporting agent-safe images (cap longest side near 1568-2000px, JPEG) keeps agents from bricking. The ZIP already uses JPEG; check the size cap in lib/export. Small, new, low overlap. Exact limit must be verified in code and vendor docs.
## Scores
frequency: 4  severity: 4  fit: 3  smallness: 4  novelty: 4

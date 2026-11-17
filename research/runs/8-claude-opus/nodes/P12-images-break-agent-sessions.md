---
id: P12
title: "Too many or too-large screenshots break the agent session"
who: developers, agent users
tools: [Claude Code, Codex]
status: verified
---
## Pain
Images in agent context have hidden limits: dimension caps, a per-session image budget, and format errors. One bad image can make every later request fail, forcing a new chat and losing context.
## Evidence
- https://github.com/anthropics/claude-code/issues/13480 (github-issue, 2025-12-09, verified): "the oversized image remains in the conversation history, causing all subsequent requests to fail with the same error" 90 reactions, 111 comments
- https://github.com/anthropics/claude-code/issues/2939 (github-issue, 2025-07-03, verified via API): "Image Upload Exceeds Size Limit Causing Persistent API Request Failure" (title) 63 reactions, 39 comments
- https://github.com/anthropics/claude-code/issues/19031 (github-issue, 2026-01-18, verified via API): "Corrupted image in context causes persistent API 400 errors, breaking the entire chat session" (title) 30 reactions, 23 comments
- https://github.com/anthropics/claude-code/issues/62466 (github-issue, 2026-05-26, verified via API): "Repeated \"Image couldn't be processed\" API errors consuming usage limit in Claude Code" (title) 24 reactions, 36 comments
- https://github.com/openai/codex/issues/31040 (github-issue, 2026-07-03, verified via API): "compaction checkpoints re-embed screenshots until rollout hits 3.9 GB" (title) 4 reactions
- https://dev.to/creatman/playwright-mcp-burns-15m-tokens-cli-does-it-in-27k-so-i-built-the-skill-that-splits-the-phases-50j7 (blog, verified): "Claude Code has a second context limit that nobody documents — an inline-image budget of roughly 50–100 blocks per session."
## How users want it fixed
- Validate image size at paste time; let users remove a bad image (#13480).
## Workarounds people use today
- Start a new chat; resize images before pasting; fewer screenshots.
## Session Recorder angle
Not in section 5. The extension already downscales screenshots to 1400 px longest side (`lib/capture/screenshots.ts`, `MAX_SHOT_DIM`), so the dimension error is handled. Open gap: a long session can hold hundreds of screenshots; telling the agent which few to open (a "key screenshots" list capped at e.g. 20) would avoid the image budget. Small, no PR overlap.
## Scores
frequency: 4  severity: 3  fit: 3  smallness: 4  novelty: 3

---
id: P15
title: Oversized or malformed screenshots brick the agent's session — context is unrecoverable
who: developers
tools: [Claude Code]
status: verified
---
## Pain
When a user pastes a screenshot into an agent, an image that is too large (>2000px, common on Retina) or malformed gets rejected by the API but stays in the conversation history — so every subsequent turn (even plain text) fails and the session is unrecoverable. The user loses the entire debugging context.

## Evidence
- https://github.com/anthropics/claude-code/issues/13480 (github-issue, 2025-12-09, verified): "the oversized image remains in the conversation history, causing all subsequent requests to fail - even plain text messages" — 90 reactions, 111 comments
- https://github.com/anthropics/claude-code/issues/56016 (github-issue, 2026-05-04, verified): "the bad image stays in the conversation history. Every subsequent turn... re-sends that history... The session is bricked."

## How users want it fixed
- Validate or resize images at paste time and offer a way to drop the offending image and recover: https://github.com/anthropics/claude-code/issues/13480

## Workarounds people use today
- ImageMagick resize before paste; hand-editing the session JSONL; starting a new conversation.

## Session Recorder angle
The extension captures screenshots as JPEG (quality 80) at controlled dimensions and redacts by default, so its exported screenshots are already sized for agent context — avoiding the Retina >2000px trap. An "agent-safe screenshot" guarantee would prevent this class of failure.

## Scores
frequency: 3  severity: 4  fit: 3  smallness: 4  novelty: 4

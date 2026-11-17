---
id: P13
title: "Cost and context: dumping a whole capture into the prompt is big and expensive"
who: developers, product
tools: [Claude Code, Cursor, BugDump, Session Recorder]
status: partly-verified
---
## Pain
A full capture — screenshots, video frames, HAR, transcript — is huge. Images and video frames
eat context fast (a single frame can cost over a thousand tokens), oversized images can break a
session, and long pasted logs push the agent toward its context limit and higher bills. People
want the smallest payload that still carries the bug.

## Evidence
- https://bugdump.com/blog/ai-agent-screen-recording-frames-mcp (blog, verified): "a 1280×720 frame costs Claude about 1,230 tokens, so the tool's description tells the agent to ask only for the moments it needs."
- https://github.com/anthropics/claude-code/issues/13480 (github-issue, 2025-12-09, verified, closed, 👍90): "[BUG] Oversized image breaks conversation permanently - no way to recover without starting new chat".
- https://forum.cursor.com/t/how-to-disable-cache-write-and-cache-read/118864 (forum, unverified): "Claude is too expensive now … more than 80[%] of the cost is caused by this."
- https://github.com/anthropics/claude-code/issues/16157 (github-issue, verified, open): "[BUG] Instantly hitting usage limits with Max subscription" — 728 reactions, 1499 comments (context/limit pain, broad).

## How users want it fixed
- Trim the payload: only the frames/logs that matter, deterministic and small (BugDump asks for six frames max).
- A size/token budget for the hand-off and a compact trim level.

## Workarounds people use today
- Manually delete logs; downscale screenshots; ask the agent for the specific seconds only.

## Session Recorder angle
Session Recorder already has deterministic trim levels (Full/Standard/Compact/Minimal) with no LLM —
arguably this pain is already half-solved inside the extension. The open slice is sizing the agent
hand-off (P02) to a token budget. Not in section 5, but novelty is limited by the existing trims.

## Scores
frequency: 3  severity: 3  fit: 4  smallness: 4  novelty: 3

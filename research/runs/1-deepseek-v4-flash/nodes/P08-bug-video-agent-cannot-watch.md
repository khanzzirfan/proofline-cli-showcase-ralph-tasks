---
id: P08
title: "An agent cannot watch a screen recording: users need frames and a text timeline"
who: developers, QA, product
tools: [Claude Code, Cursor, Codex, videobug, amagi-screen, BugDump, Tentomushi]
status: verified
---
## Pain
The clearest way to show a bug is a screen recording, but coding agents cannot watch video (MCP
has no video content type). Users are stuck narrating the video in words — a lossy step — or
building a tool to cut the video into key frames and a timeline text an agent can read. Several
small tools exist precisely to fill this gap, which proves the demand.

## Evidence
- https://github.com/s17labs/videobug (repo, verified): "Your coding agent can't watch video. Stop narrating bugs at it." It outputs "key frames your agent can see, plus the animation described as text (freeze runs, motion spikes)". MIT, one Python file.
- https://github.com/amagilabs/amagi-screen (repo, verified): "Send Claude a video of your bug, not a paragraph describing it" — detects scene changes, OCRs on-screen text, flags error frames into one `index.md`.
- https://bugdump.com/blog/ai-agent-screen-recording-frames-mcp (blog, verified): "MCP has no video content type, and Claude doesn't take video as input." Their fix is an MCP tool that "cuts frames from a bug report's screen recording at the seconds the agent picks, up to six per call".
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): "[FEATURE] Video Input Support in Claude Code" for "animation bugs, transition issues, or interaction problems that can't be captured in a single frame" — +1:46, 21 comments.
- https://news.ycombinator.com/item?id=49119880 (hn, 2026-07-31, verified): "Turning screen recordings into structured incident and bug reports … AI drafts a title, description, and reproduction steps."

## How users want it fixed
- Turn the recording into key frames + a timestamped text/motion timeline the agent can read
  (videobug, amagi-screen).
- Let the agent ask for specific seconds of the recording instead of the whole video (BugDump).

## Workarounds people use today
- Manually screenshot the moment of the bug; run videobug/amagi-screen; describe the video in prose.

## Session Recorder angle
Session Recorder already records tab video, screenshots and an event timeline. The gap: the video
is not turned into an agent-readable form. A small feature — extract N key frames around recorded
events and write them into `report.md` with timestamps and annotation captions — fits the existing
data and is a real gap. Vision/video node 2 of 2. No open PR covers this; docs/PLAN.md lists only
live streaming and rrweb replay as out of scope (different things).

## Scores
frequency: 4  severity: 4  fit: 5  smallness: 3  novelty: 4

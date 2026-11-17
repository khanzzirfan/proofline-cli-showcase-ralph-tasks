---
id: P08
title: Agents can't watch a screen recording; they need keyframes, a timeline and a transcript
who: developers, QA
tools: [Claude Code, Codex, Gemini]
status: verified
---
## Pain
Animation bugs, race conditions and gesture issues cannot be captured in a single frame, but agents cannot take video input. Even if they could, raw video burns tokens and loses the signal (cursor position, click timing, narration timing). Users want the recording turned into a small set of keyframes plus a timestamped transcript the agent can read.

## Evidence
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): "Demonstrating animation bugs, transition issues, or interaction problems that can't be captured in a single frame" — 57 reactions, 21 comments
- https://github.com/anthropics/claude-code/issues/12676 (comment, verified): "select frames at the moments narration and clicks line up, usually 4 to 8 for a 2 minute video... pass transcript, click targets, and those frames"
- https://github.com/anthropics/claude-code/issues/12676 (comment, verified): "Pick frames where the screen changes, not one per second... Transcribe the narration with timestamps."

## How users want it fixed
- Video input or, better, keyframe extraction plus transcript and click/cursor events delivered as structured text: https://github.com/anthropics/claude-code/issues/12676

## Workarounds people use today
- ffmpeg frame extraction (`-vf fps=1`); "AI, Look!" keyframe pinning; Clipy MCP; watch-video skill (a 40-second clip costs ~600 tokens).

## Session Recorder angle
The extension already records tab video, narration/transcript and click events, but `report.md` only references the video clips — it does not emit keyframes or a timed visual timeline an agent can read. This is the single strongest feature gap: no open PR touches it (HAR #32 and the closed Playwright test #22 are adjacent only).

## Scores
frequency: 4  severity: 4  fit: 5  smallness: 3  novelty: 5

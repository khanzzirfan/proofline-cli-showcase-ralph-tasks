---
id: P09
title: "My bug is a screen recording, but the agent can't watch video"
who: developers, QA, product
tools: [Claude Code, Claude in Chrome, Codex, Jam, Loom]
status: partly-verified
---
## Pain
Animation, timing and flicker bugs only show in motion. Agents take images and text, not video. People are asked to describe what the video shows, or a tool must turn the video into frames and text.
## Evidence
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): asks to "paste or reference video files in Claude Code CLI" for animation and interaction bugs. 57 reactions (46 +1), 21 comments.
- https://github.com/anthropics/claude-code/issues/14805 (github-issue, 2025-12-20, verified): Claude in Chrome records GIFs "but cannot analyze those recordings". 1 reaction, 7 comments.
- https://www.producthunt.com/products/markupr (product-hunt, 2026, unverified on re-check: HTTP 403, vendor, weak): the maker built a tool because of friction handing visual bugs to Claude Code, Codex and Gemini. 3 upvotes.
- A search result (not opened, unverified) says tools like Replay and markupR turn a recording into key frames plus transcript; vendor marketing.
## How users want it fixed
- Native video input (cc#12676), or sampled key frames from recordings (cc#14805).
## Workarounds people use today
- Extract frames with ffmpeg; write a text description; use a recorder that outputs frames and a transcript.
## Session Recorder angle
The ZIP contains .webm clips only at Full and Standard levels, and report.md already lists screenshots with timestamps and a voice transcript. So the agent already has text, frames at events and narration. A real gap would be frames at a fixed rate around errors or a "filmstrip" for animation bugs. Evidence for that exact gap is thin (one 57-reaction request, mostly general). Don't build video analysis; maybe a filmstrip around the first error. 
## Scores
frequency: 3  severity: 3  fit: 3  smallness: 2  novelty: 3

---
id: P09
title: "A bug video is dead weight for an agent: it cannot watch it"
who: developers, QA, product
tools: [Claude Code, Codex, Cursor, Loom, Jam, vidin, claude-video]
status: partly-verified
---
## Pain
Screen recording is the bug report format most non-developers produce. An agent cannot read it. Video has to become
images before a model can use it, and the naive conversion — one frame per second — produces mostly identical frames
that bury the few moments that matter and burn context. The correct shape is a small set of annotated keyframes plus
a written timeline, which today only third-party tools build.

## Evidence
- https://github.com/bradautomates/claude-video (github-repo, created 2026-04-24, verified): "Give an agent video evidence: a URL or local file becomes timestamped frames and a transcript." — signal: 21 021 stars, 2 230 forks, last pushed 2026-09-25; the strongest single signal that the gap is real, but it is a vendor's own repo
- https://github.com/teunlao/vidin (github-repo, created 2026-07-31, verified): "Claude Code, Codex and friends accept images, not video. So when a bug report arrives as a screen recording, the video is dead weight" — signal: 4 stars, 1 fork, last pushed 2026-10-15; also "someone has to watch it and retype what happened"
- https://cobaltcapture.com/guides/why-loom-doesnt-work-with-agents (vendor-doc, updated 2026-11-04, verified): "AI coding agents can't watch videos, so a Loom recording is unreadable as input. Markdown with screenshots is the format that works." — signal: vendor marketing, weak evidence
- https://news.ycombinator.com/item?id=45035578 (hn, 2025-08-27, verified): "get video and dev logs without installing anything" — signal: 17 points, 5 comments; a commenter asks "Shouldn't it run continuously for my QA and devs?"
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "Cursor's cloud agents run a full desktop with a real browser and attach screenshots and video to the PR (February 2026)" — signal: 8 👍, 3 comments; shows video-in-PR is already the competitive bar
- https://news.ycombinator.com/item?id=21049087 (hn, 2019-09-23, verified): "record a video of a bug synchronised with console logs and other technical data" — signal: 4 points, 0 comments; vendor pitch, weak

## How users want it fixed
- Turn a recording into a handful of annotated keyframes and a written timeline the agent can read
  (https://github.com/teunlao/vidin, verified — `REPORT.md` + `manifest.json` + `frames/`, served over MCP).
- Give the agent timestamped frames plus a transcript
  (https://github.com/bradautomates/claude-video, verified — the `/watch` skill extracts frames and a transcript).

## Workarounds people use today
- Install a separate MCP server (`vidin`) or agent skill (`claude-video`) that runs ffmpeg over the recording
  (https://github.com/teunlao/vidin, verified; https://github.com/bradautomates/claude-video, verified).
- Replace the video with markdown plus screenshots, the format that "works" for agents
  (https://cobaltcapture.com/guides/why-loom-doesnt-work-with-agents, verified).

## Session Recorder angle
The extension already records tab video into the ZIP (`video/001-0000.webm`, `entrypoints/offscreen/video.ts`,
`lib/export/bundle.video.test.ts`) — but only at L0/L1; at L2 "video bytes omitted while clip times remain" and at
L3 the video is gone. Nothing turns the recording into keyframes or a timeline, so today the video is exactly the
"dead weight" described above.
The honest fit is moderate: the extension already captures periodic screenshots during a take, so an
event-driven keyframe index plus a timeline could reuse that capture rather than needing ffmpeg. It is still the
largest feature on this list, and the market is already crowded (vidin, claude-video, Clipy, Loom).

## Scores
frequency: 3  severity: 3  fit: 3  smallness: 1  novelty: 4

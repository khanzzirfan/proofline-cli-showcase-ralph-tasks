---
id: P04
title: "Agents can't watch a bug video — I have to turn it into frames and text myself"
who: developers
tools: [claude-code, codex, gemini, clipy, watch-video]
status: verified
---
## Pain
No mainstream CLI agent accepts a video file, so a screen recording of a bug is useless to
them. Users end up hand-rolling the conversion: extract frames with ffmpeg, transcribe the
narration, then hand the agent a pile of PNGs. The people who have done it report that raw
frames are the wrong answer: they burn context, they lose the cursor position, and they
lose the timing that makes the narration meaningful.

## Evidence
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): "[FEATURE] Video Input Support in Claude Code" — "Claude Code currently supports pasting screenshots and referencing image files, which is extremely useful for UI debugging and visual context. However, there's no support for video input" (signal: 👍 46, ❤️ 11, 21 comments)
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2026-09-17, verified): "Three problems with raw video as input: Frame cost... Lost pointing... Lost timing." (signal: the comment has 👍 4; thread total 👍 46)
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2026-10-21, verified): "Pick frames where the screen changes, not one per second. Most frames in a screen recording are identical." (signal: thread total 👍 46, 21 comments)
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2026-06-06, verified): "Manual workaround (frame extraction via ffmpeg -i in.mp4 -vf fps=1 out_%03d.png then attaching each PNG) is exactly the kind of friction the existing image/PDF support eliminated" (signal: 👍 4 on that comment)
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2026-11-15, verified): "It scans every frame for motion and cuts... then gives Claude a one page brief and opens frame sheets only when a question needs them. A 40 second clip costs about 600 tokens." (signal: teddmchl, watch-video skill)
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2026-04-09, verified): "Gemini can take mp4 as input but AFAIK it essentially converts the video into 1s frames and process the sequence of frames." (signal: 👍 3 on that comment)
- https://github.com/clipy-recorder/clipy-mcp (github-repo, n/a, verified): "Clipy is the first agent-readable screen recorder — free, no watermark, for Mac, Chrome, and the web. One share link: humans watch the video, AI agents read the summary, key moments, and transcript." (signal: 5 stars, 2 forks; ships `get_agent_context` returning "summary + interaction timeline + key moments + transcript + available browser diagnostics) as markdown", and `get_key_moments` giving "timestamps, captions, and click coordinates")
- https://chromewebstore.google.com/detail/thinkrun-screen-recorder-for/affbcanbhbnolapiokgjnkfjccdmefmd (listing, updated 2026-08-19, verified): "ThinkRun packages what happened — video, transcript, actions, console, and network — into context an agent can parse in one pass, instead of you re-explaining it." (signal: 23 users, 0 ratings, v0.2.12)

## How users want it fixed
- The most-cited shape is **structured text plus a few frames**, not a video file: "pass transcript, click targets, and those frames, so the agent gets 'user clicked Save at 0:14, said the modal freezes, here is the frame at 0:17'" (https://github.com/anthropics/claude-code/issues/12676, 2026-09-17 comment).
- Another asks for a documented way to feed structured visual context: "the more useful feature request here is a documented way to feed structured visual context in, rather than video decoding inside the CLI." (same issue)
- One asks for change-detection frames plus narration transcript plus a preview before sending: "Show the frames before sending. Screen recordings often catch tokens, emails or notifications by accident" (same issue, 2026-10-21 comment).

## Workarounds people use today
- ffmpeg frame extraction, then attach PNGs one by one (https://github.com/anthropics/claude-code/issues/12676)
- Third-party "AI, Look!" screen recording with key-frame pinning (same issue, 2026-04-09 comment)
- The Clipy MCP server, which "pulls a recording" and hands the agent text plus frames (same issue, 2026-09-17 comment)
- The `watch-video` skill from teddmchl, which produces "a one page brief" for ~600 tokens per 40s clip (same issue, 2026-11-15 comment)

## Session Recorder angle
This is the strongest **new** pain found in this run and it maps onto what the extension
already records. Session Recorder already captures tab video (`video/NNN-mmss.webm`), screenshots
and a narrated transcript on the same clock — exactly the three inputs the users above say
the agent needs. What it does not do is *render* them into an agent-readable brief. Today the
trimmer clears the video file reference at L2+ (`lib/export/trimmer.ts:519-528`), so at Compact
and Minimal the agent sees the clip's time span but no asset, and the screenshots are only
pointers to `.jpg` files. A "visual brief" — narration transcript with timestamps, click
targets, and the 4-8 frames where the screen changed, with change detection instead of fixed
1 fps — would be a clean PR and would land exactly on the requested shape.
Overlapping open PRs: #21 (screenshot and pause keyboard shortcuts), #25 (typed value before
submit), #29 (browser, OS, viewport in report) touch inputs but none of them renders visual
evidence into text. #22 (Playwright repro test) was closed by its author. No open PR covers
frame selection or a visual brief.

## Competitive caveat (found in the US-003 verification pass)
The "visual brief" idea is **not** unclaimed ground. Two competitors already ship it:

- Clipy (https://github.com/clipy-recorder/clipy-mcp) ships an MCP server whose
  `get_agent_context` returns "summary + interaction timeline + key moments + transcript +
  available browser diagnostics) as markdown", with `get_key_moments` giving "timestamps,
  captions, and click coordinates" and `read_context_document` returning "the timestamped
  transcript with frame captions interleaved". It is only 5 stars and 2 forks, and it needs a
  paid account after a free tier.
- ThinkRun (https://chromewebstore.google.com/detail/thinkrun-screen-recorder-for/affbcanbhbnolapiokgjnkfjccdmefmd),
  a Chrome extension, markets exactly this: "ThinkRun packages what happened — video,
  transcript, actions, console, and network — into context an agent can parse in one pass,
  instead of you re-explaining it." It has 23 users and 0 ratings, updated 2026-08-19.

So the novelty of "render the video into text for the agent" drops from 4 to 2. What is still
open for Session Recorder specifically: (a) it works **offline and local** — Clipy uploads to a
cloud service and needs an API key, which is exactly the privacy objection in P12; (b) it
needs no MCP server, so it works with every agent, not only MCP-capable ones; (c) the
extension already has the click/capture clock and the narration transcript, so the marginal
work is a formatter, not a new capture pipeline. Frame *selection* by change detection is
still nobody's shipped feature, but Clipy's `get_key_moments` is close enough that the claim
"nobody does this" would be false.

## Scores
frequency: 4  severity: 4  fit: 5  smallness: 3  novelty: 2
pain_score: 16  pick_score: 31

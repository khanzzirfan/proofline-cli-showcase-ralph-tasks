---
id: P10
title: "My agent can't watch the bug video, so I screenshot frames by hand"
who: developers, QA, agent users
tools: [Claude Code, Claude in Chrome, Jam, Clipy, Replay, bug2context]
status: partly-verified
---
## Pain
A screen recording is the natural bug report, but coding agents cannot read video files. Users extract frames by hand or write long descriptions, and motion bugs (flicker, transitions, race conditions) get lost in single screenshots. Many small tools now turn recordings into key frames plus a timeline.
## Evidence
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): "there's no support for video input, which limits the tool's usefulness in scenarios like" (lists "Sharing quick recordings of bug reproduction steps") 57 reactions, 21 comments
- https://github.com/anthropics/claude-code/issues/2614 (github-issue, 2025-06-26, verified): "This tool cannot read binary files. The file appears to be a binary .mov file." 3 reactions, 10 comments
- https://github.com/anthropics/claude-code/issues/14805 (github-issue, 2025-12-20, verified): "Static screenshots miss flickering, jank, race conditions, and state changes" 1 reaction, 7 comments
- https://github.com/AryaaSk/replay (github-repo, verified): "picks the key frames, runs them through Claude with vision. ~3-5 seconds later you get a markdown timeline + key screenshots"
- https://www.reddit.com/r/ClaudeAI/comments/1xwjdzc/how_i_show_claude_code_a_ui_bug_without_writing_a/ (reddit, 2026-11, unverified, SerpAPI snippet): "it can't watch a video file in a prompt. That's why I pull out a cropped screenshot + timestamped note"
- https://www.reddit.com/r/ClaudeCode/comments/1ssub0g/a_plugin_that_lets_claude_code_watch_videos_image/ (reddit, 2026-04-22, unverified, snippet): "every time I wanted it to \"look at a video\" I'd have to screenshot frames manually"
- https://www.reddit.com/r/ClaudeAI/comments/1t9frna/built_an_mcp_that_gives_claude_code_the_ability/ (reddit, 2026-05-10, unverified, snippet): "One thing Claude Code can't do natively is watch a video"
- https://www.reddit.com/r/ClaudeAI/comments/1uppopb/clipy_mcp_claude_code_can_now_watch_my_screen/ (reddit, 2026-07-07, unverified, snippet): "One frame doesn't show the sequence of what happened."
- https://jam.dev/docs/jam-mcp (vendor-doc, weak, verified): "Paste a Jam link and your agent reads the video, logs, and requests."
## How users want it fixed
- Sample key frames from recordings for the model (#14805); video input (#12676).
- Markdown timeline + key frames instead of raw video (Replay, bug2context, Clipy).
## Workarounds people use today
- ffmpeg frame extraction, manual screenshots with timestamps, Jam MCP, Clipy/Replay/Watch Skill plugins.
## Session Recorder angle
Real gap. The ZIP has `video/*.webm` only at Full/Standard, and text agents cannot read it; at Compact/Minimal video bytes are dropped. The extension already has screenshots at events, but motion between them is lost. A small PR: at export, extract N frames from each clip around key events (clicks, errors, annotations) with `<video>` seek + canvas, write `frames/*.jpg`, and list them in the `report.md` timeline. No open PR overlaps (#21 is screenshot shortcuts only).
## Scores
frequency: 4  severity: 3  fit: 5  smallness: 3  novelty: 5

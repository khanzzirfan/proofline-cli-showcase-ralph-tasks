---
id: P08
title: "A CLI agent has no way to take a screenshot or read an image, so the bug stays a story"
who: developers
tools: [Claude Code, Codex, Copilot CLI, Cline, opencode, Cursor]
status: verified
---
## Pain
Most coding agents live in a terminal. Terminals have no image channel worth the name, so an image has to be saved
to disk, its path remembered and the path typed into the prompt — or the agent simply cannot see it at all. The
result is that a visual bug is described in words, and words are a lossy format for "the button is 3px too low".
Users have built whole scripts, browser extensions and clipboard daemons around this single gap.

## Evidence
- https://github.com/github/copilot-cli/issues/476 (github-issue, 2025-11-05, verified): "I struggle to get screenshots into the agent, and this would make debugging to and fro with the cli so much easier." — signal: 57 👍, 12 comments, closed; the quoted line is a comment by `thawkins` on 2025-11-05
- https://github.com/anthropics/claude-code/issues/12644 (github-issue, 2025-11-28, verified): "The Claude Code CLI has no way to accept images or screenshots." — signal: 35 👍, 26 comments; the author lists four broken workarounds
- https://github.com/openai/codex/issues/2221 (github-issue, 2025-08-12, verified): "Do we seriously not have a way to share images with codex yet?" — signal: 21 reactions (12 👍 / 5 🎉 / 4 👀), 9 comments, closed
- https://github.com/github/copilot-cli/issues/1276 (github-issue, 2026-02-04, verified): "Instead, users must:" — signal: 8 👍, 11 comments, still open; the body then lists three steps, "Save the image to disk", "Remember the file location" and "Paste the file path into the CLI"
- https://forum.cursor.com/t/subject-image-copy-paste-in-cursor-chat-stopped-working/167990 (forum, 2026-08-11, verified): "Attaching an image either CMD + V or dragging the image is completely broken." — signal: 171 likes, 224 views, 13 posts
- https://forum.cursor.com/t/custom-api-models-cannot-read-local-image-file-paths-pasted-images-work/167497 (forum, 2026-08-05, verified): "the model cannot correctly understand images referenced by local file path" — signal: 127 likes, 225 views, 9 posts
- https://github.com/microsoft/playwright-mcp/issues/1211 (github-issue, 2025-11-19, verified): "Bug: Screenshot tool returns corrupted image data causing permanent API error 400" — signal: 6 reactions (6 👍), 30 comments, closed
- https://github.com/microsoft/playwright-mcp/pull/98 (github-pr, 2025-03-31, verified): "Add functionality to save screenshots as image files" — signal: 2 reactions (1 🎉), 6 comments, closed
- https://github.com/anomalyco/opencode/pull/1589 (github-pr, 2025-08-04, verified): "it wasn't able to analyze images programmatically" — signal: 2 👍, 3 comments, closed
- https://github.com/OpenHands/OpenHands/issues/8387 (github-issue, 2025-05-09, verified): "Our browser tab stop showing screenshot correctly for past actions." — signal: 1 👀, 3 comments, closed; the maintainer asks for a slider to "backtrace the history web interactions (include URL and action metadata when hover on the node on the slider)"
- https://news.ycombinator.com/item?id=47453812 (hn, 2026-03-20, verified): "The only way to do that was to take a screen shot or write down the UI element and then type it into my CLI or Coding Agent tool." — signal: 2 points, 1 comment; a vendor pitch for "Knit", so weak as evidence

## How users want it fixed
- Paste an image straight into the agent prompt and have it analysed as vision content
  (https://github.com/anthropics/claude-code/issues/12644, verified).
- The agent should be able to *take* the screenshot itself, not receive one
  (https://github.com/anthropics/claude-code/issues/57034, verified).

## Workarounds people use today
- A `lastshot` shell script plus a `CLAUDE.md` rule that references the newest screenshot
  (https://github.com/anthropics/claude-code/issues/12644, verified).
- `clip2path` / `clipaste` daemons that convert a clipboard image to a file path the agent can read
  (https://github.com/anthropics/claude-code/issues/12644, verified).
- An AutoHotkey script that replaces the clipboard image with its path after a snip
  (https://github.com/anthropics/claude-code/issues/12644, verified).
- A Claude Code mod that watches the clipboard and re-joins rows
  (https://github.com/anthropics/claude-code/issues/18170, verified).

## Session Recorder angle
The extension already produces screenshots as JPEG assets (`screenshots/001-0004.jpg` in the ZIP layout,
`lib/capture/screenshots.ts`) and `report.md` references them as image links. At L3 they degrade to a filename
manifest, so a text-only agent gets names, not pixels.
The gap that is still open and small: make the images reachable from the agent's working directory (write them
next to `report.md` with the paths spelled out in the report), and attach them to a filed issue (see P04).
No open PR does either. `#43` is "Copy as cURL", `#32` is "HAR export", `#29` adds browser/OS/viewport — none
touch image delivery to an agent.

## Scores
frequency: 5  severity: 4  fit: 5  smallness: 3  novelty: 3

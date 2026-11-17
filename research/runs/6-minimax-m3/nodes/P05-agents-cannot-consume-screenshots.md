---
id: P05
title: "The agent can't consume my screenshots: paste fails, images get dropped or resized, oversized ones kill the session"
who: developers
tools: [claude-code, copilot-cli, cursor, cline, roo-code, grok-bot]
status: verified
---
## Pain
Even where an agent can *see* images, the path from "screenshot on my clipboard" to "bytes the
model can read" is broken in several places at once. Clipboard paste is unreliable across
agents and platforms; some harnesses silently drop the full-resolution bytes; some resize
them below what the model needs; and an image over 2000 px can permanently poison the
conversation so that even a plain text message keeps failing.

## Evidence
- https://github.com/anthropics/claude-code/issues/13480 (github-issue, 2025-12-09, verified): "the oversized image remains in the conversation history, causing all subsequent requests to fail with the same error - even plain text messages with no images attached." (signal: 👍 90, 111 comments; one report says "the problem was created by the claude chrome plugin itself... kills my chat")
- https://github.com/github/copilot-cli/issues/2675 (github-issue, 2026-04-13, verified): "Currently, sharing visual context requires either taking a screenshot via Chrome DevTools integration (only works for browser pages) or saving an image to a file and referencing it with @." (signal: 👍 7, 3 comments, still open)
- https://github.com/github/copilot-cli/issues/2675 (github-issue, 2026-05-31, verified): "after screenshot or copy image from anywhere, cannot paste the image to Copilot CLI directly. Need to save the screenshot/image and then @ it is not convenient at all." (signal: 👍 2 on that comment)
- https://github.com/github/copilot-cli/issues/1241 (github-issue, 2026-02-01, verified): "When I paste from a clipboard from things coming from SnagIt or Snipping Tool, nothing happens...no feedback, nada." (signal: 👍 7, closed 2026-04-07 as fixed)
- https://forum.cursor.com/t/ctrl-v-image-paste-always-fails-on-macos-execfile-missing-encodingbuffer/176096 (forum, 2026-10-25, verified): "Ctrl+V doesn't attach images from the clipboard right now, even though the screenshot is on the clipboard." (signal: 7 posts, 188 views; a second report at 177946)
- https://forum.cursor.com/t/grok-bot-drops-mcp-typeimage-bytes-from-remote-tool-results-full-res-screenshots-unsavable/177756 (forum, 2026-11-08, verified): "Grok Bot's remote MCP connector does not expose original type:"image" content from tool results to the agent... Only the text content part reaches the agent." (signal: 2 posts, 44 views)
- https://github.com/cline/cline/issues/9902 (github-issue, 2026-03-20, verified): "Browser automation fails with 'url field must be a base64-encoded image' error" — the screenshot is dropped or replaced, not delivered (signal: 👍 4, 5 comments, closed as not planned 2026-10-28)

## How users want it fixed
- A path that does not require the human to save a file: "The image would be sent as a vision-capable attachment to the model... just showing the placeholder text is fine — the image data would still be sent to the model." (https://github.com/github/copilot-cli/issues/2675)
- Images that survive at full resolution: "have the tool also return the full-resolution JPEG as a download link (or a file path the bot can reach) in its text output." (https://forum.cursor.com/t/grok-bot-drops-mcp-typeimage-bytes-from-remote-tool-results-full-res-screenshots-unsavable/177756)
- Claude Code users ask for the image bytes to be addressable at all: "The image data being vision-only and not writable to disk is a real gap." (https://github.com/anthropics/claude-code/issues/16592, 👍 14, 8 comments)

## Workarounds people use today
- Save the screenshot to a file and reference it with `@` (https://github.com/github/copilot-cli/issues/2675)
- Downscale images by hand before pasting (`convert in.png -resize '1800x1800>'`, https://github.com/anthropics/claude-code/issues/13480)
- Repair a poisoned session by hand-editing `~/.claude/projects/<cwd>/<sessionId>.jsonl` (https://github.com/anthropics/claude-code/issues/13480, 2026-05-06 comment)

## Session Recorder angle
Session Recorder already writes screenshots as `screenshots/NNN-mmss.jpg` into the ZIP, so a
file-reading agent can open them.

**Correction found in US-005 (re-reading the source):** the "make the screenshots safe for
agents" framing is **already implemented**. `lib/capture/screenshots.ts:38` defines
`const MAX_SHOT_DIM = 1400;` and `ScreenshotScheduler.capture()` (lines 160-190) downscales
any screenshot whose longest side exceeds 1400 px via `OffscreenCanvas`, re-encoding it as
JPEG (`convertToBlob({ type: 'image/jpeg' })`). The capture is `image/jpeg` from the
debugger, so the stored asset is always JPEG too. 1400 px is well under the 2000 px limit
that poisons a Claude Code session (claude-code #13480), and the stored `width`/`height`
are recorded on the screenshot event.

So the two things the extension *does* not do are narrower than the original node claimed:
1. **It does not tell the agent which file to open.** `report.md` renders a screenshot as a
   markdown image link, `![ctx](screenshots/001-0012.jpg)` (`lib/export/markdown.ts:368-376`).
   When the report is pasted as *text* into an agent chat, that link is a dead reference —
   the agent has no file to open. The evidence is named but not reachable.
2. **It does not deliver the image bytes at all.** There is no paste-to-clipboard path and
   no attachment path, so the "paste an image into the agent" route that users report as
   broken (S8, S9, S16, S17, S19) stays broken. `copyIssue()`
   (`entrypoints/share/useShareReport.ts:330`) copies *text* only.

Overlapping open PRs: #21 (screenshot and pause keyboard shortcuts), #29 (browser, OS,
viewport in report). No open PR covers image sizing (already done) or image delivery.

## Scores
frequency: 5  severity: 4  fit: 4  smallness: 3  novelty: 2
pain_score: 18  pick_score: 29

Score note (US-005): smallness 4→3 and novelty 3→2 after re-reading `lib/capture/screenshots.ts`.
The dimension-and-format half of this node is already shipped (`MAX_SHOT_DIM = 1400`, JPEG-only),
so it is not a PR-sized gap. The open remainder is delivery — telling the agent which file to
open and getting the bytes to it — which is a smaller change than the original framing implied.

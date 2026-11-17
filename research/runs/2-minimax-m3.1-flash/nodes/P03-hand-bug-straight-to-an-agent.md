---
id: P03
title: "People want to hand a bug straight to an agent, and this recorder has no channel to do it"
who: developers, QA, product
tools: [Jam, Darnly, FlowLens, Faylee, vidin, Ghostship, AnnotateFix, MCP, Claude Code, Cursor]
status: verified
---
## Pain
The wanted shape is one action: reproduce the bug and send the evidence directly to a coding agent, in a form the
agent can act on without a human in the middle. The market has filled with partial versions of this — MCP servers for
bug reporters, one-link handoffs, agent-installed reporters — but each one stops short of the full bundle
(clicks + console + network + screenshot) or of the step the agent actually needs.
This is the tool-side twin of the agent-side pain. The recording tool does its job: it captures the clicks, the
console, the network, the screenshots, the narration and writes a report. Then it stops. The report is human-shaped —
a hosted HTML page, an issue body, a Markdown file in a ZIP — and the agent-shaped thing, the thing the user actually
wants, does not exist as a single action. Getting it to the agent means export, unzip, paste, copy the prompt out of
the documentation.

## Evidence
- https://forum.cursor.com/t/integration-with-developer-tool/34824 (forum, 2024-12-14, verified): "copying and pasting stuff from chrome developer tools (API requests, responses, browser console in particular) and into cursor to troubleshoot issues" — signal: 9 432 likes, 1 923 views, 13 posts
- https://github.com/anthropics/claude-code/issues/101957 (github-issue, 2026-10-14, verified): "I have to download, unzip, upgrade gh and run it locally, which defeats the point of a cloud session." — signal: 11 reactions (10 👍 / 1 ❤️), 4 comments, still open
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/96 (github-issue, 2025-09-24, verified): "Feature Request: Support for browser extension development and debugging" — signal: 77 reactions (61 👍), 23 comments
- https://github.com/anthropics/claude-code/issues/12644 (github-issue, 2025-11-28, verified): "This forces me to switch to the web interface just to show a screenshot, breaking the development flow and context." — signal: 35 👍, 26 comments
- https://github.com/anthropics/claude-code/issues/18170 (github-issue, 2026-01-14, verified): "it breaks every terminal copy-paste of code/config blocks" — signal: 305 reactions (304 👍), 140 comments; the quoted line is a comment by `shaggyz` on 2026-10-09 with 1 👍
- https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 (forum, 2026-10-13, verified): "A customer says the discount button doesn't work. You open Cursor, but the report doesn't tell you what they clicked, what the browser logged, or which request failed." — signal: 36 likes, 36 views, 1 post
- https://news.ycombinator.com/item?id=45215032 (hn, 2025-09-11, verified): "Ghostship lets you find bugs in your web app by entering in your URL and describing a user journey." — signal: 53 points, 11 comments (Launch HN)
- https://news.ycombinator.com/item?id=45035578 (hn, 2025-08-27, verified): "getting all the context needed to debug a bug report without the endless back-and-forth" — signal: 17 points, 5 comments; vendor pitch for "Recording Links"
- https://news.ycombinator.com/item?id=48413629 (hn, 2026-06-05, verified): "Add to it MCP servers for other systems you use, like AWS Docs MCP, Atlassian MCP, Linear MCP, SearXNG MCP, Playwright MCP, etc, which basically multiplies the AI's usefulness" — signal: 171 points, 86 top-level comments (136 including replies)
- https://github.com/teunlao/vidin (github-repo, created 2026-07-31, verified): "Claude Code, Codex and friends accept images, not video. So when a bug report arrives as a screen recording, the video is dead weight" — signal: 4 stars, 1 fork, last pushed 2026-10-15; the README shows `claude mcp add vidin`
- https://news.ycombinator.com/item?id=21049087 (hn, 2019-09-23, verified): "We built a Chrome Extension that allows you to record a video of a bug synchronised with console logs and other technical data" — signal: 4 points, 0 comments; vendor pitch, weak evidence

## How users want it fixed
- One action that puts the report, its assets and the instructions into the agent's context
  (https://forum.cursor.com/t/integration-with-developer-tool/34824, verified).
- Serve the evidence over MCP so the agent pulls it rather than a human pastes it
  (https://github.com/teunlao/vidin, verified).
- Do not make the user leave the tool they are already in
  (https://github.com/anthropics/claude-code/issues/12644, verified).

## Workarounds people use today
- Export the ZIP, unzip it, paste `report.md`, copy the prompt from the docs
  (the gap the context notes already record for this extension).
- Use the terminal as a transport and accept the formatting damage
  (https://github.com/anthropics/claude-code/issues/18170, verified).
- Paste a hosted report URL and let the agent fetch it
  (https://github.com/anthropics/claude-code/issues/101957, verified).
- Install a dedicated MCP bug reporter (Jam MCP, FlowLens, vidin) alongside the recorder.
- Publish the recording to a hosted URL and paste the link into the agent
  (the extension already publishes to Cloudflare Pages or Proofline — `lib/sharing/cloudflare.ts`).

## Session Recorder angle
This is the extension's own confirmed gap, and the smallest high-value change on the list.
`entrypoints/share/useShareReport.ts` already exposes `copyIssue()` (line 330), which writes `finalBody` to the
clipboard — the *issue* Markdown, not an agent bundle. The "Suggested prompt" that makes `report.md` usable lives
only in `docs/report-format.md` (line 78) and never reaches the product. `lib/export/bundle.ts` already produces
`report.md`, `session.json`, `MANIFEST.md` and the assets at a chosen level, so an agent-ready bundle is a
rendering and clipboard job over existing output.
A local MCP server is explicitly out of scope for the extension's own v1 plan (`docs/PLAN.md` lists live streaming
to an agent as out of scope) and the notes flag it as "too big; security risk". The tractable part of this pain is
the *file-level* hand-off, not the transport.
No open PR covers this. `#22` (Playwright repro test in the ZIP) was closed by its author, `#24` adds Linear,
`#48` adds labels and assignees when filing.

## Scores
frequency: 5  severity: 4  fit: 5  smallness: 4  novelty: 5

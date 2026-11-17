---
id: P02
title: "Copy-pasting logs and cURL into the agent by hand is slow, lossy and leaks tokens"
who: developers
tools: [Claude Code, Cursor]
status: partly-verified
---
## Pain
Because the agent cannot read the browser, developers hand-copy console output, network
responses and cURL commands into the chat. It breaks flow, loses formatting, sometimes the
pasted text never reaches the agent, and it can copy secrets or tokens into the prompt.

## Evidence
- https://news.ycombinator.com/item?id=48795580 (hn, 2026-07-05, verified): "This is so helpful, thanks for open sourcing this, saves me having to copy paste from browser console to my coding agent." (comment on Show HN: Heckle, 6 points).
- https://github.com/anthropics/claude-code/issues/18170 (github-issue, verified): "Copy/paste from terminal includes unwanted indentation and trailing spaces" — 305 reactions, +1:304, 140 comments.
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 (forum, unverified: body JS-rendered, from 00-context-notes section 6): pasted debug output the agent can no longer see.
- https://github.com/anthropics/claude-code/issues/32005 (github-issue, 2026-03-08, verified): "The current workflow requires me to manually save the image as a file, note the file path, and ask Claude Code to read it … which significantly breaks the flow" — +1:8, 17 comments.

## How users want it fixed
- One-action handoff instead of manual copy-paste: capture the browser context and give it to the
  agent in a form it can read (Heckle/FlowLens style tools exist precisely for this).
- Paste that preserves formatting, and no need to save files first (claude-code#32005, #18170).

## Workarounds people use today
- Select-all copy from DevTools; save screenshots to disk and pass paths; paste HAR files.

## Session Recorder angle
This is the core gap already identified in 00-context-notes section 3: only the issue Markdown is
copied in code (`copyIssue` in `entrypoints/share/useShareReport.ts`), while the `report.md` prompt
must be assembled by hand. A "Copy for coding agent" action (prompt + trimmed report to clipboard)
directly removes this pain. No open PR does it; watch #43 (Copy as cURL) as adjacent but different.

## Scores
frequency: 5  severity: 3  fit: 5  smallness: 5  novelty: 4

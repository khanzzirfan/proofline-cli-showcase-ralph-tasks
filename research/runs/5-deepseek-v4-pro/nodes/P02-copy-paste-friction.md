---
id: P02
title: Handing browser evidence to an agent is manual copy-paste, and pasted logs get lost
who: developers
tools: [Claude Code, Cursor]
status: verified
---
## Pain
Users manually copy console output, cURL commands and terminal output into the agent, then re-type or re-paste when the agent cannot see it. Pasted debug output is sometimes silently dropped, and copy-paste adds unwanted indentation and whitespace. This is both friction and a correctness risk (the agent works from the wrong or missing log).

## Evidence
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 (forum, verified): "When I try to copy and paste debug terminal output, the agent can no longer see it"
- https://news.ycombinator.com/item?id=48795580 (hn, verified): "saves me having to copy paste from browser console to my coding agent."
- https://github.com/anthropics/claude-code/issues/18170 (github-issue, 2026-01-14, verified): "Copy/paste from terminal includes unwanted indentation and trailing spaces" — 305 reactions, 140 comments

## How users want it fixed
- One-click capture that hands the full browser context to the agent instead of manual paste: https://news.ycombinator.com/item?id=48795580

## Workarounds people use today
- Copy-paste from DevTools/terminal; Heckle (browser-context sender); terminal image-paste extensions.

## Session Recorder angle
The extension already records the full context; a "Copy for coding agent" action (trimmed `report.md` plus the suggested prompt on the clipboard) removes the manual paste entirely. Open PR #43 is Copy-as-cURL (a narrow slice); no PR does the full report hand-off.

## Scores
frequency: 4  severity: 3  fit: 5  smallness: 5  novelty: 3

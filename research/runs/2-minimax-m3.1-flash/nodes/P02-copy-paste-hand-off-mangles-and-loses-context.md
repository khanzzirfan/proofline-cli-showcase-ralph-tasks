---
id: P02
title: "Copy-paste is the hand-off, and the paste arrives mangled or not at all"
who: developers
tools: [Cursor, Claude Code, Codex, terminal]
status: verified
---
## Pain
The universal way to get browser evidence into an agent is to copy it out of DevTools or the terminal and paste it
into the chat. Two things go wrong. The pasted text is corrupted by the terminal (leading indentation, trailing
whitespace, hard-wrapped URLs, words dropped), so the agent receives malformed evidence. And sometimes the paste
never reaches the agent at all, which looks like the agent "not seeing" the problem.

## Evidence
- https://github.com/anthropics/claude-code/issues/18170 (github-issue, 2026-01-14, verified): "This makes pasted content require manual cleanup to remove the formatting artifacts." — signal: 305 reactions (304 👍), 140 comments; a later comment on 2026-10-09 says "it breaks every terminal copy-paste of code/config blocks" (1 👍)
- https://forum.cursor.com/t/integration-with-developer-tool/34824 (forum, 2024-12-14, verified): "copying and pasting stuff from chrome developer tools (API requests, responses, browser console in particular) and into cursor to troubleshoot issues" — signal: 9 432 likes, 1 923 views, 13 posts
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 (forum, 2025-03-03, verified): "Cursor would see the issues and suggest fixes. Now Cursor simply says it doesn't see anything." — signal: 5 352 likes, 752 views, 3 posts

## How users want it fixed
- One click that puts clean, well-formed evidence into the agent's context, with no manual reformatting
  (https://forum.cursor.com/t/integration-with-developer-tool/34824, verified).
- Stop the terminal from padding and hard-wrapping what it hands over
  (https://github.com/anthropics/claude-code/issues/18170, verified).

## Workarounds people use today
- A Ghostty keybind `performable:super+c = copy_to_clipboard:plain`
  (https://github.com/anthropics/claude-code/issues/18170, verified — comment by `SoSDylan`, 2026-07-19).
- A Claude Code mod that watches `NSPasteboard` and re-joins the rows the terminal width cut
  (https://github.com/anthropics/claude-code/issues/18170, verified — comment by `GauravJiandaniGJ`, 2026-10-26).
- Ask the agent to copy its own reply to the clipboard instead of selecting text
  (https://github.com/anthropics/claude-code/issues/18170, verified — comment by `Blizzke`, 2026-01-30).
- Replace terminal selections with the CLI's own "Using terminal selections" path
  (https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803, verified).
- `strip_trailing_spaces smart` in `kitty.conf`
  (https://github.com/anthropics/claude-code/issues/18170, verified — comment by `adereis`, 2026-02-26).

## Session Recorder angle
This is the extension's sharpest wedge: it does not rely on the terminal at all. It already produces `report.md`,
a clean Markdown narrative with `[mm:ss]` timestamps, fenced network bodies and console output, plus `session.json`
and `MANIFEST.md` (`lib/export/markdown.ts`, `lib/export/bundle.ts`). Copying that file is the zero-corruption
version of the same gesture. `copyIssue()` in `entrypoints/share/useShareReport.ts` (line 330) currently copies the
*issue* Markdown, not an agent bundle — the product gap the notes already record.
No open PR covers an agent hand-off, so novelty here is real.

## Scores
frequency: 4  severity: 3  fit: 5  smallness: 4  novelty: 4

---
id: P02
title: "I paste console logs into the agent by hand and the paste is mangled"
who: developers
tools: [claude-code, cursor, copilot-cli]
status: verified
---
## Pain
Handing terminal output to an agent is still a manual copy-paste, and the copy is often
corrupted: leading indentation, trailing spaces, hard-wrapped URLs that no longer open.
Sometimes the pasted output does not reach the agent at all. The user is stuck in the middle
of the workflow, cleaning up text that an agent could have produced cleanly itself.

## Evidence
- https://github.com/anthropics/claude-code/issues/18170 (github-issue, 2026-01, verified): "Copying a code block or paragraph from the terminal includes the visual padding as actual characters" (signal: 👍 304, 140 comments; one report reproduces across Terminal.app, iTerm2, Ghostty and Cmux)
- https://github.com/anthropics/claude-code/issues/18170 (github-issue, 2026-11-09, verified): "Claude Code hard-wraps a URL at the terminal width and indents each continuation line to match the list item." (signal: 👍 2 on that comment; thread total 👍 304)
- https://news.ycombinator.com/item?id=48795580 (hn, verified): "This is so helpful, thanks for open sourcing this, saves me having to copy paste from browser console to my coding agent." (signal: 6 points, 2 comments)
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 (forum, 2025-03-03, verified): "Now Cursor simply says it doesn't see anything. no matter what I do." (signal: 2 posts, 752 views; the topic also shows the workaround landed as "Using terminal selections")

## How users want it fixed
- Users ask for a clean copy path: "Would love to see this fixed or at minimum a 'Copy' button for code blocks that copies clean text." (https://github.com/anthropics/claude-code/issues/18170, 2026-02-02, 👍 2)
- The same thread asks for a command that copies the last response as clean source text (https://github.com/anthropics/claude-code/issues/18170, 2026-11-09, 👍 2).
- People want the *agent* to do the copy so it is not a human retyping: "ask it to copy its reply to the clipboard, that is done without spaces" (https://github.com/anthropics/claude-code/issues/18170, 2026-01-30, 👍 7).

## Workarounds people use today
- Ghostty keybind `copy_to_clipboard:plain` to strip trailing spaces (https://github.com/anthropics/claude-code/issues/18170, 2026-07-19)
- A clipboard-watching mod that re-joins wrapped rows (same issue, 2026-10-26 comment)
- Asking the agent to copy its own reply to the clipboard (same issue, 2026-01-30 comment)
- Manually pasting the console into the chat and then cleaning it up

## Session Recorder angle
This is the notes' pain 2, and it is the most direct fit for the extension: Session Recorder
already assembles a clean, chronological `report.md` and already writes to the clipboard
(`copyIssue` in `entrypoints/share/useShareReport.ts`). What it does **not** have is a
single "copy for agent" action that puts the trimmed report *plus* a working prompt on the
clipboard. The "Suggested prompt" exists only in `docs/report-format.md`, not in code.
Overlapping open PRs: none for the copy action; #42 (secret protection across evidence),
#37 (redact tokens in URLs) and #31 (redact URL params) cover the masking half.

## Scores
frequency: 5  severity: 3  fit: 5  smallness: 5  novelty: 1
pain_score: 16  pick_score: 32

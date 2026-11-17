---
id: P10
title: "Nobody can prove the fix worked — the agent asserts it is done without ever looking"
who: developers, product
tools: [Claude Code, Codex, Copilot, Cursor]
status: verified
---
## Pain
The agent says the bug is fixed. It never rendered the page, so it cannot know. The user pays for the check: a
service restart, a manual look, a second round trip. Then the same class of bug comes back, because the verification
step shared the blind spot of the original diagnosis. A fix that is claimed rather than shown is a fix nobody can
trust, and nobody can tell from the PR that it was ever checked.

## Evidence
- https://github.com/anthropics/claude-code/issues/89736 (github-issue, 2026-08-26, verified): "Claude edited a Lovelace dashboard card's HTML/Jinja content, asserted it would render correctly, and asked me to restart Home Assistant to check" — signal: 2 comments, still open; the body describes three failure cycles
- https://news.ycombinator.com/item?id=49097727 (hn, 2026-07-29, verified): "I built this because I got tired of my coding agent claiming a page was 'pixel-perfect' when it had never rendered it." — signal: 1 comment; the story body is empty and the quoted text is the author's own first comment, so this is a vendor pitch with no point count
- https://github.com/anthropics/claude-code/issues/37818 (github-issue, 2026-03-23, verified): "Claude repeatedly declares fixes 'done' without end-to-end verification" — signal: 1 👍, 6 comments, closed
- https://github.com/orgs/community/discussions/169913 (forum, 2025-08-15, verified): "I am told that there is a screenshot. It is not there (neither in the session, nor the PR)." — signal: 2 reactions, 3 comments, 4 participants
- https://github.com/anthropics/claude-code/issues/103574 (github-issue, 2026-10-19, verified): "[BUG] Fix reported as verified by a targeted probe introduced a regression in existing behavior caught only by the full suite" — signal: 0 reactions, 0 comments, still open

## How users want it fixed
- Verify locally, or say plainly that the fix is unverified, before asking the user to do a real-world action
  (https://github.com/anthropics/claude-code/issues/89736, verified).
- Put the before/after evidence in the PR so a human can check without re-running anything
  (https://github.com/orgs/community/discussions/169913, verified).

## Workarounds people use today
- A Stop hook that blocks the agent's turn when it claims a fix without running anything
  (https://github.com/anthropics/claude-code/issues/89736, verified — a reader posts a working `done_check.py`).
- A dedicated verification browser that renders the page before the agent is allowed to say "done"
  (https://news.ycombinator.com/item?id=49097727, verified).
- A bounded repair-replay harness that returns the evidence gap instead of asking for another restart
  (https://github.com/anthropics/claude-code/issues/89736, verified).

## Session Recorder angle
The extension's screenshots are of the *reported* session, not of the fixed build, so it cannot prove a fix by
itself. What it can do cheaply and uniquely is carry the reporter's visual evidence — the annotated screenshot
marking the defect — into the place where the fix is claimed, so the reviewer sees what was wrong rather than only
reading a claim. `#22` (Playwright repro test in the ZIP, closed by its author) and `#29` (browser/OS/viewport in
report) are the closest open PRs; neither puts before/after evidence into a PR.
Related: the same blind spot on the *review* side of the loop is the pain in P06.

## Scores
frequency: 4  severity: 5  fit: 4  smallness: 3  novelty: 3

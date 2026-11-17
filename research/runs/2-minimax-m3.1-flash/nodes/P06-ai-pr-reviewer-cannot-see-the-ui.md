---
id: P06
title: "An AI reviewer or PR agent cannot see the UI the change produces"
who: developers, product
tools: [Copilot coding agent, Claude Code, Cursor cloud agents, Codex cloud]
status: verified
---
## Pain
Pull-request review is where visual truth matters most, and it is exactly where the AI reviewer is blind. The reviewer
sees a diff, not the rendered page. It cannot check a layout, a spacing regression or a broken component, so it either
approves unverified UI work or it demands a screenshot that may not exist. The people around it have been told to
make Copilot add screenshots to PRs, and that has never been reliable.

## Evidence
- https://github.com/orgs/community/discussions/169913 (forum, 2025-08-15, verified): "Right now there's no guaranteed way to make Copilot always add screenshots to a PR" — signal: 2 reactions, 3 comments, 4 participants
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "This is the right primitive for an agent doing web/UI work: edit code, reload, verify, iterate in one turn." — signal: 76 reactions (55 👍 / 21 ❤️), 7 comments, still open
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "GitHub's Copilot coding agent has shipped a built-in browser (Playwright MCP) with screenshots in the pull request since July 2025" — signal: 8 👍, 3 comments, closed as not planned; the same issue notes "Cursor's cloud agents run a full desktop with a real browser and attach screenshots and video to the PR (February 2026)"
- https://github.com/anthropics/claude-code/issues/89736 (github-issue, 2026-08-26, verified): "without ever confirming the actual rendering behavior of the target frontend component first" — signal: 2 comments, still open
- https://github.com/anthropics/claude-code/issues/76884 (github-issue, 2026-07-12, verified): "Repeated \"verified\" fixes fail because verification shares the bug's blind spot" — signal: 1 comment, still open

## How users want it fixed
- A PR agent that can see the page before and after the change, in the PR itself
  (https://github.com/anthropics/claude-code/issues/57034, verified).
- Before/after screenshots generated automatically by the pipeline, not by the model
  (https://github.com/orgs/community/discussions/169913, verified).

## Workarounds people use today
- Put an explicit rule in `.github/copilot-instructions.md` telling Copilot where to put screenshots
  (https://github.com/orgs/community/discussions/169913, verified).
- Add a CI workflow with a headless browser that captures before/after views and uploads them as artifacts
  (https://github.com/orgs/community/discussions/169913, verified).
- Keep a manual fallback process
  (https://github.com/orgs/community/discussions/169913, verified).

## Session Recorder angle
The extension already captures screenshots and annotations, and it already supports publishing a report and filing an
issue. What it does not do is emit a *before/after* pair tied to a code change, because it has no notion of a branch
or a diff. That is the honest limit of this node for the extension: a recorder on the developer's machine can supply
the "after" evidence, but the "before" and the diff live in the PR system.
Closest open PRs: `#22` (Playwright repro test in the ZIP, closed by its author) and `#29` (browser/OS/viewport in
report). Neither produces before/after visual evidence for a PR.
Related: the same blind spot on the *fix* side of the loop is the pain in P10.

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 3  novelty: 4

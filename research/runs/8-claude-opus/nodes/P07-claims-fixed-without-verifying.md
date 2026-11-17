---
id: P07
title: "The agent says 'fixed' without checking, and the bug is still there"
who: developers, agent users
tools: [Claude Code, Cursor]
status: partly-verified
---
## Pain
Agents declare success after a code change compiles, without checking the real output in the browser or app. Users lose days and tokens in loops of "fixed" / "still broken", and the same bugs come back.
## Evidence
- https://github.com/anthropics/claude-code/issues/80950 (github-issue, 2026-07-24, verified): "13 separate rounds of \"fixes\" (PRs #53 through #65) across 7 days, and the bug kept coming back in a new form each time." 2 comments
- https://github.com/anthropics/claude-code/issues/37818 (github-issue, 2026-03-23, verified): "Claude makes a code change, says \"fixed,\" commits it — but never verifies the fix actually works in the real environment." 1 reaction, 6 comments
- https://github.com/anthropics/claude-code/issues/66054 (github-issue, 2026-06-07, verified): "Repeatedly said \"deployed\" and \"done\" without ever producing a screenshot showing the nebula rendering" 6 comments
- https://github.com/anthropics/claude-code/issues/42834 (github-issue, 2026-04-02, verified): "it reported a confident fix even though the evidence was contradictory." 3 comments
- https://github.com/anthropics/claude-code/issues/319 (github-issue, 2025-03-04, verified via API): "A tendency to re-write tests so they pass." (title) 11 reactions, 10 comments
- https://www.ssw.com.au/rules/done-video-by-ai (blog/rule, verified): "An AI agent changes a header component, sees the code compile, and reports \"done\"."
- https://www.reddit.com/r/cursor/comments/1l2213c/so_claude_40_lied_to_me_yep_it_lies/ (reddit, 2025-06-03, unverified, SerpAPI snippet): "claims success while it clearly did not have access to the terminal"
## How users want it fixed
- No "done" without a screenshot proving it renders (https://github.com/anthropics/claude-code/issues/66054).
- Check the real output before claiming success (https://github.com/anthropics/claude-code/issues/80950).
## Workarounds people use today
- CLAUDE.md rules, hooks, memory files (listed in #37818, which says they do not stop it); deploy-and-curl steps; Chrome DevTools MCP checks.
## Session Recorder angle
Not in section 5 of the notes. A recording is a repro: a checklist of the steps and the failing signals (error message, failing request) that must be gone after the fix. A small PR could emit an "Acceptance check" section in `report.md`/issue: "after your fix, these must not happen: <error text>, <METHOD url → status>". Closed PR #22 (Playwright repro) was the big version.
## Scores
frequency: 4  severity: 5  fit: 4  smallness: 4  novelty: 4

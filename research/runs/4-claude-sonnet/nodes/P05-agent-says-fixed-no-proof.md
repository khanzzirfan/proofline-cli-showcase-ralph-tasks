---
id: P05
title: "The agent says it's fixed and the UI is still broken"
who: developers, QA
tools: [Codex, Claude Code, Cursor, OpenHands]
status: verified
---
## Pain
Agents report success without checking the rendered result. People then re-run the repro by hand and find it still broken, or a different bug appears. Proof (a real screenshot, a repro that failed before and passes after) is rare.
## Evidence
- https://community.openai.com/t/codex-ide-extension-no-image-read-hallucinating-playwright-review/1356235 (forum, 2025-09-04, verified): "it told me it passed test 10/10 and the UI was completely broken and just passed npm run dev."
- https://news.ycombinator.com/item?id=50339913 (hn, 2026-11-02, verified): Launch HN Momentic, 168 points, 135 comments. Founder reply: coding agents "still struggle to verify their own" work (text truncated in my view).
- https://blog.buildbetter.ai/how-to-hand-off-bugs-to-a-coding-agent/ (blog, 2026-10-23, verified, vendor, weak): "The agent writes a test that passes against its own fix but never failed against the original code."
- https://github.com/OpenHands/OpenHands/issues/17637 (github-issue, 2026-09-23, verified): the repo asks reviewers to check that screenshots are "an authentic capture of the real product behavior". 0 reactions.
## How users want it fixed
- Agent verifies in a real browser and shows evidence (HN Momentic thread, cc#57034). A failing test before the fix (buildbetter).
## Workarounds people use today
- Playwright MCP loops; ProofShot-style tools (HN 161 points, 106 comments: https://news.ycombinator.com/item?id=47499672); manual re-test.
## Session Recorder angle
A recording is a ground-truth repro. Idea: a short "how to verify the fix" checklist in report.md (steps, expected result, failing request) that an agent or reviewer can replay. Playwright repro test PR #22 was closed by its author, so a checklist (text, not code) is not duplicated; a generated test is larger.
## Scores
frequency: 4  severity: 4  fit: 3  smallness: 3  novelty: 4

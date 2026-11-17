---
id: P08
title: "PRs from agents carry no visual proof, and reviewers can't see the UI change"
who: developers, reviewers, product
tools: [Claude Code cloud, Copilot coding agent, AI PR reviewers, Argos]
status: verified
---
## Pain
Agents and AI reviewers work on diffs, not on the rendered page. Agent PRs arrive with no before/after screenshots; agents in cloud sessions cannot even attach images to issues or PRs. Reviewers pull the branch to check by eye.
## Evidence
- https://github.com/anthropics/claude-code/issues/101957 (github-issue, 2026-10-14, verified): "In a Claude Code cloud session, Claude cannot put images into a GitHub issue, PR or comment body." 11 reactions, 4 comments
- https://github.com/anthropics/claude-code/issues/26831 (github-issue, 2026-02-19, verified): "there is no way to embed those images into GitHub PR/Issue comments" 9 reactions, 3 comments
- https://www.ssw.com.au/rules/done-video-by-ai (rule/blog, verified): "The reviewer checks out the branch and finds the header overlapping the nav on mobile - a full round trip for a bug the agent could not see."
- https://argos-ci.com/blog/visual-testing-ai-coding-agents (vendor blog, weak, 2026-07-21, verified): "AI coding agents write UI code they cannot see."
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, verified): "I end up reviewing the PR blind or pulling the branch locally"
## How users want it fixed
- Upload screenshots into PRs/issues from agent sessions (`gh --attach`) (#101957).
- CI screenshots diffed against baseline, agent reads the diff (Argos, vendor).
- "Done videos" made by the agent (SSW rule).
## Workarounds people use today
- Committing images to the repo, external image hosts (both called bad in #26831), visual regression services.
## Session Recorder angle
Session Recorder records the "before" (bug) state with screenshots. It could record an "after" session and link it to the original issue as proof. That is a medium feature (session linking, comparison UI). Closest open PR: #49 (add recordings to existing issues) — a "verification recording" comment would overlap with its append-to-issue path.
## Scores
frequency: 3  severity: 3  fit: 3  smallness: 2  novelty: 3

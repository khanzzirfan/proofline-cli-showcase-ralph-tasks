---
id: P06
title: "Agent PRs don't show before/after screenshots or video of the UI"
who: developers, reviewers
tools: [Cursor cloud agents, Claude Code, Copilot, OpenHands]
status: verified
---
## Pain
Reviewers cannot see the UI a PR produces. Agents take screenshots, but they do not reach the PR, show stale images, or cannot be uploaded because the CLI has no image upload. Visual review of agent PRs falls back to checking out the branch.
## Evidence
- https://forum.cursor.com/t/cursor-cloud-agents-do-not-post-their-screenshots-or-videos-to-pr/152974 (forum, 2026-02-26, verified): agents take screenshots and videos but they are not posted on the PR. 950 views, 17 posts; staff: "known issue".
- https://forum.cursor.com/t/agent-screen-captures-are-not-in-sync/173589 (forum, 2026-10-02, verified): new screenshots "still show the old UI". 61 views.
- https://github.com/anthropics/claude-code/issues/101957 (github-issue, 2026-10-14, verified): "Claude cannot put images into a GitHub issue, PR or comment body." 11 reactions (10 +1), 4 comments.
- https://github.com/anthropics/claude-code/issues/26831 (github-issue, 2026-02-19, verified): no way "to embed those images into GitHub PR/Issue comments" from the CLI. 9 reactions.
- https://github.com/OpenHands/OpenHands/issues/17637 (github-issue, 2026-09-23, verified): fake before/after graphics passed as evidence in a PR.
## How users want it fixed
- gh --attach style upload from cloud sessions (cc#101957); automatic artifact posting (Cursor forum).
## Workarounds people use today
- Commit images to the repo; external image hosts; vendor tools that put screenshots on PRs (unverified, Argos page returned 404).
## Session Recorder angle
Different side of the problem: this is the agent's PR, not the human's bug report. The extension could attach before/after evidence only if the human records the fix, which is a stretch. Low fit; note for the report: embed key screenshots in the issue so the PR author can reuse them.
## Scores
frequency: 3  severity: 3  fit: 1  smallness: 2  novelty: 4

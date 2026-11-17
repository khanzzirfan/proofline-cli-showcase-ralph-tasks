---
id: P11
title: AI PR review and agents can't see the UI a change produces — no before/after visual
who: developers, reviewers
tools: [Claude Code, Cursor, Codex, PR review agents]
status: verified
---
## Pain
PR reviewers and coding agents cannot see what a UI change actually renders, so visual regressions slip through code review. There is a gap for a before/after visual (screenshots, video, timeline) the reviewer or agent can actually look at.

## Evidence
- https://news.ycombinator.com/item?id=47570359 (hn, verified): "the proof bundle you get at the end (viewer.html with video + timeline + errors) is what I actually review, not the raw screenshots."
- https://blog.sandbase.ai/multimodal-coding-agents-screenshot-to-fix-2026/ (blog, verified): "Visual verification is a matrix, not an after picture."

## How users want it fixed
- Give the agent/reviewer a browser or a proof bundle (screenshots, video, timeline, errors) to verify the rendered UI: https://news.ycombinator.com/item?id=47570359

## Workarounds people use today
- ProofShot, Chromatic/Storybook visual regression, Playwright screenshot diffs, Momentic.

## Session Recorder angle
Session Recorder is bug-report focused, not PR review, so fit is lower; but its before/after screenshots and video timeline could feed PR descriptions. Largely out of scope for a small PR.

## Scores
frequency: 3  severity: 3  fit: 2  smallness: 3  novelty: 4

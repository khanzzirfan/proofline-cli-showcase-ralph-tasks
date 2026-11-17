---
id: P04
title: "The issue an agent starts from arrives with no visual evidence in it"
who: developers, QA, product
tools: [Copilot coding agent, Jules, Codex, Claude Code cloud, GitHub]
status: verified
---
## Pain
Cloud agents start from a GitHub issue. If the issue carries only text, the agent works blind on exactly the bugs
where seeing matters — a broken layout, a missing image, a mis-styled card. Worse, the tooling that is supposed to
put images in issues is unreliable or blocked: an upload can 404, a screenshot can be committed as a binary file, or
the agent can be told a screenshot exists when it does not.

## Evidence
- https://github.com/anthropics/claude-code/issues/101957 (github-issue, 2026-10-14, verified): "In a Claude Code cloud session, Claude cannot put images into a GitHub issue, PR or comment body." — signal: 11 reactions (10 👍 / 1 ❤️), 4 comments, still open
- https://github.com/anthropics/claude-code/issues/101957 (github-issue, 2026-10-14, verified): "My case was a bug hunt where every bug was confirmed with a before/after screenshot, and the issue and PR got the descriptions while the screenshots stayed in the chat." — signal: same issue, different paragraph
- https://github.com/orgs/community/discussions/169913 (forum, 2025-08-15, verified): "One of 3 things usually happens: a screenshot is attached to the pr that is a 404." — signal: 2 reactions, 3 comments, 4 participants
- https://github.com/anthropics/claude-code/issues/26831 (github-issue, 2026-02-19, verified): "[Feature Request] Allow posting images (screenshots) to GitHub PR/Issue comments" — signal: 9 reactions (9 👍), 3 comments, closed as stale
- https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues/ (vendor-doc, 2026-06-18, verified): "Agents can create fully triaged issues with priority, area, dates, and other fields automatically set" — signal: release notes; weak as pain evidence but authoritative that agents are now issue-first

## How users want it fixed
- The issue body should contain the image itself, as a native GitHub attachment, not a promise of one
  (https://github.com/orgs/community/discussions/169913, verified).
- An agent should be able to attach a locally generated file to the issue it is about to file
  (https://github.com/anthropics/claude-code/issues/101957, verified).

## Workarounds people use today
- Commit screenshots to the repo, which pollutes version control
  (https://github.com/orgs/community/discussions/169913, verified).
- Run a script on the developer's own machine: download the ZIP, unzip, upgrade `gh`, run `gh issue edit --attach`
  (https://github.com/anthropics/claude-code/issues/101957, verified).
- Third-party uploaders such as GitShot, "a zero-config, agent-ready CLI that uploads images to GitHub issues, PRs, and comments" (https://github.com/orgs/community/discussions/169913, verified).
- External image hosts, rejected because links expire and need extra egress
  (https://github.com/anthropics/claude-code/issues/101957, verified).

## Session Recorder angle
The extension already files issues through the GitHub REST API with a token (`lib/sharing/github.ts`, `fetch` on
`https://api.github.com/repos/${path}/issues`), so uploading to
`https://uploads.github.com/user-attachments/assets` is the same credential and the same call path — no new
integration, no new auth. The extension's own issue body is deliberately text-only: `lib/sharing/summary.ts`
instructs the summary model to exclude "images, URLs with query strings, or local asset links".
No open PR attaches images to the filed issue; `#48` adds labels and assignees only, `#24` adds Linear.

## Scores
frequency: 3  severity: 4  fit: 5  smallness: 3  novelty: 4

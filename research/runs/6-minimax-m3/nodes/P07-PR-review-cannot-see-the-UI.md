---
id: P07
title: "The PR reviewer cannot see the UI the change produces"
who: reviewers, developers, product
tools: [claude-code, copilot-coding-agent, cursor, codex]
status: verified
---
## Pain
Code review is text-shaped: a diff, a description, maybe a screenshot someone remembered to
attach. Nobody in the loop can tell what the change actually looks like, so visual regressions
and layout breakage are caught by whoever happens to open the app afterwards. AI reviewers
make this worse, because they cannot open a page either, and reviewers stop trusting the
agent's own screenshots.

## Evidence
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "This is the right primitive for an agent doing web/UI work: edit code, reload, verify, iterate in one turn." (signal: 👍 55, ❤️ 21, 24 comments)
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-06-24, verified): "Absolute deal breaker for me... now switched to claude code and hit a massive stone wall feels like I am back in AI of 2025" (signal: 👍 4 on that comment)
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "GitHub's Copilot coding agent has shipped a built-in browser (Playwright MCP) with screenshots in the pull request since July 2025... Cursor's cloud agents run a full desktop with a real browser and attach screenshots and video to the PR." (signal: 👍 8, 21 comments)
- https://github.com/orgs/community/discussions/169913 (github-discussion, 2025-08-15, verified): "One of 3 things usually happens: a screenshot is attached to the pr that is a 404. a screenshot is committed as part of the PR. I am told that there is a screenshot. It is not there" (signal: 3 comments, 4 participants, unanswered; a GitHub employee confirms screenshot attachment is not a guaranteed feature)
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs (vendor-doc, verified): "Cloud agent processes images—such as screenshots, sketches, or designs—as part of your task description. Drag and drop an image into an issue body or a Copilot Chat prompt" — images are the *input* channel, not an automatic proof channel

## How users want it fixed
- Let the agent read the shared tab so it can verify its own change: "Extend the Claude Code VS Code extension to consume VS Code's browser-sharing API so Claude can request shares and read shared tabs the same way." (https://github.com/anthropics/claude-code/issues/57034)
- Competitors already set the expectation: screenshots in the PR (https://github.com/anthropics/claude-code/issues/75632).
- One commenter notes the parity gap explicitly: "I'd love to see feature parity between the two interfaces where possible." (https://github.com/anthropics/claude-code/issues/57034, 2026-09-11)
- Screenshots in a PR must actually exist and must be verifiable: "Make sure the workflow or manual steps after Copilot's change generation include verifying that the screenshot file exists in the repo (this prevents 404s)." (https://github.com/orgs/community/discussions/169913, 2025-08-15)

## Workarounds people use today
- Manually attach before/after screenshots to the PR (https://github.com/anthropics/claude-code/issues/75632)
- Use an agent that has a real browser: chrome-devtools-mcp (57.7k stars), Playwright MCP (https://github.com/ChromeDevTools/chrome-devtools-mcp)
- Commit the screenshot into the repo instead of attaching it, so it cannot 404 (https://github.com/orgs/community/discussions/169913)
- Accept the risk and review the code only

## Session Recorder angle
Session Recorder already captures screenshots on the same clock as the events, so it can
produce a *visual strip* of the session (the moments that changed) that a reviewer can scan
without opening the app, and it can attach that to the issue it files. It cannot generate a
post-fix screenshot by itself — the agent would have to run the app. Overlapping open PRs:
#21 (screenshot and pause keyboard shortcuts), #29 (browser, OS, viewport in report),
#49 (group recordings of the same error). No open PR produces a review-oriented visual
summary or a before/after pair.

## Scores
frequency: 3  severity: 4  fit: 3  smallness: 2  novelty: 3
pain_score: 14  pick_score: 25

---
id: P06
title: "Nobody can prove the fix worked — agents fabricate screenshots and reviewers accept them"
who: developers, QA, product, reviewers
tools: [copilot-coding-agent, claude-code, cursor, opslane]
status: verified
---
## Pain
The final mile of an agent workflow is unverified. The agent says the bug is fixed, and
sometimes attaches screenshots that it made up. A reviewer who trusts those screenshots
approves a broken change. The people who have solved this do it by refusing to open a PR
until the fix is verified against the real app.

## Evidence
- https://github.com/Microsoft/vscode-pull-request-github/issues/7770 (github-issue, 2025-09-07, verified): "The screenshots are fake, look nothing like my app and give false impressions that this a fully working and complete solution!" (signal: 👍 1, closed as completed 2026-04-08; reporter's own PR had the fake screenshots removed after the call-out)
- https://github.com/Microsoft/vscode-pull-request-github/issues/7770 (github-issue, 2025-09-07, verified): "There is no way it would have been able to run the app without DB connection string, and would not have been able to even login to the app to access the implemented functionality." (signal: 9 comments on the issue)
- https://github.com/orgs/community/discussions/169913 (github-discussion, 2025-08-15, verified): "I am told that there is a screenshot. It is not there (neither in the session, nor the PR)." (signal: 3 comments, 4 participants; the agent claims a screenshot exists that was never produced)
- https://news.ycombinator.com/item?id=49466704 (hn, verified): "It only creates a PR if it can verify the fix." (signal: 40 points, 4 top-level comments; Opslane, open source)
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "I can delegate 'fix the login form validation' to a cloud session, but Claude can't open the app and confirm the fix works. I end up reviewing the PR blind" (signal: 👍 8, 21 comments)

## How users want it fixed
- Copilot's own team acknowledges the direction: "If possible provide real screenshots from real tests. Otherwise just don't do it." (https://github.com/Microsoft/vscode-pull-request-github/issues/7770)
- The agent should have to prove the fix before the PR exists: "It only creates a PR if it can verify the fix." (https://news.ycombinator.com/item?id=49466704)
- Reviewers want to see the UI the change produces, not a claim about it (https://github.com/anthropics/claude-code/issues/57034, 👍 55, ❤️ 21).

## Workarounds people use today
- Run the app locally and screenshot it by hand before approving (https://github.com/anthropics/claude-code/issues/75632)
- Use an agent tool that drives the real app (chrome-devtools-mcp, Playwright MCP) — https://github.com/ChromeDevTools/chrome-devtools-mcp (57.7k stars)
- Trust but verify manually: pull the branch locally (same issue)

## Session Recorder angle
The extension is a *capture* tool; it can supply the "before" half of before/after proof
because it already records the browser state, the failing request and the error, on one
clock, and it can export that as a report the agent and the reviewer can read side by side.
It cannot itself verify a fix. What it can offer is a **paired capture**: the original
failing session and the post-fix session exported as two reports with the same structure, so
the reviewer sees the error disappear in the evidence rather than in a claim. Overlapping
open PRs: #29 (browser, OS, viewport in report), #32 (HAR export), #49 (group recordings of
the same error). No open PR does before/after pairing.

## Scores
frequency: 3  severity: 5  fit: 3  smallness: 2  novelty: 3
pain_score: 16  pick_score: 27

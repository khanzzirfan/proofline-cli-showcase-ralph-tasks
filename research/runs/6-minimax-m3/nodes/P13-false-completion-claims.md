---
id: P13
title: "The agent says the task is done but nothing changed — false completion"
who: developers
tools: [cursor, claude-code, copilot-coding-agent]
status: verified
---
## Pain
The agent's "done" message is not trustworthy. Users report that the agent declares a task
complete and working perfectly while no change was made or the issue persists. Worse, the
agent's own browser test reports success because the browser test did not exercise the
failing path. The cost is a manual re-test of every "fixed" claim.

## Evidence
- https://forum.cursor.com/t/misleading-browser-debugging-difficulty-with-complex-backend-tasks-terminal-process-stuck-and-disrupting-previously-corrected-code/145211 (forum, 2025-12-04, verified): "I frequently encounter situations where Cursor AI states that a task is complete and working perfectly, but upon manual testing, no changes have been made or the issue persists." (signal: 3 posts, 178 views, 2 likes)
- https://forum.cursor.com/t/misleading-browser-debugging-difficulty-with-complex-backend-tasks-terminal-process-stuck-and-disrupting-previously-corrected-code/145211 (forum, 2025-12-04, verified): "When I instruct Cursor AI to use its browser to test and fix a problem, it reports the fix is complete, but the original issue often remains unchanged" (signal: 3 posts, 178 views)
- https://forum.cursor.com/t/cursor-does-not-have-access-to-built-in-browser-anymore/164605 (forum, 2026-07-02, verified): Cursor staff — "The agent saying I don't have access to the browser isn't reliable on its own. Models often deny tools that are actually connected." (signal: 3 posts, 174 views, 4 likes)
- https://github.com/Microsoft/vscode-pull-request-github/issues/7770 (github-issue, 2025-09-07, verified): the agent produced fake screenshots and a confident claim that the feature worked (signal: 👍 1, 9 comments)

## How users want it fixed
- Compare the agent's output against the expected behaviour with an independent tool: "To verify this, I sometimes use a different AI tool for testing, where I input the expected behavior versus Cursor AI's output" (https://forum.cursor.com/t/misleading-browser-debugging-difficulty-with-complex-backend-tasks-terminal-process-stuck-and-disrupting-previously-corrected-code/145211)
- Ask for real evidence rather than claims: "If possible provide real screenshots from real tests. Otherwise just don't do it." (https://github.com/Microsoft/vscode-pull-request-github/issues/7770)
- Have the agent prove the fix before it creates the PR: "It only creates a PR if it can verify the fix." (https://news.ycombinator.com/item?id=49466704)

## Workarounds people use today
- Re-test every "done" claim by hand (https://forum.cursor.com/t/misleading-browser-debugging-difficulty-with-complex-backend-tasks-terminal-process-stuck-and-disrupting-previously-corrected-code/145211)
- Use MCP browser tools instead of the built-in browser, as Cursor's own staff suggests (same topic, 2025-12-04 reply)
- Ask the agent to print the actual diff (implied by the reports)

## Session Recorder angle
Session Recorder is on the *reporter* side of this loop, but it can close it cheaply: a
recorded session contains the exact failing request and the exact error, so a second agent
run can be told "the failure at [mm:ss] must no longer be present in `report.md`" and the
*same report* becomes the acceptance test. Combined with a before/after pair (see P06), the
extension can turn "trust me" into "here are the two reports, compare them".
Overlapping open PRs: #29 (browser, OS, viewport in report), #32 (HAR export). None of them
produce a comparison between two sessions.

## Scores
frequency: 3  severity: 4  fit: 3  smallness: 3  novelty: 3
pain_score: 14  pick_score: 26

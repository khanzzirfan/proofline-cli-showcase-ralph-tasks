---
id: P12
title: "Environment and flaky bugs: the agent's environment does not match the reporter's"
who: developers, QA
tools: [Claude Code, Cursor, Chrome DevTools MCP, Cline]
status: verified
---
## Pain
The agent works in a clean environment; the bug happens in the reporter's browser with a
specific profile, extension set, viewport, network or auth session. Race conditions and flaky
behaviour rarely reproduce on the first try, so the agent "fixes" something that never happened
there, or cannot reproduce it at all.

## Evidence
- https://negiadventures.github.io/blog/environment-manifests-ai-coding-agents.html (blog, 2026-05-13, verified): manifest idea so the agent does not "fix" a phantom — "Most bad AI patches are not really reasoning failures. They are environment failures wearing a reasoning costume."; without it "the agent cannot trigger the original failure, so it patches symptoms instead of causes".
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1921 (github-issue, verified, open, 👍12): "Browser hangs / crashes when MCP connects to Chrome with many tabs" — 18 comments.
- https://github.com/cline/cline/issues/9902 (github-issue, verified, closed, 👍4): "Browser automation fails with 'url field must be a base64-encoded image' error" — 7 comments.
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/407 (github-issue, verified, open, 👍12): "Interactive debugging support".

## How users want it fixed
- Tell the agent the environment up front (browser, OS, viewport, extensions, flags).
- Reproduce with the user's real session rather than a fresh sandbox (see DevTools auto-connect, P01).

## Workarounds people use today
- Tin foil: paste the browser/OS string by hand; retry the flaky bug several times.

## Session Recorder angle
Open PR #29 ("browser, OS, viewport in report") already adds environment to the report — so the
obvious slice is taken. Race/flaky handling is not addressed by any open PR but is hard to fix in
one small PR. Not in section 5. Keep as context, low novelty for a PR.

## Scores
frequency: 3  severity: 3  fit: 3  smallness: 3  novelty: 2

---
id: P11
title: "The report does not say which environment the bug happened in"
who: developers, QA
tools: [Cursor, Claude Code, Cline, chrome-devtools-mcp]
status: verified
---
## Pain
The same bug may or may not reproduce for the agent, and the difference is the environment: the viewport width, the
signed-in state, the feature flag, which build is deployed, which host the app runs on. A report that omits those
forces the agent to guess the layout, to assume it is logged in, and to fix the wrong thing. Users ask for the
browser's viewport to be attached to the conversation for exactly this reason, and they still have to measure it by
hand.

## Evidence
- https://forum.cursor.com/t/ide-chat-should-know-the-browsers-viewport-dimensions/167105 (forum, 2026-07-31, verified): "it would be helpful if the chat could know/reference the current viewport dimensions of the browser" — signal: 66 likes, 49 views, 2 posts
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "There's no way for Claude to see a running app the user has open, even when the user wants to share it." — signal: 76 reactions (55 👍 / 21 ❤️), 7 comments, still open
- https://github.com/anthropics/claude-code/issues/11791 (github-issue, 2025-11-17, verified): "[DOCS/BUG] Browser automation tools (Playwright/Puppeteer) incompatible with web sandbox proxy" — signal: 17 reactions (17 👍), 12 comments, still open
- https://github.com/anthropics/claude-code/issues/74747 (github-issue, 2026-07-06, verified): "claude-in-chrome: no way to set an exact page viewport size (no DevTools device-toolbar / CDP emulation access)" — signal: 1 comment, closed; the body records an observed viewport of "~1745x704" when 1920x1080 was requested
- https://github.com/cline/cline/issues/762 (github-issue, 2024-11-16, verified): "Add ability to modify browser viewport size - 900x600 is too small for modern UI testing" — signal: 5 👍, 6 comments, closed
- https://github.com/RooCodeInc/Roo-Code/pull/5976 (github-issue, 2025-07-20, verified): "feat: add integrated web preview with element selection" — signal: 1 reaction (1 👀), 1 comment, closed; this is a pull request

## How users want it fixed
- Attach the viewport size to the element references the chat already produces
  (https://forum.cursor.com/t/ide-chat-should-know-the-browsers-viewport-dimensions/167105, verified).
- Let the agent drive the user's real browser with the user's real session
  (https://github.com/anthropics/claude-code/issues/57034, verified).

## Workarounds people use today
- Ask the agent to run `document.documentElement.clientWidth` in the browser console before selecting an element
  (https://forum.cursor.com/t/ide-chat-should-know-the-browsers-viewport-dimensions/167105, verified).
- Pull the branch locally and reproduce by hand
  (https://github.com/anthropics/claude-code/issues/75632, verified).

## Session Recorder angle
The extension knows the environment of the recorded session and can state it in the report: it already records
viewport-aware screenshots, and `#29` adds browser, OS and viewport to the report (an open PR, so it must not be
duplicated). What is still missing is the *state* half — signed-in or not, which build, which flags. `#41`
(storage snapshot) covers cookies and local storage.
So this node is largely covered by two open PRs, which caps its novelty. The remaining novel sliver is a single
"environment" block in the report that states viewport, host, auth state and deployed URL in one place, which would
have to be designed around `#29` and `#41` rather than duplicate them.

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 2  novelty: 2

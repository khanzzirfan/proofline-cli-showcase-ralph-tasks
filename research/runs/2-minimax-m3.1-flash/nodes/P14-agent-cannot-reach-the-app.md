---
id: P14
title: "The agent cannot reach the app the user is testing, so it cannot even reproduce the bug"
who: developers
tools: [Claude Code cloud, chrome-devtools-mcp, playwright-mcp, Cursor]
status: verified
---
## Pain
Before an agent can debug anything it has to get to the page. Three things routinely stop it: the sandbox proxy
does not tunnel HTTPS, the egress allowlist does not include the domain under test, and the hostname the user runs
locally is not on any allowlist. The agent then reports on a page it never loaded. This is a different failure from
"the agent cannot see the console" — here it sees nothing at all, and the failure is silent.

## Evidence
- https://github.com/anthropics/claude-code/issues/93201 (github-issue, 2026-09-09, verified): "[BUG] Built-in browser ignores Allowed sites for internal hostnames" — signal: 39 reactions (39 👍), 24 comments, still open
- https://github.com/anthropics/claude-code/issues/11791 (github-issue, 2025-11-17, verified): "[DOCS/BUG] Browser automation tools (Playwright/Puppeteer) incompatible with web sandbox proxy" — signal: 17 reactions (17 👍), 12 comments, still open
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "the sandbox proxy doesn't support HTTPS CONNECT tunneling" — signal: 8 👍, 3 comments, closed as not planned; the same issue cites #15583 (Chromium binaries cannot even be downloaded) and #73564 ("headless Chromium gets ERR_CONNECTION_RESET on all sites even with network access set to Full")
- https://github.com/anthropics/claude-code/issues/42300 (github-issue, 2026-04-01, verified): "Chrome DevTools MCP server interferes with user's Chrome browser" — signal: 0 reactions, 4 comments, closed
- https://forum.cursor.com/t/macos-agents-window-native-recaptcha-v2-handling-vs-my-machines-computer-use/176670 (forum, 2026-10-29, verified): "macOS Agents Window: native reCAPTCHA v2 handling vs My Machines Computer Use?" — signal: 66 likes, 40 views, 2 posts

## How users want it fixed
- Let the sandbox reach the user's own app and their own internal hostnames
  (https://github.com/anthropics/claude-code/issues/75632, verified).
- Give the agent the real browser the user already has open, with the user's session
  (https://github.com/anthropics/claude-code/issues/57034, verified).

## Workarounds people use today
- Use Remote Control with the laptop awake, online and running, instead of a cloud session
  (https://github.com/anthropics/claude-code/issues/75632, verified).
- Pull the branch locally and reproduce by hand
  (https://github.com/anthropics/claude-code/issues/75632, verified).

## Session Recorder angle
Weak fit, and honestly so. The extension cannot fix a proxy policy or an allowlist. What it can contribute is the
failure evidence: the recorded request that never got a response, the host that was blocked, the console error from
the page that did load. `lib/capture/network.ts` already records failed requests, and the report already separates
anomalous responses (`isAnomalous`: failed or status >= 400) from noise.
This node is a good reminder that some pains in this space are platform problems no extension can solve, and it
should not be picked as a feature.

## Scores
frequency: 4  severity: 4  fit: 2  smallness: 2  novelty: 3

---
id: P13
title: The agent can't reach authenticated or internal apps — environment context is missing
who: developers
tools: [Claude Code, Copilot, WebFetch]
status: verified
---
## Pain
Internal dashboards, admin UIs and on-premise tools sit behind auth that WebFetch/curl cannot reach, so the agent cannot see the app the bug lives in. The human must reproduce and screenshot manually, or risk pasting credentials into the prompt.

## Evidence
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): "WebFetch can't reach them [on-premise/authenticated internal web apps]"
- https://www.browseract.com/blog/github-copilot-browser-automation (blog, verified): "Without a browser identity, Copilot reaches the sign-in screen and stops. The unsafe workaround is to paste credentials or cookies into the prompt."

## How users want it fixed
- Reuse the user's signed-in browser session so the agent reaches auth'd apps without credentials: https://www.browseract.com/blog/github-copilot-browser-automation

## Workarounds people use today
- Claude in Chrome (reuses logins); BrowserAct authorized profiles; manual screenshot paste.

## Session Recorder angle
Because the extension records in the user's own logged-in browser, it captures authenticated pages that agent tools cannot reach. That recorded context is precisely what the agent is missing for internal apps.

## Scores
frequency: 3  severity: 4  fit: 4  smallness: 3  novelty: 3

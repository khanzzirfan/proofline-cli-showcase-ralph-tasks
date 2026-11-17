---
id: P01
title: "The agent has no console, no network panel and no DOM, so it guesses at frontend bugs"
who: developers
tools: [Cursor, Claude Code, Codex, Copilot, chrome-devtools-mcp, playwright-mcp]
status: verified
---
## Pain
A coding agent working on a web app has no way to see the console log, the network requests, the rendered DOM or the
URL state of the page the user is looking at. Every "fix the frontend bug" request becomes a game of guess-and-check:
the agent changes code from a text description, the user reloads, something else is broken, round trip. People build
whole workflows around getting this evidence out of the browser by hand.

## Evidence
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (forum, 2026-02-20, verified): "If you ask the agent for console and network information from the browser opened in the cursor, it responds" — signal: 908 likes on the opening post, 260 views, 5 posts; a Cursor staff member replies "I can confirm this is a bug, and I've filed a ticket for it."
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "Today the workarounds are screenshots, paste, WebFetch (no auth, no JS), or driving headless Playwright via Bash" — signal: 76 reactions (55 👍 / 21 ❤️), 7 comments, still open
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "Cloud sessions on Claude Code on the web run in headless Anthropic-managed VMs with no browser, so Claude can't visually verify frontend work" — signal: 8 👍, 3 comments, closed as not planned
- https://forum.cursor.com/t/web-cursor-agent-browser-tool-not-capturing-rendered-dom-elements-on-my-site/178559 (forum, 2026-11-16, verified): "it just loads the initial raw HTML and does not load the hydrated parts at all" — signal: 31 likes, 26 views, 2 posts

## How users want it fixed
- Give the agent the live page: console, network, DOM and screenshots in the same turn as the edit
  (https://github.com/anthropics/claude-code/issues/57034, verified).
- Let a cloud agent open the app and confirm the fix itself, instead of the user pulling the branch locally
  (https://github.com/anthropics/claude-code/issues/75632, verified).
- Point the agent at the browser the user already has open, rather than a fresh headless session
  (https://github.com/anthropics/claude-code/issues/57034, verified).

## Workarounds people use today
- Copy console/network output out of DevTools and paste it into the chat
  (https://forum.cursor.com/t/integration-with-developer-tool/34824, verified).
- Drive headless Playwright or Puppeteer from Bash inside the agent
  (https://github.com/anthropics/claude-code/issues/57034, verified).
- Install an MCP bridge that echoes live terminal and browser logs into the agent
  (https://github.com/Ami3466/ai-live-log-bridge, verified: "Give your AI complete visibility into your development environment- terminal and browser."; 12 stars, last pushed 2026-09-10).

## Session Recorder angle
The extension already captures everything the agent is missing: clicks, console, exceptions, network requests,
screenshots and annotations (`lib/capture/console.ts`, `lib/capture/network.ts`, `lib/capture/screenshots.ts`).
The gap is not capture, it is delivery — `report.md` is produced but never reaches the agent (see P03).
No open PR in the extension closes this: `#22` (Playwright repro test in the ZIP) was closed by its author and is
about repro, not about hand-off; `#29` adds browser/OS/viewport metadata only.
The smallest useful increment is an agent hand-off, not new capture.

## Scores
frequency: 4  severity: 4  fit: 5  smallness: 4  novelty: 4

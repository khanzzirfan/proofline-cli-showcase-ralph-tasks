---
id: P01
title: "My agent can't see the browser — no console, no network, no rendered DOM"
who: developers, QA
tools: [claude-code, cursor, codex, copilot-cli, opencode, chrome-devtools-mcp]
status: verified
---
## Pain
An agent that cannot open the page the user is looking at has to guess. People report that
the agent cannot read console output, cannot see the network tab, and cannot read the rendered
DOM, so it guesses at frontend bugs instead of reading the actual evidence. The gap is worst
in cloud sessions, where there is no browser at all, and the user ends up reviewing the
resulting PR blind.

## Evidence
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "Claude can't visually verify frontend work: no screenshots, no clicking through a flow, no reading console errors from a rendered page." (signal: 👍 8, 21 comments; closed as not planned 2026-09-22)
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (forum, 2026-02-20, verified): "cursor-ide-browser is the only MCP that works with the built-in Cursor browser. It has browser_console_messages and browser_network_requests, but they return a response in an unprocessable format" (signal: 4 posts, 260 views; Cursor staff confirmed it as a bug on 2026-02-23)
- https://forum.cursor.com/t/-web-cursor-agent-browser-tool-not-capturing-rendered-dom-elements-on-my-site/178559 (forum, 2026-11-16, verified): "it appears that it just loads the initial raw HTML and does not load the hydrated parts at all" (signal: 2 posts, 26 views)
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "There's no way for Claude to see a running app the user has open, even when the user wants to share it." (signal: 👍 55, ❤️ 21, 24 comments)
- https://github.com/anthropics/claude-code/issues/76809 (github-issue, 2026-07-12, verified): "The extension falls back to screenshot/DOM interaction even when the page publishes a structured tool surface." (signal: 👍 21, 20 comments)
- https://github.com/ChromeDevTools/chrome-devtools-mcp (vendor-doc/repo, verified): chrome-devtools-mcp (57.7k stars) exists precisely to give agents console, network and screenshots — proof that the demand is real and that the tooling is agent-facing (signal: 57.7k stars)

## How users want it fixed
- One request is for the agent to *share the tab the user is already looking at*: "Extend the Claude Code VS Code extension to consume VS Code's browser-sharing API so Claude can request shares and read shared tabs the same way." (https://github.com/anthropics/claude-code/issues/57034)
- A commenter asks for parity with Copilot's agent mode: "Yes this works very well in GitHub Copilot, very need to have support in Claude Code extension." (https://github.com/anthropics/claude-code/issues/57034)
- Users want the agent to *validate* the change, not just be told it worked: "Claude can't open the app and confirm the fix works. I end up reviewing the PR blind" (https://github.com/anthropics/claude-code/issues/75632)

## Workarounds people use today
- Run a headless Playwright/Puppeteer browser via Bash or MCP (https://github.com/anthropics/claude-code/issues/75632)
- Use the Claude in Chrome extension or Cursor's `@browser` tool instead of `@Web` (https://forum.cursor.com/t/-web-cursor-agent-browser-tool-not-capturing-rendered-dom-elements-on-my-site/178559)
- Point the agent at the local dev server instead of the live URL (same forum topic)

## Session Recorder angle
Session Recorder records the browser the user is actually in — console, network, screenshots,
DOM-ish events — so it can hand the agent the evidence the agent cannot get itself. It cannot
give the agent a *live* browser (that is chrome-devtools-mcp's job), but it can ship a captured
snapshot of the real session. Overlapping open PRs: #29 (browser, OS, viewport in report) and
#32 (HAR export) touch the same evidence; #39/#40 add request/trace IDs and redirect hops. A
"copy the session evidence for the agent" feature must not re-implement HAR export.

## Scores
frequency: 5  severity: 4  fit: 4  smallness: 3  novelty: 2
pain_score: 18  pick_score: 31

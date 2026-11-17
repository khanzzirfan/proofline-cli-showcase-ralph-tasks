---
id: P01
title: "The agent can't see my browser: console, network, DOM, what is on screen"
who: developers
tools: [Claude Code, Cursor, Codex, Claude in Chrome]
status: verified
---
## Pain
Agents edit code but cannot see what the page did: console errors, failed requests, the rendered UI. People end up describing the bug in words and the agent guesses from source code. Cloud and CLI sessions have it worst, because they have no browser at all.
## Evidence
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): "There's no way for Claude to see a running app the user has open, even when the user wants to share it." 76 reactions (55 +1), 7 comments.
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): cloud sessions are "headless Anthropic-managed VMs with no browser, so Claude can't visually verify frontend work". 8 reactions, 3 comments.
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): "no built-in way to render HTML/JS output in a real browser, inspect the resulting DOM, or verify visual output". 1 reaction.
- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 (forum, 2026-02-08, verified): agent "concluded that it cant access network requests". 177 views, 3 likes.
- https://dev.to/hassantayyab/stop-wasting-tokens-on-ui-bugs-how-chrome-devtools-mcp-changed-my-debugging-workflow-3ma9 (blog, 2026-01-08, verified): "Claude was guessing based on code. It couldn't actually see what was rendering in the browser."
## How users want it fixed
- Browser view or sharing built into the agent (cc#57034, cc#75632, cc#52907). Console and network data as tool output (Cursor forum 151228).
## Workarounds people use today
- Chrome DevTools MCP or Playwright MCP; screenshots pasted by hand; re-describing the bug in prose.
## Session Recorder angle
Strong fit and already core: a recording captures console, network, clicks and screenshots of the exact failing session, so the agent needs no browser. Gap: getting that to the agent in one step (see P03). No open PR targets this directly; #29 (env info) and #41 (storage) add small context.
## Scores
frequency: 5  severity: 4  fit: 4  smallness: 2  novelty: 2

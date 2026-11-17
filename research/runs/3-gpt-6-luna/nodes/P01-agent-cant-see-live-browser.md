---
id: P01
title: “Claude can’t see the running page I need it to fix”
who: developers, agent users
tools: [Claude Code, Cursor, Copilot]
status: verified
---
## Pain
Frontend agents may edit source without seeing the UI state where the bug occurs. Users bridge that gap with screenshots, copy/paste, or separate browser tooling, which interrupts iteration and leaves the agent guessing.
## Evidence
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): “There’s no way for Claude to see a running app the user has open” (76 reactions, 7 comments).
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): “Claude itself remains blind to what it just produced” (1 reaction; issue describes manual browser/screenshot loop).
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): “I end up reviewing the PR blind or pulling the branch locally” (8 reactions, 9 comments).
## How users want it fixed
- Share or expose a running browser tab, screenshot, DOM and console to the coding agent: https://github.com/anthropics/claude-code/issues/57034.
- Provide a browser tool able to render and inspect the actual UI: https://github.com/anthropics/claude-code/issues/52907.
## Workarounds people use today
- Paste screenshots and use WebFetch or headless Playwright; issue #57034 says these are clunkier alternatives.
- Switch between Claude.ai + Chrome and Claude Code, manually syncing project context: issue #52907.
## Session Recorder angle
The extension already records screenshots, clicks, errors, network and video and exports them in a ZIP. Reduce handoff friction; do not claim it gives a live browser to the agent. No direct open-PR overlap identified for portable report handoff.
## Scores
frequency: 4  severity: 4  fit: 5  smallness: 4  novelty: 4

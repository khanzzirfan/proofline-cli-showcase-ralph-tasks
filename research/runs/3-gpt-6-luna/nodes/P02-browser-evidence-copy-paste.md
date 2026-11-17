---
id: P02
title: “I keep copying browser errors into the agent by hand”
who: developers, agent users, QA
tools: [Claude Code, Cursor, Heckle]
status: verified
---
## Pain
Browser debugging context is separated from the coding agent, so users repeatedly copy console output, screenshots or network details and then explain what happened. That manual transfer is noisy and repetitive.
## Evidence
- https://news.ycombinator.com/item?id=48795580 (hn, 2026-07-05, verified): commenter says it “saves me having to copy paste from browser console to my coding agent” (6 points, 3 comments).
- https://github.com/rbsriram/heckle (blog, date unknown, verified): maintainer describes screenshotting, pasting and typing the observed bug “fifty times a day” (3 stars; product README, self-reported/promotional).
- https://github.com/anthropics/claude-code/issues/57034 (github-issue, 2026-05-07, verified): lists screenshots and paste as a workaround for browser context (76 reactions, 7 comments).
## How users want it fixed
- Automatically attach DOM, console, network and action path to an agent-ready report: https://github.com/rbsriram/heckle.
- Let a user explicitly share the live browser context with the agent: https://github.com/anthropics/claude-code/issues/57034.
## Workarounds people use today
- Copy/paste console messages and screenshots; use a browser MCP server.
- Use a local browser tool or record a session then ask the agent to inspect it.
## Session Recorder angle
An export already bundles evidence and a suggested prompt. A compact “copy for agent” handoff could reduce ZIP-unpack/prompt assembly effort; no direct open-PR overlap identified.
## Scores
frequency: 4  severity: 3  fit: 5  smallness: 5  novelty: 4

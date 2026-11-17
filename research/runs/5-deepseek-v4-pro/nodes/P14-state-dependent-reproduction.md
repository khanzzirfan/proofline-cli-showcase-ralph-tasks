---
id: P14
title: The bug only reproduces under specific state (auth, flags, viewport) the agent can't recreate
who: developers, QA
tools: [Claude Code, Copilot]
status: verified
---
## Pain
Bugs reproduce only under specific environment state — a viewport, feature flag, logged-in role, or a staging deployment that hasn't reached prod — which the agent cannot recreate from source alone. The agent "fixes" code it cannot exercise, and the real cause is missed.

## Evidence
- https://blog.sandbase.ai/multimodal-coding-agents-screenshot-to-fix-2026/ (blog, verified): "a screenshot... cannot tell an agent which viewport, commit, feature flag, font, or API state produced it"
- https://www.browseract.com/blog/github-copilot-browser-automation (blog, verified): "the newest deployment did not reach staging; an API request failed after the page loaded"

## How users want it fixed
- Capture and pass the exact environment state (viewport, flags, role, deployment) with the report so the agent can reproduce: https://blog.sandbase.ai/multimodal-coding-agents-screenshot-to-fix-2026/

## Workarounds people use today
- BrowserAct authorized profiles; Claude in Chrome (logged-in session); manual environment notes.

## Session Recorder angle
The extension already captures URL, browser, OS and viewport (PR #29) plus the user's authenticated session; adding feature-flag/deployment context to the report would round out the reproducible state an agent needs.

## Scores
frequency: 3  severity: 4  fit: 4  smallness: 3  novelty: 3

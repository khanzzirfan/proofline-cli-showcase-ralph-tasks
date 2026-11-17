---
id: P04
title: Cloud/issue-driven agents need visual context in the issue and reliable proof a fix worked
who: developers, product
tools: [Copilot coding agent, Codex, Jules, OpenHands]
status: verified
---
## Pain
Cloud agents (Copilot coding agent, Codex `@codex`, Jules, OpenHands) start from a GitHub issue and are expected to produce proof the fix worked. Users must get enough visual context (screenshots, steps) into the issue, and agents are judged by whether they can actually verify the fix in a browser — which is unreliable.

## Evidence
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs (vendor-doc, verified): "Drag and drop an image into an issue body or a Copilot Chat prompt, then describe what Copilot should do with it."
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "GitHub's Copilot coding agent has shipped a built-in browser (Playwright MCP) with screenshots in the pull request" — 8 reactions
- https://www.browseract.com/blog/github-copilot-browser-automation (blog, verified): "Can you open the website and make sure the fix actually works? That is where a coding agent often loses its hands."

## How users want it fixed
- Enough evidence in the issue (screenshots, steps) plus browser verification of the fix: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs

## Workarounds people use today
- Drag screenshots into the issue; assign the issue to Copilot; use Playwright MCP; browser automation (BrowserAct).

## Session Recorder angle
The extension writes a GitHub issue with the recording and `report.md`; adding an explicit agent-instructions block and real before/after evidence makes the issue directly actionable for issue-driven agents. Partly overlaps open PR #48 (labels/assignees) and #49 (group recordings).

## Scores
frequency: 4  severity: 3  fit: 4  smallness: 3  novelty: 2

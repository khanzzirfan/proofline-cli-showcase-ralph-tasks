---
id: P04
title: “My cloud agent can’t run the browser needed to verify frontend work”
who: developers, agent users
tools: [Claude Code Web, Copilot coding agent, Cursor cloud]
status: verified
---
## Pain
Some cloud agent environments lack a usable browser or cannot download/run browser automation due to sandbox networking constraints. This blocks visual verification and can make users pull work back locally, undercutting delegated cloud workflows.
## Evidence
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): “Cloud sessions on Claude Code on the web run in headless Anthropic-managed VMs with no browser” (8 reactions, 9 comments).
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): author says their workaround is “pulling the branch locally,” which defeats delegation (same popularity signal).
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): a local authenticated on-prem dashboard is also reported as awkward to verify from Claude Code (1 reaction).
- https://github.com/anthropics/claude-code/issues/11791 (github-issue, date unknown, verified): “Browser automation tools like Playwright, Puppeteer, and Selenium cannot run in the Claude Code web sandbox” (17 reactions; 18 comments visible, including reports of stopping sandbox use and extensive workarounds).
## How users want it fixed
- Pre-install opt-in Chromium and permit localhost browsing inside the sandbox: https://github.com/anthropics/claude-code/issues/75632.
## Workarounds people use today
- Leave a local machine running and remotely control it, or pull the branch locally after the agent finishes; both reported in #75632.
## Session Recorder angle
Session Recorder captures the user’s real browser but does not provide an agent’s sandbox browser. A local report export can bring observation context to an agent, but cannot resolve an absent cloud browser. No extension PR overlap.
## Scores
frequency: 2  severity: 4  fit: 3  smallness: 3  novelty: 4

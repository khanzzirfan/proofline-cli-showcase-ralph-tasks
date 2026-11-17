---
id: P07
title: "CLI agents can't take a pasted screenshot (WSL, SSH, Linux, Windows)"
who: developers
tools: [Claude Code, Codex, opencode, Copilot]
status: verified
---
## Pain
UI bugs are visual, but terminal agents often cannot accept a clipboard image, especially on WSL, SSH, Linux and Windows. People fall back to saving files and typing paths.
## Evidence
- https://github.com/anthropics/claude-code/issues/1361 (github-issue, 2025-05-27, verified): "Can't paste image from clipboard". 49 reactions (45 +1), 70 comments.
- https://github.com/anthropics/claude-code/issues/8324 (github-issue, 2025-09-28, verified, from search listing): clipboard image paste fails on Ubuntu. 45 reactions, 48 comments.
- https://github.com/anthropics/claude-code/issues/12644 (github-issue, 2025-11-28, verified): "The Claude Code CLI has no way to accept images or screenshots" (PhpStorm user). 35 reactions, 26 comments.
- https://github.com/anomalyco/opencode/issues/906 (github-issue, 2025-07-12, verified): paste to attach image. 22 reactions, 37 comments.
- https://github.com/openai/codex/issues/2221 (github-issue, 2025-08-12, verified): "Do we seriously not have a way to share images with codex yet?" 21 reactions.
## How users want it fixed
- Native clipboard paste on all platforms (above issues).
## Workarounds people use today
- Save screenshot to disk and give the file path; drag and drop.
## Session Recorder angle
The ZIP already gives screenshots as files with timestamps and report.md references them by path, which works with "give a file path". Gap: none large; a note in the prompt telling the agent to open specific screenshot paths. This is mostly an agent-vendor bug. Low novelty value for us.
## Scores
frequency: 5  severity: 2  fit: 1  smallness: 4  novelty: 3

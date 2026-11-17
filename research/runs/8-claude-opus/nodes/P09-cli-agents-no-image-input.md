---
id: P09
title: "I can't get a screenshot into my CLI agent"
who: developers using terminal agents
tools: [Claude Code, Codex CLI, Copilot CLI, opencode]
status: verified
---
## Pain
Terminal agents handle images poorly: no clipboard paste on some OSes (WSL, Linux, SSH), pasted screenshots silently dropped, paths auto-converted into images, or images never reach the model. Users fall back to the web chat or to describing the UI in words.
## Evidence
- https://github.com/github/copilot-cli/issues/476 (github-issue, 2025-11-05, verified): "It is not very convenient to paste an image from the clipboard in TUI" 57 reactions, 12 comments
- https://github.com/github/copilot-cli/issues/1217 (github-issue, 2026-01-31, verified via API): "[Feature Request] Support clipboard image paste in WSL from Windows" (title) 48 reactions, 3 comments
- https://github.com/anthropics/claude-code/issues/1361 (github-issue, 2025-05-27, verified via API): "[BUG] Can't paste image from clipboard" (title) 49 reactions, 70 comments
- https://github.com/anthropics/claude-code/issues/12644 (github-issue, 2025-11-28, verified): "The Claude Code CLI has no way to accept images or screenshots." 35 reactions, 26 comments
- https://github.com/openai/codex/issues/2221 (github-issue, 2025-08-12, verified): "Do we seriously not have a way to share images with codex yet?" 21 reactions, 9 comments
- https://github.com/openai/codex/issues/30529 (github-issue, 2026-06-29, verified): "The agent behaves as if no image was provided." 4 reactions, 6 comments
- https://github.com/anomalyco/opencode/issues/906 (github-issue, 2025-07-12, verified): "opencode only support attachment via drag and drop" 22 reactions, 37 comments
- https://github.com/anomalyco/opencode/issues/15728 (github-issue, 2026-03-02, verified): "The Read tool cannot pass image data to vision-capable models" 10 reactions, 12 comments
- https://github.com/anthropics/claude-code/issues/15597 (github-issue, 2025-12-28, verified): "I actually want to give claude the image PATH" 23 reactions, 20 comments
## How users want it fixed
- Alt+V / clipboard paste everywhere, including WSL (copilot-cli #476, #1217).
- Pass image file paths as text so the agent can open them itself (#15597).
## Workarounds people use today
- Save the screenshot to disk and give the agent the path; switch to web chat; ShellShot-style helpers (https://news.ycombinator.com/item?id=48489942).
## Session Recorder angle
Partly solved already: the ZIP stores screenshots as files and `report.md` references them, so an agent with file access can open them by path. Gap: the user must unzip and point the agent at the folder. Little new to build; mostly docs.
## Scores
frequency: 5  severity: 2  fit: 3  smallness: 4  novelty: 1

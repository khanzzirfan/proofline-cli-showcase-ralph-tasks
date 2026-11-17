---
id: P07
title: The agent can't read image files on its own — it is "effectively blind"
who: developers
tools: [Claude Code, Codex CLI, Gemini CLI]
status: verified
---
## Pain
Agents have vision only when the human pastes a screenshot into chat. They cannot open an image file on disk or look at a screenshot they themselves produced, so the visual verify loop is broken — the agent writes code and "hopes for the best."

## Evidence
- https://github.com/anthropics/claude-code/issues/30925 (github-issue, 2026-03-05, verified): "it can only use this ability when I manually paste an image... The agent itself has no way to look at an image file on disk... The agent is effectively blind."
- https://github.com/anthropics/claude-code/issues/32005 (github-issue, 2026-03-08, verified): "Describing a screenshot in text is time-consuming and often loses important details."

## How users want it fixed
- Extend the Read tool to feed image files to the model as vision input (a `ReadImage` tool): https://github.com/anthropics/claude-code/issues/30925
- Clipboard paste and drag/drop of images in the terminal: https://github.com/anthropics/claude-code/issues/32005

## Workarounds people use today
- Manual Cmd+V paste; Playwright MCP screenshots; saving to a path and asking the agent to Read it (fails for images).

## Session Recorder angle
The exported report already references screenshots by path, so an agent that can read images can consume them — but today most agents cannot. The extension can help by writing a text description of each screenshot/annotation into `report.md` so the agent gets visual context even without vision.

## Scores
frequency: 4  severity: 3  fit: 4  smallness: 3  novelty: 2

---
id: P07
title: "Terminal agents still can't take a pasted screenshot: images in issues are unusable"
who: developers
tools: [Claude Code, Codex CLI, Copilot CLI, opencode, VS Code Copilot Chat]
status: verified
---
## Pain
Visual debugging means a screenshot, but several agents cannot accept one. Users must save the
image to a file and pass a path, image files referenced in the repo are not read, and background
or cloud agents drop the screenshot entirely. This is a repeated, high-reaction request across
many popular repos.

## Evidence
- https://github.com/openai/codex/issues/31685 (github-issue, 2026-07-09, verified): "Screenshot-to-agent is a very common debugging and UI workflow. Requiring users to save a file and pass -i interrupts the flow".
- https://github.com/github/copilot-cli/issues/1276 (github-issue, 2026-02-04, verified): "having to save the image manually and then reference the file path adds a lot of friction" — +1:8, 11 comments, still open.
- https://github.com/anthropics/claude-code/issues/32005 (github-issue, 2026-03-08, verified): "Claude Code currently doesn't support pasting or dropping images directly into the terminal interface." — +1:8, 17 comments, closed.
- https://github.com/microsoft/vscode/issues/256095 (github-issue, verified, label `chat-vision`): "Copilot did a few funny things … It said it couldnt view the image even after finding it." — 👍5, open.
- https://github.com/microsoft/vscode/issues/280570 (github-issue, 2025-12-02, verified): background agent "Add context -> Screenshot … I can not see the screenshots"; a maintainer "Decided to disable this as there are a few edge cases it didn't work".
- https://github.com/anomalyco/opencode/issues/1429 (github-issue, verified, closed, 👍16): pasted screenshot "is not recognized as such but as a giant block of text".

## How users want it fixed
- Ctrl+V a clipboard screenshot straight into the agent, with an inline thumbnail preview
  (claude-code#32005, codex#31685, copilot-cli#1276).
- Agents should read an image file by path without special flags (vscode#256095).

## Workarounds people use today
- Save screenshot to disk; pass `-i path` (Codex) or a file path in the prompt; drag-and-drop at session start.

## Session Recorder angle
Screenshots already exist in the report and ZIP, but the agent-facing artifact is `report.md` plus
loose PNGs — which CLI agents frequently cannot read. Real gap: make the report's images easy to
feed a text-only agent (e.g. a manifest of image paths and captions, or an option to embed compact
text descriptions). Overlaps #21 (screenshot/pause keyboard shortcuts) only in the capture step.
Vision-node 1 of 2.

## Scores
frequency: 5  severity: 3  fit: 4  smallness: 4  novelty: 3

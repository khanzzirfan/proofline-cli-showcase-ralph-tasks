---
id: P09
title: “Some coding-agent workflows still need a visual artifact they can actually inspect”
who: developers, QA, agent users
tools: [Claude Code CLI, Copilot cloud agent, Crit]
status: verified
---
## Pain
Images can be useful feedback, but support depends on the agent surface. Copilot cloud explicitly supports image input, while a Claude Code issue requests an image-returning screenshot tool; this is a surface-specific gap, not evidence that all agents cannot read images.
## Evidence
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): proposes “a screenshot (returned as image Claude can actually see)” as one solution (1 reaction).
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs (vendor-doc, date unknown, verified): states Copilot cloud agent processes screenshots, sketches and designs attached to an issue or prompt.
- https://github.com/natethegreat/crit (blog, date unknown, verified): tool docs say agents read annotated screenshots and feedback JSON; 2 stars, promotional project description.
## How users want it fixed
- Return actual visual images to the agent, not only filenames or descriptions: https://github.com/anthropics/claude-code/issues/52907.
- Keep image context attached to the coding task: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs.
## Workarounds people use today
- Attach screenshots to prompts/issues or save annotated screen captures alongside structured feedback for image-capable agents.
## Session Recorder angle
Session Recorder captures screenshots, annotations and video; ZIPs include image files and asset references. Agent consumption varies, so its report prompt should explicitly say how to inspect assets. Do not infer a need for new screenshot capture from this evidence.
## Scores
frequency: 2  severity: 3  fit: 4  smallness: 4  novelty: 2

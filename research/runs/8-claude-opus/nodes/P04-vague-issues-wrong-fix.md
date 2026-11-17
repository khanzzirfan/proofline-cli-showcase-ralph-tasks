---
id: P04
title: "Vague bug reports make agents ship confident fixes for the wrong problem"
who: developers, QA, teams using cloud agents on issues
tools: [Copilot coding agent, Claude Code, Codex, Jules, OpenHands]
status: verified
---
## Pain
Cloud agents start from an issue. When the issue lacks a repro, environment, expected vs actual, or the exact failing request, the agent picks a plausible cause and "fixes" it. Research suggests agents gain most from operational cues (where to look, what failing data) rather than prose.
## Evidence
- https://overreacted.io/how-to-fix-any-bug/ (blog, verified): "Claude was repeatedly wrong because it didn’t have a repro"
- https://dev.to/skyestrela/stop-asking-ai-coding-agents-to-fix-vague-bugs-4ji6 (blog, 2026-07-25, verified): "A coding agent can produce a confident patch for the wrong problem when the input is only: The upload sometimes fails. Please fix it."
- https://www.alphaxiv.org/abs/2607.09553 (paper, 2026-07, verified; quote re-taken from the abstract in US-003): "agents benefit less from information traditionally useful to humans, such as reproduction steps, and more from sentences that expose a repair direction."
- Same paper (counter-evidence): "removing information considered important for human bug reporting, such as reproduction steps and expected behavior ... does not significantly reduce agent effectiveness when more operational cues remain available."
- https://sep.com/blog/agentic-bug-fixing-experience-report/ (blog, verified): "I wanted to know What was the problem What was the platform What are the reproduction steps"
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs (vendor-doc, verified): "Cloud agent processes images—such as screenshots, sketches, or designs—as part of your task description."
## How users want it fixed
- Record failure, environment, expected result and exact error before asking for a fix (dev.to skyestrela).
- Include localization cues (file, route, failing request) in the issue (alphaxiv paper).
## Workarounds people use today
- Bug-report skills and templates that the agent fills first (sep.com); "reproduce first, then fix" prompts.
## Session Recorder angle
Issues filed by Session Recorder already hold steps, console, network and screenshots. Missing: an "agent block" that states expected vs actual, the failing request and likely localization cues (URL route, component text near the click) in a fixed shape. Partly overlaps #48 (labels and assignees) only in the filing flow; #29 adds env info.
## Scores
frequency: 4  severity: 4  fit: 4  smallness: 4  novelty: 3

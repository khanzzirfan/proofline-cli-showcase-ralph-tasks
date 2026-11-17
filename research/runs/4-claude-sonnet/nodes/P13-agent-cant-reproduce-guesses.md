---
id: P13
title: "The agent can't reproduce my bug, so it guesses and fixes the wrong thing"
who: developers, QA
tools: [Claude Code, Cursor, Codex, Devin]
status: partly-verified
---
## Pain
Without exact steps, data and state, agents patch the symptom or a flaky test. The fix looks plausible and merges, and the bug stays. Teams say bug quality is the cause, not the model.
## Evidence
- https://blog.buildbetter.ai/how-to-hand-off-bugs-to-a-coding-agent/ (blog, 2026-10-23, verified, vendor, weak): "Nobody confirmed the bug happens reliably, so the agent 'fixes' a flaky test"
- https://news.ycombinator.com/item?id=46047931 (hn, 2025-11-25, verified): FlowLens author wants a handoff "without retyping steps, copying logs, or hoping it can reproduce the behavior". 5 points.
- https://news.ycombinator.com/item?id=45215032 (hn, 2025-09-11, verified): Launch HN Ghostship, 53 points, 23 comments; commenters say people "either have flaky e2e tests or no e2e tests".
- https://dev.to/hassantayyab/stop-wasting-tokens-on-ui-bugs-how-chrome-devtools-mcp-changed-my-debugging-workflow-3ma9 (blog, verified): "We went back and forth, wasting tokens, getting nowhere."
## How users want it fixed
- Reproducible, ordered steps and exact state in the report (buildbetter); exact context captured at the moment (FlowLens).
## Workarounds people use today
- Writing a repro by hand; asking the agent to write a failing test first.
## Session Recorder angle
Already records ordered steps with timestamps. Possible add-on: a numbered "Steps to reproduce" and "Expected vs actual" block at the top of report.md, derived from clicks and the user's notes (deterministic, no LLM). Check docs/report-format.md: the report is chronological, not a steps list. Overlap: #23 (UJG docs bundle) unclear; #25 typed value before submit supplies one detail.
## Scores
frequency: 4  severity: 4  fit: 4  smallness: 4  novelty: 3

---
id: P12
title: Vague bug reports cause reproduction back-and-forth — missing steps and environment
who: QA, developers, product
tools: [Claude Code, Cursor, Copilot]
status: verified
---
## Pain
Bug reports like "the button is broken" force developers/agents to ask "which button, which browser, what steps?" The agent cannot reproduce without the exact steps and environment, so hand-off stalls in clarification loops.

## Evidence
- https://rumana.dev/blog/visual-bug-reporting-tools-compared (blog, 2026-04-01, verified): "a bug report that said 'the button is broken'... which button... No more back-and-forth asking 'what browser were you on?'"
- https://news.ycombinator.com/item?id=49119881 (hn, verified): "reduce the back-and-forth that follows vague bug reports."
- https://news.ycombinator.com/item?id=46047931 (hn, verified): "hoping it can reproduce the behavior."

## How users want it fixed
- Automatically capture console, network, environment and reproduction steps alongside the visual evidence: https://rumana.dev/blog/visual-bug-reporting-tools-compared

## Workarounds people use today
- Jam/BetterBugs/Marker.io auto-capture; Tentomushi AI drafts steps; FlowLens instant replay.

## Session Recorder angle
This is the extension's core promise (record → annotate → file). The report already contains steps, environment, console and network; the remaining gap is framing those as agent-ready reproduction steps. Open PR #29 (browser/OS/viewport) overlaps partly.

## Scores
frequency: 4  severity: 3  fit: 5  smallness: 3  novelty: 3

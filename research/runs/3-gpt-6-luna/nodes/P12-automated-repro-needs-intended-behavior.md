---
id: P12
title: “A browser crawler can click around but still miss the bug that matters”
who: QA, developers, product
tools: [browser agents, automated QA agents]
status: verified
---
## Pain
Exploring links and interactions is not sufficient to identify whether the observed result is wrong. Without intended behavior, acceptance criteria or a human’s explanation, an automated agent may not distinguish a defect from expected behavior.
## Evidence
- https://news.ycombinator.com/item?id=45293848 (hn, 2025-09-18, verified): “Actually understanding the expected behavior ... is the tricky part” and it needs “specific assertions and acceptance criteria” (2 points, 2 comments).
- https://github.com/anthropics/claude-code/issues/52907 (github-issue, 2026-04-24, verified): detailed request says its target UI state can depend on an on-prem authenticated app and workflow-specific interactions (1 reaction).
- https://github.com/rbsriram/heckle (github-issue, date unknown, verified): product workflow asks a person to narrate what looks wrong and review the drafted task before dispatch (3 stars; promotional).
## How users want it fixed
- Preserve explicit user intent and assertions with the recorded steps: https://news.ycombinator.com/item?id=45293848.
- Let a human describe and approve the bug task before sending: https://github.com/rbsriram/heckle.
## Workarounds people use today
- Write explicit test assertions or annotate/narrate the observed mismatch.
## Session Recorder angle
Markers, annotations, notes and voice narration are already designed to preserve intent. Improve prominence of those anchors in agent handoff; no new capture feature appears necessary. No direct PR overlap found.
## Scores
frequency: 2  severity: 4  fit: 5  smallness: 5  novelty: 3

---
id: P07
title: "The customer or QA report arrives as words, and the words lose the evidence"
who: product, QA, support
tools: [Jam, Marker.io, Session Recorder, Cursor]
status: partly-verified
---
## Pain
Most bug reports are not written by the person who can fix them. A customer, a QA tester or a support agent writes
"the discount button doesn't work", and the developer has to reconstruct what was clicked, what the browser logged
and which request failed. The richer the web app, the more the words leave out. The evidence exists at the moment of
the failure, on the reporter's machine, and is gone by the time the report reaches the developer.

## Evidence
- https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 (forum, 2026-10-13, verified): "A customer says the discount button doesn't work. You open Cursor, but the report doesn't tell you what they clicked, what the browser logged, or which request failed." — signal: 36 likes, 36 views, 1 post; a vendor pitch, so it is self-interested but the scenario is concrete
- https://news.ycombinator.com/item?id=45035578 (hn, 2025-08-27, verified): "console logs, network requests, and other dev data are usually missing from bug reports" — signal: 17 points, 5 comments; vendor pitch, weak
- https://github.com/anthropics/claude-code/issues/101957 (github-issue, 2026-10-14, verified): "My case was a bug hunt where every bug was confirmed with a before/after screenshot, and the issue and PR got the descriptions while the screenshots stayed in the chat" — signal: 11 reactions (10 👍 / 1 ❤️), 4 comments, still open
- https://news.ycombinator.com/item?id=21049087 (hn, 2019-09-23, verified): "PMs and QA can on the other hand save time on bug reporting" — signal: 4 points, 0 comments; vendor pitch, weak

## How users want it fixed
- The reporter should not have to describe the bug; the tool should capture it while it happens
  (https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630, verified).
- The developer should get the missing dev data — console, network — inside the report, not in a follow-up email
  (https://news.ycombinator.com/item?id=45035578, verified).

## Workarounds people use today
- Ask the customer to record a Loom video and paste the link — which agents cannot read (see P09)
  (https://cobaltcapture.com/guides/why-loom-doesnt-work-with-agents, verified).
- Hosted "magic link" recorders that capture video and dev logs without installing anything
  (https://news.ycombinator.com/item?id=45035578, verified).

## Session Recorder angle
This is the extension's core use case and it already works: record, annotate, narrate, then file a GitHub issue or
export a ZIP. The gap is the *recipient* side of that flow — the issue that gets filed carries text only, so the
reconstructed-by-hand gap reappears at the far end (see P04 and P03).
The extension's narration and transcript (`lib/transcription/`, `lib/annotations/dictation.ts`) are already the
"reporter describes intent" half; the annotation screenshots are the "show where" half. Neither reaches the agent.

## Scores
frequency: 3  severity: 4  fit: 4  smallness: 4  novelty: 3

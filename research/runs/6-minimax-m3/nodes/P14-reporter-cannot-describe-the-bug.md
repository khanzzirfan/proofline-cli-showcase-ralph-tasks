---
id: P14
title: "The person reporting the bug doesn't know how to describe it to an agent"
who: product, QA, support, developers
tools: [jam, marker.io, darnly, flowlens, annotatefix, agentation]
status: verified
---
## Pain
The reporter is a customer, a support agent or a QA person, not the engineer. They can
*show* the broken button but cannot describe it in the terms an agent needs. The gap between
"the discount button doesn't work" and "the agent needs to know which element, what the
user typed, which request failed, and what the console said" is where the report is lost.

## Evidence
- https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 (forum, 2026-10-13, verified): "A customer says the discount button doesn't work. You open Cursor, but the report doesn't tell you what they clicked, what the browser logged, or which request failed. You still have to piece that together before the agent can help." (signal: 1 post, 36 views)
- https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 (forum, 2026-10-13, verified): "AnnotateFix lets customers point at the broken element inside your app and report the problem. The widget attaches screenshots, recent actions, console errors and failed requests." (signal: 1 post, 36 views)
- https://news.ycombinator.com/item?id=46047931 (hn, verified): "What I actually want is a way to hand the agent the exact context I just saw - without retyping steps, copying logs, or hoping it can reproduce the behavior." (signal: 5 points, 1 comment)
- https://chromewebstore.google.com/detail/handoff-%E2%80%94-visual-feedback/kdojobaddodgeecdboledochcdndkehf/reviews (review, 2026-08-26, verified): "I often use it to gather feedback on the UI for my AI agent. It's also great that there's a walkthrough tool in MCP." (signal: 5.0 from 2 ratings, 17 users)

## How users want it fixed
- Point at the element, not describe it: "lets customers point at the broken element inside your app and report the problem" (https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630)
- Attach the machine evidence automatically: "The widget attaches screenshots, recent actions, console errors and failed requests." (same topic)
- Give the agent a walkthrough rather than a description: "there's a walkthrough tool in MCP" (https://chromewebstore.google.com/detail/handoff-%E2%80%94-visual-feedback/kdojobaddodgeecdboledochcdndkehf/reviews)

## Workarounds people use today
- A customer-support agent writes the bug report by hand from the customer's description.
- The developer asks the customer for a screen recording and a HAR file (the status quo for
  anything behind a login — see P08).
- Third-party element-annotation extensions (Vibe Annotations, Handoff, AnnotateFix, ElementAgent, POKEIT, Vox Issue, Pluck, Yocoolab, Setu, AIScan, Contexify, Staktab — all listed in the Chrome Web Store "Related extensions" carousel for Darnly, https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj).

## Session Recorder angle
This is exactly what Session Recorder does today and why it exists — but the pain is *not*
fully solved: the extension requires the reporter to be the developer. The gap is a
**non-developer capture mode**: a one-click "report this" that captures the last few seconds
of context (the failed request, the console error, the element, the screen) and produces a
short report an agent can act on, without the reporter needing to open the extension UI or
read the docs. The extension already records everything needed; the work is packaging and
defaults. Overlapping open PRs: #21 (screenshot and pause keyboard shortcuts), #23 (UJG
docs bundle), #29 (browser, OS, viewport in report), #45 (shadow DOM clicks and typing).

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 3  novelty: 2
pain_score: 16  pick_score: 29

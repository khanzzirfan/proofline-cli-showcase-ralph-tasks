---
id: P16
title: "A bug report the agent can't prove — 'I can't tell' beats a wrong yes"
who: developers, QA, product
tools: [momentic, opslane, playwright, jam]
status: verified
---
## Pain
In the QA-agent world the dominant complaint is not "the agent misses bugs" but "the agent
reports bugs it cannot reproduce, and the report is not auditable". Experienced testers
say they stop reading the report after one noisy finding. The fix people converge on is a
third answer — "I can't tell" — plus the expectation that every finding carries its steps,
its evidence and an honest confidence, so a human can triage in minutes instead of hours.

## Evidence
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "The key missing details are (a) how they de-duplicate reports, (b) what evidence they attach (steps + screenshots/video + DOM/locator context), and (c) determinism/repro" (signal: 168 points, 44 top-level comments)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "outputs need to be auditable, not just accurate. Pass/fail/uncertain per check, evidence link, explicit confidence. Anything that can't show its work is asking the reader to accept vibes" (signal: 168 points, 44 top-level comments)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "a guessed pass is worse than no test... it was the answer that looks settled" (signal: 168 points, 44 top-level comments)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "A bug report with just a description usually turns into a bunch of back and forth before anyone can reproduce it, so having the actual steps there sounds like it would save a lot of that." (signal: 168 points, 44 top-level comments)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "Mo is able to inspect the network traffic" — asked for explicitly: "A lot of the failures I run into aren't visible on screen: a request that returns a 200 with an error body, a retry loop, a call that quietly fails. Do the agents get the network traffic for a failed flow?" (signal: 168 points, 44 top-level comments)
- https://github.com/Microsoft/vscode-pull-request-github/issues/7770 (github-issue, 2025-09-07, verified): "The screenshots are fake, look nothing like my app and give false impressions that this a fully working and complete solution!" (signal: 👍 1, 9 comments, closed as completed 2026-04-08; a vendor agent had to be told to remove the fake screenshots it had invented)
- https://github.com/clipy-recorder/clipy-mcp (github-repo, n/a, verified): the closest shipped implementation of the ask — markers carry an explicit three-valued verdict, "Renders with a verdict glyph (✓ pass, ✗ failure that can abort via failMode, ⚠ unverified — never a silent pass)", and it keeps the two provenances apart: "Clipy vouches only that you said it — not that it verified it" (signal: 5 stars, 2 forks)

## How users want it fixed
- Three-valued result per check, not two: pass / fail / uncertain, with the reason (https://news.ycombinator.com/item?id=50339913).
- Every finding carries the evidence: steps, screenshots or video, and the DOM/locator context, plus de-duplication (same URL).
- An explicit "cannot reproduce" state rather than a silent drop: "the docs say a bug it can't reproduce is not reported as confirmed, but does it show up anywhere or is it just dropped?" (same thread)

## Workarounds people use today
- Plant known defects in staging and count false alarms per run (https://news.ycombinator.com/item?id=50339913, comment by `haukebri`)
- Use the open-source qpilot or agent-qa harnesses instead of a paid service (same thread)
- Manual QA with a written test case per flow (same thread)

## Session Recorder angle
This is the node that fits the extension's actual data better than any other. Session Recorder
already records the *evidence chain* of a real session — the failed request, the console error,
the DOM event, the click — with one clock joining them, and it already protects errors and
their linked request bodies at every trim level. What it does not yet offer is the
**auditability frame** the QA community asks for: an explicit confidence/verdict per finding
(e.g. "this request failed, here is the body, here is the error it produced"), and the
ability to say "this is not a bug — intended behaviour" so the next agent run does not
re-flag it. A "known/not-a-bug" note in the report and a machine-readable verdict line in
`session.json` would give the extension the thing competitors with an LLM in the loop
pretend to have and it can have *deterministically*.
Overlapping open PRs: #39 (request and trace IDs of failed requests) and #41 (storage
snapshot) add identifiers, which is a prerequisite for de-duplication across reports. #49
(group recordings of the same error) addresses grouping. No open PR adds a verdict,
confidence or a not-a-bug state.

## Scores
frequency: 3  severity: 4  fit: 5  smallness: 3  novelty: 4
pain_score: 14  pick_score: 31

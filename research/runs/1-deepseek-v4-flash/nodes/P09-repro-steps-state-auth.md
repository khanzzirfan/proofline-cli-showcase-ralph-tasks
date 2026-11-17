---
id: P09
title: "An agent can't reproduce the bug: missing steps, state, auth and data"
who: developers, QA
tools: [Claude Code, Cursor, Copilot agent]
status: partly-verified
---
## Pain
Even with a good report, agents fail because the reproduction needs state the report doesn't
carry: which user, what data, whether logged in, the exact click order. QA folklore says a bug
report that can't be reproduced is worthless, and agents hit the same wall — they fix a local
fiction instead of the real bug.

## Evidence
- https://www.reddit.com/r/QualityAssurance/comments/jndw3s/bad_to_create_a_lot_of_bug_reports/ (reddit, unverified, snippet): "If they can't reproduce it, then their bug report is of no value. I don't investigate anything unless they can give me at least minimal repro steps."
- https://www.reddit.com/r/QualityAssurance/comments/rrbacl/what_is_the_ideal_bug_report_for_developers/ (reddit, unverified, snippet): "The bug report should include all the info to enable the dev to reproduce the bug, including data, specific user, evidences".
- https://negiadventures.github.io/blog/environment-manifests-ai-coding-agents.html (blog, 2026-05-13, verified): proposes an environment manifest (pinned toolchain, seeded fixtures, verifier snapshot) because "the agent cannot trigger the original failure, so it patches symptoms instead of causes".
- https://dev.to/yureki_lab/how-i-debug-a-misbehaving-ai-coding-agent-my-4-step-playbook-3m12 (blog, verified): "reproduce minimally → find the divergence turn in the transcript".

## How users want it fixed
- Reports that carry the state needed to reproduce: user/auth, data, environment, ordered steps.
- Hand the agent a runnable repro (a seeded fixture or a recorded click path), not prose.

## Workarounds people use today
- QA writes numbered steps and environment by hand; developers ask follow-up questions.

## Session Recorder angle
Session Recorder already captures clicks, inputs, navigation, tabs and an inferred OpenAPI
description, plus environment (#29 adds browser/OS/viewport). It is close to a repro recipe. A
feature that emits an explicit, ordered "repro steps + required state" block for the agent is
plausible, but #29 and #41 (storage snapshot) already touch environment/state — check overlap.
Not in section 5 of the notes.

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 4  novelty: 3

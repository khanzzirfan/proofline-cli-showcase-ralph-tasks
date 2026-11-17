---
id: P04
title: "A claimed fix needs visual proof: agents open PRs from an issue but nobody can see the bug is gone"
who: developers, QA, product
tools: [GitHub Copilot agent, Jules, Codex, OpenHands, TraceBug, Playwright]
status: verified
---
## Pain
Issue-driven agents (assign the issue to Copilot, label `jules`, comment `@codex`, `fix-me` for
OpenHands) open a PR from the issue text alone and mark it done, but the reviewer has no reliable proof
the bug is actually fixed. A passing test is not proof — it may not cover the failure — screenshots in a
PR are often missing or stale, so a human re-runs the scenario and re-captures evidence by hand every time.
(Merged with former node P10, "verify the fix": same pain, same evidence.)

## Evidence
- https://github.com/OpenHands/OpenHands/issues/8372 (github-issue, 2025-05-09, verified): "It would be nice if the agent could take a screenshot … save it. This could then be shared as part of the pull request as evidence that the interface was implemented correctly." — 👍3, closed.
- https://thunkle.ai/blog/verify-ai-agent-fix (blog, 2026-09-28, verified): "An AI agent's passing test is not proof of a security fix. Check the original failure, legitimate access and deployed code before accepting the repair."
- https://apidog.com/blog/ai-agents-screenshot-proof-reality-checker/ (blog, 2026-09-01, verified): requires "screenshot proof before AI agents can approve work" and provides "PASS/FAIL certification".
- https://github.blog/ai-and-ml/github-copilot/assigning-and-completing-issues-with-coding-agent-in-github-copilot/ (vendor-doc, 2025-06-06, verified): "Once you assign Copilot an issue … it will kick off an agent session using GitHub Actions." Weak (vendor).
- https://tracebug.dev/blog/jam-dev-alternatives (blog/vendor, 2026-07-30, verified): "Every report also embeds a generated failing Playwright test that goes green when the bug is actually fixed." Weak (vendor).
- https://safeguard.sh/resources/blog/what-an-ai-code-review-bot-cannot-see (blog, 2026-10-18, verified): GitHub's own docs say Copilot review "is not guaranteed to spot all problems", and bots "rarely show why" a change exists.

## How users want it fixed
- Agents should attach before/after visual proof to the PR (OpenHands#8372).
- A "proof of fix" gate: the original failing case re-run and shown refused, or a failing-then-passing test (thunkle.ai, TraceBug).

## Workarounds people use today
- Reviewers run the app locally; teams add visual-regression CI (Percy, Chromatic, lintlab action); re-capture screenshots by hand.

## Session Recorder angle
Session Recorder can capture the "after" state and put it in the issue, but the extension only files issues,
not PR comments. The closest small feature is an agent-ready "acceptance evidence" block in the issue/report
the agent can satisfy, plus labelled before/after screenshots. Overlaps #48 (labels/assignees) only loosely —
do not duplicate. (Because it merged P10, note that open PR #22, "Playwright repro test in ZIP", was closed
by its author: do not revive it as-is, but the space is not actively claimed.)

## Scores
frequency: 4  severity: 4  fit: 4  smallness: 3  novelty: 3
(merged max of P04 + P10; US-004 finalizes)

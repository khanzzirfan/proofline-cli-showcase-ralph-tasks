---
id: P12
title: "The issue queue fills with agent-written duplicates that a human has to triage"
who: product, developers, maintainers
tools: [GitHub Issues, Copilot, Claude Code, OpenHands]
status: verified
---
## Pain
Agents that file issues on a repo's behalf generate near-identical reports for the same bug, often one per
environment or per run. The maintainer then spends the week triaging, closing and cross-linking. GitHub shipped
duplicate detection in June 2026 precisely because of this, which is itself an admission of the size of the problem.
The reporters on the other side have no idea their report is a duplicate.

## Evidence
- https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues/ (vendor-doc, 2026-06-18, verified): "Duplicate issues are one of the biggest time sinks for maintainers: triaging the same bug filed multiple ways, closing duplicates, and linking back to the original." and "For large repositories, this can take up hours every week." — signal: release note; weak as pain evidence but authoritative that the problem is big enough for GitHub to ship a preview
- https://github.com/github/gh-aw/issues/38842 (github-issue, 2026-06-12, verified): "[agent-perf] Systemic: duplicate issue creation — agents filing identical issues in same run" — signal: 1 reaction (1 👀), 2 comments, closed
- https://github.com/github/gh-aw/issues/47811 (github-issue, 2026-07-24, verified): "[deep-report] Consolidate duplicate goroutine/HTTP-timeout fix issues filed by DeepReport and Code Quality agents" — signal: 1 reaction (1 👀), 1 comment, closed
- https://github.com/fullsend-ai/agents/issues/899 (github-issue, 2026-08-20, verified): "Triage agent's duplicate-issue closure has no tie-breaker, causing mutual/circular closures that lose bug tracking entirely" — signal: 1 👍, 5 comments, still open
- https://github.com/github/gh-aw-firewall/pull/299 (github-issue, 2026-01-17, verified): "feat: Add issue duplication agent using cache memory" — signal: 2 reactions (1 ❤️ / 1 👀), 5 comments, closed; this is a pull request
- https://github.com/norrietaylor/tt2/issues/118 (github-issue, 2026-03-02, verified): "Close duplicate step-names issue" — signal: 1 reaction (1 👀), 3 comments, closed; the body also records "16 open `agentic-workflows` failure issues are accumulating without triage"

## How users want it fixed
- Detect the duplicate before the issue is created, and let the reporter reuse the existing one
  (https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues/, verified).
- Consolidate agent-generated reports of the same failure into one thread
  (https://github.com/github/gh-aw/issues/47811, verified).

## Workarounds people use today
- Write a dedicated dedup agent that closes duplicates and labels the unique ones
  (https://github.com/norrietaylor/tt2/issues/118, verified).
- A cache-memory duplication agent
  (https://github.com/github/gh-aw-firewall/pull/299, verified).

## Session Recorder angle
The extension's `#49` (group recordings of the same error and add to existing issues) already owns the
"group identical recordings" half, so a new grouping feature has novelty 0-1. The remaining novel piece is the
*reporter-side* check — before filing, look for an existing open issue with the same error signature — which is
close to GitHub's own duplicate detection preview and would be hard to beat.
This node is real but it is mostly a GitHub-platform problem, not a recorder problem.

## Scores
frequency: 4  severity: 4  fit: 3  smallness: 2  novelty: 2

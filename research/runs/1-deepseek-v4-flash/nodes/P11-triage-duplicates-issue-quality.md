---
id: P11
title: "Triage and duplicates: reports are either too thin or far too long"
who: developers, QA, product
tools: [GitHub Copilot agent, issue triage bots, Session Recorder]
status: partly-verified
---
## Pain
Bugs arrive with too little information to act on, or with so much dumped context that the
signal is buried. Duplicates pile up, and issue-driven agents get closed as duplicates by bots
before they help. People want a report that is complete enough to reproduce, but short enough
to read and triage.

## Evidence
- https://www.reddit.com/r/QualityAssurance/comments/jndw3s/bad_to_create_a_lot_of_bug_reports/ (reddit, unverified, snippet): "What I hate the most are bug reports that are way too long and contain unnecessary info."
- https://www.reddit.com/r/QualityAssurance/comments/ud41mk/whats_your_process_to_document_communicate_an/ (reddit, unverified, snippet): "there is chance that anything that isn't in ticket will be forgotten by the time he starts solving an issue."
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): github-actions bot "Found 3 possible duplicate issues … This issue will be automatically closed as a duplicate in 3 days" — shows auto-duplicate triage in practice.
- https://github.com/anthropics/claude-code/issues/13480 (github-issue, verified): the same bot auto-flags duplicates ("Found 3 possible duplicate issues … automatically closed as a duplicate in 3 days"), so issue-driven agents can be closed as duplicates before they help.
- https://modem.ai/guides/best-tools-to-deduplicate-bug-reports (blog/vendor, 2026-08-31, verified): "Every bug tracker fills up with duplicates. One survey puts the average at 12% of bug reports." and the hard kind is "a Slack message, a Zendesk ticket, and a GitHub issue describing the same bug in three different vocabularies".

## How users want it fixed
- Reports that are structured, complete and concise: environment, steps, expected, actual.
- Fewer duplicates — search first, or group similar recordings into one issue.

## Workarounds people use today
- QA templates; maintainers close duplicates by hand; triage bots.

## Session Recorder angle
The extension already supports trim levels (Full/Standard/Compact/Minimal) for `report.md`, which
is exactly a "right length" control. Open PR #49 already "groups recordings of the same error and
adds to existing issues", so the duplicate side is taken — only the issue-quality angle is open.
Not in section 5.

## Scores
frequency: 4  severity: 3  fit: 4  smallness: 4  novelty: 2

---
id: P05
title: "The evidence carries secrets and personal data, and nothing masks it before it leaves the browser"
who: developers, QA, product, security
tools: [Claude Code, Codex, Copilot, Session Recorder]
status: verified
---
## Pain
Bug evidence is full of things that must not be shared: bearer tokens in headers and URLs, session cookies, emails,
card numbers, customer names. A recorder captures all of it by default. People then paste it into a chat agent or
attach it to a public issue, and the value is permanent — in an append-only transcript it stays in every later API
call for the life of the session, and in a GitHub issue it stays forever.

## Evidence
- https://github.com/anthropics/claude-code/issues/29434 (github-issue, 2026-02-27, verified): "The context window in Claude Code is **append-only and permanent**." and "There is no way to remove or redact it." — signal: 2 👍, 6 comments, closed as not planned (stale)
- https://github.com/anthropics/claude-code/issues/66044 (github-issue, 2026-06-07, verified): "This is table-stakes security and should not require five custom hooks per machine." — signal: 5 comments, closed as not planned; the body lists four real incidents in one household, starting "rclone.conf grepped → Google Drive OAuth tokens leaked into context (rotated)"
- https://github.com/anthropics/claude-code/issues/59094 (github-issue, 2026-05-14, verified): "Secret leak: agents read .env / credential files without redaction; remediation pushed onto user" — signal: 3 comments, closed
- https://github.com/anthropics/claude-code/issues/44868 (github-issue, 2026-03-01, verified): "Claude Code exposes secrets from .env / .dev.vars files via grep -n and Read tool, despite CLAUDE.md prohibitions" — signal: 5 👍, 10 comments, closed 2026-07-24 with state reason `not_planned`
- https://klavity.in/blog/redact-pii-and-secrets-from-bug-reports (vendor-doc, 2026-08-13, verified): "Bug report evidence — network calls, console logs, screenshots, and URLs — routinely leaks access tokens, session cookies, and personal data." — signal: vendor marketing, weak evidence; useful only because it names the five leak sites (headers, URL params, console, screenshots, storage)

## How users want it fixed
- Mask the value at capture time, before the report leaves the browser, not after
  (https://klavity.in/blog/redact-pii-and-secrets-from-bug-reports, verified — vendor source, weak; but this is the
  shape every commenter in the GitHub issues asks for: prevention at the boundary, not scrubbing afterwards).
- Refuse to surface credential-bearing material to the agent at all
  (https://github.com/anthropics/claude-code/issues/66044, verified).

## Workarounds people use today
- Five hand-written Claude Code hooks per machine: path guard, shape guard, output scanner, OCR guard, allowlist
  (https://github.com/anthropics/claude-code/issues/66044, verified).
- Community hook packs such as ClawCare
  (https://github.com/anthropics/claude-code/issues/29434, verified — comment by `natechensan`, 2026-02-27, which
  says the best it can do is log the detection on `PromptSubmitted` and `PostToolUse`).

## Session Recorder angle
The extension already redacts headers and URL params (`lib/capture/redaction.ts`), but screenshots, narration
transcripts, free-text notes and the recorded video are not covered. That is exactly the gap the evidence names.
However, five open PRs already occupy the redaction space: `#31` (URL params, founder), `#37` (tokens in URLs),
`#38` (card, IBAN, tax IDs), `#42` (secret protection across evidence), `#44` (WebSocket frame redaction).
A new redaction feature therefore scores novelty 1 at best, and the crowded topic is flagged in the notes.

## Scores
frequency: 3  severity: 5  fit: 4  smallness: 2  novelty: 1

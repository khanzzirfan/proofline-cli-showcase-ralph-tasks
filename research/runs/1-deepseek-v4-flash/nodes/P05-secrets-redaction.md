---
id: P05
title: "Fear of leaking secrets: screenshots, network bodies, URLs and local MCP servers"
who: developers, QA, security
tools: [Jam, Marker.io, Faylee, Session Recorder, local MCP servers]
status: verified
---
## Pain
Bug captures are full of live secrets: session tokens in URLs, auth headers and cookies in
network requests, card numbers in screenshots, private data in console logs. Developers fear
shipping those to a cloud tool or pasting them into an agent, and a local MCP server was shown
to be reachable by any process on the machine.

## Evidence
- https://www.infosecurity-magazine.com/news/chrome-extension-ai-engine-act-mcp/ (news, 2025-04-25, verified): researchers found a Chrome extension with "unrestricted access to the MCP server's tools even without authentication"; MCP servers "are generally open by default".
- https://tracebug.dev/blog/jam-dev-alternatives (blog/vendor, verified): lists "privacy (your bug captures contain your app's data, and they're on someone else's servers)" as a top reason teams leave cloud capture tools.
- https://rumana.dev/blog/visual-bug-reporting-tools-compared (blog, 2026-04-01, verified): QA captures "console logs, network requests, environment details" — the same fields that carry tokens.

## How users want it fixed
- Redact automatically before the report leaves the browser (tokens, cards, IBAN, URL params).
- Local-first: nothing uploaded, no account (TraceBug/openjam pitch).

## Workarounds people use today
- Manual blur/redact in screenshots before sharing; trimming network bodies by hand.

## Session Recorder angle
High overlap risk, and already crowded: open PRs #42 (secret protection across evidence), #41
storage snapshot, #38 redact card/IBAN/tax IDs, #37 redact tokens in URLs, #44 WebSocket frame
redaction, #31 redact URL params (founder). Redaction is a crowded topic (notes section 3 warns of
5 PRs) — do NOT pick this. Keep as context only.

## Scores
frequency: 4  severity: 5  fit: 4  smallness: 3  novelty: 0

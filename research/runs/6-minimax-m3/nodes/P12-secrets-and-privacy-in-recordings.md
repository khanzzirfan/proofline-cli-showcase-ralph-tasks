---
id: P12
title: "Recording the browser means recording my passwords, tokens and customer data"
who: developers, QA, product, security
tools: [jam, darnly, faylee, chrome-devtools-mcp, opslane]
status: verified
---
## Pain
Anything that watches the browser sees the logged-in session: session cookies, bearer
tokens in URLs, card numbers in forms, and whatever the user typed into a password field.
Sharing that recording with a cloud agent is a genuine data-leak risk, and users who build
products around it worry about the industry normalising it. Masking is therefore a
first-class requirement, not a nice-to-have.

## Evidence
- https://news.ycombinator.com/item?id=49466704 (hn, verified): "The end-user recording aspect makes this an absolute non-starter for me... The way the industry is normalizing a complete abandonment of user privacy absolutely boggles my mind." (signal: 40 points, 11 comments; Opslane launch)
- https://github.com/ChromeDevTools/chrome-devtools-mcp (vendor-doc/repo, verified): "chrome-devtools-mcp exposes content of the browser instance to the MCP clients allowing them to inspect, debug, and modify any data in the browser or DevTools. Avoid sharing sensitive or personal information that you don't want to share with MCP clients." (signal: 57.7k stars)
- https://chromewebstore.google.com/detail/vibe-annotations-visual-f/gkofobaeeepjopdpahbicefmljcmpeof/reviews (review, 2025-08-07, verified): "I was looking for a way to cut down on the back-and-forth between my app and Claude-code terminal, and this is perfect!" (signal: 5.0 from 11 ratings, 2,000 users — positive, but the extension exists in a category where trust is the product)
- https://github.com/anthropics/claude-code/issues/82668 (github-issue, verified): "A supported way to delegate authentication for a session that I have explicitly authorized, without the agent handling the secret in plaintext or the value entering the transcript." (signal: 7 comments)

## How users want it fixed
- Never let the secret reach the agent or the transcript: "the value is injected directly into the page, and the agent never sees it." (https://github.com/anthropics/claude-code/issues/82668)
- Vendor guidance is explicitly "avoid sharing sensitive information" rather than "we redact it for you" (https://github.com/ChromeDevTools/chrome-devtools-mcp)
- Competitors in this space market redaction as the headline feature (Darnly: "Bug reports for AI coding agents", https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj — vendor marketing, weak evidence)

## Workarounds people use today
- Manually scrub the recording before sharing (the common answer; no source quoted directly, inferred from the volume of redaction PRs in the extension repo)
- Use a local-only MCP server so nothing leaves the machine (https://github.com/UseVynix/vynix-mcp, 10 stars)
- Do not record at all (https://news.ycombinator.com/item?id=49466704)

## Session Recorder angle
The extension already records network bodies, console output, typed values and file
captures — the raw material for a leak. **Five open PRs** attack redaction (#42 secret
protection across evidence, #44 WebSocket frame redaction, #38 redact card/IBAN/tax IDs,
#37 redact tokens in URLs, #31 redact URL params — the last by the founder). So redaction
itself is *not* a novel PR here and the notes flag the topic as crowded. What is still
open, and what this node's evidence supports, is the **type-ahead** problem: the extension
knows the user typed a value into a password field (the interaction is recorded), and that
fact alone lets the report say "a password was typed at 0:11" without including the value.
No open PR covers credential *types* in the recorded interaction stream.

## Scores
frequency: 4  severity: 5  fit: 3  smallness: 4  novelty: 1
pain_score: 18  pick_score: 29

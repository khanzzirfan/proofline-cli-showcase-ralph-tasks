---
id: P17
title: "Evidence is expensive: screenshots eat the window and each agent run costs money"
who: developers
tools: [claude-code, momentic, codex, cursor, flowlens]
status: verified
---
## Pain
Evidence has a price. Every screenshot is tokens; every agent run is tokens; a QA sweep that
finds 269 bugs costs more per bug than one that finds 86. Users complain about both ends at
once: the context window fills with images, and the bill grows with the run. The evidence
tool therefore has to earn its cost by being small and targeted. The same users also complain
that the report they are forced to paste is *noisy* — it carries boilerplate they did not ask
for and cannot remove.

## Evidence
- https://github.com/anthropics/claude-code/issues/16592 (github-issue, 2026-01-07, verified): "a single session accumulated ~7MB of base64 image data across tool results. When auto-compaction triggered, it took 12+ minutes" (signal: 👍 2 on that comment; thread total 👍 14, 8 comments)
- https://github.com/anthropics/claude-code/issues/16592 (github-issue, 2026-01-07, verified): "Screenshots: 6,988 KB (86.3%)" of an 8 MB session transcript was image data (signal: same comment)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "Mo: 269 bugs, 19.3% recall, 84% precision, $2.67 per bug - Codex (GPT-6.1 Sol + Playwright MCP): 86 bugs, 6.2% recall, 86% precision, $0.80 per bug - Claude Code (Opus 5.5 + Playwright MCP): 59 bugs, 4.2% recall, 80% precision, $4.09 per bug" (signal: 168 points, 44 top-level comments; vendor benchmark, weak as vendor evidence but the price points are checkable)
- https://news.ycombinator.com/item?id=50339913 (hn, verified): "it's too slow as it relies on the cloud and it's way too expensive since most developers use a subscription service." (signal: 168 points, 44 top-level comments)
- https://github.com/anthropics/claude-code/issues/12676 (github-issue, 2025-11-29, verified): "A 2 minute recording at even 1 fps is 120 images, and almost every frame is identical to the one before it. You burn a lot of context to learn very little." (signal: 👍 4 on that comment; thread total 👍 46, ❤️ 11)
- https://chromewebstore.google.com/detail/vibe-annotations-visual-f/gkofobaeeepjopdpahbicefmljcmpeof/reviews (review, 2026-05-14, verified): "I'd like to be able to alter the baseline context that is copied with 'Copy'.. it talks about Tailwind and whatnot.. I don't want that.." (signal: 1 person found this review helpful; extension rated 5.0 from 11 ratings, 2,000 users)
- https://news.ycombinator.com/item?id=46047931 (hn, verified): FlowLens "can run in a rolling 'session replay' mode that keeps the last ~1 minute of DOM / network / console events in RAM. If something breaks, you can grab the 'instant replay' without reproducing anything." (signal: 5 points, 1 comment)

## How users want it fixed
- Send structured text plus a handful of frames instead of raw frames: "pass transcript, click targets, and those frames... That fits in a normal context window and the agent can act on it directly." (https://github.com/anthropics/claude-code/issues/12676, 2026-09-17 comment)
- Let images be disposable once consumed: "The ability to mark images as 'consumed' after processing, freeing context." (https://github.com/anthropics/claude-code/issues/16592)
- Let the user control what gets copied: "I'd like to be able to alter the baseline context that is copied with 'Copy'." (https://chromewebstore.google.com/detail/vibe-annotations-visual-f/gkofobaeeepjopdpahbicefmljcmpeof/reviews)
- Trim surgically rather than dumping everything: the extension's own docs already advise "If the agent needs one full body, re-export at L1 or L0 rather than dumping the whole session at full fidelity."

## Workarounds people use today
- Export at a lower verbosity level (L2/L3) instead of L0 (docs/report-format.md)
- Manually resize images below the 2000 px limit before pasting (https://github.com/anthropics/claude-code/issues/13480)
- Run the agent on a subscription rather than pay per-token API pricing (https://news.ycombinator.com/item?id=50339913)
- Use a rolling "instant replay" capture instead of a full session (FlowLens, https://news.ycombinator.com/item?id=46047931)

## Session Recorder angle
The extension already has the right mechanism — a deterministic four-level trimmer with a
protected-signal list. The missing piece is that the *default* is not chosen for the agent.
A "copy for agent" action should default to L2, emit an explicit token estimate, and offer
"re-export at L1" for exactly one event rather than the whole session. The extension also
already knows the byte size of every asset, so it can show the cost before the user pastes.
On the *noise* half, the extension's "baseline context" block is fixed, and the reviewer of
the closest competitor explicitly asks to be able to edit it — so the copy action needs a
user-controlled block (an editable include/exclude list of report sections), not just a
verbosity dropdown.
Overlapping open PRs: #29 (browser, OS, viewport in report) and #40 (redirect hops as
requests) change what is included; #41 (storage snapshot) is unrelated; #47 (per-repo
transcription vocabulary) touches report content. No open PR adds a token estimate, a
per-event re-export, or a user-editable copy block.

## Notes
This node absorbed the former P09 ("a report is too noisy to be useful"), which shared the
same lead evidence (#16592's "86 % of context" comment) and the same proposed fix (a
copy-for-agent action with a user-controlled block). P17 keeps the better framing because it
also covers the *money* half of the pain, which P09 never did.

## Scores
frequency: 4  severity: 4  fit: 5  smallness: 3  novelty: 1

Score note (US-004): smallness lowered 4 → 3 and novelty lowered 2 → 1 after re-reading the source tree.
`lib/export/tokens.ts` already exports `estimateTokens()` and `lib/export/bundle.ts:497` already computes
`tokens: estimateTokens(report)`, so the token estimate exists internally and only needs surfacing. What is
genuinely new is the user-editable copy block and the per-event re-export, which is a smaller slice of work
than the original score implied.
pain_score: 16  pick_score: 30

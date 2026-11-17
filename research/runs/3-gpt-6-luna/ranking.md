# Ranking

Scores use the PRD rubric: `pain_score = 2 × frequency + 2 × severity`; `pick_score = 2 × frequency + 2 × severity + 2 × fit + smallness + novelty`. Ties are ordered by node ID.

## By pain score

| Rank | Node | Pain | Pick | Frequency | Severity | Fit | Smallness | Novelty | Verification |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | P01 — Agent can't see live browser | 16 | 34 | 4 | 4 | 5 | 4 | 4 | verified |
| 2 | P07 — Fix needs visual verification | 16 | 32 | 4 | 4 | 4 | 4 | 4 | verified |
| 3 | P10 — Secrets in copied network evidence | 16 | 27 | 3 | 5 | 4 | 2 | 1 | verified |
| 4 | P02 — Browser evidence copy/paste | 14 | 33 | 4 | 3 | 5 | 5 | 4 | verified |
| 5 | P03 — Authenticated API context missing | 14 | 31 | 3 | 4 | 5 | 4 | 3 | verified |
| 6 | P13 — MCP local access risk | 14 | 24 | 2 | 5 | 3 | 2 | 2 | verified |
| 7 | P04 — Cloud agent has no browser | 12 | 25 | 2 | 4 | 3 | 3 | 4 | verified |
| 8 | P05 — Browser tools connection fragile | 12 | 28 | 3 | 3 | 4 | 4 | 4 | partly-verified |
| 9 | P12 — Automated repro needs intended behavior | 12 | 30 | 2 | 4 | 5 | 5 | 3 | verified |
| 10 | P06 — Browser network output hard to consume | 10 | 25 | 2 | 3 | 4 | 4 | 3 | partly-verified |
| 11 | P08 — PR screenshots unreliable | 10 | 26 | 2 | 3 | 4 | 4 | 4 | verified |
| 12 | P09 — Visual input coverage is not universal | 10 | 24 | 2 | 3 | 4 | 4 | 2 | verified |
| 13 | P11 — Network capture too large to hand over | 10 | 24 | 2 | 3 | 4 | 4 | 2 | partly-verified |

## By pick score

| Rank | Node | Pick | Pain | Frequency | Severity | Fit | Smallness | Novelty | Verification |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | P01 — Agent can't see live browser | 34 | 16 | 4 | 4 | 5 | 4 | 4 | verified |
| 2 | P02 — Browser evidence copy/paste | 33 | 14 | 4 | 3 | 5 | 5 | 4 | verified |
| 3 | P07 — Fix needs visual verification | 32 | 16 | 4 | 4 | 4 | 4 | 4 | verified |
| 4 | P03 — Authenticated API context missing | 31 | 14 | 3 | 4 | 5 | 4 | 3 | verified |
| 5 | P12 — Automated repro needs intended behavior | 30 | 12 | 2 | 4 | 5 | 5 | 3 | verified |
| 6 | P05 — Browser tools connection fragile | 28 | 12 | 3 | 3 | 4 | 4 | 4 | partly-verified |
| 7 | P10 — Secrets in copied network evidence | 27 | 16 | 3 | 5 | 4 | 2 | 1 | verified |
| 8 | P08 — PR screenshots unreliable | 26 | 10 | 2 | 3 | 4 | 4 | 4 | verified |
| 9 | P04 — Cloud agent has no browser | 25 | 12 | 2 | 4 | 3 | 3 | 4 | verified |
| 10 | P06 — Browser network output hard to consume | 25 | 10 | 2 | 3 | 4 | 4 | 3 | partly-verified |
| 11 | P09 — Visual input coverage is not universal | 24 | 10 | 2 | 3 | 4 | 4 | 2 | verified |
| 12 | P11 — Network capture too large to hand over | 24 | 10 | 2 | 3 | 4 | 4 | 2 | partly-verified |
| 13 | P13 — MCP local access risk | 24 | 14 | 2 | 5 | 3 | 2 | 2 | verified |

## Why the top five pick scores are ordered this way

P01 ranks first because it combines the highest fit and pain with the strongest engagement in the evidence (Claude Code issue #57034, 76 reactions), while an export/handoff improvement can help without pretending to provide live browser access. P02 is close behind: manual transfer is directly evidenced and a compact “copy for agent” flow has high fit, small implementation scope, and no noted open-PR overlap. P07 ranks third because verification is a high-severity recurring need, but Session Recorder can provide the captured failure as a target rather than verify a later fix itself. P03 ranks fourth: authenticated API context is severe and on-target, but the evidence base is weaker and current PRs #32/#43 overlap HAR and cURL functionality. P12 ranks fifth because preserving expected behavior aligns strongly with annotations and narration already in the product, but its frequency evidence is sparse and several proposed intent-capture mechanisms already exist.

The pain ranking reflects raw impact rather than implementation suitability: P10 and P13 score high in severity but low in novelty/smallness because the extension already has redaction work in open PRs and a local MCP bridge would add meaningful security scope. Partly verified P05/P06/P11 remain lower-confidence; their scores are conservative where independent first-person evidence is limited. Visual/video evidence supports a distinction between image-input surface coverage and PR artifact reliability, but does not establish a distinct video-consumption pain.

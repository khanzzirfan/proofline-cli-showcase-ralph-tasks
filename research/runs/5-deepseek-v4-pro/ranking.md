# Ranking

Scored 2026-11-17 with the PRD rubric. `pain_score = 2*frequency + 2*severity` (max 20). `pick_score = 2*frequency + 2*severity + 2*fit + smallness + novelty` (max 40). All 15 nodes are `verified` (see `sources.md`).

## By pain_score (how much the world hurts)

| Rank | Node | Title | freq | sev | pain_score |
|---|---|---|---|---|---|
| 1 | P01 | The agent can't see the browser (console, network, DOM), so it guesses at frontend bugs | 5 | 4 | 18 |
| 2 | P08 | Agents can't watch a screen recording; they need keyframes, a timeline and a transcript | 4 | 4 | 16 |
| 3 | P03 | Users want to hand a bug straight to an agent, often over MCP or one link | 4 | 4 | 16 |
| 4 | P06 | Secrets and credentials leak into agent context and MCP configs | 3 | 5 | 16 |
| 5 | P02 | Handing browser evidence to an agent is manual copy-paste, and pasted logs get lost | 4 | 3 | 14 |
| 6 | P12 | Vague bug reports cause reproduction back-and-forth — missing steps and environment | 4 | 3 | 14 |
| 7 | P13 | The agent can't reach authenticated or internal apps — environment context is missing | 3 | 4 | 14 |
| 8 | P14 | The bug only reproduces under specific state the agent can't recreate | 3 | 4 | 14 |
| 9 | P15 | Oversized or malformed screenshots brick the agent's session | 3 | 4 | 14 |
| 10 | P04 | Cloud/issue-driven agents need visual context and reliable proof a fix worked | 4 | 3 | 14 |
| 11 | P07 | The agent can't read image files on its own — it is "effectively blind" | 4 | 3 | 14 |
| 12 | P10 | Browser evidence burns tokens and the context window | 3 | 4 | 14 |
| 13 | P09 | A screenshot alone is ambiguous — which element or environment | 3 | 3 | 12 |
| 14 | P05 | Agents fabricate "proof" screenshots | 2 | 4 | 12 |
| 15 | P11 | AI PR review can't see the UI a change produces | 3 | 3 | 12 |

## By pick_score (how good it is as our PR)

| Rank | Node | Title | freq | sev | fit | small | nov | pick_score |
|---|---|---|---|---|---|---|---|---|
| 1 | P08 | Agents can't watch a screen recording; keyframes/timeline/transcript | 4 | 4 | 5 | 3 | 5 | 34 |
| 2 | P02 | Manual copy-paste hand-off of browser evidence | 4 | 3 | 5 | 5 | 3 | 32 |
| 3 | P01 | The agent can't see the browser | 5 | 4 | 4 | 3 | 2 | 31 |
| 4 | P09 | A screenshot alone is ambiguous | 3 | 3 | 5 | 4 | 4 | 30 |
| 5 | P12 | Vague bug reports cause reproduction back-and-forth | 4 | 3 | 5 | 3 | 3 | 30 |
| 6 | P03 | Hand a bug straight to an agent over MCP/link | 4 | 4 | 3 | 2 | 4 | 28 |
| 7 | P13 | Agent can't reach authenticated/internal apps | 3 | 4 | 4 | 3 | 3 | 28 |
| 8 | P14 | State-dependent reproduction | 3 | 4 | 4 | 3 | 3 | 28 |
| 9 | P15 | Oversized/malformed screenshots brick the session | 3 | 4 | 3 | 4 | 4 | 28 |
| 10 | P04 | Cloud/issue-driven agents need visual context + proof | 4 | 3 | 4 | 3 | 2 | 27 |
| 11 | P07 | Agent can't read image files on its own | 4 | 3 | 4 | 3 | 2 | 27 |
| 12 | P05 | Agents fabricate "proof" screenshots | 2 | 4 | 3 | 4 | 4 | 26 |
| 13 | P06 | Secrets leak into agent context | 3 | 5 | 3 | 3 | 1 | 26 |
| 14 | P10 | Browser evidence burns tokens | 3 | 4 | 3 | 3 | 2 | 25 |
| 15 | P11 | AI PR review can't see the UI | 3 | 3 | 2 | 3 | 4 | 23 |

## Why the top five (pick_score)

- **P08 (34)** wins because it is the one pain with both maximum fit (the extension already records video, transcript and click events but does not emit them as an agent-readable timeline) and maximum novelty (no open PR touches it). Only smallness — a keyframe/timeline exporter is a real, testable PR but not trivial — holds it back.
- **P02 (32)** is the cheapest high-value win: one clipboard action that reuses the existing `report.md` export, so smallness and fit are both maxed; it is only slightly less novel because a narrow Copy-as-cURL PR (#43) already exists.
- **P01 (31)** is the most frequent and second most painful pain in the data, and the recorder already captures the missing context, but novelty is low because many browser-sharing features exist and open PRs #29/#32 overlap.
- **P09 and P12 (30 each)** are both "surface the data the recorder already captures" wins: P09 pairs each screenshot with the annotated element's selector/text, P12 re-frames steps/environment as agent-ready reproduction steps. Both are high-fit, small, and not duplicated by an open PR.
- **P03 and the auth/state nodes (P13/P14/P15)** score 28 and just miss the top five: high pain but lower smallness (MCP/hand-off) or fit (auth/state requires the agent to consume a logged-in session the agent cannot reach).

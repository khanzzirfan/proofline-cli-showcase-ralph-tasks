# Ranking — pain research run `1-deepseek-v4-flash`

Scored 14 nodes (P10 was merged into P04 in US-003, so there is no P10). Rubric per the PRD:

- **frequency** 0-5: how many independent, high-engagement sources show the pain.
- **severity** 0-5: how much time, money or trust it costs.
- **fit** 0-5: how directly Session Recorder can address it.
- **smallness** 0-5: 5 = one clean PR of a few hundred lines with tests.
- **novelty** 0-5: 5 = nothing in the extension or its open PRs covers it.
- **pain_score** = 2*frequency + 2*severity  (max 20) — how much the world hurts.
- **pick_score** = 2*frequency + 2*severity + 2*fit + smallness + novelty  (max 40) — how good it is as our PR.

## Table 1 — by pain_score (how much the world hurts)

| rank | id | title (short) | freq | sev | fit | small | nov | **pain_score** | pick_score |
|-----:|----|---------------|-----:|----:|----:|------:|----:|---------------:|-----------:|
| 1 | P05 | Secrets leak in captures and local MCP servers | 4 | 5 | 4 | 3 | 0 | **18** | 29 |
| 2 | P01 | Agent can't see the browser (console/network/DOM) | 4 | 4 | 4 | 4 | 3 | **16** | 31 |
| 3 | P04 | A claimed fix needs visual proof | 4 | 4 | 4 | 3 | 3 | **16** | 30 |
| 4 | P08 | Agent can't watch a screen recording | 4 | 4 | 5 | 3 | 4 | **16** | 33 |
| 5 | P09 | Agent can't reproduce (steps, state, auth, data) | 4 | 4 | 4 | 4 | 3 | **16** | 31 |
| 6 | P02 | Copy-pasting logs/cURL by hand is slow and lossy | 5 | 3 | 5 | 5 | 4 | **16** | 35 |
| 7 | P07 | Terminal agents can't take a pasted screenshot | 5 | 3 | 4 | 4 | 3 | **16** | 31 |
| 8 | P03 | Hand a captured bug to an agent (MCP/hand-off) | 4 | 3 | 4 | 3 | 3 | **14** | 28 |
| 9 | P06 | AI PR review has no eyes | 4 | 3 | 3 | 3 | 3 | **14** | 26 |
| 10 | P11 | Triage and duplicates; too thin or too long | 4 | 3 | 4 | 4 | 2 | **14** | 28 |
| 11 | P12 | Environment and flaky bugs mismatch | 3 | 3 | 3 | 3 | 2 | **12** | 23 |
| 12 | P13 | Cost and context: the capture payload is huge | 3 | 3 | 4 | 4 | 3 | **12** | 27 |
| 13 | P14 | Narration/annotation hand-off not machine-readable | 3 | 3 | 4 | 4 | 3 | **12** | 27 |
| 14 | P15 | Cloud capture tools cost per seat and hoard data | 3 | 2 | 3 | 2 | 2 | **10** | 20 |

Ties on pain_score are ordered by severity, then frequency, then id.

## Table 2 — by pick_score (how good it is as OUR PR)

| rank | id | title (short) | freq | sev | fit | small | nov | pain_score | **pick_score** | open PRs to avoid |
|-----:|----|---------------|-----:|----:|----:|------:|----:|-----------:|---------------:|-------------------|
| 1 | P02 | Copy-pasting logs/cURL by hand is slow and lossy | 5 | 3 | 5 | 5 | 4 | 16 | **35** | #43 (adjacent, different) |
| 2 | P08 | Agent can't watch a screen recording | 4 | 4 | 5 | 3 | 4 | 16 | **33** | none |
| 3 | P09 | Agent can't reproduce (steps, state, auth, data) | 4 | 4 | 4 | 4 | 3 | 16 | **31** | #29, #41 |
| 4 | P07 | Terminal agents can't take a pasted screenshot | 5 | 3 | 4 | 4 | 3 | 16 | **31** | #21 (capture step only) |
| 5 | P01 | Agent can't see the browser (console/network/DOM) | 4 | 4 | 4 | 4 | 3 | 16 | **31** | none |
| 6 | P04 | A claimed fix needs visual proof | 4 | 4 | 4 | 3 | 3 | 16 | **30** | #48 (loose); #22 closed |
| 7 | P05 | Secrets leak in captures and local MCP servers | 4 | 5 | 4 | 3 | 0 | 18 | **29** | #42,#41,#38,#37,#44,#31 (crowded) |
| 8 | P03 | Hand a captured bug to an agent (MCP/hand-off) | 4 | 3 | 4 | 3 | 3 | 14 | **28** | none |
| 9 | P11 | Triage and duplicates; too thin or too long | 4 | 3 | 4 | 4 | 2 | 14 | **28** | #49 (duplicates taken) |
| 10 | P13 | Cost and context: the capture payload is huge | 3 | 3 | 4 | 4 | 3 | 12 | **27** | none |
| 11 | P14 | Narration/annotation hand-off not machine-readable | 3 | 3 | 4 | 4 | 3 | 12 | **27** | none |
| 12 | P06 | AI PR review has no eyes | 4 | 3 | 3 | 3 | 3 | 14 | **26** | none |
| 13 | P12 | Environment and flaky bugs mismatch | 3 | 3 | 3 | 3 | 2 | 12 | **23** | #29 |
| 14 | P15 | Cloud capture tools cost per seat and hoard data | 3 | 2 | 3 | 2 | 2 | 10 | **20** | none |

Ties on pick_score break as: (1) any node whose feature is essentially the same action as a
higher-ranked pick is demoted, then (2) severity, then (3) verified source count, then id.

## Why the top five sit where they do

**P02 (35) is first** because it has the highest plausible frequency (5) and combines the biggest
fit (5) with the only perfect smallness (5): a "Copy for coding agent" action is one clipboard
write in code that already exists (`copyIssue`), and `00-context-notes` §3 names it as the unfilled
gap. **P08 (33) is second** because video is where the extension already holds the raw material
(tab video + event timeline) but produces nothing an agent can read, and the evidence is strong
(videobug, amagi-screen, BugDump, claude-code#12676 at +1:46); it loses a point on smallness because
frame extraction is more than a few lines. **P09 (31) takes third** on the tie: it keeps a 4 for
fit and smallness and its feature (an ordered "repro steps + required state" block) is genuinely
distinct from the two above. **P07 (31) is fourth**, ahead of P01 on severity in the tie, and it is
the second vision node — an image manifest for text-only agents. **P01 (31) is fifth despite the
same score**, because its only plausible Session Recorder action (hand the captured console/network
to the agent) is the *same clipboard move as P02*, so we demote it rather than ship two versions of
one feature. P05 has the single highest pain_score (18) but sits seventh on pick_score: redaction is
already claimed by six open PRs (`novelty: 0`), so it is context, not a target.

## Notes

- P05 is the clearest example of the rubric working: the world hurts most (pain_score 18) but it is
  the worst *pick* (29) because six open PRs already cover it.
- Two vision/video nodes (P07, P08) both land in the top five, which matches the required "vision
  and video" area of the brief.
- P15 is competitive context (free/local/OSS vs cloud SaaS), not a buildable feature, and scores last.

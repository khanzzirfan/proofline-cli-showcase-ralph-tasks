# Ranking: 8-claude-opus

Generated 2026-11-17. 15 nodes (P01-P15), scored with the PRD rubric.
`pain_score = 2*frequency + 2*severity` (max 20). `pick_score = 2*frequency + 2*severity + 2*fit + smallness + novelty` (max 40).
Scores come from each node's `## Scores` line. "verified src" counts distinct verified URLs in the node's Evidence list (Reddit snippets are unverified and not counted).
Ties are broken by the other score, then by verified sources.

## Table 1: by pain_score (how much the world hurts, max 20)

| # | Node | Pain | freq | sev | fit | small | novel | pain_score | pick_score | verified src | overlapping PRs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P07 | The agent says 'fixed' without checking, and the bug is still there | 4 | 5 | 4 | 4 | 4 | **18** | 34 | 6 | #22 |
| 2 | P01 | My coding agent can't see the running app: no page, console or network | 5 | 4 | 4 | 2 | 2 | **18** | 30 | 7 | none |
| 3 | P02 | I copy and paste console logs into the agent all day | 5 | 3 | 5 | 5 | 4 | **16** | 35 | 6 | #43 |
| 4 | P04 | Vague bug reports make agents ship confident fixes for the wrong problem | 4 | 4 | 4 | 4 | 3 | **16** | 31 | 5 | #48, #29 |
| 5 | P14 | Devs (and agents) can't reproduce the bug QA reported | 4 | 4 | 4 | 2 | 1 | **16** | 27 | 2 | #29, #25 |
| 6 | P05 | Logs and sessions I hand to agents carry secrets and tokens | 4 | 4 | 3 | 2 | 0 | **16** | 24 | 5 | #31, #37, #38, #42, #44 |
| 7 | P10 | My agent can't watch the bug video, so I screenshot frames by hand | 4 | 3 | 5 | 3 | 5 | **14** | 32 | 5 | #21 |
| 8 | P12 | Too many or too-large screenshots break the agent session | 4 | 3 | 3 | 4 | 3 | **14** | 27 | 6 | none |
| 9 | P09 | I can't get a screenshot into my CLI agent | 5 | 2 | 3 | 4 | 1 | **14** | 25 | 9 | none |
| 10 | P11 | Browser tools flood the agent's context and burn tokens | 4 | 3 | 3 | 4 | 1 | **14** | 25 | 8 | none |
| 11 | P03 | I already found the bug; let me hand the agent exactly what I saw | 3 | 3 | 5 | 4 | 4 | **12** | 30 | 6 | none |
| 12 | P06 | A fake error or bug report can hijack the agent that reads it | 2 | 4 | 4 | 5 | 5 | **12** | 30 | 3 | none |
| 13 | P08 | PRs from agents carry no visual proof, and reviewers can't see the UI change | 3 | 3 | 3 | 2 | 3 | **12** | 23 | 5 | #49 |
| 14 | P13 | The agent's browser isn't logged in, so it can't reach the bug | 3 | 3 | 3 | 3 | 1 | **12** | 22 | 6 | #41 |
| 15 | P15 | Let the agent replay the steps I recorded instead of re-exploring | 2 | 3 | 4 | 1 | 1 | **10** | 20 | 5 | #22 |

## Table 2: by pick_score (how good it is as our PR, max 40)

| # | Node | Pain | freq | sev | fit | small | novel | pain_score | pick_score | verified src | overlapping PRs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P02 | I copy and paste console logs into the agent all day | 5 | 3 | 5 | 5 | 4 | 16 | **35** | 6 | #43 |
| 2 | P07 | The agent says 'fixed' without checking, and the bug is still there | 4 | 5 | 4 | 4 | 4 | 18 | **34** | 6 | #22 |
| 3 | P10 | My agent can't watch the bug video, so I screenshot frames by hand | 4 | 3 | 5 | 3 | 5 | 14 | **32** | 5 | #21 |
| 4 | P04 | Vague bug reports make agents ship confident fixes for the wrong problem | 4 | 4 | 4 | 4 | 3 | 16 | **31** | 5 | #48, #29 |
| 5 | P01 | My coding agent can't see the running app: no page, console or network | 5 | 4 | 4 | 2 | 2 | 18 | **30** | 7 | none |
| 6 | P03 | I already found the bug; let me hand the agent exactly what I saw | 3 | 3 | 5 | 4 | 4 | 12 | **30** | 6 | none |
| 7 | P06 | A fake error or bug report can hijack the agent that reads it | 2 | 4 | 4 | 5 | 5 | 12 | **30** | 3 | none |
| 8 | P14 | Devs (and agents) can't reproduce the bug QA reported | 4 | 4 | 4 | 2 | 1 | 16 | **27** | 2 | #29, #25 |
| 9 | P12 | Too many or too-large screenshots break the agent session | 4 | 3 | 3 | 4 | 3 | 14 | **27** | 6 | none |
| 10 | P09 | I can't get a screenshot into my CLI agent | 5 | 2 | 3 | 4 | 1 | 14 | **25** | 9 | none |
| 11 | P11 | Browser tools flood the agent's context and burn tokens | 4 | 3 | 3 | 4 | 1 | 14 | **25** | 8 | none |
| 12 | P05 | Logs and sessions I hand to agents carry secrets and tokens | 4 | 4 | 3 | 2 | 0 | 16 | **24** | 5 | #31, #37, #38, #42, #44 |
| 13 | P08 | PRs from agents carry no visual proof, and reviewers can't see the UI change | 3 | 3 | 3 | 2 | 3 | 12 | **23** | 5 | #49 |
| 14 | P13 | The agent's browser isn't logged in, so it can't reach the bug | 3 | 3 | 3 | 3 | 1 | 12 | **22** | 6 | #41 |
| 15 | P15 | Let the agent replay the steps I recorded instead of re-exploring | 2 | 3 | 4 | 1 | 1 | 10 | **20** | 5 | #22 |

## Feature idea per node (pick order)

- **P02** (35): 'Copy for coding agent' button: puts a ready prompt plus the trimmed report.md on the clipboard in one click
- **P07** (34): 'Acceptance check' section in report.md/issue: the exact errors and failing requests that must be gone after the fix
- **P10** (32): Extract key frames from the tab video around clicks, errors and annotations into frames/*.jpg and list them in the report timeline
- **P04** (31): Fixed-shape 'Agent brief' block in report.md/issue: expected vs actual, failing request, route and click-target cues
- **P01** (30): Position the report.md hand-off as the 'frozen browser snapshot' for agents with no live browser (docs + report header)
- **P03** (30): Ship an agent-ready prompt.md / AGENTS-style instruction file inside the ZIP
- **P06** (30): 'Untrusted evidence' preamble in report.md and issue body, with page-controlled text fenced
- **P14** (27): None new: core use case already served
- **P12** (27): Capped 'key screenshots' list (e.g. 20) in report.md so agents open only the images that matter
- **P09** (25): Docs: tell CLI agents to open screenshots by path from the unzipped report
- **P11** (25): Per-section token counts in the report.md header
- **P05** (24): None new: redaction is covered by five open PRs
- **P08** (23): Record an 'after' session and post it as verification proof on the original issue
- **P13** (22): State in the report that the session was authenticated (role/origin), no cookies exported
- **P15** (20): Emit a replay script from recorded steps (large; #22 closed as too big)

## Why the top five are in this order

### By pain_score
1. **P07 (18)** and **P01 (18)** tie. P07 ranks first on the tie-break because its severity is 5: users report days of "fixed"/"still broken" loops (claude-code #80950: 13 rounds over 7 days) and it costs trust, not only time. P01 has the widest reach (claude-code #57034 with 76 reactions, the 604-point HN Chrome DevTools MCP story) but a slightly lower severity, since live browser tools exist as workarounds.
2. **P02, P04, P14 (16)** follow. P02 has the most engagement in forums (Cursor thread with 47 likes and 3,295 views), P04 is backed by blogs and a 2026 paper, and P14 is the old QA "can't reproduce" loop, which is severe but whose agent-specific evidence is mostly unverified Reddit snippets.

### By pick_score
1. **P02 Copy for coding agent (35)** wins because it is the only pain with top frequency, top fit and top smallness: Session Recorder already holds the expanded console and network data; the friction left is export, unzip and paste. One button and a prompt template is a few hundred lines with tests, and only #43 (per-request cURL copy) is nearby.
2. **P07 Acceptance check (34)** has the highest pain of all and fits well: a recording already knows the error texts and failing requests that must disappear after a fix. It drops one point to P02 on fit and smallness. Closed PR #22 (Playwright repro) was the large version; a text checklist is the small one.
3. **P10 Key frames from video (32)** is the strongest vision/video gap: agents cannot read `video/*.webm`, and nothing in the extension or its open PRs turns video into frames. Its fit and novelty are maximal, but frame extraction in the offscreen document is more work (smallness 3), and much of the evidence is unverified Reddit.
4. **P04 Agent brief block (31)** is a real pain with good fit but partly overlaps the option B "agent-ready issue" idea in the notes and #48/#29 in the filing flow, so novelty is 3.
5. **P01, P03 and P06 (30)** tie. P01 is the biggest pain but the fix (live browser access) is a new product, so smallness 2. P03 is largely served by the P02 button. P06 (prompt injection via bug reports) is new, tiny and unclaimed, but has only three verified sources, so frequency 2 holds it back; it is a good add-on to any of the top three.

## Notes
- P02 and P03 point to the same feature family (a one-step hand-off). P02 is kept as the pick because its evidence is stronger.
- P05 (secrets) scores high on pain but zero on novelty: five open PRs (#31 #37 #38 #42 #44) already cover redaction.
- Vision/video nodes: P10 (pick 32) is a real, unclaimed gap; P08 (PR review blind to UI, 23) and P09 (CLI image input, 25) are real pains but mostly outside what a browser recorder can fix in one PR; P12 (image budget, 27) is a small optional add-on.

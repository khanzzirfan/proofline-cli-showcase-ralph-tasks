# Ranking (4-claude-sonnet, 2026-11-17)

Scores come from each node file. pain_score = 2f+2s. pick_score = 2f+2s+2fit+smallness+novelty (max 40).

## By pain_score

| Rank | ID | Pain | f | s | fit | small | novel | pain_score | PRs |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P01 | The agent can't see my browser: console, network, DOM, what is on scre | 5 | 4 | 4 | 2 | 2 | 18 | #29,#41 |
| 2 | P12 | The agent's built-in browser tool says it is connected, then isn't the | 5 | 3 | 2 | 1 | 3 | 16 | - |
| 3 | P05 | The agent says it's fixed and the UI is still broken | 4 | 4 | 3 | 3 | 4 | 16 | - |
| 4 | P08 | One oversized or corrupt screenshot breaks the whole agent conversatio | 4 | 4 | 3 | 4 | 4 | 16 | - |
| 5 | P13 | The agent can't reproduce my bug, so it guesses and fixes the wrong th | 4 | 4 | 4 | 4 | 3 | 16 | #23,#25 |
| 6 | P07 | CLI agents can't take a pasted screenshot (WSL, SSH, Linux, Windows) | 5 | 2 | 1 | 4 | 3 | 14 | - |
| 7 | P02 | I copy console errors, cURL and HAR into the chat by hand, and tokens  | 4 | 3 | 4 | 4 | 1 | 14 | #43,#32,#42,#37,#31,#38,#44 |
| 8 | P11 | The agent's browser isn't my logged-in session, so it can't reach the  | 4 | 3 | 3 | 2 | 1 | 14 | #41,#29 |
| 9 | P03 | I found the bug, now give my agent the exact context in one step | 3 | 3 | 5 | 5 | 5 | 12 | - |
| 10 | P04 | The agent can't see the screenshot in my GitHub issue, or I can't atta | 3 | 3 | 3 | 3 | 4 | 12 | #48 |
| 11 | P06 | Agent PRs don't show before/after screenshots or video of the UI | 3 | 3 | 1 | 2 | 4 | 12 | - |
| 12 | P09 | My bug is a screen recording, but the agent can't watch video | 3 | 3 | 3 | 2 | 3 | 12 | - |
| 13 | P10 | Browser tools dump huge snapshots, HAR and logs that burn my tokens | 3 | 3 | 3 | 4 | 2 | 12 | - |

## By pick_score

| Rank | ID | Pain | f | s | fit | small | novel | pick_score | PRs |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P03 | I found the bug, now give my agent the exact context in one step | 3 | 3 | 5 | 5 | 5 | 32 | - |
| 2 | P13 | The agent can't reproduce my bug, so it guesses and fixes the wrong th | 4 | 4 | 4 | 4 | 3 | 31 | #23,#25 |
| 3 | P01 | The agent can't see my browser: console, network, DOM, what is on scre | 5 | 4 | 4 | 2 | 2 | 30 | #29,#41 |
| 4 | P08 | One oversized or corrupt screenshot breaks the whole agent conversatio | 4 | 4 | 3 | 4 | 4 | 30 | - |
| 5 | P05 | The agent says it's fixed and the UI is still broken | 4 | 4 | 3 | 3 | 4 | 29 | - |
| 6 | P02 | I copy console errors, cURL and HAR into the chat by hand, and tokens  | 4 | 3 | 4 | 4 | 1 | 27 | #43,#32,#42,#37,#31,#38,#44 |
| 7 | P04 | The agent can't see the screenshot in my GitHub issue, or I can't atta | 3 | 3 | 3 | 3 | 4 | 25 | #48 |
| 8 | P10 | Browser tools dump huge snapshots, HAR and logs that burn my tokens | 3 | 3 | 3 | 4 | 2 | 24 | - |
| 9 | P12 | The agent's built-in browser tool says it is connected, then isn't the | 5 | 3 | 2 | 1 | 3 | 24 | - |
| 10 | P09 | My bug is a screen recording, but the agent can't watch video | 3 | 3 | 3 | 2 | 3 | 23 | - |
| 11 | P11 | The agent's browser isn't my logged-in session, so it can't reach the  | 4 | 3 | 3 | 2 | 1 | 23 | #41,#29 |
| 12 | P07 | CLI agents can't take a pasted screenshot (WSL, SSH, Linux, Windows) | 5 | 2 | 1 | 4 | 3 | 23 | - |
| 13 | P06 | Agent PRs don't show before/after screenshots or video of the UI | 3 | 3 | 1 | 2 | 4 | 20 | - |

## Why the top five by pick_score are in this order

1. **P03 (32)**: one-step hand-off. Its pain is only medium (12), but it has the best fit (5), is the smallest (5) and no open PR does it (novelty 5). It is the cleanest single PR.
2. **P13 (31)**: reproduction steps. The pain is high (16) and it fits well, and a deterministic "Steps to reproduce / Expected vs actual" block is small. It loses to P03 only on novelty, because PRs #23 and #25 touch nearby ground.
3. **P01 (30)**: the agent cannot see the browser. It is the most painful node (18, strong evidence), but the recording already solves most of it, so the open work is the hand-off (P03). Novelty is 2 and smallness 2.
4. **P08 (30)**: oversized images break sessions. Evidence is strong (90 reactions on one issue), it is small and new, but fit is medium. This one needs the image limits checked in code before building.
5. **P05 (29)**: "fixed" with no proof. High pain (16), medium fit and size. A text checklist avoids the closed PR #22 (generated test).

By pain_score, P01 leads (18). P12, P05, P08 and P13 tie at 16. P12 is mostly an agent-vendor problem, so it ranks low as a pick (fit 2, smallness 1).

Limits: no Reddit evidence (blocked), several scores for fit and smallness are my judgement, and P09 and P13 are only partly verified.


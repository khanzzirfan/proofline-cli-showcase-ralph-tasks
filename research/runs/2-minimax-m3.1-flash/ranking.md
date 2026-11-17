# Ranking — run `2-minimax-m3.1-flash`

Date: 2026-11-17 · Nodes scored: **14** (P01–P14, contiguous) · Sources backing them: **60 verified URLs**
(no unverified, 1 dropped — see `sources.md`).

Every node is scored with the rubric from `prd-pain-research.md`:

```
pain_score = 2*frequency + 2*severity                              (max 20)
pick_score = 2*frequency + 2*severity + 2*fit + smallness + novelty (max 40)
```

## How the rubric was applied

**frequency** was computed from the node's own verified evidence, not from how loud the loudest thread is.

- `D` = number of distinct verified URLs cited as evidence in the node.
- `H` = number of those URLs with high engagement (≥20 likes or points, ≥10 reactions, or ≥25 comments).
- base: **5** if `D ≥ 9` or `H ≥ 5`; **4** if `D` is 5–8, or `D` is 3–4 with `H ≥ 3`; **3** if `D` is 3–4 with
  low engagement; **2** if `D` = 2; **1** if `D` = 1.
- floor: one source with ≥500 likes/points, ≥100 reactions or ≥50 comments lifts the node to at least **4**.
- **−1 discount** when the evidence is dominated by vendor marketing or by sources the node itself flags as
  off-point for its claim (this hit P05, P07, P09, P13 — the four nodes whose sources are mostly adjacent or
  vendor, and the reason their `status` is `partly-verified` or their engagement is thin).

**severity** = time, money or trust the pain costs. **fit** = how directly Session Recorder can address it.
**smallness** = 5 is one clean PR of a few hundred lines with tests, 0 is a new product.
**novelty** = 5 means nothing in the extension or its open PRs (`#21`–`#49`, plus `#22` closed by its author)
touches it; 0 means it is already done.

Ties are broken by the other score (`pick_score` inside the pain table, `pain_score` inside the pick table),
then by node id.

## Table 1 — by `pain_score` (how much the world hurts)

| # | Node | Pain | f | s | 2f+2s | Verified sources |
|---|---|---|---|---|---|---|
| 1 | P03 hand a bug straight to an agent, the recorder has no channel | **18** | 5 | 4 | 10+8 | 11 |
| 2 | P08 a CLI agent cannot take or read images | **18** | 5 | 4 | 10+8 | 12 |
| 3 | P10 nobody can prove the fix worked | **18** | 4 | 5 | 8+10 | 5 |
| 4 | P01 the agent has no console, network panel or DOM | **16** | 4 | 4 | 8+8 | 5 |
| 5 | P06 an AI PR reviewer cannot see the UI | **16** | 4 | 4 | 8+8 | 5 |
| 6 | P11 the report does not say which environment | **16** | 4 | 4 | 8+8 | 7 |
| 7 | P05 the evidence carries secrets and personal data | **16** | 3 | 5 | 6+10 | 5 |
| 8 | P12 agent-written duplicates fill the issue queue | **16** | 4 | 4 | 8+8 | 6 |
| 9 | P14 the agent cannot reach the app at all | **16** | 4 | 4 | 8+8 | 6 |
| 10 | P02 copy-paste is the hand-off and it arrives mangled | **14** | 4 | 3 | 8+6 | 3 |
| 11 | P04 the issue an agent starts from arrives text-only | **14** | 3 | 4 | 6+8 | 4 |
| 12 | P07 the customer or QA report arrives as words | **14** | 3 | 4 | 6+8 | 5 |
| 13 | P13 the evidence is too big and its cost is unknown | **14** | 3 | 4 | 6+8 | 5 |
| 14 | P09 a bug video is dead weight for an agent | **12** | 3 | 3 | 6+6 | 6 |

## Table 2 — by `pick_score` (how good it is as our one pull request)

| # | Node | Pick | f | s | fit | small | nov | 2f+2s+2fit+small+nov | PRs named in the node |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P03 hand a bug straight to an agent, the recorder has no channel | **37** | 5 | 4 | 5 | 4 | 5 | 10+8+10+4+5 | #22, #23, #24, #48 |
| 2 | P08 a CLI agent cannot take or read images | **34** | 5 | 4 | 5 | 3 | 3 | 10+8+10+3+3 | #29, #32, #43 |
| 3 | P01 the agent has no console, network panel or DOM | **34** | 4 | 4 | 5 | 4 | 4 | 8+8+10+4+4 | #22, #29 |
| 4 | P10 nobody can prove the fix worked | **32** | 4 | 5 | 4 | 3 | 3 | 8+10+8+3+3 | #22, #29 |
| 5 | P02 copy-paste is the hand-off and it arrives mangled | **32** | 4 | 3 | 5 | 4 | 4 | 8+6+10+4+4 | — |
| 6 | P06 an AI PR reviewer cannot see the UI | **31** | 4 | 4 | 4 | 3 | 4 | 8+8+8+3+4 | #22, #29 |
| 7 | P04 the issue an agent starts from arrives text-only | **31** | 3 | 4 | 5 | 3 | 4 | 6+8+10+3+4 | #24, #48 |
| 8 | P07 the customer or QA report arrives as words | **29** | 3 | 4 | 4 | 4 | 3 | 6+8+8+4+3 | — |
| 9 | P11 the report does not say which environment | **28** | 4 | 4 | 4 | 2 | 2 | 8+8+8+2+2 | #29, #41 |
| 10 | P05 the evidence carries secrets and personal data | **27** | 3 | 5 | 4 | 2 | 1 | 6+10+8+2+1 | #31, #37, #38, #42, #44 |
| 11 | P12 agent-written duplicates fill the issue queue | **26** | 4 | 4 | 3 | 2 | 2 | 8+8+6+2+2 | #49 |
| 12 | P13 the evidence is too big and its cost is unknown | **26** | 3 | 4 | 4 | 3 | 1 | 6+8+8+3+1 | — |
| 13 | P14 the agent cannot reach the app at all | **25** | 4 | 4 | 2 | 2 | 3 | 8+8+4+2+3 | — |
| 14 | P09 a bug video is dead weight for an agent | **23** | 3 | 3 | 3 | 1 | 4 | 6+6+6+1+4 | — |

The last column lists the extension PRs each node names in its "Session Recorder angle" section — the ones an
implementer must read first. For P03, P01, P06, P10 and P04 **none** of them implements the node's feature: they are
adjacent (same area, different feature), which is why those nodes keep a `novelty` of 3–5. For P05, P11, P12 and
P13 the listed PRs are direct competitors for the same idea, which is why their `novelty` collapses to 1–2.

## Why the top five are ordered that way

**1. P03 (37) — people want to hand a bug straight to an agent, and this recorder has no channel to do it.**
It tops both tables because it is the only node that is simultaneously the most evidenced (11 verified URLs, the
second-largest set in the run, with 9 432 likes, 305 reactions, 77 reactions and 171 points inside it), the most
directly answerable (the extension already captures every piece of evidence the agent lacks — the product is
finishing the delivery) and the least covered by the open PR list. The extension's own gap is the gap: `copyIssue()`
writes the *issue* Markdown to the clipboard, while the prompt that makes `report.md` usable lives only in
`docs/report-format.md` line 78. One action — copy an agent-ready bundle — closes it in a few hundred lines.

**2. P08 (34) — a CLI agent has no way to take a screenshot or read an image.**
It has the largest evidence set in the whole run (12 verified URLs) and the clearest concentration of engagement
(171 likes, 127 likes, 57 👍, 35 👍, 21 reactions, 30 comments), so `frequency` is 5. It loses to P03 on `pick_score`
because the extension already produces the screenshots — the missing piece is making the file paths reachable from
the agent's working directory, which is a smaller, more fiddly change (`smallness` 3) and overlaps a capability
that already exists (`novelty` 3). It is the strongest *second* pick.

**3. P01 (34) — the agent has no console, no network panel and no DOM.**
Same score as P08, and the same shape of argument: the evidence (a Cursor thread with 908 likes, a claude-code
issue with 76 reactions) is exactly the evidence the extension already captures. It ranks below P08 because it has
fewer independent sources (5) and because its fix *is* P03's fix — it is the market-side view of the same delivery
feature, so novelty is 4 rather than 5.

**4. P10 (32) — nobody can prove the fix worked.**
It has the highest `severity` in the run (5): an agent that claims a fix it never rendered costs trust and ships
regressions (one cited issue describes three failure cycles; another is a regression caught only by the full
suite). It cannot outrank P03 or P08 because the extension cannot photograph the *fixed* build — its screenshots
are of the reported session — so `fit` is 4, and the tractable slice of the feature is partly the same work as
P04's (attaching the reporter's annotated evidence to the filed issue).

**5. P02 (32) — copy-paste is the hand-off, and the paste arrives mangled or not at all.**
Its three sources carry the loudest engagement in the run (9 432 likes, 5 352 likes, 305 reactions with 140
comments), but `severity` is only 3: mangled text is annoying and there are workarounds (Ghostty `copy_to_clipboard:plain`,
a clipboard mod, `kitty.conf` `strip_trailing_spaces`), so the pain costs a retry rather than a project. P02 is
also the node that P03's feature dissolves — `report.md` is the zero-corruption version of the same gesture.

## What the ranking says about the vision and video area

The PRD asked for a plain answer on vision and video, and the ranking gives one.

- The **vision gap is real** — P08 (frequency 5, 12 sources) and P06 and P10 all sit in the top ten, and the
  evidence is not thin: a CLI agent literally cannot accept an image, and an AI reviewer approves UI work it has
  never rendered.
- The **video gap is real but crowded and large** — P09 is last on `pick_score` (23) because `smallness` is 1.
  `bradautomates/claude-video` (21 021 stars), `teunlao/vidin`, Clipy and Loom already occupy the keyframes-plus-timeline
  space, and turning a `.webm` into frames needs an ffmpeg-class pipeline that does not fit "one clean PR of a few
  hundred lines".
- **What an agent can use from what the extension already records**: `video/*.webm` ships only at L0/L1, screenshots
  degrade to a filename manifest at L3, and `report.md` is prose. A text-only agent gets names and timestamps, never
  pixels or motion.

The ranking therefore points at **delivery, not capture** — which is exactly what P03, P08, P01, P02 and P04 have in
common. The three that are not delivery (P05 redaction, P11 environment metadata, P12 duplicate grouping) all score
low on `novelty` because open PRs `#31/#37/#38/#42/#44`, `#29/#41` and `#49` already occupy them.

## Nodes deliberately not picked, and why

| Node | Why not |
|---|---|
| P05 secrets and PII | `novelty` 1 — five open PRs already claim redaction (`#31`, `#37`, `#38`, `#42`, `#44`). The notes flag this topic as crowded. |
| P11 environment metadata | `novelty` 2 — `#29` (browser/OS/viewport) and `#41` (storage snapshot) already cover both halves. |
| P12 duplicate grouping | `novelty` 2 — `#49` owns "group recordings of the same error"; the rest is a GitHub-platform problem with its own duplicate-detection preview. |
| P13 context cost | `novelty` 1 — trim levels and a token estimator already exist (`lib/export/tokens.ts`). |
| P09 video | `smallness` 1 — the feature is large and the market is taken. |
| P14 agent cannot reach the app | `fit` 2 — a proxy policy and an egress allowlist are not something a Chrome extension can fix. Honest answer: do not build a feature here. |

## Limits of this ranking

- **No Reddit, Chrome Web Store, Product Hunt or G2 evidence reached the run.** Reddit's JSON API answers 403 to
  every endpoint and `web_fetch` returns a shell; the review sites are JS shells. Every frequency score therefore
  rests on GitHub issues, the Cursor forum, Hacker News and vendor blogs, which skew toward developers and away
  from QA, support and product people.
- **Vendor material is counted but discounted.** Five of the six P09 sources and three of the five P07 sources are
  vendor or competitor material; that is why both nodes carry a −1 frequency discount and a `partly-verified` status.
- **Engagement counts are point-in-time.** All signals were read on 2026-11-17 and several cited issues are still
  open, so the scores can move.
- **P03's and P08's evidence sets overlap with P02's and P01's.** They are counted in each node, because each URL
  genuinely evidences each claim; the ranking compensates by lowering `novelty` on the nodes whose fix is the same
  feature (P01, P02).
- `gh` is not installed in this environment, so the open-PR overlap list comes from the context notes and from one
  `web_fetch` on PR `#23` ("docs: add self-contained UJG bundle" — it mentions an "agent-neutral prompt" and a
  visual-review gallery, so it is adjacent to P03 but is a docs bundle, not a clipboard hand-off).

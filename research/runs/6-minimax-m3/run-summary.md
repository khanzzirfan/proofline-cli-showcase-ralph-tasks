# Run summary — `6-minimax-m3` (agent `minimaxai/minimax-m3`)

Research run for the PRD *"What hurts people who hand bugs to AI coding agents?"*, 2026-11-17.
Output dir: `research/runs/6-minimax-m3/`. Nothing was written outside it.

---

## Counts

| Metric | Count |
|---|---|
| Search queries planned and executed | **61** numbered queries across **8** source types (`plan.md` §2: A1–A15, B1–B3, C1–C6, D1–D7, E1–E5, F1–F11, G1–G8, H1–H6) |
| Hypotheses tested | **9** (H1–H9: the five pains from the notes, plus reproduction, agent-side triage/duplicates, the required vision/video area, and pains the notes missed) |
| Source URLs cited | **51** distinct URLs (S1–S51 in `sources.md`) |
| **Verified** | **51** — every one re-opened in the US-003 pass |
| **Unverified** | **0** |
| **Dropped claims** | **8** (in the "Dropped claims" table of `sources.md`) |
| Pain nodes | **16** (`nodes/P01`…`P17`, P09 merged into P17 and deleted) |
| Evidence lines across nodes | **85** bullets, referencing **43** distinct URLs |
| Popular places covered | **13** of the PRD's list (see below) |
| Raw API payloads kept | **122** files under `raw/` |
| Nodes with ≥ 2 verified sources | **16 / 16** (100 %) |
| Nodes that are **not** in section 5 of the context notes | **3** — P04 (video), P16 (auditable verdict), P17 (evidence cost); P12's credential-*type* sub-idea and P13 are also new framings |
| Open PRs checked against before proposing | **19** (#21–#49, plus #22 closed by its author) |

## Which tools worked

| Tool | Worked? | What it was used for |
|---|---|---|
| **`web_fetch`** | **Yes** — the single best tool | Rendering GitHub issue pages as plain text (body **plus every comment**, with the reaction counts visible), GitHub org discussions, Chrome Web Store listings and review pages, competitor repos. Does not consume the GitHub *search* rate limit. |
| **GitHub search API** (`api.github.com/search/issues`, `sort=reactions` / `sort=comments`) | **Yes** | The main discovery mechanism and the popularity signal (`reactions["+1"]`, `reactions.total_count`, `comments`). 10 req/min unauthenticated. |
| **GitHub core API** (issues, PRs) | **Yes**, but the 60/h limit bit | Fetching issue and PR metadata. Backs off to `web_fetch` for bodies. |
| **GitHub repo discovery** (`search/repositories`) | **Yes** | Finding competitors and grounding the `novelty` scores. Counts drift between passes — cite with a date. |
| **Cursor forum Discourse JSON** (`forum.cursor.com/search.json`, `t/{id}.json`) | **Yes** — the best single source | Ten topics with full bodies, `posts_count`, `reply_count`, `like_count`, `views` and dates, no rate limit hit. `web_fetch` on the same forum renders almost nothing; the JSON API is strictly better. |
| **Hacker News Algolia** (`hn.algolia.com/api/v1/search`, `/items/{id}`) | **Yes** | Story points and the full comment tree. The Momentic launch thread (168 points) is the highest-signal evidence in the run. Gotcha: `tags=comment` hits carry no `points` — join on `story_id`. |
| **Chrome Web Store** (via `curl` + text extraction) | **Yes** | Competitor listings and low-star reviews. The "Related extensions" carousel on one listing named ~12 direct competitors. Gotcha: `web_fetch` sometimes hits a Google consent interstitial — `curl` first, `web_fetch` second. |
| **`web_search`** | **Yes** | Broad discovery and the only route to Reddit. With `allowed_domains: ["reddit.com"]` it returns almost nothing useful. |
| **`curl` against public JSON APIs** | **Yes** | Every GitHub / Discourse / Algolia / Store call went through `curl -sL -A "pain-research/1.0"` with ~2 s spacing, and the raw payloads were kept under `raw/`. |
| **Reddit (`.json`, `.rss`, post URLs, `old.reddit.com`)** | **No — fully blocked** | `.json` returns **403** with every user agent tried; `old.reddit.com` 302s to a consent interstitial; `web_fetch` on a post URL returns the "Prove your humanity" bot challenge (HTTP 200, zero content). **No Reddit claim is used anywhere in this run.** |
| **G2 / Product Hunt** | **No — blocked** | 403/504 via both `web_fetch` and `curl`. Substitute: Chrome Web Store reviews and HN launch threads. |
| **`api.github.com/search/issues` for `getcursor/cursor`, `sst/opencode`, `All-Hands-AI/OpenHands`** | **No** | `422 Validation Failed` ("The listed users and repositories cannot be searched") in this environment. Cursor was covered through the forum instead; OpenHands and opencode only indirectly. |
| **Vendor docs / changelogs** | **Yes**, but weak | Used for capability facts (e.g. GitHub Copilot's visual-input support). Treated as weak evidence throughout. |

## Popular places covered (PRD requires ≥ 8)

anthropics/claude-code issues · forum.cursor.com (Discourse JSON) · github/copilot-cli · openai/codex ·
cline/cline · RooCodeInc/Roo-Code · ChromeDevTools/chrome-devtools-mcp · microsoft/playwright-mcp ·
Hacker News (Algolia) · Chrome Web Store (competitor listings + reviews) ·
Microsoft/vscode-pull-request-github · GitHub community discussions + Agentic Workflows ·
GitHub repo discovery · GitHub Copilot docs.

**Not covered, declared rather than silently dropped:** r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev,
r/QualityAssurance, r/ExperiencedDevs, r/programming (Reddit blocked); G2 and Product Hunt (blocked);
`getcursor/cursor`, `sst/opencode` and `All-Hands-AI/OpenHands` GitHub issue searches (422).

---

## What was produced

- `plan.md` — the US-001 search plan: 61 queries, 9 hypotheses, a 17-row provisional node table, a
  source-type map with per-tool status, and method rules.
- `nodes/P01`…`P17` (16 files) — the US-002/US-003 evidence nodes, each with ≥ 4 evidence links, the
  popularity signal, "how users want it fixed", "workarounds people use today", the Session Recorder angle
  with overlapping open PRs named, and the rubric scores.
- `sources.md` — every URL with a `verified | unverified | dropped` status, the US-003 verification
  narrative (what changed and why), the popular-places coverage table, and the dropped-claims table.
- `ranking.md` + `ranking.json` — the two ranked tables and the machine-readable ranking, **both
  generated from one script** (`raw/regen_ranking.py`) and checked against each other
  (`raw/validate_ranking.py`).
- `recommendation.md` — the top 3 feature specs (US-005).
- `run-summary.md` — this file.
- `raw/` — 122 saved API payloads plus the two scripts.

## The one substantive correction this run produced

US-004 set `top_pick` to P05 ("make the screenshots safe for agents"), on the claim that *"no 2000 px
dimension check exists anywhere"* in the extension. **That claim was wrong.** US-005 grepped for the
constant rather than the literal number and found:

```
lib/capture/screenshots.ts:38:  const MAX_SHOT_DIM = 1400;
```

with `ScreenshotScheduler.capture()` (lines 160–190) already downscalling any screenshot whose longest side
exceeds 1400 px via `OffscreenCanvas` and re-encoding it as JPEG. 1400 px is comfortably under the 2000 px
limit that poisons a Claude Code session. The sizing and format half of P05 was **already shipped**.

P05 was re-scored (smallness 4→3, novelty 3→2, pick_score 33→29), `ranking.md` and `ranking.json` were
regenerated from the corrected scores, and the open remainder of the pain became **feature 2** in
`recommendation.md` — not "make the image safe" but "make the image *reachable*": the report names the
screenshot file but the agent has no way to open it, and the extension has no path for delivering image
bytes at all.

---

## Weaknesses of this evidence

1. **No Reddit.** Reddit is the PRD's most-requested source and it contributed **zero** evidence. Every
   subreddit in the PRD's list is uncovered. The frequency scores are therefore drawn entirely from
   GitHub reactions, Cursor forum engagement, HN points, Chrome Web Store ratings and vendor docs. This
   biases the set toward *developer-tool* complaints and away from *QA and support* complaints, which live
   disproportionately on Reddit and in the "Show HN" threads. Read every frequency score as a floor.

2. **OpenHands and opencode are barely covered.** Their GitHub issues cannot be searched from this
   environment (422), and they were not replaced by a forum. Both are named by the PRD and neither is
   properly represented.

3. **GitHub reactions are a proxy, not a census.** A 👍 304 means "304 people who *cared enough to
   react*", not "304 people who hit this". The frequency rubric maps reaction counts onto 0–5, which
   compresses a lot of real variance and rewards whichever thread happened to go viral.

4. **Engagement is not severity.** The highest-reaction thread in this run (claude-code #18170, 👍 304) is
   an annoyance; the most *expensive* pain found (P12, recording your own passwords) has a smaller thread.
   The rubric weights them 2:2, which is a policy choice, not a finding.

5. **Vendor evidence is weak and was treated as weak.** The momentic benchmark numbers in P17 (269 bugs,
   $2.67 per bug) are a vendor's own benchmark of its own product. They are cited because the *price
   points* are checkable and the framing is useful, not because the comparison is sound.

6. **The competitive picture is thin and possibly out of date.** Two of the most important novelty
   constraints (Clipy, ThinkRun) were found only in the US-003 verification pass, by following a
   competitor named inside a source. That means the competitor set is **known to be incomplete**. The
   `novelty` scores for P02, P03, P04 and P05 are all capped by competitors we found by luck, and more
   exist. Any of those novelty scores should be read as an upper bound.

7. **The Chrome Web Store is a poor volume source.** Most of these niche extensions have 0–23 users and
   0–11 ratings. The store was good for *quotes* and for the "Related extensions" carousel; it cannot
   support a claim about market size.

8. **One of the top five picks rests on a single thread.** P16 (the auditable verdict, novelty 4) leans
   mostly on one HN launch thread with 168 points. It is well quoted and technically plausible, but its
   *frequency* score of 3 is the weakest of the top five.

9. **The scores rank this run's nodes for this extension.** They are not a forecast and not a market
   ranking. Four independent runs are comparing outputs; a different run with different sources would
   score these nodes differently, and the owner should compare the four rankings rather than treat this
   one as ground truth.

10. **US-005 re-read the source and found a US-004 error.** That is worth stating plainly: one of the two
    score moves in US-004 (P05 confirmed) was based on a grep that searched for the wrong token. The other
    two (P17 down, P16 up) were re-verified and hold. The pattern to carry forward is in the progress
    log: *a node that claims "the extension cannot do X" must show the grep that proves it* — and the grep
    must look for the **constant**, not the literal number in the issue title.

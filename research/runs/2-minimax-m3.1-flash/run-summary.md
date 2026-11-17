# Run summary — `2-minimax-m3.1-flash`

Research run: **2-minimax-m3.1-flash** (independent agent, one of four).
Question answered: *what hurts people who hand browser bugs to AI coding agents, and which pain should Session
Recorder by Proofline fix first?*

Dates: plan and collection 2026-11-17 · scoring and recommendation 2026-11-17.

---

## 1. What I did, in order

| Story | What happened | Artefacts |
| --- | --- | --- |
| **US-001** | Read `00-context-notes.md`, the extension's `README.md`, `PRODUCT.md`, `docs/report-format.md`, `docs/PLAN.md` and the source tree. Probed every research channel before trusting it (5 probes saved). Wrote a search plan. | `plan.md` |
| **US-002** | Ran the searches for real. 39 GitHub Search API queries, 13 Cursor-forum Discourse calls, 10 Hacker News Algolia calls, `web_search` for discovery, `web_fetch` to open and quote 13 pages. Wrote 15 nodes. | `nodes/P01..P15`, `sources.md`, `raw/` |
| **US-003** | Re-opened every cited URL, machine-checked **102 quoted fragments** against the re-fetched payloads, merged the one duplicate pair (P03/P14 → P03), dropped one unsupported claim. | `sources.md` (rewritten), `nodes/` (14), `raw/verify/` (68 payloads), `raw/validate_sources.py`, `raw/verify_final_quotes.py` |
| **US-004** | Operationalised the rubric before scoring (evidence-count → frequency, a written tie-break rule), scored all 14 nodes, and wrote both rankings. A checker script caught four cross-file drifts. | `ranking.md`, `ranking.json`, `raw/validate_ranking.py` |
| **US-005** | Re-read the extension's source tree to ground the feature specs in real files; confirmed the open-PR list live against GitHub (22 open PRs) and read PR **#23** and **#43** to characterise the overlap precisely. | `recommendation.md`, `run-summary.md` |

---

## 2. Counts

| Metric | Count |
| --- | --- |
| Planned queries in `plan.md` | **63** |
| Query source types (`ST1`–`ST10`) | **10** |
| Hypotheses tested (`H1`–`H10`) | **10** |
| Planned nodes → final nodes | 18 → **14** (`P01`–`P14`, contiguous) |
| GitHub Search API queries executed | **39** (saved as `raw/gh_*.json`) |
| Cursor forum Discourse calls (8 threads + 5 searches) | **13** (`raw/cursor_*.json`) |
| Hacker News Algolia calls (6 searches + 4 item threads) | **10** (`raw/hn_*.json`) |
| Capability probes before use | **5** (`raw/probe_*.json`) |
| Pages opened with `web_fetch` in collection | **13** |
| URLs re-opened during verification | **61** (68 raw payloads in `raw/verify/`: 39 GitHub issue/PR + 6 comment threads + 2 search results + 10 Cursor threads + 7 HN items + 3 READMEs + 1 exhausted-quota error body) |
| **Distinct URLs cited in `nodes/`** | **61** |
| **Verified** | **60** |
| **Unverified** | **0** |
| **Dropped** (opened but did not support the claim) | **1** |
| Evidence lines across the 14 nodes | **81** |
| Nodes with status `verified` | **12** |
| Nodes with status `partly-verified` | **2** (P07, P09) |
| Distinct source places covered | **22** (21 of them from the PRD's popular-places list) |
| Quoted fragments machine-checked verbatim | **102** |
| Open PRs in the target repo confirmed live | **22** |
| GitHub issues/PRs read through the REST API | **39 issue/PR payloads + 6 comment threads** (`raw/verify/gh_*.json`, `raw/verify/comments_*.json`) |
| LLM calls used to write this run | **1** (me) |

### Top three by `pick_score`

| Rank | Node | Feature recommended | pick | pain |
| --- | --- | --- | --- | --- |
| 1 | **P03** | Copy for AI agent — clipboard bundle (prompt + trimmed `report.md`) | **37** | 18 |
| 2 | **P08** | Screenshots a text-only agent can use — captions + `AGENT.md` in the pack | **34** | 18 |
| 3 | **P01** | Copy the failing call — console errors + failed requests only | **34** | 16 |

---

## 3. Which tools worked

| Tool | Result | How it was used |
| --- | --- | --- |
| **GitHub REST API — `search/issues` and `search/repositories`** | **Worked, best source in the run.** 39 queries. The search bucket (10/min) is independent of the core bucket (60/hr), so discovery survived the core quota running out. | Title-scoped queries (`repo:X browser in:title`) were the only way to get signal — an unscoped `repo:X browser console` returns 852 hits dominated by unrelated high-reaction issues. |
| **GitHub REST API — core (`/repos/{owner}/{repo}/issues/{n}`)** | **Worked, with a quota wall.** Gave `body`, `state`, `created_at`, the `comments` count and the full `reactions` breakdown. Exhausted (60/60) twice during the run; US-005's own PR-body fetches were refused and had to go through `web_fetch` instead. | One call per cited issue; comment quotes needed `/issues/{n}/comments?per_page=100&page=N` before a quote could be declared missing. |
| **`web_fetch`** | **Worked** on GitHub issue/PR/discussion HTML (returns the full body plus reaction counts) and on plain HTML pages. **Failed** on Reddit and on Chrome Web Store / Product Hunt / G2 listing pages (JS shell only). | Used for every quoted GitHub body in US-002, for all 61 verification passes in US-003, and for PR #23 and #43 in US-005. |
| **`web_search`** | **Worked** for discovery (finding URLs to fetch) and poorly for ranking. | Used to discover candidate URLs, including in repositories that refuse `repo:` searches. |
| **Cursor forum Discourse JSON API** | **Worked, highest yield per call.** `forum.cursor.com/t/<id>.json` returns the full thread, per-post `score`, `views`, `created_at` and the canonical slug. | 8 full threads + 5 keyword searches. This is where the run's two most-liked pieces of evidence live (9 432 likes and 908 likes). |
| **Hacker News (Algolia)** | **Worked.** `/search?tags=story` and `/search?tags=comment` for points and text, `/items/<id>` for whole threads. | 10 calls. One caveat: a live HN page can render while Algolia's `/items/<id>` returns 404 — a deleted story body lives in the author's first comment. |
| **Reddit JSON API** | **Did not work.** HTTP 403 on `search.json`, `top.json` and every per-post endpoint, with a generic UA, a browser UA and `Accept: application/json`; `old.reddit.com` 302s. `web_fetch` returns only a shell. | **Zero Reddit posts were cited.** The PRD listed seven subreddits; none contributed evidence. |
| **Chrome Web Store / Product Hunt / G2 reviews** | **Did not work.** HTTP 200 but only the JS shell, to both `web_fetch` and `curl`. | **Zero review pages were cited.** |
| **Repository discovery** | **Partly worked.** `getcursor/cursor`, `All-Hands-AI/OpenHands` and `sst/opencode` refuse `repo:` searches with `422 Validation Failed` (issues disabled). Their evidence came from the Cursor forum, GitHub Discussions and HN instead. | Direct issue URLs still work for OpenHands (`All-Hands-AI/OpenHands#8387` redirects); `sst/opencode#1589` is really `anomalyco/opencode` PR #1589. |
| **Vendor docs / competitor READMEs** | Worked, but counted as weak evidence and discounted. | `teunlao/vidin`, `bradautomates/claude-video`, `Ami3466/ai-live-log-bridge`, `klavity.in`, `cobaltcapture.com`, `github.blog` changelog. |

---

## 4. Weaknesses of my evidence

**1. No QA, support or product voice.** This is the biggest gap. Reddit, Chrome Web Store, Product Hunt and G2 — the
four places where QA engineers, support staff and product managers talk — were all unreachable. Every frequency
score therefore rests on GitHub issues, the Cursor forum, Hacker News and vendor blogs, which skew heavily toward
developers. The PRD's §5 pains were all developer pains, and my run found no independent voice from the people who
*write* the bug reports. Treat any claim about QA workflow as inferred, not observed.

**2. Engagement counts are point-in-time.** All signals were read on 2026-11-17. Several cited issues are still open
and several popular threads are still gaining likes, so the frequency scores can move in either direction.

**3. Vendor material is a meaningful fraction of the evidence, and it is counted but discounted.** Five of P09's six
sources and three of P07's five are vendor or competitor material — that is why both nodes carry a −1 frequency
discount and a `partly-verified` status. The discount is a judgement call, not a measurement.

**4. The top nodes' evidence sets overlap.** P03, P08, P01 and P02 all cite the same Cursor thread
(`forum.cursor.com/t/integration-with-developer-tool/34824`) and the same claude-code screenshot issue
(`#12644`). Each URL genuinely evidences each claim, so each node counts it, but the four nodes are less independent
than their individual source counts suggest. The ranking compensates by lowering `novelty` on the nodes whose fix is
the same feature (P01, P02) — but that is a mitigation, not a correction.

**5. Two of the top three nodes are the same pain seen from two sides.** P03 ("people want to hand a bug straight to
an agent") and P01 ("the agent has no console, network panel or DOM") have the same fix — delivery. The PRD's rubric
has no way to express that, so they are ranked as separate nodes and the ranking even says so. I have flagged it in
`ranking.md` and in `recommendation.md` rather than silently merging them, because the merge (P03/P14) was already done
once in US-003 on evidence grounds.

**6. The open-PR overlap list is partly second-hand.** `gh` is not installed in this environment and the GitHub core
quota was exhausted, so the PR titles come from the GitHub **search** API (22 open PRs, confirmed live in US-005) and
the PR *bodies* come from the context notes plus one `web_fetch` each on PR #23 and PR #43. I read those two
bodies because they are the closest neighbours of my pick; I did **not** read all 22 PR bodies. A PR I did not open
could overlap more than I claim. The implementer must read #23, #43, #29, #39, #41 and the redaction family (#31,
#37, #38, #42, #44) before starting.

**7. No measurement of the feature itself.** Everything here is qualitative. Nobody has measured whether a
clipboard bundle actually shortens the time-to-fix, and the extension has "almost no real user issues" (per the
context notes), so there is no in-product signal to check the hypothesis against.

**8. The vision/video area is under-sampled.** I searched it hard (the PRD required it) and found the gap is real, but
most of the video evidence is competitor marketing rather than user complaints, and I could not reach any Reddit
discussion of "agent cannot watch video" — which is exactly where the strongest evidence would be. The conclusion
("the video gap is real but the feature is too large and the market is taken") is therefore weaker than the
conclusion about images.

**9. Selection bias towards loud bugs.** The engagement-weighted frequency rule favours issues that many people
*reacted to*, which correlates with "affects many developers" rather than "costs a QA team the most hours". A quieter,
more expensive pain would score lower than it deserves.

**10. One run, one model.** This is a single independent pass by one model with its own reading of the same
evidence. The owner is comparing four runs precisely because any single one is one perspective. Where my run is most
likely to be wrong is the **novelty** scores: they depend on a partial read of the open-PR list, and a single missed
PR would invalidate a score of 4 or 5.

---

## 5. The answer in one paragraph

People do not complain that bug reports lack evidence — they complain that the evidence never *reaches* the agent.
The extension already captures the console, the network, the screenshots and the annotations that the agent cannot
see; what it lacks is a channel. So the pick is **delivery, not capture**: one click that copies an agent-ready
bundle (the instructions that today live only in `docs/report-format.md`, plus the trimmed `report.md`, plus the list
of files that ship with it) to the clipboard. It is the smallest change that closes the largest evidenced gap, it
needs no new permission or dependency, and no open PR touches it. The two runners-up — captions so a text-only
agent can read the screenshots, and a "just the failing call" excerpt — are both follow-ups on the same plumbing.
Redaction, environment metadata, duplicate grouping and video are the areas to avoid: the first three are already
claimed by open PRs (#31/#37/#38/#42/#44, #29/#41, #49) and the fourth is a large feature in a taken market.

---

## 6. Reproduction notes

- Raw payloads: `raw/` (collection) and `raw/verify/` (verification). Nothing outside this directory was written.
- Checkers, re-runnable:
  - `raw/validate_sources.py` — checks the `sources.md` header counts against its own table, that every node has a
    `status`, and that every evidence URL is listed.
  - `raw/verify_final_quotes.py` — re-reads every quoted fragment in `nodes/` against the re-fetched raw payloads.
  - `raw/validate_ranking.py` — checks `ranking.json` against the PRD schema key-for-key, recomputes both scores
    from the five axes, checks both rank arrays are sorted and tie-broken as `ranking.md` claims, parses the
    `## Scores` line out of every node and asserts it equals `ranking.json`, and asserts both `ranking.md` tables
    list every node exactly once.
  - `raw/validate_recommendation.py` — checks `recommendation.md` (US-005): exactly three features, each with the six
    required sections, a pain node cited, and both a unit and a Playwright test named; every path in a "Files likely
    touched" table really exists in the extension repo (or is marked **new** and sits inside its source tree); every
    PR number cited is in the live open-PR list, and the one closed PR named is described as closed; the three
    features map onto the three highest `pick_score` values using the tie-break written in `ranking.md`; and
    `run-summary.md` states the required counts and names the required tools.
- PR overlap evidence for US-005: `raw/us005_open_prs.json` (the 22 open PRs, trimmed to the fields the
  recommendation relies on) and `raw/us005_pr_overlap_notes.md` (the verbatim bodies of PR #23 and PR #43, the two
  closest neighbours of the pick).
- No git command that changes anything was run. No PR, issue or comment was opened anywhere. No account was signed
  into. Every request carried the user agent `pain-research/1.0` and no name, email or token.

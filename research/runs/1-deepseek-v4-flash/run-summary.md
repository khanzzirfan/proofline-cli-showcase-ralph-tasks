# Run summary — `1-deepseek-v4-flash`

Independent pain-research run for Session Recorder by Proofline. Everything read was public and
read-only; all files written live in this OUTPUT_DIR only. Dates are `YYYY-MM-DD`.

## What I searched (and with which tool)

- **Web search** (broad + `site:reddit.com`, `site:news.ycombinator.com`, `site:github.com`,
  `site:forum.cursor.com`) — discovery and Reddit/forum fallback.
- **Web fetch** on `github.com/<repo>/issues/<n>` (body, comments, open/closed state, exact
  `👍 React with 👍 N` counts, no rate limit), on repo pages, blogs, vendor docs and the Chrome Web
  Store listing — the main verification tool.
- **`curl -sL -A "pain-research/1.0"`** on the **Hacker News Algolia API**
  (`hn.algolia.com/api/v1/search`, story + comment tags) and the **GitHub search APIs**
  (`api.github.com/search/issues?sort=reactions|comments`, and
  `api.github.com/search/repositories?sort=stars`). Small raw JSON saved under `raw/`.
- **Reddit**: attempted the JSON API (`search.json`, `top`, comments) — blocked for this host.
- Read-first docs via `shell_command cat` (extension is outside the workspace root):
  `00-context-notes.md`, `README.md`, `PRODUCT.md`, `docs/report-format.md`, `docs/PLAN.md`, plus the
  extension source I cite in `recommendation.md`.

The plan (`plan.md`) named 30 concrete queries across 7 source types and 7 hypotheses (H1–H5 from the
notes, H6 vision/video, H7 pains the notes missed). I ran those plus ad-hoc follow-ups during
US-002/US-003. GitHub, HN, blogs, repo discovery and vendor docs are the load-bearing sources.

## Counts

| Thing | Count |
|---|---|
| Planned queries | 30 (plus ad-hoc follow-ups) |
| Nodes written | 14 (`P01`–`P09`, `P11`–`P15`; `P10` merged into `P04` in US-003) |
| Node files required by PRD | ≥12 (aim 15–20) — met |
| URLs catalogued in `sources.md` | 79 list lines |
| `sources.md` header status | **verified: 67, unverified: 12, dropped: 4** |
| My recount of list entries | 65 verified · 12 unverified · 4 dropped |
| Raw JSON saved in `raw/` | 29 files |
| Popular places covered | 14 |

The header (67/12/4) counts two verified URLs that share a list line with another (the two
`api.github.com/search/repositories` entries), so it reads one higher per line than a naive
`grep` of list items; both numbers are stated here so the owner can reconcile them.

**Node statuses:** verified 8 (P03, P04, P05, P06, P07, P08, P12, P15); partly-verified 6 (P01,
P02, P09, P11, P13, P14 — each has ≥1 verified source for its main claim; the unverified share is
Reddit / forum.cursor.com). No node is `unverified` end-to-end.

## Which tools worked, and which did not

- **Worked, primary:** `web_fetch` on GitHub **issue pages** (exact reactions, state, comments);
  `curl` on HN Algolia (titles + comment text) and GitHub **search/repo-discovery APIs**;
  `web_fetch` on blogs/docs. These are the sources every node rests on.
- **Worked, secondary:** `web_search` with `site:` filters to reach Reddit and forum snippets I could
  not open directly.
- **Blocked:** **Reddit** JSON API and `web_fetch` both return an HTML "Prove your humanity" shell —
  Reddit evidence is `site:reddit.com` search snippets only, marked `unverified`. **forum.cursor.com**
  threads are JS-rendered: `web_fetch` returns the title only — snippets cited, `unverified`.
- **Constrained:** the **GitHub unauthenticated core REST limit is 60/hr** and was exhausted; I
  switched to `web_fetch` on issue pages, which has no such limit. **`gh` CLI is not installed.**
- **Renames handled:** `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`; `sst/opencode` →
  `anomalyco/opencode`; `docs.github.com/.../provide-visual-inputs` 301s to a renamed page (cited
  what the landing page says).

## Weaknesses of this evidence

- **Two hosts are unverifiable here** (Reddit, forum.cursor.com) — 12 catalogued URLs. They support
  three nodes (P01, P02, P09, P11, P13, P14 partly) that are therefore only `partly-verified`, and
  their quotes come from search snippets, not opened pages.
- **Vendor marketing is over-represented for the two vision/video nodes.** Chrome DevTools-for-agents
  blog, BugDump, TraceBug, apidog, thunkle and videolens/aitasks are vendors selling the fix; they are
  labelled weak, and the *demand* side leans on GitHub issues and OSS repos (`s17labs/videobug`,
  `amagilabs/amagi-screen`) that have near-zero stars. The gap is real but thinly measured.
- **Popularity signals are uneven.** Some HN threads are 1–6 points; several `microsoft/playwright-mcp`
  issues were cited and then judged weak (0 reactions). Reaction/comment counts are a proxy, not
  proof of frequency.
- **Reviews were shallow.** I read the Chrome Web Store Jam *listing* summary and a Toolradar pricing
  page; individual low-star reviews and G2 / Product Hunt comment bodies were not rendered to me, so
  the "pain from reviews" evidence is thin.
- **No Product Hunt / G2 deep dives**, and no Reddit comment trees — the PRD's richer social sources
  are the weakest part of this run.
- **Independence limit:** I never opened any folder under `research/runs/` except this OUTPUT_DIR, and
  made no state-changing git or network calls, so nothing here cross-checks the other three runs.

## Verdict

The strongest, best-evidenced lanes are **P02** (agent clipboard hand-off; small, unfilled) and the
two vision lanes **P08** (video → frames + timeline) and **P07** (image manifest for text-only
agents), followed by **P09** (repro steps). Redaction (P05) hurts most in the world but is crowded
with six open PRs, so it is context only. Full ranking in `ranking.md` / `ranking.json`; the three
buildable specs are in `recommendation.md`.

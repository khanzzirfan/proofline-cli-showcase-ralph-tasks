# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

*Add reusable patterns discovered during development here.*

### Research API patterns (verified 2026-11-17)

- **GitHub has two separate unauthenticated buckets.** `api.github.com/search/*` allows 10 requests/minute and is
  independent of the 60/hour core bucket. The core bucket exhausts fast during a research run, so prefer
  `search/issues` and `search/repositories` for discovery and pace them ~8s apart.
- **Repos with issues disabled cannot be searched.** `repo:getcursor/cursor`, `repo:All-Hands-AI/OpenHands` and
  `repo:sst/opencode` return `422 Validation Failed` ("listed users and repositories cannot be searched"). Their
  evidence must come from a forum, GitHub Discussions HTML, or Reddit/HN instead.
- **Discourse forums expose a JSON API.** `https://forum.cursor.com/search.json?q=<terms>` returns matching topics and
  `https://forum.cursor.com/t/<slug>/<id>.json` returns the full thread text with usernames, dates and read counts.
  `web_fetch` on the same HTML page returns only the page title, so always use the `.json` twin.
- **`web_fetch` on GitHub issue/discussion HTML returns the full body plus reaction counts**, so it is a reliable
  substitute for the exhausted GitHub core API when reading a specific known issue.
- **Reddit blocks the JSON API** (403 on `search.json`, `top.json` and per-post JSON, generic and browser UA) and
  `web_fetch` returns only a shell. Fall back to `web_search` with `site:reddit.com` and mark the result unverified.
- **Chrome Web Store and Product Hunt listing pages are JS shells** to both `web_fetch` and `curl`; treat review text
  there as unverified unless a readable mirror is found.

### Verification patterns (verified 2026-11-17, US-003)

- **Use the GitHub core REST API, not `web_fetch`, to verify a cited issue.** One
  `GET /repos/{owner}/{repo}/issues/{n}` returns `body`, `state`, `state_reason`, `created_at`, the `comments` count
  and the full `reactions` breakdown (`+1`, `heart`, `eyes`, `hooray`). The `html_url` field also settles
  issue-vs-PR and redirect questions (`sst/opencode#1589` → `anomalyco/opencode/pull/1589`). The core bucket resets
  hourly, so a 40-issue verification pass fits easily in one window.
- **A quote in the issue body and a quote in a comment need different endpoints.** Body quotes live in
  `issue.body`; comment quotes live in `issue.comments[].body`. Fetch
  `/repos/{owner}/{repo}/issues/{n}/comments?per_page=100&page=N` (pages of 100) before concluding a quote is missing.
- **A quote-matching normaliser must handle markdown.** Strip `**`, backticks, list markers, smart quotes and
  escaped `\"`. Two traps: a normaliser that strips inline `N. ` markers also eats a trailing " 404. ", and a
  normaliser that unifies apostrophes must apply the same rule to both sides of the comparison.
- **A live HN page can render while Algolia's `/items/` returns 404.** A text post has an empty story body and no
  `points`; the content sits in the author's own first comment, and `objectID != story_id`. Never drop such a
  citation on the Algolia 404 alone — fetch `news.ycombinator.com/item?id=<id>` and check it.
- **Discourse `score` is fractional** (35.6, 171.4, 9432.0). Round it for the signal line and say it is rounded.
- **Verify the repo on the URL, not only the issue number.** Numbered issues repeat across repos: the screenshot
  compaction issue is `openai/codex#31040`, while `anthropics/claude-code#31040` is about plugin-cache cleanup.
- **Machine-check the whole node set before shipping.** `raw/verify_final_quotes.py` re-reads every quoted fragment
  in `nodes/` against the re-fetched raw payloads; `raw/validate_sources.py` checks the `sources.md` header counts
  against its own table, that every node has a `status`, and that every evidence URL is listed. Run both.

### Scoring-pass patterns (verified 2026-11-17, US-004)

- **A scoring pass is a cross-file edit, so validate it with a script, not by eye.** `raw/validate_ranking.py`
  re-checks the JSON schema key-for-key, recomputes `pain_score` and `pick_score` from the five axes, verifies both
  rank arrays are sorted *and* tie-broken the way the document claims, parses the `## Scores` line out of every
  node file and asserts it equals `ranking.json`, asserts both `ranking.md` tables list every node exactly once, and
  asserts every evidence URL in a node is mapped to that node in `sources.md`. It caught four real drifts on the
  first run: three node `## Scores` lines that still carried the pre-scoring frequency (P03, P04, P14) and one
  evidence URL (`news.ycombinator.com/item?id=21049087`) that P03 cited but `sources.md` mapped only to P07/P09.
- **Derive `frequency` from the evidence set, not from the loudest thread.** Count distinct verified URLs (`D`) and
  the subset with high engagement (`H` = ≥20 likes/points, ≥10 reactions, ≥25 comments), then subtract one when the
  sources are mostly vendor marketing or off-point for the node's claim. That discount is what separates P05/P07/
  P09/P13 (adjacent or vendor-heavy) from P03/P08 (independently reported).
- **Ties need a written rule before the ranks are built**, otherwise the two tables disagree with each other. The
  rule here: primary score desc, then the *other* score desc, then node id.

### Recommendation-pass patterns (verified 2026-11-17, US-005)

- **A recommendation is a cross-file edit too, so give it the same machine check.** `raw/validate_recommendation.py`
  asserts exactly three features, each with the six required sections, a pain node cited, and both a unit and a
  Playwright test named; that every path in a "Files likely touched" table **really exists in the target repo** (or
  is marked `**new**` and sits inside its source tree); that every PR number cited is in the live open-PR list and
  the one closed PR is described as closed; and that the three features map onto the three highest `pick_score`
  values under the tie-break `ranking.md` documents. It caught four real defects on its first run.
- **Parse only the FIRST table column when checking file paths.** Later columns describe the change and legitimately
  mention files that live in the *exported archive*, not the repo (`report.md`, `AGENT.md`). Matching the whole row
  produced two false failures; matching `row.split("|")[1].strip()` fixed it.
- **A stable sort is not the documented tie-break.** `sorted(nodes, key=lambda n: -n["pick_score"])` puts P01 before
  P08 (both 34) because P01 comes first in the array, while `ranking.md` documents "primary score desc, then the
  *other* score desc, then node id" — which puts P08 first (pain 18 vs 16). Any checker that re-derives a rank must
  implement the *documented* rule, not a naive sort, or it will fight the artefact it is checking.
- **Check the extension's real code before writing a feature spec.** Reading `entrypoints/share/App.tsx` and
  `useShareReport.ts` surfaced a constraint no evidence file mentioned: the only existing copy action
  (`copyIssue`) is rendered **inside** the `state.publication` branch and copies `finalBody`, which is empty unless
  the report was published. So "Copy for AI agent" must live outside that branch — copying to the local clipboard is
  a local operation, publishing is an upload. The spec also has to handle `report.md` containing its own ``` fences
  (`lib/export/markdown.ts`), so a bundle that embeds it needs a fence one backtick longer than the longest run
  inside.
- **`verified_sources` is NOT the node's evidence-bullet count.** It is the number of verified, non-dropped
  `sources.md` rows mapped to that node, so it can be **higher** than the bullet count when a node also cites a
  source in its "How users want it fixed" or "Workarounds" section (P08 = 12 mapped but 11 evidence bullets; its
  twelfth is `anthropics/claude-code#18170`, cited under Workarounds). It is never lower than the bullet count
  except where a bullet was dropped. `raw/validate_ranking.py` already enforces this rule against `sources.md` —
  recompute it the same way, and exclude the one **dropped** row (`anthropics/claude-code#31040`, mapped to P13) or
  the comparison will show a phantom drift of +1.
- **Re-confirm the open-PR list live, from the search bucket, and read the two nearest PR bodies in full.** The core
  bucket was exhausted again in US-005, but `search/issues?q=repo:…+is:pr+is:open` still worked and confirmed 22
  open PRs. `web_fetch` on PR #23 and PR #43 gave their bodies, which turned "adjacent" into "precisely adjacent":
  #23 owns "an agent-neutral prompt" **as documentation**, and #43 owns "one-click copy" **of a single request as
  cURL**. That distinction is what makes the recommendation non-duplicative, and it could not have been written from
  titles alone.

---

## 2026-11-17 - US-001
- **What was implemented**: the search plan for the pain research run. Read `00-context-notes.md`,
  `session-recorder-chrome-extension/{README,PRODUCT}.md`, `docs/report-format.md` and `docs/PLAN.md`, inventoried the
  extension's existing capabilities and its 21 open PRs, probed every research channel for real, and wrote `plan.md`
  with 63 concrete queries across 10 source types, 10 hypotheses (H6 is the required vision-and-video one), a
  popular-places coverage matrix, a planned 18-node list and an explicit risk section.
- **Files changed**: `research/runs/2-minimax-m3.1-flash/plan.md` (new),
  `research/runs/2-minimax-m3.1-flash/raw/probe_{github_reactions,github_repos,hn_algolia,cursor_forum_thread,cursor_forum_search}.json`
  (new tool-capability probes), `research/runs/2-minimax-m3.1-flash/.ralph-tui/progress.md` (this log).
  Nothing outside this output dir was written; the extension repo is untouched (`git status` clean).
- **Learnings:**
  - Patterns discovered: the Cursor forum's Discourse JSON API is the highest-yield source for agent browser pain
    (full thread text, usernames, dates, read counts) where the repo has issues disabled. GitHub issue HTML through
    `web_fetch` returns the full body *plus* reaction counts, which substitutes for the exhausted core API. GitHub's
    search bucket (10/min) is independent of the core bucket (60/hr), so discovery survives core exhaustion.
  - Gotchas encountered: Reddit's JSON API returns 403 for every endpoint and UA tried, and `web_fetch` on Reddit and
    on Chrome Web Store returns only a JS shell. `repo:` searches for `getcursor/cursor`, `All-Hands-AI/OpenHands` and
    `sst/opencode` fail with `422 Validation Failed` because issues are disabled there. Searching for `getcursor/cursor`
    by name is the only way in, so those three repos need forum/Discussions/HN/Reddit routes. The GitHub core quota was
    already exhausted (`core.remaining 0`) before this iteration finished, so `/repos/...` calls cannot be relied on.
  - Scope note: the leading candidate remains "copy an agent-ready bundle (trimmed report + prompt) to the clipboard",
    which the notes already favour, and the open PR list (#21-#49) makes anything redaction- or grouping-shaped
    novelty 0.

---


## 2026-11-17 - US-002
- **What was implemented**: collected the evidence and turned it into 15 pain nodes. Ran the plan's queries for real
  with every tool: the GitHub Search API in four paced batches (36 queries, `sort=reactions` and `sort=comments`,
  title-scoped to cut noise), the Cursor forum's Discourse JSON API (8 threads plus 5 keyword searches), the
  Hacker News Algolia API (6 searches plus 4 full item threads), `web_search` for discovery, and `web_fetch` to open
  and quote 13 pages. Wrote `nodes/P01..P15` (every node has 4-11 evidence links, all quotes verbatim and <=30
  words) and `sources.md` (57 URLs: 55 verified, 2 unverified, 0 dropped; 17 popular places named).
  Nodes not in `00-context-notes.md` §5: P06, P08, P09, P10, P11, P12, P13, P14, P15 — nine of the fifteen.
- **Files changed**: `research/runs/2-minimax-m3.1-flash/nodes/P01..P15-*.md` (15 new),
  `research/runs/2-minimax-m3.1-flash/sources.md` (new),
  `research/runs/2-minimax-m3.1-flash/raw/gh_batch_{a,b,c,d}.sh`, `raw/gh_fetch.py`, `raw/gh_fetch_note.md`,
  `raw/reddit_blocked.md`, `raw/gh_*.json`, `raw/cursor_*.json`, `raw/hn_*.json` (new evidence),
  `research/runs/2-minimax-m3.1-flash/.ralph-tui/progress.md` (this log).
  Nothing outside the output dir was written; `git status` in the extension repo is clean.
- **Learnings:**
  - Patterns discovered: the **GitHub Search API with `in:title` and only two or three terms** is the only way to get
    useful signal — a bare `repo:X browser console` returns 852 hits dominated by unrelated high-reaction issues
    (phone verification, usage limits), while `repo:X browser in:title` returns 1 010 hits that are actually about
    browsers. The reaction count is on `items[].reactions.total_count` and the `+1` count on `items[].reactions['+1']`.
    The **Cursor forum's Discourse JSON API** (`/t/<id>.json`) returns the full thread, the per-post `score` (likes),
    `views`, `created_at` and the canonical `slug` — guessing slugs from titles is wrong (`167105` is
    `...the-browsers-viewport-dimensions`, not `...the-browser-viewport-dimensions`), so always read the slug from the
    JSON. The **HN Algolia `/items/<id>` endpoint** returns the whole comment tree including points and comment counts,
    while `/search?tags=comment` returns `comment_text` but no points — use both.
  - Gotchas encountered: **GitHub issue HTML is React-rendered** — `curl` plus a regex finds only the
    "Description / opened on" shell, so `web_fetch` is the only way to read an issue body; a regex extractor that
    worked in US-001 does not work here. **Reddit is hard-blocked** (403 HTML shell on every JSON endpoint, including
    with a browser UA and `Accept: application/json`; `old.reddit.com` 302s), so no Reddit post could be cited;
    `web_search` with `site:reddit.com` returns index pages whose body text is unreadable. The **Chrome Web Store,
    Product Hunt and G2 listing pages return HTTP 200 but only the JS shell**, so no review text was readable and no
    review is cited. `All-Hands-AI/OpenHands`, `sst/opencode` and `getcursor/cursor` still reject `repo:` searches
    with 422, but `All-Hands-AI/OpenHands` issues are reachable by direct URL (they redirect to `OpenHands/OpenHands`),
    and `sst/opencode` issue #1589 is actually the PR `anomalyco/opencode#1589`.
  - Scope note: the leading candidate is unchanged and is now the top-scoring node in this run — **P14 "the recorder
    has no channel to the agent"** (pick 35), closely followed by P01 (34), P08 (34) and P10 (32). The extension
    already captures everything an agent lacks, so the winning feature is a *delivery* feature (agent-ready bundle to
    the clipboard, prompt included), not new capture. Redaction (P05), grouping (P12) and environment metadata
    (P11) score low on novelty because open PRs #31/#37/#38/#42/#44, #49 and #29/#41 already occupy those topics.

---

## 2026-11-17 - US-003
- **What was implemented**: verified every cited URL by re-opening it, then cleaned the node set. All 61 cited URLs
  were opened — 60 verified, 0 unverified, 1 dropped — and the header line now reads
  `verified: 60, unverified: 0, dropped: 1`. Every node's `status` field is now *derived* from its evidence rather
  than asserted: `verified` where two or more independent verified sources back the main claim (12 nodes),
  `partly-verified` where the main claim leans on vendor material (P07, P09). Every node has 3-11 evidence links and
  **102 quoted fragments were machine-checked verbatim** against the re-fetched raw responses.
  Merged the one duplicate pair: P03 ("hand a bug straight to an agent") and P14 ("no channel to the agent") were
  the same pain from the market side and the product side, and shared an evidence URL. They are now a single node
  **P03** with 11 verified evidence links; the old P15 became **P14** (agent cannot reach the app), so the tree is
  contiguous P01-P14 with 14 nodes.
- **Files changed**: `research/runs/2-minimax-m3.1-flash/sources.md` (rewritten, 61 rows + a corrections table),
  `research/runs/2-minimax-m3.1-flash/nodes/P01..P14-*.md` (14 rewritten; `P14-no-channel-to-the-agent.md` and
  `P15-agent-cannot-reach-the-app.md` deleted),
  `research/runs/2-minimax-m3.1-flash/raw/verify/` (61 re-fetched payloads: GitHub issue bodies, comment threads,
  forum JSON, HN items, READMEs),
  `research/runs/2-minimax-m3.1-flash/raw/{verify_cursor,verify_hn,verify_gh,verify_gh_comments,verify_gh_hunt,
  verify_check_quotes,verify_check_gh_quotes,verify_final_quotes,validate_sources}.py` (the verification harness),
  `research/runs/2-minimax-m3.1-flash/.ralph-tui/progress.md` (this log). Nothing outside the output dir was written;
  the extension repo's `git status` is clean.
- **Learnings:**
  - Patterns discovered: **the GitHub core REST API is far better than `web_fetch` for verification** — one
    `GET /repos/{owner}/{repo}/issues/{n}` returns the body, `state`, `created_at`, `comments` count and the full
    `reactions` breakdown (`+1`, `heart`, `eyes`, `hooray`) in one call, and the `html_url` field settles
    issue-vs-PR and redirect questions (`sst/opencode#1589` → `anomalyco/opencode/pull/1589`). Quote *bodies* live in
    `issue.body`; quotes attributed to a commenter live in `issue.comments[].body`, so comment threads must be
    fetched separately. Discourse's `/t/<id>.json` returns the thread **title**, the per-post `score` (likes) and
    `views`, but the score is fractional (35.6, 171.4), so round it and say so. HN's `/items/<id>` returns
    `points` and the whole comment tree, but a **text post has an empty story body and no `points`** — the real
    content sits in the author's own first comment, and `story_id` differs from `objectID`. Two checker bugs cost
    time and are worth remembering: a normaliser that strips `**` and list markers will still fail on
    `404.` at the end of a quote, and a regex that strips inline `N. ` markers will eat a trailing " 404. ".
  - Gotchas encountered: **the US-002 pass had a wrong-repo citation** — the "compaction checkpoints re-embed
    screenshots" issue is `openai/codex#31040`, not `anthropics/claude-code#31040` (that one is about plugin-cache
    cleanup). A *dropped* row, not a silently rewritten one. Three URLs cited in nodes were missing from
    `sources.md` entirely (`Ami3466/ai-live-log-bridge`, `bradautomates/claude-video`, `norrietaylor/tt2#118`).
    Several reaction/comment counts did not match the API (24 vs 7 on #57034, 5 vs 3 on #75632, 17 vs 3 on
    #26831, 1 vs 3 on #9152). Two "quotes" were **paraphrases presented as quotes** (the Klavity blog and the
    CobaltCapture page) and one claim had no source at all (`cc-safe-setup`). Issue #42300's title has no
    "[Bug]" prefix. And a **live HN page can render while Algolia's `/items/` returns 404** — do not drop such a
    citation on the Algolia 404 alone, fetch the `news.ycombinator.com` page and check it.
  - Scope note: the ranking that matters is unchanged by this pass. **P03 (hand the bug straight to an agent / no
    channel to the agent)** is the strongest node: the extension already captures everything the agent lacks, so the
    winning pull request is a *delivery* feature — an agent-ready bundle (trimmed `report.md` + the prompt from
    `docs/report-format.md`) on the clipboard — and not new capture. P01, P08 and P10 follow. Redaction (P05),
    grouping (P12) and environment metadata (P11) stay low on novelty because open PRs #31/#37/#38/#42/#44, #49
    and #29/#41 already occupy those topics. The vision/video area was searched hard and the gap is real
    (`bradautomates/claude-video` has 21 021 stars), but it is a large feature and a crowded market, so it is not
    the pick.

---

## 2026-11-17 - US-004
- **What was implemented**: scored all 14 nodes with the PRD rubric and wrote `ranking.md` (two ranked tables, the
  reasoning for the top five, the vision/video answer, the nodes deliberately not picked, and the limits of the
  evidence) and `ranking.json` (exact PRD schema, 14 node objects with `pain_rank`, `pick_rank` and `top_pick`).
  The rubric was operationalised before scoring: `frequency` is computed from the node's own evidence set — `D`
  distinct verified URLs plus `H` high-engagement ones (>=20 likes/points, >=10 reactions, >=25 comments) — with a
  -1 discount where the sources are mostly vendor marketing or off-point for the claim (P05, P07, P09, P13), a floor
  of 4 when one source carries >=500 likes/points, and a written tie-break rule (primary score, then the other score,
  then node id) so the two tables cannot disagree.
  Three frequencies changed against the US-002/US-003 estimates as a result of that rule and were propagated back into
  the node files so every artefact agrees: **P03 4->5** (11 distinct verified sources, 8 of them high-engagement —
  the second-largest evidence set in the run), **P04 4->3** (four sources, only one with real engagement) and
  **P14 3->4** (five on-point sources, three high-engagement).
  Final order: **P03 (pick 37, pain 18) is the top pick on both tables**, then P08 (34/18), P01 (34/16), P10 (32/18),
  P02 (32/14); the tail is P06 (31), P04 (31), P07 (29), P11 (28), P05 (27), P12 (26), P13 (26), P14 (25), P09 (23).
- **Files changed**: `research/runs/2-minimax-m3.1-flash/ranking.md` (new),
  `research/runs/2-minimax-m3.1-flash/ranking.json` (new),
  `research/runs/2-minimax-m3.1-flash/nodes/P03-hand-bug-straight-to-an-agent.md`,
  `research/runs/2-minimax-m3.1-flash/nodes/P04-filed-issue-arrives-text-only.md`,
  `research/runs/2-minimax-m3.1-flash/nodes/P14-agent-cannot-reach-the-app.md` (`## Scores` lines only),
  `research/runs/2-minimax-m3.1-flash/sources.md` (one row's `Node(s)` cell: HN 21049087 now also maps to P03),
  `research/runs/2-minimax-m3.1-flash/raw/validate_ranking.py` (new checker),
  `research/runs/2-minimax-m3.1-flash/.ralph-tui/progress.md` (this log). Nothing outside the output dir was
  written; the extension repo's `git status` is clean and no git command was run that changes anything.
- **Learnings:**
  - Patterns discovered: **scoring is a cross-file edit, so it needs a machine checker.** `raw/validate_ranking.py`
    now verifies the JSON schema key-for-key, recomputes both scores from the five axes, checks that each rank array
    is sorted *and* tie-broken as the document claims, parses the `## Scores` line out of every node file and
    asserts it matches `ranking.json`, asserts both `ranking.md` tables list every node exactly once, and asserts
    every evidence URL in a node is mapped to that node in `sources.md`. It found four real drifts on the first run
    (three stale node score lines and one unmapped URL) that reading the files would have missed.
  - Gotchas encountered: **the GitHub API was rate-limited again** (`core` quota exhausted, HTTP 403 on the
    extension's PR list) and **`gh` is not installed in this environment**, so the open-PR overlap list came from the
    context notes plus one `web_fetch` on PR `#23` — "docs: add self-contained UJG bundle", which mentions an
    "agent-neutral prompt" and a visual-review gallery and is therefore *adjacent* to the P03 feature rather than a
    duplicate of it. The implementer of P03 must read #23 before starting. A first pass at the tie-break rule
    ("pain_score, then node id") also made the two rank arrays disagree with the tables in `ranking.md`; the rule
    had to be "primary score, then the *other* score, then id".
  - Scope note: the ranking lands where the earlier passes pointed, but now with a number attached. **P03 is the
    pick** — one click copies an agent-ready bundle (trimmed `report.md` plus the prompt that today lives only in
    `docs/report-format.md` line 78) to the clipboard. It wins on every axis that matters: the most evidence
    (11 verified URLs, 8 high-engagement), `fit` 5 because the extension already captures everything the agent
    lacks, `smallness` 4 because `lib/export/bundle.ts` and `copyIssue()` already do most of the work, and
    `novelty` 5 because no open PR touches it. The vision/video area gets a plain answer: the gap is real (P08 has
    12 verified sources and tops the pain table's second slot) but a video feature is `smallness` 1 in a market
    already taken by `claude-video` (21 021 stars), `vidin` and Loom, so it is not the pick.
---

## 2026-11-17 - US-005
- **What was implemented**: turned the ranking into three buildable feature specs and wrote the run summary.
  Read the extension's real source tree (`entrypoints/share/{App,reducer,useShareReport}.ts`,
  `entrypoints/sidepanel/components/ExportPanel.tsx`, `lib/export/{bundle,markdown,tokens,zip}.ts`,
  `lib/sharing/github.ts`, `docs/report-format.md`) so every path in the spec is real, then re-confirmed the
  extension's open-PR list live against GitHub (22 open PRs via the **search** bucket — the core bucket was
  exhausted again) and read the bodies of PR **#23** and PR **#43** with `web_fetch` to characterise the overlap
  precisely instead of by title. Wrote `recommendation.md` (three features in pick_score order — P03 "Copy for AI
  agent" pick 37, P08 "Screenshots a text-only agent can use" 34, P01 "Copy the failing call" 34 — each with the
  cited pain nodes, UX and click count, a table of real files with line counts, a unit + Playwright test plan, a
  risk table, and the open PRs it must not duplicate) and `run-summary.md` (method, counts, which tools worked, ten
  named weaknesses of the evidence, reproduction notes).
  The recommendation is explicit: **ship feature 1 as the one pull request** — the extension already captures
  everything the agent lacks, so the winning PR is *delivery*, not capture, and it needs no new permission,
  dependency or manifest entry.
- **Files changed**: `research/runs/2-minimax-m3.1-flash/recommendation.md` (new),
  `research/runs/2-minimax-m3.1-flash/run-summary.md` (new),
  `research/runs/2-minimax-m3.1-flash/raw/validate_recommendation.py` (new checker),
  `research/runs/2-minimax-m3.1-flash/raw/us005_open_prs.json` (new — the 22 open PRs, trimmed),
  `research/runs/2-minimax-m3.1-flash/raw/us005_pr_overlap_notes.md` (new — verbatim bodies of PR #23 and #43),
  `research/runs/2-minimax-m3.1-flash/.ralph-tui/progress.md` (this log, plus a new "Recommendation-pass patterns"
  section at the top). Nothing outside this output dir was written; the extension repo's `git status` is clean and
  no git command that changes anything was run.
- **Learnings:**
  - Patterns discovered: **a spec that names files is a cross-file edit and needs the same machine check as the
    rest of the run.** `raw/validate_recommendation.py` checks the three features, the six required sections per
    feature, a pain node and both test kinds per feature, that every path in a "Files likely touched" table exists
    in the target repo (or is marked `**new**`), that every PR number cited is in the live open-PR list (and that
    the one closed PR is described as closed), that the three features map onto the three highest `pick_score`
    values under the documented tie-break, and that `run-summary.md` carries the required counts. It caught four
    real defects on its first run: two false path failures from matching the whole table row instead of the first
    column, a stable sort that contradicted the documented tie-break (P01 before P08 instead of after), and a
    "**new**" marker in the second column that the new-file check was not reading.
  - Gotchas encountered: **the GitHub core bucket was exhausted again** (`/repos/…/pulls/{n}` → 403), so the PR
    bodies had to come from `web_fetch` on the PR pages, which does return them; and **the existing copy action in
    the extension is unreachable without publishing** — `entrypoints/share/App.tsx` renders *Copy issue Markdown*
    only inside the `state.publication` branch and copies `finalBody`, which is empty unless the report was
    published, so the new clipboard action must live outside that branch (copying is local; publishing is an
    upload). Also: `report.md` contains its own ``` fences (`lib/export/markdown.ts:348-361`, `:497-503`, `:544-546`,
    `:619-630`), so a bundle that embeds it must use a fence one backtick longer than the longest run inside — the
    single most likely thing to get wrong in the implementation, and exactly what a unit test must pin.
  - Scope note: the ranking's pick is unchanged by this pass — **P03, "one click copies an agent-ready bundle to the
    clipboard"** — but the recommendation is sharper than the ranking was. Reading the source showed the gap is
    even more clear-cut than the evidence suggested (`copyIssue` copies the *issue* body and only after publishing;
    the prompt that makes `report.md` usable lives only in `docs/report-format.md:78`). PR **#23** turned out to be
    adjacent rather than duplicative: it ships "an agent-neutral prompt" as a **docs** bundle for journey-graph
    regeneration, not as a runtime clipboard action, so the recommendation states the rule explicitly — the prompt
    ships as product code in `lib/export/agent-bundle.ts` and the doc only links to it. The vision/video answer is
    unchanged and plain: the **image** gap is real (P08, 12 verified sources) and worth a second PR; the **video**
    gap is real but `smallness` 1 in a market already taken by `claude-video` (21 021 stars), `vidin` and Loom, so it
    is not the pick.
  - Correction made in this pass: the US-005 draft of `recommendation.md` quoted **P08 = 11** and **P01 = 4**
    "verified sources" — the nodes' *evidence-bullet* counts — while `ranking.json` and `ranking.md` use the
    `verified_sources` metric (verified, non-dropped `sources.md` rows mapped to the node). The prose now quotes the
    metric and says which one it is, and `raw/validate_recommendation.py` checks every "N verified sources" claim in
    `recommendation.md` against `ranking.json` at sentence level, so the two cannot drift again. The source of the
    confusion: a node may cite a verified source in a non-Evidence section, so bullets and mapped sources differ.
---

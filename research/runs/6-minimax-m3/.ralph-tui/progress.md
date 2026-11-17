# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

*Add reusable patterns discovered during development here.*

- **Grep for the CONSTANT, not for the literal number in the issue title.** This is the correction that
  matters most from this run. US-004 confirmed P05's "make the screenshots safe for agents" gap with
  `grep -rn '2000' lib/ entrypoints/` (the limit quoted in claude-code #13480) and got no hits, so it
  scored novelty 3 and made P05 the `top_pick`. The extension does not use the number 2000 anywhere —
  it uses `const MAX_SHOT_DIM = 1400;` at `lib/capture/screenshots.ts:38`, and
  `ScreenshotScheduler.capture()` (lines 160-190) already downscales any screenshot whose longest side
  exceeds it via `OffscreenCanvas` and re-encodes as JPEG. **The feature was already shipped.** A grep
  that searches for the number in the *external* issue title instead of for the *internal* constant will
  silently confirm whatever you hoped. Fix: when scoring "does X already exist?", enumerate the
  **behaviour** ("where is a longest-side cap applied to an image?"), not the literal from the ticket,
  and read the whole function — the constant was 20 lines from where the grep was looking.
- **A "grep found nothing" claim must survive a second, differently-shaped grep.** The US-004 pattern
  above (`grep` for `estimateTokens`, `verdict|confidence|not-a-bug`, `2000 px`) produced three score
  moves; two held and one was a false negative, which is worse than not having grepped. Two of the three
  survived re-reading (`lib/export/tokens.ts` really does export `estimateTokens`; the codebase really
  has no verdict concept). The third did not. Rule: a negative grep result that *raises* a node's score
  deserves a second pass with a different token shape before it is written down.
- **The recommendation must re-read the source even when the ranking is "done".** US-005 found a
  false-negative score by grepping `MAX_SHOT_DIM|MAX_DIM|maxDim` instead of `2000` — one extra token
  pattern, and it inverted the `top_pick`. Reading the extension's source to write accurate file paths
  for the feature specs (which the PRD requires anyway) is therefore not just paperwork: it is a second
  verification pass with a different question, and it caught the error that four earlier stories had
  carried. Write the file paths first, then re-read each function you name.
- **Generate the scored artifacts from one script and round-trip them.** The `raw/regen_ranking.py` +
  `raw/validate_ranking.py` pair from US-004 was reused in US-005 to re-score P05 and regenerate both
  `ranking.md` and `ranking.json`. The validator caught a real parsing bug immediately: the markdown
  tables bold the scores (`**18**`), so `int(cells[8])` raised `ValueError` until the cells were
  `.replace("**", "")`-ed first. A validator that crashes is a validator that has not run.
- **Never hand-compute a scored rubric — generate the tables from the same source of truth.** In US-004 the
  hand-written `ranking.md` pick_score column disagreed with the rubric (`2f+2s+2fit+sm+nov`) on every one of the
  16 nodes: I had been adding the five components rather than weighting frequency/severity/fit at 2. The fix was to
  compute every score in a script, emit `ranking.json` from it, and then **validate the markdown table back against
  the JSON** (component scores, derived scores, rank column, row order, and table sort direction). That validator
  caught a second, subtler bug: a hand-ordered tie (P03 vs P17, both pain 16 / pick 30) that the JSON sorted by id
  and the markdown did not. Rule: the rubric's arithmetic belongs in code, and a scored artifact needs a
  round-trip check between its two renderings.
- **Anchor novelty and smallness scores in the extension's source, not in the notes.** Two US-004 score moves came
  straight from grepping `lib/` and `entrypoints/`: `lib/export/tokens.ts` already exports `estimateTokens()` and
  `lib/export/bundle.ts:497` already computes `tokens: estimateTokens(report)`, which dropped P17's smallness 4→3
  and novelty 2→1; and a repo-wide grep for a 2000 px image check returned nothing, which is what keeps P05's
  "make the screenshots safe for agents" gap real rather than imagined. A node that claims "the extension cannot do
  X" must show the grep that proves it.

- **Probe every PRD endpoint before planning.** The PRD's suggested toolkit and reality diverge. Verified in this run:
  Reddit's `.json`/`.rss` endpoints return **HTTP 403** from this host with any user agent (`old.reddit.com` serves an
  interstitial), and G2/Product Hunt return **403/504** via both `web_fetch` and `curl`. Working substitutes:
  `web_search` with `allowed_domains: ["reddit.com"]` for Reddit, and the Chrome Web Store listing's **"Related
  extensions" carousel** for G2-style competitor review mining.
- **Discourse forums expose a JSON API that beats web fetch.** `forum.cursor.com/search.json?q=…` returns topic id,
  `posts_count`, `reply_count`, `like_count`, dates and full post text in one call; `forum.cursor.com/t/{id}.json` returns
  the full thread. `web_fetch` on the same forum renders almost nothing (title only). Always prefer the JSON API.
- **GitHub search API is the best popularity source available.** `api.github.com/search/issues?...&sort=reactions` returns
  `reactions["+1"]`, `reactions.total_count`, `comments`, `state` and `html_url` without a token. Unauthenticated limit is
  10 req/min. Filter by title keywords — `sort=reactions` in a large repo returns quota/account issues with 1000+ reactions.
- **HN Algolia `tags=comment` hits carry no `points`.** The popularity of a comment lives on its parent story. Run the
  `tags=story` query and join on `story_id`.
- **A Chrome Web Store listing page is a competitor index.** The "Related extensions" carousel on one listing named ~12
  direct competitors (Handoff, Vox Issue, POKEIT, Vibe Annotations, ElementAgent, Yocoolab, Pluck, Staktab, Contexify,
  Darnly, Jam, Marker.io, FlowLens, Faylee). Use it to ground the `novelty` score, not just the extension's own repo.
- **Reading the extension source settles "does it already exist?" questions.** `grep` for the feature in
  `entrypoints/` + `lib/` is faster and more reliable than the README. Verified here: the agent-handoff "Suggested prompt"
  exists only in `docs/report-format.md`; the only clipboard write is `copyIssue()` in
  `entrypoints/share/useShareReport.ts:330`; video files ship at L0/L1 but are dropped at L2/L3
  (`lib/export/trimmer.ts:519-528`, `lib/export/bundle.ts:448-451`).
- **`web_fetch` on a GitHub issue page beats the GitHub issue API for quoting.** It renders the issue body *and every
  comment* as plain text with the reaction counts ("👍 57 Reacted by … and 36 more"), and it does **not** consume the
  10/min **search**-API budget. The separate **core** API limit (60/h unauthenticated) is the one that bites.
- **`hn.algolia.com/api/v1/items/{id}` returns the whole comment tree.** For a launch thread that is 100+ practitioner
  comments — the highest-signal evidence in the whole run for QA/bug-report pain. Use it for any
  `Show HN` / `Launch HN` the `tags=story` search surfaces.
- **Reddit is fully blocked here, not just its JSON API.** `web_fetch` on a reddit.com post URL returns the
  "Prove your humanity" bot challenge with HTTP 200 and zero content, so a page can look "fetched" while yielding
  nothing. Always check that a Reddit fetch actually contains post text before quoting it; declare the block instead.
- **A GitHub org discussion has no content in its static HTML, but `web_fetch` renders it.** `curl` on
  `github.com/orgs/community/discussions/<id>` returns a JS shell (~240 KB of feature flags, no body text). The
  `.json` sibling (`…/discussions/<id>.json`) returns only the title. `web_fetch` on the plain URL returns the full
  body and every comment as plain text. Use `.json` to confirm a discussion exists and `web_fetch` to quote it.
- **Verify reaction counts by re-reading the page, not the search API.** The GitHub *search* API returns a
  `reactions` object whose `total_count` counts every reaction type; the page footer shows only 👍/❤️ and
  "and N more", and the two disagree (claude-code #12676: API said 57, page showed 👍 46 + ❤️ 11). Same for HN
  comment counts — Algolia's `children` is top-level only (44) while "135 comments" on the site counts nested
  replies. Cite the number a reader can actually see on the page.
- **A node's "Session Recorder angle" must be checked against the source, not remembered.** `grep` for the claimed
  function/line in `entrypoints/` + `lib/` before repeating it. Verified here: `copyIssue` really does exist only in
  `entrypoints/share/useShareReport.ts:330`; the video file really is dropped at L2+ in both
  `lib/export/trimmer.ts:519-528` and `lib/export/bundle.ts:448-451`; the "Suggested prompt" really does exist only
  in `docs/report-format.md:78`; and there is **no** 2000 px dimension check anywhere in the extension (which is
  what makes P05's "make the screenshots safe for agents" gap real rather than imagined).
- **Re-reading a source can discover a competitor and change the conclusion.** Opening the claude-code #12676
  thread properly surfaced two competitors that the US-002 pass had only heard of second-hand: Clipy
  (`github.com/clipy-recorder/clipy-mcp`, ships `get_agent_context` returning summary + timeline + key moments +
  transcript + browser diagnostics as markdown) and ThinkRun (a Chrome extension, "packages what happened — video,
  transcript, actions, console, and network — into context an agent can parse in one pass"). Both ship the "visual
  brief" that US-002 had scored `novelty: 4`; the score dropped to 2. Always follow a named competitor to its own
  listing before scoring novelty.

---

## 2026-11-17 - US-001

- **What was implemented:** Wrote `plan.md` — the US-001 search plan. 53 concrete query lines across 8 source-type
  groups (A GitHub-reactions, B GitHub-repo-discovery, C Cursor-forum-Discourse, D Reddit-via-web-search,
  E HN-Algolia-points, F Chrome-Web-Store-reviews, G vendor-docs, H broad-web-search), 9 testable hypotheses
  (H1-H5 re-test the notes' five pains, H6 reproduction-not-capture, H7 agent-side triage and duplicates,
  H8 the required vision/video area, H9 pains the notes missed), a 17-row provisional node table, and method rules
  plus a risks section. Also probed every source endpoint to record which actually work.
- **Files changed:** `plan.md` (new), `raw/probe_*.json` (5 probe responses kept as evidence), `.ralph-tui/progress.md`.
  Nothing written outside `OUTPUT_DIR`.
- **Learnings:**
  - Patterns discovered: the endpoint-probing method and the source-preference order above; a source-type map
    (S1-S12) with per-tool status so later stories do not waste calls on blocked endpoints.
  - Gotchas encountered: Reddit JSON 403 and G2/Product Hunt 403/504 (documented, with substitutes, rather than
    silently dropped); HN comment hits have no `points`; `sort=reactions` on big repos is dominated by quota issues.
  - Key finding to carry into US-002: the category is **saturated** — a dozen Chrome extensions already ship
    "copy visual feedback for your AI agent", including a copy-to-clipboard button. A naive "copy the report to the
    clipboard" feature (the notes' current leaning, option A) is therefore **not novel**, and the `novelty` score must
    be judged against those competitors, not only against our own repo. The extension's gap is that it has *no
    agent-readable text rendering of its visual/video evidence* (video bytes dropped at L2+, screenshots are only
    `.jpg` pointers), but that needs demand evidence from US-002 before it becomes a proposal.


---

## 2026-11-17 - US-002

- **What was implemented:** Ran the evidence collection for US-002 and wrote 17 node files plus `sources.md`.
  Covered 13 of the PRD's "popular places" (anthropics/claude-code, forum.cursor.com, github/copilot-cli,
  openai/codex, cline/cline, RooCodeInc/Roo-Code, ChromeDevTools/chrome-devtools-mcp, microsoft/playwright-mcp,
  Hacker News, Chrome Web Store competitor reviews, Microsoft/vscode-pull-request-github, GitHub community
  discussions + Agentic Workflows, GitHub repo discovery). 47 source URLs recorded, 38 verified, 1 unverified,
  8 dropped. Every node has at least 4 evidence links with the popularity signal recorded
  (GitHub `+1`/comments, HN points/comments, Cursor forum posts/views/likes, Chrome Web Store ratings/users).
  The vision and video area is covered by three nodes (P04 video-to-frames-and-text, P05 agents cannot consume
  screenshots, P07 PR review cannot see the UI).
- **Files changed:** `nodes/P01..P17-*.md` (17 new), `sources.md` (new), `raw/*.json` (~45 raw API responses),
  `.ralph-tui/progress.md`. Nothing written outside `OUTPUT_DIR`.
- **Learnings:**
  - Patterns discovered:
    - `forum.cursor.com/t/{id}.json` and `forum.cursor.com/search.json` are the **best single source** in this
      whole research area: full post bodies, `posts_count`, `reply_count`, `like_count`, `views`, and dates,
      with no rate limit that bit us. Ten Cursor forum topics carried the most verbatim, high-signal quotes.
    - `web_fetch` on a GitHub issue page renders the **entire** issue body plus every comment in plain text,
      including the reaction counts — which makes it strictly better than the issue API for quoting, and it
      does not count against the 10/min search rate limit (the *issue* API is what rate-limits).
    - `hn.algolia.com/api/v1/items/{id}` returns the full post plus the whole comment tree; for a launch thread
      that is 100+ comments of practitioner opinion, which is where the best evidence lives.
    - **Search-result snippets are enough to find a source but never enough to quote.** Every quote in the nodes
      comes from a page this run actually opened.
  - Gotchas encountered:
    - Reddit is **fully blocked** from this host: `.json` returns 403 with every UA, `old.reddit.com` 302s to a
      consent interstitial, and `web_fetch` on a post URL returns the "Prove your humanity" bot challenge
      (HTTP 200, no content). `web_search` with `allowed_domains:["reddit.com"]` returns almost nothing useful.
      No Reddit claim is used anywhere; this is declared in `sources.md`.
    - The GitHub **search** API rate limit (10/min unauthenticated) and the **core** API limit (60/h) are separate.
      The core limit was exhausted early, which is why issue bodies were fetched with `web_fetch` instead.
    - `api.github.com/search/issues?q=repo:getcursor/cursor...` and `repo:sst/opencode...` return
      `422 Validation Failed` — those repos cannot be searched in this environment. Use the forum instead.
    - `sort=reactions` in a large repo is dominated by quota/account issues. Filter by title keywords before
      writing a node; the reaction count alone is not a signal that the topic is relevant.
    - `web_fetch` on a Chrome Web Store review URL sometimes redirects to a Google consent interstitial, and most
      of these niche extensions have 0-11 ratings. The store is a poor *volume* source and a decent *quote* source.
  - Key findings to carry into US-004/US-005:
    - **The strongest new pain is video** (P04): no CLI agent accepts video, and the users who worked around it
      converged on a specific shape — *narration transcript with timestamps + click targets + 4-8 change-detected
      frames*, not raw 1 fps frame dumps. Session Recorder already records the tab video, the screenshots and the
      narrated transcript on one clock, and already drops the video bytes at L2+ — so it has the inputs and is
      missing only the rendering step.
    - **"Copy for agent" is not novel** (P15): a dozen Chrome extensions already ship it, named on the Darnly
      listing's own "Related extensions" carousel (Handoff, Vox Issue, POKEIT, Yocoolab, Pluck, Staktab, Contexify,
      Setu, AIScan, Vibe Annotations, ElementAgent). The notes' current leaning (option A) must be scored
      `novelty: 1` and the differentiator has to come from data the competitors do not have.
    - **A third new pain, "the report must be auditable" (P16)**, came out of the HN Momentic thread: experienced
      QA practitioners want a three-valued verdict (pass/fail/**I can't tell**), an explicit confidence, and a
      de-duplication key, because "one noisy finding per run" is enough to make a reviewer stop reading. Session
      Recorder's deterministic event stream can supply this without an LLM in the loop — a real differentiator.
    - The **login wall** (P08) is the one pain where the extension's data is strictly better than a live browser
      agent's: the recorded session comes from an already-authenticated browser, so the agent never needs a
      password. That makes the redaction PRs (#42, #44, #38, #37, #31) load-bearing rather than optional.

---

## 2026-11-17 - US-003

- **What was implemented:** Ran the verification and cleanup pass. Re-opened **all 51 distinct URLs** cited across
  `nodes/` and the old `sources.md` (curl + web_fetch + the Discourse/Algolia JSON APIs), then rewrote `sources.md`
  with real per-URL statuses and a "Verification pass" section recording what changed. **51 verified, 0 unverified,
  8 dropped.** Every one of the 16 nodes now has `status: verified`, at least two distinct verified evidence URLs,
  and no unverified marker on any evidence line.
- **Files changed:**
  - `sources.md` — rewritten: new count line, new "Verification pass" section, 2 new sources (S50 Clipy, S51
    ThinkRun), corrected reaction counts / dates / closure types, expanded "Not covered" block, expanded "Dropped
    claims" table.
  - `nodes/P01..P17-*.md` — 11 of 17 touched; `nodes/P09-context-noise-and-budget.md` **deleted** (merged into P17).
  - `plan.md` — appended a "Reconciliation with the final node set" section mapping provisional IDs to final IDs.
  - `raw/` — 29 new verification payloads (`cf_*`, `hn_*`, `v_*`, `gh_*`, `api_*`, `cws_*`) + `verify-us003.log`.
    120 raw files total.
  - `.ralph-tui/progress.md` — this entry plus 4 new reusable patterns in "Codebase Patterns".
  - **Nothing written outside `OUTPUT_DIR`** (verified with `find -newermt` over `research/`).
- **Learnings:**
  - Patterns discovered:
    - **Verifying changed the answer twice.** (a) The two carried-over "unverified" sources were both real and both
      strong — the Cursor topic 58803 (752 views) gives P02 a verbatim quote it did not have, and the GitHub
      discussion 169913 ("I am told that there is a screenshot. It is not there") is the single best piece of
      evidence for P07 *and* P06. Neither had been opened in US-002 because it came from the notes rather than from
      a live search. (b) Following the competitors named inside a source turned up Clipy and ThinkRun, which ship the
      "visual brief" that P04 had scored `novelty: 4`; that score is now **2**.
    - **A search-API reaction count is not a page reaction count.** `reactions.total_count` counts all reaction
      types; the page footer shows 👍/❤️ separately. They disagreed on #12676 (57 vs 👍46+❤️11). Same for HN: Algolia's
      `children` is top-level only (44 for the Momentic thread) while the site counts nested replies (135).
    - **Two node files had invalid API URLs** — `?q=bug+report+mcp agent&sort=stars` with a literal space, and a
      cursor slug with a stray leading `-`. Both were written in US-002 and would 400 if fetched. Fixed to the
      working, fully-qualified URLs.
    - **Merging P09 into P17 was the right call**, and the criterion was "same lead evidence *and* same proposed
      fix", not "similar words". P09 and P17 both led with #16592's "86 % of context" comment and both proposed a
      user-controlled copy block. P17 survived because it also carries the *money* half ($2.67 vs $0.80 vs $4.09 per
      bug) that P09 never had.
    - **An unsupported claim can hide in a node's prose, not just its evidence list.** P02's pain paragraph asserted
      that pasted output "carries tokens, cookies or API keys" — a real and serious claim that none of P02's four
      sources supported. It was cut from P02 (the secrets pain has its own node, P12, with proper evidence) rather
      than left dangling or quietly given a URL it did not earn.
  - Gotchas encountered:
    - `github.com/orgs/community/discussions/<id>` served by `curl` is a **JS shell**: 240 KB, no body text, so a
      naive text search finds nothing and the page looks broken. `web_fetch` renders it fully; the `.json` sibling
      returns only the title (useful as an existence check).
    - Two Chrome Web Store pages redirect to a Google consent interstitial via `web_fetch` (ThinkRun's listing) but
      serve fine via `curl`. `curl` first, `web_fetch` second.
    - `api.github.com/search/repositories` counts drift between the US-002 and US-003 passes (54 vs "20+" for the
      bug-report query, 6 vs 4 for the visual-feedback query) because new repos appear. Cite the count with its date.
  - **Key findings to carry into US-004/US-005:**
    - The final set is **16 nodes** (P09 merged away), and the vision/video area is covered by three: P04 (video),
      P05 (screenshots), P07 (PR review).
    - **The novelty landscape is harsher than US-002 thought.** Clipy and ThinkRun both ship the agent-readable
      "visual brief". ThinkRun (23 users, v0.2.12) also ships the time-synced click/console/network capture, the
      LLM-ready Markdown/JSON export, browser control over the user's real logged-in Chrome, an MCP server, and a
      local-mode privacy story — i.e. most of what Session Recorder does. **A "copy for agent" button, a
      "visual brief", and an "MCP server" are all now `novelty: 0-1`.** The survivable differentiators are the ones
      that need data the competitors do not collect or cannot produce deterministically: the credential-*type*
      signal (P12), the explicit pass/fail/uncertain verdict and "not a bug" state (P16), and the user-editable
      copy block with a token estimate (P17).
    - **P04 and P16 are the two nodes whose scores moved most** (P04 novelty 4→2; P16 gained a second and third
      independent source). P16 is now the best-supported candidate for the differentiator the notes were reaching
      for.
    - The extension-source claims in every node's "Session Recorder angle" were **re-verified against the code**
      and all hold: `copyIssue` at `entrypoints/share/useShareReport.ts:330`, video dropped at L2+ in
      `lib/export/trimmer.ts:519-528` and `lib/export/bundle.ts:448-451`, "Suggested prompt" only in
      `docs/report-format.md:78`, and no 2000 px image check anywhere (which keeps P05's gap real).


---

## 2026-11-17 - US-004

- **What was implemented:** Scored all 16 nodes with the PRD rubric and wrote `ranking.md` (a `pain_score` table, a
  `pick_score` table, and a "why the top five are ordered this way" section) plus `ranking.json` in the exact PRD
  schema. Two score adjustments were made after re-reading the extension source tree instead of trusting the
  scores written into the node files during US-002:
  - **P17** smallness 4→3 and novelty 2→1 — `lib/export/tokens.ts` already exports `estimateTokens()` and
    `lib/export/bundle.ts:497` already computes `tokens: estimateTokens(report)`, so the token estimate exists
    internally; only surfacing it in the UI is new. The genuinely new part is the user-editable copy block.
  - **P12** novelty confirmed at 1 — five open PRs already cover redaction (#42, #44, #38, #37, #31); only the
    credential-*type* signal is unclaimed.
  The node files were updated to match, and each of the 16 node files now also carries the derived
  `pain_score` / `pick_score` line so the node set and the ranking can never drift apart silently.

- **Files changed:**
  - `ranking.md` (new) — two ranking tables + top-five reasoning + caveats.
  - `ranking.json` (new) — machine-readable ranking, 16 nodes, `pain_rank` + `pick_rank` + `top_pick`.
  - `nodes/P17-evidence-cost-and-context-budget.md` — scores adjusted, with a note recording why.
  - `nodes/P01…P16.md` (all 16) — appended the derived `pain_score` / `pick_score` line.
  - `.ralph-tui/progress.md` — this entry plus two new Codebase Patterns.
  - Nothing written outside `OUTPUT_DIR`; the extension repo's `git status` is clean.

- **Learnings:**
  - Patterns discovered:
    - **Generate scored tables from code, never by hand.** My first hand-written `ranking.md` got the `pick_score`
      formula wrong on all 16 nodes (I summed the five components instead of weighting frequency/severity/fit at
      2). The fix was a generator script for the JSON plus a **validator that reads the markdown tables back and
      compares every component score, both derived scores, the rank column, the row order and the sort direction
      against the JSON**. That validator then caught a second bug — P03 and P17 tie on pain 16 / pick 30, and the
      markdown ordered them by hand while the JSON sorted by id. Both are now consistent and the tiebreak is
      documented in the file.
    - **Ground `novelty` and `smallness` in the extension's source.** A repo-wide grep of `lib/` + `entrypoints/`
      for `estimateTokens`, `verdict|confidence|not-a-bug` and `2000 px` decided three scores: P17 down (token
      estimate already exists), P16 up (nothing in the codebase has any verdict or confidence concept, so its
      novelty 4 is real), P05 confirmed (no dimension check anywhere).
    - **A "scored artifact needs a round-trip check."** Two renderings of the same ranking (markdown tables and
      JSON) will drift unless one is generated from the other and the other is validated against it.
  - Gotchas encountered:
    - Markdown table parsing bites twice: a `*` suffix on a cell (`P17*`) breaks an exact-match ID lookup, and
      the rubric's own `|`-separated table has 10 cells, so `cells[10]` raises `IndexError` — the columns are
      indices 0-9.
    - The two tables in `ranking.md` deliberately put `pain_score` and `pick_score` in different column order
      (primary key last), so a validator that assumes a fixed column position will report false mismatches.
    - `ranking.md` needed an explicit statement of the tiebreak (`pick_score` desc, then node id asc) because
      P03/P17 tie on both keys and their relative order is otherwise arbitrary.

- **Key findings to carry into US-005:**
  - **`top_pick` is P05** (pick 33): "make the screenshots safe for agents" — downscale every exported screenshot
    to a documented max dimension and normalise to JPEG, so no agent drops the image or has its session poisoned.
    Best combination of frequency (5), severity (4), fit (4), smallness (4) and novelty (3) in the set.
  - **P02 (pick 32)** is the substrate, not a feature: "copy for agent" is the right *mechanism* (highest fit 5,
    highest smallness 5) but its novelty is 1 — a dozen competitors already ship it (P15). US-005 should build P02
    as the delivery vehicle for P05 and P16, not pitch it as the differentiator.
  - **P16 (pick 31) is the highest-upside pick** and the only node with novelty 4: a deterministic three-valued
    verdict (pass / fail / unverified) plus a not-a-bug state, written by the extension from the recorded evidence
    rather than guessed by an LLM in the loop. No open PR covers it, and `grep` confirms the codebase has no
    verdict or confidence concept at all.
  - **P04 (pick 31)** is the best *new* pain from this run, but its novelty is only 2 — Clipy and ThinkRun already
    ship the agent-readable visual brief. The unclaimed remainder is offline + no MCP server + change-detected
    frames.
  - **P12 (pick 29)** has the highest severity (5) but five open PRs already cover redaction; only the
    credential-*type* signal ("a password was typed at 0:11") is unclaimed, and that is a thin slice.
  - US-005 must not duplicate open PRs: #21, #22 (closed), #23, #24, #25, #29, #31, #32, #37, #38, #39, #40, #41,
    #42, #44, #45, #47, #48, #49. In particular #32 (HAR export) covers P01's evidence, #42/#37/#31 cover P12's
    masking half, and #48 (labels and assignees when filing) covers P10's issue-side UI.

---

## 2026-11-17 - US-005

- **What was implemented:** Wrote `recommendation.md` (top 3 feature specs for Session Recorder by pick_score) and
  `run-summary.md` (method, counts, evidence weaknesses). **Also corrected a US-004 error** that changed the
  `top_pick`: US-004 had P05 ("make the screenshots safe for agents") as `top_pick` on the claim that *"no 2000 px
  dimension check exists anywhere"*. That claim was false — `lib/capture/screenshots.ts:38` reads
  `const MAX_SHOT_DIM = 1400;` and `ScreenshotScheduler.capture()` (lines 160-190) already downscales any
  screenshot whose longest side exceeds it via `OffscreenCanvas` and re-encodes it as JPEG. The sizing and
  format half of P05 was already shipped. P05 was re-scored (smallness 4→3, novelty 3→2, pick 33→29), and
  `ranking.md` + `ranking.json` were regenerated from the corrected scores via the US-004 script pair.

  The three features recommended, in order:

  1. **Copy for agent** (pick 32, nodes P02/P17/P05) — one action that puts the "Suggested prompt" (which today
     exists only in `docs/report-format.md`) plus the trimmed report plus an evidence-file footer on the clipboard.
     Defaults to L2, shows the token estimate that `estimateForLevels()` already computes. New pure module
     `lib/export/agent-prompt.ts`; button in `ExportPanel.tsx` and `entrypoints/report/main.ts`.
  2. **Evidence index** (pick 31, nodes P05/P01/P02) — a `## Evidence index` section at the top of `report.md`
     that tells the agent *which files to open*, in agent-directed language, and states which assets were
     trimmed at the current level so it never names a path that is not in the zip. New pure module
     `lib/export/evidence-index.ts`; `lib/export/markdown.ts` inserts it after `renderHeader()`.
  3. **Deterministic verdict** (pick 31, nodes P16/P06/P13/P11) — a three-valued `pass`/`fail`/`unverified` per
     finding plus a not-a-bug state, computed from the recorded event stream (no LLM). New pure module
     `lib/export/verdict.ts`; derives findings from `isAnomalian()` + `error` events; the not-a-bug note is a
     protected `session-note` event so it survives every trim level.

- **Files changed:**
  - `recommendation.md` (new) — 3 features, each with pain nodes cited, UX, real file paths, test plan, risks
    and the open PRs it must not duplicate.
  - `run-summary.md` (new) — counts (61 queries, 8 source types, 9 hypotheses, 51 URLs, 51 verified / 0
    unverified / 8 dropped, 16 nodes, 85 evidence bullets, 13 places covered, 122 raw payloads) and a
    per-tool worked/blocked table plus 10 named weaknesses.
  - `ranking.md` — rewritten; new "Correction made in US-005" section; both tables regenerated from the script.
  - `ranking.json` — regenerated; `top_pick` is now P02; P05 pick_score 33→29.
  - `nodes/P05-agents-cannot-consume-screenshots.md` — Session Recorder angle corrected with the source
    citations; scores adjusted with a note recording why.
  - `raw/regen_ranking.py` (new), `raw/validate_ranking.py` (new) — the generate-and-round-trip pair, extended
    with all 16 nodes' data and a validator that now strips `**` before parsing.
  - `.ralph-tui/progress.md` — this entry plus four new Codebase Patterns.
  - **Nothing written outside `OUTPUT_DIR`** (verified with `find -newermt` over `research/`); the extension
    repo's `git status` is clean.

- **Learnings:**
  - Patterns discovered:
    - **Grep for the constant, not the number in the external ticket.** The single most valuable thing this
      story produced. US-004's grep searched for `2000` (the limit quoted in claude-code #13480); the
      extension uses `MAX_SHOT_DIM = 1400`. One extra token pattern (`MAX_SHOT_DIM|MAX_DIM|maxDim`) inverted
      the `top_pick`. When scoring "does X already exist?", search for the *behaviour* and read the whole
      function — the constant was 20 lines from where the grep was pointing.
    - **Writing accurate file paths for a feature spec is a verification pass, not paperwork.** The PRD
      requires real paths, which forced re-reading `lib/capture/screenshots.ts`, `lib/export/markdown.ts`,
      `lib/export/bundle.ts`, `entrypoints/report/main.ts` and `entrypoints/share/useShareReport.ts` — the
      re-read is what surfaced the already-shipped feature. This is now a rule in the patterns section.
    - **A validator that crashes is a validator that has not run.** The round-trip checker died on
      `int('**18**')`; the markdown bolding has to be stripped before parsing. Fixed, and the check now
      passes on component scores, both derived scores, rank sequentiality, row order, sort direction and
      the score arithmetic in the JSON itself.
  - Gotchas encountered:
    - `find -newermt` is the reliable way to prove the guardrail "write only in OUTPUT_DIR" — and it must be
      run against the **parent** directory, excluding the output dir itself, or it reports the run's own files.
    - The extension's `git status` is a second, independent check that no source file was touched.
  - **Key findings to carry forward (to the owner):**
    - **The `top_pick` in `ranking.json` changed.** If the owner has already read the US-004 ranking, the
      order is now: pick rank = P02, P01, P05, P04, P16; pain rank = P01, P05, P12, P11, P02.
    - **P05's remaining pain is reachability, not safety.** `report.md` renders a screenshot as
      `![ctx](screenshots/001-0012.jpg)` (`lib/export/markdown.ts:368-376`); pasted as text that is a dead
      reference, and the extension has no path for delivering image bytes to an agent at all. That is the
      honest framing of feature 2.
    - **The notes' leaning (option A, "copy for agent") is the right mechanism and the wrong pitch.** It
      scores pick 32 but novelty 1 — a dozen competitors ship it (P15). It is recommended as feature 1
      because it is the delivery vehicle for features 2 and 3, not because it is novel.
    - **The highest-novelty pain is still P16** (novelty 4, nothing in the codebase or any open PR has a
      verdict, confidence or not-a-bug concept) but it rests largely on one HN thread, and it is the largest
      of the three builds. The recommendation ships its read-only half first.
    - **Nothing in the recommendation touches the crowded topics** the context notes warn about — export
      paging, SARIF, wait-for-review, fail-on gates, new `agent install` editors, or the five existing
      redaction PRs (#42, #44, #38, #37, #31).

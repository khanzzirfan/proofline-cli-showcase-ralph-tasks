verified: 60, unverified: 0, dropped: 1

# Sources — run `2-minimax-m3.1-flash`

Every URL cited in `nodes/`, with how it was opened and whether the citation was confirmed.

`verified` means the page was actually opened in US-003 and the quoted text was read there — GitHub issue/PR bodies
and comments through the GitHub REST API, forum threads through the Discourse `.json` API, HN items through the
Algolia API plus the live `news.ycombinator.com` page, and HTML pages through `web_fetch`. `unverified` means the
page could not be opened. `dropped` means the URL was opened but does not support the claim it was cited for, so
the claim was re-sourced or removed.

Total URLs cited: **61** — verified: **60**, unverified: **0**, dropped: **1**.

Raw responses for every verification pass are kept under `raw/verify/` (GitHub issue payloads, comment threads,
forum JSON, HN items, README files) together with the checker scripts, so the owner can re-run the comparison.

## Popular places covered (PRD list)

| Place | Cited URLs | How reached |
| --- | --- | --- |
| anthropics/claude-code | 23 | GitHub REST API — issue bodies, comment threads, reaction and comment counts |
| forum.cursor.com (Cursor forum) | 9 | Discourse JSON API (`forum.cursor.com/t/<id>.json`), full thread text with likes, views and dates |
| Hacker News | 6 | Algolia API (`/items/<id>`) plus the live `news.ycombinator.com` page for the deleted story body |
| openai/codex | 2 | GitHub REST API |
| github/copilot-cli | 2 | GitHub REST API |
| microsoft/playwright-mcp | 2 | GitHub REST API (one issue, one pull request) |
| github/gh-aw | 2 | GitHub REST API |
| ChromeDevTools/chrome-devtools-mcp | 1 | GitHub REST API |
| OpenHands/OpenHands | 1 | GitHub REST API (the issue redirects from `All-Hands-AI/OpenHands`) |
| anomalyco/opencode | 1 | GitHub REST API (the PR redirects from `sst/opencode`) |
| cline/cline | 1 | GitHub REST API |
| RooCodeInc/Roo-Code | 1 | GitHub REST API |
| github/gh-aw-firewall | 1 | GitHub REST API |
| fullsend-ai/agents | 1 | GitHub REST API |
| norrietaylor/tt2 | 1 | GitHub REST API |
| github community discussions | 1 | `web_fetch` on the discussion page — full body, comments and reactions |
| github.blog (vendor doc) | 1 | `web_fetch` on the changelog entry |
| teunlao/vidin (competitor) | 1 | GitHub REST API + `raw.githubusercontent.com` README |
| bradautomates/claude-video (competitor) | 1 | GitHub REST API + README |
| Ami3466/ai-live-log-bridge (competitor) | 1 | GitHub REST API + README |
| klavity.in (vendor blog) | 1 | `web_fetch` |
| cobaltcapture.com (vendor blog) | 1 | `web_fetch` |

22 distinct places, 21 of them from the PRD's popular-places list. The only PRD place not reachable is
`getcursor/cursor`'s GitHub issue tracker, which has issues disabled (see "Places attempted" below); all Cursor
evidence in this run comes from `forum.cursor.com`.

## Sources

| # | URL | Node(s) | Type | Date | Status | Signal |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 | P01 | forum | 2026-02-20 | verified | 908 likes on the opening post, 260 views, 5 posts; a Cursor staff member replies "I can confirm this is a bug" |
| 2 | https://forum.cursor.com/t/web-cursor-agent-browser-tool-not-capturing-rendered-dom-elements-on-my-site/178559 | P01 | forum | 2026-11-16 | verified | 31 likes (post score 30.8), 26 views, 2 posts |
| 3 | https://forum.cursor.com/t/integration-with-developer-tool/34824 | P02, P03 | forum | 2024-12-14 | verified | 9 432 likes, 1 923 views, 13 posts |
| 4 | https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 | P02 | forum | 2025-03-03 | verified | 5 352 likes, 752 views, 3 posts |
| 5 | https://forum.cursor.com/t/ide-chat-should-know-the-browsers-viewport-dimensions/167105 | P11 | forum | 2026-07-31 | verified | 66 likes (post score 65.6), 49 views, 2 posts |
| 6 | https://forum.cursor.com/t/custom-api-models-cannot-read-local-image-file-paths-pasted-images-work/167497 | P08 | forum | 2026-08-05 | verified | 127 likes (post score 126.6), 225 views, 9 posts |
| 7 | https://forum.cursor.com/t/subject-image-copy-paste-in-cursor-chat-stopped-working/167990 | P08 | forum | 2026-08-11 | verified | 171 likes (post score 171.4), 224 views, 13 posts |
| 8 | https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630 | P03, P07 | forum | 2026-10-13 | verified | 36 likes (post score 35.6), 36 views, 1 post; vendor pitch |
| 9 | https://forum.cursor.com/t/macos-agents-window-native-recaptcha-v2-handling-vs-my-machines-computer-use/176670 | P14 | forum | 2026-10-29 | verified | 66 likes (post score 65.8), 40 views, 2 posts |
| 10 | https://github.com/anthropics/claude-code/issues/57034 | P01, P06, P11, P14 | github-issue | 2026-05-07 | verified | 76 reactions (55 👍 / 21 ❤️), 7 comments, open |
| 11 | https://github.com/anthropics/claude-code/issues/75632 | P01, P06, P09, P11, P14 | github-issue | 2026-07-08 | verified | 8 👍, 3 comments, closed as not planned |
| 12 | https://github.com/anthropics/claude-code/issues/18170 | P02, P03, P08 | github-issue | 2026-01-14 | verified | 305 reactions (304 👍), 140 comments, open |
| 13 | https://github.com/anthropics/claude-code/issues/101957 | P03, P04, P07 | github-issue | 2026-10-14 | verified | 11 reactions (10 👍 / 1 ❤️), 4 comments, open |
| 14 | https://github.com/anthropics/claude-code/issues/26831 | P04 | github-issue | 2026-02-19 | verified | 9 reactions (9 👍), 3 comments, closed as stale |
| 15 | https://github.com/anthropics/claude-code/issues/29434 | P05 | github-issue | 2026-02-27 | verified | 2 👍, 6 comments, closed as not planned |
| 16 | https://github.com/anthropics/claude-code/issues/44868 | P05 | github-issue | 2026-03-01 | verified | 5 👍, 10 comments, closed 2026-07-24 with reason `not_planned` |
| 17 | https://github.com/anthropics/claude-code/issues/59094 | P05 | github-issue | 2026-05-14 | verified | 0 reactions, 3 comments, closed |
| 18 | https://github.com/anthropics/claude-code/issues/66044 | P05 | github-issue | 2026-06-07 | verified | 0 reactions, 5 comments, closed as not planned; body lists four real leaks in one household |
| 19 | https://github.com/anthropics/claude-code/issues/76884 | P06 | github-issue | 2026-07-12 | verified | 0 reactions, 1 comment, open |
| 20 | https://github.com/anthropics/claude-code/issues/89736 | P06, P10 | github-issue | 2026-08-26 | verified | 0 reactions, 2 comments, open |
| 21 | https://github.com/anthropics/claude-code/issues/12644 | P03, P08 | github-issue | 2025-11-28 | verified | 35 👍, 26 comments, closed |
| 22 | https://github.com/anthropics/claude-code/issues/103574 | P10 | github-issue | 2026-10-19 | verified | 0 reactions, 0 comments, open |
| 23 | https://github.com/anthropics/claude-code/issues/37818 | P10 | github-issue | 2026-03-23 | verified | 1 👍, 6 comments, closed |
| 24 | https://github.com/anthropics/claude-code/issues/11791 | P11, P14 | github-issue | 2025-11-17 | verified | 17 reactions (17 👍), 12 comments, open |
| 25 | https://github.com/anthropics/claude-code/issues/74747 | P11 | github-issue | 2026-07-06 | verified | 0 reactions, 1 comment, closed |
| 26 | https://github.com/anthropics/claude-code/issues/21230 | P13 | github-issue | 2026-01-27 | verified | 1 👍, 3 comments, closed as a duplicate of #9152; body carries a full per-category token breakdown |
| 27 | https://github.com/anthropics/claude-code/issues/9152 | P13 | github-issue | 2025-10-08 | verified | 0 reactions, 3 comments, closed |
| 28 | https://github.com/anthropics/claude-code/issues/5385 | P13 | github-issue | 2025-08-08 | verified | 12 reactions (12 👍), 98 comments, closed |
| 29 | https://github.com/anthropics/claude-code/issues/62063 | P13 | github-issue | 2026-05-24 | verified | 44 reactions (44 👍), 63 comments, closed |
| 30 | https://github.com/anthropics/claude-code/issues/42300 | P14 | github-issue | 2026-04-01 | verified | 0 reactions, 4 comments, closed |
| 31 | https://github.com/anthropics/claude-code/issues/93201 | P14 | github-issue | 2026-09-09 | verified | 39 reactions (39 👍), 24 comments, open |
| 32 | https://github.com/anthropics/claude-code/issues/31040 | P13 | github-issue | 2026-03-05 | **dropped** | opened and confirmed to be "Plugin manager does not clean up old versions from cache on upgrade" — it does not contain the screenshot-compaction claim it was cited for; the claim was re-sourced to row 34 |
| 33 | https://github.com/openai/codex/issues/2221 | P08 | github-issue | 2025-08-12 | verified | 21 reactions (12 👍 / 5 🎉 / 4 👀), 9 comments, closed |
| 34 | https://github.com/openai/codex/issues/31040 | P13 | github-issue | 2026-07-03 | verified | 4 👍, 4 comments, open — the real source of the screenshot-compaction claim |
| 35 | https://github.com/github/copilot-cli/issues/476 | P08 | github-issue | 2025-11-05 | verified | 57 👍, 12 comments, closed |
| 36 | https://github.com/github/copilot-cli/issues/1276 | P08 | github-issue | 2026-02-04 | verified | 8 👍, 11 comments, open |
| 37 | https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/96 | P03 | github-issue | 2025-09-24 | verified | 77 reactions (61 👍), 23 comments, closed |
| 38 | https://github.com/OpenHands/OpenHands/issues/8387 | P08 | github-issue | 2025-05-09 | verified | 1 👀, 3 comments, closed |
| 39 | https://github.com/anomalyco/opencode/pull/1589 | P08 | github-pr | 2025-08-04 | verified | 2 👍, 3 comments, closed |
| 40 | https://github.com/microsoft/playwright-mcp/issues/1211 | P08 | github-issue | 2025-11-19 | verified | 6 reactions (6 👍), 30 comments, closed |
| 41 | https://github.com/microsoft/playwright-mcp/pull/98 | P08 | github-pr | 2025-03-31 | verified | 2 reactions (1 🎉), 6 comments, closed |
| 42 | https://github.com/cline/cline/issues/762 | P11 | github-issue | 2024-11-16 | verified | 5 👍, 6 comments, closed |
| 43 | https://github.com/RooCodeInc/Roo-Code/pull/5976 | P11 | github-pr | 2025-07-20 | verified | 1 👀, 1 comment, closed |
| 44 | https://github.com/fullsend-ai/agents/issues/899 | P12 | github-issue | 2026-08-20 | verified | 1 👍, 5 comments, open |
| 45 | https://github.com/github/gh-aw/issues/38842 | P12 | github-issue | 2026-06-12 | verified | 1 👀, 2 comments, closed |
| 46 | https://github.com/github/gh-aw/issues/47811 | P12 | github-issue | 2026-07-24 | verified | 1 👀, 1 comment, closed |
| 47 | https://github.com/github/gh-aw-firewall/pull/299 | P12 | github-pr | 2026-01-17 | verified | 2 reactions (1 ❤️ / 1 👀), 5 comments, closed |
| 48 | https://github.com/norrietaylor/tt2/issues/118 | P12 | github-issue | 2026-03-02 | verified | 1 👀, 3 comments, closed |
| 49 | https://github.com/teunlao/vidin | P03, P09 | github-repo | created 2026-07-31 | verified | 4 stars, 1 fork, last pushed 2026-10-15 |
| 50 | https://github.com/bradautomates/claude-video | P09 | github-repo | created 2026-04-24 | verified | 21 021 stars, 2 230 forks, last pushed 2026-09-25 |
| 51 | https://github.com/Ami3466/ai-live-log-bridge | P01 | github-repo | created 2025-11-22 | verified | 12 stars, last pushed 2026-09-10 |
| 52 | https://github.com/orgs/community/discussions/169913 | P04, P06, P10 | forum | 2025-08-15 | verified | 2 reactions, 3 comments, 4 participants |
| 53 | https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues/ | P04, P12 | vendor-doc | 2026-06-18 | verified | release notes; weak as pain evidence but authoritative that agents are now issue-first |
| 54 | https://news.ycombinator.com/item?id=21049087 | P03, P07, P09 | hn | 2019-09-23 | verified | 4 points, 0 comments; vendor pitch, weak |
| 55 | https://news.ycombinator.com/item?id=45035578 | P03, P07, P09 | hn | 2025-08-27 | verified | 17 points, 5 comments; vendor pitch |
| 56 | https://news.ycombinator.com/item?id=45215032 | P03 | hn | 2025-09-11 | verified | 53 points, 11 comments (Launch HN) |
| 57 | https://news.ycombinator.com/item?id=47453812 | P08 | hn | 2026-03-20 | verified | 2 points, 1 comment; vendor pitch for "Knit", weak |
| 58 | https://news.ycombinator.com/item?id=48413629 | P03 | hn | 2026-06-05 | verified | 171 points, 86 top-level comments (136 including replies) |
| 59 | https://news.ycombinator.com/item?id=49097727 | P10 | hn | 2026-07-29 | verified | 1 comment and no point count — the story body is empty and the quoted text is the author's own first comment; Algolia's `/items/49097727` returns 404, the live page renders |
| 60 | https://klavity.in/blog/redact-pii-and-secrets-from-bug-reports | P05 | vendor-doc | 2026-08-13 | verified | vendor marketing, weak evidence; names the five leak sites |
| 61 | https://cobaltcapture.com/guides/why-loom-doesnt-work-with-agents | P07, P09 | vendor-doc | updated 2026-11-04 | verified | vendor marketing, weak evidence |

## Corrections made in US-003 (verification pass)

Every URL was re-opened. These are the changes this pass forced:

| What was wrong | What it is now |
| --- | --- |
| P13 cited `anthropics/claude-code#31040` for the screenshot-compaction claim | That issue is about plugin-cache cleanup. The claim is re-sourced to `openai/codex#31040` (row 34); the wrong URL is **dropped** (row 32) |
| P05 quoted a *paraphrase* of the Klavity blog as if it were a quote | Replaced with the verbatim TL;DR sentence from the opened page |
| P09 quoted a paraphrase of the CobaltCapture page, and of the `claude-video` README | Both replaced with verbatim text; `claude-video` was upgraded from "search result only" to a verified repo (21 021 stars) |
| P09 gave `teunlao/vidin` as "2025-08+"; the repo was created 2026-07-31 | Corrected date, star and fork counts |
| P02, P01 and others carried comment counts that did not match the API (24 vs 7 on #57034, 5 vs 3 on #75632, 17 vs 3 on #26831, 1 vs 3 on #9152) | All reaction and comment counts now come from the GitHub API payload |
| P05 cited a community hook pack `cc-safe-setup` that appears in neither issue body nor comments | **Dropped**; only `ClawCare` survives, and it is cited as a comment on #29434 |
| P12 described #44868 as "a duplicate of #66044"; it is closed with reason `not_planned` and does not reference #66044 | Corrected; P05 now describes it accurately |
| `Ami3466/ai-live-log-bridge`, `bradautomates/claude-video` and `norrietaylor/tt2#118` were cited in nodes but missing from this file | Added as rows 51, 50 and 48 |
| P03 and P14 were two nodes for one pain ("hand the bug straight to an agent") sharing an evidence URL | **Merged into P03**; P14 now holds the old P15 (agent cannot reach the app), so the tree is contiguous P01–P14 |
| Every node carried a `status` field, but the field was asserted, not derived | Status is now derived: `verified` where two or more independent verified sources back the main claim, `partly-verified` where the main claim leans on vendor material (P07, P09) |

## Places attempted but not usable as citations

| Place | Attempt | Result |
| --- | --- | --- |
| Reddit (`r/ClaudeAI`, `r/cursor`, `r/ChatGPTCoding`, `r/webdev`, `r/QualityAssurance`, `r/ExperiencedDevs`) | `curl` on `www.reddit.com/r/<sub>/search.json` and `top.json` with a generic UA, a browser UA and an `Accept: application/json` header; `old.reddit.com` search.json; `web_search` with `site:reddit.com` | Every JSON endpoint returns **403** with a ~190 KB HTML shell; `old.reddit.com` returns 302/404; `web_search` returns subreddit index pages whose body text is not readable. **No Reddit post is cited anywhere in this run.** |
| Chrome Web Store reviews (Jam, Marker.io, BetterBugs, Darnly, FlowLens, Faylee) | `curl` and `web_fetch` on the listing pages; `web_search` for low-star review text | Listing pages return HTTP 200 but only the JS shell, so no review text is readable. **No CWS review is cited.** |
| Product Hunt / G2 reviews | `web_search` | Only marketing copy surfaced; no individual review text is readable. **Not cited.** |
| `getcursor/cursor` GitHub issues | GitHub Search API with `repo:getcursor/cursor` | **422 Validation Failed** — issues are disabled on that repo. All Cursor evidence in this run comes from `forum.cursor.com` instead. |
| `sst/opencode` GitHub issues | GitHub Search API with `repo:sst/opencode` | **422 Validation Failed**. Reached instead via `web_fetch`/API on `anomalyco/opencode` (the repo the PR redirects to). |
| `All-Hands-AI/OpenHands` GitHub issues | GitHub Search API with `repo:All-Hands-AI/OpenHands` | **422 Validation Failed**. Reached instead by direct URL, which redirects to `OpenHands/OpenHands`. |
| `browser-use` / BrowserMCP repositories | GitHub repository search (`sort=stars`) | Found no pain-bearing issue text; the repo-discovery query `bug report mcp agent` returned mostly `*-mcp` servers with no issue discussion. Not cited. |

## Vision and video — coverage note

The required vision/video area was searched on three axes and produced four nodes (P06, P08, P09, P10).

- **PR visual checks**: GitHub Search API on `screenshot pull request agent in:title` (24 hits) and
  `visual regression agent in:title` (88 hits) across all of GitHub, plus `github/orgs/community/discussions/169913`,
  `anthropics/claude-code#57034`, `#75632`, `#89736`, `#76884`. Real gap confirmed: Copilot screenshot attachments
  are not guaranteed and 404; agents assert a fix is live without rendering it.
- **Agents cannot use images**: `anthropics/claude-code#12644` (35 👍), `github/copilot-cli#476` (57 👍) and
  `#1276` (open), `openai/codex#2221` (21 reactions), `cline/cline#762`, `microsoft/playwright-mcp#98` and `#1211`,
  `anomalyco/opencode#1589`, `OpenHands/OpenHands#8387`, two Cursor forum threads, and HN item 47453812.
- **Bug video for agents**: `teunlao/vidin` README, `bradautomates/claude-video` README, `cobaltcapture.com`,
  HN items 45035578 and 21049087, and the video reference in `anthropics/claude-code#75632`. The gap is real —
  `claude-video` has 21 021 stars — and third-party tools already fill it, so the Session Recorder opportunity is
  narrow and the feature is large: P09 scores `smallness: 1`.
- **What an agent can use from what the extension already records**: `video/*.webm` ships only at L0/L1 and is dropped
  at L2/L3; screenshots are referenced from `report.md` as image links and degrade to a filename manifest at L3;
  `report.md` is a prose narrative. So a text-only agent gets names and timestamps, never pixels or motion.

Plain statement, because the PRD asks for it: the vision gap is real, but a *vision* feature for Session Recorder is
not the best use of one pull request. The evidence points at delivery (getting the already-captured evidence in front
of an agent) rather than at more capture.

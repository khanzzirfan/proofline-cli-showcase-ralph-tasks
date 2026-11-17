# Run summary — pain research: 5-deepseek-v4-pro

Agent: deepseek/deepseek-v4-pro · 2026-11-17

## What I did

I ran the PRD brief end to end: planned the search (US-001), collected evidence into nodes (US-002),
verified every cited URL (US-003), scored and ranked the nodes (US-004), and wrote the recommendation
and this summary (US-005). Everything was written only inside `OUTPUT_DIR`.

## Counts

- Search queries planned: **29**, across **7 source types** (GitHub reactions, GitHub comments, GitHub
  repo discovery, Reddit top, HN Algolia, web search, web fetch).
- Hypotheses tested: **6** (the five notes pains plus the required H6 on vision/video).
- Node files: **15** (`nodes/P01`–`P15`), each with ≥2 evidence links and a popularity signal.
- Nodes NOT already in the notes' section 5: **9** (P05, P09, P10, P11, P12, P13, P14, P15, and P08's
  keyframe/timeline form is a new articulation of the required vision/video area).
- Vision/video nodes: **3** (P08 video→keyframes, P11 PR visual review, P07 agent-cannot-read-images).
- Sources: **25 verified, 0 unverified, 3 dropped** (see `sources.md`).

## What worked

- **Web search** (`web_search`): broad and `site:` queries; `site:reddit.com` returned only subreddit
  home pages (no usable threads), so Reddit contributed no cited evidence.
- **Web fetch** (`web_fetch`): opened and read every cited blog, forum, vendor-doc and HN page.
- **GitHub search API** (`search/issues`, `sort=reactions`/`sort=comments`): the primary popularity
  signal for `anthropics/claude-code` and others. The unauthenticated core API rate-limited (60/hr)
  and was exhausted by US-002, so US-003 re-verified GitHub issues by fetching the issue HTML pages
  and reading `<title>` instead.
- **HN Algolia API** (`search` and `items/{id}`): points/comments for stories, and full item + children
  text for comment-level quotes.

## What did not work

- **Reddit `search.json`**: returned an HTML block page (not JSON) for all four subreddits; recorded
  under `raw/` for transparency and marked dropped.
- **Three repos were renamed**: `getcursor/cursor`, `sst/opencode`, and `All-Hands-AI/OpenHands` →
  `OpenHands/OpenHands` all returned HTTP 422 on issue search.

## Top finding

P08 (pick_score 34) is the strongest single PR: turn the recorded tab video + transcript + click
events into an agent-readable keyframe timeline. It has maximum fit (the recorder already captures the
video/transcript/clicks but `report.md` only references the clips) and maximum novelty (no open PR
touches it). P02 (one-click "copy for coding agent", 32) and P01 (agent-consumable DOM context, 31)
round out the top three. See `recommendation.md` for the three specs.

## Weaknesses of the evidence

- **No Reddit evidence.** Reddit's JSON API is blocked, so the `r/ClaudeAI`, `r/cursor`,
  `r/ChatGPTCoding`, `r/QualityAssurance` and `r/ExperiencedDevs` coverage required by the brief could
  not be cited. The brief's Reddit fallback (web search) returned only home pages.
- **Single-source node.** P08's keyframe/timeline pain rests on one issue
  (anthropics/claude-code#12676) — but it is a very strong signal (57 reactions, 21 comments) and its
  comment quotes are the feature's whole basis.
- **CLI-agent skew.** Most strong evidence is from `anthropics/claude-code` and Cursor/HN; cloud
  agents (Jules, Devin, OpenHands resolver) are covered but thinner, because their issue trackers carry
  less community engagement.
- **Forum extraction limits.** Cursor forum pages return only their title through `web_fetch`
  (Discourse body not extracted), so P02's forum quote is title-only.
- **Vendor/blog evidence is weak.** A few nodes lean on vendor docs and blog posts (GitHub Copilot,
  Sandbase, BrowserAct, GitGuardian); these are treated as weak evidence and corroborated where possible.

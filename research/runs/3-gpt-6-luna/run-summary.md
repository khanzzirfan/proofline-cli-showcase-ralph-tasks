# Run summary

## Method and counts

- Search plan: 40 concrete queries across web search, Reddit, Hacker News, GitHub issues/discussions, Cursor forum, browser-agent repos, vendor documentation, and product/review pages.
- Research nodes: 13 (`P01`–`P13`), each with at least two cited evidence links.
- Unique URLs cited in node evidence: 18 total — 14 verified and 4 unverified. One additional discovery URL was dropped (404); counts match the first line of `sources.md`. Unverified title-only Cursor forum pages are not sole support for retained main claims.
- Required API data: GitHub reactions-sorted response, Hacker News Algolia story and comment JSON, and Reddit top-search attempt are recorded under `raw/`.

## Tools that worked

- **Web search:** Worked for broad and targeted discovery, but some searches returned temporary 502 errors or irrelevant results. Search covered the popular agent repos and communities named in `sources.md`.
- **Web fetch:** Worked for cited GitHub issues, HN pages, GitHub docs/discussions, and technical posts. Cursor forum pages yielded titles without readable post bodies and remain unverified. A discovery-only OpenHands docs URL returned 404 and is dropped.
- **GitHub API via curl:** Worked for the reactions-sorted Claude Code issue search and supplementary repo queries; raw responses are in `raw/`. Counts/reactions are recorded in sources and node evidence where visible.
- **Reddit via curl:** Did not work; Reddit returned an HTML network-security block instead of the requested JSON. A Reddit QA search result also hit a humanity challenge on fetch, so it was excluded from node evidence.
- **Hacker News Algolia API:** Worked for story and comment queries; raw JSON is saved in `raw/`, and visible points/comments are reported for cited items.

## Evidence limitations

The strongest repeated evidence comes from GitHub issues for Claude Code, especially browser visibility and verification requests; some items have substantial reactions, but repository issue activity is not a representative sample of all developers. HN evidence was low-engagement and sparse. Reddit did not provide usable API data, Cursor forum bodies could not be verified, and several searched agent repositories produced no usable first-person reports in this run. Product/project repositories and vendor-authored posts were treated as weak or promotional evidence rather than broad prevalence proof.

Visual evidence supports screenshot-input and PR screenshot reliability gaps, but the run did not verify a distinct user complaint that coding agents cannot consume bug videos. Session Recorder already exports screenshot/video assets and a manifest, so recommendations focus on handoff and asset navigation, not adding capture or video-analysis features. Scores and recommendation scope are hypotheses for a small PR, not proof of demand beyond the cited sources.

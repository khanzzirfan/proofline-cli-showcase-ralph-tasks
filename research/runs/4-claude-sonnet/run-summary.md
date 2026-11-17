# Run summary: 4-claude-sonnet (2026-11-17)

## What I did
- US-001: wrote `plan.md` with 28 queries across 6 source types and 11 hypotheses (the five notes pains, vision and video, and extras).
- US-002: ran searches, wrote 13 node files (P01 to P13) and saved raw JSON under `raw/` (69 files).
- US-003: re-fetched every cited URL and grepped each quote against the page or API text.
- US-004: scored by script, wrote `ranking.md` and `ranking.json`.
- US-005: wrote `recommendation.md` (3 specs) and this file.

## Counts
| Item | Count |
|---|---|
| Queries planned in plan.md | 28 |
| Nodes | 13 (11 verified, 2 partly-verified) |
| Nodes not in notes section 5 | 6 (P07 to P12) |
| Vision and video nodes | 5 (P04, P06, P07, P08, P09) |
| Sources recorded | 61 (verified 51, unverified 9, dropped 1) |
| Raw JSON files | 69 |
| Popular places covered | 12 of the PRD list |

## Which tools worked
- **GitHub search API** (`sort=reactions`): worked. Needed `in:title`; plain keywords returned noise.
- **Hacker News Algolia** (search and `/items/<id>`): worked.
- **Cursor forum** (Discourse `.json`): worked, gives views and likes.
- **Web fetch / curl** on issues, blogs, Chrome Web Store (Jam, Darnly): worked.
- **Chrome Web Store**: BetterBugs and Marker.io pages unavailable; Jam opened.
- **Reddit JSON** (www and old): **blocked**. `site:reddit.com` web search returned nothing. **No Reddit evidence.**
- **Product Hunt and G2**: 403 to curl; those quotes are marked unverified.
- **Web search tool**: used for broad queries; thin for Reddit.

## Weaknesses of the evidence
- No Reddit coverage: r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev, r/QualityAssurance, r/ExperiencedDevs are missing, so frequency may be under-counted for casual complaints.
- Hand-off pain (P03) rests on small Hacker News posts and vendor copy (FlowLens, Heckle, Darnly). Vendor marketing is weak evidence and engagement is low.
- The high-engagement evidence (image paste, oversized images, video input, browser connect) is about agents, not about bug reports, so the link to Session Recorder is my judgement.
- P09 and P13 are only partly verified.
- fit, smallness and novelty scores are my judgement from reading the extension files, not from building anything. Open-PR overlap was read from the notes list only, not from the PR diffs.
- Agent image-size limits (feature 3) were not checked against vendor docs or the extension's real screenshot sizes.
- Quote checks matched the page text, but GitHub reaction counts are a snapshot from the day of the run.

## Files
All writes were inside `OUTPUT_DIR`. I only read (not wrote) the notes and the extension folder.

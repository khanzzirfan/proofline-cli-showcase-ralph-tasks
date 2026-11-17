---
id: P08
title: “The agent says it added screenshots, but the PR evidence is missing or broken”
who: developers, QA, reviewers
tools: [GitHub Copilot coding agent, GitHub]
status: verified
---
## Pain
Visual proof in an agent-created PR can be inconsistent: screenshots may point to 404s, be committed as unintended files, or be claimed but absent. Reviewers cannot rely on a textual claim that a screenshot exists.
## Evidence
- https://github.com/orgs/community/discussions/169913 (github-discussion, 2025-08-15, verified): reporter says screenshots were “a 404,” committed into the PR, or missing despite being claimed; 3 comments.
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs (vendor-doc, date unknown, verified): documents adding image context to Copilot task descriptions, confirming image-based issue input is supported but not screenshot output reliability.
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): contrasts competing cloud agents’ PR screenshots with a cloud agent lacking a browser; 8 reactions, 9 comments (author’s comparison, not independent verification).
## How users want it fixed
- Provide a consistent way to capture and attach before/after evidence, with an explicit check that the artifact is present: https://github.com/orgs/community/discussions/169913.
## Workarounds people use today
- Commit screenshots in a known directory or automate capture/upload through CI; both suggestions appear in the discussion replies.
## Session Recorder angle
Existing extension screenshots and annotations are included in the ZIP manifest, but it does not verify the coding agent’s later PR artifacts. Do not overlap with #21, which covers capture/pause shortcuts; no open PR directly duplicates reliable export verification.
## Scores
frequency: 2  severity: 3  fit: 4  smallness: 4  novelty: 4

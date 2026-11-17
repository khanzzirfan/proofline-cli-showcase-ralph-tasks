# Feature 1: Copy for coding agent (with an agent brief)

## Problem

Handing a recording to a coding agent takes five manual steps: export the ZIP, unzip it, open `report.md`, find the
suggested prompt in `docs/report-format.md`, and paste both. The prompt exists only in the docs; the code can copy
issue Markdown (`copyIssue` in `entrypoints/share/useShareReport.ts`) but nothing agent-shaped.

Research (7 runs): top pick in 6 of 7. Evidence includes claude-code #57034 (76 reactions: the agent can't see the
running app) and Cursor forum threads on lossy pasting.

## What the user sees

```
 Side panel ▸ Export                             Report page (report.html)
 ┌────────────────────────────────────┐          ┌──────────────────────────────────────────┐
 │ Level  ( L0 ) ( L1 ) (•L2) ( L3 )  │          │  … report …                              │
 │ ≈ 6.2k tokens                      │          │  [ Download ZIP ]  [ Copy for agent ]  ◀─ new
 │ [ Download ZIP ] [ Copy for agent ]│ ◀─ new   └──────────────────────────────────────────┘
 │  ✓ Copied 6.2k tokens. Paste into  │
 │    Claude Code, Codex or Cursor.   │          One click. No unzip. Works offline, no account.
 └────────────────────────────────────┘
```

## Architecture

```
  user click "Copy for agent" (ExportPanel.tsx  or  report/main.ts)
        │  sessionId, level (current export level, default L2)
        ▼
  getSession / getEvents / getAssets            (lib/storage, existing)
        │
        ▼
  buildBundle({ session, events, assets, level })   (lib/export/bundle.ts, existing)
        │  ExportFile[]  ── report.md (already trimmed + redacted), MANIFEST.md, …
        │  trimmed events (via applyLevel)
        ▼
  ┌──────────────────────────── lib/export/agent-handoff.ts  (NEW, pure) ───────────────────────────┐
  │                                                                                                  │
  │  buildAgentBrief(events, session)                                                                │
  │    ├─ userContext   ← marker, note, session-note, annotation  (the user's own words lead)         │
  │    ├─ reproSteps    ← click/input/nav/spa-route/tab-* in order, labelled with briefEventLabel()   │
  │    │                  (lib/export/anchor.ts, existing), capped at N steps                         │
  │    ├─ firstFailure  ← first 'error' event, first console error, first net-request with status≥400 │
  │    ├─ expectedVsActual ← from notes/annotations when stated; otherwise "not stated by reporter"   │
  │    └─ acceptance    ← each distinct error message / failing METHOD path+status that must NOT recur│
  │                                                                                                  │
  │  renderAgentHandoff({ brief, reportMd, prompt, level })                                          │
  │    = PROMPT (from report-format "Suggested prompt", kept as one constant in code)                │
  │      + "## Agent brief" (the five sections above, each line cites [mm:ss])                      │
  │      + "## Report" (report.md text for the chosen level)                                         │
  │      + footer: what was left out (screenshots, video, bodies) and how to get it (export ZIP)      │
  │                                                                                                  │
  │  estimateTokens(text)   (lib/export/tokens.ts, existing)                                         │
  └──────────────────────────────────────────────┬───────────────────────────────────────────────────┘
                                                 │  one Markdown string
                                                 ▼
                         navigator.clipboard.writeText(text)   → status "Copied ≈N tokens"
                         (on failure: show the text in a textarea to copy by hand)
```

### Example payload (shape)

```markdown
You are a debugging assistant. Below is a recorded browser session … (suggested prompt)

## Agent brief
**Reporter's words:** > [00:41] "Pay button does nothing after I change the plan"
**Steps to reproduce** (from the recording)
1. [00:03] Open https://app.example.com/billing
2. [00:12] Click "Change plan" → select "Pro"
3. [00:38] Click "Pay"
**First failure:** [00:38] POST /api/checkout → 500; [00:38] ⚠ TypeError: cannot read 'id' of undefined
**Expected vs actual:** not stated by the reporter (infer from the steps and the failure)
**Acceptance check:** the fix is done when, repeating the steps, these no longer happen:
- POST /api/checkout returns 500
- TypeError: cannot read 'id' of undefined

## Report (level L2)
… report.md …

_Not included: 4 screenshots, 1 video segment, response bodies. Export the ZIP (L0/L1) for files._
```

## Files

| File | Change |
|---|---|
| `lib/export/agent-handoff.ts` | NEW. `buildAgentBrief`, `renderAgentHandoff`, `AGENT_PROMPT`. Pure; no chrome APIs. |
| `lib/export/agent-handoff.test.ts` | NEW. Vitest with `lib/fixtures/session-builder.ts`. |
| `entrypoints/sidepanel/components/ExportPanel.tsx` | Add the button next to Download, reuse its level + estimate. |
| `entrypoints/report/main.ts` + `index.html` | Add the button next to `downloadBtn`. |
| `docs/report-format.md`, `README.md` | Point "Use a report with a coding agent" at the button; prompt text lives in code. |
| `e2e/*.spec.ts` | One Playwright scenario: record demo bug, stop, click Copy, read clipboard, assert sections. |

## Decisions

- **Text only.** The clipboard gets Markdown, not images: agents and terminals accept pasted text everywhere.
  The footer says what was left out and that the ZIP carries the files.
- **Default level L2.** It keeps errors and failing requests and fits most context windows; the user's current level wins.
- **Brief is derived, never invented.** Every brief line cites a recorded `[mm:ss]` event; missing information is said plainly.
- **Acceptance check is the "proof of fix" hook.** It turns the recording into a test the agent (or a reviewer) can repeat.
- **Same redaction.** It reuses `buildBundle` output, so no evidence bypasses capture-time redaction.

## Tests

- Unit: brief order and caps; first failure picks the earliest of error/console/4xx-5xx; acceptance dedups;
  "not stated" path; token estimate; output for L0–L3; no asset ids or data URLs in the text.
- Playwright: demo app bug → stop → Copy → `navigator.clipboard.readText()` contains `## Agent brief` and the failing request.

## Risks

- Clipboard permission or focus failures → textarea fallback.
- Very long sessions → cap steps and acceptance items; the token estimate shows the size before copying.
- Overlap: open PRs #43 (Copy as cURL) and #48 (labels) are different; nothing else copies for agents.

# Feature 2: Video key frames and timeline

## Problem

Coding agents cannot watch video. Session Recorder can record tab video (`entrypoints/offscreen/video.ts`,
one webm per record-span, a `video-segment` event with `tStart`/`tEnd`), but:

- at L0/L1 the agent gets a multi-MB `video/NNN-mmss.webm` it cannot open;
- at L2+ `thinVideo()` clears the file, so the agent gets only "🎬 VIDEO segment 00:04–00:09".

Research (7 runs): top 5 in 5 of 7, top pick for DeepSeek v4 Pro. Evidence: claude-code #12676 "Video Input Support"
(57 reactions, 21 comments, open, lists "sharing quick recordings of bug reproduction steps"); single-purpose tools
(videobug, amagi-screen, BugDump) exist only to turn bug videos into frames and text.

## What the agent gets

```
report.md (any level)
  ## /billing
  [00:12] 🖱 click "Change plan"
  [00:12] 🖼 FRAME frames/003-0012.jpg  (after click "Change plan")      ◀─ new
  [00:38] 🖱 click "Pay"
  [00:38] ⚠ POST /api/checkout → 500
  [00:39] 🖼 FRAME frames/004-0039.jpg  (on error: POST /api/checkout 500) ◀─ new
  [00:41] > "Pay button does nothing"
  [00:41] 🖼 FRAME frames/005-0041.jpg  (annotation)                     ◀─ new

frames/   small JPEGs (≤ 1280 px wide, ~60–120 KB) kept at L0–L2, listed in MANIFEST.md
```

The timeline is the existing report timeline: frames are inserted as events at their timestamps, so they sit
next to the click, error or note that explains them. No separate timeline format.

## Architecture

```
                     (existing)                                      (existing)
  offscreen/video.ts ──▶ IndexedDB: asset{kind:'video', blob: webm}   video-segment {assetId, tStart, tEnd}
                                                     │                                 │
  ───────────────────────────────────────────── export time ─────────────────────────────────────────────
                                                     │                                 │
                                                     ▼                                 ▼
  ┌──────────────────────── lib/export/keyframes.ts  (NEW) ──────────────────────────────────────────────┐
  │                                                                                                       │
  │  1. planKeyframes(events, segments, opts)            PURE, unit-tested                                │
  │       candidates inside a segment's [tStart, tEnd]:                                                   │
  │         error / console error / net-request ≥400  → t + 300 ms   (show the result)                    │
  │         annotation, marker, note                  → t            (what the user pointed at)            │
  │         click / nav / spa-route                   → t + 500 ms   (after the UI reacts)                 │
  │         segment start and end                     → tStart + 200, tEnd − 200                           │
  │       skip a candidate within 1.5 s of a kept one (error > annotation > click > boundary)              │
  │       skip if a screenshot already exists within 1 s (no duplicate evidence)                           │
  │       cap: maxFrames (default 12 per session)                                                          │
  │       → FramePlan[] { segmentId, tSession, tInVideo = tSession − tStart, reason, eventId }             │
  │                                                                                                       │
  │  2. extractFrames(videoBlob, plan, extractor)        DOM-bound, injected                              │
  │       extractor = browserFrameExtractor (default in extension pages):                                 │
  │         <video src=URL.createObjectURL(blob) muted preload=auto>                                      │
  │         for each t: video.currentTime = t; await 'seeked'; drawImage → OffscreenCanvas/canvas         │
  │         → canvas.convertToBlob({type:'image/jpeg', quality:0.75}), scaled to ≤1280 px                 │
  │       failures per frame are recorded, never fatal (bad seek, codec) → report says "frame unavailable"│
  │                                                                                                       │
  │  3. frameEvents(plan, blobs) → synthetic 'screenshot'-like events {trigger:'video-frame', reason}      │
  │       + Asset{kind:'screenshot', mime:'image/jpeg'} (in-memory only, never written to IndexedDB)      │
  └──────────────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                                 │
                                                 ▼
  lib/export/bundle.ts  buildBundle({ …, frames?: FrameExtractor })      (existing, extended)
        if frames && session has video assets:
           events ← merge(events, frameEvents)   before applyLevel()
        applyLevel(level):  L0 L1 L2 keep 'video-frame' shots (key moments); L3 keeps event lines only
                            thinVideo() still drops the .webm at L2+  → frames replace video in compact bundles
        renderReport(): "🖼 FRAME frames/NNN-mmss.jpg (reason)" lines; MANIFEST.md lists frames/
        ▼
  ExportFile[] → ZIP download · publish (lib/sharing/report.ts) · Feature 1 footer counts frames
```

### Where it runs

```
  service worker (background.ts)   ✗ no <video>/canvas → never extracts frames; estimateForLevels() ignores frames
  side panel / report / share page ✓ DOM available → pass browserFrameExtractor into buildBundle
  vitest (jsdom)                   fake extractor returns tiny JPEG blobs → pipeline tested without decoding video
  Playwright (real Chrome)         real webm from the demo app → real frames decoded
```

## Files

| File | Change |
|---|---|
| `lib/export/keyframes.ts` | NEW. `planKeyframes` (pure), `FrameExtractor` type, `browserFrameExtractor`, `frameEvents`. |
| `lib/export/keyframes.test.ts` | NEW. Planning rules, spacing, caps, dedup with screenshots, segment bounds. |
| `lib/export/bundle.ts` | Optional `frames` input; merge frame events before `applyLevel`; write `frames/NNN-mmss.jpg`. |
| `lib/export/trimmer.ts` | `thinScreenshots('annotation-error')` (used by L2) must also keep `trigger:'video-frame'`; `'key-moments'` (L1) already keeps it because it only drops `'interaction'`; `'manifest-only'` (L3) drops it. |
| `lib/export/markdown.ts` | Render frame lines and the MANIFEST section. |
| `lib/session/types.ts` | Add `'video-frame'` to the screenshot trigger union. |
| `entrypoints/sidepanel/components/ExportPanel.tsx`, `entrypoints/report/main.ts`, `lib/sharing/report.ts` callers | Pass `browserFrameExtractor`. |
| `lib/export/bundle.video.test.ts` | Extend: L2 drops webm but keeps frames. |
| `e2e/*.spec.ts` | Record demo with video on → export L2 → ZIP has `frames/*.jpg`, report links them. |
| `docs/report-format.md` | Document `frames/` and the frame line. |

## Decisions

- **Frames at meaningful moments, not every N seconds.** The events already say when something happened; the
  planner samples the video at those times. That keeps frames few and each one explained.
- **Extraction at export, not at capture.** No change to recording, storage or permissions; old recordings benefit too.
- **Injected extractor.** `buildBundle` stays testable in jsdom; only extension pages decode video.
- **Frames replace video in compact levels.** L2 becomes the right default for agents with visual evidence intact.
- **Privacy.** Frames show the same pixels as the video the user chose to record. Capture-time redaction does
  not apply to pixels (true for screenshots today too); the export UI notes this like it does for screenshots.

## Tests

- Unit (planner): error beats click within 1.5 s; frame inside segment bounds only; cap respected; skip near
  existing screenshot; no video → no frames; stable file names.
- Unit (bundle with fake extractor): L0/L1/L2 include frames, L3 lines only; webm dropped at L2; MANIFEST lists frames.
- Playwright: real recording → frames decode → images are non-empty JPEGs at the right count.

## Risks

- **webm seeking.** MediaRecorder webm files often lack cues/duration, so seeking can be slow or land on keyframes
  only. Mitigation: set `currentTime` to a large value first to force duration, then seek; accept nearest frame;
  per-frame failure is non-fatal. This is the main technical risk; prove it first with a spike in Playwright.
- **Export time.** ~12 seeks per session; show progress in the existing "Preparing…" state.
- **Size.** 12 × ~100 KB ≈ 1.2 MB, far below the video; cap and quality are options.
- Overlap: no open PR touches video export (#21 adds screenshot shortcuts, #32 HAR export).

## Fit with Feature 1

Feature 1's footer lists frames as "not included in the copied text, in the ZIP under frames/". Built together,
the ZIP (frames + report) is the visual hand-off and the clipboard brief is the text hand-off.

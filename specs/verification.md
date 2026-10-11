# Verification and supported envelope

## Evidence contract

Every task adds or identifies its named deterministic check before running it. Planned test files/scripts in task contracts do not exist until implemented; a missing check is a failure, not permission to skip. Record exact command, revision, fixture seed/hash, executed/passed/failed/skipped counts and artifact path in progress. Rust name filters must execute at least one intended test. No paid inference or external model transport belongs in any check.

Use built-in Rust tests initially, Node's deterministic test runner for compiled JS adapters, and pinned Playwright for automated browser mechanics. Real OS IME, accessibility, native keyboards, autocorrection and dictation need a separately recorded manual/device matrix. Synthetic key events and Playwright WebKit do not establish full Safari or real-device input support.

## Fixtures

Task: 20 blocks/~10 KiB text. Long: 2,000 mixed blocks/~1 MiB. Large: 10,000/~5 MiB. Aged: long after 100,000 seeded edits. Adversarial: 250 KiB paragraph, fragmented marks, emoji/ZWJ/combining/RTL, nesting limits and wide tables. Multi-editor: 50 static previews, separately 1 and 10 active editors. Commit generators, seeds and expected semantic snapshots; record text bytes and serialized CRDT bytes separately.

## Provisional targets

These are retained design targets from the proposal and have no measured result yet. Pin actual hardware, browser/OS versions, CPU/network profiles and capability parity before making comparisons.

| Metric (p95 unless stated) | Desktop | Mid-range phone |
|---|---:|---:|
| Task preset JS+WASM+essential CSS, Brotli | 400 KiB | same artifact |
| Runtime/adapter JS, Brotli | 35 KiB | same artifact |
| Core ordinary edit | 1 ms | 2 ms |
| Input to visible update, controlled 60 Hz | 16.7 ms | 33 ms |
| Warm task activation | 50 ms | 100 ms |
| Warm long actual editability | 200 ms | 400 ms |
| Warm large actual editability | 750 ms | 1,500 ms |
| Matching preview first viewport | 50 ms | 100 ms |
| 10 KiB Markdown paste to formatted frame | 50 ms | 100 ms |
| 100 KiB Markdown paste to formatted frame | 150 ms | 300 ms |
| Local slash menu after ready | one frame | two frames |

Measure transfer, decode, compilation, instantiation, CRDT restore, DOM adoption, first accepted edit, p50/p95/p99, long tasks, memory plateau, peak paste memory, journal amplification and remote bursts. Warm includes local persistence restore; cold includes uncached assets and document transfer. Emit raw samples; summaries alone cannot establish a regression.

Qualify Task and Long as initial supported sizes. Large and Aged remain diagnostic stress fixtures until qualified. Missing a target requires a recorded release scope/architecture decision and honest published envelope. Data loss, silent import loss, divergent states, broken supported IME, corrupt undo, unsafe paste and stale-target overwrite cannot be waived as performance tradeoffs.

## Matrix and lifecycle

Automated target: Chromium, Firefox and WebKit versions pinned by the browser test lock. Manual release matrix specifies actual current desktop Chrome/Firefox/Safari and mobile Safari/Chrome versions and devices; unsupported combinations are explicit. Starting support claims are provisional until evidence exists.

Reuse suitable dev servers. Track PID, launcher, workspace, port and log for every task-owned server/browser; stop verified unused processes, verify listeners disappear, preserve other tasks' services. Record free disk before/after substantial sessions; remove only reproducible artifacts produced by that session when several GiB accumulated or less than 50 GiB remains. Preserve evidence and source.

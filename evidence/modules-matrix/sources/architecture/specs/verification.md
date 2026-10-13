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

## Public editor comparison evidence

REL-1.2 owns pinned optimized Tiptap/Lexical/edit.ac configurations and the limited plain-contenteditable reference; DOC-1.29/1.30 document and publish its evidence without another harness. Record minimal and feature-equivalent runs separately, exact versions/builds, schema/extension capabilities, rendering settings, collaboration/durability policy and all JS/WASM/CSS/optional costs. Use the fixture corpus above, identical hardware/browser/network settings and declared warmup/order/sample counts; retain unavoidable differences. Unsupported Large/Aged envelopes remain diagnostic.

REL-1.3 measures cold/warm first visible content and actual edit readiness separately, input-to-visible latency, HTML/Markdown paste, large-document operations, save/restore and reconnect with prepared local transports. REL-1.4 covers remote bursts, backpressure and mount/edit/destroy memory. Retain raw samples, p50/p95/p99 where supported by the sample count, artifact/profile hashes, failures/skips and reproduction commands. Include regressions; do not substitute targets or empty/insufficient samples for measured results. Synthetic input cannot establish real mobile/IME correctness. Public tables/charts expose provenance, Not yet measured and Inconclusive states, separate minimal/full configurations and downloadable sanitized data. No paid inference, ambient secrets or fixture recording is authorized.

## Matrix and lifecycle

Automated target: Chromium, Firefox and WebKit versions pinned by the browser test lock. Manual release matrix specifies actual current desktop Chrome/Firefox/Safari and mobile Safari/Chrome versions and devices; unsupported combinations are explicit. Starting support claims are provisional until evidence exists.

Reuse suitable dev servers. Track PID, launcher, workspace, port and log for every task-owned server/browser; stop verified unused processes, verify listeners disappear, preserve other tasks' services. Record free disk before/after substantial sessions; remove only reproducible artifacts produced by that session when several GiB accumulated or less than 50 GiB remains. Preserve evidence and source.

## Interaction-specific qualification

The [interaction case catalog](../tests/editor-interaction-cases.md) is planned coverage, not a test report. INT-1.1 creates its executable index; each behavior task creates/runs its cases; INT-1.14 records actual OS/IME/dictation/screen-reader/voice-control evidence, including extension-disabled operation. Every mandatory case must resolve to an executed assertion or an actual device observation before support is claimed. Track 39 adds independent optional-assistance lifecycle and platform qualification; a mocked recognition transport proves only the integration contract. Baseline and optional capabilities have separate published results.

## Mobile web evidence and cost

Tracks 40/41 use [mobile web](mobile-web.md), the [baseline cases](../tests/mobile-web-cases.md) and [extension cases](../tests/mobile-extension-cases.md). Record browser engine/version, device/OS, keyboard/locale, mode (tab/installed app/embedded host), requested/observed viewport policy and optional capabilities. Touch emulation and desktop WebKit are mechanical checks, not mobile support or phone-performance evidence. Compare identical packed baseline/disabled/enabled profiles, with incremental bytes, geometry work, startup/input/scroll costs and teardown counts. Preserve the existing total targets; freeze the proposed mobile allowance before measurement. Optional absent APIs require working fallbacks; required editing failures cannot be waived as optional API limitations.

## Editing suite architecture and oracles

[The suite contract](editing-regression-suite.md) separates plan validation, real semantic commands, sequence/history, property/interleaving, synthetic browser replay, actual browser actions and OS/device evidence. The [manifest](../tests/editing-suite/suite.json) indexes all 195 catalog cases, fourteen guards and twelve representative recipes; a covers link does not prove every variant of a case. Expected state must be independent of the implementation and include selection/pending marks plus attributable effects. Track 42 adds guard negative controls, fixed clocks, bounded quiescence and seeded failure minimization. Later feature/device owners retain their acceptance gates; fixture validation alone never closes them.


## Desktop interaction and mixed-extension performance

The deeper [research](../evidence/editing-performance-extension-research.md) extends existing performance gates without claiming measured improvements. Preserve existing budgets; record any proposed change before a run with its user-facing rationale. PRF cases in the [additional catalog](../tests/desktop-editing-cases.md) require the same document, machine, build mode/toolchain, warmup policy and sample method for baseline/candidate comparisons. Record distinct source/build revisions and profile identities; hold the feature set constant for like-for-like implementation comparisons. Compare baseline versus presets separately as explicit feature-cost experiments, with all other variables controlled. Report raw samples, sample count, median/p95/p99 where statistically meaningful, outliers and failures. An unrepresentative sample set is inconclusive rather than a tail-latency pass.

Measure input arrival through visible text/caret presentation separately from Rust command, FFI, patch/render/layout, persistence queue and optional-service costs. Web INP supplements these measurements but excludes continuous drag/scroll and cannot qualify them. Include long paragraphs/code lines, large selected ranges, tables, images, bidi/Unicode, active composition, slow optional work, collaboration bursts and multiple editors. Run baseline with no extensions, shipped presets and high-risk mixed features; optional work must not multiply baseline keystroke costs with total document size. Record changed blocks/bytes, rendered nodes, geometry reads/writes, queue bounds, cancellation and cache invalidation against actual edited regions. Asymptotic claims require several document sizes and raw traces, not one fast fixture.

Exercise sustained selection autoscroll and text dragging at the device's refresh rate, keyboard-open mobile viewports, native candidate windows and accessibility clients. Record missed-frame/long-task traces and the declared per-device thresholds; do not invent a universal frame guarantee or infer smoothness from average FPS. Idle editors must not poll continuously; coalesce adapter geometry per frame and stop scheduling when no interaction is active. Search/highlighting/conversion results are revisioned/cancelable and never restart a whole-document scan on every selection movement. Repeated mount/dispose, canceled transfers and extension unload must release resources and show a bounded memory plateau under a fixed replay. Tests use deterministic data/transports only. Performance evidence cannot waive content, selection, accessibility or history correctness.

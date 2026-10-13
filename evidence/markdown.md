# Markdown interchange and qualification

Date: 2026-10-13. Native parser/mapping/export uses CommonMark 0.31.2 and the pinned edit-ac-gfm-v1 fixtures. All 652 base and 23 required extension grammar cases remain covered by the portable suite; the suite itself executes 50 tests. Strikethrough, checklists and extended autolinks are enabled. Image/table/callout descriptors require explicit registration; disabled codecs retain exact source and diagnostics. Underline/unknown/unrepresentable content returns typed recovery. HTML admission is inert and bounded; raw HTML in Markdown remains a diagnosed source fallback.

## Reproduction and artifacts

Select Node 24.19.0. From core: `cargo test -p editac-markdown --locked --offline`; `npm run test:browser -- markdown-collaboration` with `EDITAC_MARKDOWN_COLLABORATION_OUTPUT` set to a separate evidence directory. The fixture generator is `core/benchmarks/paste/fixtures.mjs`, seed `editac-paste-v1-20261013`. Each receipt includes exact fixture byte/hash, browser version, source/package hashes, full raw samples, correctness snapshots and browser/server/consumer teardown. Baseline and candidate are the same fresh-session packed feature profile and machine, differing in bounded preflight reuse. Fixed batches use 2 warmups and 30 measured samples; formatted-frame cost is a conservative two-requestAnimationFrame presentation proxy. No physical-phone or peak-memory qualification is implied.

Native admission/compiled-WASM parity commands use absolute `EDITAC_WASM_COMMAND_OUTPUT=/Users/bpstr/Github/edit-ac/architecture/evidence/markdown/session-20261013/preflight-wasm`, `cargo test -p editac-wasm --lib --locked --offline`, then `node --test tests/wasm-commands.test.mjs`: 35 native + 39 Node tests passed, zero failures/skips. Wrong relative output-directory attempts are preserved, followed by the correct absolute-path parity run.

## Raw cost summaries

All values are p95 milliseconds; counts are 30 per row. The retained target is 50 ms for 10 KiB and 150 ms for 100 KiB. p99 is not qualified with this sample count.

| Engine | Source/build profile | Bytes | Prepare | Transfer | Apply | Formatted frame | Target result |
|---|---|---:|---:|---:|---:|---:|---|
| chromium | fresh-qualified | 10240 | 0.40 | 0.20 | 27.70 | 33.40 | met |
| chromium | fresh-qualified | 102400 | 3.60 | 0.50 | 154.10 | 167.80 | missed; release qualification required |
| chromium | costs-preflight | 10240 | 0.40 | 0.20 | 12.80 | 32.90 | met |
| chromium | costs-preflight | 102400 | 2.90 | 0.30 | 65.70 | 75.20 | met |
| firefox | fresh-qualified | 10240 | 1.00 | 1.00 | 63.00 | 77.00 | missed; release qualification required |
| firefox | fresh-qualified | 102400 | 8.00 | 1.00 | 201.00 | 228.00 | missed; release qualification required |
| firefox | costs-preflight | 10240 | 1.00 | 1.00 | 25.00 | 37.00 | met |
| firefox | costs-preflight | 102400 | 12.00 | 1.00 | 124.00 | 154.00 | missed; release qualification required |
| webkit | fresh-qualified | 10240 | 2.00 | 1.00 | 60.00 | 68.00 | missed; release qualification required |
| webkit | fresh-qualified | 102400 | 7.00 | 1.00 | 239.00 | 263.00 | missed; release qualification required |
| webkit | costs-preflight | 10240 | 2.00 | 1.00 | 32.00 | 40.00 | met |
| webkit | costs-preflight | 102400 | 6.00 | 1.00 | 134.00 | 156.00 | missed; release qualification required |

## Scope decision and preserved problems

This task qualifies interchange correctness and reports measured costs. It does not clear browser release track 10. The candidate meets the 10 KiB target in all three engines and the 100 KiB target in Chromium. Firefox/WebKit 100 KiB tail latency misses remain release blockers, with targets unchanged. The initial repeated-session probe revealed accumulated-history slowdown and eventual admission rejection at 100 KiB; those failures remain in `session-20261013/costs.log` and receipts. Fresh-session rows cannot qualify accumulated-history/Aged support. Engine/resource/history qualification owners must resolve that envelope before release; an offloaded parser alone would not address main-thread application cost. Original failed logs and rejected input recovery are preserved.

`session-20261013/fresh-qualified/` is the baseline; `costs-preflight/` is the candidate. Earlier remount harness failures (`fresh-costs.log`, `fresh-baseline.log`) came from reusing a fixture database across incompatible fresh identity spaces. The final harness recreates only its isolated test database and records stable fixture hashes.

Physical clipboard menus and OS shortcuts remain mandatory under FMT-1.15. Prepared browser variants do not establish actual-device support.

Portable source reconciliation is qualified by 13 dedicated cases and the 585-test core regression suite; see [source reconciliation evidence](markdown/source-reconciliation.md). The actual-device protocol and artifact identities are [pinned separately](markdown/device/manifest.json); no physical case has been observed.

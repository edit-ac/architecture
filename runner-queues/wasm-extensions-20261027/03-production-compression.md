# Deliver standard compressed production artifacts

Status: COMPLETE

Controller split, 2026-10-28: unstarted WEX-3.1 and WEX-3.2 now live in
[02d-rust-build-size.md](02d-rust-build-size.md), preserving their IDs and
implementation/validation obligations. This original source/progress pair remains
for WEX-3.3; no prior progress file or accepted task was reset. Read the current
manifest/queue, not an old stopped-run FIFO or continuation snapshot.

Progress: `.roadmap-runner/wasm-extensions-20261027/03-production-compression.progress.md`.
Entry: accepted original source01/02 and current source02a accepted/deferred dispositions;
WEX-9.1/WEX-3.1 current artifact inventory and protocol; the retained canonical
artifact after any WEX-3.2 candidate. No additional tuning capacity is granted.
User-skipped WEX-7.1/WEX-8.1 are not prerequisites; unresolved WEX-6 reductions
remain unchecked and final qualification must report them honestly.
A rejected/deferred candidate does not prevent HTTP delivery of the unchanged
canonical artifact; preserve its exact disposition and all unfinished acceptance.
The serial controller must explicitly handle a blocked predecessor at a safe
checkpoint, never claim it complete or silently reorder a running worker.

Keep one canonical kernel/current format and unchanged capabilities, Unicode,
validation, typed errors, privacy, stable targeting, history and data recovery.
Core/Task hard caps remain 524,288 total / 32,768 JS gzip bytes; expanded-document-v1
remains 1,048,576 total / 131,072 JS. Count every distinct required lazy JS, worker,
glue, Wasm, CSS and asset once. Canonical gzip is level9; improved alternate gzip
or Brotli transfer does not excuse a failed canonical gate or change its metric.
Existing Brotli quality11 is the baseline, not a newly achieved saving.

Compression candidate work, including Zopfli settings, remains with WEX-3.1/3.2
in source02d and the same cumulative 45-minute/two-hypothesis policy. The current
authorizationGate records zero remaining tuning; this roadmap grants no renewal.
Do not turn HTTP validation into another experiment or repeat rejected unchanged
settings. Keep current Wasm/browser features, CSP, MIME, streaming and cache
identity contracts; a custom decoder/dictionary/ABI needs its existing separate
proposal and all required bytes counted. No native/device qualification, paid
inference, credentials, dogfood, publication, deployment or new runner.

Use existing bounded deterministic HTTP/load checks in task-owned ignored output.
WEX-4.1/4.2 own missing broader semantic/artifact negatives and final caps; WEX-5
owns remaining startup/first-use/input/memory observations. Reuse current proof.
Workers update only verified checkboxes/Status; progress holds exact input/artifact
pins, commands, nonzero executed/passed/failed/skipped counts and failures. Preserve
unrelated dirty/index contents. Stop exact owned test servers/browsers and clean
inactive reproducible output; unchanged failures retain an owner and resume condition.

## Tasks

### Task WEX-3.3 — Deliver standard production precompression safely

- [x] WEX-3.3 Wire and verify production gzip/Brotli negotiation on local artifacts.

Purpose: Ensure production clients receive the compression achieved by the build.
Deliverable: Existing build/fixture-server support for static compressed variants, cache identities and documented host configuration.
Context: WEX-3.1 baseline or WEX-3.2 retained artifact; `core/tests/browser-size-http.test.mjs`, existing HTTP size producer/server; verification compression contract and package assets.
Dependencies: none.
Independent work: this delivery task may use the unchanged baseline while WEX-3.2 candidates are rejected; source closure binds it to the final retained artifact identity without needless repeated checks.
Session scope: One build/HTTP delivery boundary, 30–45 minutes; no remote hosting, production access or provisioning.
Acceptance: Correct Content-Encoding, Vary: Accept-Encoding, JS/Wasm MIME, immutable asset identity and decompressed byte equality for gzip/Brotli/uncompressed responses; unsupported encodings fall back properly. If selected within the shared candidate allowance, Zopfli gzip works with the ordinary gzip decoder and reports both actual wire bytes and canonical gzip-9 budget bytes. Brotli quality 11 is the existing comparison baseline. Wasm initialization/streaming works under the existing contract. Build-time compression cost, actual transfer and cold/warm cache provenance are separate from decompressed memory/compile cost. Count required lazy assets and decoder costs if any; no unsupported custom compression shortcut.

Implementation:

- [x] WEX-3.3-I1 Extend existing static-artifact packaging and local server fixtures only as needed for the selected settings; keep source assets and source maps policy intact. Document host headers and uncompressed fallback from actual output.

Validation:

- [x] WEX-3.3-V1 Run affected existing HTTP negotiation/identity tests and one packed consumer Wasm initialization through the local fixture server. Budget: 5 minutes; record selectors/counts/headers and teardown. Reserve comprehensive negative controls for WEX-4.2.

Evidence: Artifact/compressor identities, focused header/byte/load results and server/browser teardown.
Handoff: Exact failed encoding/cache/streaming case and retained canonical artifact.
Blocked behavior: Delivery failure blocks its own closure; do not change canonical gzip accounting or deploy to test it.

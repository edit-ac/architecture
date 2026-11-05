# Qualify small-editor competitiveness

Status: IN_PROGRESS

Package-size amendment, 2026-10-28: bind all comparisons to the retained source
02a highlighting/grammar/Markdown/JS changes, source 02c core change and source
03 production artifacts. Reuse unchanged observations; fill only affected
startup/compile, first highlighting/math/Markdown use, memory and input/lifecycle
gaps. Source 02b's Deep Review is not performance proof. No additional tuning
allocation or repeated benchmark run follows from these source boundaries.

Progress: `.roadmap-runner/wasm-extensions-20261027/03a-small-editor-performance.progress.md`.
Entry: source 01/02 physical functionality and source 03 retained production
delivery are complete, with current artifact/semantic receipts. Consume WEX-1.2's
frozen objectives and WEX-2.7's work attribution/shared candidate ledger. Failed
bundle budgets or rejected optimizer candidates remain explicit, but do not block
collecting honest diagnostic comparisons when current artifacts function correctly.
Do not substitute fixture runtimes for production consumers or qualify failing caps.

This source belongs to the final testing/measurement phase, after all functionality.
Reuse `core/benchmarks/comparison/` and REL-1.2–1.4/FIT owners; no new harness.
Only missing comparator fixture/oracle coverage belongs here. One parent per
session, normally 30–45 minutes including checks. Split remaining long matrices
through the controller before exceeding scope. Reuse compatible current receipts
and run only affected/missing cells; a new session is not a rerun justification.
This is not another optimization allowance. Tuning waits for a new changed-input
hypothesis within the original shared cap, or a separately authorized decision.

Keep comparisons honest: vanilla DOM/basic text, ordinary rich text and durable/
collaborative classes have separate feature inventories. React host integration
is separate and follows supported official integration guidance. Pin compiler,
package/browser/network/hardware inputs, warmth/cache policy, sample count, order
and numerical objectives before execution. Preserve existing fixture identities,
source-only Git, mocked-only transports and native/IME/OS deferrals. No paid
inference, secrets, external provisioning, publication or deployment.

Workers update only verified checkboxes/Status; source/profile pins, commands,
executed/passed/failed/skipped counts, raw samples needed for active decisions,
gap/uncertainty and handoffs belong in ignored progress/output. Failures/skips
remain unchecked with owner, fingerprint, attempted repair and changed-input resume
condition. Stop unchanged retries, owned browsers/servers and inactive reproducible
session outputs. Do not claim p95 below 100 independent samples or p99 below 1,000;
small samples and missing observations remain inconclusive. Slower comparisons
are valid measured results, not proof of meeting latency or readiness targets.

## Tasks

### Task WEX-5.1 — Extend the existing comparator for tiny documents

- [x] WEX-5.1 Define fair small-editor profiles and missing comparator coverage.

Purpose: Compare real basic editors, not only 10-KiB documents or mismatched feature bundles.
Deliverable: Separately versioned deterministic empty, 128-byte one-paragraph and 1-KiB four-paragraph fixtures; explicit basic/rich/durable profiles and comparator assertions.
Context: WEX-1.2 objectives; `core/benchmarks/comparison/{corpus,shared,tiptap-base,tiptap-minimal,editac-task,contract.test}.mjs`, package lock and README; `architecture/specs/verification.md` browser comparison/latency sections; `architecture/research/small-editor-and-loading-methods-20261027.md` Why small editors need a separate performance track; official Tiptap performance guidance only where applicable.
Dependencies: none.
Independent work: startup/input cell inventories may be prepared; execution requires these validated fixtures/profiles.
Session scope: One comparator/fixture boundary, 30–45 minutes; no package version upgrade or production editor change.
Acceptance: Preserve existing Task/Long hashes and failed observations; tiny fixtures report exact UTF-8/UTF-16, blocks and independent text/schema oracles. Current tiptap-minimal is labeled StarterKit-based; add a genuinely basic supported text/paragraph/history profile with exact declared compatible dependencies. No unused expensive plugins or intentionally poor integration on either side. Separate bare-editing cost from edit.ac durability/history/authority obligations; comparable rich/durable profiles expose remaining differences. Resolve actual cache/endpoint and version/toolchain settings before timing, with targets frozen before viewing results.

Implementation:

- [x] WEX-5.1-I1 Extend existing corpus/profile definitions and contract tests with only missing tiny-document and artifact-union assertions. Use declared locked dependencies, competent public imports and supported empty admission; do not change real data or silently relabel earlier fixtures. Bind each comparison to its capability class and original REL owner.

Validation:

- [x] WEX-5.1-V1 Run the affected existing comparator contract tests and one tiny-profile correctness smoke per changed adapter, not a timing matrix. Budget: 5 minutes. Reject zero matches, false UTF-16 byte counts, invalid undo/history parity, hidden required assets and unsupported comparator settings.

Evidence: Fixture/profile hashes, capability table, frozen objectives, exact package versions and nonzero oracle/contract results.
Handoff: First unmeasured cell, mismatch or contract failure and exact next selector.
Blocked behavior: Invalid fixtures/capability mismatch blocks dependent timing claims; repair the specific owner, not the desired timing result.

### Task WEX-5.2 — Measure tiny-editor activation and lazy first use

- [ ] WEX-5.2 Collect comparable startup/readiness and feature-first-use observations.

Purpose: Prevent shell rendering, cache warmth or deferred work from hiding startup cost.
Deliverable: Existing comparator cells for empty/128-byte/1-KiB core and matched Tiptap configurations, plus selected first-use and shared-route observations.
Context: WEX-5.1 protocol/fixtures; `core/benchmarks/comparison/{browser,run,shared}.mjs` and current production artifacts; WEX-2.2 dependency-loading and WEX-3 delivery receipts; existing REL-1.3 cold/warm endpoints and resource accounting.
Dependencies: WEX-5.1.
Independent work: WEX-5.3 input/resource cells use the same fixtures and may be selected independently.
Session scope: One bounded startup comparison cell group, 30–45 minutes; controller splits additional browser/network/cache groups before closure if needed.
Acceptance: Separately report first visible content, actual accepted first edit and committed visible update. Cold includes actual module requests/decoding/compile/instantiate/document admission or restore/DOM adoption, rather than beginning after init. Distinguish no cache, HTTP cache, initialized shared module/compiled-Wasm reuse and optional service-worker cache. Count total required lazy resources and first use of selected command-lazy features. Attribute dependency waterfalls and start-function decompression if a packer was selected. A no-editor route requests no editor artifacts where supported; no offscreen/prefetch work disappears from the inventory. No activation path accepts lost/untracked input or pretends shell paint is editability. Report absolute targets, paired Tiptap ratios and uncertainty, including losses/inconclusive cells.

Implementation:

- [ ] WEX-5.2-I1 Add only missing startup endpoint/first-use/network accounting to the current harness, reusing HTTP and sharing controls. Execute frozen representative cells in controlled order; keep network/document-fixture preparation outside or inside timers only as the declared endpoint requires, with exclusions explicit.

Validation:

- [ ] WEX-5.2-V1 Run the selected startup/first-use cells with correctness oracles and frozen sample/order policy; record nonzero counts, raw observations needed to assess gaps, feature inventories and browser/server teardown. Budget: within session; insufficient tail samples remain inconclusive and cannot satisfy an outstanding p95/p99 gate.

Evidence: Per-stage startup, cache/request provenance, first-use stall, complete artifact union, paired gaps and target dispositions.
Handoff: Remaining exact cell/owner and required samples, or first demonstrated activation bottleneck with repair hypothesis.
Blocked behavior: Do not repeatedly rerun a slower or unchanged failed cell. Record quantified gap and source-bound owner; keep original cap/latency problems visible for WEX-4.3.

### Task WEX-5.3 — Measure input responsiveness and many-small-editor cost

- [ ] WEX-5.3 Collect matched input and lifecycle/resource observations.

Purpose: Determine whether fixed Wasm/CRDT/adapter costs are competitive in short fields.
Deliverable: Existing comparator input-to-visible, direct-route attribution and 1/10/50-editor resource cells with explicit competitive gaps.
Context: WEX-5.1 protocol/fixtures; WEX-2.7 work counters; current browser input/DOM and comparator drivers; `architecture/specs/verification.md` latency, extension-dispatch, multi-editor and lifecycle sections; REL-1.3/1.4 owners.
Dependencies: WEX-5.1.
Independent work: WEX-5.2 startup observations do not block these paired input/resource cells.
Session scope: One bounded input/resource cell group, 30–45 minutes; split remaining matrix cells through the controller rather than truncate their acceptance.
Acceptance: Measure real supported browser input through committed visible text, selection/formatting, undo and representative paste separately from command-to-layout microbenchmarks. Attribute JS/Wasm call/payload counts, JSON/snapshot/validation cost, changed DOM scope and UI subscriptions; no document-wide or unrelated-extension work is concealed. Test 1/10/50 small mounts, edit/destroy/reopen, peak/retained memory and observer/timer/provider/worker counts under frozen envelopes, preserving per-editor permissions and shared immutable assets. Reuse existing 0/1/10/100 unrelated-extension work controls rather than duplicate them. Compare competent minimal and matched rich/durable Tiptap classes, with absolute existing latency targets and uncertainty; synthetic browser input does not qualify native/IME/device behavior. Preserve required correctness and report measured losses/inconclusive states honestly.

Implementation:

- [ ] WEX-5.3-I1 Add only missing real-input/lifecycle observations to current drivers and execute the frozen risk-selected cells. Record startup/preparation exclusions, warmup/order, independent sample counts and remaining unsupported combinations. A single geometry read or synthetic command does not become input-to-photon proof.

Validation:

- [ ] WEX-5.3-V1 Run selected input/lifecycle cells with text/history/selection/resource oracles and nonzero counts; retain p50 and only statistically supported tails, paired gaps, memory plateau and teardown. Budget: within session. Bind existing matching work-count receipts instead of rerunning them without changed inputs.

Evidence: Current artifact/profile/input identities, end-to-end versus attributed costs, retained/peak memory, relative/absolute target dispositions and measured gap owners.
Handoff: Exact unmeasured cell, correctness defect or quantified performance gap and concrete bounded repair hypothesis.
Blocked behavior: Target misses stay PROBLEM under canonical REL/FIT ownership; a successfully measured loss is not a competitive pass. Do not weaken semantics, reset the tuning allowance, cherry-pick a slower competitor or claim a universal Tiptap win.

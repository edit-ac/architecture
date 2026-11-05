# Deliver the outstanding Code highlighting prerequisites

Status: COMPLETE

## Entry and ownership

User authority, 2026-10-28: unblock and resume the small-core plan, completing
related unfinished implementation first. This focused execution source owns the
original RCH-1.1–1.5 requirements from architecture/roadmaps/25-rich-content-extensions.md;
their IDs and acceptance are preserved below. Native UI/OS and unrelated rich
content parents are not prerequisites. Host Rust and actual production-Wasm
highlighting probes remain required for the browser Code capability.

Existing implementation is present in editac-highlighting and the browser code
scheduler/presenter. Inspect current inputs and existing receipt references in
architecture/decisions/highlighting-backend.md and architecture/specs/rich-content-extensions.md
before rebuilding or coding. Authenticate compatible passing proof; implement or
repair only remaining behavior. No task is completed by this controller adoption.
The worker must deliver source-bound current evidence or a concrete changed-input
blocker, not repeat the WEX loading-only proof as Code qualification.

Paths in task Context below are relative to core unless prefixed architecture/.
Run Cargo/npm commands from core with pinned toolchains. One parent per worker,
normally 15–45 minutes including its focused checks. Do not introduce a new
backend, grammar dependency, registry, replica, format or broad test harness.
The named original qualification checks are real production-admission gates;
reuse matching receipts and select only affected failures after repairs. No
full workspace/browser matrix is added. Further lifecycle coverage remains in
WEX-4.1; original RCH acceptance cannot be deferred or waived to promote Code.

Progress: .roadmap-runner/wasm-extensions-recovery-20261028/01-code-prerequisites.progress.md.
Workers change only verified checkboxes and Status. Store exact input pins,
commands, nonzero executed/passed/failed/skipped counts, prior failures, reuse
reason and handoff in this separate ignored progress/output, overriding older
canonical evidence-directory wording. Keep failure.inputPaths at most 128;
full pins belong in ignored evidence. Stop unchanged failed-input redispatch.

Preserve all unrelated dirty bytes/indexes, one current format and one guarded
serial root-main controller. Mocked/prepared automated services only; no paid
inference, credentials, provider calls, publication, deployment or OS qualification.
Clean only task-owned inactive generated outputs and temporary processes.

## Tasks

### Task RCH-1.1 — Map existing modules and feature gaps

- [x] RCH-1.1 Implement and validate map existing modules and feature gaps.

Purpose: Reuse qualified modules and freeze the exact additional feature boundaries.
Context: `crates/editac-core/src/modules/`; `packages/web/src/modules/`; `tests/rich-content-entry.test.mjs`; `../architecture/evidence/modules.md`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Each feature has an owning implementation, missing-behavior list and public port target; unchanged modules are reused and planned native/TUI wiring is assigned to roadmaps31–36.

Implementation:

- [x] RCH-1.1-I1 Map existing code-block, table, image, slash, reference and reorder symbols/evidence to this contract; create the focused entry fixture and record optional dependency ownership.

Validation:

- [x] RCH-1.1-V1 node --test tests/rich-content-entry.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.1` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.1`.
Blocked behavior: Leave `RCH-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.



### Task RCH-1.2 — Qualify a portable highlighting backend

- [x] RCH-1.2 Implement and validate qualify a portable highlighting backend.

Purpose: Select a bounded highlighting implementation from actual compilation and fixture evidence.
Context: `crates/editac-highlighting/Cargo.toml`; `crates/editac-highlighting/src/lib.rs`; `crates/editac-highlighting/tests/highlight_probe.rs`; `Cargo.toml`; `fixtures/highlighting/`; `../architecture/decisions/highlighting-backend.md`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: The selected backend and three-language envelope have reproducible native/WASM probes, source-preserving fallback and actual grammar/asset byte/timing evidence; unavailable targets are not qualified.

Implementation:

- [x] RCH-1.2-I1 Create the optional editac-highlighting companion for backend/runtime dependencies and probes; register its workspace manifest without making editac-core depend on it. Probe pinned Rust/TypeScript/JSON grammars and licenses; compare a browser-only alternative only for a recorded size/startup question. Keep runtime dependencies out of minimum SDK builds.

Validation:

- [x] RCH-1.2-V1 cargo test -p editac-highlighting --test highlight_probe --locked; cargo check -p editac-highlighting --target wasm32-unknown-unknown --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.2` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.2`.
Blocked behavior: Leave `RCH-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.



### Task RCH-1.3 — Implement revisioned token spans and cache invalidation

- [x] RCH-1.3 Implement and validate implement revisioned token spans and cache invalidation.

Purpose: Make syntax appearance a bounded projection of code text.
Context: `crates/editac-highlighting/src/`; `crates/editac-highlighting/tests/highlight_incremental.rs`; `crates/editac-core/src/modules/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: RCH-1.2.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Incremental and full recomputation agree for multiline comments/strings, Unicode and undo; stale/invalid spans reject, cache bounds hold, and tokenization emits no CRDT mutations. WCF-16: Instrument recomputed blocks/cache work and compare warm incremental output with cold recomputation across version-key changes, undo and stale completion; unrelated blocks reuse results without cross-session aliasing.

Implementation:

- [x] RCH-1.3-I1 Implement the token/cache port in editac-highlighting with block/revision/language/grammar identities, cancellation and validated offset conversion. Only small descriptor/offset/span contract types may be added to public engine types; backend code and dependencies remain in the companion, and token spans stay outside document state.

Validation:

- [x] RCH-1.3-V1 cargo test -p editac-highlighting --test highlight_incremental --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence. Execute the named WCF-16 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress entry `RCH-1.3` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.3`.
Blocked behavior: Leave `RCH-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.



### Task RCH-1.4 — Add a cancellable browser highlighting scheduler

- [x] RCH-1.4 Implement and validate add a cancellable browser highlighting scheduler.

Purpose: Move optional work off the input path while keeping state ownership in the engine.
Context: `packages/web/src/modules/code/scheduler.ts`; `packages/web/src/modules/code/worker.ts`; `tests/highlight-scheduler.test.mjs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.3.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Rapid edit/language/theme changes cannot publish stale spans; queues stay bounded, timeout yields plain source and disposal cancels owned worker/request state.

Implementation:

- [x] RCH-1.4-I1 Add lazy grammar initialization and a bounded optional worker adapter over immutable block inputs; coalesce superseded requests and record startup, transfer, work and application timing separately.

Validation:

- [x] RCH-1.4-V1 npm run build; node --test tests/highlight-scheduler.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.4` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.4`.
Blocked behavior: Leave `RCH-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.



### Task RCH-1.5 — Render code tokens without disturbing editing

- [x] RCH-1.5 Implement and validate render code tokens without disturbing editing.

Purpose: Preserve selection and IME while applying syntax appearance.
Context: `packages/web/src/modules/code/presenter.ts`; `tests/browser/code-highlight.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.4.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Code stays editable before highlighting resolves; text/selection survive recoloring, remote updates and composition; readonly and unknown-language fallbacks are honest and no full document rerender occurs.

Implementation:

- [x] RCH-1.5-I1 Patch validated token spans into the existing code-block presenter and expose language/fallback state; defer patches to the active composing subtree under the web input policy.

Validation:

- [x] RCH-1.5-V1 npm run test:browser -- code-highlight. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.5` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.5`.
Blocked behavior: Leave `RCH-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.

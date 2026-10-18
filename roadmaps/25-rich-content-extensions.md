# Deliver rich content extensions with bounded work

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [the owning contract](../specs/rich-content-extensions.md), [verification](../specs/verification.md) and the active task context. Paths are relative to `core` unless prefixed with `../architecture/`. Planned implementation/test files are created by their task. Source is controller-owned; write checkmarks, state and evidence only in the separate progress file.

Upstream entry gates: `05-markdown-content.md`, `07-extension-modules.md`, `12-client-contracts.md`, `13-change-diffs.md`, `21-extension-library.md` complete at current source revisions with passing artifact evidence. Dependencies below name only parents in this file. Do not launch implementation while an upstream gate is unavailable.

Reuse qualified roadmap07/21 implementations and shared client ownership. This track delivers portable/backend contracts and browser implementations; full native/TUI wiring belongs to roadmaps31–36 and is not a prerequisite. Any use of another future feature is through the owning typed contract and prepared fixtures until downstream integration.

## Execution rules

Each iteration implements at most one parent, including all its substeps. Target 15–45 minutes plus focused validation. Locate actual symbols before editing and reuse their owning implementation. If the boundary is larger, record the remaining acceptance and a precise controller split. Keep unmet prerequisites unchecked.

Create named checks before invoking them; missing tests and zero-case filters are failures. Capture full logs locally, then record exact commands/results, nonzero executed/passed/failed/skipped counts, fixture/artifact hashes and source/implementation revisions. Use prepared network/auth/media responses and deterministic local fixtures. No model/provider calls, real credentials, private-site probes, production writes, background runner startup or publication are authorized. Follow process/disk teardown in the verification contract.

## Epic RCH-1 — Deliver rich content extensions with bounded work


### Task RCH-1.1 — Map existing modules and feature gaps

- [ ] RCH-1.1 Implement and validate map existing modules and feature gaps.

Purpose: Reuse qualified modules and freeze the exact additional feature boundaries.
Context: `crates/editac-core/src/modules/`; `packages/web/src/modules/`; `tests/rich-content-entry.test.mjs`; `../architecture/evidence/modules.md`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Each feature has an owning implementation, missing-behavior list and public port target; unchanged modules are reused and planned native/TUI wiring is assigned to roadmaps31–36.

Implementation:

- [ ] RCH-1.1-I1 Map existing code-block, table, image, slash, reference and reorder symbols/evidence to this contract; create the focused entry fixture and record optional dependency ownership.

Validation:

- [ ] RCH-1.1-V1 node --test tests/rich-content-entry.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.1` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.1`.
Blocked behavior: Leave `RCH-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.2 — Qualify a portable highlighting backend

- [ ] RCH-1.2 Implement and validate qualify a portable highlighting backend.

Purpose: Select a bounded highlighting implementation from actual compilation and fixture evidence.
Context: `crates/editac-highlighting/Cargo.toml`; `crates/editac-highlighting/src/lib.rs`; `crates/editac-highlighting/tests/highlight_probe.rs`; `Cargo.toml`; `fixtures/highlighting/`; `../architecture/decisions/highlighting-backend.md`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: The selected backend and three-language envelope have reproducible native/WASM probes, source-preserving fallback and actual grammar/asset byte/timing evidence; unavailable targets are not qualified.

Implementation:

- [ ] RCH-1.2-I1 Create the optional editac-highlighting companion for backend/runtime dependencies and probes; register its workspace manifest without making editac-core depend on it. Probe pinned Rust/TypeScript/JSON grammars and licenses; compare a browser-only alternative only for a recorded size/startup question. Keep runtime dependencies out of minimum SDK builds.

Validation:

- [ ] RCH-1.2-V1 cargo test -p editac-highlighting --test highlight_probe --locked; cargo check -p editac-highlighting --target wasm32-unknown-unknown --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.2` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.2`.
Blocked behavior: Leave `RCH-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.3 — Implement revisioned token spans and cache invalidation

- [ ] RCH-1.3 Implement and validate implement revisioned token spans and cache invalidation.

Purpose: Make syntax appearance a bounded projection of code text.
Context: `crates/editac-highlighting/src/`; `crates/editac-highlighting/tests/highlight_incremental.rs`; `crates/editac-core/src/modules/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: RCH-1.2.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Incremental and full recomputation agree for multiline comments/strings, Unicode and undo; stale/invalid spans reject, cache bounds hold, and tokenization emits no CRDT mutations. WCF-16: Instrument recomputed blocks/cache work and compare warm incremental output with cold recomputation across version-key changes, undo and stale completion; unrelated blocks reuse results without cross-session aliasing.

Implementation:

- [ ] RCH-1.3-I1 Implement the token/cache port in editac-highlighting with block/revision/language/grammar identities, cancellation and validated offset conversion. Only small descriptor/offset/span contract types may be added to public engine types; backend code and dependencies remain in the companion, and token spans stay outside document state.

Validation:

- [ ] RCH-1.3-V1 cargo test -p editac-highlighting --test highlight_incremental --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence. Execute the named WCF-16 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress entry `RCH-1.3` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.3`.
Blocked behavior: Leave `RCH-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.4 — Add a cancellable browser highlighting scheduler

- [ ] RCH-1.4 Implement and validate add a cancellable browser highlighting scheduler.

Purpose: Move optional work off the input path while keeping state ownership in the engine.
Context: `packages/web/src/modules/code/scheduler.ts`; `packages/web/src/modules/code/worker.ts`; `tests/highlight-scheduler.test.mjs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.3.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Rapid edit/language/theme changes cannot publish stale spans; queues stay bounded, timeout yields plain source and disposal cancels owned worker/request state.

Implementation:

- [ ] RCH-1.4-I1 Add lazy grammar initialization and a bounded optional worker adapter over immutable block inputs; coalesce superseded requests and record startup, transfer, work and application timing separately.

Validation:

- [ ] RCH-1.4-V1 npm run build; node --test tests/highlight-scheduler.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.4` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.4`.
Blocked behavior: Leave `RCH-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.5 — Render code tokens without disturbing editing

- [ ] RCH-1.5 Implement and validate render code tokens without disturbing editing.

Purpose: Preserve selection and IME while applying syntax appearance.
Context: `packages/web/src/modules/code/presenter.ts`; `tests/browser/code-highlight.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.4.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Code stays editable before highlighting resolves; text/selection survive recoloring, remote updates and composition; readonly and unknown-language fallbacks are honest and no full document rerender occurs.

Implementation:

- [ ] RCH-1.5-I1 Patch validated token spans into the existing code-block presenter and expose language/fallback state; defer patches to the active composing subtree under the web input policy.

Validation:

- [ ] RCH-1.5-V1 npm run test:browser -- code-highlight. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.5` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.5`.
Blocked behavior: Leave `RCH-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.6 — Complete bounded table row and column commands

- [ ] RCH-1.6 Implement and validate complete bounded table row and column commands.

Purpose: Fill missing table shape operations using the existing schema.
Context: `crates/editac-core/src/modules/tables/`; `crates/editac-core/tests/table_shape.rs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`. [additional interaction cases](../tests/desktop-editing-cases.md). [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Row/column operations validate before mutation and form one undo group; concurrent shape/cell edits and deleted destinations converge under fixed fixtures without presenter repair writes. TBL-01–TBL-04 distinguish text/cell rectangles, clear-content versus structural delete, paste dimensions/protected ranges and gesture ownership; unsupported merges reject explicitly. WCF-08: Self-paste and already over-depth fragments reject before mutation under the existing simple-cell profile; subsequent copy/serialization/history/disposal remain bounded. No nested-table support is added.

Implementation:

- [ ] RCH-1.6-I1 Inventory existing row/column insert/remove behavior, implement only missing commands and define last-row/column outcomes; apply the frozen stable-identity and resource-limit policy.

Validation:

- [ ] RCH-1.6-V1 cargo test -p editac-core --test table_shape --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence. Execute the named WCF-08 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress entry `RCH-1.6` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.6`.
Blocked behavior: Leave `RCH-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.7 — Define header and alignment table attributes

- [ ] RCH-1.7 Implement and validate define header and alignment table attributes.

Purpose: Make table formatting semantics explicit and portable.
Context: `crates/editac-core/src/modules/tables/`; `crates/editac-core/tests/table_attributes.rs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.6.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Header/alignment changes round-trip under the declared Markdown profile, reject invalid values before mutation and preserve cell identities through undo and remote changes.

Implementation:

- [ ] RCH-1.7-I1 Add or qualify bounded header/alignment commands and supported attribute codecs, preserving unknown data and checking readonly and mixed selections.

Validation:

- [ ] RCH-1.7-V1 cargo test -p editac-core --test table_attributes --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.7` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.7`.
Blocked behavior: Leave `RCH-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.8 — Qualify cell selection and rectangular clipboard

- [ ] RCH-1.8 Implement and validate qualify cell selection and rectangular clipboard.

Purpose: Complete the existing cell interaction contract without a spreadsheet model.
Context: `packages/web/src/modules/tables/`; `tests/browser/table-selection.spec.ts`; `fixtures/tables/selection/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`. [additional interaction cases](../tests/desktop-editing-cases.md). [Wordcraft amendment](../evidence/wordcraft-research.md).
Dependencies: RCH-1.7.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Selection/navigation and rectangular paste preserve cell content and intended dimensions; illegal/oversized ranges and readonly targets fail safely with one paste history group. TBL-01–TBL-04 distinguish text/cell rectangles, clear-content versus structural delete, paste dimensions/protected ranges and gesture ownership; unsupported merges reject explicitly. The refined TBL-03/NCL-20 clipboard variants require declared row/column boundaries in HTML/TSV fallbacks; newline-only flattening into one cell is not success.

Implementation:

- [ ] RCH-1.8-I1 Reuse the table presenter to implement missing keyboard/cell-range copy/paste actions and explicit end-of-table behavior; route insertion through prepared shared commands.

Validation:

- [ ] RCH-1.8-V1 npm run test:browser -- table-selection. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.8` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.8`.
Blocked behavior: Leave `RCH-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.9 — Format only the selected Markdown table

- [ ] RCH-1.9 Implement and validate format only the selected markdown table.

Purpose: Provide a predictable source formatter without rewriting unrelated source.
Context: `crates/editac-markdown/src/table_format.rs`; `crates/editac-markdown/tests/table_format.rs`; `fixtures/tables/source/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.7.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Surrounding bytes are identical, escapes/code spans/empty cells survive, formatting is idempotent, stale baselines reject and undo restores original source bytes.

Implementation:

- [ ] RCH-1.9-I1 Use retained source spans/baseline and revision-checked reconciliation for deterministic pipe/alignment/padding formatting; declare Unicode display-width and final-newline rules.

Validation:

- [ ] RCH-1.9-V1 cargo test -p editac-markdown --test table_format --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.9` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.9`.
Blocked behavior: Leave `RCH-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.10 — Bound table invalidation and rendering work

- [ ] RCH-1.10 Implement and validate bound table invalidation and rendering work.

Purpose: Keep ordinary table edits local to their affected geometry and cells.
Context: `packages/web/src/modules/tables/`; `tests/browser/table-performance.spec.ts`; `fixtures/tables/performance/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: RCH-1.8, RCH-1.9.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A cell edit does not rebuild unrelated tables; input budgets, memory and touched-cell counts are recorded on fixed hardware, with stress limits honestly qualified and failed targets retained. WCF-15: Assert affected dependency sets and cache/measurement/update counts independently of timings; cold and warm results agree, unrelated tables stay untouched, and width/font/zoom changes invalidate only justified geometry.

Implementation:

- [ ] RCH-1.10-I1 Cache indexes/geometry per table with explicit invalidation counters; measure 20x10 interactive, 100x20 stress and many-unrelated-table fixtures in production builds.

Validation:

- [ ] RCH-1.10-V1 npm run test:browser -- table-performance. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence. Execute the named WCF-15 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress entry `RCH-1.10` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.10`.
Blocked behavior: Leave `RCH-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.11 — Expose stable attachment and asset descriptors

- [ ] RCH-1.11 Implement and validate expose stable attachment and asset descriptors.

Purpose: Separate shared asset identity from temporary access URLs.
Context: `crates/editac-core/src/modules/assets.rs`; `crates/editac-core/tests/asset_descriptors.rs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Descriptors validate atomically, preserve unknown source and never persist object URLs, credentials or expiring download URLs as stable identity; clean shared fixtures expose every state.

Implementation:

- [ ] RCH-1.11-I1 Define bounded file/image/media metadata, stable asset identity, safe fallback and local/queued/available/failed/missing/revoked/locked states through existing descriptors; define host asset port records.

Validation:

- [ ] RCH-1.11-V1 cargo test -p editac-core --test asset_descriptors --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.11` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.11`.
Blocked behavior: Leave `RCH-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.12 — Implement resumable host asset work and cache lifecycle

- [ ] RCH-1.12 Implement and validate implement resumable host asset work and cache lifecycle.

Purpose: Preserve local attachment work through offline and failure boundaries.
Context: `crates/editac-session/src/assets.rs`; `crates/editac-session/tests/asset_lifecycle.rs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.11.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Crash/full disk/auth expiry/canceled upload and deletion during upload preserve recovery without duplicate publish intent or node resurrection; shared binaries are not deleted by an unscoped editor action.

Implementation:

- [ ] RCH-1.12-I1 Connect host ingest/read/cache/publish/cancel ports to bounded journal/outbox intent records and idempotent host operation IDs; define asset versus document receipts and release-reference ownership.

Validation:

- [ ] RCH-1.12-V1 cargo test -p editac-session --test asset_lifecycle --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.12` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.12`.
Blocked behavior: Leave `RCH-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.13 — Bound image decoding and presenter resources

- [ ] RCH-1.13 Implement and validate bound image decoding and presenter resources.

Purpose: Extend existing image presentation with safe resource and offline behavior.
Context: `packages/web/src/modules/images/`; `tests/browser/image-lifecycle.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.12.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Malformed/huge/SVG/animated inputs follow documented policy, no unchecked URL fetch occurs, and repeated mount/dispose leaves no object URLs, requests or decoder ownership behind.

Implementation:

- [ ] RCH-1.13-I1 Add actual-media/dimension/pixel/encoded-byte/concurrent-decode policies, alt text and offline/locked/missing fallbacks; resolve URLs only through the authorized asset port and dispose resources.

Validation:

- [ ] RCH-1.13-V1 npm run test:browser -- image-lifecycle. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.13` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.13`.
Blocked behavior: Leave `RCH-1.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.14 — Render file attachments through authorized actions

- [ ] RCH-1.14 Implement and validate render file attachments through authorized actions.

Purpose: Make non-image assets accessible without embedding executable content.
Context: `packages/web/src/modules/attachments/`; `tests/browser/attachment-actions.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.12.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Offline/forbidden/locked files remain understandable, activation rechecks authority, source/clipboard preserves identity and no shell interpolation or automatic download is possible.

Implementation:

- [ ] RCH-1.14-I1 Render filename/status/size and explicit host-authorized open/download actions; implement copy/source fallback and portable action records for downstream native/TUI hosts. Treat PDFs as opaque attachments with optional host preview, not PDF import/OCR; PDF export is a separate output track and no PDF reader is required by core.

Validation:

- [ ] RCH-1.14-V1 npm run test:browser -- attachment-actions. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.14` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.14`.
Blocked behavior: Leave `RCH-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.15 — Add safe metadata cards and controlled embed activation

- [ ] RCH-1.15 Implement and validate add safe metadata cards and controlled embed activation.

Purpose: Keep passive link cards separate from active third-party content.
Context: `packages/web/src/modules/embeds/`; `tests/browser/controlled-embeds.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.11.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Raw provider HTML never enters the editor DOM; unauthorized/unsupported/offline embeds preserve a safe label, and no document-open/remote-update event activates or fetches an embed.

Implementation:

- [ ] RCH-1.15-I1 Use prepared host resolver outputs from the link-resolution port for safe cards; register bounded allowlisted presenter templates with explicit isolated/sandboxed activation and source fallback.

Validation:

- [ ] RCH-1.15-V1 npm run test:browser -- controlled-embeds. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.15` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.15`.
Blocked behavior: Leave `RCH-1.15` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.16 — Complete slash menu input and accessibility behavior

- [ ] RCH-1.16 Implement and validate complete slash menu input and accessibility behavior.

Purpose: Qualify the existing slash menu at catalog scale using the baseline interaction contract. Task-specific gate: INT-1.9 in roadmap 38 is complete with reviewed evidence; this does not block earlier independent rich-content tasks.
Context: `packages/web/src/modules/slash/`; `tests/browser/slash-context.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Only committed local context triggers the menu; escape/empty/error/cancel cases preserve focus/selection, one selected command has one history group and ready-runtime latency is measured.

Implementation:

- [ ] RCH-1.16-I1 Reuse INT-1.9 trigger, key, IME and composite-focus regressions from specs/editor-interactions.md; add bounded 500-command filtering, large-catalog pointer/touch actions and focus/screen-reader performance checks without creating a competing key policy.

Validation:

- [ ] RCH-1.16-V1 npm run test:browser -- slash-context. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.16` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.16`.
Blocked behavior: Leave `RCH-1.16` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.17 — Implement pointer reorder with non-drag alternatives

- [ ] RCH-1.17 Implement and validate implement pointer reorder with non-drag alternatives.

Purpose: Finish pointer interaction around the already qualified semantic move.
Context: `packages/web/src/modules/reorder/`; `tests/browser/reorder-pointer.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Hover emits no document update, final drop emits one semantic move/history group, concurrent/deleted targets retain content/selection and both keyboard and non-drag pointer paths work.

Implementation:

- [ ] RCH-1.17-I1 Add derived drag thresholds, bounded hit testing/auto-scroll, cancel/drop target revalidation and a clickable Move before/after or up/down alternative; retain keyboard movement and accessibility announcements.

Validation:

- [ ] RCH-1.17-V1 npm run test:browser -- reorder-pointer. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.17` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.17`.
Blocked behavior: Leave `RCH-1.17` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.18 — Expose custom reference presenter states

- [ ] RCH-1.18 Implement and validate expose custom reference presenter states.

Purpose: Make reference presentation consume host permission outcomes without copying private metadata.
Context: `packages/web/src/modules/references/`; `tests/browser/reference-presenters.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Custom bounded triggers preserve target identity, stale results cannot switch activation targets and private display fields remain outside shared CRDT labels unless explicit disclosure is authorized.

Implementation:

- [ ] RCH-1.18-I1 Reuse registered triggers and the shared resolver port for public/private/forbidden/missing/locked states, explicit activation and safe fallback; use prepared principal-scoped responses until roadmap26 is integrated.

Validation:

- [ ] RCH-1.18-V1 npm run test:browser -- reference-presenters. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.18` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.18`.
Blocked behavior: Leave `RCH-1.18` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.21 — Implement bounded document search and replacement

- [ ] RCH-1.21 Implement bounded document search and replacement.

Purpose: Implement bounded document search and replacement within the existing editor architecture.
Context: `packages/core/src/extensions/`; `packages/web/src/extensions/`; `tests/document-search.test.mjs`; `../architecture/specs/rich-content-extensions.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: RCH-1.1.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: FND-01–FND-07 pass logical-content search, stable selection scope, transient results, captured replacement targets and one-group bounded Replace All. Regex and unsupported structural matching remain explicit absent capabilities.

Implementation:

- [ ] RCH-1.21-I1 Use existing revision/anchor/command ports for a cancelable search provider and browser presenter. Qualify any missing compound replacement primitive upstream; publish portable command/result fixtures for native consumers.

Validation:

- [ ] RCH-1.21-V1 node --test tests/document-search.test.mjs. Test stale revisions, empty/over-limit queries, unmounted content, independent expected replacements, undo and focus; compare bounded work at several sizes. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `RCH-1.21` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `RCH-1.21`.
Blocked behavior: Leave `RCH-1.21` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task RCH-1.22 — Add explicit code editing convenience commands

- [ ] RCH-1.22 Add explicit code editing convenience commands.

Purpose: Add explicit code editing convenience commands within the existing editor architecture.
Context: `packages/core/src/extensions/`; `packages/web/src/extensions/`; `tests/code-commands.test.mjs`; `../architecture/specs/rich-content-extensions.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: RCH-1.5.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: IDE-01–IDE-06 pass logical-line move/duplicate, indent, surround, declared language comments and opt-in pairing with preserved whitespace, selection and history. No implicit prose line-cut, multi-cursor or cross-block mutation.

Implementation:

- [ ] RCH-1.22-I1 Reuse code-context applicability and prepared commands; provide visible actions and optional remappable bindings. Keep auto-pair policy separate and composition-safe.

Validation:

- [ ] RCH-1.22-V1 node --test tests/code-commands.test.mjs. Assert exact LF/EOF, endpoint exclusion, one undo group and no-op/reject states; replay composition/paste/correction and native focus escape. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `RCH-1.22` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `RCH-1.22`.
Blocked behavior: Leave `RCH-1.22` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task RCH-1.23 — Preserve formatting inside tables and other rich extensions

- [ ] RCH-1.23 Preserve formatting inside tables and other rich extensions.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `packages/web/src/modules/tables/`; `tests/browser/extension-formatting.spec.ts`; `fixtures/rich-presenters/formatting/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/extension-library.md`
Dependencies: RCH-1.8, RCH-1.11, RCH-1.18.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Table cells admit the declared inline/block formatting palette, retain styles through row/column edits, rectangular copy/paste and undo, and expose scoped formatting commands. Image/file captions, references, math and other registered inline/block extensions preserve admitted formatting and source data. Unsupported styles/codecs have explicit inert fallback; literal paste remains optional and bypasses rich transformation.

Implementation:

- [ ] RCH-1.23-I1 Implement EXT-1.13 capabilities in portable/web rich presenters. Author mixed cell-range fixtures for bold/italic/underline/strike/code/link/headings/lists, header/alignment metadata, marked captions and inline extensions. Test selection direction, inaccessible or unavailable codecs, readonly, delayed preparation, format precedence, one atomic undo group and import/export round-trips; do not execute table formulas or document-supplied code.

Validation:

- [ ] RCH-1.23-V1 `npm run test:browser -- extension-formatting`. Require each admitted formatting/extension combination, negative unsupported cases and exact semantic/history/storage effects. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing required runtime tooling, failed behavior or untested mandatory cases do not qualify support; use accepted virtual runtimes/equivalents when physical hardware is unavailable.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Accept target-platform simulators/emulators/VMs under verification.md and retain virtual provenance; never relabel their results as physical-device observations.

### Task RCH-1.19 — Publish per-feature portable presenter contracts

- [ ] RCH-1.19 Implement and validate publish per-feature portable presenter contracts.

Purpose: Give downstream native/TUI work concrete feature APIs and fixtures.
Context: `packages/core/`; `packages/web/package.json`; `tests/rich-presenter-contracts.test.mjs`; `fixtures/rich-presenters/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.5, RCH-1.10, RCH-1.13, RCH-1.14, RCH-1.15, RCH-1.16, RCH-1.17, RCH-1.18, RCH-1.21, RCH-1.22, RCH-1.23.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Clean public consumers need no private paths; Swift/Kotlin/desktop/terminal records define lifecycle/focus/selection/cancel/accessibility obligations and every feature has explicit preservation/view/edit capabilities for roadmaps31–36. Publish search/code command, selection, scope and fallback contracts with exact first-party profile identities for native/terminal consumers.

Implementation:

- [ ] RCH-1.19-I1 Export versioned code-token, table-selection/commands, asset, embed, menu, reference and reorder records/actions through owning packages/crates; extend capability schema and headless presenter conformance.

Validation:

- [ ] RCH-1.19-V1 npm run build; node --test tests/rich-presenter-contracts.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.19` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.19`.
Blocked behavior: Leave `RCH-1.19` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task RCH-1.20 — Qualify rich-content performance and integration handoff

- [ ] RCH-1.20 Implement and validate qualify rich-content performance and integration handoff.

Purpose: Publish measured portable/web evidence without implying native implementation.
Context: `tests/rich-content-performance.test.mjs`; `tests/rich-content-bundles.test.mjs`; `../architecture/evidence/rich-content.md`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: RCH-1.19.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Every advertised portable/web feature has nonzero passing fixtures, exact artifacts and honest performance envelope; disabled assets issue zero requests, failures remain visible and no native/TUI parity is inferred. Task-specific evidence gates: current INT-1.16 selected-text-drag qualification and RGS-1.8 shared-driver handoff must exist before this combined qualification runs; keep the task blocked if either is missing, without implementing their behavior here. Qualify FND/IDE/TBL and actual FPX mixed-feature variants; PRF-01–PRF-06 compare supported presets with baseline at fixed workloads, including continuous drag and resource teardown. Feature absence is distinct from a passed optional test.

Implementation:

- [ ] RCH-1.20-I1 Run the contract corpus and aggregate cold/warm timings, size/token/DOM/memory counters and disposal; verify optional-disabled packed consumers and record exact platform-wiring obligations for roadmaps31–36.

Validation:

- [ ] RCH-1.20-V1 node --test tests/rich-content-performance.test.mjs tests/rich-content-bundles.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.20` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.20`.
Blocked behavior: Leave `RCH-1.20` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.

## AI epic entry conditions and execution rules

The AI extension is included in this existing content-extension roadmap. All former AI parents are retained as RCH-2.1–RCH-2.14; their implementation state remains in separate progress/evidence. Existing RCH-1 tasks retain their entry gates and ownership. The AI epic additionally requires `08-sdk-integration.md`, `38-editor-interactions.md` and `40-mobile-web.md` at reviewed qualified revisions before any RCH-2 implementation; its former `13-change-diffs.md` and `21-extension-library.md` gates are already whole-track prerequisites. Native/TUI/docs requirements remain attached to their own tasks. Do not add those downstream platform gates to the manifest's whole-track entry conditions.

Read [the AI contract](../specs/ai-extensions.md) and [SDK evaluation](../evidence/ai-extension-research.md#vercel-ai-sdk-evaluation-and-default-decision). Vercel AI SDK Core is the default TypeScript host/backend adapter behind a portable transport, while the extension is optional for editor consumers. AI native/terminal presenters are owned by this epic; existing non-AI rich-content platform wiring remains in 31–36. The initial browser release has no roadmap-25 prerequisite. Expanded consumers that require all of roadmap 25 also require this AI epic; this consolidation does not claim otherwise or mark pending platforms complete.

One iteration implements at most one bounded parent; controller-review any necessary stable split without dropping acceptance. New suites and runner routes are created by their tasks. Preserve failed/skipped evidence, distinguish deterministic, device and evidence-validator counts, and stop task-owned browsers/servers/transports in teardown. Missing one device cannot block another dependency-ready task or invalidate the separately qualified web subset, but does block an all-platform support claim.

Automated validation uses prepared responses and mocked provider transports only: no inference calls, ambient credentials, `.secrets`, subscription proxies or automatic fixture recording. No dogfood is authorized. Before any future AI test/dogfood change or run, read the Assign workspace architecture/operations/paid-inference-testing-policy.md; manual live-content dogfood also requires user-approved exact content, a hard request/monetary cap and a stop condition before any call. Device/accessibility mechanics use a mock backend and prove no model quality or settlement.

## Epic RCH-2 — Deliver optional AI writing through existing edit contracts

### Task RCH-2.1 — Define the portable AI descriptor and host transport

- [ ] RCH-2.1 Define the portable AI descriptor and host transport.

Purpose: Freeze a versioned optional command/transport envelope before clients depend on it.
Context: `packages/core/src/extensions/ai.ts`; `crates/editac-core/src/extensions/ai.rs`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: Registration names Ask AI, fill/continue, rewrite and completion capabilities with bounded context/response, cancellation and host quota admission. Disabled/unconfigured services send zero requests; credentials stay host-owned and no new persisted schema or mandatory provider dependency is added. The portable transport supports the default Vercel AI SDK Core host/backend adapter without leaking SDK types into engine/native contracts.

Implementation:

- [ ] RCH-2.1-I1 Create typed operation/request/response/status envelopes, capability declarations and prepared valid/invalid fixtures. Reuse existing descriptor, anchor and host-policy primitives; declare request/time/output caps and protected-document rejection. Specify the default Vercel AI SDK Core adapter mapping for generation/stream chunks, abort/errors and usage metadata while keeping the public envelope SDK-independent.

Validation:

- [ ] RCH-2.1-V1 `cargo test -p editac-core --test ai_extension_contract --locked`. Create the named suite; test absent/disabled registration, invalid versions, missing transport/limits, quota exhaustion, forbidden context, format rejection and unchanged document/history state. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.1` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.2 — Implement the shared AI proposal session lifecycle

- [ ] RCH-2.2 Implement the shared AI proposal session lifecycle.

Purpose: Keep asynchronous output separate from authoritative edits.
Context: `packages/core/src/extensions/ai-session.ts`; `crates/editac-core/tests/ai_extension_session.rs`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.1.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: Streaming remains ephemeral. Captured targets and relevant context revisions are checked on acceptance; stale/late/duplicate results cannot edit another target. Accept commits once through existing prepared semantics and one undo group; cancellation, failure and disposal leave document/history unchanged.

Implementation:

- [ ] RCH-2.2-I1 Implement bounded stream assembly, session/epoch generations, prepared proposal review, cancellation and explicit recovery-copy state. Consume the existing change-review and anchor services instead of adding a patch engine.

Validation:

- [ ] RCH-2.2-V1 `cargo test -p editac-core --test ai_extension_session --locked`. Create the named suite; inject duplicate/out-of-order chunks, malformed/oversized output, timeout, remote insert/delete, changed context, permission loss, read-only, switch/dispose and accept/undo/redo. Assert content, selection, origin/history and resource release. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.2` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.3 — Add Ask AI and fill or continue text on the web

- [ ] RCH-2.3 Add Ask AI and fill or continue text on the web.

Purpose: Deliver explicit prompt and generation flows with reviewable targets.
Context: `packages/web/src/extensions/ai/actions.ts`; `packages/web/tests/ai-actions.test.ts`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: A visible command, selection control and slash route invoke Ask AI or fill/continue with an explicit context scope. Ask AI answers do not edit by default; fill/continue capture caret, block or selection and require reviewed insertion/replacement. Keyboard and touch users can stop, reject, accept or regenerate without losing the target.

Implementation:

- [ ] RCH-2.3-I1 Build the prompt, answer and proposal presenters using the shared session. Add bounded mock responses for empty blocks, selected replacements, continuing text and answers; show unavailable/failed/stale states and new-request limits for regeneration.

Validation:

- [ ] RCH-2.3-V1 `npm run test:web -- ai-actions`. Create the named web suite and its runner route; exercise focus changes, no-selection/selection/empty-block targets, answer-only behavior, Unicode/RTL, safe formatted responses, cancellation and request counts. Record actual keyboard/screen-reader/touch mechanics separately with a mock backend. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.3` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.4 — Add opt-in autocomplete while writing

- [ ] RCH-2.4 Add opt-in autocomplete while writing.

Purpose: Offer bounded transient writing suggestions without disturbing text input.
Context: `packages/web/src/extensions/ai/completion.ts`; `packages/web/tests/ai-completion.test.ts`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.3.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: Completion is disabled by default and only starts after host quota/context configuration. Debounce and one current request prevent request storms. The initial default backend uses a short bounded SDK generateText response; streamed ghost text requires separate measured justification. Ghost text never enters offsets, copying, export, history or CRDT state until accepted. IME/marked text and excluded contexts suspend requests; stale suggestions are invalidated.

Implementation:

- [ ] RCH-2.4-I1 Implement manual and debounced completion, cancellation on superseding edits, bounded ghost-text rendering and configurable acceptance. Preserve Tab indent/table navigation without a valid suggestion; provide visible mobile/accessibility Accept/Dismiss and Escape dismissal.

Validation:

- [ ] RCH-2.4-V1 `npm run test:web -- ai-completion`. Create the suite and runner route with a fixed clock and mock transport. Assert exact request counts under rapid typing, IME/dictation, selection/caret/remote changes, blur, caps, disposal, code/atom exclusions and accept/undo. Test no ghost-text persistence and actual keyboard/touch/AT behavior independently. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.4` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.5 — Publish the initial selected-text AI command profile

- [ ] RCH-2.5 Publish the initial selected-text AI command profile.

Purpose: Reuse the proposal flow for common writing actions.
Context: `packages/core/src/extensions/ai-actions.ts`; `packages/web/tests/ai-transformations.test.ts`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.3.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The profile includes spelling/grammar, rephrase, simplify, shorten, extend, tone, summarize/key points and explicit-language translation. Each action declares scope and output format, preserves supported marks/atoms and reports unsupported structure. No action applies automatically or claims model accuracy from prepared responses.

Implementation:

- [ ] RCH-2.5-I1 Define deterministic command/prompt metadata and applicability over the shared envelope; provide language/tone controls and one review surface. Add prepared action results, invalid rich content and protected-atom cases rather than making provider calls.

Validation:

- [ ] RCH-2.5-V1 `npm run test:web -- ai-transformations`. Create the suite and route; test every declared command, selected and unavailable targets, missing language, unsafe output, supported format retention, read-only/stale rejection and accept/undo with unrelated remote edits. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.5` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.6 — Qualify the optional web AI profile and packed consumer

- [ ] RCH-2.6 Qualify the optional web AI profile and packed consumer.

Purpose: Prove the supported browser subset and disabled-feature costs.
Context: `packages/web/examples/ai/`; `packages/web/tests/ai-consumer.test.ts`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.4, RCH-2.5, RCH-1.20.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: An immutable packed consumer runs the declared AI profile using a mock backend with no client secret or ambient credential discovery. Implement and qualify the default Vercel AI SDK Core backend adapter using pinned stable versions and prepared mock models; incompatible runtime/API behavior blocks its support claim. The adapter must propagate host cancellation, disable automatic retries and obey pre-dispatch quotas through the portable envelope. Default bundles omit AI assets/listeners/requests. The declared desktop/mobile browser and accessibility combinations have actual mechanics evidence; prepared outputs prove integration only.

Implementation:

- [ ] RCH-2.6-I1 Add the versioned optional AI preset through existing exports and configuration precedence. Implement the default Vercel AI SDK Core backend/reference route with pinned stable dependencies and mock models, explicit provider/model injection, abort propagation, zero automatic retries and no tool/agent loops. Use streamText for Ask AI/fill previews and bounded generateText for initial autocomplete; keep SDK types private to the host adapter. Exercise minimal, document-tools, table/link and collaboration combinations; record bundle/resource deltas and capability limitations.

Validation:

- [ ] RCH-2.6-V1 `npm run test:web -- ai-consumer`. Create the suite and runner route. Check packed imports, conflicting keymaps, disable/re-enable, bounded streams, quota admission, protected-context refusal and teardown. For the default SDK adapter, use prepared mock models/simulated streams to assert abort propagation, finish/error mapping and exact request counts with retries disabled; preserve compatibility failures. Measure disabled/enabled contributions and record actual desktop/mobile keyboard/touch/screen-reader results with the mock backend. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.6` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.7 — Integrate the AI presenter in iOS

- [ ] RCH-2.7 Integrate the AI presenter in iOS.

Purpose: Deliver an independent iOS presenter through qualified native commands.
Context: `native/ios/extensions/ai/`; `native/ios/tests/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.5.
Task-specific entry gate: `16-ios-sdk.md` complete at its reviewed implementation/profile revision with passing artifacts; this applies only to this task and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The iOS consumer exposes its declared Ask AI/fill/rewrite and completion subset using captured native selection, UI-thread dispatch and platform accessibility. Unsupported inline completion has an explicit command fallback. Native marked text, navigation, read-only, remote edits and OS writing tools retain their existing owners.

Implementation:

- [ ] RCH-2.7-I1 Wire the shared transport/session into the native command and proposal presenters. Use prepared responses and qualified native text controls; add visible accept/reject/stop/status, language/tone options and a capability declaration without installing a provider.

Validation:

- [ ] RCH-2.7-V1 `bash native/ios/scripts/check.sh ai-extension`. Create the named deterministic check route. Test focus/marked-text changes, stale/duplicate results, cancellation, quota limits, protected targets, accept/undo/redo and teardown; record actual OS/device, keyboard and accessibility evidence with the mock backend. Missing required platform evidence stays unqualified. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.7` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.8 — Integrate the AI presenter in Android

- [ ] RCH-2.8 Integrate the AI presenter in Android.

Purpose: Deliver an independent Android presenter through qualified native commands.
Context: `native/android/extensions/ai/`; `native/android/tests/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.5.
Task-specific entry gate: `17-android-sdk.md` complete at its reviewed implementation/profile revision with passing artifacts; this applies only to this task and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The Android consumer exposes its declared Ask AI/fill/rewrite and completion subset using captured native selection, UI-thread dispatch and platform accessibility. Unsupported inline completion has an explicit command fallback. Native marked text, navigation, read-only, remote edits and OS writing tools retain their existing owners.

Implementation:

- [ ] RCH-2.8-I1 Wire the shared transport/session into the native command and proposal presenters. Use prepared responses and qualified native text controls; add visible accept/reject/stop/status, language/tone options and a capability declaration without installing a provider.

Validation:

- [ ] RCH-2.8-V1 `bash native/android/scripts/check.sh ai-extension`. Create the named deterministic check route. Test focus/marked-text changes, stale/duplicate results, cancellation, quota limits, protected targets, accept/undo/redo and teardown; record actual OS/device, keyboard and accessibility evidence with the mock backend. Missing required platform evidence stays unqualified. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.8` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.9 — Integrate the AI presenter in macOS

- [ ] RCH-2.9 Integrate the AI presenter in macOS.

Purpose: Deliver an independent macOS presenter through qualified native commands.
Context: `native/macos/extensions/ai/`; `native/macos/tests/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.5.
Task-specific entry gate: `18-desktop-native.md` complete at its reviewed implementation/profile revision with passing artifacts; this applies only to this task and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The macOS consumer exposes its declared Ask AI/fill/rewrite and completion subset using captured native selection, UI-thread dispatch and platform accessibility. Unsupported inline completion has an explicit command fallback. Native marked text, navigation, read-only, remote edits and OS writing tools retain their existing owners.

Implementation:

- [ ] RCH-2.9-I1 Wire the shared transport/session into the native command and proposal presenters. Use prepared responses and qualified native text controls; add visible accept/reject/stop/status, language/tone options and a capability declaration without installing a provider.

Validation:

- [ ] RCH-2.9-V1 `bash native/macos/scripts/check.sh ai-extension`. Create the named deterministic check route. Test focus/marked-text changes, stale/duplicate results, cancellation, quota limits, protected targets, accept/undo/redo and teardown; record actual OS/device, keyboard and accessibility evidence with the mock backend. Missing required platform evidence stays unqualified. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.9` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.10 — Integrate the AI presenter in Windows

- [ ] RCH-2.10 Integrate the AI presenter in Windows.

Purpose: Deliver an independent Windows presenter through qualified native commands.
Context: `native/windows/extensions/ai/`; `native/windows/tests/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.5.
Task-specific entry gate: `22-windows-native.md` complete at its reviewed implementation/profile revision with passing artifacts; this applies only to this task and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The Windows consumer exposes its declared Ask AI/fill/rewrite and completion subset using captured native selection, UI-thread dispatch and platform accessibility. Unsupported inline completion has an explicit command fallback. Native marked text, navigation, read-only, remote edits and OS writing tools retain their existing owners.

Implementation:

- [ ] RCH-2.10-I1 Wire the shared transport/session into the native command and proposal presenters. Use prepared responses and qualified native text controls; add visible accept/reject/stop/status, language/tone options and a capability declaration without installing a provider.

Validation:

- [ ] RCH-2.10-V1 `bash native/windows/scripts/check.sh ai-extension`. Create the named deterministic check route. Test focus/marked-text changes, stale/duplicate results, cancellation, quota limits, protected targets, accept/undo/redo and teardown; record actual OS/device, keyboard and accessibility evidence with the mock backend. Missing required platform evidence stays unqualified. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.10` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.11 — Integrate the AI presenter in Linux

- [ ] RCH-2.11 Integrate the AI presenter in Linux.

Purpose: Deliver an independent Linux presenter through qualified native commands.
Context: `native/linux/extensions/ai/`; `native/linux/tests/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.5.
Task-specific entry gate: `23-linux-native.md` complete at its reviewed implementation/profile revision with passing artifacts; this applies only to this task and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The Linux consumer exposes its declared Ask AI/fill/rewrite and completion subset using captured native selection, UI-thread dispatch and platform accessibility. Unsupported inline completion has an explicit command fallback. Native marked text, navigation, read-only, remote edits and OS writing tools retain their existing owners.

Implementation:

- [ ] RCH-2.11-I1 Wire the shared transport/session into the native command and proposal presenters. Use prepared responses and qualified native text controls; add visible accept/reject/stop/status, language/tone options and a capability declaration without installing a provider.

Validation:

- [ ] RCH-2.11-V1 `bash native/linux/scripts/check.sh ai-extension`. Create the named deterministic check route. Test focus/marked-text changes, stale/duplicate results, cancellation, quota limits, protected targets, accept/undo/redo and teardown; record actual OS/device, keyboard and accessibility evidence with the mock backend. Missing required platform evidence stays unqualified. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.11` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.12 — Add the terminal AI command and review fallback

- [ ] RCH-2.12 Add the terminal AI command and review fallback.

Purpose: Expose writing actions without requiring an inline visual surface.
Context: `../cli/src/tui/extensions/ai.rs`; `../cli/tests/ai_extension.rs`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.2, RCH-2.5.
Task-specific entry gate: `15-tui-client.md` complete at its reviewed implementation/profile revision with passing artifacts; this applies only to this task and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: The terminal provides explicit Ask AI/fill/rewrite commands, bounded text review/status and accept/reject/stop. Completion can be a manual proposal; no printable-key interception, ANSI-only status or background provider request is required. Baseline local/offline editing works without AI.

Implementation:

- [ ] RCH-2.12-I1 Integrate the shared session and host capability through qualified TUI editing/review; create prepared response fixtures and capability limits for the supported terminal/screen-reader combinations.

Validation:

- [ ] RCH-2.12-V1 `From ../cli: cargo test --test ai_extension --locked`. Create the named CLI suite; test Unicode targets, stale proposals, read-only/offline state, quotas, cancellation, safe output, accept/undo and resource disposal. Record actual terminal/accessibility mechanics independently with mock responses. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.12` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.13 — Qualify declared AI platform and feature combinations

- [ ] RCH-2.13 Qualify declared AI platform and feature combinations.

Purpose: Consolidate actual platform support without equating mock results with model quality.
Context: `tests/ai-extensions/`; `packages/web/examples/ai/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.6, RCH-2.7, RCH-2.8, RCH-2.9, RCH-2.10, RCH-2.11, RCH-2.12.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: A versioned matrix distinguishes each implemented, unsupported and pending platform/action. Every claimed combination has immutable deterministic and actual input/accessibility receipts. Web subset evidence from RCH-2.6 remains independently usable; this task cannot claim all-platform readiness while required native evidence is missing.

Implementation:

- [ ] RCH-2.13-I1 Assemble immutable consumers and recorded browser/native/terminal artifacts. Exercise high-risk selection/composition/collaboration/protected-content and rich-extension boundaries for every claimed subset; preserve failures and separate provider-quality evidence as absent.

Validation:

- [ ] RCH-2.13-V1 `npm run test:web -- ai-matrix`. Create the matrix/receipt check route; reject missing platform receipts, inconsistent capability declarations and prepared responses labeled as model-quality/live-usage evidence. Required skipped combinations block the corresponding support claim. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.13` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task RCH-2.14 — Document AI commands and mock-backed integration recipes

- [ ] RCH-2.14 Document AI commands and mock-backed integration recipes.

Purpose: Make the qualified first-party profile consumable without spending inference credits.
Context: `../docs/content/docs/extensions/ai/`; `packages/web/examples/ai/`; [AI contract](../specs/ai-extensions.md); [extension library](../specs/extension-library.md); [change review](../specs/change-diffs.md).
Dependencies: RCH-2.6.
Task-specific entry gate: The documentation bootstrap and build conventions from `29-public-docs-demo.md` are qualified at a reviewed revision. This task does not wait for that track's unrelated deployment or full-platform examples; platform support labels require their corresponding AI receipts.
Session scope: One named boundary, normally 15–45 minutes plus focused validation; controller-review any necessary stable split while preserving acceptance.
Acceptance: Documentation explains Ask AI, fill/continue, selected actions, autocomplete, context scopes, review/cancel, quotas and host-owned transports with a runnable prepared-response example. Supported platform subsets follow actual receipts; privacy, unsupported behavior and unknown cost are explicit. Optional AI adds no baseline release requirement.

Implementation:

- [ ] RCH-2.14-I1 Add versioned public recipes and the capability table through the existing docs/demo owners. Use the packed mock consumer, show provider-neutral backend wiring plus the default Vercel AI SDK Core backend adapter recipe with pinned versions and prepared results, and distinguish subsequent feature suggestions from committed scope. Explain cancellation propagation, disabled retries, explicit provider selection and host quotas.

Validation:

- [ ] RCH-2.14-V1 `From ../docs: npm run build`. Build docs with no inference/network-provider calls; verify example imports against the qualified packed consumer, command/capability links and absent/pending platform labels. Do not publish/deploy or start a live provider demo. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes. All provider results are prepared; no inference call is permitted.

Evidence: Separate progress entry `RCH-2.14` links changed paths and focused immutable artifacts; preserve failed evidence and label physical or virtual platform versus mocked results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `RCH-2.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

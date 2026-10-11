# Deliver rich content extensions with bounded work

Status: IN_PROGRESS

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
Context: `crates/editac-highlighting/src/`; `crates/editac-highlighting/tests/highlight_incremental.rs`; `crates/editac-core/src/modules/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.2.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Incremental and full recomputation agree for multiline comments/strings, Unicode and undo; stale/invalid spans reject, cache bounds hold, and tokenization emits no CRDT mutations.

Implementation:

- [ ] RCH-1.3-I1 Implement the token/cache port in editac-highlighting with block/revision/language/grammar identities, cancellation and validated offset conversion. Only small descriptor/offset/span contract types may be added to public engine types; backend code and dependencies remain in the companion, and token spans stay outside document state.

Validation:

- [ ] RCH-1.3-V1 cargo test -p editac-highlighting --test highlight_incremental --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

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
Context: `crates/editac-core/src/modules/tables/`; `crates/editac-core/tests/table_shape.rs`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Row/column operations validate before mutation and form one undo group; concurrent shape/cell edits and deleted destinations converge under fixed fixtures without presenter repair writes.

Implementation:

- [ ] RCH-1.6-I1 Inventory existing row/column insert/remove behavior, implement only missing commands and define last-row/column outcomes; apply the frozen stable-identity and resource-limit policy.

Validation:

- [ ] RCH-1.6-V1 cargo test -p editac-core --test table_shape --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

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
Context: `packages/web/src/modules/tables/`; `tests/browser/table-selection.spec.ts`; `fixtures/tables/selection/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.7.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Selection/navigation and rectangular paste preserve cell content and intended dimensions; illegal/oversized ranges and readonly targets fail safely with one paste history group.

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
Context: `packages/web/src/modules/tables/`; `tests/browser/table-performance.spec.ts`; `fixtures/tables/performance/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.8, RCH-1.9.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A cell edit does not rebuild unrelated tables; input budgets, memory and touched-cell counts are recorded on fixed hardware, with stress limits honestly qualified and failed targets retained.

Implementation:

- [ ] RCH-1.10-I1 Cache indexes/geometry per table with explicit invalidation counters; measure 20x10 interactive, 100x20 stress and many-unrelated-table fixtures in production builds.

Validation:

- [ ] RCH-1.10-V1 npm run test:browser -- table-performance. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

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

Purpose: Qualify the existing slash menu under realistic editor input states.
Context: `packages/web/src/modules/slash/`; `tests/browser/slash-context.spec.ts`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Only committed local context triggers the menu; escape/empty/error/cancel cases preserve focus/selection, one selected command has one history group and ready-runtime latency is measured.

Implementation:

- [ ] RCH-1.16-I1 Add missing code/literal/context exclusions, IME/selection handling, bounded 500-command filtering, pointer/touch actions, focus restoration and screen-reader states.

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


### Task RCH-1.19 — Publish per-feature portable presenter contracts

- [ ] RCH-1.19 Implement and validate publish per-feature portable presenter contracts.

Purpose: Give downstream native/TUI work concrete feature APIs and fixtures.
Context: `packages/core/`; `packages/web/package.json`; `tests/rich-presenter-contracts.test.mjs`; `fixtures/rich-presenters/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.5, RCH-1.10, RCH-1.13, RCH-1.14, RCH-1.15, RCH-1.16, RCH-1.17, RCH-1.18.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Clean public consumers need no private paths; Swift/Kotlin/desktop/terminal records define lifecycle/focus/selection/cancel/accessibility obligations and every feature has explicit preservation/view/edit capabilities for roadmaps31–36.

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
Context: `tests/rich-content-performance.test.mjs`; `tests/rich-content-bundles.test.mjs`; `../architecture/evidence/rich-content.md`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/verification.md`.
Dependencies: RCH-1.19.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Every advertised portable/web feature has nonzero passing fixtures, exact artifacts and honest performance envelope; disabled assets issue zero requests, failures remain visible and no native/TUI parity is inferred.

Implementation:

- [ ] RCH-1.20-I1 Run the contract corpus and aggregate cold/warm timings, size/token/DOM/memory counters and disposal; verify optional-disabled packed consumers and record exact platform-wiring obligations for roadmaps31–36.

Validation:

- [ ] RCH-1.20-V1 node --test tests/rich-content-performance.test.mjs tests/rich-content-bundles.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `RCH-1.20` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `RCH-1.20`.
Blocked behavior: Leave `RCH-1.20` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.

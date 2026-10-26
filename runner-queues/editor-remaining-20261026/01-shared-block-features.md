# Complete shared block conversion and insertion

Status: COMPLETE

## Goal and authority

Deliver this bounded remaining-editor milestone in `/Users/bpstr/Github/edit-ac-editor-20261026`. The user explicitly requested remaining features, performance improvements and testing gaps on 2026-10-26. This continuation follows the current editor runner's existing required ES work; it does not restart a stopped run. Current verified ES evidence is reused only for exact applicable input pins.

Progress: `.roadmap-runner/editor-remaining-20261026/01-shared-block-features.progress.md` relative to the workspace root. The controller index is README.md; workers need only this source and the current task's named context.

## Execution and ownership

Read the active shared lane section in `/Users/bpstr/Github/edit-ac/.roadmap-coordination/parallel-clients.md` before each parent. Preserve inherited dirty work identified by the editor baseline. PRIMARY owns integration/framework/backend/host work in `/Users/bpstr/Github/edit-ac`; never modify its live source, progress, index, outputs or worker. Existing UI/EDX/platform owners retain their cases. Reuse current compatible receipts, add only uncovered editor acceptance, and never run a duplicate broad matrix merely because this queue is new. At every two parents and source boundary, use the shared integration lock and record exact editor deltas, source pins, passing selectors and deferred conflicts; commit only validated safely separable owned changes.

One parent per worker, normally 15–45 minutes including checks. Workers change only verified task checkboxes and concise Status in the live source. Requirements, hashes, delivery prose and receipt reconciliation remain controller-owned and outside this source. Separate progress holds evidence and handoff; snapshots are read-only. Run and resume only with the guarded launcher and live readiness; stop on BLOCKED or repeated completed-source contracts. Never retry unchanged input.

Apply `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`: one current production format/implementation, original data preserved, unsupported envelopes reject before mutation. No silent conversion/reseed/relabel or experimental runtime compatibility. Public positions remain UTF-16; Rust owns committed semantics and shared history; adapters own temporary input/layout.

Functional delivery uses existing narrow checks and only necessary concrete-risk regressions. Comprehensive test authoring and final matrices belong to sources04–15 after all functional sources. Optimization stops after 45 minutes or two new measured hypotheses, whichever comes first; preserve useful work, remaining failed budgets and exact final QPF owners. Final hard caps remain 512 KiB combined required JS/glue/WASM/lazy bytes and 32 KiB editor JS gzip. No cap or workload may be weakened.

All automated provider/network cases use deterministic fixtures and prepared/mock transports; no paid inference, credentials, .secrets loading, subscription proxies, automatic recording, external provisioning, publication, push or deployment. Read the Assign paid-inference policy before changing/running an AI case. Prepared output proves mechanics only. Actual platform services require the declared OS host/simulator/emulator/VM; responsive viewports/cross-compilation cannot qualify native input, clipboard or accessibility. Use the installed native-testing skill for Windows/Linux runtime work. Physical-only observations stay with roadmap43.

## Entry conditions

Finish the existing editor ES functional sources and applicable safety proof before dependent work. Authenticate only current task-local interfaces and retained evidence; a COMPLETE label or stale historical readiness.json is insufficient. Existing PRIMARY receipts are read-only; use them only after exact input applicability and a safe coordinated landing of required editor inputs. A PRIMARY-owned missing dependency is an explicit external gate, never permission to implement competing framework/native UI bindings.

## Required tasks

### Task BTA-1.1 — Implement lossless captured block conversion

- [x] BTA-1.1 Implement paragraph/heading conversion over captured block targets.

Deliverable: The named BTA-1.1 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Change presentation without recreating content or identity.
Context: Originating interface owner SFC-3.2; `specs/block-actions.md` sections Lossless presentation changes and Shared command and target contract; `core/crates/editac-core/src/commands/format.rs`, `commands/blocks.rs`, `commands/editor.rs`, `history.rs`.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only.
Dependencies: none.
Independent work: Inspect binding and registry interfaces while the shared entry gate is pending.
Session scope: One prepared conversion boundary, 30–45 minutes including focused validation; split only through the controller if necessary.
Acceptance: Paragraph, heading 1–6 and heading-level changes preserve rich/opaque content, IDs, sources, placement, descendants and directional selection. Capture presentation as well as structural preconditions. Multi-target conversion is all-or-none; current-type requests are no-ops. Read-only/protected/stale/unsupported targets reject atomically. One undo/redo action preserves peer text.

Implementation:

- [x] BTA-1.1-I1 Add typed captured targets and prepare/availability routing through existing format semantics; preserve source/owner data and return existing result-selection resources.

Validation:

- [x] BTA-1.1-V1 Run `cargo test -p editac-core --locked --offline --test block_actions heading_to_paragraph_is_lossless -- --exact` and the same command with `stale_conversion_is_atomic`. These minimal regressions protect the data-loss boundary; reuse applicable existing formatting/history results. Budget: 5 minutes; record nonzero passed/failed/skipped counts. Comprehensive combinations belong to BTQ-1.1.

Evidence: Separate progress entry with changed symbols, current-format pins, focused counts and reused checks.
Handoff: Exact captured-target fields, no-op behavior, returned resource ownership and any failed preservation invariant.
Blocked behavior: Leave unchecked; record missing primitive, owner and changed-input resume condition. Do not substitute text export/import.

### Task BTA-1.2 — Expose one portable typed command contract

- [x] BTA-1.2 Expose conversion through Rust, WASM and Session/FFI ports.

Deliverable: The named BTA-1.2 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Give extensions and all clients the same action without menu dependencies.
Context: Shared command section of the contract; BTA-1.1 handoff; `core/packages/core/src/engine.ts`, `core/crates/editac-wasm/src/bridge.rs`, `core/crates/editac-session/src/`, `core/crates/editac-ffi/src/session.rs`.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only.
Dependencies: BTA-1.1.
Independent work: Record existing per-runtime binding/command adapter ownership before the prerequisite is ready.
Session scope: Thin binding of one prepared command and typed outcomes, 30–45 minutes; no platform presenter work.
Acceptance: One named capture/enumerate/prepare/commit capability exposes no-op, unavailable reasons, stale target and existing storage errors consistently. Prepare/commit recheck permissions and touched preconditions. Engine/Session clients work without optional UI. No document identity or format bump is introduced for this action; no duplicate legacy alias is published.

Implementation:

- [x] BTA-1.2-I1 Freeze concrete binding names and schemas, route adapters to the shared primitive and document plan/selection ownership and capability availability.

Validation:

- [x] BTA-1.2-V1 Run `npm run typecheck --workspace @edit-ac/core`, `node --test --test-name-pattern='lossless port' tests/wasm-block-actions.test.mjs` and `cargo test -p editac-session -p editac-ffi --locked --offline block_actions_lossless_port`. Add one minimal round trip per changed binding; require nonzero cases in each crate. Budget: 5 minutes beyond compilation; full cross-port negatives belong to BTQ-1.1.

Evidence: Progress with the exact API/ABI shape, selected compile/probe results and runtime scope.
Handoff: Command descriptor and captured-target/result examples for extension and native/TUI owners.
Blocked behavior: Record the exact missing binding or capability; do not route around shared admission.

### Task BTA-1.3 — Register extension conversions safely

- [x] BTA-1.3 Add conversion declarations and indexed preparation to the existing extension registry.

Deliverable: The named BTA-1.3 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Make custom block types participate in Turn into through public extension APIs.
Context: Contract section Extension participation; BTA-1.2 handoff; `core/packages/core/src/extensions/registry.ts`, `core/packages/web/src/extensions/authoring.ts`, `extensions/contract.ts`, `core/packages/web/src/modules/conformance.ts` (ExtensionCommandSession).
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only.
Dependencies: BTA-1.2.
Independent work: Prepare a deterministic custom source/destination fixture from admitted data types.
Session scope: One registry/preparation integration, 30–45 minutes.
Acceptance: Namespaced source/destination declarations, bounded options, capability requirements and preservation constraints validate before attachment. Duplicate registrations reject. Providers use prepared primitives and existing cancellation/history; unknown payloads survive extension disable/re-enable. Menu-off leaves the API available; absent native providers report unavailable without pretending JavaScript is portable.

Implementation:

- [x] BTA-1.3-I1 Add typed registration and captured-target enumeration, adapting the existing command session and public authoring hooks rather than creating another dispatcher.

Validation:

- [x] BTA-1.3-V1 Run `npm run typecheck --workspace @edit-ac/web` and `node --test --test-name-pattern='registration|custom lossless' tests/block-actions-contract.test.mjs`, adapting the existing extension authoring/command fixture for one custom conversion and a rejected registration. Budget: 5 minutes; record counts. BTQ-1.2 owns the remaining lifecycle/unknown-data matrix.

Evidence: Progress with declaration shape, public import recipe and focused outcomes.
Handoff: Relevant type indexes, provider lifecycle and per-runtime availability.
Blocked behavior: Name a missing admitted primitive and its owner; never expose raw document mutation as a workaround.

### Task BTA-1.4 — Enforce advanced conversion review and refusal

- [x] BTA-1.4 Implement typed impact plans and exact-plan approval for advanced conversions.

Deliverable: The named BTA-1.4 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Prevent silent loss when richer block structures are transformed.
Context: Contract sections Conversion classification and Shared command and target contract; BTA-1.3 registry; existing prepared-plan/cancellation and error owners.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only.
Dependencies: BTA-1.3.
Independent work: Classify list/task/quote/code/table/asset/custom examples from the contract while registry work proceeds.
Session scope: One plan/admission policy boundary, 30–45 minutes; do not implement every advanced mapping.
Acceptance: Lossless built-ins need no confirmation. A review-required provider returns a staged field/structure impact report; approval binds to that plan and preconditions. Changed impact, stale targets, cancellation or permission loss reject without mutation. Unspecified advanced mappings remain unavailable with reasons. Undo support alone cannot certify losslessness; confirmation never overrides schema/permission/bounds checks.

Implementation:

- [x] BTA-1.4-I1 Add classification, review-required outcomes and single-use approval binding; publish the initial available/unavailable mapping catalog without enabling unqualified table/page conversions.

Validation:

- [x] BTA-1.4-V1 Run `node --test --test-name-pattern='review approval' tests/block-actions-contract.test.mjs` with refusal, exact approval and relevant-peer-change rejection; assert unchanged bytes on rejection. Budget: 5 minutes; this minimal regression protects a concrete destructive-edit boundary. Remaining cases belong to BTQ-1.2.

Evidence: Progress with impact schema, mapping dispositions and focused counts.
Handoff: UI review data, disabled reasons and exact approval invalidation conditions.
Blocked behavior: Keep an unresolved mapping disabled and record its design owner; do not block safe paragraph/heading delivery on table redesign.

### Task BTA-1.5 — Add general captured Insert after

- [x] BTA-1.5 Insert an empty paragraph after any eligible captured sibling.

Deliverable: The named BTA-1.5 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Supply the second required block-menu action without splitting or replacing content.
Context: Contract section Optional block menu and Insert after; BTA-1.2 target/command ports; `core/crates/editac-core/src/commands/blocks.rs`, `commands/editor.rs`, `core/packages/core/src/engine.ts` and changed bridge/Session adapters.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only.
Dependencies: BTA-1.2.
Independent work: BTA-1.3 and BTA-1.4 do not block paragraph insertion.
Session scope: One shared insertion command and thin bindings, 30–45 minutes; richer creation descriptors stay disabled unless already admitted.
Acceptance: Create a stable empty paragraph immediately after the target in the same parent, after its subtree in display order. Preserve the target and descendants; select the new editable start. Reject invalid parents, stale/deleted targets and policy failures. One undo removes only the inserted block while preserving peer changes. Separator-specific insertion is not the implementation of this general contract.

Implementation:

- [x] BTA-1.5-I1 Prepare creation/placement/result selection as one shared transaction and expose it through the same captured block-action ports.

Validation:

- [x] BTA-1.5-V1 Run `cargo test -p editac-core --locked --offline --test block_actions insert_after` and `node --test --test-name-pattern='insert after port' tests/wasm-block-actions.test.mjs`. Cover root/nested placement, unchanged original content, one undo group and stale rejection. Budget: 5 minutes. Broader history/concurrency cases belong to BTQ-1.1.

Evidence: Separate progress with command shape, focused results and reused primitive evidence.
Handoff: Functional API summary and exact source pins for all BTA parents; do not repeat passing suites at the file boundary.
Blocked behavior: Record a missing parent-creation semantic and its owner; never flatten the target to make insertion possible.

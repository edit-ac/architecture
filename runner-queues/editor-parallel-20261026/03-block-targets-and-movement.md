# Add explicit block targeting and safe structural movement

Status: IN_PROGRESS

## Goal

Expose contiguous sibling block selection and qualified typed-atom movement through the existing command, fragment and reorder machinery. Retain text-range and table selection ownership; arbitrary discontiguous blocks, new block storage and duplicate/synced-block products remain out of scope.

Progress: `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` relative to the workspace root; generated evidence is ignored and not committed.

## Execution boundaries

User-authorized editor parallel lane in `/Users/bpstr/Github/edit-ac-editor-20261026`; PRIMARY integrations continue untouched in `/Users/bpstr/Github/edit-ac`. The installed 0.12.3 scheduler and worker prompt use LIVE SOURCE CHECKBOXES as task-completion authority. Workers update only verified task/substep checkboxes and concise Status in this live source; acceptance prose, IDs, requirements and dependency rules remain controller-owned. Snapshots are read-only. The separate configured progress file holds evidence, results and handoff, not the authoritative checklist. This controller correction supersedes the prior read-only-live-source instruction, which caused ES-1.1 redispatch despite accepted proof. Read the active shared coordination section before each parent; require the guarded launcher and live readiness. Preserve the launch baseline and inherited dirty work; never stage inherited WIP or modify PRIMARY. Keep exact editor-owned delivery patches and checkpoint receipts after every two parents and each source boundary; commit only safely separable validated changes and defer mixed inherited hunks for coordinated integration.

Preserve one current document format, one prepared semantic implementation and one shared history. Public positions remain UTF-16; native layout/input stays adapter-owned. Keep current text anchors and scoped table selection. No silent normalization, data migration, profile relabel, second reader, new editor framework or platform history stack. All checks use deterministic fixtures and local/mock transports; no paid inference, credentials, recording, provisioning or publication.

Select one ready parent per session. Dependencies below are local parent IDs; earlier-source and external requirements are entry receipts, checked against current source before dependent work. Independent work can proceed within this file; a blocked serial source does not automatically dispatch a later file. Record a concrete blocker fingerprint, owner, changed-input resume condition and next independent action; never loop on unchanged failures. A task exceeding its bound needs a controller split, not reduced acceptance.

Use existing focused checks during functional delivery; add all new test code and comprehensive matrices in `04-final-conformance.md`. A bounded deterministic manual fixture may prove a new path before its final automated cases exist. Record exact command, package/source pins, runtime, nonzero executed/passed/failed/skipped counts, and actual results in the separate ignored progress file. Missing fixtures, zero matches, failed compilation and required skips leave the task unchecked. Before a check, reuse compatible passing evidence; broaden only for a concrete changed boundary. Typecheck/compile the changed package with the existing current-format consumers; preserve current build admission and do not launch competing builds against another worker. Final platform/OS-input/AT observations remain roadmap43 and cannot be claimed from scripted input or a source checker. Keep only task-owned temporary outputs outside Git and clean up any task-owned browser/server.

## Entry conditions

Current-consumer CFC-1.1–1.5 and EDX-1.1 admission receipt from the existing [editing-experience queue](../editing-experience-20261024/README.md), with actual current source/build pins. Reconcile receipt validity instead of repeating its entire gate. ES-3.3 consumes ES-1.3 applicability/results from `01-text-boundaries-and-composition.progress.md`. Block conversions remain BTA/BTU/BTQ in [shared block actions](../single-format-feature-first-20261023/02b-shared-block-actions.md); unavailable conversion providers do not block select/move/plain copy commands. Inspect actual source receipts before using a BTA action.

Controller independent-work amendment, 2026-10-26: native foreground qualification ES-2.1 is not a prerequisite for ES-3.1–3.5. The queue may deliver this block-target milestone before returning to the unchanged native focus gate; final conformance still requires all ES-2/ES-3 functionality and original checks. Current accepted ES-1.3/1.4 receipts are in `.roadmap-runner/editor-parallel-20261026/tracking-repair/01-text-boundaries-and-composition.progress.md` and its named evidence; ES-2.3/2.4 receipts remain in the source02 progress file. Use these precise current-lane receipts rather than the stopped initial source01 handoff. Each selected ES-3 parent owns the bounded local artifact/admission refresh needed for its changed selected inputs; reauthenticate applicable source pins, rebuild only invalidated production artifacts and run existing focused prerequisite selectors. Preserve original CFC/EDX safety requirements and all historical failures; do not substitute stale whole-package proof or claim broader qualification. This assigns local preparation ownership without adding a second semantic implementation or allowing new final-phase test matrices.

## Tasks

### Task ES-3.1 — Define ephemeral block selections and captured command targets

- [ ] ES-3.1 Define ephemeral block selections and captured command targets.

Purpose: Selecting editable blocks is distinct from a text range and from a table cell range.
Deliverable: A view-local discriminated target contract for text, atom, contiguous sibling blocks and existing embedded scope, with stable captured identities and applicability.
Context: [behavior standards](../../specs/editing-behavior-standards.md) ES-SEL-1/ES-BLOCK-1; [block actions](../../specs/block-actions.md); [shared clients](../../specs/client-contracts.md); existing DOMSelection, StableRange, PortableCellRange and Move/Place commands.
Affected paths/symbols: `core/packages/core/src/engine.ts` target descriptors; `core/packages/web/src/dom/selection.ts` local mode; narrow existing command capture/resolver seams, not persisted `anchors::Selection`.
Entry receipts: Current captured-target/result selection and block placement APIs; BTA contract shape where conversion is available. No requirement to add native block UI in this parent.
Dependencies: none.
Independent work: ES-3.4 typed-atom move admission can be inspected independently once current-format receipt exists.
Session scope: 35 minutes plus 5 minutes current package typechecks and existing selection fixture.
Acceptance: Modes are explicit and cannot be confused by DOM selection. Block mode names contiguous siblings in one admitted scope, normalizes selected subtrees once and rejects incompatible roots. Capture carries stable IDs/permissions and a valid text return bookmark; revalidation handles deleted/stale targets. No persistent text anchor, document envelope or semantic-history representation is replaced.

Implementation:

- [ ] ES-3.1-I1 Add the smallest local target discriminator and normalized sibling/subtree selection representation at current SDK/adapter capture boundaries.
- [ ] ES-3.1-I2 Resolve each target to existing commands and result bookmarks with stable unavailable/stale reasons; retain PortableCellRange ownership and per-runtime capability declarations.

Validation:

- [ ] ES-3.1-V1 From core typecheck changed packages with `npm run typecheck --workspace packages/core` and/or `--workspace packages/web`, then reuse or run `npm run test:browser -- selection` only for the affected boundary. Manually inspect one contiguous range and one mixed-scope refusal without mutation. Budget 5 minutes; automated new modes ES-4.3.

Evidence: `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` records changed paths/interfaces, exact focused selector and source/runtime pins, executed/passed/failed/skipped counts, no-op/rejection observations, retained evidence reused and any widening reason. Final coverage owner: ES-4.3.
Handoff: Preserve the next unchecked substep, current target/contract, exact failed fixture or missing receipt, task-owned process/output paths and next precise action; do not write hashes or handoff prose into this source.
Blocked behavior: Record `BLOCKED ES-3.1` only with owner, fingerprint and exact changed-input resume condition; preserve source/data and select the named independent work if ready. Do not retry an unchanged failed check or infer approval from elapsed time.

### Task ES-3.2 — Expose keyboard-accessible contiguous block selection

- [ ] ES-3.2 Expose keyboard-accessible contiguous block selection.

Purpose: Users can select a block range without a pointer or a hidden Notion-style shortcut state.
Deliverable: Visible Select block / extend block selection / return to text commands and accessible selected-state presentation.
Context: [behavior standards](../../specs/editing-behavior-standards.md) ES-SEL-1 and ES-AX-1; [everyday editing](../../specs/editor-interactions.md) input-owner priority and Escape-then-Tab; optional block menus/reorder controls.
Affected paths/symbols: `core/packages/web/src/commands/catalog.ts`, `ui/commands.ts`, existing block/reorder presenter and local selection/focus owner.
Entry receipts: Current presenter lifecycle and captured command controls; ES-3.1 target contract.
Dependencies: ES-3.1.
Independent work: ES-3.4 typed move admission does not require this presenter; conversions remain independently owned by BTA/BTU.
Session scope: 40 minutes plus 5 minutes focused typecheck/keyboard observation.
Acceptance: A visible keyboard-accessible command selects the current block and extends to adjacent siblings with announced scope/count. Return-to-text and Enter on a selected editable block restore a valid bookmark or admitted text start; noneditable Enter uses its explicit activation capability. Up/Down in block mode changes selection focus, never content order. Escape exits block mode while preserving the next-Tab focus escape. Composition, popup and nested-control ownership win. Existing Escape cancellation/then-Tab focus exit is unchanged; no default Escape takeover or mandatory drag handle. Selection-only changes create no content, history or storage writes.

Implementation:

- [ ] ES-3.2-I1 Connect explicit command entry/extension/exit to the local block target mode and existing focus capture.
- [ ] ES-3.2-I2 Expose accessible labels, selected-state announcement and disabled reasons without loading optional UI in configurations that omit it.

Validation:

- [ ] ES-3.2-V1 From core run `npm run typecheck --workspace packages/web` and the affected existing `npm run test:interactions -- --group keyboard` or `command-surfaces` group after confirming its dispatcher name. Use one deterministic keyboard-only select/extend/return observation and verify no engine update. Budget 5 minutes; new keyboard/accessibility tests ES-4.3/4.4.

Evidence: `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` records changed paths/interfaces, exact focused selector and source/runtime pins, executed/passed/failed/skipped counts, no-op/rejection observations, retained evidence reused and any widening reason. Final coverage owner: ES-4.3 and ES-4.4.
Handoff: Preserve the next unchecked substep, current target/contract, exact failed fixture or missing receipt, task-owned process/output paths and next precise action; do not write hashes or handoff prose into this source.
Blocked behavior: Record `BLOCKED ES-3.2` only with owner, fingerprint and exact changed-input resume condition; preserve source/data and select the named independent work if ready. Do not retry an unchanged failed check or infer approval from elapsed time.

### Task ES-3.3 — Apply one mixed-selection applicability and preservation matrix

- [x] ES-3.3 Apply one mixed-selection applicability and preservation matrix.

Purpose: Copy, cut, delete, formatting, Enter and moves have predictable results when text and whole objects share a selection.
Deliverable: Current command applicability/refusal for mixed text/whole-atom/block targets with exact preserved tails and result selection.
Context: [behavior standards](../../specs/editing-behavior-standards.md) ES-BLOCK-1, ES-FMT-1 and ES-INT-1; [everyday editing](../../specs/editor-interactions.md) transfer/formatting; EDX-2.6 and INT-1.3/1.4/1.10/1.16 remain canonical owners.
Affected paths/symbols: `core/packages/web/src/input/keyboard.ts`, clipboard fragment capture, command applicability, existing shared prepared fragment operation; no second fragment encoder.
Entry receipts: ES-1.3 selected replacement receipt; current EDX-2.6 implementation/evidence and BTA provider availability for conversion only. Reuse any exact row already closed there.
Dependencies: ES-3.1.
Independent work: ES-3.4 structural move admission can proceed; unavailable conversion or unknown payload does not block unrelated matrix rows.
Session scope: 40 minutes plus 5 minutes one affected existing interaction group.
Acceptance: Partial prose → whole admitted object → partial prose/list ranges have explicit per-command availability and atomic outcomes. Partial atoms and incompatible table/embedded scopes reject before mutation; unknown retained data never becomes fallback text. Copy/cut retains exact supported fragments, cut removes only after successful preparation/write, and formatting changes only applicable selected text and admitted atom backing-text ranges, including supported reference labels, asset fallback text and inert source text; non-markable objects remain unchanged and protected/unqualified selected text rejects the whole action. Converted block families delegate to BTA; mixed selection is not permission to discard metadata.

Implementation:

- [x] ES-3.3-I1 Crosswalk every matrix row to existing EDX/INT/BTA code/evidence; record preserved prefix/suffix, IDs/metadata and caret/result policy rather than blanket support.
- [x] ES-3.3-I2 Repair only remaining target-dispatch/refusal gaps through existing commands and fragment APIs; expose stable reasons in controls and retain one transaction/history unit.

Validation:

- [x] ES-3.3-V1 Typecheck changed TS packages; compile changed Rust crates only if preparation changes. Run one affected existing `test:interactions` group among deletion, formatting, paste or text-drag, not all, and a bounded manual mixed-range acceptance/refusal fixture. Budget 5 minutes; full mixed matrix automated once in ES-4.3.

Evidence: `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` records changed paths/interfaces, exact focused selector and source/runtime pins, executed/passed/failed/skipped counts, no-op/rejection observations, retained evidence reused and any widening reason. Final coverage owner: ES-4.3.
Handoff: Preserve the next unchecked substep, current target/contract, exact failed fixture or missing receipt, task-owned process/output paths and next precise action; do not write hashes or handoff prose into this source.
Blocked behavior: Record `BLOCKED ES-3.3` only with owner, fingerprint and exact changed-input resume condition; preserve source/data and select the named independent work if ready. Do not retry an unchanged failed check or infer approval from elapsed time.

### Task ES-3.4 — Admit identity-preserving moves for qualified typed atoms

- [ ] ES-3.4 Admit identity-preserving moves for qualified typed atoms.

Purpose: Known movable objects can be reordered without being copied into new identities or flattened.
Deliverable: An explicit select/move/copy/delete/convert capability matrix and narrow current MoveCommand extension for qualified module atoms.
Context: [behavior standards](../../specs/editing-behavior-standards.md) ES-BLOCK-2 and ES-INT-1; [engine contract](../../specs/engine.md) placement/admission; [durability](../../specs/document-durability.md); current module descriptors.
Affected paths/symbols: `core/crates/editac-core/src/commands/move.rs`, existing placement/admission and module descriptors; current Session/WASM result mapping only if required.
Entry receipts: Current Move/Place cycle/stale checks and retained-module data receipt. Qualify admitted image/asset/reference/callout/inert kinds individually; table movement requires its current table-scope owner receipt.
Dependencies: none.
Independent work: ES-3.1–3.3 targeting and applicability work can proceed independently. An unqualified table/custom kind does not block proven kinds.
Session scope: 40 minutes plus 5 minutes focused Rust compile/existing move check; no descriptor/storage redesign.
Acceptance: A qualified kind moves with identical owner/descendant IDs, payloads, asset/reference ownership, unknown bounded fields and anchors. Placement cycles, stale siblings, read-only and permission failures leave state/history unchanged. Unknown or unsupported kinds remain inert with a reason. A structural Move never becomes copy/delete or fallback-text transfer; ordinary selected-text fragment drag keeps its existing identity contract and does not inherit this whole-block ID guarantee; undo retains unrelated peer edits.

Implementation:

- [ ] ES-3.4-I1 Audit current descriptor/placement preservation and publish per-kind capability/refusal; reuse existing container/plain-block support without widening blindly.
- [ ] ES-3.4-I2 Extend the existing move allowlist/admission only for kinds with complete preservation guarantees and a current target scope; leave unsupported kinds explicit.

Validation:

- [ ] ES-3.4-V1 From core run `cargo check -p editac-core --locked --offline` and one existing move/placement test selector located before execution; use one deterministic known-atom move/no-op/rejection fixture if absent. Compare complete payload/identity snapshots without creating a new suite. Budget 5 minutes; new persistence/concurrency variants ES-4.3.

Evidence: `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` records changed paths/interfaces, exact focused selector and source/runtime pins, executed/passed/failed/skipped counts, no-op/rejection observations, retained evidence reused and any widening reason. Final coverage owner: ES-4.3.
Handoff: Preserve the next unchecked substep, current target/contract, exact failed fixture or missing receipt, task-owned process/output paths and next precise action; do not write hashes or handoff prose into this source.
Blocked behavior: Record `BLOCKED ES-3.4` only with owner, fingerprint and exact changed-input resume condition; preserve source/data and select the named independent work if ready. Do not retry an unchanged failed check or infer approval from elapsed time.

### Task ES-3.5 — Use captured atom and block targets in reorder controls

- [ ] ES-3.5 Use captured atom and block targets in reorder controls.

Purpose: Reorder UI does not require an editable text caret inside a noneditable object.
Deliverable: Existing reorder controls consume typed targets and shared move availability while retaining keyboard/touch/focus behavior.
Context: [behavior standards](../../specs/editing-behavior-standards.md) ES-SEL-1/ES-BLOCK-2/ES-AX-1; [block actions](../../specs/block-actions.md) optional controls; existing reorder module and BTU presenter ownership.
Affected paths/symbols: `core/packages/web/src/modules/reorder.ts` capture/commit/focus, command controls and result selection application.
Entry receipts: ES-3.4 current move-capability receipt; no dependency on unqualified atom families.
Dependencies: ES-3.1, ES-3.2, ES-3.4.
Independent work: ES-3.3 mixed text applicability is independent of single-target reorder presentation.
Session scope: 30 minutes plus 5 minutes focused typecheck/reorder group.
Acceptance: Known atom/block targets reorder through the same shared Move action from keyboard/buttons/pointer, with stable captured target and appropriate post-move block/text selection. Disabled kinds explain why. Optional UI can remain absent; composition/read-only/popup/focus-exit behavior and no-op history stay intact.

Implementation:

- [ ] ES-3.5-I1 Remove the text-bookmark prerequisite only where a validated typed target supplies an appropriate return selection.
- [ ] ES-3.5-I2 Bind capability/refusal and post-move focus to the existing reorder action, revalidating stale targets and avoiding a separate drag transaction implementation.

Validation:

- [ ] ES-3.5-V1 From core run `npm run typecheck --workspace packages/web` and `npm run test:browser -- reorder` only when its retained evidence is invalidated. Use one bounded noneditable-target keyboard move observation; new full target cases ES-4.3. Budget 5 minutes.

Evidence: `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` records changed paths/interfaces, exact focused selector and source/runtime pins, executed/passed/failed/skipped counts, no-op/rejection observations, retained evidence reused and any widening reason. Final coverage owner: ES-4.3 and ES-4.4.
Handoff: Preserve the next unchecked substep, current target/contract, exact failed fixture or missing receipt, task-owned process/output paths and next precise action; do not write hashes or handoff prose into this source.
Blocked behavior: Record `BLOCKED ES-3.5` only with owner, fingerprint and exact changed-input resume condition; preserve source/data and select the named independent work if ready. Do not retry an unchanged failed check or infer approval from elapsed time.

## Milestone handoff

The progress file carries a compact interface and evidence summary for the next source. Reuse compatible checks; this boundary does not require another suite run. Completion of this source does not close final conformance, OS/AT observations or publication gates.

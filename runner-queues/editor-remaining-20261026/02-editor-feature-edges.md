# Complete optional block actions and large-document admission

Status: COMPLETE

## Goal and authority

Deliver this bounded remaining-editor milestone in `/Users/bpstr/Github/edit-ac-editor-20261026`. The user explicitly requested remaining features, performance improvements and testing gaps on 2026-10-26. This continuation follows the current editor runner's existing required ES work; it does not restart a stopped run. Current verified ES evidence is reused only for exact applicable input pins.

Progress: `.roadmap-runner/editor-remaining-20261026/02-editor-feature-edges.progress.md` relative to the workspace root. The controller index is README.md; workers need only this source and the current task's named context.

## Execution and ownership

Read the active shared lane section in `/Users/bpstr/Github/edit-ac/.roadmap-coordination/parallel-clients.md` before each parent. Preserve inherited dirty work identified by the editor baseline. PRIMARY owns integration/framework/backend/host work in `/Users/bpstr/Github/edit-ac`; never modify its live source, progress, index, outputs or worker. Existing UI/EDX/platform owners retain their cases. Reuse current compatible receipts, add only uncovered editor acceptance, and never run a duplicate broad matrix merely because this queue is new. At every two parents and source boundary, use the shared integration lock and record exact editor deltas, source pins, passing selectors and deferred conflicts; commit only validated safely separable owned changes.

One parent per worker, normally 15–45 minutes including checks. Workers change only verified task checkboxes and concise Status in the live source. Requirements, hashes, delivery prose and receipt reconciliation remain controller-owned and outside this source. Separate progress holds evidence and handoff; snapshots are read-only. Run and resume only with the guarded launcher and live readiness; stop on BLOCKED or repeated completed-source contracts. Never retry unchanged input.

Apply `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`: one current production format/implementation, original data preserved, unsupported envelopes reject before mutation. No silent conversion/reseed/relabel or experimental runtime compatibility. Public positions remain UTF-16; Rust owns committed semantics and shared history; adapters own temporary input/layout.

Functional delivery uses existing narrow checks and only necessary concrete-risk regressions. Comprehensive test authoring and final matrices belong to sources04–15 after all functional sources. Optimization stops after 45 minutes or two new measured hypotheses, whichever comes first; preserve useful work, remaining failed budgets and exact final QPF owners. Final hard caps remain 512 KiB combined required JS/glue/WASM/lazy bytes and 32 KiB editor JS gzip. No cap or workload may be weakened.

All automated provider/network cases use deterministic fixtures and prepared/mock transports; no paid inference, credentials, .secrets loading, subscription proxies, automatic recording, external provisioning, publication, push or deployment. Read the Assign paid-inference policy before changing/running an AI case. Prepared output proves mechanics only. Actual platform services require the declared OS host/simulator/emulator/VM; responsive viewports/cross-compilation cannot qualify native input, clipboard or accessibility. Use the installed native-testing skill for Windows/Linux runtime work. Physical-only observations stay with roadmap43.

## Entry conditions

Finish the existing editor ES functional sources and applicable safety proof before dependent work. Authenticate only current task-local interfaces and retained evidence; a COMPLETE label or stale historical readiness.json is insufficient. Existing PRIMARY receipts are read-only; use them only after exact input applicability and a safe coordinated landing of required editor inputs. A PRIMARY-owned missing dependency is an explicit external gate, never permission to implement competing framework/native UI bindings.

## Required tasks

### Task BTU-1.1 — Add the configurable block menu and handle

- [x] BTU-1.1 Present Turn into and Insert after through captured block actions.

Deliverable: The named BTU-1.1 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Provide discoverable per-block actions without moving semantics into UI code.
Context: Originating interface owner BTA-1.2; Contract sections Optional block menu and Shared command and target contract; BTA interface summary; `core/packages/web/src/surface.ts`, `editor.ts`, `extensions/configuration.ts`, `modules/reorder.ts` and a task-owned block-actions presenter.
Entry receipts: Source01 BTA-1.2–1.5 exact current capability/registry/plan/insertion proof.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Dependencies: none.
Independent work: SDK recipe drafting can proceed before presenter attachment is complete.
Session scope: One optional presenter and configuration integration, 30–45 minutes; preserve a usable intermediate state and request a split if its lifecycle integration exceeds this boundary.
Acceptance: Menu and reorder handle can be enabled independently. Supported editable blocks expose Turn into and Insert after; destinations/current state/disabled reasons come from the shared API. Focus captures the intended block before opening. Escape/cancel is mutation-free. Read-only, IME, touch, nested-control and disposal rules reuse existing owners. Menu-off adds no presenter or per-keystroke registry scan and leaves conversion API capability unchanged.

Implementation:

- [x] BTU-1.1-I1 Attach an optional accessible block-actions presenter, derive its items from shared capability data and route commits through existing storage/history. Reuse reorder for its handle rather than duplicating moves.

Validation:

- [x] BTU-1.1-V1 Run `npm run typecheck --workspace @edit-ac/web` and `node --test --test-name-pattern='menu baseline|insert after|menu off' tests/browser/block-actions.spec.ts` for heading conversion, insertion, Escape and menu-off API use. Budget: 5 minutes beyond build. Comprehensive device/focus matrices belong to BTQ-1.3 and final platform owners.

Evidence: Progress with configuration shape, selected browser counts and owned resource teardown.
Handoff: Presenter/handle ownership, captured target lifetime and unresolved layout/accessibility cases.
Blocked behavior: Record the missing shared interface; never infer a target from a changed caret or apply DOM-only edits.

### Task BTU-1.2 — Share conversion actions with slash and keyboard commands

- [x] BTU-1.2 Route slash, keyboard and review UI through the shared conversion capability.

Deliverable: The named BTU-1.2 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Keep conversion behavior coherent across interaction methods and expose advanced impact plans safely.
Context: Contract sections Shared command and target contract and Conversion classification; BTU-1.1 presenter; `core/packages/web/src/commands/catalog.ts`, `modules/slash.ts`, `input/keyboard.ts`, existing command controls and result-selection ownership.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only. Required repaired prerequisite: [BTA-2.1](../editor-slash-unblock-20261026/01-atomic-conversion-cleanup.md) and its current focused proof at `.roadmap-runner/editor-slash-unblock-20261026/01-atomic-conversion-cleanup.progress.md`. Reassess only after that owner delivers atomic captured cleanup; the unchanged menu/slash/shortcut acceptance below is not waived.
Dependencies: BTU-1.1.
Independent work: Read existing shortcut reservations and slash selection behavior before integration.
Session scope: One action-routing integration, 30–45 minutes; no new semantic implementation.
Acceptance: Menu, slash and configured shortcuts use the same conversion identity, capability checks and target semantics. Invoking a conversion through slash removes only its captured transient trigger/query as part of the same atomic intent; never remove unrelated content. Reserved OS/host shortcuts remain reserved. A review-required plan displays exact impact and cancel/approve controls; changing the target or impact invalidates approval. Lossless heading conversion executes without a confirmation prompt.

Implementation:

- [x] BTU-1.2-I1 Adapt existing command catalog/slash capture to conversion actions and render the shared impact report with explicit approval, cancellation and predictable focus restoration.

Validation:

- [x] BTU-1.2-V1 Run `node --test --test-name-pattern='entry parity|review cancellation' tests/browser/block-actions.spec.ts`, comparing direct API/menu/slash/shortcut results on one rich block and cancelled/stale review. Budget: 5 minutes; reuse BTU-1.1 evidence for unchanged paths. Broader combinations belong to BTQ-1.3.

Evidence: Progress with shared action IDs, trigger cleanup ownership and exact focused results.
Handoff: Shortcut/selection policy and review UI outcome mapping for final tests and platform consumers.
Blocked behavior: If slash cannot capture its query safely, record the exact shared primitive gap; do not perform trigger deletion and conversion as separate commits.

### Task BTU-1.3 — Publish coherent local API and extension recipes

- [x] BTU-1.3 Document and wire public local-consumer recipes for block conversion.

Deliverable: The named BTU-1.3 outcome and unchanged Acceptance below, with scoped current-source proof.
Purpose: Make the required block API usable without knowledge of presenter internals.
Context: Originating interface owner BTU-1.1; Delivered BTA/BTU interfaces; `core/packages/web/src/index.ts`, `core/packages/core/src/index.ts`, `core/packages/web/README.md`, `core/packages/core/README.md`, existing SDK and extension authoring examples.
Affected paths/symbols: Only this task's Context implementation/dispatcher and configured local progress; discover actual symbols before editing.
Entry receipts: The task-local current interfaces and applicable proof described in Context and this source's entry conditions; historical source hashes are leads only.
Dependencies: BTU-1.1, BTU-1.2.
Independent work: Draft accurate planned recipes while entry interfaces settle; publish implemented claims only after focused proof.
Session scope: Public exports and three concise recipes, 20–40 minutes.
Acceptance: Recipes show a headless lossless heading conversion, optional menu/handle configuration and one custom conversion declaration with unavailable/review outcomes. Core operations remain available without UI. Configured content permission is distinct from menu filtering. Record actual Rust/WASM/Session/FFI availability and native/TUI presenter follow-ups; do not claim an unimplemented runtime or conversion. No new published package version or deployment is implied.

Implementation:

- [x] BTU-1.3-I1 Expose the single intended facade and update local examples/docs; remove contradictory new examples or accidental aliases before freezing the API.

Validation:

- [x] BTU-1.3-V1 Run `node --test --test-name-pattern='documented recipes' tests/block-actions-consumer.test.mjs`, compiling the three documented examples through the existing consumer harness and exercising their public imports. Budget: 5 minutes; broader packed/lazy/disabled-extension checks belong to BTQ-1.2 and BTQ-1.3.

Evidence: Progress with public imports, source/runtime pins and focused example results.
Handoff: Functional completion summary, outstanding final acceptance and named platform owners. Reuse all compatible predecessor evidence.
Blocked behavior: Record a concrete export/provider gap; do not label planned behavior implemented.

### Task EFG-1.1 — Repair the current large-document input prerequisite

- [x] EFG-1.1 Admit an authentic current-format large editing fixture without weakening resource safety.

Purpose: The ES-3.5 handoff records INT-1.10 stopping during oversized document construction, before actual editor behavior. A prepared adapter result is not runtime proof.
Deliverable: One admitted deterministic large checkpoint/fixture and the smallest owning admission repair, or a precise supported refusal with the original required large-workload owner left open.
Context: `architecture/specs/editor-interactions.md` INT-1.10; `architecture/specs/document-durability.md`; `.roadmap-runner/editor-parallel-20261026/03-block-targets-and-movement.progress.md` Deferred gates; current core resource admission and the existing browser large-document fixture.
Affected paths/symbols: Existing core document resource admission, current-format deterministic fixture and existing browser interaction dispatcher; discover actual symbols before editing.
Entry receipts: Current-format safety receipt and ES-3.5 current core/web artifact pins; reject stale artifacts rather than recreating historical proof.
Dependencies: none.
Independent work: BTU-1.1–1.3 do not depend on this fixture.
Session scope: One fixture/admission boundary, at most 45 minutes including a focused check; request a bounded split for a deeper production resource redesign.
Acceptance: Freeze the actual required corpus identity and existing limits before repair. If the fixture is valid, load the real compiled editor and observe content, selection, one edit and undo; existing oversized/malformed rejection remains nonmutating. Do not lower the required workload, raise hard limits, bypass admission or count a mocked adapter as runtime evidence. A documented valid resource refusal leaves this parent unfinished with the owning repair and exact resume input.

Implementation:

- [x] EFG-1.1-I1 Reproduce the saved admission failure once on authenticated changed/current input; distinguish invalid fixture construction from an engine defect, then correct the owning boundary without changing the required corpus or safety contract.

Validation:

- [x] EFG-1.1-V1 Run only the existing selected INT-1.10 fixture and affected admission negative selector; record nonzero executed/passed/failed/skipped counts, content/selection/history oracle and input pins. Budget: 8 minutes after reused build evidence; comprehensive scaling belongs to QPF-1.2.

Evidence: Configured separate progress contains exact fixture size, original failure, changed-input hypothesis, current accepted/rejected states and focused results; generated bulk remains ignored.
Handoff: Next unchanged acceptance, owning code/fixture, source pins, failed selector and exact prerequisite; no source delivery prose.
Blocked behavior: Preserve the failure fingerprint and original required workload; return BLOCKED after the one concrete repair attempt if no independent work remains. No unchanged retry.

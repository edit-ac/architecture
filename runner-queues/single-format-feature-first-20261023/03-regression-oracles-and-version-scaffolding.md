# Port regression semantics and retire unused version scaffolding

Status: IN_PROGRESS

## Goal and entry conditions

SFC-3 current projection/command/consumer interfaces are applicable; exact prior source tests remain available for semantic mapping, without requiring old readers in production.

## Execution policy

Superseding user decision, 2026-10-23: follow `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`. One production document schema/profile (the existing witnessed v5 format) and one current implementation per API/wire/ABI contract until publication. Retired development readers and fabricated previous/current release matrices are fixture history only; preserve useful behavior assertions on current-format cases. Never silently relabel, migrate, reset or reseed real data. Retain actual protocol/update-encoding semantics, external formats and document revision/history. Older version-specific runtime clauses in copied historical acceptance are superseded by this decision, not by dropping their semantic regressions.

One serial controller, root `/Users/bpstr/Github/edit-ac`, existing main branches only; no worktree, parallel lane, subagents or second run. Use only active source/progress and its named prerequisite summary. Prior run f6915e733a5ecb9c1c64e7ff is stopped, not restarted. Preserve its dirty work and exact successful/failing evidence. Workers may change only task checkboxes and the Status line in this source. Put delivery summaries, source hashes, reconciliation receipts, timestamps and counts only in the separate progress file or ignored receipts. Never add or update a Current delivery paragraph here: changing acceptance prose on each pass forces another reconciliation. Read current prerequisites from `.roadmap-runner/single-format-feature-first-20261023/readiness.json` and its bounded handoff rows. The first source adapts existing collectors to this successor manifest; old matrix paths are historical evidence only.

Canonical shared-format cleanup and a focused safety gate precede native consumers. Then complete independent features before remaining optimization and comprehensive final suites. Size/latency work gets at most 45 minutes OR two materially different measured hypotheses per batch, whichever comes first. Checkpoint useful code and honest unresolved numbers, then advance independent feature work. Parent completion for a bounded optimization batch never closes its original hard-budget predicate; QPF final gates still own unchanged 512 KiB total/32 KiB editor-JS gzip caps and complete resource/tail proof. Never rerun an unchanged failing inventory. A true semantic/data-safety defect or missing required interface blocks only its dependents.

Use existing narrow deterministic checks during delivery, record meaningful counts and exact input hashes, and add a small regression only for a concrete shared-contract risk. Full test development/matrices stay with final owners; the focused format cutover gate is an explicit prerequisite to safely continue feature work. Port rather than suppress useful old regression assertions. Missing commands, zero cases, failures and required skips cannot pass. Historical fixture-oracle executions do not establish production legacy support. No new production legacy flag or old compatibility crate is allowed.

No paid inference, credentials, `.secrets`, subscription proxy, live fixture recording, paid services, physical-device qualification, publication, push, deployment or new external integration. Use prepared/mock transports for every automated provider case. Appropriate simulators/emulators and OS hosts/VMs must prove claimed target behavior; host-only JNA and responsive browser viewports are not mobile OS proof. Unknown/retired envelopes reject before mutation and preserve original checkpoint/journal recovery bytes. Optional encrypted/cloud release claims remain out of profile without removing baseline or discovered required tests.

One parent per worker, normally 15–45 minutes including focused checks. Commit only validated owned source on current main at safe checkpoints, under the coordination lock; never blindly stage prior dirty paths, stash/reset, or edit another worker's files. Generated evidence/binaries stay ignored and task-owned; keep concise counts/pins/failure dispositions, remove inactive reproducible bulk output. Tear down owned browsers/servers and check disk after substantial builds. Select another local ready parent beside a blocker; when none is ready, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, return BLOCKED, and let the event guard stop the controller. No unchanged retry or automatic restart.

## Epic REGRESSION_ORACLES_AND_VERSION_SCAFFOLDING — Port regression semantics and retire unused version scaffolding

### Task SFC-4.1 — Port useful behavioral regression fixtures

- [ ] SFC-4.1 Port useful behavioral regression fixtures.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; constructor/callsite inventory; original core initialization/format/text/projection/anchor/structural/profile tests
Dependencies: none.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Every useful original semantic regression has a current-format fixture/test owner, with the same intended safety invariant or explicit corrected witnessed behavior. No required test disappears as a skip/ignore, zero group or renamed unsupported positive.

Implementation:

- [ ] SFC-4.1-I1 Port original legacy setup/IDs/expected outputs to the current engine while preserving independent semantic assertions. Keep format-specific historical qualification tests independent from runtime and labelled as fixture-oracle history. Remove transitional old constructor aliases after compile callers are accounted for.

Validation:

- [ ] SFC-4.1-V1 Compile affected test targets and run their changed selections. Compare discovered original semantic case IDs to current tests/oracles; report unavoidable changed behavior with its approved spec, never erase the old failure disposition.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task SFC-4.2 — Isolate historical readers from production inputs

- [ ] SFC-4.2 Isolate historical readers from production inputs.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; `core/fixtures/schema-v1` through v5, current library dependency modules and WASM packaging
Dependencies: SFC-4.1.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Historical v1–v4 readers/mappers exist only as independent fixture oracles or archived source, outside all production imports/dependency graphs/exported features. The runtime contains only current decoder/replay/model helpers. Required current/native regression tests still execute meaningful cases.

Implementation:

- [ ] SFC-4.2-I1 Audit actual module/feature/dependency closure. Move reusable current helpers into src rather than importing old fixture mappers, without introducing a legacy-runtime feature flag or compatibility crate. Keep bounded old test bytes/provenance; no bulk generated snapshot restoration.

Validation:

- [ ] SFC-4.2-V1 Use deterministic module/graph/static negative controls and affected canonical/oracle test runs. One changed production build may confirm closure; no repeated size tuning. Verify current and old fixture oracles are labelled separately.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task SFC-4.3 — Remove synthetic previous-release and unused API variants

- [ ] SFC-4.3 Remove synthetic previous-release and unused API variants.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; `core/scripts/compatibility-policy.mjs`; compatibility policy/tests; capability/API/ABI descriptor factories; current guides
Dependencies: none.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Before publication there is one supported current API/ABI/protocol contract per actual boundary. Fabricated previous/current SDK revision closures and obsolete unpublished adapters/aliases no longer create runtime support or gate same-format reopening. Real external formats, document revisions, wire/encoding/descriptor validation and deterministic unsupported-input tests remain.

Implementation:

- [ ] SFC-4.3-I1 Inventory alternate-version code by actual current consumers. Replace synthetic release-matrix qualification with independently packed current consumers and exact unsupported-tuple/unknown-data recovery tests. Remove only unused unpublished alternatives; do not conflate distinct real contracts or require an exact old Git hash for same-format data.

Validation:

- [ ] SFC-4.3-V1 Run affected compatibility/contract/export/consumer tests with real current round trips, bad tuple/revision nonmutation and retained recovery data. No live provider/network service or full performance campaign.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

## Epic ALPHA_BLOCK_UI — Deliver configurable block actions

The preceding source must hand off completed BTA-1.1–1.5 interfaces and focused proof before BTU implementation. Finish these shared product features before native delivery and final testing. Reuse the existing move implementation; add configurable block-local discoverability and preserve headless API use.

### Task BTU-1.1 — Add the configurable block menu and handle

- [ ] BTU-1.1 Present Turn into and Insert after through captured block actions.

Purpose: Provide discoverable per-block actions without moving semantics into UI code.
Context: Originating interface owner BTA-1.2; Contract sections Optional block menu and Shared command and target contract; BTA interface summary; `core/packages/web/src/surface.ts`, `editor.ts`, `extensions/configuration.ts`, `modules/reorder.ts` and a task-owned block-actions presenter.
Dependencies: none.
Independent work: SDK recipe drafting can proceed before presenter attachment is complete.
Session scope: One optional presenter and configuration integration, 30–45 minutes; preserve a usable intermediate state and request a split if its lifecycle integration exceeds this boundary.
Acceptance: Menu and reorder handle can be enabled independently. Supported editable blocks expose Turn into and Insert after; destinations/current state/disabled reasons come from the shared API. Focus captures the intended block before opening. Escape/cancel is mutation-free. Read-only, IME, touch, nested-control and disposal rules reuse existing owners. Menu-off adds no presenter or per-keystroke registry scan and leaves conversion API capability unchanged.

Implementation:

- [ ] BTU-1.1-I1 Attach an optional accessible block-actions presenter, derive its items from shared capability data and route commits through existing storage/history. Reuse reorder for its handle rather than duplicating moves.

Validation:

- [ ] BTU-1.1-V1 Run `npm run typecheck --workspace @edit-ac/web` and `node --test --test-name-pattern='menu baseline|insert after|menu off' tests/browser/block-actions.spec.ts` for heading conversion, insertion, Escape and menu-off API use. Budget: 5 minutes beyond build. Comprehensive device/focus matrices belong to BTQ-1.3 and final platform owners.

Evidence: Progress with configuration shape, selected browser counts and owned resource teardown.
Handoff: Presenter/handle ownership, captured target lifetime and unresolved layout/accessibility cases.
Blocked behavior: Record the missing shared interface; never infer a target from a changed caret or apply DOM-only edits.

### Task BTU-1.2 — Share conversion actions with slash and keyboard commands

- [ ] BTU-1.2 Route slash, keyboard and review UI through the shared conversion capability.

Purpose: Keep conversion behavior coherent across interaction methods and expose advanced impact plans safely.
Context: Contract sections Shared command and target contract and Conversion classification; BTU-1.1 presenter; `core/packages/web/src/commands/catalog.ts`, `modules/slash.ts`, `input/keyboard.ts`, existing command controls and result-selection ownership.
Dependencies: BTU-1.1.
Independent work: Read existing shortcut reservations and slash selection behavior before integration.
Session scope: One action-routing integration, 30–45 minutes; no new semantic implementation.
Acceptance: Menu, slash and configured shortcuts use the same conversion identity, capability checks and target semantics. Invoking a conversion through slash removes only its captured transient trigger/query as part of the same atomic intent; never remove unrelated content. Reserved OS/host shortcuts remain reserved. A review-required plan displays exact impact and cancel/approve controls; changing the target or impact invalidates approval. Lossless heading conversion executes without a confirmation prompt.

Implementation:

- [ ] BTU-1.2-I1 Adapt existing command catalog/slash capture to conversion actions and render the shared impact report with explicit approval, cancellation and predictable focus restoration.

Validation:

- [ ] BTU-1.2-V1 Run `node --test --test-name-pattern='entry parity|review cancellation' tests/browser/block-actions.spec.ts`, comparing direct API/menu/slash/shortcut results on one rich block and cancelled/stale review. Budget: 5 minutes; reuse BTU-1.1 evidence for unchanged paths. Broader combinations belong to BTQ-1.3.

Evidence: Progress with shared action IDs, trigger cleanup ownership and exact focused results.
Handoff: Shortcut/selection policy and review UI outcome mapping for final tests and platform consumers.
Blocked behavior: If slash cannot capture its query safely, record the exact shared primitive gap; do not perform trigger deletion and conversion as separate commits.

### Task BTU-1.3 — Publish coherent local API and extension recipes

- [ ] BTU-1.3 Document and wire public local-consumer recipes for block conversion.

Purpose: Make the required block API usable without knowledge of presenter internals.
Context: Originating interface owner BTU-1.1; Delivered BTA/BTU interfaces; `core/packages/web/src/index.ts`, `core/packages/core/src/index.ts`, `core/packages/web/README.md`, `core/packages/core/README.md`, existing SDK and extension authoring examples.
Dependencies: BTU-1.1, BTU-1.2.
Independent work: Draft accurate planned recipes while entry interfaces settle; publish implemented claims only after focused proof.
Session scope: Public exports and three concise recipes, 20–40 minutes.
Acceptance: Recipes show a headless lossless heading conversion, optional menu/handle configuration and one custom conversion declaration with unavailable/review outcomes. Core operations remain available without UI. Configured content permission is distinct from menu filtering. Record actual Rust/WASM/Session/FFI availability and native/TUI presenter follow-ups; do not claim an unimplemented runtime or conversion. No new published package version or deployment is implied.

Implementation:

- [ ] BTU-1.3-I1 Expose the single intended facade and update local examples/docs; remove contradictory new examples or accidental aliases before freezing the API.

Validation:

- [ ] BTU-1.3-V1 Run `node --test --test-name-pattern='documented recipes' tests/block-actions-consumer.test.mjs`, compiling the three documented examples through the existing consumer harness and exercising their public imports. Budget: 5 minutes; broader packed/lazy/disabled-extension checks belong to BTQ-1.2 and BTQ-1.3.

Evidence: Progress with public imports, source/runtime pins and focused example results.
Handoff: Functional completion summary, outstanding final acceptance and named platform owners. Reuse all compatible predecessor evidence.
Blocked behavior: Record a concrete export/provider gap; do not label planned behavior implemented.

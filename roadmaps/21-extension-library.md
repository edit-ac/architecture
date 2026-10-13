# Expose the public portable extension library

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [the owning contract](../specs/extension-library.md), [shared client contracts](../specs/client-contracts.md) and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned implementation/test files are created by their task. Source is controller-owned; write checkmarks, state and evidence only in the separate progress file.

Upstream entry gates: `07-extension-modules.md` and `12-client-contracts.md` complete at current source revisions with passing artifact evidence; `05-markdown-content.md` passes the portable and simulator/emulator development level defined in verification.md, including FMT-1.12. Physical FMT-1.15-V1 remains a release gate. Cross-roadmap IDs are context references; dependencies below name only parents in this file. Do not launch implementation while an upstream gate is unavailable.

Reuse the qualified built-in modules rather than duplicating them. This track owns public contracts, conformance fixtures, examples and platform presenter obligations; tracks 16/17/18 own their full native/desktop renderers. Define those downstream hooks without depending on completed downstream implementations. The final full-delivery gate consumes the library and actual platform evidence.

Controller development-entry amendment (2026-10-13): interpret the roadmap-05 gate using the simulator/emulator development level in `../architecture/specs/verification.md`. Qualified portable FMT-1.1–FMT-1.14 behavior plus the actual passing virtual-device receipt is sufficient for this development track; physical FMT-1.15-V1 remains an open release obligation. No other upstream acceptance is waived.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus focused validation. Inspect actual symbols before editing; reuse the qualified owning implementation. If the named boundary is larger, record the exact remaining acceptance and a proposed controller split rather than silently expanding scope or weakening it. Other dependency-ready parents in this track are permitted independent work; unmet prerequisites remain unchecked.

Create the named tests before invoking them. Capture full logs locally; record nonzero executed/passed/failed/skipped counts, exact commands, fixture/artifact hashes and revisions in progress. Missing tests, zero-match filters, failed checks and skipped required cases never prove completion. Use deterministic fixtures and mocked host/auth/receipt transports. No model/provider calls, live credential loading, production document writes, background runner startup or publication are authorized by this implementation track.

## Epic EXT-1 — Expose the public portable extension library


### Task EXT-1.1 — Verify extension and shared-client entry contracts

- [ ] EXT-1.1 Implement and validate verify extension and shared-client entry contracts.

Purpose: Identify existing modules and reusable contracts before exposing a public library.
Context: `crates/editac-core/src/modules/`; `packages/web/src/modules/`; `../architecture/evidence/modules.md`; `../architecture/specs/client-contracts.md`; `../architecture/specs/extension-library.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Current Markdown, module and client gates pass; existing descriptor/codec/command/presenter symbols are mapped once, including the six built-in modules and unsupported cases. No basic module is reimplemented merely to create the library.

Implementation:

- [ ] EXT-1.1-I1 Map qualified implementations and record the existing evidence for each built-in descriptor, command and fallback. Define the public-library ownership boundary and fixture directory using current schema/client contract revisions.

Validation:

- [ ] EXT-1.1-V1 Rerun the named upstream module/Markdown conformance fixtures at their reviewed revisions and record nonzero selected tests plus an interface map in ../architecture/evidence/extension-entry.md. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.1` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.1`.
Blocked behavior: Leave `EXT-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.2 — Expose stable public extension entry points

- [ ] EXT-1.2 Implement and validate expose stable public extension entry points.

Purpose: Let independent consumers register supported extension data without private imports.
Context: `crates/editac-core/src/modules/mod.rs`; `packages/core/`; `packages/web/package.json`; `packages/web/src/modules/index.ts`; `tests/extension-exports.test.mjs`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Rust/browser public imports expose validated descriptor, command and codec contracts with supported versions; clean consumers require no internal source paths. Registering a data-defined mark/atom uses unchanged engine artifacts, and invalid/duplicate descriptors fail atomically.

Implementation:

- [ ] EXT-1.2-I1 Promote the existing supported interfaces through owning crate/package exports and versioned types. Document which registrations use qualified generic primitives and which new editing semantics require core implementation. Keep executable renderer functions outside document state.

Validation:

- [ ] EXT-1.2-V1 Run the focused Rust module registration checks and node --test tests/extension-exports.test.mjs against built/packed artifacts; assert duplicate/invalid registration and stable public-import behavior. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.2` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.2`.
Blocked behavior: Leave `EXT-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.3 — Build reusable descriptor and fallback conformance fixtures

- [ ] EXT-1.3 Implement and validate build reusable descriptor and fallback conformance fixtures.

Purpose: Give every first- or third-party module the same data-preservation checks.
Context: `crates/editac-core/tests/extension_contract.rs`; `fixtures/extensions/`; `packages/web/src/modules/conformance.ts`; `tests/extension-contract.test.mjs`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.2.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A descriptor and fixed fixture set exercise validation, deterministic serialization, bounds and unknown/disabled-version fallback in Rust and web. Canonical semantic results agree and original unknown payload remains recoverable without executing code.

Implementation:

- [ ] EXT-1.3-I1 Extract reusable test helpers around existing module interfaces. Include custom mark/atom and built-in examples, unknown versions, invalid attributes/content, disabled renderers and malformed/oversized data; compare semantic projections rather than CRDT byte ordering.

Validation:

- [ ] EXT-1.3-V1 cargo test -p editac-core --test extension_contract --locked; node --test tests/extension-contract.test.mjs. Confirm each advertised fixture cell runs and unknown data round-trips unchanged. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.3` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.3`.
Blocked behavior: Leave `EXT-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.4 — Qualify module codecs and version migration boundaries

- [ ] EXT-1.4 Implement and validate qualify module codecs and version migration boundaries.

Purpose: Preserve module data through Markdown editing and explicit schema evolution.
Context: `crates/editac-core/tests/extension_codecs.rs`; `fixtures/extensions/versions/`; `tests/extension-codecs.test.mjs`; `../architecture/specs/formats.md`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.3.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Supported codecs/copy/export preserve qualified semantics; edits elsewhere retain unknown module identity/data. Unsupported or unsafe source/migration changes reject before mutation. Old/new/unknown versions and delayed offline updates follow the existing schema/epoch transition contract.

Implementation:

- [ ] EXT-1.4-I1 Extend conformance hooks for Markdown/source reconciliation, literal-text bypass and pure candidate-data migrations. Declare supported transitions per descriptor; reuse the owning document migration protocol instead of silently rewriting live state on registration.

Validation:

- [ ] EXT-1.4-V1 cargo test -p editac-core --test extension_codecs --locked; node --test tests/extension-codecs.test.mjs. Include interrupted/failed migration, unsupported versions, unchanged opaque data and delayed old-epoch updates. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.4` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.4`.
Blocked behavior: Leave `EXT-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.5 — Qualify module commands and lifecycle behavior

- [ ] EXT-1.5 Implement and validate qualify module commands and lifecycle behavior.

Purpose: Ensure extensions respect shared history, capabilities and bounded change notifications.
Context: `crates/editac-core/tests/extension_commands.rs`; `packages/web/src/modules/conformance.ts`; `tests/extension-lifecycle.test.mjs`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.3.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Command preparation is nonmutating until commit, history grouping matches intent and read-only blocks mutations. Irrelevant patches do not invoke the module; errors, stale async results, cancellation and repeated disposal cannot corrupt state or leak live callbacks.

Implementation:

- [ ] EXT-1.5-I1 Add reusable command/applicability/history and subscription lifecycle fixtures around existing APIs. Include local/remote origins and stable view identity; route every extension request through the shared command/capability boundary after engine transactions are released.

Validation:

- [ ] EXT-1.5-V1 cargo test -p editac-core --test extension_commands --locked; node --test tests/extension-lifecycle.test.mjs. Assert mutation counts, undo groups, observer calls and disposal/stale-result behavior. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.5` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.5`.
Blocked behavior: Leave `EXT-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.6 — Define platform presenter conformance interfaces

- [ ] EXT-1.6 Implement and validate define platform presenter conformance interfaces.

Purpose: Give platform clients one implementable extension interface without coupling library completion to their UI delivery.
Context: `crates/editac-core/src/modules/`; `packages/web/src/modules/`; `fixtures/extensions/presenters/`; `tests/extension-presenters.test.mjs`; `../architecture/specs/extension-presenters.md`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.4, EXT-1.5.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Browser, terminal, Swift/iOS, Kotlin/Android and desktop presenter contracts name focus/input/composition, selection, accessibility, clipboard/source, patch, cancel and disposal obligations. Headless adapters satisfy the shared protocol; no full renderer/platform parity is asserted by those probes.

Implementation:

- [ ] EXT-1.6-I1 Define typed presenter inputs/results and platform capability records over existing node/command interfaces. Create tests/extension-presenters.test.mjs with headless contract adapters and fixtures; document how tracks 16/17/18 and terminal integration consume them without storing callbacks in CRDT state.

Validation:

- [ ] EXT-1.6-V1 node --test tests/extension-presenters.test.mjs. Run every declared host adapter and verify shared update/cancel/dispose traces; reject missing adapters and zero matching cases. Record which real-platform qualification cells remain owned by downstream tracks. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.6` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.6`.
Blocked behavior: Leave `EXT-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.7 — Publish built-in capability and parity obligations

- [ ] EXT-1.7 Implement and validate publish built-in capability and parity obligations.

Purpose: Make every supported host/module claim traceable to an explicit requirement and evidence owner.
Context: `fixtures/extensions/capabilities.json`; `docs/extensions/capabilities.md`; `tests/extension-capabilities.test.mjs`; `../architecture/specs/extension-presenters.md`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.6.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Slash, references, reorder, images, tables and math each declare preservation/view/edit/copy/Markdown/accessibility/rendering cells for supported hosts. Required parity cells have fixture IDs and a platform owner; fallback is distinct from richer view/edit parity and unknown data remains preserved.

Implementation:

- [ ] EXT-1.7-I1 Create the machine-readable capability schema and populate it from existing module evidence plus shared presenter obligations. Name required keyboard/focus behavior and honest platform fallbacks; mark future renderer evidence as pending instead of claiming completion.

Validation:

- [ ] EXT-1.7-V1 node --test tests/extension-capabilities.test.mjs. Reject missing required module/host cells, contradictory fallback/parity claims and unsupported evidence references; inspect that downstream obligations are concrete without depending on completed platform renderers. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.7` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.7`.
Blocked behavior: Leave `EXT-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.8 — Integrate references with host-controlled authority

- [ ] EXT-1.8 Implement and validate integrate references with host-controlled authority.

Purpose: Let extensions resolve references safely through the app catalog and configured service adapters.
Context: `packages/web/src/modules/references.ts`; `crates/editac-core/tests/extension_references.rs`; `tests/extension-references.test.mjs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.5, EXT-1.6.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Opening/rendering references performs no implicit fetch or permission grant; ac identifiers and labels remain intact offline. Host-approved lookup handles revocation, stale/out-of-order results and deleted anchors without unauthorized insertion, secret exposure or stale UI activation.

Implementation:

- [ ] EXT-1.8-I1 Adapt the existing reference module to the shared catalog/authority capabilities and typed host resolver contract. Preserve explicit activation and label fallback; distinguish mutable identifiers from bearer credentials/content hashes and route edits through current session capabilities.

Validation:

- [ ] EXT-1.8-V1 cargo test -p editac-core --test extension_references --locked; node --test tests/extension-references.test.mjs. Use mocked resolver/auth results to assert no-call-on-open, forbidden targets, cancellation, stale result suppression and read-only behavior. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.8` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.8`.
Blocked behavior: Leave `EXT-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.9 — Measure optional extension loading boundaries

- [ ] EXT-1.9 Implement and validate measure optional extension loading boundaries.

Purpose: Keep disabled presenters out of minimal bundles while preserving their stored data.
Context: `tests/extension-bundles.test.mjs`; `scripts/`; `fixtures/extensions/consumers/`; `docs/extensions/footprint.md`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.2, EXT-1.7, EXT-1.8.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Packed minimal and enabled browser consumers have recorded JS/WASM/CSS/asset manifests; disabled optional presenter assets are absent and not implicitly requested. The default Task preset passes verification.md's 512 KB total / 32 KB editor JS gzip hard caps and reports the 256 KB total / 16 KB JS preferred-size results (KB = 1,000 bytes). Required lazy code, generated WASM glue and runtime dependencies count; enabled optional costs are reported separately. Native/TUI manifests identify optional dependencies honestly; size claims use actual artifacts and declared settings.

Implementation:

- [ ] EXT-1.9-I1 Extend existing module bundle checks to public imports and lazy presenter entry points. Apply the user-approved gzip hard caps and preferred sizes from verification.md; record measured baseline deltas and fail either default-profile hard-cap overrun or missing required artifact. Confirm enabled/disabled fallback behavior from the same descriptor fixtures.

Validation:

- [ ] EXT-1.9-V1 node --test tests/extension-bundles.test.mjs. Compare production artifact manifests/import traces, including referenced assets and unchanged fallback data; record exact builds and byte counts. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.9` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.9`.
Blocked behavior: Leave `EXT-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.10 — Ship an executable third-party extension tutorial

- [ ] EXT-1.10 Implement and validate ship an executable third-party extension tutorial.

Purpose: Show independent authors how to add a mark and atom through stable contracts.
Context: `examples/extensions/`; `docs/extensions/authoring.md`; `tests/extension-tutorial.test.mjs`; `fixtures/extensions/consumers/`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.4, EXT-1.5, EXT-1.6, EXT-1.9.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A clean consumer registers one data-defined mark and atom using public imports and unchanged engine/WASM/native artifacts. The examples pass shared conformance, preserve source/opaque data without renderers, and dispose resources. Documentation distinguishes data-defined behavior from new core editing semantics.

Implementation:

- [ ] EXT-1.10-I1 Write a minimal tutorial and fixtures for descriptor registration, optional presenter, codec/fallback, command use and conformance execution. Reuse existing build/pack machinery; explain host capability and migration obligations without introducing another package or plugin runtime.

Validation:

- [ ] EXT-1.10-V1 node --test tests/extension-tutorial.test.mjs against packed library artifacts. Verify no private imports or core rebuild, missing-renderer preservation, read-only behavior and cleanup; execute all documented commands in a prepared consumer. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.10` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.10`.
Blocked behavior: Leave `EXT-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task EXT-1.12 — Publish validated first-party configuration profiles

- [ ] EXT-1.12 Publish validated first-party configuration profiles.

Purpose: Publish validated first-party configuration profiles within the existing editor architecture.
Context: `packages/core/src/extensions/`; `fixtures/extensions/profiles/`; `tests/extension-profiles.test.mjs`; `../architecture/specs/extension-library.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: EXT-1.5, EXT-1.6, EXT-1.9.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: FPX-01–FPX-03 and FPX-05–FPX-08 qualify baseline/preset configuration, versions/conflicts, deterministic precedence, data-preserving disablement and lifecycle. Known contract fixtures stand in for future features; their real combinations remain downstream evidence.

Implementation:

- [ ] EXT-1.12-I1 Publish versioned core/document-tools/code-tools profile contracts and validate dependency/capability/precedence before activation. Reuse registry/conformance/lifecycle interfaces; wire downstream profiles when their features qualify, without claiming their current availability.

Validation:

- [ ] EXT-1.12-V1 node --test tests/extension-profiles.test.mjs. Permute legal order, inject duplicate/incompatible registration and callback failures, check absent-feature imports and repeated teardown in packed consumers. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `EXT-1.12` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `EXT-1.12`.
Blocked behavior: Leave `EXT-1.12` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task EXT-1.13 — Define formatting-preserving extension transfer codecs

- [ ] EXT-1.13 Define formatting-preserving extension transfer codecs.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `crates/editac-core/`; `fixtures/extensions/clipboard/`; `tests/extension-formatting.test.mjs`; `../architecture/specs/extension-library.md`; [native clipboard cases](../tests/native-clipboard-cases.md)
Dependencies: EXT-1.4, EXT-1.6, EXT-1.12.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Table, image, reference, math and other registered extension codecs declare supported inline/block formatting and preserve semantic data through copy/cut/paste, import/export and undo. Table cells preserve marks, links, code and paragraph styles plus admitted row/column/span/header metadata. Unknown or unavailable extensions preserve bounded inert source and show explicit fallback; no silent flattening, code/formula execution or asset fetch.

Implementation:

- [ ] EXT-1.13-I1 Extend codec descriptors with formatting capabilities and prepared-transfer entry points. Author portable conformance fixtures for mixed table-cell selections, nested inline content, captions, references/math, checked resource limits, version migration, absent presenters/codecs, plain paste and two-view/native transfer ownership. Make every presenter consume the same atomic prepared edit and formatting policy.

Validation:

- [ ] EXT-1.13-V1 `node --test tests/extension-formatting.test.mjs`. Use deterministic codecs and prepared data only; assert formatting, history, selection, failure atomicity and preserved-source fallback. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing tools/devices or skipped mandatory cases do not qualify support.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Never substitute simulation for physical-device evidence.

### Task EXT-1.11 — Record the public library integration handoff

- [ ] EXT-1.11 Implement and validate record the public library integration handoff.

Purpose: Give platform and final release tracks reproducible extension contracts and artifact evidence.
Context: `docs/extensions/`; `fixtures/extensions/capabilities.json`; `../architecture/evidence/extension-library.md`; `tests/extension-consumers.test.mjs`; `../architecture/specs/extension-library.md`.
Dependencies: EXT-1.7, EXT-1.8, EXT-1.9, EXT-1.10, EXT-1.12, EXT-1.13.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Public consumer checks pass at immutable revisions, required platform parity obligations are linked to owners/fixtures, and actual missing renderer/device evidence remains explicit. Library completion proves contracts/examples, not downstream native renderer or publication completion. Include validated official profile contracts and downstream owners for FPX-04 actual high-risk combinations; do not infer future feature or platform readiness from contract fixtures.

Implementation:

- [ ] EXT-1.11-I1 Assemble versioned public-interface documentation, conformance fixture hashes, built-in matrix, packed consumer artifacts and compatibility notes. Link downstream renderer obligations and final cross-client qualification without introducing a dependency cycle or reimplementing modules.

Validation:

- [ ] EXT-1.11-V1 node --test tests/extension-consumers.test.mjs; rerun only required affected library conformance checks and inspect the capability handoff for missing owners. Preserve failed evidence and report packaging/publication separately. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `EXT-1.11` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `EXT-1.11`.
Blocked behavior: Leave `EXT-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.

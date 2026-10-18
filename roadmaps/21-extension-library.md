# Expose the public portable extension library

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [the owning contract](../specs/extension-library.md), [shared client contracts](../specs/client-contracts.md) and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned implementation/test files are created by their task. Source is controller-owned; write checkmarks, state and evidence only in the separate progress file.

Upstream entry gates: `07-extension-modules.md` and `12-client-contracts.md` complete at current source revisions with passing artifact evidence; `05-markdown-content.md` passes the portable and simulator/emulator development level defined in verification.md, including FMT-1.12. Physical-or-virtual FMT-1.15-V1 remains a release gate. Cross-roadmap IDs are context references; dependencies below name only parents in this file. Do not launch implementation while an upstream gate is unavailable.

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
Acceptance: Packed minimal and enabled browser consumers have recorded JS/WASM/CSS/asset manifests; disabled optional presenter assets are absent and not implicitly requested. The default Task preset passes verification.md's 512 KiB total / 32 KiB editor JS gzip hard caps and reports the 256 KB total / 16 KB JS preferred-size results (KB = 1,000 bytes). Required lazy code, generated WASM glue and runtime dependencies count; enabled optional costs are reported separately. Native/TUI manifests identify optional dependencies honestly; size claims use actual artifacts and declared settings.

Implementation:

- [ ] EXT-1.9-I1 Extend existing module bundle checks to public imports and lazy presenter entry points. Apply the user-approved gzip hard caps and preferred sizes from verification.md; record measured baseline deltas and fail either default-profile hard-cap overrun or missing required artifact. Confirm enabled/disabled fallback behavior from the same descriptor fixtures.
- [ ] EXT-1.9-I2 Check the shared-resource rules in web.md for two enabled consumers of an optional parser/presenter and mixed enabled/disabled configurations: one static artifact graph/URL, isolated registration/mutable renderer state, owner-Document style lifetime and no requests on disabled-only pages. Mixed-page manifests report the enabled union and incremental costs. Reuse SDK-1.9/1.10's site harness when available; do not gate portable extension work on a downstream SDK task or add another runtime registry. FIT-1.6 requires the integrated exact-artifact receipt before making site-wide claims. Earlier EXT receipts remain historical until these additional cases are executed.

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

Mixed-configuration acceptance (2026-10-15): Loading common code for one profile does not register it in a sibling profile. Add simultaneous equal/mixed-profile fixtures with independent keymaps, permissions, history and teardown; configurations reuse common artifacts rather than generating profile-specific engine builds. Future profile features remain gated by their owning tasks. SDK-1.9/1.10 and FIT-1.6 qualify integration across frameworks/routes without treating prior profile-contract fixtures as shipped feature combinations.

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

- [ ] EXT-1.13-V1 `node --test tests/extension-formatting.test.mjs`. Use deterministic codecs and prepared data only; assert formatting, history, selection, failure atomicity and preserved-source fallback. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing required runtime tooling, failed behavior or untested mandatory cases do not qualify support; use accepted virtual runtimes/equivalents when physical hardware is unavailable.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Accept target-platform simulators/emulators/VMs under verification.md and retain virtual provenance; never relabel their results as physical-device observations.

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

## Extension DX follow-up — 2026-10-17

User-authorized additions to this existing roadmap; no separate extension DX track or runner is created. Read [the shared extension DX contract](../specs/extension-dx.md) and [32 planned acceptance cases](../tests/extension-dx-cases.md). Individual extension composition is primary; optional default/document presets are convenience configurations, not use-case restrictions. Keep the same execution, ownership, deterministic fixture, paid-inference, evidence and teardown rules as the original tasks.

Original task IDs, completed progress and qualification receipts are preserved. They do not complete these added parents. Previously qualified baseline prerequisites keep their original parent/artifact scope; new facade functionality requires the named new feature gates. Cross-roadmap feature gates refer to specific parents, not a whole expanded track that would introduce a dependency cycle. Adopt revised sources only at an owning controller's safe checkpoint; do not change active queues or start duplicate workers. Runtime, platform and release claims remain evidence-gated.

### Task EXT-1.14 — Freeze the public extension configuration contract

- [ ] EXT-1.14 Freeze the public extension configuration contract.

Purpose: Define the smallest consistent typed facade over existing public extension primitives.
Context: [DX contract](../specs/extension-dx.md); [case catalog](../tests/extension-dx-cases.md); `packages/web/src/extensions/`; `packages/core/src/extensions/`; `scripts/test-extension-dx.mjs`; `tests/extension-dx/contract.test.mjs`.
Dependencies: EXT-1.11.
Cross-roadmap feature gates: SDK-1.10, with exact applicable passing artifacts; these are parent-specific gates, not completion of an expanded downstream track.
Session scope: One public API/admission contract; split implementation delivery into the dependent parents below.
Acceptance: DXC-01/03/25/27: proposed names/options, extensions array, configure isolation, readiness, errors, dependencies/conflicts and legacy-option precedence have typed positive/negative fixtures. Distinguish behavior, data-defined marks/atoms and engine-semantic additions; no product-specific feature restrictions or arbitrary hot schema registration. Freeze configurable lightweight core-formatting options, independent opt-in collaboration/presence, no-provider local readiness and instance authority/history isolation. Declare operation/source/range interests and one-time conflict resolution for the existing runtime, without baseline per-keystroke registry scans.

Implementation:

- [ ] EXT-1.14-I1 Freeze versioned facade/authoring types and contract fixtures around existing registry/profile/session ports. Specify default/document convenience semantics and migration aliases, asset override, callback authority and required-ready versus command-lazy states. Create the fail-closed named-group test entry before running it.

Validation:

- [ ] EXT-1.14-V1 Run `npm run typecheck` and `node scripts/test-extension-dx.mjs --group contract`. Verify typed invalid configurations and independent admission expectations without fetching assets or mutating an attached document; record nonzero exact counts and immutable inputs.

Evidence: Separate EXT-1.14 progress links the API decision, fixtures, commands/counts and any upstream primitive gap.
Handoff: Last frozen interface, rejected alternative or exact missing prerequisite and next bounded change.
Blocked behavior: Keep EXT-1.14 unchecked; record source/error/prerequisite fingerprint, owner, attempted repair and exact resume condition. Do not restart unchanged failed work.

### Task EXT-1.15 — Expose approachable custom extension authoring primitives

- [ ] EXT-1.15 Expose approachable custom extension authoring primitives.

Purpose: Let authors express behavior, options and admitted data without implementing SDK plumbing.
Context: [Portable extension contract](../specs/extension-library.md); [DX contract](../specs/extension-dx.md#an-approachable-extension-authoring-api); `packages/web/src/extensions/`; `packages/core/src/extensions/`; `tests/extension-dx/authoring.test.mjs`.
Dependencies: EXT-1.14.
Cross-roadmap feature gates: SDK-1.11, with exact applicable passing artifacts; these are parent-specific gates, not completion of an expanded downstream track.
Session scope: A typed authoring facade and existing-port helpers, not arbitrary new editing semantics.
Acceptance: DXC-08/29: a behavior extension and admitted mark/atom use public Extension.create/configure-style APIs against unchanged engine artifacts. Authors receive bounded subscriptions, command/target and managed-resource helpers; callbacks cannot bypass readonly, preparation, atomic history or preservation. Platform and schema limits are explicit. Use existing indexed dispatch; empty, disabled and unrelated extensions have no callbacks or registry/document scans on input. Selection/format/structural patches and disposal retain correct interest filtering; configuration/admission runs once.

Implementation:

- [ ] EXT-1.15-I1 Implement typed options/defaults, commands, lifecycle, key/input/paste precedence, ephemeral decoration and cleanup integration using existing owners. Create original minimal behavior/mark/atom consumers and document explicit new-semantic/migration boundaries. Supply actionable diagnostics and exported declarations without private source imports. Add deterministic dispatch work counters and 0/1/10/100 unrelated-descriptor fixtures with corrupted broad-scan/unrelated-callback controls; reuse the current ModuleRuntime rather than introduce another dispatcher.

Validation:

- [ ] EXT-1.15-V1 Run `npm run typecheck`, `npm run build` and `node scripts/test-extension-dx.mjs --group authoring`. Check clean packed public imports, unchanged WASM hashes, invalid/duplicate definitions, readonly/failure/disposal and absent-presenter round trips with independent expected content. Assert DXC-29 work bounds, selection/format/structural filtering and negative-control sensitivity; timing qualification remains with FIT and SDK owners.

Evidence: EXT-1.15 progress links authoring types, public consumers, conformance results and platform limitations.
Handoff: Last helper/consumer, unavailable semantic primitive and next bounded action.
Blocked behavior: Keep EXT-1.15 unchecked with the exact owning API gap; do not expose raw CRDT writes or introduce a parallel state store.

### Task EXT-1.16 — Add bounded pattern matching and managed async resolution

- [ ] EXT-1.16 Add bounded pattern matching and managed async resolution.

Purpose: Make parsing plus host lookup plus safe prepared application reusable for custom extensions.
Context: [Matching contract](../specs/extension-dx.md#pattern-recognition-and-asynchronous-resolution); [link resolution](../specs/link-resolution.md); `packages/web/src/extensions/`; `tests/extension-dx/matching.test.mjs`.
Dependencies: EXT-1.15.
Session scope: One generic matching/resolution facility over existing input/anchor/command ports.
Acceptance: DXC-09/12/13: changed-range matching has bounded context, local/composition/code/link/literal policies, stable target capture, generation/authority/source revalidation, deduplication and bounded async work. It performs no speculative mutation or implicit lookup on remote changes/reopen/export. Reuse qualified LNK host resolution/cancellation contracts; missing shared behavior is an explicit owner gate.

Implementation:

- [ ] EXT-1.16-I1 Implement typed matcher/resolver/application hooks and managed transient status. Define input/paste trigger and undo suppression policies, principal-scoped cache limits, safe URL admission and current-text checks. Keep host credentials outside documents/logs and document trusted callback versus isolated worker execution.

Validation:

- [ ] EXT-1.16-V1 Run `node scripts/test-extension-dx.mjs --group matching`. Use deterministic delayed/denied/out-of-order resolvers and real engine anchors to verify bounded work, unchanged text/history on failure, unrelated-edit rebasing and zero stale/cross-instance effects. Record exact counts and inputs.

Evidence: EXT-1.16 progress links reusable hooks, resource bounds, independent race outcomes and LNK applicability.
Handoff: Last trigger/async boundary, failing target/authority case or upstream gap and next action.
Blocked behavior: Keep EXT-1.16 unchecked with a concrete resume condition; do not use raw offsets across awaits or sequential mutations to imitate atomic application.

### Task EXT-1.17 — Ship the verified issue-code linking recipe

- [ ] EXT-1.17 Ship the verified issue-code linking recipe.

Purpose: Demonstrate ASD-123 to task-link behavior with configuration and a small host resolver.
Context: [DX contract](../specs/extension-dx.md#pattern-recognition-and-asynchronous-resolution); [DXC cases](../tests/extension-dx-cases.md); `examples/extensions/task-links/`; `tests/extension-dx/task-links.test.mjs`.
Dependencies: EXT-1.16.
Session scope: One complete custom-reference/linking recipe using the generic facility, not a task-product dependency in core.
Acceptance: DXC-10/11/12/13/14: found tasks add one validated link over unchanged code text; not-found/denied/error/timeout never fabricate URLs or change history. Preserve adjacent formatting/selection, reject obsolete results, converge through peer updates and support undo/redo without immediate reapplication. The example has one public import/configuration and a prepared catalog resolver.

Implementation:

- [ ] EXT-1.17-I1 Add a canonical standalone recipe and fixed task catalog with explicit delimiter/paste/exclusion policy. Show standard link marks first and document the distinct optional persistent-reference representation. Expose transient loading/error states, cancellation and one-action history through existing helpers; no live task service, startup lookup or content upload.

Validation:

- [ ] EXT-1.17-V1 Run `node scripts/test-extension-dx.mjs --group task-links` using packed modules, real input/engine history/peer paths and mocked task responses. Assert before/after text/marks/history and request counts for found/not-found/stale/undo/dispose cases in the named browsers; record nonzero counts and teardown.

Evidence: EXT-1.17 progress links the downloadable recipe, exact configured API, task fixtures and independent behavior outcomes.
Handoff: Last verified scenario, remaining browser/input boundary and next bounded action.
Blocked behavior: Keep EXT-1.17 unchecked with the exact matcher/command prerequisite; do not replace lookup with URL interpolation or claim a fixture resolver is production integration.

### Task EXT-1.18 — Prefer platform spellcheck with an optional custom recipe

- [ ] EXT-1.18 Prefer platform spellcheck with an optional custom recipe.

Purpose: Reuse browser/user spelling facilities by default and prove an explicit optional checker without new committed document semantics.
Context: [Spelling contract](../specs/extension-dx.md#spell-checking-custom-parsing-and-url-insertion); `examples/extensions/spellcheck/`; `tests/extension-dx/spellcheck.test.mjs`. [Platform editing contract](../specs/platform-editing-services.md); [ENV variants](../tests/platform-editing-cases.md).
Dependencies: EXT-1.15.
Cross-roadmap feature gates: SDK-1.12, with exact applicable passing artifacts; these are parent-specific gates, not completion of an expanded downstream track.
Session scope: One browser platform/off/custom policy adapter and prepared custom-checker recipe. Reuse existing input/history primitives; native implementation and platform-wide observations remain with their named owners.
Acceptance: DXC-15/16 and ENV-01–06 pass: default platform reuse respects user/inherited settings; off and explicit custom modes preserve independent autocorrection and report unknown/unsupported or coupled traits. No inferred setting or unavailable locale triggers forced enablement/custom fallback. Platform/off load no checker/dictionary/worker; custom presentation avoids unapproved overlap. Accepted current corrections make one prepared replacement with formatting/selection/shared undo; stale analysis does nothing. Preserve composition, code exclusions, instance isolation and disposal. No hosted checker is required. Actual browser observations remain mandatory under INT-1.14, with native control evidence owned separately.

Implementation:

- [ ] EXT-1.18-I1 Provide one-import platform/off/custom policy with separate autocorrection, host preference preservation and capability diagnostics. Reuse native browser spelling presentation; provide a tiny prepared dictionary/mock checker only for explicit custom mode, with managed async work and accessible suggestions. Reuse replacement/decoration/history ports, preserve user settings on reconfiguration/disposal, and document locale/Unicode/exclusion and coupled-control limits. Supply the actual-browser runbook and record upstream gaps rather than duplicating missing primitives.

Validation:

- [ ] EXT-1.18-V1 Run `node scripts/test-extension-dx.mjs --group spellcheck`. Execute ENV-01–06 and correction/history aspects of ENV-07 with prepared checker data through the real engine: user-default preservation, off/custom/autocorrection combinations, unavailable/unknown locale/provider, asset absence, overlap handling, Unicode/composition, current/stale acceptance, readonly, selection/formatting, one undo/redo and teardown. Assert emitted effects/request counts and mode/instance isolation. Hand off the exact browser fixture/runbook to INT-1.14; synthetic events alone do not establish platform support.

Evidence: EXT-1.18 progress links the recipe, dictionary/checker scope, decoration outcomes and correction evidence.
Handoff: Last suggestion/input/resource case, unavailable primitive or exact failure and next action.
Blocked behavior: Keep EXT-1.18 unchecked; do not persist spelling decorations as semantic marks or call a paid/production provider to bypass missing fixtures.

### Task EXT-1.19 — Ship custom parsing and URL insertion recipes

- [ ] EXT-1.19 Ship custom parsing and URL insertion recipes.

Purpose: Show third parties how to map small source formats and host-resolved URLs to existing semantic commands.
Context: [Parsing contract](../specs/extension-dx.md#spell-checking-custom-parsing-and-url-insertion); [formats](../specs/formats.md); `examples/extensions/parsing/`; `examples/extensions/url-insert/`; `tests/extension-dx/parsing.test.mjs`.
Dependencies: EXT-1.15, EXT-1.16.
Session scope: Two small recipes over the same existing prepared transfer/command boundary; no new general parser or schema.
Acceptance: DXC-17/18: a bounded declared source syntax prepares one admitted fragment, with literal bypass, precedence and retained unsupported source. URL insertion applies only safe authorized results at a current target; absent custom-reference presenters retain fallback. No raw DOM mutation, automatic public-fetch fallback or new writable model.

Implementation:

- [ ] EXT-1.19-I1 Provide canonical small parser and URL-insert consumers through the public authoring helpers and configured host resolver. Define grammar/input limits, diagnostics, source recovery, current target validation and undo; document codec versus input-rule versus custom-reference choices and reuse owning FMT/LNK fixtures where applicable.

Validation:

- [ ] EXT-1.19-V1 Run `node scripts/test-extension-dx.mjs --group parsing`. Check accepted/literal/unsupported/oversized input, safe/unsafe/not-found URLs, cancellation/stale targets, one atomic history result and unknown-data fallback against independent semantic expectations; record counts and exact consumers.

Evidence: EXT-1.19 progress links both original recipes, grammar and resolution policy plus conformance outcomes.
Handoff: Last source/URL case, exact missing codec/command prerequisite and next bounded action.
Blocked behavior: Keep EXT-1.19 unchecked with the owner/resume condition; do not mutate before validation or advertise unsupported parsing as a successful conversion.

### Task EXT-1.20 — Document the extension API and executable authoring recipes

- [ ] EXT-1.20 Document the extension API and executable authoring recipes.

Purpose: Make supported custom extension creation understandable from public documentation and working examples.
Context: [DX documentation contract](../specs/extension-dx.md#documentation-and-delivery-evidence); [public docs](../specs/public-docs-demo.md); `docs/extensions/`; `examples/extensions/`; `tests/extension-dx/documentation.test.mjs`.
Dependencies: EXT-1.15, EXT-1.17, EXT-1.18, EXT-1.19.
Cross-roadmap feature gates: SDK-1.12, with exact applicable passing artifacts; these are parent-specific gates, not completion of an expanded downstream track.
Session scope: Canonical SDK authoring guide and source manifest; public site rendering remains DOC-1.34/1.35 ownership.
Acceptance: DXC-22: getting started uses one import/configuration; API reference and original behavior/mark/atom, ASD-123, spelling, parser and URL recipes explain options, before/after results, errors, async cancellation, history and cleanup. Supported interfaces are exact and typed, advanced hosting is separate, and no planned facade is presented as already executable.

Implementation:

- [ ] EXT-1.20-I1 Write canonical extension selection/configuration, Extension.create authoring, lifecycle/input/command/codec/decoration and migration guides from validated consumers. Add a recipe/source/version manifest for DOC-1.34/1.35 reuse and a small third-party packaging/conformance guide. Explain unchanged-WASM data extensions versus new Rust semantics and host/platform limits.

Validation:

- [ ] EXT-1.20-V1 Run `node scripts/test-extension-dx.mjs --group documentation` against installed tarballs. Compile and execute documented source ranges, reject private imports and stale manifest/options, and compare independent recipe outcomes including failures and disposal; record exact counts and identities.

Evidence: EXT-1.20 progress links canonical pages, recipe source ranges, package versions and runnable drift checks.
Handoff: Last documented surface, exact unavailable example or public-site downstream owner and next action.
Blocked behavior: Keep EXT-1.20 unchecked where an advertised recipe lacks an artifact; label conceptual material and do not substitute configuration-only snippets for working behavior.

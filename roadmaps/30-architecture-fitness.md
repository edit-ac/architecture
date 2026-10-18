# Enforce maintainable ecosystem boundaries

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

Physical follow-up sequencing (user decision, 2026-10-18): transfer deferred physical-only observations to [roadmap 43](43-physical-device-verification.md) after development. Accepted target-platform virtual checks and tested equivalents remain valid; no physical device is required to finish this development roadmap. Failed implementation, virtual input/semantic checks and applicable performance budgets remain blockers. Preserve original case IDs and historical evidence; do not mark deferred physical runs passed.

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/ecosystem-maintainability.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: `08-sdk-integration.md`, `12-client-contracts.md`, `21-extension-library.md` at reviewed immutable source/implementation revisions with passing evidence.  Local Dependencies fields refer only to this file.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration, with its implementation and validation substeps. Read task-local context rather than the complete ecosystem. Create named checks before invoking them; unknown suites, zero matches and skipped platforms cannot pass. Use deterministic fixtures and prepared transports, no live model/provider calls or paid inference. Do not load `.secrets`. Missing toolchains or upstream evidence block only their dependent tasks. Do not launch another controller or publish outside a named release task.

## Epic FIT-1 — Enforce maintainable ecosystem boundaries

### Task FIT-1.1 — Freeze and check dependency-layer ownership

- [ ] FIT-1.1 Freeze and check dependency-layer ownership.

Purpose: Freeze and check dependency-layer ownership as one bounded integration or qualification boundary.
Context: `contracts/layers.json`; `scripts/check-architecture.mjs`; `tests/architecture/layers/`; `../architecture/specs/ecosystem-maintainability.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Engine and minimum SDK imports exclude UI/network/cloud/conversion/highlighting runtime dependencies; intended companions remain explicit. WCF-18: Negative graph fixtures reject unclassified production packages, forbidden transitive/default-feature reachability and test helpers on runtime edges; allowed optional/test-only controls pass.

Implementation:

- [ ] FIT-1.1-I1 Create the manifest-driven fitness dispatcher and graph adapters for Cargo/JS package imports; seed a forbidden-layer negative fixture and reject unknown/zero suites.

Validation:

- [ ] FIT-1.1-V1 `node scripts/check-architecture.mjs --suite layers`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified. Execute the named WCF-18 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Separate progress entry `FIT-1.1` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.2 — Define the shared capability and compatibility schema

- [ ] FIT-1.2 Define the shared capability and compatibility schema.

Purpose: Define the shared capability and compatibility schema as one bounded integration or qualification boundary.
Context: `contracts/capabilities.schema.json`; `contracts/profiles/`; `tests/architecture/profiles/`; `../architecture/specs/ecosystem-maintainability.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: FIT-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Available/enabled/authorized/qualified states are distinct; converter directions and version/evidence identities are validated. WCF-17: Derive command/surface consistency checks from existing descriptors and bindings; reject missing IDs/conflicting aliases and stale support evidence without a duplicate semantic registry. Route existence never establishes current permission or executed qualification.

Implementation:

- [ ] FIT-1.2-I1 Create the small schema and migrate duplicate capability vocabulary without inventing extra runtime services. Include unknown-version/read-preservation and permission-not-capability negative cases.

Validation:

- [ ] FIT-1.2-V1 `node scripts/check-architecture.mjs --suite profiles`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified. Execute the named WCF-17 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Separate progress entry `FIT-1.2` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.3 — Integrate native and release profile producers

- [ ] FIT-1.3 Integrate native and release profile producers.

Purpose: Integrate native and release profile producers as one bounded integration or qualification boundary.
Context: `native/*/capability.json`; `scripts/release-profile.mjs`; `tests/architecture/profile-producers/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: FIT-1.2.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Existing producer outputs map to the shared schema; missing required runtime/equivalent evidence cannot become a supported native claim; physical/manual availability alone is not a blocker under verification.md.

Implementation:

- [ ] FIT-1.3-I1 Add shared validation adapters and fixture producers for pending platforms; actual native records are admitted only after their own platform qualification. Define consumer format for docs/demo/cloud.

Validation:

- [ ] FIT-1.3-V1 `node scripts/check-architecture.mjs --suite profile-producers`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `FIT-1.3` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.4 — Unify bounded asynchronous service lifecycles

- [ ] FIT-1.4 Unify bounded asynchronous service lifecycles.

Purpose: Unify bounded asynchronous service lifecycles as one bounded integration or qualification boundary.
Context: `crates/editac-session/`; `packages/web/src/services/`; `tests/architecture/service-lifecycle/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: FIT-1.2.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Cancellation/disposal, stale revision, replaced session, permission loss and queue saturation behave consistently without dropping acknowledged work.

Implementation:

- [ ] FIT-1.4-I1 Qualify the repeated service envelope in actual highlight/asset/resolver/conversion ports as they become available; supply deterministic contract providers first and register real adapters at their tracks.

Validation:

- [ ] FIT-1.4-V1 `node scripts/check-architecture.mjs --suite service-lifecycle`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `FIT-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.5 — Qualify supported upgrade and rollback combinations

- [ ] FIT-1.5 Qualify supported upgrade and rollback combinations.

Purpose: Qualify supported upgrade and rollback combinations as one bounded integration or qualification boundary.
Context: `fixtures/compatibility/`; `tests/architecture/compatibility/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: FIT-1.2.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Exact previous/current schema, wire, descriptor, public API and ABI combinations recover or reject with explicit migration/export outcomes.

Implementation:

- [ ] FIT-1.5-I1 Build immutable version fixtures and compatibility policy; include unknown extension data and persisted newer-schema rollback. Do not claim every historical version is supported.

Validation:

- [ ] FIT-1.5-V1 `node scripts/check-architecture.mjs --suite compatibility`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `FIT-1.5` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.6 — Check independent consumer and optional-loading boundaries

- [ ] FIT-1.6 Check independent consumer and optional-loading boundaries.

Purpose: Check independent consumer and optional-loading boundaries as one bounded integration or qualification boundary.
Context: `tests/consumers/`; `tests/architecture/loading/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: FIT-1.1, FIT-1.2.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Packed consumers work without workspace aliases; disabled heavy format/highlighting/cloud dependencies stay outside minimal loading. Default Task browser artifacts pass verification.md's 512 KiB total / 32 KiB editor JS gzip hard caps, including required lazy code, WASM glue and runtime dependencies; missing measurements or either overrun fail qualification. Report preferred-size results against 256 KB total / 16 KB JS and enabled optional costs separately (KB = 1,000 bytes).

Implementation:

- [ ] FIT-1.6-I1 Extend existing package/FFI consumer harnesses with import graph and artifact-byte checks; consume the shared gzip counting/cap assertions from verification.md/SDK-1.8 and report preferred-size status without duplicating the measurement harness. Scope semver checks to exported public contracts and actual supported consumer versions.
- [ ] FIT-1.6-I2 Consume SDK-1.10's exact-artifact SHR-01–SHR-08 receipt for task-description/comment mounts and task-description/document routes. Check one compatible resolved runtime/common chunk graph, single-flight initialization, instance/preset/permission isolation, shared asset teardown and separate same-realm versus HTTP-cache behavior. Reuse SDK-1.9/1.10's fixtures and duplicate-asset/eager-import negative controls; missing cases or stale build identities fail this added gate. Preserve earlier FIT receipts and adopt amended source only at a safe controller checkpoint; old single-consumer passes cannot qualify the new matrix.

Validation:

- [ ] FIT-1.6-V1 `node scripts/check-architecture.mjs --suite consumers-loading`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Shared-resource acceptance (2026-10-15): The same command verifies the added receipt and detector sensitivity, standalone default caps, mixed-page union/incremental costs and cold/warm route results under [web.md](../specs/web.md#shared-resources-across-editors-and-site-routes). A passing unit loader or cache-hidden duplicate is insufficient. Create/extend the receipt checks before invocation; no new harness or numeric budget is implied.

Evidence: Separate progress entry `FIT-1.6` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.7 — Record dependency and license maintenance evidence

- [ ] FIT-1.7 Record dependency and license maintenance evidence.

Purpose: Record dependency and license maintenance evidence as one bounded integration or qualification boundary.
Context: `scripts/check-dependencies.mjs`; `licenses/`; `tests/architecture/dependencies/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: FIT-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Release inventory covers optional native/WASM/font/grammar/media components with exact revisions/notices; unavailable advisory sources are explicit.

Implementation:

- [ ] FIT-1.7-I1 Generate dependency inventories from locks and artifact manifests, document update owners and run current advisory/license checks. Use negative fixtures for missing notices; do not invent certification.

Validation:

- [ ] FIT-1.7-V1 `node scripts/check-dependencies.mjs --check`; `node scripts/check-architecture.mjs --suite dependencies`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `FIT-1.7` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.8 — Establish feature-aware performance and accessibility gates

- [ ] FIT-1.8 Establish feature-aware performance and accessibility gates.

Purpose: Establish feature-aware performance and accessibility gates as one bounded integration or qualification boundary.
Context: `benchmarks/profiles/`; `contracts/profiles/`; `tests/architecture/budgets/`; `../architecture/specs/ecosystem-maintainability.md`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: FIT-1.3, FIT-1.6.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Metrics include feature set, sizes, hardware and raw samples; review limits before measurement and do not pass skipped or incomparable data. PRF-01–PRF-07 add input-to-visible attribution, continuous drag/scroll frame traces, native text-service costs, changed-region scaling, queue bounds and repeated-disposal memory. Preserve existing budgets; report raw comparable samples and inconclusive results without claiming universal performance.

Implementation:

- [ ] FIT-1.8-I1 Extend existing verification profile with measured optional loading, incremental invalidation, peak memory, table/highlighter and accessibility evidence inputs. Record unavailable target platforms honestly.

Validation:

- [ ] FIT-1.8-V1 `node scripts/check-architecture.mjs --suite budgets`; run owning feature/platform benchmark commands named in the profile. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `FIT-1.8` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task FIT-1.9 — Qualify redacted diagnostics and failure taxonomy

- [ ] FIT-1.9 Qualify redacted diagnostics and failure taxonomy.

Purpose: Qualify redacted diagnostics and failure taxonomy as one bounded integration or qualification boundary.
Context: `crates/editac-session/src/diagnostics.rs`; `tests/architecture/diagnostics/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: FIT-1.4.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Support artifacts expose bounded IDs/timing/error/durability state but no seeded document text, private titles, tokens or keys.

Implementation:

- [ ] FIT-1.9-I1 Define stable error categories and privacy-preserving debug export; test failure recovery routing across store, resolver, converter and host adapters with prepared sources.

Validation:

- [ ] FIT-1.9-V1 `node scripts/check-architecture.mjs --suite diagnostics`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `FIT-1.9` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `FIT-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

## Extension DX follow-up — 2026-10-17

User-authorized additions to this existing roadmap; no separate extension DX track or runner is created. Read [the shared extension DX contract](../specs/extension-dx.md) and [32 planned acceptance cases](../tests/extension-dx-cases.md). Individual extension composition is primary; optional default/document presets are convenience configurations, not use-case restrictions. Keep the same execution, ownership, deterministic fixture, paid-inference, evidence and teardown rules as the original tasks.

Original task IDs, completed progress and qualification receipts are preserved. They do not complete these added parents. Previously qualified baseline prerequisites keep their original parent/artifact scope; new facade functionality requires the named new feature gates. Cross-roadmap feature gates refer to specific parents, not a whole expanded track that would introduce a dependency cycle. Adopt revised sources only at an owning controller's safe checkpoint; do not change active queues or start duplicate workers. Runtime, platform and release claims remain evidence-gated.

### Task FIT-1.10 — Measure facade costs and qualify compressed delivery

- [ ] FIT-1.10 Measure facade costs and qualify compressed delivery.

Purpose: Establish exact initial/deferred costs, dispatch baseline attribution and real compressed asset delivery using the existing accounting and performance producers.
Context: [Byte budgets](../specs/verification.md#browser-bundle-size-budgets); [size contract](../specs/extension-dx.md#size-reduction-and-compression); `scripts/check-browser-size.mjs`; `scripts/browser-size-contract.mjs`; `tests/extension-dx/size.test.mjs`.
Dependencies: FIT-1.6.
Cross-roadmap feature gates: SDK-1.12, with exact applicable passing artifacts; these are parent-specific gates, not completion of an expanded downstream track.
Session scope: Facade cost attribution and local HTTP compression proof using existing producers; candidate optimization remains SDK-1.13 and full workload qualification remains FIT-1.11.
Acceptance: DXC-19/20/26/29: baseline, individual extensions, representative combinations and shared-site unions record raw/gzip/Brotli, initial/deferred/combined assets and hashes. Required lazy code counts and existing caps remain enforced. Local HTTP proves negotiation/MIME/Vary/cache/uncompressed fallback and byte identity; request absence and duplicate controls fail when corrupted. Include disabled collaboration retained-code/provider/request/work counters and direct-port/facade dispatch baselines. Freeze numerical per-workload latency/regression limits, sampling and environment before SDK-1.13 candidate runs under the [performance contract](../specs/verification.md#extension-dispatch-and-jswasm-performance).

Implementation:

- [ ] FIT-1.10-I1 Extend existing packed inventory/shared-resource producers for facade entries, per-format/dictionary assets and compression behavior. Pin exact inputs, compressor settings, server headers and browser cache provenance. Attribute JS/glue/WASM/parser/asset retention and preserve default Task capability equivalence; separately report any new generic preset inventory. Create the fail-closed performance group over existing benchmark/input producers, operation/source/range counters and 0/1/10/100 unrelated-extension fixtures. Export immutable baseline/profile receipts for SDK-1.13; this group must not depend on downstream SDK-1.13/FIT-1.11 results.

Validation:

- [ ] FIT-1.10-V1 Run `npm run check:browser-size` with a unique absolute evidence output directory and `node scripts/test-extension-dx.mjs --group size`. Run the created `node scripts/test-extension-dx.mjs --group performance` baseline/work-count checks. Execute local compressed delivery and cold/warm consumer checks, retain raw inventories/negative controls and record nonzero counts, hard/preferred results and teardown. Unavailable optional features retain explicit pending cells.

Evidence: FIT-1.10 progress links immutable production inventories, byte attribution, delivery headers and budget results.
Handoff: Largest measured contributors, current headroom, pending feature cells and next concrete reduction hypothesis.
Blocked behavior: Keep missing admission unchecked; do not exclude required lazy code, change caps or substitute Brotli for gzip admission.

### Task FIT-1.11 — Qualify clean consumers and extension composition

- [ ] FIT-1.11 Qualify clean consumers and extension composition.

Purpose: Verify the complete DX from an external integrator's installed packages.
Context: [Case catalog](../tests/extension-dx-cases.md); [shared resources](../specs/web.md#shared-resources-across-editors-and-site-routes); `tests/extension-dx/consumers.test.mjs`; `tests/architecture/`; `examples/`.
Dependencies: FIT-1.10, FIT-1.6.
Cross-roadmap feature gates: SDK-1.11, SDK-1.12, EXT-1.17, EXT-1.18, EXT-1.19, SDK-1.13, EXT-1.20, with exact applicable passing artifacts; these are parent-specific gates, not completion of an expanded downstream track.
Session scope: Reuse existing pinned plain/React/Astro and shared-resource producers; do not create another framework editor harness.
Acceptance: DXC-07/22/23/24/27/28/29/30/32: clean public-import consumers configure independent features with no workspace aliases, private initialization or duplicated engines. Baseline/individual/risk-selected combinations cover input/keymaps, async races, history, unknown data, readonly and remount/routes. Required coverage and platform/feature limits are explicit; no release claim follows merely from source compilation. Qualify mixed local/collaborative editors, independently disabled presence, direct-port/facade and heavy-feature workloads against the frozen FIT-1.10 latency/work profile. Include cold first edit, warm activation, input-to-visible p50/p95/p99, remote bursts and repeated-disposal memory; preserve per-workload failures and inconclusive noise.

Implementation:

- [ ] FIT-1.11-I1 Extend the current installed-tarball and canonical architecture admission with facade/authoring/recipe identities, typed options, isolated feature composition and shared load/disposal proofs. Record selection rationale and uncovered combinations, plus eager-import, stale-result, duplicate-runtime and documentation-drift negative controls, plus unrelated-callback, full-document-input-export, whole-registry-scan and per-character JS/WASM-call controls. Reuse the existing real browser input and performance producers, including selected wrapper state and small-input/batched-work comparisons. Feed applicable receipts to FIT-1.6 and DOC owners without rewriting historical qualification.

Validation:

- [ ] FIT-1.11-V1 Run `node scripts/test-extension-dx.mjs --group consumers`, `node scripts/test-extension-dx.mjs --group performance`, the affected existing packed framework/shared-resource checks and `node scripts/check-architecture.mjs --suite consumers-loading`. Use real compiled engine/input/storage with deterministic resolver/checker services; retain exact browser/package/input hashes, nonzero counts, failures/skips, byte admission and teardown.

Evidence: FIT-1.11 progress links complete case ownership, clean consumers, independent outcomes, inventories and downstream handoff.
Handoff: Last composition/runtime cell, explicit unsupported combinations or release/platform obligation and exact next owner.
Blocked behavior: Keep unmet required cells unchecked with task/source/error/prerequisite fingerprint; do not waive failure/skip, claim native parity or publish packages to complete this parent.

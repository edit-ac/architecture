# Enforce maintainable ecosystem boundaries

Status: IN_PROGRESS

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

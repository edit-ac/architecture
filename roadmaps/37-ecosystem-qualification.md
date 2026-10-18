# Qualify the expanded editor ecosystem

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

Physical follow-up sequencing (user decision, 2026-10-18): transfer deferred physical-only observations to [roadmap 43](43-physical-device-verification.md) after development. Accepted target-platform virtual checks and tested equivalents remain valid; no physical device is required to finish this development roadmap. Failed implementation, virtual input/semantic checks and applicable performance budgets remain blockers. Preserve original case IDs and historical evidence; do not mark deferred physical runs passed.

## Goal and entry conditions

Workspace: `core`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/ecosystem-maintainability.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: `20-product-scenarios.md`, `25-rich-content-extensions.md`, `26-link-resolution.md`, `27-document-conversion.md`, `28-cloud-document-store.md`, `30-architecture-fitness.md`, `31-ios-extension-integration.md`, `32-android-extension-integration.md`, `33-macos-extension-integration.md`, `34-windows-extension-integration.md`, `35-linux-extension-integration.md`, `36-terminal-extension-integration.md`, `39-assistive-input.md`, `41-mobile-web-extensions.md` at reviewed immutable source/implementation revisions with passing evidence.  Local Dependencies fields refer only to this file.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration, with its implementation and validation substeps. Read task-local context rather than the complete ecosystem. Create named checks before invoking them; unknown suites, zero matches and skipped platforms cannot pass. Use deterministic fixtures and prepared transports, no live model/provider calls or paid inference. Do not load `.secrets`. Missing toolchains or upstream evidence block only their dependent tasks. Do not launch another controller or publish outside a named release task.

## Epic EQL-1 — Qualify the expanded editor ecosystem

### Task EQL-1.1 — Freeze the expanded release matrix

- [ ] EQL-1.1 Freeze the expanded release matrix.

Purpose: Freeze the expanded release matrix as one bounded integration or qualification boundary.
Context: `contracts/profiles/expanded.json`; `tests/scenarios/run.mjs`; `../architecture/specs/ecosystem-maintainability.md`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Every requested feature maps to an actual package/client/direction and upstream evidence revision; unknown or skipped mandatory cells fail. Review the additional desktop/native/official-preset case inventory and bind applicable release profiles; source-only cases remain planned.

Implementation:

- [ ] EQL-1.1-I1 Extend the existing20 scenario dispatcher and release profile with25–28 and30–36 inputs; docs29 evidence remains pending until EQL-1.7; separate base, expanded and optional encrypted profiles and retain prior failures.

Validation:

- [ ] EQL-1.1-V1 `node tests/scenarios/run.mjs expanded-matrix`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.1` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.2 — Qualify rich content and interaction scenarios

- [ ] EQL-1.2 Qualify rich content and interaction scenarios.

Purpose: Qualify rich content and interaction scenarios as one bounded integration or qualification boundary.
Context: `tests/scenarios/rich-content/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Code, tables, assets/embeds, slash/reorder and references work on web and all five native clients with the agreed semantics and actual UI.

Implementation:

- [ ] EQL-1.2-I1 Run shared document fixtures and real client interaction evidence, including readonly/undo, disconnect, composition and accessible non-drag movement; no fallback counts as rich editing.

Validation:

- [ ] EQL-1.2-V1 `node tests/scenarios/run.mjs expanded-rich-content`; use each31–35 actual OS consumer artifact. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.2` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.3 — Qualify link privacy and cloud authorization

- [ ] EQL-1.3 Qualify link privacy and cloud authorization.

Purpose: Qualify link privacy and cloud authorization as one bounded integration or qualification boundary.
Context: `tests/scenarios/link-cloud-security/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Cross-tenant/private metadata cannot leak through previews, caches, redirects, assets or reconnect; public auto mode remains useful within policy.

Implementation:

- [ ] EQL-1.3-I1 Combine26 and28 real adapters with adversarial prepared services and principal changes. Check denied internal links never reach public metadata fetching.

Validation:

- [ ] EQL-1.3-V1 `node tests/scenarios/run.mjs expanded-link-cloud`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.3` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.4 — Qualify format interoperability and source preservation

- [ ] EQL-1.4 Qualify format interoperability and source preservation.

Purpose: Qualify format interoperability and source preservation as one bounded integration or qualification boundary.
Context: `tests/scenarios/document-formats/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Claimed import/export directions meet their fidelity tier, report loss and preserve unsupported source; PDF is export-only on every client.

Implementation:

- [ ] EQL-1.4-I1 Run27 fixtures through web/native/CLI wrappers, validate rendered PDF output separately from layout, and verify cancel/failure leaves original content/output intact.

Validation:

- [ ] EQL-1.4-V1 `node tests/scenarios/run.mjs expanded-formats`; execute the qualified independent document/PDF output validators from27 evidence. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.5 — Qualify feature-aware performance and accessibility

- [ ] EQL-1.5 Qualify feature-aware performance and accessibility.

Purpose: Qualify feature-aware performance and accessibility as one bounded integration or qualification boundary.
Context: `benchmarks/profiles/expanded/`; `tests/scenarios/expanded-accessibility/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.2, EQL-1.4.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Measured minimum/expanded loading, large code/table behavior and actual OS accessibility meet reviewed limits; runtime bounds cannot waive data safety.

Implementation:

- [ ] EQL-1.5-I1 Aggregate raw feature samples and per-platform31–36 evidence; fix regressions with focused cases before widening the supported envelope.

Validation:

- [ ] EQL-1.5-V1 `node tests/scenarios/run.mjs expanded-performance`; `node tests/scenarios/run.mjs expanded-accessibility`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.5` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.6 — Verify cloud deployment readiness and recovery evidence

- [ ] EQL-1.6 Verify cloud deployment readiness and recovery evidence.

Purpose: Verify cloud deployment readiness and recovery evidence as one bounded integration or qualification boundary.
Context: `services/document-store/`; `docs/cloud-readiness.md`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.3.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Local reference conformance is distinguished from a production provider claim; deployment config, restore, tenancy and durable-receipt failure cases are reproducible.

Implementation:

- [ ] EQL-1.6-I1 Inspect28 service/adapter artifacts and deployment runbook. Qualify a real configured provider only under its actual deployment authorization; leave unspecified providers unsupported rather than inventing production evidence.

Validation:

- [ ] EQL-1.6-V1 `node tests/scenarios/run.mjs expanded-cloud-readiness`; require the declared provider-specific checks for any claimed production target. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.6` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.7 — Verify public docs and demo against the expanded profile

- [ ] EQL-1.7 Verify public docs and demo against the expanded profile.

Purpose: Verify public docs and demo against the expanded profile as one bounded integration or qualification boundary.
Context: `../docs/releases/site.json`; `contracts/profiles/expanded.json`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.2, EQL-1.3, EQL-1.4, EQL-1.5, EQL-1.9.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: The actual public site/demo uses the same immutable SDK/profile and accurately presents platform/format/cloud limits.

Implementation:

- [ ] EQL-1.7-I1 External task gate: require DOC-1.14 completion at the candidate/profile revisions from EQL-1.9. Consume29 deployment evidence, check generated tables/snippets, and verify real public fixture editing and export. Keep unavailable/optional backend modes clearly labeled.

Validation:

- [ ] EQL-1.7-V1 `node tests/scenarios/run.mjs expanded-public-delivery`; run the docs deployment check against its recorded URL. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.7` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task EQL-1.8 — Release the qualified expanded ecosystem profile

- [ ] EQL-1.8 Release the qualified expanded ecosystem profile.

Purpose: Release the qualified expanded ecosystem profile as one bounded integration or qualification boundary.
Context: `scripts/release-profile.mjs`; `docs/releases/`; `licenses/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: EQL-1.5, EQL-1.6, EQL-1.7.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Published artifacts, notices, migration notes, source/package hashes and consumer evidence agree. No unqualified platform or encryption capability is advertised.

Implementation:

- [ ] EQL-1.8-I1 Promote the same immutable candidate artifacts published by EQL-1.9 through the existing qualified release process, without rebuilding or republishing an existing version; then publish the expanded profile and final release labels. Any artifact change requires affected qualification and docs/demo rechecks. Optional protected extensions additionally require the expanded24 gate.

Validation:

- [ ] EQL-1.8-V1 `node scripts/release-profile.mjs --check`; `node tests/scenarios/run.mjs expanded-release`; verify exact registry/distribution artifacts using clean consumers. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `EQL-1.8` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `EQL-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.


### Task EQL-1.9 — Publish immutable expanded release candidates

- [ ] EQL-1.9 Publish immutable expanded release candidates.

Purpose: Supply real immutable artifacts to public documentation and demo consumers before final promotion.
Context: `scripts/release-profile.mjs`; `release/candidates/`; `../architecture/specs/packages-release.md`; `../architecture/specs/public-docs-demo.md`.
Dependencies: EQL-1.5, EQL-1.6.
Session scope: One reviewed candidate publication boundary plus clean-consumer checks; split artifact families before exceeding a bounded session.
Acceptance: Exact versions, integrity, notices, capability limits and source/build provenance are recorded. Real candidate artifacts are available under the qualified prerelease channel; no empty placeholder or unqualified API is published. Candidate labeling does not claim final expanded support.

Implementation:

- [ ] EQL-1.9-I1 Use existing release gates to build and publish actual changed artifacts under the intended prerelease channel (`next` for npm) and immutable native/CLI candidate assets. Record public package/download identities and clean-consumer results. DOC-1.6/1.10/1.13 consume these candidates; EQL-1.7 waits for DOC-1.14 before EQL-1.8 promotion. The docs source is not a whole-track entry prerequisite for this roadmap.

Validation:

- [ ] EQL-1.9-V1 `node scripts/release-profile.mjs --check`; extend and run `node tests/scenarios/run.mjs expanded-candidate-consumers`. Verify exact downloaded/registry versions and hashes in clean consumers; record nonzero tests, failures/skips, source/profile revisions and publication receipts.

Evidence: Separate progress entry `EQL-1.9` records artifact identities, receipts, profile revisions and immutable consumer evidence.
Handoff: Last verified artifact, remaining publication or consumer check, and next bounded action.
Blocked behavior: Leave `EQL-1.9` unchecked when publication or required qualification is unavailable; record owner/unblock condition and preserve partial publication receipts to avoid duplicate versions. Docs conceptual work may continue; runnable advanced claims may not bypass this gate.

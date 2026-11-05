# Verify the Rust architecture and quality changes

Status: COMPLETE

## Goal and entry contract

This final source owns remaining permanent test development and cross-boundary
coverage after all functional work in sources 01–03. It is not a prerequisite to
their focused delivery. Progress:
`.roadmap-runner/rust-architecture-quality-20261026/04-final-verification.progress.md`.
Before starting, verify all 13 functional parents have current accepted receipts;
do not infer acceptance from FIFO advancement. Each task lists the specific
receipts it consumes. Read those compact entries and named code, not all prior
sources or full logs. Reuse compatible checks and fill only outstanding gaps.

Planning does not dispatch a runner. Adopt through the existing guarded controller
at a safe checkpoint, preserving ownership, integration policy, dirty work and
current contracts. One ready parent per session; all four are independent once
their entry receipts are valid. No provider calls, credentials, paid inference,
automatic recording, live dogfood, document migration, publication or OS/device
qualification. Treat AI proposal code only as local typed source/recovery logic.

Use deterministic fixtures and ignored task-owned outputs. Keep evidence hashes,
commands, pins, counts and handoffs in progress; only checkboxes/Status change
here. A missing test, zero-match selector, skip or target absence remains an open
requirement. Record a blocker fingerprint, owner, attempted repair and exact
changed-input resume condition; no unchanged retry. Run broader checks only for
demonstrated impact or a named existing gate, recording reason and budget first.
This source does not mandate another full suite or optimization campaign.

## Tasks

### Task RAQ-4.1 — Guard dependency roots and optional capability boundaries

- [x] RAQ-4.1 Add remaining dependency regression coverage and close root acceptance.

Purpose: Prevent the demonstrated fork/feature/layering failures from returning.
Deliverable: Deterministic assertions integrated into existing architecture checks.
Context: F01–F03; current manifests and architecture graph checks; standalone root metadata, session feature declarations, authority contract.
Entry receipts: RAQ-1.1 through RAQ-1.4 from source 01, with exact resolved source/feature pins.
Dependencies: none.
Independent work: RAQ-4.2–RAQ-4.4 remain eligible if their entry receipts are valid.
Session scope: Missing graph/root assertions plus bounded compile coverage, 30–45 minutes including checks.
Acceptance: Supported root graphs select one intended Yrs source; required locks resolve offline. Minimal browser/session graphs exclude Markdown and test support; source-edit consumers include their needed feature. FFI no longer depends on the reference host. Positive and deliberately invalid graph fixtures are distinguished. Host compilation is not mislabeled OS qualification.

Implementation:

- [x] RAQ-4.1-I1 Extend the existing FIT architecture mechanism rather than adding a parallel dependency registry. Add only missing positive/negative assertions for fork identity, runtime/dev edges and feature reachability.
- [x] RAQ-4.1-I2 Cover root, CLI, formats, formats-native and formats-WASM lock resolution, and base/asset/native-store/source-edit session combinations, reusing valid delivery receipts. Give uncompiled standalone fixtures an explicit disposition and owner.

Validation:

- [x] RAQ-4.1-V1 Run the new graph checks with nonzero positive/negative counts and only outstanding `cargo metadata --locked --offline`/targeted compile combinations. Budget: 10 minutes within the session; stop and split a larger matrix instead of silently skipping roots or compiling every feature together.

Evidence: Progress contains the root/feature matrix, exact reused receipts, new check counts and unresolved target limitations.
Handoff: Exact graph edge, root or feature combination still failing and its concrete repair owner.
Blocked behavior: Record the exact failing root/graph and repair owner, leave coverage unchecked, and select another final parent with valid receipts; a missing target is not a pass.

### Task RAQ-4.2 — Guard diagnostic privacy and complete recoverability

- [x] RAQ-4.2 Complete error-formatting, cause and recovery regression coverage.

Purpose: Diagnostic safety and compact errors must not lose recovery information.
Deliverable: Focused regression cases for current public session/review error contracts.
Context: Q01/Q02; current error payloads/accessors, review rejection and stale-source cases.
Entry receipts: RAQ-2.1 and RAQ-2.2, including their minimal sentinel check, size measurements and API mapping.
Dependencies: none.
Independent work: RAQ-4.1, RAQ-4.3 and RAQ-4.4 remain eligible.
Session scope: Remaining error/recovery coverage only, 30 minutes including checks.
Acceptance: Display, Debug and traversable causes never contain synthetic document/source sentinels, including nested Conflict fields and snapshot text. Typed recovery returns exact base/proposal/current state. Leaf/wrapper cause behavior is honest. Stale or rejected apply leaves the live document and history intact. Size checks are meaningful for supported pointer widths and do not bake in one machine's incidental byte count.

Implementation:

- [x] RAQ-4.2-I1 Reuse the minimal defect test and add only uncovered nested-error, snapshot and cause cases; retain byte-exact recovery assertions and avoid logs containing real document text.
- [x] RAQ-4.2-I2 Exercise one current stale-source/rejected-review flow through the public API, including typed recovery and unchanged live state; add a size regression only where it protects the chosen representation contract.

Validation:

- [x] RAQ-4.2-V1 Run the new exact error cases and the outstanding public recovery selector; record executed/passed/failed/skipped counts and current feature flags. Budget: 5 minutes, with no provider transport or broad AI test suite.

Evidence: Progress maps each diagnostic/recovery guarantee to one current passing case and identifies reused coverage.
Handoff: Error path or payload still exposed/lost and a synthetic reproducer; no blanket formatting suppression substitutes for typed recovery.
Blocked behavior: Record the synthetic exposing/losing variant and its functional repair owner; other final parents remain eligible and this guarantee stays open.

### Task RAQ-4.3 — Verify planner and bridge semantic equivalence

- [x] RAQ-4.3 Close remaining semantic coverage for the structural moves.

Purpose: Cleaner modules must preserve one atomic preparation/commit model across adapters.
Deliverable: Focused remaining regression coverage for moved planner and bridge boundaries.
Context: A01/Q03; portable bridge, private fragment/command helpers, existing editor admission, transfer, table and bridge fixtures.
Entry receipts: RAQ-1.5, RAQ-2.3 and RAQ-2.4, plus RAQ-3.1/RAQ-3.2 selector/helper mappings where affected tests moved.
Dependencies: none.
Independent work: RAQ-4.1, RAQ-4.2 and RAQ-4.4 remain eligible.
Session scope: Missing coverage for the actually moved families, 30–45 minutes including checks; no exhaustive editor requalification.
Acceptance: Current-format prepare/preview remains silent; valid commit preserves one intended origin/notification; malformed or stale plans do not mutate; UTF-16 and stable selection behavior, fragment order and table/opaque recovery remain intact for moved code. Both adapters use the same bridge implementation and preserve current JSON/wire output and limits. Historical fixture data is not migrated.

Implementation:

- [x] RAQ-4.3-I1 Map moved branches to existing current-format cases and delivery receipts. Add focused cases only for uncovered branch/admission/selection behavior; preserve useful independent historical oracle assertions.
- [x] RAQ-4.3-I2 Reuse existing browser/native fixture equivalence mechanisms for one valid and one rejecting bridge envelope; keep target-specific translation checks at their adapters.

Validation:

- [x] RAQ-4.3-V1 Run only the new or invalidated selected cases and outstanding adapter compile checks, listing exact names and counts. Budget: 10 minutes. Reuse already-passing witness/notification tests; any broader gate needs an explicit impact reason and budget.

Evidence: Progress maps each moved responsibility to its current equivalent behavior receipt and lists untested runtime boundaries honestly.
Handoff: Exact command family, adapter or invariant still failing and the smallest reproducible current fixture.
Blocked behavior: Record the failed current-format invariant and smallest affected functional repair; other final parents remain eligible without repeating unchanged semantic checks.

### Task RAQ-4.4 — Guard quality enforcement and reproducible build feedback

- [x] RAQ-4.4 Verify test ownership, fixture isolation, lint enforcement and tuning claims.

Purpose: Make the structural/build improvements durable without manufacturing performance claims.
Deliverable: Remaining architecture/test-topology assertions and an accurate final quality/performance disposition.
Context: F04/Q04/P01; Cargo target topology, fixture-support edges, owned-code lint configuration, current build scripts and retained timing receipts.
Entry receipts: RAQ-2.5 and RAQ-3.1–RAQ-3.3, plus final feature/bridge interfaces from source 01.
Dependencies: none.
Independent work: RAQ-4.1–RAQ-4.3 remain eligible with valid receipts.
Session scope: Remaining check integration and final accounting, 30–45 minutes; no new optimization hypotheses.
Acceptance: Each migrated scenario has one discoverable owner; fixture support is development-only and its assertions remain meaningful. Selected quality lints actually run on intended owned packages/features, with explicit reviewed exceptions and vendor separation. Performance claims cite compatible measurements; an inconclusive/deferred hypothesis stays labeled that way. Production caps, debugging tradeoffs and active-lane isolation remain explicit.

Implementation:

- [x] RAQ-4.4-I1 Add missing topology/normal-edge assertions to existing architecture checks, and connect selected lint commands to the existing local/CI check entry point. Keep source fixtures authored; do not commit generated baselines, reports or caches.
- [x] RAQ-4.4-I2 Reconcile unique test counts, lint resolutions/exceptions and RAQ-3.3 decisions against current inputs. Preserve explicit final-fitness deferrals; do not restart timing experiments or demand a broad suite merely to close this source.

Validation:

- [x] RAQ-4.4-V1 Run new topology checks and only invalidated owned-package lint/format selectors. Verify every retained performance result applies to current configuration without repeating it unless inputs changed. Budget: 8 minutes.
- [x] RAQ-4.4-V2 Verify task-owned process teardown and remove inactive task outputs; record exact cleanup paths, reclaimed space and remaining free space while preserving source, user data and active work.

Evidence: Progress provides final unique/duplicate counts, check coverage, exceptions, reused measurements, deferrals and cleanup results.
Handoff: Exact unresolved policy/target/measurement mismatch and owner. Overall completion requires all four final parents and all 13 functional parents with valid evidence.
Blocked behavior: Record the unresolved topology/lint/measurement predicate and owner; keep final acceptance open without a fresh tuning campaign, and continue other eligible final parents.

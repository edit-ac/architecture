# Freeze the portable engine contracts

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/engine.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: verified project scaffolding, locked runtime and available local deterministic toolchains.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic FND-1 — Freeze the portable engine contracts

### Task FND-1.1 — Lock the protocol toolchain

- [ ] FND-1.1 Lock the protocol toolchain.

Purpose: Deliver lock the protocol toolchain as one reviewable boundary.
Context: `Cargo.toml`; `package.json`; `Cargo.lock`; `package-lock.json`; `../architecture/specs/engine.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Native Cargo check and a wasm32-unknown-unknown compile succeed with the pinned compiler; JS fixture imports resolve. Document actual feature flags and compiler requirements.

Implementation:

- [ ] FND-1.1-I1 Add exact candidate Yrs/Yjs/y-protocols and wasm-bindgen pins from the dependency report, enable small-client, and configure UTF-16 in one engine factory. Keep Yjs dev-only. Resolve the lockfiles and preserve any incompatible-version failure.

Validation:

- [ ] FND-1.1-V1 cargo check --workspace --locked; cargo check -p editac-wasm --target wasm32-unknown-unknown --locked; node --input-type=module -e "import('yjs').then(y=>new y.Doc().destroy())". Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.1`.
Blocked behavior: Leave `FND-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.2 — Create reproducible semantic fixtures

- [ ] FND-1.2 Create reproducible semantic fixtures.

Purpose: Deliver create reproducible semantic fixtures as one reviewable boundary.
Context: `fixtures/generate.mjs`; `fixtures/manifest.json`; `tests/fixtures.test.mjs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Repeated generation produces identical hashes; all declared corpus sizes and Unicode cases have assertions. Aged edits are a recipe until applied by a real engine.

Implementation:

- [ ] FND-1.2-I1 Generate Task, Long, Large, Aged input recipes and adversarial Unicode/nesting content using a fixed seed. Store expected semantic shape and hashes, with text bytes separate from update bytes.

Validation:

- [ ] FND-1.2-V1 node --test tests/fixtures.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.2`.
Blocked behavior: Leave `FND-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.3 — Prove Yrs and Yjs update exchange

- [ ] FND-1.3 Prove Yrs and Yjs update exchange.

Purpose: Deliver prove Yrs and Yjs update exchange as one reviewable boundary.
Context: `crates/editac-core/tests/interop.rs`; `tests/interop.test.mjs`; `fixtures/interop/`; `../architecture/specs/engine.md`.
Dependencies: FND-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Rust-to-JS and JS-to-Rust preserve text/attributes across emoji, duplicated updates and shuffled delivery; receipt of bytes is not called a durable acknowledgment.

Implementation:

- [ ] FND-1.3-I1 Build a tiny shared XML/text fixture, not the final editor schema. Export/apply v1 binary updates and state vectors in Rust and JS using distinct client IDs and explicit offsets.

Validation:

- [ ] FND-1.3-V1 cargo test -p editac-core --test interop --locked; node --test tests/interop.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.3`.
Blocked behavior: Leave `FND-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.4 — Implement the XML structural probe

- [ ] FND-1.4 Implement the XML structural probe.

Purpose: Deliver implement the XML structural probe as one reviewable boundary.
Context: `crates/editac-core/tests/structure_xml.rs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.2, FND-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: The probe exposes exactly where moves preserve or replace shared text identity; it does not claim a final schema.

Implementation:

- [ ] FND-1.4-I1 Implement one test-only XML candidate with a minimal move/edit fixture and identity trace. Keep it isolated from production commands.

Validation:

- [ ] FND-1.4-V1 cargo test -p editac-core --test structure_xml --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.4`.
Blocked behavior: Leave `FND-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.5 — Implement the stable-registry structural probe

- [ ] FND-1.5 Implement the stable-registry structural probe.

Purpose: Deliver implement the stable-registry structural probe as one reviewable boundary.
Context: `crates/editac-core/tests/structure_registry.rs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.2, FND-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: The probe records placement winners and retained identity on both replicas without a second CRDT.

Implementation:

- [ ] FND-1.5-I1 Implement one test-only stable text registry and placement candidate with the same minimal move/edit fixture as XML.

Validation:

- [ ] FND-1.5-V1 cargo test -p editac-core --test structure_registry --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.5`.
Blocked behavior: Leave `FND-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.6 — Compare structural representations

- [ ] FND-1.6 Compare structural representations.

Purpose: Deliver compare structural representations as one reviewable boundary.
Context: `crates/editac-core/tests/structure_probe.rs`; `benchmarks/structure/`; `../architecture/evidence/structure-probe.md`; `../architecture/specs/engine.md`.
Dependencies: FND-1.4, FND-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Both candidates use the same seeded fixtures and report semantic outcomes, retained text identities and implementation cost; no claim relies only on CRDT byte convergence.

Implementation:

- [ ] FND-1.6-I1 Run the existing XML and registry probes on identical move/move and move/edit fixtures; compare identity, semantic outcomes and complexity, then select a candidate for conflict tests.

Validation:

- [ ] FND-1.6-V1 cargo test -p editac-core --test structure_probe --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.6`.
Blocked behavior: Leave `FND-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.7 — Specify and probe delete versus edit

- [ ] FND-1.7 Specify and probe delete versus edit.

Purpose: Deliver specify and probe delete versus edit as one reviewable boundary.
Context: `crates/editac-core/tests/delete_edit_probe.rs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Replica projections agree and concurrently edited content is neither silently discarded nor resurrected unpredictably.

Implementation:

- [ ] FND-1.7-I1 Apply deletion and concurrent text edits to the candidate; define tombstone visibility and recoverable content behavior with fixed schedules.

Validation:

- [ ] FND-1.7-V1 cargo test -p editac-core --test delete_edit_probe --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.7`.
Blocked behavior: Leave `FND-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.8 — Specify and probe split and join conflicts

- [ ] FND-1.8 Specify and probe split and join conflicts.

Purpose: Deliver specify and probe split and join conflicts as one reviewable boundary.
Context: `crates/editac-core/tests/split_join_probe.rs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Both replicas resolve each prepared schedule to the same documented content and placement without cloning shared text as a shortcut.

Implementation:

- [ ] FND-1.8-I1 Apply split/edit and join/edit schedules to the candidate and record text/anchor ownership across source and destination blocks.

Validation:

- [ ] FND-1.8-V1 cargo test -p editac-core --test split_join_probe --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.8`.
Blocked behavior: Leave `FND-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.9 — Specify and probe hierarchy conflicts

- [ ] FND-1.9 Specify and probe hierarchy conflicts.

Purpose: Deliver specify and probe hierarchy conflicts as one reviewable boundary.
Context: `crates/editac-core/tests/hierarchy_probe.rs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Each fixture has one winning placement and bounded traversal; no cycle hangs and no repair write feedback loop.

Implementation:

- [ ] FND-1.9-I1 Test duplicate placements, cycles, orphans and nested-list move schedules; choose a deterministic read projection instead of platform-specific repair writes.

Validation:

- [ ] FND-1.9-V1 cargo test -p editac-core --test hierarchy_probe --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.9`.
Blocked behavior: Leave `FND-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.10 — Define delete and hierarchy conflict behavior

- [ ] FND-1.10 Define delete and hierarchy conflict behavior.

Purpose: Deliver define delete and hierarchy conflict behavior as one reviewable boundary.
Context: `crates/editac-core/tests/structure_conflicts.rs`; `../architecture/decisions/002-document-structure.md`; `../architecture/specs/engine.md`.
Dependencies: FND-1.7, FND-1.8, FND-1.9.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every case has one expected deterministic semantic projection on all replicas; unresolved identity/cycle behavior blocks schema adoption with a bounded follow-up question.

Implementation:

- [ ] FND-1.10-I1 Collect the passing conflict-family probes into the selected structural policy ADR and a regression aggregator. Resolve contradictions before adopting the schema.

Validation:

- [ ] FND-1.10-V1 cargo test -p editac-core --test structure_conflicts --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.10`.
Blocked behavior: Leave `FND-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.11 — Freeze schema and protocol profile

- [ ] FND-1.11 Freeze schema and protocol profile.

Purpose: Deliver freeze schema and protocol profile as one reviewable boundary.
Context: `../architecture/specs/schema-v1.md`; `../architecture/specs/protocol-v1.md`; `fixtures/schema-v1/`; `../architecture/specs/engine.md`.
Dependencies: FND-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A reviewer can construct the same schema in Rust and JS without guessing; profile versions and unsupported-version behavior are explicit. No Tiptap document compatibility claim is made.

Implementation:

- [ ] FND-1.11-I1 Record the chosen root keys, value types, stable ID format, initialization/epoch rule, offset mode, update encoding, origin semantics and structural conflict policy from passing probes. Include JS fixture mapping and compatibility negotiation.

Validation:

- [ ] FND-1.11-V1 cargo test -p editac-core --test structure_conflicts --locked; node --test tests/interop.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.11`.
Blocked behavior: Leave `FND-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.12 — Prove the frozen structural schema across Rust and JS

- [ ] FND-1.12 Prove the frozen structural schema across Rust and JS.

Purpose: Deliver prove the frozen structural schema across Rust and JS as one reviewable boundary.
Context: `crates/editac-core/tests/schema_interop.rs`; `tests/schema-interop.test.mjs`; `fixtures/schema-v1/`; `../architecture/specs/engine.md`.
Dependencies: FND-1.11.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Pinned Yrs and JS Yjs agree on structural outcomes, relative anchors and retained text identities; text-only interoperability is insufficient.

Implementation:

- [ ] FND-1.12-I1 Upgrade the earlier text fixture to the exact frozen root/placement/text schema. Exchange moves, deletes and overlapping edits in both language directions and compare canonical semantic projections.

Validation:

- [ ] FND-1.12-V1 cargo test -p editac-core --test schema_interop --locked; node --test tests/schema-interop.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.12`.
Blocked behavior: Leave `FND-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.13 — Prove the browser WASM loading boundary

- [ ] FND-1.13 Prove the browser WASM loading boundary.

Purpose: Deliver prove the browser WASM loading boundary as one reviewable boundary.
Context: `crates/editac-wasm/`; `packages/core/`; `tests/wasm-load.test.mjs`; `../architecture/specs/engine.md`.
Dependencies: FND-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Built WASM initializes from a supplied URL and a local package consumer; importing the JS module during SSR does not touch window or initialize a document. Record binary and glue bytes.

Implementation:

- [ ] FND-1.13-I1 Add a minimal actual wasm-bindgen bridge around the tested fixture and an explicit asynchronous init(assetUrl) contract. Add pinned build tooling/scripts and a packed asset smoke test; avoid hand metadata being overwritten by generated pkg files.

Validation:

- [ ] FND-1.13-V1 npm run build:wasm; node --test tests/wasm-load.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.13` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.13`.
Blocked behavior: Leave `FND-1.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FND-1.14 — Approve the engine foundation evidence

- [ ] FND-1.14 Approve the engine foundation evidence.

Purpose: Deliver approve the engine foundation evidence as one reviewable boundary.
Context: `../architecture/evidence/foundation.md`; `../architecture/specs/engine.md`.
Dependencies: FND-1.12, FND-1.13.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Schema, UTF-16, interop and WASM boundary checks are reproducible with no skips; structural uncertainty is resolved before engine tasks start.

Implementation:

- [ ] FND-1.14-I1 Link the selected schema/profile, real compiled artifact, fixture hashes and failed alternatives. State the supported update pair and unresolved risks with owners.

Validation:

- [ ] FND-1.14-V1 cargo test -p editac-core --locked; node --test tests/schema-interop.test.mjs tests/wasm-load.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FND-1.14` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FND-1.14`.
Blocked behavior: Leave `FND-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

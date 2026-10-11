# Prove native portability without claiming native SDK parity

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/modules-native.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic NAT-1 — Prove native portability without claiming native SDK parity

### Task NAT-1.1 — Verify portable engine entry gate

- [ ] NAT-1.1 Verify portable engine entry gate.

Purpose: Deliver verify portable engine entry gate as one reviewable boundary.
Context: `crates/editac-core/`; `../architecture/specs/engine.md`; `../architecture/specs/modules-native.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Core tests run natively; missing platform tooling is recorded with an exact installation/host unblock condition.

Implementation:

- [ ] NAT-1.1-I1 Check native cargo compilation, command/anchor/patch fixtures and absence of DOM dependencies in core. Inventory installed Swift/Kotlin/NDK toolchains before native work.

Validation:

- [ ] NAT-1.1-V1 cargo test -p editac-core --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.1`.
Blocked behavior: Leave `NAT-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task NAT-1.2 — Define and generate bounded native bindings

- [ ] NAT-1.2 Define and generate bounded native bindings.

Purpose: Deliver define and generate bounded native bindings as one reviewable boundary.
Context: `crates/editac-ffi/`; `../architecture/specs/native-abi.md`; `../architecture/specs/modules-native.md`.
Dependencies: NAT-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Native bridge compiles; generated Swift/Kotlin interfaces agree on UTF-16 and bytes; no per-character FFI chatter or leaked engine internals.

Implementation:

- [ ] NAT-1.2-I1 Pin UniFFI runtime/generator, define opaque handles and batched commands/patches, explicit ownership/thread/error/cancel rules and schema versions. Keep callbacks outside held Rust transactions.

Validation:

- [ ] NAT-1.2-V1 cargo test -p editac-ffi --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.2`.
Blocked behavior: Leave `NAT-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task NAT-1.3 — Build a Swift headless round-trip host

- [ ] NAT-1.3 Build a Swift headless round-trip host.

Purpose: Deliver build a Swift headless round-trip host as one reviewable boundary.
Context: `native/ios/probe/`; `tests/native/swift-fixture.sh`; `../architecture/specs/modules-native.md`.
Dependencies: NAT-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Swift fixture semantics match Rust; dispose and typed failure paths work; all required build commands/toolchain versions are recorded.

Implementation:

- [ ] NAT-1.3-I1 Compile a minimal Swift host that creates/restores a document, applies prepared commands and reads patches using shared fixed fixtures. Record binding copies and lifecycle.

Validation:

- [ ] NAT-1.3-V1 bash tests/native/swift-fixture.sh. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.3`.
Blocked behavior: Leave `NAT-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task NAT-1.4 — Build a Kotlin headless round-trip host

- [ ] NAT-1.4 Build a Kotlin headless round-trip host.

Purpose: Deliver build a Kotlin headless round-trip host as one reviewable boundary.
Context: `native/android/probe/`; `tests/native/kotlin-fixture.sh`; `../architecture/specs/modules-native.md`.
Dependencies: NAT-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Kotlin semantics match Rust/Swift fixture expectations; architecture/ABI artifacts are identified; unavailable platform builds remain unchecked.

Implementation:

- [ ] NAT-1.4-I1 Compile a minimal Kotlin host with the appropriate native library packaging, applying the same prepared commands/updates and disposal/error tests.

Validation:

- [ ] NAT-1.4-V1 bash tests/native/kotlin-fixture.sh. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.4`.
Blocked behavior: Leave `NAT-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task NAT-1.5 — Probe one iOS text-control patch

- [ ] NAT-1.5 Probe one iOS text-control patch.

Purpose: Deliver probe one iOS text-control patch as one reviewable boundary.
Context: `native/ios/probe/`; `tests/manual/ios-probe.md`; `../architecture/specs/modules-native.md`.
Dependencies: NAT-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Real native control is used without WebView; composition/attachment gaps and copy costs are recorded as preparation evidence, not SDK support.

Implementation:

- [ ] NAT-1.5-I1 Use UITextView/TextKit to apply one local and one remote range patch with selection and marked-text ownership; demonstrate a custom mark and inline attachment if supported by the probe.

Validation:

- [ ] NAT-1.5-V1 Build/run the probe with the pinned Xcode command documented in tests/manual/ios-probe.md. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.5`.
Blocked behavior: Leave `NAT-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task NAT-1.6 — Probe one Android text-control patch

- [ ] NAT-1.6 Probe one Android text-control patch.

Purpose: Deliver probe one Android text-control patch as one reviewable boundary.
Context: `native/android/probe/`; `tests/manual/android-probe.md`; `../architecture/specs/modules-native.md`.
Dependencies: NAT-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Real native input is used; selection/composition gaps, toolchain/device and copy counts are captured without parity claims.

Implementation:

- [ ] NAT-1.6-I1 Use EditText/Editable/spans to apply range patches and observe InputConnection composing/batch semantics; demonstrate mark and attachment or explicit unsupported result.

Validation:

- [ ] NAT-1.6-V1 Build/run the probe with the pinned Gradle/adb commands documented in tests/manual/android-probe.md. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.6`.
Blocked behavior: Leave `NAT-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task NAT-1.7 — Write the native SDK follow-up boundary

- [ ] NAT-1.7 Write the native SDK follow-up boundary.

Purpose: Deliver write the native SDK follow-up boundary as one reviewable boundary.
Context: `../architecture/evidence/native-preparation.md`; `../architecture/specs/native-follow-up.md`; `../architecture/specs/modules-native.md`.
Dependencies: NAT-1.5, NAT-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Preparation evidence supports a feasible follow-up plan; no full mobile SDK or cross-platform parity is asserted by these probes.

Implementation:

- [ ] NAT-1.7-I1 List measured binding/platform constraints and missing IME, clipboard, accessibility, attachments, persistence, reconnect and packaging work. Split future iOS/Android deliverables from browser release.

Validation:

- [ ] NAT-1.7-V1 cargo test -p editac-ffi --locked; review the Swift/Kotlin and real-control evidence for missing/skipped cases. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `NAT-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `NAT-1.7`.
Blocked behavior: Leave `NAT-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

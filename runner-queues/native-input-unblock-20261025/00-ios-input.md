# Implement the missing iOS input owner

Status: IN_PROGRESS

## Goal and bounded entry conditions

Workspace: `core`, invoked from root `/Users/bpstr/Github/edit-ac`; paths below are core-relative unless explicitly prefixed. Original owners: IOS-1.1–1.7; EDX-2.1. This is a bounded extraction of the input prerequisites from [the platform owner](../../roadmaps/16-ios-sdk.md), not completion of its tables, attachments, accessibility, packaging, release or full qualification tasks. Deliver a real reusable input adapter, not another fixed-node probe. Read [native module ownership](../../specs/modules-native.md), [editing intent](../../specs/editing-experience.md) and the active input portion of [platform editing policy](../../specs/platform-editing-services.md).

Entry: consume current generated NativeSession/FFI and the existing prepared edit, projection, selection and history results validated in `.roadmap-runner/editing-experience-20261024/00-current-consumer-prerequisites.progress.md` and `01-shared-history-and-breaks.progress.md`. Read only CFC/EDX-1 interface receipts needed by the parent. Do not require whole historic roadmaps or deleted generated evidence. Authenticate the consumed public interface and current-format fixture; if an actual missing shared primitive is found, repair only the existing owner at the narrow boundary or record the exact prerequisite. Existing six wider FFI fixture/source failures stay with EDX-3.1; this source cannot claim their qualification. Toolchain: iOS SDK via xcrun; Swift package host target and an iOS simulator compile target.

## Execution and safety

The user requested unblocking and continuing the existing editing/UI run on 2026-10-25. Implement the missing native owner instead of retrying the old absent-adapter gate. One guarded serial root-main runner, one parent per iteration. Inspect current exports before editing; reuse the single current Session/FFI command, history, prepared-target and durability owners. Existing review/probe code is a reference, not a production editor. Keep platform policy out of Rust; no second semantic/history/storage implementation, compatibility aliases or silent document conversion.

Requirements and acceptance are read-only. Follow the runner-selected tracking mode for verified task checkbox/Status changes only; keep implementation results, hashes and detailed evidence in the separate progress file. Keep original IDs, acceptance and ownership. Implement at most one parent per 30–45-minute session including focused checks; checkpoint partial implementation with exact next function/command before the deadline. Do not turn a missing planned path or selector into an external blocker: creating it is the implementation task. Add only the smallest production-linked bootstrap/regression fixture necessary to prove the changed boundary. Comprehensive suites and new case matrices remain with EDX-3 and UI final testing, after functional delivery. Reuse compatible current receipts; no broad inventory, full engine suite or unchanged failed retry.

Read owning AGENTS.md and only the current task's named specs/paths. Use deterministic real-engine fixtures and prepared/mock network transports. No AI/provider calls, secrets, paid inference, external provisioning, push, deployment or publication. Missing physical hardware is not a gate; required virtual/runtime proof remains unqualified until executed. Never represent compiler-only or host protocol proof as target IME/runtime qualification.

At every two completed parents and source boundary, preserve unrelated dirty bytes/index, acquire `.roadmap-coordination/integration.lock` and commit only validated owned source hunks on existing main. Do not blanket stage, stash, reset, create worktrees or agents. Current prior WIP remains unstaged unless exact task ownership and validation are established. Preserve generated failed diagnostics only while useful, keep artifacts ignored and clean inactive task outputs/processes. On an unchanged external toolchain/host blocker, record original owner, task/source/error/prerequisite fingerprint, attempted repair and exact changed-input resume trigger; select another ready sibling. End BLOCKED only when no useful current-source implementation remains, so the guard stops the run. Never start another controller or retry yourself.

### Task NIP-1.1 — Create the production input host and bounded dispatcher

- [x] NIP-1.1 Create the production input host and bounded dispatcher.

Purpose: Remove the concrete missing iOS input prerequisite for IOS-1.1–1.7; EDX-2.1.
Deliverable: `native/ios/Sources/EditacIOS/input/` and the relevant existing package/consumer, with focused selector `native/ios/scripts/check.sh bootstrap`.
Context: `native/ios/Package.swift; native/ios/Bindings/Swift/EditacNative.swift; native/ios/probe/UIKit/Probe.swift; tests/native/ios-control.py`; read only the affected source symbols and active contract above.
Dependencies: none.
Independent work: Other dependency-ready parents in this source; unrelated platform work is controller-owned in separate files.
Session scope: One input integration boundary, 30–45 minutes including checks; checkpoint partial production code before exceeding it.
Acceptance: An ordinary production consumer creates and disposes one session-backed native input control. One real current-format document is read through the actual binding; disposed callbacks reject. The named bootstrap selector exists and compiles the affected host/binding; one production-linked nonzero lifecycle fixture passes. A fake Session or a probe-only executable is insufficient.

Implementation:

- [x] NIP-1.1-I1 Create native/ios/Sources/EditacIOS/input/ and wire UITextView/TextKit, UITextInput and the generated Swift NativeSession to one current Session lifecycle. Reuse review ownership/disposal patterns without presenting read-only review as editing. Keep generated bindings sourced from the current owner; initialize unimplemented capabilities honestly. Introduce `native/ios/scripts/check.sh bootstrap` (invoke Python or bash as appropriate), rejecting unknown selectors and zero cases. If a required local compiler is absent, first produce useful platform-independent integration source and a precise compiler requirement without claiming it builds.

Validation:

- [x] NIP-1.1-V1 Run `native/ios/scripts/check.sh bootstrap` through its declared interpreter and pinned toolchain; implement the planned selector before invoking it. Select only the affected compiler/control/real-binding fixture, budget at most 5 minutes after compilation inputs are ready. Record exact command/runtime/exit and executed/passed/failed/required-skipped counts; zero cases, missing tooling and required skips cannot pass. Reuse unchanged prerequisite results.

Evidence: Separate configured progress for this file; changed production paths/interfaces, selector results, remaining qualification and original-owner mapping. No generated output in Git.
Handoff: Last implemented function, exact remaining code/command, source inputs, failure and changed-input next step.
Blocked behavior: Leave this original boundary unchecked; name toolchain/host/API owner and exact resume condition, continue any ready sibling or exit BLOCKED. No unchanged retry.

### Task NIP-1.2 — Project text and UTF-16 selection through one owner

- [x] NIP-1.2 Project text and UTF-16 selection through one owner.

Purpose: Remove the concrete missing iOS input prerequisite for IOS-1.1–1.7; EDX-2.1.
Deliverable: `native/ios/Sources/EditacIOS/input/` and the relevant existing package/consumer, with focused selector `native/ios/scripts/check.sh projection`.
Context: `native/ios/Package.swift; native/ios/Bindings/Swift/EditacNative.swift; native/ios/probe/UIKit/Probe.swift; tests/native/ios-control.py`; read only the affected source symbols and active contract above.
Dependencies: NIP-1.1.
Independent work: Other dependency-ready parents in this source; unrelated platform work is controller-owned in separate files.
Session scope: One input integration boundary, 30–45 minutes including checks; checkpoint partial production code before exceeding it.
Acceptance: A normal mounted control consumes an actual shared projection and round-trips one non-ASCII selection through the current binding. Applying a projection emits no edit; read-only/disposed updates are nonmutating. Compile the target control and execute one production-linked projection/selection fixture.

Implementation:

- [x] NIP-1.2-I1 Bind committed projection/results to native/ios/Sources/EditacIOS/input/; map native UTF-16 selection and focus through existing stable targets. Guard projection-origin callbacks and detach/disposal; read-only rejects before mutation. Do not duplicate text or selection semantics.

Validation:

- [x] NIP-1.2-V1 Run `native/ios/scripts/check.sh projection` through its declared interpreter and pinned toolchain; implement the planned selector before invoking it. Select only the affected compiler/control/real-binding fixture, budget at most 5 minutes after compilation inputs are ready. Record exact command/runtime/exit and executed/passed/failed/required-skipped counts; zero cases, missing tooling and required skips cannot pass. Reuse unchanged prerequisite results.

Evidence: Separate configured progress for this file; changed production paths/interfaces, selector results, remaining qualification and original-owner mapping. No generated output in Git.
Handoff: Last implemented function, exact remaining code/command, source inputs, failure and changed-input next step.
Blocked behavior: Leave this original boundary unchecked; name toolchain/host/API owner and exact resume condition, continue any ready sibling or exit BLOCKED. No unchanged retry.

### Task NIP-1.3 — Route committed text edits and native replacements

- [ ] NIP-1.3 Route committed text edits and native replacements.

Purpose: Remove the concrete missing iOS input prerequisite for IOS-1.1–1.7; EDX-2.1.
Deliverable: `native/ios/Sources/EditacIOS/input/` and the relevant existing package/consumer, with focused selector `native/ios/scripts/check.sh edits`.
Context: `native/ios/Package.swift; native/ios/Bindings/Swift/EditacNative.swift; native/ios/probe/UIKit/Probe.swift; tests/native/ios-control.py`; read only the affected source symbols and active contract above.
Dependencies: NIP-1.2.
Independent work: Other dependency-ready parents in this source; unrelated platform work is controller-owned in separate files.
Session scope: One input integration boundary, 30–45 minutes including checks; checkpoint partial production code before exceeding it.
Acceptance: A committed insert/delete/replacement reaches the actual Session once and uses the existing history. A rejected/stale edit preserves document and selection without recursive native callbacks. The smallest actual control or real-binding edit fixture passes with nonzero counts; do not substitute source inspection for behavior.

Implementation:

- [ ] NIP-1.3-I1 Route insert, delete and replacement callbacks from UITextView/TextKit, UITextInput and the generated Swift NativeSession through existing prepared command admission. Capture target and selection before async/native work, apply the shared command result and restore selection/focus. Reject stale/read-only edits before mutation. Native temporary buffers are projections only.

Validation:

- [ ] NIP-1.3-V1 Run `native/ios/scripts/check.sh edits` through its declared interpreter and pinned toolchain; implement the planned selector before invoking it. Select only the affected compiler/control/real-binding fixture, budget at most 5 minutes after compilation inputs are ready. Record exact command/runtime/exit and executed/passed/failed/required-skipped counts; zero cases, missing tooling and required skips cannot pass. Reuse unchanged prerequisite results.

Evidence: Separate configured progress for this file; changed production paths/interfaces, selector results, remaining qualification and original-owner mapping. No generated output in Git.
Handoff: Last implemented function, exact remaining code/command, source inputs, failure and changed-input next step.
Blocked behavior: Leave this original boundary unchecked; name toolchain/host/API owner and exact resume condition, continue any ready sibling or exit BLOCKED. No unchanged retry.

### Task NIP-1.4 — Integrate marked text and composition ownership

- [ ] NIP-1.4 Integrate marked text and composition ownership.

Purpose: Remove the concrete missing iOS input prerequisite for IOS-1.1–1.7; EDX-2.1.
Deliverable: `native/ios/Sources/EditacIOS/input/` and the relevant existing package/consumer, with focused selector `native/ios/scripts/check.sh composition`.
Context: `native/ios/Package.swift; native/ios/Bindings/Swift/EditacNative.swift; native/ios/probe/UIKit/Probe.swift; tests/native/ios-control.py`; read only the affected source symbols and active contract above.
Dependencies: NIP-1.3.
Independent work: Other dependency-ready parents in this source; unrelated platform work is controller-owned in separate files.
Session scope: One input integration boundary, 30–45 minutes including checks; checkpoint partial production code before exceeding it.
Acceptance: One production-linked deterministic native protocol fixture demonstrates provisional text is not double committed, commit reaches one shared command and cancel restores the original state/selection. A relevant remote/stale-target path rejects safely. Compile the actual platform adapter; record toolkit/settings and distinguish deterministic protocol proof from target IME observations. Comprehensive target-runtime variants remain EDX-3.3.

Implementation:

- [ ] NIP-1.4-I1 Integrate platform marked/composing range, commit/cancel, batch edits and OS replacement lifecycle at native/ios/Sources/EditacIOS/input/. Preserve provisional input outside shared committed state, resolve captured targets once and use the existing overlap policy. Expose platform/off/custom spelling and independent autocorrection where supported; report coupled or unsupported traits. Use existing platform policy, not a new engine semantic.

Validation:

- [ ] NIP-1.4-V1 Run `native/ios/scripts/check.sh composition` through its declared interpreter and pinned toolchain; implement the planned selector before invoking it. Select only the affected compiler/control/real-binding fixture, budget at most 5 minutes after compilation inputs are ready. Record exact command/runtime/exit and executed/passed/failed/required-skipped counts; zero cases, missing tooling and required skips cannot pass. Reuse unchanged prerequisite results.

Evidence: Separate configured progress for this file; changed production paths/interfaces, selector results, remaining qualification and original-owner mapping. No generated output in Git.
Handoff: Last implemented function, exact remaining code/command, source inputs, failure and changed-input next step.
Blocked behavior: Leave this original boundary unchecked; name toolchain/host/API owner and exact resume condition, continue any ready sibling or exit BLOCKED. No unchanged retry.


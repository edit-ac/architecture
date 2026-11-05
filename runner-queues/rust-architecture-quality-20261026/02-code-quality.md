# Improve editor Rust diagnostics and code structure

Status: COMPLETE

## Goal and execution contract

Own Q01–Q04 from `architecture/research/rust-architecture-quality-20261026.md`.
Read only the selected finding and named source. Progress:
`.roadmap-runner/rust-architecture-quality-20261026/02-code-quality.progress.md`.
Entry: resolve current source-service symbols after any RAQ-1.2/RAQ-1.3 move and
consume their feature/interface receipts if adopted. Those moves are not a
technical prerequisite to safe error formatting or planner cleanup; target the
current implementation and record its pins. No whole-track or OS gate applies.

Planning does not authorize dispatch. Use existing guarded ownership/integration
rules at controller adoption, one ready parent per session, preserving all other
dirty work. Keep one prepared semantic pipeline and current wire/document format.
Update authoritative API contracts before an unavoidable public shape change.
No blanket renaming, generic handler framework, dependency upgrade, provider call,
secret access, migration, publication or platform qualification.

Use isolated ignored Cargo output, existing exact test selectors and bounded
checks. A minimal regression for the confirmed diagnostic defect is permitted;
remaining test development and matrices belong to source 04. Record input pins,
commands, elapsed budget and nonzero pass/fail/skip counts in progress. Reuse
matching evidence. Only checkboxes and Status change in this source. Blockers
remain unchecked with task/input/error fingerprint, owner, attempted repair and
changed-input resume condition; independent ready work continues without retries
of unchanged failures.

## Tasks

### Task RAQ-2.1 — Preserve recovery without exposing it in diagnostics

- [x] RAQ-2.1 Make session error formatting content-free and preserve useful causes.

Purpose: Ordinary error formatting must not disclose complete document recovery content.
Deliverable: Explicit safe Display/Debug implementations and honest nested error causes.
Context: Q01; `editac-session/src/{edit_service,review_apply,session,ports}.rs`, `editac-markdown/src/reconcile.rs::Conflict`, and callers formatting these errors.
Dependencies: none.
Independent work: RAQ-2.3 and RAQ-2.4 remain eligible; RAQ-2.2 waits for the diagnostic contract.
Session scope: These error types and direct formatting callers only, 30–45 minutes including checks.
Acceptance: Both Display and Debug exclude synthetic base/proposed/current text and nested conflict source/detail content. Complete recovery remains available through explicit typed fields/accessors. Causes wrapping an existing `Error` remain discoverable through `source()`; leaf errors remain leaves. Recursive formatting of exposed causes is also content-free. Stable wire error codes remain unchanged.

Implementation:

- [x] RAQ-2.1-I1 Follow the existing redacted `ReviewError` pattern for safe diagnostic summaries; inspect nested conflict fields and ordinary caller formatting instead of hiding recovery data.
- [x] RAQ-2.1-I2 Implement cause delegation where the wrapped type implements `Error`, preserving typed access otherwise. Add only the minimal sentinel regression needed to lock the demonstrated defect; avoid a new error-macro dependency.

Validation:

- [x] RAQ-2.1-V1 Run the minimal synthetic sentinel check over Display, Debug and available cause chains; verify recovery fields still contain their exact input. Reuse or run `cargo test --manifest-path core/Cargo.toml -p editac-session --test edit_service stale_source_is_recoverable_without_replacing_current_document --locked --offline -- --exact`, enabling `source-edit` once RAQ-1.3 applies. Budget: 3 minutes; no real document content or provider transport.

Evidence: Progress records diagnostic fields retained, redaction assertions, cause behavior and exact recovery-case counts.
Handoff: Remaining error variant/caller exposing content and a synthetic reproducer; do not classify an untested variant as safe.
Blocked behavior: If any formatted path still exposes content, keep this parent open with its synthetic reproducer; RAQ-2.3 and RAQ-2.4 remain eligible while RAQ-2.2 waits.

### Task RAQ-2.2 — Bound cold recovery error payloads

- [x] RAQ-2.2 Reduce large session error values without weakening recovery.

Purpose: Keep cold recovery payloads from inflating ordinary Result values and nested errors.
Deliverable: Owned indirection for substantial error recovery payloads with typed access retained.
Context: Q02; `ServiceError::SourceConflict`, `ReviewError`, `ReviewFailure`, affected session/receipt/proposal return paths and their direct consumers. Review baseline: 264/472 bytes on aarch64 macOS.
Dependencies: RAQ-2.1.
Independent work: RAQ-2.3 and RAQ-2.4 do not depend on error layout.
Session scope: One coherent session/review error representation change, 30–45 minutes including checks.
Acceptance: Measured sizes of the changed error values decrease on the same target; affected large-result diagnostics are removed or precisely justified. Recovery bytes, snapshot/error state, typed classification, redaction and supported cause chains are preserved. Successful operations acquire no recovery allocation. No whole-enum boxing of unrelated hot commands is introduced.

Implementation:

- [x] RAQ-2.2-I1 Measure the actual dominant variants, group cold recovery data into explicit owned payloads, and introduce indirection only at those boundaries.
- [x] RAQ-2.2-I2 Update pattern matches/accessors and API documentation in one unit; retain the RAQ-2.1 diagnostic contract and all existing recovery ownership.

Validation:

- [x] RAQ-2.2-V1 Compare `size_of` on the same target and rerun only the affected sentinel/recovery case from RAQ-2.1. Check the affected session library with Clippy's large-result/large-variant lints. Budget: 3 minutes; report architecture-specific sizes without a throughput or compile-speed claim.

Evidence: Progress records before/after sizes, remaining justified diagnostics, exact recovery checks and API changes.
Handoff: Unconverted match/accessor or unchanged large variant; preserve full payloads rather than dropping data to meet a size target.
Blocked behavior: If recovery or diagnostics change incorrectly, preserve the original payload and record the failing accessor; RAQ-2.3 and RAQ-2.4 remain eligible.

### Task RAQ-2.3 — Isolate fragment preparation responsibilities

- [x] RAQ-2.3 Move fragment planning into a private coherent module.

Purpose: Make fragment validation and preparation readable without changing the semantic owner.
Deliverable: A private fragment planner behind the current Document entry points.
Context: Q03; `core/crates/editac-core/src/commands/editor.rs::{prepare_fragment_move,prepare_fragment_transfer,prepare_fragment,apply_fragment_opaque}`, existing `editor/table_fragment.rs`, `tests/{opaque_fragments,compound_fragment_order,extension_transfer_deletion}.rs`.
Dependencies: none.
Independent work: RAQ-2.1 and RAQ-2.4 are logically independent; serial ownership prevents simultaneous edits of the same file.
Session scope: Fragment preparation only, 30–45 minutes with focused validation; no command-dispatch rewrite.
Acceptance: Fragment-specific helpers have one private home; public preparation APIs and opaque plans preserve behavior. Validation still precedes mutation, rejected input leaves document/history/selection unchanged, and original transfer ordering remains intact. No public helper is added solely for tests.

Implementation:

- [x] RAQ-2.3-I1 Move fragment-specific helpers and data handling with the smallest necessary private visibility; retain meaningful boundary and invariant comments.
- [x] RAQ-2.3-I2 Keep public entry points thin and remove superseded helper definitions. Preserve all existing bounds, UTF-16/stable-target handling and table fragment integration.

Validation:

- [x] RAQ-2.3-V1 Select one existing opaque/compound fragment case exercising the moved path plus one malformed-input rejection. Record exact selectors and nonzero counts before running. Budget: 3 minutes; comprehensive transfer cases belong to RAQ-4.3.

Evidence: Progress maps old/new helper ownership and the two focused semantic receipts. No compile-speed improvement is claimed from file splitting.
Handoff: Remaining fragment helper, dependency and observed invariant; propose a further bounded split if the session budget is exceeded.
Blocked behavior: If a helper cannot be moved within the semantic boundary, report the smallest controller split; other ready quality parents remain eligible.

### Task RAQ-2.4 — Separate command-family planning from dispatch

- [x] RAQ-2.4 Reduce the responsibility of the central editor preparation method.

Purpose: Make command admission, staged planning and commit invariants independently understandable.
Deliverable: Private command-family helpers under the existing single planner.
Context: Q03; `commands/editor.rs::{prepare_editor_with_registry_and_preview,replace_staged_content,admit_editor,commit_editor}`, current command modules and `transaction_tests`.
Dependencies: none.
Independent work: RAQ-2.1 and RAQ-2.3 remain logically eligible; adopt this task only with exclusive ownership of the affected file.
Session scope: One coherent command-family extraction from the large dispatch method, 30–45 minutes including tests. Record remaining families as explicit later work if a controller split is necessary; do not claim the whole method improved from formatting alone.
Acceptance: Dispatch delegates a substantive command family through explicit private inputs/results. All commands still share the existing staged replica, resource accounting, witness/admission and final commit. Rejection is silent and accepted batches retain one origin/notification contract. No new handler trait registry or duplicate validation path.

Implementation:

- [x] RAQ-2.4-I1 Select the largest cohesive family whose local state can be passed explicitly; extract its existing logic without adding a general framework or changing validation order.
- [x] RAQ-2.4-I2 Make the remaining dispatcher express the preparation sequence clearly, retain shared budgets, and document only the invariants needed at helper boundaries.

Validation:

- [x] RAQ-2.4-V1 Run the existing exact unit cases `commands::editor::transaction_tests::editor_admission_preview_keeps_exact_owned_bytes_and_commit_notifies_once` and `commands::editor::transaction_tests::editor_admission_malformed_update_is_silent_in_preview_and_commit`; retain or update their module path after moves. Budget: 3 minutes. Add one existing selected family case only if neither exercises the moved branch.

Evidence: Progress identifies the extracted family, responsibility removed from dispatch and invariant-case receipts.
Handoff: Exact remaining family or shared mutable dependency; do not weaken opaque-plan validation to make extraction easier.
Blocked behavior: If the family exceeds the session boundary or invariant checks fail, record the exact family and repair/split owner; continue other ready quality work.

### Task RAQ-2.5 — Enforce selective Rust quality checks

- [x] RAQ-2.5 Establish an owned-code lint policy with narrow justified exceptions.

Purpose: Prevent substantive regressions while keeping intentional ownership and vendor code explicit.
Deliverable: Scoped lint configuration, resolved relevant diagnostics and documented exceptions.
Context: Q04; core workspace/member lint manifests, FFI's separate unsafe policy, `core/crates/editac-core/src/patches.rs::subscribe`, current Clippy diagnostics and existing CI/check entry points.
Dependencies: RAQ-2.2.
Independent work: RAQ-2.3 and RAQ-2.4 do not wait for lint policy; their changed inputs are rechecked only when relevant.
Session scope: Policy and substantive findings in the reviewed owned-code closure, 30–45 minutes; no mass style rewrite.
Acceptance: Correctness and selected suspicious/performance rules have explicit enforcement; Rust warnings in changed owned code are resolved or reasoned narrowly. No broad `allow`, vendored cleanup, blanket pedantic denial or global warning-baseline artifact is added. The audited FFI unsafe boundary and core forbid policy retain their distinct strength. Callback ownership remains correct for disposal and reentrancy.

Implementation:

- [x] RAQ-2.5-I1 Triage current diagnostics by risk and scope; fix demonstrated issues and choose explicit local exceptions for intentional patterns. Trace the non-Send callback ownership before changing Arc/Mutex, documenting a justified exception if no safe improvement is warranted.
- [x] RAQ-2.5-I2 Integrate selected lints into existing check configuration with no new dependency or blanket auto-fix. Keep style-only suggestions advisory and vendor warnings separately attributed.

Validation:

- [x] RAQ-2.5-V1 Run focused Clippy for the changed library packages/features and a rustfmt check on changed Rust source. If callback ownership changed, run one existing reentrant/disposal patch test with a nonzero selector. Budget: 4 minutes; full lint closure is RAQ-4.4.

Evidence: Progress lists enforced rules, substantive resolutions, each narrow exception and focused results. Diagnostic counts do not equal defect counts.
Handoff: Exact unresolved diagnostic with ownership rationale or reproduction; no code-wide suppression is an acceptable closure.
Blocked behavior: If a selected lint reveals unresolved correctness or ownership behavior, keep it explicit and request a bounded repair; do not suppress it globally or block unrelated ready planner work.

## Source handoff

Record current error APIs/sizes, redaction and cause guarantees, planner module
ownership, lint policy, input pins and check receipts in progress. RAQ-4.2 owns
remaining recovery/error coverage; RAQ-4.3 owns semantic equivalence; RAQ-4.4 owns
remaining lint enforcement coverage. Closing this source does not require repeats
of compatible passing evidence or final runtime qualification.

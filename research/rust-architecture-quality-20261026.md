# Rust architecture, code quality and build review

Date: 2026-10-26. Scope: the current editor Rust implementation, its session and
binding boundaries, optional format roots, and the CLI dependency graph. This is
an authored assessment of local source, not release qualification or a clean-tree
benchmark. Core was at `a528829`, CLI at `a219ec5`; both had ongoing uncommitted work.
Revalidate the named symbols before implementation.

The [delivery roadmap](../runner-queues/rust-architecture-quality-20261026/README.md)
assigns every finding below a delivery owner and a final verification owner.

## Method and limits

Applied the installed `rust-skills` rules for workspace dependencies, additive
features, module boundaries, library errors, diagnostic privacy, large enum
variants and measurement before optimization. Used locked offline Cargo metadata,
normal dependency trees, targeted source inspection, Clippy 0.1.97 on Rust 1.97.1,
and isolated deterministic probes. Codanna was unavailable; source discovery used
bounded text searches. No provider calls, secrets, OS qualification, full test
suite, live queue mutation or implementation changes were part of this review.

The focused Clippy command selected `editac-core`, `editac-session` and
`editac-wasm` libraries with `-W clippy::all`. It completed successfully, including
diagnostics from local dependencies. Excluding vendored Yrs, it reported 105
warnings: core 44, session 42, Markdown 13, HTML 4 and diff 2. Categories included
54 `collapsible_if`, 34 `result_large_err`, four `large_enum_variant`, and one
`arc_with_non_send_sync`. These are triage inputs, not 105 confirmed defects.
Clippy did not cover the CLI, FFI, native-store feature or every feature combination.

## Findings and decisions

### F01 — Required Yrs fork is not a dependable standalone-root contract

`core/crates/editac-formats/Cargo.toml` declares its own workspace without the Yrs
patch in `core/Cargo.toml`. Core now calls fork-only methods, including
`copy_local_redone_from`, `try_visit_map` and `try_visit_sequence`.
An isolated consumer of `editac-formats` with `jobs` resolved registry Yrs and
failed with eight compiler errors. Adding the existing local Yrs patch to that
consumer made compilation pass. Locked metadata passed for core, CLI and
formats-WASM; formats and formats-native required lockfile updates.

Make the required fork consistent across supported roots and fixtures that consume
current core. Choose one explicit source policy; do not create another reader or
semantic implementation. Refresh only affected lockfiles. Cargo ignores patches
declared by dependency workspaces, so a successful root build cannot prove a
standalone consumer works. [Cargo patch reference](https://doc.rust-lang.org/cargo/reference/overriding-dependencies.html#the-patch-section).

### F02 — Asset-only browser consumers compile source-editing dependencies

The normal WASM dependency tree is
`editac-wasm -> editac-session -> editac-markdown -> pulldown-cmark`.
The browser uses session assets and revision support, but `edit_service`,
`review_apply` and `ai_proposal` are unconditional modules and Markdown is an
unconditional dependency. `session.rs::apply_prepared_service` and
`commit_service_plan` also refer directly to source-service types; gating only
`lib.rs` would leave an incomplete split.

First isolate those service methods, then make the source-edit capability additive
and opt-in for consumers that need it. Keep browser assets/revisions and ordinary
session durability independent. Preserve the existing source-edit workflow in
CLI, native, host and conversion consumers by enabling the capability explicitly.
This is a compile-graph finding; no emitted-WASM size reduction was measured.

### F03 — Native client contracts depend on the reference server implementation

`core/sdk/c/authority.rs` imports admission types, `companion::strict_json` and
`sqlite::etag` from `editac-document-store`. The FFI manifest therefore depends on
the reference host library, which also compiles HTTP and persistence code.
Extract the storage-independent protocol helpers into a lower shared contract
library consumed by host and client. Preserve the wire format and one validation
implementation. This does not claim that removing the edge removes SQLite from
FFI: native session persistence already uses SQLite independently.

### F04 — Tests duplicate both suites and substantial fixture source

Cargo discovers 72 integration-test targets in `editac-core`.
`structure_conflicts.rs` also includes the standalone `delete_edit_probe.rs`,
`hierarchy_probe.rs` and `split_join_probe.rs`; `table_shape.rs` includes standalone
`table_structure.rs`. At least 21 test functions therefore have duplicate owners.
The 1,416-line schema-v5 fixture mapper is included directly by 24 targets.

Give each scenario one discoverable owner and compile reusable fixture support
through a dev-only crate. Preserve independent oracle logic and historical fixture
bytes. Migrate affected selectors and their owned callers coherently; do not edit
live runner inputs or silently drop scenarios. Cargo documents separate integration
test executables and the cost of many targets. [Cargo targets](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#integration-tests).

### Q01 — Public error formatting exposes recovery content

`editac-session/src/edit_service.rs::ServiceError` derives `Debug`; its
`SourceConflict` contains `base`, `proposed` and `current: Snapshot`. `Display`
delegates to that derived representation. An isolated probe constructed the real
type with synthetic sentinels and confirmed both representations include both
source strings. This demonstrates diagnostic exposure, not an observed external
transmission. `ReviewError` already has a useful content-free Debug implementation.

Use concise content-free Display and structured redacted Debug. Preserve complete
recovery through explicit typed access. Audit nested `Conflict.source/detail` as
well as outer fields. `SessionError`, `ServiceError` and `ReviewError` currently
use empty `Error` implementations; preserve nested causes where they implement
`Error`, with the same redaction guarantees. Do not replace typed failures with
strings or add a macro dependency solely to implement these small traits.
[Rust Error contract](https://doc.rust-lang.org/std/error/trait.Error.html).

### Q02 — Recovery payloads make common error results large

The same probe measured `ServiceError` at 264 bytes and `ReviewError` at 472 bytes
on aarch64 macOS. Clippy reports 34 large-result warnings across the session
closure. These sizes are architecture-specific; no throughput or compile-time
speedup is established. Move substantial cold recovery payloads behind owned
indirection while retaining typed matching, complete bytes and current-document
information. Measure before/after size and preserve cause chains and recovery.
Do not box every command or change a hot command enum merely to silence a lint.
[Clippy result_large_err](https://rust-lang.github.io/rust-clippy/rust-1.97.0/index.html#result_large_err).

### Q03 — Planner responsibilities exceed a useful module boundary

`commands/editor.rs` has 3,680 lines in the reviewed tree. Fragment preparation
occupies much of the first half; `prepare_editor_with_registry_and_preview`
spans roughly 1,270 lines. This is a maintainability finding, not proof of incorrect
semantics. Split fragment preparation and command-family planning into private
modules while preserving one validation/preparation/commit pipeline. Keep the
prepared plan opaque and the semantic engine authoritative; no generic handler
framework or second planner. File splitting alone does not establish faster builds.

### Q04 — Lint findings need a scoped, enforceable policy

Workspace lints currently enforce the Rust unsafe policy but do not establish a
selective Clippy policy. Address demonstrated unused imports and substantive
diagnostics, and record narrow exceptions with reasons. In particular,
`patches.rs::subscribe` uses `Arc<Mutex<...>>` around a callback without Send/Sync
bounds; inspect subscription disposal and reentrancy before changing ownership.
This warning alone is not a concurrency defect. Preserve the FFI crate's audited
unsafe boundary and the stronger core prohibition. Avoid repository-wide
`cargo fix`, blanket pedantic denial, vendored warning cleanup, or exception lists
that merely freeze every current warning.

### A01 — Shared bridge code bypasses a Cargo dependency boundary

`editac-ffi/src/lib.rs` includes `assets.rs`, `bridge.rs` and `comparison.rs` from
the WASM crate with `#[path]`. The same semantic source is reused, which is good,
but ownership and common tests belong in a portable library consumed by both
adapters. Keep JavaScript and UniFFI/C translation at their respective edges.
Extraction must preserve wire bytes, limits and behavior. Native and WASM targets
still require separate compilation; a shared crate cannot remove that requirement.

### P01 — Build tuning requires workflow measurements

Core, CLI and standalone formats roots resolve separate default target directories.
Existing FFI debug outputs include an approximately 275 MiB static archive.
These observations justify measurement of compatible per-lane cache reuse,
development debug information and artifact generation. They are not elapsed-time
benchmarks. Preserve production browser LTO/size settings and all hard caps.
At most one 45-minute optimization batch or two materially different measured
hypotheses may precede independent feature work; defer unsuccessful hypotheses
to existing final fitness ownership. [Cargo build-performance guidance](https://doc.rust-lang.org/cargo/guide/build-performance.html).

## Existing ownership and acceptance

This follow-up supplements ENG/NAT/FIT/ECO contracts rather than reopening completed
tasks wholesale. Reuse applicable current-source receipts. The planned queue owns
the specific Rust gaps above; canonical architecture fitness and final runtime
qualification retain their broader responsibilities. All roadmap work remains
unchecked until implemented and validated. No publication, deployment, paid
inference, document conversion, new runner or live queue adoption is authorized.

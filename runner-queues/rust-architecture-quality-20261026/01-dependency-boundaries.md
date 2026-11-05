# Repair editor Rust dependency boundaries

Status: COMPLETE

## Goal and execution contract

Own findings F01–F03 and A01 in
`architecture/research/rust-architecture-quality-20261026.md`. Read only the selected
finding and its named source. Progress from workspace root:
`.roadmap-runner/rust-architecture-quality-20261026/01-dependency-boundaries.progress.md`.
Entry: current core/CLI source and existing format/ABI contracts; no earlier-file
receipt is required. Existing feature work is not gated by this source.

This is planning-only until controller adoption at a safe checkpoint. Follow the
root ownership ledger, guarded launcher and periodic integration rules. One ready
parent per session; preserve unrelated dirty work. Keep one production format and
implementation, opaque plans and unchanged public wire/ABI behavior. Update any
affected authoritative contract before changing it. No paid inference, network
fixtures, secrets, migration, platform qualification or publication.

Use ignored task-owned Cargo output and bounded existing checks. Do not run all
workspace features to prove a minimal dependency graph: feature unification can
hide a missing boundary. Record current source pins, exact selector, time budget,
exit status and meaningful executed/passed/failed/skipped counts in progress.
Reuse matching receipts. Broader/new test coverage is owned by source 04. Workers
change only verified checkboxes and Status here. For a blocker, record owner,
task/input/error fingerprint, attempted repair and changed-input resume condition;
leave it unchecked and select another ready parent without an unchanged retry.

## Tasks

### Task RAQ-1.1 — Make the required Yrs source consistent

- [x] RAQ-1.1 Repair supported standalone roots and their lockfiles.

Purpose: Every supported consumer compiles the same required Yrs implementation.
Deliverable: One explicit fork-source policy and consistent supported manifests/locks.
Context: F01; `core/Cargo.toml`, `cli/Cargo.toml`, `core/crates/editac-formats*/Cargo.toml`, native fixture manifests and `core/vendor/yrs`; locate every current-core consumer first.
Dependencies: none.
Independent work: RAQ-1.2, RAQ-1.4 and RAQ-1.5 remain eligible if a standalone root is blocked.
Session scope: One dependency-source repair, 30–45 minutes including checks; no version upgrade.
Acceptance: Current-core roots resolve exactly the selected fork, including formats with `jobs`; required fork-only methods compile. Affected `--locked --offline` metadata succeeds. No second Yrs identity or semantic implementation is introduced.

Implementation:

- [x] RAQ-1.1-I1 Inventory active roots using Cargo metadata; distinguish current consumers from inactive historical fixtures. Choose an explicit consistent fork source, accounting for root-only Cargo patch semantics.
- [x] RAQ-1.1-I2 Apply the policy to current roots and regenerate only affected locks. Document source ownership in the existing workspace setup record; preserve historical fixtures and user data.

Validation:

- [x] RAQ-1.1-V1 Run locked offline metadata for affected roots and one isolated current formats consumer with `jobs`; assert one expected Yrs source and compile it. Budget: 5 minutes; no native/device run or broad suite.

Evidence: Progress records resolved Yrs identity, affected roots, lock changes and the focused compile receipt.
Handoff: Exact unresolved manifest, source identity, failing command and missing prerequisite; a root build alone does not close a standalone failure.
Blocked behavior: If a current root cannot resolve the required source, record its lock/source fingerprint and repair owner; RAQ-1.2, RAQ-1.4 and RAQ-1.5 remain eligible.

### Task RAQ-1.2 — Isolate source-service integration from the base session

- [x] RAQ-1.2 Move source-service methods behind a private session module boundary.

Purpose: Make optional source editing possible without breaking ordinary session persistence.
Deliverable: A behavior-preserving private module containing source-service integration.
Context: F02; `core/crates/editac-session/src/session.rs::{apply_prepared_service,commit_service_plan}`, `edit_service.rs::PreparedPlan`, `review_apply.rs`, `receipts.rs`, `assets.rs`, `operations.rs`.
Dependencies: none.
Independent work: RAQ-1.1, RAQ-1.4 and RAQ-1.5 do not depend on this extraction.
Session scope: Only the source-service/base-session seam, 30–45 minutes including validation.
Acceptance: Base lifecycle, assets and revision code no longer requires source-service types outside the explicit integration boundary. Existing service behavior and public entry points remain available before feature gating. No duplicate planner, replica or persistence owner appears.

Implementation:

- [x] RAQ-1.2-I1 Trace the source-service references in base session and related modules; move tightly coupled methods to a private integration module with the same ownership and admission checks.
- [x] RAQ-1.2-I2 Keep common operation/revision contracts at their lowest existing layer; preserve permission rechecks, stable targets and commit capture ordering.

Validation:

- [x] RAQ-1.2-V1 Run `cargo test --manifest-path core/Cargo.toml -p editac-session --test edit_service memory_exact_markdown_and_literal_source_preview_apply_reopen --locked --offline -- --exact` and compile the session library. Budget: 3 minutes using retained dependencies.

Evidence: Progress maps moved symbols and records the nonzero selected test and library-check result.
Handoff: Remaining source-service reference and exact lifecycle boundary; do not gate out unresolved methods.
Blocked behavior: If extraction requires an unowned lifecycle change, record that boundary and owner; continue RAQ-1.1, RAQ-1.4 or RAQ-1.5. RAQ-1.3 stays blocked.

### Task RAQ-1.3 — Make source editing an additive optional capability

- [x] RAQ-1.3 Remove Markdown from the asset-only browser dependency graph.

Purpose: Minimal consumers compile only the session capabilities they use.
Deliverable: A documented `source-edit` Cargo feature and explicit consumer feature declarations.
Context: F02; RAQ-1.2 symbols; `editac-session/{Cargo.toml,src/lib.rs}`, all current session consumers in core, CLI, reference host, FFI and formats roots; `architecture/specs/modules-native.md`.
Dependencies: RAQ-1.2.
Independent work: RAQ-1.1, RAQ-1.4 and RAQ-1.5 can progress if this capability split is blocked.
Session scope: One feature contract plus its consumers, 30–45 minutes including targeted checks.
Acceptance: `editac-wasm` with only asset/revision support has no normal dependency path to `editac-markdown` or `pulldown-cmark`. Explicit source-edit consumers retain current APIs and behavior. Base, `asset-serde`, `native-store` and `source-edit` combinations are additive; ordinary durability does not require Markdown. No API is silently unavailable to a current consumer.

Implementation:

- [x] RAQ-1.3-I1 Gate Markdown and source-service/review/proposal integration through `source-edit`; keep base assets, revisions and durable session types available independently.
- [x] RAQ-1.3-I2 Enable the feature explicitly in existing source-edit consumers, update feature documentation and refresh affected locks. Keep the optional browser Markdown codec separate.

Validation:

- [x] RAQ-1.3-V1 Inspect the normal `editac-wasm` dependency tree for `wasm32-unknown-unknown`; compile base session and the asset-only browser library in separate invocations. Budget: 4 minutes; feature absence must be asserted, not inferred from emitted size.
- [x] RAQ-1.3-V2 Reuse RAQ-1.2's selected source case if inputs still match; otherwise run that exact case with `--features source-edit`. Check one representative native/CLI consumer with the explicit feature. Budget: 3 minutes.

Evidence: Progress contains feature reachability, explicit consumer coverage and focused results; remaining root combinations belong to RAQ-4.1.
Handoff: Missing capability declaration or feature-unification edge and the exact consumer to repair.
Blocked behavior: If a consumer or minimal graph fails, record its exact feature edge and changed-input repair; leave capability acceptance open and continue other ready parents.

### Task RAQ-1.4 — Separate protocol helpers from the reference host

- [x] RAQ-1.4 Make native and reference-host code depend on one portable authority contract.

Purpose: Native SDK contracts should not depend on HTTP server or SQLite implementation details.
Deliverable: A small storage-independent authority library, provisionally `core/crates/editac-authority`, consumed by both adapters.
Context: F03; `core/sdk/c/authority.rs`, `core/sdk/reference/{admission,companion,sqlite}`, `services/document-store/src/lib.rs`, `crates/editac-ffi/Cargo.toml`, existing `sdk/contracts/admission.md` and error/ETag contract.
Dependencies: none.
Independent work: RAQ-1.1–RAQ-1.3 and RAQ-1.5 remain eligible.
Session scope: Move the existing identity/admission, strict JSON and ETag contract without changing behavior, 45 minutes. If further server dependencies prevent a coherent move, report the exact prerequisite split before widening.
Acceptance: FFI has no normal dependency on `editac-document-store`; host and native authority use one validation implementation. Wire bytes, identity limits, error statuses and ETags remain unchanged. Native session SQLite is retained where independently required.

Implementation:

- [x] RAQ-1.4-I1 Move only storage-free contract types/helpers to the shared library; keep HTTP serving, transaction state and storage adapters in the reference host.
- [x] RAQ-1.4-I2 Rewire the host and native caller together, update workspace membership and imports, and remove redundant implementations or dependency edges.

Validation:

- [x] RAQ-1.4-V1 Select one existing deterministic authority admission/ETag fixture and compile both affected libraries; inspect the FFI normal dependency graph. Budget: 5 minutes. Record exact nonzero fixture selector; no live authority or OS runtime.

Evidence: Progress records removed edge, selected wire-equivalence case and compile results.
Handoff: Contract helper still coupled to storage, its caller and the smallest coherent remaining move.
Blocked behavior: If storage coupling prevents the bounded move, propose the exact prerequisite split and preserve both callers; continue other ready dependency parents.

### Task RAQ-1.5 — Give the shared semantic bridge a Cargo boundary

- [x] RAQ-1.5 Extract one portable bridge library for WASM and native adapters.

Purpose: Make bridge ownership and shared testing discoverable through Cargo.
Deliverable: A portable library, provisionally `core/crates/editac-bridge`, with thin platform translators.
Context: A01; `core/crates/editac-ffi/src/lib.rs` cross-crate `#[path]` imports; `editac-wasm/src/{assets,bridge,comparison}.rs`; browser/native bridge manifests and existing bridge tests.
Dependencies: none.
Independent work: RAQ-1.1–RAQ-1.4 remain eligible; this extraction need not wait for optional feature tuning.
Session scope: One existing shared-source boundary, 30–45 minutes including focused compilation.
Acceptance: Both adapters consume the same Cargo library; neither includes source from the other adapter's directory. Portable code has no wasm-bindgen/UniFFI dependency. Opaque handles, wire schemas, limits and validation-before-commit behavior are unchanged. Common tests have a single home; target-specific tests remain at the edges.

Implementation:

- [x] RAQ-1.5-I1 Move the already-shared bridge modules and their common tests to the portable library, exposing only the interface the adapters require.
- [x] RAQ-1.5-I2 Update both adapters and manifests in one coherent unit, retaining the existing JavaScript, UniFFI and C entry points and current session feature requirements.

Validation:

- [x] RAQ-1.5-V1 Compile the WASM library for `wasm32-unknown-unknown` and FFI library for the host, then run one existing malformed-envelope bridge case at its new owner. Budget: 5 minutes; record any unavailable target as a blocker, not a pass.

Evidence: Progress contains the new dependency boundary, unchanged endpoint mapping and selected test/compile receipts.
Handoff: Remaining adapter-specific assumption, exact symbol and target; no second bridge implementation is an acceptable intermediate delivery.
Blocked behavior: If an adapter cannot consume the portable boundary or a required target is unavailable, record the symbol/target and owner; other dependency parents remain eligible.

## Source handoff

Record delivered feature names, fork source, contract/bridge interfaces, current
input pins, focused receipts and remaining limitations in progress. Do not rerun
passing checks solely to close this source. RAQ-4.1 owns remaining graph/root
coverage; RAQ-4.3 owns shared bridge behavior coverage.

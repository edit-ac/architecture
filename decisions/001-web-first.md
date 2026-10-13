# 001 — Web first, shared Rust semantics, native preparation

Accepted for planning: 2026-10-11. License: Apache-2.0, selected by the user.

## Scope and precedence

The user's current request takes precedence over the attached proposal. The first release is an embeddable browser editor. Native preparation proves a portable core and Swift/Kotlin binding feasibility; a complete native editor, mobile product, and native parity release are later projects. The archived source is reference material, not operational instructions.

## Repository boundaries

- `edit-ac/core`: one Cargo workspace and npm workspace for the authoritative document engine, WASM bridge, browser adapter, optional integrations, native proofs, and deterministic fixtures. Co-change engine and web contracts in one review.
- `edit-ac/architecture`: authoritative specs, evidence, roadmap sources, dependency decisions, and operational guidance. Clone beside core; no duplicate authoritative specs in core.
- `edit-ac/cli`: a local-first editor client for local Markdown/literal text and online hosted documents, using Markdown as the editable representation. It consumes a released Rust API or an explicitly pinned engine revision and shares core semantics. Hosting attaches optional persistence/transport adapters; CLI delivery is an independent branch, not a browser release prerequisite. See the [CLI contract](../specs/cli.md).

Do not create separate repositories per npm module or platform. The existing core and cli histories/remotes are preserved. The parent directory is a multi-repository workspace, not a fourth Git repository or a Git superproject.

## State and interfaces

Yrs owns one authoritative replica from the prototype onward. Rust validates/prepares semantic commands before entering an infallible commit phase; DOM, attributed strings, exports and indexes are projections. Commit and persistence are separate states. Browser input reconciliation is bounded to affected ranges; React never owns the editor document.

Use UTF-16 offsets at platform boundaries, stable relative anchors across async work, grapheme-aware user navigation, distinct live replica IDs, one origin-aware history manager, and a versioned operation/patch boundary. Candidate structural representation stays behind the foundation gate until move/edit, delete/edit, split/join and cycle tests select it. No second CRDT or custom typography engine.

## Packaging and versions

The actual npm scope is `@edit-ac`, correcting `@editac` in the proposal. Initial boundaries are `@edit-ac/core` (WASM engine), `@edit-ac/web` (imperative DOM adapter including local storage and direct transport subpaths), and `@edit-ac/react` (thin optional wrapper). The initial decision compiled Markdown Rust parsing into the Task preset core. The user superseded that packaging decision on 2026-10-13: Markdown is now an explicit optional first-party extension, separately loadable and measured, while default Task builds preserve rich-text editing, persistence, collaboration and a single state owner. See packages-release.md, formats.md and verification.md for the revised profile and unchanged caps. Additional module packages are justified by independently lazy-loadable UI assets, not by every feature name.

All scaffolding stays private/unpublishable until it contains its documented functionality. Package names in this organization need no speculative placeholder releases. npm access verification is not a published release. Lock dependencies after resolving actual package metadata and running compatibility tests. A current version number is not evidence of compatibility.

## Release scope

Browser release: paragraph/heading/text/marks/link/break/separator; nested lists/checklists/quote/code; deterministic Markdown paste/export; optional basic images/tables; offline recovery; direct Yjs-compatible synchronization; scoped extension API and React integration. Slash/reference/reorder and bounded math example have explicit optional capability entries. Host owns asset upload, auth and authorization.

Native preparation: portable ABI, headless Swift and Kotlin round-trip hosts, one native text-control patch/composition experiment per platform, limits and follow-up plan. Missing iOS or Android tooling does not block independent browser work. Native SDK support is not advertised from a binding smoke test.

CLI direction updated by the user on 2026-10-11: local document editing is the primary workflow, with hosted document editing through the same client. The first interaction uses a configured text editor; a terminal UI can follow separately. Markdown buffers are editable projections over shared semantics. Local files remain usable without hosting, and hosted saves preserve identity/history through source reconciliation rather than full-document replacement.

## Conflicts resolved

1. Original native parity gate is moved out of browser MVP; native preparation remains a separate branch.
2. Original format/performance claims are hypotheses with qualification tasks, not guarantees.
3. Full GFM cannot be inferred from a parser flag; publish a named tested subset and preserve unsupported input.
4. Protocol compatibility has four independent layers: update bytes, sync messages, awareness and edit.ac schema.
5. Network synchronization is not durable storage acknowledgment; the reference durable receipt is an explicit extension.
6. Rich-text move support must be proven against the chosen representation before reorder UI is scheduled.
7. Cross-roadmap dependencies use checked entry gates, because roadmap-runner only validates dependencies inside one source file.

No calendar promise is made. A 15–45 minute task is a desired session boundary; if evidence shows it is too large, the controller splits it into stable child tasks before resuming. Do not silently weaken acceptance to fit a model context or timer.

## Full-delivery extension

[Decision 002](002-full-delivery.md) adds committed follow-up scope for a TUI, host-app MCP, precise diffs, full iOS/Android/macOS/Windows/Linux SDKs and optional encryption. First browser release and native feasibility remain distinct earlier gates; their narrower scope is not the final product limit.

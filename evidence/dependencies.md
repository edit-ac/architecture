# edit-ac dependency and architecture verification

Reviewed 11 October 2026 against the complete proposed roadmap and official documentation/registries. These are design recommendations and verified API facts, not tested implementation or performance results. Context7 instructions were read; Context7 tools were unavailable, so official docs and registry metadata were used.

The [locked dependency probe](dependency-probe/README.md) subsequently passed native and wasm32 type checks with Rust 1.97.1, using the exact Rust pins below. This establishes dependency resolution/type compatibility only; runtime, Yjs schema, release artifact and performance gates remain open.

## Resolved scope and naming conflicts

- The user's current scope is a web editor and native preparation. It supersedes the attachment's requirement to ship complete iOS/Android editors in the MVP. Native preparation needs portable contracts and a binding proof; native input parity remains a later, separately gated roadmap.
- The publishing scope is `@edit-ac/*`, not the attachment's `@editac/*`. The existing scaffold uses Rust crate names `editac-*` with Rust identifiers `editac_*`; preserve that convention.
- A small WASM size and the original performance budgets are targets, not established feasibility. Measure full required JS/WASM/CSS and first accepted input; preserve evidence if targets fail.
- Yrs is authoritative. Yjs belongs in interoperability fixtures, not a second writable production browser model. Existing providers accepting `Y.Doc` do not automatically accept a Yrs/WASM handle.

## Candidate exact dependency pins

Public registry metadata was fetched successfully with read-only network escalation. The original registry responses were inspected during setup; the public URLs below allow rechecking. Temporary local records are not a portable evidence dependency. Versions are proposals until lockfile/build and protocol conformance checks succeed.

| Dependency | Exact candidate | Verified metadata | Intended use / constraint |
|---|---|---|---|
| yrs | 0.28.0 | MIT; published 2026-09-17; no registry `rust_version` declared | Core; enable `small-client` for Yjs 13; set UTF-16 explicitly |
| yjs | 13.6.33 | MIT; Node >=16, npm >=8 | JS interoperability fixtures only; stable line, not v14 RC |
| y-protocols | 1.0.7 | MIT; peer `yjs ^13.0.0`; Node >=16 | Protocol fixtures; not a `Y.Doc` adapter for Yrs |
| pulldown-cmark | 0.13.4 | MIT; Rust >=1.71.1 | Initial parser candidate with explicit profile/conformance gate |
| wasm-bindgen | 0.2.129 | MIT OR Apache-2.0; Rust >=1.81 | WASM boundary; CLI must match crate version exactly |
| wasm-pack | 0.15.0 | MIT OR Apache-2.0; no registry MSRV | Build tooling only; explicit web target and artifact tests |
| uniffi | 0.32.2 | MPL-2.0; no registry MSRV | Native-preparation spike; keep runtime/generator versions aligned |

Exact registry URLs: [Yrs](https://crates.io/api/v1/crates/yrs), [Yjs](https://registry.npmjs.org/yjs/latest), [y-protocols](https://registry.npmjs.org/y-protocols/latest), [parser](https://crates.io/api/v1/crates/pulldown-cmark), [wasm-bindgen](https://crates.io/api/v1/crates/wasm-bindgen), [wasm-pack](https://crates.io/api/v1/crates/wasm-pack), [UniFFI](https://crates.io/api/v1/crates/uniffi).

Registry MSRVs do not establish the workspace MSRV: Yrs/UniFFI and transitive crates need a compiler/build probe. Select the actual installed or CI toolchain explicitly and record its successful version; do not invent compatibility from missing metadata. Preserve licenses and generated dependency notices. UniFFI's MPL license is a dependency fact, not a reason to infer the project's own license.

## Critical facts and implementation consequences

### CRDT compatibility, offsets, and command failure

Yrs 0.28 uses 53-bit client identifiers by default. Its `small-client` feature supports older Yrs <=0.26 and Yjs pre-v14. Distinct active replicas must have distinct IDs. Use one document factory that selects `small-client`, `OffsetKind::Utf16`, stable root names, schema/epoch metadata, and update-v1 encoding for the initial interoperability profile. Do not rely on defaults. [Yrs crate documentation](https://docs.rs/yrs/latest/yrs/)

Yrs defaults to byte offsets; explicit UTF-16 is supported. DOM/native boundaries count UTF-16 code units, while user navigation/deletion must respect grapheme boundaries. Test supplementary characters, combining sequences, flags, ZWJ emoji, RTL, and offsets inside surrogate pairs. Return typed invalid-boundary errors before mutation. [Text API](https://docs.rs/yrs/latest/yrs/types/text/trait.Text.html)

Yrs commits when a mutable transaction is dropped; it does not provide ordinary error rollback. Resolve anchors, validate schema/resource limits, and prepare all fallible steps before opening the live mutation transaction. Revalidate preconditions against the current document revision before commit. A sequence of fallible mutations must not be described as atomic simply because it shares a transaction. [Yrs transaction lifecycle](https://docs.rs/yrs/latest/yrs/)

UndoManager groups changes by capture interval and origins, not exactly one entry per transaction. Explicitly separate semantic operations using reset boundaries and tracked local origins; exclude remote/restore operations. Test undo after remote edits, composition, move, and paste. Define dynamic undo scope for newly created shared text. [Yrs UndoManager](https://docs.rs/yrs/latest/yrs/undo/struct.UndoManager.html)

### Structural schema is a blocking design spike

Yrs XML and a block-registry/placement model have different tradeoffs. A registry is not automatically correct. Test move/move, move/edit, delete/edit, split/edit, join/edit, list nesting, ancestor cycles, orphans, invalid references, duplicate updates, and all relevant merge orders before freezing either representation.

Candidate design: stable content IDs plus a single replacement value for each placement tuple, rather than independently merged parent/order fields. This is a proposal, not an established protocol. Specify deterministic projection and ordering under concurrency; no platform-specific repair writes. Preserve inaccessible concurrent content for recovery. Schema selection must block production renderer/serialization implementation, but fixture and input spikes can proceed independently.

### Markdown coverage is narrower than a GFM label suggests

pulldown-cmark 0.13.4 is an event parser with individual options for tables, task lists, and strikethrough. Its `ENABLE_GFM` option currently documents blockquote callout tags; it must not be treated as a switch for full GitHub-flavored Markdown. Bare-URL/email autolinks and safe raw-HTML admission need explicit fixtures and implementation decisions. [Parser API](https://docs.rs/pulldown-cmark/latest/pulldown_cmark/), [options](https://docs.rs/pulldown-cmark/0.13.4/pulldown_cmark/struct.Options.html)

Use CommonMark 0.31.2 plus a named edit-ac extension profile, not an unqualified GFM-conformance claim. GFM's published specification is based on CommonMark 0.29; pin both fixture baselines and record differences. A parser spike must prove the required extension set or produce an ADR selecting another parser/composable extension before Markdown implementation. No silent content loss. [CommonMark](https://spec.commonmark.org/), [GFM](https://github.github.com/gfm/)

The parser is not a serializer or sanitizer. Define deterministic semantic Markdown export separately. Underline, unknown atoms, table cells, and unsupported raw HTML need explicit representability/fallback diagnostics. HTML clipboard import needs a separate allowlisted semantic importer with URL validation; avoid assuming parser safety applies to imported DOM.

### WASM and native preparation

`wasm-pack --target web` emits browser ES modules with explicit WASM initialization; bundler and Node output modes differ. Choose one production loading contract, expose asset URL/init control for CSP/CDN/SSR hosts, and test packed consumer installation in a browser and SSR import. Avoid generated output `package.json` accidentally overwriting hand-maintained public package metadata. [wasm-pack build](https://rustwasm.github.io/docs/wasm-pack/commands/build.html)

UniFFI generates bindings for Rust interfaces including Swift/Kotlin; it does not supply native packaging or text-editing views. Its guide explicitly separates binding generation from shipping the Rust library. Native-preparation acceptance is a compilable shared-core call, deterministic fixtures, ownership/thread/error contracts and measured copy counts. Full UITextView/Editable adapters, IME, attachments, accessibility and real-device validation are a distinct future workstream. [UniFFI guide](https://mozilla.github.io/uniffi-rs/latest/), [UniFFI crate](https://docs.rs/uniffi/latest/uniffi/)

### Input and durability

The Input Events specification makes IME composition input noncancelable. `beforeinput` alone cannot enforce model ownership. Browser reconciliation requires composition/input handling, stable selection anchors, bounded fallback observation and suppression of adapter-generated mutations. Avoid patching the active composing subtree; decide and test what happens when a remote deletion removes that target. Synthetic events cannot qualify real operating-system IME behavior. [Input Events Level 2](https://www.w3.org/TR/input-events-2/), [MDN browser behavior](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event)

IndexedDB strict durability is a hint. Local acknowledgment follows transaction completion; storage eviction, user deletion and all power failures cannot be promised away. Journal immutable updates, publish checkpoint+coverage metadata transactionally, retain unacknowledged local writes, preserve a prior recovery point, and test every commit boundary. A sync handshake is not a durable remote receipt; the latter is a versioned application-level extension. [IndexedDB specification](https://w3c.github.io/IndexedDB/)

## Smaller-model task implications

Each task needs one bounded artifact/behavior, exact prerequisite IDs, owned paths, commands, a fixture-based acceptance result, and an explicit stop condition. Structural schema, browser composition, parser profile, ABI and dependency checks are gates with ADR/evidence outputs; never mark feasibility as proven by writing scaffolding. Maintain failure/skip evidence, use deterministic fixtures only, and keep paid providers out of all tests.

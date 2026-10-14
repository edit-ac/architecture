# Public extension library contract

Status: development contract extending the qualified first-party modules.

The library exposes the existing [portable module contract](modules-native.md)
through stable, documented entry points and conformance fixtures. It consumes
the [shared client contracts](client-contracts.md) and [Markdown contract](formats.md).
It does not recreate the existing slash/reference/reorder/image/table/math
implementations or turn document data into executable plugin code.

## Public entry points and registration

Publish supported Rust descriptor/command/codec interfaces from their owning
crate and browser integration from documented package exports. Use the existing
`@edit-ac/core` and `@edit-ac/web` boundaries unless a measured, independently
consumed feature justifies another package. Internal source paths are not public
import contracts. Pin fixture consumers to immutable packages/revisions.

Each descriptor names a namespace, type, version, content shape, bounded
attributes, applicable built-in commands, Markdown codecs, fallback policy and
supported host capabilities. Validate descriptors before attaching a document;
duplicate/incompatible registrations fail without partial mutation. Freeze a
session's registry according to the existing schema/initialization contract.

Data-defined marks and atoms using qualified schema/command primitives register
without rebuilding the Rust engine or its WASM/native bindings. This does not
promise arbitrary new editing semantics without engine work. A host may supply
its own renderer implementation through a typed interface; renderer callbacks,
code and downloaded executable plugins never live in document state. Unknown
types and versions retain their bounded original payload and explicit fallback.

### Implemented public v1 entry points

`@edit-ac/core/extensions` owns the portable registry (also re-exported compatibly
by `@edit-ac/web`). `@edit-ac/web/modules` exposes that same registry with browser
runtime/presenter contracts; heavy math remains `@edit-ac/web/math`.
`EXTENSION_API_VERSION = 1` and the `ModuleDefinitionV1`, `ExtensionCommandV1`,
`MarkdownCodecV1`, `MarkdownExtensionV1` aliases identify this API contract, not
stored module data versions. Existing bounded data versions remain positive u32.
Rust uses `editac_core::modules::v1` and `editac_markdown::v1` re-exports from
owning crates. Public package declarations require no private source imports.

Registration consumes the existing data-only attributed-text contract and freezes
before attachment. It does not authorize a new arbitrary-attribute editing command
or schema migration. Runtime/codec callbacks remain host objects. Invalid,
duplicate and incompatible entries fail before insertion; previously accepted
entries remain unchanged. See packed consumer evidence in
`../evidence/extension-exports.md` for exact artifact qualification.

## Conformance and evolution

The reusable conformance suite accepts a descriptor plus fixed fixtures and
checks validation, deterministic serialization, supported Markdown round trips,
copy/export behavior, command applicability/preparation/commit, undo grouping,
origin handling, subscription filtering, disposal and unknown-version retention.
It compares canonical semantic outcomes rather than raw CRDT byte equality.
Every claimed capability has a test or an explicit external qualification owner.

Codecs preserve unknown/disabled module data or produce recoverable diagnostics
before mutation. A codec cannot silently reinterpret arbitrary source into an
unsupported module. Source-reconciliation fixtures must show that edits elsewhere
retain module identity and content. Literal-text input bypasses Markdown codecs.

Descriptor/schema evolution declares compatible reads, supported migration paths
and unsupported versions. Migration operates on validated candidate data and
commits through the existing schema/epoch transition protocol when required; no
automatic in-place rewrite may invalidate offline updates. Failed migration keeps
the original data recoverable. Qualification includes old/new/unknown versions,
interrupted migration and delayed updates. Module version numbers alone do not
authorize a document-wide schema transition.

### Candidate-data evolution conformance

The public Rust `modules::v1::ModuleEvolution` and browser
`prepareModuleMigration` accept a bounded declaration of compatible descriptor
reads and directed version transitions. Both validate source and target data using
the owning frozen registry. Undeclared/reverse/unknown transitions reject before
calling the trusted host transform. Preparation preserves the original envelope
and returns inert candidate data; there is no document handle, live-state rewrite
or implicit migration on registration. Callback failure or discarding preparation
leaves the original recoverable. A candidate is not a prepared engine edit.
The host must separately use a supported owning edit or explicit new-epoch
migration protocol. This interface does not introduce arbitrary attribute editing
or authorize reinterpreting an existing checkpoint under a different identity.

`prepareExtensionSource` is a reusable browser conformance hook over the owning
Markdown codec and bounded literal-input path. Literal input calls no codecs.
The fixed version corpus is `core/fixtures/extensions/versions/conformance.json`;
EXT-1.4 exercises actual Rust source reconciliation/checkpoints, portable
fragment copy/export, production WASM clipboard/copy and delayed epoch replay.
Reference Markdown export retains a diagnostic and typed recovery when its
identity cannot be represented. Unavailable math/future extension codecs keep
opaque payload and source; this is preservation, not richer format support.

## Presenter and host interfaces

Presenters receive stable node identity, validated content, selection/capability
state and bounded incremental patches. They request edits through shared prepared
commands and expose idempotent update/dispose/cancel behavior. They do not own
another writable document or invoke callbacks under engine transactions. Async
results carry request identity and are ignored after cancellation, disposal or
target revision change. UI actions respect the host's read-only capability.

### Command preparation lifecycle conformance

`@edit-ac/web/modules` exports `ExtensionCommandSession` over the host's existing
`ExtensionCommandHost` capability port. A host supplies current activation,
a document/epoch/content revision token, and its shared `can`/`commit` entry
points (such as `BrowserEditor`). Async preparation carries an abort signal;
superseding, cancellation, disposal or content revision changes reject late
results. Applicability is checked on the returned request and revision/cancellation
are checked again after that callback; commit rechecks current host permissions.
The helper owns no engine, semantic store, subscription bus or mutation escape.

The host retains ownership of preparation/atomic commit, persistence admission
and one-intent history grouping. Observers run through the owning engine and
`ModuleRuntime` after engine transactions return. Returned caret/selection
resources retain their normal caller ownership. Trusted preparation failures are
reported as failed/cancelled outcomes; an exception does not preempt unbounded
in-process execution. The fixed command corpus and canonical Rust/browser checks
are qualified in `../evidence/extension-commands.md`. Browser conformance uses
production WASM, actual storage middleware and prepared IndexedDB completion;
it does not claim OS/device renderer or deployed persistence qualification.

Define separate browser, terminal, Swift/iOS, Kotlin/Android and desktop adapter
contracts for focus, input/composition ownership, accessible labels/actions,
clipboard/Markdown representation, selection/atom boundaries and theme/lifecycle.
Use headless conformance adapters here. Full platform renderers and real-device
evidence belong to their platform tracks; this track supplies their fixtures and
acceptance hooks without depending on those downstream implementations.

## Built-in capability obligations

| Module | Shared obligation | Presenter obligation |
|---|---|---|
| Slash | Local trigger invokes one registered command/history group | Accessible menu and focus restoration; remote edits never open it |
| References | Persistent target identity/label, host resolver, cancellation | Honest unresolved label and accessible explicit activation |
| Reorder | Identity-preserving semantic move and stable selection | Keyboard action on each editable host; pointer handle when supported |
| Images | Bounded metadata, alt text, host asset policy, preserved source | Accessible image or declared fallback; no implicit upload |
| Tables | Bounded rectangle and shared simple-cell commands | Selection/navigation and clipboard behavior or a declared nonediting fallback |
| Math | Bounded source and safe codec, invalid-source retention | Qualified renderer or explicit source fallback; no inferred typesetting parity |

The machine-readable matrix distinguishes data preservation, view, edit, copy,
Markdown, accessibility and optional rendering for every supported host/module
combination. Mandatory product parity cells are explicit; unsupported cells need
an owner and delivery gate rather than disappearing from the matrix. Source-only
fallback meets preservation, not a richer rendering/editing claim. Platform tracks
consume these obligations, and final cross-client qualification verifies them.

Reference lookup/activation uses host-controlled catalog/authority capabilities,
including configured `ac://` resolution. A reference is an identifier, never
credentials or proof of immutable content. Opening/rendering a document does not
implicitly fetch reference targets or images, launch commands, read arbitrary
files or grant remote editing authority. Prepared host-resolver tests cover
revocation, delayed/out-of-order results, forbidden targets and stale anchors.

## Loading, examples and publication boundary

Optional browser presenter assets load only when explicitly enabled/needed.
Minimal bundles omit disabled presenter code/assets; stored data remains readable
through fallback. Record actual JS/WASM/CSS/asset contributions and pinned build
settings. Native/TUI manifests identify optional dependencies and renderer assets;
do not equate a source feature flag with measured binary-size savings.

Provide a third-party tutorial for one data-defined mark and one atom, using only
public imports and the conformance harness. Its clean consumer fixture must work
with unchanged engine artifacts, survive absent renderers, preserve data through
Markdown/source editing, and dispose resources. Show where a genuinely new
editing semantic requires core work. These documentation examples are validated
consumer artifacts, not merely copied implementation snippets.

Build/pack/consumer qualification belongs here; publication follows the release
policy. No marketplace, downloaded plugin execution, remote service deployment
or provider inference is required to demonstrate the library.

## Rich ecosystem delivery

Baseline07/21 contracts remain the foundation. [Rich content](rich-content-extensions.md) adds portable code highlighting, table formatting, assets/embeds and interaction upgrades. [Link resolution](link-resolution.md) separates public metadata from principal-scoped internal references; [conversion](document-conversion.md) provides optional document formats with PDF export only. Roadmaps31–36 integrate actual clients and37 qualifies the expanded profile. Heavy providers remain optional and permission checks stay host-owned.

## Assistive input extension

Track 39 uses these same registration/presenter/conformance interfaces for [assistive input](assistive-input.md). Its descriptor exposes optional command/status/host-transport capabilities without a persisted transcript, second editing model or built-in speech provider. Baseline keyboard, native dictation and accessibility remain usable without the descriptor. Native integrations have task-specific SDK gates and actual platform evidence.

## Mobile web presenter obligations

[Mobile web](mobile-web.md) supplies minimal shared browser focus/viewport/capability ports; [track 41](../roadmaps/41-mobile-web-extensions.md) qualifies existing extension presenters on touch devices. Each presenter declares gesture/focus/scroll ownership, reachable tap controls, cancellation, capability fallback, loading trigger and per-instance resources. Disabled registration causes no feature import/evaluation, listeners/observers, assets, worker or network work. Native selection/scroll/zoom and baseline command access stay usable without enhanced mobile UI.


## Official configuration profiles

First-party ownership must produce repeatable configurations. Track 21 publishes versioned core, document-tools and code-tools presets with exact extension identities, required capabilities, compatible version ranges, deterministic command/keymap/input-rule precedence, schema admission, optional host permissions and explicit conflicts. A host's explicit remapping is allowed and appears in diagnostics; registration/import order cannot silently choose a winner. Validate the entire configuration before activation and report actionable duplicate/conflict/missing-capability errors without mutating an open document. Upgrading or disabling a presenter cannot reinterpret or drop stored content; retain the declared lossless fallback and gate serialization/schema migrations through existing contracts.

Every official descriptor declares focused/nested-control ownership, text versus block drag ownership, composition exclusions, selection/result policy, history grouping, supported platform presenters, cancellation and resource teardown. Reuse the current command registry and lifecycle ports; do not build a parallel event bus or semantic store. SDK default behavior is a tested preset, not an unspecified bag of plugins. No first-party extension may repair baseline selection/input by storing a second document model.

Conformance runs baseline-with-none, every official preset, each feature independently and risk-selected pairs/triads that share input, selection, history, schema or async resources. Record the selection rationale and explicit uncovered combinations; pairwise testing alone does not establish all combinations. Include duplicate registration, permutations where order is declared irrelevant, conflicting keys/input rules, unload/reload at an active selection, stale async completion, renderer failure and observer failure. Preserve committed edits if a post-commit callback throws. In-process exceptions can be isolated; an infinite-loop plugin cannot be safely preempted in the same thread. Heavy/untrusted optional work uses existing worker/process boundaries with time and size limits where needed, not an unsupported claim that try/catch prevents hangs. Disabled presets evaluate no feature modules and create no listeners, workers or network traffic. [Research](../evidence/editing-performance-extension-research.md) and FPX cases supply the evidence boundaries.


## AI writing extension

[The AI epic in roadmap 25](../roadmaps/25-rich-content-extensions.md#epic-rch-2--deliver-optional-ai-writing-through-existing-edit-contracts) delivers the optional [AI writing profile](ai-extensions.md) through these same descriptor, presenter and configuration interfaces: Ask AI, fill/continue text, selected-text actions and opt-in autocomplete. Provider credentials, context permissions and hard request limits remain host-owned; streamed proposals/ghost text stay outside committed document state until explicit acceptance through existing review/semantic commands. Disabled profiles load no AI assets or transports. Capability receipts distinguish each platform subset and mocked integration from model quality. Track 39 and native OS writing tools retain their existing ownership; no speech or Tiptap runtime dependency is added.

## Formatting-preserving transfer capabilities

EXT-1.13 owns the portable extension formatting/clipboard contract. Each descriptor declares admitted inline/block formatting, structured transfer codecs and absent-codec/source-preservation behavior. Table cells preserve marks, links, code, paragraph styles and admitted structure; captions, references, math and future extensions use the same prepared atomic mutation and version/resource checks. Every web/native presenter exposes formatting and literal paste consistently. Unsupported extensions keep bounded inert source with explicit diagnostics; transfer cannot execute code/formulas or fetch assets without a host capability. Native platform tasks own OS-host/simulator fixtures and actual-device qualification remains separate.

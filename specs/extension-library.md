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

## Presenter and host interfaces

Presenters receive stable node identity, validated content, selection/capability
state and bounded incremental patches. They request edits through shared prepared
commands and expose idempotent update/dispose/cancel behavior. They do not own
another writable document or invoke callbacks under engine transactions. Async
results carry request identity and are ignored after cancellation, disposal or
target revision change. UI actions respect the host's read-only capability.

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

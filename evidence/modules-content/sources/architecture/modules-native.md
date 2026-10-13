# Extension modules and native preparation

## Portable extension contract

A registered module declares a namespaced type/version, validated attributes and content shape, commands, codecs and deterministic fallback. Freeze registrations before mounting a document. Dynamic JavaScript behavior is not portable Rust behavior; data-only custom marks and atoms must work without recompilation, while new editing semantics need shared engine work.

The document never contains executable callbacks, downloaded plugins or renderer code. Unknown type/version/renderer preserves original bounded data and displays a safe fallback. Invalid descriptors fail before any document mutation. Platform hooks render existing semantic content and do not own a second writable model.

Subscriptions filter changed kind/range/selection. Stable renderer views receive patches and dispose all owned resources. Asynchronous resolver results carry request identity and cancellation; a stale response cannot mutate the document. Modules do not scan the entire document on each transaction.

## First-party modules

| Module | Required behavior | Boundary |
|---|---|---|
| Slash | Local context trigger, accessible keyboard/touch menu, command invocation | Remote edits never open the menu |
| References | Host resolver, persistent target ID and label, cancellation | No implicit fetch merely from opening a document |
| Reorder | Keyboard and optional handle call one semantic move | Requires proven identity-preserving move policy |
| Images | URL/alt/dimensions metadata, host asset policy, fallback | Uploads/auth are host services |
| Tables | Bounded rectangle, simple cell editing and selection | No merged cells, spreadsheets or layout engine |
| Math example | Bounded LaTeX source, lazy safe renderer, error/source fallback | No full TeX or native typesetting claim |

Publish capabilities separately for read/edit/copy/Markdown/native. A source fallback is preservation, not a claim of native rendering parity. Disabled UI modules must be absent from minimal bundles; their data remains recoverable.

### Bounded reference descriptor

The first reference presenter uses the existing opaque content-block envelope: `["module:editac.reference", 1, {"targetId": string, "label": string}]`. The host owns the opaque target identity; it is never interpreted as a URL or fetched on mount, recovery, render or export. Both fields are nonempty, single-line strings of at most 512 UTF-16 units; target IDs exclude control characters. The atom's committed text is the label fallback. Disabled or unknown renderers preserve tuple and text; Markdown exports the escaped label with an explicit identity-loss diagnostic. This bounded module provides block insertion; inline reference editing is a later extension-library boundary.

The explicit presenter retains a stable range, stores its query outside the document and invokes only the configured host resolver after user activation. Every query owns an AbortSignal and monotonically increasing request identity. Query changes, target changes, composition, read-only, focus exit and disposal invalidate pending work. Only a current result may prepare/commit one atomic fragment through the engine and host commit port. Failed, canceled or invalid results preserve source.

### Bounded image and table presenters

The optional browser `contentModules` factory renders existing v1 opaque image/table tuples. A synchronous host image policy supplies an absolute HTTP(S) asset URL or denies loading; absent policy never loads the authored URL. Alt/title and original source remain inert metadata. Credential-bearing, executable and control-bearing URLs are rejected. Uploads and authentication remain host services.

Simple table cells use labeled native controls for temporary text, selection, copy and composition. The portable prepared `tableCell` editor command carries owner ID, exact expected descriptor, zero-based row/column and bounded single-line text. Rust rejects stale/non-table/out-of-range/invalid edits before live mutation, retains marks on surviving text runs and unaffected cells, and updates the tuple plus inert tab/newline fallback in one atomic history group. The original source field remains import provenance; export uses the current rows. Disabled presenters preserve the tuple and fallback through storage recovery. Merged cells, nested blocks, spreadsheets and full native table editing are outside this boundary.

## Native preparation output

The first browser release does not require native SDK parity. The native roadmap proves the portable boundary and estimates the remaining work with evidence. Use a pinned UniFFI runtime/generator initially; measure copies and call count before freezing it. MPL-2.0 dependency licensing does not change the project's Apache-2.0 source license; retain required notices and review any modifications to dependency files.

ABI: opaque engine handle, explicit drop/dispose, batched commands and patches, stable UTF-16 units, relative async anchors, typed errors and cancellation, versioned schema/profile. Specify which executor/thread owns a handle; no arbitrary callbacks under a live transaction or lock. Expose owned buffers/snapshots, not borrowed Rust internals across FFI.

Build Swift and Kotlin headless fixtures using the same seed/snapshot corpus. Then use one real UIKit/TextKit control and one EditText/Editable control to probe range patching, selection and composition. Record unsupported mark/attachment behavior honestly. Never implement native support through a WebView.

Full native editor work remains a later separately scoped project: marked/composing text, autocorrect/dictation, OS keyboard, undo gestures, clipboard, accessibility, attachments, storage, lifecycle reconnect, packaging and real-device matrix. Binding generation alone proves none of these. Missing Xcode/SDK/device access has an explicit unblock condition and does not gate independent web tasks.

Sources: [UniFFI](https://mozilla.github.io/uniffi-rs/latest/), [UIKit TextKit](https://developer.apple.com/documentation/uikit/textkit), [Android InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection).

## Full native and library follow-ups

The preparation-only scope above applies to roadmap 09. Full requested SDK parity is delivered by [native-sdk-parity](native-sdk-parity.md) and roadmaps 16/17/18/22/23 for iOS, Android, macOS, Windows and Linux. [Extension-library](extension-library.md) and roadmap 21 supply portable public contracts and presenter conformance. Browser release remains independent, but the full-client milestone requires genuine mandatory native editing capabilities.

## Interaction and assistance follow-ups

The slash module follows [editor interactions](editor-interactions.md), qualified by INT-1.9 before browser release. Rich-content catalog-scale behavior remains in RCH-1.16. [Assistive input](assistive-input.md) defines an optional portable assistance descriptor and platform presenters in track 39; baseline accessible editing and native OS dictation remain required when it is absent.

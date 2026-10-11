# edit.ac — MVP Development Roadmap

**Version:** 0.1 · **Date:** 11 October 2026  
**Status:** Proposed architecture and acceptance criteria; no performance results have been measured.  
**Product:** An open-source, embeddable collaborative rich-text editor with a Rust core, a small WASM/browser adapter, and genuinely native iOS/Android editing adapters.

> One document engine. Every platform. Every format. Every consumer.
>
> **This MVP proves the document engine and editing experience—not the entire future platform.**

## 1. Release objective and scope

Replace the everyday Tiptap/Lexical use case: task descriptions, comments, notes, and longer structured documents. Deliver fast initial display, fast *actual editability*, responsive typing, first-class Markdown paste, reliable offline persistence, and concurrent editing across browsers and native controls.

“Replacement” means an alternative editor SDK with a documented migration path. It does **not** mean binary compatibility with ProseMirror plugins, Tiptap extensions, Lexical nodes, or their existing collaborative document schemas.

### Included

| Area | MVP requirement |
|---|---|
| Basic editing | Text, selections, keyboard navigation, undo/redo, clipboard, composition, accessibility, read-only mode |
| Rich text | Paragraphs, headings, bold, italic, strike, underline, inline code, links, hard breaks, separators |
| Structured content | Nested ordered/unordered lists, checklists, blockquotes, fenced code; basic images and rectangular tables through optional modules |
| Markdown | Shared Rust parser and serializer; formatted paste; typing shortcuts; explicit literal-paste mode; documented CommonMark/GFM profile |
| Collaboration | Yrs-backed state, tested Yjs interoperability, reconnect, offline merge, relative selections, optional awareness/carets |
| Durability | Local update journal, safe checkpoints, recovery, unsynced-update retention, explicit persistence failures |
| Extensibility | Typed nodes, marks, commands, scoped subscriptions, portable schema descriptors, per-platform rendering hooks |
| Optional interactions | First-party slash commands, reference/mention commands, block reorder, inline/block math example module |
| Platforms | Browser SDK and native iOS/Android SDKs with sample hosts; no WebView |
| Integration | Headless Rust API, framework-independent web API, thin React wrapper, shared fixtures and migration tooling |

### Excluded

Desktop/mobile product shells, account/workspace products, a commercial cloud, vectors/RAG, AI chat/MCP products, PDF/DOCX ingestion, pagination/print layout, databases, macros, executable documents, a plugin marketplace, and a bespoke binary-container project. A small reference sync service is test/integration infrastructure, not a cloud product.

Native SDK work **is included**. Shipping a mobile application is not. Advanced table layout, merged cells, spreadsheet behavior, full TeX, and pixel-identical rendering across operating systems are not MVP requirements.

## 2. What the reference products tell us

Tiptap is already modular. Its public extension API separates nodes, marks, and behavior; supports configuration, commands, chaining, keyboard shortcuts, and input/paste hooks. Borrow the ergonomic pattern, not its runtime or ProseMirror-specific contracts. [S01]

Tiptap also has an official Markdown integration, including extension-level parsing/serialization, a generic suggestion utility, drag handles, and math nodes. These are feature/API references—not gaps we should pretend do not exist. [S02–S05]

| Tiptap reference | Proposed editac equivalent |
|---|---|
| `Node.create`, `Mark.create` | `defineNode`, `defineMark` with portable schema descriptors |
| `Extension.configure` | Explicit module configuration before mounting |
| `commands`, `chain().run()`, `can()` | Validated commands, one-transaction chains, nonmutating applicability checks |
| Input/paste rules | Local typing recognizers plus a real Markdown parser for pasted documents |
| `parseHTML`, `renderHTML`, node views | Separate import/export hooks and incremental platform renderers |
| Suggestion utility | Shared local trigger engine; web/native menu presenters; cancellable search |
| Drag handle | Reorder UI invoking a semantic move operation |
| Mathematics | Stored LaTeX source plus optional rendering adapters |

Performance comparisons must use optimized baselines. Tiptap documents integration-level rendering controls, and Lexical already performs dirty-node reconciliation and can let the browser handle ordinary text insertion. Avoiding a React rerender is good engineering, not by itself a new advantage. [S06, S07]

**The intended advantage:** shared Rust semantics across web and native, a small measured editing footprint, bounded incremental work, and collaboration/durability that do not need to be added after the model is designed.

## 3. Architecture and state ownership

```text
Host application / optional toolbar / framework wrapper
                         |
          Semantic commands + scoped subscriptions
                         |
     +-------------------+--------------------+
     |                   |                    |
Browser adapter      iOS adapter         Android adapter
DOM/contenteditable  UIKit/TextKit       EditText/Editable
selection + IME      native input       native input
     |                   |                    |
     +-------- compact operation/patch ABI ---+
                         |
                  editac-core (Rust)
       schemas · commands · anchors · local history
       validation · dirty ranges · document projection
                         |
            Yrs store: one authoritative replica
                  /                 \
     persistence adapter        sync adapter
     IndexedDB / native DB      Yjs-compatible protocol
                  \                 /
              checkpoints + binary updates

Rust Markdown parser/serializer -> prepared edit batches
Optional modules -> schemas, commands, renderers, serializers
```

### 3.1 One writable document, not synchronized copies

**Decision:** use Yrs as the authoritative collaborative store from the first prototype, including single-user editing. The Rust semantic layer operates on that store. DOM nodes, native attributed strings, navigation indexes, and JSON exports are projections—not independent writable documents.

This includes a fixed CRDT cost in the base runtime. Networking, awareness, menus, math, and other modules remain optional. Do not build a second “fast local” engine and migrate documents into collaboration later. Revisit this decision only with measured evidence and an explicit architecture change.

Keep lightweight read indexes where necessary; update them from transactions. Do not maintain a second full mutable JSON tree or serialize the whole document after every keystroke.

Yrs documents version-sensitive compatibility settings and unique active-client identity requirements. Pin the Yrs/Yjs pair and its options; do not assume “latest with latest” is automatically compatible. [S08]

### 3.2 Core primitives

The semantic contract contains stable node identities, container/block/inline types, attributed text, typed attributes, relative anchors, transactions, and versioned schema descriptors.

Positions at browser/native boundaries use explicitly defined UTF-16 offsets; Rust UTF-8 storage conversions are tested. User-facing movement/deletion respects grapheme boundaries and native input behavior. Persisted or asynchronous targets use stable anchors rather than stale integer positions. Yrs provides an explicit UTF-16 offset mode; Yjs documents relative positions for concurrent editing. [S09, S10]

Commands must be **prepared and validated before mutating the live store**. Do not assume dropping or failing a Yrs transaction rolls it back: its documented transaction lifecycle commits changes when the transaction is dropped. Fallible parsing and expensive preparation stay outside the mutation phase. [S08]

### 3.3 Structural representation: decide with adversarial tests

In Gate 1, compare a conventional Yrs XML representation with an identity-preserving block registry and separate placement metadata. Favor the latter if it passes the editing tests without excessive complexity.

Candidate: each block owns its text/attributes independently of its location. A move changes a placement record, not the text object. Placement changes should be indivisible at the semantic level, with deterministic ordering and a specified concurrent-move policy.

Before freezing the schema, prove simultaneous move/move, move/edit, delete/edit, split/edit, join/edit, and nested-list operations. Define one winning placement, cycle/orphan handling, and recovery behavior for content edited concurrently with deletion. Do not clone/delete rich-text objects as a shortcut for moving them.

A converged CRDT can still represent an invalid or surprising editor structure. Define deterministic projection rules; do not let each platform “repair” the document by emitting different corrective writes.

### 3.4 Suggested repository structure

```text
crates/
  editac-core/          # Semantic model, commands, Yrs integration, anchors
  editac-markdown/      # Parser, serializer, shared dialect and fixtures
  editac-store/         # Persistence contracts, native journal/checkpoints
  editac-wasm/          # Compact web binding; no DOM engine here
  editac-ffi/           # Swift/Kotlin bindings
packages/
  web/                 # DOM adapter and imperative API
  react/               # Thin host wrapper; not document ownership
  persistence-web/     # IndexedDB adapter
  sync-web/            # Wire protocol, reconnect, awareness
  modules/             # Slash, references, reorder, math, images, tables
native/
  ios/                 # Native editing view and Swift package
  android/             # Native editing view and Android library
examples/
  task-editor/         # Minimal web host
  ios-host/            # SDK validation host, not a product application
  android-host/
  sync-server/         # Reference relay + durable persistence contract
spec/
  model.md
  protocol-profile.md
  module-contract.md
  durability.md
  markdown-profile.md
benchmarks/
fixtures/
```

Keep these as a few cohesive libraries rather than dozens of premature micro-packages. UniFFI is a candidate for generated Swift/Kotlin bindings; benchmark its boundary and copying costs before freezing the ABI. [S11]

## 4. Browser editing: the critical path

Use one coherent editing surface for normal text flow, with semantic block mapping and inline noneditable attachments as needed. Do not default to a separate `contenteditable` root for every paragraph: cross-block selection, navigation, clipboard, and accessibility must work as a continuous document.

For ordinary text insertion, allow native browser behavior where proven correct and reconcile the affected range. For structural changes, use explicit commands. During composition, retain native ownership of the active composition surface and reconcile with stable anchors; remote changes must not replace the composing DOM subtree underneath the input method.

`beforeinput` alone is insufficient. Some edits do not produce a usable/cancelable event, including composition and browser corrections. Implement `input`, composition events, and a bounded mutation-observer fallback. [S12]

**Per edit:** resolve the affected range → prepare/commit one semantic edit → emit a compact dirty-range patch → update only affected DOM/native spans → enqueue persistence and synchronization.

No whole-document HTML/Markdown serialization, global formatting scan, framework rerender, synchronous network request, or renderer reconstruction belongs on this path. The application’s save callback receives update metadata/bytes, not a newly generated full-document JSON tree.

Keep ordinary editing and its authoritative model together on the browser thread initially. Use workers for sufficiently large independent parsing/export jobs—not an asynchronous round trip for every key. A worker-produced insertion batch still has transfer and main-thread CRDT-application costs; measure both.

Use one editor-owned semantic history system. Browser and native undo gestures delegate to it. Composition, Markdown paste, formatting, and reorder each have intentional undo grouping. Remote changes do not become local undo entries. Tiptap’s collaboration documentation similarly requires replacing its normal history with collaboration-aware history. [S13]

## 5. Loading that feels instant without hiding work

Expose distinct lifecycle signals:

- `visible`: content is displayed.
- `ready`: the authoritative state, input handlers, selection mapping, and persistence adapter are attached; input can be accepted.
- `localCommitted`: a particular update has completed its local persistence transaction.
- `remoteCommitted`: a service has explicitly acknowledged durable storage of that update.

### Loading strategy

Render small, revision-tagged HTML previews without loading the editing runtime for every task in a list. Preload the runtime when the route clearly needs editing; intent prefetch is a supplement, not a focus-time dependency waterfall. Reuse compilation/runtime setup across editor mounts where safe.

Restore a current local CRDT checkpoint plus a bounded tail of updates. Reuse a matching static DOM projection when practical. Match preview content and schema versions before enabling edits; do not briefly enable a preview and subsequently overwrite the user's input during hydration.

A preview that disagrees with recovered state is replaced by recovered state before activation. Existing documents must not be initialized again from Markdown/JSON just because a network response has not arrived; concurrent re-import can duplicate content.

For larger documents, avoid expensive offscreen layout and eagerly mounting rich custom views. Start with semantic DOM and carefully tested layout containment/deferred decoration. Introduce true viewport virtualization only after tests cover cross-boundary selection, find, copy-all, navigation, screen readers, and composition. Ordinary browser find cannot search content that has been removed from the DOM; replacement search behavior must be explicit.

**Important limit:** a single Yrs document is not made lazily editable merely by rendering the first screen. Full state restoration may still require reading/applying substantial CRDT state. Measure this separately. Checkpoints do not turn the process into constant-time loading. Sharded/subdocument architectures are not silently added to this MVP; failure to meet the declared size envelope triggers a visible architecture decision.

Count total JS + WASM + CSS transfer, decompression, compilation, instantiation, data decoding, DOM adoption, and time to first accepted edit. A tiny JS wrapper hiding a large WASM download is not a small editor.

## 6. Markdown as a native editing capability

### 6.1 Specify the dialect

Implement CommonMark 0.31.2 semantics, with a named GFM profile adding task lists, strikethrough, autolinks, and basic tables. These are defined standards/features, not a loose collection of regular expressions. Raw HTML is parsed according to the input grammar but admitted to the document only through an explicit safe import policy. [S14, S15]

The `markdown` module is included in the recommended task-editor preset. The GFM preset declares its table/image dependencies. A minimal host may omit them, but then import must preserve the source in a clear fallback and report the unsupported construct—not silently drop rows, images, or text.

Use `pulldown-cmark` as the initial Rust parser candidate, consuming parse events directly into a prepared semantic batch. It is designed as a pull parser and supports CommonMark and optional extensions. Benchmark the entire paste pipeline, not just its parser. [S16]

### 6.2 Clipboard behavior

Use deterministic precedence: valid editac fragment → explicit Markdown flavor or “paste as Markdown” action → sanitized rich HTML → plain text processed under the host's declared Markdown-paste policy. Malformed internal fragments fall back safely. Pasting into code remains literal.

The task-editor preset formats Markdown received as plain text by default. Provide a visible “paste plain text” command/shortcut for literal content. Do not use AI or undocumented probability heuristics to decide whether the user intended formatting.

For ordinary pastes, parse once and commit once so the first resulting document frame is formatted. Do not insert raw Markdown and run a second whole-document formatting pass afterward. One undo removes the entire paste; redo restores it.

For oversized pastes, preserve the captured text, prepare the insertion asynchronously when beneficial, and keep its target as a relative anchor. On completion, revalidate the target; a deleted target must not redirect content silently. Show a cancellable pending operation when the budget cannot be met. Do not promise arbitrary multi-megabyte pastes finish in one frame.

Nested fences, code spans, escaped delimiters, lists, and reference-style links must be parsed as a document. Splitting a paste into independent paragraphs can change meaning; GFM's parsing description explicitly identifies block and link-reference dependencies. [S15]

### 6.3 Round trips

Share import/export semantics across Rust, WASM, iOS, and Android. Preserve semantic meaning, including code whitespace, marks, links, and nesting. Do not claim byte-for-byte recovery of the author's original Markdown spelling after rich-text edits.

Typing shortcuts inspect the current syntactic context, not the entire document. Remote CRDT updates carry already-structured content and must not be reparsed independently as Markdown on every client.

## 7. Collaboration and durability from the foundation

### 7.1 Interoperability contract

Pin and test four separate layers: Yjs/Yrs update encoding; synchronization messages; awareness; editac's document schema. Yjs documents incremental update exchange, and Yrs supplies protocol machinery. A Rust document handle is nevertheless not a JavaScript `Y.Doc`, so existing JS providers need an explicit adapter or direct wire implementation. [S17, S18]

Use the chosen common update encoding as the baseline and test optional alternatives separately. Include browser–browser, browser–Rust, browser–iOS, browser–Android, and iOS–Android matrices. A small JS Yjs fixture must read/write the **same editac schema** for interoperability testing.

This does not establish direct live-edit compatibility with a Tiptap/ProseMirror Yjs document. Such migration requires an explicit converter and session transition.

Transport attachment must be optional and must not change document semantics. Presence/cursors are ephemeral and throttled separately; document updates are persisted. Use transaction origins to prevent echoes. Give independently editing replicas distinct client identities, including separate tabs.

### 7.2 Local persistence

Browser storage uses IndexedDB; native storage uses a transactional database adapter. Journal immutable binary updates promptly, with per-writer sequence/identity, schema version, and document/session identity. Store checkpoint publication and coverage metadata transactionally. Retain unsynced edits until an explicit durable remote acknowledgment permits pruning under the recovery policy.

Local commit acknowledgment occurs after the storage transaction completes, not when an update is queued or a timer fires. Use strict durability where supported and appropriate, while reporting the adapter's actual guarantee. The IndexedDB standard defines this as a hint, so browser storage cannot honestly promise survival of all power failures, quota changes, eviction, or user deletion. [S19]

Do not rely on unload handlers. Surface quota/permission errors, preserve in-memory edits where possible, provide a recovery export, and stop claiming the document is saved. Cache eviction is not equivalent to document deletion.

### 7.3 Remote commit is not ordinary synchronization

A provider's “synced” event or state-vector exchange is not automatically a disk-commit receipt. For a `remoteCommitted` status, the reference service must acknowledge an identified update only after its storage commit. Use an explicit negotiated service message or separate receipt channel without pretending it is part of baseline Yjs interoperability.

Offline writes remain local until authentication/authorization allows upload. Revocation must preserve rejected local work for recovery rather than silently discarding it. Authentication and document-level authorization are host/service responsibilities, enforced on the server, not by client schema validation.

### 7.4 Recovery, compaction, and history

Publish a checkpoint only after it is durably stored. Retain the previous valid checkpoint and covered journal entries until replacement publication is safe. Test crashes between every write/commit boundary.

Checkpoint **CRDT state**, retaining identity needed for reconnect. A JSON snapshot is a content export, not a substitute for collaborative history. Re-importing it starts a new explicit session/epoch; stale offline updates must not be silently merged into a rewritten identity space.

Keep current undo history bounded and origin-aware using the CRDT history machinery. Cross-restart preservation of the entire undo stack is not an MVP promise; document-content recovery is. Yjs documents selective undo with tracked origins and explicit grouping. [S20]

## 8. Simple extension API without a browser-only core

### Extension contract

A module declares a namespaced type/version, attribute schema, allowed content shape, commands, serialization, optional Markdown syntax, and a deterministic fallback. Platform adapters supply renderers and native interaction presenters.

Common custom marks and atoms should be definable through data descriptors and composition of existing primitives, without rebuilding Rust. Novel editing semantics may require a shared Rust module; a JavaScript callback does not automatically execute on iOS/Android.

Unknown content must remain intact when its renderer is absent. Show a non-destructive fallback. Never execute code embedded in a document, fetch a plugin because content names it, or let a missing module erase data.

Subscribe by node kind, command, changed range, or active selection. Optional modules must not register unbounded whole-document work on every transaction. Async resolvers use cancellation and stale-result guards. Stable render views are patched, not recreated on each selection change.

### Proposed integration API

The following is an **API design sketch**, not a package that exists today:

```ts
import { createEditor } from '@editac/web';
import { taskPreset } from '@editac/presets';
import { indexedDb } from '@editac/persistence-web';

const editor = await createEditor({
  element: document.querySelector('#description'),
  documentId: 'task:123:description',
  load: () => repository.loadCheckpointAndUpdates(),
  preset: taskPreset({ markdown: 'gfm' }),
  persistence: indexedDb({ namespace: 'task-editor' }),
});

editor.chain().focus().toggleMark('bold').run();
editor.insertMarkdown('## Acceptance criteria\n- [ ] Works offline');

// Origin and dirty ranges are metadata, not a reserialized document.
const unsubscribe = editor.subscribe(
  { event: 'localCommitted' },
  commit => host.showSavedRevision(commit.id),
);

// Attaching network transport does not replace or recreate the document.
editor.attachSync(host.createSyncTransport());

// The host awaits this before navigation when it needs a local-commit barrier.
await editor.flush({ target: 'local' });
unsubscribe();
await editor.destroy();
```

Initialization errors must leave an accessible read-only/recovery view rather than an apparently editable control. Host wrappers must clean up subscriptions, observers, timers, native references, and document handles.

### Optional modules delivered in the MVP

| Module | Behavior | Required constraints |
|---|---|---|
| Slash | `/` opens local commands with keyboard/touch navigation | No scan of the whole document; no popup triggered by remote edits |
| References | `@`, `[[`, or configured trigger; host resolves people/tasks/documents | Persist target identity + label fallback; no automatic network fetch on open; cancel stale searches |
| Reorder | Handle, keyboard move, native touch controls | One semantic move; stable content identity; concurrent editing survives |
| Math | Inline/block LaTeX source with optional rendering | No full TeX engine; bounded safe rendering; preserve invalid source; native renderer or explicit source fallback |
| Tables/images | Basic GFM content and native attachments | No merged cells, spreadsheet formulas, upload product, or layout engine |

Example portable math node descriptor:

```ts
const mathInline = defineNode({
  name: 'editac.math.inline',
  version: 1,
  shape: 'inline-atom',
  attributes: { latex: { type: 'string', required: true } },
  fallback: { kind: 'text', attribute: 'latex' },
});
```

Register its Markdown codec and browser/native renderer separately. The official Tiptap math extension uses KaTeX, which is a useful web-rendering reference, not a native-text solution. Defer renderer code/fonts until needed; do not falsely claim a source fallback is typeset native math. [S05]

A native example must demonstrate at least one genuine custom mark and one native inline attachment. This validates extensibility even before a complete native math renderer is selected. Publish a platform-support matrix for every optional module: native table editing, for example, must be implemented and tested or explicitly shown as a preserved fallback, never implied by web support alone.

## 9. Native adapters: no WebView, no second editor model

**iOS:** start with `UITextView` and TextKit, applying attributed-text range patches and explicit attachment rendering. Bridge selection, marked text, autocorrection, dictation, undo, clipboard, and accessibility into the shared engine. Apple documents these as native text editing/layout facilities. [S21]

**Android:** start with `EditText`/`Editable`/spans and its native input connection, adding specialized handling only where necessary. Respect composing ranges, batch edits, selection updates, clipboard, and accessibility. The Android input-connection contract describes these obligations. [S22]

Do not replace the entire attributed string or `Editable` after each remote edit. Native controls own their temporary composition state; Rust owns committed semantics. Render custom objects through native attachments/views, not HTML.

Parity means shared content, operations, undo policy, Markdown, and collaboration—not identical pixels. Optional native menus use platform UI but invoke the same commands. A future React Native binding wraps these native views; it does not replace them with a WebView.

## 10. Performance budgets and benchmark rules

These are **proposed engineering targets**, not claims about an existing implementation. Gate 0 measures feasibility and records any change to a target with the reason. Do not remove features, weaken durability, or omit WASM bytes to manufacture a win.

### Test corpus

| Fixture | Contents |
|---|---|
| Task | 20 blocks, approximately 10 KiB of source text |
| Long | 2,000 mixed blocks, approximately 1 MiB of source text |
| Large | 10,000 blocks, approximately 5 MiB of source text |
| Aged | Long fixture after 100,000 editing operations; record actual CRDT state size |
| Adversarial | 250 KiB single paragraph, fragmented marks, nested lists, wide tables, emoji/RTL/combining text |
| Multi-editor | 50 static previews; separately test 1 and 10 active editors |

Use fixed reproducible content, not only repeated identical strings that compress unrealistically well. Source text size and serialized CRDT state size are separate measurements.

### Initial targets

| Metric | Desktop target | Mid-range phone target |
|---|---:|---:|
| Runtime/adapter JS alone, Brotli | ≤35 KiB | Same artifact |
| Task preset total JS + WASM + essential CSS, Brotli, including Yrs and Markdown | ≤400 KiB | Same artifact |
| Core ordinary edit, p95 | ≤1 ms | ≤2 ms |
| Input-to-visible-update, controlled 60 Hz, p95 | ≤16.7 ms | ≤33 ms |
| Warm task activation, p95 | ≤50 ms | ≤100 ms |
| Warm long-document actual editability, p95 | ≤200 ms | ≤400 ms |
| Warm large-document actual editability, p95 | ≤750 ms | ≤1,500 ms |
| Matching cached/SSR first viewport display | ≤50 ms | ≤100 ms |
| 10 KiB Markdown paste to first formatted frame, p95 | ≤50 ms | ≤100 ms |
| 100 KiB Markdown paste to first formatted frame, p95 | ≤150 ms | ≤300 ms |
| Local slash menu after runtime ready, p95 | ≤one frame | ≤two frames |

The transfer target includes all required editing dependencies; optional tables, math fonts, and menu UI are itemized separately. A minimal preset and a feature-equivalent comparison preset are both reported. The large-document timings are deliberately distinct from the instant visual-preview target.

Warm means editor assets are cached and the document is available locally; timings include local load, restore, and adapter activation. Cold tests also include uncached transfer, compile/instantiate, and document download on a fixed network profile. No “instant” claim excludes a required hidden download. Record application route latency separately from editor overhead.

### Comparison and regression policy

Compare native `contenteditable`, optimized Tiptap, optimized Lexical, and editac using equal capabilities, content, collaboration, persistence policy, styling, and device conditions. Record exact dependencies/commit IDs and include small-document tests where WASM overhead may erase its benefits.

Record p50/p95/p99, cold/warm load, bytes, JS and WASM memory, DOM count, long tasks, paste peak memory, journal/write amplification, restore time, and remote-update bursts. Do not use synthetic keyboard events alone to claim real IME or input latency correctness.

No retained-memory growth trend after repeated mount/edit/destroy runs; account for WASM allocator high-water marks separately from leaks. Target a stable plateau rather than requiring every runtime to return its memory pages immediately.

A material regression against the better feature-equivalent baseline requires an explicit explanation and a release decision. “Best performance ever” is an ambition; publish only comparisons actually measured. Core correctness and supported input behavior are non-negotiable gates.

## 11. Gated implementation roadmap

### Gate 0 — Measurement harness and architecture spikes

Build optimized Tiptap/Lexical/plain-contenteditable fixtures, a release-build Rust/WASM size probe with Yrs + Markdown, and minimal iOS/Android native hosts. Pin protocol/library versions and document the target browser/OS matrix.

Test a keystroke, composition, a remote insertion, and a native range patch before designing the final extension API. Measure boundary copying and WASM startup. Compare structural representations using a minimal concurrent-move test.

**Exit:** reproducible baseline reports, compatibility profile, input-risk register, and a demonstrated shared-core call from browser/iOS/Android. Failed size/startup targets produce an architecture decision, not an unsupported promise.

### Gate 1 — Durable collaborative kernel

Implement schema descriptors, identity, attributed text, commands, anchors, validation-before-mutation, transaction origins, selective history, checkpoints, local journals, and sync fixtures. Specify concurrent structural behavior.

Use property tests for random replica operations and fault injection around storage publication. Test new-document initialization versus restoration explicitly.

**Exit:** Rust and JS Yjs replicas converge semantically after reordering, duplication, disconnection, and replay; locally committed content recovers after process termination; invalid local commands have no partial effect. No full editor UI is required to verify this gate.

### Gate 2 — Thin browser editor and loading path

Implement the coherent contenteditable surface, incremental patches, selections, composition handling, native-input reconciliation, clipboard foundation, keyboard navigation, and editor-owned undo. Add revision-tagged static rendering and local activation.

Measure long-document restoration and offscreen rendering immediately. Exercise native adapters in parallel with the same transaction corpus.

**Exit:** usable text/formatting editor; composition and cross-block operations work; editing does not wait for network sync; no full-document serialization on ordinary typing; startup is measured as both visibility and editability.

### Gate 3 — Markdown and everyday richness

Add nested lists, checklists, blockquotes, code, links, basic table/image modules, Markdown import/export, formatted paste, shortcuts, and safe HTML clipboard import. Implement ordinary one-transaction paste and the oversized-paste path.

**Exit:** declared CommonMark/GFM fixtures pass; 10/100 KiB paste budgets are measured; paste/undo/redo works during collaboration; unsupported content is preserved with diagnostics.

### Gate 4 — Native SDK parity

Complete iOS/Android native editing adapters and sample hosts. Add native menus/attachments, formatted paste, hardware/software keyboard behavior, accessibility, lifecycle recovery, and background/foreground reconnect handling.

**Exit:** browser, iOS, and Android edit the same document concurrently and offline without a WebView; parity suite covers text, formatting, lists, links, undo, paste, composition, and a custom node. Native support is a release gate, not a future footnote.

### Gate 5 — Optional modules and stable public API

Finalize nodes/marks/commands, portable schemas, scoped events, serializers, read-only fallbacks, and lazy renderers. Ship slash/reference/reorder modules and the math example. Add the thin React wrapper and native API samples.

**Exit:** a custom mark and inline atom are implemented without modifying core code; unsupported renderers preserve content; disabled modules do not ship their renderer/UI code; reorder survives concurrent text edits.

### Gate 6 — Migration, hardening, and MVP release

Add scoped Tiptap JSON import for the supported node/mark set, semantic HTML/Markdown export, unknown-node reporting, security/resource limits, leak tests, and documentation. Migrate existing collaborative data through an explicit new session rather than silently switching schemas underneath old clients.

Run cold/warm browser tests, real-device input checks, native crash/restart tests, long-running collaboration workloads, and persistence-failure tests. Enforce element/attribute/URL allowlists for imported HTML; prohibit scripts, event handlers, and executable URLs. Bound imported bytes, nesting, attribute sizes, and remote-update queues. Publish the complete benchmark matrix and known limitations.

**Exit:** an existing task-description integration can switch to editac with documented changes, retain its supported content, use optional modules, and meet the defined correctness and performance envelope.

## 12. First runnable milestone

The first demo is deliberately small: one task description with a paragraph, heading, bold text, and a list, opened in two browsers and a minimal native host.

Paste Markdown; edit concurrently; disconnect; type using an IME; terminate a client after a local-commit acknowledgment; restore; reconnect; verify content and selection behavior. Include a larger fixture in the same harness so the architecture cannot hide behind a tiny happy-path document.

Do not begin with the slash-menu visuals or a custom `.acdoc` container. Begin with **input → semantic transaction → durable update → convergent replica → incremental patch**.

## 13. Release blockers and architectural prohibitions

A release is blocked by lost locally committed content in the supported process-crash model, silent import loss, divergent semantic states, duplicate initialization, broken composition in the declared matrix, corrupt undo, unsafe clipboard content, unexplained stale-edit overwrites, or native “support” implemented through a WebView.

Do not introduce a second authoritative state owner, serialize Markdown on every edit, rerender the document through React, run every module on every keystroke, treat a sync event as durable storage, implement a second CRDT, create a custom typography engine, or advertise lossless migration for unsupported formats.

The binary choice remains modest: use Yjs/Yrs updates and checkpoints for live durability/collaboration, versioned JSON for semantic interchange, and Markdown for authoring/interchange. A future `.acdoc` package can wrap these capabilities after the editor earns its performance and reliability claims.

---

## Primary sources reviewed

Sources were checked on 11 October 2026. They establish reference APIs and platform constraints; the architecture, roadmap, and numerical budgets above are proposals, not results reported by these sources.

- **[S01]** Tiptap Extension API: https://tiptap.dev/docs/editor/extensions/custom-extensions/create-new/extension
- **[S02]** Tiptap Markdown introduction and extension integration: https://tiptap.dev/docs/editor/markdown and https://tiptap.dev/docs/editor/markdown/guides/integrate-markdown-in-your-extension
- **[S03]** Tiptap Suggestion utility: https://tiptap.dev/docs/editor/api/utilities/suggestion
- **[S04]** Tiptap Drag Handle: https://tiptap.dev/docs/editor/extensions/functionality/drag-handle
- **[S05]** Tiptap Mathematics: https://tiptap.dev/docs/editor/extensions/nodes/mathematics
- **[S06]** Tiptap integration performance: https://tiptap.dev/docs/guides/performance
- **[S07]** Lexical updates and reconciliation: https://lexical.dev/docs/concepts/updates
- **[S08]** Yrs crate documentation, including compatibility and transaction lifecycle: https://docs.rs/yrs/latest/yrs/
- **[S09]** Yrs text offset configuration: https://docs.rs/yrs/latest/yrs/types/text/trait.Text.html
- **[S10]** Yjs relative positions: https://docs.yjs.dev/api/relative-positions
- **[S11]** Mozilla UniFFI guide: https://mozilla.github.io/uniffi-rs/latest/
- **[S12]** MDN `beforeinput` behavior: https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event
- **[S13]** Tiptap Collaboration and history: https://tiptap.dev/docs/editor/extensions/functionality/collaboration
- **[S14]** CommonMark specification: https://spec.commonmark.org/
- **[S15]** GitHub Flavored Markdown specification: https://github.github.com/gfm/
- **[S16]** pulldown-cmark guide: https://pulldown-cmark.github.io/pulldown-cmark/
- **[S17]** Yjs update API: https://docs.yjs.dev/api/document-updates
- **[S18]** Yrs synchronization protocol: https://docs.rs/yrs/latest/yrs/sync/protocol/trait.Protocol.html
- **[S19]** IndexedDB specification and durability semantics: https://w3c.github.io/IndexedDB/
- **[S20]** Yjs UndoManager: https://docs.yjs.dev/api/undo-manager
- **[S21]** Apple UIKit TextKit: https://developer.apple.com/documentation/uikit/textkit
- **[S22]** Android InputConnection: https://developer.android.com/reference/android/view/inputmethod/InputConnection

# Extension integration, authoring and optional web delivery

Device sequencing (superseding user decision, 2026-10-18): every device/target-runtime/OS-input/AT observation in this document is owned by [final roadmap43](../roadmaps/43-physical-device-verification.md) under the [web feature-first policy](../operations/web-feature-first-20261018.md). Feature implementation keeps focused deterministic correctness/data-safety checks; device rows and D observations run later on accepted simulators/emulators/VMs/OS hosts without waiting for physical hardware. Preserve original case IDs and criteria; deferred observations remain unchecked and do not block web feature completeness. Exhaustive qualification/performance follows the stated later phase.

Status: planned follow-up contract, authorized 2026-10-17. Implementation belongs to the existing [SDK](../roadmaps/08-sdk-integration.md), [extension library](../roadmaps/21-extension-library.md), [architecture fitness](../roadmaps/30-architecture-fitness.md) and [public documentation](../roadmaps/29-public-docs-demo.md) roadmaps. Proposed APIs below describe the target experience; they are not shipped exports or executable support claims.

## Delivery ownership in existing roadmaps

| Existing roadmap | Added parents | Scope |
|---|---|---|
| 08 SDK integration | SDK-1.11–SDK-1.13 | One-import configuration, managed independent bundles/assets, measured SDK/WASM reductions |
| 21 Extension library | EXT-1.14–EXT-1.20 | Typed configuration contract, authoring API, managed matching, task-link/spellcheck/parsing recipes and canonical documentation |
| 30 Architecture fitness | FIT-1.10–FIT-1.11 | Size/compression inventories and clean installed composition consumers |
| 29 Public documentation | Existing DOC-1.34/1.35 amended | Catalog and authoring tutorials from canonical qualified SDK sources |

These are new follow-up acceptance requirements in existing roadmaps. Historical receipts for their original parent sets remain valid only for those original requirements and artifact identities; they do not complete the new parents. Existing consumers of a previously qualified baseline keep their original prerequisite scope. New facade claims require the specific new parent receipts below; no whole-track gate may create a cycle by waiting on its own downstream follow-up. No acceptance is waived and no active runner queue is changed by this planning amendment.

## Composition is the public model

Applications choose extensions individually through one editor configuration. A task, comment or document can require any supported combination; application labels never determine extension eligibility, schema, permissions or mandatory downloads. Optional default and document presets are convenience configurations that expand to inspectable extension lists with explicit overrides. They are not separate engines or closed feature tiers.

Existing Task/core/document-tools/code-tools names and their pinned qualification evidence remain historical and compatibility contracts. The existing SDK and extension-library follow-ups introduce generic public naming and a migration path without silently changing existing behavior, reclassifying required bytes as optional or invalidating stored documents. The default Task budget continues to apply to its existing capability inventory until a separately approved baseline change. Applications may configure extensions without selecting a preset.

Keep one Rust/Yrs semantic owner. Mandatory engine primitives include correct UTF-16 and grapheme boundaries, schema/data admission, stable anchors, atomic commands, history, updates and unknown-extension preservation. Browser input, composition, selection and accessible editing remain baseline adapter responsibilities. Optional conversion, highlighting, math, spelling dictionaries, resolver behavior and their UI/assets remain outside minimum loading. New editing semantics still require shared engine implementation; a JavaScript extension cannot bypass admission or own another writable model.

## Core and extension boundaries

Keep the default editor small. Basic text editing and inexpensive built-in formatting can be configured directly in core; hosts can enable or disable offered formatting commands, shortcuts and controls without constructing a behavior extension for each keystroke. Freeze the exact typed options in EXT-1.14. Hiding a command is not a schema migration, authorization decision or permission to discard existing marks. Preserve admitted formatting and unknown payloads when a control or presenter is disabled.

Heavy implementations belong behind explicit extension capabilities: collaboration transport and presence, Markdown parsing, rich table/media tools, math, syntax highlighting, conversion, spelling, asynchronous resolution and optional assistance. Engine validation and atomic semantic primitives remain shared Rust responsibilities, including primitives used by these extensions. A cheap baseline table representation need not load advanced table UI. Extension manifests declare semantic/schema needs, dependencies, input interests, readiness and cleanup; importing a factory cannot activate its implementation. Existing default Task capabilities and byte accounting stay intact during migration.

### Optional collaboration per editor

Collaboration is an explicit per-editor configuration over the existing sync/session ports. A site can mount a plain comment field, a formatted local editor and a collaborative document together; any of them may independently opt in. A comment input is not the Comments annotation extension, and neither its name nor a sibling document enables networking. Absence of collaboration must leave ordinary editing, local persistence, local undo/redo and recovery usable without a provider, connection, authorization lookup or remote-ready wait.

Separate collaboration transport, awareness/presence and peer-caret presentation. Presence is optional even when document synchronization is enabled. Disabled collaboration installs no collaboration subscriptions, retry timers, provider instances, sockets or awareness work. Its dedicated implementation/provider assets stay outside that consumer's requested/evaluated graph; shared engine/Yrs update primitives and local durability bytes remain baseline costs. Verify retained code as well as network absence: today's `packages/web/src/editor.ts` statically imports `SyncSession`, so explicit attachment alone does not prove a slim disabled bundle. SDK-1.12 must measure and isolate orchestration where retained while preserving the legacy attach API.

Use the existing document handle, history owner, immutable update bytes, authorization and bounded send/receive queues. Never add a JS Y.Doc mirror or a second undo manager to imitate Tiptap. Attach/detach must preserve content, selection, history and recoverable unsent edits. Admission checks identity/schema/epoch and current authority; detachment, reconfiguration and disposal invalidate pending attachment work and late provider callbacks. Loading a shared immutable chunk or WASM module grants no sibling editor a provider, document identity, selection or authority. Shared transport services still route each message by its authorized document/session. Hosts must explicitly opt into any remote-sync readiness gate; routine local input never awaits it.

## Interfaces on speed-critical paths

Adapt the existing indexed ModuleRuntime and engine subscription ports. Resolve options, dependencies, command/keymap precedence and schema descriptors once at configuration/attachment, not on every input event. Dispatch only to enabled subscriptions interested in the operation/source/range or requested selection change. A disabled or unrelated extension must not add callbacks, full-document serialization, whole-registry scans or document-size work to a keystroke. Use changed ranges and bounded matching context; a broad observer must declare its cost and cannot become the default authoring helper.

Keep local input, selection, composition and atomic history synchronous through their current owners. Background parsing, lookup, highlighting, export, network and presence must not be awaited on that path. Coalesce derived decoration/view work using revision-aware invalidation without delaying semantic commits or reading stale targets. React and other wrappers subscribe to selected state rather than re-rendering every extension/toolbar for each transaction. Disposal unregisters indexed interests and cancels owned work; cached immutable code must not retain per-editor listeners or writable state.

Measure facade and dispatcher costs against the same direct-port consumer and features. Required [performance evidence](verification.md#extension-dispatch-and-jswasm-performance) includes both work counters and end-to-end latency; a microbenchmark alone cannot prove user-visible speed. Do not add a parallel registry, dispatcher or benchmark framework.

## One import and configuration

The public web facade exports lightweight extension factories alongside editor creation. A normal integration configures a feature once; it does not manually assemble a codec, registry, worker, renderer, subscriptions and cleanup. Existing low-level exports remain available for advanced hosts and compatibility.

Target notation, subject to the typed contract frozen by EXT-1.14:

```ts
import { createEditor, Markdown, PdfExport, PatternLink } from '@edit-ac/web';

const editor = createEditor(root, {
  ...hostOptions,
  extensions: [
    Markdown.configure(),
    PdfExport.configure(),
    PatternLink.configure({
      name: 'acme.task-links',
      pattern: /\bASD-\d+\b/gu,
      resolve: async ({ text, signal }) => {
        const task = await tasks.findByCode(text, { signal });
        return task ? { href: task.url } : null;
      },
    }),
  ],
});
await editor.ready;
```

The application owns tasks.findByCode and its authorization. The example adds a standard safe link to the unchanged code text only after a successful lookup; persistent custom-reference identity is an explicitly different representation. Export and Markdown factories advertise only converter directions already qualified by their owners. No PDF import is introduced.

Configuration is typed and immutable. configure() returns a fresh value; it cannot modify another editor's defaults, services, dictionaries or keymaps. Validate names, versions, options, dependencies, capabilities, duplicate/conflicting bindings and schema before attachment. Errors identify the extension and option and explain the remedy. Import order is not an undocumented conflict-resolution mechanism. Do not create a second registry, command bus or lifecycle manager: adapt the existing portable registry, profile admission and session/presenter ports.

## Loading and lifecycle behind the facade

Factory entry points contain descriptors and small configuration code. Heavy parsers, layout engines, dictionaries, grammars, renderers, fonts and workers are reachable only through dedicated asynchronous entries. Static named imports from the facade must not eagerly import those implementations; a dynamic import of a broad all-extensions barrel is not a substitute for independent feature chunks. A converter's distinct directional entry can share genuinely common codec assets without loading unrelated formats. Default-only production graphs and runtime traces prove absence of disabled implementation bytes and requests.

The SDK owns conventional bundler asset discovery and compatible loader wiring. Direct-browser, CDN and custom worker hosts get one documented asset-manifest/base-URL override, plus precise CSP/CORS/MIME errors. Do not expose per-extension hand-written initialization as the normal getting-started path. Select a supported package layout through packed production consumers, not a package-name-only assumption. Lightweight facade exports and focused advanced subpaths may coexist; large independently consumed converter packages remain justified where measured.

Installing distributed optional files and downloading/executing them are different costs. If a converter is separately installed, define its dependency and loader resolution explicitly: a disabled consumer must not fail bundling because an optional peer import is missing. Do not promise that a static facade can discover an arbitrary uninstalled package. Prove the chosen lightweight-factory/dedicated-chunk packaging in a clean consumer, including omitted optional installations where supported.

Document which extensions must be ready before accepting their input and which load on a command or first presentation. editor.ready waits for required input adapters; command-lazy exporters need not block typing. Readiness, unavailable, loading, failure, retry and cancellation are observable through a common typed interface. A parser never fetches synchronously during input; until ready, its declared policy retains literal input or rejects its explicit operation with source retained. Missing optional code cannot turn ordinary typing into data loss.

The existing immutable session registry is validated/frozen before attachment. Lightweight descriptors can precede heavy implementation loading. Behavior-only enable/disable uses declared lifecycle capabilities; schema/descriptor changes require a documented session reconfiguration or safe view remount. Do not claim arbitrary hot schema registration. Abort pending work and release views, listeners, workers, temporary buffers and references on disable/dispose, including late completion. Module code can remain cached after disposal; per-editor resources cannot.

Share compatible immutable JS/WASM/assets across instances and routes under the existing [shared-resource contract](web.md#shared-resources-across-editors-and-site-routes). Keep configuration, authority, document data, selection, history, requests and cancellation instance-scoped. Loading a feature for one editor does not enable it in another. Bundler splitting, single-flight initialization and HTTP-cache reuse are separate measured properties.

## An approachable extension authoring API

Expose a small typed Extension.create() authoring entry and typed configure() options. The exact interfaces are frozen and versioned before implementation. A basic behavior extension and a mark/atom using admitted primitives must work from public imports with unchanged engine WASM. Authors supply their behavior and data definition; the SDK supplies registration, bounded changed-range subscriptions, local input/paste hooks, command preparation, stable target capture, managed async resolution, ephemeral decorations and cleanup helpers.

Provide clear recipes for commands, configurable options, keyboard/input/paste precedence, parsing/codecs, safe links, custom-reference fallback, spelling suggestions, accessibility and lifecycle events. Distinguish decoration-only state from committed data and portable descriptors from platform callbacks. Deriving a configured extension preserves its original identity/version unless an explicit new data type is declared. A convenience extension must not expose raw CRDT mutation or DOM-as-document-state hooks.

Use the existing prepared command/commit and history/result-selection contracts. If a requested behavior needs an unavailable primitive, record the exact upstream gap and implement it through its owner rather than simulate atomicity with sequential edits. Publish capability and platform limits and test fixtures for custom extensions; browser callbacks do not imply native execution. Tiptap's documented [creation/options/command/lifecycle surface](https://tiptap.dev/docs/editor/extensions/custom-extensions/create-new/extension) and [configuration/extension examples](https://tiptap.dev/docs/editor/extensions/custom-extensions/extend-existing) are DX references, not runtime, schema or ProseMirror compatibility requirements.

## Pattern recognition and asynchronous resolution

The reusable facility separates bounded matching, host resolution and prepared application. It supports local typing and explicitly configured paste behavior, with declared delimiters and code/link/literal-context exclusions. It operates on changed ranges plus bounded context rather than rescanning a document per transaction. Pattern and resolver callbacks are trusted host code with documented execution limits; same-thread infinite loops are not preempted by AbortSignal. Heavy or untrusted parsing uses an isolated worker.

For ASD-123, preserve literal text while a lookup is pending. Query only the configured host after an eligible local match. The resolver returns a validated safe href or not-found; no speculative URL template, placeholder link or mutation occurs before success. Not-found, unavailable permission, failure, invalid URL and cancellation leave authored text and document history unchanged. Status is optional transient presentation and cannot persist private response details.

Capture stable anchors, document/session identity, matched source and request generation. Before applying a response, revalidate that the same eligible text remains, authority still permits editing and no conflicting manual link has appeared. A newer unrelated edit may preserve the anchored match; an edited/deleted match, undo-invalidated intent, read-only transition, disposal or replacement request prevents stale application. Deduplicate pending work and bound concurrency/time/output/cache scope. Undo of generated linking does not immediately trigger the same link again without a new eligible local action. Reopen, remote updates, export and document inspection do not trigger lookups by default.

Apply a successful result through one prepared link-mark command, retaining text, unrelated formatting, selection and the declared history policy. Test collaborator convergence and undo/redo with independently authored expectations. Host resolvers own credentials and principal-scoped access; an internal denial cannot fall back to public metadata fetching. Automatic link text, custom reference identity and URL insertion are separate explicit policies over the existing [link contract](link-resolution.md).

## Spell checking, custom parsing and URL insertion

Prefer platform spellcheck reuse under the [platform editing contract](platform-editing-services.md): default `platform` respects browser/OS/user preferences, `off` suppresses checking where supported, and explicit `custom` accepts a host checker. Platform mode must not force checking on or infer effective user settings from an HTML property. Unsupported or unknown state stays explicit; absence never triggers an automatic custom fallback. Do not implement a second dictionary or suggestion UI when the selected platform already supplies them. Autocorrection is independently configured; spelling modes must not silently toggle it or unrelated IME/prediction services. Document inseparable platform controls and preserve user choices.

The custom checker is an optional behavior/presenter extension, with no built-in service account. Only enabled custom mode loads its dictionaries/analysis workers; platform/off incur no such SDK assets. Avoid duplicate platform/custom spelling presentation through an independently supported control or explicit limitation/overlap resolution. Underlines and suggestions are ephemeral decorations, not CRDT marks. Changed-range work excludes composition. An accepted platform or custom correction uses one prepared replacement with current-text/anchor validation, preserved formatting/selection and shared undo. Unknown words, stale results and failed analysis never modify text.

The portable adapter exposes `Spelling.configure` through the public web import, returning the matching `platform` policy and immutable `extensions` selection. Custom mode requires an explicit checker, accessible transient presenter and `overlap: 'allow'` because browser hints cannot guarantee exclusive suppression. The optional checker execution module loads only for eligible custom input; platform/off preserve an empty checker graph. Unknown/unavailable locales or checker failures retain editing without fallback. The standalone prepared recipe and INT-1.14 observation runbook live in `core/examples/extensions/spellcheck/`.

Managed matching defaults to the link result family. An explicit `application: 'replacement'` admits only bounded plain replacement results through `ExtensionContextV1.replacement`, the existing formatting-aware prepared command route; link consumers reject replacement results and replacement consumers reject link results. This extends no engine/schema/history semantics. The existing first-selected-character formatting policy and captured-target undo bookmarks apply, including mixed-format boundaries; adjacent text and original formatting are preserved by undo. Suggestions remain ephemeral while a managed request waits for explicit acceptance. Current text, stable anchors, authority, composition, foreign editable focus and disposal are rechecked before commit.

DXC-15/16 and [ENV-01–ENV-07](../tests/platform-editing-cases.md) cover preferences, locales/exclusions, mode transitions, instance isolation, assets, correction/history and teardown. Prepared dictionaries/mock checkers prove semantics, never provider quality or actual OS spelling support. Browser observations belong to INT-1.14; native adapters and DEL-1.7 qualify their own controls under the shared platform policy.

A custom parsing tutorial translates a small bounded source or paste syntax through an existing codec/prepared-fragment boundary. It declares precedence, literal bypass, unsupported-input diagnostics and recoverable source. A URL-insert tutorial validates a host-resolved URL and updates the captured range through existing commands. Neither tutorial mutates the DOM as an authoritative model, executes document content, fetches document-selected code or claims new schema semantics without qualification.

## Size reduction and compression

Reuse the [existing byte inventory and budgets](verification.md#browser-bundle-size-budgets); do not build another accounting harness. Report baseline, each extension, representative combinations and multi-editor/site unions. Record initial/deferred resources separately and combined, raw/gzip/Brotli bytes, hashes and exact compressor settings. Required lazy code still counts. Enabled optional costs are explicit; disabled features contribute no heavy implementation assets. Broader combinations are chosen by shared input/history/async risk, with uncovered combinations stated.

Measure contributions before choosing reductions: broad re-export/side-effect retention, generated glue, WASM dispatch/export reachability, parser/serializer dependencies, duplicated chunks, fonts/grammars and compilation/startup cost. Optimize actual retained work and use the existing size-oriented Rust/WASM build controls. Preserve Unicode correctness, schema/fallback compatibility, history, collaboration, persistence and the existing default clipboard guarantees. Do not create an engine binary per preset or remove promised features merely to pass a cap.

Qualify gzip/Brotli server/CDN delivery with Content-Encoding, Vary: Accept-Encoding, correct JS/WASM MIME, immutable compatible asset URLs and uncompressed fallback. Preserve compressed/decompressed size distinction and cold/warm transfer provenance. HTTP compression reduces transfer bytes; it does not reduce decompressed WASM memory or compilation automatically. Choose precompression and caching from measurements, with no remote infrastructure provisioning required for local proof. Record measured gains, startup/compile tradeoffs and remaining headroom; no speculative percentage reduction is promised. Existing caps are unchanged.

WASM is a workload-specific optimization, not an automatic speed guarantee. Attribute call count, encoding/decoding, copies, allocations, execution and rendering separately before moving work. Keep semantic ownership in Rust; compare equivalent pure JS/WASM kernels only where they do not introduce another writable document. Batch work at existing semantic transaction boundaries, avoid per-character boundary chatter and measure small interactive inputs as well as large batches. SDK-1.13 uses the performance contract to accept or reject each hypothesis; size wins cannot conceal input, startup or memory regressions.

## Review basis — 2026-10-17

Tiptap documents [extensions](https://tiptap.dev/docs/editor/core-concepts/extensions) for content and behavior and an optional [StarterKit](https://tiptap.dev/docs/editor/extensions/functionality/starterkit) with configurable/disabled members. These inform composition and basic defaults, without requiring Tiptap runtime or schema compatibility. Its [Collaboration extension](https://tiptap.dev/docs/editor/extensions/functionality/collaboration) configures a Yjs document/fragment and supplies history that conflicts with ordinary UndoRedo; edit.ac instead retains its existing Rust/Yrs document/history owner. Its [performance guide](https://tiptap.dev/docs/guides/performance) recommends isolated editor components and selected-state subscriptions. These are upstream design references, not measured edit.ac results.

The local review inspected `BrowserEditor.attachSync` and the static sync import in `packages/web/src/editor.ts`, the operation/source indexes in `packages/web/src/modules/runtime.ts`, and admission/freeze in `packages/core/src/extensions/registry.ts`. They provide existing integration points; runtime and bundle overhead remain to be measured. [V8's call/inlining discussion](https://v8.dev/blog/wasm-speculative-optimizations) explains why call overhead can dominate tiny functions; the [Rust/WASM size guide](https://rustwasm.github.io/docs/book/reference/code-size.html) supports attribution before tuning. Neither establishes a universal WASM advantage or an edit.ac speedup.

## Documentation and delivery evidence

Ship one-import getting started, first-party configuration, a public API reference and original runnable custom extension tutorials. Include ASD-123, spelling suggestions, a custom parser and URL insertion with deterministic fixture services, plus mark/atom examples using admitted data primitives. Show only public imports, typed options, behavior before/after, errors, cancellation, undo, preservation and disposal. Beginners do not copy internal codec/worker orchestration. Advanced asset hosting and migration from low-level APIs are separate guides.

Core owns canonical recipes and clean packed consumers; DOC-1.34/1.35 consume their immutable qualified source ranges in the public catalog/tutorials. Planned notation stays labeled until the matching artifact exists. [The case catalog](../tests/extension-dx-cases.md) defines required outcomes, not passing evidence. Create named tests before executing them and record nonzero counts, failures/skips, exact source/package/build identities and process teardown. All automated services are deterministic fixtures/mock transports; no paid inference, secret loading, publication or deployment is authorized by this amendment.

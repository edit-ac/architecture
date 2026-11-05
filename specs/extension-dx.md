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

Separate collaboration transport, awareness/presence and peer-caret presentation. Presence is optional even when document synchronization is enabled. Disabled collaboration installs no collaboration subscriptions, retry timers, provider instances, sockets or awareness work. Its dedicated implementation/provider assets stay outside that consumer's requested/evaluated graph; shared engine/Yrs update primitives and local durability bytes remain baseline costs. Verify retained code as well as network absence: the current packed Task consumer retains the editor/surface dynamic sync imports in one JS output, so deferred execution and explicit attachment alone do not prove a slim disabled bundle. SDK-1.12 must measure and isolate orchestration where retained while preserving the legacy attach API.

Use the existing document handle, history owner, immutable update bytes, authorization and bounded send/receive queues. Never add a JS Y.Doc mirror or a second undo manager to imitate Tiptap. Attach/detach must preserve content, selection, history and recoverable unsent edits. Admission checks identity/schema/epoch and current authority; detachment, reconfiguration and disposal invalidate pending attachment work and late provider callbacks. Loading a shared immutable chunk or WASM module grants no sibling editor a provider, document identity, selection or authority. Shared transport services still route each message by its authorized document/session. Hosts must explicitly opt into any remote-sync readiness gate; routine local input never awaits it.

## Frozen core and companion contract — 2026-10-28

WEX-1.2 freezes the following delivery contract over the existing v1 ports; it
is not a declaration that the remaining physical boundaries or qualification
have shipped. There is one current document identity, one canonical browser
kernel and one semantic owner. Presets select capabilities, not formats,
compiled runtimes or permission levels.

| Boundary | Required inventory and responsibility |
|---|---|
| Semantic kernel | Current identity/schema/limit admission; Unicode/UTF-16 and grapheme correctness; all admitted basic formatting and inert unknown data; stable anchors; prepared text/fragment/format/editor commands; atomic validation/commit, selection results, history and update primitives. Shared table identities, cell/rectangle validation and preservation stay authoritative here even when advanced table tools are disabled. |
| Baseline browser adapter | Accessible text input/composition, selection/navigation, DOM patches, undo/redo and baseline clipboard/HTML/link behavior. The normal persistent editor also owns checkpoint/journal recovery, local storage attachment and explicit save/error reporting. Hiding controls cannot remove those guarantees or stored marks. |
| Minimum production resources | Common core JS/glue/Wasm, essential CSS, registry admission, local durability and update/protocol primitives. No Markdown parser, typesetter, highlighter, remote provider/presence, custom dictionary, resolver or converter implementation is inferred from a sibling editor or an imported factory. |
| Optional implementations | Bounded codecs, comparison/export preparation, advanced table tools, presenters and host services use the existing resource/attachment and prepared-command ports. Their disabled stored data keeps an honest lossless fallback. The [named expanded inventory](extension-library.md#expanded-document-reference-configuration) is a separate configuration, never a relabeled Task. |

The minimum kernel still admits the one current format. A basic comparison can
exercise only paragraph/text/undo through the borrowed-engine surface; that is
an explicitly edit-only control, not permission to remove persistence from the
normal editor or claim that it is the existing default Task product.

### Companion interfaces and refusal behavior

These are roles of existing interfaces, not another plugin ABI or serialized
request envelope. `EXTENSION_DX_VERSION = 1`, `ConfiguredExtensionV1`,
`ExtensionStatusV1`, `ProfileResource`, the existing asset override and registry
remain canonical. Artifact compatibility is the exact reviewed package/build,
glue, ABI and URL under the web resource contract; data version is separate.

| Role | Existing boundary and allowed result | Required admission/refusal |
|---|---|---|
| Data/codec | `MarkdownCodec` consumes bounded source/options or immutable `FragmentBlock[]` and returns `PreparedMarkdown` / `MarkdownExport`, including diagnostics and recovery. Other codecs use their existing typed data result. A companion's memory holds only disposable working data. | No document, history, raw Rust pointer or plan handle crosses into a second kernel. Retain source on unavailable/unsupported/invalid output. The owning kernel validates every fragment before one prepared commit. No fallback parser, format relabel or silent conversion. |
| Command preparation | Host-owned context captures the existing `CapturedCommand` / `StableRange`; async work may return data for the existing `PrepareRequest`. Application rechecks current target/source, revision/generation, document/epoch, readonly and permission through the owning session. | `can`/prepare/commit and result selection/history remain synchronous in that kernel. A stale, cancelled, denied or unsupported result performs no mutation. A prepared plan cannot be imported from a companion replica. |
| Presenter/service | Existing incremental projection/patch, resource activation, host connector and resolver/checker ports; executable URLs are trusted host configuration, never document content. Return decoration, validated host data or a prepared command request. | No raw CRDT/DOM mutation authority, implicit public-fetch fallback or authority granted by shared code. Missing required host capability is an explicit unavailable/configuration error; preserve data and local recovery. |

Observe `unavailable/idle/loading/ready/failed/cancelled` and generation through
`ExtensionStatusV1`; do not invent a parallel status bus. Respect the configured
`required-input`, `command-lazy` or `presentation-lazy` policy. Required adapters
settle before actual edit readiness; command-lazy export never gates ordinary
typing. Until a parser is ready, retain literal source or refuse its explicit
operation. Current factories that declare required-input cannot be advertised as
already lazy; WEX-2.1/2.2 reconcile descriptor and managed-adapter readiness.

Freeze/validate the complete descriptor graph before attachment. Duplicate IDs,
incompatible data definitions, missing dependencies/permissions and unresolved
binding ties reject without partial activation. Preset overrides replace an
explicitly named member before admission; import/list order is not precedence.
Mixing legacy assembly (including Task preset fields) with facade assembly is a
typed conflict, not silent merging. Hosts use either the preserved legacy Task
path or the explicit expanded list, never a spread of one into the other.

Enable/disable owns per-instance subscriptions, stable targets, permission scope,
request generation and abort state. Disposal is idempotent; late completion must
release its resource and attach nothing. Shared immutable module initialization
may finish for another consumer, but retains no disposed document or callback.
No timer/provider/subscription/network work belongs to a disabled feature.

### Semantic comparison companion admission — 2026-10-28

Controller adoption for WEX-2.3: use a managed, explicitly preloaded stateless
comparison companion and preserve the synchronous `EngineHandle.compareSemantic`
and `WebHistoryStore.compare` contracts. This selects option (a) of the recorded
WEX-2.3 proposal. Loading may be asynchronous; comparison after readiness stays
synchronous. Local input, capture, history and ordinary editor readiness never
wait for comparison. The comparison action reports unavailable/loading until
its own managed resource is ready; it must not silently return a Promise.

The originating kernel exposes one read-only `prepare_semantic_comparison`
operation over the existing serialized `{before, after}` capture request. It
retains the current 4-MiB request bound, strict capture version/field parsing,
document/epoch/schema/profile scope checks, observed-token validation, binding
and semantic hash checks, canonical representation and unknown-data admission.
Keep the current 1-MiB/10,000-node/32-depth representation limits. Apply the same
checks and error behavior as the current `comparison::compare` before returning
data; neither JS nor the companion becomes a document admission authority.

The prepared result is a detached immutable pair of admitted semantic snapshots
and their existing `RevisionScope` metadata, named `before` and `after`. It uses
the current representation types/encoding; it is transient comparison input,
never stored document data, another capture format or a transferable engine
handle. Representation construction and bounded decoding may be shared pure
helpers; document/capture admission has one kernel implementation. No writable
replica, raw pointer, plan, allocation ownership or engine handle crosses modules.

The companion consumes only that pair, runs the existing `editac-diff` semantic
algorithm and returns the existing `SemanticComparison` model. Retain its
10,001-change and 4-MiB output bounds and equivalent structured failures. Move
the heavy algorithm's browser root into the companion; keep necessary capture,
representation and validation helpers in the kernel. Native consumers may keep
their existing synchronous bridge adapter using the same pure algorithm. There
is one canonical browser kernel, independent of presets, and no copied diff
implementation, dynamic linking framework or alternate HTML export path.

Attach the typed comparison adapter explicitly per engine/editor through the
existing resource/attachment ports. Match exact reviewed core/companion package,
build, glue, ABI and executable URL identities before activation. Reuse the
existing asset overrides and `ExtensionStatusV1` state/generation; do not invent
another loader or status bus. Shared immutable initialization can deduplicate,
but cannot enable a sibling instance. Before readiness or after detach, comparison
throws the existing structured `CapabilityUnavailable` error without mutation.
Invalid captures keep their existing validation failures once comparison is
admitted. Initialization failure, retry, abort, reconfiguration and disposal are
per instance; stale initialization must release its attachment and activate
nothing. Validate the companion's bounded result before exposing it.

WEX-2.3 owns implementation and focused comparison/error/disabled-graph checks.
WEX-2.6 wires the named expanded consumer to managed preload and action readiness;
WEX-4.1 owns remaining lifecycle coverage. Existing baseline HTML clipboard/export
stays in core and is not a removable leaf. This decision authorizes implementation,
not qualification, measured byte savings or a renewed optimization allocation.

### Standalone companions versus function splitting

Retain standalone stateless companions through these ports as the selected
architecture. This decision does not move shared validation/commit or introduce
another writable model. The [Leptos guide](https://book.leptos.dev/deployment/binary_size.html#code-splitting)
provides an alternative: lazy functions become async. The inspected
[cargo-leptos transform](https://github.com/leptos-rs/cargo-leptos/blob/af947bcdbbe2953865b855855f639b57585b0d12/src/wasm_split_tools/mod.rs)
declares `wasm_split_cli_support = "0.2.3"`; the inspected 0.2.3 crate emits
split modules and a prefetch manifest and links a generated JS loader. This is not an existing
edit.ac build option or a demonstrated byte saving.

| Concern | Existing standalone boundary | Single build graph split at async leaves |
|---|---|---|
| Toolchain | Rust/Cargo 1.97.1, bindgen 0.2.129, existing browser profile/Binaryen 132 and independent Markdown build; no framework dependency. | Requires split-point instrumentation, a pinned supported transform and generated loader integrated with bindgen/optimization/cache identity. Installed build scripts and Binaryen npm tools provide no such pipeline. No Leptos/nightly/framework adoption is authorized. |
| Memory/table/import ownership | Kernel owns its memory/table and document. Stateless companion owns independent scratch memory; immutable data crosses existing typed ports. Current kernel imports no host memory/table. | The inspected [0.2.3 emitter](https://docs.rs/crate/wasm_split_cli_support/0.2.3/source/src/emit.rs) shares data through linear-memory addresses and functions through an indirect table; its split analysis roots the main memory/table, and the JS loader invokes table callbacks. A viable edit.ac proposal must pin those main-kernel imports/exports, allocator/relocations and each leaf, with no second document. Current import/export guards do not establish this compatibility. Pointer/table bindings and changed glue cannot be silently treated as the present ABI. |
| Loading and bytes | Existing asset discovery/status/cancellation; measure common runtime plus each enabled module and glue once. | Count main and all required leaf chunks, loader/glue/manifest/CSS/assets and duplicated shared code. Async syntax alone proves neither smaller total union nor faster first use. No candidate measurement belongs to this contract session. |
| Readiness/failure | Only already asynchronous codec/export/analysis/presentation work may load separately; explicit unavailable/failed results retain source. | Only compatible async leaves are candidates. Input, composition, selection, validation/atomic commit and history cannot acquire a first-load await. Define retry, partial-load failure and per-instance cancellation before adoption. |

A future materially different split design needs an explicit proposal and
amended owning spec/acceptance before implementation, followed by current
boundary/semantic proof. The default here remains existing companions. Size or
startup experiments wait for physical delivery and consume the single shared
[optimization allowance](verification.md#shared-optimization-allowance).

## Residual delivery and final-check ownership

One responsible delivery parent and one WEX final-check parent are assigned to
each residual below. Canonical SDK/EXT/FIT/REL acceptance stays with its existing
roadmap owner; WEX supplies the bounded completion and receipts, not a duplicate
API, suite or benchmark. Already extracted RAQ session/bridge/native-service
boundaries are reused. Source-present v1 configure/resource/Markdown ports are
not a new claim that their unchecked canonical parents passed.

| Residual | Delivery parent | Final-check parent | Existing requirement consumed |
|---|---|---|---|
| Minimal Rust/browser feature graph | WEX-1.3 | WEX-4.1 | RAQ-1/4 boundary proof; SDK-1.12 |
| Disabled collaboration retained orchestration | WEX-1.4 | WEX-4.1 | SDK-1.12 |
| Typed options, presets, readiness/conflicts and custom authoring | WEX-2.1 | WEX-4.1 | SDK-1.11, EXT-1.14/1.15 |
| Independent codecs/presenters and managed assets, including Code admission | WEX-2.2 | WEX-4.1 | SDK-1.12; RCH-1.2–1.5 plus WCU-1.1 provide source-bound Code facade admission; complete expanded-consumer proof remains WEX-2.2 |
| Comparison/nonbaseline export preparation | WEX-2.3 | WEX-4.1 | SDK-1.13 and current codec/durability contracts |
| Advanced table tooling with retained shared invariants | WEX-2.4 | WEX-4.1 | Current table/durability contracts and original STB/RCH assertions |
| Optional host service/resolver/checker orchestration | WEX-2.5 | WEX-4.1 | EXT-1.16–1.19; feature semantics remain their existing owners |
| Named core/expanded public consumers and honest recipes | WEX-2.6 | WEX-4.3 | SDK-1.11/1.12, EXT-1.20 |
| Small-editor activation and lazy first-use fixed costs | WEX-2.7 | WEX-5.2 | SDK-1.13; REL-1.3 |
| Small-editor input/dispatch fixed costs | WEX-2.7 | WEX-5.3 | SDK-1.13; REL-1.3 |
| Small-editor retained resource/disposal costs | WEX-2.7 | WEX-5.3 | FIT-1.11; REL-1.4 |
| Retain one safely evaluated production optimization | WEX-3.2 | WEX-4.2 | SDK-1.13; WEX-3.1 supplies the frozen protocol/remaining shared allowance |
| Standard HTTP compression/cache/byte identity | WEX-3.3 | WEX-4.2 | FIT-1.10 |
| Missing tiny fixtures and competent comparator profiles | WEX-5.1 | WEX-4.3 | REL-1.2 |
| Remaining preservation/lifecycle coverage | WEX-4.1 | WEX-4.3 | FIT-1.11 |
| Current Task/expanded artifact assertions | WEX-4.2 | WEX-4.3 | FIT-1.10/1.11; REL-1.2 |

These receipt destinations are not reverse prerequisites. Execution remains
source01 → source02 → source03 → source03a → source04, with original per-parent
edges; WEX-2.7 cannot wait for WEX-5 results, nor WEX-3.1 for final WEX-4 size
qualification. FIT-1.10's baseline/work-count inputs precede SDK-1.13 candidates;
FIT-1.11 consumes their results. Existing qualified feature prerequisites are
consumed by exact applicable receipt, never expanded into a whole-track gate.
No dependency edge or checklist denominator is added by this ownership map.

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

The [block-actions contract](block-actions.md) adds required typed conversion registration, captured block targets, availability/disabled reasons and prepared lossless or explicitly reviewed conversion plans. Built-in heading/paragraph commands remain usable when optional block menus are off. Consume the existing registry, command-session and history owners; do not add a second dispatcher or editor state model. Delivery and final test ownership are in the [block-actions plan](../runner-queues/alpha-block-actions-20261023/README.md).

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

## Markdown table-source data boundary proposal — WEX-6.3

Decision state, refined for WSD-1.3 on 2026-10-29: **pending explicit adoption**. This proposal authorizes
no public API, wire, ABI or runtime change and claims no size saving. The decision
owner must explicitly adopt the payload, kernel guards and transport limits below
and reconcile WEX-6.3/WEX-6.4 acceptance before implementation. WEX-6.4 owns that
implementation; the existing size-candidate allowance is not renewed by adoption.
Keep all three WEX-6.3 checkboxes open while adoption is absent.

### Current retained entry paths

The following is source-call attribution, not an emitted Wasm call graph. Paths
are relative to `core/`; no build, size candidate or test is part of this review.

| Root / call site | Work reachable from the optional codec today |
|---|---|
| `crates/editac-markdown-wasm/src/lib.rs`: exported `table_source` → `table_source_value` → two `SnapshotInput::restore` calls | Each action restores both supplied checkpoints, even capture, which does not subsequently use the current document. Metadata includes identity, initialized state and writer ID; bytes travel separately. `DocumentIdentity::current` and restore perform admission, not just deserialization. |
| `crates/editac-core/src/document.rs`: `Document::restore` → `restore_with_budget` | Reaches update decoding/merging, staging and baseline Yrs documents, immutable-base and table-retention validation, replay projections/source-identity checks, pending-update rejection, candidate table snapshot validation, fresh writer/replica allocation and materialized table texts. These are actual calls, not an inference from Cargo edges. |
| `crates/editac-markdown/src/reconcile.rs`: `SourceBaseline::capture`, `prepare_table_format`, `source_with_current_table` | Captures a checkpoint and visible-owner bindings, reads external semantic fragments plus registered table-source provenance, compares normalized cell semantics, parses exact source, formats only the selected range and reparses the result. A changed format calls `Document::prepare_editor`, producing a disposable prepared editor plan in the codec. The Wasm adapter extracts source/replacement/expected attributes and drops that plan. |
| `crates/editac-bridge/src/bridge.rs`: `prepare_table_source`, `Plan::TableSource`, `commit` | The live kernel separately prepares the same source metadata command, guards exact checkpoint bytes before prepare and commit (including no-op), consumes a single-use token and owns history. `commands/editor/table_planner.rs` checks the exact current descriptor before `table::stage_source`. |
| `crates/editac-core/src/interchange.rs`: `parse`, `transfer_blocks`, `transfer_value` | Bounded transport and fragment/content/mark/link validation also serve ordinary import/export/equivalence. Removing restoration must not remove these checks. `yrs::Any` tuple translation can remain; a remaining Yrs dependency alone does not establish retained restoration. |

`SourceBaseline::prepare_inner` also restores an opening checkpoint for general
native source reconciliation, but `table_source_value` does not call that method.
Do not attribute every function in `reconcile.rs` to the exported table-source root
or delete the native workflow on the strength of this review.

### Proposed single current payload and ownership

Preserve the public `SourceBaseline` operations (`originalSource`,
`prepareTableFormat`, `sourceWithCurrentTable`, `dispose`) and explicit Markdown
registration/readiness. Replace the unpublished codec request in place; add no
legacy alias, second document format, companion document handle or writable model.

| Boundary | Current | Proposed, subject to adoption |
|---|---|---|
| Engine → adapter | `Checkpoint` metadata/bytes from the live engine; optional caller-supplied opening checkpoint | Keep those bytes private to the engine adapter. Add one bounded kernel projection port, `table_source_projection(input, checkpointBytes)`, with input `{mode, identity, initialized, writerId, owners}`. It admits against the owning engine identity. An exact live checkpoint uses the existing live document; only `mode:"opening"` permits a historical opening restored read-only inside the kernel through the existing restore path. `mode:"current"` requires exact live checkpoint equality. No restoration moves into JavaScript. |
| Kernel projection result | No source-specific projection port | `{identity, entries:[{owner, position, fragment, issue, expected}]}` as specified below. Entries cover only requested visible block owners in absolute visible order. An available `fragment` is the lossless external `FragmentBlock`, with registered table dialect provenance and retained source substituted exactly as `source_fragment` does today. `expected` is the actual production block-attribute tuple, kept privately by the adapter for the existing prepare command. It is distinct from the external table conversion tuple. Unknown/opaque data is preserved, never converted to an executable descriptor. |
| Adapter → codec | `TableSourceRequest`: baseline/current checkpoints, source, owners, action, selected owner, origin and options; Wasm receives JSON plus two byte arrays | `table_source(input, openingProjection, currentProjection)`, three bounded JSON strings. Metadata is the action union below; projections contain only `{identity, entries:[{owner, position, fragment, issue}]}`. No update bytes, initialized/writer metadata, production `expected` tuple, plan token or engine pointer crosses into the codec. Opening/current are separately owned immutable copies; never reuse a mutable callback object as the authoritative capture. |
| Codec → adapter → engine | `{source, changed?, replacement?, expected?}` followed by live prepare/commit | Return `{source}` for capture/recover; `{source, changed, replacement}` for prepare. The adapter supplies the private opening `expected`, replacement and origin to existing `prepare_table_source`, **using opening checkpoint bytes**, not a freshly captured checkpoint. The bridge's equality check therefore rejects a stale opening after any intervening change, including callback reentrancy. Origin validation and token/history ownership remain in the live kernel. |

Extract the pure parse/bind/equivalence/format/recovery logic into one data helper
within the existing Markdown crate. Both the native `SourceBaseline` adapter and
the optional Wasm entry use it; do not implement a second table lexer or semantic
comparison in the kernel or JavaScript. Document-specific projection extraction
belongs in the existing kernel interchange/bridge boundary. Codec capture checks
owner/block/range counts, uniqueness and increasing positions. Prepare checks the
selected retained top-level table against its opening/current semantic fragment;
recovery checks every bound owner and its order against current data. Preserve the
current distinction: prepare is strictly opening-revision pinned; recovery permits
undo/redo and reopen when represented semantics still agree.

The adapter validates current/opening identity through the kernel before invoking
the codec. Compare the full profile/schema/protocol/encoding/offset/document/epoch
tuple, not writer ID, a state vector or semantic equality. After a recover callback,
check that its captured current checkpoint is still current before returning source.
Keep permission/readonly admission at the existing host command boundary; an inert
projection or codec result confers no write permission. The kernel still validates
the prepared table metadata update and commits once. Parser fidelity remains a
codec obligation; the kernel does not acquire a Markdown parser.

### Exact proposed request, result and type ownership — WSD-1.3

These are the complete proposed envelopes, not additional runtime interfaces.
All fields shown are required; the action union forbids fields from other actions.
Reject unknown/duplicate envelope fields, invalid discriminants and invalid scalar
types before use. This does not reject unknown data inside an admitted opaque
tuple. Normalize omitted public option flags to `false` before transport.

```ts
// U32 is an integer in [0, 4294967295], never a floating-point position.
type U32 = number;
type SourceIdentity = {
  profile: string; schema: string; protocolVersion: U32; updateEncoding: U32;
  offsets: "utf16"; documentId: string; epoch: string;
};
type SourceOptions = { images: boolean; tables: boolean; callouts: boolean };
type SourceFields = { source: string; owners: readonly string[]; options: SourceOptions };
type TableSourceInput = SourceFields & (
  | { action: "capture" }
  | { action: "recover"; owner: string }
  | { action: "prepare"; owner: string }
);
type TableSourceValue =
  | { fragment: FragmentBlock; issue: null }
  | { fragment: null; issue: "UnsupportedContent" };
type TableSourceEntry = { owner: string; position: U32 } & TableSourceValue;
type TableSourceProjection = {
  identity: SourceIdentity; entries: readonly TableSourceEntry[];
};
type KernelTableSourceInput = {
  mode: "opening" | "current"; identity: SourceIdentity;
  initialized: true; writerId: U32; owners: readonly string[];
};
type KernelTableSourceProjection = {
  identity: SourceIdentity;
  entries: readonly (TableSourceEntry & { expected: Json | null })[];
};
type TableSourceTextResult = { source: string }; // capture and recover only
type TableSourcePrepareResult = { source: string; changed: boolean; replacement: string };
type KernelTableSourcePrepareInput = {
  owner: string; expected: Json; source: string; origin: string;
}; // existing prepare_table_source JSON; opening checkpoint travels separately
// Existing kernel prepare result and single-use commit(token) remain unchanged:
type KernelTableSourcePrepareResult = { token: string; revision: number };
type SourceError = {
  code: "InvalidInput" | "ResourceLimit" | "EngineRejected" |
        "InvalidHandle" | "CapabilityUnavailable" | "Disposed";
  operation: string; message: string;
};
```

`SourceIdentity` aliases the full current `DocumentIdentity`/`Snapshot.identity`
contract in `packages/core/src/engine.ts`; no new identity version is introduced.
All seven fields must equal the owning engine's current identity. The kernel
applies existing initialized-checkpoint/writer admission; writer ID is provenance,
not a revision or document identity. Owner strings are opaque existing node IDs,
not parser indexes. `position` is the absolute zero-based visible-node index;
entries contain only visible nodes of kind `block`, ordered exactly as the kernel
projection request's `owners` (the action protocol defines each request's scope).
There are no extra or duplicate entries. Positions strictly increase, but need
not be contiguous. Missing/deleted owners reject; reversed recovery order retains
`MovedTarget`, while duplicate/out-of-order capture bindings retain
`AmbiguousMapping`. No new per-ID string cap is imposed beyond current admission
and the aggregate envelope limits.

`FragmentBlock`, `FragmentRun`, content tuples and opaque marks retain the existing
inert value types owned by core's editor/fragment and content modules. The wire
shape is the canonical external fragment emitted by `interchange::transfer_value`;
known nested fields keep their existing validators. An opaque tuple must survive
the read-only projection decoder losslessly, even when an executable content
codec is not registered. In particular, do not route this decoder through
`transfer_blocks`' `unregistered content` rejection, register unknown content, or
weaken ordinary Markdown import. Unknown data remains non-executable data.

`issue` is a deferred existing `source_fragment` refusal, not an overflow escape:
only an otherwise admitted visible block whose existing source-fragment read
would return `UnsupportedContent` may use `fragment:null`. Its original bytes
remain in the kernel/private opening checkpoint. Available unknown/opaque values
must be copied, never replaced by this marker. A size, identity, missing-owner or
malformed-checkpoint failure still rejects at the kernel boundary. Capture today
binds parser ranges and visible owners without requiring all blocks to be
reconcilable; making every fragment read a successful-capture prerequisite would
silently narrow that behavior. Prepare/recover consume a required unavailable
entry by returning the same `UnsupportedContent` refusal, without dropping source.

Own the new inert `TableSourceProjection`, `TableSourceEntry`,
`CapturedTableSource` and `TableSourcePrepared` types and the pure
`capture_table_source`, `prepare_table_source_data`, `recover_table_source_data`
helpers in the existing `editac-markdown/src/table_format.rs` module. Keep the
parser, `source_equivalent` and semantic `equivalent` implementations canonical;
make their existing crate-private seam callable rather than duplicate them.
`CapturedTableSource` holds opening identity, source/options/owner bindings, parsed
blocks and UTF-8 ranges; `TableSourcePrepared` holds only source/changed/replacement. No helper
accepts or reaches `Document`, a checkpoint, `TextOrigin`, a plan or mutation.
`SourceBaseline` in `reconcile.rs` remains the native document adapter: perform
identity/exact-byte checks, build the same projections, call the shared helpers,
then prepare the native editor plan there. Its general Literal/paragraph source
reconciliation and `prepare_inner` workflow remain intact. Preserve native typed
`Conflict` recovery fields; ordinary diagnostics remain redacted.

The exact shared pure seam is:

```rust
capture_table_source(source: &str, codecs: Codecs, owners: &[String],
    opening: &TableSourceProjection) -> Result<CapturedTableSource, Conflict>;
prepare_table_source_data(base: &CapturedTableSource,
    current: &TableSourceProjection, owner: &str) -> Result<TableSourcePrepared, Conflict>;
recover_table_source_data(base: &CapturedTableSource,
    current: &TableSourceProjection, owner: &str) -> Result<String, Conflict>;
```

These are proposed signatures, not compiled declarations. Native table methods
adapt their retained data to this seam; the stateless Wasm entry captures the same
inert baseline before dispatching each action. Exact checkpoint checks and native
editor-plan preparation stay outside these functions.

The kernel projection builder belongs in the existing bridge/document-interchange
boundary. It alone reads `external_fragment_for_node`, retained table source and
the actual production `fragment_for_node(...).attributes` tuple for `expected`.
The tuple is not the external `Content::Table` conversion tuple. No new types
crate, document cache, engine handle, pointer or second writable replica is
proposed. `packages/core/src/engine.ts` owns the TS adapter declarations and
private capture; `packages/markdown/src/index.ts` and the Markdown Wasm entry
adapt to them together in WSD-4.3. Replace the exported codec-hook
`TableSourceRequest`/`TableSourceResult` shape in that atomic cutover; public
`SourceBaseline` methods keep their existing signatures. Add no compatibility
alias to the unpublished checkpoint-based codec contract.

### Action protocol and atomicity

| Action | Kernel/adapter sequence | Pure codec obligation and result |
|---|---|---|
| capture | Copy source/options/owners and opening checkpoint privately; validate explicit opening against the owning engine with `mode:"opening"`. Exact-live bytes use the live document; only a historical opening may restore once, entirely in the kernel. Keep opening projection/expected tuples privately. Obtain a current identity projection with `mode:"current", owners:[]`; it carries no unused current fragments. | Parse with the canonical enabled codecs; preserve the empty-source fallback. Require parser block/range/owner counts to agree, unique owners, valid UTF-8 slice boundaries and increasing opening positions. Do not newly require every opening block to be semantically equivalent or formattable at capture. Call `table_source(input, openingProjection, currentProjection)` and return exactly `{source}` equal to the original text. |
| prepare | Request `mode:"current"` with the **private opening checkpoint** and bound owners. The kernel rejects unequal bytes/identity before codec work, including no-op. Invoke the codec with fresh detached projection copies. After the callback, validate its result and pass private opening `expected`, private owner/origin, result `replacement` and the same opening checkpoint to existing `prepare_table_source`. The callback supplies no authority-bearing fields. | Require a bound selected retained top-level table with tables enabled; use opening/current semantic fragments and provenance, exact retained source/range and the canonical row lexer. Replace only that range, reparse and compare all parsed semantics and diagnostic codes. Return `{source, changed, replacement}` with `changed === (source !== originalSource)`; replacement is the selected table text even for no-op. |
| recover | Capture a fresh current checkpoint and obtain `mode:"current"` projection for all bound owners. Call the codec on detached copies. After the callback, recheck engine disposal/registration and call the same projection port with `mode:"current", owners:[]` and the captured current checkpoint: unequal live bytes reject before returning text. No plan is allocated or committed. | Identity must match opening. Substitute only the selected current retained table source into the opening text. Reparse, compare opening/candidate semantics, then compare every bound current fragment with its candidate block in increasing current order. Return `{source}`; checkpoint equality with opening is deliberately not required, allowing supported undo/redo and reopen. |

`table_source_projection` returns JSON `KernelTableSourceProjection` and accepts
its JSON input plus one checkpoint byte array. `table_source` accepts exactly
three JSON strings: action metadata, opening projection and current projection;
its result is the action-specific JSON object above. The codec sees neither
checkpoint bytes nor private `expected`/origin. The capture current projection has
zero entries; prepare/recover current projections cover all bound owners.
Identity is checked for both projections. Current-mode projection never restores
a checkpoint; a stale read cannot fall back to historical-opening admission.

Before each callback, retain a separate immutable authoritative copy (serialized
strings or independently owned data); shallow `Object.freeze` is insufficient for
nested objects and byte arrays. Caller-supplied opening bytes and all nested
inputs are copied after ordinary plain-data admission. The callback cannot modify
the adapter's opening checkpoint, expected tuple, owners, options or origin.
Validate returned JSON shape, limits and changed flag, recheck disposal and the
captured Markdown registration after every callback, and pass no codec-supplied
identity/expected/token into a kernel command. A custom codec remains responsible
for parser fidelity, as for existing Markdown hooks; data is not write permission.
Host permission/readonly admission continues at its existing command boundary.

The live kernel repeats exact opening-byte comparison, origin/descriptor/target
validation and plan limits in `prepare_table_source`. It returns the existing
single-use plan token; commit consumes it before rechecking the exact checkpoint,
including no-op. A changed commit performs one existing editor transaction/history
group. A no-op consumes a guarded token with no update/history group. Every
refusal leaves document bytes/history unchanged by this operation; a reentrant
host edit remains that host edit and must not be rolled back. There is no source
rewrite, checkpoint replacement, plan retry or silent recapture after rejection.

Current implementation gaps must not be mistaken for preserved proof: the old
codec restores each checkpoint against its own supplied identity, so capture
does not itself bind a foreign opening to the live engine; later prepare/recover
compare identities. The TS prepare adapter also passes a fresh current checkpoint
to the bridge and relies on codec-side opening validation, and recover lacks the
post-callback checkpoint check. The proposed earlier foreign-capture refusal,
private-opening kernel guard and callback checks are explicit adoption terms.

### Bounds, refusal and cost to verify

Keep source and formatted replacement at 1,048,576 UTF-8 bytes, at most 128 owner
bindings, parser ranges on valid byte boundaries and existing fragment limits
(128 blocks, 1,024 outer runs, 1 MiB outer text, 16 containers, six known marks per
run), plus existing nested table/opaque-value limits. Public positions remain
UTF-16; source slices remain UTF-8 byte ranges. Keep checkpoint admission at the
existing 16 MiB per supplied checkpoint and metadata JSON at 2 MiB. Proposed
projection transport ceiling: 16 MiB **per projection**, separate from metadata,
checked before allocation/serialization as well as codec decoding; all existing
JSON depth/structure and nested-content limits still apply. Do not simply pack
both projections into today's 2 MiB request or strip unknown data to make it fit.

The exact proposed transport accounting is below. Byte caps include JSON syntax
and escaping, not just string payloads; count the complete value, including
envelopes, at each boundary. No field may be truncated to meet a cap.

| Value | UTF-8 byte ceiling | Count/shape ceiling |
|---|---:|---|
| Action metadata, or kernel projection input | 2,097,152 each | At most 128 owners; three explicit boolean options for codec metadata; 100,000 visited JSON values, depth 32 with the root at depth 0 |
| Opening checkpoint, or supplied current checkpoint | 16,777,216 each | Existing initialized-checkpoint admission; never encoded into JSON or given to codec |
| Complete kernel projection result (including private expected tuples), or each codec projection | 16,777,216 each | At most 128 entries; current capture/check-only projection has zero; 100,000 JSON values, depth 32 per complete projection |
| Original source, recovered/formatted full source, selected replacement | 1,048,576 each | UTF-8 source slice boundaries; outer fragment admission remains 128 blocks, 1,024 runs, 1,048,576 text bytes, 16 containers per block and six known marks per run |
| Codec success result | 16,777,216 | Exact action result shape; no returned fragment/checkpoint/expected tuple. Two maximally JSON-escaped 1 MiB strings fit this ceiling; still count the actual output |
| Final kernel prepare JSON | 2,097,152 | Existing owner/expected/source/origin validators; at most 128 live plans (`bridge::MAX_PLANS`), checkpoint is separate |
| Error JSON | 4,096 | Only code/operation/message; message at most 512 Unicode scalars, safe constant reason plus redacted detail, no source or tuple payload |

Structural integer fields use their existing integer domains; opaque JSON numbers
and values retain current kernel admission rather than being coerced or filtered
by a new generic JS validator. Nested table/content/opaque values must still pass
the existing content and fragment validators; the outer counts are not an
exemption from their per-value limits. Opening/current limits are independent:
never combine them into one 16 MiB allowance. Check size/count/depth while bounded
reading/writing, before cloning an unbounded value or allocating the full encoded
output. Reuse a capped serializer/deserializer for projections and results;
`interchange::parse` retains its current 2 MiB ceiling for ordinary commands.
Do not raise that shared constant to admit the new 16 MiB projection envelopes.

The 16 MiB projection ceiling is a proposed transport bound, not proof that every
currently successful checkpoint/source pair fits it. WEX-6.4/WSD-4 must establish a
conservative encoded bound for represented fragments (including JSON escaping,
table cells and opaque data) against existing admission, or return a concrete
limit amendment for explicit adoption before shipping. Reject overflow without
mutation and retain original source/checkpoint bytes; silently narrowing admitted
content is not an implementation shortcut.

The proof includes the new projection depth/count overhead, private `expected`
duplication, escaping and the unchanged final prepare envelope, not merely raw
fragment text. A cap that cannot represent existing admitted recovery data is a
decision-owner amendment, not permission to mark that content unavailable or
raise shared command limits. No such proof or amendment is supplied by WSD-1.3.

Retain deterministic `InvalidInput`, `ResourceLimit`, `EngineRejected` and
capability/disposal failures. Preserve identity mismatch, stale/no-op plan,
deleted/moved owner, overlap, unsupported dialect/nested source and ambiguous
mapping distinctions. Do not leak retained source into ordinary error messages;
the caller keeps exact original text and recovery data on all failures. Recovery
substitutes only the selected current retained table source into opening bytes,
reparses and compares every represented binding. It never serializes the entire
document or repairs source on rejection.

Wasm errors retain the existing rejected JSON-string `SourceError` transport;
success has no error wrapper. Adapter lifecycle failures remain `EngineError`.
Use the originating operation (`tableSourceProjection`, `tableSource`,
`prepareTableSource`, `commit`, or the existing public adapter operation), without
embedding caller text in messages. The deterministic refusal map is:

| Condition | Code / retained distinction |
|---|---|
| Malformed envelope, unknown/duplicate schema field, action/scalar mismatch | `InvalidInput` |
| New transport byte/count/depth overflow, or existing live-plan count overflow | `ResourceLimit`; retain the existing final-prepare checkpoint-length branch's `EngineRejected` / `StalePlan` |
| Foreign full identity, or checkpoint rejected by current restore admission | `EngineRejected`; retain `IdentityMismatch` or the existing kernel admission reason |
| Unequal checkpoint at current projection, prepare or commit, including no-op | `EngineRejected` / `StalePlan` |
| Missing/deleted owner, reversed recovery order, ambiguous capture mapping | `EngineRejected` / `DeletedTarget`, `MovedTarget`, `AmbiguousMapping` respectively |
| Changed represented semantics, live marks or provenance | `EngineRejected` / `Overlap` |
| Disabled table codec on prepare, non-table/nested/unsupported dialect, unavailable source fragment, invalid retained range | `EngineRejected` / `UnsupportedContent`; retain existing kernel `UnsupportedTarget` where that boundary owns the refusal |
| Consumed/released/foreign plan token | Existing `InvalidHandle` |
| Disposed engine/baseline or removed/replaced registration | Existing `Disposed` or `CapabilityUnavailable` |

Validate resource/shape and owning identity before document-derived projection;
current-mode equality precedes formatting. Codec validation then follows the
action protocol; live prepare and commit repeat their existing guards. Multiple
invalid conditions need a deterministic boundary refusal, not an attempt to repair
them. All failures preserve the private original source/checkpoint for retry or
explicit recovery; no error counts as recovered text or a successful commit.
Do not add an unconditional tables-enabled gate to capture/recover: their existing
parse/equivalence behavior remains action-specific, including `Overlap` on a
recovery semantic mismatch.

Today there are two explicit restores per codec action; each restore constructs
staging, baseline and fresh replicas. A changed format also prepares one discarded
plan before the live engine prepares another. The proposed normal live capture
needs zero restores, an explicit historical opening needs at most one kernel
restore at capture, and later prepare/recover need none. It retains two immutable
data projections (up to 32 MiB serialized under the proposed ceilings), opening
checkpoint bytes privately, and source/parsed working copies; actual peak memory
and clone/encoding work remain unmeasured. Reuse rather than retain another copy
of unchanged opening data when safe, without weakening immutability.

The intended removed codec roots are `SnapshotInput::restore`, document snapshot/
checkpoint capture, document-based `SourceBaseline` calls and discarded editor
plan preparation. Ordinary Markdown parsing/export/equivalence and portable
fragment validation remain. Core already exports restore, external fragments,
table-source reads, prepare and commit, but the new projection serializer, bounds
and glue can increase core cost. No byte delta or net saving is established here.
WEX-6.4 must inspect emitted roots and report core **and** codec deltas plus the
complete distinct-resource gzip union under the existing allowance; moving bytes
between artifacts or summing overlapping estimates is not acceptance.

The source call graph to remove from the **optional codec export** is:

```text
table_source -> table_source_value
  -> SnapshotInput::restore(opening) -> Document::restore -> restore_with_budget
  -> SnapshotInput::restore(current) -> Document::restore -> restore_with_budget
  -> SourceBaseline::capture -> Document::{snapshot,checkpoint}
  -> prepare_table_format -> source_fragment / Document reads
       -> Document::prepare_editor -> discarded PreparedEditorEdit
  -> source_with_current_table -> Document::snapshot / source_fragment

proposed codec: table_source -> capture/prepare/recover pure data helpers
proposed kernel: table_source_projection
  opening + historical bytes -> existing Document::restore (at most once/capture)
  current -> exact byte/identity guard -> live fragment/source projection (no restore)
  -> existing prepare_table_source -> existing guarded single-use commit
```

Only the old exported table-source reachability is attributed here; the deeper
restore internals above reuse the earlier source attribution, not a new emitted
graph measurement. General native `SourceBaseline::prepare_inner` restoration
and ordinary Markdown import/export validation remain owned by their existing
paths. Newly retained kernel cost can include projection admission/serialization,
lossless opaque decoding, private copies and repeated exact-byte comparisons;
new codec cost includes projection decoding and bounds. Report each Wasm plus
wrapper/glue and the distinct-resource union at WSD-4.4. The research baseline
Markdown 1,814,436 raw / 585,582 gzip bytes is retained evidence, not a new result
or an estimate of removable bytes.

### WSD-4 preservation and adoption matrix

This maps the proposal to existing source-04 acceptance without editing or
expanding that controller-owned roadmap. Every row is an implementation/proof
obligation for its existing owner, not a passing runtime assertion here.

| Existing owner | Contract seam / preserved assertion | Existing evidence selector or required missing proof |
|---|---|---|
| WSD-4.1 | One pure formatter/recovery helper in `table_format.rs`; native adapters keep one implementation, general reconciliation and typed errors | `editac-markdown` existing `table_format` cases and canonical lexer corpus; select exact existing filters at implementation |
| WSD-4.1 / WSD-4.3 | Selected range only; unchanged other tables, spans, backing text, identities/records; Unicode scalar padding, escapes/marks, CRLF/mixed endings/no EOF newline | `exercise`, `selected_first_table_keeps_surrounding_bytes_and_second_table_exact`, `selected_second_table_keeps_first_table_exact`, lexical/Unicode/line-ending cases in `crates/editac-markdown/tests/table_format.rs` |
| WSD-4.2 | Full opening/current identity, strict private opening bytes before prepare and delayed commit, guarded no-op, no mutation/history on refusal | Existing bridge `prepare_table_source` / `Plan::TableSource` / `commit`; native `stale_baseline_and_delayed_commit_reject_with_zero_effects`, `stale_noop_commit_also_rejects`, `foreign_replica_identity_rejects_prepare_and_commit`, remote-replay case |
| WSD-4.2 / WSD-4.3 | Exact production descriptor, target and origin remain kernel-owned; no callback authority; one transaction/history group and single-use token | Existing bridge source-table success/stale/noop cases below and native descriptor/limit cases; private-copy/reentrancy and earlier foreign-capture behavior need focused proof at cutover |
| WSD-4.3 | Recovery joins current selected table source to opening bytes, compares every represented owner/order and semantics, supports ordinary undo/redo/reopen | `exercise`, changed/deleted-target and live-cell-mark native cases; existing bridge history/recovery/targeted-invalidation case; post-callback stale recovery needs focused proof |
| WSD-4.3 | Unknown/opaque attributes and original recovery data survive disabled codecs and refusals; malformed/duplicate envelopes and overflow reject without partial writes | Existing non-table/unknown-owner/disabled-codec, source-limit, excess-cell and nested-container refusals; existing Wasm admission assertions below; lossless projection decoding and complete encoded bounds need proof, not fixture relabeling |
| WSD-4.3 | Atomically switch kernel export, codec Wasm, both TS adapters and affected declarations; no checkpoint codec alias or stored-data conversion | Existing Markdown consumer selectors and installed declarations specified by WSD-4.3; no build/consumer execution in WSD-1.3 |
| WSD-4.4 | Remove exported restore/discarded-plan roots without removing portable validation; measure core, codec and the nonoverlapping resource union | Emitted graph/import-tree and current artifact/resource inventories; zero renewed optimization seconds/hypotheses; source graph alone is insufficient |

Decision owner still owes an explicit adoption reference for the complete schema,
mode-specific guards, deferred-unavailable capture representation, pure type owner,
callback protocol and numerical transport/error limits above. Before WSD-4 dispatch,
the controller must reconcile any concrete amendment with WEX-6.3/WEX-6.4 and
WSD-4 acceptance, confirm checkout/build ownership and candidate authority, and
retain the preservation-bound proof obligation at its existing owner. Discharge
that proof or adopt a concrete limit amendment before the runtime cutover ships;
it does not prevent WSD-4.1's adopted private extraction. Completing WSD-1.3 is allowed
while this decision is pending; it neither checks WEX-6.3 adoption nor releases
source 04. No runtime cutover, encoded-bound proof, emitted-root result, size delta
or peak-memory result is claimed.

### Preserved assertions and adoption gate

Source review maps the proposal to these existing assertions; none was executed
or promoted to a passing receipt by this proposal:

- `crates/editac-markdown/tests/table_format.rs`: `exercise` and the selected-first/
  second-table cases preserve surrounding bytes, all other tables, spans, backing
  text, table identities/records, one undo group, no-op behavior, undo/redo and
  reopened source recovery. Keep the original `source_reads == 0` and no topology
  rebuild assertions, including any historical failures.
- The same file's escaped-pipe/code/mark, Unicode-scalar, CRLF, mixed-ending,
  missing-EOF-newline and implicit-empty-cell cases preserve exact lexemes;
  excess-cell and nested-container cases reject rather than discard source.
- Its stale-baseline/delayed-commit, stale-noop, changed-descriptor/deleted-target,
  foreign-identity, remote-replay, disabled-codec/unknown-owner, source-limit and
  live-cell-mark cases preserve refusal and zero-effect assertions.
- `crates/editac-bridge/src/table_source_cases.rs`:
  `source_table_codec_engine_history_recovery_and_targeted_invalidation`,
  `source_table_stale_prepare_and_single_use_commit_have_zero_effects` and
  `source_table_noop_guard_and_invalid_target_reject_without_mutation` retain the
  real optional-codec → live-kernel boundary, patch targeting, fresh replay parity,
  history/recovery, exact stale guards and consumed-token rejection.
- `crates/editac-markdown-wasm/src/lib.rs` existing Unicode roundtrip, unknown/
  unbounded input, optional-content and unsafe-link admission cases remain required.
  WEX-6.4 selects affected existing cases; WEX-4.1/4.2 retain broad coverage ownership.

Missing proof: emitted restoration-root removal, transport-bound preservation,
mutation/reentrancy resistance of projection copies, packed consumer/load parity,
focused semantic results and core-plus-codec resource accounting. Adoption reference:
**none**. Exact decision needed: adopt this one current projection payload, private
opening-checkpoint guard, shared pure codec helper and proposed transport ceiling
with its admission-proof obligation, or state a concrete amendment. Then update
the affected live task acceptance together before WEX-6.4 changes contracts.
Until that decision, defer to the user/controller decision owner; do not repeatedly
redispatch the same proposal review. Independent source tasks remain eligible.

## Size reduction and compression

Reuse the [existing byte inventory and budgets](verification.md#browser-bundle-size-budgets); do not build another accounting harness. Report baseline, each extension, representative combinations and multi-editor/site unions. Record initial/deferred resources separately and combined, raw/gzip/Brotli bytes, hashes and exact compressor settings. Required lazy code still counts. Enabled optional costs are explicit; disabled features contribute no heavy implementation assets. Broader combinations are chosen by shared input/history/async risk, with uncovered combinations stated.

Measure contributions before choosing reductions: broad re-export/side-effect retention, generated glue, WASM dispatch/export reachability, parser/serializer dependencies, duplicated chunks, fonts/grammars and compilation/startup cost. Optimize actual retained work and use the existing size-oriented Rust/WASM build controls. Preserve Unicode correctness, schema/fallback compatibility, history, collaboration, persistence and the existing default clipboard guarantees. Do not create an engine binary per preset or remove promised features merely to pass a cap.

Qualify gzip/Brotli server/CDN delivery with Content-Encoding, Vary: Accept-Encoding, correct JS/WASM MIME, immutable compatible asset URLs and uncompressed fallback. Preserve compressed/decompressed size distinction and cold/warm transfer provenance. HTTP compression reduces transfer bytes; it does not reduce decompressed WASM memory or compilation automatically. Choose precompression and caching from measurements, with no remote infrastructure provisioning required for local proof. Record measured gains, startup/compile tradeoffs and remaining headroom; no speculative percentage reduction is promised. Existing caps are unchanged.

WASM is a workload-specific optimization, not an automatic speed guarantee. Attribute call count, encoding/decoding, copies, allocations, execution and rendering separately before moving work. Keep semantic ownership in Rust; compare equivalent pure JS/WASM kernels only where they do not introduce another writable document. Batch work at existing semantic transaction boundaries, avoid per-character boundary chatter and measure small interactive inputs as well as large batches. SDK-1.13 uses the performance contract to accept or reject each hypothesis; size wins cannot conceal input, startup or memory regressions.

### Post-RAQ attribution decision — 2026-10-28

WEX-1.1 uses a fresh production build and the existing packed Task consumer, not
the historical byte observations. Its source pins, resource inventory, section
inspection and limitations live in
`.roadmap-runner/wasm-extensions-20261027/01-core-boundaries.progress.md` at the
workspace root. Inventory generation does not qualify the existing size caps;
both Task caps remain unmet. No optimizer candidate or runtime contract change
is adopted by this decision.

Keep one Rust semantic kernel for document admission, validation, preparation,
atomic commit, history, anchors and update primitives. The post-RAQ normal Wasm
graph already consumes the portable bridge, session asset serialization and HTML
codec without the optional Markdown/source-edit, native-store, database,
authority-service or native-adapter implementations. Reuse those extracted
boundaries; a Cargo edge alone is not proof of retained shipping bytes or a
hot-loadable capability.

The packed JS graph retains collaboration attachment, session and presence
orchestration through the editor/surface dynamic imports. In this single-output
consumer those imports defer execution, not delivery bytes. WEX-1.4 should use the
existing attachment/resource gateway for that measured seam, preserving the
shared update/protocol primitives and required persistence/asset work. Keep
explicit attachment callers, per-editor permissions, cancellation and disposal;
do not introduce another loader, event bus or writable document. Other retained
configuration, conversion and spelling adapters remain separately visible work,
not assumed savings from this seam.

Exact production data matches establish retained grapheme and ICU
normalization/property tables. Preserve their Unicode editing and URL/IDNA
behavior. The canonical normal Cargo graph contains no regex crate family;
there is no measured regex-table reduction to claim. Name-preserving diagnostics
implicate typed Serde/JSON instantiations and formatting/container paths as
investigation leads. They do not justify removing required serializers, typed
errors or recovery detail. The Wasm adapter already shares its result/error
serialization helpers; retain that control rather than proposing it again.
The diagnostic layout differs from production, so its
shallow symbol sizes are not shipping ownership totals or compressed savings.
Transitive retained-call-graph and individual merged-data ownership remain gaps.

Generated glue is already included in the packed JS resource. The current
production bindings use legacy reference handling despite the optimizer's
reference-types allowance; preserving compiler feature metadata in a diagnostic
changed the bindgen boundary. Treat alternate glue/ABI settings as a separately
proposed contract decision, not an attribution-only improvement. WEX-1.2 still
owns the frozen capability/interface inventory and budget mapping before any gate
change. Preserve Task editing, composition, selection, clipboard, formatting,
local recovery and history while hosts select optional implementations.

## Review basis — 2026-10-17

Tiptap documents [extensions](https://tiptap.dev/docs/editor/core-concepts/extensions) for content and behavior and an optional [StarterKit](https://tiptap.dev/docs/editor/extensions/functionality/starterkit) with configurable/disabled members. These inform composition and basic defaults, without requiring Tiptap runtime or schema compatibility. Its [Collaboration extension](https://tiptap.dev/docs/editor/extensions/functionality/collaboration) configures a Yjs document/fragment and supplies history that conflicts with ordinary UndoRedo; edit.ac instead retains its existing Rust/Yrs document/history owner. Its [performance guide](https://tiptap.dev/docs/guides/performance) recommends isolated editor components and selected-state subscriptions. These are upstream design references, not measured edit.ac results.

The local review inspected `BrowserEditor.attachSync` and the static sync import in `packages/web/src/editor.ts`, the operation/source indexes in `packages/web/src/modules/runtime.ts`, and admission/freeze in `packages/core/src/extensions/registry.ts`. They provide existing integration points; runtime and bundle overhead remain to be measured. [V8's call/inlining discussion](https://v8.dev/blog/wasm-speculative-optimizations) explains why call overhead can dominate tiny functions; the [Rust/WASM size guide](https://rustwasm.github.io/docs/book/reference/code-size.html) supports attribution before tuning. Neither establishes a universal WASM advantage or an edit.ac speedup.

## Documentation and delivery evidence

Ship one-import getting started, first-party configuration, a public API reference and original runnable custom extension tutorials. Include ASD-123, spelling suggestions, a custom parser and URL insertion with deterministic fixture services, plus mark/atom examples using admitted data primitives. Show only public imports, typed options, behavior before/after, errors, cancellation, undo, preservation and disposal. Beginners do not copy internal codec/worker orchestration. Advanced asset hosting and migration from low-level APIs are separate guides.

Core owns canonical recipes and clean packed consumers; DOC-1.34/1.35 consume their immutable qualified source ranges in the public catalog/tutorials. Planned notation stays labeled until the matching artifact exists. [The case catalog](../tests/extension-dx-cases.md) defines required outcomes, not passing evidence. Create named tests before executing them and record nonzero counts, failures/skips, exact source/package/build identities and process teardown. All automated services are deterministic fixtures/mock transports; no paid inference, secret loading, publication or deployment is authorized by this amendment.

# Rich-content implementation ownership

RCH-1.1 maps current implementation boundaries; it does not qualify feature runtime,
performance, production-Wasm consumption, native UI or a release. The deterministic
[entry map](../../core/fixtures/rich-content/entry-map.json) names actual definitions,
public port targets, original remaining owners and focused validation targets.
Its source hashes identify working-tree bytes, including unfinished changes;
`sourceRevision` is repository provenance, not a claim that HEAD contains those bytes.
The [entry check](../../core/tests/rich-content-entry.test.mjs) verifies the map.

## Reuse and remaining ownership

Existing implementation stays with its current owner. “Remaining” below means the
original behavior must be reconciled and verified there; source presence alone does
not certify it or justify implementing a second copy. The map's `gaps` retain the
original RCH IDs and behavior, with `owner-acceptance-unverified` status. Its
`validationTargets` are check navigation, never passing receipts.

| Feature | Existing implementation and public target | Remaining original ownership |
| --- | --- | --- |
| Code | `BlockCommand` and `DOMRenderer` preserve literal code. `editac-highlighting::Backend` and `cache::BlockInput` own derived syntax. `@edit-ac/web/modules` exports `HighlightScheduler`, `createHighlightWorker`, `codeHighlighting`; `@edit-ac/core/extensions` exports `executeCodeCommand`; `@edit-ac/web` exports `codeCommands`. | RCH-1.2: authenticate selected backend/grammar and actual production-Wasm probes. RCH-1.3: revision/cache/cancellation/offset invariants and WCF-16 counts. RCH-1.4: lazy bounded scheduling. RCH-1.5: editing/composition-safe rendering. RCH-1.22: logical-line commands and opt-in pairing. |
| Tables | Existing Rust `EditorCommand` / `TableAction` and current table projection own semantics. `contentModules` delegates to `tablePresenters` / `currentTable` through `@edit-ac/web/modules`. Reuse direct cell editing and scoped commands. | RCH-1.6–1.10: structure/concurrency/rejections, header/alignment, rectangles/navigation/clipboard, exact-source formatting, affected-table work and cache bounds. Current independent table data is authoritative; historical tuple readers are not a compatibility requirement. |
| Assets | Rust `AssetDescriptor` and Session `AssetWork` own identity and lifecycle. `@edit-ac/core` exports `AssetIdentity`; `@edit-ac/web/assets` exports `AssetSession` and host transport types. | RCH-1.11–1.12: validate descriptor states and forbidden persisted credentials/URLs, then resumable idempotent work, journaling, cancellation, recovery and reference release. |
| Images | `imagePresenters` is installed by `contentModules`; `ImageAssetPort`, `ImageMetadata` and `ContentOptions` are public at `@edit-ac/web/modules`. | RCH-1.13: actual media/decode bounds, SVG/animation policy, offline/unsafe fallback and request/decoder/object-URL disposal. |
| Files | `attachmentPresenters` and `AttachmentPort` already exist at `@edit-ac/web/modules`; reuse bounded clipboard metadata and explicit authorized open/download. | RCH-1.14: inaccessible/offline/locked states, fresh action authorization and identity-preserving export. PDF stays opaque. |
| Embeds | `embedPresenters` at `@edit-ac/web/modules` reuses link resolution through `@edit-ac/web/links`; source fallback and host-trusted provider templates already exist. | RCH-1.15: bounded metadata, explicit fresh activation, isolation and teardown; no provider HTML or automatic network on rendering. |
| Slash | `slashCommands`, `SlashPresenter` and `SlashContext` remain at `@edit-ac/web/modules`; reuse prepared registered actions. | RCH-1.16: complete committed-context/IME/accessibility/cancel/error/focus behavior and later ready-runtime measurements. |
| References | `Content`, `ReferenceLookupSession` and `PrivateReferenceView` retain semantic target/fallback and host privacy. `referenceSuggestions`, `ReferenceHostV1`, `privateReferenceDisplay` are public at `@edit-ac/web/modules`. | RCH-1.18: configured bounded triggers, all display states, stale activation and privacy invariants. |
| Reorder | Rust `MoveCommand` owns final mutation. `reorderControls` / `ReorderPresenter` at `@edit-ac/web/modules` already provide pointer sessions and keyboard/click alternatives. | RCH-1.17: threshold/hit-testing/autoscroll/cancellation, concurrent anchors and exactly one final move/history group; no hover mutation. |
| Find/Replace | `DocumentSearchSession` at `@edit-ac/core/extensions` and `documentSearch` at `@edit-ac/web/modules` already implement a bounded logical ordinary-text index and controls. | RCH-1.21: literal captured scope, stale/cancel/limit behavior and atomic Replace All. No admitted search/replacement profile for module payloads or table cells; do not flatten them. |
| Formatting | Rust `FormatCommand`, `ExtensionTransferRegistry` at `@edit-ac/core/extensions`, and `mathAtom` at `@edit-ac/web/math` remain owners. `mathAtom` is defined in `math-definition.ts` and re-exported by `math.ts`. | RCH-1.23: declared cell/block palette, rich transfer/history and caption/reference/math preservation; unsupported content remains inert. |

RCH-1.19 owns portable presenter records and downstream handoff; RCH-1.20 owns full
rich-content workload/performance qualification. Neither is closed by this map.
No shared Session, review, transfer, storage, schema or ABI contract changes here.

## Optional dependency boundaries

- Syntect 5.3.0 with the pure Rust regex backend and two-face 0.5.2 live in the
  independent `editac-highlighting` companion, as recorded in the
  [backend decision](../decisions/highlighting-backend.md). The engine does not
  depend on that runtime. Workers/grammars are optional; immediate plain editing
  must remain usable without them. The historical probe receipt cited by that
  decision is not authenticated by this task.
- Rust owns table/format commands; browser geometry, clipboard, tokens, menus,
  media and pointer state are derived. They never introduce another replica.
- Host asset ports own authorization, storage/upload, encryption policy, decoding
  policy and binary collection. `AssetSession` is the existing browser durable
  binding, not a second lifecycle. Release-reference does not delete a global blob.
- Host link/reference resolvers own disclosure, permission and egress policy.
  Embed activation requires explicit host-approved templates. Local slash, search
  and reorder need no network service; automated service checks use prepared data.
- KaTeX 0.19.0 remains a separately loaded math renderer. The minimal modules
  entry must not eagerly import it or its renderer.

## Platform handoff

Portable semantic and presenter contracts feed the existing extension roadmaps:
[31 iOS](../roadmaps/31-ios-extension-integration.md),
[32 Android](../roadmaps/32-android-extension-integration.md),
[33 macOS](../roadmaps/33-macos-extension-integration.md),
[34 Windows](../roadmaps/34-windows-extension-integration.md),
[35 Linux](../roadmaps/35-linux-extension-integration.md), and
[36 terminal](../roadmaps/36-terminal-extension-integration.md).
Native/TUI wiring is assigned there, not a prerequisite for this browser map.
Device/input/accessibility observations remain with final roadmap43 under the
[verification policy](../specs/verification.md).

## Current cache recovery — RCH-1.3

The existing optional `editac-highlighting::cache` implementation is verified for
revisioned, per-block derived appearance. Exact input keys include source,
revision, language, enabled state and grammar/query/theme identities; unrelated
blocks reuse snapshots. The named incremental test covers multiline Unicode,
undo/redo, stale and foreign-session rejection, UTF-16 validation, cancellation
and bounded retention. Its ten cases pass on Rust 1.97.1 / macOS arm64.

The existing isolated engine consumer also passes: five projections across warm
reuse, edit, undo and redo leave checkpoint bytes and history counts unchanged.
No cache/backend/engine code or public contract needed repair. RCH-1.2's twelve
relevant backend/grammar/build pins still match; its recorded production-Wasm
observations are unchanged. This cache check does not qualify browser scheduling,
rendering, native consumers or final workload/size limits; those original owners
remain open. The map above retains original task ownership for navigation.

Exact commands, source/fixture hashes, work counts, direct logs and the initial
shell-PATH launch failures are recorded in the ignored recovery progress and its
`evidence/RCH-1.3-delivery.json`. No formal Runner check receipt is claimed.

## Current browser scheduler recovery — RCH-1.4

The existing `HighlightScheduler` and explicit module worker need no source
repair. Lazy initialization, immutable inputs, latest-per-block coalescing,
bounded queues, stale/foreign-result rejection, timeout source fallback and
owned disposal pass the named 13-case check with zero failures or skips on
Node 24.19.0, npm 11.17.0 and macOS arm64. The required workspace build passes.

The real Chromium 156 worker runs the pinned production WASM for Rust,
TypeScript and JSON, rejects 48 superseded churn requests, handles unsupported
language/grammar and terminates both normal and hung workers. All owned requests,
timers and workers are cleared. Startup, transfer, work and application callback
observations are recorded separately. These are focused correctness/diagnostic
observations, not DOM/input performance, IME, final workload or size qualification.
RCH-1.5 and downstream qualification retain their original acceptance.

The four backend artifacts and twelve relevant prerequisite source pins match
RCH-1.2/1.3. Exact hashes, commands, counts, raw browser observations, launch
correction and cleanup are in the ignored progress and
`evidence/RCH-1.4-delivery.json`; no formal Runner receipt is claimed.

## Current code presenter recovery — RCH-1.5

The existing presenter applies validated CSS Custom Highlight ranges without
replacing canonical text nodes. Renderer hold/resume defers composing subtrees;
language and loading/fallback states remain explicit. No production repair was
needed. The named browser suite passes eleven cases each in Chromium 156,
Firefox 157 and Playwright WebKit 27.2 on pinned Node 24.19.0. Strengthened remote
selection assertions and a new nonempty Unicode composition case pass separately
in all three engines. Effective current coverage is twelve cases per engine;
unchanged cases retain their original proof rather than being rerun.

The checks exercise immediate trusted typing, backward Unicode selection,
remote/language/theme churn, native subtree preservation, composition commit and
caret, readonly/unknown-language/plain fallbacks, and owned teardown. Recoloring
preserves checkpoint/history and unrelated DOM identity; composition creates one
undo group. The focused web production build passes and reproduces every tested
package asset byte-for-byte. All checks have zero failures or skips. Source pins,
commands, counts, browser artifacts and cleanup are in the ignored progress and
`evidence/RCH-1.5-delivery.json`; these are direct results, not Runner receipts.
Prepared composition events do not qualify OS IME. Case durations and screenshots
are diagnostics; full workload, performance/size caps and native platform gates
remain with downstream original owners.

## Historical evidence limits

The [prerequisite provenance fixture](../../core/fixtures/rich-content/prerequisites.json)
retains roadmap05/07/12/13/21 receipt paths, hashes, commands and original reported
counts. At recovery on 2026-10-28 those receipts and their logs were unavailable.
They supply ownership history only; no current passing proof is reused. In
particular, the recorded EXT-1.13 formatting limitation stays with RCH-1.23.
This mapping does not recreate removed generated logs or certify an upstream
platform. Current executed checks, exact input pins and the preserved initial
entry-check failures belong in the separate ignored runner evidence/progress.

## Production Code facade admission — WCU-1.1

`Code.configure()` now admits the existing managed syntax presenter through the
production facade. It is presentation-lazy: plain input never awaits assets.
Per-surface resource activation reports readiness/failure/cancellation, honors
disabled configuration even on explicit load, and disposes pending/late work.
No parser, renderer, registry, document format, code-command or pair behavior
was added. Code alone is qualified in the portable descriptor/fixture; Pairs
and code-tools remain pending.

Current affected checks: 30 contract, 8 portable profile, and 30 packed loading
cases pass with zero final failures/skips. Loading covers three named browser
engines and direct/bundled hosts, production admission with fixture override
false/absent, Rust/Unicode backward selection, unchanged document, disabled
requests/graph, sibling isolation, failed-asset editable fallback and cancellation.
RCH-1.5 implementation/artifact pins match; the only changed evidence-file
hash is this appended delivery note, with the original RCH bytes preserved.
Its source/IME/remote/history observations remain scoped and reusable. OS IME, full workloads, hard caps, comprehensive
lifecycle and the complete expanded consumer remain with downstream owners.
Historical compilation/launch and repaired fixture failures are preserved in
WCU-1.1 delivery evidence; none is counted as a current pass.

Detailed commands, source/package/runtime pins, counts, repairs and cleanup:
`.roadmap-runner/wasm-extensions-recovery-20261028/.roadmap-runner/02-code-facade-admission-d9439c68656e/evidence/WCU-1.1-delivery.json`
from the workspace root. This is source-bound admission, not publication or
expanded-consumer qualification. WEX-2.2 consumes this result.

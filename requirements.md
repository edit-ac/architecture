# Requirement review and delivery mapping

Reviewed against the current docs on 2026-10-12. “Covered” below means planned contract/tasks, not shipped functionality. The existing scaffold does not establish editor behavior. The user's native desktop clarification includes macOS, Windows and Linux.

| Requirement | Existing coverage | Adjustment and delivery gate |
|---|---|---|
| First-class local-first/offline collaborative editing | 02 engine, 03 journal/recovery, 06 reconnect/receipts, 11 hosted CLI | 12 adds portable sessions, native stores, local channels, source catalog and offline policy; 20 verifies actual multi-client scenarios |
| Markdown/literal file editing and hosted CLI | Expanded 11 uses external editor; FMT-1.12 reconciles source | Preserve this work; 15 adds built-in TUI, ac:// routing, dirty-buffer conflicts and deterministic terminal qualification |
| Agent Markdown editing/uploads through embedding app MCP | Portable source reconciliation, commands/anchors and host auth responsibilities | 12 adds shared revision/policy/operation service; 14 adds host-tool schemas, prepare/diff/apply, durable retries and realtime observation; CLI MCP stays optional |
| Exact Git-like diffs and tracking | CRDT update/patch metadata only; no review/history API | 13 adds immutable representation-specific revisions, exact patches, semantic changes, review UI and restore-as-new-edit; native/TUI presenters consume it |
| PM ticket web/mobile/desktop embedding | Framework-independent browser preset, first-party React/Astro integrations, native probes | SDK-1.7 adds Astro; SDK-1.4/1.6 qualify and document both framework consumers. 16/17/18/22/23 deliver real native editors; 20 qualifies the same mandatory ticket capabilities across all five native OS targets and web |
| Framework integrations as a product adoption channel | Shared Rust/WASM engine and imperative web SDK | React and Astro are committed first-party bindings; future frameworks reuse the optional adapter boundary with their own compatibility, lifecycle, packed-consumer and quickstart evidence. Astro 7's Rust compiler direction aligns with edit.ac's Rust-first positioning; no compatibility or performance claim follows without qualification |
| Collaborative cross-platform documents | Browser/Rust fixtures; native future scope | Shared session/update profile and every actual client participate in 20 offline/crash/reconnect/composition tests |
| Native iOS/Android with same capabilities | 09 probes only | 16/17 deliver complete adapters, typed bindings, storage/sync, mandatory module UI and packaged consumers; actual device evidence closes in 20 |
| Native macOS/Windows/Linux | Not previously planned | Independent 18/22/23 platform tracks with toolkit feasibility, real native controls, bindings, package consumers and qualified support matrix |
| Readonly, undo/redo, custom references/extensions | Engine history and browser modules | Enforce readonly in shared mutation admission including MCP; qualify native/terminal histories and host-authorized reference hooks in every client |
| First-class extension library and thin core | Built-in browser modules and descriptors | 21 publishes coherent portable contracts, conformance harness, adapter hooks and third-party recipes; keep UI/network/MCP/crypto out of the semantic core |
| Optional encryption/private documents | Baseline safe import/auth only | 19 builds explicit local/E2EE profiles after threat-model/protocol selection; 24 gates real key providers, protected scenarios and independent review |

## Corrections to the proposed statements

- **Offline-first** includes cached/new local documents, supported crash recovery and explicit pending/rejected uploads. It cannot make uncached remote data available, prevent browser eviction, or erase a revoked user's already-held plaintext.
- **CLI/TUI collaboration** uses the same identity and command/recovery contracts. URLs resolve through configured hosts/catalogs; ordinary web pages and hash-looking strings do not confer edit authority.
- **MCP readiness** is a reusable host-app integration. Annotation hints are insufficient for permissions/idempotency; a Markdown candidate upload is revision-checked input to shared reconciliation, not a stale whole-document replacement.
- **Exact diff** names exact source bytes or a declared normalized projection and provides a separate semantic view. A Yjs state vector alone is not an exact revision token, and CRDT update bytes are not a review diff.
- **Native parity** needs actual editing/IME/accessibility/module evidence. Bindings and data-preserving fallbacks do not alone satisfy same-capability claims.
- **Encrypted mode** needs key/membership/rotation/recovery and a declared agent plaintext endpoint. An opaque relay cannot simultaneously decrypt Markdown or provide plaintext search/diffs.

## Why the planned core can support this

One portable authoritative replica, stable node identities/anchors, validated commands, origin-aware history, incremental patches and shared format reconciliation are the right prerequisites. New companion modules provide session/identity, revision/diff and optional security functions; presenters and MCP remain adapters. This is architectural compatibility by design, not proof that the future implementation meets every requirement.

The follow-up entry gates check the implemented schema/ABI and require a migration/compatibility decision if evidence contradicts the plan. The active foundation source/IDs remain untouched. Existing CLI amendments are preserved. See [decision 002](decisions/002-full-delivery.md), [scenario contract](specs/delivery-scenarios.md) and [primary-source implementation research](evidence/followup-research.md).

## Extension and ecosystem review — 2026-10-11

The user clarified that PDF is **export-only**. PDF import, OCR and PDF-reader dependencies are outside this plan. New format directions have explicit fidelity tiers; no “all document formats are lossless” promise is made.

| Requested addition | Existing baseline | Added delivery |
|---|---|---|
| Code blocks with fast syntax highlighting | Literal code/Markdown fences; no highlighting implementation track |25 portable optional highlighter/worker and performance fixtures;31–36 actual client wiring |
| Fast table formatting | Bounded rectangular table module |25 stable structural editing, cached layout, explicit Markdown formatter and stress/interactive envelopes |
| Images, attachments and embeds | Image metadata/host upload hook |25 staged blob lifecycle, bounded media, safe embed presenters;28 host asset service |
| Broad document interchange | Markdown, safe HTML and semantic JSON |27 DOCX/ODT/RTF/EPUB/CSV/TSV directions plus PDF export;31–36 client actions |
| Slash menu |07 local accessible menu |25 query lifecycle/large command catalog and no remote-open behavior; client integration gates |
| Drag/drop block editing |07 shared semantic move, keyboard/optional handle |25 pointer/touch/autoscroll/cancel and non-drag pointer alternative; native wiring |
| Customizable references |07/21 resolver and descriptor contract |26 typed host API, stable identity, caching, permission/cancellation, UI customization and documentation |
| Automatic URL title/favicon display | URL validation only |26 policy-enabled local-paste pipeline, safe metadata fetching and per-viewer display |
| Private/internal links | Host authority principle |26 principal-scoped API/cache, activation authorization, indistinguishable denial and no public-fetch fallback |
| Professional public docs repository | Architecture/internal specs plus planned API docs |Created public docs source repository;29 site generation, executable guides, versioning/search/accessibility and publication |
| Public demo | SDK consumer fixtures only |29 actual packaged-editor playground, local-first/multi-view scenarios, deployed URL verification and rollback |
| Cloud document-store readiness |06 test relay and12 store/transport ports |28 durable reference host with reusable storage adapters, tenant auth, asset finalization, recovery and deployment evidence |
| Maintainable ecosystem | Thin core and portable module model |30 executable layer, compatibility, capability, optional-loading, dependency and diagnostics gates;37 expanded qualification |

The baseline browser profile remains independently deliverable. Roadmaps31–35 preserve independent native implementation. Roadmap36 covers terminal representations without claiming graphical embed parity. Optional encrypted profile24 is extended to protect the new assets, converters, resolvers and cloud integration. Documentation site/demo publication and production cloud-provider qualification remain future tasks; a clean source repository is not evidence of a live editor deployment.

## Everyday editing and assistive technology

The October 11 interaction request is captured in [editor interactions](specs/editor-interactions.md), [targeted cases](tests/editor-interaction-cases.md), [research](evidence/editor-interaction-research.md) and [assistive input](specs/assistive-input.md). Coverage below means planned work; current browser packages are scaffolds.

| Requirement | Owner | Qualification |
|---|---|---|
| Enter/new blocks, Shift+Enter/same block, contextual code/list/table behavior | WEB-1.8; INT-1.2 | Semantic/caret snapshots, next typed character, storage/Markdown and undo |
| Selection formatting, toolbar focus, pending marks and alternate styles | INT-1.3 | Forward/backward/mixed/collapsed selections, explicit unsupported-format preservation |
| Backspace/Delete, graphemes, whitespace and special characters | INT-1.4, INT-1.8 | Unicode vectors, exact code points, boundary no-ops, valid UTF-16 and source recovery |
| Tab, Shift+arrows, cursor placement and platform keyboard controls | INT-1.5, INT-1.6 | Visual navigation, context focus escape, non-US layouts and native/AT shortcuts |
| IME, dictation, autocorrection, virtual keyboards and replacement | INT-1.7, INT-1.14 | Exactly-once deterministic traces plus actual OS/device observations |
| Slash-menu trigger, keyboard/pointer/AT controls and async results | MOD-1.4; INT-1.9; RCH-1.16 for scale | Stable query target, composition priority, focus retention, enabled results and undo |
| Paste flavors, literal mode, rich HTML, Markdown and parsing | INT-1.10, INT-1.11 | Pinned grammar, synthetic external-app payloads, safe atomic fallback and exact whitespace |
| History/races/read-only and accessibility baseline | INT-1.12–INT-1.14 | Zero-mutation rejection, independent remote history, real screen-reader/voice-control checks |
| Optional dictation/assistance extension and native integrations | AIN-1.1–AIN-1.11 | Shared descriptor, mocked lifecycle, independently gated native/TUI presenters and actual device evidence |

Track 38 is a prerequisite of browser release track 10; track 39 gates expanded ecosystem qualification 37. Basic accessible editing and OS dictation are baseline obligations, not optional-extension features. The catalog is a minimum regression set to grow with observed failures, not a promise to enumerate every possible browser/OS edge case.

## Browser delivery size — 2026-10-13

The user-approved [gzip bundle budgets](specs/verification.md#browser-bundle-size-budgets) replace the proposal's Brotli bundle targets. The default Task preset has a 512 KB total hard cap and 256 KB preferred size; editor JavaScript has a separate 32 KB hard cap and 16 KB preferred size. KB = 1,000 bytes. Required WASM glue, runtime dependencies and lazy required code count. SDK-1.8 owns implementation to get below both caps and the executable measurement/enforcement harness before comparison baselines; REL-1.2/1.3, EXT-1.9 and FIT-1.6 reuse it. Either hard-cap overrun or missing required measurements block release qualification, while preferred-size misses remain explicit optimization work. Mobile additions fit inside these caps.

## Touch devices and mobile web platforms

The mobile-web follow-up is captured in [mobile web](specs/mobile-web.md), [baseline tests](tests/mobile-web-cases.md), [extension tests](tests/mobile-extension-cases.md) and primary-source [platform](evidence/mobile-web-platform-research.md)/[touch](evidence/touch-extension-research.md) research. This is planned implementation/qualification, not a current capability claim.

| Requirement | Owner | Acceptance boundary |
|---|---|---|
| Native touch selection, long-press/context menu, scroll/zoom, stylus and mixed pointers | MWB-1.2 | Preserve OS editing, scoped gestures, cancellation, tap alternatives and accessible targets |
| Mobile typing, correction, swipe/handwriting, IME, repeated deletion and hardware keyboard changes | MWB-1.3 | Existing semantic/event contracts, exactly-once input and actual device observations |
| Keyboard occlusion, safe areas, viewport resize/zoom, rotation, split screens and embedding | MWB-1.4 | Observed geometry, stable selection/focus, bounded shared scheduling and fallback |
| Mobile command access and keyboard/browser API support | MWB-1.5, MWB-1.7 | Reachable controls without modifier keys; optional VirtualKeyboard/layout/lock and experimental EditContext with fallback |
| Mobile clipboard, picker/share blur, lifecycle/BFCache and recovery | MWB-1.6 | Stable targets, harmless cancellation, no duplicate callbacks or false unload durability |
| Small baseline core and bounded optional overhead | MWB-1.1, MWB-1.9; MWX-1.1, MWX-1.8 | No browser policy in Rust; frozen incremental/total budgets, lazy optional loading and measured lifecycle resources |
| Baseline modules on touch devices | MWB-1.8 | Native interaction preservation and visible command routes, even without enhanced presenters |
| Rich menus/references, code/tables, drag/resize, assets/embeds, conversion and assistive controls | MWX-1.2–MWX-1.7 | Feature-specific mobile edge cases through existing commands and host capabilities |
| Actual mobile web/platform support claims | MWB-1.10/1.11; MWX-1.8 | Mechanics separate from iPhone/iPad/Android device, keyboard, browser-mode and AT receipts |

Track 40 gates browser release 10 without requiring rich extensions or native SDKs. Track 41 gates expanded qualification 37; web assistance prerequisites are task-specific. Optional API absence is a tested fallback condition, not permission to drop required editing/accessibility behavior.

## Regression prevention and test-suite construction

[Round-two research](evidence/editor-regressions-round2.md) and [testing methods](evidence/editor-testsuite-methods.md) feed the [suite contract](specs/editing-regression-suite.md), [additional cases](tests/editor-regression-cases.md) and [machine-readable manifest](tests/editing-suite/suite.json). Coverage is specified for 272 cases; execution remains independently tracked.

| Requirement | Owner | Proof required |
|---|---|---|
| Consistent real-engine fixtures and selection/effect oracles | RGS-1.1/1.2 | Qualified logical-ID mapping, independently authored states, atomic text/mark/structure behavior |
| Undo grouping, transaction-entry selection and remote/rebase history | RGS-1.3 | Fixed-clock sequences including single-character paste/cut and mapped bookmarks |
| Exactly-once input, IME ownership and renderer echo suppression | WEB-1.13, RGS-1.4 | Pre-routing real-DOM/engine ADR qualification, then shared-driver production-adapter integration; correlated traces followed by deliberate identical edits; actual OS evidence stays separate |
| Normalization, Unicode and operation/interleaving invariants | RGS-1.5 | Version-pinned vectors, bounded seeds, convergence/fixed-point checks and minimized failures |
| Callback/async failure and disposal safety | RGS-1.6 | Fault injection at real ports, committed-state preservation and no late/refocused mutation |
| Custom views, widgets and nested clipboard/drop ownership | RGS-1.7 | Base then combined browser cases; exact identity/selection and one intended edit |
| Falsifiable coverage and CI qualification | RGS-1.8 | Negative controls, real assertion counts and matching revisions; no metadata-only passes |

Track 42 precedes 38, and thus the mobile/extension qualification tracks, without changing the native/browser ownership model. Engine compound-operation, selection-result, history and callback gaps are explicit prerequisites; sequential commits followed by repair/undo are not accepted as atomic editing.


## Desktop conventions, first-party configurations and deeper native coverage

Research on Word/Pages/LibreOffice and IDE conventions extends existing tracks, with no new roadmap. [The additional catalog](tests/desktop-editing-cases.md) supplies 77 planned cases; [desktop](evidence/desktop-editing-research.md), [native](evidence/native-editing-research.md) and [performance/extension](evidence/editing-performance-extension-research.md) evidence distinguishes product decisions from source precedent. Selected Enter was already BRK-04; deeper variants add explicit independently authored recipes, not a duplicate feature claim.

| Requirement | Existing track owners | Required evidence |
|---|---|---|
| Pointer selection, replacement boundaries and context targets | INT-1.2, INT-1.15 | SEL cases; forward/backward and whole-document replacement, autoscroll and platform granularity |
| Actual selected-text move/copy | INT-1.16, INT-1.17 | MOV/XFR source-destination/history snapshots, modifiers, self-drop, failure/cancel/remote and cross-document receipts |
| Native command/replacement surfaces | INT-1.18; platform SDK input/command tasks | CMD/NAT focused responder, provided-range replacement and real OS observations |
| Optional first-party search and code conveniences | RCH-1.21, RCH-1.22; native/mobile/terminal feature consumers | FND/IDE bounded operations, stable scope, undo and explicit unsupported capabilities |
| Table clear versus structural delete | RCH-1.6, RCH-1.8 | TBL semantic selection and atomic dimension/protection cases |
| Stable official configurations | EXT-1.12, EXT-1.5; RCH-1.20 | FPX presets, precedence, compatibility, actual high-risk combinations and resource failure tests |
| Platform protocol precision | IOS/AND/DSK/WIN/LNX selection/input/clipboard/accessibility and qualification tasks | NAT API-specific units, composition, services, provider lifetimes and device receipts |
| Responsive mixed-feature editing | FIT-1.8, RCH-1.20, MWB-1.9, MWX-1.8 | PRF comparable input-to-visible, continuous frame, memory, loading and native traces under existing budgets |

Those desktop additions preserved the previous 42 roadmaps and 512 bounded parents. The AI extension and editor migration/comparison/docs-example additions expanded the plan to 42 roadmaps and 550 parents. Subsequent bounded additions, including browser-size optimization SDK-1.8, bring the current validated total to 556 parents. Runtime bindings and device/performance results remain separate. An unlimited promise of every possible behavior or universal best performance cannot be established by a finite catalog; required boundary combinations, explicit supported profiles, minimized new regressions and measured release gates govern delivery.


## AI Extensions

The October 12 request adds [the AI contract](specs/ai-extensions.md) and [the AI epic in roadmap 25](roadmaps/25-rich-content-extensions.md#epic-rch-2--deliver-optional-ai-writing-through-existing-edit-contracts). Existing assistive input (39), host MCP edits (14) and change review (13) supply reusable boundaries but did not explicitly include these AI writing features. Coverage means planned delivery, not implementation or model quality.

| Requirement | Delivery owner | Acceptance boundary |
|---|---|---|
| Autocomplete while writing | RCH-2.4 | Opt-in debounced ghost text, explicit acceptance, IME/selection protection, stale invalidation and hard request limits |
| Ask AI, fill text and continue writing | RCH-2.3 | Explicit instruction/context; answer-only mode or reviewed captured-target insertion/replacement |
| Related Tiptap-style writing actions | RCH-2.5 | Spelling/grammar, rephrase, simplify, shorten/extend, tone, summarize/key points and target-language translation |
| Optional portable transport and safe review | RCH-2.1/2.2 | Default Vercel AI SDK Core backend behind a portable transport; host credentials/permissions/quotas, bounded streams, existing anchors/diffs/history and no late mutation |
| First-party profile and independent clients | RCH-2.6–RCH-2.14 | Packed web profile, independent native/TUI presenters, honest platform matrix and mock-backed documentation |

[Additional suggestions](evidence/ai-extension-research.md#additional-first-party-candidates) remain a prioritization list, not new commitments. This optional extension does not gate baseline browser delivery, install a provider or authorize paid testing/dogfood.

## Editor migration and comparison documentation — 2026-10-12

The user requested editor-specific content migration examples and a public feature/benchmark comparison section. These are documentation delivery requirements, not new converter compatibility or performance claims.

| Requirement | Track owners | Required evidence |
|---|---|---|
| Migration overview, fixtures and safe cutover | DOC-1.15; SDK-1.5 for scoped Tiptap conversion | Versioned exports/schema, independent expected semantics, diagnostics, asset/metadata mappings, interrupted batch recovery and new collaboration epoch/session |
| Tiptap, ProseMirror, Lexical, Slate/Plate, Quill, Draft.js, Editor.js, BlockNote, CKEditor 4/5 and TinyMCE guides | DOC-1.16–1.26 | One guide per source-editor boundary, pinned native export fixtures, explicit fidelity/custom-content limits; immutable target consumer evidence before executable conversion claims |
| HTML, Markdown and plain text for other editors | DOC-1.27 | Separate route/dialect fixtures, Froala/Summernote/CodeMirror/Monaco entry points and declared losses |
| Versioned feature comparison | DOC-1.28; DOC-1.3/1.14 navigation/drift | Primary-source versions/review dates, precise support categories, edit.ac qualification profiles and links to migration guides |
| Reproducible benchmark methodology and public results | REL-1.2/1.3/1.4; DOC-1.29/1.30 | Optimized comparable profiles, cold/warm visible/edit-ready and editing/paste/storage/reconnect metrics, bytes/memory, raw samples/counts, meaningful percentiles, regressions/failures and immutable artifact provenance |

Documentation bootstrap and source-export examples may proceed before converters qualify. Actual target conversion and measured result acceptance require their own evidence; absent measurements remain Not yet measured, insufficient samples remain Inconclusive and design targets never become results. The existing core benchmark harness remains the sole measurement owner; these additions neither start a runner nor authorize paid inference or public deployment.

## Tiptap-informed docs structure and concrete examples — 2026-10-12

Extend the existing docs track with original edit.ac material using Tiptap's Getting started, Core concepts, Extensions, API, Guides and Examples organization as a reader reference. Preserve the existing Migrate/Compare sections and site implementation; no Tiptap API/plugin/schema compatibility follows from this structure. The canonical section/example matrix is in [public docs](specs/public-docs-demo.md#reader-structure-and-concrete-examples).

| Requirement | Task owners | Concrete evidence |
|---|---|---|
| Section navigation, page templates and executable getting started | DOC-1.3/1.4/1.5 | Canonical Zola sections, version/status/prerequisite fields, minimal browser/React/Astro create-edit-save-read-only-dispose consumers and checked snippet source ranges |
| Core concepts and command/event references | DOC-1.31/1.32/1.33 | Project kickoff fixture, semantic tree/transcripts, formatting/split/join/history snapshots and subscription/commit/cleanup timelines |
| Extension catalog and custom extension tutorials | DOC-1.34/1.35 | Versioned descriptor/options/profiles; callout block, highlight mark and local command/menu examples with interchange, unknown-data and presenter limits |
| Complete example gallery and task recipes | DOC-1.36/1.37; existing DOC-1.6/1.7/1.8/1.9–1.11 consumers | Ticket, collaborative note and structured report source/downloads; accessible toolbar, Markdown paste, save/reconnect, import/upload/link failure and cancellation outcomes |
| Troubleshooting and release drift | DOC-1.38/1.12/1.14 | Deterministic diagnostic/recovery fixtures, data preservation, accessibility/search/mobile checks and examples/manifest.json drift gates |

Documentation source and explicitly conceptual examples can proceed before packages qualify. Concrete executable examples must consume exact immutable artifact/profile evidence, independent expected outcomes and prepared local/provider transports; this work does not authorize paid inference, new editor features or deployment.

## Clipboard format and device follow-up ownership

| Requirement | Future task owners | Acceptance evidence |
|---|---|---|
| Full supported clipboard palette and optional plain paste | FMT-1.13; WEB-1.9 | Internal/Markdown/HTML/plain precedence, declared host policy, literal shortcuts/control, one undo group and safe fallback |
| Native simulator/emulator and OS-host clipboard mechanics | IOS/AND/DSK/WIN/LNX-2.4 | NCL-01–NCL-20 with explicit virtual versus physical provenance; no native runs in this roadmap revision |
| Native physical mobile and desktop clipboard | DEL-1.9/DEL-1.10 | NCL-01–NCL-28 with real-device/OS/menu/provider/privacy/accessibility artifacts |
| Table and other extension formatting preservation | EXT-1.13; RCH-1.23; NIX/NAX/NMX/NWX/NLX-1.9; MWX-1.9 | Formatted cells, captions and inline/block extension codec round-trips, accessible commands, literal bypass and source-preserving absence |

## Content migration sequencing — 2026-10-13

The user deferred editor-content migrations and migration guides until full app completion and qualification. SDK-1.5 and DOC-1.15–1.27 are preserved in [the deferred migration backlog](operations/deferred-content-migrations.md), outside active SDK/docs runners. Earlier migration requirement mappings describe retained future scope, not current delivery gates. SDK integration/recovery examples and comparison documentation proceed without migration dependencies. No migration implementation or qualification is claimed by this deferral.

# Text and block editing standards review

Review date: 2026-10-24. Scope: architecture, current source and implementation planning; no runtime conformance or compilation result is claimed by this review.

## Provenance and method

The requested starting point is [Szövegszerkesztő kutatás](chatgpt-conversation://6add1b3b-88dc-83ed-97b6-ea5334fffe1d). Its three available exchanges cover editor feature specifications, lower-level standards and Notion-like block semantics. The conversation reader returned all three exchanges, but capped two long assistant messages at 20,000 characters. The linked Library report was not returned as an attachment. This review therefore does **not** claim to have inspected its reported 29 pages, 90 source groups or all acceptance fixtures. It aggregates the retrieved material, independently checks relevant primary references, and inspects our code and existing authorities.

Code evidence below describes the current, substantially dirty sibling checkouts. It includes work already being delivered by the existing runner. Paths and symbols are the durable locators; line references are inspection aids and may move. Source presence, a checked roadmap parent, and a passing current-runtime receipt are different evidence levels. Codanna was unavailable in the tool inventory and local command lookup; bounded text searches and targeted reads were used instead. No editor test, provider call, build, runner start or queue mutation formed part of this review.

The resulting [behavior supplement](../specs/editing-behavior-standards.md) records our selected profile. The [planned delivery queue](../runner-queues/editing-standards-20261024/README.md) closes only residual gaps and preserves existing task ownership.

## What counts as a standard

There is no single specification for the complete experience of a rich text or block editor. Distinguish four kinds of evidence:

| Kind | Examples | How edit.ac uses it |
| --- | --- | --- |
| Normative algorithms and interfaces | Unicode annexes, encoding rules, browser and native interfaces | Specify coordinate systems, admissible input and adapter obligations. A draft is not a browser-support promise. |
| Accessibility requirements and patterns | WCAG, ATAG, ARIA APG | Specify operable authoring, accessible content and control focus behavior; declare actual tested scope separately. |
| Established product conventions | Writer, CKEditor, Lexical, Notion | Compare outcomes and identify missing decisions. A vendor shortcut or data structure is not a universal requirement. |
| Our product decisions | Paragraph Tab indentation, link-end insertion, supported schema, source-mode TUI | Keep explicit, discoverable and consistent with the existing architecture. Document intentional differences. |

The implementation role matters: Rust owns content and semantic transactions; browser/native adapters own input sessions and visual layout; hosts own application-level navigation and external data. “Conforms to Unicode/WCAG/Notion” is too broad to be a useful capability claim.

## Primary-source baseline

References were checked on the review date. Versions below describe the retrieved specifications, **not** the Unicode tables or capabilities deployed by our dependencies and operating systems.

| Area | Primary source and inspected status | Relevant conclusion |
| --- | --- | --- |
| Text boundaries | [UAX #29, revision 49 / Unicode 18](https://www.unicode.org/reports/tr29/tr29-49.html) | Grapheme, word and sentence boundaries are distinct; tailoring and editing policy must be declared. |
| Deployed segmentation | [unicode-segmentation 1.12.0 generated tables](https://docs.rs/unicode-segmentation/1.12.0/src/unicode_segmentation/tables.rs.html) | The pinned crate's `UNICODE_VERSION` declares 16.0.0, also verified in its installed source. A reference to Unicode 18 does not upgrade our implementation. |
| Normalization | [UAX #15, revision 58](https://www.unicode.org/reports/tr15/tr15-58.html) | Normalization can change sequences and coordinates. Preserve source text under our existing policy. |
| Bidi and wrapping | [UAX #9, revision 52](https://www.unicode.org/reports/tr9/tr9-52.html), [UAX #14, revision 57](https://www.unicode.org/reports/tr14/tr14-57.html) | Logical order, display order and line-break opportunities are separate. Native layout remains authoritative for visual movement. |
| Encoding | [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629), [WHATWG Encoding](https://encoding.spec.whatwg.org/) (Living Standard) | Explicit decoding and malformed-input policy are required at each boundary. |
| Browser selection | [Selection API](https://www.w3.org/TR/2026/WD-selection-api-20260611/) (Working Draft) | Preserve anchor/focus and direction; browser ranges do not replace semantic anchors. |
| Editing intentions | [Input Events Level 2](https://www.w3.org/TR/2026/WD-input-events-2-20261015/) (Working Draft) | Use input intentions and replacement targets, including paths without keyboard events. |
| Event lifecycle | [UI Events](https://www.w3.org/TR/2026/WD-uievents-20260221/) (Working Draft) | Composition lifecycle and observed event order require adapter-specific handling. |
| Keyboard meaning | [key values](https://www.w3.org/TR/2025/REC-uievents-key-20250422/), [code values](https://www.w3.org/TR/2025/REC-uievents-code-20250422/) (Recommendations) | Semantic keys and physical keys are different; text entry must not assume a US layout. |
| Transfer | [Clipboard API](https://www.w3.org/TR/2026/WD-clipboard-apis-20260624/) (Working Draft) | Native representations and event access are adapter mechanisms, not permission to trust incoming fragments. |
| Accessible authoring | [ATAG 2.0](https://www.w3.org/TR/ATAG20/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendations) | Both operating the authoring tool and preserving accessible content need acceptance. |
| Toolbar focus | [ARIA APG toolbar pattern](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/) | Keep document selection while control focus moves; support keyboard entry, movement and exit. |
| macOS input | [NSTextInputClient](https://developer.apple.com/documentation/appkit/nstextinputclient) | Marked text, replacement and geometry belong at the native input boundary. The web reader exposed only the JavaScript/Markdown landing page; protocol behavior is corroborated by our native adapter, not a claimed full API-page read. |
| Android input | [InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection) | Distinguish surrounding-text units, composition and batch input. |
| Windows input | [ITextStoreACP](https://learn.microsoft.com/en-us/windows/win32/api/textstor/nn-textstor-itextstoreacp) | Text-store access, selection and notifications are platform obligations. |
| Linux input | [Gtk.IMContext](https://docs.gtk.org/gtk4/class.IMContext.html) | Preedit/commit and surrounding text require an adapter; native index units are not interchangeable. |
| Undo conventions | [Lexical History](https://lexical.dev/docs/concepts/history) | Typing/deletion coalescing, selection/focus changes and composition boundaries need deliberate grouping choices. Retain our shared history. |
| Selective history | [Yjs UndoManager](https://docs.yjs.dev/api/undo-manager) | Origin scoping and selection metadata are useful reference concepts; do not introduce a second undo manager beside Rust. |
| List behavior | [CKEditor list editing](https://ckeditor.com/docs/ckeditor5/latest/features/lists/lists-editing.html) | Nesting, Enter and adjacent-list behavior must be explicit, including differences from our current list model. |
| Link insertion state | [CKEditor typing around links](https://ckeditor.com/docs/ckeditor5/latest/features/link.html#typing-around-links) | The same visible boundary can mean typing inside or outside a link. Our outside-at-end policy already chooses a different default. |
| Schema and selections | [ProseMirror guide](https://prosemirror.net/docs/guide/) | Document, selection and pending marks are distinct state; transactions carry their changes. Direct fetch failed, but primary-site indexed excerpts supplied the relevant sections. |
| Structural constraints | [Slate normalization](https://docs.slatejs.org/concepts/11-normalizing), [Quill Delta design](https://v2.quilljs.com/docs/guides/designing-the-delta-format) | Useful examples of explicit invariants and canonical representations, not replacement models for edit.ac. |
| Block conventions | [Notion keyboard shortcuts](https://www.notion.com/help/keyboard-shortcuts), [Notion block objects](https://developers.notion.com/reference/block) | Addressable blocks, type/parent/children and block operations add a product layer above text. Selection and action semantics matter more than copying menu labels. |
| Broad workflow inventory | [Writer 26.2 text basics](https://books.libreoffice.org/en/WG262/WG26202-TextBasics.html), [advanced text](https://books.libreoffice.org/en/WG262/WG26203-TextAdvanced.html), [OpenOffice Writer specification archive](https://www.openoffice.org/specs/writer/index.html) | Useful completeness and specification-writing references. Pagination, academic fields and review workflows are separate capabilities. |

Two cautions change implementation planning. Input Events 2 §7 puts `compositionupdate` before the paired input events, while UI Events §3.6.6 puts `beforeinput` before `compositionupdate`. Both retrieved documents are drafts. Our qualification must use observed traces and idempotent intent handling rather than assert one universal event sequence. Also, browser `Intl.Segmenter` and native text engines can use different Unicode data from the pinned Rust helper; API availability and accepted mutation boundaries need explicit agreement.

The conversation also discusses custom shaping, EditContext, CF_HTML byte offsets, XML/ODF/OOXML, generic JSON patches, synced blocks and database views. These are useful future boundary checklists. They do not justify a new renderer, a new persistent format, an office suite importer, a JSON-patch text engine or a Notion-like application database in this task. Current [format](../specs/formats.md), [conversion](../specs/document-conversion.md), [storage](../specs/storage-sync.md) and [durability](../specs/document-durability.md) authorities retain those decisions. The conversation's claims about a particular Notion synchronization implementation were not adopted as architectural facts.

## Existing architecture already matches the foundation

| Concern | Source evidence in sibling repositories | Disposition |
| --- | --- | --- |
| UTF-16 transport and grapheme deletion | `core/crates/editac-core/src/anchors.rs` (`move_grapheme`, `deletion_range`); `commands/editor.rs` (`DeleteGraphemeAt`); `packages/web/src/input/keyboard.ts` | Keep. Do not redefine a character as a Rust `char` or one UTF-16 unit. |
| Native visual movement | `core/packages/web/src/dom/selection.ts` (`trackNativeMovement`, `#completeMovement`); `tests/browser/interactions/navigation.spec.ts` | Keep layout in the adapter; close the capability/version gap below. |
| One input owner | `core/packages/web/src/input/text.ts` and `composition.ts`; browser composition suites | Keep intent correlation, supplied targets and temporary composition. Synthetic traces do not prove actual IME support. |
| Shared history | `core/crates/editac-core/src/history.rs`; Session/FFI history result transport; `native/macos/.../commands/NativeCommands.swift` | CFC and EDX shared/macOS history parents are checked in the inspected source. Consume their current receipts; do not reassert the historical selection bug as reproduced. |
| Rich selection transfer | `core/packages/web/src/clipboard/fragment.ts` (`selectionFragment`, captured preparation/cut); `input/drag.ts` | Partial text, complete supported atoms, container paths and same-session transfer already exist. |
| Split, join and lists | `core/crates/editac-core/src/commands/blocks.rs`, `lists.rs`, `editor.rs`; `tests/lists/production.rs` | Existing prepared operations cover substantial behavior and atomic failure. Extend only demonstrated residuals. |
| Stable moves | `core/crates/editac-core/src/commands/move.rs`; `packages/web/src/modules/reorder.ts`; `tests/browser/reorder.spec.ts` | Preserve identity, structural version checks and cycle rejection; supported kinds are currently bounded. |
| Conversion and unknown data | [Block actions](../specs/block-actions.md); `tests/demo_block_actions.rs`, `tests/opaque_fragments.rs` | BTA/BTU/BTQ already own shared conversion, extension applicability, presenters and preservation proof. |
| Whitespace, normalization and shortcut policy | [Everyday editing](../specs/editor-interactions.md), [editing experience](../specs/editing-experience.md), [platform services](../specs/platform-editing-services.md) | Preserve exact authored sequences, declared literal newline conversion, semantic keys and explicit focus escape. |

## Residual gaps from the source inspection

“Not located” describes the inspected scope, not a proof that no implementation exists anywhere. The first delivery task rechecks the current source and exact receipts because an active runner may close a gap first.

| Gap | Evidence and present state | Required delta and ownership |
| --- | --- | --- |
| G01 Segmentation profile and optional browser APIs | `core/crates/editac-core/Cargo.toml:16` pins 1.12.0; `packages/web/src/dom/selection.ts:69,82` directly uses `Intl.Segmenter` and `Selection.modify`. No capability guard in that repair path. | Declare deployed version/tailoring and safely handle missing or disagreeing APIs. Reuse the engine helper; INT-1.4/1.5/1.8. |
| G02 Cross-block web composition | `packages/web/src/input/composition.ts:59–60` rejects endpoints on different owners as `unsupported-composition-range`. | Support compatible prose selections through existing prepared range operations, without committing deletion at composition start. INT-1.7. |
| G03 Cross-block macOS replacement and breaks | `native/macos/Sources/EditacMacOS/input/NativeCommittedInput.swift:55–58`, `NativeComposition.swift:190–200`, `commands/NativeCommands.swift:221–225` impose same-owner guards. | Carry compatible multi-block replacement through the existing Session boundary. Reconcile current EDX/native ownership before implementation; do not redo completed history work. |
| G04 Language/base-direction profile | Browser navigation tests set host `dir=ltr/rtl`, but no persisted paragraph-language/direction contract was located. | Specify host inheritance and native equivalents first; expose limits honestly. No browser-only persistent metadata or automatic bidi rewriting. |
| G05 TUI navigation | `cli/src/tui/input.rs:111–122` handles Ctrl+A then declines other modifiers; no word/document/page navigation branches were found. `positions.rs` intentionally uses logical source order. | Add a discoverable terminal-supported profile for word/document/page navigation without promising GUI bidi layout or stealing global TUI commands. |
| G06 Explicit block selection | `core/packages/web/src/dom/selection.ts:10,197–224` supports text ranges and one noneditable node; retained text capture excludes node mode. `anchors.rs:171` has two text endpoints. | Add ephemeral, discriminated command targets and contiguous sibling/subtree block selection. Keep semantic text anchors and persistent schema. No arbitrary discontiguous selection. |
| G07 Mixed text/object behavior precision | Fragment support already exists; the partial paragraph → atom → partial list-item command matrix is scattered across contracts. | Make availability, preservation, resulting selection and atomic refusal explicit. Reuse INT/EDX feature-boundary owners rather than add another fragment engine. |
| G08 Typed block movement | `commands/move.rs:95–110` accepts list/quote containers and paragraph/heading/code/separator; module blocks are excluded. Reorder capture also needs a text selection (`reorder.ts:254`). | Publish per-kind applicability and extend the same move command only for preservation-qualified current module content. Use block targets instead of inventing fake text offsets. |
| G09 Formatting, search and accessibility proof | Existing specs cover pending marks, link end typing, scoped Find, toolbar selection and AT focus. This review did not reproduce a new implementation defect. | Retain these as required regression/integration outcomes; add uncovered cases once in final coverage and actual platform observations in roadmap43. |
| G10 Conversion and structural collaboration | Current BTA/DRA acceptance already covers identity, advanced mappings, table concurrency and durable structure. Source/tests alone do not prove all acceptance. | Cross-reference existing owners and consume exact preservation receipts; do not duplicate conversion, table or CRDT development. |

## Coverage of the conversation's wider feature inventory

| Research area | Our authority or selected disposition |
| --- | --- |
| Lifecycle, structure, identity and unknown content | Engine, current schema, block actions and document durability. |
| Selection/focus and keyboard behavior | Everyday editing plus ES-SEL-1 / ES-KEY-1 in the supplement. |
| Input, Unicode, composition, layout | Existing web/native contracts plus ES-TEXT-1/2/3 and ES-INPUT-1. |
| Formatting, pending styles and search | Existing everyday/rich-content contracts; ES-FMT-1 makes the boundary and scoped support explicit. |
| Lists, quote, code and block operations | Existing Enter/list/Tab contracts; ES-BLOCK-1/2 adds cross-context applicability. |
| Tables and embedded applications | Current table/extension selection owns interior edits; no implicit host-record editing or deletion. |
| Clipboard, drag and conversion | Existing fragments, formats and conversion classification; ES-INT-1. |
| Undo/redo, collaboration and presence | Shared local-origin history and durable relative anchors; distinct from revision restore and review suggestions. |
| Saving, recovery and assets | Storage receipts and durable format; transport acknowledgement is not redefined as a save receipt. |
| Accessibility and platform input | Existing platform owners and final roadmap43; ES-AX-1. |
| Comments, suggestions and revision review | Existing change-review and anchor contracts; no new review UI or copied-discussion semantics implied by block copy. |
| Publishing, printing, academic fields and office-format fidelity | Existing optional conversion/publication scope. Not prerequisites for everyday editing. |
| Programmatic/agent editing and extensions | Same validated semantic commands and captured targets; no UI shortcut path with weaker safety. |

## Acceptance and execution boundary

The selected behavior is intentionally close to ordinary rich editors while retaining our declared differences: paragraph Tab indentation with Escape then Tab focus escape, outside-link typing at the end boundary, table-cell Enter as an in-cell break, and logical-order TUI source editing. Notion's Escape-to-block-mode behavior cannot replace our existing popup/IME/focus-escape contract. Generic Duplicate, synced content, page/database transforms, arbitrary multi-cursor editing and dormant-property storage are not added to the baseline.

Implementation must assert content **and** identity, selection direction/affinity, next typed position, history/publication count, cancellation and recovery. Deterministic mechanics, build success and real OS/IME/assistive observations are separate results. Comprehensive case development belongs after functional delivery; platform observations remain with [roadmap43](../roadmaps/43-physical-device-verification.md). Planning starts no runner, changes no active source snapshot and grants no publication or paid-inference authorization.

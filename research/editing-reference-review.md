# Editing reference review — 2026-10-24

Purpose: strengthen observable editing behavior, feature descriptions and tests. The [experience contract](../specs/editing-experience.md) contains edit.ac's decisions; this document records provenance and differences. External documentation is evidence for a design choice, not proof that our implementation works.

## Local copy of the requested site

The full reachable public [CKEditor Editor Recommendations site](https://ckeditor.github.io/editor-recommendations/) is saved locally in `architecture/.artifacts/editing-reference/ckeditor-20261024/`. Open its README for links to readable text. `raw/` retains original response bytes, `text/` holds searchable text, and `manifest.json` records requested/final URLs, content types, byte counts, SHA-256 hashes, retrieval time, failures and outbound links. The traversal covers all reachable same-site pages and their local assets, not external discussion threads, CDN libraries or analytics. It does not claim to discover unlinked private URLs.

Reproduce into a fresh ignored directory from the workspace root:

```sh
python3 architecture/scripts/archive-editor-recommendations.py \
  --destination architecture/.artifacts/editing-reference/ckeditor-next
```

The archive is local reference material, not project source or a vendored runtime. [About/license](https://ckeditor.github.io/editor-recommendations/about/) identifies CKSource copyright and CC BY-NC-SA 4.0. Attribution is retained in raw pages, text headers and the archive README. Text extraction removes scripts/styles and layout whitespace; raw bytes remain unchanged. Do not relicense the downloaded material as Apache-2.0 or publish it with the SDK. Requirements below and in the companion contract are independently expressed product decisions.

The eleven additional primary references below also have local response/text copies and a URL/hash manifest in `architecture/.artifacts/editing-reference/supporting-20261024/`. Each retains its own source rights; these ignored downloads are for local research. Refreshing the main-site archive does not refresh these independent snapshots.

## Page-by-page review and disposition

| Source | Useful contribution | edit.ac decision / existing owner |
|---|---|---|
| [Home](https://ckeditor.github.io/editor-recommendations/) | Feature, usability and use-case taxonomy. | Keep capability descriptions separate from test/implementation status. |
| [About](https://ckeditor.github.io/editor-recommendations/about/) | Editor-neutral intent and source license. | Archive locally with attribution; use primary standards to supplement dated guidance. |
| [General policies](https://ckeditor.github.io/editor-recommendations/general-policies/) | Semantic, accessible, portable content and platform modifier conventions. | Preserve semantic commands and platform input ownership; no universal Ctrl-only shortcuts. |
| [Bold](https://ckeditor.github.io/editor-recommendations/features/bold.html) | Familiar label and semantic output. | Existing mark codec decides output; MRK tests cover uniform/mixed and pending state. |
| [Italic](https://ckeditor.github.io/editor-recommendations/features/italic.html) | Describes alternate voice and proposes `i`. | Do not replace our emphasis/italic serialization simply to match this historical preference. Distinguish semantic meaning through existing format contracts. |
| [Strikethrough](https://ckeditor.github.io/editor-recommendations/features/strikethrough.html) | Represents content no longer relevant. | A strike mark is not tracked deletion or review history. |
| [Highlight](https://ckeditor.github.io/editor-recommendations/features/highlight.html) | Highlights contextual relevance. | Explicit capability/value; preserve mixed state and report lossy exports. |
| [Headings](https://ckeditor.github.io/editor-recommendations/features/headings.html) | Heading split versus end-of-heading exit. | Adopt context-sensitive Enter; do not restrict the schema to its suggested three heading levels. BRK-05. |
| [Bulleted list](https://ckeditor.github.io/editor-recommendations/features/bulleted-list.html) | Split, join, indent and empty-item exit. | Preserve nesting and one-transaction history; Shift+Enter remains in the same item. BRK-06/DEL/KEY. |
| [Numbered list](https://ckeditor.github.io/editor-recommendations/features/numbered-list.html) | Ordered structure and list keyboard transitions. | Preserve ordered starts and surrounding list identity; do not rebuild lists from displayed numbers. |
| [Link](https://ckeditor.github.io/editor-recommendations/features/link.html) | Destination semantics. | Add safe URL policy, captured range, cancel/stale-target tests and typing-boundary behavior through existing link owners. |
| [Image](https://ckeditor.github.io/editor-recommendations/features/image.html) | Alternative text, figure/caption structure. | Preserve supported alt/caption semantics and atomic-object navigation; no mandatory wrapper migration. |
| [Quote](https://ckeditor.github.io/editor-recommendations/features/quote.html) | Quotation with optional attribution. | Preserve existing quote containers; figure/citation support must be explicitly modeled before advertising it. |
| [Table](https://ckeditor.github.io/editor-recommendations/features/table.html) | Structured cells, headers and captions. | Respect current table/header capabilities; do not convert the first row into a header or require figure wrappers during editing. |
| [Enter key](https://ckeditor.github.io/editor-recommendations/usability/enter-key.html) | Separates paragraph creation from a line break within a block. | Directly supports BRK-01/02. Assert owner, content and next typed sentinel, not only appearance. |
| [Inline style state](https://ckeditor.github.io/editor-recommendations/usability/inline-style-state.html) | Enumerates ambiguous selection and empty-block cases; explicitly a draft. | Do not adopt its first-character algorithm or remembered empty-block style proposal wholesale. Our whole-selection mixed state and transient pending marks remain authoritative. |
| [Tab key](https://ckeditor.github.io/editor-recommendations/usability/tab-key.html) | Predictable focus traversal and restored selection. | Keep prose traversal and qualified list/code/table exceptions with keyboard escape; avoid traps. |
| [Article comments](https://ckeditor.github.io/editor-recommendations/use-cases/article-comments.html) | Compact authoring use case. | Example composition only; no forced preset or implicit Send behavior. |
| [Blog/article](https://ckeditor.github.io/editor-recommendations/use-cases/blog-article.html) | Long-form structural content. | Test headings/lists/media together, but individual features remain independently configurable. |
| [Private message](https://ckeditor.github.io/editor-recommendations/use-cases/private-message.html) | Message authoring conventions. | Host submission policy is separate from editor Enter semantics and IME confirmation. |

## Additional primary references

| Reference | What it adds and how we use it |
|---|---|
| [W3C Input Events Level 2](https://www.w3.org/TR/input-events-2/) | Distinct `insertParagraph` and `insertLineBreak` intentions, target ranges and composition ordering. Add beforeinput-only tests; do not assume hardware keydown or universal browser support. Working-draft status is not browser qualification. |
| [CKEditor 5 ShiftEnter](https://ckeditor.com/docs/ckeditor5/latest/api/module_enter_shiftenter-ShiftEnter.html) | Contemporary separate Shift+Enter feature/command. Compare terminology without importing its plugin architecture or document model. |
| [CommonMark 0.31.2 hard/soft breaks](https://spec.commonmark.org/0.31.2/#hard-line-breaks) | Distinguishes source hard breaks from soft line endings. Check our exporter/importer for trailing/repeated authored breaks; Markdown syntax is not the live editor's schema. |
| [Unicode UAX #29](https://www.unicode.org/reports/tr29/) | Grapheme segmentation basis. Combine it with UTF-16 boundary checks and declared tailoring; a code point or code unit alone is not a user-visible character. |
| [WAI-ARIA toolbar pattern](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/) | Keyboard focus management and control navigation. Pair labels/states with captured editor selection; toolbar arrows must not move the document caret. |
| [Clipboard API](https://www.w3.org/TR/clipboard-apis/) | Copy/cut/paste events and data transfer boundaries. Retain import sanitization and source-delete ordering; API presence does not prove permission or transfer success. |
| [AppKit NSTextInputClient](https://developer.apple.com/documentation/appkit/nstextinputclient) | Marked text, selected/replacement ranges and committed text responsibilities. [Readable primary source](https://developer.apple.com/documentation/appkit/nstextinputclient.md). Our adapter must preserve composition and route committed edits to Session. |
| [UIKit UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) | Selected/marked ranges, positions and caret geometry. [Readable primary source](https://developer.apple.com/documentation/uikit/uitextinput.md). A desktop key test cannot qualify these mobile contracts. |
| [Android InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection) | IME text, composition and deletion methods have distinct semantics/units. Test the actual adapter/IME instead of treating a newline as a key event. |
| [Microsoft custom text input](https://learn.microsoft.com/en-us/windows/apps/develop/input/custom-text-input) | Text services coordinate text and selection updates with application-owned editing. A Windows bridge needs its own target-range/composition observations. |
| [GTK IMContext](https://docs.gtk.org/gtk4/class.IMContext.html) | Separate preedit and commit lifecycle and surrounding-text facilities. Linux input tests must preserve that distinction. |

No single source specifies every editor. The authoritative context table, atomic transaction boundaries, stable anchors and per-platform tests are edit.ac decisions reconciled with existing specifications. Standards conformance, matching another editor's visual output and passing a shared engine test are three different claims.

## Implementation inspection

Codanna MCP and CLI were unavailable in this session; bounded path/literal searches were used instead. Existing browser `breaks.spec.ts` already covers paragraph splits, same-owner breaks, selected replacement, repeated breaks, codec/storage and contextual transitions. The keyboard adapter already has a shared `hardBreak` route. The additional gap to guard is input-intent delivery without a hardware keydown, paired with a visual-wrap negative control.

The inspected AppKit command enum/router exposed Enter and split but no explicit hard-break command; `insertLineBreak:` fell through to NSTextView. That is a concrete adapter gap even though browser hard-break tests exist. Terminal `cli/src/tui/input.rs` edits source text and deliberately inserts source newlines; it is not evidence of rich-paragraph behavior. iOS/Android and Windows/Linux each require their own adapter evidence; shared bindings and capability declarations do not complete those rows. See the action table and platform matrix for exact closure conditions. Runtime results belong in the conversation/ignored test output, not this source review.

The amendment adds the explicit AppKit command and Shift+Return/selector routing, with deterministic runtime regressions. The history assertion then exposes a separate [native selection-restoration defect](../specs/editing-experience.md#open-regression-native-history-loses-the-editing-selection); the route addition does not qualify native history. Its failing test remains enabled, and the shared history transport work stays open. The full native gate also needs its stale capability revision/input pins reconciled at a validated checkpoint.

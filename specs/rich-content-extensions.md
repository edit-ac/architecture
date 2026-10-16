# Rich content extension contracts

Status: planned portable and web delivery, roadmap 25. Reuse roadmap 07 implementations and roadmap 21 public interfaces; this work adds the named gaps rather than replacing qualified modules. Full native/TUI integration consumes these contracts in roadmaps 31–36 and is not an upstream prerequisite.

## Ownership and public boundary

Rust remains authoritative for content, schema, commands, validation, source reconciliation and history. Highlight tokens, table layout, decoded media, menus and drag geometry are derived presenter state. Platform caches may be discarded without changing the document. Optional processing/presenter dependencies are absent from minimal consumers when disabled.

Expose each feature through the owning Rust crate and documented `@edit-ac/core`/`@edit-ac/web` exports. Reuse existing extension descriptors, command preparation, scoped subscriptions and presenter lifecycle. A new crate/package requires an explicit consumption/size reason. Define versioned feature records and capabilities for data preservation, view, edit, copy, source, accessibility and optional network activation.

Portable presenter ports carry stable node identity, content revision, source/profile, selection/readonly capabilities and bounded patches. Results carry request identity/revision; stale, canceled or disposed results cannot mutate or repaint a replaced target. Define prepare/apply actions separately from derived appearance updates. Publish fixtures that Swift/Kotlin/desktop/terminal presenters can consume without browser types.

## Code blocks and highlighting

Persist literal code and a validated language identifier. Highlight spans, grammar/theme caches and syntax trees never become collaborative marks or another writable document. Preserve unsupported labels and provide immediate plain-code editing when a language is unavailable, loading, over budget or disabled.

Qualify a maintained Rust-capable backend and exact grammar/query versions before selection. Tree-sitter is an initial candidate, not a promise of performance or coverage. Test Rust, TypeScript and JSON initially; every additional language names grammar license/version, bounds and evidence. Optional browser-only alternatives may be compared, but do not imply portable native tokenization.

Own backend code, grammar dependencies, caches and compile probes in the optional `editac-highlighting` Rust companion crate. It is independently consumed by native hosts and optional browser worker bindings; the semantic engine has no dependency on that runtime. Small descriptor/offset/span records may remain public engine contract types. Reuse existing npm package exports for optional loading until measured consumption justifies another npm package.

The highlighting port accepts immutable block text/edits plus prior cache identity and returns validated token spans and a cache handle. Cache keys include block/revision/language/grammar/query/theme versions. Test UTF-8-to-UTF-16 conversion, overlapping/invalid spans and multiline state changes. Incremental output must equal the selected backend's full recomputation for the same input. Bound retained trees/tokens and invalidate on identity/language/profile changes.

Browser workers are optional scheduling adapters, not owners of document state. Record startup, transfer, processing and DOM-application costs separately; coalesce obsolete requests, bound queues and terminate owned workers on disposal. Highlighting never delays input, local persistence or collaboration. Rendering preserves selection and leaves the active composing subtree browser-owned until safe reconciliation. A highlighting failure remains a visible plain-code fallback, not lost source.

## Table editing, layout and source formatting

Keep bounded rectangular tables and simple cells; merged cells, spreadsheet formulas and a general layout engine remain outside this contract. Extend the existing module with explicit row/column insert/remove, header/alignment, cell selection, keyboard movement and cell-range copy/paste commands where missing. Record behavior when deleting the last row/column and for readonly/invalid targets. Every accepted operation has one intentional undo group.

The public `tableRectangle` editor command routes exact-descriptor clear (`cells: null`) and literal row/column matrices through the existing Rust rectangle preparation (128 affected cells, 1 MiB replacement). Dimensions must match; expansion, merged cells and nested fragments reject. Host-owned protected coordinates accompany the captured descriptor; whole-document authorization remains the host commit owner's responsibility. Browser cell selection is transient and explicit, separate from native cell text selection. Shape changes remain explicit `tableStructure` commands. The browser exposes separate cell-selection buttons (Shift-click extends the rectangle), preserving the native textarea Tab order. Enter enters the first selected cell; typing replaces that cell only. Delete/Backspace clears the rectangle, while structural removal currently requires one selected row or column. Clipboard output is explicitly literal HTML/TSV/plain text; marked transfer is unqualified. Literal input normalizes CRLF, retains explicit row/column boundaries and requires exact dimensions. Unsupported HTML markup, merges or nesting reject even when accompanied by a flattened fallback. No table resize/drag preview is introduced; nested controls retain their own input/selection/gesture owner beside the optional block reorder controls.

Commands use stable table/row/cell identities and the frozen structural concurrency policy. Qualify concurrent row/column changes, cell edits and deleted destinations. Deterministic core projection resolves invalid remote structures; presenters do not emit their own repair transactions.

Cache geometry/indexes per table and invalidate only affected tables/cells. A cell edit must not scan or rerender every table in the document. Native/TUI ports expose cell rectangles/selection and semantic navigation separately from browser DOM geometry. Copy/export preserves hidden/unknown bounded content or reports a recoverable limitation.

The Markdown table formatter is an explicit selected-table source operation. Use the retained source baseline and revision-checked reconciliation; preserve surrounding bytes, code spans, escaped pipes, alignment, empty cells and final-newline policy. Record the Unicode display-width policy used for aesthetic padding. Formatting is deterministic and idempotent on its own output, with one undo group. It does not normalize an entire file or run automatically on every cell edit.

## Attachment and blob lifecycle

Define file/image/media descriptors with stable host asset identity, bounded filename/media type/size/hash metadata, alt text/caption where applicable and a safe fallback. Temporary object URLs and expiring signed download URLs belong to presentation, not persistent shared identity. A filename, MIME declaration or hash alone does not grant download rights.

The host asset port handles authorize, ingest, read/cache, publish, resolve URL, cancel and release-reference operations with explicit capabilities. Upload/account/storage products remain host responsibilities. Define local-only, queued, available, failed, missing, revoked and locked outcomes, including what other replicas display before bytes become remotely available. Asset commit and document update receipts remain distinct.

Journal resumable local work and bound blob/cache/outbox storage. Crash, full disk, auth expiry, offline reconnect and deletion during upload preserve recovery data without resurrecting deleted nodes. Idempotent host operation IDs prevent duplicate upload intent; transport retry semantics are explicit. Shared binary deletion/garbage collection requires host ownership/refcount policy rather than an editor deleting data on every removed node. E2EE ports preserve the security profile across originals, thumbnails, caches and exports.

## Image, file and embed presentation

Images enforce encoded-byte, decoded-pixel, dimension and concurrent-decode limits. Validate the actual media type under host policy; handle malformed/SVG/animated content explicitly. Render alt text and missing/offline/locked fallback. Dispose object URLs, observers, decoders and requests. External image loading requires host asset policy; parsing/opening a document does not authorize arbitrary URL fetches.

File attachments expose accessible filename/status/size and an explicit host-authorized open/download action. Clipboard/source export uses the declared stable identity/fallback and reports unavailable binary data. Native attachment view and terminal fallback records are part of the public presenter contract, not an assertion that those presenters already ship.

PDF export is a separate requested output capability. An attached PDF remains an opaque file asset; optional host preview is not PDF import, OCR or conversion into editable content. The semantic core requires no PDF reader. Do not add a PDF ingestion prerequisite to attachment handling.

Embeds store a bounded URL/provider identity and safe fallback, never executable HTML/code. Separate a metadata card from an activated interactive embed. Hosts register allowlisted presenter templates and an isolated/sandboxed activation policy; raw oEmbed/provider HTML never enters the editor DOM. Apply the [link resolver contract](link-resolution.md) to metadata and secondary media URLs. Roadmap 25 uses prepared resolver fixtures; actual resolver integration and native/TUI presenters are qualified downstream. Unsupported/offline/readonly modes retain identity and safe content.

## Slash, references and reorder

Extend the existing slash menu with explicit trigger context, code/literal exclusions, IME lifecycle, selection replacement and query-length/result-count bounds. Filtering is scoped to current input context. Focus restoration, escape, empty/error states, touch/pointer selection and screen-reader labels are tested; remote edits/replay never open the menu. Async providers follow the shared cancellation/revision contract.

Custom references retain stable target identity and user-authored fallback text. Their presenter consumes the host resolver's public/private/forbidden/missing/locked outcomes, without inventing target access or sharing private titles. Lookup, disclosure and cache policy live in [link-resolution.md](link-resolution.md). The feature supports configured `@`, `[[` or other bounded triggers through the existing registration interface, with plain-text fallback and explicit activation.

Block pointer reorder uses a derived drag session: threshold, hit testing, auto-scroll, valid destination, cancellation and current target anchors. Hover does not mutate CRDT state; final acceptance prepares one semantic move and one history group. Preserve content identity and selection under concurrent edits/deletion. Provide keyboard movement and a simple click/tap alternative such as Move before/after; keyboard alone does not replace the non-drag pointer alternative. Announce destination/result through platform accessibility ports.

## Measurement and qualification

Use production artifacts and fixed hardware/browser/toolchain profiles from [verification.md](verification.md). No numbers below are measured results. Retain failed samples and make a measured accept/revise decision before publishing support claims. Record p50/p95/p99, exact fixture hashes, 100 warm samples, separate cold loads, main-thread/worker/transfer/apply costs, bundle bytes and memory/DOM/token counts.

| Area | Fixture and initial acceptance target |
|---|---|
| Input | Preserve existing p95 visible-update targets of 16.7 ms desktop / 33 ms phone; optional presentation never gates a commit |
| Highlighting | 10/100 KiB code, 250 KiB long line, 100 small blocks and language/theme churn; proposed main-thread decoration slices <=4/8 ms; yield or plain-code fallback beyond qualified limits |
| Tables | 20x10 interactive and 100x20 stress tables, many unrelated tables, long/Unicode cells; input targets plus counters proving only affected table/cells are invalidated |
| Menus | 500 deterministic local commands/results; existing one-frame/two-frame p95 ready-runtime target; host lookup latency separately visible |
| Reorder | 2,000-block fixture with bounded geometry work and proposed 16.7/33 ms pointer-frame p95; no update during hover and one accepted move |
| Assets | Bounded request/decode concurrency, offline/failure fixtures and repeated disposal; no unbounded queues, object URLs or retained subscriptions |

Measure full highlight/format latency separately from input. Attribute >50 ms long tasks in ordinary-edit fixtures. A worker is not proof of responsiveness. Minimal disabled consumers must exclude optional grammar/presenter assets and issue zero requests for them. Device IME/accessibility/native rendering requires downstream real-platform evidence.

## Work-count and structural rejection refinements

[WCF-08/WCF-15/WCF-16](../tests/wordcraft-regression-cases.md) extend existing table/highlight owners. Reject table-into-own-cell and over-depth fragments before mutation under the bounded simple-cell policy; exercise copy, serialization, history and disposal afterward with small fixtures. Do not add nested-table semantics.

Instrument cache hits/misses, measured cells, recomputed blocks and rendered updates separately from timings. Declare the affected dependency set for content versus width/font/zoom or grammar/query/theme changes; unaffected tables/blocks reuse results. Compare warm/incremental results to cold recomputation, bound retained resources and reject stale/cross-session results. This adds test observations, not a second model, general layout engine or always-on telemetry. Offline proofing remains deferred.

## Primary references

- [Tree-sitter highlighting](https://tree-sitter.github.io/tree-sitter/3-syntax-highlighting.html) and [incremental parsing](https://tree-sitter.github.io/tree-sitter/using-parsers/3-advanced-parsing.html)
- [Shiki browser performance guidance](https://shiki.style/guide/best-performance)
- [ProseMirror table command/cache precedent](https://github.com/ProseMirror/prosemirror-tables)
- [WAI-ARIA suggestion pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) and [non-drag pointer alternative](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)
- [oEmbed response/security contract](https://oembed.com/)

## Mobile browser integration

Track 25 continues to own portable semantics and existing presenters. [Track 41](../roadmaps/41-mobile-web-extensions.md) adds the [mobile extension cases](../tests/mobile-extension-cases.md) after those capabilities exist: keyboard-open menus, native selection coexistence, touch table/code controls, cancelable drag/resize with tap alternatives, file/camera/share fallback and media resource teardown. Reuse [mobile web](mobile-web.md) ports from track 40; do not add viewport or gesture policy to Rust. The optional integration does not gate baseline mobile editing.


## First-party document search and code conveniences

These optional features extend track 25 and reuse the semantic engine, public commands and existing presenter contracts. [Desktop research](../evidence/desktop-editing-research.md) supplies precedents; [desktop cases](../tests/desktop-editing-cases.md) define the chosen scope. Their absence does not disable ordinary native/browser Find or baseline editing.

Document Find searches logical content, including unmounted blocks, through a bounded revisioned index. Default matching is literal and case-sensitive, without Unicode normalization or invisible content rewriting. Expose whole-document and captured-selection scopes; matches cannot cross atom, table-cell or block boundaries unless an explicitly documented query profile supports those boundaries. A case-insensitive profile must declare Unicode/locale rules and map matches back to complete original characters. Regex/wildcards, format matching and workspace-wide search remain unsupported until separately bounded and qualified. Search highlight is transient presentation, not a persisted mark or remote edit. Enter/Shift+Enter in the search field navigate next/previous; Escape closes it and restores the appropriate editor selection without overwriting later deliberate navigation. Empty queries clear results without generating zero-length replacements. Result wrap and count are explicit and accessible.

Replace Current acts on the anchored current match after revision/permission revalidation, not the find input's selection. Replace All enumerates nonoverlapping matches in the captured scope of one revision, prepares a bounded compound operation and commits once with one undo group; it never recursively searches its own inserted replacement. Record match/count/byte limits before execution. On limit, stale target or unsupported structure, keep the document unchanged and offer a narrower scope; do not silently perform a partial replace-all. Async scanning is cancelable and rejects stale results. Existing marks outside replaced ranges remain unchanged; inserted text follows the captured destination typing-mark policy. Protected/read-only ranges are excluded with explicit counts before confirmation or cause atomic rejection according to the named profile, never silent skipping. Remote edits require revalidation/recomputation before any destructive commit. Native OS find UI may use this provider after the platform task qualifies its scope/history and focus behavior.

The code convenience profile provides move selected logical lines up/down, duplicate logical lines, indent/outdent, and explicit surround-selection with a supported paired delimiter. A selection ending at the start of the next line excludes that untouched line. Preserve LF, tabs, trailing spaces, marks allowed by code, directional selection and EOF without a terminal LF. Moving past block boundaries is a no-op; do not merge code with prose or move table cells. Each accepted operation has one undo group and complete prepared validation. Enable line comments only for a declared language/comment grammar; unknown languages expose an unavailable command. Automatic pair completion is a separate explicit opt-in: suppression during composition, paste, correction, remote replay and literal input is mandatory; overtype/backspace behavior is fixed by the profile. Visible command access and remappable platform bindings take precedence over borrowing conflicting IDE keys. Multi-cursor, AST refactoring, language servers and macro recording are outside this profile.

Table commands distinguish a text range from a cell rectangle. Delete/Backspace on a cell rectangle clears editable contents while retaining table geometry; Remove Rows/Columns is an explicit structural action. Mixed protected cells, partially selected merged cells if supported, rectangular paste dimension mismatch, literal TSV and nested native controls require declared outcomes before mutation. Unsupported merged cells never get flattened silently. These extend RCH-1.6/1.8 rather than introducing a second table model.


## Optional AI writing extensions

The [AI contract](ai-extensions.md) is delivered by RCH-2.1–RCH-2.14 in this same roadmap. It includes autocomplete, Ask AI, fill/continue and selected-text actions using Vercel AI SDK Core as the default TypeScript backend adapter behind the portable host transport. Edit.ac retains target capture, transient suggestions, proposal review, semantic acceptance and history. The SDK/provider remains absent from the Rust engine and disabled/minimal editor clients.

AI-only SDK/browser/mobile prerequisites and independent native/TUI/docs entry gates are declared in the AI epic; existing RCH-1 gates remain intact. AI native/TUI wiring stays with RCH-2 platform tasks, while existing non-AI native/TUI rich presenters remain owned by 31–36. No paid testing or live dogfood is authorized. [The SDK evaluation](../evidence/ai-extension-research.md#vercel-ai-sdk-evaluation-and-default-decision) records fit, limitations and the task-ID migration.

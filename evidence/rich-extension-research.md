# Extension scope and implementation-pattern review

Reviewed 11 October 2026: `extension-library.md`, `modules-native.md`, `formats.md`, and relevant roadmap 07/21 contracts. This is a planning review, not an implementation audit or benchmark result. No project files changed, packages installed, live metadata fetched for user documents, or paid calls made.

## Current coverage and gaps

| Capability | Existing coverage | Gap to close |
|---|---|---|
| Code blocks | Literal source/language labels and Markdown fences | No syntax-highlighting implementation, language grammar/loading policy, incremental tokenization or performance task |
| Tables | Bounded rectangle, simple cell editing/copy, preservation | No explicit source formatter, row/column/header/alignment command inventory, per-table cache or concurrent shape/performance matrix |
| Images | URL/alt/dimensions, host policy and fallback | No stable asset lifecycle, offline binary availability, decode-size limits or failed upload/recovery contract |
| Attachments/embeds | Unknown atoms and generic extension hooks | No first-party file attachment or controlled embed contract; generic raw embed HTML must not inherit image safety assumptions |
| Slash menu | Local trigger, keyboard/touch, cancellation, one history group | Needs context exclusions, IME/selection cases, bounded filtering, full pointer/screen-reader evidence and measured cold/warm cost |
| Block reorder | Semantic move, keyboard and optional drag handle | Needs explicit pointer drag/drop/auto-scroll/cancel behavior and a non-drag pointer alternative |
| Custom references | Target identity/label, host resolver, stale result protection | Good base; needs per-viewer private metadata, permission-scoped caches and disclosure rules |
| Automatic title/favicon | No dedicated contract | Conflicts with no-fetch-on-open unless a new host-policy-controlled enrichment boundary is explicit |

MOD-1.7 combines images and tables into one broad task. Split their delivery/validation while reusing the existing implementation; roadmap 21 should qualify and expose new capabilities, not reimplement them. Extend the capability matrix beyond the current six built-ins when attachments, embeds and highlighting become advertised features.

## Verified primary-source patterns

**Portable highlighting.** Tree-sitter has a Rust/C highlighting library with grammar-specific queries. Its incremental parser accepts an edited previous tree and shares structure with the newly parsed result. This supports a Rust-first candidate, but does not establish small bundles, complete language coverage or bounded latency for edit-ac. Pin grammar/query versions and measure each supported target/language. [Highlighting](https://tree-sitter.github.io/tree-sitter/3-syntax-highlighting.html), [incremental parsing](https://tree-sitter.github.io/tree-sitter/using-parsers/3-advanced-parsing.html)

**Optional browser alternative.** Shiki recommends fine-grained language/theme bundles, reuse of a highlighter, and avoiding full bundles in constrained browser environments. Its performance guide discusses workers and startup costs. A Shiki adapter can be optional browser presentation, but cannot be advertised as shared Rust/native tokenization. Do not select either candidate without the scope/size spike. [Shiki performance guidance](https://shiki.style/guide/best-performance)

**Table implementation precedent.** ProseMirror tables separates cell selections, copy/paste, commands and structural validation; its TableMap is cached per table with table-relative positions. Its repair helper can skip unchanged document regions. Borrow locality and command boundaries, not ProseMirror document ownership or its write-based repair behavior: edit-ac still needs deterministic core projection/concurrent policies. Merged cells remain excluded unless separately authorized. [Official table module](https://github.com/ProseMirror/prosemirror-tables)

**Menus and drag accessibility.** WAI-ARIA combobox guidance defines focus, popup and keyboard behavior useful for reference suggestions. Choose the correct command-menu/suggestion semantics instead of blindly adding a combobox role to the whole rich editor. WCAG dragging guidance requires a single-pointer alternative without dragging; keyboard controls alone do not satisfy that specific requirement. [Combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/), [dragging movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)

**Metadata is untrusted remote input.** Open Graph defines fields including title/image/canonical URL; it does not establish a permission to fetch them or trust their URLs. HTML defines linked icons and favicon fallback behavior. oEmbed rich/video responses contain HTML and its own security guidance warns about XSS and URL schemes. Treat metadata cards and executable embeds as different capabilities. [Open Graph](https://ogp.me/), [HTML icons](https://html.spec.whatwg.org/multipage/links.html#rel-icon), [oEmbed](https://oembed.com/)

**Fetching boundary.** Browser fetch remains subject to CORS; `no-cors` is not a readable metadata bypass. A host-supplied metadata resolver may be needed, but becomes an SSRF boundary. OWASP recommends allowlisting where possible and disabling automatic redirects that could bypass validation. [Fetch/CORS](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch), [OWASP SSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)

## Proposed implementation contracts

### Code blocks and tables

Persist code text and a validated language identifier only. Highlight tokens/theme/layout are disposable projections, never collaborative marks or another authoritative document. Cache by stable block identity, content revision, grammar/query and theme version; reject late results. Rust token offsets need tested conversion to UTF-16/DOM positions. A browser worker receives bounded immutable block snapshots/edits, not a second writable editor replica. Plain code remains immediately editable during loading, timeout or unsupported language. Never patch the composing subtree merely to recolor it.

Separate table editing, visual layout and Markdown source formatting. Shared row/column/cell commands validate a bounded rectangle and use stable identities; cache indexes per changed table. Qualify concurrent row/column deletion/insertion and cell edits without platform-specific repair writes. A source formatter prepares a revision-checked edit for the selected table only, preserves surrounding source, handles escaped pipes/code spans/alignment/empty cells, and forms one undo group. Source display-column alignment needs a documented Unicode width policy; it is not document semantics.

### Assets and embeds

Persist stable host asset identity plus bounded metadata, alt text and declared fallback. Temporary object URLs or expiring signed download URLs are resolved presentation state, not permanent shared identity. Define local-only/queued/available/failed/revoked states, offline cache requirements, cancellation and recovery; upload/storage remains the embedding host's service. Deleting a node during an upload must not resurrect it. Asset cleanup needs host policy; an editor must not delete shared binaries merely because one reference disappeared.

Bound encoded bytes, decoded pixel count, dimensions and concurrent decoding. Revoke object URLs and cancel work on disposal. Rendering a stored external image requires explicit host asset policy; document open does not silently grant arbitrary network access. Generic files render as accessible attachments with explicit activation. Rich embeds use allowlisted host presenters and a reviewed isolated/sandboxed activation policy, never arbitrary provider HTML in the editor DOM. An offline/unsupported embed preserves its URL/identity and safe label. E2EE asset/profile rules apply to originals, thumbnails, metadata and caches.

### Automatic metadata and private links

Add an explicit enrichment policy: disabled, local paste/insert only, or user-requested refresh. “Automatic” means the host has opted into enrichment for that initiating local action; opening a document, remote edits, replay and merely rendering links never trigger fetches. Network preparation occurs outside semantic commit. Resolve using cancellation and node/revision/URL identity; a stale title must not overwrite edited user text or resurrect a deleted link. Metadata updates have explicit history grouping; cached preview changes need not mutate the document.

The public-URL resolver admits only configured HTTP(S) URLs without embedded credentials. Apply bounded timeout/response/decompression/image limits, no browser/session cookies or forwarded authorization, and an egress policy. Disable redirects by default; if supported, validate every hop and its actual resolved connection address. Cover private/loopback/link-local/reserved IPv4/IPv6, DNS changes/rebinding, encoded-host tricks and cloud metadata destinations. Favicon and Open Graph image URLs require the same validation, not an unchecked second fetch. Avoid third-party favicon services that disclose document URLs by default. Cache and log sanitized keys; URLs/query strings can contain secrets.

Private internal links use a separate host-authorized catalog resolver, not the public fetcher with private-network checks disabled. Check the current user's target permission for lookup, activation, title/icon and preview. Scope caches to tenant/actor/authority/capability context and invalidate on expiry/revocation. Denied/missing targets use the host's non-disclosing outcome policy. Keep fetched private titles/icons per viewer by default: writing them into shared CRDT fallback labels discloses them to everyone allowed to read that document. Persist a title only when the host explicitly authorizes that disclosure; revocation cannot erase text already legitimately shared/copied. A reference never grants access to its target.

## Bounded task units to map into the existing roadmap

The identifiers below are proposals, not additional active roadmap IDs. Each task owns its named fixtures/behavior; implementation and validation should fit one focused session or be split before starting.

| Unit | Prerequisites | Deliverable and decisive acceptance |
|---|---|---|
| H1 Highlighting feasibility | Code-block core + WASM packaging | Tree-sitter Rust candidate versus optional browser alternative on Rust/TS/JSON fixtures; exact asset/grammar versions, bytes, timings, fallback and target compilation; ADR selects supported languages/backend |
| H2 Incremental token pipeline | H1 | Block-local cache/token spans with cancellation and revision guards; incremental output equals full recompute after multiline comment/string edits and undo; no CRDT formatting writes |
| H3 Browser code presentation | H2 + web IME gate | Optional worker/lazy assets, selection-preserving incremental spans, unknown-language plain fallback; no stale recolor or composing subtree replacement; measured cold/warm costs |
| T1 Table commands and races | Current simple-table schema | Row/column/header/alignment/cell-selection command inventory, bounds and concurrent shape fixtures; stable IDs and one semantic history group per command |
| T2 Selected-table formatter | Source reconciliation + T1 | Deterministic selected-table source formatting; exact surrounding bytes unchanged, special syntax retained, stale baseline rejected and one undo restores original bytes |
| T3 Table cache and rendering | T1 | Per-table indexes/incremental affected-cell patches; counters prove unrelated tables are not rebuilt; keyboard/cell paste and performance corpus pass |
| A1 Attachment lifecycle | Host asset port + session persistence | Stable descriptors and deterministic upload/cache/failure/cancel/revoke fixtures; interrupted/offline work recovers and no signed URL becomes shared permanent identity |
| A2 Image presenter | A1 + current image module | Decode/dimension/concurrency limits, alt text, offline/missing fallback and object URL disposal; no fetch on open without host policy |
| A3 Controlled embeds | A1 + resolver policy | Metadata-only card and separately activated allowlisted embed; untrusted HTML never enters live editor DOM; offline/unknown provider preserves source |
| M1 Slash/reference interaction | Existing MOD-1.4/1.5 | Context and composition exclusions, bounded result list/filtering, escape/focus/selection behavior, cancellation and screen-reader/pointer fixtures; local triggers only |
| D1 Pointer reorder | Existing semantic moves/MOD-1.6 | Drag threshold, bounded hit testing/auto-scroll, cancel/drop/deleted-target races plus Move before/after or Move up/down clickable alternative; no model writes during hover |
| U1 Safe public metadata resolver | Host policy port | Prepared DNS/redirect/private-IP/oversize/timeout/credential fixtures for page and icon/image fetches; all denied paths produce no outbound transport call |
| U2 Automatic enrichment | U1 + metadata descriptors | Opt-in local-insert/refresh lifecycle, cache/cancel/stale-result handling, bounded title/icon fields and explicit metadata history policy; remote/replay/open causes zero calls |
| R1 Private target disclosure | Existing EXT-1.8 + permission ports | Two-user/tenant forbidden/revoked/stale-cache fixtures; per-viewer labels and authorized publication policy; unauthorized peers receive no private metadata |
| Q1 Extension evidence | Relevant units above | Capability matrix, clean consumer fixtures, fixture counts, exact versions, actual size/performance traces and disabled-asset/network checks; no fallback mislabeled as rich rendering |

## Performance acceptance to measure, not claim today

Use fixed devices/browser versions from the existing verification spec, production builds, 100 warm samples per interactive case, and separately recorded cold loads. Capture p50/p95/p99, main-thread time, worker/transfer/application time, bytes, peak/retained memory, DOM/token counts and cancellation/disposal. Proposed thresholds require a measured accept/revise ADR; there are no measurements in this review.

- Preserve existing input-to-visible p95 targets: 16.7 ms desktop / 33 ms phone. Highlighting and metadata must never gate committed editing or local persistence. Record attributable long tasks; no new >50 ms task during the bounded ordinary-edit fixture.
- Highlight corpus: 10 KiB/100 KiB mixed-language blocks, a 250 KiB long line, 100 small code blocks, multiline state changes and rapid language/theme changes. Proposed ordinary-edit main-thread decoration slice: <=4 ms desktop / <=8 ms phone; yield/degrade to plain text beyond the qualified envelope. Measure complete highlight latency separately rather than hiding it in a worker.
- Table corpus: 20x10 interactive table, 100x20 stress table, many unrelated small tables, long cells and escaped/Unicode source. Ordinary cell edit must meet editor input targets and touch only the affected table/cells; source formatting reports preparation and commit time separately. Larger tables remain an explicit qualified envelope, not an implied spreadsheet claim.
- Slash/reference local filtering with 500 deterministic commands/candidates: existing one-frame/two-frame p95 menu target after runtime ready. Host lookup latency is separately visible; cancellation removes work and stale responses cannot reset focus.
- Reorder: pointer-frame p95 <=16.7/33 ms with 2,000 blocks, bounded geometry work, no CRDT update until final drop and one update/history group after acceptance. Include a smaller fixture for low-end supported devices rather than assuming desktop behavior generalizes.
- Asset/metadata fixtures: disabled feature causes zero asset requests and excludes optional presenter/grammar assets from packed bundles. Concurrent request/decode limits are enforced; canceled/disposed work creates no mutation. Repeated mount/open/close cycles plateau in memory and leave no object URLs, listeners, workers or requests alive.

Real OS IME, screen-reader, pointer/touch and native image/embed behavior require device evidence. Prepared transport/metadata fixtures cover correctness and privacy without calling real private sites or model APIs.

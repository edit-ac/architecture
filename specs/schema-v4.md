# Nested structural editor profile v4

Status: controller-authored development contract; ENG-1.19/1.20 qualification and ENG-1.21 production integration are required. This is not a passing interoperability, persistence or release claim. Preserve the qualified v1/v2/v3 layouts, fixtures and receipts.

## Envelope and roots

Schema `editac.registry.editor.v4`, profile `editac.yrs-yjs.editor.v4`; protocol version 1, update encoding 1, UTF-16 offsets. Keep Yrs 0.28.0 with small-client, Yjs 13.6.33, y-protocols 1.0.7 and the pinned toolchains. Use the exact external protocol-v1 envelope, initialized flag and fresh independent writer identities. Admission checks the exact profile/schema/document/epoch before live mutation. No optimistic v3 acceptance, new roots in an old profile, automatic migration or reseeding restored empty documents. A future explicit migration retains the old checkpoint and creates a new epoch.

All ten roots are `MapRef` / `Y.Map`. Preserve v3's retained original-text and operation semantics except the explicitly specified v4 extensions below:

| Root | Exact values |
| --- | --- |
| `registry-parents` | Original source `n:<writer>:<counter>` to immutable `block`; container `c:<writer>:<counter>` to immutable `list` or `quote` |
| `registry-texts` | Original source ID to its single persistent nested `XmlTextRef` / `Y.XmlText`; containers have no text entry |
| `registry-placements` | Original source/container ID to its immutable initial `[parentId, order]` tuple; integral order 0…4294967295 |
| `delete-probe-tombstones` | Original/derived owner/container ID to permanent boolean true |
| `registry-block-attributes` | Original/derived text owner to one complete block-presentation tuple, specified below |
| `registry-ownership-ops` | Unique operation ID to one immutable split/join/place operation tuple |
| `registry-owner-origins` | Each original text source to true; no container or derived owner membership |
| `registry-container-attributes` | List container to `["unordered"]`, `["ordered", start]` or `["checklist"]`; quote container to `["quote"]` |
| `registry-list-item-attributes` | Original/derived text owner to `["check", boolean]`; absence means unchecked |
| `registry-entity-controls` | Original/container/operation ID to `["enabled", boolean]`; absence means enabled |

Array values are atomic `Any::Array` / plain JavaScript arrays, never nested independently merged shared arrays. Writer/counter grammar and bounds match v3; `c:` is a separate namespace allocated monotonically with no reuse. Containers never acquire source texts; splits never clone texts or create registry source entries. Creation reserves immutable kind, initial placement, original-text/origin membership if applicable, and required initial metadata in one prepared transaction. Initial roots/rows establish base versions and are retained thereafter.

Only `@root`, lists and quotes can be parents. Container attributes are stored independently of text length. Ordered start is an integral number 1…2147483647. List mode and start replace as one tuple; concurrent tuple writes use the pinned map conflict rule, not independently merged type/start fields. Checklist state applies to a direct editable child of a checklist container; outside that context retain it dormant without rendering a checkbox. List numbering is derived from current visible direct editable children in sibling order, starting at the tuple's start, with no numbering writes during projection. Nested containers do not increment their parent's editable-child ordinal. Malformed known tuples reject admission; valid unknown JSON discriminants stay opaque with safe retained fallback and cannot be semantic command targets. No extension fetch/execution.

Unknown immutable kind strings retain the same namespace/text/origin membership shapes: an original keeps its text in a read-only safe fallback; an opaque container retains its children, which project at root because it is not an allowed parent. Local creation/structural edits support only the named known kinds. Nonstring kinds or incompatible shared types reject admission; opaque retention does not grant execution or a guessed structural role.

## Ownership, placement and hierarchy

Keep v3 split/join tuples, binary source-relative cuts, dependency graph and total operation ranking (depth, numeric writer, numeric counter). Add:

`["place", targetId, targetVersion, parentId, parentVersion, beforeSiblingId, beforeSiblingVersion]`

`beforeSiblingId` and its version are both null for append. For `@root`, parent version is `"base"`. Other version fields are `"base"` or an operation ID. All non-base versions are graph dependencies. The operation ID is a version token; only split operations create a derived text owner with that ID.

Initial sibling order is initial numeric placement order, then namespace ASCII and numeric writer/counter. Read valid initial nested placements, detach the smallest canonical ID in each cycle, and project missing/unknown/noncontainer parents at root. Retain the raw placement without repair writes. Enforce iterative bounded traversal. Containers own no characters. Each text owner has one effective parent and sibling position; project the resulting tree in preorder.

Replay starts from that base tree. Split inserts the derived right owner immediately after left under the same parent and retains the existing span/cut/version semantics. Join requires two adjacent visible editable owners with the same parent; it preserves left identity/placement/metadata, absorbs right and concatenates retained original spans. It cannot join a container or separator; code joins require matching code language tuples. Endpoint/empty and split-after-join behavior remain required. Both operations retain immutable source identities and all losing intentions.

A place operation applies only if dependencies succeeded; target/current versions match; parent is visible, enabled and an allowed container (or root); target is visible and not tombstoned; and the proposed parent is neither target nor its descendant. Remove target from its current siblings and insert before the named visible sibling under the new parent, or append. The before sibling must exist under that parent, match its version and differ from target. Consume only the target version, replacing it with the operation ID; container children retain their identities and internal order when their parent moves. Local invalid/cyclic/depth-exhausting targets reject the complete preparation before mutation. A remotely conflicting/ineligible operation remains a losing/recoverable intention under deterministic replay, not a guessed repair. Missing binary/version dependencies remain dormant under v3's rules.

Two operations on different targets can coexist; overlapping target versions and stale parent/before versions follow the documented replay eligibility and ranking. Concurrent move/move, move/edit and moves forming a potential cycle must converge under duplicate/reordered delivery. A hidden/absorbed/disabled parent causes its otherwise live children to project at root; their content is not silently swallowed. Tombstones and disabled original owners retain hidden source spans as recovery. Explicit subtree deletion, if implemented by a later command, names its complete prepared target set; a container tombstone alone is not implicit cascading deletion.

Block metadata on a derived split owner inherits the live left-owner tuple until explicitly overridden, as in v3. Checklist state differs: a new split owner defaults to unchecked; splitting a checked item retains left's check and gives right an unchecked default. Absorbed right state remains retained. Unknown and losing owner metadata stays dormant; it cannot duplicate character ownership.

## Code and separators

Extend the atomic block-presentation tuples to `["paragraph"]`, `["heading", level]`, `["code", language]`, and `["separator"]`. Heading level remains integral 1…6. Language is an ASCII string of at most 64 bytes matching `[A-Za-z0-9+._-]*`, including empty. Unknown valid JSON discriminants retain v3's opaque fallback; malformed known tuples reject complete admission/preparation.

Code is presentation on an editable owner, not a replacement original rich text. Preserve whitespace, blank lines, original characters, anchors and unknown attributes. Render existing rich marks dormant in code. New literal edits explicitly insert unmarked runs without inheriting adjacent marks; rich-format commands reject code targets before any partial mixed batch. Converting back to paragraph exposes the retained marks. Newline edits inside code remain literal text, not an automatic split into rich blocks. Code split/join is explicit and preserves matching language, original spans and identity; mismatched-language joins reject without mutation. Code-language changes are metadata-only atomic tuples.

A separator is a noneditable presentation on an empty owner. Conversion of nonempty text rejects rather than dropping/hiding user text. Preserve that owner's original identity and empty span; text/mark/split/join targeting the separator returns a typed unsupported-target result. Insert/delete/convert commands must prepare an accessible adjacent paragraph when no visible editable text owner would remain, reserving its fresh identity in the same transaction. Reject resource/identity failure before any live write; no partially committed separator that traps the document. Empty ordinary paragraph/heading/code owners count as editable.

## History, deletion and retained state

Immutable source registrations, nested text identities, container registrations and operation tuples are never removed/replaced to implement undo. `registry-entity-controls` permits reversible local history intents: an atomic enabled tuple hides/reactivates an original/container or disables/reactivates an operation. Permanent tombstones always win over enable. Disabled operations do not replay; their dependent intentions remain retained losing/dormant. Disabling a source preserves its original content as recovery; disabling a container follows the hidden-parent rule; re-enable restores visibility only when valid under the remaining graph. Unknown-yet-valid IDs in controls are retained dormant within the resource bound. Projection never writes enable flags.

Control conflicts use the pinned map tuple rule. Qualification covers disable/enable/duplicate/restore/concurrent control and dependency cases, including edited original content and stable anchors. This proves the history primitive, not selective history grouping. ENG-1.11 must exclude remote/restore/initialize origins, use explicit command group boundaries, limit text/metadata undo scopes so immutable registry/operation rows survive, and use these controls for structural creation/operation history. Undo after remote changes preserves the remote bytes and resolves affected content through the qualified projection; no pretend history by reseeding or copying a document.

## Admission and functional envelope

Retain v3's staging, exact-root/shared-type, immutable-row, binary decode and external recovery policy. Validate all new tuples, namespaces, container/text/origin membership, operation/control shapes and bounds before applying to the live replica. Replacement/removal of immutable original/container registrations, initial placements or operation tuples rejects. Mutable presentation/check/control tuples may change or become absent under their documented defaults. Known incompatible kinds/tuple shapes are not unknown extension data. An unresolved but valid parent/dependency retains its raw intent as specified; malformed values do not gain a fallback pass.

Retained originals plus containers total at most 4096; operations at most 4096; spans at most 8192; controls at most 8192. Hierarchy and dependency depth at most 128, iterative edge visits at most 16777216. Keep v3 limits for source UTF-8/UTF-16 totals, update/checkpoint bytes, JSON/binary depth, structs, IDs, cuts and allocation clocks. Typed resource-limit/recovery is atomic; no omitted nodes or partial mutation. These are functional ceilings, not performance qualification. List indentation accepts root depth zero through depth 128 and rejects a complete batch if any moved descendant exceeds it.

## Qualification and consumption

ENG-1.19 creates `core/fixtures/schema-v4/` and `core/crates/editac-core/tests/structural_profile.rs`: exact ten-root construction, descriptor and Rust/Yjs exchange; nested list/quote/container placements; ordered starts/modes/check state; original/derived owners; empty nodes; place/split/join interactions; hierarchy/cycle/orphan/deleted-parent behavior; mark/anchor identity; control history primitives; malformed/profile/epoch/resource rejection; both directions, seeded replicas, duplicate/reordered delivery and restore. Coverage compares visible tree, recovery, metadata and source identities, not merely binary agreement. Preserve and reuse ENG-1.8-P1's read-only validation evidence; adapt quote/container validation under this profile rather than treating it as persistence proof.

ENG-1.20 separately qualifies code/separator tuples and the complete literal-mark/whitespace/blank-line/conversion/empty-editable-neighbor matrix with the same exact descriptor and real Rust/Yjs exchange. Test invalid languages/levels/nonempty separator targets, code join compatibility, mixed-batch atomic rejection and concurrent metadata/remote edits. Its command-policy fixture is deterministic; no live provider calls.

ENG-1.21 integrates the exact qualified v4 profile in production create/restore/admission, hierarchical projection, anchors and shared prepared place/text/format/structural primitives. It reruns both qualification suites and required legacy/regression families with exact hashes/counts. It does not finish list/quote behaviors (ENG-1.8), code/separator command behaviors (ENG-1.9), move acceptance (ENG-1.10), or history grouping (ENG-1.11). Those parents use this contract and still meet every original criterion. Lists/quotes and code/separators cannot use an unqualified descriptor; the profile is not declared supported until both qualification receipts and the production integration pass. A failed or oversized boundary requires a precise controller repair/split proposal, not an unspecified request for another schema.

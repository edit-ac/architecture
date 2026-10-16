# Wordcraft-derived reliability and qualification cases

Status: planned acceptance, not executed tests. These 19 cases extend existing owners; they add no parent task, runtime dependency, format direction or feature profile. Priority order is failure paths, converter qualification, then cache/command checks. [Research and overlap map](../evidence/wordcraft-research.md) records upstream provenance and the canonical cases reused below.

Use synthetic, nonsensitive fixtures, fixed clocks, prepared host responses and real production boundaries. At failure checkpoints assert content, selection, pending marks, history, revision, emitted updates, durability/receipt state and job-owned resources as applicable. Capture actual work counts as well as outcome. A test may lower a configurable budget to exercise the production rejection path; it must not allocate hundreds of MiB or reproduce a stack overflow. Existing platform qualification policy permits named simulators/emulators/VMs/OS hosts with required runtime evidence. No paid inference, private documents, automatic font downloads or provider recording.

## Recovery rejection and retry — LOC-1.6, CAP-1.5

LOC-1.6 owns the browser case; CAP-1.5 reuses it through the shared lifecycle profile rather than introducing another persistence mechanism.

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-01 | P0 | Recovery snapshot exceeds a small configured cap; tick repeatedly with unchanged content; separately inject quota failure, then change the relevant budget/storage condition | Last valid checkpoint/journal/outbox and unsaved state survive; unchanged permanent rejection does not repeat expensive serialization/write attempts. Transient failures use bounded backoff. Report attempt/serialized/written-byte counts and explicit retry condition; an eligible changed input or repaired condition can recover. No timer-only retry storm or false saved state. |

## Queued mutation expiry — AGT-1.4

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-02 | P0 | Hold an agent apply in a controlled queue until its execution deadline/cancellation, then release; separately lose the response after commit and retry the same request | Expired/cancelled work is rechecked at serialized admission and makes zero mutations. Post-commit timeout cannot roll back or claim clean rejection: existing pending/unknown-durability and durable receipt rules apply. Same ID/payload resolves the original result without duplicate insertion; changed payload rejects. Bound queue/frame/connection work in the host profile. |

## Asynchronous output completion — CNV-1.2

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-03 | P0 | Host starts Save-before-New/Open at revision N; picker cancels, write/close fails, completion is duplicated, or editing advances to N+1 before success | Initiation is not completion. Correlated job/revision outcome gates the host transition; cancel/failure retains the document and recoverable edits. N completion never marks N+1 saved or closes over newer edits. Duplicate/late completion cannot affect another session. Job cleanup does not erase committed assets or the last valid artifact. Conversion receipt is not a journal durability receipt. |

## Native file publication failure — CLI-1.5

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-04 | P0 | Save beside an existing temp file/directory/symlink; two saves collide; inject short write, full disk and replacement failure, including a changed destination fingerprint | Exclusively owned temporary files and stale-target checks preserve original/neighbor bytes and permissions under the declared platform policy. Cleanup removes only this job's temp file. Publication uncertainty stays explicit with recoverable source; no last-writer-wins override of our existing fingerprint contract or invented power-loss guarantee. |

## Direction and completeness reporting — CNV-1.1

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-05 | P0 | Prepared capability profile admits import but not export; invoke Save/export through each advertised host route; separately exhaust output pages/nodes/bytes | Capability failure is actionable and visible; an authorized supported Save As path may be offered. No success/no-op or silent suffix truncation. A partial/lossy artifact requires an explicit declared policy and acknowledgement, never a complete-export receipt. Retain original input and edits. This fixture adds no legacy DOC or PDF import support. |

## Cumulative container and decoder work — CNV-1.4

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-06 | P0 | Many relationships reference the same malformed/oversized image; repeat after aggregate budget exhaustion; nest parser scans that each appear individually bounded | Charge nested work against the job's aggregate budget and remaining allowance before allocation/decode. Cache rejection by immutable input/resource/profile within the job, or equivalent bounded deduplication: no repeated expensive decode for the same rejected resource. Record attempts, actual inflated/decoded bytes, pixels and work units; stop on exhaustion, clean staging and leave live state unchanged. A new eligible job does not inherit an invalid rejection. |
| WCF-07 | P0 | Minimal ZIPs contain duplicate and normalized-alias part names, conflicting relationships, corrupt entries or false declared sizes; permute entry order | Reject ambiguous/invalid required content deterministically before commit; no last-entry-wins result or log-only omission of corrupt content. Actual decoded sizes govern bounds. Unsupported optional content follows complete structured diagnostics and retained-input policy. No external fetch or active-content execution. |

## Recursive paste admission — RCH-1.6

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-08 | P0 | Copy a table and paste it into one of its own cells repeatedly; submit an already over-depth internal/foreign fragment | The existing bounded simple-cell profile rejects unsupported nesting before mutation or staging publication. Assert unchanged identity/content/history; then exercise copy, serialization, undo/redo and disposal without recursive overflow. Test the configured depth boundary with small fixtures; do not expand support to nested or merged tables. |

## Import span admission — CNV-1.5

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-09 | P0 | Synthetic Unicode runs and adapter-produced spans have inconsistent lengths, overflow, split UTF-8 characters or split UTF-16 surrogate pairs; valid astral/combining neighbors are controls | Validate the declared coordinate system and checked arithmetic before producing a semantic batch. Invalid spans reject atomically with diagnostics/source retention; valid text maps exactly to public UTF-16/stable-anchor boundaries. No unchecked indexing, panic recovery as admission, normalization of authored text or partial import. |

## Semantic DOCX fidelity — CNV-1.7

CNV-1.5/1.6 provide the imported projections; CNV-1.7 owns the round-trip assertions and representability reports.

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-10 | P0 | Minimal DOCX wraps a TOC field in block content control `w:sdt` with `w:docPartObj`; compare plain rich-text wrapper and plain paragraph controls | Diagnose unsupported wrapper/field structure explicitly even when visible text survives. Retain original input; any lossy conversion is explicit. Compare semantic structure and report completeness, not text alone. No implied content-control, TOC-editing or opaque-package preservation feature. |
| WCF-11 | P1 | Hand-authored DOCX fixtures vary localized default styles, omitted/empty paragraph defaults, adjacent bullet/numbered lists and unsupported package parts/relationships | Supported semantics survive import/export/re-import, including list type/start and admitted marks/assets; unsupported metadata/relationships are accounted for. Independent package inspection checks references and duplicate IDs. ZIP bytes, incidental generated IDs and Word pagination are not equality oracles; no silent defaults, unknown-part execution or arbitrary round-trip promise. |

## Controlled export font environment — CNV-1.8

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-12 | P1 | Qualify export with an allowlisted, version/hash-pinned font set; remove a required face and vary fallback availability explicitly | Record font/backend versions, licenses and environment. Missing coverage gives the declared diagnostic/fallback or unavailable profile, never a hidden host-font dependency or document-triggered download. Independent target results retain their provenance; screenshot drift alone is not a semantic failure. |

## Independent PDF output oracles — CNV-1.9

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-13 | P0 | Export Arabic lam-alef, mixed RTL/Latin/numbers, ligatures and combining marks with the pinned fonts, including zero-advance glyph behavior where supported | Independently inspect generated PDF logical text/search/copy/reading order and render shaping. Correct pixels cannot excuse reversed/dropped characters; correct text cannot excuse broken placement. Expected strings are hand-authored, with reader/version-specific behavior reported. No PDF input feature or runtime reader dependency. |
| WCF-14 | P1 | Export synthetic long words, explicit breaks, tables and images spanning pages; deliberately perturb a test artifact's clipping, line break or logical text | Use separate semantic/text and visual/layout checks: page count, clipping, line correspondence/position and declared raster tolerances. Negative controls must fail their relevant oracle; a similarity average cannot hide missing lines/pages. Retain diagnostics and pinned reference provenance; no blanket Word pagination or PDF/UA claim. |

## Localized table work — RCH-1.10

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-15 | P1 | Warm several tables, edit one cell, edit an unrelated paragraph, scroll, then change table width/font/zoom; repeat mount/dispose | Assert affected dependency sets and cache hit/miss/measurement/update counts separately from elapsed time. Unrelated tables are not rebuilt; content-only edits recompute only the declared necessary cells/row/column dependencies. Width/font/zoom invalidates the appropriate geometry. Warm output equals cold recomputation; caches stay bounded and disposal releases ownership without semantic writes. |

## Incremental analysis correctness — RCH-1.3

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-16 | P1 | Warm highlight caches; edit one block, undo/redo, switch language/grammar/query/theme version, replace session and return a stale worker result | Incremental spans equal full recomputation for the same pinned input. Record recomputed blocks/work; unchanged dependencies reuse results and changed keys invalidate them. Stale results cannot publish, cross-session identity cannot alias, retained data is bounded, and analysis creates no CRDT/history changes. No proofing/dictionary service added. |

## Command inventory integrity — FIT-1.2

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-17 | P1 | Build the claimed command/surface matrix from existing descriptors and host bindings; inject missing command IDs, duplicate/conflicting aliases, unavailable direction and stale evidence | Static checks detect inconsistent advertisements without a second handwritten semantic registry. Available/enabled/authorized/qualified remain distinct; unsupported routes are explicit. Registration alone never reports support. CMD-01 supplies actual equivalence/no-op/history evidence on each claimed surface; hosts recheck authority at activation. |

## Dependency-graph guard sensitivity — FIT-1.1

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-18 | P1 | Feed Cargo/JS graph fixtures with an unclassified production package, optional codec/font dependency reachable from baseline, or test helper as a runtime dependency | Every forbidden edge/classification fails through the real graph adapter; allowed optional/test-only controls pass. Inspect transitive/default-feature reachability and declared target profiles, not names alone. No production engine/UI coupling or extra baseline assets; preserve current bundle caps. |

## Changed-field formatting dialogs — INT-1.3

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| WCF-19 | P1 | Open an existing/claimed property dialog or formatting surface on forward/backward mixed formatting; accept unchanged, change one field, cancel, or change target revision/permission while open | Mixed/unrepresented properties remain intact. Unchanged/cancel creates zero edits/history; one intentional changed-field batch creates one undo group and restores all prior properties on undo. Stale/unauthorized targets reject or follow existing explicit revalidation policy, never retarget the latest caret. Pending marks and a next typed sentinel agree with the formatting contract. |

## Existing cases reused without new IDs

REG-01/REG-02/REG-05 carry nested-command, selection-replacement and pending-mark variants; CMD-01 carries surface equivalence. PST-05 already owns failed-cut preservation; KEY-06 owns AltGr/non-US shortcuts; EVT-03/EVT-04 own the composition lifecycle; NCL-16/NCL-20 and TBL-03 own structural clipboard outcomes. Use the linked catalogs and existing owners rather than parallel Wordcraft-only versions. Existing case variants are refined in place where needed. Offline proofing remains deferred.

# Wordcraft research and planning amendment

Reviewed 2026-10-16 at [eae242176108d328c5dd81fbc10370c51ab90706](https://github.com/storytold/wordcraft/commit/eae242176108d328c5dd81fbc10370c51ab90706). The issue inventory contained 1,025 issues (567 open); selected source, tests and issue reports were inspected. This is source research and planned acceptance, not a Wordcraft build, reproduced vulnerability, measured benchmark, or edit.ac runtime qualification. Issue states below reflect that snapshot; some reports are explicitly static audits.

## Authorized scope and priority

The user requested strengthening existing roadmaps and test scenarios, prioritizing failure paths, converter qualification and cache/command checks. [Nineteen new cases](../tests/wordcraft-regression-cases.md) join the existing suite and existing parent ownership. No new roadmap, parent task, dependency edge, runtime package or supported format is introduced. Offline proofing remains deferred. Existing progress/checkmarks and historical evidence are not rewritten; added cases and changed variants require their own matching-revision execution evidence.

1. Failure paths: retry/work bounds, queue expiry versus post-commit uncertainty, output completion, native publication, completeness diagnostics, hostile containers, nesting and spans.
2. Conversion qualification: semantic subset/unsupported reports, hand-authored packages, controlled fonts, independent PDF text and visual oracles.
3. Cache/command checks: affected-work counters, cold/incremental equivalence, capability-to-route consistency, dependency guard sensitivity and changed-field dialogs.

This priority does not reorder active runner queues or bypass prerequisites. Controllers adopt amended sources at a safe checkpoint, map prior evidence to unchanged acceptance only, and schedule the added cases under their existing owners. A completed parent does not imply these later cases passed. Do not restart a worker merely because a planning source changed.

## Implementation references and architectural fit

| Reference at reviewed commit | Technique | edit.ac boundary |
|---|---|---|
| [Image resource importer](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/docbin/src/media.rs) | Cache failed as well as successful resources; use remaining allowance before decode/copy | Borrow the bounded-work technique for optional admitted formats/assets, not legacy DOC support |
| [Layout cache tests](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/layout/src/tests.rs#L1344-L1377) | Assert cache misses and retained per-cell layouts | Existing table/highlight projections, stable identities and versioned dependencies; no general typesetter |
| [Mixed property tests](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/ui-egui/src/dialogs.rs#L3861-L3900) | Only changed properties commit; unchanged acceptance is a no-op | Existing prepared batch, target revalidation and local history |
| [Synthetic DOCX packages](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/docx/tests/passthrough.rs) | Isolate defaults, numbering and unsupported structures | Compare supported semantics and complete diagnostics; retain original input |
| [PDF comparison tooling](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/xtask/src/visual_diff.rs) | Separate text/line geometry and raster evidence | Generated-export validation only; no PDF importer/runtime reader |
| [Async saves](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/ui-egui/src/async_saves.rs), [safe-save tests](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/engine/tests/safe_save.rs) | Completion tickets and owned temporary files | Host file lifecycle, separate from durable journal receipts; retain our stale-file protection |
| [Registry](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/engine/src/lib.rs), [layer checker](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/xtask/src/layers.rs) | Derive coverage/graph checks from actual metadata | Reuse existing descriptors and capability evidence; no second semantic registry |

Wordcraft's Arc-shared mutable tree, byte/path positions and snapshot undo do not replace Yrs, UTF-16 public boundaries, stable anchors or prepare/validate/commit. Its package reader skips some unreadable entries and inserts named parts into a map; do not inherit log-only loss or ambiguous duplicate handling. Its [gap assessment](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/docs/gaps.md) acknowledges missing real-world corpus qualification. Source availability and feature registration are not fidelity proof. The [NOTICE](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/NOTICE) offers MIT or Apache-2.0 for code, with separate third-party/branding terms; this amendment imports no code/assets and approves no dependency.

## Issue provenance and overlap

| Upstream issue | Snapshot state/evidence | Case or existing coverage |
|---|---|---|
| [#2456](https://github.com/storytold/wordcraft/issues/2456) repeated oversized recovery writes | Open; reported measured reproduction | WCF-01 |
| [#1331](https://github.com/storytold/wordcraft/issues/1331) timed-out queued edits | Open; static audit | WCF-02; existing AGT receipt boundary remains authoritative |
| [#1315](https://github.com/storytold/wordcraft/issues/1315) asynchronous save-before-open | Closed; initial static audit, current completion-ticket source inspected | WCF-03 |
| [Safe-save implementation/tests](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/engine/tests/safe_save.rs) | Source/test inspection only | WCF-04; extends CLI-1.5 failures |
| [#2445](https://github.com/storytold/wordcraft/issues/2445) import-only Save, [#1341](https://github.com/storytold/wordcraft/issues/1341) silent limit truncation | Open; user reproduction / static audit respectively | WCF-05; no legacy DOC scope |
| [#1334](https://github.com/storytold/wordcraft/issues/1334) repeated rejected-image decode, [#1336](https://github.com/storytold/wordcraft/issues/1336) nested uncharged parser work | Closed / open; initial static audits | WCF-06; actual codec budgets, no replacement Markdown parser |
| [Package reader](https://github.com/storytold/wordcraft/blob/eae242176108d328c5dd81fbc10370c51ab90706/crates/docx/src/package.rs#L167-L204) | Source inspection | WCF-07 sharpens already required duplicate/hostile-container policy |
| [#1596](https://github.com/storytold/wordcraft/issues/1596) self-paste nesting | Open; reported CLI reproduction | WCF-08; reject outside simple-cell profile |
| [#1337](https://github.com/storytold/wordcraft/issues/1337) invalid imported run boundaries | Closed; initial static audit | WCF-09; reinforces existing UTF-16 admission |
| [#2427](https://github.com/storytold/wordcraft/issues/2427) dropped TOC content-control wrapper | Open; minimal synthetic package reproduction | WCF-10/11; diagnostics, not added TOC/package fidelity |
| [#2310](https://github.com/storytold/wordcraft/issues/2310) correct-looking Arabic PDF with wrong logical text | Open; font/reader-specific reproduction | WCF-12/13/14 |
| [#811](https://github.com/storytold/wordcraft/issues/811) large-table scrolling, reviewed cache tests | Closed; user report and source inspection | WCF-15/16; synthetic fixtures, not attached private files |
| [#2420](https://github.com/storytold/wordcraft/issues/2420) queued background UI input ignored | Open; reported reproduction | WCF-17 and CMD-01: semantic command success must be observed; synthetic UI delivery is a distinct capability |
| [#1346](https://github.com/storytold/wordcraft/issues/1346) untouched mixed formatting overwritten | Closed; initial static audit, current test inspected | WCF-19 |
| [#1363](https://github.com/storytold/wordcraft/issues/1363), [#419](https://github.com/storytold/wordcraft/issues/419), [#424](https://github.com/storytold/wordcraft/issues/424) undo grouping/pending marks | Closed; static audit / reported reproductions | Refine REG-01/REG-02/REG-05; adapt pending-mark behavior to our no-history toggle and successful-history-navigation contract, not Wordcraft snapshot undo |
| [#2423](https://github.com/storytold/wordcraft/issues/2423), [#2398](https://github.com/storytold/wordcraft/issues/2398) multiline/plain and table clipboard loss | Open; reported reproductions | Refine PST-03 and TBL-03, reuse NCL-16/NCL-20 |
| [#1265](https://github.com/storytold/wordcraft/issues/1265), [#2388](https://github.com/storytold/wordcraft/issues/2388), [#1888](https://github.com/storytold/wordcraft/issues/1888) failed cut, AltGr, IME overlap | Closed / open / open; reported failures | Reuse PST-05, KEY-06 and EVT-03/EVT-04; refine the existing geometry/shortcut variants |

## Validation scope

`npm run check` validates roadmap structure, case ownership/counts, fixture metadata and planning-validator contracts only. Runtime execution remains with the mapped owners and their separate progress. New cases have no execution receipts in this amendment. Preserve all failed/skipped historical results, the existing baseline bundle caps, optional converter boundaries and export-only PDF policy.

Planning validation passed on 2026-10-16: 42 roadmaps, 558 parents, 1,693 checkboxes; 324 catalog cases, 14 recipes and 14 guards; 14 planning-validator tests passed, zero failures/skips. [Validation record](wordcraft-planning/validation.json) and [check log](wordcraft-planning/check.log) retain commands, scope and source hashes. These counts do not report runtime execution of the new scenarios.

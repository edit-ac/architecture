# One durable format, then feature completeness

User decision, 2026-10-23: use one current production document/API contract until publication, preserve durable data and regressions, update guides/roadmaps, and do not let size tuning hold independent features. One serial Roadmap Runner in `/Users/bpstr/Github/edit-ac` on existing main branches; no new workspace, worktree, parallel lane or subagent.

[Decision 006](../../decisions/006-single-format-before-publication.md) and the [durability contract](../../specs/document-durability.md) govern this successor to stopped run `f6915e733a5ecb9c1c64e7ff`. Its progress, accepted RWP-1.1/G1–G7 evidence and interrupted G8/dirty source are preserved. Queue construction, source validation and the initial current-format API do not claim that runtime cleanup is complete.

The canonical identity keeps `editac.registry.editor.v5` / `editac.yrs-yjs.editor.v5`, protocol 1, update encoding 1 and UTF-16. The schema suffix does not require a second reader. Historical layouts remain test/oracle references. Port semantic regressions instead of dropping them; old/future input must reject before mutation and retain recovery bytes. Do not create a runtime legacy flag or silently relabel/migrate/reseed development data. Identify actual data before designing a necessary explicit offline conversion.

Order: authenticate preserved source/data; complete current admission/replay/projection/commands/consumer cutover and a focused user-required durability gate; close the audited table/journal/structural-lifetime defects and deliver shared block conversion, extensions and configurable menus; finish native/terminal feature projections; then bounded remaining optimization; finally full functional/virtual-runtime suites and unchanged performance/size/resource gates. The targeted cutover gate is a technical prerequisite for safely using the changed shared data contract, not a broad test campaign before all features. Full suites and comprehensive test development retain their final owners.

Each optimization batch ends after 45 minutes or two materially different measured hypotheses, whichever occurs first. A batch may complete with an honest unresolved measurement and precise final-test owner; it cannot claim a hard-budget pass. Required 512 KiB total/32 KiB JS gzip caps and native tail/resource limits are not weakened. No repeated unchanged failed benchmark, receipt reconstruction or speculative old-version optimization. Data-safety/correctness and required missing APIs remain real local blockers.

The copied original native/terminal predicate map remains complete; profile-specific legacy runtime clauses are superseded by the current-format decision while their useful behaviors stay covered. Only one final testing owner executes each requirement. Source files remain bounded/controller-owned; progress, runtime matrices, samples and reports stay separate and ignored. The first source adapts existing collectors to this successor manifest rather than duplicating them. Existing required full-suite tests are never silently removed as out-of-profile.

Physical-only qualification, paid inference/credentials/proxies, cloud provisioning, optional encrypted/cloud release claims, push/publication/deployment and external integrations remain excluded. Real user revision history, external format support and necessary distinct protocol/ABI/encoding validation remain required. Appropriate simulator/emulator/OS-host proof is still mandatory for actual target claims. On a concrete unavailable dependency, continue independent local tasks; if none is ready, record a fingerprint and exact changed-input condition and stop the controller via the guard.

## Ordered sources

| Order | Source | Phase | Parents |
| --- | --- | --- | ---: |
| 1 | [00-source-and-data-handoff.md](00-source-and-data-handoff.md) | inventory | 2 |
| 2 | [01-canonical-admission-and-replay.md](01-canonical-admission-and-replay.md) | implementation | 3 |
| 3 | [01b-durable-tables-and-lifetime.md](01b-durable-tables-and-lifetime.md) | implementation | 5 |
| 4 | [02-canonical-projection-and-consumers.md](02-canonical-projection-and-consumers.md) | implementation | 3 |
| 5 | [02b-shared-block-actions.md](02b-shared-block-actions.md) | implementation | 5 |
| 6 | [03-regression-oracles-and-version-scaffolding.md](03-regression-oracles-and-version-scaffolding.md) | implementation | 6 |
| 7 | [04-durability-gate-and-guide-handoff.md](04-durability-gate-and-guide-handoff.md) | gate | 2 |
| 8 | [05-macos-input-part-1.md](05-macos-input-part-1.md) | implementation | 5 |
| 9 | [06-macos-input-part-2.md](06-macos-input-part-2.md) | implementation | 3 |
| 10 | [07-macos-rich-content.md](07-macos-rich-content.md) | implementation | 5 |
| 11 | [08-macos-lifecycle.md](08-macos-lifecycle.md) | implementation | 5 |
| 12 | [09-macos-extensions-package-part-1.md](09-macos-extensions-package-part-1.md) | implementation | 4 |
| 13 | [10-macos-extensions-package-part-2.md](10-macos-extensions-package-part-2.md) | implementation | 4 |
| 14 | [11-macos-extensions-package-part-3.md](11-macos-extensions-package-part-3.md) | implementation | 2 |
| 15 | [12-ios-input-part-1.md](12-ios-input-part-1.md) | implementation | 5 |
| 16 | [13-ios-input-part-2.md](13-ios-input-part-2.md) | implementation | 3 |
| 17 | [14-ios-rich-content.md](14-ios-rich-content.md) | implementation | 5 |
| 18 | [15-ios-lifecycle.md](15-ios-lifecycle.md) | implementation | 5 |
| 19 | [16-ios-extensions-package-part-1.md](16-ios-extensions-package-part-1.md) | implementation | 4 |
| 20 | [17-ios-extensions-package-part-2.md](17-ios-extensions-package-part-2.md) | implementation | 4 |
| 21 | [18-ios-extensions-package-part-3.md](18-ios-extensions-package-part-3.md) | implementation | 2 |
| 22 | [19-android-input-part-1.md](19-android-input-part-1.md) | implementation | 5 |
| 23 | [20-android-input-part-2.md](20-android-input-part-2.md) | implementation | 3 |
| 24 | [21-android-rich-content.md](21-android-rich-content.md) | implementation | 5 |
| 25 | [22-android-lifecycle.md](22-android-lifecycle.md) | implementation | 5 |
| 26 | [23-android-extensions-package-part-1.md](23-android-extensions-package-part-1.md) | implementation | 4 |
| 27 | [24-android-extensions-package-part-2.md](24-android-extensions-package-part-2.md) | implementation | 4 |
| 28 | [25-android-extensions-package-part-3.md](25-android-extensions-package-part-3.md) | implementation | 2 |
| 29 | [26-windows-input-part-1.md](26-windows-input-part-1.md) | implementation | 5 |
| 30 | [27-windows-input-part-2.md](27-windows-input-part-2.md) | implementation | 3 |
| 31 | [28-windows-rich-content.md](28-windows-rich-content.md) | implementation | 5 |
| 32 | [29-windows-lifecycle.md](29-windows-lifecycle.md) | implementation | 5 |
| 33 | [30-windows-extensions-package-part-1.md](30-windows-extensions-package-part-1.md) | implementation | 4 |
| 34 | [31-windows-extensions-package-part-2.md](31-windows-extensions-package-part-2.md) | implementation | 4 |
| 35 | [32-windows-extensions-package-part-3.md](32-windows-extensions-package-part-3.md) | implementation | 2 |
| 36 | [33-linux-input-part-1.md](33-linux-input-part-1.md) | implementation | 5 |
| 37 | [34-linux-input-part-2.md](34-linux-input-part-2.md) | implementation | 3 |
| 38 | [35-linux-rich-content.md](35-linux-rich-content.md) | implementation | 5 |
| 39 | [36-linux-lifecycle.md](36-linux-lifecycle.md) | implementation | 5 |
| 40 | [37-linux-extensions-package-part-1.md](37-linux-extensions-package-part-1.md) | implementation | 4 |
| 41 | [38-linux-extensions-package-part-2.md](38-linux-extensions-package-part-2.md) | implementation | 4 |
| 42 | [39-linux-extensions-package-part-3.md](39-linux-extensions-package-part-3.md) | implementation | 2 |
| 43 | [40-terminal-recovery.md](40-terminal-recovery.md) | implementation | 4 |
| 44 | [41-terminal-extensions.md](41-terminal-extensions.md) | implementation | 5 |
| 45 | [42-bounded-remaining-optimization.md](42-bounded-remaining-optimization.md) | implementation | 3 |
| 46 | [43-full-shared-suites.md](43-full-shared-suites.md) | testing | 4 |
| 47 | [44-full-web-suites-part-1.md](44-full-web-suites-part-1.md) | testing | 5 |
| 48 | [45-full-web-suites-part-2.md](45-full-web-suites-part-2.md) | testing | 3 |
| 49 | [46-full-macos-suites.md](46-full-macos-suites.md) | testing | 5 |
| 50 | [47-full-ios-suites.md](47-full-ios-suites.md) | testing | 5 |
| 51 | [48-full-android-suites.md](48-full-android-suites.md) | testing | 5 |
| 52 | [49-full-windows-suites.md](49-full-windows-suites.md) | testing | 5 |
| 53 | [50-full-linux-suites.md](50-full-linux-suites.md) | testing | 5 |
| 54 | [51-full-terminal-suites.md](51-full-terminal-suites.md) | testing | 2 |
| 55 | [52-full-performance-part-1.md](52-full-performance-part-1.md) | testing | 5 |
| 56 | [53-full-performance-part-2.md](53-full-performance-part-2.md) | testing | 1 |
| 57 | [54-aggregate-readiness.md](54-aggregate-readiness.md) | testing | 3 |

Total: 57 bounded sources / 226 parents. All original 155 native parents and preserved terminal predicates retain implementation/testing ownership. No original source/progress is rewritten into a fictitious passing result.

## Adopted alpha audit

The [alpha audit map](../alpha-block-actions-20261023/README.md) is now integrated into this existing queue: 16 additional parents and 10 mandatory requirement rows. No additional controller is needed. The two expanded shared sources are split into adjacent bounded entries 01/01b and 02/02b, preserving every task ID and acceptance clause. Files 01–04 deliver durable data and block actions before the native feature phase; files 43–51 verify shared, browser and platform behavior; file 54 refuses alpha readiness until the audit rows and all original gates pass. The opening source and its progress were not edited by this adoption. Future workers load these revised sources when their existing FIFO entries start.

## Completed handoff recovery

Run `6bd65538752cad53b001fcb8` was stopped after a self-invalidating source-summary loop. SFC-1.1/1.2 are verified in their existing progress and receipts; runtime cutover remains pending. Resume this same serial workspace queue at source 01. Workers update only checkboxes and Status in source files. Source hashes, delivery prose and reconciliation records belong in separate progress/ignored receipts. The event guard stops repeated completed-source reconciliations as well as BLOCKED workers.

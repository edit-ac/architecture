# One durable format, then feature completeness

User decision, 2026-10-23: use one current production document/API contract until publication, preserve durable data and regressions, update guides/roadmaps, and do not let size tuning hold independent features. One serial Roadmap Runner in `/Users/bpstr/Github/edit-ac` on existing main branches; no new workspace, worktree, parallel lane or subagent.

[Decision 006](../../decisions/006-single-format-before-publication.md) and the [durability contract](../../specs/document-durability.md) govern this successor to stopped run `f6915e733a5ecb9c1c64e7ff`. Its progress, accepted RWP-1.1/G1–G7 evidence and interrupted G8/dirty source are preserved. Queue construction, source validation and the initial current-format API do not claim that runtime cleanup is complete.

The canonical identity keeps `editac.registry.editor.v5` / `editac.yrs-yjs.editor.v5`, protocol 1, update encoding 1 and UTF-16. The schema suffix does not require a second reader. Historical layouts remain test/oracle references. Port semantic regressions instead of dropping them; old/future input must reject before mutation and retain recovery bytes. Do not create a runtime legacy flag or silently relabel/migrate/reseed development data. Identify actual data before designing a necessary explicit offline conversion.

Order: authenticate preserved source/data; complete current admission/replay/projection/commands/consumer cutover and a focused user-required durability gate; finish native/terminal feature projections; then bounded remaining optimization; finally full functional/virtual-runtime suites and unchanged performance/size/resource gates. The targeted cutover gate is a technical prerequisite for safely using the changed shared data contract, not a broad test campaign before all features. Full suites and comprehensive test development retain their final owners.

Each optimization batch ends after 45 minutes or two materially different measured hypotheses, whichever occurs first. A batch may complete with an honest unresolved measurement and precise final-test owner; it cannot claim a hard-budget pass. Required 512 KiB total/32 KiB JS gzip caps and native tail/resource limits are not weakened. No repeated unchanged failed benchmark, receipt reconstruction or speculative old-version optimization. Data-safety/correctness and required missing APIs remain real local blockers.

The copied original native/terminal predicate map remains complete; profile-specific legacy runtime clauses are superseded by the current-format decision while their useful behaviors stay covered. Only one final testing owner executes each requirement. Source files remain bounded/controller-owned; progress, runtime matrices, samples and reports stay separate and ignored. The first source adapts existing collectors to this successor manifest rather than duplicating them. Existing required full-suite tests are never silently removed as out-of-profile.

Physical-only qualification, paid inference/credentials/proxies, cloud provisioning, optional encrypted/cloud release claims, push/publication/deployment and external integrations remain excluded. Real user revision history, external format support and necessary distinct protocol/ABI/encoding validation remain required. Appropriate simulator/emulator/OS-host proof is still mandatory for actual target claims. On a concrete unavailable dependency, continue independent local tasks; if none is ready, record a fingerprint and exact changed-input condition and stop the controller via the guard.

## Ordered sources

| Order | Source | Phase | Parents |
| --- | --- | --- | ---: |
| 1 | [00-source-and-data-handoff.md](00-source-and-data-handoff.md) | inventory | 2 |
| 2 | [01-canonical-admission-and-replay.md](01-canonical-admission-and-replay.md) | implementation | 3 |
| 3 | [02-canonical-projection-and-consumers.md](02-canonical-projection-and-consumers.md) | implementation | 3 |
| 4 | [03-regression-oracles-and-version-scaffolding.md](03-regression-oracles-and-version-scaffolding.md) | implementation | 3 |
| 5 | [04-durability-gate-and-guide-handoff.md](04-durability-gate-and-guide-handoff.md) | gate | 2 |
| 6 | [05-macos-input-part-1.md](05-macos-input-part-1.md) | implementation | 5 |
| 7 | [06-macos-input-part-2.md](06-macos-input-part-2.md) | implementation | 3 |
| 8 | [07-macos-rich-content.md](07-macos-rich-content.md) | implementation | 5 |
| 9 | [08-macos-lifecycle.md](08-macos-lifecycle.md) | implementation | 5 |
| 10 | [09-macos-extensions-package-part-1.md](09-macos-extensions-package-part-1.md) | implementation | 4 |
| 11 | [10-macos-extensions-package-part-2.md](10-macos-extensions-package-part-2.md) | implementation | 4 |
| 12 | [11-macos-extensions-package-part-3.md](11-macos-extensions-package-part-3.md) | implementation | 2 |
| 13 | [12-ios-input-part-1.md](12-ios-input-part-1.md) | implementation | 5 |
| 14 | [13-ios-input-part-2.md](13-ios-input-part-2.md) | implementation | 3 |
| 15 | [14-ios-rich-content.md](14-ios-rich-content.md) | implementation | 5 |
| 16 | [15-ios-lifecycle.md](15-ios-lifecycle.md) | implementation | 5 |
| 17 | [16-ios-extensions-package-part-1.md](16-ios-extensions-package-part-1.md) | implementation | 4 |
| 18 | [17-ios-extensions-package-part-2.md](17-ios-extensions-package-part-2.md) | implementation | 4 |
| 19 | [18-ios-extensions-package-part-3.md](18-ios-extensions-package-part-3.md) | implementation | 2 |
| 20 | [19-android-input-part-1.md](19-android-input-part-1.md) | implementation | 5 |
| 21 | [20-android-input-part-2.md](20-android-input-part-2.md) | implementation | 3 |
| 22 | [21-android-rich-content.md](21-android-rich-content.md) | implementation | 5 |
| 23 | [22-android-lifecycle.md](22-android-lifecycle.md) | implementation | 5 |
| 24 | [23-android-extensions-package-part-1.md](23-android-extensions-package-part-1.md) | implementation | 4 |
| 25 | [24-android-extensions-package-part-2.md](24-android-extensions-package-part-2.md) | implementation | 4 |
| 26 | [25-android-extensions-package-part-3.md](25-android-extensions-package-part-3.md) | implementation | 2 |
| 27 | [26-windows-input-part-1.md](26-windows-input-part-1.md) | implementation | 5 |
| 28 | [27-windows-input-part-2.md](27-windows-input-part-2.md) | implementation | 3 |
| 29 | [28-windows-rich-content.md](28-windows-rich-content.md) | implementation | 5 |
| 30 | [29-windows-lifecycle.md](29-windows-lifecycle.md) | implementation | 5 |
| 31 | [30-windows-extensions-package-part-1.md](30-windows-extensions-package-part-1.md) | implementation | 4 |
| 32 | [31-windows-extensions-package-part-2.md](31-windows-extensions-package-part-2.md) | implementation | 4 |
| 33 | [32-windows-extensions-package-part-3.md](32-windows-extensions-package-part-3.md) | implementation | 2 |
| 34 | [33-linux-input-part-1.md](33-linux-input-part-1.md) | implementation | 5 |
| 35 | [34-linux-input-part-2.md](34-linux-input-part-2.md) | implementation | 3 |
| 36 | [35-linux-rich-content.md](35-linux-rich-content.md) | implementation | 5 |
| 37 | [36-linux-lifecycle.md](36-linux-lifecycle.md) | implementation | 5 |
| 38 | [37-linux-extensions-package-part-1.md](37-linux-extensions-package-part-1.md) | implementation | 4 |
| 39 | [38-linux-extensions-package-part-2.md](38-linux-extensions-package-part-2.md) | implementation | 4 |
| 40 | [39-linux-extensions-package-part-3.md](39-linux-extensions-package-part-3.md) | implementation | 2 |
| 41 | [40-terminal-recovery.md](40-terminal-recovery.md) | implementation | 4 |
| 42 | [41-terminal-extensions.md](41-terminal-extensions.md) | implementation | 5 |
| 43 | [42-bounded-remaining-optimization.md](42-bounded-remaining-optimization.md) | implementation | 3 |
| 44 | [43-full-shared-suites.md](43-full-shared-suites.md) | testing | 2 |
| 45 | [44-full-web-suites-part-1.md](44-full-web-suites-part-1.md) | testing | 5 |
| 46 | [45-full-web-suites-part-2.md](45-full-web-suites-part-2.md) | testing | 2 |
| 47 | [46-full-macos-suites.md](46-full-macos-suites.md) | testing | 5 |
| 48 | [47-full-ios-suites.md](47-full-ios-suites.md) | testing | 5 |
| 49 | [48-full-android-suites.md](48-full-android-suites.md) | testing | 5 |
| 50 | [49-full-windows-suites.md](49-full-windows-suites.md) | testing | 5 |
| 51 | [50-full-linux-suites.md](50-full-linux-suites.md) | testing | 5 |
| 52 | [51-full-terminal-suites.md](51-full-terminal-suites.md) | testing | 2 |
| 53 | [52-full-performance-part-1.md](52-full-performance-part-1.md) | testing | 5 |
| 54 | [53-full-performance-part-2.md](53-full-performance-part-2.md) | testing | 1 |
| 55 | [54-aggregate-readiness.md](54-aggregate-readiness.md) | testing | 3 |

Total: 55 bounded sources / 210 parents. All original 155 native parents and preserved terminal predicates retain implementation/testing ownership. No original source/progress is rewritten into a fictitious passing result.

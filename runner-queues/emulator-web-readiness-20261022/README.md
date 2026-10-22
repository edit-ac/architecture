# Single-workspace native and web readiness queue

User instruction, 2026-10-22: queue the reviewed remaining work and run one controller directly in `/Users/bpstr/Github/edit-ac` on its current main branches (the user's master). No worktrees, parallel lanes, delegated agents or second workspace run.

This controller index is not a worker source. Pass only the current bounded Markdown source to the runner. `manifest.json` records ordered files, exact source hashes, separate ignored progress paths and entry evidence. `requirement-map.json` preserves each native/terminal originating parent, original feature acceptance and unique final testing owner. These are authored requirements, not passing test reports.

Sequence: reconcile current deliveries and virtual-runtime prerequisites; repair measured web/native hotspots; deliver missing native input, rich content, lifecycle, extension and package features; finish terminal/shared-client gaps; then run the complete shared/web/native/terminal suites, performance/size/resource gates and final aggregate reconciliation. Native feature projections authenticate existing applicable implementations before doing work, so later deliveries supersede stale blocked snapshots. Original roadmap checkboxes/progress and all original acceptance remain intact. All comprehensive test development and campaign work is after functional files.

Scope covers web, iOS/iPadOS simulators, Android emulators and macOS/Windows/Linux OS hosts or VMs, plus full existing shared/terminal suites. Actual required virtual OS behavior is mandatory. Physical-only observations are deferred and unclaimed. Optional encrypted/cloud release profiles, publishing, pushes, deployment, external service provisioning and paid inference are excluded; this never removes discovered required tests or baseline safety checks. Prepared AI fixtures establish integration mechanics only.

The 137 transferred task rows and referenced cases are reconciled by RRD-1.1 and QRD-1.2; target behavior is tested once by its named QWB/native/QPF owner. A known unavailable required VM/OS profile blocks only dependent assertions and remains explicitly unproven. Within a source, independent tasks proceed; if none remains, the controller stops at the completed BLOCKED worker rather than retrying unchanged. A serial FIFO cannot advance past an incomplete source: preserve later queued work and give the controller an exact prerequisite/repair resume condition. Do not fake a pass to advance.

Every task names its actual prerequisite evidence; local Dependencies fields contain only IDs within the same source. Earlier-file inputs live in the bounded ignored readiness matrix. Missing unrelated release labels cannot block implemented feature wiring. The queue uses existing dispatchers; missing required tests are built by their final testing owner. Full suites are required, with exact current-source compatible results reused instead of repeated for each task.

Generated progress, runtime matrix, binaries, screenshots, samples and logs stay in ignored task-owned directories. Preserve concise counts, source/runtime pins and active failure dispositions; do not commit generated evidence. Normal source commits remain on the existing main branches at two-parent/source boundaries. No remote operation is authorized.

## Ordered sources

| Order | Source | Phase | Parents |
| --- | --- | --- | ---: |
| 1 | [00-reconcile.md](00-reconcile.md) | inventory | 3 |
| 2 | [01-web-performance-repairs.md](01-web-performance-repairs.md) | implementation | 3 |
| 3 | [02-native-performance-repairs.md](02-native-performance-repairs.md) | implementation | 3 |
| 4 | [03-macos-input-part-1.md](03-macos-input-part-1.md) | implementation | 5 |
| 5 | [04-macos-input-part-2.md](04-macos-input-part-2.md) | implementation | 3 |
| 6 | [05-macos-rich-content.md](05-macos-rich-content.md) | implementation | 5 |
| 7 | [06-macos-lifecycle.md](06-macos-lifecycle.md) | implementation | 5 |
| 8 | [07-macos-extensions-package-part-1.md](07-macos-extensions-package-part-1.md) | implementation | 4 |
| 9 | [08-macos-extensions-package-part-2.md](08-macos-extensions-package-part-2.md) | implementation | 4 |
| 10 | [09-macos-extensions-package-part-3.md](09-macos-extensions-package-part-3.md) | implementation | 2 |
| 11 | [10-ios-input-part-1.md](10-ios-input-part-1.md) | implementation | 5 |
| 12 | [11-ios-input-part-2.md](11-ios-input-part-2.md) | implementation | 3 |
| 13 | [12-ios-rich-content.md](12-ios-rich-content.md) | implementation | 5 |
| 14 | [13-ios-lifecycle.md](13-ios-lifecycle.md) | implementation | 5 |
| 15 | [14-ios-extensions-package-part-1.md](14-ios-extensions-package-part-1.md) | implementation | 4 |
| 16 | [15-ios-extensions-package-part-2.md](15-ios-extensions-package-part-2.md) | implementation | 4 |
| 17 | [16-ios-extensions-package-part-3.md](16-ios-extensions-package-part-3.md) | implementation | 2 |
| 18 | [17-android-input-part-1.md](17-android-input-part-1.md) | implementation | 5 |
| 19 | [18-android-input-part-2.md](18-android-input-part-2.md) | implementation | 3 |
| 20 | [19-android-rich-content.md](19-android-rich-content.md) | implementation | 5 |
| 21 | [20-android-lifecycle.md](20-android-lifecycle.md) | implementation | 5 |
| 22 | [21-android-extensions-package-part-1.md](21-android-extensions-package-part-1.md) | implementation | 4 |
| 23 | [22-android-extensions-package-part-2.md](22-android-extensions-package-part-2.md) | implementation | 4 |
| 24 | [23-android-extensions-package-part-3.md](23-android-extensions-package-part-3.md) | implementation | 2 |
| 25 | [24-windows-input-part-1.md](24-windows-input-part-1.md) | implementation | 5 |
| 26 | [25-windows-input-part-2.md](25-windows-input-part-2.md) | implementation | 3 |
| 27 | [26-windows-rich-content.md](26-windows-rich-content.md) | implementation | 5 |
| 28 | [27-windows-lifecycle.md](27-windows-lifecycle.md) | implementation | 5 |
| 29 | [28-windows-extensions-package-part-1.md](28-windows-extensions-package-part-1.md) | implementation | 4 |
| 30 | [29-windows-extensions-package-part-2.md](29-windows-extensions-package-part-2.md) | implementation | 4 |
| 31 | [30-windows-extensions-package-part-3.md](30-windows-extensions-package-part-3.md) | implementation | 2 |
| 32 | [31-linux-input-part-1.md](31-linux-input-part-1.md) | implementation | 5 |
| 33 | [32-linux-input-part-2.md](32-linux-input-part-2.md) | implementation | 3 |
| 34 | [33-linux-rich-content.md](33-linux-rich-content.md) | implementation | 5 |
| 35 | [34-linux-lifecycle.md](34-linux-lifecycle.md) | implementation | 5 |
| 36 | [35-linux-extensions-package-part-1.md](35-linux-extensions-package-part-1.md) | implementation | 4 |
| 37 | [36-linux-extensions-package-part-2.md](36-linux-extensions-package-part-2.md) | implementation | 4 |
| 38 | [37-linux-extensions-package-part-3.md](37-linux-extensions-package-part-3.md) | implementation | 2 |
| 39 | [38-terminal-recovery.md](38-terminal-recovery.md) | implementation | 4 |
| 40 | [39-terminal-extensions.md](39-terminal-extensions.md) | implementation | 5 |
| 41 | [40-full-shared-suites.md](40-full-shared-suites.md) | testing | 2 |
| 42 | [41-full-web-suites-part-1.md](41-full-web-suites-part-1.md) | testing | 5 |
| 43 | [42-full-web-suites-part-2.md](42-full-web-suites-part-2.md) | testing | 2 |
| 44 | [43-full-macos-suites.md](43-full-macos-suites.md) | testing | 5 |
| 45 | [44-full-ios-suites.md](44-full-ios-suites.md) | testing | 5 |
| 46 | [45-full-android-suites.md](45-full-android-suites.md) | testing | 5 |
| 47 | [46-full-windows-suites.md](46-full-windows-suites.md) | testing | 5 |
| 48 | [47-full-linux-suites.md](47-full-linux-suites.md) | testing | 5 |
| 49 | [48-full-terminal-suites.md](48-full-terminal-suites.md) | testing | 2 |
| 50 | [49-full-performance-part-1.md](49-full-performance-part-1.md) | testing | 5 |
| 51 | [50-full-performance-part-2.md](50-full-performance-part-2.md) | testing | 1 |
| 52 | [51-aggregate-readiness.md](51-aggregate-readiness.md) | testing | 3 |

Total: 52 bounded sources / 203 parents. Historical source roadmaps remain 43 files / 577 original parents; these projections add no new product requirement. No readiness claim follows from queue construction or source-contract validation.

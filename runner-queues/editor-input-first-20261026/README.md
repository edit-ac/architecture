# Put input and navigation delivery first

User-authorized queue replacement, 2026-10-26. The [ProseMirror gap plan](../prosemirror-input-20261026/README.md), including the additional open-source editor findings, now leads EDITOR. Its15 functional parents run before remaining feature delivery, performance improvements and final testing. Its5 final coverage parents stay in the testing phase, after all functionality and bounded optimization. Original case IDs, acceptance, prerequisites and one final owner per finding are preserved.

The CLI only appends. Replace the FIFO through a managed stop at the next completed-worker checkpoint and a guarded successor start with queue-spec.json. Preserve the completed ES and BTA source/progress receipts without re-running them. Preserve the current BTU/EFG source, its progress path, validated checkmarks and unfinished work as a later functional entry. Keep all originally queued remaining editor performance/test sources and progress paths unchanged. A completed parent may still share a source with unchecked siblings; it is never reset for the reorder.

| Order | Worker source | Phase |
| --- | --- | --- |
| 1 | `prosemirror-input-20261026/01-key-intent-and-text-boundaries.md` | functional |
| 2 | `prosemirror-input-20261026/02-rich-context-and-navigation.md` | functional |
| 3 | `prosemirror-input-20261026/02b-native-editing-intents.md` | functional |
| 4 | `editor-remaining-20261026/02-editor-feature-edges.md` | functional |
| 5 | `editor-remaining-20261026/03-bounded-performance.md` | optimization |
| 6 | `prosemirror-input-20261026/03-final-input-coverage.md` | testing |
| 7 | `editor-remaining-20261026/04-shared-test-gaps.md` | testing |
| 8 | `editor-remaining-20261026/05-browser-regressions.md` | testing |
| 9 | `editor-remaining-20261026/06-browser-product-coverage.md` | testing |
| 10 | `editor-remaining-20261026/07-web-performance-qualification.md` | testing |
| 11 | `editor-remaining-20261026/08-terminal-coverage.md` | testing |
| 12 | `editor-remaining-20261026/09-macos-coverage.md` | testing |
| 13 | `editor-remaining-20261026/10-ios-coverage.md` | testing |
| 14 | `editor-remaining-20261026/11-android-coverage.md` | testing |
| 15 | `editor-remaining-20261026/12-windows-coverage.md` | testing |
| 16 | `editor-remaining-20261026/13-linux-coverage.md` | testing |
| 17 | `editor-remaining-20261026/14-native-performance-qualification.md` | testing |
| 18 | `editor-remaining-20261026/15-budget-enforcement-and-handoff.md` | testing |

The original plan in PRIMARY remains planning-only and read-only. Adopted EDITOR copies carry explicit execution authority. PRIMARY integration/framework/backend/native UI and EDX cases keep their owners and source/progress FIFO. Read their receipts only where current input applicability holds. Never stage inherited dirty source, manufacture missing evidence, change document formats/data, weaken caps, run paid synthetic inference, publish or start a second EDITOR controller. The shared coordination lock governs checkpoints; dynamic run/guard IDs and verification live in ignored `.roadmap-runner/editor-input-first-20261026/`.

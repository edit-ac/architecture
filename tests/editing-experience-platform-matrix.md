# Editing experience platform acceptance matrix

Contract: [editing experience](../specs/editing-experience.md). This extends BRK/SEL/MRK/NAV/SPC and existing ENV/mobile/native cases, not a replacement suite. Every row is required for a claimed platform. Status here is **required**, not executed or passed. Preserve the existing feature-first scheduling: focused tests accompany implementation; target-runtime and AT qualification belongs to roadmap43.

## Shared vectors, independent adapters

| Variant | Input / action | Exact semantic oracle |
|---|---|---|
| BRK-02/middle | Paragraph `ab|cd`; line-break intent; X | Same block/parent/attributes; `ab\nXcd`; caret UTF-16 4, one break commit before X. |
| BRK-01/control | Same initial content; paragraph intent; X | Two paragraphs `ab`, `Xcd`; caret in second at 1. |
| BRK-02/wrap-control | Narrow `ab cd ef` enough to wrap; move Down | Same owner/text/revision/history; no LF inserted. Explicit break then inserts exactly one LF. |
| BRK-03/trailing | Empty and `abc|`; two break actions; X | `\n\nX` or `abc\n\nX` in one owner, exact trailing-line caret and authored-break count. |
| BRK-04/replacement | `a[bc]d`, both directions; break | `a\nd`; caret at 2; one undo restores `abcd` and original directed selection; redo restores break. |
| BRK-02/UTF16 | `😀|x`; break; X | `😀\nXx`, caret UTF-16 4; valid boundaries and unchanged emoji. |
| MRK-04/break | Bold+italic `ab|cd`; break; X | X retains applicable marks, no empty formatting nodes; same owner. |
| BRK-05–08/context | Heading, nested/checked list, quote, code, cell | Preserve the correct owner/container; use contract Enter control; no extra item/row/cell for a hard break. |
| G01/delivery | Key + duplicate notifications, then an intentional second break | Exactly one edit for the first intent and one for the second; do not deduplicate identical content. |
| G05/composition | Composition update, confirmation Enter, next deliberate break | Confirmation commits composed text only; later break works once. Cancel restores baseline; no partial persistence. |
| G02/permission | Same actions read-only, invalid/stale selection or incompatible range | Rejected/no-op with unchanged revision, text, selection, history and journal. |
| G03/G07/reopen | Break, undo, redo, save/reopen, copy/export/import | Same authored break and structure; meaningful selection after live undo/redo; document survives reopen; lossy formats report loss. |

Run forward/backward selection variants and empty/start/end positions where applicable. Test unchanged neighboring blocks and metadata, not only concatenated text. Viewport movement cannot substitute for authored-line assertions.

## Target entry points and existing test homes

| Target | Required delivery paths | Existing implementation/test home / owner |
|---|---|---|
| Shared Rust/Session | Prepared `hardBreak`/split, selected replacement, stable result anchors, history, current checkpoint | `core/crates/editac-core/tests/editing_regressions.rs`, `core/crates/editac-session`; INT-1.2 / RGS. |
| Web Chromium | Native keyboard, beforeinput-only paragraph/line break, clipboard, DOM selection, IndexedDB | `core/tests/browser/interactions/breaks.spec.ts`, `break-tables.spec.ts`; INT-1.2. |
| Web Firefox | Same variants on Firefox, with browser-specific event observations | Same actual browser harness; Chromium passes are not reused as Firefox evidence. |
| Web WebKit | Same variants on WebKit | Same harness; desktop WebKit is not iOS Safari evidence. |
| Mobile web iOS/Android | Soft keyboard, composition/correction, toolbar break, selection handles, hardware keyboard when available | `core/tests/mobile-web/`; roadmaps40/41 and final43. Emulated viewport alone is insufficient. |
| macOS AppKit | Shift+Return NSEvent, `insertLineBreak:`, ordinary Return, menu/command, marked text, undo/redo | `core/native/macos/tests/Commands/CommandsTests.swift`, Composition tests; roadmap18/33. |
| iOS UIKit | UITextInput range/composition, software return/action, explicit break control, hardware Shift+Return | `core/native/ios/tests/` plus native input owner; roadmap16/31. Add adapter tests where none exist. |
| Android | InputConnection commit/composing/batch requests, IME action, explicit break control, hardware event | `core/native/android/sdk/src/test/` plus emulator instrumentation required; roadmap17/32. JVM tests alone do not qualify IME. |
| Windows | Chosen native toolkit's text/selection/composition requests, hardware key and accessibility command | Desktop native owner, roadmap18/34; requires implemented target host and tests, not capability metadata. |
| Linux | Chosen toolkit's preedit/commit, surrounding text/deletion, hardware key and accessibility command | Desktop native owner, roadmap18/35; requires Linux runtime tests. |
| Terminal/CLI | Source-mode LF/CRLF, semantic command mode if offered, PTY key encoding and alternate hard-break command | `cli/src/tui/input.rs`, `cli/src/tui/commands.rs`; roadmap15/36. Source LF and rich semantic break are tested separately. |

## Test commands and recording

From `core`, select Node from `.node-version` and run `npm run test:interactions -- --group breaks` for the complete existing browser break gate. For a changed variant, the existing browser dispatcher accepts a Node test-name filter: `node scripts/test-browser.mjs interaction-breaks --test-name-pattern='BRK-02.*intent'`. The dispatcher covers Chromium, Firefox and WebKit. A subset is reported as a subset and cannot close the full gate.

From `core`, `bash native/macos/scripts/check.sh commands` runs the native command gate with its pinned Xcode/SDK/OS and generated FFI. Missing pins, build failures, missing tests or skipped tests are unmet evidence, not permission to mark the platform passed. Use actual UIKit/Android/Windows/Linux/PTY owners' implemented commands once available; do not invent a green dispatcher for missing tests.

Receipts identify source and built-artifact hashes, runtime/OS/browser/IME/AT versions, physical versus virtual provenance, executed/passed/failed/skipped counts, failing vector IDs and precise limitations. Keep generated output ignored and task-owned; delete successful temporary builds after diagnosis. Preserve concise failure diagnostics while unresolved. Documentation/fixture validation counts must remain separate from semantic, browser and native runtime counts.

The [native history-selection regression](../specs/editing-experience.md#open-regression-native-history-loses-the-editing-selection) is an open required G03/G07 variant. Its test must continue to fail until the selection travels through shared history and is applied after native projection. Do not change its oracle to accept a reset-to-start caret or count the other hard-break cases as its replacement.

## Terminal and block-selection observation inputs

ES-4.4 deterministic coverage and its exact limits are mapped in [standards conformance](editing-standards-conformance.md#terminal-commands-and-accessible-selection). These are observation inputs for existing PHY-1.1/PHY-1.4 and native/mobile owners, not new tasks or completed qualification. Keep the original matrix denominator and unqualified rows.

| Existing owner / runtime | Observation recipe | Required record and limitation |
| --- | --- | --- |
| PHY-1.1/PHY-1.4; actual terminal emulator and AT | Open exact Unicode/CRLF source containing Hungarian accents, a combining cluster, emoji and Hebrew. Exercise reported Ctrl/Alt word movement, both Shift directions, Ctrl-Home/End, PageUp/Down across a resized viewport, then F1 alternatives when modifiers are intercepted. Check Ctrl-S/Z/Y/D and exit precedence while the picker is open. | Name terminal/emulator, OS, locale/layout, crossterm report/encoding, terminal size and AT version. Preserve source bytes and semantic history during movement. Logical source order and escaped display controls do not establish visual RTL or speech/braille support. Do not invent a word deletion when Ctrl-Backspace is indistinct. |
| PHY-1.4; desktop browser with target OS/AT | Discover the host's labeled Select block command or its declared remap; enter at a text bookmark, extend in both directions, inspect mode/count/type and focused outline, then Enter or Return to text and type at the retained bookmark. Repeat for a supported noneditable object and its labeled command alternative to dragging. | Record browser/OS/AT versions and actual spoken/braille output, selected/focused object and accessible description. DOM live regions and outline assertions prove mechanics only. The catalog supplies no default global block-entry chord; the deterministic fixture's F8 is a host-defined test profile. |
| PHY-1.4 and original input owners; actual IME and popup | While composing, use confirmation/Escape and attempt block entry; then open a link/command popup, dismiss it, and use Escape followed by Tab/Shift+Tab to leave. Repeat with embedded editable controls and a host-reserved/remapped chord. | Record input method, locale/layout, focus owner and delivered events. Confirm no intercepted IME/embedded-field key, unexpected content transaction, history entry or focus trap. Prepared composition flags are not an OS IME observation. |
| PHY-1.2/PHY-1.3; iOS/Android native and mobile web | Apply the same named selection/return/announcement recipe through the implemented host controls, software keyboard and VoiceOver/TalkBack; include viewport transitions and supported hardware keys. | Use the existing accepted simulator/emulator/device routes with their exact runtime and AT evidence. Desktop Chromium/Firefox/WebKit receipts do not qualify mobile Safari, Android IME or native accessible authoring. |

No terminal emulator/OS keyboard-layout, real IME, screen-reader, braille or mobile/native observation was executed by ES-4.4. Support remains unqualified until its original runtime owner supplies that evidence.

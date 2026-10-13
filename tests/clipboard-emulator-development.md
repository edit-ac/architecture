# Clipboard simulator/emulator development gate

User authorization: 2026-10-13, "Lets unblock, emulator should do for now". This procedure unblocks development only. Preserve FMT-1.15-V1 physical-device qualification as an open release gate. Execute this as CAP-1.1-I2/V2 and record the resulting virtual receipt for FMT-1.15-I2/V2 without changing controller-owned checkboxes.

Use one task-owned Android Emulator with Chrome or one iOS Simulator with Safari. The controller verified Android AVDs EditAC_API_36 and Assign_HONOR_Pad_X8a_API_35 plus the installed iOS 26.5 runtime. Availability is not a pass. Preserve the Assign AVD and any simulator owned by another task. Prefer a separately named clone/new EditAC clipboard virtual device and report its identity; check process/chat ownership before reusing an existing instance. No external service, paid inference, credentials or real document is needed.

Read core/tests/manual/markdown-clipboard.md for the existing palette, setup and observation oracle. Use the isolated worktree's current built production engine/web fixture and enable the qualified Markdown capability explicitly. If the new optional extension has been integrated, enable it using its public host registration. Never modify another lane's source merely to make the fixture run. Record current artifact hashes; old receipt hashes cannot qualify rebuilt artifacts. Use a task-owned local server/port with appropriate emulator networking or Android adb reverse; localhost on iOS Simulator is suitable. Preserve full build/test logs.

Required representative cases on that virtual platform:

1. VDEV-PASTE: copy the pinned Markdown palette through the simulator/emulator OS clipboard and paste using its browser's native paste menu into the editor. Inspect the admitted headings/marks/list/check/code/link and enabled image/table semantics against the existing palette oracle. Setup and passive inspection through browser debugging are allowed; synthetic event dispatch or directly calling the editor paste API is not evidence of the menu entry point.
2. VDEV-ONCE: capture a passive clipboard/beforeinput/input trace and semantic history/storage counters around that action. Assert exactly one committed paste and undo/journal boundary, with no duplicate insertion.
3. VDEV-UNDO: use the host undo/redo controls and verify the whole admitted paste is one undo group and redo restores it.
4. VDEV-RELOAD: wait for the actual local durability acknowledgment, reload/reopen and verify the saved semantic document is restored.
5. VDEV-LITERAL: use the host's supported plain-paste action or explicitly disabled Markdown policy/capability with the same native clipboard route. Exact Unicode and Markdown delimiters stay literal without inferred formatting. Record the exact host policy used; do not claim an unavailable OS plain-paste shortcut.

All five assertions must actually run and pass with zero required skips. An unsupported optional asset may retain its exact data/diagnostic under the existing codec contract, but may not be silently dropped. A failed native/menu/tooling case remains blocked with a precise repair action. Preserve failed attempts. Do not repeat already passing portable upstream audits unless this fixture changes their code.

Write architecture/evidence/markdown/emulator-development/receipt.json with environmentKind=simulator or emulator, virtualDevice identity/runtime, browser version, source/package hashes, actual event/action methods, executed/passed/failed/skipped counts, per-case observations, screenshots/traces/log hashes, reproduction and physicalDevices.observed=0. Set developmentGate=PASS only on actual passing observations; physicalReleaseGate=NOT_QUALIFIED. Link this from CAP progress and update the Markdown owning evidence handoff. The controller owns source checkmarks; workers write only progress/evidence.

Track task-owned emulator/simulator, server and browser-debugging processes and stop them after the cases, including failure teardown. Preserve other tasks' instances and evidence. Stop and report a concrete blocker if no device can execute the cases; do not retry unchanged prerequisites indefinitely.

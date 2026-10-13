# Integrate optional rich services into the CLI and TUI

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `cli`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/ecosystem-maintainability.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: `15-tui-client.md`, `25-rich-content-extensions.md`, `26-link-resolution.md`, `27-document-conversion.md`, `30-architecture-fitness.md` at reviewed immutable source/implementation revisions with passing evidence.  Local Dependencies fields refer only to this file.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration, with its implementation and validation substeps. Read task-local context rather than the complete ecosystem. Create named checks before invoking them; unknown suites, zero matches and skipped platforms cannot pass. Use deterministic fixtures and prepared transports, no live model/provider calls or paid inference. Do not load `.secrets`. Missing toolchains or upstream evidence block only their dependent tasks. Do not launch another controller or publish outside a named release task.

## Epic TCX-1 — Integrate optional rich services into the CLI and TUI

### Task TCX-1.1 — Verify terminal extension service bindings

- [ ] TCX-1.1 Verify terminal extension service bindings.

Purpose: Verify terminal extension service bindings as one bounded integration or qualification boundary.
Context: `src/tui/`; `tests/extension_entry.rs`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: CLI consumes immutable core service revisions with existing15 buffer/reconciliation/diff behavior preserved.

Implementation:

- [ ] TCX-1.1-I1 Bind the shared capability/profile and optional provider ports; record actual terminal representation limits, and keep network/conversion optional.

Validation:

- [ ] TCX-1.1-V1 `cargo test --test extension_entry --locked`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `TCX-1.1` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `TCX-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task TCX-1.2 — Add bounded code syntax and table formatting actions

- [ ] TCX-1.2 Add bounded code syntax and table formatting actions.

Purpose: Add bounded code syntax and table formatting actions as one bounded integration or qualification boundary.
Context: `src/tui/extensions/content.rs`; `tests/tui_content_extensions.rs`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: TCX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Visible code coloring and Markdown table formatting stay responsive, preserve source spelling outside edited ranges and handle UTF-16/grapheme conversions. Expose the qualified code-tools commands and document search through terminal controls where supported; bind relevant FND/IDE cases without claiming pointer/OS GUI parity.

Implementation:

- [ ] TCX-1.2-I1 Use25 provider spans and formatter; do not silently rewrite hosted source baselines. Add cancellation, limit fallback and one-group undo while retaining recoverable dirty buffers.

Validation:

- [ ] TCX-1.2-V1 `cargo test --test tui_content_extensions --locked`; run prepared terminal render/performance fixtures. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `TCX-1.2` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `TCX-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task TCX-1.3 — Add asset and embed source workflows

- [ ] TCX-1.3 Add asset and embed source workflows.

Purpose: Add asset and embed source workflows as one bounded integration or qualification boundary.
Context: `src/tui/extensions/assets.rs`; `tests/tui_asset_extensions.rs`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: TCX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: User can attach/reference/list/export assets through host ports; terminal cards preserve embed data without claiming graphical rendering.

Implementation:

- [ ] TCX-1.3-I1 Wire25 staged transfers and explicit open/download actions with permission, byte limits and recovery; no automatic external process launch from document content.

Validation:

- [ ] TCX-1.3-V1 `cargo test --test tui_asset_extensions --locked`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `TCX-1.3` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `TCX-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task TCX-1.4 — Add permission-aware references and link metadata

- [ ] TCX-1.4 Add permission-aware references and link metadata.

Purpose: Add permission-aware references and link metadata as one bounded integration or qualification boundary.
Context: `src/tui/extensions/links.rs`; `tests/tui_link_extensions.rs`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: TCX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Auto mode obeys local-paste policy; private title/cache/activation rules match26 and offline source editing remains available.

Implementation:

- [ ] TCX-1.4-I1 Use the shared resolvers and safe terminal presentation with explicit refresh/open commands; sanitize terminal control sequences and never trust imported permission labels.

Validation:

- [ ] TCX-1.4-V1 `cargo test --test tui_link_extensions --locked`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `TCX-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `TCX-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task TCX-1.5 — Expose qualified format conversion commands

- [ ] TCX-1.5 Expose qualified format conversion commands.

Purpose: Expose qualified format conversion commands as one bounded integration or qualification boundary.
Context: `src/commands/convert.rs`; `tests/conversion_commands.rs`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: TCX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Import/export accepts declared formats with loss reports, atomic save/stale-target protection and cancellation; PDF input is rejected as export-only.

Implementation:

- [ ] TCX-1.5-I1 Bind27 jobs with explicit file destinations and format detection/override policy; optional heavyweight providers are separately loaded and unavailable providers fail actionably.

Validation:

- [ ] TCX-1.5-V1 `cargo test --test conversion_commands --locked`; validate MD/DOCX/secondary formats and deterministic PDF export fixtures. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `TCX-1.5` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `TCX-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task TCX-1.6 — Qualify terminal command, readonly and collaboration parity

- [ ] TCX-1.6 Qualify terminal command, readonly and collaboration parity.

Purpose: Qualify terminal command, readonly and collaboration parity as one bounded integration or qualification boundary.
Context: `tests/tui_extension_scenarios.rs`; `docs/tui-support.md`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: TCX-1.2, TCX-1.3, TCX-1.4, TCX-1.5.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Extension actions respect readonly/permissions and concurrent source reconciliation; terminal limitations are explicit rather than graphical parity claims. Record official profile identities and supported FND/IDE/FPX variants, explicit terminal limitations and deterministic command/history evidence.

Implementation:

- [ ] TCX-1.6-I1 Run local/hosted prepared fixtures through actual CLI/TUI with extension actions and recovery; update the qualified profile and clean package consumer.

Validation:

- [ ] TCX-1.6-V1 `cargo test --test tui_extension_scenarios --locked`; rerun the existing clean CLI package-consumer command recorded in15 evidence. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `TCX-1.6` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `TCX-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

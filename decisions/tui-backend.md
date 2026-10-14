# Terminal backend selection

Decision: accepted for TUI-1.2 on 2026-10-14. Select **Ratatui 0.30.2 with
Crossterm 0.29.0**. This is dependency and headless API qualification; the
interactive editor, terminal lifecycle and packaged PTY workflows remain the
later TUI roadmap tasks.

## Bounded comparison

Two stacks were considered in one session. Both reuse Ratatui's renderer and
TestBackend; neither needs a separate rendering implementation.

| Candidate | Compiler / license | Platform and input fit | Decision |
| --- | --- | --- | --- |
| Ratatui 0.30.2 + Crossterm 0.29.0 | Declared Rust 1.88.0 / 1.63.0 respectively; both MIT | Upstream declares Unix and Windows terminal support. Typed key, resize, focus and bracketed-paste events; synchronous poll/read. | Selected: one input/output stack across the intended desktop OS families. |
| Ratatui 0.30.2 + Termion 4.0.6 | Ratatui Rust 1.88.0; Termion declares no MSRV; both MIT | Termion documents Linux, macOS and Redox; direct TTY input/raw mode/alternate screen. Windows is outside its documented platform set. | Rejected: would require another input backend for Windows. Not compiled or qualified here. |

Primary references, inspected for this decision:

- [Ratatui installation and matching Crossterm version](https://ratatui.rs/installation/).
- [Ratatui 0.30.2 manifest, compiler, license and feature definitions](https://docs.rs/crate/ratatui/0.30.2/source/Cargo.toml).
- [Ratatui backend architecture](https://ratatui.rs/concepts/backends/).
- [Crossterm 0.29.0 manifest and feature definitions](https://docs.rs/crate/crossterm/0.29.0/source/Cargo.toml).
- [Crossterm 0.29.0 platform declarations and tested terminals](https://docs.rs/crate/crossterm/0.29.0/source/README.md).
- [Crossterm 0.29.0 event ownership and raw-mode requirements](https://docs.rs/crossterm/0.29.0/crossterm/event/index.html).
- [Termion 4.0.6 platform and input documentation](https://docs.rs/termion/4.0.6/termion/)
  and [manifest](https://docs.rs/crate/termion/4.0.6/source/Cargo.toml).

Versioned registry manifests, README/license files and `cargo info` output are
retained under `evidence/tui-backend/session-20261014/`; registry source is used
where the web fetch of the versioned manifest was unavailable. No lower MSRV is
inferred from an unversioned tutorial.

## Exact selected dependency surface

`cli/Cargo.toml` pins `ratatui =0.30.2`, disables its defaults and enables only
`crossterm_0_29`. It pins `crossterm =0.29.0`, disables direct defaults and
explicitly requests `events`, `bracketed-paste`, `windows`. The lockfile fixes
the complete resolved graph and registry checksums, including ratatui-core
0.1.2, ratatui-crossterm 0.1.2 and ratatui-widgets 0.3.2.

Cargo feature unification matters: ratatui-crossterm enables its own defaults
and Crossterm defaults transitively. Effective Crossterm features therefore
include `default` and `derive-more` as well as the three requested features;
ratatui-core and ratatui-crossterm include `underline-color`. These are accepted
and captured in `features.log` and `metadata.json`. No async event stream,
OSC52 clipboard, alternate backend, calendar, macros or unstable feature is
selected. Terminal I/O uses the process terminal, without `use-dev-tty`.

The workspace's exact Rust 1.97.1/edition 2024 toolchain remains unchanged.
All declared MSRVs in the locked metadata fit that compiler; the selected
Ratatui companions and macro dependencies require at most 1.88.0. The selected
backend crates are MIT and their license texts are retained alongside the
Apache-2.0 application. This does not change the application license.

## Input, PTY and unsupported capabilities

The future event loop must own synchronous `poll`/`read` on the same thread;
it must not mix those calls with EventStream. Enable raw mode before keyboard
reading, and explicitly enable/disable bracketed paste and focus reporting
under the terminal lifecycle guard. Key release/repeat and extended modifiers
depend on the terminal protocol; event variants do not establish universal
delivery. Unsupported focus/paste reporting requires documented fallback;
paste size limits, literal handling and Unicode caret behavior remain TUI-1.5.

Interactive use requires a usable terminal/console. Unix PTY tests need a
controlling slave terminal, fixed dimensions and scripted bytes; a Windows
console/ConPTY harness needs its own target-platform execution. A pipe can
exercise command output but does not establish raw mode, input decoding,
restoration, signals, resize delivery, or interactive terminal support.
There is no network/account/service prerequisite for these backend APIs.

Upstream OS coverage is a selection criterion, not an edit.ac support claim.
This run executes on native macOS 26.4.1 (25E253), arm64, with no terminal
emulator attached to the probe. Windows, Linux, Redox, real terminal keyboard
protocols, screen readers, IME, clipboard, bidi layout and hardware/virtual
input support are unqualified. No GUI-native input/accessibility capability
is supplied by this dependency choice. TUI-1.4 owns terminal restoration and
control escaping; TUI-1.11 owns actual binary PTY behavior; TUI-1.12 owns the
evidence-backed support matrix. Named target-platform VMs/test hosts remain
valid qualification environments under the platform policy.

## Headless proof and handoff

`cli/tests/tui_backend.rs` exercises Ratatui frame drawing and resize with
TestBackend, prepared key/paste/focus values, actual CrosstermBackend drawing
and mode-command encoding into memory, and a prepared BrokenPipe writer.
It does not call the OS event reader or mutate a document/session. The
initial test compile failure (Infallible versus io::Error) is preserved;
the test return type was corrected without weakening assertions.

Acceptance: `cargo test --test tui_backend --locked` passes 4 executed,
4 passed, 0 failed/ignored/filtered; `cargo tree --locked` resolves the graph.
Full commands, revisions, fixture/source/artifact hashes and setup failure
details are in `evidence/tui-backend/session-20261014/receipt.json`.
TUI-1.3 can now wire the existing catalog/session owners; it must preserve
the single-engine and capability boundaries documented in `evidence/tui-entry.md`.

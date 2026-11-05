# Local Windows and Linux native testing

Status: Linux infrastructure verified; Windows installed; first-run/provisioning pending; no edit.ac SDK or product qualification claimed.
Owner: edit.ac native platform owners. Reviewed: 2026-10-26.
Related: [workspace setup](../WORKSPACE_SETUP.md), [feature-first decision](web-feature-first-20261018.md), [Windows roadmap](../roadmaps/22-windows-native.md), [Linux roadmap](../roadmaps/23-linux-native.md).

The requested local environment is prepared for focused platform work. It does not lift the existing Windows/Linux feature-first deferral or move roadmap43 device/runtime qualification into earlier feature gates.

## Local runner and evidence

The shared controller is `/Users/bpstr/Documents/Codex/native-qa`; read its `README.md` and `capabilities.json` for current state and commands. The Mac is ARM64 with 8 GiB RAM: run one guest at a time and never stop a VM owned by another active task. No Docker/Colima or host filesystem mounts are used.

- **Linux verified infrastructure:** existing `editac-linux` Lima/VZ guest, Ubuntu 26.04.1 ARM64, 2 CPUs/2 GiB RAM/24 GiB disk. CLI, GTK4/libadwaita/WebKitGTK development dependencies and Xvfb/Openbox X11 input/screenshot harness are provisioned. Infrastructure smoke on 2026-10-25: **2 passed, 0 failed, 0 skipped**. Real GNOME desktop, Wayland, portals, GPU, tray and assistive-technology workflows are not verified. This is not Ubuntu 24.04 coverage.
- **Windows pending:** UTM 5.0.8 `windows-qa`, ARM64 virtualization, 2 CPUs/4 GiB RAM/64 GiB sparse disk, SSH forwarded from `127.0.0.1:2222` to guest 22. Windows 11 Pro installation completed. On 2026-10-26 console input recovered using 200–250 ms key holds; region/keyboard and first-run updates completed. Local account creation awaits human credential entry and specific administrator/standard-account authorization. SSH provisioning and interactive smoke are not complete. Do not claim Windows tests passed.
- **Licensing:** Microsoft offers a free 90-day Enterprise evaluation with no product key, but the inspected public download link resolved to x64 despite the overview advertising ARM64. The staged official consumer ARM64 ISO is not an Enterprise evaluation license. On 2026-10-25 the user chose regular Windows 11 Pro ARM64 with activation left to them, approved its license, and Windows Pro installation completed on the empty VM disk. Continue Pro setup rather than blocking on evaluation media; record actual activation state without claiming an evaluation license. No purchase or activation bypass is authorized.
- **Architecture:** ARM64 results do not establish native Windows/Linux x64 support. Label x64 Windows application/Python emulation separately from native ARM64 and native x64 OS evidence.

Use `$linux-native-testing` or `$windows-native-testing` (installed personal skills; maintained sources in `/Users/bpstr/Documents/Codex/native-qa/skills`). They route provisioning, explicit source staging, guest commands and artifact collection. No project chats were messaged or runners restarted by this setup.

```sh
cd /Users/bpstr/Documents/Codex/native-qa
limactl start editac-linux
# Check current endpoint: limactl show-ssh editac-linux; update linux-qa Port if changed.
python3 scripts/qa.py doctor linux
python3 scripts/sync.py linux /Users/bpstr/Github/edit-ac/core
# Write test.sh using the returned guest source directory and the project command below.
python3 scripts/qa.py run linux --project edit-ac --mode cli --script /absolute/test.sh
# Use --mode xvfb for an X11 GUI suite; Windows uses cli or desktop once provisioned.
limactl stop editac-linux
```

Source staging transfers tracked working-tree bytes and records hashes; it omits untracked files, symlinks, credentials and caches. Inspect omissions and explicitly stage required safe untracked fixtures. A snapshot missing relevant changed source cannot qualify a candidate; Git-dependent checks need a real guest checkout. Honor project toolchain pins and use one build job on the small Linux guest.

Scripts receive `QA_ARTIFACTS`, a unique guest output directory. The controller collects JUnit/TRX, screenshots, app/installer logs and independent test/transfer exit codes under `/Users/bpstr/Documents/Codex/native-qa/artifacts/edit-ac/PLATFORM/RUN/`, outside project Git. Preserve actual failures and nonzero executed/pass/fail/skip counts. Record source HEAD and dirty-byte hashes, package hash, OS/build, guest/app/harness architecture, emulation, toolchain and desktop mode/resolution/scaling. A harness pass is not a product test or release gate. Use deterministic fixtures/mock transports without `.secrets` or provider credentials.

Windows UI tests require the limited `NativeQA` scheduled task in an already logged-in, unlocked `qa` desktop; direct SSH execution is for CLI tests. Respect MSI reboot results and real installer behavior. Linux Xvfb results cover X11 only. For real desktop/Wayland, establish a graphical-session-bound runner and verify session/automation permission before testing. Preserve clean powered-off bases and use disposable test clones when exercising installation/upgrade/uninstallation.

## edit.ac checks

Stage `core/` or `cli/` and any required sibling-owned inputs. Preserve Rust 1.97.1 and the current npm/Node/wasm-bindgen pins from the actual source. Keep separate exchange directories required by `WORKSPACE_SETUP.md`; do not reuse mutable fixtures across runs.

Focused shared-engine example from core: `cargo test --locked -p editac-core --test table_shape` (current existing target). CLI checks run from the separate cli source with its own Cargo pin. Select the affected test/fixture rather than launching full browser/native matrices for infrastructure changes.

`core/native/desktop/capability.json` currently declares `native.desktop.pending.v1` with unqualified resources. Available GTK libraries and a working Xvfb harness do not establish a Linux consumer/SDK or Windows native control implementation. Implement and qualify the actual Windows/Linux consumers only under their owning accepted tasks. Do not run Swift/macOS-only fixtures on Linux or treat Rust cross-compilation as native runtime evidence. Shared Rust semantic/storage/ABI owners remain unchanged.

For an implemented consumer, test real text input/composition, selection/history, clipboard, persistence and the task's accessibility cases in its target OS session. Label X11-only observations, defer real Wayland/GPU assertions until observed, and preserve existing roadmap43 device predicates and failure history. No public documentation, package publication, ABI/schema change or paid inference is authorized by this environment setup.

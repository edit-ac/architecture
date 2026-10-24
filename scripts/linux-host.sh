#!/bin/bash
# Operate only the task-owned local VM; never propagate ambient credentials.
set -euo pipefail
task_root=$(cd "$(dirname "$0")/.." && pwd)
task_vm=editac-linux
case "${1:-}" in
  start)
    if test -d "${LIMA_HOME:-$HOME/.lima}/$task_vm"; then
      exec limactl start --tty=false "$task_vm"
    fi
    exec limactl start --tty=false --name="$task_vm" "$task_root/toolchains/linux-host.yaml"
    ;;
  stop)
    exec limactl stop --tty=false "$task_vm"
    ;;
  status)
    exec limactl list "$task_vm" --json
    ;;
  provision-rust)
    # Verify the official installer digest before execution, then pin the core compiler.
    exec limactl shell "$task_vm" bash -s <<'GUEST'
set -euo pipefail
task_scratch=$(mktemp -d)
trap 'rm -rf "$task_scratch"' EXIT
cd "$task_scratch"
task_url=https://static.rust-lang.org/rustup/dist/aarch64-unknown-linux-gnu/rustup-init
curl --fail --location --silent --show-error "$task_url" --output rustup-init
curl --fail --location --silent --show-error "$task_url.sha256" --output rustup-init.sha256
sha256sum -c rustup-init.sha256
chmod +x rustup-init
./rustup-init -y --no-modify-path --profile minimal --default-toolchain 1.97.1
"$HOME/.cargo/bin/rustup" component add rustfmt --toolchain 1.97.1
for task_tool in rustup rustc cargo rustfmt cargo-fmt; do
    task_link="/usr/local/bin/$task_tool"
    if test -e "$task_link" && test "$(readlink "$task_link")" != "$HOME/.cargo/bin/$task_tool"; then
        printf 'Preserve existing unrelated compiler: %s\n' "$task_link" >&2
        exit 1
    fi
    sudo ln -sfn "$HOME/.cargo/bin/$task_tool" "$task_link"
done
"$HOME/.cargo/bin/rustc" --version
GUEST
    ;;
  smoke)
    limactl shell "$task_vm" sh -c 'mkdir -p /tmp/editac-linux-smoke'
    limactl shell "$task_vm" sh -c 'cat > /tmp/editac-linux-smoke/control.c' < "$task_root/toolchains/linux-gtk-smoke.c"
    exec limactl shell "$task_vm" bash -s <<'GUEST'
set -euo pipefail
trap 'rm -rf /tmp/editac-linux-smoke' EXIT
test "$(uname -s)" = Linux
printf 'Linux host: 1 passed, 0 failed; '
uname -sm
cc /tmp/editac-linux-smoke/control.c -o /tmp/editac-linux-smoke/control $(pkg-config --cflags --libs gtk4)
dbus-run-session -- xvfb-run -a /tmp/editac-linux-smoke/control
"$HOME/.cargo/bin/rustc" --version | tee /tmp/editac-linux-smoke/rust-version
grep -q 'rustc 1.97.1 ' /tmp/editac-linux-smoke/rust-version
printf 'Pinned Rust compiler: 1 passed, 0 failed\n'
GUEST
    ;;
  shell)
    shift
    exec limactl shell "$task_vm" "$@"
    ;;
  *)
    printf 'Usage: bash %s {start|stop|status|provision-rust|smoke|shell COMMAND...}\n' "$0" >&2
    exit 2
    ;;
esac

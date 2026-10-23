#!/usr/bin/env python3
"""Start or attach to one Roadmap Runner and require a live deterministic guard.

Pass normal runner arguments after start/attach. Attach accepts a run ID and an
explicit --workspace; it never starts a worker or changes a queue.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time


def workspace_argument(arguments):
    index = arguments.index("--workspace")
    workspace = Path(arguments[index + 1])
    if not workspace.is_absolute() or not workspace.is_dir():
        raise ValueError("--workspace must name the existing absolute workspace root")
    return workspace.resolve()


def stop(cli, record):
    result = subprocess.run([cli, "stop", record["id"], "--workspace", record["workspace"], "--json"],
                            capture_output=True, text=True, timeout=30)
    if result.returncode:
        raise RuntimeError("Guard failed and runner stop failed: " + result.stderr[-1000:])


def arm_guard(cli, record):
    workspace = Path(record["workspace"]).resolve()
    progress = Path(record["progressFile"]).resolve()
    if not progress.is_relative_to(workspace):
        raise ValueError("Runner progress must remain inside its workspace")
    # The progress-side event file ends at one roadmap. Only the manager's
    # stream remaps per-source completion to roadmap_completed and follows FIFO.
    events = Path(record["artifacts"]["events"])
    if not events.is_absolute():
        raise ValueError("Managed runner must return an absolute events artifact")
    directory = workspace / ".roadmap-runner" / "guards"
    directory.mkdir(parents=True, exist_ok=True)
    receipt = directory / (record["id"] + ".json")
    script = Path(__file__).with_name("guard-roadmap-recovery.py").resolve()
    if receipt.exists():
        existing = json.loads(receipt.read_text())
        pid = existing.get("pid")
        if (existing.get("state") == "armed" and existing.get("events") == str(events)
                and isinstance(pid, int)):
            command = subprocess.run(["ps", "-p", str(pid), "-o", "command="],
                                     capture_output=True, text=True, timeout=5).stdout
            if str(script) in command and f"--run-id {record['id']}" in command:
                return {"pid": pid, "receipt": str(receipt), "state": "armed"}
    command = [sys.executable, str(script), "--run-id", record["id"], "--workspace", str(workspace),
               "--events", str(events), "--receipt", str(receipt), "--cli", cli]
    with (directory / (record["id"] + ".log")).open("a") as log:
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError("Guard exited before readiness; inspect " + str(receipt))
        if receipt.exists():
            state = json.loads(receipt.read_text())
            if state.get("pid") == process.pid and state.get("state") == "armed":
                return {"pid": process.pid, "receipt": str(receipt), "state": "armed"}
        time.sleep(0.05)
    raise RuntimeError("Guard did not acknowledge readiness within 10 seconds")


def run(cli, mode, arguments):
    workspace = workspace_argument(arguments)
    command = [cli, "start" if mode == "start" else "status", *arguments]
    if "--json" not in command:
        command.append("--json")
    result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    if result.returncode:
        raise RuntimeError(result.stderr[-2000:] or result.stdout[-2000:])
    record = json.loads(result.stdout)
    try:
        if Path(record["workspace"]).resolve() != workspace:
            raise ValueError("Runner returned another workspace")
        if record["processState"] in ("running", "starting"):
            record["loopGuard"] = arm_guard(cli, record)
    except Exception:
        stop(cli, record)
        raise
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", default=shutil.which("roadmap-runner"))
    parser.add_argument("mode", choices=("start", "attach"))
    parser.add_argument("runner_arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.cli:
        parser.error("roadmap-runner is unavailable; select --cli /absolute/path/to/roadmap-runner")
    print(json.dumps(run(str(Path(args.cli).resolve()), args.mode, args.runner_arguments), indent=2))


if __name__ == "__main__":
    main()

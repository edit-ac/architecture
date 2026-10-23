#!/usr/bin/env python3
"""Stop a blocked worker or repeated completed-source loop, preserving its FIFO.

The runner currently re-enters recovery even when no dependency changed. This
event-file guard performs no inference and never restarts a controller.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import time


def blocked_worker(event, run_id, workspace):
    if (event.get("runId") != run_id or event.get("type") != "runner.turn_finished"
            or event.get("role") != "worker" or event.get("interrupted")):
        return None
    progress = Path(event.get("progressFile", "")).resolve()
    if not progress.is_relative_to(workspace.resolve()) or not progress.is_file():
        return None
    text = progress.read_text()
    if "Status: BLOCKED" not in text.split("##", 1)[0]:
        return None
    return progress


class CompletedSourceGuard:
    """Catch repeated successful reconciliation of an already checked source."""

    def __init__(self):
        self.previous = None
        self.previous_iteration = None

    def inspect(self, event, run_id, workspace):
        if (event.get("runId") != run_id or event.get("type") != "runner.turn_finished"
                or event.get("role") != "worker" or event.get("code") != 0
                or event.get("interrupted") or event.get("timedOut")):
            return None
        source = Path(event.get("roadmap", "")).resolve()
        progress = Path(event.get("progressFile", "")).resolve()
        if any(not p.is_relative_to(workspace.resolve()) or not p.is_file()
               for p in (source, progress)):
            self.previous = None
            return None
        checks = re.findall(r"^\s*- \[([ xX])\] (.+)$", source.read_text(), re.MULTILINE)
        # Check the whole acceptance contract, not just checkbox labels. A real
        # controller amendment must reset detection. Ignore the exact volatile
        # paragraph responsible for the original self-referential hash loop.
        contract = re.sub(r"^Current delivery:.*\n?", "", source.read_text(), flags=re.MULTILINE)
        contract = re.sub(r"^Status:.*$", "", contract, flags=re.MULTILINE)
        fingerprint = (str(source), contract.strip())
        complete = checks and all(state.lower() == "x" for state, _ in checks)
        iteration = (str(source), event.get("iteration")) if event.get("iteration") is not None else None
        if iteration is not None and iteration == self.previous_iteration:
            return None
        stuck = complete and self.previous == fingerprint
        self.previous = fingerprint if complete else None
        self.previous_iteration = iteration
        return progress if stuck else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--events", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--cli", required=True, type=Path)
    parser.add_argument("--max-hours", type=float, default=168)
    parser.add_argument("--poll-seconds", type=float, default=5)
    args = parser.parse_args()
    cursor = args.events.stat().st_size if args.events.exists() else 0
    deadline = time.monotonic() + max(0, args.max_hours) * 3600
    state = {"runId": args.run_id, "workspace": str(args.workspace), "state": "armed",
             "pid": os.getpid(), "events": str(args.events)}
    completed = CompletedSourceGuard()

    def save(**fields):
        state.update(fields, checkedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
        temporary = args.receipt.with_suffix(args.receipt.suffix + f".{os.getpid()}.tmp")
        temporary.write_text(json.dumps(state, indent=2) + "\n")
        temporary.replace(args.receipt)

    def stop(reason, **fields):
        command = [str(args.cli), "stop", args.run_id, "--workspace", str(args.workspace), "--json"]
        result = subprocess.run(command, text=True, capture_output=True, timeout=30)
        try:
            response = json.loads(result.stdout)
        except ValueError:
            response = result.stdout[-4096:]
        save(state=f"stopped-on-{reason}" if result.returncode == 0 else "stop-failed",
             exitCode=result.returncode, command=command, stderr=result.stderr[-4096:],
             response=response, **fields,
             resumeCondition="Qualified dependency return or concrete changed repair input; preserve existing queue")

    save()
    try:
        while True:
            if time.monotonic() >= deadline:
                stop("guard-expired")
                return
            if not args.events.exists():
                time.sleep(max(0.01, args.poll_seconds))
                continue
            if args.events.stat().st_size < cursor:
                raise RuntimeError("Event stream was truncated; loop detection is no longer reliable")
            with args.events.open() as stream:
                stream.seek(cursor)
                while True:
                    start = stream.tell()
                    line = stream.readline()
                    if not line or not line.endswith("\n"):
                        cursor = start
                        break
                    cursor = stream.tell()
                    event = json.loads(line)
                    if event.get("runId") != args.run_id:
                        continue
                    if event.get("type") in ("runner.stopped", "runner.completed", "runner.failed", "runner.finished"):
                        save(state="runner-ended", event=event)
                        return
                    progress = blocked_worker(event, args.run_id, args.workspace)
                    reason = "blocked-worker"
                    if progress is None:
                        progress = completed.inspect(event, args.run_id, args.workspace)
                        reason = "repeated-completed-source"
                    if event.get("type") == "runner.turn_finished" and event.get("role") == "worker":
                        save(lastObservedIteration=event.get("iteration"), sourceFile=event.get("roadmap"),
                             sourceRevision=event.get("sourceRevision"))
                    if progress is None:
                        continue
                    # The exact run ID and workspace are revalidated by the management
                    # CLI; no PID guessing, process-name killing or worktree mutation.
                    stop(reason, progressFile=str(progress), completedIteration=event.get("iteration"))
                    return
            time.sleep(max(0.01, args.poll_seconds))
    except Exception as error:
        # A broken guard must not leave an unattended runner without detection.
        stop("guard-error", error=f"{type(error).__name__}: {error}")
        raise


if __name__ == "__main__":
    main()

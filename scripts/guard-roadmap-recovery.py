#!/usr/bin/env python3
"""Stop one managed runner after a completed BLOCKED worker, preserving its FIFO.

The runner currently re-enters recovery even when no dependency changed. This
event-file guard performs no inference and never restarts a controller.
"""
import argparse
import datetime
import json
from pathlib import Path
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--events", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--cli", required=True, type=Path)
    parser.add_argument("--max-hours", type=float, default=168)
    args = parser.parse_args()
    cursor = args.events.stat().st_size if args.events.exists() else 0
    deadline = time.monotonic() + max(0, args.max_hours) * 3600
    state = {"runId": args.run_id, "workspace": str(args.workspace), "state": "armed"}

    def save(**fields):
        state.update(fields, checkedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
        args.receipt.write_text(json.dumps(state, indent=2) + "\n")

    save()
    while True:
        if time.monotonic() >= deadline:
            save(state="expired", resumeCondition="Hourly monitor may re-arm against the current live run ID")
            return
        if not args.events.exists():
            time.sleep(5)
            continue
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
                if progress is None:
                    continue
                # The exact run ID and workspace are revalidated by the management
                # CLI; no PID guessing, process-name killing or worktree mutation.
                command = [str(args.cli), "stop", args.run_id, "--workspace", str(args.workspace), "--json"]
                result = subprocess.run(command, text=True, capture_output=True, timeout=30)
                save(state="stopped-on-blocked-worker" if result.returncode == 0 else "stop-failed",
                     progressFile=str(progress), completedIteration=event.get("iteration"),
                     exitCode=result.returncode, command=command, stderr=result.stderr,
                     response=json.loads(result.stdout) if result.returncode == 0 else result.stdout,
                     resumeCondition="Qualified dependency return or concrete changed repair input; preserve existing queue")
                return
        time.sleep(5)


if __name__ == "__main__":
    main()

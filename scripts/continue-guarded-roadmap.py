#!/usr/bin/env python3
"""Start one pinned guarded successor after an explicitly authorized run completes."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


def requirements_hash(text):
    text = re.sub(r"^- \[[ xX]\]", "- []", text, flags=re.M)
    text = re.sub(r"^Status: .*", "Status: STATE", text, flags=re.M)
    return hashlib.sha256(text.encode()).hexdigest()


def validate_boundary(status, gates, successors):
    if status.get("processState") != "exited" or status.get("roadmapState") != "complete":
        raise ValueError("Prerequisite run did not exit complete; no successor authorized")
    if status.get("exitCode") != 0:
        raise ValueError("Prerequisite run failed; no successor authorized")
    actual = [(entry["roadmap"], entry["progressFile"]) for entry in status["queue"]]
    expected = [(entry["source"], entry["progress"]) for entry in gates]
    if actual != expected or any(entry["state"] != "complete" for entry in status["queue"]):
        raise ValueError("Prerequisite FIFO or completion differs from adopted plan")
    for entry in gates + successors:
        text = Path(entry["source"]).read_text()
        if requirements_hash(text) != entry["requirementsHash"]:
            raise ValueError("Requirements changed: " + entry["source"])
    for entry in gates:
        text = Path(entry["source"]).read_text()
        checks = re.findall(r"^- \[([ xX])\] (\S+)", text, re.M)
        if (not checks or any(mark.lower() != "x" for mark, _ in checks)
                or not re.search(r"^Status: COMPLETE$", text, re.M)):
            raise ValueError("Prerequisite acceptance remains open: " + entry["source"])
        if not re.search(r"^Status: COMPLETE$", Path(entry["progress"]).read_text(), re.M):
            raise ValueError("Prerequisite progress is not complete: " + entry["progress"])


def write_receipt(path, state, **details):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {"state": state, "at": datetime.datetime.now(datetime.timezone.utc).isoformat(), **details}
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, indent=2) + "\n")
    temporary.replace(path)


def continue_once(plan):
    receipt = Path(plan["receipt"])
    if receipt.exists() and json.loads(receipt.read_text()).get("state") == "started":
        return
    workspace = Path(plan["workspace"]).resolve()
    deadline = time.monotonic() + min(plan.get("deadlineSeconds", 604800), 604800)
    write_receipt(receipt, "waiting", afterRun=plan["afterRun"])
    while True:
        result = subprocess.run([plan["cli"], "status", plan["afterRun"], "--workspace",
                                 str(workspace), "--json"], capture_output=True, text=True,
                                timeout=30, check=True)
        status = json.loads(result.stdout)
        if status["id"] != plan["afterRun"] or Path(status["workspace"]).resolve() != workspace:
            raise ValueError("Runner identity/workspace differs from adopted boundary")
        if status["processState"] not in ("running", "starting"):
            break
        if time.monotonic() >= deadline:
            raise ValueError("Continuation expired; no successor started")
        time.sleep(30)
    validate_boundary(status, plan["gates"], plan["successors"])
    first = plan["successors"][0]
    expected_pending = [{"roadmap": entry["source"], "progressFile": entry["progress"]}
                        for entry in plan["successors"][1:]]
    if json.loads(Path(plan["pendingQueueSpec"]).read_text()) != expected_pending:
        raise ValueError("Successor pending FIFO differs from pinned plan")
    command = [sys.executable, str(workspace / "architecture/scripts/guarded-roadmap-runner.py"),
               "--cli", plan["cli"], "start", first["source"], "--workspace", str(workspace),
               "--progress-file", first["progress"], "--queue-spec", plan["pendingQueueSpec"],
               "--client", "codex", "--timeout", "50m", "--recover-blocked",
               "--resolver-attempts", "1", "--resolver-timeout", "10m", "--blocked-policy", "stop",
               "--notify", "off", "--no-prevent-sleep", "--idempotency-key",
               plan["idempotencyKey"], "--json"]
    result = subprocess.run(command, cwd=workspace, capture_output=True, text=True, timeout=120)
    Path(plan["launchResult"]).write_text(result.stdout)
    Path(plan["launchResult"]).with_suffix(".stderr").write_text(result.stderr)
    if result.returncode:
        raise RuntimeError("Guarded successor launch failed; see launch diagnostics")
    successor = json.loads(result.stdout)
    if successor.get("loopGuard", {}).get("state") != "armed":
        raise ValueError("Guarded successor did not acknowledge live readiness")
    write_receipt(receipt, "started", afterRun=plan["afterRun"], runId=successor["id"],
                  guard=successor["loopGuard"], launchResult=plan["launchResult"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    args = parser.parse_args()
    plan = json.loads(Path(args.plan).read_text())
    try:
        continue_once(plan)
    except Exception as error:
        write_receipt(Path(plan["receipt"]), "stopped", afterRun=plan["afterRun"], reason=str(error))
        raise


if __name__ == "__main__":
    main()

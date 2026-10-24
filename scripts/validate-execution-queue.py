#!/usr/bin/env python3
"""Validate a controller queue against its actual task contracts and receipt owners."""
import argparse
import hashlib
import json
from pathlib import Path
import re

TASK = re.compile(r"^- \[[ xX]\] ([A-Z]+-\d+\.\d+)(?:\s|$)", re.M)
ID = re.compile(r"\b[A-Z]+-\d+\.\d+\b")


def requirements_hash(text):
    text = re.sub(r"^- \[[ xX]\]", "- []", text, flags=re.M)
    text = re.sub(r"^Status: .*", "Status: STATE", text, flags=re.M)
    return hashlib.sha256(text.encode()).hexdigest()


def validate(plan, virtual_sources=None):
    """Return concise errors; virtual sources support review before a safe landing."""
    virtual_sources = virtual_sources or {}
    errors = []
    queue = plan.get("queue", [])
    tasks = plan.get("tasks", {})
    if not queue or not tasks:
        return ["Queue and task ownership map must both be nonempty"]
    if len(queue) > 100:
        errors.append("Managed runner queue exceeds 100 sources")
    positions, progress_paths, actual, sections = {}, set(), {}, {}
    first_verification = None
    last_functional = None
    for index, entry in enumerate(queue):
        source, progress = entry["source"], entry["progress"]
        if source in positions:
            errors.append(f"Duplicate queued source: {source}")
        if progress in progress_paths:
            errors.append(f"Duplicate progress path: {progress}")
        positions[source] = index
        progress_paths.add(progress)
        try:
            text = virtual_sources.get(source)
            if text is None:
                text = Path(source).read_text()
        except OSError as error:
            errors.append(f"Missing source: {source}: {error}")
            continue
        if not re.search(r"^Status: (IN_PROGRESS|COMPLETE|BLOCKED|STOPPED)$", text, re.M):
            errors.append(f"Invalid runtime header: {source}")
        if len(text.encode()) > 32768:
            errors.append(f"Worker source exceeds 32 KiB input budget: {source}")
        expected_hash = entry.get("requirementsHash")
        if expected_hash and expected_hash != requirements_hash(text):
            errors.append(f"Requirements changed without controller reconciliation: {source}")
        found = TASK.findall(text)
        if not found:
            errors.append(f"No parent tasks: {source}")
        for tid in found:
            if tid in actual:
                errors.append(f"Duplicate task ID: {tid}")
            actual[tid] = source
        for section in re.split(r"(?=^### Task )", text, flags=re.M)[1:]:
            match = re.match(r"### Task ([A-Z]+-\d+\.\d+)\b", section)
            if match:
                sections[match[1]] = section
        phases = {tasks[t]["phase"] for t in found if t in tasks}
        if "verification" in phases:
            if len(phases) != 1:
                errors.append(f"Verification mixed with functional work: {source}")
            first_verification = index if first_verification is None else first_verification
        elif phases:
            last_functional = index
    if any(path in positions for path in progress_paths):
        errors.append("A progress file aliases a queued source")
    if first_verification is not None and last_functional is not None and first_verification < last_functional:
        errors.append("Verification is scheduled before required functional delivery")
    for tid, source in actual.items():
        if tid not in tasks:
            errors.append(f"Task has no owner record: {tid}")
        elif tasks[tid].get("source") != source:
            errors.append(f"Task owner differs from actual source: {tid}")
    graph = {}
    for tid, task in tasks.items():
        if tid not in actual:
            errors.append(f"Owner record has no queued implementation task: {tid}")
        if task.get("phase") not in {"functional", "environment", "verification"}:
            errors.append(f"Invalid task phase: {tid}")
        source = task["source"]
        if source not in positions:
            errors.append(f"Task source is not queued: {tid}")
        elif task.get("progress") != queue[positions[source]]["progress"]:
            errors.append(f"Task receipt points to the wrong progress file: {tid}")
        dependencies = task.get("requires", [])
        graph[tid] = set(dependencies)
        for dependency in dependencies:
            owner = tasks.get(dependency)
            if owner is None:
                errors.append(f"Unqueued prerequisite: {tid} -> {dependency}")
            elif source in positions and owner["source"] in positions and positions[owner["source"]] > positions[source]:
                errors.append(f"Prerequisite scheduled after consumer: {tid} -> {dependency}")
        section = sections.get(tid, "")
        declared = set()
        for line in section.splitlines():
            if line.startswith(("Dependencies:", "Entry receipts:")):
                declared.update(ID.findall(line))
                for dependency in ID.findall(line):
                    if dependency not in dependencies:
                        errors.append(f"Source prerequisite missing from dependency map: {tid} -> {dependency}")
                    if line.startswith("Dependencies:") and dependency in tasks and tasks[dependency]["source"] != source:
                        errors.append(f"Cross-file dependency must use Entry receipts: {tid} -> {dependency}")
        for dependency in set(dependencies) - declared:
            errors.append(f"Prerequisite hidden from worker task contract: {tid} -> {dependency}")
    pending = {tid: set(deps) & set(tasks) for tid, deps in graph.items()}
    while pending:
        ready = {tid for tid, deps in pending.items() if not deps}
        if not ready:
            errors.append("Dependency cycle: " + ", ".join(sorted(pending)[:12]))
            break
        pending = {tid: deps - ready for tid, deps in pending.items() if tid not in ready}
    expected_ui = [(x["source"], x["progress"]) for x in plan.get("originalUiPairs", [])]
    if expected_ui:
        expected_sources = {x[0] for x in expected_ui}
        actual_ui = [(x["source"], x["progress"]) for x in queue if x["source"] in expected_sources]
        if len(actual_ui) != len(expected_ui) or set(actual_ui) != set(expected_ui):
            errors.append("Original UI source/progress pairs changed")
        if plan.get("preserveUiOrder", True) and actual_ui != expected_ui:
            errors.append("Original UI source/progress pairs or relative order changed")
        if not plan.get("preserveUiOrder", True) and not plan.get("uiOrderAmendment"):
            errors.append("UI reordering requires a controller amendment")
    if not set(plan.get("originalTaskIds", [])) <= set(tasks):
        errors.append("An original task was dropped")
    for accepted in plan.get("acceptedInputs", []):
        try:
            text = Path(accepted["source"]).read_text()
            progress = Path(accepted["progress"])
            if requirements_hash(text) != accepted["requirementsHash"]:
                errors.append(f"Accepted prerequisite requirements changed: {accepted['source']}")
            if hashlib.sha256(progress.read_bytes()).hexdigest() != accepted["progressSha256"]:
                errors.append(f"Accepted prerequisite evidence changed: {progress}")
            for tid in accepted["taskIds"]:
                if not re.search(r"^- \[x\] " + re.escape(tid) + r"\s", text, re.M):
                    errors.append(f"Accepted prerequisite is unchecked: {tid}")
        except OSError as error:
            errors.append(f"Accepted prerequisite evidence missing: {error}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--pending-patches", type=Path)
    arguments = parser.parse_args()
    plan = json.loads(arguments.manifest.read_text())
    virtual = {}
    if arguments.pending_patches:
        virtual = {key: value["afterText"] for key, value in json.loads(arguments.pending_patches.read_text()).items()}
    errors = validate(plan, virtual)
    print(json.dumps({"sources": len(plan.get("queue", [])), "parents": len(plan.get("tasks", {})),
                      "dependencyEdges": sum(len(t.get("requires", [])) for t in plan.get("tasks", {}).values()),
                      "externalInputsPending": sum(x.get("state") != "ready" for x in plan.get("externalInputs", [])),
                      "failures": len(errors), "errors": errors}, indent=2))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())

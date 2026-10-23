#!/usr/bin/env python3
"""Build RRD-1.3's bounded owner/selector handoff without application execution.

Run from the workspace after readiness-inventory.py. --check authenticates the
saved handoff, including current source/dependency and workspace ownership facts.
Availability probe receipts are reused; no runtime, suite or provider is invoked.
Consumers read prerequisites.RRD-1.3, then only their entries/tasks/original rows.
"""

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
from readiness_config import Locations, arguments


ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "architecture/runner-queues/emulator-web-readiness-20261022"
STATE = ROOT / ".roadmap-runner/emulator-web-readiness-20261022"
STORE = ROOT / "architecture/.artifacts/emulator-web-readiness-20261022/handoff.json"
LINK = STATE / "handoff.json"
ID = re.compile(r"\b[A-Z][A-Z0-9]*-\d+(?:\.\d+)*\b")
OWNED = {"scripts/readiness-handoff.py", "runner-queues/emulator-web-readiness-20261022/00-reconcile.md"}
CONFIG = Locations()


def configure(manifest, runtime_root=None):
    global CONFIG, QUEUE, STATE, STORE, LINK, OWNED
    CONFIG = Locations(manifest, runtime_root)
    QUEUE, STATE = CONFIG.queue, CONFIG.state
    STORE, LINK = CONFIG.store / "handoff.json", STATE / "handoff.json"
    OWNED = {"scripts/readiness-handoff.py", "scripts/readiness-inventory.py", "scripts/readiness-runtimes.py",
             "scripts/readiness_config.py", "tests/readiness_collectors_test.py",
             str((QUEUE / CONFIG.data['entries'][0]['file']).relative_to(ROOT / 'architecture'))}


def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stable_source(text):
    # Only runner-authorized task state and concise delivery status may differ.
    text = re.sub(r"^- \[[ x]\]", "- [ ]", text, flags=re.M)
    text = re.sub(r"^Current delivery:.*\n\n?", "", text, flags=re.M)
    return re.sub(r"^Status:.*\n", "", text, flags=re.M)


def command(*args):
    return subprocess.check_output(args, text=True).strip()


def acceptance_checkpoint(data):
    """Compare accepted inputs, excluding explicitly unvalidated observations."""
    data = copy.deepcopy(data)
    for repo in data['workspace']['repositories'].values():
        # Current owned staging and unrelated external edits are observations.
        # Preserved paths, source pins, heads and all acceptance rows still match.
        repo.pop('ownedDirtyPaths', None)
        repo.pop('externalInputs', None)
    return data


class Inventory:
    def __init__(self):
        self.checks = 0
        self.errors = []
        self.pins = {}

    def require(self, ok, label):
        self.checks += 1
        if not ok:
            self.errors.append(label)

    def read(self, path):
        path = Path(path)
        name = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        self.pins[name] = sha(path.read_bytes())
        return path.read_text()

    def load(self, path):
        return json.loads(self.read(path))

    def workspace(self, coordination):
        records = {}
        preserved = CONFIG.preserved_inputs(self.load) if CONFIG.successor else {}
        for repo in ["architecture", "core", "cli", "docs"]:
            cwd = str(ROOT / repo)
            branch = command("git", "-C", cwd, "branch", "--show-current")
            dirty = subprocess.check_output(["git", "-C", cwd, "status", "--porcelain=v1", "-uall"], text=True).splitlines()
            self.require(branch == "main", repo + " remains on current main")
            # Capture every path; do not stash, reset or stage unrelated work.
            preserved_paths = {r["path"]: r for r in preserved.get(repo, [])}
            external = []
            for path, row in preserved_paths.items():
                current_sha = sha((ROOT / repo / path).read_bytes())
                if row.get('externalOwner'):
                    external.append({'path': path, 'owner': row['externalOwner'], 'observedSha256': row['sha256'],
                                     'currentSha256': current_sha, 'state': 'external active edit; unvalidated'})
                else:
                    original = CONFIG.preserved_path(row, ROOT / repo / path)
                    original_sha = sha(original.read_bytes())
                    self.pins[str(original.relative_to(ROOT))] = original_sha
                    self.require(original_sha == row['sha256'], repo + " preserved " + path)
                    if row.get('evolvedOwner'):
                        external.append({'path': path, 'owner': row['evolvedOwner'], 'originalSha256': row['sha256'],
                                         'preservedAt': str(original), 'currentSha256': current_sha,
                                         'state': 'original bytes authenticated; evolved live source unvalidated'})
            unowned = [r for r in dirty if not (repo == 'architecture' and r[3:] in OWNED) and r[3:] not in preserved_paths]
            # A successor worker must preserve concurrent controller edits too.
            # Inventory them explicitly; their existence grants no write/commit
            # ownership and is never accepted implementation evidence.
            if CONFIG.successor:
                for row in unowned:
                    path = ROOT / repo / row[3:]
                    external.append({'path': row[3:], 'status': row[:2],
                        'currentSha256': sha(path.read_bytes()) if path.is_file() else None,
                        'owner': 'external concurrent task; not owned by this collector',
                        'state': 'unvalidated; preserve outside this worker commit'})
            self.require(CONFIG.successor or not unowned, repo + " owned or explicitly external dirty paths")
            records[repo] = {"branch": branch, "head": command("git", "-C", cwd, "rev-parse", "HEAD"),
                             "ownedDirtyPaths": [r[3:] for r in dirty if repo == 'architecture' and r[3:] in OWNED],
                             "preservedDirtyPaths": [r[3:] for r in dirty if r[3:] in preserved_paths and not preserved_paths[r[3:]].get('externalOwner')],
                             "externalInputs": external}
        processes = command("ps", "-axo", "pid,ppid,command").splitlines()
        controllers = []
        for line in processes:
            columns = line.split(None, 2)
            if len(columns) != 3:
                continue
            pid, _, argv = columns
            controller = re.fullmatch(r"\S+ (\S*/roadmap-runner/dist/worker\.js) (.+) ([a-f0-9]{24})", argv)
            # Match actual controller argv, never a shell or a worker prompt.
            if not controller:
                continue
            state_file = Path(controller[2]) / "runs" / controller[3] / "state.json"
            if state_file.exists():
                state = json.loads(state_file.read_text())
                controllers.append({"pid": int(pid), "runId": controller[3], "workspace": state["workspace"]})
        current = [p for p in controllers if p["workspace"] == str(ROOT)]
        retired = [p for p in controllers if p["workspace"].startswith(str(ROOT) + "-")]
        self.require(len(current) == 1 and current[0]["runId"] == coordination["primaryRunId"]
                     and current[0]["pid"] == coordination["primaryPid"], "one matching current-root controller")
        self.require(not retired and coordination["parallelState"] == "stopped", "retired edit-ac controllers stopped")
        self.require(coordination["singleWorkspaceOnly"], "single-workspace authority")
        return {"repositories": records, "controllers": current, "retiredControllers": retired,
                "unrelatedControllersPreserved": [p for p in controllers if p not in current and p not in retired],
                "checkpoint": "Acquire .roadmap-coordination/integration.lock; commit only validated owned source on existing main after two parents and at source boundaries. Never stash/reset or stage other work.",
                "ignoredScratch": str(STORE.parent), "progressRoot": str(STATE),
                "runtimeQualification": "none; controller/source inventory only"}

    def selectors(self, text, row, mac_suites):
        validation = text.split("\nValidation:", 1)[1].split("\nEvidence:", 1)[0]
        commands = re.findall(r"`((?:bash|powershell|cargo|npm|node|swift|python3) [^`\n]+)`", validation)
        if not commands:
            commands = re.findall(r"(?:-V\d+ )((?:cargo|npm|bash|powershell) .+?)(?=\. (?:Drive|Assert|Require)|$)", validation, re.M)
        result = []
        cwd = ROOT / ("cli" if row["profile"] == "terminal" else "core")
        for cmd in dict.fromkeys(commands):
            parts = shlex.split(cmd)
            status = "needs-owner-selector-authentication"
            missing = []
            if parts[0] in ["bash", "powershell"]:
                i = parts.index("-File") + 1 if "-File" in parts else 1
                path = cwd / parts[i]
                if path.exists():
                    self.read(path)
                    if parts[i] == "native/macos/scripts/check.sh":
                        status = "declared-dispatcher-selector" if parts[-1] in mac_suites else "missing-dispatcher-selector"
                        if status.startswith("missing"):
                            missing.append(parts[-1])
                    else:
                        status = "existing-driver-needs-target-authentication"
                else:
                    status = "missing-dispatcher"
                    missing.append(str(path.relative_to(ROOT)))
            elif parts[0] == "cargo" and "--test" in parts:
                target = parts[parts.index("--test") + 1].rstrip(".")
                path = cwd / "tests" / (target + ".rs")
                if path.exists():
                    self.read(path)
                    status = "declared-cargo-test-target"
                else:
                    status = "missing-cargo-test-target"
                    missing.append(str(path.relative_to(ROOT)))
            result.append({"command": cmd, "cwd": str(cwd), "state": status,
                           "missing": missing, "executed": False})
        return {"validationRef": f"architecture/roadmaps/{row['source']}#task-{row['original'].lower()}",
                "validationSha256": sha(validation.encode()), "commands": result,
                "repairOwner": row["testingOwner"],
                "repair": "Final testing owner supplies missing dispatchers/variants on the original implementation owner; existing selectors are prerequisite evidence only. Require nonzero execution and truthful failure/skip counts.",
                "cost": {"focusedExpectedMinutes": [1, 5], "finalGroupPlanningMinutes": [15, 45],
                         "measuredSeconds": None, "state": "unmeasured; planning bounds are not observed suite costs",
                         "owner": row["testingOwner"],
                         "beforeFullRun": "Reuse exact current-source full receipts or enumerate discovery and measure cost; request a controller split if indivisible full command exceeds worker allowance. Never run partial coverage as full."}}

    def build(self):
        source = module("readiness-inventory")
        runtimes = module("readiness-runtimes")
        source.configure(CONFIG.manifest, STATE)
        runtimes.configure(CONFIG.manifest, STATE)
        upstream = self.load(STATE / "readiness.json")
        runtime = self.load(STATE / "runtimes.json")
        # Authenticate existing passing inventories, without redoing availability probes.
        current = source.build()
        upstream_checks = source.validate(current)
        self.require(upstream == current, "RRD-1.1 current-source inventory unchanged")
        runtime_checks = runtimes.validate(runtime)
        manifest = self.load(QUEUE / "manifest.json")
        mapping = self.load(QUEUE / "requirement-map.json")
        coordination = self.load(ROOT / ".roadmap-coordination/queue.json")
        workspace = self.workspace(coordination)
        self.require(manifest["workspace"] == str(ROOT) and manifest["mode"] in {"single-workspace-main", "single-workspace-main-feature-first"}, "queue workspace/profile")
        baseline = command("git", "-C", str(ROOT / "architecture"), "log", "-1", "--format=%H", "--", str(CONFIG.manifest.relative_to(ROOT / "architecture")))
        entries, tasks, sources = [], {}, {}
        for index, entry in enumerate(manifest["entries"]):
            path = QUEUE / entry["file"]
            text = path.read_text()
            raw = sha(path.read_bytes())
            if raw != entry["sha256"]:
                original = command("git", "-C", str(ROOT / "architecture"), "show", baseline + ":" + str(path.relative_to(ROOT / "architecture"))) + "\n"
                self.require(sha(original.encode()) == entry["sha256"], entry["file"] + " authored hash")
                self.require(stable_source(text) == stable_source(original), entry["file"] + " only authorized state changes")
            else:
                self.require(True, entry["file"] + " authored hash")
            sources[entry["file"]] = {"authoredSha256": entry["sha256"], "criteriaSha256": sha(stable_source(text).encode())}
            parents = re.findall(r"^### Task (\S+)", text, re.M)
            self.require(len(parents) == entry["parents"], entry["file"] + " parent count")
            self.require(Path(entry["progressFile"]).is_relative_to(ROOT / ".roadmap-runner"), entry["file"] + " current-root progress")
            for task in parents:
                self.require(task not in tasks, task + " unique queue owner")
                section = source.section(text, task)
                deps = ID.findall(source.field(section, "Dependencies") or "")
                self.require(all(d in parents and parents.index(d) < parents.index(task) for d in deps), task + " local dependency order")
                tasks[task] = {"file": entry["file"], "phase": entry["phase"], "order": index,
                               "localDependencies": deps, "prerequisiteRows": [],
                               "acceptanceSha256": sha(source.field(section, "Acceptance").encode()),
                               "sourceRef": str(path.relative_to(ROOT)) + "#task-" + task.lower()}
            entries.append({"file": entry["file"], "parents": parents, "phase": entry["phase"],
                            "progressFile": entry["progressFile"], "entryTaskPrerequisites": entry["entryTaskPrerequisites"],
                            "consume": ["handoff.json.prerequisites." + ("SFC-1.1" if CONFIG.successor else "RRD-1.3"), "handoff.json.tasks.<active-id>", "readiness.json relevant original/suite rows", "runtimes.json relevant target/toolchain row"],
                            "entryConditions": entry["entryConditions"]})
        # Reuse the authored contract with the queue's actual pinned runner version.
        contract = Path.home() / ".nvm/versions/node/v24.21.0/lib/node_modules/@bpstr/roadmap-runner/dist/roadmap-contract.js"
        runner = self.load(contract.parent.parent / "package.json")
        self.read(contract)
        self.require(runner["version"] == manifest["runnerVersion"], "queue runner contract version")
        node = Path.home() / ".nvm/versions/node" / ("v" + json.loads((ROOT / "core/package.json").read_text())["engines"]["node"]) / "bin/node"
        js = """import fs from 'node:fs'; import {pathToFileURL} from 'node:url';
const {validateRoadmap}=await import(pathToFileURL(process.argv[1]).href);
const q=process.argv[2], m=JSON.parse(fs.readFileSync(q+'/manifest.json','utf8'));
console.log(JSON.stringify(m.entries.map(e=>({file:e.file,errors:validateRoadmap(fs.readFileSync(q+'/'+e.file,'utf8'))}))));"""
        contract_results = json.loads(command(str(node), "--input-type=module", "-e", js, str(contract), str(QUEUE)))
        for result in contract_results:
            self.require(not result["errors"], result["file"] + " runner contract: " + "; ".join(result["errors"]))
        for entry in entries:
            for dep in entry["entryTaskPrerequisites"]:
                self.require(dep in tasks and tasks[dep]["order"] < tasks[entry["parents"][0]]["order"], entry["file"] + " cross-file entry prerequisite " + dep)
        mac_dispatcher = ROOT / "core/native/macos/scripts/check.py"
        tree = ast.parse(self.read(mac_dispatcher))
        mac_suites = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "SUITES" for t in n.targets))
        mac_suites = {name: list(selector) for name, selector in mac_suites.items()}
        canonical = self.load(ROOT / "architecture/roadmaps/manifest.json")
        prefix_sources = {r["prefix"]: ROOT / "architecture/roadmaps" / r["file"] for r in canonical["roadmaps"]}
        owners = []
        by_original = {r["original"]: r for r in upstream["nativeAndTerminal"]}
        canonical_tasks = {task: row["source"] for task, row in by_original.items()}
        for mapped in mapping["originalNativeAndTerminalParents"]:
            row = by_original[mapped["original"]]
            original = row["original"]
            original_text = self.read(ROOT / "architecture/roadmaps" / row["source"])
            section = source.section(original_text, original)
            self.require(sha(section.encode()) == row["canonicalSectionSha256"], original + " canonical section pin")
            test = mapped["testingOwner"]
            impl = mapped.get("featureTask")
            self.require(test in tasks and tasks[test]["file"] == mapped["testingFile"], original + " unique final-test reference")
            if impl:
                projection = source.section((QUEUE / mapped["featureFile"]).read_text(), impl)
                self.require(impl in tasks and tasks[impl]["file"] == mapped["featureFile"], original + " implementation reference")
                self.require(row["currentAcceptance"] in source.field(projection, "Acceptance"), original + " full original acceptance preserved")
                self.require(test in source.field(projection, "Acceptance"), original + " retained final predicate owner")
                self.require(tasks[impl]["order"] < tasks[test]["order"], original + " implementation before final test")
            prerequisites = []
            for prior in mapped.get("priorTasks", []):
                if prior not in canonical_tasks:
                    path = prefix_sources[prior.split("-")[0]]
                    source.section(self.read(path), prior)
                    canonical_tasks[prior] = path.name
                self.require(prior in canonical_tasks, original + " canonical prior owner " + prior)
                prior_row = by_original.get(prior)
                projected = prior_row.get("featureTask") if prior_row else None
                if projected:
                    self.require(tasks[projected]["order"] <= tasks[impl]["order"], original + " prior projection order " + prior)
                prerequisites.append({"original": prior, "implementationOwner": projected or prior,
                                      "source": "architecture/roadmaps/" + canonical_tasks[prior],
                                      "consume": "readiness.json.nativeAndTerminal original=" + prior,
                                      "state": "authenticate exact interface before use; whole-platform completion is not a prerequisite"})
            if impl:
                tasks[impl]["prerequisiteRows"] = prerequisites
                tasks[impl]["originalOwners"] = [original]
            # Qualification-only originals are implemented/repaired by their existing
            # original owner inside the final-test boundary, never duplicated.
            owners.append({"original": original, "profile": row["profile"],
                           "implementationOwner": impl or original, "testingOwner": test,
                           "implementationDisposition": "feature-projection" if impl else "qualification-only; final-test owner audits/repairs original owner",
                           "acceptanceRef": f"architecture/roadmaps/{row['source']}#task-{original.lower()}",
                           "acceptanceSha256": sha(row["currentAcceptance"].encode()), "caseTokens": row["caseTokens"],
                           "reusedDeliveries": row["reusedDeliveries"], "prerequisites": prerequisites,
                           "selectors": self.selectors(section, row, mac_suites),
                           "state": "unqualified; no source or target runtime gate closed"})
        self.require(len(owners) == 166 and len({r["original"] for r in owners}) == 166, "all original predicate owners unique")
        for task, item in tasks.items():
            if item["phase"] != "implementation" or item.get("originalOwners"):
                continue
            if CONFIG.successor and task.startswith("SFC-"):
                item["originalOwners"] = [task]
                item["policyRef"] = "architecture/decisions/006-single-format-before-publication.md"
                item["prerequisiteRows"] = [{"original": dep, "state": "requires verified current-format interface; metadata is not cutover proof"}
                                            for dep in item["localDependencies"]]
                continue
            section = source.section((QUEUE / item["file"]).read_text(), task)
            context = source.field(section, "Context")
            originals = set(ID.findall(context))
            mapped_originals = {original for original, target in mapping['performanceOwners'].items() if target == task}
            originals.update(mapped_originals)
            for match in re.finditer(r"\b([A-Z][A-Z0-9]*-\d+)\.(\d+)[–−-](?:\d+\.)?(\d+)\b", context):
                originals.update(f"{match[1]}.{n}" for n in range(int(match[2]), int(match[3]) + 1))
            item["originalOwners"] = sorted(originals)
            self.require(bool(originals), task + " named original owner")
            for original in sorted(originals):
                if original.startswith("NPR-"):
                    path = Path("/Users/bpstr/Github/edit-ac-shared-features-20261016/.roadmap-runner/post-alpha-performance-20261019/roadmap.md")
                elif original in tasks:
                    path = QUEUE / tasks[original]["file"]
                elif original.startswith("RWP-") and CONFIG.successor:
                    path = ROOT / "architecture/runner-queues/emulator-web-readiness-20261022/01-web-performance-repairs.md"
                else:
                    path = prefix_sources[original.split("-")[0]]
                original_section = source.section(self.read(path), original)
                item.setdefault("originalRefs", []).append({"original": original, "source": str(path),
                    "acceptanceSha256": sha(source.field(original_section, "Acceptance").encode()),
                    "disposition": "Repair only this original owner; originating runtime/performance thresholds remain with the named final-test owner."})
                self.require(original in context or original in mapped_originals or original.startswith("SDK-1."), task + " original reference " + original)
        for key in ["performanceOwners", "aggregateOwners"]:
            for original, targets in mapping[key].items():
                for target in ID.findall(targets):
                    self.require(target in tasks, key + " reference " + original + " -> " + target)
        # Shared semantic dependencies stay with canonical owners. Missing
        # historical proof must never be turned into replacement engine code.
        repairs = [{"original": r["original"], "implementationOwner": r["implementationOwner"],
                    "testingOwner": r["testingOwner"], "selectors": r["selectors"]["validationRef"],
                    "missing": c["missing"], "command": c["command"],
                    "repair": "Supply this exact original-owner dispatcher/target/selector in its bounded feature/final-test parent; do not duplicate shared semantics."}
                   for r in owners for c in r["selectors"]["commands"] if c["missing"]]
        for r in owners:
            if not r["selectors"]["commands"]:
                repairs.append({"original": r["original"], "implementationOwner": r["implementationOwner"],
                                "testingOwner": r["testingOwner"], "repair": "Authenticate the original validation and create an explicit nonzero selector on this original owner before final testing."})
        for retained in upstream["portableReturns"]:
            if retained["missingFiles"]:
                repairs.append({"original": retained["originalOwner"], "implementationOwner": retained["implementationOwner"],
                    "testingOwner": retained["testingOwner"], "missing": retained["missingFiles"],
                    "evidence": "readiness.json.portableReturns id=" + retained["id"],
                    "repair": "Authenticate current original-owner format interfaces and replace absent obsolete proof helpers on the existing final-test owner if needed. Missing historical helpers do not authorize duplicate format/engine semantics or fabricated qualification."})
        self.require(subprocess.run(["git", "-C", str(ROOT / "architecture"), "check-ignore", "-q", str(STORE)]).returncode == 0, "ignored handoff storage")
        self.read(Path(__file__))
        parent = "SFC-1.1" if CONFIG.successor else "RRD-1.3"
        return {"schemaVersion": 1, "parent": parent,
                "prerequisites": {parent: {"state": "ownership-handoff-verified", "nextOwner": "SFC-1.2" if CONFIG.successor else "RWP-1.1",
                    "requires": [] if CONFIG.successor else ["RRD-1.1", "RRD-1.2"], "runtimeQualification": "none; all final runtime/full-suite predicates remain open"}},
                "workspace": workspace, "authoredQueueRevision": baseline, "sources": sources,
                "entries": entries, "tasks": tasks, "originals": owners, "repairRequests": repairs,
                "performanceOwners": mapping["performanceOwners"], "aggregateOwners": mapping["aggregateOwners"],
                "runtimeConstraints": {p: {"implementationOwner": t["implementationOwner"], "testingOwners": t["testingOwners"],
                    "unavailablePrerequisites": t["unavailablePrerequisites"], "packageRoute": t["packageRoute"],
                    "independentWork": "Current-source implementation and available profile checks remain eligible; required unavailable target assertions stay unproven."}
                    for p, t in runtime["targets"].items()},
                "sharedPrerequisitePolicy": {"consume": "readiness.json relevant suite/portableReturns and exact canonical Context; use only current-source accepted interfaces",
                    "missingInput": "Record canonical original task/source/hash, exact absent interface and original-owner repair within current bounded parent. Never replace engine semantics in a platform adapter.",
                    "historicalReceipts": "Absent generated output and old BLOCKED/COMPLETE labels neither prove missing code nor qualify current behavior."},
                "staleStateDispositions": upstream["staleStateDispositions"],
                "transferredCoverage": {"rows": len(upstream["transferred"]), "consume": "readiness.json.transferred by original ID; unresolved case tokens remain unchanged",
                    "virtualOwner": "QRD-1.2", "excludedClaims": manifest["excludedClaims"],
                    "physicalOnly": "separately unexecuted, never a prerequisite; required virtual variants retained"},
                "dispatcherInventory": {"macos": {"source": str(mac_dispatcher.relative_to(ROOT)), "selectors": mac_suites,
                    "perStepTimeoutSeconds": [180, 300], "runtimeQualification": "not executed; timeouts are not measured suite costs"},
                    "web": {"source": "core/scripts/test-browser.mjs", "fullDiscoveryOwner": "QWB-1.1"},
                    "shared": runtime["toolchains"]["shared"], "terminal": runtime["toolchains"]["terminal"]},
                "reusedValidation": {"authoredQueue": baseline,
                    "sourceInventory": upstream_checks, "runtimeMetadata": runtime_checks["inventoryChecks"],
                    "availabilityProbesExecutedThisInvocation": 0, "queueContractFiles": len(contract_results)},
                "sourcePins": dict(sorted(self.pins.items()))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    arguments(parser)
    args = parser.parse_args()
    configure(args.manifest, args.runtime_root)
    inventory = Inventory()
    data = inventory.build()
    if args.check:
        saved = json.loads(LINK.read_text())
        inventory.require(acceptance_checkpoint(saved) == acceptance_checkpoint(data),
                          "saved handoff matches current sources/owners/workspace; refresh after changed inputs")
    report = {"executed": inventory.checks, "passed": inventory.checks - len(inventory.errors),
              "failed": len(inventory.errors), "skipped": 0, "errors": inventory.errors,
              "queueFiles": len(data["entries"]), "parents": len(data["tasks"]), "originalOwners": len(data["originals"]),
              "repairRequests": len(data["repairRequests"]), "applicationTestsExecuted": 0, "runtimeProbesExecuted": 0,
              "providerRequests": 0, "output": str(LINK)}
    print(json.dumps(report, sort_keys=True))
    if inventory.errors:
        return 1
    if not args.check:
        if LINK.exists() and not LINK.is_symlink():
            raise ValueError("Refuse to replace existing regular handoff")
        if LINK.is_symlink() and LINK.resolve() != STORE:
            raise ValueError("Refuse to replace another owner's handoff link")
        STORE.parent.mkdir(parents=True, exist_ok=True)
        STORE.write_text(json.dumps(data, indent=2) + "\n")
        if not LINK.is_symlink():
            CONFIG.link(LINK, STORE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

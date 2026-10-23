#!/usr/bin/env python3
"""Reconcile RRD-1.1 inputs without executing application/provider checks.

Supply --manifest and optional --runtime-root for a successor queue.
Run from the workspace: python3 architecture/scripts/readiness-inventory.py
Use --check to authenticate an existing inventory against the same inputs.
The workspace-facing JSON links to ignored architecture/.artifacts storage.
This inventory records proof availability; it never qualifies a runtime.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from readiness_config import Locations, arguments


ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "architecture/runner-queues/emulator-web-readiness-20261022"
STATE = ROOT / ".roadmap-runner/emulator-web-readiness-20261022"
OUTPUT = STATE / "readiness.json"
STORAGE = ROOT / "architecture/.artifacts/emulator-web-readiness-20261022/readiness.json"
CASE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z]+)*-\d+(?:\.\d+)*(?:[–−-]\d+)?\b")
PINS = {}
CONFIG = Locations()


def configure(manifest, runtime_root=None):
    global CONFIG, QUEUE, STATE, OUTPUT, STORAGE
    CONFIG = Locations(manifest, runtime_root)
    QUEUE, STATE = CONFIG.queue, CONFIG.state
    OUTPUT, STORAGE = STATE / "readiness.json", CONFIG.store / "readiness.json"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(ROOT / repo), *args], text=True).strip()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def ref(path):
    path = Path(path).absolute()
    name = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    PINS[name] = digest(path.read_bytes())
    return name


def read(path):
    path = Path(path)
    ref(path)
    return path.read_text()


def load(path):
    return json.loads(read(path))


def section(text, task):
    match = re.search(r"^### Task " + re.escape(task) + r"\b.*?(?=^### Task |\Z)", text, re.M | re.S)
    if not match:
        raise ValueError(f"Missing canonical task {task}")
    return match.group()


def field(text, name):
    match = re.search(r"^" + name + r": (.*)$", text, re.M)
    return match[1] if match else None


def cases(text):
    # Retain ranges literally; the source reference/digest remains authoritative.
    return sorted(set(CASE.findall(text)))


def paths_from(text):
    paths = set()
    for token in re.findall(r"`([^`\n]+)`", text):
        for part in token.split(";"):
            part = part.strip()
            if "/" in part and not any(c in part for c in " *<>{}()"):
                candidate = ROOT / part
                if not candidate.exists():
                    candidate = ROOT / "core" / part
                if candidate.exists() and candidate.is_relative_to(ROOT):
                    paths.add(str(candidate.relative_to(ROOT)))
    return sorted(paths)


# Authored task-to-delivery associations. Runtime results stay in named progress.
DELIVERIES = [
    ("D24P-1.1", "9e61dd5", "shared", "NRB-1.1", 12),
    ("D24P-1.2", "5168537", "shared", "NRB-1.2", 6),
    ("D24P-1.3", "a13a919", "shared", "NRB-1.2", 6),
    ("D24P-1.4", "ded1f5c", "shared", "NRB-1.3", 11),
    ("D24P-1.5", "71134f4", "shared", "NRB-1.4", None),
    ("D24P-2.1", "e15314f", "macos", "DSK-1.18", 5),
    ("D24P-2.2", "4941954", "macos", "DSK-1.18", 7),
    ("D24P-2.3", "1246590", "macos", "DSK-1.18", 5),
    ("D24P-2.4", "243a497", "macos", "DSK-1.18", 2),
    ("D24P-3.1", "c799e97", "ios", "IOS-1.18", 4),
    ("D24P-3.2", "7ceb604", "ios", "IOS-1.18", 4),
    ("D24P-3.3", "cc494ce", "ios", "IOS-1.18", 4),
    ("D24P-3.4", "c4e08f1", "ios", "IOS-1.18", 2),
    ("D24P-4.1", "ea1cc50", "android", "AND-1.18", 4),
    ("D24P-4.2", "2f365d6", "android", "AND-1.18", 4),
    ("D24P-4.3", "855108b", "android", "AND-1.18", 4),
    ("D24P-4.4", "8c3ae57", "android", "AND-1.18", 2),
]
RETURNS = [
    ("portable-browser-commands", "feec140", "INT-1.18", "QWB-1.1"),
    ("native-session-commands", "9ab8759", "DSK-1.7", "QMC-1.1"),
    ("native-clipboard-formats", "c50f546", "DSK-1.13", "QMC-1.2"),
    ("rich-browser-format-return", "c4f45d1", "FMT-1.13", "QWB-1.7"),
]


def commit_evidence(short):
    commit = git("core", "rev-parse", short)
    subprocess.run(["git", "-C", str(ROOT / "core"), "merge-base", "--is-ancestor", commit, "HEAD"], check=True)
    changed = git("core", "diff-tree", "--no-commit-id", "--name-only", "-r", "-m", commit).splitlines()
    files = sorted(set(p for p in changed if (ROOT / "core" / p).is_file()))
    unchanged, evolved = [], []
    for name in files:
        now = ref(ROOT / "core" / name)
        old = subprocess.check_output(["git", "-C", str(ROOT / "core"), "show", f"{commit}:{name}"])
        (unchanged if digest(old) == PINS[now] else evolved).append(now)
    return {"commit": commit, "ancestorOfCurrentMain": True, "retainedFiles": unchanged,
            "laterModifiedFiles": evolved, "missingFiles": sorted(set(changed) - set(files)),
            "applicability": "retained implementation; changed inputs require affected proof authentication; no fresh runtime claim"}


def authenticate_pins(pins, base):
    rows = []
    for name, expected in sorted(pins.items()):
        path = Path(name) if Path(name).is_absolute() else base / name
        actual = digest(path.read_bytes()) if path.is_file() else None
        rows.append({"path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                     "expectedSha256": expected, "currentSha256": actual,
                     "state": "matched" if actual == expected else "changed" if actual else "absent-historical-input"})
        if path.is_file():
            ref(path)
    return rows


def preserved_work():
    baseline = CONFIG.preserved_inputs(load)
    if len([r for r in baseline["core"] if not r.get('externalOwner')]) != 44:
        raise ValueError("Expected 44 preserved core paths")
    old_manifest = load(ROOT / "architecture/runner-queues/emulator-web-readiness-20261022/manifest.json")
    progress_path = Path(old_manifest["entries"][1]["progressFile"])
    progress = read(progress_path)
    accepted = []
    proof_owners = {}
    receipt_names = [("RWP-1.1-I1", "rwp-1.1"), ("RWP-1.1-I2", "rwp-1.1-i2"),
                     ("RWP-1.1-I3", "rwp-1.1-i3"), ("RWP-1.2-I1-G1", "rwp-1.2")]
    receipt_names += [(f"RWP-1.2-I1-S1-G{n}", f"rwp-1.2-s1-g{n}") for n in range(2, 8)]
    for task, directory in receipt_names:
        path = ROOT / "core/.artifacts" / directory / "receipt.json"
        if task not in progress:
            raise ValueError("Missing accepted progress reference: " + task)
        row = {"id": task, "progress": str(progress_path), "receipt": str(path),
               "state": "historical-accepted; current runtime qualification not inferred"}
        if path.is_file():
            receipt = load(path)
            expected = re.search(re.escape('core/.artifacts/' + directory + '/receipt.json') + r'`[^\n]*?SHA256 `([a-f0-9]{64})`', progress)
            if expected and digest(path.read_bytes()) != expected[1]:
                raise ValueError("Historical receipt hash differs from accepted progress: " + task)
            pins = dict(receipt.get("sourcePins", {}))
            owned = receipt.get("ownedAuthoredSource", receipt.get("ownedSource", {}))
            if isinstance(owned, dict):
                pins.update(owned)
            for name in owned:
                proof_owners[name] = task
            notice = receipt.get('generatedNotice')
            if notice:
                pins[notice['path']] = notice['sha256']
                proof_owners[notice['path']] = task + ' generated-notice; never stage as authored source'
            row.update(receiptSha256=digest(path.read_bytes()),
                       inputAuthentication=authenticate_pins(pins, ROOT / "core"),
                       counts=receipt.get("acceptedCounts", receipt.get("finalAcceptedCoverage", receipt.get("counts"))),
                       commands=receipt.get("commands", [
                           {k: c[k] for k in ["command", "args", "exit", "counts", "executed", "passed", "failed", "skipped"] if k in c}
                           for c in receipt.get("checks", [])]),
                       runtime=receipt.get("runtime", receipt.get("runtimes", receipt.get("runtimeProvenance"))),
                       failureDispositions={k: receipt[k] for k in ["failureDispositions", "earlierFailures", "earlierSetupFailures"] if k in receipt})
            row["reuse"] = "Matching input hashes retain scoped historical evidence only; changed or absent inputs require owner proof. No aggregate replay/cutover/size qualification."
        else:
            row.update(receiptSha256=None, inputAuthentication=[],
                       reuse="Named progress preserves accepted history; removed generated receipt is not a prerequisite or current proof.")
        accepted.append(row)
    preserved = []
    for repo, rows in baseline.items():
        for old in rows:
            path = ROOT / repo / old["path"]
            actual = digest(path.read_bytes()) if path.is_file() else None
            if not actual:
                raise ValueError("Preserved input changed: " + str(path))
            preserved_path = path if old.get('externalOwner') else CONFIG.preserved_path(old, path)
            ref(preserved_path)
            ref(path)
            matches = [r['id'] for r in accepted if any(p['path'] == str(path.relative_to(ROOT)) and p['state'] == 'matched'
                                                       for p in r['inputAuthentication'])]
            historical_owner = old.get('externalOwner') or proof_owners.get(old['path'])
            if repo == 'core':
                next_owner = ('SFC-2.3' if old['path'] in ['crates/editac-core/src/editor.rs', 'crates/editac-core/src/editor_replay.rs', 'crates/editac-core/src/lib.rs']
                              else 'SFC-4.1' if old['path'].startswith('crates/editac-core/tests/') or old['path'] == 'tests/wasm-commands.test.mjs'
                              else 'SFC-3.2' if '/commands/' in old['path']
                              else 'SFC-3.3' if old['path'].startswith('crates/')
                              else 'RBO-1.1')
            else:
                next_owner = 'controller'
            preserved.append({"repo": repo, **old, "preserved": digest(preserved_path.read_bytes()) == old['sha256'],
                "preservedAt": str(preserved_path), "currentSha256": actual,
                "state": "external active edit; excluded from this worker's accepted proof" if old.get('externalOwner') else "original bytes preserved; evolved live source unvalidated" if old.get('evolvedOwner') else "original bytes preserved",
                "historicalOwner": historical_owner or ('interrupted-G8' if next_owner == 'SFC-2.3' else 'controller' if repo != 'core' else 'predecessor; matching proof references below'),
                "matchingEvidence": matches, "deliveryOwner": old.get('deliveryOwner', next_owner),
                "commitDisposition": "preserve pending cutover owner; historical affected-runtime evidence is not current cutover proof"})
    commits = {}
    for repo, short in {"architecture": "94c53f2", "core": "6a6482d", "cli": "ff768a1", "docs": "663f0dd"}.items():
        commit = git(repo, "rev-parse", short)
        subprocess.run(["git", "-C", str(ROOT / repo), "merge-base", "--is-ancestor", commit, "HEAD"], check=True)
        commits[repo] = {"commit": commit, "ancestorOfMain": True,
                         "paths": git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines()}
    return {"baselineRef": str(ROOT / ".roadmap-runner/emulator-web-readiness-20261022/pre-schema-policy-dirty-inputs.json"),
            "paths": preserved, "initialCommits": commits, "accepted": accepted,
            "interrupted": {"id": "RWP-1.2-I1-S1-G8", "state": "interrupted-unvalidated", "owner": "SFC-2.3",
                            "resume": "current-format replay cutover, preserving original regression assertions; no dual-runtime optimization"}}


def build():
    PINS.clear()
    ref(Path(__file__))
    queue = load(ROOT / ".roadmap-coordination/queue.json")
    manifest = load(CONFIG.manifest)
    ref(Path(__file__).with_name("readiness_config.py"))
    canonical = load(ROOT / "architecture/roadmaps/manifest.json")
    mapping = load(QUEUE / "requirement-map.json")
    transfer = load(ROOT / "architecture/operations/device-requirements-20261018.json")
    ledger = load(ROOT / "core/fixtures/product-scenarios/web/features.json")
    for file in ["FEATURES.md", "ALPHA.md"]:
        ref(ROOT / "core/examples/task-editor" / file)
    for file in ["Cargo.toml", "Cargo.lock", "native/SHARED_REVIEW.md",
                 "crates/editac-ffi/src/session_review.rs", "crates/editac-session/src/history_store.rs",
                 "crates/editac-diff/src/portable.rs", "crates/editac-ffi/generated/EditacNative.swift",
                 "native/macos/Package.swift", "native/ios/Package.swift"]:
        ref(ROOT / "core" / file)
    sources = {}

    def original(file, task):
        path = ROOT / "architecture/roadmaps" / Path(file).name
        if path.name not in {r["file"] for r in canonical["roadmaps"]}:
            raise ValueError(f"Unknown manifest source {file}")
        if path.name not in sources:
            sources[path.name] = read(path)
        return section(sources[path.name], task)

    prior = queue["previousCompletedFeatureQueue"]
    progress = [read(Path(row["progressFile"])) for row in prior]
    prior_root = Path(prior[0]["progressFile"]).parent.parent
    web_progress_path = prior_root / "web-feature-first-20261018/03-web-alpha-progress.md"
    web_progress = read(web_progress_path)
    native = []
    for item in mapping["originalNativeAndTerminalParents"]:
        text = original(item["source"], item["original"])
        native.append({**item, "profile": {"DSK": "macos", "IOS": "ios", "AND": "android",
            "WIN": "windows", "LNX": "linux", "NIX": "ios", "NLX": "linux", "TUI": "terminal",
            "TCX": "terminal", "NAX": "android", "NMX": "macos", "NWX": "windows"}[item["original"].split("-")[0]],
            "currentAcceptance": field(text, "Acceptance"),
            "canonicalSectionSha256": digest(text.encode()), "caseTokens": cases(text),
            "existingContextPaths": paths_from(field(text, "Context") or ""),
            "implementationOwner": item["featureTask"] or item["original"],
            "implementationState": "owner must authenticate remaining original predicates; existing paths alone are not feature proof",
            "proofState": "final target-runtime/full-suite proof open"})
    by_original = {r["original"]: r for r in native}
    deliveries = []
    for task, commit, platform, owner, count in DELIVERIES:
        group = int(task.split("-")[1].split(".")[0]) - 1
        if not re.search(r"^- \[x\] " + re.escape(task) + r"(?=\s|$)", progress[group], re.M):
            raise ValueError(f"Delivery is not checked in named progress: {task}")
        deliveries.append({"id": task, "profile": platform, "originalOwner": owner,
            "implementationOwner": by_original.get(owner, {}).get("featureTask") or owner,
            "testingOwner": by_original.get(owner, {}).get("testingOwner") or "QSH-1.1",
            "evidenceRef": prior[group]["progressFile"] + "#checked-item-evidence",
            "historicalAcceptedFeatureCases": count, "historicalFailures": "retain dispositions in named evidence; accepted failures/skips zero",
            "proofBoundary": "actual macOS Session/SQLite; iOS/Android adapter compile only, target execution unproven" if platform in ["ios", "android"] else "host feature proof; aggregate runtime/performance remains open",
            **commit_evidence(commit)})
    for row in native:
        row["reusedDeliveries"] = [d["id"] for d in deliveries if d["originalOwner"] == row["original"]]
        if row["reusedDeliveries"]:
            row["implementationState"] = "feature delivered; authenticate retained inputs, do not reimplement from old blockers"
    transferred = []
    for item in transfer["entries"]:
        text = original(item["source"], item["taskId"])
        old = "\n".join(item["originalParagraphs"])
        native_row = by_original.get(item["taskId"])
        excluded = Path(item["source"]).name.startswith("24-")
        transferred.append({"id": item["taskId"], "source": item["source"],
            "transferRef": f"architecture/operations/device-requirements-20261018.json#entries/{item['taskId']}",
            "originalSourceSha256": item["originalSourceSha256"], "transferredParagraphsSha256": digest(old.encode()),
            "currentCanonicalSectionSha256": digest(text.encode()), "caseTokens": cases(old + "\n" + text),
            "implementationOwner": native_row["implementationOwner"] if native_row else item["taskId"],
            "testingOwner": native_row["testingOwner"] if native_row else "QRD-1.2",
            "originalQualificationOwner": item["owner"],
            "profiles": [native_row["profile"]] if native_row else ["web", "ios", "android", "macos", "windows", "linux", "terminal", "shared"],
            "disposition": "optional-encrypted-profile-outside-readiness" if excluded else "in-scope-virtual-owner-assigned",
            "physicalOnlyDisposition": "physical-only observations remain separately unexecuted; no physical-device prerequisite",
            "unresolvedCriteriaRef": item["source"] + "#task-" + item["taskId"].lower(),
            "unresolvedCaseTokens": cases(old + "\n" + text),
            "state": "unproven; historical deferred label does not establish a missing implementation",
            "catalogReferences": sorted(set(re.findall(r"(?:tests|specs)/[A-Za-z0-9_./-]+\.md", old + text)))})
    proofs = {p["id"]: p for p in ledger["proofs"]}
    web = []
    for row in ledger["features"]:
        refs = []
        for pid in sorted({p["id"] for p in row["proofs"]}):
            p = proofs[pid]
            for kind in ["receipts", "sourceManifests"]:
                for receipt in p.get(kind, []):
                    path = ROOT / "core" / receipt["path"]
                    state = "absent-historical-reference"
                    if path.is_file():
                        state = "present-hash-matched" if digest(path.read_bytes()) == receipt["sha256"] else "present-hash-mismatch"
                    refs.append({"proof": pid, "kind": kind, **receipt, "availability": state})
        apis = []
        for api in row["apis"]:
            path = ROOT / "core" / api["path"]
            apis.append({**api, "exists": path.is_file(), "sourceRef": ref(path) if path.is_file() else None})
        testing = "QWB-1.1"
        if row["id"] in ["WEB-TOUCH", "WEB-ASSISTANCE", "WEB-MOBILE-EXTENSIONS"]:
            testing = "QWB-1.6"
        elif row["id"] in ["WEB-ROUTES", "WEB-LOCAL", "WEB-READONLY", "WEB-COLLABORATION"]:
            testing = "QWB-1.5"
        elif row["id"] in ["WEB-MARKDOWN", "WEB-CONVERSION", "WEB-AI-OPTIONAL", "WEB-RICH-TRANSFER", "WEB-TABLES", "WEB-INLINE-MEDIA", "WEB-REFERENCES", "WEB-SEARCH-CODE", "WEB-MATH-REORDER"]:
            testing = "QWB-1.7"
        web.append({"id": row["id"], "requirement": row["requirement"], "apis": apis,
            "implementationOwner": "WFE-3.1", "testingOwner": testing,
            "featureCases": row["proofs"], "evidence": refs, "historicalProgressRef": str(web_progress_path) + "#checked-item-evidence",
            "proofState": "recorded feature completion; authenticate surviving receipts/source pins before aggregate reuse",
            "unresolvedTargetClaims": "full suites, target OS input/accessibility and performance retain original owners"})
    returns = [{"id": name, "originalOwner": owner, "implementationOwner": by_original.get(owner, {}).get("featureTask") or owner,
                "testingOwner": testing, **commit_evidence(commit)} for name, commit, owner, testing in RETURNS]
    suites = []
    for profile, impl, test, path in [
        ("web", "WFE-3.1", "QWB-1.1", "core/packages/web"),
        ("ios", "RIO-1.1", "QIO-1.1", "core/native/ios"),
        ("android", "RAN-1.1", "QAN-1.1", "core/native/android"),
        ("macos", "RMC-1.1", "QMC-1.1", "core/native/macos"),
        ("windows", "RWI-1.1", "QWI-1.1", "core/native/windows"),
        ("linux", "RLN-1.1", "QLN-1.1", "core/native/linux"),
        ("terminal", "TUI-1.1", "QTS-1.1", "cli"),
        ("shared", "FND-1.1", "QSH-1.1", "core/crates")]:
        required = sorted({r["testingOwner"] for r in native if r["profile"] == profile})
        if profile == "web":
            required = [f"QWB-1.{n}" for n in range(1, 8)]
        elif profile == "shared":
            required = ["QSH-1.1", "QSH-1.2"]
        suites.append({"profile": profile, "implementationOwner": impl, "testingOwner": test,
                       "requiredTestingOwners": required,
                       "implementationRoot": path, "exists": (ROOT / path).is_dir(),
                       "missingImplementation": None if (ROOT / path).is_dir() else {"owner": impl, "unblock": "create the original native SDK bootstrap/dispatcher; authenticate on required OS runtime"},
                       "fullSuiteState": "required-unproven; no application tests run by inventory",
                       "runtimePrerequisiteOwner": test if CONFIG.successor else "RRD-1.2"})
    preservation = preserved_work() if CONFIG.successor else None
    parent = "SFC-1.1" if CONFIG.successor else "RRD-1.1"
    return {"schemaVersion": 1, "parent": parent, "profile": manifest["profile"],
            "sourceContractSha256": manifest["entries"][0]["sha256"],
            "prerequisites": {parent: {"state": "source-inventory-verified", "nextOwner": "SFC-1.2" if CONFIG.successor else "RRD-1.2",
                "coverage": "137 transfers; 166 native/terminal owners; 17 D24P deliveries; 19 web features; 4 portable returns; 8 suite families",
                "runtimeQualification": "not performed; no implementation or runtime acceptance inferred from inventory"}},
            "excludedClaims": manifest["excludedClaims"], "terminalFullSuiteRequired": True,
            "repositories": {repo: {"branch": git(repo, "branch", "--show-current"), "head": git(repo, "rev-parse", "HEAD")}
                             for repo in ["architecture", "core", "cli", "docs"]},
            "suites": suites, "nativeAndTerminal": native, "deliveries": deliveries,
            "portableReturns": returns, "web": web, "transferred": transferred,
            "referencedDocuments": [{"source": r["source"], "originalOwner": r["owner"],
                "caseTokens": cases("\n".join(r["originalDeviceParagraphs"])),
                "transferRef": "architecture/operations/device-requirements-20261018.json#referencedDocuments/" + r["source"],
                "state": "original predicates retained by transfer owner; virtual coverage QRD-1.2, physical observations separate"}
                for r in transfer["referencedDocuments"]],
            "aggregateOwners": mapping["aggregateOwners"], "performanceOwners": mapping["performanceOwners"],
            "missingFeatureEntries": [{"profile": s["profile"], "path": s["implementationRoot"],
                "owner": s["implementationOwner"], "disposition": s["missingImplementation"]}
                for s in suites if not s["exists"]],
            "unverifiedFeaturePredicates": [{"original": r["original"], "owner": r["implementationOwner"],
                "criterion": r["currentAcceptance"], "disposition": "predicate needs owner authentication; absence of prior generated evidence is not missing code"}
                for r in native if not r["reusedDeliveries"]],
            "staleStateDispositions": [
                {"source": "core/examples/task-editor/FEATURES.md", "state": "pending prose superseded by named WFE-3.1/3.2 checked evidence; do not redo feature work",
                 "evidence": str(web_progress_path), "bothParentsChecked": all(re.search(r"^- \[x\] " + re.escape(task) + r"(?=\s|$)", web_progress, re.M) for task in ["WFE-3.1", "WFE-3.2"])},
                {"source": "older native progress", "state": "blocked labels predate retained D24P and portable returns; authenticate original predicates independently"}],
            "preservedWork": preservation,
            "sourcePins": dict(sorted(PINS.items()))}


def validate(matrix):
    checks = []

    def require(condition, label):
        checks.append(label)
        if not condition:
            raise ValueError(label)

    for name, count, key in [("transferred", 137, "id"), ("deliveries", 17, "id"),
                             ("nativeAndTerminal", 166, "original"), ("web", 19, "id"), ("portableReturns", 4, "id")]:
        rows = matrix[name]
        require(len(rows) == count and len({r[key] for r in rows}) == count, name + " exact unique coverage")
        for row in rows:
            require(bool(row["implementationOwner"] and row["testingOwner"]), name + "/" + row[key] + " owners")
    for row in matrix["transferred"]:
        require(row["caseTokens"] == row["unresolvedCaseTokens"] and bool(row["disposition"]), row["id"] + " retained case references/disposition")
    require({r["profile"] for r in matrix["suites"]} == {"web", "ios", "android", "macos", "windows", "linux", "terminal", "shared"}, "complete profiles")
    require(all(r["exists"] or r["missingImplementation"] for r in matrix["suites"]), "implementation roots or explicit missing-owner disposition")
    require(matrix["terminalFullSuiteRequired"], "terminal full suite retained")
    require(matrix["staleStateDispositions"][0]["bothParentsChecked"], "web closure recorded in named progress")
    for path, sha in matrix["sourcePins"].items():
        require(digest((ROOT / path).read_bytes()) == sha, "source pin " + path)
    require(git("architecture", "check-ignore", str(STORAGE)) == str(STORAGE), "ignored physical matrix storage")
    return {"executed": len(checks), "passed": len(checks), "failed": 0, "skipped": 0,
            "applicationTestsExecuted": 0, "providerRequests": 0,
            "rows": {k: len(matrix[k]) for k in ["transferred", "deliveries", "nativeAndTerminal", "web", "portableReturns", "suites"]},
            "sourcePins": len(matrix["sourcePins"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    arguments(parser)
    args = parser.parse_args()
    configure(args.manifest, args.runtime_root)
    matrix = build()
    result = validate(matrix)
    if args.check:
        if json.loads(OUTPUT.read_text()) != matrix:
            raise ValueError("Inventory differs from current inputs; reconcile before reuse")
    else:
        STORAGE.parent.mkdir(parents=True, exist_ok=True)
        if OUTPUT.is_symlink() and OUTPUT.resolve() != STORAGE:
            raise ValueError("Refuse to replace an inventory link owned elsewhere")
        if OUTPUT.exists() and not OUTPUT.is_symlink():
            raise ValueError("Refuse to replace an existing regular inventory; preserve/reconcile it first")
        STORAGE.write_text(json.dumps(matrix, indent=2) + "\n")
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        if not OUTPUT.is_symlink():
            CONFIG.link(OUTPUT, STORAGE)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

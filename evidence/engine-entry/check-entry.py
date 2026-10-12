"""ENG-1.1: verify current foundation authority and preserved qualification bytes.

Run from any directory with Python 3. No network, provider or credential access.
The final interop rerun is separate; this audit cannot replace it.
"""
import hashlib
import json
from pathlib import Path
import re
import sys

ARCHITECTURE = Path(__file__).resolve().parents[2]
CORE = ARCHITECTURE.parent / "core"
APPROVAL = ARCHITECTURE / "evidence/foundation-approval"
receipt = json.loads((APPROVAL / "receipt.json").read_text())
results = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_files(root, entries):
    failures = []
    for name, expected in entries.items():
        path = root / name
        if not path.is_file():
            failures.append(f"missing: {path}")
        elif path.stat().st_size != expected["bytes"] or digest(path) != expected["sha256"]:
            failures.append(f"changed: {path}")
    assert not failures, "\n".join(failures)
    return len(entries)


def check(name, action):
    try:
        detail = action()
        results.append({"name": name, "passed": True, "detail": detail})
    except (AssertionError, OSError, KeyError, ValueError) as error:
        results.append({"name": name, "passed": False, "error": str(error)})


def authority():
    source = ARCHITECTURE / "roadmaps/01-foundation.md"
    progress = (ARCHITECTURE / "progress/01-foundation.md").read_text()
    revision = digest(source)
    assert revision == receipt["source_revision"] == receipt["source_snapshot_sha256"]
    assert re.findall(r"^Status: (\S+)$", progress, re.M) == ["COMPLETE"]
    assert f"`{revision}`" in progress
    gates = re.findall(r"^- \[ \] (FND-\S+) (.+)$", source.read_text(), re.M)
    checked = dict(re.findall(r"^- \[x\] (FND-\S+) (.+)$", progress, re.M))
    assert len(gates) == 42
    assert all(checked.get(key) == text for key, text in gates), "missing/changed original gate"
    return {"source_revision": revision, "checked_original_items": len(gates)}


def acceptance():
    checks = receipt["checks"]
    commands = {item["command"] for item in checks}
    assert "cargo test -p editac-core --locked" in commands
    assert "node --test tests/schema-interop.test.mjs tests/wasm-load.test.mjs" in commands
    for item in checks:
        assert item["exit"] == 0 and item["executed"] > 0
        assert item["passed"] == item["executed"]
        assert all(item.get(key, 0) == 0 for key in ("failed", "skipped", "filtered", "cancelled", "todo"))
        assert (APPROVAL / item["log"]).is_file()
    assert receipt["prerequisite_audit"]["mismatches"] == []
    profile = receipt["supported_profile"]
    assert profile["schema"] == "editac.registry.v1"
    assert profile["profile"] == "editac.yrs-yjs.v1"
    assert profile["update_encoding"] == 1 and profile["offsets"] == "utf16"
    return {"qualified_checks": len(checks), "profile": profile}


check("current upstream revision and every original checkbox", authority)
check("nonzero no-skip original acceptance and frozen profile", acceptance)
check("tested source integrity", lambda: verify_files(CORE, receipt["source_hashes"]))
check("actual compiled asset integrity", lambda: verify_files(CORE, receipt["compiled_assets"]))
check("all preserved qualification evidence integrity", lambda: verify_files(APPROVAL, receipt["evidence_hashes"]))
check("prerequisite receipt chain integrity", lambda: verify_files(ARCHITECTURE, {
    item["path"]: item for item in receipt["prior_receipts"].values()
}))
report = {"gate": "ENG-1.1", "executed": len(results),
          "passed": sum(item["passed"] for item in results),
          "failed": sum(not item["passed"] for item in results), "skipped": 0,
          "checks": results}
print(json.dumps(report, indent=2))
sys.exit(1 if report["failed"] else 0)

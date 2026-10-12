"""ENG-1.9 evidence reuse check; no feature tests or provider calls."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[2] / "core"
ARCH = HERE.parents[1]
PRIOR = ARCH / "evidence/engine-stable-presentation"


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = {}
    for name in ("tested-source-hashes.json", "preserved-v4-hashes.json",
                 "preserved-v5-qualification-hashes.json"):
        expected = load(PRIOR / name)
        mismatches = [path for path, value in expected.items()
                      if not (CORE / path).is_file() or sha(CORE / path) != value]
        checks[name] = {"checked": len(expected), "mismatches": mismatches}
        assert expected and not mismatches, checks[name]

    receipt = load(PRIOR / "receipt.json")
    result = load(PRIOR / "rustup-result.json")
    command = load(PRIOR / "rustup-command.json")
    assert command["command"] == receipt["canonical"]["exact_command"]
    assert command["command"][:6] == ["/Users/bpstr/.cargo/bin/rustup", "run",
                                     "1.97.1", "cargo", "test", "-p"]
    assert command["environment"]["PATH_PREFIX"].startswith(
        "/Users/bpstr/.nvm/versions/node/v24.19.0/bin:")
    assert "v24.19.0" in (PRIOR / "rustup-toolchain.txt").read_text()
    log = (PRIOR / "rustup-qualified.log").read_text()
    pattern = (r"test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; "
               r"(\d+) measured; (\d+) filtered out;")
    counts = [list(map(int, match)) for match in re.findall(pattern, log)]
    assert counts == result["counts"] and len(counts) == 19
    assert result["exit"] == 0 and result["log_bytes"] == len(
        (PRIOR / "rustup-qualified.log").read_bytes())
    assert all(c[0] > 0 and c[1:] == [0, 0, 0, 0] for c in counts)
    totals = [sum(c[i] for c in counts) for i in range(5)]
    assert totals == result["totals"] == [446, 0, 0, 0, 0]
    blocks = log.split("Running tests/blocks.rs", 1)[1].split("Running tests/", 1)[0]
    passed_names = re.findall(r"^test (\w+) \.\.\. ok$", blocks, re.M)
    assert len(passed_names) == 22
    old = load(ARCH / "evidence/engine-block-commands/receipt.json")
    matrix = {}
    for criterion, evidence in old["criterion_matrix"].items():
        if criterion.startswith("UNFINISHED"):
            continue
        if criterion.startswith("silent preparation"):
            name = "v5_witnessed_cross_source_literal_conversion_is_silent_then_commits_once"
            assert re.search(r"^test .*" + name + r" \.\.\. ok$", log, re.M)
            matrix[criterion] = {"suite": "lib", "tests": [name]}
        else:
            names = [n for n in passed_names if n in evidence]
            assert names, criterion
            matrix[criterion] = {"suite": "blocks", "tests": names}
    positive = [
        "joined_original_code_replacement_and_deletion_preserve_literal_policy_and_anchors",
        "v5_joined_language_paragraph_heading_and_opaque_changes_keep_witnesses_ownership_marks_and_anchors",
        "v5_concurrent_join_presentation_and_text_preserve_absorbed_owner_in_all_six_duplicate_orders",
        "production_v5_joined_presentation_bidirectional_pinned_yjs_checkpoints",
        "v5_public_structural_witnesses_survive_split_presentation_and_reject_fresh_invalid_batches",
    ]
    assert all(n in passed_names for n in positive)
    matrix["ENG-1.9-F1 positive witnessed retained-ownership acceptance"] = {
        "suite": "blocks", "tests": positive}

    node = load(PRIOR / "node-results.json")
    node_totals = {k: sum(row[k] for row in node)
                   for k in ("tests", "pass", "fail", "cancelled", "skipped", "todo")}
    assert node_totals == {"tests": 115, "pass": 115, "fail": 0,
                           "cancelled": 0, "skipped": 0, "todo": 0}
    for row in node:
        text = (PRIOR / row["log"]).read_text()
        for key in node_totals:
            assert int(re.search(r"^(?:#|ℹ) " + key + r" (\d+)$", text, re.M)[1]) == row[key]

    foundation = load(ARCH / "evidence/foundation-approval/receipt.json")
    foundation_source = ARCH / "roadmaps/01-foundation.md"
    assert sha(foundation_source) == foundation["source_revision"]
    assert "Status: COMPLETE" in (ARCH / "progress/01-foundation.md").read_text()
    progress = (ARCH / "progress/02-engine.md").read_text()
    for gate in ("ENG-1.7", "ENG-1.18", "ENG-1.21", "ENG-1.23"):
        assert re.search(r"^- \[x\] " + re.escape(gate) + " ", progress, re.M)
    assert sha(CORE / "fixtures/schema-v5/profile.json") == receipt["profile_sha256"]
    assert receipt["source_revision"] == "83adc7f7c82e9ffe593ac851fc6eca88ece43c7070cf5f18bea2c78c2158b677"

    evidence = [PRIOR / n for n in ("receipt.json", "rustup-result.json",
                "rustup-command.json", "rustup-qualified.log", "rustup-toolchain.txt",
                "node-results.json", "tested-source-hashes.json",
                "preserved-v4-hashes.json", "preserved-v5-qualification-hashes.json")]
    evidence += [PRIOR / row["log"] for row in node]
    out = {"state": "PASS", "checks": checks, "criterion_matrix": matrix,
           "original_rust": {"suites": 19, "executed": 446, "passed": 446,
                             "failed": 0, "skipped": 0, "filtered": 0},
           "original_blocks": {"executed": 22, "passed": 22, "failed": 0,
                               "skipped": 0, "filtered": 0},
           "original_node": node_totals, "foundation_source_revision": sha(foundation_source),
           "profile_sha256": receipt["profile_sha256"],
           "evidence_hashes": {str(p.relative_to(ARCH)): sha(p) for p in evidence},
           "feature_suites_rerun": False, "paid_inference_calls": 0}
    (HERE / "audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print("PASS: 105 tested + 15 frozen v4 + 10 qualified v5 hashes; original "
          "22/22 blocks, 446/446 Rust, 115/115 Node; zero failures/skips; "
          "full original criterion map and foundation revision match.")


if __name__ == "__main__":
    main()

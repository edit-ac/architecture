import copy
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).parents[1] / "scripts/validate-execution-queue.py"
SPEC = importlib.util.spec_from_file_location("execution_queue", MODULE)
QUEUE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(QUEUE)


class ExecutionQueueTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.plan = {"queue": [], "tasks": {}}
        for tid in ["SDK-1.1", "UI-1.1", "TEST-1.1"]:
            source = self.root / (tid + ".md")
            source.write_text(f"# Deliver\n\nStatus: IN_PROGRESS\n\n### Task {tid} — Deliver\n\n- [ ] {tid} Deliver.\n\nDependencies: none.\nAcceptance: Real behavior passes.\n")
            progress = str(source.with_suffix(".progress.md"))
            self.plan["queue"].append({"source": str(source), "progress": progress})
            self.plan["tasks"][tid] = {"source": str(source), "progress": progress,
                                      "phase": "verification" if tid.startswith("TEST") else "functional",
                                      "requires": []}
        self.plan["tasks"]["UI-1.1"]["requires"] = ["SDK-1.1"]
        self.plan["tasks"]["TEST-1.1"]["requires"] = ["UI-1.1"]
        for tid, dependency in [("UI-1.1", "SDK-1.1"), ("TEST-1.1", "UI-1.1")]:
            path = Path(self.plan["tasks"][tid]["source"])
            path.write_text(path.read_text() + f"\nEntry receipts: {dependency}.\n")

    def fails_with(self, message):
        self.assertTrue(any(message in e for e in QUEUE.validate(self.plan)), QUEUE.validate(self.plan))

    def test_closed_ordered_queue_passes(self):
        self.assertEqual([], QUEUE.validate(self.plan))

    def test_original_unqueued_backend_receipt_cannot_pass(self):
        self.plan["tasks"]["UI-1.1"]["requires"].append("BWF-1.1")
        self.fails_with("Unqueued prerequisite: UI-1.1 -> BWF-1.1")

    def test_prerequisite_cannot_be_hidden_only_in_controller_map(self):
        path = Path(self.plan["tasks"]["UI-1.1"]["source"])
        path.write_text(path.read_text().replace("Entry receipts: SDK-1.1.", "Entry receipts: none."))
        self.fails_with("Prerequisite hidden from worker task contract")

    def test_later_prerequisite_cannot_pass(self):
        self.plan["queue"][:2] = self.plan["queue"][1::-1]
        self.fails_with("Prerequisite scheduled after consumer")

    def test_cycle_cannot_pass(self):
        self.plan["tasks"]["SDK-1.1"]["requires"] = ["UI-1.1"]
        self.fails_with("Dependency cycle")

    def test_unmapped_explicit_receipt_cannot_pass(self):
        path = Path(self.plan["tasks"]["UI-1.1"]["source"])
        path.write_text(path.read_text() + "\nEntry receipts: BNA-1.2.\n")
        self.fails_with("Source prerequisite missing from dependency map")

    def test_runtime_planned_header_cannot_pass(self):
        path = Path(self.plan["queue"][0]["source"])
        path.write_text(path.read_text().replace("IN_PROGRESS", "PLANNED"))
        self.fails_with("Invalid runtime header")

    def test_progress_alias_cannot_pass(self):
        self.plan["queue"][0]["progress"] = self.plan["queue"][1]["source"]
        self.fails_with("progress file aliases")

    def test_dropped_original_task_cannot_pass(self):
        self.plan["originalTaskIds"] = ["SDK-1.1", "UI-1.1", "OLD-1.1"]
        self.fails_with("original task was dropped")

    def test_final_testing_before_functionality_cannot_pass(self):
        self.plan["queue"] = [self.plan["queue"][2], *self.plan["queue"][:2]]
        self.fails_with("Verification is scheduled before")

    def test_receipt_path_mismatch_cannot_pass(self):
        self.plan["tasks"]["UI-1.1"]["progress"] = "some-other-authority.md"
        self.fails_with("wrong progress file")

    def test_requirements_pin_allows_verified_checkbox_and_status_updates(self):
        entry = self.plan["queue"][0]
        path = Path(entry["source"])
        entry["requirementsHash"] = QUEUE.requirements_hash(path.read_text())
        path.write_text(path.read_text().replace("- [ ]", "- [x]").replace("IN_PROGRESS", "COMPLETE"))
        self.assertEqual([], QUEUE.validate(self.plan))

    def test_changed_acceptance_requires_controller_reconciliation(self):
        entry = self.plan["queue"][0]
        path = Path(entry["source"])
        entry["requirementsHash"] = QUEUE.requirements_hash(path.read_text())
        path.write_text(path.read_text().replace("Real behavior passes", "Compilation alone passes"))
        self.fails_with("Requirements changed without controller reconciliation")

    def test_wrong_ui_pair_order_cannot_pass(self):
        self.plan["originalUiPairs"] = copy.deepcopy(self.plan["queue"][:2][::-1])
        self.fails_with("Original UI source/progress pairs or relative order changed")

    def test_ui_order_amendment_must_be_explicit(self):
        self.plan["originalUiPairs"] = copy.deepcopy(self.plan["queue"][:2][::-1])
        self.plan["preserveUiOrder"] = False
        self.fails_with("UI reordering requires a controller amendment")

    def accepted_fixture(self):
        source = self.root / "accepted.md"
        source.write_text("# Prior\n\nStatus: COMPLETE\n\n- [x] PRIOR-1.1 Done.\n")
        progress = self.root / "accepted.progress.md"
        progress.write_text("Prepared proof: 1 passed, 0 failed.\n")
        self.plan["acceptedInputs"] = [{"source": str(source), "progress": str(progress),
                                      "taskIds": ["PRIOR-1.1"],
                                      "requirementsHash": QUEUE.requirements_hash(source.read_text()),
                                      "progressSha256": hashlib.sha256(progress.read_bytes()).hexdigest()}]
        return source, progress

    def test_reopened_accepted_gate_cannot_pass(self):
        source, _ = self.accepted_fixture()
        source.write_text(source.read_text().replace("[x]", "[ ]"))
        self.fails_with("Accepted prerequisite is unchecked")

    def test_changed_accepted_evidence_requires_reconciliation(self):
        _, progress = self.accepted_fixture()
        progress.write_text("Required check now failed.\n")
        self.fails_with("Accepted prerequisite evidence changed")


if __name__ == "__main__":
    unittest.main()

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "guarded_continuation", Path(__file__).parents[1] / "scripts/continue-guarded-roadmap.py")
continuation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(continuation)


class GuardedContinuationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        source = self.root / "gate.md"
        source.write_text("# Gate\n\nStatus: COMPLETE\n\n- [x] FIX-1.1 Deliver\n- [x] FIX-1.1-V1 Check\n")
        progress = self.root / "progress.md"
        progress.write_text("Status: COMPLETE\n")
        self.gate = {"source": str(source), "progress": str(progress),
                     "requirementsHash": continuation.requirements_hash(source.read_text())}
        self.status = {"id": "fixture-run", "workspace": str(self.root),
                       "processState": "exited", "roadmapState": "complete", "exitCode": 0,
                       "queue": [{"roadmap": str(source), "progressFile": str(progress),
                                  "state": "complete"}]}

    def test_accepts_completed_exact_fifo_with_current_acceptance(self):
        continuation.validate_boundary(self.status, [self.gate], [])

    def test_checkbox_updates_are_permitted_but_open_checks_block(self):
        source = Path(self.gate["source"])
        source.write_text(source.read_text().replace("[x] FIX-1.1-V1", "[ ] FIX-1.1-V1"))
        self.assertEqual(continuation.requirements_hash(source.read_text()),
                         self.gate["requirementsHash"])
        with self.assertRaisesRegex(ValueError, "acceptance remains open"):
            continuation.validate_boundary(self.status, [self.gate], [])

    def test_changed_acceptance_or_progress_pair_blocks(self):
        source = Path(self.gate["source"])
        source.write_text(source.read_text().replace("Deliver", "Different acceptance"))
        with self.assertRaisesRegex(ValueError, "Requirements changed"):
            continuation.validate_boundary(self.status, [self.gate], [])
        self.status["queue"][0]["progressFile"] = str(self.root / "other.md")
        with self.assertRaisesRegex(ValueError, "FIFO"):
            continuation.validate_boundary(self.status, [self.gate], [])

    def test_stopped_prerequisite_does_not_launch_a_successor(self):
        self.status.update(processState="stopped", roadmapState="stopped", exitCode=75)
        plan = {"workspace": str(self.root), "cli": "fixture-cli", "afterRun": "fixture-run",
                "receipt": str(self.root / "continuation.json"), "gates": [self.gate],
                "successors": []}
        fake = subprocess.CompletedProcess([], 0, json.dumps(self.status), "")
        with patch.object(continuation.subprocess, "run", return_value=fake) as run:
            with self.assertRaisesRegex(ValueError, "did not exit complete"):
                continuation.continue_once(plan)
        self.assertEqual(run.call_count, 1)
        self.assertIn("status", run.call_args.args[0])

    def test_complete_boundary_launches_once_with_explicit_recovery(self):
        successor = self.root / "successor.md"
        successor.write_text("# Next\n\nStatus: IN_PROGRESS\n\n- [ ] FIX-2.1 Deliver\n")
        entry = {"source": str(successor), "progress": str(self.root / "next.progress.md"),
                 "requirementsHash": continuation.requirements_hash(successor.read_text())}
        pending = self.root / "pending.json"
        pending.write_text("[]\n")
        plan = {"workspace": str(self.root), "cli": "fixture-cli", "afterRun": "fixture-run",
                "receipt": str(self.root / "continuation.json"), "gates": [self.gate],
                "successors": [entry], "pendingQueueSpec": str(pending),
                "launchResult": str(self.root / "launch.json"), "idempotencyKey": "fixture-once"}
        launch = {"id": "fixture-successor", "loopGuard": {"state": "armed", "pid": 123}}
        results = [subprocess.CompletedProcess([], 0, json.dumps(self.status), ""),
                   subprocess.CompletedProcess([], 0, json.dumps(launch), "")]
        with patch.object(continuation.subprocess, "run", side_effect=results) as run:
            continuation.continue_once(plan)
            self.assertIn("--recover-blocked", run.call_args.args[0])
            self.assertEqual(json.loads(Path(plan["receipt"]).read_text())["runId"],
                             "fixture-successor")
            continuation.continue_once(plan)
            self.assertEqual(run.call_count, 2)


if __name__ == "__main__":
    unittest.main()

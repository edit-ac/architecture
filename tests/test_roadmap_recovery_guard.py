"""Deterministic safety checks; never launch or stop a real runner."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("guard", Path(__file__).resolve().parents[1] / "scripts/guard-roadmap-recovery.py")
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)


class GuardTests(unittest.TestCase):
    def test_stops_only_completed_owned_blocked_worker(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            progress = workspace / "progress.md"
            progress.write_text("# Progress\n\nStatus: BLOCKED\n\n## Handoff\nMissing shared API")
            event = {"runId": "owned", "type": "runner.turn_finished", "role": "worker", "progressFile": str(progress)}
            self.assertEqual(GUARD.blocked_worker(event, "owned", workspace), progress.resolve())
            for patch in [{"runId": "other"}, {"role": "supervisor"}, {"type": "runner.turn_starting"}, {"interrupted": True}]:
                self.assertIsNone(GUARD.blocked_worker(event | patch, "owned", workspace))

    def test_active_progress_and_historical_blocked_text_do_not_stop(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            progress = workspace / "progress.md"
            progress.write_text("Status: IN_PROGRESS\n## History\nStatus: BLOCKED")
            event = {"runId": "owned", "type": "runner.turn_finished", "role": "worker", "progressFile": str(progress)}
            self.assertIsNone(GUARD.blocked_worker(event, "owned", workspace))

    def test_foreign_workspace_progress_never_stops_owned_runner(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            progress = workspace / "foreign.md"
            progress.write_text("Status: BLOCKED")
            event = {"runId": "owned", "type": "runner.turn_finished", "role": "worker", "progressFile": str(progress)}
            self.assertIsNone(GUARD.blocked_worker(event, "owned", workspace / "owned"))


if __name__ == "__main__":
    unittest.main()

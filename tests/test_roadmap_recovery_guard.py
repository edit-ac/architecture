"""Deterministic safety checks; never launch or stop a real runner."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("guard", Path(__file__).resolve().parents[1] / "scripts/guard-roadmap-recovery.py")
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)


class GuardTests(unittest.TestCase):
    def test_completed_source_prose_churn_stops_on_second_successful_worker(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            source, progress = workspace / "source.md", workspace / "progress.md"
            source.write_text("Status: COMPLETE\n- [x] SFC-1.1 preserved\n")
            progress.write_text("Status: IN_PROGRESS\nReconcile new hash")
            event = dict(runId="owned", type="runner.turn_finished", role="worker", code=0,
                         roadmap=str(source), progressFile=str(progress))
            guard = GUARD.CompletedSourceGuard()
            self.assertIsNone(guard.inspect(event, "owned", workspace))
            source.write_text(source.read_text() + "Current delivery: new source hash\n")
            for patch in [dict(runId="other"), dict(role="supervisor"), dict(code=1),
                          dict(interrupted=True), dict(timedOut=True)]:
                self.assertIsNone(guard.inspect(event | patch, "owned", workspace))
            self.assertEqual(guard.inspect(event, "owned", workspace), progress)

    def test_open_or_changed_checklist_does_not_count_as_completed_source_loop(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            source, progress = workspace / "source.md", workspace / "progress.md"
            source.write_text("- [ ] SFC-1.1 active\n")
            progress.write_text("Status: IN_PROGRESS\n")
            event = dict(runId="owned", type="runner.turn_finished", role="worker", code=0,
                         roadmap=str(source), progressFile=str(progress))
            guard = GUARD.CompletedSourceGuard()
            for _ in range(3):
                self.assertIsNone(guard.inspect(event, "owned", workspace))
            source.write_text("- [x] SFC-1.1 done\n")
            self.assertIsNone(guard.inspect(event, "owned", workspace))
            source.write_text(source.read_text() + "- [x] SFC-1.2 new acceptance\n")
            self.assertIsNone(guard.inspect(event, "owned", workspace))
            source.write_text("")
            self.assertIsNone(guard.inspect(event, "owned", workspace))

    def test_foreign_completed_source_never_stops_owned_runner(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            source, progress = workspace / "source.md", workspace / "progress.md"
            source.write_text("- [x] done\n")
            progress.write_text("Status: IN_PROGRESS\n")
            event = dict(runId="owned", type="runner.turn_finished", role="worker", code=0,
                         roadmap=str(source), progressFile=str(progress))
            guard = GUARD.CompletedSourceGuard()
            for _ in range(2):
                self.assertIsNone(guard.inspect(event, "owned", workspace / "other"))

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

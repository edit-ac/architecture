"""Deterministic safety checks; never launch or stop a real runner."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("guard", Path(__file__).resolve().parents[1] / "scripts/guard-roadmap-recovery.py")
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)
LAUNCH_SPEC = importlib.util.spec_from_file_location("launcher", Path(__file__).resolve().parents[1] / "scripts/guarded-roadmap-runner.py")
LAUNCHER = importlib.util.module_from_spec(LAUNCH_SPEC)
LAUNCH_SPEC.loader.exec_module(LAUNCHER)


class GuardTests(unittest.TestCase):
    def test_read_only_source_uses_current_progress_completion(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            source, progress = workspace / "source.md", workspace / "progress.md"
            source.write_text("- [ ] ES-1.1 original acceptance\n")
            progress.write_text("Status: IN_PROGRESS\n## History\nStatus: COMPLETE\n")
            event = dict(runId="owned", type="runner.turn_finished", role="worker", code=0,
                         roadmap=str(source), progressFile=str(progress), iteration=1)
            guard = GUARD.CompletedSourceGuard()
            self.assertIsNone(guard.inspect(event, "owned", workspace))
            self.assertIsNone(guard.inspect(event | dict(iteration=2), "owned", workspace))
            progress.write_text("# Progress\n\nStatus: COMPLETE\n\n## Evidence\nPassed\n")
            completed = event | dict(iteration=3)
            self.assertIsNone(guard.inspect(completed, "owned", workspace))
            self.assertIsNone(guard.inspect(completed, "owned", workspace))
            self.assertEqual(guard.inspect(event | dict(iteration=4), "owned", workspace), progress)
            source.write_text("- [ ] ES-1.1 revised acceptance\n")
            self.assertIsNone(guard.inspect(event | dict(iteration=5), "owned", workspace))

    def test_real_acceptance_amendment_and_duplicate_event_are_not_loops(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            source, progress = workspace / "source.md", workspace / "progress.md"
            source.write_text("- [x] done\nAcceptance: original contract\n")
            progress.write_text("Status: IN_PROGRESS\n")
            event = dict(runId="owned", type="runner.turn_finished", role="worker", code=0,
                         roadmap=str(source), progressFile=str(progress), iteration=1)
            guard = GUARD.CompletedSourceGuard()
            self.assertIsNone(guard.inspect(event, "owned", workspace))
            self.assertIsNone(guard.inspect(event, "owned", workspace))
            source.write_text("- [x] done\nAcceptance: revised contract\n")
            self.assertIsNone(guard.inspect(event | dict(iteration=2), "owned", workspace))
            other = workspace / "next.md"
            other.write_text(source.read_text())
            self.assertIsNone(guard.inspect(event | dict(roadmap=str(other)), "owned", workspace))

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


class ResolverRecoveryTests(unittest.TestCase):
    def test_one_resolver_per_failure_with_duplicate_event_deduplication(self):
        guard = GUARD.ResolverRecoveryGuard()
        event = dict(roadmap="source", task="A", iteration=1, sessionId="one", failureFingerprint="original")
        self.assertTrue(guard.permit(event, 10))
        self.assertTrue(guard.permit(event | dict(type="runner.turn_finished"), 20))
        self.assertFalse(guard.permit(event | dict(iteration=2, sessionId="two"), 30))
        self.assertTrue(guard.permit(event | dict(iteration=3, sessionId="three", failureFingerprint="changed-input"), 40))

    def test_missing_resolver_times_out_and_actual_resolver_clears_deadline(self):
        guard = GUARD.ResolverRecoveryGuard()
        event = dict(roadmap="source", task="A", iteration=1, sessionId="one")
        guard.permit(event, 10)
        self.assertFalse(guard.expired(69))
        self.assertTrue(guard.expired(70))
        guard.observe(dict(type="runner.turn_starting", role="resolver"))
        self.assertFalse(guard.expired(100))


class GuardProcessTests(unittest.TestCase):
    """Exercise the real event watcher against a local fake management CLI."""

    def exercise(self, lines, expected_state, stopped, max_hours="0.01", last_iteration=None, allow_resolver=False, blocked_progress=False):
        with tempfile.TemporaryDirectory(prefix="editac-loop-test-") as directory:
            workspace = Path(directory).resolve()
            source, progress = workspace / "source.md", workspace / "progress.md"
            source.write_text("Status: COMPLETE\n- [x] SFC-1.1 done\nCurrent delivery: previous source hash\n")
            progress.write_text("Status: IN_PROGRESS\nReconcile the new hash\n")
            if blocked_progress:
                progress.write_text("Status: BLOCKED\nExact source-bound prerequisite\n")
            next_source = workspace / "next.md"
            next_source.write_text("Status: IN_PROGRESS\n- [ ] DRA-1.2 implementation\n")
            events, receipt, calls = workspace / "events.jsonl", workspace / "guard.json", workspace / "calls.json"
            events.write_text("")
            cli = workspace / "fake-runner"
            cli.write_text("#!" + sys.executable + "\nimport json,sys\nfrom pathlib import Path\n"
                           + f"Path({str(calls)!r}).write_text(json.dumps(sys.argv[1:]))\n"
                           + "print(json.dumps({'processState':'stopped'}))\n")
            cli.chmod(0o700)
            command = [sys.executable, str(Path(GUARD.__file__)), "--run-id", "owned",
                       "--workspace", str(workspace), "--events", str(events), "--receipt", str(receipt),
                       "--cli", str(cli), "--poll-seconds", "0.01", "--max-hours", max_hours]
            if allow_resolver:
                command.append("--allow-resolver-recovery")
            with (workspace / "guard.log").open("w") as log:
                process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
                try:
                    deadline = time.monotonic() + 3
                    while not receipt.exists() and process.poll() is None and time.monotonic() < deadline:
                        time.sleep(0.01)
                    self.assertTrue(receipt.exists(), "guard did not become ready")
                    base = dict(runId="owned", type="runner.turn_finished", role="worker", code=0,
                                roadmap=str(source), progressFile=str(progress))
                    with events.open("a") as stream:
                        for line in lines:
                            if isinstance(line, dict) and line.get("roadmap") == "NEXT":
                                line = line | dict(roadmap=str(next_source))
                            stream.write((line if isinstance(line, str) else json.dumps(base | line)) + "\n")
                    process.wait(timeout=4)
                    self.assertEqual(json.loads(receipt.read_text())["state"], expected_state)
                    if last_iteration is not None:
                        self.assertEqual(json.loads(receipt.read_text())["lastObservedIteration"], last_iteration)
                    self.assertEqual(calls.exists(), stopped)
                    if stopped:
                        self.assertEqual(json.loads(calls.read_text()),
                                         ["stop", "owned", "--workspace", str(workspace), "--json"])
                finally:
                    if process.poll() is None:
                        process.terminate()
                        process.wait(timeout=3)

    def test_repairable_result_handoff_allows_resolver_and_normal_completion(self):
        self.exercise([
            dict(type="runner.task_result_invalid", recovery="resolver", failureFingerprint="shape", task="A", sessionId="one", iteration=1),
            dict(type="runner.turn_starting", role="resolver"),
            dict(type="runner.completed"),
        ], "runner-ended", False, allow_resolver=True)

    def test_valid_blocked_worker_allows_one_resolver(self):
        self.exercise([
            dict(type="runner.task_result", task="A", failureFingerprint="source-bound"),
            dict(task="A", iteration=1, sessionId="one"),
            dict(type="runner.turn_starting", role="resolver"),
            dict(type="runner.completed"),
        ], "runner-ended", False, allow_resolver=True, blocked_progress=True)

    def test_repeated_unchanged_blocked_worker_stops(self):
        self.exercise([
            dict(type="runner.task_result", task="A", failureFingerprint="source-bound"),
            dict(task="A", iteration=1, sessionId="one"),
            dict(type="runner.turn_starting", role="resolver"),
            dict(task="A", iteration=2, sessionId="two"),
        ], "stopped-on-blocked-worker", True, allow_resolver=True, blocked_progress=True)

    def test_repeated_identical_repairable_result_still_stops(self):
        self.exercise([
            dict(type="runner.task_result_invalid", recovery="resolver", failureFingerprint="shape", task="A", sessionId="one", iteration=1),
            dict(type="runner.turn_starting", role="resolver"),
            dict(type="runner.task_result_invalid", recovery="resolver", failureFingerprint="shape", task="A", sessionId="two", iteration=2),
        ], "stopped-on-invalid-task-result", True, allow_resolver=True)

    def test_unsafe_result_still_stops_with_recovery_enabled(self):
        self.exercise([dict(type="runner.task_result_invalid", recovery="stop")], "stopped-on-invalid-task-result", True, allow_resolver=True)

    def test_completed_source_loop_invokes_exact_stop(self):
        self.exercise([dict(iteration=41), dict(iteration=42)], "stopped-on-repeated-completed-source", True)

    def test_invalid_event_fails_closed(self):
        self.exercise(["{invalid json"], "stopped-on-guard-error", True)

    def test_invalid_task_result_stops_before_legacy_handoff_redispatch(self):
        self.exercise([dict(type="runner.task_result_invalid", task="BFT-1.2",
                            reasonCode="legacy_handoff_retained", iteration=41)],
                      "stopped-on-invalid-task-result", True)

    def test_foreign_invalid_task_result_does_not_stop_owned_runner(self):
        self.exercise([dict(type="runner.task_result_invalid", runId="other"),
                       dict(type="runner.completed")], "runner-ended", False)

    def test_guard_expiry_fails_closed(self):
        self.exercise([], "stopped-on-guard-expired", True, max_hours="0")

    def test_foreign_events_and_normal_completion_do_not_stop_runner(self):
        self.exercise([dict(runId="other", iteration=41), dict(runId="other", iteration=42),
                       dict(type="runner.completed")], "runner-ended", False)

    def test_guard_survives_roadmap_completion_and_observes_next_source(self):
        self.exercise([dict(iteration=1), dict(type="runner.roadmap_completed"),
                       dict(type="runner.started", roadmap="NEXT"),
                       dict(iteration=9, roadmap="NEXT"), dict(type="runner.completed")],
                      "runner-ended", False, last_iteration=9)


class GuardedLauncherTests(unittest.TestCase):
    def test_guard_uses_managed_stream_instead_of_progress_side_stream(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            managed_events = workspace / "managed-events.jsonl"
            record = dict(id="owned", workspace=str(workspace), progressFile=str(workspace / "progress.md"),
                          artifacts=dict(events=str(managed_events)))

            def ready(command, **kwargs):
                receipt = Path(command[command.index("--receipt") + 1])
                receipt.write_text(json.dumps(dict(pid=12345, state="armed")))
                return SimpleNamespace(pid=12345, poll=lambda: None)

            with patch.object(LAUNCHER.subprocess, "Popen", side_effect=ready) as process:
                self.assertEqual(LAUNCHER.arm_guard("/fake/runner", record)["state"], "armed")
                command = process.call_args.args[0]
                self.assertEqual(command[command.index("--events") + 1], str(managed_events))

    def test_failed_guard_start_stops_runner(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = str(Path(directory).resolve())
            record = dict(id="owned", workspace=workspace, processState="running",
                          progressFile=workspace + "/progress.md")
            with patch.object(LAUNCHER.subprocess, "run", return_value=SimpleNamespace(
                    returncode=0, stdout=json.dumps(record), stderr="")) as runner, \
                    patch.object(LAUNCHER, "arm_guard", side_effect=RuntimeError("failed to arm")):
                with self.assertRaisesRegex(RuntimeError, "failed to arm"):
                    LAUNCHER.run("/fake/runner", "start", ["source.md", "--workspace", workspace])
                self.assertEqual(runner.call_args_list[-1].args[0],
                                 ["/fake/runner", "stop", "owned", "--workspace", workspace, "--json"])

    def test_guarded_start_preserves_fifo_and_attach_never_starts_worker(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = str(Path(directory).resolve())
            record = dict(id="owned", workspace=workspace, processState="running",
                          progressFile=workspace + "/progress.md")
            for mode, args in [("start", ["source.md", "--queue", "next.md", "--workspace", workspace]),
                               ("attach", ["owned", "--workspace", workspace])]:
                with patch.object(LAUNCHER.subprocess, "run", return_value=SimpleNamespace(
                        returncode=0, stdout=json.dumps(record), stderr="")) as runner, \
                        patch.object(LAUNCHER, "arm_guard", return_value={"state": "armed"}):
                    result = LAUNCHER.run("/fake/runner", mode, args)
                    self.assertEqual(result["loopGuard"]["state"], "armed")
                    self.assertEqual(runner.call_args.args[0],
                                     ["/fake/runner", "start" if mode == "start" else "status", *args, "--json"])


    def test_resolver_mode_is_explicit_and_propagated_without_queue_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = str(Path(directory).resolve())
            record = dict(id="owned", workspace=workspace, processState="running", progressFile=workspace + "/progress.md")
            arguments = ["source.md", "--queue", "next.md", "--workspace", workspace]
            with patch.object(LAUNCHER.subprocess, "run", return_value=SimpleNamespace(returncode=0, stdout=json.dumps(record), stderr="")), \
                    patch.object(LAUNCHER, "arm_guard", return_value={"state": "armed"}) as guard:
                result = LAUNCHER.run("/fake/runner", "start", arguments, True)
                guard.assert_called_once_with("/fake/runner", result, True)

    def test_resolver_guard_rejects_a_nonresolving_controller(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory).resolve()
            record = dict(id="owned", workspace=str(workspace), progressFile=str(workspace / "progress.md"),
                          artifacts=dict(events=str(workspace / "events.jsonl")), options=dict(blockedPolicy="stop"))
            with self.assertRaisesRegex(ValueError, "requires --blocked-policy resolve"):
                LAUNCHER.arm_guard("/fake/runner", record, True)


if __name__ == "__main__":
    unittest.main()

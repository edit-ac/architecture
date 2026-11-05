# Unblock the small-core extension delivery

Status: ADOPTED

Compiler amendment, 2026-10-28: the current FIFO has ten entries, including
[WEX source02d](../wasm-extensions-20261027/02d-rust-build-size.md) before source03.
It preserves WEX-3.1/3.2 IDs in that new source and keeps WEX-3.3 in the original
source/progress pair, adding only WEX-9.1/9.2. The manifest preserves the previous
nine-source pins and records new source ownership/hashes and the runtime-enqueue
outcome. Older counts and continuation details below are historical. No original
correctness blocker or exhausted tuning authority is changed by this queue update.

Current queue amendment, 2026-10-28: the user's package-size and Deep Review
request inserts WEX sources 02a, 02b and 02c after original source 02 and before
source 03. The current [queue-spec.json](queue-spec.json) has nine entries and
matches the root-main/WEX queues; the [WEX amendment](../wasm-extensions-20261027/README.md#package-sizing-and-deep-review-amendment--2026-10-28)
owns the seven added parents, acceptance, skill availability and unchanged
optimization allowance. Original six-source recovery details below are historical
adoption records. The last inspected run is stopped; preserve its source02
blocker and re-pin the amended remaining FIFO before any guarded continuation.
Do not replay the old ignored continuation plan with obsolete requirement hashes.

User authority: “Unblock and resume”, 2026-10-28. Preserve the seven accepted
WEX parents, original source/progress pairs, all failure evidence and unrelated
source/index contents. Current [manifest](manifest.json) maps the six sources in
[queue-spec.json](queue-spec.json). The original WEX plan still owns its 20 parents;
six focused prerequisite parents add real Code work rather than weakening its gate.

| Order | Source | Progress from workspace root |
| --- | --- | --- |
| 1 | 01-code-prerequisites.md: original RCH-1.1–1.5 implementation/qualification | .roadmap-runner/wasm-extensions-recovery-20261028/01-code-prerequisites.progress.md |
| 2 | 02-code-facade-admission.md: WCU-1.1 production facade integration | .roadmap-runner/wasm-extensions-recovery-20261028/02-code-facade-admission.progress.md |
| 3 | Original WEX 02 optional extensions: four remaining parents | .roadmap-runner/wasm-extensions-20261027/02-optional-extensions.progress.md |
| 4 | Original WEX 03 production compression | .roadmap-runner/wasm-extensions-20261027/03-production-compression.progress.md |
| 5 | Original WEX 03a small-editor comparisons | .roadmap-runner/wasm-extensions-20261027/03a-small-editor-performance.progress.md |
| 6 | Original WEX 04 final qualification | .roadmap-runner/wasm-extensions-20261027/04-final-qualification.progress.md |

Current RCH receipts and Code facade admission are genuine entry conditions for
WEX-2.2, not whole-track/native release gates. Existing compatible implementations
and proof are reused; no source-only status or fixture override grants production
qualification. WEX-2.3 implements the adopted managed-preload/synchronous comparison
contract; no further unchanged architecture-gate redispatch is authorized.

Installed Roadmap Runner 0.12.4 forwards --recover-blocked only to the first source.
Run sources 1–2 through the guarded launcher, then use the finite deterministic
architecture/scripts/continue-guarded-roadmap.py with the pinned ignored
continuation-plan.json to start sources 3–6 through that launcher with explicit
recovery. It requires the exact predecessor FIFO to exit complete, every selected
acceptance and progress to be COMPLETE, and unchanged requirement hashes. Any
failure stops the handoff, preserving old state; no model-driven retries, progress
reset or second active runner. Resolve live IDs from the continuation receipt and
.roadmap-runner/wasm-extensions-20261028-recovery/active-handoff.json.

Functional work precedes final testing. WEX-4.1 remains the final lifecycle owner;
reuse compatible original focused qualification evidence without duplicate suites.
Keep the existing one shared 45-minute/two-hypothesis optimization allowance,
512-KiB total/32-KiB JS default caps and 1-MiB expanded total canonical gzip cap.
Native/backend/QPF stops, one current format, mocked-only services and no
credentials/paid inference/push/publication/deployment remain in force.

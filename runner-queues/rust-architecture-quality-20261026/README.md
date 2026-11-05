# Editor Rust architecture and quality roadmap

Status: PLANNED

User sequencing amendment, 2026-10-27: the planned [small core and optional Wasm
extensions follow-up](../wasm-extensions-20261027/README.md) begins after all four
sources here, including final RAQ verification, are complete. It reuses these
dependency/bridge repairs, delivers extension architecture before production
compression, and does not change this roadmap's requirements or any live queue.

Close the dependency, diagnostic, code-structure and build-feedback gaps in the
[Rust review](../../research/rust-architecture-quality-20261026.md). This plan has
13 functional parents and four final verification parents. It supplements the
existing ENG/NAT/FIT/ECO owners and does not add another canonical product track.
All tasks are new, unchecked requirements; review probes do not complete delivery.

## Ordered worker sources

| Order | Source | Parents | Outcome | Separate progress path from workspace root |
| --- | --- | ---: | --- | --- |
| 1 | [01-dependency-boundaries.md](01-dependency-boundaries.md) | 5 | Consistent Yrs source, optional source editing, shared authority and bridge libraries | `.roadmap-runner/rust-architecture-quality-20261026/01-dependency-boundaries.progress.md` |
| 2 | [02-code-quality.md](02-code-quality.md) | 5 | Safe error diagnostics, bounded error payloads, private planner modules and selective lints | `.roadmap-runner/rust-architecture-quality-20261026/02-code-quality.progress.md` |
| 3 | [03-build-feedback.md](03-build-feedback.md) | 3 | Unique test ownership, reusable fixture support and measured build tuning | `.roadmap-runner/rust-architecture-quality-20261026/03-build-feedback.progress.md` |
| 4 | [04-final-verification.md](04-final-verification.md) | 4 | Remaining dependency, recovery, semantic and build regression coverage | `.roadmap-runner/rust-architecture-quality-20261026/04-final-verification.progress.md` |

The [manifest](manifest.json) is a planning index, not runtime configuration. This
README and the whole research report are controller context; workers read only
their active file, its selected finding and named source/spec sections. Each task
includes its own affected paths, acceptance, bounded checks and handoff. Local
dependency IDs mean validated parents in the same file. Earlier-file prerequisites
are explicit entry receipts, not implicit whole-roadmap gates.

## Execution and ownership

Creating this roadmap does not start, append, resume or change a runner. Adoption
belongs to the existing controller at a safe checkpoint. When separately
authorized, use `architecture/scripts/guarded-roadmap-runner.py`, live readiness,
the shared coordination ledger and existing main-branch/lane policy. Do not start
a second root runner or edit a checkout with another active worker. Respect
periodic editor-to-main delivery and integration locking when implementation is
eventually adopted. No running source, progress file or queue was changed here.

Preserve the current document format, data, semantic rules, wire/ABI contracts and
opaque prepared plans. Update the relevant authoritative spec and acceptance
together before any unavoidable shared contract change. Keep no compatibility
implementation or automatic migration. Existing feature work remains independently
deliverable; this plan is not a new prerequisite for unrelated product features.

Select one ready parent per session, normally 15–45 minutes including focused
checks. Workers change only verified source checkboxes and Status; receipts,
hashes, source pins, commands, counts and handoffs go in separate progress. Failed,
blocked or skipped parents stay unchecked. Record task/input/error fingerprints,
repair attempted, owner and exact changed-input resume condition. Do not retry an
unchanged failure. Later independent tasks inside a source remain eligible; a
blocked FIFO source does not automatically dispatch later files.

Keep automated checks deterministic and offline where specified. No paid inference,
`.secrets`, provider recording or live dogfood. An AI-named module in a compile
graph does not authorize provider execution. No OS/device qualification,
publication, deployment or dependency-version upgrade is introduced.

Functional parents use existing targeted checks; permanent test development and
broader remaining coverage belong only to source 04. A minimal regression assertion
may accompany a concrete defect fix where needed. Reuse passing evidence with
matching inputs; a source boundary is not a reason to rerun it. Use ignored,
task-owned output and isolated Cargo targets; no clean of shared caches. Retain
only diagnostics for active failures, stop owned processes and remove inactive
session build artifacts. Readiness caps and source-only Git remain in force.

## Finding ownership

| Finding | Delivery owner(s) | Final verification owner |
| --- | --- | --- |
| F01 Required Yrs fork and standalone locks | RAQ-1.1 | RAQ-4.1 |
| F02 Source-editing dependency leakage | RAQ-1.2, RAQ-1.3 | RAQ-4.1 |
| F03 Native dependency on reference host | RAQ-1.4 | RAQ-4.1 |
| A01 Cross-crate bridge source inclusion | RAQ-1.5 | RAQ-4.3 |
| Q01 Diagnostic content exposure and missing causes | RAQ-2.1 | RAQ-4.2 |
| Q02 Large recovery errors | RAQ-2.2 | RAQ-4.2 |
| Q03 Planner module structure | RAQ-2.3, RAQ-2.4 | RAQ-4.3 |
| Q04 Selective lint/ownership policy | RAQ-2.5 | RAQ-4.4 |
| F04 Duplicate test and fixture compilation | RAQ-3.1, RAQ-3.2 | RAQ-4.4 |
| P01 Measured compile feedback | RAQ-3.3 | RAQ-4.4 |

## Completion and deferrals

Each functional source closes on its own focused evidence. Overall completion
requires all 17 parents, including final source 04, with no skipped acceptance.
RAQ-3.3 can conclude that a hypothesis should be deferred, with evidence and an
existing final-fitness owner; it cannot claim a speedup or relaxed hard cap.
Optional profile tuning is limited to one 45-minute batch or two materially
different measured hypotheses, whichever comes first, before independent feature
work. Broad runtime optimization, FFI packaging redesign and OS qualification
require separately scoped evidence and remain outside this plan.

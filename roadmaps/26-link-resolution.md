# Resolve public metadata and private links safely

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [the owning contract](../specs/link-resolution.md), [verification](../specs/verification.md) and the active task context. Paths are relative to `core` unless prefixed with `../architecture/`. Planned implementation/test files are created by their task. Source is controller-owned; write checkmarks, state and evidence only in the separate progress file.

Upstream entry gates: `12-client-contracts.md`, `21-extension-library.md` complete at current source revisions with passing artifact evidence. Dependencies below name only parents in this file. Do not launch implementation while an upstream gate is unavailable.

Reuse qualified roadmap07/21 implementations and shared client ownership. This track delivers portable/backend contracts and browser implementations; full native/TUI wiring belongs to roadmaps31–36 and is not a prerequisite. Any use of another future feature is through the owning typed contract and prepared fixtures until downstream integration.

## Execution rules

Each iteration implements at most one parent, including all its substeps. Target 15–45 minutes plus focused validation. Locate actual symbols before editing and reuse their owning implementation. If the boundary is larger, record the remaining acceptance and a precise controller split. Keep unmet prerequisites unchecked.

Create named checks before invoking them; missing tests and zero-case filters are failures. Capture full logs locally, then record exact commands/results, nonzero executed/passed/failed/skipped counts, fixture/artifact hashes and source/implementation revisions. Use prepared network/auth/media responses and deterministic local fixtures. No model/provider calls, real credentials, private-site probes, production writes, background runner startup or publication are authorized. Follow process/disk teardown in the verification contract.

## Epic LNK-1 — Resolve public metadata and private links safely


### Task LNK-1.1 — Freeze resolver ports and enrichment policies

- [ ] LNK-1.1 Implement and validate freeze resolver ports and enrichment policies.

Purpose: Reuse shared resolution while separating public metadata from private authority.
Context: `crates/editac-session/src/links/mod.rs`; `crates/editac-session/tests/link_contract.rs`; `tests/link-contract.test.mjs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Rust/browser fixtures agree on typed outcomes and authority ownership; core transactions perform no network work and native/TUI consumer records are defined without requiring those implementations.

Implementation:

- [ ] LNK-1.1-I1 Define bounded request/result/action records, host principal/capability context, disabled/local-paste/refresh policies and cancellation/freshness; map existing reference/catalog interfaces instead of duplicating them.

Validation:

- [ ] LNK-1.1-V1 cargo test -p editac-session --test link_contract --locked; node --test tests/link-contract.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.1` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.1`.
Blocked behavior: Leave `LNK-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.2 — Normalize and admit public URL requests

- [ ] LNK-1.2 Implement and validate normalize and admit public url requests.

Purpose: Reject unsafe locators before any transport action.
Context: `crates/editac-session/src/links/public_url.rs`; `crates/editac-session/tests/public_url.rs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Malformed/credential-bearing/unsupported/overlong/forbidden forms produce typed denial with zero outbound calls; valid URLs retain intentional path/query semantics and no URL grants document access.

Implementation:

- [ ] LNK-1.2-I1 Use a standards-based parser for configured HTTP(S), host/port/length and credential rules; normalize deterministic cache keys and redact URL secrets from ordinary diagnostics.

Validation:

- [ ] LNK-1.2-V1 cargo test -p editac-session --test public_url --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.2` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.2`.
Blocked behavior: Leave `LNK-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.3 — Enforce public metadata egress and redirect limits

- [ ] LNK-1.3 Implement and validate enforce public metadata egress and redirect limits.

Purpose: Bind public requests to an explicit SSRF-resistant host transport.
Context: `crates/editac-session/src/links/egress.rs`; `crates/editac-session/tests/link_egress.rs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.2.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Prepared DNS/rebinding/numeric-host/private/metadata-IP/redirect fixtures cannot connect to denied destinations; no cookies or forwarded authorization leak and oversized/slow responses abort within limits.

Implementation:

- [ ] LNK-1.3-I1 Define validated actual-connection address admission, configured allowlists, protected IPv4/IPv6 ranges, time/byte/decompression limits and credentials-free transport; disable redirects by default and validate each enabled hop.

Validation:

- [ ] LNK-1.3-V1 cargo test -p editac-session --test link_egress --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.3` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.3`.
Blocked behavior: Leave `LNK-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.4 — Parse bounded title and icon metadata

- [ ] LNK-1.4 Implement and validate parse bounded title and icon metadata.

Purpose: Convert untrusted responses to safe display records.
Context: `crates/editac-session/src/links/metadata.rs`; `crates/editac-session/tests/link_metadata.rs`; `fixtures/links/html/`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.3.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Malformed/control-character/huge and secondary-URL attack fixtures yield safe bounded metadata or fallback; canonical metadata cannot change document identity and icons cannot bypass egress checks.

Implementation:

- [ ] LNK-1.4-I1 Extract deterministic bounded Open Graph/title/icon fields using inert parsing, normalize display text and validate canonical/icon/image URLs through the same admission port; keep raw embed HTML out of results.

Validation:

- [ ] LNK-1.4-V1 cargo test -p editac-session --test link_metadata --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.4` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.4`.
Blocked behavior: Leave `LNK-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.5 — Bound public metadata scheduling and cache work

- [ ] LNK-1.5 Implement and validate bound public metadata scheduling and cache work.

Purpose: Make lookups finite, cancellable and independent of editing latency.
Context: `crates/editac-session/src/links/public_resolver.rs`; `crates/editac-session/tests/link_public_lifecycle.rs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.4.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Burst/offline/timeout/dispose fixtures stay within queue/response bounds, canceled work produces no mutations and cache reuse respects policy/authority without exposing secret URL details.

Implementation:

- [ ] LNK-1.5-I1 Connect host transport/parser using bounded concurrency, request deduplication, policy-scoped freshness/negative cache and cancellation; expose cache-hit versus network-wait timing.

Validation:

- [ ] LNK-1.5-V1 cargo test -p editac-session --test link_public_lifecycle --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.5` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.5`.
Blocked behavior: Leave `LNK-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.6 — Enrich links on host-approved local paste

- [ ] LNK-1.6 Implement and validate enrich links on host-approved local paste.

Purpose: Deliver automatic title/favicon behavior only for authorized initiating actions.
Context: `packages/web/src/modules/links/enrichment.ts`; `tests/browser/link-enrichment.spec.ts`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.5.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Local paste under enabled policy enriches safely; open/remote/replay/history causes zero calls; late results cannot overwrite edited text or resurrect nodes, and metadata history/readonly behavior is explicit.

Implementation:

- [ ] LNK-1.6-I1 Wire disabled/local-paste/explicit-refresh settings to the existing local command origin; capture node/URL/revision/request identity and separate cached preview from deliberate shared metadata commits.

Validation:

- [ ] LNK-1.6-V1 npm run test:browser -- link-enrichment. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.6` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.6`.
Blocked behavior: Leave `LNK-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.7 — Resolve private catalog targets under current permissions

- [ ] LNK-1.7 Implement and validate resolve private catalog targets under current permissions.

Purpose: Keep private lookup distinct from unrestricted webpage retrieval.
Context: `crates/editac-session/src/links/private_resolver.rs`; `crates/editac-session/tests/private_link_auth.rs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A document reader without target permission receives no private metadata or privilege escalation; wrong tenant/authority/locked endpoint and stale authorization fixtures fail without weakening public egress rules.

Implementation:

- [ ] LNK-1.7-I1 Adapt existing configured catalog/ac authority ports to require host principal capability for target/title/icon/preview/activation; preserve credentials inside host adapters and non-disclosing forbidden/missing outcomes.

Validation:

- [ ] LNK-1.7-V1 cargo test -p editac-session --test private_link_auth --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.7` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.7`.
Blocked behavior: Leave `LNK-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.8 — Isolate private metadata caches and disclosure

- [ ] LNK-1.8 Implement and validate isolate private metadata caches and disclosure.

Purpose: Prevent metadata sharing across principals or collaborative labels.
Context: `crates/editac-session/src/links/private_cache.rs`; `crates/editac-session/tests/private_link_cache.rs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.7.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Two-principal/two-tenant fixtures cannot reuse secret titles/icons; fetched private fields never enter shared CRDT snapshots by default, and revoked display state is hidden under the documented offline lease policy.

Implementation:

- [ ] LNK-1.8-I1 Key private cache by principal/tenant/authority/target and permission policy revision; handle expiry/logout/switch/revoke/lock and explicit host-authorized metadata publication.

Validation:

- [ ] LNK-1.8-V1 cargo test -p editac-session --test private_link_cache --locked. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.8` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.8`.
Blocked behavior: Leave `LNK-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.9 — Render permission-aware internal link states

- [ ] LNK-1.9 Implement and validate render permission-aware internal link states.

Purpose: Give private references honest viewer-specific presentation.
Context: `packages/web/src/modules/references/`; `tests/browser/private-link-display.spec.ts`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.8.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Authorized and unauthorized concurrent viewers see only their permitted metadata; account/permission changes remove stale private display, while shared user-authored text and target identity remain intact.

Implementation:

- [ ] LNK-1.9-I1 Consume the shared private result variants in existing reference presenters with neutral/user-authored fallback, scoped display fields, accessible status and cancellation/disposal.

Validation:

- [ ] LNK-1.9-V1 npm run test:browser -- private-link-display. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.9` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.9`.
Blocked behavior: Leave `LNK-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.10 — Revalidate reference activation and deep links

- [ ] LNK-1.10 Implement and validate revalidate reference activation and deep links.

Purpose: Open the intended authorized target without treating locators as commands.
Context: `packages/web/src/modules/links/activation.ts`; `tests/link-activation.test.mjs`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.6, LNK-1.9.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Stale metadata cannot change the clicked target; forbidden/revoked/read-only/navigation cases are explicit, no shell command interpolation occurs and copied locators contain no credentials.

Implementation:

- [ ] LNK-1.10-I1 Route external/private/deep-link activation through validated host action objects and current capabilities; keep safe copy-locator behavior separate from credentials and document write permission.

Validation:

- [ ] LNK-1.10-V1 npm run build; node --test tests/link-activation.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.10` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.10`.
Blocked behavior: Leave `LNK-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.11 — Export resolver and presenter conformance contracts

- [ ] LNK-1.11 Implement and validate export resolver and presenter conformance contracts.

Purpose: Make native/TUI and host backends consume the same resolver semantics.
Context: `packages/core/`; `packages/web/package.json`; `tests/link-public-exports.test.mjs`; `fixtures/link-presenters/`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.10.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Clean consumers use public imports only, all result states preserve principal/cancellation/readonly semantics, and downstream native/TUI work has concrete typed actions without claiming current platform delivery.

Implementation:

- [ ] LNK-1.11-I1 Publish supported request/result/cache-policy/activation interfaces through existing boundaries and headless per-platform fixtures; specify the host connection-admission obligation and roadmaps31–36 wiring points.

Validation:

- [ ] LNK-1.11-V1 npm run build; node --test tests/link-public-exports.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.11` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.11`.
Blocked behavior: Leave `LNK-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.


### Task LNK-1.12 — Qualify privacy performance and resolver handoff

- [ ] LNK-1.12 Implement and validate qualify privacy performance and resolver handoff.

Purpose: Record complete portable/web safety and latency evidence.
Context: `tests/link-resolution-qualification.test.mjs`; `../architecture/evidence/link-resolution.md`; `../architecture/specs/link-resolution.md`; `../architecture/specs/verification.md`.
Dependencies: LNK-1.11.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Every required policy has nonzero passing fixtures, denied transports make zero calls, secret private fields stay out of shared snapshots/logs, input is never blocked and actual resolver/platform limits are published.

Implementation:

- [ ] LNK-1.12-I1 Aggregate malicious page/icon and permission/cache fixtures, cold/warm local/network timing, concurrency/response caps, no-call origins and disposal; record backend adapter requirements and downstream platform gaps.

Validation:

- [ ] LNK-1.12-V1 node --test tests/link-resolution-qualification.test.mjs. Assert the acceptance cases; record exact command/exit, nonzero selected tests, failures/skips, fixture/revision hashes and relevant performance/artifact evidence.

Evidence: Progress entry `LNK-1.12` links changed paths, source/implementation revisions, commands/results and fixture/artifact hashes. Preserve failures; durable summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failure/missing decision and next bounded action for `LNK-1.12`.
Blocked behavior: Leave `LNK-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the gate without polling.

# WEB-1.4 prerequisite gap

Static diagnosis, 2026-10-12; no implementation or acceptance check executed.
Immutable browser source revision: `895c9f7fdf7d3a10192cead10ed16c8b13d0bd082dd9f35037f0599b381122ff`. Reference file hashes and repository HEADs: `receipt.json`. Uncommitted prior browser/storage implementation is preserved; HEAD alone does not identify those files.

## Governing evidence

- `specs/web.md:141` requires the qualified composition ADR for WEB input implementation and applies G01–G14.
- `specs/editing-regression-suite.md:35` explicitly requires fixing the ADR before WEB-1.4–WEB-1.7 implementation and calls its absence a prerequisite gap. G05 at line 16 requires qualified buffering/finalization/cancel policy before adapter implementation.
- `specs/editor-interactions.md:61` confirms that the ADR is a development output, not assumed evidence.
- The four documents in `decisions/` contain no input/composition ADR. Scoped searches of specs/decisions and current core packages/tests/fixtures find requirements, not qualification evidence. No production `packages/web/src/input/` or `tests/browser/input.spec.ts` exists.
- `roadmaps/42-editing-regression-suite.md:95` assigns ADR/correlation qualification before production routing to RGS-1.4-I1. Its entry gate at line 9 requires track 08 complete; `roadmaps/08-sdk-integration.md:9` requires track 04 complete. The cycle is WEB-1.4 → qualified ADR/RGS-1.4 → track 08 → track 04/WEB-1.4. These live roadmaps are diagnostic references, not authority to perform another parent in this iteration.

## Remaining-gate scan

| Gate | Required predecessor | Current result |
|---|---|---|
| WEB-1.4 | WEB-1.3 plus qualified ADR | WEB-1.3 recorded complete; ADR unavailable |
| WEB-1.5 | WEB-1.4 | Not ready |
| WEB-1.6 | WEB-1.5 | Not ready |
| WEB-1.7 | WEB-1.6 | Not ready |
| WEB-1.8 | WEB-1.7 | Not ready |
| WEB-1.9 | WEB-1.8 | Not ready |
| WEB-1.10 | WEB-1.9 | Not ready |
| WEB-1.11 | WEB-1.10 | Not ready |
| WEB-1.12 | WEB-1.11 | Not ready |

No independent ready parent exists. Implementing routing first or accepting a proposed ADR as qualified would bypass the explicit prerequisite. No production/spec/roadmap changes or provider calls were made; no gate was checked. Earlier checked evidence is preserved, not rerun or freshly qualified.

## Required controller action

Schedule a bounded pre-WEB-1.4 ADR/correlation qualification prerequisite with an executable real-DOM/real-engine probe, resolving the track-42/08 entry cycle. Its output must fix temporary composition ownership, finalization/cancellation, intent identity/terminal disposition and renderer-echo suppression, with observed notification fixtures and nonzero passing qualification evidence. Alternatively supply an existing qualified ADR and its exact evidence if one exists outside the checked paths. Revise the controller-owned source/entry ordering for the next snapshot; retain all original browser criteria. This worker did not authorize a waiver or change sources.

Retry only when that qualification evidence or a controller-revised prerequisite scope arrives. No feature check ran (0 executed/passed/failed/skipped; not a pass). No task-owned browser/server started or stopped. Existing unrelated processes preserved. Data volume free: 28212080640 bytes is recorded exactly in receipt.json; no session build/cache artifacts created or removed.

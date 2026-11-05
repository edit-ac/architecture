# Deliver Drupal canonical document fields

Status: PLANNED

## Goal and entry conditions

Workspace: `core`; paths are core-relative and planned. Deliver an optional Drupal module with a configurable canonical document field type, actual editor widget and safe display formatter. It depends directly on the standalone PHP SDK and existing browser editor; no Laravel, Symfony or Filament installation is required. There is one unversioned current editor format.

Entry: 01a-php-sdk BPH-1.1/1.2/1.9/1.11 provide the plain PHP package, validation/repository/transaction interfaces and actual checkpoint outcomes; 00-contracts BSC-1.7 provides the oracle/selector dispatcher. Existing `packages/web/` supplies accepted canonical create/restore/flush and mount/dispose. BDR-1.3 must expose/reuse immutable SDK snapshot lookup/retention before revisioned fields pass; BDR-1.7 additionally requires a qualified SDK read-only render/export boundary. Missing APIs are named SDK/Rust-owner blockers, not permission to copy codecs or rendering semantics. No later Node framework adapter is a prerequisite. Record targeted earlier selectors/results in ignored progress rather than relying on queue position.

Authority: [Drupal field contract](../../specs/backend-sdk-adapters.md#drupal-document-fields), [canonical durability](../../specs/document-durability.md), [Drupal Field API](https://api.drupal.org/api/drupal/core%21modules%21field%21field.api.php/group/field_types/11.x) and [render cache metadata](https://www.drupal.org/docs/drupal-apis/render-api/cacheability-of-render-arrays). Select one maintained Drupal/PHP baseline during implementation and author its capability declaration; no historical editor/framework matrix is implied.

## Execution and validation rules

Commands below are planned selectors introduced by BSC-1.7, registered by each owner; a missing selector fails. Prefer an existing package/kernel/browser fixture or a minimal prepared data-loss guard. Comprehensive Drupal field/entity/widget/formatter cases have one owner, BNT-1.8; BFT-1.3/1.5 retain shared database and backend authorization coverage, reused rather than rerun wholesale.

Use prepared auth/content and local/mock transports; actual local Drupal/SQLite storage proves scoped entity transactions. No production credentials, paid inference, registry publication, deployment or automatic fixture recording. Canonical bytes/references, configuration and user data are never silently migrated, reseeded or purged. Generated assets, caches, packed modules and test output stay ignored; preserve only active failure diagnostics. Reuse/track and tear down only confirmed task-owned test browsers/listeners/servers.

This source starts/enqueues no runner and changes no active snapshot. Adopt under the existing coordinator/guard/readiness receipt at a safe checkpoint. Workers update only verified checkboxes/Status; source hashes/results/handoff belong in ignored progress. Stop on BLOCKED or unchanged failed input, record a precise changed-input resume condition and continue only independent ready work.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/02b-drupal-fields.progress.md` (architecture-relative, ignored). Record actual runtime/source/selector/exit and meaningful executed/passed/failed/skipped counts, plus delivered interfaces and exact prerequisite gaps.

## Epic BDR-1 — Deliver Drupal canonical document fields

### Task BDR-1.1 — Create the optional Drupal module and SDK services

- [ ] BDR-1.1 Create the optional Drupal module and SDK services.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/composer.json; adapters/cms/drupal/editac.info.yml; adapters/cms/drupal/editac.services.yml; adapters/cms/drupal/config/schema/.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: none (validated plain PHP SDK entry only).
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Composer/module metadata and DI wrap the PHP SDK directly, with explicit validator/repository/connection/configuration and permissions. Drupal and SDK baseline ranges are declared; Laravel/Filament are absent and no external service starts on enable.

Implementation:

- [ ] BDR-1.1-I1 Add authored module metadata, services and configuration schema, mapping Drupal services to SDK interfaces without a second save algorithm. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.1`: Enable the module in a fresh ignored local Drupal site and inspect dependency/configuration graphs for direct SDK use and absence of Laravel/Filament. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.2 — Implement the configurable canonical field type

- [ ] BDR-1.2 Implement the configurable canonical field type.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/src/Plugin/Field/FieldType/; adapters/cms/drupal/src/TypedData/; adapters/cms/drupal/config/schema/.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.1.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: FieldItem/Typed Data properties and storage/settings/constraints retain stable item ID, document/epoch and exact committed snapshot/revision reference. Field cardinality, required/isEmpty and initialized-empty semantics are explicit; field delta is not identity and HTML is not canonical storage.

Implementation:

- [ ] BDR-1.2-I1 Define one current field schema and plugin with bounded values and SDK identity validation; expose normal Field UI settings and default widget/formatter identifiers. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.2`: Create a field through actual Drupal configuration, store one initialized-empty reference and distinguish it from absent data; reorder two items without changing their stable IDs. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.3 — Bind immutable SDK snapshots to entity revisions

- [ ] BDR-1.3 Bind immutable SDK snapshots to entity revisions.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: sdk/php/src/Persistence/; adapters/cms/drupal/src/Repository/; adapters/cms/drupal/src/Revision/.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.2.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Field values pin exact committed immutable SDK snapshots, retrievable after later edits and retained while referenced by any entity revision. Old/reverted revisions never read latest-by-document-ID. Missing snapshot lookup/retention in the SDK is repaired with BPH-1.9 owner; no Drupal-only history/decoder appears.

Implementation:

- [ ] BDR-1.3-I1 Reuse/expose the minimal SDK snapshot read/retain/release port and connect Drupal revision references. Keep immutable past values separate from explicit current working-state writes. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.3`: Save two revisions with different exact snapshot references in real local Drupal; render/read the older snapshot after the newer save and verify original bytes remain unchanged. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.4 — Map translations and moderation to explicit document scope

- [ ] BDR-1.4 Map translations and moderation to explicit document scope.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/src/Revision/; adapters/cms/drupal/src/Translation/; adapters/cms/drupal/src/Entity/.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.3.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Language-specific fields have isolated document scope by default; explicit cloning/sharing policy preserves item identity and original snapshots. Draft/published moderation references stay pinned, and reverting is an authorized explicit write rather than silent reseeding.

Implementation:

- [ ] BDR-1.4-I1 Connect existing entity revision/translation/moderation hooks to SDK scope and snapshot references; declare optional core-module capabilities rather than requiring moderation everywhere. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.4`: Use one prepared two-language entity and draft/published pair; a draft/language edit does not change the other translation or the published revision snapshot. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.5 — Implement the editor widget and AJAX lifecycle

- [ ] BDR-1.5 Implement the editor widget and AJAX lifecycle.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/src/Plugin/Field/FieldWidget/; adapters/cms/drupal/js/; adapters/cms/drupal/editac.libraries.yml.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.3.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: A real browser editor widget uses asset libraries/behaviors with bounded attach/detach and single initialization across AJAX/BigPipe/form rebuilds. Multiple/nested field paths, read-only/required/error/accessibility and extension settings preserve identity/history and pending recovery; no redraw imports full content.

Implementation:

- [ ] BDR-1.5-I1 Wrap the existing browser SDK and Drupal form/asset extension points, with stable item handles and explicit disposal/unsaved state. Avoid a parallel text model or per-keystroke canonical payload resubmission. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.5`: Attach the same actual widget twice through a prepared AJAX rebuild, edit two field items and detach; verify one session per item, no cross-field text and retained unsaved recovery. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.6 — Coordinate entity save, access and SDK commit

- [ ] BDR-1.6 Coordinate entity save, access and SDK commit.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/src/Save/; adapters/cms/drupal/src/Access/; adapters/cms/drupal/src/Form/.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.4, BDR-1.5.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Entity/field/revision/language access and CSRF protect save/preview paths; exact SDK inputs use stable operation identity and configured shared database transaction. Entity rollback/validation/conflict produces no false receipt or published association. Remote storage cannot advertise atomic entity save without explicit staged reconciliation.

Implementation:

- [ ] BDR-1.6-I1 Map Drupal policy, validation and actual connection/transaction callbacks to SDK orchestration; preserve unsaved edits and original references on failure, including AJAX retry. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.6`: Commit one real local entity/document save and force one entity rollback plus denied field request; only the committed operation has a receipt and association. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.7 — Implement the safe revision-pinned field formatter

- [ ] BDR-1.7 Implement the safe revision-pinned field formatter.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/src/Plugin/Field/FieldFormatter/; adapters/cms/drupal/src/Render/.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.4.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Formatter loads the referenced immutable snapshot through the SDK and consumes qualified read-only render/export output with safe Drupal render/text-format policy. Cache tags/contexts/max-age include exact revision, language, settings and access dependencies; unsafe unknown content and later drafts cannot leak. Missing SDK rendering blocks rich capability.

Implementation:

- [ ] BDR-1.7-I1 Wrap the existing qualified SDK renderer and Drupal render/access/cache interfaces. Expose configurable view modes and explicit escaped/plain-text fallback without duplicating document semantics or trusting raw stored HTML. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.7`: Render a prepared older published snapshot under two access/language contexts after a draft edit; inspect exact output/cache metadata and ensure forbidden/unsafe content is absent. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.8 — Connect optional Media and reference cleanup

- [ ] BDR-1.8 Connect optional Media and reference cleanup.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: adapters/cms/drupal/src/Asset/; adapters/cms/drupal/src/Lifecycle/; adapters/cms/drupal/editac.install.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.3, BDR-1.6.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Optional Drupal Media/File selection and usage tracking use existing authorized SDK/blob finalization; upload/selection is not availability. Entity/field/revision deletion releases only its references under retention. No config deletion/uninstall silently purges canonical documents or referenced history; baseline fields need no Media provider.

Implementation:

- [ ] BDR-1.8-I1 Map optional asset access/usage and reference lifecycle callbacks to SDK ports, with explicit unavailable/unsupported outcomes and scoped retention-aware cleanup. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.8`: Use one prepared pending/finalized asset and two retained revision references; deleting one reference cannot delete the shared snapshot/asset or manufacture availability. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDR-1.9 — Deliver the Drupal field example and install guide

- [ ] BDR-1.9 Deliver the Drupal field example and install guide.

Purpose: Deliver this SDK-backed Drupal boundary.
Deliverable: examples/sdk-adapters/drupal/; adapters/cms/drupal/README.md; sdk/contracts/support.json.
Context: Drupal contract above; Deliverable source and named SDK results.
Dependencies: BDR-1.4, BDR-1.6, BDR-1.7, BDR-1.8.
Independent work: Other prerequisite-ready siblings remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Local example installs the module, configures node/custom entity fields, widget and formatter, and demonstrates canonical save/reopen, revisions/translations and explicit supported optional capabilities. Config export contains settings only; no content migration, body-field replacement, public package write or production credentials.

Implementation:

- [ ] BDR-1.9-I1 Provide authored module/example installation metadata, Field UI recipes, default display settings, exact SDK topology and declared baseline/capabilities. Pack generated editor assets only outside Git. Register its focused selector; defer full suites.

Validation:

- [ ] BDR-1.9-V1 Run `node scripts/sdk-adapter-delivery.mjs BDR-1.9`: Follow the documented local node field install/edit/save/reopen and older-revision display flow; validate custom entity configuration and config export, reusing prior accepted fixture results. Budget: at most 5 minutes; reuse unchanged SDK results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Record module/SDK interfaces, selected baseline/capabilities, actual delivery selectors/results and remaining rich-render/history/API gaps in ignored progress. BNT-1.8 owns comprehensive Drupal coverage; existing BFT evidence is reused. Do not claim unsupported remote atomicity, unavailable environments or publication readiness.

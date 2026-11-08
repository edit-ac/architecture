# Notion block editor and edit.ac

- **Status:** Research complete for this bounded comparison; plan additions are unimplemented
- **Owner:** edit.ac architecture
- **Last reviewed:** 2026-11-08
- **Related:** [Interaction contract](../specs/editor-interactions.md), [rich-content contract](../specs/rich-content-extensions.md), [planned acceptance cases](../tests/notion-block-cases.md), [track 38](../roadmaps/38-editor-interactions.md), [track 25](../roadmaps/25-rich-content-extensions.md)

## Question and evidence

The requester selected edit.ac as the target and asked to complete research and update its plans, without implementing missing features. This comparison uses current Rust/Yrs and browser source, retained qualification receipts, official Notion documentation and a disposable signed-in Notion session observed on 2026-11-08. It does not transfer another product's backlog or architecture assumptions into edit.ac.

The inspected local source baseline predates the current upstream delivery. This publication preserves the newer upstream source-only, single-current-format and feature-first/final-roadmap-43 policies; it does not recertify later engine implementations. Each proposed task must first disposition current source and existing receipts. Baseline source revisions: architecture `b0fc8ebb89d3ea67092c43eb6a21a346b45a965e`; core `5b3e96ec259f1cdd8df2971b2192c9cacf225a65`. Codanna remained bound to another workspace, so bounded source reads supplied this project's code evidence. Retained tests below were inspected, not rerun or automatically recertified against current hashes.

REA 6.8.0 supplied public-page and passive native-window evidence. Public rendered-page records retained from the same day's first pass include `ev_b36973f6162a8ef880d5bb4323705b523496db7a9792b31b96e1b37e63ba08bd` and `ev_2f837b91df53407a3afda9f07199759f01619b7c356990a554cdc91e03540861`. They establish published-page rendering at desktop/narrow sizes, not editing. The continuation's native-window record is `ev_666498012c0d9f35a1bf5f7293c3cfdcc34a1e45f451ef44c45277da2815ade5`; it includes companion-window chrome/thumbnail and has Accessibility capture disabled, so it is supplementary pixels rather than an event/DOM trace. Feature interactions below were performed and checked through CUA AX/DOM. Private captures and full receipts stay outside public Git in the workspace's qualification-evidence area.

## Additional observed Notion behavior

| Observation | Result and limit |
| --- | --- |
| Six-dot handle click | **Observed:** clicking the handle opened the selected block's context menu. This closes the earlier observation gap where only the keyboard menu and accessible handle label had been checked. The menu exposed type/conversion, color, link, duplicate, move, delete, comment and suggested-edit actions. |
| Block color | **Observed:** the color submenu separated text from background tokens. Applying Yellow background changed the sample block's rendered background; Default background restored it. This does not establish every inline/color inheritance or export rule. |
| Toggle conversion and children | **Observed:** converting a parent bullet to Toggle list preserved its checked nested item. Closing removed the child from the visible accessibility tree; reopening restored the checked item. Undo of conversion restored the original bullet and child. Fold-state persistence across accounts/devices was not established. |
| Copy block link | **Partially observed:** the action displayed a copied-link success message, but clipboard readback did not yield a URL. Clipboard fidelity, URL shape, move/reload stability and access denial remain unverified. A toast is not a passing copy/navigation test. |
| Retained first-pass interactions | Slash filtering/cancellation, insertion versus conversion, list nesting/outdent/Undo, duplicate/Undo, parent-plus-child selection, subtree drag/Undo, simple-table entry and column conversion were observed earlier in the same day's session. These are single-user interaction observations, not synchronization qualification. |
| Narrow layout | The desktop session kept columns side by side after resizing to 390 pixels. This is not proof of native-phone behavior or a requirement to copy that layout. |

The samples' default background and bullet/checklist structure were restored. No AI action, sharing change, upload or account-permission experiment was performed. The shipped session reported build `23.13.20261108.0710`; conclusions concern that observed session rather than all Notion clients.

## Inspected local baseline and plan disposition

`Implemented` below means source exists, with the stated retained proof where available. `Planned` does not mean shipped or qualified.

| Capability | edit.ac evidence | Disposition / owner |
| --- | --- | --- |
| Headings, basic marks and structural formatting | `core/crates/editac-core/src/document.rs` validates H1–H6; `core/crates/editac-core/src/commands/format.rs` has six inline marks and multi-owner formatting. Retained format receipt (local retained receipt; not a published artifact). | Reuse existing engine; no new heading or basic-formatting task. |
| Stable editing targets | `core/crates/editac-core/src/anchors.rs` resolves document/source-relative Yrs anchors to position/deleted/unresolvable. Retained anchors receipt (local retained receipt; not a published artifact) records 24/24. | Reuse qualified anchors. Public durable URLs are a separate host contract, RCH-1.30. |
| Cross-parent semantic movement | `core/crates/editac-core/src/commands/move.rs` already validates root/list/quote destinations, rejects cycles/stale structural versions and preserves source-relative selection. Retained move receipt (local retained receipt; not a published artifact) records 35/35. | Do not create another move engine. Existing RCH-1.17 owns pointer/non-drag exposure; new range UI consumes that owner. |
| Atomic and multi-owner edits | `core/crates/editac-core/src/commands/editor.rs` prepares bounded batches on an isolated replica and rechecks identity/revision/checkpoint before one live update. This is not a complete block-range selection product. | INT-1.20 defines/fills only missing range primitives; INT-1.21 owns selection/bulk presentation. |
| Handle-opened contextual actions | Existing command/reorder modules and INT-1.18 cover parts of routing; the complete block-targeted handle menu is not established. | New INT-1.19: captured block target, click/drag separation, conversion and shared applicability. |
| Collapsible sections/headings | A formatting `Toggle` operation is not a collapsible structural node. Current kind/presentation allowlists do not admit the new family. | RCH-1.24 semantic/compatibility producer, then RCH-1.25 presenter. |
| Text/highlight/block palette | Six basic marks exist and custom-mark registration is implemented; no qualified first-party authored color/highlight palette was found. Code token decorations are unrelated. | RCH-1.26 through the registry/format owner, with explicit inline/block semantics. |
| Page column layout | No column container is in the admitted structural kinds. Rectangular table columns are different. | RCH-1.27 semantic/format producer, then RCH-1.28 responsive presenter. |
| Heading outline | Existing headings, anchors and patches are useful inputs; a complete generated outline surface is not established. | RCH-1.29, generated navigation rather than a new stored TOC node. |
| Anchored discussions | Anchors do not establish a thread entity, permission model or discussion UI. | RCH-1.31 defines portable host-required annotation targets/presenters. Host storage/auth/audit stay outside the semantic engine. |
| Suggested edits | Revisioned semantic diffs/hunk application are already planned in track 13; AI proposal sessions are separately planned. Neither is current qualified human review support. | RCH-1.32 consumes DIF-1.4/1.5; no separate accepted-body writer or mandatory AI transport. |
| Images, references, callouts and tables | `core/crates/editac-core/src/modules/content.rs` has inert descriptors; module receipt (local retained receipt; not a published artifact) records 54 browser checks. Richer lifecycle/UI remains planned. | Reuse RCH-1.6–1.15 for table, asset and controlled-embed work; no duplicate basic-content track. |
| Synced blocks, database views and authored buttons | References are not transclusion; tables are not host database queries; presenter buttons are not executable document semantics. No matching admitted semantic families were found. | RCH-1.33 records three explicitly deferred capability decisions. Adoption requires separate use-case/contract selection. |

## Plan changes and sequence

The current upstream roadmap graph and final roadmap-43 runtime/device ownership are retained. Thirteen new unchecked parents fill specific gaps:

- **Track 38:** INT-1.19 handle context; INT-1.20 prepared range operations; INT-1.21 multi-block selection/bulk presenter. INT-1.14 remains the final interaction/device/AT consumer.
- **Track 25:** RCH-1.24–1.33 cover toggle semantics/presentation, palette, column semantics/presentation, generated outline, host block links, anchored discussion, human review and the three deferred strategic decisions. Existing RCH-1.15 and RCH-1.17 are refined, and RCH-1.19/1.20 retain portable-contract/final-testing ownership.

Keep existing completed engine/browser/module receipts and source IDs. A new consumer does not reopen a qualified semantic producer or require another full suite. New families must settle their one-current-format/Markdown/ABI/durability obligations before writable admission; these planning additions do not themselves amend the one current document format. No new roadmap, runner, publication, cloud service or code implementation is started.

The [planned 40-case catalog](../tests/notion-block-cases.md) assigns finite producer/final-consumer ownership. It contains future acceptance descriptions, not executable recipes or passing results. Functional delivery uses the smallest meaningful proving case. Existing final owners fill missing executable recipes and cross-feature/device assertions after the functional batch; they reuse compatible passes rather than repeat every earlier check. The optional rich pointer-range branch belongs to RCH-1.20, keeping baseline interaction completion independent of that later profile.

## Official source references and unresolved questions

The documented feature boundary uses [writing and editing](https://www.notion.com/help/writing-and-editing-basics), [keyboard shortcuts](https://www.notion.com/help/keyboard-shortcuts), [columns and tables](https://www.notion.com/help/columns-headings-and-dividers), [synced blocks](https://www.notion.com/help/synced-blocks), [comments](https://www.notion.com/help/comments-mentions-and-reminders), [sharing](https://www.notion.com/help/sharing-and-permissions), [mobile UI](https://www.notion.com/help/workspaces-on-mobile) and the [public Block API](https://developers.notion.com/reference/block). Public API shape is not proof of Notion's internal editor library, collaboration algorithm or storage architecture.

Notion internals, multi-user/permission/offline behavior, native mobile/touch/IME/AT, full clipboard fidelity and the documented bulk-toggle shortcut discrepancy remain unverified. These are explicit evidence limits, not missing edit.ac features by inference. The plan's own device/host/recovery tests must establish edit.ac behavior independently; a competitor capture cannot qualify this SDK.

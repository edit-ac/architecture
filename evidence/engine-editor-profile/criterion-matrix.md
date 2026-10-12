# ENG-1.21 production integration coverage

## Exact v4 creation, restore, admission; no migration/reseeding

- `production_create_uses_exact_ten_roots_and_restored_empty_is_not_reseeded`
- `malformed_immutable_root_source_tuple_and_resource_updates_are_atomic`
- `stale_and_cross_replica_plans_and_profile_epoch_fail_atomically`

## Hierarchical read-only snapshots, container/check/number tuples and unknown recovery

- `production_projection_matches_qualified_hierarchy_metadata_and_read_only_bytes`
- `metadata_only_changes_rebuild_check_number_and_revision_and_stale_all_plans`
- `opaque_immutable_source_and_container_admit_read_only_and_keep_children`
- `entity_controls_keep_immutable_rows_recovery_descendants_and_reactivate`

## Prepared placement/creation and reversible controls preserve subtree/source/mark/anchor identities

- `prepared_nested_place_preserves_subtree_sources_marks_and_anchors`
- `create_container_and_original_atomically_then_place_and_check`
- `disabling_place_operation_replays_retained_intent_and_restores`
- `real_production_three_replica_move_move_edit_six_orders_and_duplicate_restore`
- `v4_whole_batch_preparation_is_silent_commit_is_one_origin_and_only_local_writer`

## Shared text/format and nested split/join, endpoint/empty/repeat/multiple originals

- `nested_split_join_retains_checked_default_unicode_marks_and_original_identity`
- `production_nested_endpoint_empty_and_repeated_split_after_multi_source_join`
- `shared_formatting_crosses_nested_containers_and_empty_block_tuples_are_atomic`

## Code literal insertion/dormant marks and noneditable separators; atomic neighbor reservation

- `explicit_code_split_join_and_literal_newlines_preserve_dormant_marks`
- `separator_is_noneditable_and_last_editable_owner_reserves_adjacent_paragraph`
- `rich_format_mixed_code_and_unknown_targets_reject_without_mark_changes`
- `inaccessible_separator_neighbor_identity_overflow_and_nonempty_creation_are_atomic`

## Complete invalid/mixed/stale/profile/epoch/resource rejection before any live write

- `mixed_invalid_block_metadata_and_nonempty_separator_never_partially_write`
- `cycles_illegal_parents_and_incompatible_joins_reject_before_commit`
- `malformed_immutable_root_source_tuple_and_resource_updates_are_atomic`
- `stale_and_cross_replica_plans_and_profile_epoch_fail_atomically`
- `depth_128_text_is_editable_and_whole_subtree_depth_overflow_rejects_atomically`

## Actual production Rust/Yjs bytes, pinned tools, replay/checkpoint/unknown recovery

- `production_bidirectional_pinned_yjs_exchange_and_remote_unknown_recovery`
- `real_production_three_replica_move_move_edit_six_orders_and_duplicate_restore`

## Legacy contracts, qualification receipts and hierarchy prerequisite preserved

- `regressions-2.log: all 16 nonzero Rust suites; v4 qualification mapper/descriptor unchanged; isolated exchange families; legacy parsers and bounds retained`


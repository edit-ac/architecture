from pathlib import Path
import hashlib,json,re,subprocess
root=Path('/Users/bpstr/Github/edit-ac/core');out=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
changed=['crates/editac-core/src/commands/blocks.rs','crates/editac-core/src/commands/mod.rs','crates/editac-core/src/commands/editor.rs','crates/editac-core/src/commands/text.rs','crates/editac-core/tests/blocks.rs','fixtures/schema-v4/blocks-exchange.mjs','fixtures/schema-v4/blocks-contract-probe.mjs']
reg=json.loads((out/'regressions.json').read_text())
node=[]
for p in out.rglob('*.log'):
 if p.parts[-2]=='exchange':continue
 s=p.read_text(errors='replace');m=re.search(r'(?:ℹ |# )tests (\d+)',s)
 if m:node.append({'log':str(p.relative_to(out)),'executed':int(m[1]),**{k:int(re.search(r'(?:ℹ |# )'+tag+r' (\d+)',s)[1]) for k,tag in [('passed','pass'),('failed','fail'),('skipped','skipped')]},'kind':'diagnostic-only' if p.name=='contract-probe.log' else 'pinned binary interoperability'})
receipt={
 'task':'ENG-1.9','state':'IN_PROGRESS; implementation advanced, original acceptance fails', 'date':'2026-10-11','iteration':5,'prompt_revision':'7eaa063f3629','source_snapshot':'source-f6218bddbd75.md','source_revision':'8569ff462b210eb9478fb409f9cd179506cb1f3efab3247bf3d678257353aa30',
 'source_snapshot_sha256':sha(root.parent/'architecture/progress/.roadmap-runner/02-engine-4d812f5d0e69/source-f6218bddbd75.md'),
 'core_base_revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'architecture_base_revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root.parent/'architecture',text=True).strip(),
 'changed_paths':changed,'source_hashes':{p:sha(root/p) for p in changed},
 'unchanged_contract_hashes':{p:sha(root/p) for p in ['fixtures/schema-v4/mapping.rs','fixtures/schema-v4/mapping.mjs','fixtures/schema-v4/profile.json','fixtures/schema-v4/seed.json']},
 'implementation':'Block commands expand on disposable v4 state. Text preparation reused read-only; edits rebound to stage sources to preserve one local writer. One explicit-origin commit. SetCode/paragraph, literal text/hard break, explicit split/join, nested separator conversion/insertion/deletion, paragraph reservation and typed directional editable anchors. Atomic PresentationConflict guard rejects metadata changes that invalidate retained joins.',
 'criterion_matrix':{
  'literal whitespace/blank lines/dormant marks/unknown labels/empty restore':'code_literal_whitespace_blank_lines_dormant_marks_and_empty_restore; production_blocks_bidirectional_pinned_yjs_exchange_and_restore',
  'language bounds/atomic invalid batches':'code_language_bounds_and_mixed_invalid_batches_are_atomic',
  'split endpoints/empty/matching and incompatible joins':'code_split_endpoints_and_matching_join_preserve_original_sources; incompatible_join_and_rich_format_on_code_reject_without_mutation',
  'hard break insertion without implicit split':'hard_break_in_rich_text_keeps_owner_and_newline_is_not_a_split',
  'separator nested insertion/navigation/paragraph typing/deletion':'separators_insert_both_sides_preserve_nested_identity_and_navigate; separator_conversion_reserves_accessible_empty_paragraph_atomically; deleting_only_separator_prepares_neighbor_and_retains_recovery_identity',
  'nonempty/noneditable separator rejection':'separator_rejects_text_split_join_nonempty_and_wrong_navigation_targets',
  'stale/replica/profile/epoch/anchor/resource no partial writes':'stale_wrong_replica_deleted_anchor_and_resource_rejection_are_atomic; v3_profile_and_wrong_epoch_anchors_do_not_acquire_v4_roots_or_mutate; last_editable_separator_reservation_resource_failure_leaves_live_state_exact',
  'three-writer reorder/duplicate/recovery/original identity':'three_writer_code_metadata_literal_edit_and_separator_races_replay_restore (3 families × 6 schedules, every update duplicated)',
  'silent preparation/single-origin/only local CRDT writer':'lib::commands::editor::transaction_tests::v4_block_text_batch_is_silent_and_commits_once_with_only_local_writer',
  'UNFINISHED joined-owner metadata-only conversion/language updates':'joined_original_code_replacement_and_deletion_preserve_literal_policy_and_anchors FAILS PresentationConflict; guarded safety passes separately; contract-gap.md'},
 'feature':{'command':'PATH=/Users/bpstr/.nvm/versions/node/v24.19.0/bin:$PATH EDITAC_BLOCK_COMMAND_EXCHANGE='+str(out/'exchange-final')+' CARGO_INCREMENTAL=0 cargo test -p editac-core --test blocks --locked','log':'feature-4.log','exit':101,'executed':16,'passed':15,'failed':1,'skipped':0,'filtered':0},
 'regressions':reg,'node_checks':node,
 'final_distinct_rust_counts':{'executed':362,'passed':361,'failed':1,'skipped':0,'filtered':0},
 'final_node_counts':{'functional_executed':sum(x['executed'] for x in node if x['kind']!='diagnostic-only'),'functional_passed':sum(x['passed'] for x in node if x['kind']!='diagnostic-only'),'functional_failed':0,'functional_skipped':0,'diagnostic_executed':2,'diagnostic_passed':2},
 'non_test_checks':{'cargo fmt --all --check':0,'git diff --check':0},
 'preserved_failures':['feature-1.log (compile imports/types)','feature-2.log (compile fixture keys/Arc moves)','feature-3.log (13 pass/2 fail; plain-text Yjs oracle repaired; original joined presentation split observed)','exchange/node-feature-3-failure.log','feature-4.log (15 pass/1 fail; atomic guard prevents silent split)'],
 'prerequisite_evidence':'Existing qualified matrices and passing receipts retained; no prior receipt claimed this newly discovered joined-owner presentation composition. Current regression results do not close ENG-1.9 or resolve its missing positive proof.',
 'controller_handoff':'contract-gap.md: specify and qualify retained-join eligibility under metadata-only presentation before production integration/positive test. No descriptor/replay-schema modification was inferred.',
 'next_ready_parent':'ENG-1.10 (ENG-1.8 named dependency remains verified; no implementation begun this iteration)','paid_inference_calls':0,'secrets_loaded':False,'publication':False,'deployment':False,'hygiene':json.loads((out/'hygiene.json').read_text())}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
manifest={str(p.relative_to(out)):sha(p) for p in out.rglob('*') if p.is_file() and p.name!='artifact-hashes.json'}
(out/'artifact-hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('receipt',receipt['final_distinct_rust_counts'],'Node',receipt['final_node_counts'],'artifacts',len(manifest))

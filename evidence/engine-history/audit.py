"""Collect exact current ENG-1.11 qualification evidence; never run provider calls."""
import datetime, hashlib, json, pathlib, re, subprocess
root=pathlib.Path('/Users/bpstr/Github/edit-ac/core')
out=root.parent/'architecture/evidence/engine-history'
def write(name,value): (out/name).write_text(json.dumps(value,indent=2)+'\n')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert json.loads((out/'regression-result.json').read_text())['exit']==0
s=(out/'regressions.log').read_text()
suites=[]
for name,body in re.findall(r'Running ([^\n]+)\n(.*?)(?=\n\s*Running |\Z)',s,re.S):
 m=re.search(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out;',body)
 assert m,name
 passed,failed,ignored,measured,filtered=map(int,m.groups())
 assert passed>0 and failed==ignored==measured==filtered==0,name
 suites.append({'suite':name.split(' (')[0],'executed':passed+failed,'passed':passed,'failed':failed,'skipped':ignored,'filtered':filtered})
assert len(suites)==20 and sum(x['passed'] for x in suites)==474
feature=[x for x in suites if x['suite']=='tests/history.rs'];assert len(feature)==1 and feature[0]['passed']==28
nodes=[]
for p in sorted((out/'regression-exchange').rglob('*.log')):
 text=p.read_text(errors='replace'); counts={k:int(v) for k,v in re.findall(r'(?:ℹ|#) (tests|pass|fail|cancelled|skipped|todo) (\d+)',text)}
 if counts:
  assert counts['tests']>0 and counts['tests']==counts['pass'] and all(counts.get(x,0)==0 for x in ['fail','skipped','cancelled','todo']),p
  nodes.append({'log':str(p.relative_to(out)),**counts})
assert len(nodes)==15 and sum(x['tests'] for x in nodes)==120
write('rust-results.json',suites);write('node-results.json',nodes)
hashes=json.loads((out/'tested-source-hashes.json').read_text());assert all(digest(root/p)==v for p,v in hashes.items())
frozen={}
for name in ['preserved-v4-hashes.json','preserved-v5-qualification-hashes.json']:
 h=json.loads((root.parent/'architecture/evidence/engine-stable-presentation'/name).read_text());assert all(digest(root/p)==v for p,v in h.items()); frozen[name]={'matched':len(h),'mismatches':0}
write('profile-audit.json',frozen)
feature_source=(root/'crates/editac-core/tests/history.rs').read_text()
passed_names=set(re.findall(r'^test (\w+) \.\.\. ok$',s,re.M))
criteria={
 'local selective origin exclusion':['local_undo_after_remote_insertion_keeps_remote_unicode_and_anchor','remote_replay_restore_and_selection_do_not_enter_history_or_clear_redo','distinct_typing_origins_and_composition_sessions_never_merge'],
 'explicit command boundaries and deterministic typing/composition':['explicit_edits_are_separate_inside_capture_interval_and_clear_redo','deterministic_typing_capture_timeout_origin_and_reset_boundaries','composition_group_is_explicit_and_paste_format_move_break_coalescing','one_mixed_prepared_operation_undoes_text_metadata_and_move_as_one_group'],
 'scoped rich text and metadata history':['deletion_replacement_unicode_undo_restores_original_identity_and_marks','rich_format_command_is_one_group_and_remote_text_survives','text_and_metadata_history_can_repeat_undo_redo_without_losing_deleted_payloads','literal_code_history_keeps_dormant_marks_and_exact_whitespace'],
 'immutable creation/operation rows and original text identity':['initial_creation_rows_text_and_required_metadata_survive_undo_redo','newly_created_text_enters_scope_for_later_typing_but_creation_content_is_retained','structural_move_undo_retains_operation_and_remote_descendant_edits','split_join_history_keeps_multisource_ownership_marks_and_anchors','metadata_history_does_not_rewrite_established_v5_join_witnesses'],
 'permanent tombstones, remote bytes and dependent recovery/anchors':['permanent_remote_tombstone_wins_over_structural_redo_and_keeps_recovery_bytes','dependent_remote_place_is_retained_dormant_and_anchor_reroutes_when_split_undone','container_control_undo_does_not_swallow_live_children','remote_text_and_presentation_on_local_creation_survive_control_undo_redo'],
 'bounded capture, redo policy and nonmutating failures':['group_count_payload_and_commit_caps_evict_old_history_without_content_writes','clear_and_invalid_configuration_are_nonmutating','rejected_and_stale_preparation_preserve_history_state_and_redo','staged_history_resource_rejection_is_atomic_and_retry_requires_changed_remote_state','concurrent_separator_presentation_blocks_incompatible_undo_before_live_mutation'],
 'ordinary update replay, supported profiles and pinned bidirectional interop':['history_updates_converge_under_six_three_writer_duplicate_reorder_schedules','v4_profile_uses_same_selective_controls_without_mutating_frozen_mapping','pinned_bidirectional_yjs_history_exchange_and_remote_text_preservation'],
}
assert all(name in passed_names and 'fn '+name+'(' in feature_source for names in criteria.values() for name in names)
write('criterion-map.json',criteria)
command=['/Users/bpstr/.cargo/bin/rustup','run','1.97.1','cargo','test','-p','editac-core','--test','history','--locked']
feature_log=(out/'history-qualified-rustup.log').read_text();assert '28 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out' in feature_log
write('history-command.json',{'command':command,'cwd':str(root),'environment':{'PATH_PREFIX':'/Users/bpstr/.nvm/versions/node/v24.19.0/bin:/Users/bpstr/.cargo/bin','RUSTC':'/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustc','CARGO_INCREMENTAL':'0','EDITAC_HISTORY_EXCHANGE':str(out/'exchange')},'exit':0})
assert 'Finished `dev` profile' in (out/'wasm-qualified.log').read_text()
write('wasm-command.json',{'command':['rustup','run','1.97.1','cargo','check','-p','editac-core','--target','wasm32-unknown-unknown','--locked'],'environment':{'RUSTC':'/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustc','CARGO_TARGET_DIR':'/tmp/editac-history-wasm-20261011T230118','CARGO_INCREMENTAL':'0'},'exit':0,'kind':'kernel compile only; no WASM binding acceptance claim','failed_attempt':'wasm-check.log; Cargo selected Homebrew rustc without wasm target despite installed rustup target; repaired compiler selection'})
receipt={
 'gate':'ENG-1.11','children':['ENG-1.11-I1','ENG-1.11-V1'],'state':'implemented and locally verified','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_revision':'83adc7f7c82e9ffe593ac851fc6eca88ece43c7070cf5f18bea2c78c2158b677','source_snapshot':'progress/.roadmap-runner/02-engine-4d812f5d0e69/source-f6218bddbd75.md','prompt_revision':'7eaa063f3629',
 'core_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'working_tree_dirty':True,'tested_source_hashes':'tested-source-hashes.json','tested_source_count':len(hashes),
 'changed_paths':['crates/editac-core/src/history.rs','crates/editac-core/src/lib.rs','crates/editac-core/src/document.rs','crates/editac-core/src/commands/text.rs','crates/editac-core/src/commands/format.rs','crates/editac-core/src/commands/structure.rs','crates/editac-core/src/commands/editor.rs','crates/editac-core/tests/history.rs','tests/history-exchange.mjs'],
 'rust':{'feature':28,'regression':446,'executed':474,'passed':474,'failed':0,'skipped':0,'filtered':0,'suites':20,'log':'regressions.log','results':'rust-results.json'},
 'node':{'feature':5,'regression':115,'executed':120,'passed':120,'failed':0,'skipped':0,'cancelled':0,'todo':0,'results':'node-results.json'},
 'coverage':'criterion-map.json','bounded_schedule_coverage':{'writers':3,'arrival_permutations':6,'accepted_deliveries':54,'atomic_incomplete_dependency_rejections':6,'duplicate_undo_redo_replay':True},
 'policy':{'supported_history_profiles':['v4','v5'],'opt_in':'enable_history','legacy_profiles':'explicit UnsupportedProfile; no migration','default_max_groups':100,'default_update_budget_bytes':8388608,'default_max_group_commits':256,'default_typing_timeout_ms':500,'capture_clock':'fixed internal clock; caller-supplied monotonic typing time','selection_only_history':False,'clear_history_mutates_content':False,'cross_restart_stack_restore':False},
 'preserved_failures':['check-1.log','history-1.log','history-2.log','history-3.log','history-4.log','history-5.log','wasm-check.log','failure-notes.json'],
 'frozen_profiles':frozen,'hygiene':'hygiene.json','upstream':'01-foundation COMPLETE revision 38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897; interop/schema_interop remain passing in this integration execution',
 'permissions':{'paid_inference':False,'publication':False,'deployment':False,'source_roadmap_edited':False,'second_parent_processed':False},
}
write('receipt.json',receipt)
artifacts={str(p.relative_to(out)):digest(p) for p in out.rglob('*') if p.is_file() and p.name!='artifacts.json'}
write('artifacts.json',artifacts)
print(json.dumps({'gate':receipt['gate'],'rust':474,'node':120,'source_hashes':len(hashes),'profile_hashes':sum(v['matched'] for v in frozen.values()),'artifacts':len(artifacts)}))

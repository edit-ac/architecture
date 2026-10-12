"""Audit exact counts, fixed criterion coverage and unchanged tested sources."""
import datetime,hashlib,json,pathlib,re,subprocess
root=pathlib.Path('/Users/bpstr/Github/edit-ac/core'); out=root.parent/'architecture/evidence/engine-patches'
def write(n,x): (out/n).write_text(json.dumps(x,indent=2)+'\n')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert json.loads((out/'regression-result.json').read_text())['exit']==0
s=(out/'regressions.log').read_text(); suites=[]
for name,body in re.findall(r'Running ([^\n]+)\n(.*?)(?=\n\s*Running |\Z)',s,re.S):
 m=re.search(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out;',body); assert m,name
 passed,failed,skipped,measured,filtered=map(int,m.groups()); assert passed>0 and failed==skipped==measured==filtered==0,name
 suites.append(dict(suite=name.split(' (')[0],executed=passed+failed,passed=passed,failed=failed,skipped=skipped,filtered=filtered))
assert len(suites)==20 and sum(x['passed'] for x in suites)==474
feature=(out/'patches-4.log').read_text(); assert (out/'patches-4.exit').read_text().strip()=='0'
assert '23 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out' in feature
write('rust-results.json',dict(feature=dict(executed=23,passed=23,failed=0,skipped=0,filtered=0,log='patches-4.log'),regressions=suites,distinct_total=497))
nodes=[]
for p in sorted((out/'exchange').rglob('*.log')):
 text=p.read_text(errors='replace'); counts={k:int(v) for k,v in re.findall(r'(?:ℹ|#) (tests|pass|fail|cancelled|skipped|todo) (\d+)',text)}
 if counts:
  assert counts['tests']>0 and counts['tests']==counts['pass'] and all(counts.get(x,0)==0 for x in ['fail','skipped','cancelled','todo']),p
  nodes.append(dict(log=str(p.relative_to(out)),**counts))
assert len(nodes)==15 and sum(x['tests'] for x in nodes)==120
write('node-results.json',nodes)
hashes=json.loads((out/'tested-source-hashes.json').read_text()); assert all(digest(root/p)==h for p,h in hashes.items())
frozen={}
for name in ['preserved-v4-hashes.json','preserved-v5-qualification-hashes.json']:
 h=json.loads((root.parent/'architecture/evidence/engine-stable-presentation'/name).read_text()); assert all(digest(root/p)==v for p,v in h.items()); frozen[name]=dict(matched=len(h),mismatches=0)
write('profile-audit.json',frozen)
passed_names=set(re.findall(r'^test (\w+) \.\.\. ok$',feature,re.M))
criteria={
 'one versioned changed-node/range selection/update batch per commit':['text_batch_has_exact_version_origin_bytes_node_and_utf16_range','rich_and_block_format_are_single_batches_with_fixed_ranges','block_only_batch_has_changed_node_without_text_range','production_mixed_editor_batch_emits_once_with_all_touched_families','direct_structure_commit_has_one_batch_with_derived_owner_nodes','split_join_batches_preserve_source_identity_and_report_visibility_changes','replay_is_one_remote_batch_and_duplicate_rejected_input_are_silent','undo_redo_emit_one_semantic_batch_and_preserve_remote_edits','structural_history_multitransaction_work_is_one_batch_per_undo_redo'],
 'deferred callbacks after transactions and locks; no reentrant panic':['nested_commit_callbacks_can_read_prepare_commit_and_preserve_delivery_order','each_commit_excludes_older_pending_ranges_without_consuming_snapshot_evidence'],
 'irrelevant listeners excluded':['irrelevant_node_source_selection_listeners_are_silent','new_listener_excludes_batches_already_queued_before_subscription','preparation_applicability_invalid_stale_and_noop_do_not_emit'],
 'observer errors cannot corrupt committed state':['returned_errors_and_unwinding_panics_do_not_corrupt_commit_or_other_observers'],
 'unsubscribe removes callbacks and disposal is idempotent':['disposal_is_idempotent_releases_capture_and_drop_unsubscribes','dispose_during_callback_suppresses_later_listener_in_same_batch','self_disposal_is_safe_and_subscription_after_commit_does_not_receive_old_batch','document_drop_invalidates_outstanding_subscription_and_owned_patch_survives'],
 'selection metadata stable anchors explicit deletion no content history':['selection_events_have_no_content_update_or_history_and_commit_resolves_anchor','deleted_selection_endpoint_is_explicit_and_node_scopes_see_recovery'],
 'replica and legacy command integration':['reordered_duplicate_three_replica_batches_converge_with_fixed_distinct_counts','legacy_profile_text_format_and_structure_commits_also_publish_once'],
}
assert all(set(names)<=passed_names for names in criteria.values()); write('criterion-map.json',criteria)
source=root.parent/'architecture/progress/.roadmap-runner/02-engine-4d812f5d0e69/source-f6218bddbd75.md'; assert digest(source)=='83adc7f7c82e9ffe593ac851fc6eca88ece43c7070cf5f18bea2c78c2158b677'
write('feature-command.json',dict(command=['/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/cargo','test','-p','editac-core','--test','patches','--locked'],cwd=str(root),environment=dict(PATH_PREFIX='/Users/bpstr/.nvm/versions/node/v24.19.0/bin',RUSTC='/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustc',RUSTDOC='/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustdoc'),node='v24.19.0',exit=0,log='patches-4.log'))
write('failure-notes.json',[
 dict(log='patches-1.log',kind='compile failure; zero tests executed',repair='Map projection errors to EditorError and annotate derived diff collections.'),
 dict(log='patches-2.log',kind='test harness compile failure; zero tests executed',repair='Use pinned Yrs Any::from numeric tuples.'),
 dict(log='patches-3.log',executed=23,passed=18,failed=5,skipped=0,repair='Filter listeners by subscription sequence. Four fixed fixtures use UTF-16 offset 3 outside the surrogate pair and current writer-scoped creation ID.'),
])
receipt=dict(gate='ENG-1.12',children=['ENG-1.12-I1','ENG-1.12-V1'],state='implemented and locally verified',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_revision=digest(source),source_snapshot=str(source.relative_to(root.parent/'architecture')),prompt_revision='7eaa063f3629',core_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),working_tree_dirty=True,
 changed_paths=['crates/editac-core/src/patches.rs','crates/editac-core/tests/patches.rs','crates/editac-core/src/lib.rs','crates/editac-core/src/document.rs','crates/editac-core/src/history.rs','crates/editac-core/src/commands/text.rs','crates/editac-core/src/commands/format.rs','crates/editac-core/src/commands/structure.rs','crates/editac-core/src/commands/editor.rs'],
 rust=dict(feature=23,regression=474,distinct_executed=497,passed=497,failed=0,skipped=0,filtered=0,results='rust-results.json'),node=dict(executed=120,passed=120,failed=0,skipped=0,cancelled=0,todo=0,results='node-results.json'),
 coverage='criterion-map.json',tested_source_hashes='tested-source-hashes.json',tested_source_count=len(hashes),frozen_profiles=frozen,
 behavior=dict(patch_version=1,observation_tokens='local sequence and content revision; not CRDT time',selection='local stable anchors plus explicit current resolution; no content history/update',delivery='post-transaction and post-lock, ordered queued reentrant commits, subscription sequence boundary',scopes=['all','nodes','sources','selection','updates'],disposal='idempotent; callback captures released immediately except while executing; drop unsubscribes',errors='returned callback errors and native unwinding panics disable the faulting observer and record bounded diagnostics; committed state and other callbacks survive',panic_scope='unwinding builds; no claim to catch aborting process/WASM traps',limits=dict(subscriptions=1024,failure_records=64,error_message_chars=1024),retained_projection='immutable derived node deltas; no second writable replica',scope='Rust production patches only; no JS subscription or WASM binding acceptance'),
 preserved_failures=['patches-1.log','patches-2.log','patches-3.log','failure-notes.json'],hygiene='hygiene.json',upstream='ENG-1.11 history 28/28 revalidated in current combined suite; foundation interop/schema_interop pass',permissions=dict(paid_inference=False,publication=False,deployment=False,source_roadmap_edited=False,second_parent_processed=False))
write('receipt.json',receipt)
print(json.dumps(dict(gate='ENG-1.12',rust=497,node=120,source_hashes=len(hashes),profile_hashes=sum(x['matched'] for x in frozen.values()))))

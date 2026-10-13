import json, hashlib, re, shutil, subprocess
from pathlib import Path
from datetime import datetime, timezone
root=Path('../architecture/evidence/browser-composition-remote')
run=root/'run-1'
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,d): p.write_text(json.dumps(d,indent=2)+'\n')
checks=[]; allfacts=[]
for suite,count,env,command in [('canonical',23,'COMPOSITION_REMOTE','npm run test:browser -- composition-remote'),('composition',38,'COMPOSITION','npm run test:browser -- composition')]:
 log=(run/(suite+'.log')).read_text()
 totals={k:[int(x) for x in re.findall(r'ℹ '+k+r' (\d+)',log)] for k in ['tests','pass','fail','cancelled','skipped']}
 assert totals['tests']==[count]*3 and totals['pass']==[count]*3,totals
 assert all(v==[0]*3 for k,v in totals.items() if k not in ['tests','pass']),totals
 engines=[]
 for engine in ['chromium','firefox','webkit']:
  p=run/suite/engine/'facts.json';d=json.loads(p.read_text());allfacts.append(d)
  assert len(d['cases'])==count and all(c['passed'] for c in d['cases']) and d['sourcesUnchanged']
  assert all(d['cleanup'].values()),d['cleanup']
  engines.append({'engine':engine,'version':d['browser']['version'],'executed':count,'passed':count,'failed':0,'skipped':0,'canceled':0,'facts':str(p.relative_to(root)),'factsSha256':digest(p),'packed':d['packed']})
 checks.append({'command':f'EDITAC_{env}_OUTPUT=../evidence/browser-composition-remote/run-1/{suite} '+command,'exit':0,'log':'run-1/'+suite+'.log','executed':count*3,'passed':count*3,'failed':0,'skipped':0,'canceled':0,'engines':engines})
narrow=(run/'narrow.log').read_text();assert 'ℹ tests 1' in narrow and 'ℹ pass 1' in narrow and 'ℹ fail 0' in narrow
checks.insert(0,{'command':'EDITAC_COMPOSITION_REMOTE_OUTPUT=../evidence/browser-composition-remote/run-1/narrow node --test --test-name-pattern=collapsed-at tests/browser/composition-remote.spec.ts','exit':0,'executed':1,'passed':1,'failed':0,'skipped':0,'canceled':0,'log':'run-1/narrow.log'})
narrowFacts=json.loads((run/'narrow/facts.json').read_text());assert len(narrowFacts['cases'])==1 and narrowFacts['cases'][0]['passed'] and narrowFacts['sourcesUnchanged'] and all(narrowFacts['cleanup'].values());allfacts.append(narrowFacts)
sources={}
for d in allfacts:
 for p,h in d['sources'].items():
  assert digest(p)==h,(p,'changed since check')
  if p in sources: assert sources[p]==h
  sources[p]=h
extra=json.loads((run/'additional-start-hashes.json').read_text())
for p,h in extra.items():assert digest(p)==h; sources[p]=h
snapshot='../architecture/progress/.roadmap-runner/04-browser-input-2e7632377a71/source-e70e728e1701.md'
assert digest(snapshot)=='78ed60d4dd3fa0c8055ffe2dbc957703e144f2e69172c0e26e1cb112e953c2ab'
write(root/'tested-source-hashes.json',sources)
for p in sources:
 # Snapshot in-scope code and harness without copying controller roadmaps.
 if not p.startswith('../'):
  target=run/'tested-sources'/p;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
changed=['packages/web/src/input/composition.ts','fixtures/browser-input/session.mjs','tests/browser/composition-remote.spec.ts','scripts/test-browser.mjs','fixtures/browser-input/README.md']
manifest={p:digest(p) for p in changed};write(root/'implementation-hashes.json',manifest)
pids=[p['pid'] for d in allfacts for p in d['processes']]
ps=subprocess.run(['ps','-axo','pid,ppid,command'],capture_output=True,text=True).stdout
(run/'processes-after.txt').write_text(ps)
remaining=[line for line in ps.splitlines() if line.strip() and line.strip().split()[0] in {str(p) for p in pids}]
assert not remaining,remaining
listeners=subprocess.run(['lsof','-nP','-iTCP','-sTCP:LISTEN'],capture_output=True,text=True).stdout
(run/'listeners-after.txt').write_text(listeners)
disk=subprocess.check_output(['df','-k','/System/Volumes/Data'],text=True);(run/'disk-after.txt').write_text(disk);free=int(disk.splitlines()[1].split()[3])*1024
cleanup={'browserControllersExited':len(pids),'allBrowserPidsAbsent':True,'allFixtureListenersRemoved':True,'allTemporaryPackedConsumersRemoved':True,'additionalPathsRemoved':[],'additionalBytesReclaimed':0,'remainingFreeBytes':free,'protectedListeners':sorted(set(int(x) for x in re.findall(r':(5173|8081|8001|4321|5432) \(LISTEN\)',listeners))),'details':'run-1/processes-after.txt and listeners-after.txt; narrow controller also exited in facts. No unrelated processes stopped; qualification artifacts retained.'}
write(run/'cleanup.json',cleanup)
receipt={'gate':'WEB-1.7','children':['WEB-1.7-I1','WEB-1.7-V1'],'state':'implemented and locally mechanically verified; prepared composition and peer deletion probe, no OS/device/release/deployment claim','sourceSnapshot':'../../progress/.roadmap-runner/04-browser-input-2e7632377a71/source-e70e728e1701.md','sourceRevision':digest(snapshot),'promptRevision':'7eaa063f3629','coreBaseRevision':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'architectureBaseRevision':subprocess.check_output(['git','-C','../architecture','rev-parse','HEAD'],text=True).strip(),'implementationRevision':hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest(),'verifiedAtUtc':datetime.now(timezone.utc).isoformat(),'sourceHashes':'tested-source-hashes.json','sourceManifestSha256':digest(root/'tested-source-hashes.json'),'testedSources':'run-1/tested-sources/','changedPaths':changed,'checks':checks,'nonSuiteChecks':[{'command':'npm run build --workspace @edit-ac/web','exit':0,'log':'run-1/build.log'},{'command':'npm run typecheck','exit':0,'log':'run-1/typecheck.log'},{'command':'git diff --check','exit':0,'log':'run-1/diff-check.log'},{'command':'node --check fixtures/browser-input/session.mjs','exit':0,'log':'run-1/fixture-syntax.log'}],'adr':{'version':1,'path':'../../decisions/004-browser-input-composition.md','sha256':digest('../architecture/decisions/004-browser-input-composition.md')},'prerequisites':{'engineSourceRevision':digest('../architecture/roadmaps/02-engine.md'),'storageSourceRevision':digest('../architecture/roadmaps/03-local-storage.md'),'comparison':'run-1/prerequisite-hashes.json','compositionReceipt':'../browser-composition/receipt.json','unchangedProduction':'Core/storage/DOM/selection/TextInput/reconcile sources and artifacts retain passing upstream evidence. Composition change fully regressed; fixture replacement helper is additive.'},'acceptance':{'remoteInsertions':'Before/at/after collapsed targets and directional replacement boundaries: held native text/node/caret, admitted peer state, authored final text/caret, exactly one local update/history/journal per composition. Selected-range insertion/deletion/replacement rejects remote-overlap and retains composed recovery text.','targetDeleted':'Real admitted Yjs deletion-probe updates hold the native owner until terminal boundary; final/blur reject stale-target, preserve captured text, remove deleted projection and clear selection without inserting into an adjacent block. Cancel/read-only retain text in canceled result.','independentPatches':'Independent peer block projection proceeds while composing owner remains held; burst updates project latest peer state. Local undo/redo affects composition only and retains peer updates.','ownership':'Duplicate terminal notifications do not repeat edits. Rejected target releases ownership for deliberate ordinary input; identical consecutive compositions remain distinct. UTF-16 and forward/backward replacements are authored.'},'fixtureSeed':'Fresh alpha/independent recovered real packed engine, peer checkpoint/update and isolated IndexedDB per case; explicit a😀b UTF-16 baseline.','qualificationLimits':'Composition replay is prepared real DOM through production handlers; remote text operations use second real engine and real update admission; target deletion uses existing Yjs deletion-probe tombstones, not a public semantic delete API. No provider/network/OS IME/device/release qualification.','cleanup':cleanup,'evidenceRelocation':'Commands used /Users/bpstr/Github/edit-ac/evidence/browser-composition-remote during execution; after all teardown, artifacts relocated intact to architecture/evidence/browser-composition-remote. Original facts/log paths remain unedited.'}
write(root/'receipt.json',receipt)
print(json.dumps({'canonical':69,'composition':114,'narrow':1,'failed':0,'skipped':0,'canceled':0,'receipt':str(root/'receipt.json'),'implementationRevision':receipt['implementationRevision'],'cleanup':cleanup}))

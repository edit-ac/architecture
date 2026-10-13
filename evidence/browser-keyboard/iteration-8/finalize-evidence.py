from pathlib import Path
import hashlib,json,shutil,subprocess,datetime,re
base=Path(__file__).resolve().parent
records=json.loads((base/'qualified-results.json').read_text()); paths={};checks=[]
expected={'keyboard':42,'input':17,'reconcile':30,'composition':38,'composition-remote':23}
for record in records:
 suite=record['suite'];assert record['exit']==0
 log=base/('qualified-'+suite+'.log');text=log.read_text()
 for field,value in [('tests',expected[suite]),('pass',expected[suite]),('fail',0),('skipped',0),('cancelled',0)]:
  assert [int(n) for n in re.findall(r'ℹ '+field+r' (\d+)',text)]==[value]*3,(suite,field)
 rows=[]
 for engine in ['chromium','firefox','webkit']:
  f=base/('qualified-'+suite)/engine/'facts.json';d=json.loads(f.read_text());assert len(d['cases'])==expected[suite];assert all(c['passed'] for c in d['cases']);assert d['sourcesUnchanged'];assert all(d['cleanup'].values())
  for p,h in d['sources'].items():
   assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,(suite,p)
   paths[p]=h
  rows.append({'engine':engine,'browser':d['browser'],'executed':expected[suite],'passed':expected[suite],'failed':0,'skipped':0,'cancelled':0,'facts':str(f),'factsSha256':hashlib.sha256(f.read_bytes()).hexdigest(),'packed':d['packed'],'cleanup':d['cleanup']})
 checks.append({'command':record['command'],'exit':0,'environmentOutputVariable':'EDITAC_'+suite.upper().replace('-','_')+'_OUTPUT','environmentOutputValue':str(base/('qualified-'+suite)),'requiredCasesExcluded':3 if suite=='keyboard' else 0,'engines':rows,'log':str(log),'logSha256':hashlib.sha256(log.read_bytes()).hexdigest()})
for p in ['tests/browser/input.spec.ts','tests/browser/composition.spec.ts','packages/core/src/engine.ts','crates/editac-core/src/commands/editor.rs','crates/editac-core/src/commands/lists.rs','crates/editac-wasm/src/bridge.rs']:
 paths[p]=hashlib.sha256(Path(p).read_bytes()).hexdigest()
for p,h in paths.items():
 dest=base/'tested-sources'/p;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
(base/'implementation-sha256.json').write_text(json.dumps(paths,indent=2)+'\n')
ps=subprocess.check_output(['ps','-axo','pid,ppid,command'],text=True);(base/'processes-final.txt').write_text(ps)
ls=subprocess.run(['lsof','-nP','-iTCP','-sTCP:LISTEN'],text=True,capture_output=True).stdout;(base/'listeners-final.txt').write_text(ls)
alive={int(line.split(None,2)[0]):line for line in ps.splitlines()[1:] if line.split()};survivors=[]
for root in [base,base.parent/'iteration-7']:
 for f in root.rglob('facts.json'):
  d=json.loads(f.read_text())
  for item in d.get('processes',[])+[d.get('server',{})]:
   if item.get('pid') in alive:survivors.append({'pid':item['pid'],'command':alive[item['pid']],'facts':str(f)})
assert not survivors,survivors
resources={'recordedTaskPidsStillAlive':survivors,'protectedPortsListening':{str(port):any(':'+str(port)+' ' in line for line in ls.splitlines()) for port in [5173,8081,8001,4321,5432]},'stoppedByWorker':[]};assert all(resources['protectedPortsListening'].values())
(base/'resource-check.json').write_text(json.dumps(resources,indent=2)+'\n')
disk=subprocess.check_output(['df','-k','/System/Volumes/Data'],text=True);(base/'disk-final.txt').write_text(disk);free=int(disk.splitlines()[-1].split()[3])
subprocess.run(['du','-sk','target','node_modules','packages/web/dist',str(base)],stdout=(base/'sizes-final.txt').open('w'),check=True)
r=subprocess.run(['git','diff','--check'],text=True,capture_output=True);(base/'diff-check-final.log').write_text(r.stdout+r.stderr);assert r.returncode==0
(base/'git-status-final.txt').write_text(subprocess.check_output(['git','status','--short'],text=True))
attempts=[]
for p in base.glob('*.log'):
 text=p.read_text();counts={key:sum(int(x) for x in re.findall(r'ℹ '+key+r' (\d+)',text)) for key in ['tests','pass','fail','cancelled','skipped']}
 attempts.append({'log':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'counts':counts})
narrow=[]
for engine in ['chromium','firefox','webkit']:
 f=base/'escape-final'/engine/'facts.json';d=json.loads(f.read_text());assert len(d['cases'])==6 and all(c['passed'] for c in d['cases']) and d['sourcesUnchanged'];narrow.append({'engine':engine,'executed':6,'passed':6,'failed':0,'skipped':0,'cancelled':0,'facts':str(f)})
receipt={'task':'WEB-1.8','state':'partial; original parent/I1/V1 remain unchecked; C1 verified','date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sourceRevision':'78ed60d4dd3fa0c8055ffe2dbc957703e144f2e69172c0e26e1cb112e953c2ab','promptRevision':'7eaa063f3629','coreBaseRevision':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'implementationManifest':'implementation-sha256.json','testedSources':'tested-sources/','checks':checks,'narrow':{'command':['npm','run','test:browser','--','keyboard','--test-name-pattern=native-focus-escape'],'exit':0,'engines':narrow,'log':'escape-final.log'},'build':{'command':'npm run build --workspace @edit-ac/web','exit':0,'log':'build-final.log'},'typecheck':{'command':'npm run typecheck','exit':0,'log':'typecheck-final.log'},'diffCheck':{'command':'git diff --check','exit':0,'log':'diff-check-final.log'},'preservedAttempts':attempts,'interimEvidence':'pre-fallback-receipt.json; pre-fallback-implementation-sha256.json; pre-fallback-tested-sources/','unmetCriteria':[{'criterion':'Context-appropriate Enter at heading end','requiredUnexecutedCases':3,'failureEvidence':'../iteration-7/initial.log','failureSha256':hashlib.sha256((base.parent/'iteration-7/initial.log').read_bytes()).hexdigest(),'failureUnchanged':True,'unblock':'Qualified atomic contextual heading-end engine/WASM command; controller split in controller-split.md'}],'qualificationLimits':['Real packed engine/storage/DOM; native keyboard versus prepared provenance recorded per case.','No actual OS/device IME qualification. Firefox keyboard.type tab composition setup rejection preserved; the indentation test seeds authored whitespace through real recovery, not injected composition.','Node reports zero skips for name-excluded tests; three required heading-end cases intentionally NOT executed. Partial results do not satisfy parent acceptance.'],'resources':resources,'disk':{'freeKiB':free,'removedPaths':[],'reclaimedBytes':0,'sessionConsumers':'Removed by test teardown','largestPreexistingCandidate':'core/target: 5.8 GiB; not touched; separate cleanup question pending'}}
(base/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('Final receipt:',len(paths),'manifest paths;',sum(x['executed'] for c in checks for x in c['engines']),'executed/passed; 3 required exclusions;',round(free/1024/1024,1),'GiB free; no surviving task processes.')

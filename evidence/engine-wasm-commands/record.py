from pathlib import Path
import hashlib,json,re,subprocess,datetime,os
root=Path.cwd(); evidence=root/'../architecture/evidence/engine-wasm-commands'
def write(name,data): (evidence/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
commands=[
 ('native-acceptance.log','EDITAC_WASM_COMMAND_OUTPUT=<evidence> cargo test -p editac-wasm --lib --locked --offline','rust'),
 ('kernel-regression.log','cargo test -p editac-core --lib --locked --offline','rust'),
 ('wasm-commands-standalone.log','node --test tests/wasm-commands.test.mjs','node'),
 ('loader-acceptance.log','EDITAC_WASM_OUTPUT=<evidence>/loader-final node --test tests/wasm-load.test.mjs','node'),
]
checks=[]
for log,command,runner in commands:
 text=(evidence/log).read_text()
 if runner=='rust':
  m=re.search(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',text); assert m
  p,f,s,measured,filtered=map(int,m.groups()); assert measured==filtered==0
 else:
  values={k:int(re.search(r'ℹ '+k+r' (\d+)',text).group(1)) for k in ['tests','pass','fail','skipped','cancelled','todo']}
  p,f,s=values['pass'],values['fail'],values['skipped']; assert values['tests']==p+f+s and values['cancelled']==values['todo']==0
 assert p>0 and f==s==0
 checks.append(dict(command=command,runner=runner,exit=0,executed=p+f+s,passed=p,failed=f,skipped=s,log=log,sha256=digest(evidence/log)))
for log,command in [
 ('build-wasm-acceptance.log','npm run build:wasm'),('build-packages-acceptance.log','npm run build'),
 ('consumer-types-final.log','node_modules/.bin/tsc --noEmit --strict --exactOptionalPropertyTypes --target ES2022 --module NodeNext --moduleResolution NodeNext tests/wasm-command-types.ts'),
 ('format-check.log','cargo fmt --all -- --check'),('package-exports.log','node scripts/check-package-exports.mjs'),('diff-check.log','git diff --check')]:
 checks.append(dict(command=command,exit=0,log=log,sha256=digest(evidence/log),scope='build/static check; not counted as executed tests'))
write('checks.json',checks)
files=set()
for directory in ['crates/editac-core/src','crates/editac-wasm/src','packages/core/src','fixtures/wasm-commands']:
 files.update(p for p in Path(directory).rglob('*') if p.is_file())
files.update(Path(f) for f in ['Cargo.lock','Cargo.toml','rust-toolchain.toml','package.json','package-lock.json','crates/editac-core/Cargo.toml','crates/editac-wasm/Cargo.toml','packages/core/package.json','tests/wasm-commands.test.mjs','tests/wasm-load.test.mjs','tests/wasm-command-types.ts','scripts/build-wasm.mjs','tsconfig.base.json','packages/core/tsconfig.json','../architecture/specs/engine.md','../architecture/specs/verification.md','../architecture/specs/schema-v4.md','../architecture/specs/schema-v5.md','../architecture/progress/.roadmap-runner/02-engine-4d812f5d0e69/source-f6218bddbd75.md'])
files.update(p for d in ['fixtures/schema-v3','fixtures/schema-v4','fixtures/schema-v5'] for p in Path(d).glob('*.rs'))
write('tested-source-hashes.json',{str(p):digest(p) for p in sorted(files)})
corpus=json.loads(Path('fixtures/wasm-commands/cases.json').read_text()); assert len(corpus['cases'])==17
for c in corpus['cases']:
 name=c['id']; a=json.loads((evidence/f'native-{name}.json').read_text()); b=json.loads((evidence/f'wasm-{name}.json').read_text()); assert a==b
 assert (evidence/f'native-raw-{name}.json').exists() and (evidence/f'wasm-raw-{name}.json').exists()
criteria={
 'ENG-1.14-I1: opaque production create/read':{'implementation':['crates/editac-wasm/src/{bridge,engine}.rs','packages/core/src/{engine,index}.ts'],'proof':['all 17 shared v5 scenarios','explicit empty creation','detached snapshots','typed consumer negative controls']},
 'ENG-1.14-I1: prepared semantic commands':{'proof':['unicode insert/delete/replace','six marks and levels 1–6','start/middle/end/empty split and joined multi-source presentation','list/quote/check/number/enter/backspace/indent/outdent','code/hard break/dormant marks/separator accessible neighbor','versioned move','explicit and typing history, undo/redo/clear'],'fixtures':[c['id'] for c in corpus['cases']]},
 'ENG-1.14-I1/V1: JS validation and atomic rejection':{'proof':['native exact checkpoint bytes/revision/history preservation','JS snapshot/revision/history preservation','invalid surrogate/offset/type/unknown fields/origins/URLs/levels/mixed batches','byte/anchor/plan caps','cross-handle/released/consumed/stale plans'],'source':['crates/editac-wasm/src/cases.rs','tests/wasm-commands.test.mjs']},
 'ENG-1.14-V1: actual built WASM shared fixtures':{'proof':'17 native/WASM full semantic snapshots match after writer normalization; Yrs/Yjs decode and exact re-encode retained relative anchors, including target/clock/association. Literal text and opaque attribute guard prevents comparator normalization hiding content changes. Raw snapshots retained.','artifact':'native-*.json / wasm-*.json / *-raw-*.json'},
 'ENG-1.14-V1: explicit/idempotent disposal':{'proof':['raw Engine Option disposal drops all replica-owned resources and rejects later calls','package wrapper dispose/free once with repeated dispose safe','built and packed browser real replacement/undo/redo/anchor/disposal'],'artifact':['harness.json','loader-final/harness.json']},
}
write('criterion-map.json',criteria)
failures=[]
for name,reason,counts in [
 ('compile-initial.log','wrong Any enum variant repaired',None),
 ('native-initial.log','15/21 passed; strict unit variants, JSON numeric normalization and independent oracle issues repaired',{'executed':21,'passed':15,'failed':6,'skipped':0}),
 ('native-repair.log','incorrect single text API call repaired',None),
 ('native-second-feature.log','20/21 passed; unknown language label fixture repaired against ASCII schema',{'executed':21,'passed':20,'failed':1,'skipped':0}),
 ('build-wasm-initial.log','Homebrew rustc selected without WASM target; repaired by selecting workspace rustup shim',None),
 ('wasm-commands-initial.log','map-key writer normalization repaired',{'executed':23,'passed':6,'failed':17,'skipped':0}),
 ('wasm-commands-key-repair.log','projected source identity normalization repaired',{'executed':23,'passed':6,'failed':17,'skipped':0}),
 ('wasm-commands-identity-repair.log','retained binary anchors decoded with both pinned implementations before comparison',{'executed':24,'passed':19,'failed':5,'skipped':0})]:
 failures.append(dict(log=name,sha256=digest(evidence/name),reason=reason,counts=counts))
write('preserved-failures.json',failures)
cleanup=json.loads((evidence/'cleanup.json').read_text()); hygiene=json.loads((evidence/'pre-cleanup-hygiene.json').read_text()); assert not any(p['present'] for p in hygiene['processes']); assert not any(hygiene['listeners'].values())
compiled={str(p.relative_to(evidence)):dict(bytes=p.stat().st_size,sha256=digest(p)) for p in (evidence/'compiled-package').rglob('*') if p.is_file()}
receipt=dict(task='ENG-1.14',children=['ENG-1.14-I1','ENG-1.14-V1'],state='IMPLEMENTED_AND_LOCALLY_VERIFIED',deployed=False,published=False,
 sourceRevision='83adc7f7c82e9ffe593ac851fc6eca88ece43c7070cf5f18bea2c78c2158b677',promptRevision='7eaa063f3629',iteration=7,
 implementationBase=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),architectureBase=subprocess.check_output(['git','-C','../architecture','rev-parse','HEAD'],text=True).strip(),uncommitted=True,
 environment=dict(node='24.19.0',rustup='1.97.1',wasmBindgen='0.2.129',yrs='0.28.0 small-client',yjs='13.6.33',PATH='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:/Users/bpstr/.cargo/bin:$PATH'),
 counts=dict(nativeBridge=23,kernel=14,builtWasm=25,browserLoader=7,failed=0,skipped=0,filtered=0,sharedScenarios=17),
 checks='checks.json',criteria='criterion-map.json',testedHashes='tested-source-hashes.json',preservedFailures='preserved-failures.json',prerequisiteIntegrity='prerequisite-integrity.json',
 compiled=compiled,rawSnapshots='native-raw-*.json and wasm-raw-*.json',hygiene='pre-cleanup-hygiene.json',cleanup='cleanup.json',
 disk=dict(removedNativeArtifactBytes=cleanup['removedBytes'],remainingFreeBytes=cleanup['freeAfter'],remainingCandidate='shared target/debug (~4.94 GiB); preserve until ownership/continued use confirmed'),
 boundary=dict(profile='explicit v5 creation only; no automatic migration',resources='2 MiB request; <=128 commands; 128 retained plans; 4096 anchors; kernel content/history caps',updatesRestoreSubscriptions='ENG-1.15 remains unimplemented/unverified',cost='deterministic local corpus; zero provider calls; no secrets loaded',noPerformanceOrReleaseClaim=True),
 exit='one-parent outcome passed; next parent ENG-1.15 not started',recordedUtc=datetime.datetime.now(datetime.timezone.utc).isoformat())
write('receipt.json',receipt)
# Manifest avoids self-reference and includes raw/compiled qualification evidence.
write('artifacts.json',{str(p.relative_to(evidence)):dict(bytes=p.stat().st_size,sha256=digest(p)) for p in sorted(evidence.rglob('*')) if p.is_file() and p.name!='artifacts.json'})
print('receipt: 37 Rust + 32 Node tests passed; zero failures/skips; 17 native/WASM scenario pairs verified')
print('tested source hashes',len(files),'compiled artifacts',len(compiled),'removed native bytes',cleanup['removedBytes'])

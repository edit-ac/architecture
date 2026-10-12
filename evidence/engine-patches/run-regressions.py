"""Run existing deterministic integration harnesses in isolated evidence paths."""
import datetime, hashlib, json, os, pathlib, subprocess
root=pathlib.Path('/Users/bpstr/Github/edit-ac/core')
out=root.parent/'architecture/evidence/engine-patches'
prior=json.loads((root.parent/'architecture/evidence/engine-history/regression-command.json').read_text())
command=prior['command']
selected={k:str(out/'exchange'/pathlib.Path(v).name) for k,v in prior['environment'].items() if k.startswith('EDITAC_')}
selected.update(RUSTC='/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustc',RUSTDOC='/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustdoc',CARGO_INCREMENTAL='0')
env=os.environ.copy(); env.update(selected); env['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:/Users/bpstr/.cargo/bin:'+env['PATH']
node=subprocess.check_output(['node','--version'],env=env,text=True).strip(); assert node=='v24.19.0'
paths=set(json.loads((root.parent/'architecture/evidence/engine-history/tested-source-hashes.json').read_text())) | {'crates/editac-core/src/patches.rs','crates/editac-core/tests/patches.rs'}
hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in sorted(paths)}
(out/'tested-source-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
(out/'regression-command.json').write_text(json.dumps(dict(command=command,cwd=str(root),environment=selected,PATH_PREFIX=env['PATH'].split(':',2)[:2],node=node,start_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n')
with (out/'regressions.log').open('wb') as log: r=subprocess.run(command,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
unchanged=all(hashlib.sha256((root/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
result=dict(exit=r.returncode,tested_sources_unchanged=unchanged,tested_source_count=len(hashes),log_bytes=(out/'regressions.log').stat().st_size)
(out/'regression-result.json').write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result)); raise SystemExit(r.returncode or (0 if unchanged else 1))

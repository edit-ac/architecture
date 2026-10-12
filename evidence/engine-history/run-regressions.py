import hashlib, json, os, pathlib, subprocess, datetime
root = pathlib.Path('/Users/bpstr/Github/edit-ac/core')
out = root.parent / 'architecture/evidence/engine-history'
previous = json.loads((root.parent / 'architecture/evidence/engine-stable-presentation/rustup-command.json').read_text())
command = previous['command'].copy()
command[-1:-1] = ['--test','history']
env = os.environ.copy()
selected = {k: str(out / 'regression-exchange' / pathlib.Path(v).name) for k,v in previous['environment'].items() if k != 'PATH_PREFIX'}
selected['EDITAC_HISTORY_EXCHANGE'] = str(out / 'regression-exchange/history')
selected['RUSTC'] = '/Users/bpstr/.rustup/toolchains/1.97.1-aarch64-apple-darwin/bin/rustc'
selected['CARGO_INCREMENTAL'] = '0'
env.update(selected)
env['PATH'] = '/Users/bpstr/.nvm/versions/node/v24.19.0/bin:/Users/bpstr/.cargo/bin:' + env['PATH']
node = subprocess.check_output(['node','--version'],env=env,text=True).strip()
assert node == 'v24.19.0', node
sources = json.loads((root.parent / 'architecture/evidence/engine-stable-presentation/tested-source-hashes.json').read_text())
paths = set(sources) | {'crates/editac-core/src/history.rs','crates/editac-core/tests/history.rs','tests/history-exchange.mjs'}
hashes = {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in sorted(paths)}
(out/'tested-source-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
(out/'regression-command.json').write_text(json.dumps({'command': command,'cwd':str(root),'environment':selected,'PATH_PREFIX':env['PATH'].split(':',2)[:2],'node':node,'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
with (out/'regressions.log').open('wb') as log:
    result = subprocess.run(command,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
unchanged = all(hashlib.sha256((root/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
(out/'regression-result.json').write_text(json.dumps({'exit':result.returncode,'tested_sources_unchanged':unchanged,'tested_source_count':len(hashes)},indent=2)+'\n')
print(json.dumps({'exit':result.returncode,'node':node,'tested_sources_unchanged':unchanged,'log_bytes':(out/'regressions.log').stat().st_size}))
raise SystemExit(result.returncode or (0 if unchanged else 1))

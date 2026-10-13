from pathlib import Path
import os, shutil, subprocess, json
root=Path.cwd(); out=root.parent/'architecture/evidence/browser-size-optimization/iteration1'; dest=out/'baseline-core'; dest.mkdir(exist_ok=True); (dest/'dist/wasm').mkdir(parents=True,exist_ok=True)
env=os.environ.copy();env['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:'+env['PATH']
toolchain='1.97.1'
env['RUSTC']=subprocess.check_output(['rustup','which','--toolchain',toolchain,'rustc'],text=True).strip()
cargo=subprocess.check_output(['rustup','which','--toolchain',toolchain,'cargo'],text=True).strip()
commands=[[cargo,'build','-p','editac-wasm','--release','--features','foundation-fixture','--target','wasm32-unknown-unknown','--locked','--offline'],['wasm-bindgen','target/wasm32-unknown-unknown/release/editac_wasm.wasm','--target','web','--out-dir',str(dest/'dist/wasm'),'--out-name','editac_wasm']]
results=[]
for i,cmd in enumerate(commands):
 with (out/f'baseline-build-{i}.log').open('w') as log:r=subprocess.run(cmd,env=env,stdout=log,stderr=subprocess.STDOUT)
 results.append({'command':cmd,'exit':r.returncode});assert r.returncode==0
for p in (root/'packages/core/dist').iterdir():
 if p.is_file():shutil.copy2(p,dest/'dist'/p.name)
# The pre-separation loader, freshly compiled by tsc as the explicit fixture entry.
for suffix in ['js','d.ts']:
 content=(dest/'dist'/f'fixture.{suffix}').read_text().replace('initFixture','init').replace('wasm-fixture/','wasm/')
 (dest/'dist'/f'index.{suffix}').write_text(content)
for name in ['package.json','README.md','LICENSE','THIRD-PARTY-NOTICES.txt']:shutil.copy2(root/'packages/core'/name,dest/name)
(out/'baseline-build-receipt.json').write_text(json.dumps({'profile':'release (unoptimized size policy), full foundation fixture roots','baseline':'reconstructed fresh pre-optimization configuration; current identical semantic engine source plus fixture feature/module separation, original opaque loader','commands':results},indent=2)+'\n')
print('fresh reconstructed baseline ready',dest)

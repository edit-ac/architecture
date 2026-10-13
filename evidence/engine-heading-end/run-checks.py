from pathlib import Path
import subprocess, os, json, time, tarfile, shutil
root=Path('/Users/bpstr/Github/edit-ac/core'); evidence=root.parent/'architecture/evidence/engine-heading-end'
env=os.environ.copy(); env['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:/Users/bpstr/.cargo/bin:'+env['PATH']
commands=[]
def run(name,args,extra=None,cwd=root):
    log=evidence/(name+'.log'); start=time.time()
    with log.open('w') as f: r=subprocess.run(args,cwd=cwd,env={**env,**(extra or {})},stdout=f,stderr=subprocess.STDOUT)
    commands.append(dict(name=name,command=args,cwd=str(cwd),exit=r.returncode,seconds=round(time.time()-start,2),log=str(log.relative_to(evidence)),bytes=log.stat().st_size))
    (evidence/'checks.json').write_text(json.dumps(commands,indent=2)+'\n')
    print(json.dumps(commands[-1]),flush=True)
    if r.returncode: raise SystemExit(r.returncode)
run('versions',['node','--version'])
run('build-wasm',['npm','run','build:wasm'])
run('build',['npm','run','build'])
run('typecheck',['npm','run','typecheck'])
(evidence/'commands').mkdir(exist_ok=True)
run('native-wasm-fixtures',['cargo','test','-p','editac-wasm','--lib','--locked','--offline'],{'EDITAC_WASM_COMMAND_OUTPUT':str(evidence/'commands')})
run('pack',['npm','pack','--workspace','@edit-ac/core','--pack-destination',str(evidence),'--json'])
pack=json.loads((evidence/'pack.log').read_text())[0]; tarball=evidence/pack['filename']
consumer=evidence/'consumer'; package=consumer/'node_modules/@edit-ac/core'; package.mkdir(parents=True,exist_ok=True)
with tarfile.open(tarball) as t:
    for m in t.getmembers():
        if m.name.startswith('package/'):
            m.name=m.name[len('package/'):]
            if m.name: t.extract(m,path=package,filter='data')
(consumer/'package.json').write_text('{"private":true,"type":"module"}\n')
shutil.copyfile(root/'tests/wasm-command-types.ts',consumer/'wasm-command-types.ts')
run('packed-types',['node',str(root/'node_modules/typescript/bin/tsc'),'--strict','--noEmit','--target','ES2022','--module','NodeNext','--moduleResolution','NodeNext','wasm-command-types.ts'],cwd=consumer)
run('wasm-commands',['node','--test','tests/wasm-commands.test.mjs'],{'EDITAC_WASM_COMMAND_OUTPUT':str(evidence/'commands'),'EDITAC_WASM_COMMAND_PACKAGE':str(package)})
run('editor-history-regressions',['cargo','test','-p','editac-core','--test','editor_profile','--test','stable_editor_profile','--test','history','--test','blocks','--locked','--offline'])
run('format-check',['cargo','fmt','--all','--','--check'])
run('diff-check',['git','diff','--check'])

from pathlib import Path
import os,json,subprocess
root=Path(__file__).resolve().parents[3]/'core'
out=Path(__file__).resolve().parent
node=Path('/Users/bpstr/.nvm/versions/node/v24.19.0/bin')
env=dict(os.environ,PATH=str(node)+os.pathsep+os.environ['PATH'])
assert subprocess.check_output(['node','--version'],env=env,text=True).strip()=='v24.19.0'
old=out/'exchange/node.log'
if old.exists(): (out/'exchange/node-unqualified-26.log').write_bytes(old.read_bytes())
commands=[('feature-pinned',['cargo','test','-p','editac-core','--test','block_profile','--locked']),('legacy-pinned',['cargo','test','-p','editac-core','--test','format_commands','--test','interop','--test','schema_interop','--test','split_join','--locked'])]
results=[]
for name,cmd in commands:
 log=out/(name+'.log')
 with log.open('wb') as stream: result=subprocess.run(cmd,cwd=root,env=env,stdout=stream,stderr=subprocess.STDOUT)
 results.append({'command':cmd,'log':str(log.relative_to(out)),'exit_code':result.returncode,'node_runtime':'v24.19.0'})
 (out/'pinned-check-results.json').write_text(json.dumps(results,indent=2)+'\n')
 print(name,'exit',result.returncode,'log bytes',log.stat().st_size,flush=True)
 if result.returncode: raise SystemExit(result.returncode)

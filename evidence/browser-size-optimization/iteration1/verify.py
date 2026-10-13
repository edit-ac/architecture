from pathlib import Path
import subprocess,os,re,json,time
out=Path('../architecture/evidence/browser-size-optimization/iteration1').resolve();env=os.environ.copy();env['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:'+env['PATH']
rust=out/'rust-qualified/fixtures'
env.update(EDITAC_BROWSER_SIZE_OUTPUT=str(out/'direct-import'),EDITAC_WASM_OUTPUT=str(out/'fixture-compatibility-final'),EDITAC_BASELINE_OUTPUT=str(out/'baseline'),EDITAC_PACKED_OUTPUT=str(out/'packed'),EDITAC_MODULE_BUNDLES=str(out/'module-bundles'),EDITAC_CHECKPOINT_OUTPUT=str(out/'checkpoint'),EDITAC_LIFECYCLE_OUTPUT=str(out/'storage-lifecycle'),EDITAC_SYNC_PROTOCOL_OUTPUT=str(out/'sync-protocol'),EDITAC_EXTENSION_ENTRY_FIXTURES=str(rust/'extension_entry_output'),EDITAC_MATH_FIXTURES=str(rust/'math_fixtures'),EDITAC_MODULE_REGISTRY_FIXTURES=str(rust/'module_registry_fixtures'))
commands=[('packages',['npm','run','check:packages']),('size-runtime',['node','--test','tests/browser-size.test.mjs','tests/browser-size-consumer.test.mjs','tests/wasm-load.test.mjs','tests/large-update-recovery.test.mjs','tests/protocol-toolchain.test.mjs']),('module-storage-sync',['node','--test','tests/module-runtime.test.mjs','tests/module-contract.test.mjs','tests/module-bundles.test.mjs','tests/checkpoint.test.mjs','tests/storage-lifecycle.test.mjs','tests/sync-protocol.test.mjs']),('baseline',['npm','run','check:browser-baseline'])]
for suite in ['sdk','input','input-policy','composition','composition-remote','selection','recovery','offline-collaboration','markdown-paste','clipboard-formats','markdown-extensions','html-paste','markdown-collaboration','module-runtime','module-contract','extension-entry','content-modules','math']:
 env['EDITAC_'+suite.upper().replace('-','_')+'_OUTPUT']=str(out/'browser'/suite)
 commands.append((suite,['npm','run','test:browser','--',suite]))
commands.append(('packed',['node','--test','tests/packed-consumers.test.mjs']))
results=[]
for name,cmd in commands:
 started=time.monotonic();log=out/('verify-'+name+'.log')
 with log.open('w') as f:r=subprocess.run(cmd,env=env,stdout=f,stderr=subprocess.STDOUT)
 text=log.read_text();counts={}
 for key in ['tests','pass','fail','cancelled','skipped']:
  found=re.findall(r'(?:^|\n)(?:# |ℹ )'+key+r' (\d+)',text);counts[key]=sum(map(int,found))
 results.append({'name':name,'command':cmd,'exit':r.returncode,'seconds':round(time.monotonic()-started,2),'counts':counts,'log':str(log)})
 (out/'verification.json').write_text(json.dumps({'environment':{k:v for k,v in env.items() if k.startswith('EDITAC_')},'checks':results},indent=2)+'\n')
 print(name,r.returncode,counts,flush=True)
 if r.returncode:print('preserved failure:',log,flush=True)

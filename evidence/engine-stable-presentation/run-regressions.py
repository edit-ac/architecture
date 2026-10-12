from pathlib import Path
import subprocess,os,json,re
root=Path(__file__).resolve().parent
repo=Path('/Users/bpstr/Github/edit-ac/core')
env=os.environ.copy();env['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:'+env['PATH']
variables=['EDITOR','RETAINED','BLOCK','FORMAT','FORMAT_BLOCK','BLOCK_KINDS','OWNERSHIP','MOVE','STRUCTURAL','GENERAL','LIST','SPLIT_JOIN']
for name in variables:env['EDITAC_'+name+'_EXCHANGE']=str(root/'regression-exchange'/name.lower())
for name in ['INTEROP','SCHEMA_INTEROP']:env['EDITAC_'+name+'_OUTPUT']=str(root/'regression-exchange'/name.lower())
suites=['retained_presentation_profile','editor_profile','lists','moves','text_commands','format_commands','anchors','split_join','structural_profile','block_kinds_profile','ownership_profile','block_profile','initialization','projection','interop','schema_interop']
cmd=['cargo','test','-p','editac-core','--locked','--lib']
for name in suites:cmd+=['--test',name]
cmd+=['--no-fail-fast']
selected={k:v for k,v in env.items() if k.startswith('EDITAC_')};selected['PATH_PREFIX']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin'
(root/'regression-command.json').write_text(json.dumps({'command':cmd,'cwd':str(repo),'environment':selected},indent=2)+'\n')
with (root/'regressions.log').open('w') as f:r=subprocess.run(cmd,cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT)
s=(root/'regressions.log').read_text();counts=[list(map(int,m)) for m in re.findall(r'test result: .*? (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',s)]
result={'exit':r.returncode,'suites':len(counts),'counts':counts,'totals':[sum(c[i] for c in counts) for i in range(5)],'log_bytes':len(s.encode())}
(root/'regression-result.json').write_text(json.dumps(result,indent=2)+'\n');print(result);raise SystemExit(r.returncode)

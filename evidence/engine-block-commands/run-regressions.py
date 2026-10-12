import json, os, re, subprocess
from pathlib import Path
root=Path('/Users/bpstr/Github/edit-ac/core')
out=Path(__file__).resolve().parent
env=os.environ.copy();env['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:'+env['PATH'];env['CARGO_INCREMENTAL']='0'
for name,directory in {'EDITAC_EDITOR_EXCHANGE':'editor-exchange','EDITAC_STRUCTURAL_EXCHANGE':'structural-exchange','EDITAC_BLOCK_KINDS_EXCHANGE':'block-kinds-exchange','EDITAC_OWNERSHIP_EXCHANGE':'ownership-exchange','EDITAC_BLOCK_EXCHANGE':'block-exchange','EDITAC_SPLIT_JOIN_EXCHANGE':'split-join-exchange','EDITAC_LIST_EXCHANGE':'list-exchange','EDITAC_INTEROP_OUTPUT':'interop','EDITAC_SCHEMA_INTEROP_OUTPUT':'schema-interop'}.items():env[name]=str(out/directory)
command=['cargo','test','-p','editac-core','--locked','--lib','--test','editor_profile','--test','structural_profile','--test','block_kinds_profile','--test','ownership_profile','--test','block_profile','--test','initialization','--test','projection','--test','anchors','--test','text_commands','--test','format_commands','--test','split_join','--test','lists','--test','interop','--test','schema_interop','--no-fail-fast']
with (out/'regressions-1.log').open('w') as log:r=subprocess.run(command,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
s=(out/'regressions-1.log').read_text();counts=[dict(zip(['passed','failed','skipped','measured','filtered'],map(int,m))) for m in re.findall(r'test result: \w+\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',s)]
report={'command':command,'environment':{k:v for k,v in env.items() if k.startswith('EDITAC_') or k in ['PATH','CARGO_INCREMENTAL']},'exit':r.returncode,'suites':counts,'totals':{k:sum(x[k] for x in counts) for k in ['passed','failed','skipped','filtered']},'log':'regressions-1.log'}
(out/'regressions.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'exit':r.returncode,'suites':len(counts),'totals':report['totals'],'logBytes':len(s)}));print('\n'.join(line for line in s.splitlines() if line.startswith('error:') or line.startswith('---- ')))

import json,hashlib
from pathlib import Path
base=Path('../architecture/evidence')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
specs=[
 ('slash','slash','browser-tabindex','packages/web/src/modules/slash.ts',{'read':['eligible','literal'],'edit':['keyboard-history','pointer-focus','ime-priority','provenance'],'disabled':['provenance','context']}),
 ('references','references','browser-pre-clipboard-repair','packages/web/src/modules/references.ts',{'read':['no-implicit','recovery-fallback'],'edit':['stale-query','keyboard-history','anchored-selection'],'copy':['clipboard-fallback'],'disabled':['recovery-fallback']}),
 ('reorder','reorder','complete-browser','packages/web/src/modules/reorder.ts',{'read':['tab-enter'],'edit':['keyboard-parity','button-parity','concurrent-before','concurrent-after','invalid-descendant','history'],'disabled':['recovery-disposal']}),
 ('images','content','canonical','packages/web/src/modules/content.ts',{'read':['render','no-policy','failed-policy'],'copy':['image-copy'],'disabled':['disabled-initial','disabled-recovery']}),
 ('tables','content','canonical','packages/web/src/modules/content.ts',{'read':['render'],'edit':['edit','history','composition','stale-composition','empty-multiline'],'copy':['keyboard-copy'],'markdown':['edit','disabled-recovery'],'disabled':['disabled-initial','disabled-recovery']}),
 ('math','math','browser','packages/web/src/modules/math.ts',{'read':['inline','display','invalid','renderer-safety','load-error'],'disabled':['disabled','absentRenderer','peer-source']})]
rows=[]
for name,group,run,source,caps in specs:
 proofs=[]
 for engine in ['chromium','firefox','webkit']:
  for cap,cases in caps.items():
   for case in cases:
    selected=run
    if name=='references' and case=='clipboard-fallback':selected='browser-clipboard-repair'
    if name=='math' and case=='peer-source':selected='peer-repair'
    p=base/f'modules-{group}'/selected/engine/'receipt.json';d=json.loads(p.read_text());c=next(x for x in d['cases'] if x['name']==case);assert c['passed']
    assert sha(Path(source))==d['sources'][source]
    proofs.append({'capability':cap,'case':case,'engine':engine,'artifact':str(p.relative_to(base)),'sha256':sha(p)})
 rows.append({'module':name,'parent':{'slash':'MOD-1.4','references':'MOD-1.5','reorder':'MOD-1.6','images':'MOD-1.7','tables':'MOD-1.7','math':'MOD-1.8'}[name],'source':source,'sourceSha256':sha(Path(source)),'qualifiedCapabilities':list(caps),'proofs':proofs})
d={'schemaVersion':1,'sourceRevision':'621cbff280187a584cd0ceb5b9ac66d176b916c16f99ba34a48e6fd74c08c294','scope':'Packed production browser mechanics with prepared fixtures; no device, native editing, deployment, provider or performance qualification.','modules':rows}
(base/'modules-matrix/capabilities.json').write_text(json.dumps(d,indent=2)+'\n')
print('Prepared six module rows,',sum(len(r['proofs']) for r in rows),'passing case references')

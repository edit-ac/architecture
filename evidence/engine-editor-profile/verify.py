from pathlib import Path
import json,os,re,subprocess,time
root=Path(__file__).resolve().parent
check=json.loads((root/'checks.json').read_text())
env=os.environ.copy();env.update(check['environment'])
started=time.time()
with (root/'regressions-2.log').open('w') as output:
    p=subprocess.run(check['regression_command'],env=env,stdout=output,stderr=subprocess.STDOUT)
log=(root/'regressions-2.log').read_text()
counts=[{'passed':int(a),'failed':int(b),'ignored':int(c),'filtered':int(d)} for a,b,c,d in re.findall(r'test result: .*? (\d+) passed; (\d+) failed; (\d+) ignored; \d+ measured; (\d+) filtered out',log)]
summary={'command':check['regression_command'],'exit_code':p.returncode,'elapsed_seconds':round(time.time()-started,2),'suites':counts,'totals':{k:sum(c[k] for c in counts) for k in ['passed','failed','ignored','filtered']},'log_bytes':(root/'regressions-2.log').stat().st_size}
(root/'regressions-2-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
raise SystemExit(p.returncode)

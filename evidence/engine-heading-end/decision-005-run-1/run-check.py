import sys,subprocess,pathlib,json,re,time,os
root=pathlib.Path(__file__).resolve().parent
name=sys.argv[1];command=sys.argv[2:];start=time.time()
os.environ['PATH']='/Users/bpstr/.nvm/versions/node/v24.19.0/bin:/Users/bpstr/.cargo/bin:'+os.environ['PATH']
for key,dirname in {'EDITAC_BLOCK_COMMAND_EXCHANGE':'blocks-exchange','EDITAC_STABLE_JOIN_EXCHANGE':'joined-exchange','EDITAC_HISTORY_EXCHANGE':'history-exchange','EDITAC_EDITOR_EXCHANGE':'editor-exchange','EDITAC_STABLE_EDITOR_EXCHANGE':'stable-editor-exchange'}.items():
 os.environ[key]=str(root/dirname)
with (root/(name+'.log')).open('w') as f:
 r=subprocess.run(command,stdout=f,stderr=subprocess.STDOUT,cwd=os.environ.get('EDITAC_CHECK_CWD'))
s=(root/(name+'.log')).read_text()
counts=[dict(zip(['passed','failed','skipped','measured','filtered'],map(int,m))) for m in re.findall(r'test result: .*? (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out',s)]
node={k:int(v) for k,v in re.findall(r'(?:#|ℹ) (tests|pass|fail|cancelled|skipped|todo) (\d+)',s)}
entry={'command':command,'cwd':os.environ.get('EDITAC_CHECK_CWD',os.getcwd()),'exit':r.returncode,'seconds':round(time.time()-start,2),'bytes':len(s.encode()),'log':name+'.log','toolchain':'Rust 1.97.1 rustup; Node 24.19.0; wasm-bindgen 0.2.129','rustSuites':counts,'nodeCounts':node}
(root/(name+'.json')).write_text(json.dumps(entry,indent=2)+'\n');print(json.dumps(entry))
if r.returncode: print(s[-3000:])
sys.exit(r.returncode)

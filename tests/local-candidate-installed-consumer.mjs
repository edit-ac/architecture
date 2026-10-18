// Executed from an independently installed candidate; imports resolve there only.
import assert from 'node:assert/strict';
import { readFileSync, writeFileSync } from 'node:fs';
import { createServer } from 'node:http';
import { createHash } from 'node:crypto';
const [candidate, output] = process.argv.slice(2);
const receipt = {candidate, node:process.version, cases:[], packs:[], counts:{executed:0,passed:0,failed:0,skipped:0}, cleanup:{}};
const hash = data => createHash('sha256').update(data).digest('hex');
const check = async (name, action) => {
  const fact={name,passed:false};receipt.cases.push(fact);receipt.counts.executed++;
  try { await action();fact.passed=true;receipt.counts.passed++; }
  catch(error){fact.error=error.stack;receipt.counts.failed++;throw error;}
};
let server, engine, restored;
try {
  assert.equal(process.version,'v24.19.0');
  // Prohibit ambient nonlocal fetches, including during package import.
  const nativeFetch=globalThis.fetch;
  const requests=[];
  globalThis.fetch=(url,...args)=>{
    const value=new URL(typeof url==='string'?url:url.url);
    assert.equal(value.hostname,'127.0.0.1','Only task-owned WASM HTTP transport permitted');
    requests.push(value.pathname);return nativeFetch(url,...args);
  };
  const core=await import('@edit-ac/core');
  await check('public-imports-have-no-browser-or-network-side-effects',async()=>{
    const web=await import('@edit-ac/web');
    assert.equal(typeof web.createEditor,'function');assert.equal(typeof core.init,'function');
    assert.equal(typeof globalThis.document,'undefined');assert.deepEqual(requests,[]);
  });
  if(candidate==='sdk-framework-v1') {
    await check('installed-react-ssr-and-astro-import-remain-inert',async()=>{
      const React=await import('react');const {renderToStaticMarkup}=await import('react-dom/server');
      const {EditorHost}=await import('@edit-ac/react');
      const astro=await import('@edit-ac/astro');assert.equal(typeof astro.mountEditorHost,'function');
      assert.match(renderToStaticMarkup(React.createElement(EditorHost,{options:{}})),/^<div/);
      assert.deepEqual(requests,[]);
    });
  } else {
    await check('installed-authoring-configuration-exports',async()=>{
      const web=await import('@edit-ac/web');
      assert.ok(web.Extension);assert.equal(typeof web.Extension.create,'function');
      assert.ok(web.Spelling);assert.equal(typeof web.Spelling.configure,'function');
      assert.throws(()=>web.Spelling.configure({mode:'automatic'}));assert.deepEqual(requests,[]);
    });
  }
  const coreWasm=readFileSync('node_modules/@edit-ac/core/dist/wasm/editac_wasm_bg.wasm');
  let markdownWasm;
  if(candidate==='sdk-framework-v1') markdownWasm=readFileSync('node_modules/@edit-ac/markdown/dist/wasm/editac_markdown_wasm_bg.wasm');
  receipt.runtime={coreSha256:hash(coreWasm),markdownSha256:markdownWasm?hash(markdownWasm):null};
  server=createServer((request,response)=>{
    const bytes=request.url==='/core.wasm'?coreWasm:request.url==='/markdown.wasm'?markdownWasm:null;
    if(!bytes){response.writeHead(404);response.end();return;}
    response.setHeader('Content-Type','application/wasm');response.end(bytes);
  });
  await new Promise(ok=>server.listen(0,'127.0.0.1',ok));
  receipt.server={pid:process.pid,port:server.address().port,purpose:'LCR-1.1 installed production WASM'};
  const origin='http://127.0.0.1:'+server.address().port;
  let runtime;
  await check('production-engine-invalid-asset-retry-and-current-wasm',async()=>{
    await assert.rejects(core.init(origin+'/missing.wasm'));
    runtime=await core.init(origin+'/core.wasm');
    engine=runtime.createEngine({profile:'v5',documentId:'85000000-0000-4000-8000-000000000001',epoch:'86000000-0000-4000-8000-000000000001',nodes:[{text:'Project kickoff 😀'}]});
    assert.match(JSON.stringify(engine.read()),/Project kickoff 😀/);
  });
  await check('production-checkpoint-reopen-and-disposal',()=>{
    const checkpoint=engine.checkpoint();const before=engine.read();
    restored=runtime.restoreEngine(checkpoint.identity,checkpoint);
    // Engine-local writer IDs are intentionally absent from this semantic oracle.
    assert.deepEqual(restored.read().visible,before.visible);
    assert.ok(Array.isArray(before.visible)&&before.visible.length>0);
    assert.match(JSON.stringify(restored.read()),/Project kickoff 😀/);
    restored.dispose();assert.throws(()=>restored.read(),/disposed/i);restored=null;
  });
  if(candidate==='sdk-framework-v1') {
    const {initMarkdown}=await import('@edit-ac/markdown');
    const codec=await initMarkdown(origin+'/markdown.wasm');engine.registerMarkdown(codec);
    await check('markdown-independent-format-roundtrip',()=>{
      const source='# Project kickoff\n\nA **bold** task and [safe](https://example.com/) link.\n';
      const prepared=engine.importMarkdown(source);
      assert.equal(prepared.source,source);assert.equal(prepared.blocks.length,2);
      assert.ok(prepared.blocks[1].runs.some(run=>run.text==='bold'&&run.marks.some(mark=>mark.mark==='bold')));
      const exported=engine.exportMarkdown(prepared.blocks);
      assert.match(exported.markdown,/\*\*bold\*\*/);
      assert.deepEqual(codec.exportMarkdown(codec.importMarkdown(exported.markdown).blocks),exported);
    });
    await check('markdown-disabled-unknown-source-retains-recovery',()=>{
      const source='> [!NOTE]\n> Original recovery 😀';
      const prepared=codec.importMarkdown(source);
      assert.equal(prepared.source,source);assert.ok(prepared.diagnostics.length>0);
      assert.equal(JSON.stringify(engine.read()).includes('Project kickoff 😀'),true);
      assert.equal(codec.importMarkdown('[unsafe](javascript:alert(1))').blocks.some(block=>block.runs.some(run=>run.marks.some(mark=>mark.mark==='link'))),false);
    });
  }
  receipt.requests=requests;
} catch(error) { receipt.error=error.stack;process.exitCode=1; }
finally {
  restored?.dispose();engine?.dispose();
  if(server?.listening){server.closeAllConnections();await new Promise(ok=>server.close(ok));}
  receipt.cleanup.serverClosed=!server?.listening;
  writeFileSync(output,JSON.stringify(receipt,null,2)+'\n');
}

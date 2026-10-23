// Supporting primitive probe, NOT production table/runtime acceptance.
import * as Y from '../../core/node_modules/yjs/dist/yjs.mjs';
import assert from 'node:assert/strict';
import test from 'node:test';
const root = 'table-text/t:1:1/r:1:2/k:1:4/base';
function doc(id, seed) { const d = new Y.Doc(); d.clientID = id; if(seed) Y.applyUpdate(d, seed); return d; }
function merges(a,b,expected) {
  const aa=Y.encodeStateAsUpdate(a), bb=Y.encodeStateAsUpdate(b);
  for (const order of [[aa,bb,aa],[bb,aa,bb]]) {
    const d=doc(30); for(const update of order) Y.applyUpdate(d, update);
    for(const [name,value] of Object.entries(expected)) assert.equal(d.getText(name).toString(),value);
    const reopened=doc(40,Y.encodeStateAsUpdate(d));
    for(const [name,value] of Object.entries(expected)) assert.equal(reopened.getText(name).toString(),value);
    d.destroy(); reopened.destroy();
  }
  a.destroy(); b.destroy();
}
test('primitive only: independently created named roots merge simultaneous first writes',()=>{
  const a=doc(10),b=doc(20); a.getText(root).insert(0,'X');b.getText(root).insert(0,'Y'); merges(a,b,{[root]:'XY'});
});
test('primitive only: pinned same-gap ordering matches authored expected text',()=>{
  const seed=doc(1);seed.getText(root).insert(0,'base');const bytes=Y.encodeStateAsUpdate(seed);seed.destroy();
  const a=doc(10,bytes),b=doc(20,bytes);a.getText(root).insert(2,'X');b.getText(root).insert(2,'Y');merges(a,b,{[root]:'baXYse'});
});
test('primitive only: separate named cell roots preserve both edits',()=>{
  const other='table-text/t:1:1/r:1:2/k:1:5/base';const a=doc(10),b=doc(20);
  a.getText(root).insert(0,'LEFT EDIT');b.getText(other).insert(0,'RIGHT EDIT');merges(a,b,{[root]:'LEFT EDIT',[other]:'RIGHT EDIT'});
});

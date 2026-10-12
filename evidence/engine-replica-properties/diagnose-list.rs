#[path="/Users/bpstr/Github/edit-ac/core/fixtures/schema-v5/mapping.rs"] mod m;
use editac_core::document::*;
use std::{fs,collections::BTreeSet,path::PathBuf};use yrs::{Map,ReadTxn,Transact};
fn identity()->DocumentIdentity {DocumentIdentity::v5("77777777-7777-4777-8777-777777777777","88888888-8888-4888-8888-888888888888").unwrap()}
fn main(){
 let root=PathBuf::from("/Users/bpstr/Github/edit-ac/core/fixtures/replica-seeds/list-arrival");let seed=fs::read(root.join("seed.bin")).unwrap();
 let cp=InitializedCheckpoint{identity:identity(),initialized:true,writer_id:11,bytes:seed};let mut d=Document::restore(&identity(),&cp,&[]).unwrap();let updates=(0..16).map(|i|ReplayUpdate{identity:identity(),bytes:fs::read(root.join(format!("update-{i:03}.bin"))).unwrap()}).collect::<Vec<_>>();
 let mut pending=BTreeSet::new();
 for arrival in [10,6,15,3,13,8,4,12,7,0,5,2,1,11,14,9]{pending.insert(arrival);loop{let mut progress=false;for i in pending.iter().copied().collect::<Vec<_>>(){match d.apply_replay(&updates[i]){Ok(())=>{pending.remove(&i);progress=true;},Err(DocumentError::IncompleteRestore)=>{},Err(e)=>{
 println!("arrival={arrival} pending={i} error={e:?}");let old=m::replica(39901);m::apply(&old,&d.checkpoint().bytes).unwrap();let after=m::replica(39902);m::apply(&after,&d.checkpoint().bytes).unwrap();m::apply(&after,&updates[i].bytes).unwrap();println!("project-old={:?} project-after={:?}",m::project(&old).err(),m::project(&after).err());
 let a=old.transact();let b=after.transact();for root in [0,2,3,5,6]{for (key,v) in a.get_map(m::ROOTS[root]).unwrap().iter(&a){if b.get_map(m::ROOTS[root]).unwrap().get(&b,key)!=Some(v.clone()){println!("changed immutable {root} {key}: {v:?} -> {:?}",b.get_map(m::ROOTS[root]).unwrap().get(&b,key));}}}
 println!("pending-after={} ",b.store().pending_update().is_some()||b.store().pending_ds().is_some());fs::write("/Users/bpstr/Github/edit-ac/architecture/evidence/engine-replica-properties/list-rejected-checkpoint.bin",d.checkpoint().bytes).unwrap();return;}}}if !progress{break;}}}
}

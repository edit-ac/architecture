//! WEB-1.14: independent content, stable-caret and selective-history oracles.
use editac_core::{
    Utf16Offset as U,
    anchors::{Bias, Resolution},
    commands::{editor::*, format::*, text::*},
    document::{BlockAttributes, CreationPermit, Document, DocumentIdentity, InitialNode},
    history::HistoryConfig,
    patches::PatchScope,
};
use std::{
    cell::RefCell,
    rc::Rc,
    sync::atomic::{AtomicU64, Ordering},
};
use yrs::Any;

fn origin() -> TextOrigin {
    TextOrigin::new("heading-end:explicit").unwrap()
}
fn edit(d: &mut Document, commands: &[EditorCommand]) {
    let plan = d.prepare_editor(commands, &origin()).unwrap();
    d.commit_editor(plan).unwrap();
}
fn engine(texts: &[&str]) -> Document {
    static NEXT: AtomicU64 = AtomicU64::new(1);
    let suffix = NEXT.fetch_add(1, Ordering::Relaxed);
    let identity = DocumentIdentity::v5(
        format!("91000000-0000-4000-8000-{suffix:012}"),
        format!("92000000-0000-4000-8000-{suffix:012}"),
    )
    .unwrap();
    let mut d = Document::create(
        CreationPermit::authorize_new(identity).unwrap(),
        &texts
            .iter()
            .map(|s| InitialNode {
                kind: "block".into(),
                text: (*s).into(),
            })
            .collect::<Vec<_>>(),
    )
    .unwrap();
    let id = blocks(&d)[0].id.clone();
    edit(
        &mut d,
        &[EditorCommand::Block {
            target: id.clone(),
            tuple: Any::Array(vec![Any::from("heading"), Any::from(3u32)].into()),
        }],
    );
    if !texts[0].is_empty() {
        let selection = d
            .selection(
                (&id, U(0), Bias::Left),
                (&id, U(texts[0].encode_utf16().count() as u32), Bias::Right),
            )
            .unwrap();
        let p = d
            .prepare_format(
                &[FormatCommand {
                    selection,
                    mark: Mark::Bold,
                    action: FormatAction::Apply,
                    href: None,
                }],
                &origin(),
            )
            .unwrap();
        d.commit_format(p).unwrap();
    }
    d.enable_history(HistoryConfig::default()).unwrap();
    d
}
fn blocks(d: &Document) -> Vec<editac_core::projection::ProjectedNode> {
    d.snapshot()
        .unwrap()
        .visible
        .into_iter()
        .filter(|n| n.kind == "block")
        .map(|n| (*n).clone())
        .collect()
}
fn text(n: &editac_core::projection::ProjectedNode) -> String {
    n.runs.iter().map(|r| r.text.as_str()).collect()
}
fn heading(d: &Document, offset: u32) -> EditorCommand {
    let id = blocks(d)[0].id.clone();
    EditorCommand::HeadingEnd {
        owner: id.clone(),
        at: d.anchor(&id, U(offset), Bias::Right).unwrap(),
    }
}
fn frozen(d: &Document) -> (Vec<u8>, Vec<u8>, u64, editac_core::history::HistoryState) {
    (
        d.checkpoint().bytes,
        d.state_vector_v1(),
        d.revision(),
        d.history_state(),
    )
}
fn reject(d: &mut Document, commands: &[EditorCommand]) {
    let events = Rc::new(RefCell::new(0));
    let count = events.clone();
    let _sub = d
        .subscribe(PatchScope::All, move |_, _| {
            *count.borrow_mut() += 1;
            Ok(())
        })
        .unwrap();
    let old = frozen(d);
    assert!(d.can_editor(commands, &origin()).is_err());
    assert!(d.prepare_editor(commands, &origin()).is_err());
    assert_eq!(frozen(d), old);
    assert_eq!(*events.borrow(), 0);
}

#[test]
fn heading_end_preserves_heading_marks_and_one_update_history_with_stable_utf16_caret() {
    let mut d = engine(&["A😀Z", "untouched"]);
    let before = blocks(&d);
    let cmd = heading(&d, 4);
    let EditorCommand::HeadingEnd { at, .. } = &cmd else {
        unreachable!()
    };
    let at = at.clone();
    let events = Rc::new(RefCell::new(Vec::new()));
    let count = events.clone();
    let _sub = d
        .subscribe(PatchScope::Updates, move |_, p| {
            count.borrow_mut().push(p.clone());
            Ok(())
        })
        .unwrap();
    let old = frozen(&d);
    d.can_editor(std::slice::from_ref(&cmd), &origin()).unwrap();
    let plan = d.prepare_editor(&[cmd], &origin()).unwrap();
    assert_eq!(frozen(&d), old);
    assert!(events.borrow().is_empty());
    let commit = d.commit_editor(plan).unwrap();
    let after = blocks(&d);
    assert_eq!(after.len(), 3);
    assert_eq!(after[0].id, before[0].id);
    assert_eq!(after[0].parent, before[0].parent);
    assert_eq!(after[0].block_attributes, Some(BlockAttributes::Heading(3)));
    assert_eq!(after[0].runs, before[0].runs);
    assert_eq!(after[2].runs, before[1].runs);
    assert_eq!(after[2].id, before[1].id);
    assert_eq!(after[1].block_attributes, Some(BlockAttributes::Paragraph));
    assert_eq!(after[1].parent, after[0].parent);
    assert_eq!(text(&after[1]), "");
    assert!(
        matches!(d.resolve_anchor(&at).unwrap(), Resolution::Position(p) if p.node == after[1].id && p.offset == U(0))
    );
    assert_eq!(d.history_state().undo_groups, 1);
    assert_eq!(d.revision(), old.2 + 1);
    let events = events.borrow();
    assert_eq!(events.len(), 1);
    assert_eq!(
        events[0].update.as_ref().unwrap().bytes,
        commit.update.bytes
    );
}

#[test]
fn heading_end_selected_suffix_replacement_is_one_prepared_batch() {
    let mut d = engine(&["A😀Z", "keep"]);
    let id = blocks(&d)[0].id.clone();
    let selection = d
        .selection((&id, U(1), Bias::Left), (&id, U(4), Bias::Right))
        .unwrap();
    let at = d.anchor(&id, U(1), Bias::Right).unwrap();
    edit(
        &mut d,
        &[
            EditorCommand::Text(TextCommand::Delete { selection }),
            EditorCommand::HeadingEnd {
                owner: id.clone(),
                at: at.clone(),
            },
        ],
    );
    let b = blocks(&d);
    assert_eq!(b.iter().map(text).collect::<Vec<_>>(), ["A", "", "keep"]);
    assert_eq!(b[0].block_attributes, Some(BlockAttributes::Heading(3)));
    assert!(
        b[0].runs
            .iter()
            .all(|r| r.attributes.get("bold") == Some(&Any::Bool(true)))
    );
    assert!(
        matches!(d.resolve_anchor(&at).unwrap(), Resolution::Position(p) if p.node == b[1].id && p.offset == U(0))
    );
    assert_eq!(d.history_state().undo_groups, 1);
    d.undo().unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "keep"]
    );
    d.redo().unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A", "", "keep"]
    );
}

#[test]
fn heading_end_cross_block_selected_replacement_stages_deletions_join_and_destination() {
    let mut d = engine(&["A😀Z", "remove", "peer"]);
    let b = blocks(&d);
    let at = d.anchor(&b[0].id, U(1), Bias::Right).unwrap();
    let a_range = d
        .selection((&b[0].id, U(1), Bias::Left), (&b[0].id, U(4), Bias::Right))
        .unwrap();
    let b_range = d
        .selection((&b[1].id, U(0), Bias::Left), (&b[1].id, U(6), Bias::Right))
        .unwrap();
    edit(
        &mut d,
        &[
            EditorCommand::Text(TextCommand::Delete { selection: a_range }),
            EditorCommand::Text(TextCommand::Delete { selection: b_range }),
            EditorCommand::Join {
                first: b[0].id.clone(),
                second: b[1].id.clone(),
            },
            EditorCommand::HeadingEnd {
                owner: b[0].id.clone(),
                at: at.clone(),
            },
        ],
    );
    let result = blocks(&d);
    assert_eq!(
        result.iter().map(text).collect::<Vec<_>>(),
        ["A", "", "peer"]
    );
    assert_eq!(result[0].id, b[0].id);
    assert_eq!(
        result[0].block_attributes,
        Some(BlockAttributes::Heading(3))
    );
    assert_eq!(result[1].block_attributes, Some(BlockAttributes::Paragraph));
    assert!(
        matches!(d.resolve_anchor(&at).unwrap(), Resolution::Position(p) if p.node == result[1].id && p.offset == U(0))
    );
    assert_eq!(d.history_state().undo_groups, 1);
    d.undo().unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "remove", "peer"]
    );
    d.redo().unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A", "", "peer"]
    );
}

#[test]
fn heading_end_ineligible_targets_and_resource_rejection_are_atomic() {
    let mut d = engine(&["A😀Z", "paragraph"]);
    for offset in [0, 1, 3] {
        let cmd = heading(&d, offset);
        reject(&mut d, &[cmd]);
    }
    let b = blocks(&d);
    let at = d.anchor(&b[1].id, U(9), Bias::Right).unwrap();
    reject(
        &mut d,
        &[EditorCommand::HeadingEnd {
            owner: b[1].id.clone(),
            at,
        }],
    );
    let at = d.anchor(&b[0].id, U(4), Bias::Right).unwrap();
    reject(
        &mut d,
        &[EditorCommand::HeadingEnd {
            owner: "missing".into(),
            at: at.clone(),
        }],
    );
    let cmd = heading(&d, 4);
    reject(&mut d, &vec![cmd; 4097]);
    let mut empty = engine(&[""]);
    let cmd = heading(&empty, 0);
    reject(&mut empty, &[cmd]);
}

#[test]
fn heading_end_later_invalid_command_rolls_back_entire_preparation() {
    let mut d = engine(&["A😀Z"]);
    let cmd = heading(&d, 4);
    reject(
        &mut d,
        &[
            cmd,
            EditorCommand::Join {
                first: "missing".into(),
                second: "missing".into(),
            },
        ],
    );
    let b = blocks(&d);
    let selection = d
        .selection((&b[0].id, U(0), Bias::Left), (&b[0].id, U(4), Bias::Right))
        .unwrap();
    let cmd = heading(&d, 4);
    reject(
        &mut d,
        &[EditorCommand::Text(TextCommand::Delete { selection }), cmd],
    );
}

#[test]
fn heading_end_stale_and_wrong_replica_plans_are_silent() {
    let mut d = engine(&["A😀Z", "peer"]);
    let cmd = heading(&d, 4);
    let plan = d.prepare_editor(&[cmd], &origin()).unwrap();
    let b = blocks(&d);
    let at = d.anchor(&b[1].id, U(0), Bias::Right).unwrap();
    edit(
        &mut d,
        &[EditorCommand::Text(TextCommand::Insert {
            at,
            text: "R".into(),
        })],
    );
    let before = frozen(&d);
    assert!(d.commit_editor(plan).is_err());
    assert_eq!(frozen(&d), before);
    let plan = d.prepare_editor(&[heading(&d, 4)], &origin()).unwrap();
    let mut peer = Document::restore(d.identity(), &d.checkpoint(), &[]).unwrap();
    let before = frozen(&peer);
    assert!(peer.commit_editor(plan).is_err());
    assert_eq!(frozen(&peer), before);
}

#[test]
fn heading_end_undo_redo_preserves_unrelated_remote_text_and_peer_convergence() {
    let mut d = engine(&["A😀Z", "peer"]);
    let b = blocks(&d);
    let mut peer = Document::restore(d.identity(), &d.checkpoint(), &[]).unwrap();
    let at = peer.anchor(&b[1].id, U(4), Bias::Right).unwrap();
    let plan = peer
        .prepare_text(
            &TextCommand::Insert {
                at,
                text: "R".into(),
            },
            &origin(),
        )
        .unwrap();
    let remote = peer.commit_text(plan).unwrap().update.unwrap();
    let cmd = heading(&d, 4);
    edit(&mut d, &[cmd]);
    peer.apply_replay(&editac_core::document::ReplayUpdate {
        identity: d.identity().clone(),
        bytes: d.update_v1(&peer.state_vector_v1()).unwrap(),
    })
    .unwrap();
    d.apply_replay(&remote).unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "", "peerR"]
    );
    assert_eq!(d.history_state().undo_groups, 1);
    let undo = d.undo().unwrap().unwrap();
    peer.apply_replay(&undo.update.unwrap()).unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "peerR"]
    );
    assert_eq!(
        blocks(&peer).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "peerR"]
    );
    assert_eq!(
        blocks(&d)[0].block_attributes,
        Some(BlockAttributes::Heading(3))
    );
    let redo = d.redo().unwrap().unwrap();
    peer.apply_replay(&redo.update.unwrap()).unwrap();
    assert_eq!(
        blocks(&d).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "", "peerR"]
    );
    assert_eq!(
        blocks(&peer).iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "", "peerR"]
    );
    assert_eq!(
        blocks(&peer)[1].block_attributes,
        Some(BlockAttributes::Paragraph)
    );
}

#[test]
fn heading_end_under_quote_keeps_parent_and_does_not_change_context_commands() {
    use editac_core::commands::lists::{ContainerStyle, ListCommand};
    let mut d = engine(&["A😀Z", "peer"]);
    let id = blocks(&d)[0].id.clone();
    edit(
        &mut d,
        &[EditorCommand::List(ListCommand::Wrap {
            targets: vec![id],
            style: ContainerStyle::Quote,
        })],
    );
    d.clear_history();
    let before = blocks(&d);
    let cmd = heading(&d, 4);
    edit(&mut d, &[cmd]);
    let b = blocks(&d);
    assert_eq!(b[0].parent, before[0].parent);
    assert_eq!(b[1].parent, before[0].parent);
    assert_eq!(b[0].runs, before[0].runs);
    assert_eq!(b[1].block_attributes, Some(BlockAttributes::Paragraph));
    assert_eq!(d.history_state().undo_groups, 1);
}

#[test]
fn heading_end_deleted_stable_target_is_rejected_without_redirect() {
    let mut d = engine(&["A😀Z", "peer"]);
    let cmd = heading(&d, 4);
    let id = blocks(&d)[0].id.clone();
    edit(
        &mut d,
        &[EditorCommand::Enable {
            target: id,
            enabled: false,
        }],
    );
    reject(&mut d, &[cmd]);
    assert_eq!(blocks(&d).iter().map(text).collect::<Vec<_>>(), ["peer"]);
}

#[test]
fn heading_end_caret_identifies_new_paragraph_before_existing_shared_source_sibling() {
    let mut d = engine(&["A😀Ztail", "peer"]);
    let owner = blocks(&d)[0].id.clone();
    let cut = d.anchor(&owner, U(4), Bias::Right).unwrap();
    edit(
        &mut d,
        &[EditorCommand::Split {
            owner: owner.clone(),
            at: cut.clone(),
        }],
    );
    let Resolution::Position(sibling) = d.resolve_anchor(&cut).unwrap() else {
        panic!()
    };
    edit(
        &mut d,
        &[EditorCommand::Block {
            target: sibling.node,
            tuple: Any::Array(vec![Any::from("paragraph")].into()),
        }],
    );
    d.clear_history();
    let cmd = heading(&d, 4);
    let EditorCommand::HeadingEnd { at, .. } = &cmd else {
        unreachable!()
    };
    let at = at.clone();
    edit(&mut d, &[cmd]);
    let b = blocks(&d);
    assert_eq!(
        b.iter().map(text).collect::<Vec<_>>(),
        ["A😀Z", "", "tail", "peer"]
    );
    assert_eq!(b[1].block_attributes, Some(BlockAttributes::Paragraph));
    assert!(
        matches!(d.resolve_anchor(&at).unwrap(), Resolution::Position(p) if p.node == b[1].id && p.offset == U(0)),
        "heading-end cut must identify the new paragraph, not its shared-source sibling"
    );
}

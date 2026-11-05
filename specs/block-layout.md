# Block indentation in the current document

User decision, 2026-10-24: ordinary paragraph Tab increases block indentation;
Shift+Tab decreases it. The visible Indent/Outdent actions use the same semantic
operation. They do not insert whitespace or change paragraph/heading kinds.
Escape then Tab/Shift+Tab exits the editor; read-only surfaces retain native
focus traversal. Lists retain structural nesting, code retains literal line
indentation, and tables retain cell navigation.

An inapplicable list indentation (first item or nesting bound) is a handled
no-op that keeps editor focus. Escape-Tab remains available; a rejected structural
change must not turn an ordinary indentation key into unintended focus traversal.

The single current pre-publication layout gains the optional Map root
`registry-block-layout`. Its keys are admitted original/derived text-owner IDs;
each value is the exact atomic tuple `["indent", level]`, where level is an
integer 0 through 8. Absence means zero. Malformed tuples, non-finite/fractional
levels, out-of-range levels and dangling/non-text-owner keys reject before live
mutation. Existing same-format documents without layout entries remain valid;
no envelope relabel, conversion, reset or older reader is involved.

Indentation is independent of block type, runs, source spans, table content,
placement and checklist state. Different owners merge independently; concurrent
assignments to the same owner's layout follow the existing Y.Map conflict rule.
Only layout changes; unknown content is retained without interpretation or
execution. The ordinary layout command may address admitted block owners without
editing their opaque data. No new runtime compatibility profile is introduced.

Local prepared commands validate their entire batch, bounds and ownership before
mutation. A range adjusts each touched block once and keeps its direction/caret.
Level-zero outdent and the maximum-level indent are handled no-ops, with no
history group, journal update or focus movement. Split/Enter inherits the source
owner's captured level for its new sibling. Join retains the first owner's level
and keeps the absorbed owner's entry dormant for undo. Moves and block-kind
changes preserve layout. Selective undo/redo and checkpoint/journal reopen retain
the actual level and original identities; transient CSS is never storage.

Projection exposes positive levels as optional `editor.indent`; absent means
zero. Web rendering derives logical inline-start indentation from that value,
using an overridable `--editac-indent-step` (default 1.5em), including RTL. Host
UI libraries must call the shared commands rather than mutate DOM margins.

Required focused proof: paragraph/heading and selected-range keyboard/button
parity; zero/max no-ops; Escape-Tab and read-only traversal; unchanged text,
marks and owner IDs; split/join; undo/redo; real WASM/IndexedDB reopen; concurrent
distinct-owner preservation; and atomic malformed-layout rejection. Full native,
interchange/conversion fidelity and aggregate qualification remain their existing
owners' work; this amendment is not alpha or release acceptance.

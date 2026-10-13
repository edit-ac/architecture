# Markdown parser qualification

2026-10-12, local deterministic Rust qualification. Candidate pulldown-cmark
0.13.4 is admitted for `edit-ac-gfm-v1` with only TABLES, TASKLISTS and
STRIKETHROUGH enabled. CommonMark baseline uses Options::empty(). GFM callouts,
math, footnotes, metadata, superscript and definition lists remain disabled.

The downloaded CommonMark 0.31.2 corpus contains 652 official examples. All
grammar results pass; 22 byte-level HTML differences are preserved in the
initial log. The comparator permits quote/entity serialization and example
175's newline before a raw div in a list. It preserves code whitespace. This
is grammar qualification, not permission to install raw HTML in a document.

The versioned official cmark-gfm 0.29.0.gfm.13 specification supplies all 23
examples in the four required extension sections. All pass after documented
HTML renderer normalization: alignment attributes, structural table newlines,
empty tbody and checkbox attribute ordering/void spelling/adjacent whitespace.
The expected source/HTML corpus is preserved independently of implementation.

The candidate has no extended-autolink events. The portable bounded text-event
adapter fills that gap, with GFM URL/domain/email boundaries, punctuation,
parenthesis and entity-tail rules. Adjacent decoded text events are coalesced;
existing links/images/code remain excluded. Single-tilde strike is disabled to
retain the named 0.29 double-tilde rule. URL admission is still governed by core
policy: grammar recognition does not authorize FTP, relative or unsafe URLs.

Decision: retain this pinned parser plus the qualified event adapter. Production
mapping must use this profile, preserve unsupported source with diagnostics,
and validate through portable engine contracts before mutation. Gap owner:
FMT-1.3 for semantic mapping; FMT-1.6 for optional descriptors.

Command: `cargo test -p editac-markdown --test parser_profile --locked --offline`.
Final result: 6 tests executed/passed; 0 failed/ignored/skipped. Embedded corpus
assertions cover 652 baseline and 23 required-extension examples. Initial
failures and every retry remain under `markdown/parser-profile*.log`.
Sources: https://spec.commonmark.org/0.31.2/spec.json and
https://raw.githubusercontent.com/github/cmark-gfm/0.29.0.gfm.13/test/spec.txt.
This evidence establishes the parser boundary only, not semantic fidelity,
whole-pipeline cost, browser or physical-device support.

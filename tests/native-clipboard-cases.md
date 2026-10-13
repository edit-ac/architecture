# Planned native clipboard and formatting cases

Status: planned; no native tests or device runs executed by this roadmap revision.

IOS/AND/DSK/WIN/LNX-2.4 own simulator, emulator or OS-host execution of NCL-01–NCL-20. DEL-1.9/DEL-1.10 own physical-device and real-OS execution of NCL-01–NCL-28. NIX/NAX/NMX/NWX/NLX-1.9 own extension integration; unavailable optional extensions have explicit fallback expectations. Do not record a mock, injected callback, simulator or VM as a physical-device result.

Each future receipt records the case ID, environment class, device/virtual-device model, OS image/build, toolkit/SDK/package/codec revisions, keyboard/IME and accessibility versions, source/target app, actual clipboard flavors, menu/shortcut, semantic selection/content, undo/redo, update/journal counts and failure evidence. Use prepared data and mock network/provider transports. No paid inference, secret loading or fixture recording from providers.

## Transfer matrix — IOS-2.4, AND-2.4, DSK-2.4, WIN-2.4, LNX-2.4, DEL-1.9, DEL-1.10

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| NCL-01 | P0 | Native Copy/Paste menus between two SDK editors; no key event | Correct original target, supported semantics and one paste history/update group |
| NCL-02 | P0 | Copy a cross-block forward and backward selection | Order, endpoint clipping, headings, paragraphs, Unicode and all admitted inline marks preserved |
| NCL-03 | P0 | Cut with successful, throwing, silently refused and canceled OS clipboard writes | Delete only after successful required flavor transfer; failures preserve content, history and storage |
| NCL-04 | P0 | Paste internal fragment, explicit Markdown, HTML/RTF and plain text from one offer | Declared precedence and codec capability used once; unsupported flavor retains source/diagnostics |
| NCL-05 | P0 | Invoke Paste without formatting from reachable native menu/toolbar | All rich codecs bypassed; whitespace/newlines/Unicode literal under target policy |
| NCL-06 | P0 | Ctrl+Shift+V on Windows/Linux and Command+Shift+V or Command+Option+Shift+V on macOS/iOS hardware keyboard | Advertised platform shortcut routes to the same literal command; ordinary paste remains formatted; unsupported OS binding documented |
| NCL-07 | P0 | Paste rich HTML/Markdown/internal data into code and inline-code contexts | Literal text; no syntax transformation, formatting injection or executable content |
| NCL-08 | P0 | Native paste callback followed by OS text replacement notifications; repeat identical payload intentionally | One commit per actual user intent; callbacks deduplicated without suppressing the second paste |
| NCL-09 | P0 | Soft-keyboard/native-menu replacement with no keyboard event and different callback order | Selection captured before replacement; one prepared edit and correct result caret |
| NCL-10 | P0 | Invalid version/schema, malformed data, oversized/deep hierarchy and surrogate-interior selection | Safe bounded rejection/fallback; no partial edits, arbitrary loads or hidden source loss |
| NCL-11 | P0 | Script/HTML handler, unsafe URL, CSS, RTF object, file reference and clipboard promise attack data | No code/formula execution or implicit resource access; safe text/source retained with diagnostics |
| NCL-12 | P0 | Delayed OS provider; move selection, edit remotely or delete the original target before completion | Stable initiating target/session revalidated; later selection preserved; deleted target rejects atomically |
| NCL-13 | P0 | Permission denied, native clipboard unavailable, expired activation or empty flavors | Accessible explanation/fallback; no selection deletion or repeated permission prompts |
| NCL-14 | P0 | Read-only transition, active IME composition, backgrounding or disposal during delayed paste | Declared composition policy and cancellation apply; no late mutation/history/journal update |
| NCL-15 | P0 | Undo and redo multi-block formatted paste and cut/paste separately | Each transfer is one history group; formatting, structure and caret restore predictably |
| NCL-16 | P0 | Copy nested numbered/check lists and quotes across editors | Admitted hierarchy, numbering, checked state and formatting round-trip; unsupported structure remains explicit |
| NCL-17 | P0 | Two views of one document and two different documents; close source editor during delayed transfer | Provider lifetime and scoped ownership preserved; no cross-document insertion or teardown |
| NCL-18 | P0 | Paste formatted text into selected rich content with emoji, RTL and combined accents | Valid UTF-16/grapheme boundaries, direction and surrounding content preserved |
| NCL-19 | P0 | Copy images/captions, references, math and unknown extension with codec present/absent | Admitted format/source preserved; host asset authority enforced; fallback is explicit and inert |
| NCL-20 | P0 | Copy table cells with bold/italic/underline/strike/code/links/headings plus rows, columns and spans | Registered table codec preserves formatting and admitted structure; plain paste is literal; one atomic undo group |
| NCL-21 | P0 | Physical iPhone/iPad long-press Copy/Cut/Paste with selection handles and keyboard open | Real OS pasteboard and native menu flow verified; no synthetic-event substitution |
| NCL-22 | P0 | Physical Android devices with stock and supported vendor keyboards; toolbar/system paste menu | Real clipboard overlay/replacement callbacks qualified for each claimed keyboard/OS profile |
| NCL-23 | P0 | Physical mobile device plus hardware keyboard; formatted and plain paste shortcuts | Advertised shortcuts, target/focus and keyboard policy verified on each claimed device |
| NCL-24 | P0 | Physical device cross-app transfer to/from a browser, word processor and native notes app | Actual offered flavors and resulting semantic formatting recorded; loss or unsupported formats explicit |
| NCL-25 | P0 | VoiceOver/TalkBack/Narrator or declared desktop screen reader invokes Copy/Cut/Paste/plain paste | Named accessible actions and correct selection/result; manual assistive-input evidence retained |
| NCL-26 | P0 | Physical OS privacy prompts, managed clipboard restriction, focus change, share sheet and background/foreground | Permission, activation, lifetime and cancellation behavior verified without fabricated support claims |
| NCL-27 | P0 | Real macOS/Windows and Linux X11/Wayland installations; copy then exit source app | Declared clipboard/PRIMARY lifetime survives or fails as documented; no dangling provider or data loss |
| NCL-28 | P0 | Physical device pasted table/extension content, undo, app restart and offline recovery | Admitted formatting/structure and durable local state preserved; unknown/absent extension source recoverable |

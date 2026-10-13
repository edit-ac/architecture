# Assistive input and alternative editing research

Research date: 2026-10-11. Scope: primary standards, platform documentation and
public upstream regression reports for native dictation, alternative formatting,
keyboard operation, screen readers, IME and bidirectional text. This is planning
evidence, not executed compatibility or accessibility qualification.

## Baseline and extension boundary

The existing [browser input contract](../specs/web.md) already requires input
reconciliation, composition ownership, normal document semantics and actual OS
IME evidence. The [native parity contract](../specs/native-sdk-parity.md) assigns
platform input and accessibility to native adapters. The
[extension contract](../specs/extension-library.md) already requires accessible
presenters and one shared command/history path. Preserve these as mandatory
baseline behavior when an optional assistance package is absent or disabled.

The recommended extension scope is additional discoverability and presentation:
an accessible command search, named formatting controls, selection tools,
optional host-owned speech UI and configurable interaction preferences. It must
not supply a second document model, a separate formatting engine, substitute
accessibility for missing core semantics, or become a prerequisite for OS-native
dictation. The engine receives validated semantic edits and stable anchors;
microphone state, recognition services and OS accessibility APIs stay in hosts.

## Native speech and browser input

W3C Input Events Level 2 describes speech, keyboard and IME as ways of expressing
editing intentions. Its published table does not define an
`insertFromDictation` input type. It defines replacement and composition
operations, target ranges and cancellation rules; the document remains a Working
Draft with implementation testing in progress. Do not treat it as proof of
identical browser event sequences. [Input Events Level 2](https://www.w3.org/TR/input-events-2/)

MDN documents that `beforeinput` can be absent or non-cancelable for changes such
as IME, spelling correction and autocomplete. Consequently, successful editing
cannot depend only on canceling `beforeinput`, or on observing keyboard events.
Retain the existing `input` and bounded DOM-reconciliation path and prevent
double commits when both paths observe the same edit.
[MDN beforeinput](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event)

Native dictation should enter through the host's ordinary text-input adapter.
It can replace existing text or deliver a phrase at once. Preserve formatting,
selection, paragraph boundaries, anchor mapping and documented undo grouping.
Do not infer speech provenance from an event type or assume each phrase is a
single keypress. Composition ownership and cancellation rules must also cover
dictation or correction sequences that use composition on a qualified platform.

Apple distinguishes Dictation from Voice Control: Voice Control provides
navigation and editing commands as well as text entry, and takes over dictation
when enabled. Formatting, punctuation and language support are OS features, not
commands that edit.ac should universally reinterpret in arbitrary text.
[Apple Dictation commands](https://support.apple.com/en-gb/guide/mac-help/mh40695/26/mac/26),
[Apple Dictation](https://support.apple.com/en-gb/guide/mac-help/mh40584/26/mac/26)

Native does not imply offline. Microsoft documents Windows voice typing as
online speech recognition, while Windows Voice Access can author text and
operate the PC without an internet connection. Platform help and any product
privacy claims must distinguish these mechanisms. No new edit.ac speech
provider, API key or paid service is required by this proposal.
[Windows voice typing](https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc),
[Windows Voice Access FAQ](https://support.microsoft.com/en-us/accessibility/windows/voice-access/voice-access-frequently-asked-questions-faqs)

Android's native `InputConnection` explicitly supports committed text,
composing-region replacement, selection and correction callbacks. A native
adapter must honor those platform contracts through its existing integration;
capturing hardware key events cannot stand in for input-method support.
[Android InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection)

Browser `SpeechRecognition` is a separate app-controlled service. MDN marks it
limited availability and notes that some browser implementations send audio to a
server. Do not activate it as an automatic fallback when native dictation is
unavailable, or label it offline without qualifying the actual configuration.
[MDN SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)

If a later host supplies optional speech transport, the contract should expose
explicit start/stop/cancel, permission and availability states, request identity,
interim versus final results, locale and declared processing location. Interim
results must follow a defined provisional-text policy rather than generate
independent committed history entries. Late results after cancellation,
permission revocation, disposal or a superseded session must have no effect.
An asynchronously recognized result must not be redirected to the current caret
when its original target has disappeared. Keep recoverable text available to
the user and require an explicit destination before applying it elsewhere.

## Keyboard, voice activation and formatting routes

Every editing action needs an operable route without slash syntax or dragging.
Route the toolbar, command search, context actions and shortcuts through the same
prepared command and applicability state. Preserve the selection when entering
controls; after a completed or canceled command, restore an appropriate editor
position without stealing focus from a user's subsequent action. Respect
read-only state consistently. Plain-text/source mode can be a useful additional
route, but it must not excuse inaccessible rich editing or silently discard
unsupported structure when changing modes.

Visible control labels should occur in their accessible names so voice-control
users can activate what they see. Prefer stable, concise names for actions such
as Bold, Heading, Insert link and Move block up. This follows WCAG's label-in-name
guidance. Avoid global printable-character shortcuts; when provided, they need
the criterion's disable/remap/focus-scoping behavior. Dictated words can otherwise
trigger unintended single-character commands.
[WCAG 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html),
[WCAG 2.1.4](https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html)

Slash UI requires an explicit interaction model. The APG combobox pattern is a
value-entry widget with a popup; it is not a generic role for an entire rich
document. Recommended design choices are a separately named command-search
input with a listbox, or a named menu button for a command menu. If inline slash
suggestions remain, document their actual accessible roles and keyboard/focus
model and qualify them with real assistive technology. Do not add combobox
attributes to the document merely because a popup exists.
[APG Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/),
[APG Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)

For a search combobox/listbox, DOM focus stays in the search input while
`aria-activedescendant` identifies the active option; expanded, controls and
selection state must agree with visible state. Escape closes without applying a
command. Browser text-editing keys must keep working. A modal command dialog has
its own dialog focus behavior and must restore focus on close. These are
alternative models, not attributes to combine indiscriminately.
[APG Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/),
[APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

A toolbar can use one tab stop with arrow navigation among its controls. Keep a
visible focus indicator and prevent sticky formatting panels or suggestions from
entirely obscuring a focused control. Announce relevant asynchronous states such
as an unavailable command or canceled recognition request without moving focus;
avoid making the entire document a live region or announcing each interim
character. Reordering also needs a single-pointer alternative to dragging,
alongside keyboard operation.
[APG Toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/),
[WCAG Focus Not Obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html),
[WCAG Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html),
[WCAG Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)

## Bidirectional text and input methods

W3C internationalization guidance uses semantic `dir` markup for base direction,
logical layout properties and direction isolation for inserted text. `dir=auto`
is useful when content direction is unknown; `bdi` or equivalent direction
isolation prevents labels and user-supplied fragments from affecting surrounding
text. Do not reverse stored text or equate right alignment with RTL semantics.
[Structural direction](https://www.w3.org/International/questions/qa-html-dir),
[Inline bidi examples](https://www.w3.org/International/articles/inline-bidi-markup/bidi_examples.en)

Architecture consequence: distinguish logical document offsets and anchor/focus
direction from visual caret movement. Let the qualified platform input layer
handle visual movement; project its resulting selection to core coordinates.
Alternative formatting UI must preserve mixed Arabic/Hebrew and Latin content,
digits, punctuation, link labels, combining characters and emoji. It must not
consume candidate-navigation arrows, Enter or Escape while an IME owns them.

## Regression evidence from upstream editors

These reports identify failure modes worth testing. They do not establish a
present defect in edit.ac or a current supported/unsupported verdict for an
upstream editor.

- Lexical issue 4801 reports iOS autocorrection dropping bold/italic formatting
  in version 0.11.2; the issue is closed. Include native correction of formatted
  text and verify both resulting text and mark retention.
  [Lexical 4801](https://github.com/facebook/lexical/issues/4801)
- Lexical issue 4326 reports composition replacement over a larger selection
  producing empty content. Include replacement spanning blocks, canceled and
  committed composition, and undo restoration. The reporter's hypothesis about
  internal mutation handling is not treated as established root cause.
  [Lexical 4326](https://github.com/facebook/lexical/issues/4326)

## Deterministic checks and manual qualification

Automated fixtures establish adapter and command behavior under their prepared
inputs. Accessibility-tree snapshots and automated rules can identify structural
problems. None prove what an actual screen reader speaks, native dictation
produces, an IME commits or a user can complete. W3C explicitly says automated
tools cannot determine accessibility on their own.
[WAI evaluation guidance](https://www.w3.org/WAI/test-evaluate/tools/selecting/)

| Area | Deterministic acceptance cases | Actual platform qualification |
|---|---|---|
| Dictation and correction | Phrase insertion; selected-range replacement; newline/paragraph; punctuation; mark retention; one edit observed by multiple events commits once; bounded history; cancel; empty result | Dictate and correct actual text using the declared OS speech feature; verify cursor, formatting, undo and continued typing |
| Composition | Partial/final replacement fixtures; Japanese/Korean/Chinese candidate strings; dead keys; combining marks; emoji; selected multi-block replacement; no command execution during composition | Use actual OS input methods; change candidates; cancel and commit; test selected replacement and subsequent undo |
| Concurrent/lifecycle edits | Remote insertion before/inside/after target; target removal; read-only transition; blur; document switch; disposal; late result; duplicate result; canceled permission flow | Dictate while focus/lifecycle changes and while an actual second client edits; verify no lost text or insertion into an unrelated target |
| Command UI | Roles/names/states; active option; no-results; disabled command; keyboard open/navigate/activate/Escape; selection mapping; focus restore; toolbar roving focus; no remote-opened slash popup | Screen-reader navigation and announcements; voice activation by visible label; switch/keyboard-only use; candidate navigation while popup would otherwise be eligible |
| Formatting alternatives | Same prepared command and undo result from toolbar/search/shortcut; read-only denial; retained unsupported content in source round trips; explicit no-loss fallback | Apply and undo formatting with screen reader and voice-control users; move between text and controls without losing the intended range |
| RTL and selection | Logical offsets, anchor/focus orientation, grapheme boundaries, direction serialization and isolated labels | Mixed-direction caret/selection, word movement, replacement, copying and reading order on each declared host |
| Presentation | Focus states, contrast checks, zoom/reflow screenshots, reduced-motion preference, no transient-text live-region flooding | Magnification, high contrast/forced colors where available, touch target use, focus visibility with on-screen keyboards and overlays |

Use prepared text and fake transports for every automated recognition/provider
case, including permission errors, interim results, reorderings, retries and
timeouts. Do not record live fixtures, load `.secrets`, spend inference credits,
or send audio/content to providers. No tests, native speech sessions, provider
calls or assistive-technology qualification were executed during this research.

A release claim needs a declared matrix with exact app/browser, OS, hardware,
assistive-technology and input-language versions. Candidate rows include Safari
with VoiceOver and macOS Dictation/Voice Control; Windows browsers with NVDA and
Voice Access/voice typing; iOS VoiceOver and native Dictation; Android TalkBack and
the declared keyboard/voice input; Windows native accessibility and Linux Orca
with their actual native editors. These are proposed coverage rows, not current
support claims. TUI evidence must name its terminal and screen reader and cannot
be inherited from web or native GUI results. Native Windows, Linux and mobile
rows are gated by their own platform implementation and available equipment.

For each manual row record scenario, exact environment, expected result,
observed result, pass/fail/blocked state, evidence location and known limitation.
Missing equipment or an untested combination remains blocked or unqualified;
passing mocks must not convert it into a pass. Include people who use the
relevant assistive technology in usability validation when possible.

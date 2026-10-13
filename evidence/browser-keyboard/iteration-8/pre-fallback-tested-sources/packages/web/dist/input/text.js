import { KeyboardInput } from './keyboard.js';
import { CompositionInput } from './composition.js';
import { reconcileMutation } from './reconcile.js';
let editorSequence = 0;
const ordinary = new Set(['insertText', 'deleteContentBackward', 'deleteContentForward']);
/** Ordinary input adapter. Rust owns every committed edit; DOM text is read only
 * for a bounded native intent in one mapped text block. Unsupported mutations
 * retain explicit recovery text; composition and structural commands have separate owners.
 * Construct after renderer/selection and commit through attached local storage.
 */
export class TextInput {
    renderer;
    selection;
    engine;
    commit;
    intents = [];
    trace = [];
    recovery = [];
    scope;
    content = new Map();
    subscription;
    observer;
    events = new WeakMap();
    listeners = [];
    sequence = 0;
    generation = 1;
    disposed = false;
    readOnly = false;
    composition;
    keyboard;
    rendering = false;
    queued = false;
    key;
    pending;
    jobs = [];
    constructor(renderer, selection, engine, commit) {
        this.renderer = renderer;
        this.selection = selection;
        this.engine = engine;
        this.commit = commit;
        if (renderer.patchBoundary)
            throw new Error('Input owner already attached');
        const snapshot = engine.read();
        this.scope = `${snapshot.identity.documentId}/${snapshot.identity.epoch}/${++editorSequence}`;
        for (const node of snapshot.visible)
            this.content.set(node.id, node.runs.map(run => run.text).join(''));
        this.readOnly = renderer.root.contentEditable === 'false';
        this.subscription = engine.subscribe({ type: 'all' }, patch => {
            for (const change of patch.nodes) {
                if (change.type === 'visible')
                    this.content.set(change.node.id, change.node.runs.map(run => run.text).join(''));
                else
                    this.content.delete(change.type === 'removed' ? change.id : change.node.id);
            }
        });
        this.composition = new CompositionInput(renderer, selection, engine, {
            begin: () => {
                this.flushNative();
                const intent = this.key?.disposition === 'native-pending' ? this.key : this.pending?.disposition === 'native-pending' ? this.pending : this.create('composition');
                intent.origin = 'composition';
                this.pending = intent;
                return intent;
            },
            content: node => this.content.get(node),
            apply: (intent, range, text) => this.apply(intent, range, text),
            recovery: (intent, value) => this.recover(intent, value),
            drain: () => this.mutations(this.observer.takeRecords())
        });
        this.keyboard = new KeyboardInput(renderer, selection, engine, commit, () => this.readOnly || this.disposed || this.composition.active);
        this.observer = new MutationObserver(records => this.mutations(records));
        this.observer.observe(renderer.root, { subtree: true, childList: true, characterData: true });
        renderer.patchBoundary = {
            before: () => { this.mutations(this.observer.takeRecords()); this.rendering = true; },
            after: () => {
                const records = this.observer.takeRecords();
                if (records.length)
                    this.record({ type: 'renderer-echo', trusted: false, generation: this.generation, count: records.length });
                this.rendering = false;
            }
        };
        for (const type of ['keydown', 'keyup', 'beforeinput', 'input', 'compositionstart', 'compositionupdate', 'compositionend', 'blur']) {
            const listener = event => this.handle(event);
            this.listeners.push([type, listener]);
            renderer.root.addEventListener(type, listener);
        }
    }
    create(origin) {
        const intent = { id: `${this.scope}/${this.generation}/${++this.sequence}`, generation: this.generation, origin, disposition: 'native-pending' };
        this.intents.push(intent);
        if (this.intents.length > 128)
            this.intents.shift();
        return intent;
    }
    record(trace) { this.trace.push(trace); if (this.trace.length > 256)
        this.trace.shift(); }
    reject(intent, reason) { intent.disposition = 'rejected'; intent.reason = reason; }
    recover(intent, recovery) {
        this.reject(intent, recovery.reason);
        intent.text = recovery.text;
        this.recovery.push({ ...recovery, intent: intent.id, generation: intent.generation });
        if (this.recovery.length > 32)
            this.recovery.shift();
    }
    handle(event) {
        if (this.disposed)
            return;
        const input = event, key = event;
        const trace = { type: event.type, trusted: event.isTrusted, generation: this.generation, inputType: input.inputType, cancelable: event.cancelable };
        this.record(trace);
        const owned = this.events.get(event);
        if (owned) {
            trace.intent = owned.id;
            if (event.type === 'beforeinput' && event.cancelable && owned.disposition !== 'native-pending')
                event.preventDefault();
            return;
        }
        const compositionOwner = this.composition.handle(event, this.readOnly);
        if (compositionOwner) {
            if (event.type === 'compositionstart' || event.type === 'keydown' || event.type === 'beforeinput')
                this.keyboard.resetFocusEscape();
            this.events.set(event, compositionOwner);
            trace.intent = compositionOwner.id;
            // The composition lifecycle owns its final notifications and commit key.
            // Release ordinary routing references at its terminal boundary, even when
            // an IME does not deliver keyup, so later non-keyboard input is independent.
            if (event.type === 'keyup' || compositionOwner.disposition !== 'native-pending') {
                if (this.key === compositionOwner)
                    this.key = undefined;
            }
            if (compositionOwner.disposition !== 'native-pending' && this.pending === compositionOwner)
                this.pending = undefined;
            return;
        }
        if (input.isComposing || key.isComposing) {
            if (event.type === 'beforeinput') {
                const intent = this.key ?? this.create('beforeinput');
                this.pending = intent;
                this.events.set(event, intent);
                trace.intent = intent.id;
            }
            return;
        }
        if (event.type === 'keyup' || event.type === 'blur') {
            if (event.type === 'blur')
                this.keyboard.resetFocusEscape();
            this.flushNative();
            if (this.key?.disposition === 'native-pending')
                this.key.disposition = 'handled';
            this.key = undefined;
            this.pending = undefined;
            return;
        }
        const action = this.keyboard.action(event);
        if (action && (event.type === 'keydown' || event.type === 'beforeinput' && event.cancelable)) {
            this.flushNative();
            const intent = event.type === 'beforeinput' ? this.key ?? this.create('beforeinput') : this.create('key');
            const result = intent.disposition === 'native-pending' ? this.keyboard.execute(action, `keyboard:${intent.id}`) : { disposition: intent.disposition };
            if (result) {
                if (event.cancelable)
                    event.preventDefault();
                Object.assign(intent, result);
                this.events.set(event, intent);
                trace.intent = intent.id;
                if (event.type === 'keydown')
                    this.key = intent;
                this.pending = intent;
                return;
            }
            // Native deletion/Tab is not an editor command intent.
            intent.disposition = 'handled';
        }
        if (event.type === 'keydown') {
            this.flushNative();
            if (key.key.length === 1 || ['Backspace', 'Delete', 'Dead', 'Process', 'Unidentified'].includes(key.key)) {
                this.key = this.create('key');
                this.events.set(event, this.key);
                trace.intent = this.key.id;
            }
            return;
        }
        if (event.type === 'input') {
            this.flushNative();
            if (this.pending) {
                this.events.set(event, this.pending);
                trace.intent = this.pending.id;
            }
            return;
        }
        if (event.type !== 'beforeinput')
            return;
        this.flushNative();
        const intent = this.key ?? this.create('beforeinput');
        this.pending = intent;
        this.events.set(event, intent);
        trace.intent = intent.id;
        if (intent.disposition !== 'native-pending') {
            if (event.cancelable)
                event.preventDefault();
            return;
        }
        if (this.readOnly) {
            if (event.cancelable)
                event.preventDefault();
            this.reject(intent, 'read-only');
            return;
        }
        if (!ordinary.has(input.inputType) || !event.cancelable || (input.inputType === 'insertText' && input.data === null))
            return;
        const target = this.selection.retain();
        if (!target) {
            event.preventDefault();
            this.reject(intent, 'unmapped-selection');
            return;
        }
        let range = target.range, ownedRange;
        try {
            const a = this.engine.resolve(range.anchor), b = this.engine.resolve(range.focus);
            if (a.type !== 'position' || b.type !== 'position' || a.node !== b.node) {
                event.preventDefault();
                this.reject(intent, 'unsupported-ordinary-range');
                return;
            }
            if (input.inputType !== 'insertText' && a.offset === b.offset) {
                // Use the browser's actual deletion unit (grapheme/word policy), never a
                // guessed UTF-16 code unit. Engines without target ranges mutate natively.
                const ranges = input.getTargetRanges();
                const native = ranges.length === 1 ? ranges[0] : undefined;
                const start = native && this.selection.toModel(native.startContainer, native.startOffset, 'right');
                const end = native && this.selection.toModel(native.endContainer, native.endOffset, 'left');
                if (!start || !end || start.node !== a.node || end.node !== a.node || start.offset === end.offset)
                    return;
                const anchor = this.engine.anchor(start.node, start.offset, 'right');
                try {
                    ownedRange = { anchor, focus: this.engine.anchor(end.node, end.offset, 'left') };
                }
                catch (error) {
                    this.engine.releaseAnchor(anchor);
                    throw error;
                }
                range = ownedRange;
            }
            event.preventDefault();
            this.apply(intent, range, input.inputType === 'insertText' ? input.data : '');
        }
        catch (error) {
            event.preventDefault();
            this.reject(intent, error instanceof Error ? error.message : String(error));
        }
        finally {
            if (ownedRange)
                this.release(ownedRange);
            target.dispose();
        }
    }
    mutations(records) {
        if (!records.length || this.disposed || this.rendering)
            return;
        if (this.composition.active) {
            this.record({ type: 'composition-mutations', trusted: false, generation: this.generation, count: records.length, ...(this.composition.owner ? { intent: this.composition.owner.id } : {}) });
            return;
        }
        // A fresh native mutation is an owner even when there was no beforeinput.
        // Terminal prior owners cannot consume independent deliberate mutations.
        const intent = this.pending?.disposition === 'native-pending' ? this.pending : this.create('native');
        this.pending = intent;
        this.record({ type: 'native-mutations', trusted: false, generation: this.generation, count: records.length, intent: intent.id });
        const mutation = reconcileMutation(this.renderer, this.content, records);
        if (mutation.type === 'unsupported') {
            this.recover(intent, mutation.recovery);
            for (const node of mutation.nodes)
                this.renderer.resume(node);
            // Unknown/root structure cannot be reconstructed by a bounded block patch.
            // Stop editing and expose the recovery result for host remount/recovery.
            if (!mutation.recovery.node || mutation.recovery.reason === 'native-limit') {
                this.readOnly = true;
                this.renderer.setReadOnly(true);
                this.selection.clear();
                const native = this.renderer.root.ownerDocument.getSelection();
                // A detached mapped block can leave stale native endpoints. Clear only
                // this editor's selection; unrelated page selections remain untouched.
                if (native?.anchorNode && (this.renderer.root.contains(native.anchorNode) || this.renderer.getNodeId(native.anchorNode)))
                    native.removeAllRanges();
            }
            return;
        }
        if (mutation.type === 'unchanged') {
            intent.disposition = 'handled';
            this.renderer.resume(mutation.node);
            return;
        }
        if (this.readOnly) {
            this.recover(intent, { reason: 'read-only', node: mutation.node, text: mutation.captured, truncated: false });
            this.renderer.resume(mutation.node);
            return;
        }
        const { node, before, start, end, text, captured, caret } = mutation;
        const anchor = this.engine.anchor(node, start, 'right');
        let focus;
        try {
            focus = this.engine.anchor(node, end, 'left');
        }
        catch (error) {
            this.engine.releaseAnchor(anchor);
            throw error;
        }
        // If records arrive twice before dispatch, keep the final affected-block edit,
        // releasing the superseded preparation rather than committing intermediate DOM.
        const previous = this.jobs.findIndex(job => job.intent === intent);
        if (previous >= 0)
            this.release(this.jobs.splice(previous, 1)[0].range);
        this.jobs.push({ intent, node, before, range: { anchor, focus }, text, captured, ...(caret ? { caret } : {}) });
        if (!this.queued) {
            this.queued = true;
            const generation = this.generation;
            queueMicrotask(() => { this.queued = false; if (generation === this.generation)
                this.drain(); });
        }
    }
    flushNative() { this.mutations(this.observer.takeRecords()); this.drain(); }
    drain() {
        for (const job of this.jobs.splice(0)) {
            try {
                if (job.intent.disposition !== 'native-pending')
                    continue;
                if (this.content.get(job.node) !== job.before) {
                    this.recover(job.intent, { reason: 'native-baseline-changed', node: job.node, text: job.captured, truncated: false });
                    this.renderer.resume(job.node);
                    continue;
                }
                // Canonicalize only this block before engine patching; native wrappers
                // may have invalidated cached text nodes. Captured anchors remain valid.
                if (!job.caret)
                    this.selection.capture();
                this.renderer.resume(job.node);
                this.apply(job.intent, job.range, job.text, job.caret, false);
                if (job.intent.disposition === 'rejected') {
                    this.recover(job.intent, { reason: job.intent.reason ?? 'native-commit-failed', node: job.node, text: job.captured, truncated: false });
                    this.renderer.resume(job.node);
                }
            }
            finally {
                this.release(job.range);
            }
        }
    }
    apply(intent, range, text, nativeCaret, moveCaret = true) {
        if (this.disposed || intent.generation !== this.generation) {
            intent.disposition = 'disposed';
            return;
        }
        if (this.readOnly) {
            this.reject(intent, 'read-only');
            return;
        }
        const a = this.engine.resolve(range.anchor), b = this.engine.resolve(range.focus);
        if (a.type !== 'position' || b.type !== 'position' || a.node !== b.node) {
            this.reject(intent, 'stale-target');
            return;
        }
        if (a.offset === b.offset && !text) {
            intent.disposition = 'handled';
            return;
        }
        // The upper endpoint survives replacement; a start anchor attached to the
        // deleted selection can collapse to its beginning instead of the new end.
        const caretAnchor = this.engine.anchor(a.node, Math.max(a.offset, b.offset), 'right');
        try {
            this.engine.history({ type: 'explicit' });
            this.commit({ kind: 'text', origin: `text-input:${intent.id}`, command: { type: 'replace', range, text } });
            intent.disposition = 'committed';
            intent.text = text;
            const caret = this.engine.resolve(caretAnchor);
            if (nativeCaret) {
                const anchor = this.selection.toDOM({ node: a.node, offset: nativeCaret.anchor, bias: 'right' });
                const focus = this.selection.toDOM({ node: a.node, offset: nativeCaret.focus, bias: 'right' });
                if (anchor && focus)
                    this.renderer.root.ownerDocument.getSelection()?.setBaseAndExtent(anchor.node, anchor.offset, focus.node, focus.offset);
            }
            else if (moveCaret && caret.type === 'position') {
                const point = this.selection.toDOM({ ...caret, bias: 'right' });
                if (point)
                    this.renderer.root.ownerDocument.getSelection()?.setBaseAndExtent(point.node, point.offset, point.node, point.offset);
            }
            this.selection.capture();
        }
        catch (error) {
            this.reject(intent, error instanceof Error ? error.message : String(error));
            intent.text = text;
        }
        finally {
            this.engine.releaseAnchor(caretAnchor);
        }
    }
    release(range) { this.engine.releaseAnchor(range.anchor); this.engine.releaseAnchor(range.focus); }
    setReadOnly(value) {
        if (value) {
            const owner = this.composition.owner;
            this.composition.finish('readonly');
            // This terminal transition has no final event to release routing owners.
            if (this.key === owner)
                this.key = undefined;
            if (this.pending === owner)
                this.pending = undefined;
        }
        this.flushNative();
        this.readOnly = value;
        this.renderer.setReadOnly(value);
    }
    async settle() {
        const generation = this.generation;
        for (let turn = 0; turn < 8; turn++) {
            if (generation !== this.generation)
                return;
            this.flushNative();
            await Promise.resolve();
            if (!this.queued && !this.jobs.length)
                return;
        }
        throw new Error('Ordinary input did not settle in eight microtask turns');
    }
    dispose() {
        if (this.disposed)
            return;
        this.composition.finish('dispose');
        this.composition.dispose();
        this.keyboard.dispose();
        this.disposed = true;
        this.generation++;
        this.observer.disconnect();
        this.subscription.dispose();
        this.renderer.patchBoundary = undefined;
        this.renderer.setReadOnly(true);
        for (const [type, listener] of this.listeners)
            this.renderer.root.removeEventListener(type, listener);
        for (const job of this.jobs.splice(0)) {
            job.intent.disposition = 'disposed';
            this.release(job.range);
        }
        for (const intent of this.intents)
            if (intent.disposition === 'native-pending')
                intent.disposition = 'disposed';
        this.content.clear();
    }
}

import { recoverLocalDocument } from './entry.js';
import { bindEditorSurface, reserveEditorSurface } from './surface.js';
import { BrowserLifecycle, previewMatches } from './lifecycle.js';
const mounts = new WeakMap();
let editorSequence = 0;
/** Browser input owner. All editing begins after authoritative local recovery.
 * Hosts call destroy with flush policy before discarding their last replica. */
export class BrowserEditor {
    root;
    ready;
    lifecycle;
    status;
    plainButton;
    plainTarget;
    capturePlainTarget = (event) => {
        if (event.type === 'keydown' && event.key !== 'Tab')
            return;
        this.plainTarget?.dispose();
        this.plainTarget = this.selection?.retain();
        if (event.type === 'pointerdown')
            event.preventDefault();
    };
    plainClick = () => {
        const target = this.plainTarget;
        this.plainTarget = undefined;
        void this.plainPaste(undefined, target).catch(() => { });
    };
    session;
    renderer;
    selection;
    input;
    surface;
    releaseSurface;
    unsubscribe;
    closing = false;
    destroyed = false;
    destroyPromise;
    result;
    cancelActivation;
    readOnly;
    constructor(root, options) {
        this.root = root;
        if (mounts.has(root))
            throw Error('Editor already mounted on this surface');
        options.modules?.freeze();
        this.releaseSurface = reserveEditorSurface(root);
        mounts.set(root, this);
        const captured = { ...options, identity: { ...options.identity },
            ...(options.preview ? { preview: { identity: { ...options.preview.identity }, revision: options.preview.revision } } : {}) };
        this.readOnly = options.readOnly ?? false;
        this.lifecycle = new BrowserLifecycle(!!root.childNodes.length, this.readOnly);
        root.contentEditable = 'false';
        root.setAttribute('role', 'textbox');
        root.setAttribute('aria-multiline', 'true');
        root.setAttribute('aria-label', options.label ?? root.getAttribute('aria-label') ?? 'Document editor');
        root.setAttribute('aria-readonly', 'true');
        root.setAttribute('aria-busy', 'true');
        if (!root.hasAttribute('tabindex'))
            root.tabIndex = 0;
        this.status = root.ownerDocument.createElement('p');
        this.status.setAttribute('role', 'status');
        this.status.id = `editac-status-${++editorSequence}`;
        root.setAttribute('aria-describedby', [root.getAttribute('aria-describedby'), this.status.id].filter(Boolean).join(' '));
        this.status.textContent = 'Loading local document';
        root.after(this.status);
        if (options.plainPasteControl !== false) {
            this.plainButton = root.ownerDocument.createElement('button');
            this.plainButton.type = 'button';
            this.plainButton.textContent = 'Paste without formatting';
            this.plainButton.disabled = true;
            this.status.after(this.plainButton);
            this.plainButton.addEventListener('pointerdown', this.capturePlainTarget);
            this.plainButton.addEventListener('click', this.plainClick);
            root.addEventListener('keydown', this.capturePlainTarget);
        }
        this.ready = this.activate(captured);
        void this.ready.catch(() => { });
    }
    get state() { return this.lifecycle.state; }
    get clipboardRecovery() { return this.input?.clipboard.recovery.map(record => ({ ...record })) ?? []; }
    subscribe(listener) { return this.lifecycle.subscribe(listener); }
    async activate(options) {
        try {
            const cancellation = new Promise((_, reject) => { this.cancelActivation = () => reject(Error('Editor initialization canceled')); });
            const recovery = (options.recover ?? recoverLocalDocument)(options).then(async (session) => {
                // A shared runtime/host recovery operation may not be abortable. It can
                // never attach a canceled surface; release any late replica immediately.
                if (this.closing || this.destroyed) {
                    await session.storage.destroy({ policy: 'report' });
                    throw Error('Editor initialization canceled');
                }
                return session;
            });
            const session = await Promise.race([recovery, cancellation]);
            this.cancelActivation = undefined;
            if (this.closing || this.destroyed) {
                await session.storage.destroy({ policy: 'report' });
                throw Error('Editor initialization canceled');
            }
            this.session = session;
            const snapshot = session.writer.engine.read();
            const preview = options.preview ? previewMatches(options.preview, snapshot.identity, snapshot.revision) ? 'matched' : 'replaced' : 'none';
            // Always bind fresh canonical mappings, including matching preview content.
            // Raw host DOM is never reused as an authoritative editable projection.
            this.surface = bindEditorSurface(this.root, session.writer.engine, { readOnly: true,
                ...(options.modules ? { modules: options.modules } : {}),
                ...(options.moduleRuntime ? { moduleRuntime: options.moduleRuntime } : {}),
                ...(options.label === undefined ? {} : { label: options.label }),
                ...(options.clipboardCodecs === undefined ? {} : { clipboardCodecs: options.clipboardCodecs }),
                commit: request => this.commit(request) });
            this.renderer = this.surface.renderer;
            this.selection = this.surface.selection;
            this.input = this.surface.input;
            this.input.shortcuts.enabled = options.typingShortcuts ?? true;
            this.input.clipboard.plainTextPolicy = options.plainTextPolicy ?? (options.preset === 'minimal' ? 'literal' : 'markdown');
            this.input.clipboard.contentCodecs = options.contentCodecs ?? {};
            this.unsubscribe = session.storage.subscribe(state => {
                if (this.destroyed)
                    return;
                this.lifecycle.update({ localCommitted: state.localCommitted, error: state.error });
                if (state.phase === 'error')
                    this.status.textContent = 'Local save failed. Export recovery content before closing.';
            });
            this.input.setReadOnly(this.readOnly);
            this.root.setAttribute('aria-readonly', String(this.readOnly));
            this.root.setAttribute('aria-busy', 'false');
            this.status.textContent = 'Document ready';
            if (this.plainButton)
                this.plainButton.disabled = this.readOnly;
            this.lifecycle.update({ phase: 'ready', ready: true, visible: true, preview });
        }
        catch (error) {
            if (!this.closing && !this.destroyed) {
                this.root.contentEditable = 'false';
                this.root.setAttribute('aria-busy', 'false');
                this.root.setAttribute('aria-readonly', 'true');
                this.status.setAttribute('role', 'alert');
                this.status.textContent = 'Unable to open local document. Recovery content remains read-only.';
                this.lifecycle.update({ phase: 'failed', ready: false, readOnly: true, error });
            }
            throw error;
        }
        finally {
            this.cancelActivation = undefined;
        }
    }
    requireReady() {
        if (this.closing || this.destroyed || !this.state.ready || !this.session)
            throw Error('Editor is not ready');
        return this.session;
    }
    get moduleRuntime() { return this.renderer?.moduleRuntime; }
    read() { return this.requireReady().writer.engine.read(); }
    commit(request) {
        const session = this.requireReady();
        if (this.readOnly)
            throw Error('Editor is read-only');
        return session.storage.commit(request);
    }
    setReadOnly(value) {
        if (this.closing || this.destroyed)
            throw Error('Editor is closing');
        this.readOnly = value;
        this.input?.setReadOnly(value);
        this.root.setAttribute('aria-readonly', String(value || !this.state.ready));
        if (value) {
            this.plainTarget?.dispose();
            this.plainTarget = undefined;
        }
        if (this.plainButton)
            this.plainButton.disabled = value || !this.state.ready;
        this.lifecycle.update({ readOnly: value });
    }
    paste(data, options = {}) {
        this.requireReady();
        return this.input.clipboard.paste(data, options);
    }
    pasteDeferred(data, options = {}) {
        this.requireReady();
        return this.input.clipboard.pasteDeferred(data, options);
    }
    pastePlainText(read) {
        this.plainTarget?.dispose();
        this.plainTarget = undefined;
        return this.plainPaste(read);
    }
    plainPaste(read, target) {
        this.requireReady();
        return this.input.clipboard.pastePlainText(read ?? (() => {
            const clipboard = this.root.ownerDocument.defaultView?.navigator.clipboard;
            return clipboard?.readText ? clipboard.readText() : Promise.reject(Error('Script clipboard unavailable; use native paste'));
        }), target).then(result => {
            if (result.disposition === 'rejected' && !this.closing && !this.destroyed)
                this.status.textContent = 'Plain paste unavailable. Use native Paste or allow clipboard access.';
            return result;
        });
    }
    flush(options) { return this.requireReady().storage.flush(options); }
    recoveryExport() { if (!this.session || this.destroyed)
        throw Error('No live recovery replica'); return this.session.storage.recoveryExport(); }
    destroy(options = { policy: 'flush' }) {
        if (this.result)
            return Promise.resolve(this.result);
        if (this.destroyPromise)
            return this.destroyPromise;
        if (options.policy !== 'flush' && options.policy !== 'report')
            return Promise.reject(Error('Explicit destroy policy required'));
        this.closing = true;
        this.root.contentEditable = 'false';
        this.root.setAttribute('aria-readonly', 'true');
        // Publish the shared teardown promise before notifying reentrant subscribers.
        this.destroyPromise = Promise.resolve().then(async () => {
            try {
                this.lifecycle.update({ phase: 'closing', ready: false, readOnly: true });
                this.cancelActivation?.();
                this.cancelActivation = undefined;
                this.plainTarget?.dispose();
                this.plainTarget = undefined;
                if (this.plainButton) {
                    this.plainButton.disabled = true;
                    this.plainButton.removeEventListener('pointerdown', this.capturePlainTarget);
                    this.plainButton.removeEventListener('click', this.plainClick);
                }
                this.root.removeEventListener('keydown', this.capturePlainTarget);
                this.surface?.dispose();
                this.unsubscribe?.();
                const provisional = this.input?.recovery.map(r => ({ text: r.text, reason: r.reason })) ?? [];
                const clipboard = this.clipboardRecovery;
                await this.ready.catch(() => { });
                const report = this.session ? await this.session.storage.destroy(options) : { unsaved: false, recovery: null };
                this.destroyed = true;
                this.status.remove();
                this.plainButton?.remove();
                this.root.setAttribute('aria-busy', 'false');
                mounts.delete(this.root);
                this.releaseSurface();
                const description = this.root.getAttribute('aria-describedby')?.split(/\s+/).filter(id => id !== this.status.id).join(' ');
                if (description)
                    this.root.setAttribute('aria-describedby', description);
                else
                    this.root.removeAttribute('aria-describedby');
                this.result = { ...report, provisional, clipboard };
                this.lifecycle.dispose();
                return this.result;
            }
            catch (error) {
                this.status.setAttribute('role', 'alert');
                this.status.textContent = 'Local save failed. Export recovery content before closing.';
                this.lifecycle.update({ phase: 'failed', ready: false, readOnly: true, error });
                this.destroyPromise = undefined;
                throw error;
            }
        });
        return this.destroyPromise;
    }
}
export function mountEditor(root, options) { return new BrowserEditor(root, options); }

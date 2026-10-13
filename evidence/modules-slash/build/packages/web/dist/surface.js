import { DOMRenderer } from './dom/render.js';
import { DOMSelection } from './dom/selection.js';
import { TextInput } from './input/text.js';
const mounted = new WeakSet();
/** Reserve before asynchronous recovery so both mount paths share ownership. */
export function reserveEditorSurface(root) {
    if (mounted.has(root))
        throw Error('Editor already mounted on this surface');
    mounted.add(root);
    let released = false;
    return () => { if (!released) {
        released = true;
        mounted.delete(root);
    } };
}
/** Shared adapter assembly for recovered documents and host-owned replicas. */
export function bindEditorSurface(root, engine, options = {}) {
    const renderer = new DOMRenderer(root, engine, { readOnly: true, ...(options.modules ? { modules: options.modules } : {}), ...(options.moduleRuntime ? { moduleRuntime: options.moduleRuntime } : {}) });
    let selection, input;
    try {
        root.setAttribute('role', 'textbox');
        root.setAttribute('aria-multiline', 'true');
        root.setAttribute('aria-label', options.label ?? root.getAttribute('aria-label') ?? 'Document editor');
        if (!root.hasAttribute('tabindex'))
            root.tabIndex = 0;
        selection = new DOMSelection(renderer, engine);
        input = new TextInput(renderer, selection, engine, options.commit ?? (request => engine.commit(engine.prepare(request))), options.clipboardCodecs ?? []);
        if (options.slash)
            input.attachSlash(options.slash);
        input.shortcuts.enabled = options.typingShortcuts ?? true;
        input.clipboard.plainTextPolicy = options.plainTextPolicy ?? (options.preset === 'minimal' ? 'literal' : 'markdown');
        input.clipboard.contentCodecs = options.contentCodecs ?? {};
        input.setReadOnly(options.readOnly ?? false);
        root.setAttribute('aria-readonly', String(options.readOnly ?? false));
        const boundInput = input, boundSelection = selection;
        let disposed = false;
        return { renderer, selection: boundSelection, input: boundInput,
            dispose() {
                if (disposed)
                    return;
                disposed = true;
                root.contentEditable = 'false';
                root.setAttribute('aria-readonly', 'true');
                try {
                    boundInput.dispose();
                }
                finally {
                    try {
                        boundSelection.dispose();
                    }
                    finally {
                        renderer.dispose();
                    }
                }
            } };
    }
    catch (error) {
        try {
            input?.dispose();
        }
        finally {
            try {
                selection?.dispose();
            }
            finally {
                renderer.dispose();
            }
        }
        root.contentEditable = 'false';
        throw error;
    }
}
/** Mount a synchronous view over a host-owned engine, without a storage service. */
export function mountEditorSurface(root, engine, options = {}) {
    const release = reserveEditorSurface(root);
    try {
        const binding = bindEditorSurface(root, engine, options);
        let disposed = false;
        const requireLive = () => { if (disposed)
            throw Error('Editor surface is disposed'); };
        return {
            get slash() { return binding.input.slash; },
            get moduleRuntime() { return binding.renderer.moduleRuntime; },
            get recovery() { return binding.input.recovery.map(({ text, reason }) => ({ text, reason })); },
            settle() { requireLive(); return binding.input.settle(); },
            setReadOnly(value) { requireLive(); binding.input.setReadOnly(value); root.setAttribute('aria-readonly', String(value)); },
            dispose() { if (disposed)
                return; disposed = true; try {
                binding.dispose();
            }
            finally {
                release();
            } },
        };
    }
    catch (error) {
        release();
        throw error;
    }
}

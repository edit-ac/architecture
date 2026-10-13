/* tslint:disable */
/* eslint-disable */

export class Engine {
    free(): void;
    [Symbol.dispose](): void;
    anchor(input: string): string;
    apply_update(input: string, bytes: Uint8Array): string;
    can(input: string): string;
    checkpoint_bytes(): Uint8Array;
    checkpoint_metadata(): string;
    commit(token: string): string;
    dispose(): void;
    encode_update(vector: Uint8Array): Uint8Array;
    export_anchor(token: string): string;
    export_markdown(input: string): string;
    history(input: string): string;
    import_anchor(input: string): string;
    import_markdown(input: string): string;
    markdown_equivalent(input: string): string;
    constructor(input: string);
    prepare(input: string): string;
    read(): string;
    release_anchor(token: string): void;
    release_plan(token: string): void;
    resolve(token: string): string;
    /**
     * Explicit initialized restore; never imports defaults or reuses a writer.
     */
    static restore(input: string, bytes: Uint8Array): Engine;
    state_vector(): Uint8Array;
    /**
     * Pull the detached batch only after the semantic call has returned.
     */
    take_patch(): string;
}

/**
 * Own one UTF-16 Yrs replica using the earlier disposable XML interop fixture.
 */
export class Fixture {
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Decode before mutation; only trusted deterministic fixture updates are supported.
     */
    apply_v1(bytes: Uint8Array): void;
    constructor();
    text(): string;
    update_v1(): Uint8Array;
    utf16_length(): number;
}

/**
 * Cumulative fixture creation count; loading a module never creates a replica.
 */
export function created_document_count(): number;

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
    readonly memory: WebAssembly.Memory;
    readonly __wbg_engine_free: (a: number, b: number) => void;
    readonly __wbg_fixture_free: (a: number, b: number) => void;
    readonly created_document_count: () => number;
    readonly engine_anchor: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_apply_update: (a: number, b: number, c: number, d: number, e: number) => [number, number, number, number];
    readonly engine_can: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_checkpoint_bytes: (a: number) => [number, number, number, number];
    readonly engine_checkpoint_metadata: (a: number) => [number, number, number, number];
    readonly engine_commit: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_dispose: (a: number) => void;
    readonly engine_encode_update: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_export_anchor: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_export_markdown: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_history: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_import_anchor: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_import_markdown: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_markdown_equivalent: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_new: (a: number, b: number) => [number, number, number];
    readonly engine_prepare: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_read: (a: number) => [number, number, number, number];
    readonly engine_release_anchor: (a: number, b: number, c: number) => [number, number];
    readonly engine_release_plan: (a: number, b: number, c: number) => [number, number];
    readonly engine_resolve: (a: number, b: number, c: number) => [number, number, number, number];
    readonly engine_restore: (a: number, b: number, c: number, d: number) => [number, number, number];
    readonly engine_state_vector: (a: number) => [number, number, number, number];
    readonly engine_take_patch: (a: number) => [number, number, number, number];
    readonly fixture_apply_v1: (a: number, b: number, c: number) => [number, number];
    readonly fixture_new: () => number;
    readonly fixture_text: (a: number) => [number, number];
    readonly fixture_update_v1: (a: number) => [number, number];
    readonly fixture_utf16_length: (a: number) => number;
    readonly __wbindgen_exn_store: (a: number) => void;
    readonly __externref_table_alloc: () => number;
    readonly __wbindgen_externrefs: WebAssembly.Table;
    readonly __wbindgen_malloc: (a: number, b: number) => number;
    readonly __wbindgen_realloc: (a: number, b: number, c: number, d: number) => number;
    readonly __externref_table_dealloc: (a: number) => void;
    readonly __wbindgen_free: (a: number, b: number, c: number) => void;
    readonly __wbindgen_start: () => void;
}

export type SyncInitInput = BufferSource | WebAssembly.Module;

/**
 * Instantiates the given `module`, which can either be bytes or
 * a precompiled `WebAssembly.Module`.
 *
 * @param {{ module: SyncInitInput }} module - Passing `SyncInitInput` directly is deprecated.
 *
 * @returns {InitOutput}
 */
export function initSync(module: { module: SyncInitInput } | SyncInitInput): InitOutput;

/**
 * If `module_or_path` is {RequestInfo} or {URL}, makes a request and
 * for everything else, calls `WebAssembly.instantiate` directly.
 *
 * @param {{ module_or_path: InitInput | Promise<InitInput> }} module_or_path - Passing `InitInput` directly is deprecated.
 *
 * @returns {Promise<InitOutput>}
 */
export default function __wbg_init (module_or_path?: { module_or_path: InitInput | Promise<InitInput> } | InitInput | Promise<InitInput>): Promise<InitOutput>;

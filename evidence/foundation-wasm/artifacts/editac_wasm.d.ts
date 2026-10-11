/* tslint:disable */
/* eslint-disable */

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
    readonly __wbg_fixture_free: (a: number, b: number) => void;
    readonly created_document_count: () => number;
    readonly fixture_apply_v1: (a: number, b: number, c: number) => [number, number];
    readonly fixture_new: () => number;
    readonly fixture_text: (a: number) => [number, number];
    readonly fixture_update_v1: (a: number) => [number, number];
    readonly fixture_utf16_length: (a: number) => number;
    readonly __wbindgen_exn_store: (a: number) => void;
    readonly __externref_table_alloc: () => number;
    readonly __wbindgen_externrefs: WebAssembly.Table;
    readonly __wbindgen_malloc: (a: number, b: number) => number;
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

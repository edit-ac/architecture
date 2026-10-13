import type { FragmentBlock } from '@edit-ac/core';
import type { SlashContext } from './slash.js';
export interface ReferenceTarget {
    targetId: string;
    label: string;
}
export interface ReferenceQuery {
    query: string;
    requestId: number;
    signal: AbortSignal;
}
/** Only explicit user search calls this host port. Mount/render never resolve IDs. */
export type ReferenceResolver = (request: Readonly<ReferenceQuery>) => readonly ReferenceTarget[] | Promise<readonly ReferenceTarget[]>;
export type ReferenceFactory = (context: SlashContext) => ReferencePresenter;
export declare function referenceBlock(target: ReferenceTarget): FragmentBlock;
export declare function referenceSuggestions(resolve: ReferenceResolver): ReferenceFactory;
/** A transient host search UI. Only the engine commits the chosen inert atom. */
export declare class ReferencePresenter {
    private readonly context;
    private readonly resolve;
    readonly menu: HTMLElement;
    readonly search: HTMLInputElement;
    readonly control: HTMLButtonElement;
    private readonly items;
    private readonly status;
    private session;
    private captured;
    private pending;
    private requestId;
    private lastQuery;
    private composing;
    private results;
    private active;
    private readOnly;
    private disposed;
    private committing;
    private readonly listeners;
    constructor(context: SlashContext, resolve: ReferenceResolver);
    private listen;
    private inside;
    get open(): boolean;
    private clearCapture;
    private capture;
    openExplicit(): void;
    private invalidate;
    private query;
    activate(index: number): void;
    handle(event: Event): boolean;
    dismiss(restore?: boolean): void;
    setReadOnly(value: boolean): void;
    dispose(): void;
}

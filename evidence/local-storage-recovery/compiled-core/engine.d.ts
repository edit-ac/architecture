/** Explicit v5 creation; importing this module never allocates a replica. */
export interface CreateOptions {
    profile: "v5";
    documentId: string;
    epoch: string;
    nodes: readonly {
        text: string;
    }[];
}
declare const anchorBrand: unique symbol;
declare const planBrand: unique symbol;
/** Scoped to one engine. Release when no longer needed. */
export type AnchorToken = string & {
    readonly [anchorBrand]: true;
};
/** Single-use plan; failed stale commits consume it too. */
export type PlanToken = string & {
    readonly [planBrand]: true;
};
export type Bias = "left" | "right";
export interface StableRange {
    anchor: AnchorToken;
    focus: AnchorToken;
}
export type ContainerStyle = {
    type: "unordered" | "checklist" | "quote";
} | {
    type: "ordered";
    start: number;
};
export interface MoveTarget {
    id: string;
    version: string;
}
export type EditorCommand = {
    type: "insert";
    at: AnchorToken;
    text: string;
} | {
    type: "delete";
    range: StableRange;
} | {
    type: "replace";
    range: StableRange;
    text: string;
} | {
    type: "split" | "enter" | "backspace";
    owner: string;
    at: AnchorToken;
} | {
    type: "join";
    first: string;
    second: string;
} | {
    type: "wrap";
    targets: readonly string[];
    style: ContainerStyle;
} | {
    type: "setStyle";
    container: string;
    style: ContainerStyle;
} | {
    type: "setChecked";
    owner: string;
    checked: boolean;
} | {
    type: "indent" | "outdent" | "setParagraph" | "convertSeparator" | "deleteSeparator";
    owner: string;
} | {
    type: "move";
    target: MoveTarget;
    parent: MoveTarget;
    before?: MoveTarget | null;
} | {
    type: "setCode";
    owner: string;
    language: string;
} | {
    type: "hardBreak";
    at: AnchorToken;
} | {
    type: "insertSeparator";
    beside: string;
    side: "before" | "after";
} | {
    type: "insertParagraph";
    separator: string;
    side: "before" | "after";
    text: string;
};
export type TextCommand = Extract<EditorCommand, {
    type: "insert" | "delete" | "replace";
}>;
export type FormatAction = "apply" | "remove" | "toggle";
export interface MarkCommand {
    range: StableRange;
    mark: "bold" | "italic" | "strike" | "underline" | "code" | "link";
    action: FormatAction;
    href?: string | null;
}
export interface BlockFormatCommand {
    targets: readonly string[];
    attributes: {
        type: "paragraph";
    } | {
        type: "heading";
        level: number;
    };
    action: FormatAction;
}
export type PrepareRequest = {
    kind: "text";
    origin: string;
    command: TextCommand;
} | {
    kind: "editor";
    origin: string;
    commands: readonly EditorCommand[];
} | {
    kind: "format";
    origin: string;
    marks: readonly MarkCommand[];
    blocks: readonly BlockFormatCommand[];
};
export type Json = null | boolean | number | string | Json[] | {
    [key: string]: Json;
};
export interface ProjectedNode {
    id: string;
    kind: string;
    parent: string;
    order: number;
    spans: {
        source: string;
        identity: string;
        start: number;
        end: number;
    }[];
    runs: {
        text: string;
        attributes: Record<string, Json>;
    }[];
    blockAttributes: Json;
    editor: null | {
        version: string;
        containerAttributes: Json;
        checked: boolean | null;
        number: number | null;
    };
}
export interface Snapshot {
    revision: number;
    identity: {
        profile: string;
        schema: string;
        documentId: string;
        epoch: string;
        protocolVersion: number;
        updateEncoding: number;
        offsets: "utf16";
    };
    visible: ProjectedNode[];
    recovery: ProjectedNode[];
    retainedStructure: Json;
    changedNodes: string[];
    touchedRanges: {
        source: string;
        start: number;
        newStart: number;
        oldEnd: number;
        newEnd: number;
    }[];
}
export type AnchorResolution = {
    type: "position";
    node: string;
    offset: number;
    source: string;
    sourceOffset: number;
    bias: Bias;
} | {
    type: "deleted";
    source: string;
    owner: string;
} | {
    type: "unresolvable";
    reason: string;
};
export type HistoryRequest = {
    type: "state" | "undo" | "redo" | "clear" | "boundary" | "explicit";
} | {
    type: "typing";
    session: number;
    time_ms: number;
} | {
    type: "composition";
    session: number;
};
export interface HistoryState {
    revision: number;
    undoGroups: number;
    redoGroups: number;
    retainedUpdateBytes: number;
}
export type DocumentIdentity = Snapshot["identity"];
/** Persist the envelope atomically with these owned v1 bytes. Writer is provenance. */
export interface Checkpoint {
    identity: DocumentIdentity;
    initialized: true;
    writerId: number;
    bytes: Uint8Array;
}
export interface ReplayUpdate {
    identity: DocumentIdentity;
    bytes: Uint8Array;
}
export type PatchScope = {
    type: "all" | "updates" | "selection";
} | {
    type: "nodes" | "sources";
    ids: readonly string[];
};
export interface Patch {
    version: number;
    sequence: number;
    revision: number;
    identity: DocumentIdentity;
    writerId: number;
    operation: "Text" | "Format" | "Structure" | "Editor" | "Remote" | "Undo" | "Redo" | "Selection";
    origin: string;
    changedNodes: string[];
    changedSources: string[];
    nodes: ({
        type: "visible" | "recovery";
        node: ProjectedNode;
    } | {
        type: "removed";
        id: string;
    })[];
    touchedRanges: Snapshot["touchedRanges"];
    selectionChanged: boolean;
    selection: null | {
        anchor: AnchorResolution;
        focus: AnchorResolution;
    } | {
        error: string;
    };
    update: ReplayUpdate | null;
    projectionError: string | null;
}
/** Callback capture is released on disposal; active becomes false on engine disposal too. */
export interface PatchSubscription {
    readonly active: boolean;
    dispose(): void;
}
export interface ObserverError {
    subscriptionId: number;
    message: string;
}
export interface EngineHandle {
    read(): Snapshot;
    anchor(node: string, offset: number, bias: Bias): AnchorToken;
    resolve(anchor: AnchorToken): AnchorResolution;
    releaseAnchor(anchor: AnchorToken): void;
    prepare(request: PrepareRequest): PlanToken;
    can(request: PrepareRequest): boolean;
    commit(plan: PlanToken): {
        revision: number;
    };
    releasePlan(plan: PlanToken): void;
    history(request: HistoryRequest): HistoryState;
    checkpoint(): Checkpoint;
    stateVector(): Uint8Array;
    /** Default vector encodes the entire state. A vector alone is not a content revision. */
    encodeUpdate(stateVector?: Uint8Array): ReplayUpdate;
    applyUpdate(update: ReplayUpdate): {
        revision: number;
    };
    /** Runs after the WASM borrow/transaction returns. Nested batches dispatch FIFO. */
    subscribe(scope: PatchScope, callback: (patch: Patch) => void): PatchSubscription;
    takeObserverErrors(): ObserverError[];
    /** Drops replica and all anchors/plans/history. Safe to call repeatedly. */
    dispose(): void;
}
export declare class EngineError extends Error {
    readonly code: string;
    readonly operation: string;
    constructor(code: string, operation: string, message: string);
}
/** Internal compiled boundary; application clients use EngineHandle. */
export interface RawEngine {
    read(): string;
    anchor(input: string): string;
    resolve(token: string): string;
    prepare(input: string): string;
    commit(token: string): string;
    history(input: string): string;
    release_anchor(token: string): void;
    release_plan(token: string): void;
    checkpoint_metadata(): string;
    checkpoint_bytes(): Uint8Array;
    state_vector(): Uint8Array;
    encode_update(vector: Uint8Array): Uint8Array;
    apply_update(input: string, bytes: Uint8Array): string;
    take_patch(): string;
    dispose(): void;
    free(): void;
}
export declare function createHandle(construct: (json: string) => RawEngine, options: CreateOptions): EngineHandle;
export declare function restoreHandle(construct: (json: string, bytes: Uint8Array) => RawEngine, expected: DocumentIdentity, checkpoint: Checkpoint, journal?: readonly ReplayUpdate[]): EngineHandle;
export {};

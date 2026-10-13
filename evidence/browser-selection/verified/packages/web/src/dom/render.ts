import type { EngineHandle, Json, Patch, PatchSubscription, ProjectedNode } from "@edit-ac/core";

export interface DOMPosition { node: Node; start: number; length: number }
type Run = ProjectedNode["runs"][number];
interface RenderedRun { element: HTMLElement; key: string; text: string; positions: DOMPosition[] }
interface Entry { node: ProjectedNode; outer: HTMLElement; content: HTMLElement; key: string; runs: RenderedRun[] }
const tuple = (value: Json | undefined): Json[] => Array.isArray(value) ? value : [];

/** Internal projection adapter. It renders engine state, never imports DOM state.
 * Input/selection readiness is a separate lifecycle gate. No DOM access at import.
 */
export class DOMRenderer {
  private readonly entries = new Map<string, Entry>();
  private readonly owners = new WeakMap<Node, string>();
  private readonly subscription: PatchSubscription;
  private disposed = false;
  private revision: number;
  constructor(readonly root: HTMLElement, engine: EngineHandle, options: { readOnly?: boolean } = {}) {
    const snapshot = engine.read();
    this.revision = snapshot.revision;
    root.replaceChildren();
    root.contentEditable = options.readOnly ? "false" : "true";
    const nodes = new Map(snapshot.visible.map(node => [node.id, node]));
    for (const node of snapshot.visible) this.update(node, nodes.get(node.parent));
    this.arrange();
    this.subscription = engine.subscribe({ type: "all" }, patch => this.apply(patch));
  }
  getBlock(id: string): HTMLElement | undefined { return this.entries.get(id)?.content; }
  getNodeId(node: Node): string | undefined {
    for (let at: Node | null = node; at && at !== this.root; at = at.parentNode) {
      const id = this.owners.get(at);
      if (id && this.entries.get(id)?.outer.contains(node)) return id;
    }
    return undefined;
  }
  /** UTF-16 text and hard-break map; empty-block placeholder has length zero. */
  positions(id: string): readonly DOMPosition[] {
    const entry = this.entries.get(id);
    if (!entry) return [];
    let offset = 0;
    return entry.runs.flatMap(run => run.positions.map(position => {
      const result = { ...position, start: offset }; offset += position.length; return result;
    }));
  }
  /** Document-ordered editable blocks, excluding containers and noneditable atoms. */
  textBlockIds(): string[] {
    return [...this.entries.values()].filter(entry => entry.runs.length > 0 && entry.content.contentEditable !== "false")
      .sort((a, b) => a.node.order - b.node.order).map(entry => entry.node.id);
  }
  setReadOnly(value: boolean): void { if (!this.disposed) this.root.contentEditable = value ? "false" : "true"; }
  dispose(): void {
    if (this.disposed) return;
    this.disposed = true; this.subscription.dispose(); this.root.contentEditable = "false";
    this.entries.clear();
  }
  private apply(patch: Patch): void {
    if (this.disposed || patch.revision < this.revision) return;
    if (patch.projectionError) throw new Error(`DOM projection failed: ${patch.projectionError}`);
    this.revision = patch.revision;
    let structure = false;
    // Apply metadata first so children see their new parent presentation.
    const changed = new Map<string, ProjectedNode>();
    for (const change of patch.nodes) if (change.type === "visible") changed.set(change.node.id, change.node);
    const parentOf = (node: ProjectedNode) => changed.get(node.parent) ?? this.entries.get(node.parent)?.node;
    for (const change of patch.nodes) {
      if (change.type !== "visible") {
        const id = change.type === "removed" ? change.id : change.node.id;
        const entry = this.entries.get(id);
        if (entry) { entry.outer.remove(); this.entries.delete(id); structure = true; }
      } else {
        const old = this.entries.get(change.node.id);
        structure ||= !old || old.node.parent !== change.node.parent || old.node.order !== change.node.order;
        const previousOuter = old?.outer;
        this.update(change.node, parentOf(change.node));
        structure ||= previousOuter !== this.entries.get(change.node.id)?.outer;
      }
    }
    // Parent style changes may alter child wrappers/checklist metadata.
    if (structure || patch.operation === "Editor" || patch.operation === "Structure") {
      for (const entry of this.entries.values()) this.update(entry.node, parentOf(entry.node));
      this.arrange();
    }
  }
  private update(node: ProjectedNode, parent: ProjectedNode | undefined): void {
    const block = tuple(node.blockAttributes), style = tuple(node.editor?.containerAttributes);
    const isListItem = parent?.kind === "list";
    const tag = node.kind === "list" ? (style[0] === "ordered" ? "ol" : "ul") : node.kind === "quote" ? "blockquote" :
      block[0] === "separator" ? "hr" : block[0] === "heading" && Number.isInteger(block[1]) && Number(block[1]) >= 1 && Number(block[1]) <= 6 ? `h${block[1]}` : block[0] === "code" ? "pre" : "p";
    const key = `${tag}:${isListItem}`;
    let entry = this.entries.get(node.id);
    if (!entry || entry.key !== key) {
      const content = this.root.ownerDocument.createElement(tag);
      const outer = isListItem ? this.root.ownerDocument.createElement("li") : content;
      if (outer !== content) outer.append(content);
      const old = entry;
      entry = { node, content, outer, key, runs: [] };
      this.entries.set(node.id, entry);
      this.owners.set(content, node.id); this.owners.set(outer, node.id);
      outer.dataset.nodeId = node.id;
      if (old) { old.outer.replaceWith(outer); }
    }
    entry.node = node;
    if (tag === "hr") { entry.content.contentEditable = "false"; entry.content.setAttribute("aria-label", "Separator"); return; }
    if (node.kind === "list" || node.kind === "quote") {
      if (tag === "ol" && Number.isSafeInteger(style[1])) entry.content.setAttribute("start", String(style[1]));
      else entry.content.removeAttribute("start");
      return;
    }
    if (isListItem) {
      if (node.editor?.number !== null && node.editor?.number !== undefined) entry.outer.setAttribute("value", String(node.editor.number));
      else entry.outer.removeAttribute("value");
      // A static, noneditable checklist marker; commands own toggling later.
      let marker = entry.outer.querySelector<HTMLElement>(":scope > [data-check-marker]");
      if (tuple(parent?.editor?.containerAttributes)[0] === "checklist") {
        if (!marker) { marker = this.root.ownerDocument.createElement("span"); marker.dataset.checkMarker = ""; marker.contentEditable = "false"; entry.outer.prepend(marker); }
        marker.textContent = node.editor?.checked ? "☑" : "☐";
        marker.setAttribute("role", "img"); marker.setAttribute("aria-label", node.editor?.checked ? "Checked" : "Unchecked");
      } else marker?.remove();
    }
    this.patchRuns(entry, node.runs, tag === "pre");
  }
  private arrange(): void {
    const groups = new Map<HTMLElement, HTMLElement[]>();
    for (const entry of [...this.entries.values()].sort((a, b) => a.node.order - b.node.order)) {
      const parent = this.entries.get(entry.node.parent);
      // Nested containers follow a list item's paragraph, never sit inside it.
      const target = parent ? (parent.node.kind === "block" && parent.outer !== parent.content ? parent.outer : parent.content) : this.root;
      const children = groups.get(target) ?? []; children.push(entry.outer); groups.set(target, children);
    }
    for (const [parent, children] of groups) {
      let cursor: ChildNode | null = parent.firstChild;
      for (const child of children) {
        // Skip a list item's own text and static marker when arranging nested lists.
        while (cursor && !children.includes(cursor as HTMLElement)) cursor = cursor.nextSibling;
        if (child !== cursor) parent.insertBefore(child, cursor);
        cursor = child.nextSibling;
      }
    }
  }
  private markKey(run: Run): string {
    const a = run.attributes;
    return JSON.stringify([a.bold === true, a.italic === true, a.strike === true, a.underline === true, a.code === true, this.safeHref(a.link)]);
  }
  private safeHref(value: Json | undefined): string | null {
    if (typeof value !== "string") return null;
    try { const url = new URL(value, this.root.ownerDocument.baseURI); return ["http:", "https:", "mailto:"].includes(url.protocol) ? url.href : null; }
    catch { return null; }
  }
  private createRun(run: Run, code: boolean): RenderedRun {
    const element = this.root.ownerDocument.createElement("span");
    let target: HTMLElement = element;
    const attrs = run.attributes;
    for (const [name, tag] of [["bold", "strong"], ["italic", "em"], ["strike", "s"], ["underline", "u"], ["code", "code"]] as const) {
      if (!code && attrs[name] === true) { const wrapper = this.root.ownerDocument.createElement(tag); target.append(wrapper); target = wrapper; }
    }
    const href = code ? null : this.safeHref(attrs.link);
    if (href) { const link = this.root.ownerDocument.createElement("a"); link.href = href; link.rel = "noopener noreferrer"; target.append(link); target = link; }
    const parts = code ? [run.text] : run.text.split("\n");
    const positions: DOMPosition[] = [];
    parts.forEach((part, i) => {
      if (i) { const br = this.root.ownerDocument.createElement("br"); target.append(br); positions.push({ node: br, start: 0, length: 1 }); }
      const text = this.root.ownerDocument.createTextNode(part); target.append(text); positions.push({ node: text, start: 0, length: part.length });
    });
    return { element, text: run.text, key: this.markKey(run), positions };
  }
  private patchRuns(entry: Entry, runs: readonly Run[], code: boolean): void {
    // Empty blocks need a visible caret line; it contributes no model offset.
    const desired = runs.length ? runs : [{ text: "", attributes: {} }];
    const old = entry.runs;
    let prefix = 0, suffix = 0;
    const same = (a: RenderedRun, b: Run) => a.text === b.text && a.key === this.markKey(b);
    while (prefix < old.length && prefix < desired.length && same(old[prefix]!, desired[prefix]!)) prefix++;
    while (suffix < old.length - prefix && suffix < desired.length - prefix && same(old[old.length - suffix - 1]!, desired[desired.length - suffix - 1]!)) suffix++;
    const middle: RenderedRun[] = [];
    for (let i = prefix; i < desired.length - suffix; i++) {
      const run = desired[i]!, existing = i < old.length - suffix ? old[i] : undefined;
      const parts = code ? [run.text] : run.text.split("\n");
      if (existing && existing.key === this.markKey(run) && existing.positions.length === parts.length * 2 - 1) {
        // Retain text nodes and BR atoms across edits within the same lines.
        parts.forEach((part, index) => {
          const position = existing.positions[index * 2]!, text = position.node as Text;
          if (text.data !== part) {
            let start = 0, end = 0;
            while (start < text.length && start < part.length && text.data[start] === part[start]) start++;
            while (end < text.length - start && end < part.length - start && text.data[text.length - end - 1] === part[part.length - end - 1]) end++;
            text.replaceData(start, text.length - start - end, part.slice(start, part.length - end));
          }
          position.length = part.length;
        });
        existing.text = run.text; middle.push(existing);
      } else middle.push(this.createRun(run, code));
    }
    const next = [...old.slice(0, prefix), ...middle, ...(suffix ? old.slice(old.length - suffix) : [])];
    for (const run of old) if (!next.includes(run)) run.element.remove();
    let cursor: ChildNode | null = entry.content.firstChild;
    for (const run of next) { if (run.element !== cursor) entry.content.insertBefore(run.element, cursor); cursor = run.element.nextSibling; }
    entry.runs = next;
    const placeholder = entry.content.querySelector(":scope > br[data-placeholder]");
    if (desired.every(run => run.text === "") && !code) {
      if (!placeholder) { const br = this.root.ownerDocument.createElement("br"); br.dataset.placeholder = ""; entry.content.append(br); }
    } else placeholder?.remove();
  }
}

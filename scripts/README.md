# Roadmap checks

Install locked development dependencies with `npm ci`, then run
`npm run validate:roadmaps` from this repository. The command validates every
`roadmaps/*.md` file with the pinned Roadmap Runner 0.8.0 contract. It also checks
the manifest's file coverage and upstream dependency graph, task prefixes, global
checkbox IDs, opening status lines and explicit local Markdown links in task
Context paragraphs. JSON output gives file, task, checkbox and link counts plus
errors; any error exits with status 1.

The manifest is `roadmaps/manifest.json` with this shape:

```json
{"roadmaps":[{"file":"01-foundation.md","prefix":"BASE","upstream":[],"workspace":"core"}]}
```

`upstream` contains filenames in the same directory. `workspace` is `core` or
`cli`. Upstream entry conditions are reviewed task acceptance: the manifest check
establishes graph consistency, not completion of another roadmap. The official
contract validates dependencies within each individual roadmap.

When a verified local checkout of Roadmap Runner is available, dependencies need
not be installed for this check:

```sh
node scripts/validate-roadmaps.mjs --runner-contract /absolute/path/to/roadmap-runner/dist/roadmap-contract.js
```

Both paths require package name `@bpstr/roadmap-runner` and version `0.8.0`.
The script resolves the installed package manifest before locating its bundled
contract because this version does not declare an exported API entry point.
An upgrade requires reviewing this integration and the roadmap contract together.
These checks never start a runner or make inference calls. They do not prove
that acceptance criteria are sufficient or that implementation work is complete.

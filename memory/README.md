# memory/ — project memory index

Structured, machine-linted project memory. Shape + rules: [HYGIENE.md](HYGIENE.md).
Generated index: [LIVE.md](LIVE.md) (builds with a non-terminal unit) + `ledger/<month>.md` shards,
both rendered by `tools/memory-tree/gen_build_index.py` from build front matter and spec status headers.

The discipline is a SIGNAL, not a directory. A build folder is named for its slug alone; which
discipline it served is declared in each spec's status header as `streams <value>[+<value>]`, over the
closed enum `.memory-tree.conf` declares. A build that spans two disciplines is one build.

## Root files

- [DECISIONS.md](DECISIONS.md) — append-only decision index, every family, grouped for reading.
- [TEMPLATE-SPEC.md](TEMPLATE-SPEC.md) — the canonical spec / design-pass format (hygiene check 12).
- [HYGIENE.md](HYGIENE.md) — the rule set; `tools/memory-tree/check-memory-hygiene.sh` is its enforcement.

## Directories

- [builds/](builds/) — one folder per slug: `README.md` · `RUN.md` (unattended run-state, only while a run is or was live) · `prompts/` `spec/` `build/` `reviews/`.
- [backlog/](backlog/) — one mutable shard per id family: `PLAY.md` `KICK.md` `TOOL.md` `DEPL.md`.
- [gotchas/](gotchas/) — the recurring-bug-class catalogue behind hygiene checks 17-19.
- [guides/](guides/) — binding protocols that are not rules of the tree: [REVIEW-PROTOCOL.md](guides/REVIEW-PROTOCOL.md) · [UNATTENDED-PROTOCOL.md](guides/UNATTENDED-PROTOCOL.md) with its second half [UNATTENDED-VERBS.md](guides/UNATTENDED-VERBS.md).
- [map/](map/) — the self-verifying codebase map: feature dossiers, the shrink-only baseline, generated artifacts.
- [archive/](archive/) — rotated indexes, template version snapshots, and the RETIRED session ledger at [archive/ledger/](archive/ledger/).
- [ledger/](ledger/) — GENERATED month shards, one row per build opened that month. Never hand-edited.
- [project/](project/) — the gate's own waiver registries (`*.txt`) and nothing else: legacy-files, curation-debt, id-orphan-waiver, corpus-path-unresolved, unarmed-branches, method-carriers.

## Streams (the closed enum)

| Value | Family | What it covers |
|---|---|---|
| `playbook` | `PLAY` | the governance template + its companions |
| `kickoff` | `KICK` | the `/session-kickoff` engine + the manifest ratchet |
| `tooling` | `TOOL` | the reusable kits in `tools/` |
| `deployer` | `DEPL` | the single-ratchet deployer research + design |

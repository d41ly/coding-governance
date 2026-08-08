# memory/ — project memory index

Structured, machine-linted project memory. Shape + rules: [HYGIENE.md](HYGIENE.md). Generated tree: [TREE.md](TREE.md).

The discipline is a SIGNAL, not a directory. A build folder is named for its slug alone; which
discipline it served is declared in each spec's status header as `streams <value>[+<value>]`, over the
closed enum `.memory-tree.conf` declares. A build that spans two disciplines is one build.

## Root files

- [DECISIONS.md](DECISIONS.md) — append-only decision index, every family, grouped for reading.
- [TEMPLATE-SPEC.md](TEMPLATE-SPEC.md) — the canonical spec / design-pass format (hygiene check 12).
- [HYGIENE.md](HYGIENE.md) — the rule set; `tools/memory-tree/check-memory-hygiene.sh` is its enforcement.

## Directories

- [builds/](builds/) — one folder per slug: `README.md` · `STATUS.md` · `prompts/` `spec/` `build/` `reviews/`.
- [backlog/](backlog/) — one mutable shard per id family: `PLAY.md` `KICK.md` `TOOL.md` `DEPL.md`.
- [archive/](archive/) — rotated indexes and version snapshots.
- [project/](project/) — session machinery: MEMORY.md, IN-FLIGHT.md (pointer) + in-flight/<tag>.md, journal/, notes.

## Streams (the closed enum)

| Value | Family | What it covers |
|---|---|---|
| `playbook` | `PLAY` | the governance template + its companions |
| `kickoff` | `KICK` | the `/session-kickoff` engine + the manifest ratchet |
| `tooling` | `TOOL` | the reusable kits in `tools/` |
| `deployer` | `DEPL` | the single-ratchet deployer research + design |

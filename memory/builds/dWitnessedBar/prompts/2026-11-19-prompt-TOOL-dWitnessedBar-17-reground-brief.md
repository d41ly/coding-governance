**Serves:** journal TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18

# Brief — dWitnessedBar: TOOL-dWitnessedBar-17, TOOL-dWitnessedBar-18 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The run's first two builders each stopped at a divergence, because the
specs were written at `cdfbd1cf` and the tree has moved since; each spec is now re-grounded before its dispatch.

## The brief

### Goal

Revise each spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read each spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge. Re-derive each PINNED count with the command the
   spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every new member listed
   in Files touched with the legs its guard names on the gates section's leg line, and a prose-only mention named as
   outside the population. Cite moved lines as `path#symbol` or blob-pinned, never a bare `path:line`.
   What is built so far:
   - Built: unit 26 (`7526c98fa`, the `resolve_bash_py` block, `scan_bare_bash`); unit 27 (`8b3aa5783`,
     `tools/lib/refuse-wrong-shell.sh`, section `2n`); unit 48 (`15bb9de79`); unit 49 (`ebe9575ea`); unit 13
     (`9cdebebc4`, red-fixes `a96cb1dec` and `15710a90a`: `tools/lib/legacy_ledger.py` with `read_rows`,
     `read_registrations` over every tracked `kit.toml` and the `DEPLOYER_HOME` registry, `read_renames`,
     `compare_to_base`, `write_rows`, the CLI `read|compare|carry` with `compare --measured <path>`, inline copies in
     memory-tree and gate-lint, the ledger class in `tools/memory-tree/merge-rows.py`, section `2o`). Unit 50 (rev-4)
     is building now.
   - Queued from re-grounded specs, each the contract for what will exist: unit 15 (rev-8: `test.seed`), unit 12
     (rev-6: `leg`, `check`, `pack` tag namespaces, `tag` on every leg, `[[numbered_check]]` tables), unit 61 (rev-3),
     unit 22 (rev-4: `tests` edge field), unit 47 (rev-6), unit 19 (rev-4: the leg's `purpose`), unit 11 (rev-6: the
     gate-leg factory), unit 14 (rev-7: the `ratchet` leg pack), unit 45 (rev-3) and unit 54 (rev-4), which land in one
     merge, unit 16 (rev-6: gov's registries converted onto the ledger; §8 F7 leaves `positional-refs.txt`,
     `unpinned-facts.txt` and `positional-producers.txt` to unit 18), unit 46 (rev-5: `--seed-pins`).
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. Unit 16's re-ground (§8 F7) leaves `positional-refs.txt`, `unpinned-facts.txt` and `positional-producers.txt` to
   unit 18. Unit 18's spec homes the first two under `tools/playbook/`; they live under `memory/project/` at HEAD. It
   does not name `positional-producers.txt`; add it with its reader and the legs its guard names.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-17, TOOL-dWitnessedBar-18. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-17.md`, `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-18.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.

**Serves:** journal TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16

# Brief — dWitnessedBar: TOOL-dWitnessedBar-14, TOOL-dWitnessedBar-16 re-grounded on the tree as built, before dispatch

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
   - Built: unit 26 (`7526c98fa`, the `resolve_bash_py` block, `scan_bare_bash`); unit 27 (`cc35bb62c`,
     `tools/lib/refuse-wrong-shell.sh`, section `2n`); unit 48 (`75a15d9ce`); unit 49 (`ef33493d7`); unit 13
     (`34f8bb7db`, red-fixes `010323e92` and `2bd7e6e36`: `tools/lib/legacy_ledger.py` with `read_rows`,
     `read_registrations` over every tracked `kit.toml` and the `DEPLOYER_HOME` registry, `read_renames`,
     `compare_to_base`, `write_rows`, the CLI `read|compare|carry` with `compare --measured <path>`, inline copies in
     memory-tree and gate-lint, the ledger class in `tools/memory-tree/merge-rows.py`, section `2o`). Unit 50 (`2b4d10063`, red-fix `cb93e79f0`: `--coverage` in `tools/lib/refuse-wrong-shell.sh`).
     Unit 15 (rev-8: `test.seed` at every check's registration) is building now.
   - Queued from re-grounded specs, each the contract for what will exist: unit 12
     (rev-6: `leg`, `check`, `pack` tag namespaces, `tag` on every leg, `[[numbered_check]]` tables), unit 61 (rev-3),
     unit 22 (rev-4: `tests` edge field), unit 47 (rev-6), unit 19 (rev-4: the leg's `purpose`), unit 11 (rev-6: the
     gate-leg factory), unit 14 (rev-7: the `ratchet` leg pack), unit 45 (rev-3) and unit 54 (rev-4), which land in one
     merge, unit 16 (rev-6: gov's registries converted onto the ledger; §8 F7 leaves `positional-refs.txt`,
     `unpinned-facts.txt` and `positional-producers.txt` to unit 18), unit 46 (rev-5: `--seed-pins`).
   - Also queued: unit 17 (rev-4: the seven record and row pins as keyed populations), unit 18 (rev-5: §8 F4 —
     `positional-refs` registers in `tools/playbook/kit.toml`, the other lists and `landed-steps` in
     `tools/govkit/registry.toml`; §8 F6 — `landed-steps` graded by `leg = "ratchet (both ways)"`), unit 52 (rev-3),
     unit 53 (rev-3).
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. Two findings from the units 17 and 18 re-ground bind this pair:
   - Unit 14 S6 (the both-ways compare) prints a registration whose `leg` names its own leg as `graded by` rather
     than grading it. Units 17 (§8 F5) and 18 (§8 F6) register `date-cutoffs` and `landed-steps` with
     `leg = "ratchet (both ways)"`, so S6 must GRADE a registration that names that leg. Settle S6 and its criteria.
   - Unit 16 registers two populations in `tools/govkit/entries/*.kit.toml`, but unit 13's landed
     `read_registrations` reads only files named exactly `kit.toml` (and the `DEPLOYER_HOME` registry). Re-home those
     registrations where the reader sees them, or settle it as a fork by M3.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-14, TOOL-dWitnessedBar-16. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md`, `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.

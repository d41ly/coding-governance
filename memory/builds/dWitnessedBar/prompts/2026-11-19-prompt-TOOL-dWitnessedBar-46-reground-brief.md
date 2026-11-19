**Serves:** journal TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-54

# Brief — dWitnessedBar: TOOL-dWitnessedBar-46, TOOL-dWitnessedBar-54 re-grounded on the tree as built, before dispatch

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
   - Built: unit 26 (`7526c98fa`, the `resolve_bash_py` block `scan_bash` / `scanBash`, `scan_bare_bash` in
     `tools/run-gates/measure_legs.py`); unit 27 (`cc35bb62c`, `tools/lib/refuse-wrong-shell.sh` in every
     `resolve_python` member, section `2n`); unit 48 (`75a15d9ce`, row_grammar's resolver an adapter); unit 49
     (`ef33493d7`, shape 4 of `scan_bare_bash`). Unit 13 (rev-4) is building now; unit 50 (rev-4) builds after it.
   - Queued from re-grounded specs, each the contract for what will exist: unit 13 (rev-4: `tools/lib/legacy_ledger.py`
     with `read_rows`, `read_registrations`, `read_renames`, `compare_to_base`, `write_rows`, the CLI verbs
     `read|compare|carry` with `compare --measured <path>`, parity row `legacy_ledger_py`, section `2o`); unit 15
     (rev-8: `test.seed`); unit 12 (rev-6: the `leg`, `check`, `pack` tag namespaces, `tag` on every leg, `LEG_KEYS`
     gaining `tag`, `[[numbered_check]]` tables); unit 61 (rev-3); unit 22 (rev-4: `tests` edge field on legs); unit 47
     (rev-6); unit 19 (rev-4: the leg's `purpose` field); unit 11 (rev-6: the gate-leg factory, declaration order, the
     factory rendering `pass_leg`); unit 14 (rev-7: the `ratchet` leg pack, `retrofit.widen`); unit 45 (rev-3, §8 F3:
     units 45 and 54 land in one merge, 45 first).
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. Unit 45's re-ground (§8 F3) couples it with unit 54: govkit selfcheck's `_gwbad` test refuses any `when` outside
   `<conf>:<KEY>=<value>`, unit 54 S2 widens that test, and unit 54 S3 needs unit 45's `exists:` reading in `regen.py`,
   so both land in one merge, 45 first, under one bar. Make unit 54's Rollout agree.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-54` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-46, TOOL-dWitnessedBar-54. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-46.md`, `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-54.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.

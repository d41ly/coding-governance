**Serves:** journal TOOL-dWitnessedBar-16

# Brief — dWitnessedBar: TOOL-dWitnessedBar-16 revised over its second builder's divergence

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 16's second builder stopped at a divergence before writing any
code, against the rev-10 spec; the spec is revised by its writer before a third dispatch.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD.

### Items

1. Read the second builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-16-2-builder-return.md`, whole, and
   settle its three points in one revision, against the landed `tools/lib/legacy_ledger.py` and
   `tools/memory-tree/ratchet.py`:
   - Every registration's `seed` argv. The landed `seed_population`, `run_unarmed` and `run_seed_laundering` need an
     argv that measures each population as keyed rows; none of the converted populations has one, and most readers
     have no measure mode. Name each population's seed, or state one rule (for example, that a hand-curated
     population's seed reads its own tracked home back) that `run_unarmed`, `run_seed_laundering` and S3's `present`
     all accept, and carry what it adds into Scope, Files touched and Acceptance. The choice is a fork for item 3; keep
     the unit no larger than the rule needs.
   - The empty homes: §5 says an empty population reads `unarmed`, but the landed `run_populated` fails an armed home
     with a seed and no rows until unit 7 lands, and seven converted homes are empty today. Say what those homes are at
     this pass so §5, §7 and the bar agree.
   - `readme-contract.txt`: its conversion rides a main-loop commit after the pass, so a reader of it accepts both
     grammars for that commit's span. Name that transitional read, its removal (in this unit's own follow-up commit or a
     named later unit) and the acceptance that observes the removal, so S4 and AC3 hold once it is gone.
   Also state the gap the builder noted: after S6's rename, `test_codebase_map.py` still passes `baseline.toml`, so the
   baseline's never-gains check reads UNGRADED until unit 51 lands.
2. The spec is already over its size budget (warn mode). Where the revision adds text, tighten wording elsewhere rather
   than grow it, without changing a claim the builders have checked. Leave carried clause tokens byte-identical;
   blob-pin only code-file line citations.
3. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-16`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/memory-tree/gen_build_index.py --check-coverage`,
and fix every finding about this spec they name. Write no numeric fact without an id, a path:line, PINNED or DERIVED on
its line.

### Acceptance

The three commands exit 0; the spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-16. No product code. No change to Goal or Scope intent beyond what the divergence
forces.

### Limitations

The status header keeps its status. The write grant is
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md` alone.

### Reuse

The spec's §10 seam, and unit 14's `conf-scalar-pins` registration as the landed precedent for a seed.

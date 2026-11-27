**Serves:** journal TOOL-dTotalRecall-62
**Caused-by:** TOOL-dTotalRecall-62

# Build brief — TOOL-dTotalRecall-62, a spec-amendment unit built by the spec writer

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 62's whole deliverable is the amendment text it writes into the
specs of units 52 and 59; the write gate admits a spec write from the spec writer alone, so this unit's pass is the
writer's edit and the main loop's pass commit.

## The brief

### Goal

Apply `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-62.md` (rev-3, INPROGRESS) to the specs of units
52 and 59 exactly as its §2 and §4 state, so its AC1 holds at this pass's tip.

### Items

1. Unit 52 is at rev-5 (`0d962fa0c`): unit 43's divergence fold moved the `record-kinds-legacy` merge into it as S4 and
   AC5 (unit 43 §8 F6). Apply unit 62's S1 and S2 over that text: unit 52 builds no `absorbs` re-key (no `absorbs` line
   in its registration block, nothing for the field in Inventory, Files touched, §5 or §7's New arm), and its AC2 reads
   the run's real merge-base (`check_new_at_base` true, `compare_to_base` naming no `gained` key), its title and §1 saying
   why. Keep S4 and AC5, the merge itself, as rev-5 states them.
2. Apply unit 62's S3 to unit 59: its S2 states that unit 52 builds no `absorbs`, its AC2 stands as the observation of
   that, its title, §4, §5 and consumes-from line carry no cut, its S1 and AC1 name the `new at` reading, and its S3
   fixture proof stands.
3. Bump each amended spec's rev by one and add one §9 line `amended by TOOL-dTotalRecall-62` naming this brief's file
   stem; an amendment the target already holds is counted present and named so (unit 62 S4). Keep every edge's mirror
   with its sibling (hygiene check 12).
4. Each amended spec's status header keeps `DEFERRED`. Unit 62's own spec is not yours to edit: the main loop flips it.

Before returning, run unit 62's AC1 (`grep -n "absorbs = "` over spec 52 prints nothing, `grep -c "check_new_at_base"`
over spec 52 prints at least 1, `grep -c "amended by TOOL-dTotalRecall-62"` prints at least 1 for each of specs 52 and
59), then `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-52 TOOL-dTotalRecall-59` and
`python tools/check-spec-tokens.py --spec <path>` over each amended spec, and fix every finding they name. A §8
resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`; every number carries an id, a path:line, PINNED or
DERIVED on its line. Do not commit.

### Acceptance

Unit 62's AC1 holds over the two amended specs, and the check commands exit 0 for each.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec outside units 52 and 59.

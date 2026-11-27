**Serves:** journal TOOL-dTotalRecall-61
**Caused-by:** TOOL-dTotalRecall-61

# Build brief — TOOL-dTotalRecall-61, a spec-amendment unit built by the spec writer

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 61's whole deliverable is the amendment text it writes into the
specs of units 53, 55, 56 and 57; the write gate admits a spec write from the spec writer alone, so this unit's pass is
the writer's edit and the main loop's pass commit.

## The brief

### Goal

Apply `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-61.md` (rev-3, INPROGRESS) to the specs of units
53, 55, 56 and 57 exactly as its §4 "The amendments" states, so its AC1 holds at this pass's tip.

### Items

1. Write each amendment §4 gives into the spec it names (unit 53's S2, S22, S34, AC1 and AC34 text; units 55, 56 and 57
   as §4 states), keeping every other line of those specs as it stands. Unit 50 (CLOSED at `7f51d13dd`) landed
   `CAUSE_WRITER_KEPT`'s eight build-folder rows keyed by repository path and `CAUSE_WRITER_PINNED`'s row; unit 40
   (CLOSED) landed `ALIAS_COMPARE_KEPT` keyed under the tool root. Where §4's text cites either, check it against
   `tools/memory-tree/record_causes.py` and `tools/memory-tree/record_kinds.py` at HEAD.
2. Bump each amended spec's rev by one and add one §9 line naming `TOOL-dTotalRecall-61` and this brief's file stem.
3. Each amended spec's status header keeps `DEFERRED`. Unit 61's own spec is not yours to edit: the main loop flips it.

Before returning, run unit 61's AC1 (`grep -n "stays in its constant at this pass"` over spec 53, and
`grep -c TOOL-dTotalRecall-61` over the §9 of specs 53, 55, 56 and 57), then
`bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-53 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57`
and `python tools/check-spec-tokens.py --spec <path>` over each amended spec, and fix every finding they name. A §8
resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`; every number carries an id, a path:line, PINNED or
DERIVED on its line. Do not commit.

### Acceptance

Unit 61's AC1 holds over the four amended specs, and the check commands exit 0 for each.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec outside units 53, 55, 56 and 57.

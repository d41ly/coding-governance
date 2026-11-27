**Serves:** journal TOOL-dTotalRecall-63

# Build brief — TOOL-dTotalRecall-63, a spec-amendment unit built by the spec writer

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 63's whole deliverable is an amendment to
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md`; the write gate admits a spec
write from the spec writer alone, so this unit's pass is the writer's edit and the main loop's pass commit.

## The brief

### Goal

Apply `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-63.md` (rev-4, INPROGRESS) to unit 46's
spec exactly as its §4 "The amendment to unit 46" states, so its AC1 holds at this pass's tip.

### Items

1. Unit 46's AC1 gains, after its present first sentence, the clause and fixture §4 quotes, and its present
   Red-when line, which names `IndexError` alone, gives way to §4's. Keep every other line of spec 46 as it
   stands: its own re-check runs after units 63 and 64 are built.
2. Bump spec 46's rev by one and add one §9 line in the form §4 gives:
   `rev-<N> · 2026-11-22 · AC1 · the cited-family case, added by TOOL-dTotalRecall-63 (id 3, item H3 shared with id 22)`.
3. Spec 46's status header keeps `DEFERRED`. Unit 63's own spec is not yours to edit: the main loop flips it.

Before returning, run `grep -n "ZED-aFoo-2"` and `grep -c "added by TOOL-dTotalRecall-63"` over spec 46 (unit 63's
AC1), `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-46`,
`python tools/check-spec-tokens.py --spec <spec 46>` and `python tools/playbook/writing_practice.py check pinned-facts`,
and fix every finding they name in spec 46. The write grant is spec 46 alone; do not commit.

### Acceptance

Unit 63's AC1 reads green over spec 46; the three checks exit 0 or read green.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other change to spec 46; unit 64 amends its S1, §4 and edge after this pass. No product code.

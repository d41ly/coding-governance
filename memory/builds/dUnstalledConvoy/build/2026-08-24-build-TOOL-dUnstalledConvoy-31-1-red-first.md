# TOOL-dUnstalledConvoy-31 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-31

The arms are case 3h3 of `tools/run-gates/run-gates.test.sh`, shared with
`TOOL-dUnstalledConvoy-32` because the two read the same fixture: five legs across two chunks, one
chunk mixed and one entirely held. Building them apart would have meant two fixtures asserting
about one run.

The red-first pass applied the ARMS ALONE, against the runner as `2f13349c` left it.

## The arms, and the break each one was observed against

| arm | red-first verdict |
|---|---|
| AC1 the total is the count that RAN | RED — `gates GREEN — 5/5 legs passed` when two ran |
| AC2 the summary names the held population | RED — same line, no note at all |
| AC3 the recorded `ran` figure equals the printed total | RED — the verdict record said `ran 5` |
| AC3b the held count is on the record | RED — there was no `held` field |
| AC4 with the switch on, the total is the whole manifest | **passes without the fix** |

AC4 is a control: with the switch on nothing is held, so the pre-fix arithmetic was already right.
It is kept because a note that survives a run with nothing to report is the same defect pointing the
other way.

## What made the smaller number honest

`82/82` with no explanation reads as a bar that shrank for reasons nobody recorded, so the note names
the population and the remedy in the same breath. `held` is a separate tally from `skipped` for the
same reason the leg verb is separate: a guard-skip runs again when its path moves, a held leg runs
when somebody sets a variable, and a reader who cannot tell them apart waits for the wrong one.

`ran` is computed ONCE and read by stdout, the durable summary and the verdict record. Three call
sites recomputing one figure is how two of them come to disagree, and this is the figure a reader
quotes.

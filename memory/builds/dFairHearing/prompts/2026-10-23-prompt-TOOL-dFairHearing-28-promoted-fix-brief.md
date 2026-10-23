**Serves:** research TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32

# Promoted-units fix brief, round three — one writer per unit, each its own files only

The round-3 spec audit (`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`) promoted five units; `memory/builds/dFairHearing/RUN.md` carries their `rescope · item add` rows. Before the round-4 audit pins them, do YOUR unit's row, the unit your handoff names, and touch no other file. The specs are uncommitted at rev-1 and unaudited: edit in place, with no rev bump. Do not commit, stage, or run the build-index generator or any gate.

## Every unit — one departure record

Write it in the grammar of `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-20-deviation-201.md`:

- **Departs from:** `dFairHearing [roster]`
- **Hand-off:** `design-to-spec`
- **Cause:** `review finding`
- **Risk:** `additive`
- **Approver:** the spec writer, under `author-recorded` (`PLAY-dClosedLoop-4`)
- **Follow-through:** `new unit <id>`
- **Caused-by:** `PLAY-dClosedLoop-2`
- **Reason:** names the finding it closes, and says this is a spec run, so the unit is carried forward once (`UNATTENDED-STOPS.md` §15).
- **Evidence:** the round-3 audit record, the rescope add row, and the spec.

File it as `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>1.md`, that is `-deviation-281`, `-291`, `-301`, `-311` or `-321`. The Before line names only specced units; there is no `TOOL-dFairHearing-19` spec (it is the build's ask) and no unit 24.

## Per unit

- **TOOL-dFairHearing-28** — the departure record only.
- **TOOL-dFairHearing-29** — hygiene check 25 on its §2 **S2**. The check's trigger is any retirement verb from its list (`tools/memory-tree/check-memory-hygiene.sh`, the trigger and word lists) anywhere in the item, beside any identifier-shaped backticked token in it. If S2 truly retires a named thing, add `**Readers:**` with `by name:` (the readers found by grep) and `by value:` (its readers, or `NO VALUE READERS` and a reason). Otherwise reword it off the verb with no change of meaning. Then the departure record.
- **TOOL-dFairHearing-30** — hygiene check 12: its §6 **AC4** names no backticked witness (`SPEC_WITNESS_CUTOFF`). Give AC4 the backticked command, file or arm that observes it, without changing what it observes. Then the departure record.
- **TOOL-dFairHearing-31** — hygiene check 25 on §2 **S3**, handled as for unit 29. Then the departure record.
- **TOOL-dFairHearing-32** — hygiene check 25 on §2 **S18** and **S23**, handled as for unit 29. Then the departure record.

Report each edit verbatim.

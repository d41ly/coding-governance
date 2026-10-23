**Serves:** research TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40

# Promoted-units fix brief, round five — the last round, one writer per unit, each its own files only

The round-5 spec audit (`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`) promoted three units; `memory/builds/dFairHearing/RUN.md` carries their `rescope · item add` rows.

The owner stopped the audit chain after this round (`memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`), so no audit will read these specs. Write them as you would want a builder to read them unreviewed.

Do YOUR unit's row, the unit your handoff names, and touch no other file. The specs are uncommitted at rev-1: edit in place, with no rev bump. Do not commit, stage, or run the build-index generator or any gate.

## Every unit — one departure record

Write it in the grammar of `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-33-deviation-331.md`, the same fixed fields:

- **Departs from:** `dFairHearing [roster]`
- **Hand-off:** `design-to-spec`
- **Cause:** `review finding`
- **Risk:** `additive`
- **Approver:** the spec writer, under `author-recorded` (`PLAY-dClosedLoop-4`)
- **Follow-through:** `new unit <id>`
- **Caused-by:** `PLAY-dClosedLoop-2`
- **Reason:** names the round-5 finding(s) it closes, says this is a spec run so the unit is carried forward once (`UNATTENDED-STOPS.md` §15), and says no audit names it, citing the owner's record above.
- **Evidence:** the round-5 audit record, the rescope add row, the spec, and the owner's record.
- **Before:** names only specced units (1 to 18, 20 to 23 and 25 to 37).

File it as `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>1.md`, that is `-381`, `-391` or `-401`.

## Per unit

- **TOOL-dFairHearing-38, -39** — the departure record only.
- **TOOL-dFairHearing-40** — two fixes, then the departure record:
  - **`check-spec-tokens.py` `[path]` hit.** §6 cites `3708a705:tools/hooks/agent-cap.test.sh`. Write it without a path-shaped token in §6, for example "base `3708a705`'s `agent-cap.test.sh`"; the full path stays in §2 or §4.
  - **Hygiene check 25 on §2 S20.** The trigger is a retirement verb from its list (`tools/memory-tree/check-memory-hygiene.sh`, the trigger and word lists) anywhere in the item, beside any identifier-shaped backticked token. If S20 truly retires a named thing, add `**Readers:**` with `by name:` (readers found by grep) and `by value:` (readers, or `NO VALUE READERS` and a reason). Otherwise reword it off the verb with no change of meaning.

Report each edit verbatim.

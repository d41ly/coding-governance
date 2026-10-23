**Serves:** research TOOL-dFairHearing-4 TOOL-dFairHearing-18 TOOL-dFairHearing-27 TOOL-dFairHearing-25

# Edge-fix brief — three hygiene refusals over the spec set, one writer per unit

The full hygiene check refuses three things. Do YOUR unit's row, the unit your handoff names, and touch no other file. Do not commit, stage, or run the build-index generator or any gate.

- **TOOL-dFairHearing-4** — check 12. `TOOL-dFairHearing-12`'s §3 declares **consumes-from** `TOOL-dFairHearing-4`, and spec 4 declares no matching **hands-off** `TOOL-dFairHearing-12` back.
  - Read spec 12's edge and what it consumes. Add the matching hands-off line to spec 4's §3, naming what spec 4 hands over. If spec 4 does not in fact produce it, say so in your report instead of adding the edge.
  - Spec 4 was audited, so this is a `rev-N+1` bump with a §9 line naming the disagreement (build method M2: a disagreement is fixed in exactly one document).
  - Then also correct the **Before:** line of `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-25-deviation-251.md`. It names an id range ending at `TOOL-dFairHearing-24`, a unit that does not exist. State the specced units before it instead, 1 to 18 and 20 to 23, with no `24`. Change nothing else in that record.
- **TOOL-dFairHearing-18** — check 12. `TOOL-dFairHearing-14`'s §3 declares **hands-off** `TOOL-dFairHearing-18`, and spec 18 declares no matching **consumes-from** `TOOL-dFairHearing-14` back.
  - Read spec 14's edge. Add the matching consumes-from line to spec 18's §3, or report why spec 18 consumes nothing of 14.
  - Make it a `rev-N+1` bump with a §9 line.
- **TOOL-dFairHearing-27** — check 25 (`memory/HYGIENE.md` item 25). Its §2 S22 reads as retiring a named thing: the trigger is any listed retirement verb anywhere in the item, beside any identifier-shaped backticked token in it (`tools/memory-tree/check-memory-hygiene.sh`, the trigger and its word lists).
  - If S22 does retire a named thing, add a `**Readers:**` clause with `by name:`, the readers that spell the name found by grep, then `by value:`, its readers or `NO VALUE READERS` and a reason.
  - If it does not, reword it off the verb with no change of meaning.
  - Spec 27 is unaudited at rev-1: edit in place, no bump.

Report each edit verbatim, and each new status header.

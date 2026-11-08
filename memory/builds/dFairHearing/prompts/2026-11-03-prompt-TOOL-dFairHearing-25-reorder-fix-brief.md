# Fix brief — the replay units 25, 30 and 35 ordered after the units that correct their procedure

**Serves:** research TOOL-dFairHearing-25 TOOL-dFairHearing-30 TOOL-dFairHearing-35

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Fix an ordering defect on M2's ordering axis ("no sub-spec depends on a unit sequenced after it"). Units 25 (order 20), 30 (order 21) and 35 (order 22) run the build's blind replays: replay 1's two design-audit runs and unit 15's eight with-and-without runs. Units sequenced after them correct the procedure those runs follow: unit 27 S22 (the clone's EXIT trap), unit 32 S13 to S21 (the orchestrating-commit binding, the placement step, per-attempt clone names, the void and re-run cap), and units 36, 37 and 40 refining 30 and 32. Running the replays first would spend about ten full review runs on a procedure about to change, and a repair unit (M4) corrects an UNBUILT sibling's spec, which 25, 30 and 35 would no longer be. Commit nothing; the main loop commits.

### Items
1. Read every unbuilt spec's §3 Edges (units 25, 27 to 40) and list each `consumes-from` and `hands-off` that names 25, 30 or 35, in both directions.
2. Give 25, 30 and 35 orders after every unit that corrects their procedure or spec, keeping their own relative order (25, then 30, then 35) and every `consumes-from` edge satisfied; the header `order N` is the field. If a unit after them consumes from one of them, say so and order it after too, or report the cycle.
3. If any of those specs states its order or its position in a sentence (for example "ordered directly after unit 23"), re-word it to match.
4. Rev bump and one §9 line per spec touched, naming this brief. Leave each status header's state as it is.

### Acceptance
After the edit, no unbuilt unit's spec is corrected by a unit ordered after it, and no `consumes-from` edge points forward. The return lists each spec's old and new order.

### Gates
None you run.

### Non-goals
No change to any replay's design, bar or procedure; only order fields and order sentences. No code.

---
name: a-terminal-spec-named-by-a-pass-splits-the-waiver-joins
description: closing a spec makes its spec-token waiver stale to the bar join, while the pass join still grades that spec when a commit names it, so no waiver row satisfies both
kind: class
---

# A terminal spec named by a pass splits the two waiver joins

## Symptom

The push bar reds `spec tokens (the pass's own spec)` with one unwaived `[path]` hit in a CLOSED
spec. The row that waived the hit was deleted one commit earlier, because the same bar's
`spec tokens (a spec's own names resolve)` called it a `STALE WAIVER`. Put the row back and the
second leg reds. Take it out and the first one does.

## Where it bit

Node d, 2026-11-14, landing `branch/d-builds-clarification-dfddc4`. The close-out flipped
`TOOL-dPolishedVitrine-1` to CLOSED. The bar join grades live specs only, so the waiver for that
spec's citation of a since-deleted ledger file produced no hit and read stale. The fix commit
deleted the row and named the unit in its subject. `--pass-spec` takes the newest unit the range
names and grades its spec "whatever their status", so it graded the closed spec and found the
citation unwaived.

## The fix

The two joins disagree about one population: the bar join excludes terminal specs, and the pass
join includes the one a commit names. Until one rule governs both, a commit that removes a waiver
row for a terminal spec must not name that spec's unit in its subject or `Pass:` trailer. The commit
that removes the row is records work, not a pass over the unit.

No machine gate yet. The gate that fits is in `tools/check-spec-tokens.py`: the stale-waiver check
should count a row as live while any spec the pass join can reach still produces its hit, or the
pass join should skip a terminal spec the way the bar join does.

# TOOL-dTracedLattice-7 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-7

**Evidences:** TOOL-dTracedLattice-7
- AC1 — `python tools/memory-recall/test_recall_floor.py` — the arm `rm3 is seed-stable (S3 / AC1)` runs the same query under `PYTHONHASHSEED` 0, 1, 7, 42 and 1234, one SUBPROCESS each because the interpreter reads that variable at start-up, and asserts identical rankings. Observed RED against the shipped implementation: `rm3 returned different rankings under different PYTHONHASHSEED values … 0=['target-cand02…`. Green after: `identical across 5 seeds`
- AC2 — `python tools/memory-recall/selftest.py` — `verbatim.json`'s `bench.py` pin moved `5a46060ffb2008fc` to `8006144bcb9d0839` in the same commit as the change. A pin updated later is a window in which the assertion passes against the wrong bytes
- AC3 — amended rev-4, and measured both ways — `python tools/memory-recall/bench.py <data> <fixture> --sets records --subs rm3` under seeds 0, 7 and 1234 reports `0.29` on every run, BEFORE the fix and after. That is not stability, it is a metric that cannot see the defect: over a symmetric candidate set the aggregate recall counts how many queries hit, and exactly `RM3_TERMS` of them hit whichever terms were chosen. The RANKING moves and the score does not, so the criterion now grades the ranking
- AC4 — `tools/memory-recall/README.md` — names `grep`, `fts5` and `fts5w` as measured seed-stable, `rm3` as the one that was not and now is, with the mechanism, and states plainly that the dense and hybrid substrates are NOT covered by the arm and nobody has measured them
- S1 — `tools/memory-recall/bench.py` `run_rm3` — BOTH halves, because either alone leaves the other free: the deduped terms are sorted before `Counter.update`, fixing the insertion order that `set` iteration made seed-dependent, and the selection uses an explicit `(-count, term)` key instead of inheriting `most_common`'s insertion-order tie-break

## The fixture is the work, and a naive one proves nothing

A corpus with no tie has nothing for a tie-break to get wrong. The first fixture — twelve identical
documents — returned the same ids on every seed against the SHIPPED implementation, which reads as a
pass and is a fixture that cannot fail. The one that discriminates puts 24 candidate terms at
IDENTICAL document frequency across the `RM3_DOCS` seed documents, so `most_common` is deciding a
24-way tie and nothing but its rule separates them, then gives each candidate its own target
document so the chosen `RM3_TERMS` are visible in the retrieved ids. The arm carries that
construction in its own header, and asserts it retrieved at least one expansion target before
comparing anything.

## Five seeds, not three

The criterion asks for at least three. The pre-fix implementation agreed with itself across some
seed PAIRS by luck, so a two-seed arm can be green on a broken build; five was the smallest count
that reddened every time it was run.

## What this ledger does not evidence

`rm3` is not this repository's pinned floor substrate — `.memory-tree.conf` pins `records:fts5`— so
the merge bar is not where this fix is verified. `recall floor arms` is, and that leg is HELD on a
plain bar, which §7 now says correctly after the round-3 fold caught it saying the opposite. Nothing
here measures whether `rm3` is a GOOD substrate; §3 puts that out of scope and this unit only makes
it reproducible.

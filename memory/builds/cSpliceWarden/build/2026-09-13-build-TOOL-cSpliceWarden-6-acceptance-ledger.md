# Acceptance ledger — TOOL-cSpliceWarden-6, the rotation-mode grader

**Serves:** journal TOOL-cSpliceWarden-6

Every criterion is answered by something RUN on node `c` on 2026-09-13. Two of the five were observed
on the REAL tree by staging a break into it and reverting; the rest are fixture arms in
`row_grammar.py --selftest`, which passes 31 arms with this unit's eight added.

**Evidences:** TOOL-cSpliceWarden-6

- AC1 — `row_grammar.py --check-rotation` over the real tree, with one scratch row at status OPEN
  appended to `memory/archive/TOOL.2026-08-14.md`, named that row with its status and its line 55,
  and reported clean once it was removed. The fixture arm asserts the same over `ARCH-tStay-1`, whose
  id this ledger may spell because the fixture defines it.
- AC2 — `--check-rotation` over a fixture whose shard and archive both carry `ARCH-tBoth-1`
  reported that the pair does not partition the family and named that id. Confirmed on the real tree
  too, by re-adding an already-archived id to `memory/backlog/TOOL.md` and reverting.
- AC3 — the fixture arm over `ARCH-tBold-1` holds: a bold-wrapped id in a cut archive is still a
  row and is still graded. Confirmed on the real tree with a bold-wrapped scratch row at status
  SPECCED, which was named. This is the evasion that killed the shell implementation — it passed
  there, and `memory/DECISIONS.md` carries fifteen bold-wrapped ids, so the exclusivity arm was blind
  to fifteen live rows on the day it was written.
- AC4 — with `ROTATION_MODE` set to `snapshot` and then to blank, `--check-rotation` exited 0 and
  said in each case that the mode is not graded and how many archives that leaves ungraded. Observed
  on the real tree by setting each value and reverting, and pinned by two fixture arms.
- AC5 — over a fixture tree carrying a live shard and no archive at all, `--check-rotation` under
  `cut` printed that it graded NOTHING rather than reporting clean. That is the anti-vacuity branch,
  and without it a green here would be coverage of an empty population.

## What this ledger does NOT evidence

Nothing here observes anything about `snapshot`. Its assertion is not implemented, deliberately, and
§4 of the spec carries the measurement showing its baseline commit is not resolvable in this repo's
history shape. A tree declaring `snapshot` gets an announcement and no coverage, and that is the
honest state rather than an oversight.

Nothing here observes the CONTENT of any archive. Check 24 grades the partition — terminal-only and
disjoint — never whether the rows in an archive are the right rows or their status true.

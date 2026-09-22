# cMendedVintage — the acceptance ledger for unit 4

**Serves:** journal DEPL-cMendedVintage-4

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commit, `81ce02a4`, 2026-09-16. Where a criterion is
answered by a command it was replayed at the shell against this worktree and its result is given;
where it is answered by what the building pass measured, the commit or the spec's own revision log
is cited AS the record and named as such. No merge bar, no `*.test.sh` and no self-test runner ran
in this pass: `tools/govkit/selftest.py` was READ, never executed, and the one predicate replayed
below was replayed by a standalone script rather than by running that suite.*

## The one thing worth reading twice

**The class predicate was observed both ways here, at this tip and at the build's BASE, and the
BASE observation is the one that matters.** A predicate that passes proves nothing until the
population it grades is known non-empty and known to contain the defect. Replayed over
`tools/govkit/govkit.py` at base `859daa67`: two string literals name both `unattributed` and
`--re-adopt`, and exactly one of them omits `--pin` — the withheld-stamp remedy this unit rewrites.
At this tip the population is still two and none omits `--pin`. figure: DERIVED at observation
time, both sides.

**AC1's behavioural half is NOT observed, and the spec says so itself.** Rev-3 note (e) records
that running the printed command and re-reading the row's evidence "is observed only by the new
selftest arm, which this pass did not run; it is owed to the bar at close". This ledger does not
improve on that, and AC5 is owed for the same reason: its arm lives in the same unrun fixture block.

**Evidences:** DEPL-cMendedVintage-4

- AC1 — `tools/govkit/selftest.py` — the criterion's FIRST half is observed here: the withheld-stamp
  branch in `tools/govkit/govkit.py`, read at this tip, prints
  `govkit adopt --re-adopt --pin <path>=<rev> --write`, which names `--re-adopt`, `--pin` and
  `--write`, and it is now the same form the sibling remedy in that file has printed since
  `DEPL-dCarriedReceipt-13`. The SECOND half — that running exactly that printed command leaves the
  row's `evidence` reading `pinned` — is NOT observed by anybody. It needs the `dGV-8` ungraded-row
  fixture, so it lives inside the suite, and the spec's own rev-3 note (e) records that the building
  pass did not run it and that it is owed at the run's close. It is still owed.
- AC2 — `python tools/govkit/govkit.py update --target /nonexistent-target --write --allow-ungraded`
  — replayed at this tip. Exit 2, printing
  `govkit: unknown or incomplete argument: --allow-ungraded`.
  The refusal comes out of `parse_args`, which walks argv before the verb is
  dispatched, so the nonexistent target was never read and the refusal is the argv one and not a
  target failure. The criterion's Red-when — the flag gone from the docs and left in the parser — is
  closed in the direction that matters here: the `USAGE` synopsis line for `update` now offers
  `[--to <rev>] [--write] [--write-withdrawals]` and nothing else, and the parser refuses the name.
- AC3 — `grep -c 'allow_ungraded' tools/govkit/govkit.py` — replayed at this tip: prints `0`, exit 1,
  which is grep's no-match code and not a failure. The Red-when this criterion names as likeliest —
  the `parse_args` return element, whose removal changes an unpack in another function — is closed:
  the tuple element, its unpack in `main` and the keyword pass to `cmd_update` all went in the same
  commit. The predicate is KNOWN too narrow and is deliberately left as written: commit `81ce02a4`
  records fifteen occurrences removed across three spellings on fourteen lines, of which this
  pattern sees eight, and `DEPL-cMendedVintage-20` owns widening it. The two spellings this
  criterion cannot see were re-derived here anyway and are also zero.
- AC4 — `tools/govkit/govkit.py` — observed twice. The commit records the RED three ways: the class
  predicate reds on shipped HEAD naming exactly the remedy this commit fixes, reds again on a staged
  extra string, and its liveness arm reds when the population is emptied. Replayed here at this tip
  and at base `859daa67` by a standalone `ast` walk that reproduces the committed arm's predicate —
  same literal collection, same `JoinedStr` handling, same scoping on `unattributed` — rather than
  by running the suite: one violator at BASE, none at this tip, population two on both sides. The
  `ast` read is load-bearing rather than decorative, and that is why a grep would not do: the remedy
  is an implicitly-concatenated f-string whose `unattributed` and `--pin` sit on different source
  lines, so no per-line pattern can see the pair at all.
- AC5 — `dGV-8` — the arm is present and re-pointed, read in `tools/govkit/selftest.py` at this tip.
  It still asserts the receipt is NOT re-stamped by comparing the receipt's stamp against the old
  one, and it now also requires `--re-adopt`, `--pin` and `--write` in the same output, which is the
  corrected remedy. The two `--allow-ungraded` arms that sat beside it are gone with the override,
  which is the deletion S5 asked for, and this arm survived it. What is NOT observed is the arm
  RUNNING: it is in the same fixture block as AC1's behavioural half, which the spec records as
  unrun, so its green is asserted by the file and by nothing else, and it is owed with AC1.

## What this ledger does NOT claim

That the merge bar is green, or that any leg of it ran, in either pass. `govkit selftest` owns every
arm this unit added or rewrote and is unobserved for this unit end to end. That matters more here
than usual: this unit deleted two arms and replaced a third, so the suite is the only thing that
would catch a rewrite that no longer compiles or no longer reaches its subject.

That an adopter was tested, or that a real `unattributed` row was ever cleared by the corrected
remedy. gov holds no `.governance/install.json` of its own, so the only available observation is the
fixture, and the fixture did not run. An operator who follows the new sentence is following a string
this ledger has read and nobody has executed.

That `WIRE-INTO-PROJECT.md`'s rewritten migration paragraph was graded. No criterion covers the
runbook half; the commit records two occurrences of the retired flag removed from it, and a repo-wide
grep at this tip returns no `*.md` hit outside other builds' own frozen records.

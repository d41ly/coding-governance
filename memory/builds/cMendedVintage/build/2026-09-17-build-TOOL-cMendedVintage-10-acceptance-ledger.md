# cMendedVintage — the acceptance ledger for unit 10

**Serves:** journal TOOL-cMendedVintage-10

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real driver verb
twice over identical scratch fixtures — once against the BASE driver, once against the patched one —
and diffing the two transcripts byte for byte after scrubbing shas and timestamps.*

## The one thing worth reading twice

**The brief's account of the red is stale, and the red itself is real.** The brief says `--audit`
reports no unit dispatched and open. It does not: on this tree it lists this very unit, because the
main loop parked a dispatch row for it before the pass started. The disagreement the criterion exists
to catch is per-unit, not whole-audit, and it reproduces exactly: `--audit` grades
`DEPL-cMendedVintage-15`
as not open, while check 49 refuses a declaration of
`tools/govkit/govkit.py`
naming that same unit's first row. AC2 is amended to the per-unit shape it was always about, logged
as rev-2, and no other criterion moved.

**The fix had one place it could go badly wrong, and it is not the one the spec named.** The spec's
risk is AC3 — closing a row nothing supersedes. The real trap sits one step earlier: the function is
handed a declared SET, not a row, and `--audit` hands it the UNION of a unit's same-anchor rows. A
test that asked "is this set the last row's set" would have called every multi-row unit superseded,
graded it closed, and made the stall clock structurally incapable of ever reporting STALLED. The
implemented rule therefore resolves the row by the LAST row carrying the identical set and treats an
unmatched set as superseded by nothing, so the audit's union falls through to the commit test exactly
as at BASE. rev-2 writes that into section 4.

**One behavioural change, and the fixture proves it is one.** The scratch transcript diff between the
BASE driver and the patched one is a single hunk: AC1's refusal becomes an acceptance. The
identical-re-declaration case, the new-anchor case, the single-row reservation and the empty-sibling
announcement are byte-identical across the two runs.

**Evidences:** TOOL-cMendedVintage-10

- AC1 — `--dispatch` — on a scratch repo, one unit declared `tools/a.sh`, re-declared at the same
  anchor as `tools/b.sh`, and committed a change to `tools/b.sh` under a subject naming it. A second
  unit then declared `tools/a.sh` — the path only the abandoned row names. The BASE driver answered
  with check 49's non-disjointness refusal naming the first unit; the patched driver answered
  `dispatch declared`
  and announced that the sibling set was empty, which is the same run reporting that BOTH of the
  first unit's rows are now closed rather than one of them going quiet.
- AC2 — amended rev-2 — the criterion's rev-1 premise ("`--audit` reports no unit dispatched and
  open") is false on every tree this unit could be graded against, because the run's own row for this
  unit is open while it runs. Re-phrased per-unit and then observed on the REAL record, in a
  throwaway clone of this worktree at the same HEAD so no live run-state file was touched: at BASE
  the clone refused
  `tools/govkit/govkit.py`
  for `DEPL-cMendedVintage-15` while `--audit` did not list that unit; with the patched driver in the
  same clone the identical command printed
  `dispatch declared`.
  `--audit` over the live tree is unchanged by the patch — same unit, same PROGRESSING verdict,
  before and after — which is the union fall-through doing its job.
- AC3 — `no sibling pass is open` — three controls, all byte-identical between the BASE and patched
  transcripts. A unit whose only row is its first keeps its declared path reserved, and a second unit
  declaring that path is still refused. A second unit declaring a disjoint path is accepted and the
  empty-sibling line does NOT print, because an open sibling exists. With no dispatch row on file at
  all the line DOES print. Two further controls guard the same property from the other side: two rows
  carrying an IDENTICAL set supersede nothing and the reservation holds, and a later row parked at a
  NEW anchor is a different pass rather than a supersession, so that reservation holds too.

## What ran, and what is owed

One checker ran directly, because it grades bytes this commit writes:
`python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`
reports OK over 107 tracked shell files with no undeclared loop fed by a command substitution. The
new loop is fed by a heredoc whose body is a VARIABLE, so it is graded in the reported-not-gated
class and needs no registry row. That stands in for the
`shell hygiene (a loop fed by a command substitution)`
merge-bar leg, which is section 7's fourth gate. `bash -n` over the edited driver was run before any
verb was pointed at it, for the reason the hazard section of the brief gives.

Three of section 7's gates are OWED to the bar the run closes with, and none of them can be observed
from inside a pass that is forbidden to run a gate or a suite: `unattended kit gate`,
`unattended skill wiring`, and `harness arms (fail branches armed or pinned)`. The third is worth a
sentence rather than a shrug: this unit adds NO `fail` branch and rewords none, so neither the branch
floor nor the armed floor can have moved, and the pin is untouched. The first two are owed because
this unit edits the driver the kit gate grades.

The unit's own self-test suite is likewise OWED. It carries the arms that pin the behaviours the
scratch fixture reproduced by hand — the same-anchor union, the identical re-declaration, the
declaration-commit-only case — and those arms were read against the change rather than executed: each
resolves to a single-row or unmatched-set shape, which the implemented rule leaves untouched.

## What the bug-class checklist changed

Run after the commit, from `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`.

`gate-you-have-only-seen-pass` is why the fixture runs twice rather than once. A transcript from the
patched driver alone would have shown three acceptances and proved nothing about which of them the
change caused; the BASE transcript is what makes the single-hunk diff a measurement.

`fixture-passes-by-finding-nothing` is why AC1's two rows declare DIFFERENT files and the pass commit
lands inside the LATER one. Had both rows named the same file, the commit would have closed the first
row at BASE too and the arm would have been green before the change.

`amendment-leaves-its-other-half-standing` was checked against rev-2's own edit: section 3's
non-goals, section 5's risk bullet and the S1 to S3 scope items all still describe the landed shape,
because rev-2 adds a rule section 4 was silent about rather than replacing one it stated.

`ledger-token-wrapped-across-a-line-joins-nothing` is why every backticked span in this record sits
whole on one line.

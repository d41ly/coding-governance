# cMendedVintage — the acceptance ledger for unit 15

**Serves:** journal DEPL-cMendedVintage-15 DEPL-cMendedVintage-10

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
scratch fixture targets at the shell, three times: once clean and once per staged break.*

## The one thing worth reading twice

**The blocker was already closed when this unit started, and not in the shape its spec predicted.**
rev-1 was drafted against a PREDICTION of `DEPL-cMendedVintage-10`, which landed one commit earlier.
It predicted a snapshot entry stamped
`(govkit)`
and asked for two repairs: a restore stage that reaches it and an exclusion in the orphan sweep. What
`-10` actually shipped is the same repair by a different mechanism — the entry is attributed to NO
kit, the restore loop's own selection reads
`x["kit"] == eid or x["origin"] == "attributes"`,
and the sweep is scoped to
`s["origin"] == "table"`.
All three of rev-1's code changes were therefore already in the tree in another spelling. Re-applying
any of them would have been a second answer to one question, so this unit wrote NO engine code. rev-2
records S1, S2 and S3 as DISCHARGED AT BASE and re-states the goal as the thing that was genuinely
missing: nobody had ever executed it.

**So the unit's whole deliverable is the fixture `-10` could not build, and it closes that unit's
OWED criterion.** `-10` recorded AC4 OWED because no fixture in the tree produced a pin block and a
green-to-red kit at once: its own fixture kit declares
`[check] none`,
and the `-14` roll fixture's kits declare no
`[[lf_pin]]`.
The arm this unit lands is a SECOND scratch gov built from the `-14` builders with an
`[[lf_pin]]`
on the kit that rolls back. It runs, and both halves hold.

**Both failing cases were observed, and they separate exactly as the brief predicted.** The gate was
not landed on a green run alone. Two breaks were staged into the COPIED engine, one per half:

- Selection narrowed back to `x["kit"] == eid` — AC2 REDS, and the detail shows why in bytes: the
  file holds `tools/demo/*.txt text eol=lf`, gov's freshly written pin, where the pre-run bytes had
  the fixture's tampered line. AC3 stays GREEN. That is the run that restores everything else and
  leaves gov's block staged in a repository gov does not own.
- The sweep's origin scope removed — AC3 REDS on the line
  `govkit update — verify (no kit): NOT VERIFIED`
  while AC2 stays GREEN. That is the run that puts the block back and still calls it an orphan.

Neither break reds the other's arm, which is what makes the pair worth having rather than one
combined assertion.

**rev-1 predicted the wrong string for the spurious line, too.** It said the run would print
`verify (govkit): NOT VERIFIED`.
Because `-10` chose to attribute the entry to no kit at all, the line the sweep actually produces
when its scope is removed reads `(no kit)`. The arm therefore does not match a literal at all: it
derives the claimed set from the fixture's own receipt at observation time and reds on any
`NOT VERIFIED`
line naming something outside it. A literal would have passed over this rename.

**Evidences:** DEPL-cMendedVintage-15

- AC1 — `origin` — the entry's `kit` is `None` and the restore reaches it by origin, asserted
  through its two observable consequences rather than by printing a run-local structure: the entry is
  restored (AC2) and it is not swept (AC3). Read at the source as well, at the site that builds the
  entry and at the two that consume it, and the comment there states the same reason rev-2 now does.
- AC2 — `.gitattributes` — on a scratch target whose pin block was tampered inside the marker pair
  and committed, `update --write` printed
  `wrote the lf-pin block [spliced]`
  and then `rolled back 1`, and the file came back byte-identical to its pre-run bytes. Both liveness
  halves are asserted because either absence makes the arm vacuous: with no write there is no
  snapshot entry, and with no rollback the restore stage is never entered. The rollback line also
  NAMES the path, which is section 5's observability claim and is asserted separately.
- AC3 — `NOT VERIFIED` — the same run's output carries no such line naming a kit outside the
  fixture's own `install.json` claimed set. The claimed set is read from the receipt at observation
  time and its non-emptiness is asserted, so the arm cannot pass by quantifying over nothing.

**Evidences:** DEPL-cMendedVintage-10

- AC4 — `.gitattributes` — NO LONGER OWED. That unit's ledger records the mechanism as built and
  unexecuted, and its reason was correct at the time: no fixture could stage the green-to-red
  transition on a target that also has a block. This unit's fixture does both, and the observation is
  AC2 above — the block a rolled-back run rewrote holds its pre-run bytes afterwards, with the
  restore reported rather than silent. That unit's own record is left as it stands: it is a landed
  record of what was true when it was written, and this is the second half arriving.

## What did not run, and why

`tools/govkit/selftest.py` gained one arm group and was NOT executed as a suite, by this pass's own
mandate. Instead the arm was replayed OUTSIDE it, expression for expression, against the same engine:
the fixture builders were inlined into a scratch runner, and every expression the shipped arm
evaluates — `marker_pair`, `GA_BLOCK_ID`, `find_block`, the span arithmetic that picks the line above
the close marker, the byte comparison, the receipt read and the
`NOT VERIFIED`
filter — ran verbatim and returned the asserted values. What was NOT replayed is the suite's own
`run()` wrapper; the arm does not use it, driving the engine through `run_in_gov` exactly as the
`-14` block beside it does.

Four gates are owed to the bar this run closes with: `govkit selftest`, `govkit selfcheck`,
`govkit refusal join` and `govkit acceptance matrix`. One checker WAS run directly, because it grades
bytes this commit writes:
`bash tools/check-install-prefix.sh`
reports clean at 268 shipped files with 136 recorded files and none rising. Both changed Python files
were parsed with `ast.parse` rather than compiled by name, so no argv in this pass named a suite.
`python tools/govkit/refusal_join.py` was not run: this unit adds no refusal branch and the engine is
untouched, so its count cannot have moved.

## The finding this unit did not fix

**A THIRD consumer of the synthetic id, which no spec in this build had named.** The per-kit version
delta groups RECEIPT rows by `kit`, so every `update` against a target with a pin block prints
`(govkit)                     gov side unresolvable — no comparison is possible`
as its own row. It is noise rather than a false verdict: nothing is left unrestored and nothing is
called an orphan. It predates this whole build — `apply` has stamped that receipt row since
`DEPL-dCarriedReceipt-2` and the delta table arrived at `DEPL-dGaugedVintage-9` — and closing it means
either changing what `apply` stamps, which rev-1 named as a non-goal and rev-2 keeps, or a second
filter in a report this unit was not scoped to touch. rev-2 records it as a non-goal with that
reasoning rather than leaving it as an undocumented observation.

## What the bug-class checklist changed

Recorded after the commit, from `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`.

`fixture-passes-by-finding-nothing` was the class this unit spent the most care on, and it changed
the fixture twice. The block is TAMPERED rather than left as installed, because an untouched target
reads `current`, writes nothing, and then AC2 compares a file no run ever touched. The pin is
declared on the kit that ROLLS BACK rather than on its green sibling, because a pin on the sibling
still produces a block but the restore stage is entered by the other kit and the coupling is
accidental. Both were checked by observing what the run printed, not by reasoning about it.

`gate-you-have-only-seen-pass` is why the two breaks exist at all, and why they are two rather than
one: a single combined break would have shown the pair red together and said nothing about whether
either arm can fail alone.

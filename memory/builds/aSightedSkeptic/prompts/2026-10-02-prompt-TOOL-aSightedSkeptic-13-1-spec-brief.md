**Serves:** journal TOOL-aSightedSkeptic-13

# Spec brief — TOOL-aSightedSkeptic-13, adopted by the owner on 2026-10-02

**The defect.** Check 23 of the unattended kit gate (`tools/unattended/check-unattended.sh`, the loop
that starts `ds_over=""; ds_over_n=0; ds_graded=0`) skips a run record only when its own `phase` fact
reads `LANDED` or `ABORTED`. This repository lands IN PLACE, so a landed record's file stays
`LANDING` forever, and check 23 re-grades every in-place run that ever landed, on every bar,
walking its whole dispatch history one git call at a time. Its undeclared-write count therefore
carries landed history that can never change, and a landed run's count is charged against every
later run's ceiling.

**The seam that already answers it.** Check 7, a few hundred lines below, excludes a record as
"derived LANDED": phase `LANDING`, its landing commit read by the kit library's
`read_landing_commit`, and that commit an ancestor of the advertised default-branch tip (`ADV_HEAD`,
verified to resolve). It fails CLOSED and says so: no advertisement, or a tip this clone cannot
resolve, keeps the record counted with an unconditional line naming why. Read that block whole,
including its comments, before writing the spec.

**One mechanism.** Check 23 applies the same derived-LANDED exclusion, through ONE predicate both
checks call, so the two cannot drift into two answers. Extracting check 7's inline test into a
named function in the same file (or the kit library, if that is where the gate's other shared
predicates live — decide in §8 by reading where `read_landing_commit` lives) is the expected shape;
name it through `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` (or the cell the
conf declares for shell). Check 23 announces every record it excludes, the way check 7 does, on the
default channel, and announces when the exclusion is UNAVAILABLE.

**The pin.** `UNDECLARED_WRITE_CEILING` in `.unattended.conf` is shrink-only and its comment says to
LOWER it when the count falls and to say in the commit message what closed. Measure the count before
and after on this tree, and lower the pin to the new count in the same unit. Never raise it.

**Scope edges.** Other checks in the same file that loop over `$RUNS` with only a
`LANDED|ABORTED` skip may carry the same defect. Inventory them with a grep and NAME them in §3
Non-goals with their line numbers; do not change them in this unit (one mechanism per spec).

**Universality.** The gate ships to adopters. Nothing here may assume this repo's lander mode: under
`LANDER_MODE=primary` a landed record is rewritten to `LANDED` and the existing skip already covers
it, so the new exclusion must be a no-op there and must say nothing false.

**Kit version.** The unattended kit's version moves once (find every carrier
`tools/check-kit-versions.sh` pairs for the unattended kit; the owner memory says a watched kit file
owes the version in every carrier, plus the manifest's last-audit and last-body-change where
watched).

**§6 witnesses.** A slice of `tools/unattended/check-unattended.test.sh` holding the new arms: a
LANDING record whose landing commit is on the advertised tip is excluded from check 23 and named; one
whose commit is not on it is still graded; no advertisement keeps it graded and prints UNAVAILABLE;
check 7's existing exclusion arms still pass through the shared predicate. Each arm observed RED
against the pre-change gate. The full suite is not run in a pass (it is hours); the main loop runs
the arms' slice and the unattended kit gate leg at VERIFYING. Also: the leg's own count before and
after on this tree, printed by `bash tools/unattended/check-unattended.sh` with `REPORT=1`, which is
the measurement the pin change rests on.

Order verb: `order 13`. Tier-2.

# Build brief — TOOL-cMendedVintage-8

**Serves:** journal TOOL-cMendedVintage-8

Read the spec whole first. Small unit, sharp edges, and one criterion you will not be able to run.

*Standing note: seventeen briefs in this build carried a figure or mechanism measurement disproved,
and every one of the last ten units amended its own spec mid-build after measuring. The last one
found a §4 claim about what `govkit.py` prints today was simply false. Treat this as evidence, not
authority.*

## Why this matters to an adopter

`govkit update` re-runs each kit's `[check]` and rolls the kit back on a red. Because the empty-scope
case and a genuine conf refusal share one exit status, a correctly installed process-monitor can be
WITHDRAWN because of what happened to be running on the machine at that moment. The verdict depends
on the time of day, which is the defect.

## S3 is the guard, and it is the thing that must survive

The refusal handler keeps returning 1, unchanged. A duplicate `PROCMON_ROOTS`, an unparseable conf,
an absent conf, a census that cannot run — all stay failures. The spec builds the discriminator in
the ENGINE and only reads it in the adopter for exactly this reason: a single-line change on the
adopter side would demote the conf-parse refusal along with it, and that refusal is the one thing in
this path that must not become a skip.

Observe that directly. Stage a broken conf and confirm it still exits 1 after your change.

## Your own arm can become the bug it is testing

S6 asks for an arm over a conf whose single root is a real directory nothing runs under. On a heavily
loaded machine that is a claim about machine state — the same class of claim this unit exists to
remove from the verdict. Pick a root that cannot plausibly host a process (a fresh scratch directory
you just made, not a temp root something else might use), and say in the ledger why your choice is
stable rather than assuming it.

## The fixture must actually REACH the delegation

S6's `.test.sh` arm needs the scratch repo to copy `scope.py` and `census.py` beside the adopter, or
the adopter never delegates and the arm passes by finding nothing. That is this repo's named
fixture-passes-by-finding-nothing class, and your spec has already pre-empted it — do not undo the
pre-emption by simplifying the fixture.

## AC6 is half-OWED and you cannot run the other half

`adopt-process-monitor.test.sh` is a `*.test.sh` suite and `gate-guard.js` denies it in this pass, so
that arm ships unexecuted. The `selftest.py` arm you CAN exercise directly. Record the shell arm as
OWED honestly rather than claiming it, and if you can reach its fixture setup by hand — building the
scratch repo and invoking the adopter without the suite harness — do that and say exactly what you
ran, because it is the difference between written and observed.

`FLOOR_ASSERTIONS` in that file moves with your new arm. It is currently 31. That number is a floor
over what the suite executes, so derive the new value from a run rather than incrementing by one on
faith — and if you cannot run the suite, say that the floor was reasoned rather than measured.

## The line numbers are partly stale

`adopt-process-monitor.sh` has moved since this spec was written; `scope.py` has not. Locate the
adopter's branch by symbol and by the text the spec quotes, and do not trust `:228-232`.

## Explicitly out

No change to what `--check-conf` means when roots DO admit live work. No capture of the child's
stderr into the adopter's note. No fix for the path-SPELLING dependency — a root declared in MSYS
form never matching a census carrying Windows spellings — which this unit narrows to a skip and does
not close. No new `[[outcome]]` row, no new gate leg, no predicate over descriptors.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers in test files —
that class has landed twice in this build, both times in a test-side helper. Spell no
`tools/<kit>/…` path in shipped prose or comments.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-8-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line — check 23 is HELD under `--staged`. Re-declare with `--dispatch` if your write
set grows; it refuses a declaration naming `RUN.md`. Bound every command at 900s or more.

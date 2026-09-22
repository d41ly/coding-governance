# Build brief — TOOL-cMendedVintage-10

**Serves:** journal TOOL-cMendedVintage-10

You are fixing the driver that is running this build. Read the spec whole first, then read the
hazard section below before you touch the file.

*Standing note: nine briefs in this build carried a figure or mechanism measurement disproved.
Anything below I have not run is marked UNVERIFIED.*

## THE HAZARD THAT IS UNIQUE TO THIS UNIT

`tools/unattended/unattended.sh` is the script the main loop invokes between every pass. **Bash reads
a script from a byte offset as it executes**, so editing it while an invocation is in flight makes
that invocation throw a syntax error at an innocent line and voids its verdict. This repo has that
recorded as a live gotcha.

You are a sidechain and the main loop is idle while you run, so the window is small — but do not
leave the file half-written between commands, and do not run a driver verb against a file you are
mid-edit on. Write the change, then exercise it.

Exercise it against a SCRATCH run-state file, never this build's own `RUN.md`. A driver verb pointed
at the live record while you are testing a predicate that decides refusals is how a test corrupts the
run it belongs to.

## The defect, and how it was found

`check_pass_open` closes a dispatch row only when a commit naming that unit WROTE inside THAT row's
declared set. `DEPL-cMendedVintage-15` declared four times, narrowing as it discovered it needed no
engine change at all, and its first row names `tools/govkit/govkit.py`. It correctly wrote nothing
there, so that row can never close, and check 49 now refuses `DEPL-cMendedVintage-17`'s declaration
of the same file.

The predicate rewards a pass that writes everything it declared and punishes one that finds it needs
less. That is the shape to keep in mind while you fix it.

## Two things the spec records that you should verify rather than assume

**`--audit` and check 49 disagree today.** The audit reports no unit dispatched and open on the same
tree where check 49 refuses on an open sibling. AC2 is written against that disagreement, and it is
observable at BASE right now — confirm it before you change anything, because it is the clearest
possible red.

**Narrowing is permitted by the verb and refused by the Skill's text.** Do not resolve that; it is
parked for the owner and §3 says so. Your fix must be correct whichever way it later resolves.

## The risk your own criterion names

`AC3` is the one this unit would most plausibly fail: closing a row that nothing supersedes would let
two genuinely concurrent passes claim one path, which is the disjointness proof this check exists to
be. Observe it — a unit with a single dispatch row must still print `no sibling pass is open` exactly
as at BASE.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to any test
file — that class has landed twice in this build, both in test-side helpers. Spell no
`tools/<kit>/…` path in shipped prose and check your own comments against the carried-prefix
predicate, which was widened four units ago. This file is shell: the shell-hygiene leg reds on a loop
fed by a command substitution, and it is in your §7.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-10-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows — and note the irony that
doing so is the exact act whose bookkeeping you are repairing. Bound every command at 900s or more.

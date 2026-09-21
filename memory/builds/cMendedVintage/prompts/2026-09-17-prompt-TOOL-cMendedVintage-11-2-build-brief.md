# Build brief — TOOL-cMendedVintage-11

**Serves:** journal TOOL-cMendedVintage-11

Read the spec whole first. This unit is unusual for this build: the defect is **not ours**, and the
product is **not wrong**. You are repairing a test fixture that has never been able to grade its own
subject on this node.

*Standing note: treat the spec and this brief as evidence, not authority. Every one of the last five
units amended its own spec after measuring.*

## The attribution, already measured — do not re-derive it, but do confirm it

A read-only investigation established all of this before you were dispatched:

- The arm fails at BASE `859daa67` and at HEAD with the identical tuple `(False, [], [])`, and its
  text is byte-identical at both — 2912 characters each.
- It landed 2026-09-08 from node `a` and has failed on node `c` on all three recorded gate readings.
  There is no green in the ledger to regress from.
- It reproduces in a standalone process where no other arm has run, so it is not leaked state from
  `TOOL-cMendedVintage-8`, whose `PROCMON_ROOT` save and restore is correct.
- Six failures out of six at the arm's own 3-second wait. Not load-sensitive.

## The cause, and the one repair that must not be made

The arm launches through a bare `bash`. On this node that resolves to WSL, and a WSL process is not a
Windows process, so the census cannot enumerate the tree it just staged.

At a **20-second wait the arm flips green** — walking `conhost.exe`, `wslhost.exe` and two copies of
the launcher, with **zero members of the staged tree**. That is a green earned by counting plumbing,
which is the green-by-absence class §7 names. **Raising the wait is the one repair that must not be
made**, and your spec's §3 says so.

## What the untouched product does under a resolved launcher

Swap the launcher for the resolved Git Bash and change nothing else:

```
WALKED (7) = the two msys sleeps, a third sleep, the native python grandchild,
             the nested bash, the launcher and the target
REPORT walked=7 kill_set=7 killed=7 survivors=[] errors=[]
VERDICT arm-tuple = (True, [], [])
```

Both graphs walked, the native grandchild reached, seven of seven dead. `census.py`, `scope.py` and
`reap.py` are measurably correct and §3 forbids touching them.

## Resolution is by EXECUTION, not by lookup

A name on `PATH` is not evidence. This repo already records that lesson for a different interpreter —
`tools/lib/resolve-python.sh` RUNS each candidate because the MS-Store `python3` stub answers
`command -v` and then exits 9009. Same shape, different binary. You are not reusing that file, and
§3 says why no shared helper is minted for one caller; what you take from it is the discipline.

## The member assertion is part of the fix, not a tidy-up

With a count, the 20-second run is green and wrong. With the members named, it is red and says which
member is missing. The count is what let launcher plumbing look like a passing test, so replacing it
is what stops the next environment difference doing this again.

## S4 is easy to forget

The cleanup probe shells through a bare `bash` too, so it cannot see a WSL tree either. Today its
strays only die because tearing down the launcher tears down the session. Route it through the same
resolved launcher.

## Your failing case needs no staging

The current shipped behaviour IS the red, on this node, right now. Run the arm before you touch it
and record the tuple. That is a luxury most units in this build did not have.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers in test files —
that class has landed twice in this build, both in test-side helpers. Spell no `tools/<kit>/…` path
in shipped prose or comments, and note that this ban bites here: your spec's own §10 had to cite the
python resolver as a DISCIPLINE rather than name it as a dependency, and your code must not spell a
sibling kit's path either.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-11-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round.

`python tools/process-monitor/selftest.py` is yours and you should run it — it is fast, about 59
seconds, and it is the direct observation of every criterion here. `adopt-process-monitor.test.sh` is
a `*.test.sh`; the run is in VERIFYING so it is no longer denied, but it is slower and its
`FLOOR_ASSERTIONS` must not move, because you add and remove no assertion in that file.

**A sibling unit is building beside you**, `DEPL-cMendedVintage-25`, entirely inside
`tools/govkit/`. Your write sets are disjoint. Do not touch that kit and do not be surprised by its
commits. Bound every command at 900s or more.

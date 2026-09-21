# Build brief — TOOL-cMendedVintage-12

**Serves:** journal TOOL-cMendedVintage-12

Read the spec whole first. Then read `pass_commit`'s header in
`tools/unattended/lib-unattended.sh`, twenty lines below the function you are repairing. That header
is your specification — the same class was diagnosed and fixed there on 2026-09-10 and it records the
measurement, the reasoning and the two properties that must hold together.

*Standing note: treat the spec and this brief as evidence, not authority. Every one of the last nine
units amended its own spec after measuring, and three found their own criteria could not fail.*

## THE HAZARD THAT IS UNIQUE TO THIS UNIT

You are editing the library the driver sources on every verb. **Bash reads a script from a byte
offset as it executes**, so a mid-flight edit throws a syntax error at an innocent line and voids
that invocation. This repo carries it as a live gotcha and a unit of this build already paid for it.

Write the change, then exercise it. Do not leave the file half-written between commands, and do not
point a driver verb at a file you are mid-edit on.

## You have no dispatch declaration, deliberately

`--dispatch` is the verb you are repairing and it does not complete — four attempts, the last exiting
on a one-hour bound at 11350 seconds with nothing written. So this unit has **no dispatch row**, the
exception is recorded in your spec's §9 and in the run's parked decisions, and you should not try to
create one. Your write set is `tools/unattended/lib-unattended.sh`, the shell-hygiene checker, its
registry if one is owed, your spec and your acceptance ledger. If it grows beyond that, say so in the
ledger rather than declaring it.

## The measurement you inherit — confirm it cheaply, do not re-derive it

- Four `--dispatch` runs died: 2h14m, 420s bounded, 300s traced, and 11350s bounded. None wrote a row.
- Ten stalled process trees were reaped before the last measurement, the oldest alive 18h42m after
  another builder abandoned it unread. So it is not contention between them.
- With `< /dev/null` it behaved identically, so it is not the stdin class.
- A `bash -x` trace ends inside `read_brief_paths`, which is called once per commit per dispatch row.
- `RUN.md` is 71037 bytes and there are 106 commits since BASE.

## The fix is a shape you copy, not one you invent

`pass_commit` runs its walk in the CURRENT shell with stdout redirected to a scratch file, and reads
that file by redirect. No pipe exists, so no EOF has to arrive; a redirect from a file creates no
subshell, so a `return` still returns from the function. `read_brief_paths` prints rather than
returning, so it needs only the second property — but take the same shape, because a reader that
matches its neighbour is one a later maintainer can trust at a glance.

`memory/gotchas/bounded-through-a-pipe-is-unbounded.md` is the class.

## S3 is the left-shift and S4 is what makes it honest

The shell-hygiene leg refuses a loop fed by a command substitution, repo-wide. This loop is fed by a
heredoc over a **variable**, and the variable was assigned from the substitution on the line above.
The predicate does not follow the assignment, so it was blind to the one instance that mattered.

Widen it to follow ONE assignment, then **run the widened predicate over the real tree and report
hits AND near-misses**. Two units of this build did exactly this and both had a wrong first draft —
one credited every mutating call in a function to every binding of a name. If the widened predicate
reds something innocent, that is a finding about the predicate, not an obstacle.

## AC1 is the one that proves the unit and the one you could fake

It has two halves: the returned path set is UNCHANGED before and after, and a bounded `--dispatch`
COMPLETES and writes its row. The first half matters more than it looks — the disjointness verdict
rests on those paths, and a repair that quietly changes them would move a safety answer while
claiming to fix a stall. Capture the set on a known commit and unit before you touch anything.

For the second half, `DEPL-cMendedVintage-26` is waiting on a dispatch and its brief is already
written. If your repair works, declaring it is the proof — and if you declare it, say so clearly in
your ledger so the main loop does not declare it twice.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers in test files.
Spell no `tools/<kit>/…` path in shipped prose or comments. Write no count of a derived population
into prose.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-12-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round. I got this wrong in three separate
specs in this build, including yours, so check your own bullets against the rule rather than against
the examples around you.

The run is in VERIFYING, so nothing denies a suite. `bash tools/unattended/unattended.test.sh` is
yours. Bound every command at 900s or more.

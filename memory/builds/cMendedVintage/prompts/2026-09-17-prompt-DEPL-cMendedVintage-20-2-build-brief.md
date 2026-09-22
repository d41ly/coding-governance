# Build brief — DEPL-cMendedVintage-20

**Serves:** journal DEPL-cMendedVintage-20

Read the spec whole first. This is the LAST unit of the build, and it is the only one whose whole
subject is another criterion's blindness.

*Standing note: twenty briefs in this build carried a figure or mechanism measurement disproved, and
every one of the last thirteen units amended its own spec mid-build after measuring. Treat this as
evidence, not authority.*

## The spec's figures are BASE figures, and they are correct — I checked

`grep -c 'allow_ungraded' tools/govkit/govkit.py` returns **8** at BASE `859daa67` and the widened
`grep -cE 'allow[_-]ungraded|ALLOW_UNGRADED'` returns **14**, exactly as §1 says. On the tree you are
building against, both return **0**: `DEPL-cMendedVintage-4` drained them at commit `81ce02a4`.

That is the sequencing working, not a problem. Your edge to that unit says the arm is red by
construction before it lands. It has landed, so your arm is GREEN ON ARRIVAL — which means the only
way to see it fail is to stage a re-introduction, and an arm nobody has seen fail is an assertion
about nothing.

Re-measure both numbers yourself rather than quoting mine.

## Stage the break on a COPY, not on the worktree file

`tools/govkit/govkit.py` is NOT in your write set, `DEPL-cMendedVintage-19` landed changes in it
minutes ago, and this build enters its closing review immediately after you. A re-introduced
`ALLOW_UNGRADED` left behind in the real file would be caught, expensively, at exactly the wrong
moment.

Give the arm its target path as a parameter defaulting to the derived module path. Then the failing
case is observed against a scratch copy under the run's scratch root and the worktree is never
touched. That is a better arm anyway — a checker that can only read one hard-coded path cannot be
tested at all.

## What makes this a class arm rather than a bigger grep

S3: the population is the WHOLE operator-facing surface of that module — the USAGE block, every
string literal, every identifier — and never a section of it. A pattern scoped to argv parsing is the
same blindness one level in, which is the defect you are fixing. The original criterion missed the
USAGE line, the USAGE sentence, the `over` clause, the argv arm and the `parse_args` unpack, and that
last one is the site its own Red-when named as the likeliest miss.

S2: the retired list is one literal per flag, beside the arm, each carrying the date and the unit id
that retired it. A retirement with no row is a retirement nothing grades — so the list is the thing
that has to be easy to add to.

S4: the arm names in its own header what it does NOT check. It reads one module, it cannot see a flag
re-introduced in `selftest.py` or in a sibling tool, and it grades spelling rather than behaviour. A
structural check reads as a semantic one to everybody who did not write it.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` — that class has landed twice in this build, both in test-side helpers. Spell no
`tools/<kit>/…` path in shipped prose or comments.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-20-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED — `govkit selftest` is
banned in this pass, so the arm ships executed only by whatever you can run directly.

**The ledger bullet shape.** `memory/HYGIENE.md` gives the form as `- AC1 — ``<token>`` — what was
observed`: the backticked witness on the bullet's FIRST line, immediately after the label. Check 23
reads form from that line alone. The AMENDED form is `- AC2 — amended rev-<n> — …` and carries no
backtick. The token must share content with the criterion's own backticked token, case-folded either
way round — and if the CRITERION's span wraps across a line break it offers no whole token and
nothing can join it, which is how the previous unit failed. Check 23 is HELD under `--staged`, so no
commit hook will tell you.

Re-declare with `--dispatch` if your write set grows; it refuses a declaration naming `RUN.md`. Bound
every command at 900s or more.

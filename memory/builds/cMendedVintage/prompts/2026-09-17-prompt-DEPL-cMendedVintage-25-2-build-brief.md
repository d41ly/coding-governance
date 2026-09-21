# Build brief — DEPL-cMendedVintage-25

**Serves:** journal DEPL-cMendedVintage-25

Read the spec whole first, then read finding **H1** in
`memory/builds/cMendedVintage/reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md`.

*Standing note: this is the last of the four units the closing review adopted. The three blockers are
repaired; the build waits on you and on one sibling running beside you. Treat the spec and this brief
as evidence, not authority — every one of the last five units amended its own spec after measuring,
and two of them found their own acceptance criteria could not fail as written.*

## Four separate lenses found this independently

That is unusual and it is worth knowing: the word-split is visible from the security lens, the
correctness lens, the data-integrity lens and the integration-seams lens at once. It means the defect
is not subtle and the risk in this unit is not finding it — it is fixing one site and leaving the
other, or fixing the parsing and leaving a second spelling of the same hazard.

## What the damage is

`git add --renormalize` folds a dirty pinned path's UNCOMMITTED content into an index gov does not
own. The cleanliness guard exists to stop exactly that, and a path carrying a space or a non-ASCII
byte walks straight past it because the guard word-splits `git diff --name-only`.

## Both sites, and the second spelling

The review names `tools/govkit/govkit.py:8562` and a sibling near `:5493`. Fix ONE and the other
still ships. The `-z` form with NUL-delimited parsing is the fix at both.

Then the question your spec raises and you must answer by measurement: git's default `core.quotePath`
is a SECOND spelling of the same hazard — a non-ASCII path comes back quoted and escaped rather than
raw, so a reader that splits correctly can still compare the wrong bytes. `-z` disables the quoting
as well as the splitting, but say what you MEASURED rather than what you assume, because that is a
claim about git's behaviour and not about this code.

## The left-shift reaches the class

Any place the engine parses git plumbing output by word-splitting, not just these two. Run the
candidate predicate over the real tree BEFORE wiring it and print hits AND near-misses.
`DEPL-cMendedVintage-21` and `-23` both did this and both had a wrong first draft — `-23`'s credited
every mutating call in a function to every binding of a name. Report both lists in your ledger even
if the answer is two sites.

## Observe the fold, not the exit code

The red is an operator's uncommitted content appearing in the index after a run. Build the fixture
with a pinned path whose name carries a space, put real uncommitted content in it, run, and assert
the index does not carry it. No exit code will show this.

## Read what landed in the same file while you were specced

`DEPL-cMendedVintage-22`, `-23` and `-24` have all landed in `tools/govkit/govkit.py` since the
review was written — the drift guard, a containment check hoisted to the top of the pins arm, and a
`WRITING_DISPOSITIONS` set feeding three call sites including the renormalize guard's neighbour.
Expect every line number in the review to be wrong and locate by symbol.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments. Write no
count of a derived population into prose.

## Required of every unit

gov keeps no govkit receipt, so no criterion here is observable against this repo — each needs a
scratch fixture target under the run's scratch root. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-25-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round.

**On the suite.** `python tools/govkit/selftest.py` is its own program, not a deployer subcommand.
The unit before you could not finish it inside a 600s bound on this loaded machine and reported that
as a skip rather than as a number — do the same if it happens to you, and do not let a run straddle
your own commit. It currently carries reds and a crash in the `-14` reap fixture that are under
separate triage and are **not yours**. Bound every command at 900s or more.

**A sibling unit is building beside you**, `TOOL-cMendedVintage-11`, entirely inside
`tools/process-monitor/`. Your write sets are disjoint. Do not touch that kit and do not be surprised
by its commits.

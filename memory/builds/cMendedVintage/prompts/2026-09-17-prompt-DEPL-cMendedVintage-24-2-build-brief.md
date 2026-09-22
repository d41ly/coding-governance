# Build brief — DEPL-cMendedVintage-24

**Serves:** journal DEPL-cMendedVintage-24

Read the spec whole first, then read finding **B3** in
`memory/builds/cMendedVintage/reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md`.

*Standing note: this unit exists because the closing review returned BLOCKED. Your finding is the
third blocker; the first two are repaired and the build waits on this and one more. Treat the spec
and this brief as evidence, not authority — the last four units each amended their own spec after
measuring, one of them correcting a claim the spec made about a neighbouring population.*

## What the outcome actually is

Not a refusal that fails to fire. The operator's UNCOMMITTED `.gitattributes` content is staged by
gov and then destroyed outright by the rollback's `checkout-index -f`. That is the precise hazard
`demand_claimed_paths_clean` exists to prevent, happening at the one path the function carves out.

`DEPL-cMendedVintage-10` is what falsified the carve-out's justification, in this same diff, by
teaching `update --write` to write that file and `git add` it. The function's header still argues the
old case in as many words.

## BOTH halves move, and this is the class that has fired most in this build

The predicate AND the header prose that justifies it. A header still arguing a case the code stopped
implementing is `amendment-leaves-its-other-half-standing`, which has now fired in five separate
units here, twice inside a unit written to fix an earlier instance of it. Grep your own diff for the
other half before you commit, and say in the ledger that you did.

## The design choice your spec makes, and the one it rejects

Your spec chose between "include the `attributes` row" and "include every row whose disposition this
build taught `update` to write". Read its reasoning and then check it against the code: the second
form is the class fix and the first is the instance fix, and this repo's §7 says to gate the class.
If the code disagrees with the spec — if the disposition set is not derivable where the predicate
stands — amend the spec and say why the instance form is what you shipped.

## Observe the destruction, not the exit code

The red is an operator's uncommitted bytes gone from the worktree after a run that rolled back. Build
the fixture with real uncommitted content in `.gitattributes`, capture it, run, and assert byte
equality afterwards. An exit code will not show this and neither will the receipt.

## Read what landed an hour ago in the same arm

`DEPL-cMendedVintage-23` just hoisted a containment check to the TOP of the pins arm and collapsed
three joins onto one `pins_path` binding. That is the arm your predicate has to reach, so read that
change before designing, and expect the review's line numbers to be wrong.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments. Write no
count of a derived population into prose — `DEPL-cMendedVintage-23` shipped exactly that defect
inside the checker it wrote to enforce a neighbouring half of the same rule, and its own checklist
run caught it.

## Required of every unit

gov keeps no govkit receipt, so no criterion here is observable against this repo — each needs a
scratch fixture target under the run's scratch root. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-24-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round. Check 23 is HELD under `--staged`.

**The suite is runnable and you should run it**, as `python tools/govkit/selftest.py`, which is its
own program rather than a deployer subcommand. Two cautions from the unit before you. Do NOT let a
run straddle your own commit — that is the `suite-invalidated-by-a-commit-under-it` class and makes
the totals a caveated number rather than a verdict. And if you stage a break to observe an arm going
red, make sure the staged break does not run FIRST and contaminate the fixture the arm then reads;
that cost the last unit a red it had to explain rather than a verdict it could use.

The suite currently reports roughly 1365 green and 43 red and then dies with a `FileNotFoundError` in
the `-14` reap fixture at `tools/demo/one/conf.txt`. **None of that is yours** — it is under separate
triage. Bound every command at 900s or more.

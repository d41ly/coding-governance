# cMendedVintage — the acceptance ledger for unit 7

**Serves:** journal DEPL-cMendedVintage-7

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commit, `e6612579`, 2026-09-16. Where a criterion is
answered by a command it was replayed at the shell against this worktree and its result is given;
where it is answered by what the building pass measured, the commit is cited AS the record and named
as such. No merge bar, no `*.test.sh` and no self-test runner ran in this pass:
`tools/govkit/selftest.py` was READ, never executed.*

## The one thing worth reading twice

**AC1 cannot be replayed here, and the criterion says so itself.** Its fixture is a scratch install
under the building run's own scratch root, and its `fixture:` line records that this repo keeps no
receipt of one. So the only account of the flip actually running in both directions is the commit's,
and this pass rebuilt nothing to improve on it. What survives in the tree is the expression; reading
an expression is a weaker observation than running it, and this ledger does not pretend otherwise.

**The failing case came first, which is the useful half of that record.** Against the unflipped
engine the three unset-direction arms went red — an engine treating an unset variable as off, which
is AC1's own Red-when.

**No criterion here covers the adopter.** The charter's dark-landing rule asks for a fixture and then
one adopter. The spec answers that in section 8 by declaring the adopter half an external edge, and
this ledger claims nothing about it: gov holds no install of its own and none was touched.

**Evidences:** DEPL-cMendedVintage-7

- AC1 — `GOVKIT_RERENDER=0` — NOT REPLAYED HERE; commit `e6612579` is the record, and it names both
  directions against a scratch install under that run's scratch root. With the variable unset the
  run printed its re-render summary, a `ran` line and the refreshed artifact; with the value `0`
  exported it printed the DECLINED line and left the artifact untouched. What IS readable at this
  tip is the expression the criterion is about: `tools/govkit/govkit.py:7471` reads
  `_rerender_on = os.environ.get("GOVKIT_RERENDER") != "0"`, which takes an unset variable as ON and
  the literal `0` as OFF — the two directions the Red-when pairs. The standing exerciser for the
  behavioural half is the `govkit selftest` leg, which has run for this unit in neither pass, so AC1
  is owed to it.
- AC2 — `git grep -n "GOVKIT_RERENDER" -- tools/govkit/` — REPLAYED at this tip. Exit 0, 23 hits,
  nine in `govkit.py` and fourteen in `selftest.py`. Exactly ONE site still removes the variable
  from a child environment, the `_pvENV` strip at `selftest.py:9273`, and it carries the line S2
  allows in place of a pin: the strip stays and every block below it now runs with the step ON,
  because block 1 exports the value on its own `update` line and the strip therefore drops only this
  node's opinion. The three sites whose subject is the off path are pinned instead, spelled
  `env=dict(os.environ, GOVKIT_RERENDER="0")` at `selftest.py:6663`, `:9424` and `:9914`, each above
  a comment naming the flip. `git grep -n 'k != "GOVKIT_RERENDER"' -- tools/` returns no hit at exit
  1, which is grep's no-match code and not a failure, so no single-variable strip survives anywhere
  in the kits. figure: DERIVED at this tip — eight sites in that file set the value explicitly,
  three to `0` and five to `1`, and none is left inheriting.
- AC3 — `git grep -ln "GOVKIT_RERENDER" -- tools/ WIRE-INTO-PROJECT.md` — REPLAYED at this tip:
  twelve files, which is the carrier count the commit says it corrected. The ten outside
  `tools/govkit/` were read here and every one describes the step as running by default and names
  `0` as the way off — the `kit.toml` of drift-audit, lexicon, memory-recall, memory-tree,
  unattended and workflows, `tools/workflows/README.md`, the two `*.test.sh` headers under the
  review-harness home, and `WIRE-INTO-PROJECT.md` at line 1015. One thing the criterion does not
  reach, stated rather than glossed: `WIRE-INTO-PROJECT.md` line 1320 exports the value `1` on an
  `update` line inside a migration recipe. That is a command and not a claim about the default, so
  it is not the Red-when, but it is the one live `=1` spelling left in the runbook.
- AC4 — `python tools/govkit/govkit.py selfcheck` — REPLAYED at this tip. Exit 0, and arm 7l's own
  note reports 15 sentences naming an update and a re-render, 0 calling a flag-off run silent, over
  6 kits declaring `[[regenerate]]`. That zero is what this criterion asks for: no live instance
  remains of a sentence calling a flag-off update silent without naming the `re-rendered` row it
  still prints. This is a run at the BUILD's tip, not at the unit's own commit; for that one the
  commit is the record and it reports the same exit.

## What this ledger does NOT claim

That the merge bar is green, or that any leg of it ran, in either pass. `govkit selftest` owns all
four child-environment sites this unit decided and is unobserved for it end to end. That matters
more than usual here: three arms whose subject is the OFF path stopped stripping the variable and
started pinning it, so a wrong pin would leave a suite that looks green while grading the opposite
path. The leg is owed at the run's close, and AC1 is owed with it.

That any arm in `tools/govkit/selftest.py` passes, or that the file even imports. It was read at
this tip and executed by nothing.

That an adopter was tested. gov keeps no `.governance/install.json`, so a fixture is the only
observation available to this repo, and the spec's section 8 assigns the adopter half of the
dark-landing rule to the first consumer that pulls this release. Nobody has performed it, and
nothing in this tree can.

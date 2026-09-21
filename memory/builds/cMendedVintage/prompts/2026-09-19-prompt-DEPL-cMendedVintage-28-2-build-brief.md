# Build brief — DEPL-cMendedVintage-28

**Serves:** journal DEPL-cMendedVintage-28

Read the spec whole first. Its §4 carries the measurement this unit rests on, so you do not have to
re-derive it — but you should re-take it, because it is cheap and it is the whole argument.

*Standing note: treat the spec and this brief as evidence, not authority. Every one of the last
twelve units amended its own spec after measuring. Two found their own criteria could not fail, and
one found a fixture its spec asked for that cannot exist.*

## The safety is NOT broken, and knowing that changes what you are doing

Three engine variants against one fixture, measured on bytes:

| variant | result | the file outside the target root |
|---|---|---|
| shipped | refuses, untracked-shadow message | **unchanged** |
| shadow refusal staged out | refuses, containment message | **unchanged** |
| both staged out | exits 0, reports `pins-withdrawn` | **mutated** |

The third row is what makes the second mean anything: it proves the fixture genuinely reaches the
splice. So `DEPL-cMendedVintage-23`'s containment proof is intact and you are not racing a live
vulnerability. What you are fixing is which of two guards speaks, and therefore whether an operator
gets a remedy they can run.

## The collision, in one paragraph

S4's untracked-shadow refusal sits in `update`'s preamble, roughly sixty lines of engine before the
classification loop where `demand_contained_dest` sits. A path that escapes the target root is in no
index by construction, so the shadow predicate matches it and the run dies before the loop starts.
`DEPL-cMendedVintage-24` created this by replacing a literal `== "table"` role filter with
`derive_graded_rows`, which admits the `attributes` row for the first time. Bisected: green at
`-23`'s own commit, red at every vintage since.

## Confirm the impossible remedy yourself — it is one command

The refusal tells the operator to `git add` the escaping path. Run it. Git answers that the path is
outside the repository. That is the user-facing half of this unit and it takes ten seconds to see.

## What must not move

`DEPL-cMendedVintage-24`'s widening stays. It exists because gov was staging an operator's
uncommitted `.gitattributes` on every run and then destroying it in the rollback. Narrowing the
shadow population back to a role literal would fix your diagnostic by reopening a destroyed-work
blocker. **AC2 is written against exactly that** and is the criterion this unit would most plausibly
fail — stage an inside path that is present in the worktree and absent from the index, and confirm
it still refuses with the shadow wording after your change.

`demand_contained_dest` itself stays, and so does the `pins` arm's call to it. That call is already
above the join, above the read and above the withdrawal exit.

## AC3 is a vacuous arm and AC4 is the one nothing asserts

AC3's sibling is green **today**, satisfied by a run that refused for an unrelated reason and never
reached the branch it grades. That is a skip wearing a pass. Make it assert the run reached the
containment guard, not merely that it refused.

AC4 asserts the ORDERING. Nothing does today — containment is first only because the spec says so.
Stage `demand_contained_dest` out of the preamble and confirm the arm reds naming which guard
answered.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments. Write no
count of a derived population into prose.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-28-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape**, and I am the wrong person to learn this from by example: the backticked
witness sits on the bullet's FIRST line, immediately after the label, and check 23 reads form from
that line alone. The AMENDED form is `- AC2 — amended rev-<n> — …` and carries no backtick. The token
must share content with the criterion's own backticked token, case-folded either way round. I have
now written that rule into six briefs and broken it in four specs, including yours — check your
bullets against the rule, not against the shapes around you.

**A build pass runs no suite.** The pass directive overrides any brief, and two units before you were
right to refuse. Replay your arms directly against scratch fixtures in the shape the permanent arms
use, and record the suite verdict as OWED. For context: the deployer suite is at 36 red, down from
68, and your two arms are among the survivors.

`--dispatch` works and costs about two and a half minutes. Bound every command at 900s or more.

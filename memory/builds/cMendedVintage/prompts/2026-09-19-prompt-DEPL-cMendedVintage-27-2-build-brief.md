# Build brief — DEPL-cMendedVintage-27

**Serves:** journal DEPL-cMendedVintage-27

Read the spec whole first. This is the last unit the suite attribution adopted, and the last one
standing between this build and its closing review.

*Standing note: treat the spec and this brief as evidence, not authority. Every one of the last
eleven units amended its own spec after measuring. The unit before you found its rev-1 asked for a
fixture that CANNOT EXIST — an in-scope `attributes` row that is untracked — and rewrote the
criterion to assert the pairing it actually needed. Expect to do the same.*

## What happened

`DEPL-cMendedVintage-19` was adopted because a schema-3 row kept `engine` and took the full table
disposition against a rule that declares `project-owned` and supplies no bytes. It fixed that by
un-gating the role re-resolution from `if schema < 2 and …` to `if …`.

The consequence, measured: a row recorded `engine` whose descriptor now resolves `rendered` takes the
new `role-moved` branch, so **nothing is written, the row is not re-stamped, and it never reaches the
three-way merge**. In the migration fixtures the harness row is exactly that row, so the conflict the
vintage-migration runbook exists to handle no longer happens, and its STOP arms now read *"block 1's
last update named no three-way conflict, so there is nothing to set aside"*.

Nine failures, all in `[-PV]`.

## Two facts that shape the answer, both measured

**Two of the nine are an EXPECTED flip, and the fixture said so in advance.** Its header records that
the durable repair is `DEPL-dPolishedVitrine-1`, and that when it lands the two `F1 PRECONDITION`
arms flip and the migration retires with them. Your spec must separate those two from the other
seven, and say which it makes green and which it lets flip. Getting this wrong in either direction is
the likeliest way to fail this unit: force all nine green and you have re-broken what `-19` fixed;
accept all nine and you have shipped a runbook with no conflict path.

**`b52b5d80` touched `tools/govkit/selftest.py` not at all**, and the suite carries zero arms tagged
for that unit — its evidence went into `tools/govkit/matrix.py`. The unit landed with nothing in the
suite that could have shown this. That is worth a scope item or a non-goal in its own right, and your
spec already has a view; check it against the tree.

## What must not reopen

`-19`'s own subject: the re-resolution and the `role-moved` report both stay. What changes is which
rows reach the merge. Stage `-19`'s original case — a schema-3 `engine` row against a descriptor
declaring `project-owned` with no bytes — and confirm it still reports `role-moved` and still writes
nothing after your change.

## The observable

`[-PV]` is build `dPolishedVitrine`: 104 arms cut out of `WIRE-INTO-PROJECT.md`'s vintage-migration
runbook and run by bash against ten throwaway consumer repos modelled on the real adopters, including
their commit hooks. 103 were green at BASE. It is the only thing in the suite that exercises the
harness row's role transition end to end.

`python tools/govkit/selftest.py` is its own program and takes about 33 minutes. **A build pass is
forbidden to run a suite** — the pass directive overrides any brief, and the unit before you was
right to refuse it. Replay your arms directly against scratch fixtures instead, in the shape the
permanent arms use, and record the suite verdict as OWED.

The number for the main loop's bar: 68 red at the time of the attribution, `DEPL-cMendedVintage-26`
expected to return about 25 of them, and your nine minus the two expected flips on top of that.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments. Write no
count of a derived population into prose.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-27-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round.

`--dispatch` works again and costs about two and a half minutes — `TOOL-cMendedVintage-12` repaired
it after four attempts had hung. Re-declare if your write set grows. Bound every command at 900s or
more.

# Build brief — DEPL-cMendedVintage-26

**Serves:** journal DEPL-cMendedVintage-26

Read the spec whole first. Then read the disposition inputs below, because this unit repairs
regressions that a unit THIS RUN ADOPTED shipped while fixing a blocker, and the shape of that
mistake is the thing most worth avoiding twice.

*Standing note: treat the spec and this brief as evidence, not authority. Every one of the last eight
units amended its own spec after measuring.*

## What happened, plainly

`DEPL-cMendedVintage-24` was adopted to close a blocker: an operator's UNCOMMITTED `.gitattributes`
was being staged by gov and then destroyed by the rollback's `checkout-index -f`. It closed that. It
also shipped two predicates that account for **25 of the deployer suite's 68 failures**, and both are
shipped-behaviour regressions in `update` that any adopter reaches.

The suite could not have told anyone: it crashed partway through and killed its own interpreter, for
three separate reasons, and only ran to completion after all three were cleared.

## The evidence, already measured — confirm it, do not re-derive it

- BASE `859daa67` runs the suite to completion: **1203 green, 30 red**.
- HEAD: **1397 green, 68 red**.
- Reverting these two predicates on a throwaway clone: **68 red becomes 45**. Twenty-five fixed, zero
  unrelated regressions.

Logs are under the run's scratch root: `base_run.txt`, `gkself2.txt`, `probe_run.txt`.

## Mechanism A — every scoped update is refused

The index read is built from `rows_all`, which is `--kits` SCOPED. The shadow test iterates
`derive_graded_rows(receipt)`, which is UNSCOPED. So the "present in the index" set only ever holds
the scoped paths, and every out-of-scope writing row whose file exists on disk is absent from it BY
CONSTRUCTION.

Reproduced at the commit boundary on a two-kit target: the parent runs clean with `rc 0`, and the
commit REFUSES with `rc 2` naming two files that are **committed and tracked**. The message is
factually false and sends the operator to `git add` a file that is already added.

## Mechanism B — the closing self-audit reds on any rename

`_graded_paths` comes from the POST-run receipt; the path set it is checked against is a PRE-run
snapshot; and a rename puts the OLD path into the written set. The old path is in the snapshot and
gone from the post-run receipt, so every renamed row reports itself as having come apart, and
`update --write` over a renaming vintage exits 1 with a finding it invented about itself.

Fix one and the other still ships. The spec names both.

## Do NOT simply restore BASE

BASE's predicate was scoped AND role-filtered — `if UPDATE_ROLE.get(...) == "table"`. Dropping the
role filter is what let it reach `DEPL-cMendedVintage-23`'s deliberately escaping row on an unscoped
run, which is coverage worth keeping. You need the scope corrected AND the wider role set kept. A
revert gives you neither problem and loses the reason `-24` exists.

**What must not reopen:** the uncommitted-`.gitattributes` destruction. Stage that case and confirm
it still refuses after your change.

## The observable is the suite, and it is the honest one

The `[-PV]` family is build `dPolishedVitrine` — 104 arms cut out of the vintage-migration runbook in
`WIRE-INTO-PROJECT.md` and run by bash against ten throwaway consumer repos modelled on the real
adopters, including their commit hooks. 103 were green at BASE. Fifteen of your casualties are there,
because block 1 of that runbook is `--kits` scoped, so it exits 2 and every later block STOPs.

Your other casualties: `[-13] AC2` twice, `[-14R] AC4`, `[-23]` twice, `[-11] AC2`, `S2` and `S11`,
and `[-RS1] AC4` twice downstream.

`python tools/govkit/selftest.py` is its own program, takes about 33 minutes, and the run is in
VERIFYING so nothing denies it. Run it. The number to beat is 68 red; reverting both predicates gives
45, so a correct fix should land at or near 43 with your own new arms green. **Do not let a run
straddle your own commit** — that grades two engines and makes the total a caveated number.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments. Write no
count of a derived population into prose.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-26-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded either way round, and a criterion whose own span wraps
across a line break offers no token for anything to join.

Regenerate the build index with `gen_build_index.py --write` AFTER `git add`. Re-declare with
`--dispatch` if your write set grows; it refuses a declaration naming `RUN.md`. Bound every command
at 900s or more.

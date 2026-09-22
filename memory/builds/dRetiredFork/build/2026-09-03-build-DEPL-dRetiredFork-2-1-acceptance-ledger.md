# Acceptance ledger — DEPL-dRetiredFork-2

**Serves:** journal DEPL-dRetiredFork-2

Tier-2 · node d · 2026-09-03

**One of two defects is fixed and landed. The other is diagnosed, built, measured working, and NOT
landed** — because landing it breaks a standing invariant another unit established, on the verb
whose failure mode is silent data loss in a repository gov does not own.

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-2

- AC6b — MET — `govkit update --kits memory-tree` now reports `scope: --kits memory-tree -> 29 of
  160 receipt row(s)` and `--kits unattended -> 25 of 160`. Before the fix the flag was parsed and
  discarded: the scoped and unscoped runs produced **byte-identical output**, with nothing saying
  the scope was ignored. An entry the receipt does not claim now REFUSES rather than widening
  silently
- AC7 — MET — `python tools/govkit/selftest.py` reports all arms held and
  `python tools/govkit/govkit.py selfcheck` exits 0 with the landed change
- AC1 — **NOT MET.** Built and measured working, then withdrawn. See below
- AC2 — **NOT MET as a landed behaviour**, but MEASURED: with the pass in place a new `rendered`
  source is reported and not written. `memory/guides/UNATTENDED-VERBS.md [rendered]` appeared as
  `NEW (not landed)` — the exact trap S3b names, observed rather than reasoned about
- AC3 — NOT MET — the decline join was written but never exercised, because both adopters use
  `[[decline]]` zero times
- AC4 — NOT MET — the `0 new` line exists only in the withdrawn half
- AC5 — MEASURED, and the spec's numbers do not reproduce. NicoCares shows **9 landable** new
  sources and 8 reported-not-landed, not the spec's five — gov has shipped more since `b0108f13`,
  including files this very build added. inCMS could not be measured at all: `update` refuses there
  on a pre-existing receipt corruption, a row carrying `commit` and no `gov_oid`, which is unrelated
  to this unit
- AC6 — NOT MET — the copy-once guard is in the withdrawn half

## What was withdrawn, and why a run should not have landed it

The new-source pass works. Measured against NicoCares: 9 landable, 8 correctly reported-not-landed,
each named with its role and the reason it was not landed.

Then the selftest failed **19 arms**, and the one that matters reads:

```
[-11] AC6 THE STANDING PREDICATE: the tracked-file count is UNCHANGED
      across a run with no --write-withdrawals — 18 -> 25
```

That is not an arm that drifted. It is a deliberate invariant another unit established about this
verb, and the whole point of this unit is to change it. Making that change means rewriting nineteen
arms that encode it — on the verb whose own docstring says its failure mode is silent data loss in a
repository the operator owns and gov does not.

**That is a contract change an owner makes, not a run.** Parked with the three options stated. The
alternative — rewriting the arms that would have caught the risk, in order to land the thing that
carries it — is precisely the shape this build has spent twenty-five units removing.

## What the withdrawn half proved before it was withdrawn

- the population defect is real: a gov source with no receipt row is never constructed, classified,
  counted or printed
- the join that fixes it is the one `plan --coverage` already performs, so it adds a caller and not
  a second answer
- **rev-1's gate was wrong and the spec's correction is right**: `LANDABLE_ROLES` derives from
  `ROLE_KINDS`, which marks `seed` as `write`, so it would have admitted a role whose own
  disposition — `report-reseed` — says this verb never writes it. The gate is `UPDATE_ROLE`'s
  `table` disposition, which is `engine` alone
- a new `rendered` source is reported, not landed. Observed on the live NicoCares receipt

## A note on the parked record's own text

The park row lost the word `update` to shell command substitution: backticks inside a `--item`
argument were evaluated before the driver saw them. The row's meaning is intact and this ledger
carries the full statement; a second near-duplicate park would inflate the count of decisions the
owner must read, which the driver's own documentation warns against.

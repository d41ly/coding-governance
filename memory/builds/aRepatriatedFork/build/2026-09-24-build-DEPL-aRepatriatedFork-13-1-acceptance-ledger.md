# DEPL-aRepatriatedFork-13 — acceptance ledger

**Serves:** journal DEPL-aRepatriatedFork-13

One unit pass under the mandate. It ran no merge bar and no self-test suite. The arm group this unit
adds to `tools/govkit/selftest.py`, `check_adopter_owned`, was run on its own by importing the suite
and calling that one function over a scratch root under `%TEMP%`: 17 arms, all held. The whole
`selftest.py` suite was not run, and the close owes it.

Every new arm was also observed RED. Ten staged breaks were each written into a COPY of `govkit.py`,
never the real file, and the arm group was run against each copy. Every break redded at least one
arm. They removed the path grade, the non-engine-role refusal, the import grade, the `contract`
disposition, the `when_owned` stand-down, the consumer grade, the zero-clause refusal, the F3
escalation, the installed-consumer mark, and the `declared` evidence. The first run of that sweep
found two arms that could not red. The AC1 fixture named files that did not exist, so the
missing-file refusal answered for the path grade. No fixture source was reached by a second rule, so
the non-engine refusal was never the deciding branch. Both arms were fixed before the build went on.

The adopter was read-only. The observations used two `git clone --local --shared` clones of
`C:/projects/incms/main` at `bc7e955894e15f34a086c1875f2f9af3cceb77bb`, under `%TEMP%/ic13` and
`%TEMP%/ic13c`. Each clone carried one scratch commit. `ic13` added the five `[[own]]` rows and
`ic13c` added none, and both were then re-adopted with `adopt --re-adopt --write` against gov
73113582. Nothing was written in the real inCMS tree.

## The five rows inCMS would add (S6)

```toml
[[own]]
path = "scripts/gen_build_index.py"
implements = "memory-tree:gen_build_index.py"
why = "inCMS wrote its own before gov did; a parallel program, converging under DEPL-aRepatriatedFork-20"

[[own]]
path = "scripts/corpus_ids.py"
implements = "memory-tree:corpus_ids.py"
why = "inCMS wrote its own before gov did; a parallel program, converging under DEPL-aRepatriatedFork-20"

[[own]]
path = "scripts/gotchas.py"
implements = "memory-tree:gotchas.py"
why = "inCMS wrote its own before gov did; a parallel program, converging under DEPL-aRepatriatedFork-20"

[[own]]
path = "scripts/merge-rows.py"
implements = "memory-tree:merge-rows.py"
why = "inCMS wrote its own before gov did; a parallel program, converging under DEPL-aRepatriatedFork-20"

[[own]]
path = "scripts/check-docs-hygiene.sh"
implements = "memory-tree:check-memory-hygiene.sh"
why = "inCMS wrote its own before gov did; a parallel program, converging under DEPL-aRepatriatedFork-20"
```

## What the inCMS clone measured

The receipt inCMS holds today yields 12 `unattributed` rows under a read-only `update`, the figure
the spec pinned. That figure cannot be compared with a re-adopted receipt, because re-adopting
against 73113582 attributes this build's own newer engines too. So the control clone was re-adopted
with no rows, and it reads 22. The clone with the five rows reads 18. The four that left are the
four programs, and `scripts/check-docs-hygiene.sh` was never an `unattributed` row.

`check` on `%TEMP%/ic13` printed five parity lines. `gen-build-index` holds 2 of 3, because the file
lacks the four names `marker-contract.test.sh` imports, and that test is marked as an installed
consumer that cannot run. `corpus-ids` holds 0 of 2: its `--print-defined-ids` prints its usage and
exits 2, which marks `scripts/manifest-check.sh`, and it has no `ask_shell`. `gotchas` holds 1 of 1.
`merge-rows.py` prints `contract (none)`. `hygiene-print-modes` holds 1 of 3. inCMS's
`check-docs-hygiene.sh` ignores `--print-append-only-ere` and `--print-rotated-archive-ere` and runs
its whole 119-second check instead. The failing rotated-archive clause marks `scripts/row_grammar.py`.
Gov's `scripts/check-memory-hygiene.sh` printed one line saying no emitted leg runs it.

That measurement changed the build twice. The print-mode clauses first expected any output at all,
and that read inCMS's failing hygiene output as a pass. They now expect one line, or one path per
line. The probe timeout went from 120 s to 60 s. `check` exited 1 on two findings that predate this
unit: `check-testsuite-counts` declares no `[check]`, and the `pytest-ini-knobs` hole is
undischarged. The parity report added no finding.

**Evidences:** DEPL-aRepatriatedFork-13
- AC1 — `[[own]]` — `adopt --write` exits 1 naming `[[own]] row 1` for `tools/demo/run x.py`, graded as `'own.path'`, and for `../run.py`, refused as leaving the target repository. Both files exist, so neither refusal is the missing-file one, and no receipt is written
- AC2 — `seed` — `implements = "demo:seed.txt"` exits 1 with `names a source gov ships as seed`. A source a rendered rule reaches beside its engine rule exits 1 with `ships as rendered`
- AC3 — `adopter-owned` — after gov moves one commit, `update --write` prints `adopter-owned 1` in its summary, no `unattributed`, and the receipt's `gov_commit` equals the new gov HEAD
- AC4 — `unattributed` — the same arm group run against a7c78ad2's `govkit.py` adopts the owned file as `unattributed 1, verbatim 3`, and `update --write` prints `The receipt is NOT re-stamped: 1 row`. The suite keeps a current-engine control arm that records the row `unattributed` and sees the stamp withheld
- AC5 — `[[contract]]` — `govkit selfcheck` exits 0 over this repo and names all four memory-tree contracts. The scratch gov's selfcheck names `demo/run`, and exits 1 on a clause citing `tools/demo/nope.py` and on `demo/empty`, which has zero clauses
- AC6 — `govkit check` — prints `contract demo/run <- tools/demo/run.py: 1/2 clauses hold` and `FAILS imports beta — needed by tools/demo/use.py`, and exits 0. With `use.py` dropped from the receipt, the clause prints without the mark and the exit is still 0
- AC7 — `INSTALLED CONSUMER CANNOT RUN` — the same line carries `INSTALLED CONSUMER CANNOT RUN: tools/demo/use.py against tools/demo/run.py`, and the exit stays 0. With `use.py` on an emitted leg's argv, `check` exits 1 naming that leg, which is F3's escalation
- AC8 — `measured-pins` — the fixture's `when_owned` hole prints `stood down — run.py adopter-owned here`, and with the row recorded `engine` the same hole prints `is UNDISCHARGED`. At `%TEMP%/ic13`, `measured-pins` and `stale-header-waiver` both print as stood down
- AC9 — `unattributed` — at `%TEMP%/ic13`, `update` counts 18 `unattributed` rows against the control clone's 22, and none of the four programs is among them. It prints five parity lines, and `check` prints `measured-pins` stood down. The `row_grammar.py` mark is re-derived under spec rev-3, since `row_grammar.py` no longer imports `parse_conf` from `corpus_ids.py`. `row_grammar.py` is still marked, for the rotated-archive print mode. Both figures are re-derived here: the pinned 12 and 8 describe a receipt taken at a7c78ad2
- AC10 — `govkit update` — one scratch gov and one target with no `[[own]]` rows. Only `govkit.py` changed between runs: this unit's, 73113582's, then a7c78ad2's. Read-only `adopt`, read-only `govkit update` and `govkit check` gave byte-identical stdout and identical exit codes (0, 0, 1) under all three

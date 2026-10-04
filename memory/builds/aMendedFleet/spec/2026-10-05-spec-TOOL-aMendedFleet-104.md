# TOOL-aMendedFleet-104 — the foreign-prefix leg declares `review-replay selftest` a whole run

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 105

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The held `foreign-prefix parity (every self-test at three prefixes)` leg reds on the daily remote CI
job with `[scripts] review-replay selftest · probe · rc 0 · 1s · RED, an undeclared whole run: it
printed no probe marker, so it ran every arm`. That is cause C8 of the held-red census. The leg runs
every self-test row with `FOREIGN_PREFIX_PROBE=1` and requires each row either to print the marker
`foreign-prefix-probe: stopped after 1 arm` or to be declared in its `WHOLE_RUN` array. The
`review-replay selftest` row is neither. It is the `--selftest` mode of a SHIPPED engine,
`tools/workflows/review_replay.py`, which is exactly the kind of row the array already declares, nine
times, with the reason that a probe site there would be adopter-facing. This unit adds the tenth.

## 2. Scope (IN)

- **S1** — `WHOLE_RUN` in `tools/run-gates/foreign-prefix.gov.test.sh` gains the row
  `review-replay selftest`, with the reason string its nine shipped-engine siblings carry verbatim.
  Observed by AC1, AC2 and AC3.
- **S2** — The remote observation: the first scheduled run of the remote CI workflow after landing
  prints the row as a declared whole run and no longer reds it as an undeclared one. Observed by AC4.

## 3. Non-goals (OUT)

- A probe site inside `review_replay.py`'s `run_selftest`. The tool ships to adopters under
  `tools/workflows/kit.toml`'s engine rule, and the array's stated reason for every sibling row is that
  a probe site in a shipped engine is adopter-facing. The whole suite costs about a second, so running
  it whole at each prefix costs nothing the leg would notice.
- The leg's other red rows on the census runs, `row-grammar selftest` and `settings-merge selftest`.
  Both are already declared whole and red on their exit code from cause C1, which is unit 97's; the
  job stays red until that unit lands.
- Catching an undeclared shipped `--selftest` row before the held job does. The leg itself reds both
  directions; that it is held off the bar is the 2026-08-23 owner ruling, and moving it is not this
  unit's.

### Edges

none

## 4. Design

### Evidence

Read at HEAD `34a99ad1`, whose bytes for every file below equal base `7af5f564` and `origin/main`.

- The census row for cause C8, in
  `memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md`, quotes
  the CI line and names `tools/run-gates/foreign-prefix.gov.test.sh` line 248, the `run_row` verdict.
- On node a, `FOREIGN_PREFIX_PROBE=1 python tools/workflows/review_replay.py --selftest` exits 0,
  ends `selftest: 19/19 arms`, and prints the marker zero times. The row is therefore a whole run, and
  the leg's verdict on it is correct for an undeclared row.
- The row is declared by `tools/workflows/kit.toml` as `review-replay selftest`, landed 2026-10-01 by
  commit `c84cf6661` of the aSightedSkeptic build. The probe and `WHOLE_RUN` landed the same day with
  the aRepatriatedFork build's unit 52, and neither build saw the other's row; the census reads no
  review-replay row in the 10-02 run's log.
- `run-selftests.sh --list` prints the row as `review-replay selftest` with argv
  `python3 tools/workflows/review_replay.py --selftest`, so the population name the declaration must
  match is that string.
- `WHOLE_RUN` carries nine rows whose reason is `a --selftest mode of a shipped engine, so a probe site
  would be adopter-facing`, among them `shell-hygiene selftest`, which `tools/workflows/kit.toml` names
  as the model this row mirrors.

### Mechanism

One array element, placed after `playbook render selftest` so the shipped-engine rows stay together
before `tier2-review self-test`:

```
  "review-replay selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
```

`run_at_prefix` then queues the row for the serial whole-run pass rather than the pool, and `run_row`
grades it `whole`: green on exit 0 with no marker, red as a stale declaration if it ever prints one.
The stale-declaration check before the prefix loop reds if the name stops matching a population row.
No function, floor or other row changes.

### Files touched (estimate)

- `tools/run-gates/foreign-prefix.gov.test.sh`

### Alternatives rejected

- **Honour the probe in `run_selftest`.** It would make the row green as a probe row, at the price of
  an environment branch in a file every adopter receives, which is the trade the array's reason
  refuses for every sibling engine.
- **Exempt the row from the leg altogether.** The row's prefix question is real: the tool reads no
  path outside its kit, and running it whole at a foreign prefix is the check that this stays true.

## 5. Production-readiness checklist

- security — N/A: a test file's declaration list; no input, write path or surface.
- perf / scale — about one second per prefix, run serially after the pool drains.
- error / empty / loading states — the leg's stale-declaration and stale-marker lines cover both ways
  this declaration can go wrong.
- observability — the leg prints `declared whole run — review-replay selftest` with its reason on
  every run.
- risks — none beyond a byte mismatch with the population name, which the stale-declaration check
  reds.
- testing — AC1 to AC3 are direct and take seconds; AC4 is the held job's.
- migration — N/A.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `grep -c '"review-replay selftest|a --selftest mode of a shipped engine' tools/run-gates/foreign-prefix.gov.test.sh`
  runs, it prints `1`.
  Red when: the declaration is absent, which at base printed `0` and on CI read as `an undeclared
  whole run`.
- **AC2** — When `FOREIGN_PREFIX_PROBE=1 python tools/workflows/review_replay.py --selftest` runs on
  node a, it exits 0 and prints no line equal to `foreign-prefix-probe: stopped after 1 arm`, which is
  the exact condition the leg's `run_row` grades green for a `whole` row.
  Red when: the tool prints the marker, so the new declaration reads as stale.
- **AC3** — When `grep -n 'name = "review-replay selftest"' tools/workflows/kit.toml` runs, it prints
  one line, and the quoted name is byte-equal to the name AC1's declaration carries before its `|`.
  Red when: the two spellings differ, which the leg reports as a whole-run declaration naming no row.
- **AC4** — When the first scheduled run of `.github/workflows/remote-ci.yml` after landing completes,
  `gh run view` with `--log` over its foreign-prefix parity job prints
  `foreign-prefix: declared whole run — review-replay selftest` and no `review-replay selftest` row
  marked `an undeclared whole run`.
  Red when: the CI log still carries the C8 line.
  permission: the leg is held; no unit pass runs it. The main loop reads this log after landing, and
  may run the leg on demand filtered by its own `--kit review-replay` option. The job may still fail
  on cause C1's rows until unit 97 lands; the review-replay row is graded at the `scripts` prefix
  either way, because that prefix runs every row before it is judged.

## 7. Gates

`foreign-prefix parity (every self-test at three prefixes)` · `spec tokens (a spec's own names resolve)`

The guards join owes no further leg: the one path in Files touched trips only the broad `tools/` and
`tools/run-gates/` guards, which `tools/check-spec-tokens.py` excludes and prints.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the held-red census row for C8, the row run on node a under
  the probe environment, and the leg's declaration list at base.

## 10. Reuse audit

The seam is the leg's own `WHOLE_RUN` array in `tools/run-gates/foreign-prefix.gov.test.sh` and its
existing shipped-engine reason string, reused verbatim; no new mechanism is owed.
`python tools/codebase-map/reuse_lookup.py "declare a self-test that cannot stop after one arm as a
whole run in the foreign-prefix leg"` returned only generic `run` symbols and prints `unscanned
layers: .sh`, so it cannot see the shell array; the seam was found by reading the leg. Recall returned
the aRepatriatedFork build's unit 52 spec, which defines the flag, the marker and the declared
whole-run list, and its acceptance ledger, whose AC3 observed a declared row that prints the marker
reds as stale; that is the direction AC2 guards.

Where the report and the tree disagree: none. The census named both remedies; the tree's nine sibling
declarations decide between them.

Recall terms used: `python tools/memory-recall/query.py "how does a shipped engine's --selftest row satisfy the foreign-prefix probe, and why are such rows declared whole runs" --terms "foreign-prefix FOREIGN_PREFIX_PROBE WHOLE_RUN whole-run probe marker stopped-after-1-arm shipped engine adopter-facing --selftest aRepatriatedFork-52"`

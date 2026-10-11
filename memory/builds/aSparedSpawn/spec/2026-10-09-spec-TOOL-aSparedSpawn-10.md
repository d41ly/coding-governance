# TOOL-aSparedSpawn-10 — foreign-prefix parity probes one shard per sharded suite and pools its whole runs

**Status:** INPROGRESS · rev-3 · 2026-10-11 · node a · Tier-2 · base 22efab65 · streams tooling · order 2 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aSparedSpawn-10-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-10-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`foreign-prefix parity (every self-test at three prefixes)` spends most of each prefix on two
classes of row that buy little. On the profiled bar's `[scripts]` prefix, shards 2 to 8 of the two
sharded unattended suites took 4094 of the 6709 probe leg-seconds, each paying the whole suite
prologue for one arm, and the declared whole-run rows ran serially after the pool drained, 611 s
(`memory/builds/aMeteredSweep/build/2026-10-08-build-TOOL-aMeteredSweep-1-research-other-legs.md`,
"foreign-prefix parity"). This unit probes one shard per sharded family and runs the whole-run rows
inside the pool under the load-scaled hang bound aMeteredSweep already landed. The round-two menu
estimates about 2.4 ks a run on node `a`; it is an estimate, not a reading.

## 2. Scope (IN)

- **S1** — Sharded families are DERIVED from the population, never declared: rows whose argv ends in
  `--shard <i>/<n>` and is otherwise identical form one family. Per prefix, one row of each family is
  probed and every other row prints `[<prefix>] <row> · represented · by shard <k>/<n>`, a skip that
  announces itself and is counted neither as graded nor as passed. Observed by AC1 and AC2.
- **S2** — Which shard represents a family is chosen by the rule F1 resolves, and every run prints
  the rule's input and its answer. The modulus is the family's SELECTED size, which is its arity on
  an unfiltered run, and the family's rows are taken in shard order. The kit version marker is the
  line its `kit.toml` `version_from` names, read at HEAD and at HEAD's first parent; a HEAD with no
  first parent probes every shard, and a kit declaring no marker is said so and rotates. Observed by
  AC3.
- **S3** — Whole-run rows are dispatched into the same pool as probe rows, before them and longest
  budget first, each still bounded by `run_row` at `HANG_FACTOR` times `LOAD_RATIO` times its budget.
  The deferral into a serial tail after `wait` (`tools/run-gates/foreign-prefix.gov.test.sh:317-328`)
  is undone. Observed by AC4 and AC5.
- **S4** — A `--plan` flag prints, for gov's own prefix, each row's kind (probe, whole or
  represented) and the dispatch order, then exits without cloning and without running a suite, so the
  selection is observable in the time of one `run-selftests.sh --list` (77 s on node `a`, measured
  2026-10-11). The plan reuses that one listing for the stale-declaration guard. Observed by AC1, AC3
  and AC4.
- **S5** — The existing both-directions guards stand and run under `--plan` too: a `WHOLE_RUN` or
  `GOV_LAYOUT` entry naming no row reds, a whole row printing the probe marker reds, a probe row
  printing none reds, and a prefix that selected no row reds. Observed by AC6.
- **S6** — The header's "WHAT THIS DOES NOT CHECK" list gains the shard line in §4. NOT OBSERVED —
  header prose, read in the diff.
- **S7** — The leg is timed before and after, quiet, on a frozen clone. Observed by AC7.
- **S8** — ADOPTED from TOOL-aSparedSpawn-8's pass. `shell hygiene (a loop fed by a command
  substitution)` is red since `786644cee`, whose top-level exit arm in
  `tools/unattended/unattended.test.sh` reads a loop over a here-string of a variable assigned from
  `$(awk …)`. The scan's capture is written to a file under the suite's scratch and the loop reads
  that file, so the site is gone rather than registered: the registry's `<<<` count for that suite
  stays the one site that predates the leg. Observed by AC8.
- **S9** — ADOPTED from TOOL-aSparedSpawn-8's pass. The `run-gates-2leg` row of
  `memory/project/fork-ceilings.txt` reads 95 or 96 because the pool polls its workers, and its
  ceiling of 96 reds a reading of 97 for no defect. The row takes a STATED MARGIN rather than a
  deterministic count: its ceiling becomes 99, the highest reading plus 3, which is also the most the
  stale direction admits at the lowest reading (95 plus max(3, 5 %)). The row's reason says so.
  Making the count deterministic means changing the runner's polling, which is not this unit's
  subject. Observed by AC9.

## 3. Non-goals (OUT)

- Change-scoped row selection by `gate-legs.json` guard paths (round one's lever 3). It needs a
  recorded green at a sha, which is a new record to keep honest.
- Dropping one of the `scripts/` and `vendor/gov/` prefixes. They differ in depth, and a
  `..`-counting prologue can pass one and fail the other (round one, lever 4, not recommended).
- Moving any suite's `FOREIGN_PREFIX_PROBE` site earlier in its prologue.
- Re-measuring `LOAD_RATIO` per dispatched row; it stays measured once per prefix.

### Edges

none

## 4. Design

### What a shard probe actually asks

Round one wrote that shards 2 to 8 "answer the same question", because `--shard k/8` only selects
arms. That holds for the PROLOGUE. It does not hold for the arm: each sharded suite carries one
`FOREIGN_PREFIX_PROBE` stop per region, at the head of that region (`tools/unattended/unattended.test.sh`
`:795`, `:2230`, `:3872`, … and `tools/unattended/check-unattended.test.sh` `:812`, `:1249`, …, eight
each at 22efab65), so shard k's probe runs the prologue plus the first arm of region k. Probing one
shard therefore keeps the prologue's question at every prefix and gives up seven first-arms per
family per prefix. F1 is how that loss is bounded. The header says so in one line: "a shard-specific
prefix defect in a region's first arm is seen only when that region's shard is the representative".

### Whole rows in the pool

Whole rows were serial because "its budget was measured one suite at a time" (`:317`). Since
aMeteredSweep's S10 that budget is a hang guard and not a cost verdict (`:241-252`): `HANG_FACTOR=3`
at `:253`, scaled by `measure_load_ratio` at `:255`, applied in `run_row` at `:271-285`. A cost
verdict at a foreign prefix is not this leg's question; the bar grades cost at gov's own prefix.
Dispatching them first, longest budget first, keeps the longest row off the tail.

### Selection, one function

The row loop at `:300-322` today both classifies and dispatches. It is split so `--plan` and the run
share one classifier: a pass reads the `--list` population into arrays, classifies each row, orders
the dispatch, and either prints the plan or runs it. `--kit` filters before families are formed, so
a filtered run's family is the rows it selected.

### Inventory

| identifier | kind | cell that grades it |
|---|---|---|
| `--plan` | CLI flag of the suite | none |
| `load_population` | shell function: the `--list` text into row arrays, filtered | `lexicon naming predicates`, shell cell |
| `derive_row_kinds` | shell function: each row's kind and representative, one rule line per family | `lexicon naming predicates`, shell cell |
| `derive_dispatch_order` | shell function: whole rows by descending budget, then probe rows | `lexicon naming predicates`, shell cell |
| `read_kit_marker` | shell function: a kit's version marker line at a revision | `lexicon naming predicates`, shell cell |
| `print_plan` | shell function: the `--plan` body and its one-probe-per-family count | `lexicon naming predicates`, shell cell |
| `check_declarations` | shell function: the stale `WHOLE_RUN` and `GOV_LAYOUT` guard, shared by both paths | `lexicon naming predicates`, shell cell |
| `represented` | verdict word on a row line | none |

### Files touched (estimate)

- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/unattended/unattended.test.sh` (S8)
- `memory/project/fork-ceilings.txt` (S9)

### Alternatives rejected

- **A declared `SHARD_REP` array** (round one's proposal). A declaration is a second answer to a
  question the argv already answers, and it goes stale when a suite is resharded.
- **Probe shard 1 always.** Region 1's first arm would be the only one ever probed at a foreign prefix.
- **Whole rows serial but concurrent with the pool's tail.** Saves less and keeps two dispatchers.

## 5. Production-readiness checklist

- security — No new surface; the leg still runs in a scratch clone it deletes.
- perf / scale — Round one: ~500 s wall per prefix from S1 and ~300 s from S3, estimates on node `a`.
- error / empty / loading states — An empty selection still reds; a represented row is never a pass.
- observability — Every represented row and the representative rule print on every run.
- risks — A shard-specific prefix defect waits until rotation reaches its region (F1); whole rows
  now share the pool's load, and the hang bound is measured once per prefix before the pool starts.
- testing — `--plan` makes classification observable without a clone; the staged breaks in §6.
  Inside a pass the leg file cannot run at all, `--plan` included, so the pass observes the same
  classifier through a fixture that runs the plan branch's calls over the leg's own classifier block.
- migration — If the run-gates kit ships this file, its version bumps; `kit epoch` decides.
- user docs — N/A — the leg's header is its documentation.

## 6. Acceptance criteria

- **AC1** — When the suite runs with `--plan`, it prints one line per row with its kind, exactly one
  row of each sharded family is `probe`, every other shard row is `represented`, and no clone is made.
  Red when: a family has two probe rows or none, a shard row is missing from the plan, or a clone
  directory appears under `TMPDIR`.
- **AC2** — When a prefix runs with `--kit unattended`, each represented row prints its
  `represented · by shard <k>/<n>` line, and the prefix's summary counts it apart from graded rows.
  Red when: a represented row is silent, or counted in the graded or passed figure.
  cost: one filtered run, three clones and moves; minutes on node `a`.
- **AC3** — When `--plan` runs at two commits whose rotation input differs under the rule F1
  resolves, the plan prints that input and a different representative for the same family.
  Red when: the representative never moves, or the input is not printed.
- **AC4** — When `--plan` runs, every `WHOLE_RUN` row is dispatched before any probe row, in
  descending budget order, and `git grep -n 'runs/whole'` over the suite prints nothing.
  Red when: a whole row is ordered after a probe row, or the serial replay remains.
- **AC5** — When one whole row's budget is staged to 1 s in a scratch copy of
  `tools/run-gates/selftest-budgets.txt` and that row runs filtered by `--kit`, its line reads
  "a hang: killed at" with the scaled factor, and the pool's other rows are not held behind it.
  Red when: the row runs unbounded, or the verdict line names no factor.
- **AC6** — When a `WHOLE_RUN` entry naming no row is added in a scratch copy of the suite, `--plan`
  exits 1 naming it.
  Red when: `--plan` exits 0, which means the plan path skipped the stale-declaration guard.
- **AC7** — When the leg runs once at base 22efab65 and once after the pass, quiet, on a frozen
  clone, both wall times are recorded with the instrument in the build folder, and the after time is
  lower.
  Red when: the after time is not lower.
  figure: DERIVED at observation; round one's ~3000 s per green run is an estimate, not a target.
  cost: two whole runs of the leg, about 4500-5000 s each on node `a` by round one's estimate.
  permission: held suites are the owner's manual run (owner ruling, 2026-10-06).
- **AC8** — When `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`
  runs before the pass, it names the unattended driver's suite with 2 measured sites at `<<<` against
  1 declared; after the pass it exits 0 with no finding, and the registry is unchanged.
  Red when: the checker still names that suite, or the pass widened the registry row instead.
- **AC9** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only
  run-gates-2leg` runs after the pass, the row reads ok at ceiling 99, and the row's reason names the
  margin and the readings it is set over.
  Red when: the count reads above 99, the stale direction reds, or the reason states no margin.

## 7. Gates

`foreign-prefix parity (every self-test at three prefixes)` ·
`testsuite counts (every bar self-test prints one)` ·
`kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` ·
`spec tokens (a spec's own names resolve)` ·
`shell hygiene (a loop fed by a command substitution)` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`python resolver (behaviour + inline parity + idiom ban)` · `pre-push run-log line` ·
`push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `recall floor` ·
`recall floor arms` · `run-gates canary` · `run-gates evidence` · `run-gates turnstile` ·
`run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` ·
`profile-bar selftest` · `install-prefix self-test` · `dead-path carriers self-test` ·
`spec-tokens self-test` · `kit-placeholders self-test` · `unattended kit gate` ·
`codebase-map coverage + freshness`

New arm: tools/run-gates/foreign-prefix.gov.test.sh --plan · covers AC1 AC3 AC4 AC6 · a stale WHOLE_RUN entry, and a second probe row forced into one family · FLOOR_ASSERTIONS unchanged

## 8. Open questions

- **F1 — Whether skipping shards 2..8 at foreign prefixes leaves a shard-specific prefix bug unseen,
  and how the representative is chosen.** It does: each shard's probe runs its own region's first arm
  (§4), so a prefix defect reached only there is unseen until that shard is probed.
  - (a) Rotate by commit: representative index = (HEAD's sha as an integer) mod n, plus one; and run
    every shard of a family when the sharded suite's kit version marker differs from HEAD's first
    parent's.
  - (b) Rotate by commit, with no full run on a version bump.
  - (c) Always shard 1; accept the loss.
  - (d) Every shard, as today; take only S3's saving.
  - Recommendation: (a). A version bump is when a prefix defect is likeliest to ship, and rotation
    reaches every region within about n landings.
  - RESOLVED (owner, 2026-10-10): (a) rotate by commit, and run every shard on a kit version bump.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-11 · §2 §4 §6 §7 S2 S4 S8 S9 AC8 AC9 · the build pass. S8 and S9 adopt the two
  reds TOOL-aSparedSpawn-8 found, each with its own criterion. S2 says what F1's (a) reads: the
  modulus is the family's selected size, and the marker is the `version_from` line of the suite's
  kit at HEAD and at its first parent. S4 no longer promises seconds: one `--list` took 77 s on node
  `a`, so the plan lists once and reuses it for the declaration guard. The inventory names the
  functions the split makes. AC2, AC5 and AC7 run the leg itself, so they are owed at VERIFYING; AC3
  is observed on a hand-built scratch clone at two commits, and AC6 on a scratch copy there.
- rev-3 · 2026-10-11 · §5 · the build pass. The unattended kit's gate-guard refuses any command that
  runs this leg's file before VERIFYING, `--plan` included, so AC1, AC3, AC4 and AC6 as worded are
  observed at VERIFYING with the other owed criteria, and rev-2's scratch-clone and scratch-copy
  routes for AC3 and AC6 are withdrawn. The pass observes the same classifier through a fixture,
  committed beside the acceptance ledger as `2026-10-11-build-TOOL-aSparedSpawn-10-plan-fixture.sh`:
  it extracts the leg's lines from `SELF_ROW=` to the `--plan` branch verbatim and runs that
  branch's five calls over a hand-built git repository holding the real unattended `kit.toml` and
  driver, at a root commit, at two commits whose rotation input differs, at a version bump, and
  with a stale `WHOLE_RUN` entry and a second probe row each staged. AC4's `git grep` half needs no
  run and is observed in the pass.

## 10. Reuse audit

No existing seam fits: `tools/codebase-map/reuse_lookup.py "run one row of the foreign prefix
population in a pool"` ranks only name-stem hits (`rows`, `row`, `run`, `run_arms`), none of which
classifies a self-test population. The unit reuses the suite's own `run_row`, `HANG_FACTOR` and
`measure_load_ratio`, landed by aMeteredSweep, and changes no shared code.

Recall terms used: foreign-prefix probe WHOLE_RUN shard hang bound HANG_FACTOR load ratio pool width marker

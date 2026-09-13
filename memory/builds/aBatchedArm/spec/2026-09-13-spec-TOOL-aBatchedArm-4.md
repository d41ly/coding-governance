# TOOL-aBatchedArm-4 — declared execution modes for the self-test runner

**Status:** OPEN · rev-1 · 2026-09-13 · node a · Tier-2 · base c2db2f5d · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates/run-selftests.sh` grades 61 suites and has two execution shapes: a no-flag serial
loop that issues cost verdicts, and `--sweep`, which pools and withholds them. The owner ruled that
the mode is DECLARED — pooled available, serial possible when deliberately chosen — and that the row
checker stops redding a `--shard i/n` token. This unit does both, and does the three things the
tree's own records say are needed for the pooled half to be sound rather than the shape that already
killed 14 of 58 suites once.

## 2. Scope (IN)

- **S1** — the row checker at `run-selftests.sh:357-361` admits a numeric-ratio token. The predicate
  is a REGEX, `^[0-9]+/[0-9]+$`, not the glob `[0-9]*/[0-9]*`: the glob is one digit then anything,
  so `3rdparty/1.sh` and `2026/09-notes.md` would skip the tracked-path check — verified by staging
  both. Observed by **AC1**.
- **S2** — the executing mode is DECLARED: `--serial` and `--pooled` are the two spellings, the
  bare `run` invocation REFUSES naming both, and `--sweep` stays as an alias of `--pooled` so no
  recorded invocation breaks. `--check`, `--list` and `--rank` execute nothing and take no mode.
  Mode resolution sits AFTER the `--check` exit at `:322`, because the width block before it runs on
  every bar through the unguarded `--check` leg, and a refusal placed there reds the merge bar rather
  than an on-demand run. Observed by **AC2** and **AC3**.
- **S3** — the three callers declare their mode in the same commit: `run-unattended-gates.sh:263`
  passes `--serial`, and the four arms of `run-selftests.test.sh` that invoke the bare mode pass it
  too. The strings those arms assert — `self-tests GREEN|RED`, `OVER BUDGET`, the unresolved-row
  `FAIL` line — are emitted unchanged by `--serial`. Observed by **AC4**.
- **S4** — cost verdicts are issued ONLY under `--serial`, and the reason is stated in the runner's
  header rather than implied: contention dilation on this population is not a scalar — 1.5 to 1.85x
  for a bar leg, 3 to 15x under the sweep, 5.5x median across concurrent bars — so no multiplier
  turns a serial budget into a pooled one, and the full sweep of 2026-09-08 that tried x3 killed 14
  of 58 suites. `--pooled` withholds every cost verdict and counts them, as `--sweep` does today.
  Observed by **AC5**.
- **S5** — the pooled HANG bound is a declared factor over the serial reading, separate from the
  cost budget, and it is re-declared from the 2 that killed 14 rows to a value the first pooled run
  of the shard rows measures. The killed ratios were censored at 3.0, so no existing data says what
  factor suffices; the number is derived from that run and written beside the declaration with its
  reading. Observed by **AC6**.
- **S6** — the two `tools/install-prefix-carried.txt` BANS this unit trips are raised by hand with a
  fourth-column reason, because the ratchet can lower a count and never raise one:
  `run-selftests.sh` at exactly 6 carried literals, and `selftest-budgets.txt` at 14, which eight
  shard rows with explicit argv raise to 22 (observed `ROSE 14 -> 15` with one row staged). Owed as a
  deliverable and named here so it is not discovered at the push. Observed by **AC7**.

## 3. Non-goals (OUT)

- **A contention model that makes a pooled cost verdict sound.** `TOOL-aPooledSweep-2` left an
  explicit edge that a future unit wanting a pooled reading to grade anything must establish one
  first. This unit does not; it withholds, which is what the existing design already does and what
  the 14 kills say is the only honest verdict.
- **A per-row mode column.** Every reader stops at `f[3]`, a fifth column lands in `argv` and is
  `eval`'d, and the mode a row needs is a property of the RUN, not the row: the same shard row is
  graded serially for its budget and run pooled for its speed. Mode per invocation, not per row.
- **Teaching `--rank` to accept a `pooled@` reading.** Refused by `TOOL-aQuenchedHarness-6` S3a and
  armed at `run-selftests.test.sh:272-275`: a contended reading must never rank beside serial ones.
  The shard rows' budgets are SERIAL readings, taken by a one-off `--serial` pass of the eight rows,
  so they carry no such token and `--rank` is untouched.
- **Taking the turnstile.** The runner composes its condition token from knobs and observes nothing
  about the host, so `pooled@8x1` is byte-equal between an idle box and one where another worktree's
  bar is running — which is the state the full sweep recorded. That gap is real and is
  `TOOL-aBatchedArm-3` AC4's "idle box" with no mechanism behind it; it is named here and not built.
- **Re-hosting the gov canary's shard-join arm over the budget rows.** It would red immediately on
  `unattended.test.sh`, which declares `SHARD_ARITY=2` and whose budget row calls it whole. That is
  `TOOL-aBatchedArm-3` S4's problem and it must scope the arm to scripts a row calls WITH `--shard`.

### Edges

- **consumes-from** `none`
- **hands-off** `TOOL-aBatchedArm-3` — the eight rows, the arity raise and the calibration run that
  measures S5's factor. The two must land together: the suite pins `SHARD_ARITY=2` three times and
  refuses `--shard 1/8` today, so a row that resolves at the runner still exits 2 at the script.

## 4. Design

### Why the mode is per invocation and why bare `run` refuses

The owner's ruling reads serial as the DECLARED option. Two facts from the tree decide how: the one
caller that reports cost, `run-unattended-gates.sh:263`, invokes the runner bare and reads only the
exit code — under a silent pooled default it would print GREEN with every delegated budget withheld;
and four arms of the runner's own held self-test assert serial-only strings on the bare invocation.
So a silent default in EITHER direction is a coupling nobody declared. Bare `run` refuses, both
callers declare, and the refusal names both spellings.

### Why a pooled cost verdict is withheld and not scaled

Read the tree's own numbers before proposing a factor. `TOOL-aScannedThrottle-6`: 1.5 to 1.85x for
a bar leg at width 8. The full sweep record, 2026-09-08: four small suites at 3 to 15x under
`pooled@8x1`, an 8 s suite killed at 121 s. The budgets header: 5.5x median and 47.1x worst across
concurrent bars. Three "8-wide" conditions, fifteen-fold apart, and the token unchanged across them.
The sweep's bound was `budget x sweep-ceiling-factor 2`, three times the worst serial reading, and it
killed 14 of 58. A number that cannot be predicted from the declared condition is a number a verdict
must not rest on.

### What the cost model says about the goal, said here because it bears on the whole build

The pooled-sweep record's cost model: the gate self-test costs what it costs because it makes
roughly 53,000 forks at roughly 190 ms each on a SERIALISED spawn path, and "a pool contends on
precisely the resource the work is made of, so widening it inflates every member". The nine-suite
A/B reached 1.72x at width 8, not 8x, and the three-suite A/B was a LOSS with both long suites
slower pooled. **Eight shards of a fork-bound suite, 8-wide, on this host, share that path.** Whether
they reach 20 minutes is `TOOL-aBatchedArm-3` AC4's measurement and nothing else answers it; this
unit is what makes that measurement runnable, and it is designed so AC4 can FAIL and be read —
per-shard readings printed, the width pair printed, the whole-suite figure derived from the eight.
On a node without the on-access scanner (`TOOL-aGradedDoorway-8`: 19 to 39 ms per spawn against
251 here) the same split is trivially inside the target. The target may be a property of the host.

### Rollout

S1 first, alone, because it is one regex and unblocks everything. S2 and S3 in one commit, because
the refusal and the callers that satisfy it cannot be split across a bar. S6 before any shard row is
staged. S4 and S5 with `TOOL-aBatchedArm-3`, since the factor is measured from its rows.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh`, `tools/run-gates/run-selftests.test.sh`,
`tools/unattended/run-unattended-gates.sh`, `tools/run-gates/selftest-budgets.txt` (the factor
declaration), `tools/install-prefix-carried.txt`, and this build's records.

## 5. Production-readiness checklist

- security — N/A. Scheduling and verdict wording; no suite's subject changes.
- perf / scale — the pooled mode is the whole point and its wall clock is measured by unit 3's AC4.
- error / empty / loading states — bare `run` refuses naming both modes; an unknown mode token
  refuses as today; a factor that is absent or non-numeric refuses the pooled run rather than
  defaulting, which is the rule `sweep-ceiling-factor` already carries.
- observability — a pooled run prints the width pair and the factor it derived each bound from, and
  every withheld verdict is counted and named, so a GREEN under `--pooled` cannot be read as a cost
  claim.
- risks — the pooled mode has killed a quarter of its population once. S5's factor is the guard, and
  it is measured rather than guessed. The second risk is the spawn path making the goal unreachable on
  this host, which is stated in §4 rather than discovered at AC4.
- testing — the runner's own self-test gains one arm per refusal and one per mode, each staged and
  observed RED first.
- migration — `--sweep` aliases `--pooled` and no recorded invocation breaks; the two callers that
  invoked bare `run` declare `--serial` in the same commit.
- user docs — the runner's `--help` names both modes and the reason bare `run` refuses.

## 6. Acceptance criteria

- **AC1** — When a budget row's argv carries `--shard 1/8`, `run-selftests.sh --check` passes; when
  it carries an untracked path whose first component begins with a digit, `--check` still REDS
  naming it.
  Red when: either direction fails, which is the glob-versus-regex difference the skeptic staged
  with a digit-led directory name.
- **AC2** — When `run-selftests.sh` is invoked with no mode flag, it exits 2 naming `--serial` and
  `--pooled` and executes no suite.
  Red when: it runs serially, which is the silent default the ruling removes.
- **AC3** — When `run-selftests.sh --check` runs on a tree whose rows are valid, it exits 0 without
  touching mode resolution.
  Red when: the mode refusal reaches the `--check` path and reds the bar leg at `gate-legs.json`.
- **AC4** — When `run-unattended-gates.sh --selftests` runs, it invokes the runner with `--serial`
  and its summary line is byte-identical to today's; and the four bare-mode arms of
  `run-selftests.test.sh` pass with `--serial` added.
  Red when: any of the four asserted strings changes, or the kit runner's exit code changes.
- **AC5** — When a suite runs under `--pooled`, its cost verdict is WITHHELD and counted, and the
  withheld count is printed with the width pair; under `--serial` the same suite gets an `OVER
  BUDGET` line when it breaches.
  Red when: a pooled run prints `OVER BUDGET`, which is a verdict resting on a number §4 shows cannot
  be predicted.
- **AC6** — When the first pooled run of the eight shard rows completes, the factor S5 declares is
  written beside its reading, and a re-run at that factor kills no shard.
  `figure:` DERIVED from that run.
  `cost:` one pooled run of eight shards, then one more.
  Red when: the factor is typed from the sweep's 2, which killed 14 of 58.
- **AC7** — When the eight shard rows are staged, `bash tools/check-install-prefix.sh` is green with
  the two raised counts each carrying a fourth-column reason.
  Red when: the leg reds `ROSE`, which is the ban firing on a raise nobody explained.

## 7. Gates

`memory hygiene` · `install-prefix (shipped surface)` · `run-selftests self-test` · `run-gates canary`

New arm: `tools/run-gates/run-selftests.test.sh` · the bare-`run` refusal, the regex admitting a ratio
and refusing a path, and the pooled-withholds-serial-grades pair, each staged and observed RED then
unstaged · floor to move: the suite's own, up by the arms added.

## 8. Open questions

- **F1 · Should bare `run` refuse, or default to `--serial` with a printed notice?** Refuse. A printed
  notice on a caller that reads only the exit code is a notice nobody reads, and that caller is the
  one reporting cost. RESOLVED (agent, 2026-09-13, delegated): refuse; both callers are edited in the
  same commit and there are exactly three of them.
- **F2 · What factor does S5 declare before the first pooled run exists?** None. A factor typed
  before it is measured is the sweep's 2 wearing a new name. RESOLVED (agent, 2026-09-13,
  delegated): the pooled mode REFUSES to run the shard rows until the factor row exists, and the
  first pooled run is taken with the bound disabled and a wall bound only, which is how the reading
  that sets the factor gets taken at all.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft, from a five-lens research fan over the runner, the pooled-sweep
  record, budget attribution, the consumers and the row grammar, each with a skeptic. Two things the
  fan corrected before this was written: the glob form of S1 admits paths and the regex does not;
  and a condition-matching rule for cost verdicts would grade zero of 61 rows today, so the honest
  shape is withhold-under-pool rather than match-and-grade.

## 10. Reuse audit

- **The seam is the runner's existing mode machinery**, verified at source: `MODE` at
  `run-selftests.sh:104`, the `--sweep` branch at `:297`, the withheld counter at `:659-664`, the
  refusal shape `SELFTEST_OUTER_WIDTH` already uses at `:301-315`, and the factor grammar
  `sweep-ceiling-factor` already carries in the budgets header. Nothing is invented: two spellings for
  one existing branch, one refusal in the existing shape, one regex for one glob, and one declared
  factor beside the one that exists. The `--rank` refusal of `pooled@` at `:134` and `:172` is
  REUSED as-is, which is what keeps shard budgets serial readings. The reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "declare a self-test runner's execution mode per invocation and withhold cost verdicts under a pool"`
  — and returned `build_self_chain` and `scan_verdicts` from the process-monitor kit, neither of
  which is this seam; it reports `unscanned layers: .sh`, so it cannot see the runner at all and its
  result is not evidence either way. The seam above was found by reading the file.
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.
  It surfaced `TOOL-aPooledSweep-1` through `-7`, the full-sweep record and `TOOL-aReapedSpinner-23`;
  the five-lens fan then read each at source.

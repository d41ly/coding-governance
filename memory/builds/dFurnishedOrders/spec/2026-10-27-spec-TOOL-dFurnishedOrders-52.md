# TOOL-dFurnishedOrders-52 — the sixth spec audit's 26 minors: a `govkit selftest` row priced for unit 48's runs, the ratchet observed through C5, apply's problems read by their total, one receipt needle, gov's one trip rule, live fixtures, every path token refused, a roles reading any directory reproduces, an interrupt that grades the whole kill, and ledger reads that survive a wrap

**Status:** OPEN · rev-3 · 2026-10-27 · node d · Tier-2 · base 84ab3c6f · streams tooling · order 29 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-50-round6-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-50-round6-fix-return.md) | research | TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-50-round6-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-50-round6-fix-brief.md) | research | TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 |
| [2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`)
confirmed 15 MEDIUM and 11 LOW findings by raw id, beside its two HIGHs, which take
`TOOL-dFurnishedOrders-50` and `TOOL-dFurnishedOrders-51`. BUILD-METHOD M4 batches the minors into
one unit (§8 F1). A finding the report merged into an item still takes its own scope item, and each
takes the severity its raw-id tally gives it (`review-shape` line: medium 15, low 11).

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M1 | 1 | MEDIUM | unit 48 S11, S16, AC5, AC12, §4 clause 1, §7; unit 47 S3 | S1 |
| M1 | 20 | MEDIUM | unit 48 §4 clause 1, Files touched, §7 | S2 |
| M1 | 28 | MEDIUM | unit 47 S3, AC3; unit 48 AC5, AC12; unit 49 §4 | S3 |
| L1 | 10 | LOW | unit 48 §4 clause 1, AC5 cost | S4 |
| M2 | 2 | MEDIUM | unit 48 AC1 | S5 |
| M2 | 7 | MEDIUM | unit 48 S1, AC1 | S6 |
| M2 | 23 | MEDIUM | unit 48 S1, AC1 | S7 |
| M3 | 6 | MEDIUM | unit 47 S2, AC1 | S8 |
| M3 | 13 | MEDIUM | unit 47 S2, AC1 | S9 |
| M3 | 27 | MEDIUM | unit 47 S2, AC1 | S10 |
| L2 | 19 | LOW | unit 47 S2, AC1 | S11 |
| M4 | 8 | MEDIUM | unit 49 S4, S5, §4, AC4 | S12 |
| M4 | 26 | MEDIUM | unit 49 S4, §4, AC4 | S13 |
| L3 | 22 | LOW | unit 49 S4, §4, AC4 | S14 |
| M5 | 9 | MEDIUM | unit 49 S6, §4, AC5 | S15 |
| M6 | 12 | MEDIUM | unit 48 S16, §4, §10 | S16 |
| M7 | 18 | MEDIUM | unit 48 S22, S24; unit 43 AC1, AC2 | S17 |
| M8 | 29 | MEDIUM | unit 48 S25, AC12 | S18 |
| L4 | 4 | LOW | unit 49 AC3 | S19 |
| L5 | 5 | LOW | unit 49 S3, S6, §5 | S20 |
| L6 | 11 | LOW | unit 49 AC3; unit 48 AC10 | S21 |
| L7 | 14 | LOW | unit 47 S1, §10 | S22 |
| L7 | 30 | LOW | unit 47 S1, §4, AC2 | S23 |
| L8 | 15 | LOW | unit 49 S1, AC1, §10 | S24 |
| L9 | 16 | LOW | unit 49 S5, §4 | S25 |
| L10 | 21 | LOW | unit 48 Files touched, §4 clause 3 | S26 |

## 2. Scope (IN)

Each item states the built tree's end state. The pass does what is missing, or records that a landed
unit already left it so, as `TOOL-dFurnishedOrders-41` §4 does.

### The `govkit selftest` budget row (M1, L1)

- **S1** — id 1. The row prices unit 48's runs. The `govkit selftest` row of
  `tools/run-gates/selftest-budgets.txt` (`:66`, 1600 at `84ab3c6f`) is at least
  `ceil(1.5 * (1065 + t + u))`. `t` is unit 47 S3's apply seconds. `u` is the seconds of the runs
  unit 48 adds to the leg (its AC5's two `apply --all`, its AC12's two `apply` and seven `witness`
  runs, and the fixture runs of its AC3, AC4, AC8, AC9 and AC11), plus the runs this unit's own arm
  adds (AC7's witness, and AC8's two `witness` and two `apply`). Observed by AC1.
- **S2** — id 20. Priced where no batch clause breaks. This unit runs at order 29. That is after
  units 47 and 49 have written the budgets file and unit 48 has landed its runs, so no two units at
  one order write the file, and no unit at order 27 reads another's pass as an input. Its §7 names
  both budget legs. Observed by AC1.
- **S3** — id 28. `u` is reproducible from the note. The pass times each command S1 lists once, by
  running that command on a scratch target, never by running the suite. The row's note lists the
  commands and the seconds of each. The estimate at authoring is about 40 s for the two `apply --all`
  (unit 48 AC5's own cost line), PINNED, 2026-10-27. Observed by AC1.
- **S4** — id 10. The note matches the leg's cost. The note opens `worst of 7 readings 1065s`, the
  first `CONDS` shape (`tools/run-gates/run-selftests.sh:430-432`), so `--rank` still reads it. It
  then names `t` and `u` with their figures, so unit 47 AC3's red-when ("the arm's apply lands inside
  the leg with its cost unpriced") does not hold on the tip. Observed by AC1.

### The ratchet's own predicate (M2)

- **S5** — id 2. Unit 48 AC1 is observed through C5 itself. Its ledger answers AC1 in the AMENDED
  form, naming this item. The observation is `bash skills/session-kickoff/manifest-check.sh` on unit
  48's pass tip, printing no line holding `watched files changed since last-audit`, the form unit 46 S6
  uses. No acceptance probe re-types C5's predicate. Observed by AC2.
- **S6** — id 7. The decoy case is graded. C5's `-G'^last-audit:'` search takes no pathspec, and it
  keeps a candidate only where the manifest block's stamp differs from its parent's
  (`skills/session-kickoff/manifest-check.sh:1527-1533`). A scratch clone graded at this pass makes
  two commits after the stamp: one edits a watched path with no re-stamp, and one adds a
  `last-audit:` line to a scratch spec. C5 then prints the failure line, while the copy unit 48 AC1
  wrote names the decoy commit as S. Observed by AC2.
- **S7** — id 23. Empty W passes and empty S fails, as C5 decides (`:1526-1534`). With no watched
  change since the stamp, the scratch clone prints no failure line, and the copy's `merge-base` is
  never reached. Observed by AC2.

### apply's problems, read by their total (M3, L2)

- **S8** — id 6. `n` is apply's own total. `read_emit_problems(stdout)` in `tools/govkit/selftest.py`
  takes `n` from the last line matching `^govkit: (\d+) problem\(s\)$`, and never counts lines.
  Unit 47's arm prints that `n`. Observed by AC3.
- **S9** — id 13. Notes add nothing. `Report.emit` prints every note, then every problem, then the
  total (`tools/govkit/govkit.py:1641-1649`). The problems are the `n` `govkit: ` lines just before
  the total. A note (`:8238`) and a `[[decline]]` line (`:4911`, `:5010`) never join them. Observed by
  AC3.
- **S10** — id 27. Ids by the two quoting forms. Entry ids come only from those `n` lines, matching
  `kit '<eid>'` and `entry '<eid>'`. A problem naming a leg (`:8358`, `:8376`) or nothing (`:7926`,
  `:7945`, `:8204`, `:8226`) is printed verbatim. Observed by AC3.
- **S11** — id 19. One parse, not a whole-output match. `read_emit_problems` is the only reader of
  `Report.emit` output in the suite's new arms, the cure
  `memory/gotchas/line-claim-matched-over-the-whole-output.md` names. Unit 47's ledger answers AC1 in
  the AMENDED form, naming this item. Observed by AC3.

### The roles row's reading (M4, L3, L9)

- **S12** — id 8. A command that reproduces from any directory. The `roles adopter self-test` row's
  note in `tools/run-gates/selftest-budgets.txt` names
  `C=$(git rev-parse --git-common-dir); grep -h '^roles adopter self-test' "$C"/gate-run/*/*.leg "$C"/worktrees/*/gate-run/*/*.leg`.
  That reads the main checkout's windows and every worktree's, the file's rule "across every worktree"
  (`:20-21`). Unit 49's ledger answers AC4 with that spelling, naming this item. Observed by AC4.
- **S13** — id 26. One field, and no empty answer. `R` is the largest tab-separated fourth field of
  the lines printed. The leg name holds spaces, so a whitespace split is wrong. Zero lines printed
  fails AC4, and never reads as `R` = 0. Observed by AC4.
- **S14** — id 22. No directory pairing. The note and unit 49's AC4 drop "run from the main
  checkout's git dir". S12's spelling needs none. Observed by AC4.
- **S25** — id 16. The note in the file's grammar. The roles row's note opens
  `worst of 5 readings 60s` (59.737 rounded up), then names the window, S12's command and `S`. That
  matches the first `CONDS` pattern (`tools/run-gates/run-selftests.sh:430-432`), so `--rank` reads
  the row as backed. Observed by AC14.

### The interrupt arm (M5, L5)

- **S15** — id 9. The arm grades the whole kill path. Unit 51 S3's patch raises on its first call
  only. The arm also asserts two things: the kill path's own `taskkill` child reached the original
  `Popen.wait`, and `run_tree_kill` (`tools/run-gates/regen.py:249-267`) returned normally rather
  than raising. So `proc.kill()` and the reap ran. A failure names the step that did not run.
  Observed by AC5.
- **S20** — id 5. No 15 s wait for a stub that never starts. The patched first call stops polling
  once `self.poll()` shows the child exited before the pid file appeared, and prints
  `DEAD PROBE: stub never started` at once. The standing arm's dead-stub case then costs under a
  second, so unit 49's `S` needs no 15 s term. Observed by AC10.

### The guard arm (M6)

- **S16** — id 12. Gov's one trip rule decides coverage. `check_selftest_guard_coverage` decides
  whether a required path is covered by passing the set to `check-spec-tokens.py --legs-for -` through
  `read_legs_for` (`tools/policy/check_policy.py:3902`), as `check_guard_trace` does (`:4051`), and
  testing that `govkit selftest` is among each path's legs. That replaces unit 48 S16's hand-rolled
  `covered := ...` rule. A glob guard row is printed as unevaluated, never as covering or
  missing. A row `{prefix}/process-monitor` with no trailing slash covers what is under it, as
  `check_guard_trips` reads it (`tools/memory-tree/design_lib.py:589-598`). Observed by AC6.

### Live fixtures for unit 43 (M7)

- **S17** — id 18. Unit 43's AC1 and AC2 fixtures gain `source` fields on their `engine` rows,
  spelling gov's layout, so unit 48 S22's receipt rule still derives `tools/review-harness` and
  `tools/hooks` from them. Unit 43's ledger answers AC1 and AC2 in the AMENDED form, naming this item.
  Observed by AC7.

### The deploy descriptor's boundary (M8)

- **S18** — id 29. Every path token refused when malformed. `target_context`
  (`tools/govkit/govkit.py:1436-1497`) raises `Refusal` naming the key when a key of
  `PER_KIT_PATH_TOKENS` (`:1400`) is present under `[kit.<eid>]` and is not a non-empty string. It
  does the same for a non-string value under `[answers]` or `[kit.<eid>]`, which `:1487-1495` skip
  today, after which `memory_root` defaults to `memory`. `[kit.memory-recall] kit = 5` therefore
  refuses, where `:1479-1481` fall back to `{prefix}/{eid}` today. Observed by AC8.

### Criteria that read what they claim (L4, L6, L8, L10)

- **S19** — id 4. Unit 49 AC3 reads unit 46's ledger alone. Its observation is
  `git grep -n -F "ceil(1.5 * (R + S))" -- 'memory/builds/dFurnishedOrders/build/*TOOL-dFurnishedOrders-46*acceptance-ledger*'`,
  and the matched line is that ledger's AC4 row. Unit 49's ledger answers AC3 in the AMENDED form,
  naming this item. Observed by AC9.
- **S21** — id 11. A wrapped token still matches. Unit 49 AC3 and unit 48 AC10 read each ledger
  bullet with its continuation lines joined to its first line by single spaces, before matching.
  Each ledger row these two criteria read also carries its token on the bullet's first physical line,
  as `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` requires. Observed by AC11.
- **S24** — id 15. Unit 49 S1's pass commits by the driver's rule. The commits of units 45 and 46
  are those `read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1149`) attributes to each
  over the build range: a `Pass:` trailer naming the unit, or no trailer and a subject naming it. That
  is the rule `tools/memory-tree/deviation_join.py:50-55` calls the driver's pass rule. Paths come
  from `git show --name-only`. Unit 49's ledger answers AC1 in the AMENDED form, naming this item.
  Observed by AC13.
- **S26** — id 21. Unit 48's write set names the symbols render. Unit 48 mints `derive_rule_homes`
  and `check_selftest_guard_coverage`, so the pre-commit codebase-map leg
  (`.githooks/pre-commit:280-292`) requires `memory/map/generated/symbols.json` regenerated and staged
  with them. Unit 48's `dispatch` row in `memory/builds/dFurnishedOrders/RUN.md` names that file.
  Where it was recorded without it, unit 48's ledger names this item beside the amendment. This
  unit's own Files touched names it. Observed by AC15.

### One receipt needle (L7)

- **S22** — id 14. One helper, two callers. `check_receipt_reached(stdout)` in
  `tools/govkit/selftest.py` answers whether `apply` printed its receipt step. It matches `/RECEIPT]`
  as the re-apply arm already does (`:6769-6771`, and `:3533`). Unit 47's arm and the re-apply arm
  both call it. Observed by AC12.
- **S23** — id 30. No step index typed. No literal `[<digits>/RECEIPT]` remains in
  `tools/govkit/selftest.py`, so a step added to `STEPS` (`tools/govkit/govkit.py:94-102`) moves no
  arm. Unit 47's ledger answers its S1 and AC2 in the AMENDED form, naming this item. Observed by
  AC12.

## 3. Non-goals (OUT)

- The two HIGH findings of the same report: `TOOL-dFurnishedOrders-50` (id 17) and
  `TOOL-dFurnishedOrders-51` (id 24).
- Rewording the spec text of units 43 and 47 to 49. Where a landed criterion cannot hold as written,
  that unit's ledger answers it AMENDED, naming the item.
- The report's left-shift gates (the spec-lints, the checklist entries and the policy checks). No
  clause of this build names them.
- Writing the run-state file. S26 reads unit 48's `dispatch` row, which the main loop's `--dispatch`
  wrote.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-43` — AC1's and AC2's fixtures and the arm over them, which S17 gives `source` fields (id 18)
- **consumes-from** `TOOL-dFurnishedOrders-47` — S1's receipt needle, S2's problem count and S3's budget input `t`, which S1, S3, S8 to S11, S22 and S23 settle (ids 1, 28, 6, 13, 27, 19, 14, 30)
- **consumes-from** `TOOL-dFurnishedOrders-48` — AC1, AC5, AC10, AC12, S16, S22, S25 and its write set, which S1 to S7, S16 to S18, S21 and S26 settle (ids 1, 20, 28, 10, 2, 7, 23, 12, 18, 29, 11, 21)
- **consumes-from** `TOOL-dFurnishedOrders-49` — S1, S4 to S6, AC3 and AC4 and the roles row's note, which S12 to S15, S19 to S21, S24 and S25 settle (ids 8, 26, 22, 9, 4, 5, 11, 15, 16)
- **consumes-from** `TOOL-dFurnishedOrders-50` — the narrowed required set of `check_selftest_guard_coverage`, whose covered rule S16 moves onto `check_guard_trips` (id 12)
- **consumes-from** `TOOL-dFurnishedOrders-51` — the patched wait with its live read and cleanup, which S15 and S20 hold to a whole kill path and an early exit (ids 9, 5)
- **hands-off** `TOOL-dFurnishedOrders-53` — S16's covered rule over the required set, which unit 53 S1 makes one-way for a required directory (id 11 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-54` — S16's `--legs-for` route and AC6's scratch legs copy, whose trip answer unit 54 S1 and S2 move onto the `legs` argument (id 3 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-55` — S16's unevaluated glob row and AC6's glob case, whose source unit 55 S1 moves onto the `legs` rows (id 18 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-56` — AC6's slashless case, whose verdict alone unit 56 S1 and S3 replace with the covering row the arm returns (id 25 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-58` — S9, S13, S15 to S26, AC1, AC4 to AC6, AC8, AC9, AC11 to AC13, AC15 and §7, which unit 58 S5 to S21 settle (ids 33, 9, 8, 32, 6, 13, 7, 15, 34, 27, 20, 12, 24, 31, 10, 21, 17 of the seventh audit)
- **hands-off** `TOOL-dFurnishedOrders-60` — S13's `R` and `S`, S24's route, AC4 and AC13, which unit 60 S12, S17 and S22 settle (ids 5, 3 and 18 of the eighth audit)

## 4. Design

### Why one unit

The minors land on units 43 and 47 to 51. M4 admits two batch units only when the halves split into
two disjoint write sets by M6. The write sets would split, a govkit half (`tools/govkit/`) and a
budgets and roles half, but clause 2 fails. S1's `u` includes the `witness` and `apply` runs that S17
and S18's cases add to `tools/govkit/selftest.py`, so the budgets half would read the govkit half's
added cost as an acceptance input. One unit at order 29, after everything it lands on, sequences
that, and it is the shape M4 names first.

### apply's problems, after this unit

```
read_emit_problems(stdout):
    total := last line matching ^govkit: (\d+) problem\(s\)$     -> n (absent -> 0, no lines)
    probs := the n lines before it, each starting "govkit: "     (notes and declines print earlier)
    ids   := kit '<eid>' / entry '<eid>' in probs; other probs verbatim
check_receipt_reached(stdout) := "/RECEIPT]" in stdout          (one needle, both arms)
```

### The two budget rows, after this unit

```
govkit selftest          <at least ceil(1.5 * (1065 + t + u))>
    worst of 7 readings 1065s, + t (unit 47 apply) + u (units 48 and 52: <cmd> <s>s, ...), x1.5
roles adopter self-test  <max(60, ceil(1.5 * (R + S)))>
    worst of 5 readings 60s over every worktree's retained gate-run windows
    (C=$(git rev-parse --git-common-dir); grep -h ... "$C"/gate-run/*/*.leg "$C"/worktrees/*/gate-run/*/*.leg),
    plus S s of sleep, x1.5
```

### Inventory

Minted: `read_emit_problems` and `check_receipt_reached` in `tools/govkit/selftest.py`. The lexicon
answered OK for both on `py.function`. No flag, key or file.

### Migration

None: no arm here has run, and S18 refuses only shapes that crash or silently fall back today.

### Rollout

Live at landing, at order 29, after every unit it lands on. govkit's version moves for the kit epoch
leg where its shipped bytes move (S18). No path here is on the `watch:` line, so no re-stamp is owed.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/govkit/govkit.py`
- `tools/run-gates/selftest-budgets.txt`
- `tools/roles/adopt-roles.test.sh`
- `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Two batch units, a govkit half and a budgets half (§8 F1).** Clause 2 breaks on S1's `u`, as
  "Why one unit" states.
- **Price `u` from unit 48's stated costs alone (S3).** The report's id 28 alternative stands, but
  this unit runs after unit 48, so it can time the real commands. An estimate cannot match that, and
  it would leave this unit's own runs out.
- **Match `govkit: ` lines and subtract notes by text (S9).** Notes carry no fixed text. The total
  line is the one count `Report.emit` itself states.
- **Keep unit 48 S16's own covered rule (S16).** It reads a slashless directory row as uncovered and
  a glob as nothing, a second answer beside the runner's.

## 5. Production-readiness checklist

- security — S18 refuses malformed path tokens at the write boundary, never deriving a home from a
  value the operator mistyped.
- perf / scale — S20 takes about 15 s off every roles suite run. S1 prices about 40 s or more already
  added. S16 adds one `--legs-for` subprocess per run.
- error / empty / loading states — S13 refuses zero readings. S8 reads an absent total as no
  problems. S16 names unevaluated rows.
- observability — each re-priced note names its inputs and command. S15 names the kill step that did
  not run.
- risks — S16's subprocess makes the arm depend on `check-spec-tokens.py` running. A failure is a
  named RuntimeError (`check_policy.py:3903-3905`), never a pass.
- testing — AC1 to AC15 by probes and fixtures; the arms of §7 at the close.
- migration — none.
- user docs — none: self-test arms, budget rows and a refusal message.

## 6. Acceptance criteria

- **AC1** — When `grep -n "^govkit selftest" tools/run-gates/selftest-budgets.txt` runs, the row's
  budget is at least `ceil(1.5 * (1065 + t + u))`. Its note opens `worst of 7 readings 1065s` and
  names `t`, `u` and each command of `u` with its seconds.
  Red when: unit 48's added runs land in the leg with their cost unpriced.
  figure: 1065 and `t` = 20 are PINNED (unit 47 S3); `u` is DERIVED at the pass from the commands
  timed.
- **AC2** — When the pass clones the tip into a short path under `%TEMP%` and runs
  `bash skills/session-kickoff/manifest-check.sh` there, it prints no
  `watched files changed since last-audit` line. After one commit editing a watched path with no
  re-stamp and one adding a `last-audit:` line to a scratch spec, it prints that line, while
  `git log -1 --format=%H -G'^last-audit:'` over the same range names the decoy commit.
  Red when: an acceptance probe certifies a predicate C5 does not apply.
  fixture: a scratch clone under `%TEMP%`.
- **AC3** — When `python -c` imports the suite and passes `read_emit_problems` the captured stdout of
  unit 47 AC1's `apply --all`, its count equals the printed total. Its ids name no kit that appears
  only in a note. With one extra note line and one `[[decline]]` line inserted before the problems,
  the count and ids are unchanged. A leg-name problem and an id-less problem come back verbatim.
  Red when: a note or decline line is counted, or an id-less problem is dropped.
  figure: 41 `govkit: ` lines, 21 notes and 19 problems on 2026-10-27, PINNED from the report's id 6;
  the run's own figures are DERIVED.
- **AC4** — When S12's command runs from the repository root, from the directory
  `git rev-parse --git-common-dir` names, and from a worktree, it prints the same lines each time. The
  largest tab-separated fourth field is `R`, and the roles row is at least `max(60, ceil(1.5 * (R + S)))`.
  With both globs pointed at an empty scratch directory, the observation fails rather than taking
  `R` = 0.
  Red when: the note's command depends on the working directory, or an empty reading prices the row.
  figure: `R` was 59.737 on 2026-10-27 and is DERIVED again at observation.
- **AC5** — When the interrupt arm's probe runs with `run_tree_kill` wrapped to record its return,
  the record shows it returned normally, and the original `Popen.wait` was called on the `taskkill`
  child. With the wrapper raising inside the kill step instead, the arm fails naming the kill step.
  Red when: the arm grades a kill path its own patch truncated.
- **AC6** — When `check_selftest_guard_coverage` runs over a scratch legs copy whose
  `{prefix}/process-monitor/` row is spelled `{prefix}/process-monitor`, it reports no path under
  `tools/process-monitor/` as uncovered. With a glob row added under the prefix, one ending in `*.py`,
  it prints that row as unevaluated.
  Red when: the arm's covered rule disagrees with `check_guard_trips`.
  fixture: scratch copies of `tools/gate-legs.json`, passed as arguments.
- **AC7** — When unit 43's AC1 witness runs over its amended fixture, whose `engine` rows carry
  `source` fields, it exits 1 naming the adopter suite alone and its scan line counts
  `1 kit suite(s)`. `derive_receipt_homes` over the AC2 fixture lists `tools/hooks` for agent-cap.
  Red when: unit 48 S22's receipt rule empties a landed fixture's homes.
- **AC8** — When `witness <t> checklist` runs over a receipt target whose `deploy.toml` under
  `.governance` holds `[kit.memory-recall]` `kit = 5`, and again with `[answers]` `memory_root = 5`,
  each run exits 1 naming the key with no `Traceback`. `python tools/govkit/govkit.py apply --target <t>`
  over each exits 2 naming the key.
  Red when: a non-string path token or answer is accepted and a home derived in its place.
  fixture: two scratch targets under `%TEMP%`.
- **AC9** — When S19's scoped `git grep` runs on today's tree it prints nothing, because no unit 46
  ledger exists. After the close it prints one line, that ledger's AC4 row.
  Red when: the read is non-empty before the ledger it grades is written.
  cost: the second half is observed at the close, after the main loop writes the ledger.
- **AC10** — When the interrupt arm's probe runs with a stub that exits before writing its pid, it
  prints `DEAD PROBE: stub never started` within 2 s.
  Red when: a dead stub costs the standing arm its full 15 s.
- **AC11** — When `python -c` joins each `- ` bullet of a scratch ledger with its continuation lines
  and searches for `ceil(1.5 * (R + S))`, it finds a token wrapped across two physical lines. A line
  grep over the same file does not.
  Red when: a ledger that answers the criterion reads as unanswered.
  fixture: a scratch ledger under `%TEMP%`.
- **AC12** — When `git grep -n -E "\[[0-9]+/RECEIPT\]" -- tools/govkit/selftest.py` runs it prints
  nothing. `git grep -c "check_receipt_reached(" -- tools/govkit/selftest.py` prints at least 3: the
  definition and two callers. `check_receipt_reached` returns true on a stdout carrying
  `[12/RECEIPT]`.
  Red when: an arm types the step index or keeps a second needle.
- **AC13** — When a probe sources `tools/unattended/lib-unattended.sh` and runs
  `read_attribution_tokens` over a scratch repository whose commit has no trailer and the subject
  `build(x): TOOL-dFurnishedOrders-46 ...`, that commit's line carries the token
  `TOOL-dFurnishedOrders-46`.
  Red when: a trailerless pass commit drops out of a unit's write set.
  fixture: a scratch repository under `%TEMP%`.
- **AC14** — When `python -c` reads the `^roles adopter self-test` row of
  `tools/run-gates/selftest-budgets.txt`, its fourth tab-separated field matches
  `worst of (\d+) readings (\d+)s`.
  Red when: the re-priced row falls outside `--rank`'s grammar.
- **AC15** — When `grep -n -E "dispatch · item [0-9a-f]+ TOOL-dFurnishedOrders-(48|52) · "
  memory/builds/dFurnishedOrders/RUN.md` runs, each unit's row names
  `memory/map/generated/symbols.json`.
  Red when: a pass that stages a `.py` file records a write set without the render it regenerates.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `roles adopter self-test` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC6 AC7 AC8 AC12 · `read_emit_problems` over a note-and-decline stdout, the guard arm over a slashless and a glob row, unit 43's fixtures with `source` fields, two non-string deploy values and `check_receipt_reached` on a moved step index, each staged by restoring the replaced line after deleting `tools/govkit/__pycache__` and running Python with `-B` · none
New arm: tools/roles/adopt-roles.test.sh · covers AC5 AC10 · the interrupt arm's whole-kill record and its dead-stub early exit, staged by making the patched wait raise on every call after deleting `tools/roles/__pycache__` and running Python with `-B` · none

## 8. Open questions

- **F1 — How many units do the minors take?** Options: (a) one; (b) two, a govkit half and a
  budgets and roles half. (b) fails M6 clause 2 on S1's `u`, which reads the govkit half's added runs
  (§4 "Why one unit"). RESOLVED (agent,
  2026-10-27, delegated): (a), rung 1, BUILD-METHOD M4's one-unit rule. widens: none · relaxes: none
- **F2 — Where does `u` come from (S1, S3)?** Options: (a) timed at this pass on the commands unit 48
  adds; (b) pinned from unit 48 AC5's stated cost. This unit runs after unit 48, so (a) is available
  and measures what (b) estimates. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic's
  corrected fix of id 1 and the file's own rule (`tools/run-gates/selftest-budgets.txt:20-21`).
  widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F4 — The units this one lands on are unbuilt.** Units 43 and 47 to 51 are specced and unbuilt at
  `84ab3c6f`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on each at the pass
  and records any item a landed unit already closed, rung 1, the brief's rule. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit of the round-5 promotions' minors batched: 15
  MEDIUM and 11 LOW.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-53, TOOL-dFurnishedOrders-54, TOOL-dFurnishedOrders-55, TOOL-dFurnishedOrders-56, TOOL-dFurnishedOrders-58, promoted from the spec audit of the round-6 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md`); nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-60, promoted from the spec audit of the round-7 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended:

- `Report.emit` (`tools/govkit/govkit.py:1641-1649`) as the grammar S8 to S11 parse, and the
  re-apply arm's `/RECEIPT]` needle (`tools/govkit/selftest.py:6769-6771`) for S22 and S23.
- `read_legs_for`, `check_guard_trace` and `check_guard_trips` (`tools/policy/check_policy.py:3902`,
  `:4051`; `tools/memory-tree/design_lib.py:589`), and `read_guard_misses`
  (`tools/run-gates/measure_legs.py:3194`), for S16.
- C5 (`skills/session-kickoff/manifest-check.sh:1524-1535`) for S5 to S7.
- `read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1149`) for S24.
- `target_context` and `PER_KIT_PATH_TOKENS` (`tools/govkit/govkit.py:1400`, `:1436-1497`) for S18.
- The budgets file's calibration rule (`:20-21`) and `--rank`'s `CONDS`
  (`tools/run-gates/run-selftests.sh:430-435`) for S1 to S4, S12 to S14 and S25.

`python tools/codebase-map/reuse_lookup.py "count the problem lines a govkit report printed before
its total"` ranked `before`, `counts`, `report`, `Problem` and `check_line`, name-token neighbours
none of which parses `Report.emit`. The recall probe returned units 44 and 47, this report's M3,
TOOL-aDeferredBar-4 and two dRedressedBar specs, none disagreeing with source. Where this spec's
seams differ from units 47 to 49's own §10 (unit 47's "no arm tolerates an adopter exit", unit 48's
"no existing seam fits the guard arm", unit 49's "nothing beyond `git log`"), source holds the seams
named above, as the report's ids 14, 12 and 15 measured.

Recall terms used: `python tools/memory-recall/query.py "how does a selftest arm parse govkit problem
lines and price its leg budget" --terms "Report.emit problem total note govkit selftest budget row
re-price RECEIPT step needle wrapped ledger token"`

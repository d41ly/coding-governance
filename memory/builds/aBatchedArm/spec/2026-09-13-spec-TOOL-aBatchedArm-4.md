# TOOL-aBatchedArm-4 — declared execution modes for the self-test runner

**Status:** OPEN · rev-3 · 2026-09-13 · node a · Tier-2 · base c2db2f5d · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round1.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round2.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates/run-selftests.sh` grades 61 suites and has two execution shapes: a no-flag serial
loop that issues cost verdicts, and `--sweep`, which pools and withholds them. The owner ruled that
the mode is DECLARED — pooled available, serial possible when deliberately chosen — and that the row
checker stops redding a `--shard i/n` token. This unit does exactly those two things plus the
wiring that gives the pooled mode a consumer. **It does NOT change the pooled hang bound**; that is
`TOOL-aBatchedArm-5`, because the bound is the mechanism that killed 14 of 58 suites once and it
deserves its own spec rather than a paragraph in this one.

## 2. Scope (IN)

- **S1** — the row checker at `run-selftests.sh:357-361` admits a numeric-ratio token. The predicate
  is a REGEX, `^[0-9]+/[0-9]+$`, not a glob: a glob's `[0-9]*` is one digit then anything, so a
  digit-led directory name would skip the tracked-path check — staged and proven. Observed by
  **AC1**.
- **S2** — the executing mode is DECLARED: `--serial` and `--pooled` are the two spellings, the
  bare `run` invocation REFUSES naming both, and `--sweep` stays as an alias of `--pooled` so no
  recorded invocation breaks. `--check`, `--list` and `--rank` execute nothing and take no mode.
  The refusal sits AFTER the `--list` exit at `:374` and BEFORE the filter-liveness refusal at
  `:383`, pinned by line rather than by "after `--check`", because the width block before `:322`
  runs on every bar and a refusal there reds the merge bar. Observed by **AC2** and **AC3**.
- **S3** — the kit runner gets BOTH spellings and the risky one lands DARK. `run-unattended-gates.sh
  --selftests --serial` is today's behaviour byte-for-byte; `--selftests --pooled` exists and is not
  the default; bare `--selftests` REFUSES naming both, the same rule the runner applies one level
  down. The four tracked carriers that record the DoD command — `.githooks/gate-env.sh:27`,
  `tools/unattended/kit.toml:125-126`, `run-unattended-gates.sh:26-27` and `:203`, and
  `AGENTS.md:519` — say `--serial` in the same commit, so the verdict they name is the one that was
  measured. **The flip of that default to `--pooled` is `TOOL-aBatchedArm-5`'s act**, taken only once
  the bound is sound: the full-sweep TSV rows 51 to 57 show FIVE of the seven current unattended rows
  killed at rc=124 under exactly the bound `--pooled` would inherit today, so a flipped default would
  ship five TIMEOUTs on the DoD command. Under either spelling the kit runner's summary line names the
  mode and, under pooled, the withheld count parsed from the runner's own summary line. The FIVE arms
  of `run-selftests.test.sh` that invoke the bare mode declare `--serial`, and the strings they assert
  — `self-tests GREEN|RED`, `OVER BUDGET`, the unresolved-row `FAIL` line, the filter-liveness
  refusal — are emitted unchanged. Observed by **AC4** and **AC5**.
- **S4** — cost verdicts are issued ONLY under `--serial`; `--pooled` withholds and counts them
  exactly as `--sweep` does today at `:659-664`. Observed by **AC6**.
- **S5** — every printed remedy and the usage line name a DECLARED invocation. Today
  `run-selftests.sh`'s own remedies and `memory/guides/SESSION-KICKOFF.md:132` teach the bare form,
  which after S2 is the refused one. Observed by **AC7**.
- **S6** — the `tools/install-prefix-carried.txt` BAN on `run-selftests.sh` stays at exactly six.
  The usage line S5 rewrites is ALREADY one of the six counted literals, so the rewrite edits that
  occurrence in place and adds none: a raise here would red the leg `SLACK`, the ban firing in the
  other direction. rev-2 said "raise for the new literal" on a false premise. Observed by **AC8**.

## 3. Non-goals (OUT)

- **The pooled hang bound.** `--pooled` inherits `--sweep`'s bound unchanged: budget times
  `sweep-ceiling-factor`. That shape killed 14 of 58 suites in the full sweep of 2026-09-08 and three
  records rejected it as a predictor — `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` §3, and the
  sweep record's own remedy. Replacing it with `derive-ceilings.py`'s evidence shape (a per-row
  pooled reading carrying the runner's condition token, monotone, with `ceiling-margin.txt`'s
  `max(120 s, 1.0 × max)` headroom) is `TOOL-aBatchedArm-5`. rev-1 put a declared factor here and
  round 1 was right that it was the rejected design with a larger integer.
- **The eight shard rows, the arity raise, and their serial calibration pass.** `TOOL-aBatchedArm-3`,
  which now declares `consumes-from` this unit.
- **A contention model that makes a pooled cost verdict sound.** `TOOL-aPooledSweep-2` left that as
  an explicit edge; withholding is the honest verdict until one exists.
- **A per-row mode column.** Every reader stops at `f[3]`, a fifth column lands in `argv` and is
  `eval`'d, and the mode is a property of the run: the same row is graded serially and run pooled.
- **Teaching `--rank` to accept a `pooled@` reading.** Refused by `TOOL-aQuenchedHarness-6` S3a and
  armed at `run-selftests.test.sh:272-275`. Shard budgets stay serial readings.
- **Taking the turnstile.** `pooled@8x1` is byte-equal on an idle box and on one where another
  worktree's bar is running. Real, named, not built here.

### Edges

- **consumes-from** `none` — this is the prerequisite: nothing in it needs a shard row to exist.
- **hands-off** `TOOL-aBatchedArm-3` — the eight rows, the `SHARD_ARITY` raise, the one-off serial
  pass that produces their budgets, and the `selftest-budgets.txt` install-prefix raise.
- **hands-off** `TOOL-aBatchedArm-5` — the evidence-derived pooled hang bound.

## 4. Design

### Why the mode is per invocation and why bare `run` refuses

Two facts from the tree: the one caller that reports cost, `run-unattended-gates.sh:263`, invokes
the runner bare and reads only the exit code, so a silent pooled default prints GREEN with every
budget withheld; and five arms of the runner's held self-test assert serial-only strings on the bare
invocation. A silent default in EITHER direction is a coupling nobody declared. Bare `run` refuses,
every caller declares, and the refusal names both spellings.

### Why the kit runner's verdict path is pooled and its cost path is declared

The owner's ruling is pooled-primary: "pooled is available and serial stays possible when it is
deliberately declared". rev-1 inverted it for the one consumer, wiring `:263` to `--serial` and
leaving nothing in the tree issuing `--pooled` — so every criterion could go green with the build's
goal unmet on any invocation that existed, and the eight shard rows would have run one after another
paying seven extra prologues. The verdict path is the pooled one; the serial cost pass is its own
declared invocation, which is also the periodic serial sweep `TOOL-aQuenchedHarness-9` already calls
owed.

### Why a pooled cost verdict is withheld and not scaled

Contention dilation on this population is not a scalar: 1.5 to 1.85x for a bar leg
(`TOOL-aScannedThrottle-6`), 3 to 15x under the sweep (an 8 s suite killed at 121 s), 5.5x median
across concurrent bars. Three "8-wide" conditions, fifteen-fold apart, one token. A number that cannot
be predicted from the declared condition is a number a verdict must not rest on.

### What the cost model says about the goal

The gate self-test is fork-bound on a SERIALISED spawn path — roughly 53,000 forks at roughly 190 ms —
and "a pool contends on precisely the resource the work is made of". The nine-suite A/B reached 1.72x
at width 8, not 8x; the three-suite A/B was a loss. Eight shards 8-wide share that path. Whether
they reach 20 minutes is `TOOL-aBatchedArm-3` AC4's measurement, made runnable by this unit's S3, and
designed so it can FAIL and be read. On a node without the on-access scanner (19 to 39 ms per spawn
against 251 here) the same split is trivially inside the target. The target may be a property of
the host.

### Rollout

S1 alone first. S2, S3, S5 in one commit — the refusal, the callers that satisfy it, and the strings
that teach it cannot be split across a bar. S6 in that same commit, since the usage line is the new
literal. S4 is already the tree's behaviour under `--sweep` and lands as the alias.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh`, `tools/run-gates/run-selftests.test.sh`,
`tools/unattended/run-unattended-gates.sh`, `memory/guides/SESSION-KICKOFF.md` (the `:132` line,
and the runner joins its `watch:` list so the manifest ratchet sees the next edit, with `last-audit`
re-stamped in the S5 commit), `.githooks/gate-env.sh`, `tools/unattended/kit.toml`, `AGENTS.md`
(the four DoD carriers), and this build's records. `tools/install-prefix-carried.txt` is READ by
AC8 and not edited.

## 5. Production-readiness checklist

- security — N/A. Scheduling and verdict wording; no suite's subject changes.
- perf / scale — this unit makes the pooled path REACHABLE; unit 3 makes it fast and unit 5 makes
  it safe. On its own it changes no suite's wall clock.
- error / empty / loading states — bare `run` refuses naming both modes; an unknown mode token
  refuses as today; the filter-liveness refusal at `:383` is unchanged and sits after the mode
  refusal, so a wrong filter under a declared mode still reds by name.
- observability — a pooled run prints the width pair and the withheld count on its summary line, and
  the kit runner repeats both, so neither GREEN can be read as a cost claim.
- risks — the pooled mode has killed a quarter of its population once, and this unit inherits that
  bound unchanged. Stated in §3 rather than hidden; unit 5 is the guard.
- testing — the runner's self-test gains one arm per refusal, one per mode, and one for the regex in
  each direction, each staged and observed RED first.
- migration — `--sweep` aliases `--pooled`; the five bare-mode arms, the one bare caller and the four
  DoD carriers declare `--serial` in the same commit, so every recorded verdict is the one that was
  measured; the pooled default is landed dark and flipped by unit 5.
- user docs — the usage line and `SESSION-KICKOFF.md:132` teach the declared forms.

## 6. Acceptance criteria

- **AC1** — When a budget row's argv carries `--shard 1/8`, `run-selftests.sh --check` passes; when
  it carries an untracked path whose first component begins with a digit, `--check` still REDS
  naming it.
  Red when: either direction fails, which is the glob-versus-regex difference staged in round 1.
- **AC2** — When `run-selftests.sh` is invoked with no mode flag and no non-executing verb, it exits
  2 naming `--serial` and `--pooled` and executes no suite.
  Red when: it runs serially, which is the silent default the ruling removes.
- **AC3** — When `run-selftests.sh --check` runs on a tree whose rows are valid, it exits 0; and
  when it is given an unknown `--kit` filter under a declared mode, the filter-liveness refusal at
  `:383` still fires by name.
  Red when: the mode refusal reaches the `--check` path, or it shadows the liveness refusal.
- **AC4** — When `run-unattended-gates.sh --selftests --serial` runs, its summary line names
  `serial`, carries an `OVER BUDGET` line for any breach, and is byte-identical to today's bare
  invocation's; when `--selftests --pooled` runs, the summary names `pooled` and a withheld count of
  exactly 7, parsed from the runner's own `cost verdict(s) WITHHELD` line on stdout; when bare
  `--selftests` runs, it exits 2 naming both spellings and executes nothing.
  `fixture:` the seven tracked unattended rows at `selftest-budgets.txt:110-116`; no new fixture.
  `cost:` one serial pass of those rows, roughly 12657 s of readings, plus one pooled pass.
  Red when: any of the three prints the other mode's summary, the pooled count is not 7, or bare
  `--selftests` runs a suite.
- **AC5** — When the five bare-mode arms of `run-selftests.test.sh` run with `--serial` added, each
  passes asserting its existing string unchanged.
  Red when: any asserted string changes, or an arm is left invoking the refused bare form.
- **AC6** — When a suite runs under `--pooled`, its cost verdict is WITHHELD and counted; under
  `--serial` the same suite gets an `OVER BUDGET` line when it breaches.
  Red when: a pooled run prints `OVER BUDGET`, which is a verdict resting on an unpredictable number.
- **AC7** — When each of the five sites that teach an invocation is EXERCISED — the usage line via
  `run-selftests.sh --help`, the three printed remedies via the refusals that print them (they
  interpolate `$SELF`, so a grep cannot see them), and `memory/guides/SESSION-KICKOFF.md:132` read as
  text — every emitted or written command names `--serial` or `--pooled`.
  Red when: any emitted remedy or the manifest line names the bare form, which rev-2's grep could not
  have caught for four of the five.
- **AC8** — When this unit's commit is staged, `bash tools/check-install-prefix.sh` is green with the
  `run-selftests.sh` count UNCHANGED at six.
  Red when: the leg reds `ROSE` or `SLACK` — the first is a literal added, the second is the count
  raised for a literal that already existed, and rev-2 would have caused the second.

## 7. Gates

`memory hygiene` · `install-prefix (shipped surface)` · `run-selftests self-test` · `run-gates canary`
· `every held leg is budgeted, every budget row resolves` · `kickoff-manifest ratchet` · `run-gates gov canary`

Derived from `tools/gate-legs.json` against Files touched, as round 2 M1 asked: the three added are
the `--check` leg S1 rewrites (unguarded, on every bar), the manifest ratchet whose manifest S5
edits, and the gov canary guarded on `tools/run-gates/`. `unattended skill wiring` is dropped; it
reads none of the five touched files.

New arm: `tools/run-gates/run-selftests.test.sh` · the bare-`run` refusal, the regex admitting a ratio
and refusing a digit-led path, and the pooled-withholds-serial-grades pair, each staged and observed
RED then unstaged · floor to move: the suite's own, up by the arms added.

## 8. Open questions

- **F1 · Should bare `run` refuse, or default to `--serial` with a printed notice?** Refuse. A printed
  notice on a caller that reads only the exit code is a notice nobody reads. RESOLVED (agent,
  2026-09-13, delegated): refuse; the one caller and five arms are edited in the same commit.
- **F2 · Where does the refusal sit?** Between `:374` and `:383`, so `--list` still exits before it
  and the filter-liveness refusal still fires after it. RESOLVED (agent, 2026-09-13, delegated):
  pinned by line in S2, because "after `--check`" left it anywhere in a 30-line span and round 1 H3
  showed the fifth arm's verdict depends on which side of `:383` it lands.

## 9. Revision log

- rev-3 · 2026-09-13 · §2 S3 · §2 S6 · §4 Files · §5 migration · §7 · AC4 · AC7 · AC8 · folded
  spec-audit round 2 (BLOCKED, 3 blockers, CONVERGING from 8, precision 0.57). The blocker: rev-2
  flipped the DoD command's default to `--pooled` at the inherited budget x2 bound, and the sweep TSV
  rows 51 to 57 show five of the seven unattended rows killed under exactly that bound — verified in
  the tree. Both spellings now; the default stays `--serial` and is flipped by the unit that owns the
  bound; the four DoD carriers are named and edited. S6 rested on a false premise: the usage line is
  already a counted literal, so the count stays at six and AC8 names `SLACK`. AC7 now exercises the
  five sites rather than grepping them, since three remedies interpolate `$SELF`. §7 derived from the
  manifest, three legs added and one dropped. AC4 given its cross-process mechanism and pinned count.
- rev-2 · 2026-09-13 · §1 · §2 S3 · §2 S5 · §2 S6 · §3 · Edges · §4 · AC4 · AC5 · AC7 · AC8 · F2 ·
  folded spec-audit round 1 (BLOCKED, 8 blockers, 12 defects, precision 0.57). Three things it was
  right about and this rev takes: rev-1's S3 wired the only consumer to `--serial` and left NOTHING
  issuing `--pooled`, so the goal was unreachable on any invocation in the tree — the kit runner now
  carries the pooled verdict path and a declared serial cost path; rev-1's S5 factor was the shape
  `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` §3 and the sweep record all rejected, and
  `derive-ceilings.py` already owns the evidence shape — the bound is now `TOOL-aBatchedArm-5` and
  this unit inherits `--sweep`'s unchanged; and the edges were wrong in both direction and mutuality
  — this unit is the prerequisite with two `hands-off` and no `consumes-from`, and unit 3's mirror is
  written. Five bare-mode arms, not four; the refusal pinned by line.
- rev-1 · 2026-09-13 · initial draft, from a five-lens research fan with skeptics.

## 10. Reuse audit

- **The seam is the runner's existing mode machinery**, verified at source: `MODE` at
  `run-selftests.sh:104`, the `--sweep` branch at `:297`, the withheld counter at `:659-664`, the
  refusal shape `SELFTEST_OUTER_WIDTH` already uses at `:301-315`. Nothing is invented: two spellings
  for one existing branch, one refusal in the existing shape, one regex for one glob. The `--rank`
  refusal of `pooled@` at `:134` and `:172` is REUSED as-is. The reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "declare a self-test runner's execution mode per invocation and withhold cost verdicts under a pool"`
  — and returned `build_self_chain` and `scan_verdicts` from the process-monitor kit, neither of
  which is this seam; it reports `unscanned layers: .sh`, so it cannot see the runner and its result
  is not evidence either way. The seam was found by reading the file. **Disposition of every record
  §10 cites**, since round 1's left-shift asked for one: `TOOL-aPooledSweep-1` through `-7` REUSED
  (the mode machinery and the withholding); `TOOL-aPooledSweep-2` §3 REFUSED-BY (the factor, now
  unit 5's problem to answer); `TOOL-dRetiredFork-40` REFUSED-BY (same); `TOOL-aReapedSpinner-23`
  NOT-THIS-SEAM (nested pools, withdrawn); `TOOL-aQuenchedHarness-6` S3a REUSED (the `--rank`
  refusal).
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.

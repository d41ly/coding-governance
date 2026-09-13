# TOOL-aBatchedArm-4 — declared execution modes for the self-test runner

**Status:** OPEN · rev-4 · 2026-09-13 · node a · Tier-2 · base c2db2f5d · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-prompt-TOOL-aBatchedArm-4-build-brief.md](../prompts/2026-09-13-prompt-TOOL-aBatchedArm-4-build-brief.md) | journal | — |
| [2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round1.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round2.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-4-spec-audit-round3.md) | spec-audit | — |

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
- **S2** — the RUNNER's executing mode is DECLARED: `--serial` and `--pooled` are the two spellings,
  the bare `run` invocation REFUSES naming both, and `--sweep` stays as an alias of `--pooled` so no
  recorded invocation breaks. `--check`, `--list` and `--rank` execute nothing and take no mode.
  The refusal sits AFTER the `--list` exit at `:374` and BEFORE the filter-liveness refusal at
  `:383`, pinned by line, because the width block before `:322` runs on every bar through the
  unguarded `--check` leg and a refusal there reds the merge bar. Observed by **AC2** and **AC3**.
- **S3** — the KIT RUNNER's grammar, stated once because three routes reach its self-test half and
  rev-3 covered one. `run-unattended-gates.sh` takes a VERB and a MODE as two positionals in either
  order, parsed at `:121-161`. The verb is `--selftests`, `--checks` or `--all`, and the no-argument
  default to `--selftests` is KEPT. The mode is `--serial` or `--pooled`. **Every route that reaches
  the self-test half — bare, `--selftests`, `--all` — REFUSES at `:121-161` when no mode is given,
  naming both spellings; `--checks` reaches no self-test and takes no mode.** `--serial` runs the
  self-test half exactly as today; `--pooled` runs it through the runner's pool and exists so unit 3
  can measure it; **neither is the default, and the flip to `--pooled` is `TOOL-aBatchedArm-5`'s
  act** once the bound is sound — the full-sweep TSV rows 51 to 57 show FIVE of the seven current
  unattended rows killed at rc=124 under exactly the bound `--pooled` inherits today. Observed by
  **AC4**.
- **S4** — the kit runner's summary line gains exactly ONE mode token under both spellings, in the
  shape `unattended gates GREEN — <n> ran on demand · serial` (or `· pooled, <k> cost verdicts
  withheld`), with `<k>` parsed from the runner's own `cost verdict(s) WITHHELD` line on stdout.
  Everything else the kit runner prints, and its exit code, is byte-identical to today under
  `--serial`. Observed by **AC4**.
- **S5** — cost verdicts are issued ONLY under `--serial`; `--pooled` withholds and counts them
  exactly as `--sweep` does today at `:659-664`. Observed by **AC5**.
- **S6** — every carrier that records or teaches an invocation of either runner spells a declared
  mode, all in the same commit as S2 and S3. The RUNNER's sites: its usage line at `:77-78` and
  `:93-94`, the three printed remedies at `:412`, `:746` and `:758`, and
  `memory/guides/SESSION-KICKOFF.md:132`. The KIT RUNNER's sites: its own `--help` at `:127-130`
  (drop `(default)`, list both modes, keep the literal on its line), `:26-27` and `:203`,
  `.githooks/gate-env.sh:27`, `tools/unattended/kit.toml:125-126` (both lines), `AGENTS.md:519`,
  `tools/unattended/README.md:66`, and `SESSION-KICKOFF.md:168-169`. The runner joins
  `SESSION-KICKOFF.md`'s `watch:` list and `last-audit` is re-stamped in this commit. Observed by
  **AC6** and **AC7**.
- **S7** — the `AGENTS.md:519` edit is budgeted: the file sits 18 bytes under the unguarded
  charter-size cap, and appending ` --serial` costs 9, so the edit is the appended flag and nothing
  else. Measured at staging by the leg, not asserted. Observed by **AC8**.
- **S8** — the `tools/install-prefix-carried.txt` BAN on `run-selftests.sh` stays at exactly six and
  the one on `run-unattended-gates.sh` stays at its count: every usage line S6 rewrites is ALREADY a
  counted literal, so each rewrite edits its occurrence in place and adds none. A raise would red
  `SLACK`. Observed by **AC9**.

## 3. Non-goals (OUT)

- **The pooled hang bound.** `--pooled` inherits `--sweep`'s bound unchanged: budget times
  `sweep-ceiling-factor`. That shape killed 14 of 58 suites in the full sweep of 2026-09-08 and three
  records rejected it as a predictor — `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` §3, and the
  sweep record's own remedy. Replacing it with `derive-ceilings.py`'s evidence shape and re-pointing
  the carriers to `--pooled` is `TOOL-aBatchedArm-5`.
- **The eight shard rows, the arity raise, and their serial calibration pass.** `TOOL-aBatchedArm-3`,
  which declares `consumes-from` this unit.
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
- **hands-off** `TOOL-aBatchedArm-5` — the evidence-derived pooled hang bound, and re-pointing the
  carriers from `--serial` to `--pooled` once it holds.

## 4. Design

### Why the mode is declared at both runners and why every bare form refuses

The runner: the one caller that reports cost invoked it bare and read only the exit code, so a
silent pooled default would print GREEN with every budget withheld; five arms of its held self-test
assert serial-only strings on the bare invocation. The kit runner: three routes reach its self-test
half (bare defaults to `--selftests` at `:121`; `--all` at `:123`; `--selftests` at `:125`), and
`TOOL-aQuenchedHarness-4` AC6 records `--all` as a compensating check — a rule covering one route
would let `--all` print RED with "12 ran" for seven suites that never ran. A silent default in EITHER
direction, at EITHER runner, is a coupling nobody declared. Every bare form refuses naming both
spellings; every carrier declares.

### Why `--serial` stays the recorded verdict and `--pooled` is landed dark

The DoD verdict path is `--serial`, by declaration at every carrier, and it is byte-identical to
today except for the one appended mode token. `--pooled` is a declared invocation that exists, is
exercised by AC4 here and by `TOOL-aBatchedArm-3` AC4's measurement, and is named by NO carrier until
`TOOL-aBatchedArm-5` re-points them. Said plainly: after this unit, nothing in the tree issues
`--pooled` by a recorded DoD command, and that is deliberate — the bound it would run under has
killed a quarter of its population once, and §1's own rule is that risky behaviour lands dark and
is flipped on after in-place verification. rev-2 flipped it on; round 2 verified the five kills.

### Why a pooled cost verdict is withheld and not scaled

Contention dilation on this population is not a scalar: 1.5 to 1.85x for a bar leg
(`TOOL-aScannedThrottle-6`), 3 to 15x under the sweep (an 8 s suite killed at 121 s), 5.5x median
across concurrent bars. Three "8-wide" conditions, fifteen-fold apart, one token. A number that cannot
be predicted from the declared condition is a number a verdict must not rest on.

### What the cost model says about the goal

The gate self-test is fork-bound on a SERIALISED spawn path — roughly 53,000 forks per run — and "a
pool contends on precisely the resource the work is made of". Per spawn on node `a`: 251 ms,
recorded in `TOOL-aGradedDoorway-10`; on node `d`, with the scanner present, 19 to 39 ms. The
nine-suite A/B reached 1.72x at width 8, not 8x; the three-suite A/B was a loss. Eight shards 8-wide
share that path. Whether they reach 20 minutes is `TOOL-aBatchedArm-3` AC4's measurement, made
runnable by this unit's `--pooled`, and designed so it can FAIL and be read. The target may be a
property of the host.

### Rollout

S1 alone first. S2 through S8 in ONE commit — the refusals, every caller and carrier that satisfies
them, the summary shape, the byte budget and the literal counts cannot be split across a bar without
one of them redding it.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` ·
`tools/unattended/run-unattended-gates.sh` · `tools/unattended/README.md` ·
`tools/unattended/kit.toml` · `.githooks/gate-env.sh` · `AGENTS.md` ·
`memory/guides/SESSION-KICKOFF.md` · this build's records. Nine files.
`tools/install-prefix-carried.txt` is READ by AC9 and not edited.

## 5. Production-readiness checklist

- security — N/A. Scheduling and verdict wording; no suite's subject changes.
- perf / scale — this unit makes the pooled path REACHABLE; unit 3 makes it fast and unit 5 makes
  it safe. On its own it changes no suite's wall clock.
- error / empty / loading states — every bare form at both runners refuses naming both modes; an
  unknown token refuses as today; the runner's filter-liveness refusal at `:383` still fires after
  the mode refusal, so a wrong filter under a declared mode still reds by name.
- observability — one mode token on the kit runner's summary under both spellings, and under pooled
  the withheld count beside it, so neither GREEN can be read as a cost claim.
- risks — the pooled mode has killed a quarter of its population once, and this unit inherits that
  bound unchanged behind a declared, non-default invocation. Unit 5 is the guard.
- testing — the runner's self-test gains one arm per refusal, one per mode, and one for the regex in
  each direction; the kit runner's self-test gains one arm per route-without-mode refusal; each
  staged and observed RED first.
- migration — `--sweep` aliases `--pooled`; the five bare-mode arms, every caller and every carrier
  declare `--serial` in the same commit; the pooled default is landed dark and flipped by unit 5.
- user docs — both `--help` texts and the three manifest and README lines teach the declared forms.

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
- **AC4** — When `run-unattended-gates.sh` runs in each of these forms:
  bare, `--selftests`, `--all` — each exits 2 naming both modes and executes no suite;
  `--serial` and `--selftests --serial` — the output is byte-identical to today's bare run except
  for the appended ` · serial` on the summary line, and the exit code is unchanged;
  `--pooled` — the summary carries ` · pooled, <k> cost verdicts withheld` where `<k>` equals the row
  count `run-selftests.sh --kit tools/unattended --list` prints at observation time, the `_uc` the
  kit runner derives at `:258`; and the runner's `peak concurrency P of outer O` line shows O equal to
  the lesser of the resolved width and that row count, with P at least 2;
  `--checks` — runs with no mode and no refusal.
  `figure:` `<k>` DERIVED at observation, never pinned.
  `fixture:` the seven tracked unattended rows at `selftest-budgets.txt:110-116`; on a host whose
  resolved width is 1 the pooled arm cannot pass and SKIPS naming itself and why.
  `cost:` one serial pass, roughly 12657 s of readings; one pooled pass bounded at the largest row
  budget times the factor, 27200 s at HEAD.
  Red when: any refusing form runs a suite, the serial output differs beyond the token, `<k>` is not
  the derived count, or O or P is 1 on a host whose width is not.
- **AC5** — When a suite runs under `--pooled`, its cost verdict is WITHHELD and counted; under
  `--serial` the same suite gets an `OVER BUDGET` line when it breaches.
  Red when: a pooled run prints `OVER BUDGET`, which is a verdict resting on an unpredictable number.
- **AC6** — When each site that teaches an invocation is EXERCISED — the runner's usage via
  `run-selftests.sh --help`, its remedy at `:412` via `SELFTEST_TIMEOUT_BIN=nonexistent --pooled`,
  its remedy at `:746` via any completed `--pooled` run over the test fixture, its remedy at `:758`
  via a RED one, the kit runner's usage via `run-unattended-gates.sh --help`, and
  `SESSION-KICKOFF.md:132` and `:168-169`, `tools/unattended/README.md:66` read as text — every
  emitted or written command names `--serial` or `--pooled`, and NONE spells the bare form or
  `(default)`.
  Red when: any emitted remedy or written line names the bare form, which a grep could not have
  caught for the three remedies that interpolate the runner's own path.
- **AC7** — When the carrier lines `.githooks/gate-env.sh:27`, `tools/unattended/kit.toml:125` and
  `:126`, `run-unattended-gates.sh:26-27` and `:203`, and `AGENTS.md:519` are read as text after the
  S6 commit, each names `--serial` beside `run-unattended-gates.sh`.
  Red when: any spells the bare form, which is the recorded DoD command pointing at a refusal.
- **AC8** — When the S7 commit is staged, the `charter size` leg is green with `AGENTS.md` inside its
  cap.
  Red when: the leg reds, which is 9 bytes spent against 18 of headroom by an edit that added more
  than the flag.
- **AC9** — When the S2 through S8 commit is staged, `bash tools/check-install-prefix.sh` is green
  with the `run-selftests.sh` count UNCHANGED at six and the `run-unattended-gates.sh` count
  unchanged.
  Red when: the leg reds `ROSE` or `SLACK` — the first is a literal added, the second is a count
  raised for a literal that already existed.

## 7. Gates

`memory hygiene` · `install-prefix (shipped surface)` · `run-selftests self-test` · `run-gates canary`
· `run-gates gov canary` · `every held leg is budgeted, every budget row resolves` · `kickoff-manifest ratchet`
· `charter size` · `lexicon naming predicates` · `unattended skill wiring`

Derived over the nine files in Files touched by this rule: every leg whose `guard` covers a touched
path or whose `argv` names one, plus the unguarded legs that read a touched file. `charter size`
reads `AGENTS.md`; `lexicon naming predicates` grades every touched `.sh`; the manifest ratchet's
manifest is `SESSION-KICKOFF.md`; `unattended skill wiring` reads `kit.toml` and `run-unattended-gates.sh`.
The three `.githooks/`-guarded self-tests run on the kit-work bar and are not listed one by one.

New arm: `tools/run-gates/run-selftests.test.sh` · the bare-`run` refusal, the regex admitting a ratio
and refusing a digit-led path, the pooled-withholds-serial-grades pair, and the `:412` remedy naming a
mode · `tools/unattended/run-unattended-gates.test.sh` · one refusal per route reaching the self-test
half without a mode · each staged and observed RED then unstaged · floor to move: each suite's own,
up by the arms added.

## 8. Open questions

- **F1 · Should bare `run` refuse, or default to `--serial` with a printed notice?** Refuse. A printed
  notice on a caller that reads only the exit code is a notice nobody reads. RESOLVED (agent,
  2026-09-13, delegated): refuse at both runners; every caller and carrier is edited in one commit.
- **F2 · Where does the runner's refusal sit?** Between `:374` and `:383`. RESOLVED (agent,
  2026-09-13, delegated): pinned by line in S2, because "after `--check`" left it anywhere in a
  30-line span and the fifth arm's verdict depends on which side of `:383` it lands.
- **F3 · Keep or drop the kit runner's no-argument default to `--selftests`?** Keep. RESOLVED
  (agent, 2026-09-13, delegated): it is the smaller diff, the carriers then read ` --serial` alone,
  and that is what fits `AGENTS.md`'s 18-byte headroom; the refusal is on the MODE, not the verb.

## 9. Revision log

- rev-4 · 2026-09-13 · §2 S3 through S8 · §3 · Edges · §4 · §5 · §6 AC4 through AC9 · §7 · F3 ·
  folded spec-audit round 3 (BLOCKED, 4 blocker rows in one defect, NON-CONVERGENT by rows against
  round 2's 3, disposition FOLD — this spec is not re-reviewed). The defect: rev-3's S3 stated the
  kit runner's mode rule for `--selftests` only, while the tree reaches the self-test half by the
  bare form (`:121` default) and by `--all` (`:123`) too, three carriers spell those routes, and the
  parser takes one positional; built as written, `--all` would print RED for seven suites that never
  ran with every criterion green. S3 now states the grammar once — verb and mode as two positionals,
  every route to the self-test half refuses without a mode — and F3 keeps the no-argument default.
  Also folded: AC4's serial clause was unsatisfiable (a mode token AND byte-identity), now scoped to
  "identical except the token"; the carriers were observed by nothing, now AC7; three more sites
  teach the bare form (the kit runner's own `--help`, `README.md:66`, `SESSION-KICKOFF.md:168-169`),
  now in S6 and AC6; `AGENTS.md` had 18 bytes of headroom, now S7 and AC8; §4 still argued rev-2's
  pooled-primary design and §5 still hardcoded `:263`, both rewritten; §7 re-derived over nine
  files with the rule stated; AC4's pooled arm was green on a width-1 pool, now asserts the runner's
  peak line and skips by name where it cannot; AC4 typed 7 for a derived count, now derived; AC7's
  mechanism named by line and trigger with the negative clause restored; the scanner cite folded.
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
  refusal shape `SELFTEST_OUTER_WIDTH` already uses at `:301-315`; and at the kit runner, the
  verb parser at `run-unattended-gates.sh:121-161` and the `_uc` derivation at `:258`. Nothing is
  invented: two spellings for one existing branch, one refusal in the existing shape at each runner,
  one regex for one glob. The `--rank` refusal of `pooled@` at `:134` and `:172` is REUSED as-is. The
  reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "declare a self-test runner's execution mode per invocation and withhold cost verdicts under a pool"`
  — and returned `build_self_chain` and `scan_verdicts` from the process-monitor kit, neither of
  which is this seam; it reports `unscanned layers: .sh`, so it cannot see either runner and its
  result is not evidence either way. The seams were found by reading the files. **Disposition of
  every record §10 cites**: `TOOL-aPooledSweep-1` through `-7` REUSED (the mode machinery and the
  withholding); `TOOL-aPooledSweep-2` §3 REFUSED-BY (the factor, now unit 5's to answer);
  `TOOL-dRetiredFork-40` REFUSED-BY (same); `TOOL-aReapedSpinner-23` NOT-THIS-SEAM (nested pools,
  withdrawn); `TOOL-aQuenchedHarness-6` S3a REUSED (the `--rank` refusal); `TOOL-aQuenchedHarness-4`
  AC6 REUSED (the `--all` compensating check, which is why `--all` is a route S3 covers);
  `TOOL-aGradedDoorway-10` REUSED (the per-spawn figures in §4).
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.

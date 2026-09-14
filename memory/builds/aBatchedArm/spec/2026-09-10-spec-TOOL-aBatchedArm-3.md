# TOOL-aBatchedArm-3 — grade the gate self-test as eight declared shards

**Status:** CLOSED · rev-8 · 2026-09-14 · node a · Tier-2 · base 0422ea2e · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-aBatchedArm-3-build-brief.md](../prompts/2026-09-13-prompt-TOOL-aBatchedArm-3-build-brief.md) | journal | — |
| [2026-09-14-prompt-TOOL-aBatchedArm-5-closing-fix-brief.md](../prompts/2026-09-14-prompt-TOOL-aBatchedArm-5-closing-fix-brief.md) | journal | TOOL-aBatchedArm-5 TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 |
| [2026-09-10-review-TOOL-aBatchedArm-3-spec-audit-round1.md](../reviews/2026-09-10-review-TOOL-aBatchedArm-3-spec-audit-round1.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round2.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round3.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round4.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round4.md) | spec-audit | — |
| [2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round5.md](../reviews/2026-09-13-review-TOOL-aBatchedArm-3-spec-audit-round5.md) | spec-audit | — |
| [2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md) | diff-review | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-4 TOOL-aBatchedArm-5 |

<!-- /gen:spec-records -->

## 1. Goal

`unattended gate selftest` is the costliest row in the declared self-test population. Split its
293 invocations across eight declared rows the runner's `--pooled` mode executes concurrently, and
MEASURE what that buys on this host against a two-shard reading taken on the same clone at BASE — because
`TOOL-aPacedTurnstile-8` measured the crossover at two, and `TOOL-aScannedThrottle-6` measured the
pool's dilation. **This unit lowers ONE row.** The kit's pooled wall stays floored at the driver
suite's row until that suite is declared sharded, which `aPacedTurnstile-8` records as "both must
move together" and which is a separate unit.

Every line anchor below is against the tree at the base this header names, cited by text beside the
number so a moved line is a moved anchor rather than a wrong one.

## 2. Scope (IN)

- **S1** — raise `SHARD_ARITY` from 2 to 8 in `tools/unattended/check-unattended.test.sh` and re-cut
  the regions. **Cuts fall ONLY at `reset_tree`-led block edges**, as `TOOL-aShardedFloor-3` §4
  requires. Invocation count is the first guess; the cut is re-balanced against the per-shard SERIAL
  readings S2 takes, iterating until `max(shard)` is within a declared tolerance of `sum / 8`, and
  every candidate's timing is recorded beside the one chosen. **Every helper defined inside a region
  and called past a cut is hoisted to the prologue** beside `anchor_break`; the population is
  DERIVED at build time as every `name() {` definition between the first `in_shard` line and the
  floor line, and the count is written into the HOIST SET note from that derivation — this spec
  types no figure for it. Observed by **AC1**, **AC2** and **AC10**.
- **S2** — replace the single unsharded row in `tools/run-gates/selftest-budgets.txt` with eight
  rows, one per shard, each carrying a SERIAL reading from one `--serial` pass. The rows' argv
  literals raise the file's count in `tools/install-prefix-carried.txt`, a BAN the ratchet cannot
  raise, so the count is raised by hand with a fourth-column reason in the same commit. Observed by
  **AC3** and **AC7**.
- **S3** — declare eight per-shard floors and re-measure `FLOOR_ASSERTIONS`, each within the ~3 %
  headroom the file's own floor block argues for, both figures beside each constant. **The figure
  every floor and AC1 read is the FLOOR-GRADED count** — `$n` at the text `[ "$n" -ge "$FLOOR" ]` —
  and `PROLOGUE_ARMS` is DERIVED as that count's prologue share, which is 0 at this base: the C21
  pair at the text `c21_fixture=$(mktemp -d)` runs AFTER the floor grade and is an EPILOGUE constant
  only the PASS line carries. The comment at the text `PROLOGUE_ARMS is 0` is therefore TRUE and
  stands; rev-3 said to correct it and was wrong. Observed by **AC2** and **AC11**.
- **S4** — PORT the gov canary's shard-join predicate (`run-gates.gov.test.sh`, the text `shard
  contract`) to the budget file's row format as ONE join function, scoped to scripts a budget row
  calls WITH `--shard`. Retarget BOTH whole-suite notes at it in the same commit: the kit runner's
  help text at `run-unattended-gates.sh` (the text `run UNSHARDED on purpose`) and the suite's own
  note at the text `WHAT A GREEN SHARD LEG IS EVIDENCE ABOUT`. Observed by **AC5**.
- **S5** — the replay rule compares TOPOLOGY, not verdicts and not shas. `TOOL-aShardedFloor-3`
  AC2 rejected verdict vectors for the right reason and then compared sha-bearing listings, which
  differ between any two processes and which its own build never discharged — so that oracle is
  REFUSED here after round 5 measured it, and what survives of it is the STATE-not-verdict rule and
  the named negative. The capture at each boundary is the set of ref NAMES on the fixture origin
  and locally, plus the ANCESTRY relations among them that any later arm depends on — today the one
  the `SH_I = 2` replay establishes, `unit` an ancestor of `main` — expressed as
  `git merge-base --is-ancestor` verdicts, never as shas. The unsharded run captures that at each
  boundary's line; shard k captures it at its start; **a replay is owed where the two differ and is
  correct when they match after it**, both captures named on failure. **The named negative, per
  boundary:** where the boundary's derived leaked set is non-empty, run the shard with it planted
  and absent and require the NAME set to differ; where it is empty, the arm SKIPS naming the
  boundary and that nothing existed to plant — a skip that announces itself, never a pass by
  vacuity. The leaks are DERIVED from both stores: every head on the fixture origin or in the local
  `refs/heads` that a fresh start does not carry. At this base that is `ahead` (origin, from the
  text `"$ahead:refs/heads/ahead"`) and `trunk` (BOTH — created locally at the text
  `git branch -f trunk main` and pushed at the next line). `reset_tree` gains the delete of that
  derived set as ONE invocation against the bare origin, `git --git-dir="$ORIGIN" update-ref
  --stdin`, because the `update-ref --stdin` it runs today addresses the CLONE and cannot reach the
  origin; the local half rides the clone-side batch that already exists. The three carriers —
  variables, functions, refs — are scanned per boundary and the scan is recorded. Observed by
  **AC8** and **AC12**.
- **S6** — the accumulation-dependent control gets a MECHANISM, not a placement, and the count it
  asserts is DECLARED BY ITS BLOCK, not typed here. The population by the note's own key is ONE arm,
  at the text `the tree is still clean after nine mutations`. Its block (the text `Nine branches,
  nine arms` through that control) holds more than nine `reset_tree`-led cycles — arm 6b alone runs
  three — and none is a `mutate()` call, so "nine" is the arm count and not the cycle count. The
  block sets `MUT_EXPECTED` beside its first cycle and each `reset_tree`-led cycle in it increments
  a process-local `MUT`; the control asserts `same "<label>" "$MUT" "$MUT_EXPECTED"` BEFORE calling
  `run`. A control cut from its block reds at runtime; the correct unsharded run stays green because
  the constant and the counter are both the block's own. The note's "TWO CONTROLS" is corrected to
  the count found. Observed by **AC9**.

## 3. Non-goals (OUT)

- **Batching arms.** `TOOL-aBatchedArm-1`, measured at 40 to 44 minutes on its own.
- **The group linter.** `TOOL-aBatchedArm-2`.
- **The pooled hang bound and the carrier flip.** `TOOL-aBatchedArm-5`. This unit's rows run under
  `--sweep`'s inherited bound until it lands, and AC4's reading is what seeds its evidence.
- **Repairing the suite's pre-existing RED.** `TOOL-aQuenchedHarness-9` and `TOOL-aHoistedPass-38`
  own those. This unit must not change any arm's verdict.
- **Sharding the driver suite.** `TOOL-aTracedSpawn-1` records that quoting one `$1` makes it run
  unsharded; that is its remedy, not a reason it cannot be sharded. Its row is the kit's pooled floor
  after this unit lands, and `aPacedTurnstile-8` says both suites must move together for the pool to
  move. A separate unit, named here so the floor is not a surprise.

### Edges

- **consumes-from** `TOOL-aBatchedArm-4` — the regex that lets a `--shard i/8` row pass `--check`, the
  declared `--pooled` mode, and the kit runner's `--pooled` path.
- **hands-off** `TOOL-aBatchedArm-5` — the evidence-derived pooled hang bound; AC4's reading seeds it.
- **hands-off** `TOOL-aBatchedArm-1` — the conversion, which lands on top of this split.

## 4. Design

### What the split is expected to buy, and how the measurement decides the arity

The owner ruled eight (`TOOL-aGradedDoorway-7` S2, 2026-08-29), and this id CARRIES that ruling for
this suite — `-7` S2 is superseded here and keeps the driver half; the edge grammar admits only
`consumes-from` and `hands-off`, so the supersession is stated here rather than as a bullet. `TOOL-aPacedTurnstile-8`, CLOSED,
sharded both unattended suites and found "TWO shards each is sufficient: past that the bar is
throughput-bound and further splitting buys exactly zero" — on the BAR's pool, filled with other
legs. The on-demand pooled run of the eight rows alone fills eight slots, but shares one serialised
spawn path (~190 ms per fork, per the full-sweep record) that `TOOL-aScannedThrottle-6` measures
dilating a bar leg 1.5 to 1.85x. So AC4 takes TWO readings on the same frozen clone: the two-shard
wall at BASE before S1 lands, and the eight-shard pooled wall at HEAD after. **The 20-minute arm decides the goal.
The ratio of eight's longest shard to two's longest decides the arity**: at or above 0.5, eight
bought less than two would, F2's fallback applies, and the arity is lowered with both readings beside
it. Neither result is hidden inside the other.

### Why the split is safe, on three carriers

Shell variables: zero cross a boundary (measured at rev-1, and it was the wrong carrier to stop at).
Functions: 28 are defined inside regions and any cut past one that is called later breaks it; S1
hoists them and derives the count. Refs: region one's `ahead` block force-pushes `main` and leaves
`unit` its ancestor, and region two's `tWaive` fixture fast-forwards onto that without saying so — a
CONFLICT in a bare shard-2 run, which the file's existing `SH_I = 2` replay (the text `REPLAY WHAT
REGION ONE LEAVES`) exists to prevent and records three arms failing silently without. S5 turns that
one hand-written replay into a rule the cut is checked against at every boundary.

### Why the floor-graded count is the figure

The floor grades `$n` at the text `[ "$n" -ge "$FLOOR" ]`. The C21 pair runs after it, so the PASS
line prints 2 more than the floor graded. Every floor, and AC1's identity, reads the floor-graded
figure, because that is the one a shard can fail on; `PROLOGUE_ARMS` for that figure is 0 and the
existing comment saying so is correct. rev-3 declared it 2 from the PASS line and would have redded
AC1 by 14 on a correct cut.

### Rollout

The leak delete (S5's `reset_tree` change) lands FIRST in its own commit, with AC12 observed, so its
effect on the unsharded verdict is never confounded with the re-cut's. Then S1, S3, the replays and
S6 together — a re-cut region without its floor, its replay or its instrumented control is a shard
that cannot fail on coverage. S2 once the serial readings exist. S4 last. AC4's two-shard reading is
taken before any of it, at BASE.

### Alternatives rejected

**Batching alone.** 40 to 44 minutes unsharded.

**Cutting spawns.** `TOOL-aTracedSpawn-2` bounds it at roughly 2 s per invocation of real work.

**Two shards.** Not rejected: it is F2's fallback, and AC4 measures it at BASE on the same clone.

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh` · `tools/run-gates/selftest-budgets.txt` ·
`tools/install-prefix-carried.txt` · `tools/run-gates/run-selftests.sh` or a sibling, for the ported
join · `tools/unattended/run-unattended-gates.sh`, the whole-suite note · this build's records.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the whole unit, measured twice at one commit so the arity is decided by evidence.
- error / empty / loading states — the arity and range refusals stay exact at 8; a row with no serial
  reading has no budget and `--check` reds it.
- observability — each shard prints its floor-graded count against its floor; the join names any
  missing index; AC4 prints all eight walls, max/mean, and the two ratios.
- risks — the class AC1 cannot see is an arm that executes and passes vacuously; S6's `MUT` counter
  is the mechanism that makes the one such arm FAIL when separated. Everything else a cut can break
  is on one of the three carriers S5 scans.
- testing — AC1 observed FAILING on a deliberately mis-cut region; AC8's replay observed failing when
  removed; AC9's control observed failing when separated; AC11's floor observed failing on a stranded
  block.
- migration — none. Reverting is the constant and one budget row.
- user docs — the two whole-suite notes are retargeted.

## 6. Acceptance criteria

- **AC1** — When `check-unattended.test.sh` runs at all eight shard indices and unsharded, reading
  the FLOOR-GRADED count from each, `sum(eight) == unsharded` holds exactly, `PROLOGUE_ARMS` being 0
  for that figure.
  `figure:` DERIVED from the nine runs.
  Red when: any other value.
- **AC2** — When an arm is deliberately moved into a shard that does not carry the state it depends
  on, `check-unattended.test.sh --shard <i>/8` REDS for that index.
  Red when: the move runs green.
- **AC3** — When `run-selftests.sh --kit tools/unattended/check-unattended.test.sh --list` runs, it
  names exactly eight rows; and `--check` exits 0 with them present.
  Red when: it names one, or `--check` reds.
- **AC4** — When `run-selftests.sh --pooled --kit tools/unattended/check-unattended.test.sh` runs on
  a frozen clone with no other bar on the box (asserted by `ps` before the run and named in the
  record), the runner's own `SWEEP of N suite(s), width W (outer O, inner I)` line shows N = 8 and
  O ≥ 8, and the record carries: all eight shard walls, their max and mean, the longest wall, and the
  two-shard longest wall taken on the SAME frozen clone at this spec's BASE, before S1 landed,
  as two concurrent direct invocations `check-unattended.test.sh --shard 1/2` and `--shard 2/2`
  timed with `date +%s` — direct, because at BASE no shard row exists for the runner to pool and
  the arity-2 contract does. **Every timed invocation, all ten, is a reading only if the suite's
  own TRAILER is present in its captured output** — the line at the text `this leg ran shard` for a
  shard, the `PASS (…)` line for a green unsharded run, and for a red-but-complete unsharded run the
  last `FAIL` line followed by exit; `PASS` and `FAIL executed` alone are NOT the witness, because a
  red-but-complete run prints neither. A timing with no trailer is an arm that did not reach its
  end, the class this repo's `ab-arm-must-prove-it-ran` note records, and is recorded as NO READING.
  `figure:` every number DERIVED from the two runs.
  `fixture:` the eight rows via the substring filter the runner honours; the profile row; the
  two-shard reading needs no row.
  `cost:` per-row bound = shard budget × `sweep-ceiling-factor`; run wall = the runner's `SWEEP_WALL`
  over the eight rows, printed at start; no typed number.
  Red when: the longest eight-shard wall exceeds 20 minutes (the GOAL, sends the remainder to
  batching); OR the longest eight-shard wall is ≥ 0.5 × the two-shard longest (the ARITY, F2's
  fallback applies); OR O < 8 on a host whose width is not (the run cannot pass and SKIPS by name).
- **AC5** — When one shard row is deleted from the declaration, the ported join REDS naming the
  missing index; and the join does NOT red on `unattended.test.sh`, which declares an arity and is
  called whole.
  Red when: eight-minus-one rows report green, or the sibling reds the join.
- **AC6** — When the split lands, the `FAIL` set across the eight shards is identical to the
  unsharded `FAIL` set at the same commit; and the unsharded run's floor-graded count equals the
  pre-split unsharded count, so no `in_shard k` region went green by absence when the arity moved.
  This is the VERDICT oracle and it is deliberately second to AC8's STATE oracle: it catches a
  verdict that moved, and AC8 catches the state that would move one silently.
  `cost:` one unsharded run plus eight sharded runs on the frozen clone.
  Red when: any `FAIL` line appears or disappears, or the unsharded count fell.
- **AC7** — When the eight rows are staged, `bash tools/check-install-prefix.sh` is green with the
  budgets-file count raised by hand and a fourth-column reason naming the eight literals.
  Red when: `ROSE`.
- **AC8** — When shard k starts at each of the seven boundaries, its topology capture — the ref
  NAME sets from `git ls-remote --heads "$ORIGIN"` and `git for-each-ref --format='%(refname)'
  refs/heads`, plus the `git merge-base --is-ancestor` verdicts the replay establishes — EQUALS the
  unsharded run's capture at that boundary's line, both captures in the build log; and at every
  boundary whose derived leaked set is non-empty, the same shard with that set planted and absent
  yields two DIFFERENT name sets, the arm each boundary breaks named; and at every boundary whose
  set is empty, the log carries the skip line naming it.
  `cost:` one unsharded run capturing at seven lines, seven shard starts, and up to seven
  planted/absent pairs, on the frozen clone.
  Red when: any boundary's captures differ after the replay, a non-empty negative shows no
  difference, or a boundary is neither paired nor named as skipped. No shard is required to run
  GREEN; the suite is red at BASE and §3 forbids changing that. Shas are not compared, because two
  processes never share one.
- **AC12** — When `reset_tree` runs after the leak-producing arms, `git ls-remote --heads` on the
  fixture origin AND `git for-each-ref refs/heads` in the clone each show the head set a fresh start
  shows; and the unsharded run's `FAIL` set with the delete in place is byte-identical to its `FAIL`
  set at this spec's base — observed in its OWN commit, landed before the re-cut, so the two changes
  are never graded together.
  Red when: a leaked head survives a reset in either store, or the delete moved any unsharded
  verdict — this unit changing a verdict through a fixture fix, which §3 forbids.
- **AC9** — When the `still clean after nine mutations` control is separated from its counted block,
  the shard carrying it REDS on the `same` over `$MUT` against `$MUT_EXPECTED`; and the correct
  unsharded run stays GREEN on the same assertion.
  Red when: the separated control runs green, OR the unsharded run reds — which is a typed count
  disagreeing with the block's own.
- **AC10** — When any helper defined inside a region is called from a different shard,
  `check-unattended.test.sh --shard <i>/8` REDS with command-not-found; observed by hoisting all but
  one and running the shard that calls it.
  Red when: the un-hoisted helper's caller runs green.
- **AC11** — When a block is deliberately stranded past an `exit` inside one shard, that shard REDS
  its floor; and every `FLOOR_SHARD_i` sits within the ~3 % headroom of its reading, both figures
  written beside it.
  Red when: the stranded shard runs green, or a floor is outside its headroom.
  `cost:` one stranded run per shard the arm is staged in; the floors come from AC1's nine runs.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `every held leg is budgeted, every budget row resolves`
· `install-prefix (shipped surface)` · `run-gates canary` · `run-selftests self-test`

New arm: `tools/unattended/check-unattended.test.sh` · a mis-cut region, a removed replay, a
separated control, an un-hoisted helper, a stranded block, each staged and observed RED then unstaged
· `tools/run-gates/run-selftests.test.sh` · a deleted shard row redding the ported join · floor to
move: `FLOOR_ASSERTIONS` plus eight new per-shard floors, measured under S3.

## 8. Open questions

- **F1 · Where does the shard-join predicate live?** RESOLVED (agent, 2026-09-13, delegated): ported
  as ONE function fed by the budget rows here and by the manifest in `TOOL-aGradedDoorway-8`'s kit
  file, scoped to `--shard` callers.
- **F2 · Eight, or fewer?** Eight is the owner's ruling. RESOLVED (owner, 2026-08-29): eight, with
  the fallback now MEASURED rather than argued — AC4's two-shard reading at BASE on the same clone,
  and the arity lowered with both readings beside it if eight's longest is at or above half of two's.

## 9. Revision log

- rev-8 · 2026-09-14 · §4 Rollout · §6 AC1 · AC4 · AC6 · AC8 · AC12 · CLOSED by owner ruling, as it
  stands. Two owner rulings govern this revision. 2026-09-13: build agents run no self-test on every
  step — build first, one verification pass when the build is complete; §4 Rollout's per-commit
  grading is superseded and AC12's "own commit" reading is satisfied by the final unsharded `FAIL`
  set at HEAD equalling BASE's. 2026-09-14: land the unit as it stands and run no gate until every
  unit of the build is built; the verification pass was stopped after its repeat's fourth shard.
  OBSERVED (the acceptance ledger has every run, wall and witness): AC1 — the eight floor-graded
  counts sum to the unsharded 555 exactly, `PROLOGUE_ARMS` 0; AC6 — the eight `FAIL` sets union to
  the unsharded 21 and are identical to BASE's 21, the count 555 against 554 being the one `same`
  S6 adds; AC8's positive half — seven boundary captures byte-identical to the unsharded run's,
  boundary 4 carrying `unit<main=yes` after the replay and the other six a fresh start; AC12 both
  halves; AC3, AC5 and AC7 in Phase A; AC4 arm one — the two-shard longest at BASE is 6656 s,
  taken beside this build's own shard run; the balance verdict OUTSIDE 1.35 on the first cut and
  the one permitted re-cut taken, whose repeat read 1301 · 1147 · 925 · 1407 s for shards 1..4
  before the stop. NOT OBSERVED, owed at the build's final gate pass: AC2, AC9, AC10, AC11 (the
  staged breaks), AC4 arm two (the pooled reading, the 20-minute verdict and the arity ratio — F2
  stays at eight until it is read), AC8's negative half, and shard 8's direct count and wall, so
  `FLOOR_SHARD_8` and its budget are DERIVED and say so beside themselves. One host fact this
  build measured that the record did not carry: a checker invocation on node `a` costs 47 to 60 s
  on an otherwise idle box, so the unsharded suite is ~5.8 hours there whatever the load, and the
  `~2 s` bound `TOOL-aTracedSpawn-2` records is another host's; the 20-minute target is a node `d`
  question, or a spawn-path question, and this unit did not answer it.
- rev-7 · 2026-09-13 · §2 S5 · §4 Rollout · §6 AC4 · AC8 · AC12 · §10 · folded spec-audit round 5
  (BLOCKED, 12 blocker rows in 3 defects, NON-CONVERGENT by rows against round 4's 4, precision
  0.75, disposition FOLD — the loop's exit; this spec is not re-reviewed). The oracle rev-6 reused
  from `TOOL-aShardedFloor-3` AC2 is sha-bearing and per-process, so it reds a correct cut at every
  boundary, and that build never discharged it — REFUSED here, keeping its state-not-verdict rule
  and its named negative. The capture is now TOPOLOGY: ref NAME sets plus `merge-base --is-ancestor`
  verdicts, never shas. The negative SKIPS by name at an empty boundary rather than redding by
  "no pair". AC4's witness was `PASS` or `FAIL executed`, neither of which a red-but-complete run
  prints; it is now the suite's trailer. `reset_tree`'s `update-ref --stdin` addresses the CLONE, so
  the origin delete is its own `--git-dir="$ORIGIN"` invocation and rev-6's "batched into the one it
  already runs on the bare repo" was false at source. `trunk` is created LOCALLY before it is pushed,
  so the derivation covers both stores. The delete lands in its own commit ahead of the re-cut so
  AC12 grades it alone.
- rev-6 · 2026-09-13 · §1 · §2 S5 · §4 · §6 AC4 · AC6 · AC8 · AC11 · AC12 · F2 · folded spec-audit
  round 4 (BLOCKED, 4 blocker rows, CONVERGING from 8, precision 0.40, scoped to S5/S6/AC4/AC8/AC9).
  S6, AC9 and the base bump drew zero confirmed findings and stand. The blocker: rev-5's
  verdict-based replay oracle compares `FAIL` sets, which the helpers print only on failure, so a
  red-at-BASE arm, a vacuous control or a shared needle leaves the set unchanged with the state
  wrong — and `TOOL-aShardedFloor-3` AC2 had already rejected exactly that oracle for exactly this
  file, in favour of comparing STATE with a named negative. rev-1 of that spec made the same mistake
  for the same reason. S5 and AC8 now REUSE that oracle; AC8 no longer requires a green shard, which
  §3 forbade. New AC12 observes that the leak delete moves no unsharded verdict, since AC6 cannot
  see a change on both sides. The leaks are derived (`ahead` and `trunk` at this base) and the
  delete is batched into the existing `update-ref --stdin`, not one push per ref. AC4's ten timed
  arms now require their own summary line as a completion witness, the `ab-arm-must-prove-it-ran`
  class. Five "at the same commit" sites corrected to "same clone, BASE then HEAD".
- rev-5 · 2026-09-13 · §2 S1 · §2 S5 · §2 S6 · §6 AC4 · AC6 · AC8 · AC9 · base · folded spec-audit
  round 3 (BLOCKED, 8 blocker rows, CONVERGING from 9, precision 0.42). Both blockers were the same
  defect as round 2's: a figure typed where the build should derive it. S5's "exactly one non-empty
  boundary" was false — the checker reads every remote head by `ls-remote` on every run, so the diff
  is non-empty at every region-two boundary and a read-based rule cannot decide; the rule is now
  VERDICT-based, each boundary run with and without its replay and the `FAIL` sets compared, and the
  `refs/heads/ahead` leak that `reset_tree` never cleared is fixed. S6's "nine" was the arm count,
  not the cycle count, and would have redded the correct unsharded run; the block now declares its
  own expected count and the control asserts that. AC4's two readings "at the same commit" cannot
  coexist across the arity change; the two-shard reading is two concurrent direct invocations at
  BASE on the same clone. The hoist population is derived, not typed as 28. AC6 gains the
  green-by-absence guard for `in_shard k > 8`. Base bumped to `0422ea2e`, since this unit consumes
  `--pooled` and the old base predates it.
- rev-4 · 2026-09-13 · §1 · §2 S1 through S6 · §3 · Edges · §4 · §5 · §6 AC1, AC3, AC4, AC8 through
  AC11 · §7 · F1 · F2 · §10 · folded spec-audit round 2 (BLOCKED, 9 blocker rows, precision 0.67).
  Three round-1 folds were half-right. `PROLOGUE_ARMS`: the floor-graded count EXCLUDES the C21 pair,
  which runs after the grade, so it is 0 and the comment rev-3 ordered corrected is TRUE — rev-3's 2
  would have redded AC1 by 14 on a correct cut. Replays: "seven" was the arity minus one; the file has
  one producer, one consumer and one leak, so S5 is a per-boundary ref-state DIFF rule and AC8 expects
  exactly one non-empty boundary. Controls: S6 was placement-only where the note says a separated
  control stays GREEN; it now carries a `MUT` counter the control asserts, and the population is one.
  Also: cuts only at block edges and re-balanced by serial readings, not invocation count
  (`aShardedFloor-3` §4); AC4's population isolated to the eight rows by the substring filter, its
  width asserted from the runner's own line, and a two-shard reading taken at the same commit so the
  ratio compares like with like; 28 region-local helpers hoisted with a derived count; the driver row
  named as the kit's pooled floor with the `aTracedSpawn-1` citation corrected; floors given an
  observable; `supersedes` edge to `aGradedDoorway-7` S2; anchors by text; `cost:` derived; the
  suite's own whole-suite note retargeted; a backlog-sharding citation dropped from §10.
- rev-3 · 2026-09-13 · §2 S1 through S6 · §4 · AC1 · AC4 · AC8 · AC9 · §10 · folded round 1's eight
  blockers, held until the runner settled.
- rev-2 · 2026-09-13 · Edges · §2 S2 · order · mirrors `TOOL-aBatchedArm-4` rev-2's split.
- rev-1 · 2026-09-10 · initial draft, from the measurement that batching alone lands at 40 to 44
  minutes. Adopted by `--rescope --act add` under protocol §11.

## 10. Reuse audit

- **The seams**, verified at source: the suite's shard contract — `SHARD_ARITY`, the parsed flag, the
  arity and range refusals, `in_shard()` — and its existing `SH_I = 2` replay at the text `REPLAY WHAT
  REGION ONE LEAVES`, which S5 generalises into a rule; the budget file's row grammar, which carries
  a per-row argv and needs no change; the runner's substring `--kit` filter, which AC4 uses to isolate
  the eight rows; and the gov canary's join at `run-gates.gov.test.sh`, which S4 PORTS. The reuse
  probe was run for THIS unit —
  `python tools/codebase-map/reuse_lookup.py "split a shell self-test into concurrent shard regions with a per-boundary replay of git ref state and a per-shard floor"`
  — and returned `build_self_chain`, `git` and `resolve_shell_argv`, none of which is any of these
  seams; it reports `unscanned layers: .sh`, so it cannot see the suite or the runner and its result
  is not evidence either way. The seams were found by reading the files.
  **Disposition of every record cited**: `TOOL-aShardedFloor-2` and `-3` REUSED for the contract
  and the block-edge cut rule; `-3`'s AC2 REUSED for its state-not-verdict rule and its named
  negative and REFUSED-BY for its sha-bearing capture, which round 5 measured redding a correct cut
  and which that build's own ledger never discharged — recorded because a reuse audit that finds a
  seam owes the reader whether the seam was ever seen working; `TOOL-aPacedTurnstile-8` REUSED (the crossover and "both must move
  together"); `TOOL-aScannedThrottle-6` REUSED (the dilation); `TOOL-aGradedDoorway-7` S2 SUPERSEDED
  for this suite; `TOOL-aGradedDoorway-8` REUSED (the join, one function two feeders);
  `TOOL-aTracedSpawn-1` REUSED (the driver's remedy); `TOOL-dScriptedRepeat-15` NOT-THIS-SEAM (a
  scoping ruling, and rev-3 cited it as a shard decision, which it is not).
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "what was measured about sharding a self-test suite, where the crossover is between shard count and throughput on a serialised spawn path, and how per-shard budgets and the whole-suite claim are derived" --terms "shard arity crossover throughput-bound dilation budget derivation whole-suite claim prologue floor in_shard region replay spawn serialised"`.

# TOOL-aBatchedArm-3 — grade the gate self-test as eight declared shards

**Status:** OPEN · rev-3 · 2026-09-13 · node a · Tier-2 · base e9ed269b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-review-TOOL-aBatchedArm-3-spec-audit-round1.md](../reviews/2026-09-10-review-TOOL-aBatchedArm-3-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`unattended gate selftest` is the costliest row in the declared self-test population and the member
the pooled runner's wall clock cannot fall below. Its 293 invocations are independent by
construction — the suite resets the tree before nearly every arm. Split them across eight declared
rows the runner's `--pooled` mode executes concurrently, and MEASURE what that buys on this host,
because the tree's own record says the crossover was two.

## 2. Scope (IN)

- **S1** — raise `SHARD_ARITY` from 2 to 8 in `tools/unattended/check-unattended.test.sh` and re-cut
  the two `in_shard` regions into eight, balanced by invocation count. Declare a REAL
  `PROLOGUE_ARMS` constant derived from the arms outside every `in_shard` region — the file today
  asserts 0 in a comment at `:3153` and the true figure is 2, from the epilogue — and correct that
  comment. Observed by **AC1**.
- **S2** — replace the single unsharded row in `tools/run-gates/selftest-budgets.txt` with eight
  rows, one per shard, each carrying a SERIAL reading taken by one `--serial` pass of the eight.
  The rows' explicit argv literals raise the file's count in `tools/install-prefix-carried.txt`, a
  BAN the ratchet cannot raise, so the count is raised by hand with a fourth-column reason in the
  same commit. The `--shard i/8` token passes `run-selftests.sh --check` because
  `TOOL-aBatchedArm-4` S1 landed the regex. Observed by **AC3** and **AC7**.
- **S3** — declare eight per-shard assertion floors and re-measure `FLOOR_ASSERTIONS`, each carrying
  the reading it was set against, and state which printed figure — the floor-graded count or the
  PASS-printed count, which differ by 2 today — every reading is taken from. Observed by **AC2**.
- **S4** — PORT the gov canary's shard-join predicate (`run-gates.gov.test.sh:360-406`, which
  iterates `gate-legs.json` argv lists) to the budget file's row format, so eight green shards
  constitute a whole-suite claim. A port and not a reuse: the canary is manifest-scoped and this
  suite has no manifest row. Scoped to scripts a budget row calls WITH `--shard`, or it reds at once
  on `unattended.test.sh`, which declares an arity and is called whole. Observed by **AC5**.
- **S5** — derive a per-boundary REPLAY for each of indices 2 through 8, generalising the `SH_I = 2`
  block at `check-unattended.test.sh:1277-1293`, which the file already hand-replays because region
  one's anchor arms leave `unit` an ancestor of `main` and region two's `tWaive` fixture depends on
  it. The coupling is git REF state, not shell variables; the zero-variable scan in rev-1 measured
  the wrong carrier. Each replay is observed FAILING when removed. Observed by **AC8**.
- **S6** — enumerate BY LINE the accumulation-dependent controls — the "tree is still clean after N
  mutations" shape the file's own shard note at `:3132-3140` says LOSE THEIR MEANING WITHOUT FAILING
  when split — and pin each into the same shard as the mutations it counts. Observed by **AC9**.

## 3. Non-goals (OUT)

- **Batching arms.** `TOOL-aBatchedArm-1`, measured at 40 to 44 minutes on its own.
- **The group linter.** `TOOL-aBatchedArm-2`.
- **The pooled hang bound and the carrier flip.** `TOOL-aBatchedArm-5`. This unit's rows run under
  `--sweep`'s inherited bound until it lands, and this unit's AC4 run is what seeds its evidence.
- **Repairing the suite's pre-existing RED.** `TOOL-aQuenchedHarness-9` and `TOOL-aHoistedPass-38`
  own those; 12 failures in shard 1 and 23 in shard 2 at BASE. This unit must not change any arm's
  verdict.
- **Sharding the sibling driver suite.** `TOOL-aTracedSpawn-1` records it cannot run unsharded.

### Edges

- **consumes-from** `TOOL-aBatchedArm-4` — the regex that lets a `--shard i/8` row pass `--check`, the
  declared `--pooled` mode, and the kit runner's `--pooled` path that runs the eight rows concurrently.
- **hands-off** `TOOL-aBatchedArm-5` — the evidence-derived pooled hang bound; AC4's reading is what
  seeds it.
- **hands-off** `TOOL-aBatchedArm-1` — the conversion, which lands on top of this split.

## 4. Design

### What the split is expected to buy, and why the number is not eight

The owner ruled eight on 2026-08-29 (`TOOL-aGradedDoorway-7` S2, "pick 8 and fix what breaks"). The
tree's own measurement says the crossover was TWO: `TOOL-aPacedTurnstile-8`, CLOSED, sharded both
unattended suites and found "TWO shards each is sufficient: past that the bar is throughput-bound at
~766s and further splitting buys exactly zero". That was the BAR's pool, filled with other legs; the
on-demand pooled run holds only these rows, so eight fill eight slots. But the resource they share is
the spawn path, which the full-sweep record measures as serialised at ~190 ms per fork, and
`TOOL-aScannedThrottle-6` measures in-pool dilation at 1.5 to 1.85x for a bar leg. Eight shards of a
fork-bound suite may buy far less than 4x over two. **AC4 therefore reports the RATIO of the pooled
wall to the serial sum, not only whether it cleared 20 minutes**, so a throughput-bound result is
recorded rather than hidden inside a red.

### Why the split is safe, and what the first measurement got wrong

rev-1 measured zero shell variables crossing an `in_shard` boundary and called the split safe. The
carrier that matters is git REF state: region one's anchor arms check out `main`, commit, force-push
and merge back, leaving `unit` an ancestor of `main`, and region two's `tWaive` fixture relies on that
without saying so — its merge is a fast-forward in the whole-suite run and a CONFLICT in a bare
shard-2 run. The file already knows this: `:1277-1293` hand-replays it for `SH_I = 2` and records
three arms failing silently without the replay. An eight-way cut owes seven such replays, derived
rather than hand-written, and each observed failing when removed. `anchor_break` and `anchor_restore`
are already hoisted; the replay is the other half of the HOIST SET.

### Why the two counts differ and which one grades

The floor at `:3130` grades `$n`, the executed assertion count. The PASS line prints a figure that
is 2 higher at HEAD, because the epilogue's two arms run after the floor check. `PROLOGUE_ARMS` is
undeclared in this file (the sibling declares 18) and the comment at `:3153` claiming 0 is false.
S3 declares it, and every reading names the floor-graded figure, because that is the one a shard
can fail on.

### Rollout

S1, S3, S5 and S6 land together — a re-cut region without its floor, its replay or its pinned
controls is a shard that cannot fail on coverage. S2 follows once the serial readings exist. S4 last,
since a join over eight rows needs the eight rows.

### Alternatives rejected

**Batching alone.** 40 to 44 minutes unsharded, because excluding the control arms leaves 95 blocks
carrying 136 solo invocations.

**Cutting spawns.** `TOOL-aTracedSpawn-2` bounds it at roughly 2 s per invocation of real non-spawn
work.

**Two shards, as the crossover measured.** Not rejected — it is the fallback F2 names if AC1 cannot
be satisfied at eight, and it is what AC4's ratio will show is or is not enough.

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh` · `tools/run-gates/selftest-budgets.txt` ·
`tools/install-prefix-carried.txt` · `tools/run-gates/run-selftests.sh` or a sibling, for the
ported join · `tools/unattended/run-unattended-gates.sh:157-158`, whose help text says the suites run
UNSHARDED on purpose and is false after S2 · this build's records.

## 5. Production-readiness checklist

- security — N/A. Scheduling only; no arm's subject changes.
- perf / scale — the whole unit, and it may not reach the target on this host; AC4 records the ratio
  either way.
- error / empty / loading states — the suite already REFUSES an out-of-range or wrong-arity
  `--shard`; S1 keeps that refusal exact at the new arity. A row with no serial reading refuses the
  pooled run, by `TOOL-aBatchedArm-5`'s rule once it lands and by `--sweep`'s inherited bound before.
- observability — each shard prints its executed count against its own floor; the ported join names
  any missing index; AC4 prints the ratio.
- risks — a cut that separates an arm from state a sibling established produces a GREEN that proves
  nothing. S5's replays and S6's pinned controls are the mitigation; AC8 and AC9 observe them
  failing when removed. **The class AC1 cannot see** — an arm that executes and passes vacuously — is
  exactly S6's population, and the count identity is not a substitute for it.
- testing — AC1 is the control and is observed FAILING on a deliberately mis-cut region before the
  split is trusted.
- migration — none. Reverting is restoring the constant and one budget row.
- user docs — the kit runner's help text at `:157-158` is rewritten; N/A otherwise.

## 6. Acceptance criteria

- **AC1** — When `check-unattended.test.sh` runs at all eight shard indices and unsharded, reading
  the FLOOR-GRADED count from each, `sum(eight counts) == unsharded + (SHARD_ARITY - 1) * PROLOGUE_ARMS`
  holds exactly.
  `figure:` DERIVED from the nine runs; `PROLOGUE_ARMS` read from the declaration S1 adds.
  Red when: any other value, which is an arm in no shard or in two.
- **AC2** — When an arm is deliberately moved into a shard that does not carry the state it depends
  on, `check-unattended.test.sh --shard <i>/8` REDS for that index. Staged and observed before the
  split is trusted.
  Red when: the move runs green, which is a split that proves nothing.
- **AC3** — When `bash tools/run-gates/run-selftests.sh --kit tools/unattended --list` runs, it names
  eight `unattended gate selftest` rows and not one; and `--check` exits 0 with them present.
  Red when: it names one, or `--check` reds the shard token.
- **AC4** — When `bash tools/unattended/run-unattended-gates.sh --pooled` runs on a frozen clone with
  no other bar on the box, the longest shard's wall clock is recorded, AND the ratio of that wall to
  the sum of the eight serial readings is printed and recorded.
  `figure:` both DERIVED from that run.
  `fixture:` the eight rows; the box's idleness is asserted by `ps` before the run and named in the
  record, since nothing in the runner observes it.
  `cost:` one pooled pass under `--sweep`'s inherited bound, 27200 s at the largest row.
  Red when: the longest shard exceeds 20 minutes — which sends the goal to `TOOL-aBatchedArm-1`'s
  batching on top — OR the ratio is above 0.5, which means eight bought less than 2x and
  `TOOL-aPacedTurnstile-8`'s crossover held; both are recorded, neither is hidden.
- **AC5** — When one shard row is deleted from the declaration, the ported join REDS naming the
  missing index; and when `unattended.test.sh`, which declares an arity and is called whole, is
  present, the join does NOT red on it.
  Red when: eight-minus-one rows report a whole-suite green, or the sibling suite reds the join.
- **AC6** — When the split lands, the `FAIL` set across the eight shards is identical to the
  unsharded `FAIL` set at the same commit.
  `cost:` one unsharded run plus eight sharded runs on a frozen clone.
  Red when: any `FAIL` line appears or disappears.
- **AC7** — When the eight rows are staged, `bash tools/check-install-prefix.sh` is green with the
  `selftest-budgets.txt` count raised by hand and a fourth-column reason naming the eight literals.
  Red when: the leg reds `ROSE`, which is the ban firing on a raise nobody explained.
- **AC8** — When any one of the seven derived replays for indices 2 through 8 is removed, that
  shard's `tWaive` merge conflicts and the shard REDS.
  Red when: a shard without its replay runs green, which is the silent-failure mode `:1277`'s own
  comment records three arms taking.
- **AC9** — When an accumulation-dependent control is separated from the mutations it counts, its
  shard REDS rather than degrading into a duplicate of the opening control.
  Red when: the separated control runs green, which the file's own note at `:3132` says is the
  failure mode of a split.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `every held leg is budgeted, every budget row resolves`
· `install-prefix (shipped surface)` · `run-gates canary` · `run-selftests self-test`

New arm: `tools/unattended/check-unattended.test.sh` · a region deliberately mis-cut so an arm loses
its state, a replay removed, and a control separated from its mutations, each staged and observed RED
then unstaged · `tools/run-gates/run-selftests.test.sh` · a deleted shard row redding the ported join
· floor to move: `FLOOR_ASSERTIONS` plus eight new per-shard floors, all measured under S3.

## 8. Open questions

- **F1 · Where does the shard-join predicate live?** REOPENED at rev-3: the gov canary's predicate
  is manifest-scoped and this suite has no manifest row, so applying it is a PORT. RESOLVED (agent,
  2026-09-13, delegated): port it to the budget file's row format in the runner or a sibling, scoped
  to scripts a row calls WITH `--shard`; the kit-shipping half stays `TOOL-aGradedDoorway-8`'s row.
- **F2 · Eight, or fewer?** Eight is the owner's ruling. RESOLVED (owner, 2026-08-29): eight. If AC1
  cannot be satisfied at eight, or AC4's ratio shows eight bought less than two would, the finding
  is recorded and the arity is lowered with the reading beside it, never raised to fit.

## 9. Revision log

- rev-3 · 2026-09-13 · §1 · §2 S1 through S6 · §4 · §5 · §6 AC1 · AC3 · AC4 · AC5 · AC8 · AC9 · §7
  · F1 · §10 · folded spec-audit round 1 (BLOCKED, 8 blockers), held until the runner unit's shape
  settled because three of them were about the runner. Two dissolved with `TOOL-aBatchedArm-4`: the
  row checker admits the shard token (B3, B4) and `--pooled` exists (B1, B2). The rest were real:
  the zero-variable scan measured the wrong carrier and `:1277-1293` already hand-replays the git
  ref state that actually couples regions (B5, H4), now S5 and AC8; the join is a port not a reuse
  and would red on the sibling suite (B6), now S4 and AC5 scoped; the file's own note names controls
  that lose meaning when split and AC1 cannot see them (B7, H3), now S6 and AC9; the reuse audit was
  declined and four deciding records were absent (B8), now §10 with this unit's own probe, which
  surfaced `TOOL-aPacedTurnstile-8`'s crossover at TWO — AC4 now reports the ratio so a
  throughput-bound result is recorded; `PROLOGUE_ARMS` undeclared and the two counts differ (H1, H2),
  now S1, S3 and AC1's arithmetic; §7's leg wrong (M1); the kit runner's help text falsified by S2
  (M2), now in Files touched.
- rev-2 · 2026-09-13 · Edges · §2 S2 · order · mirrors `TOOL-aBatchedArm-4` rev-2's split.
- rev-1 · 2026-09-10 · initial draft, from round 2's measurement that batching alone lands at 40 to
  44 minutes. Adopted by `--rescope --act add` under protocol §11.

## 10. Reuse audit

- **The seam is the suite's own shard contract**, verified at source at
  `tools/unattended/check-unattended.test.sh:29-56` — `SHARD_ARITY`, the parsed `--shard <i>/<n>`
  flag, the arity and range refusals, `in_shard()` — plus the `SH_I = 2` replay at `:1277-1293`,
  which S5 generalises rather than reinvents, and the HOIST SET note that already names
  `anchor_break` and `anchor_restore`. The declaration seam is `tools/run-gates/selftest-budgets.txt`'s
  row grammar, which carries a per-row argv and needs no format change. The join seam is
  `tools/run-gates/run-gates.gov.test.sh:360-406`, which F1 resolves to PORTING. The reuse probe was
  run —
  `python tools/codebase-map/reuse_lookup.py "batch staged breaks into one fixture and assert the emitted failure set"`
  — for the build's first unit, and reports `unscanned layers: .sh`; it cannot see any of these seams
  and its result is not evidence either way. The seams were found by reading the file.
- **The retrieval arguments, verbatim, THIS unit's own:**
  `python tools/memory-recall/query.py "what was measured about sharding a self-test suite, where the crossover is between shard count and throughput on a serialised spawn path, and how per-shard budgets and the whole-suite claim are derived" --terms "shard arity crossover throughput-bound dilation budget derivation whole-suite claim prologue floor in_shard region replay spawn serialised"`.
  It returned `TOOL-aPacedTurnstile-8` first — the measured crossover at two — and
  `TOOL-aRelaxedShard-4`, `TOOL-aShardedFloor-3` and `TOOL-dScriptedRepeat-15`, which are the shard
  contract's own decisions. rev-1's §10 cited a probe run for a different unit; round 1 B8 was right
  that a probe for batching is not a reuse audit for sharding.

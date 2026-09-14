---
slug: aBatchedArm
node: a
opened: 2026-09-10
streams: tooling
roster: TOOL
ids: TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 TOOL-aBatchedArm-4 TOOL-aBatchedArm-5
authorized-by: prompt
---

# aBatchedArm — divide the suite that floors the pool

## The problem this build exists to solve

`unattended gate selftest` is the costliest row in the declared self-test population and the member
the pooled runner's wall clock cannot fall below. It costs that because it re-runs the whole checker
once per arm. **The figures live in `TOOL-aBatchedArm-1` §1 and §4 and are not restated here**, which
is `two-answers-to-one-question` applied to this file: the spec carries a base sha, so its numbers
are a measurement at a commit, and a second copy in prose beside it is the copy that rots. The
current ranking is one command away: `bash tools/run-gates/run-selftests.sh --rank`.

`TOOL-aPooledSweep-7` names the remedy and does not build it: "Falling further means dividing that
one suite." This build is that follow-up. Target: a verdict in under 20 minutes, no assertion deleted.

## Expected improvements

- Eight declared shard rows the runner's pool executes concurrently, so the verdict arrives in
  roughly a tenth of the wall clock with no assertion changed and no new oracle.
- Batching on top of that split, for the arms that can share a tree.
- A structural linter that enforces the partition, so a mis-grouped arm reds instead of passing.

## Detriments if this is not built

- The pool stays floored at this one member, so the whole population keeps a 2.5 hour wall.
- A suite nobody can afford to run is a suite nobody runs. This one is RED at BASE and has been since
  before `TOOL-aQuenchedHarness-9` counted it, which is what a held, unaffordable check decays into.

## Build-level rules

**Three routes are closed and the specs own the evidence, not this slot.** The `lib-selftest` port,
by ratified `TOOL-aPooledSweep-3`; further spawn cutting, bounded by `TOOL-aTracedSpawn-2`; and
batching the control arms, by `TOOL-dScriptedRepeat-15` S3. Each is argued with its measurement in
`TOOL-aBatchedArm-1` §3 and §4.

**A CHECK NUMBER IS NOT A BRANCH IDENTIFIER, and that killed the first design.** Only 6 of 29 check
numbers carry a single branch; check 16 carries 34. So no control is witnessed by a sibling firing
under the same number, and no `miss` or `same` arm is batched at all. That exclusion is why batching
alone measures 40 to 44 minutes.

**The baseline is RED and is the oracle.** Equivalence is the `FAIL` line set plus the executed
assertion count — NOT a per-arm inventory, because the helpers are silent on a pass.

**OWNER RULINGS, 2026-09-10, answering the parked scope question.** (1) The route is the SHARED
RUNNER: `tools/run-gates/run-selftests.sh` gets a slash-tolerant row checker and DECLARED execution
modes, so pooled is available and **serial stays possible when it is deliberately declared**. That
ruling resolves the tension this build parked on — `OUTER=1` exists so racing suites do not charge
each other's contention to the wrong budget, and a declared mode carries that contract explicitly
instead of implying it. (2) The batching units are BUILT, after the shard route, not retired.
(3) Everything on this branch lands.

**OWNER RULINGS, 2026-09-13/14.** No self-test per step; no gate until every unit is built;
ONE verification pass at the end. Unit 3's first pass was stopped for it.

**OWNER RULING, 2026-09-14, unit 1:** the `$out` token allowed, nineteen groups, sets from the
observed run at the final pass.

## Parked decisions

None yet.

<!-- roster:units -->
| Order | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBatchedArm-4` | declared execution modes for the shared runner: `--serial` and `--pooled`, bare run refuses, the row checker admits a shard token. The prerequisite. |
| 2 | `TOOL-aBatchedArm-3` | grade the suite as EIGHT declared shard rows. The split that reaches the goal, once the runner can run it. |
| 3 | `TOOL-aBatchedArm-5` | the evidence-derived pooled hang bound, and the flip of the kit runner's default to pooled once it is sound. UNSPECCED. |
| 4 | `TOOL-aBatchedArm-1` | one assertion helper, `emitted`, plus the grouping of arms whose breaks do not interfere. Measured at 40 to 44 minutes alone. |
| 5 | `TOOL-aBatchedArm-2` | the structural group linter that enforces unit 1's partition. |

**The order is the reverse of the order the first three were written in, and that is the build's own
finding.** Batching was specced first and audited twice; round 2 measured that it cannot reach the
goal alone. The shard split reaches it — but only through a runner that can run shards concurrently,
which is unit 4, and only safely under a bound that is not the one that killed 14 of 58 suites, which
is unit 5. Units 4 and 5 were adopted after those measurements, not planned.
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node a · opened 2026-09-10 · streams tooling
ids TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 TOOL-aBatchedArm-4 TOOL-aBatchedArm-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBatchedArm-4 — declared execution modes for the self-test runner](spec/2026-09-13-spec-TOOL-aBatchedArm-4.md) | 1 | 2 | CLOSED | rev-5 | 2026-09-13 |
| [TOOL-aBatchedArm-3 — grade the gate self-test as eight declared shards](spec/2026-09-10-spec-TOOL-aBatchedArm-3.md) | 2 | 2 | CLOSED | rev-8 | 2026-09-14 |
| [TOOL-aBatchedArm-5 — the evidence-derived pooled hang bound, and the flip](spec/2026-09-13-spec-TOOL-aBatchedArm-5.md) | 3 | 2 | CLOSED | rev-7 | 2026-09-14 |
| [TOOL-aBatchedArm-1 — batch the gate self-test's arms by tree state](spec/2026-09-10-spec-TOOL-aBatchedArm-1.md) | 4 | 2 | CLOSED | rev-7 | 2026-09-14 |
| [TOOL-aBatchedArm-2 — the structural group linter over the batched self-test](spec/2026-09-10-spec-TOOL-aBatchedArm-2.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-14 |
<!-- /gen:build-units -->

Records: 29 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBatchedArm-4` | no |
| 2 | `TOOL-aBatchedArm-3` | no |
| 3 | `TOOL-aBatchedArm-5` | no |
| 4 | `TOOL-aBatchedArm-1` | no |
| 5 | `TOOL-aBatchedArm-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

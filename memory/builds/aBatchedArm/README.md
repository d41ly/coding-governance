---
slug: aBatchedArm
node: a
opened: 2026-09-10
streams: tooling
roster: TOOL
ids: TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3
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

**The port is CLOSED, by ratified decision and not by preference.** `TOOL-aPooledSweep-3`: `arm`
takes one POSITIVE substring, these suites assert negatives, so a port rewrites the assertion and the
inventory diff refuses it. This suite carries 101 `miss` and 27 `same`. Re-opening it starts with the
harness vocabulary `TOOL-aPooledSweep-7` enumerates, and that is a different build.

**Cutting spawns cannot reach the target.** `TOOL-aTracedSpawn-2` measured roughly 2 s per invocation
of real non-spawn work, a ~586 s floor at 293 invocations. Only invocations move the number.

**The batching premise has a counter-example this build inherits.** `TOOL-aDrainedSluice-5` N17 found
it false where callers short-circuit. Reproduced here 2026-09-10: eight staged breaks emitted four
checks, one tripping check 1, whose branch exits at `check-unattended.sh:198`.

**A CHECK NUMBER IS NOT A BRANCH IDENTIFIER, and that killed the first design.** Only 6 of 29 check
numbers carry a single branch; check 16 carries 34. So no control can be witnessed by a sibling
firing under the same number, `TOOL-dScriptedRepeat-15` S3 stands unqualified, and no `miss` or
`same` arm is batched at all. That exclusion is why batching alone measures 40 to 44 minutes and why
the shard split is unit 1 of the three.

**The baseline is RED and is the oracle.** Equivalence is the `FAIL` line set plus the executed
assertion count — NOT a per-arm inventory, because the helpers are silent on a pass.

## Parked decisions

None yet.

<!-- roster:units -->
| Order | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBatchedArm-3` | grade the suite as EIGHT declared shards the runner's pool executes concurrently. This is the half that meets the goal. |
| 2 | `TOOL-aBatchedArm-1` | one assertion helper, `emitted`, plus the grouping of arms whose breaks do not interfere. An optimisation on top of the split, measured at 40 to 44 minutes alone. |
| 3 | `TOOL-aBatchedArm-2` | the structural group linter that enforces unit 1's partition, which unit 1 can state and cannot check per group. |

**The order is the reverse of the order they were written in, and that is the build's own finding.**
The batching unit was specced first and audited twice; round 2 then measured that it cannot reach the
goal alone, because excluding the control arms `TOOL-dScriptedRepeat-15` S3 forbids batching leaves
95 blocks carrying 136 solo invocations. The shard split reaches it with no new oracle. Unit 3 was
adopted under protocol §11 after that measurement, not planned.
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 3 unit(s) · node a · opened 2026-09-10 · streams tooling
ids TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBatchedArm-3 — grade the gate self-test as eight declared shards](spec/2026-09-10-spec-TOOL-aBatchedArm-3.md) | 1 | 2 | OPEN | rev-1 | 2026-09-10 |
| [TOOL-aBatchedArm-1 — batch the gate self-test's arms by tree state](spec/2026-09-10-spec-TOOL-aBatchedArm-1.md) | 2 | 2 | OPEN | rev-3 | 2026-09-10 |
| [TOOL-aBatchedArm-2 — the structural group linter over the batched self-test](spec/2026-09-10-spec-TOOL-aBatchedArm-2.md) | 3 | 2 | OPEN | rev-2 | 2026-09-10 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: TOOL-aBatchedArm-3.

Ids no `spec-audit` record has ever named: TOOL-aBatchedArm-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBatchedArm-3` | no |
| 2 | `TOOL-aBatchedArm-1` | no |
| 3 | `TOOL-aBatchedArm-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

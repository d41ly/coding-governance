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

- One invocation per BATCH of mutually independent breaks, instead of one per arm.
- `set(emitted signatures) == set(expected)` as the assertion, which is the RED observation for every
  break in the batch AND the GREEN control for every branch outside it. The paired-control doctrine
  is absorbed rather than weakened.
- All 178 branch signatures are unique under `check-arms.py`'s own normaliser, verified 2026-09-10,
  so the set has a sound key.

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
checks, one tripping check 1, whose branch exits at `check-unattended.sh:198`. The partition must
respect short-circuits; set equality is what makes a truncated batch red rather than green.

**The baseline is RED and is the oracle.** Equivalence is verdict identity per arm, not a green run.

## Parked decisions

None yet.

<!-- roster:units -->
| Unit | Mechanism |
|---|---|
| `TOOL-aBatchedArm-1` | one assertion helper, `emitted`, plus the grouping of arms whose breaks do not interfere onto one tree and one invocation |

Decomposed to ONE unit deliberately. The earlier plan carried four — a declarative arm table, a
partition solver, a golden-set oracle and a liveness pin — and §4 of the spec rejects that shape on
the measurement: a table rewrites 377 assertions to reach a target one helper reaches, and a
rewritten assertion is what closed the port. The liveness pin is not a second mechanism either, since
`FLOOR_ASSERTIONS` survives the conversion and is re-measured under S4.
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 2 unit(s) · node a · opened 2026-09-10 · streams tooling
ids TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBatchedArm-1 — batch the gate self-test's arms by tree state](spec/2026-09-10-spec-TOOL-aBatchedArm-1.md) | 2 | 2 | OPEN | rev-3 | 2026-09-10 |
| [TOOL-aBatchedArm-2 — the structural group linter over the batched self-test](spec/2026-09-10-spec-TOOL-aBatchedArm-2.md) | 3 | 2 | OPEN | rev-2 | 2026-09-10 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 2 | `TOOL-aBatchedArm-1` | no |
| 3 | `TOOL-aBatchedArm-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

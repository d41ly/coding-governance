---
slug: aDrainedSluice
node: a
opened: 2026-08-08
streams: tooling
roster: TOOL
ids: TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9
---

# aDrainedSluice — drain the tooling backlog to zero

Every OPEN and DEFERRED row in `memory/backlog/TOOL.md` is resolved: built, or closed WONTDO with the
reason. Eleven rows in, zero out.

## Units

| Unit | Sub-spec | Backlog row it drains |
|---|---|---|
| V1 | `spec-aDrainedSluice-2-v1-arms-every-gate` — CLOSED | `TOOL-aFoldedQuarry-8` |
| V3 | `spec-aDrainedSluice-3-v3-nested-recordings` — CLOSED | `TOOL-aRuledParchment-2` |
| V4 | `spec-aDrainedSluice-4-v4-rev-scan-reset` — CLOSED | `TOOL-aBatchedLintel-2` |
| V2 | `spec-aDrainedSluice-5-v2-arm-the-branches` — CLOSED | `TOOL-aFoldedQuarry-7` |
| V5 | `spec-aDrainedSluice-6-v5-python-resolver` — CLOSED | `TOOL-aQuarriedLantern-2` |
| V6 | `spec-aDrainedSluice-7-v6-recall-cache-cap` — CLOSED | `TOOL-aQuarriedLantern-3` |
| V7 | `spec-aDrainedSluice-8-v7-three-hardenings` — CLOSED | `TOOL-aFoldedQuarry-3/-4/-5` |
| V8 | `spec-aDrainedSluice-9-v8-dead-path-census` — CLOSED | `TOOL-aFoldedQuarry-6` |

`TOOL-bThriftyBellows-2` needs no unit: it is a performance idea for `gen-memory-tree.sh`, and that
script was deleted with the authored tree index. It closes WONTDO in V9, citing its successor.

A row becomes a link when its sub-spec lands. A link to an unwritten file is a broken link, and
hygiene check 2 is right to say so.

## Order

V1 → V3 → V4 first: each changes the set of `fail` branches, and V2 arms whatever that set finally
is. Arming before the set settles would be arming a moving target. V5–V8 are independent of the
branch work and of each other.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aDrainedSluice-1` | 2 | drain the tooling backlog to zero |
| 2 | `TOOL-aDrainedSluice-2` | 2 | V1: the harness meta-gate discovers its gates |
| 3 | `TOOL-aDrainedSluice-3` | 2 | V3: check 5 governs a recording at any depth |
| 4 | `TOOL-aDrainedSluice-4` | 2 | V4: the §9 rev high-water stops at §9 |
| 5 | `TOOL-aDrainedSluice-5` | 2 | V2: arm every pinned branch, or say why not |
| 6 | `TOOL-aDrainedSluice-6` | 2 | V5: one python resolver, and it EXECUTES the candidate |
| 7 | `TOOL-aDrainedSluice-7` | 2 | V6: the recall cache is bounded |
| 8 | `TOOL-aDrainedSluice-8` | 2 | V7: three gates that could not see what they judge |
| 9 | `TOOL-aDrainedSluice-9` | 2 | V8: a dead DIRECTORY citation is a dead citation |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 9 unit(s) · node a · opened 2026-08-08 · streams tooling
ids TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aDrainedSluice-1 — drain the tooling backlog to zero](spec/2026-08-08-spec-aDrainedSluice-1.md) | — | 2 | CLOSED | rev-2 | 2026-08-08 |
| [TOOL-aDrainedSluice-2 — V1: the harness meta-gate discovers its gates](spec/units/2026-08-08-spec-aDrainedSluice-2-v1-arms-every-gate.md) | — | 2 | CLOSED | rev-2 | 2026-08-20 |
| [TOOL-aDrainedSluice-3 — V3: check 5 governs a recording at any depth](spec/units/2026-08-08-spec-aDrainedSluice-3-v3-nested-recordings.md) | — | 2 | CLOSED | rev-2 | 2026-08-20 |
| [TOOL-aDrainedSluice-4 — V4: the §9 rev high-water stops at §9](spec/units/2026-08-08-spec-aDrainedSluice-4-v4-rev-scan-reset.md) | — | 2 | CLOSED | rev-3 | 2026-08-20 |
| [TOOL-aDrainedSluice-5 — V2: arm every pinned branch, or say why not](spec/units/2026-08-08-spec-aDrainedSluice-5-v2-arm-the-branches.md) | — | 2 | CLOSED | rev-4 | 2026-08-08 |
| [TOOL-aDrainedSluice-6 — V5: one python resolver, and it EXECUTES the candidate](spec/units/2026-08-08-spec-aDrainedSluice-6-v5-python-resolver.md) | — | 2 | CLOSED | rev-3 | 2026-08-08 |
| [TOOL-aDrainedSluice-7 — V6: the recall cache is bounded](spec/units/2026-08-08-spec-aDrainedSluice-7-v6-recall-cache-cap.md) | — | 2 | CLOSED | rev-3 | 2026-08-08 |
| [TOOL-aDrainedSluice-8 — V7: three gates that could not see what they judge](spec/units/2026-08-08-spec-aDrainedSluice-8-v7-three-hardenings.md) | — | 2 | CLOSED | rev-3 | 2026-08-08 |
| [TOOL-aDrainedSluice-9 — V8: a dead DIRECTORY citation is a dead citation](spec/units/2026-08-08-spec-aDrainedSluice-9-v8-dead-path-census.md) | — | 2 | CLOSED | rev-3 | 2026-08-20 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aDrainedSluice-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
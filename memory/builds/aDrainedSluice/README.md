---
slug: aDrainedSluice
node: a
opened: 2026-08-08
streams: tooling
roster: TOOL
ids: TOOL-aDrainedSluice-1..-9
---

# aDrainedSluice — drain the tooling backlog to zero

Every OPEN and DEFERRED row in `memory/backlog/TOOL.md` is resolved: built, or closed WONTDO with the
reason. Eleven rows in, zero out.

## Units

| Unit | Sub-spec | Backlog row it drains |
|---|---|---|
| V1 | `spec-aDrainedSluice-2-v1-arms-every-gate` — pending | `TOOL-aFoldedQuarry-8` |
| V3 | `spec-aDrainedSluice-3-v3-nested-recordings` — pending | `TOOL-aRuledParchment-2` |
| V4 | `spec-aDrainedSluice-4-v4-rev-scan-reset` — pending | `TOOL-aBatchedLintel-2` |
| V2 | `spec-aDrainedSluice-5-v2-arm-the-branches` — pending | `TOOL-aFoldedQuarry-7` |
| V5 | `spec-aDrainedSluice-6-v5-python-resolver` — pending | `TOOL-aQuarriedLantern-2` |
| V6 | `spec-aDrainedSluice-7-v6-recall-cache-cap` — pending | `TOOL-aQuarriedLantern-3` |
| V7 | `spec-aDrainedSluice-8-v7-three-hardenings` — pending | `TOOL-aFoldedQuarry-3/-4/-5` |
| V8 | `spec-aDrainedSluice-9-v8-dead-path-census` — pending | `TOOL-aFoldedQuarry-6` |

`TOOL-bThriftyBellows-2` needs no unit: it is a performance idea for `gen-memory-tree.sh`, and that
script was deleted with the authored tree index. It closes WONTDO in V9, citing its successor.

A row becomes a link when its sub-spec lands. A link to an unwritten file is a broken link, and
hygiene check 2 is right to say so.

## Order

V1 → V3 → V4 first: each changes the set of `fail` branches, and V2 arms whatever that set finally
is. Arming before the set settles would be arming a moving target. V5–V8 are independent of the
branch work and of each other.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 9 unit(s) · node a · opened 2026-08-08 · streams tooling · ids TOOL-aDrainedSluice-1..-9

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aDrainedSluice-1 — drain the tooling backlog to zero](spec/2026-08-08-spec-aDrainedSluice-1.md) | INPROGRESS | rev-1 | 2026-08-08 |
| [TOOL-aDrainedSluice-2 — V1: the harness meta-gate discovers its gates](spec/units/2026-08-08-spec-aDrainedSluice-2-v1-arms-every-gate.md) | INPROGRESS | rev-2 | 2026-08-08 |
| [TOOL-aDrainedSluice-3 — V3: check 5 governs a recording at any depth](spec/units/2026-08-08-spec-aDrainedSluice-3-v3-nested-recordings.md) | INPROGRESS | rev-2 | 2026-08-08 |
| [TOOL-aDrainedSluice-4 — V4: the §9 rev high-water stops at §9](spec/units/2026-08-08-spec-aDrainedSluice-4-v4-rev-scan-reset.md) | INPROGRESS | rev-3 | 2026-08-08 |
| [TOOL-aDrainedSluice-5 — V2: arm every pinned branch, or say why not](spec/units/2026-08-08-spec-aDrainedSluice-5-v2-arm-the-branches.md) | INPROGRESS | rev-2 | 2026-08-08 |
| [TOOL-aDrainedSluice-6 — V5: one python resolver, and it EXECUTES the candidate](spec/units/2026-08-08-spec-aDrainedSluice-6-v5-python-resolver.md) | INPROGRESS | rev-1 | 2026-08-08 |
| [TOOL-aDrainedSluice-7 — V6: the recall cache is bounded](spec/units/2026-08-08-spec-aDrainedSluice-7-v6-recall-cache-cap.md) | INPROGRESS | rev-1 | 2026-08-08 |
| [TOOL-aDrainedSluice-8 — V7: three gates that could not see what they judge](spec/units/2026-08-08-spec-aDrainedSluice-8-v7-three-hardenings.md) | INPROGRESS | rev-1 | 2026-08-08 |
| [TOOL-aDrainedSluice-9 — V8: a dead DIRECTORY citation is a dead citation](spec/units/2026-08-08-spec-aDrainedSluice-9-v8-dead-path-census.md) | INPROGRESS | rev-2 | 2026-08-08 |
<!-- /gen:build-index -->

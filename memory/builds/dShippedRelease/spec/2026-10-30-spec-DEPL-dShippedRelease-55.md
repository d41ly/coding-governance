# DEPL-dShippedRelease-55 — `release.pick` stops at what an environment already runs, so a re-tick promotes nothing older

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 72 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, item B5. Unit 15 S6 picks the newest landed green SHA that E lacks, with no stop at what E
already runs, and records are per (SHA, environment), so a passed-over SHA still reads as lacked.
After E takes S3 the next tick promotes S2, then S1, down the line: a downgrade the design row at
layer-expansions:387 had ruled out. This unit gives the walk a floor and says how each outcome
counts.

## 2. Scope (IN)

- **S1** — The floor, `derive_pick_floor(E, root)` in `tools/integrations/release.py`: the newest
  SHA on the first-parent line whose `release` record for E reads `verified`, or `None`. Observed by
  AC1, AC3.
- **S2** — The walk. `run_release_pick` walks from the tip and stops at the floor, exclusive. Every
  SHA at or behind the floor is superseded in E and is never picked. Observed by AC1.
- **S3** — `lacks`. A SHA with any `release` record for E is not lacked, whatever its outcome, so
  one tick's decision is never asked again. §4 "How an outcome counts" states each of the six.
  Observed by AC2.
- **S4** — An environment with no `verified` record has no floor: the walk takes the newest green
  SHA, and that promote sets the floor. A newly listed environment does not walk history. Observed
  by AC3.

## 3. Non-goals (OUT)

- What each outcome routes to: unit 15's `release.route` stands.
- The engine's answer for an empty environment: DEPL-dShippedRelease-77.

### Edges

- **consumes-from** `DEPL-dShippedRelease-15` — `run_release_pick`, the `release` record and `read_core_verdict`'s green, the walk this unit bounds

## 4. Design

### Evidence

- Unit 15 S6 states the pick, and its §4 "The records" keys a record by (SHA, environment).
- `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:387` carries the rule S6 left out, "an
  older SHA it passes over is superseded in E".

### How an outcome counts

| Outcome | E lacks the SHA | Sets the floor |
|---|---|---|
| no record | yes, above the floor | no |
| `verified` | no | yes |
| `held` | no | no |
| `rolled-forward` | no | no |
| `rolled-back` | no | no |
| `halted` | no | no |
| `unverified` | no | no |

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_pick_floor` | function, `tools/integrations/release.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/integrations/release.py`: S1 to S4
- `tools/integrations/release_fixture.py`: the cases of §6

### Alternatives rejected

- **Comparing `read-current`'s id with each SHA.** An engine reports a digest and no SHA, so it
  cannot order two landings.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — the walk stops at the floor, so a long history costs what the landings since it
  cost.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a `held` SHA is never re-offered, so a refused approval needs a later landing to move E;
  that is what `held` means in unit 15 S7.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python release_fixture.py --case pick-floor` plants three green landed SHAs and
  promotes the newest to `verified`, a second tick prints `nothing` and runs no `promote`.
  Red when: the second tick picks the next older SHA, the downgrade.
- **AC2** — When `--case pick-rolled-back` plants a `rolled-back` record on the newest SHA above a
  `verified` one, the tick prints `nothing`, and with one more green SHA landed it picks that one.
  Red when: a SHA rolled back in E is picked again, or a later landing is blocked by it.
- **AC3** — When `--case pick-new-environment` lists a new E over three green SHAs, the tick picks
  the newest, and after its `verified` record the next tick prints `nothing`.
  Red when: a new environment walks down history, one SHA per tick.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/release_fixture.py · covers AC1 AC2 AC3 · `pick-floor`, its failing case the walk with no floor · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 72 (BLOCKER, item B5) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is unit 15's `run_release_pick`.
`python tools/codebase-map/reuse_lookup.py "pick the newest verified release for an environment without going below the running one"`
ranked name-stem helpers (`derive_runner_verbs`, `run_without_git_env`, `ts_release`) and no release
reader, since `release.py` is specced and unbuilt, so no existing seam fits outside it. The recall
probe surfaced scout C's row and unit 15's brief line, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does promotion avoid a downgrade and what does an environment with no deployment read" --terms "release pick superseded environment rollback expect compare-and-swap first deploy engine verify"`

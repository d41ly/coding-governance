# DEPL-dShippedRelease-86 — `release.pick` stops at the newest SHA carrying any record for E

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 86 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, item B4, which stands beside id 5
(DEPL-dShippedRelease-91). Under unit 55 only `verified` sets the floor, S2 stops only at the floor,
and S3 only marks the recorded SHA as not lacked. E verified at S1 with landings S2 to S5: a tick picks
S5, verify fails, the default `deploy.on-verify-fail = roll-forward` ends `rolled-forward` with E still
running S5, and the next tick finds S4 unrecorded above the floor and promotes it over S5, then S3.
That is the downgrade unit 55 exists to close, on the default policy.

## 2. Scope (IN)

- **S1** — The stop. `derive_pick_stop(E, root)` in `tools/integrations/release.py` returns the newest
  SHA on the first-parent line carrying any `release` record for E, whatever the outcome, or `None`.
  Observed by AC1, AC2.
- **S2** — The walk. `run_release_pick` walks from the tip and stops at S1's SHA, exclusive, so only a
  SHA newer than E's newest record is a candidate. Observed by AC1.
- **S3** — The floor's one use. `derive_pick_floor` stays as the reader of E's last verified SHA for
  unit 15 S10's `rollback-and-ask`, and the walk reads it no longer. Observed by AC3.

## 3. Non-goals (OUT)

- The operator's view of a frozen E and the new-environment case: DEPL-dShippedRelease-91.
- What each outcome routes to: unit 15's `release.route` stands.
- A wider release-fixture rule: the audit's left-shift item is this unit's own case.

### Edges

- **consumes-from** `DEPL-dShippedRelease-55` — `derive_pick_floor`, the walk and the table this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-15` — `run_release_pick` and the `release` record
- **hands-off** `DEPL-dShippedRelease-91` — `derive_pick_stop`, whose frozen state that unit prints

## 4. Design

### Evidence

- Unit 55 §4 "How an outcome counts" lets only `verified` set the floor, and unit 15 S10's `roll-forward` ends `rolled-forward` with no rollback.
- `tools/policy/catalogue.toml:1030` sets `default = "roll-forward"` on `deploy.on-verify-fail`.
- Unit 55 AC2 plants the failed SHA directly above the verified one, so it cannot see an unrecorded SHA beneath the record.

### How an outcome counts

| Outcome | E lacks the SHA | Stops the walk | Read by `derive_pick_floor` |
|---|---|---|---|
| no record | yes, above the stop | no | no |
| `verified` | no | yes | yes |
| `held` | no | yes | no |
| `rolled-forward` | no | yes | no |
| `rolled-back` | no | yes | no |
| `halted` | no | yes | no |
| `unverified` | no | yes | no |

### Supersedes

- Unit 55 S1 as the walk's input, S2, S3's "one tick's decision" sentence, S4's "no floor" and its §4 table: the table above.
- Unit 55 AC1, AC2 and AC3 stand; each still answers as written under the stop.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_pick_stop` | function, `tools/integrations/release.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/integrations/release.py`: S1, S2, S3
- `tools/integrations/release_fixture.py`: the plants of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — the walk stops at E's newest record, so a long history costs what the landings since it cost.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a SHA that failed verify freezes E until a later landing; a downgrade is the alternative, and DEPL-dShippedRelease-91 prints the frozen state.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python release_fixture.py --case pick-stop` plants each of `rolled-forward`,
  `unverified`, `held` and `rolled-back` on the newest of four green SHAs, with two unrecorded SHAs
  below it and above a `verified` one, each next tick prints `nothing` and runs no `promote`.
  Red when: the tick promotes an unrecorded SHA beneath a recorded one, the downgrade on the default
  policy.
- **AC2** — When the same case runs with no `verified` record for E, each next tick prints `nothing`.
  Red when: an environment with no floor walks down history, one SHA per tick.
- **AC3** — When `--case rollback-floor` runs `rollback-and-ask` with a `rolled-forward` record above
  a `verified` one, `rollback` names the `verified` SHA.
  Red when: the stop replaced the floor where a last good SHA is the question.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/release_fixture.py · covers AC1 AC2 AC3 · `pick-stop`, its failing case the walk stopping at the verified floor · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 86 (BLOCKER, item B4) of the round-2 spec audit.

## 10. Reuse audit

The seam extended is `run_release_pick` (unit 15 S6) and unit 55's walk, in `tools/integrations/release.py`.
`python tools/codebase-map/reuse_lookup.py "stop a release walk at the newest recorded sha for an environment"`
ranked name-stem helpers (`records`, `walk`, `extract_records`, `read_records`) and no release reader,
since `release.py` is specced and unbuilt, so no seam fits outside it. The recall probe surfaced unit
55 and report item B4, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does release pick stop on a sha with any outcome" --terms "release pick record environment outcome verified rolled-forward held floor superseded walk downgrade"`

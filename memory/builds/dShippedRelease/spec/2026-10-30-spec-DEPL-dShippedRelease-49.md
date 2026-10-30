# DEPL-dShippedRelease-49 — `read_parent_state` reads `landed` only for a parent whose units shipped

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 6 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 28 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, which shares item B1 with id 70 (DEPL-dShippedRelease-50). Unit 11 §4 reads `landed` on
`phase: LANDING` or a rotated `RUN.LANDED.<hash>.md`, first match wins. This chain lands each build
twice, a spec run and then a build run, so parents whose every unit is unbuilt read `landed`,
`run_deploy_parents` answers `land`, and a dependent lands ahead of a product that does not exist.
This unit keys `landed` on the one tree fact that says units shipped.

## 2. Scope (IN)

- **S1** — The landed test, `test_parent_landed(slug, tip, root)` in `tools/loop/deploy_items.py`.
  It reads the parent's README at the advertised tip and is true only when the generated line reads
  `**Build status:** CLOSED` and the `gen:build-units` region holds at least one row whose Status is
  `CLOSED`. Observed by AC1, AC2.
- **S2** — The `landed` row of unit 11 §4 "The state read" reads S1 alone. `read_parent_state` reads
  neither a `phase:` fact nor a `RUN.LANDED.<hash>.md` file for this state: a landing of a spec run
  is no evidence that a parent's product exists. Observed by AC2.
- **S3** — AC1 of unit 11 is restated here: its `parent-landed` plant holds
  `**Build status:** CLOSED`, and a rotated record with no such line answers no `landed`. Observed
  by AC1, AC3.
- **S4** — The tree fixture. `--plant parents-at-head` runs `read_parent_state` over every slug a
  planted README's `parents:` names and fails on any `landed` beside `**Build status:** DEFERRED`.
  Observed by AC3.

## 3. Non-goals (OUT)

- What a parent that is not `landed` then reads, and the `withdrawn` row: DEPL-dShippedRelease-50,
  the other half of item B1.
- Reading the landing record: unit 11 §8 F1 keeps this read off unit 1's ref, and this unit keeps
  that.

### Edges

- **consumes-from** `DEPL-dShippedRelease-11` — `read_parent_state` and its first-match table, without which there is no row to key
- **hands-off** `DEPL-dShippedRelease-50` — `test_parent_landed`, the row tested before the `held` and `withdrawn` rows that unit settles

## 4. Design

### Evidence

- Unit 11 §4 "The state read" states the row this unit moves; S3 answers `land` when every parent is
  `landed`.
- `tools/memory-tree/gen_build_index.py:1531` renders `**Build status:** {build['status']}`, so the line is
  generated, and `git grep` over `memory/builds/*/README.md` printed 147 CLOSED and 20 DEFERRED at base,
  PINNED at `f4597719`.
- `memory/builds/dWitnessedBar/README.md:98` reads `**Build status:** DEFERRED` with `phase: LANDING` at
  `memory/builds/dWitnessedBar/RUN.md:19`, the shape report item B1 names.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_parent_landed` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S4
- `help/loop.md`: the `landed` test, one sentence

### Alternatives rejected

- **A landing commit on the tip**, unit 11's first reading: a spec run's landing commit is on the
  tip too, so the test cannot tell a spec run from a build run. Rejected by the probe of §4's two
  lines.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a parent closed by retiring every unit has no `CLOSED` row and reads as not landed, the
  safe direction; `withdrawn` is the route for it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/loop.md` gains one sentence.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant parent-landed` runs over a bare remote
  whose tip holds a README reading `**Build status:** CLOSED` with one `CLOSED` unit row,
  `read_parent_state` answers `landed`; a tip holding `RUN.LANDED.abc.md` and no such line does not
  answer `landed`.
  Red when: a rotated record alone reads `landed`, so a parent with no shipped unit admits its
  dependent.
- **AC2** — When `--plant parent-spec-run-landed` runs, a tip whose run record reads
  `phase: LANDING` and whose README reads `**Build status:** DEFERRED`, `read_parent_state` does not
  answer `landed`.
  Red when: the first-match table still reads the run record, the case report item B1 measured on
  parents of this chain.
- **AC3** — When `--plant parents-at-head` runs over a planted README naming one CLOSED and one
  DEFERRED parent, it exits 0 and prints one `landed` and one line that is not `landed`; with the
  DEFERRED parent's test forced true it exits 1.
  Red when: a `landed` beside `**Build status:** DEFERRED` passes, so the left-shift case cannot
  fail.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 · the plants of §6, its failing case `test_parent_landed` reading `phase: LANDING` · none

## 8. Open questions

- **F1 — What says a parent shipped?** Options: (a) the generated `**Build status:** CLOSED` with a
  `CLOSED` unit row; (b) the landing record of a run that built units; (c) a count of non-terminal
  roster rows. (b) reads a ref unit 1 writes, which unit 11 §8 F1 refused, and (c) restates the
  rollup the generator already derives. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, one
  generated fact and no second reader of it. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 28 (BLOCKER, item B1) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-11's `read_parent_state`, whose table this unit re-keys.
`python tools/codebase-map/reuse_lookup.py "decide whether a parent build landed from its build status and run record"`
ranked name-stem helpers (`run`, `build`, `records`, `build_commit`) and no function reading a
build's state, so the read stays where unit 11 put it. The generated status line is the rendered
output of `tools/memory-tree/gen_build_index.py:1531`, read as a tree fact. The recall probe
surfaced report item B1 and the carry-forward ask TOOL-dBoundRoles-27, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a dependent read that its parent build landed when a spec run closes by carry-forward" --terms "parent landed build status DEFERRED carry-forward RUN.LANDED phase LANDING spec run build run"`

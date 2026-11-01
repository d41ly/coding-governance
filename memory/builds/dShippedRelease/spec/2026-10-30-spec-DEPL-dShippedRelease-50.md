# DEPL-dShippedRelease-50 — a carried parent reads `held`, only a terminal disposition reads `withdrawn`, and a spec-run landing is exempt from the hold

**Status:** OPEN · rev-3 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 6 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-49 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-53 DEPL-dShippedRelease-56 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-60 DEPL-dShippedRelease-73 DEPL-dShippedRelease-55 DEPL-dShippedRelease-77 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-76 DEPL-dShippedRelease-75 DEPL-dShippedRelease-67 DEPL-dShippedRelease-54 DEPL-dShippedRelease-57 DEPL-dShippedRelease-74 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 70 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, which shares item B1 with id 28 (DEPL-dShippedRelease-49). Unit 11's `withdrawn` row names
`deferred`, a terminal triage state at flow-steps:737 and :765, while `**Build status:** DEFERRED`
on a carry-forward close means units wait for a build run. A carried parent must read `held`, and a
rotated `RUN.LANDED` beside a live build run must read `held` too. The child's own spec-run landing
has no answer yet, so this unit states it.

## 2. Scope (IN)

- **S1** — The `withdrawn` row of unit 11 §4 reads a terminal disposition only:
  `read_withdrawn_parents` names the slug, the tip's run record reads `phase: ABORTED`, or the state
  is one of flow-steps:436's other terminal words. `**Build status:** DEFERRED` is no such
  disposition, so a carried parent falls through to `held`. Observed by AC1, AC2.
- **S2** — The plants. `parent-deferred` of unit 11's AC3 is the terminal case, a run record reading
  `phase: ABORTED`. `parent-spec-run-landed` is `phase: LANDING` with `**Build status:** DEFERRED`,
  answering `held`. `parent-rotated-then-building` is `RUN.LANDED.<hash>.md` with a live `RUN.md`,
  answering `held`. Observed by AC1, AC2.
- **S3** — A spec-run landing is exempt. `test_spec_run_landing(build, root)` is true when every row
  of the landing build's own `gen:build-units` region reads `DEFERRED`. `run_deploy_parents` then
  exits 0 and prints `deploy.parents — land · spec run · 0 unit(s) built`, under each `deps.landing`
  value, since a landing of specs alone carries none of a parent's unlanded product. Observed by
  AC3.

## 3. Non-goals (OUT)

- The `landed` test: DEPL-dShippedRelease-49.
- `deps.on-parent-withdrawn`'s values: TOOL-dDeclaredLoop-15.

### Edges

- **consumes-from** `DEPL-dShippedRelease-11` — the `withdrawn` row, `run_deploy_parents` and the plants this unit restates
- **consumes-from** `DEPL-dShippedRelease-49` — `test_parent_landed`, tested ahead of this unit's rows; without it a carried parent never reaches them
- **hands-off** `DEPL-dShippedRelease-81` — `test_spec_run_landing`, which that unit carries to the queue (review id 2)
- **hands-off** `DEPL-dShippedRelease-82` — the exemption of S3, which that unit observes through to the push (review id 87)
- **hands-off** `DEPL-dShippedRelease-106` — the text and code which the round-2 minors batch repairs (review ids 32, 41, 43, 50, 51, 99, 100)
- **hands-off** `DEPL-dShippedRelease-69` — `read_build_rows` and the spec-run rule, beside which that unit's carry-forward read stays apart (review id 50)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 9)

## 4. Design

### Evidence

- Unit 11 §4 lists `deferred` beside `retired`, `refused` and `answered` as a terminal state, and its AC3 answers
  `withdrawn` on `parent-deferred`; report id 70 records why testing `deferred` first answers the wrong state.
- README rule 1 of this build makes a spec run close by carry-forward with every unit DEFERRED, so a dependent's spec
  run would otherwise wait for parents that its own chain builds later.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_spec_run_landing` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `help/loop.md`: the three readings and the spec-run exemption

### Alternatives rejected

- **A carried test ahead of `withdrawn`.** The audit's first fix tests `deferred` first and answers
  `withdrawn`, which its own plant refutes; narrowing the row needs no new test.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a build that defers every unit late in a build run passes as a spec run; its landing then
  carries only what its units already landed, and it holds nothing a parent owns.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/loop.md` states the three readings and the exemption.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant parent-spec-run-landed` runs,
  `read_parent_state` answers `held`; when `--plant parent-rotated-then-building` runs it answers
  `held`.
  Red when: a carried parent reads `withdrawn` and routes, or a rotated record reads `landed` beside
  a live build run.
- **AC2** — When `--plant parent-deferred` runs, a run record reading `phase: ABORTED`, it answers
  `withdrawn`, and the verb exits 4.
  Red when: a terminal disposition holds for ever.
- **AC3** — When `python deploy_items.py parents --build fx` runs on a build whose units all read
  `DEFERRED`, beside a parent reading `held`, it exits 0 and prints `spec run`; with one unit
  `CLOSED` it exits 3.
  Red when: a spec-run landing is held on an unbuilt parent, or a built unit passes under the
  exemption.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 · the plants of §6, its failing case `deferred` tested as `withdrawn` · none

## 8. Open questions

- **F1 — Is a child's spec-run landing held on an unbuilt parent?** Options: (a) exempt, since it
  carries specs and no product; (b) held, as any landing. (b) stops every spec run of this chain
  until its parents are built, and the build order needs those specs first. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3, the option that leaves the chain able to land. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 70 (BLOCKER, item B1) of the round-1 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-2 spec audit's promoted units declare toward this unit (units 69, 81, 82, 106); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

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

# DEPL-dShippedRelease-82 — A spec run lands past an unbuilt parent end to end, its rows read after the defer flip

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 7 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 87 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B2 with id 2
(DEPL-dShippedRelease-81). Unit 12 S6 runs `check_landing_admitted` first and exits 5 on 3, and unit
50's AC3 reads only `parents --build fx`, so an exempt spec run passes `deploy.parents` and still
cannot land while its criterion reads green. Unit 4's order also walks `--to-land` before `--close`,
and no spec says when the rows the exemption reads turn DEFERRED. This unit fixes that moment and
observes the push.

## 2. Scope (IN)

- **S1** — The moment. `test_spec_run_landing` reads the `gen:build-units` region at the build's HEAD
  when it is called. A spec run flips its units DEFERRED and renders the region before
  `--deploy run <slug> --to-land`, and `tools/unattended/VERBS.template.md` states that. A walk ahead
  of the flip answers `awaiting`, exit 3, and a re-walk after the flip passes, so the wrong order
  holds and never lands. Observed by AC2.
- **S2** — The entry follows the flip. `write_queue_entry` runs at `deploy.land`, after `--close`, so
  `parents-admit` is written from flipped rows; an entry written before the flip gives way to a new
  tree's entry, as unit 12 S1 appends one. Observed by AC3.
- **S3** — The end-to-end case. `--case engine-spec-run-land` lands an all-DEFERRED build with a `held`
  parent from `deploy.parents` through `run_deploy_land` and the lander, and asserts the remote's tip
  holds the SHA. Observed by AC1.

## 3. Non-goals (OUT)

- The queue's key and skip: DEPL-dShippedRelease-81, the other half of item B2.
- A checklist item for every exemption's readers: the audit's left-shift item, which no clause of
  this build names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-81` — `test_parents_admit` and `parents-admit`, the exemption this unit walks to the push
- **consumes-from** `DEPL-dShippedRelease-12` — `check_landing_admitted`, `run_deploy_land` and S6's lander call
- **consumes-from** `DEPL-dShippedRelease-50` — AC3's exemption, which this unit observes past `deploy.parents`
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 9, 55)

## 4. Design

### Evidence

- Unit 12 S6 runs `check_landing_admitted` first; unit 12 S9 is enqueue, admit, land (report id 87).
- Unit 4 S15's order, as DEPL-dShippedRelease-58 S3 restates it: `--deploy run <slug> --to-land`, `--close`, `--deploy land <slug>`, `--landed`, `--deploy run <slug>`.
- README rule 1 of this build: a spec run specs, audits and defers every unit, and closes by carry-forward.

### Supersedes

- Unit 50 §5's risk line reads with S1 here: the rows are read at the build's HEAD, after the flip.
- Unit 50 AC3 stands; it observes the verb, and AC1 here observes the landing.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1
- `tools/loop/deploy_fixture.py`: S3's case
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: S1's sentence

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a run that flips late pays one held walk; that is the safe direction, and the line it prints names the flip.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `memory/guides/UNATTENDED-VERBS.md` states the flip's place, through its template.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-spec-run-land` lands an all-DEFERRED build
  with a `held` parent, `git ls-remote` on the fixture's bare remote prints the SHA on the default
  branch, and the outcome record reads a landed class.
  Red when: a spec run passes `deploy.parents` and the lander exits 5 for ever.
  fixture: the stub bar is unit 4's, order 10, so the main loop observes this case at the close.
- **AC2** — When the case's `--to-land` runs with one row still `OPEN`, `deploy.parents` exits 3
  printing `awaiting`; after the flip and the render the same walk exits 0.
  Red when: the rows are read before the flip with no hold, or a flipped build stays held.
- **AC3** — When `--case engine-spec-run-reentry` enqueues before the flip and again after it,
  `derive_landing_queue` reads the later entry's `parents-admit: yes`.
  Red when: a stale `no` strands the run behind its own earlier entry.

## 7. Gates

`recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `engine-spec-run-land`, its failing case a `held` parent with `parents-admit` written `no` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 87 (BLOCKER, item B2) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `run_deploy_land` and `check_landing_admitted` (unit 12 S3, S9), and the case joins `deploy_fixture.py`.
`python tools/codebase-map/reuse_lookup.py "skip a queue entry while a parent build has not landed"`
ranked name-stem helpers (`note`, `build`, `has`, `skip`) and no admission path, because `tools/loop/`
is specced and unbuilt. A read of the method found `check_spec_run`
(`tools/unattended/unattended.sh:5152`) as the run-side test, which review id 50 takes up in the minors
batch. The recall probe surfaced scout B's row and report item B2, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the landing queue treat a spec run with an unbuilt parent" --terms "landing queue parent skip spec run exemption deps.landing derive_landing_queue admit carry-forward DEFERRED held"`

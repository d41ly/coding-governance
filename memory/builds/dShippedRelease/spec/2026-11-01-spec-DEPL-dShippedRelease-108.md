# DEPL-dShippedRelease-108 — `run_deploy_items` runs `--deploy review` at one fixed step, so a default landing reaches `not-placed`

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, BLOCKER, item B1.
Unit 14 S6 runs the verb only before the item a `derive_breakpoints` row's `position` names, and
`opt-in`, the catalogue default, places no row. So the `not-placed` write in `run_deploy_review` is
unreachable from `run_deploy_items`, `review` stays `unfired`, and every landing at the default holds at
`deploy.close`. Unit 80's AC1 stays green because its fixture calls the verb directly. This unit gives
the walk one unconditional step and proves the default through the real walk.

## 2. Scope (IN)

- **S1** — The step. `run_deploy_items` runs `--deploy review <slug> <sha>` immediately before
  `item.deploy.notify`, whatever `review.deploy` reads, and reads no `derive_breakpoints` row itself.
  An exit 0 goes on, and exit 3 or any other non-zero stops the walk with that exit, as unit 4 S1
  states for an item. Observed by AC1, AC2.
- **S2** — One reader of the row. Fire or `not-placed` is decided inside the verb, by unit 80's value
  table. A row whose `position` names another item still fires at this step, so no second place holds
  a review. Observed by AC1, AC2.
- **S3** — The leg before the landing. `--deploy run <slug> --to-land` stops ahead of
  `item.deploy.land`, so it never reaches the step. Observed by AC3.
- **S4** — The fixture. `--case review-first-walk` runs `--deploy run <slug>` through the real walk and
  then `--deploy close`, with no direct call of `--deploy review`. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The verb's arms: DEPL-dShippedRelease-80 stands.
- A step for any other breakpoint: no clause of this build places one in the deploy walk.
- A checklist item that a criterion for a walk step must run the walk: the audit's left-shift item,
  which no clause of this build names, and S4 is its one instance.

### Edges

- **consumes-from** `DEPL-dShippedRelease-80` — the verb's arms, which decide fire or `not-placed` at this step
- **consumes-from** `DEPL-dShippedRelease-14` — S6's step, whose row condition this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-4` — `run_deploy_items` and its stop rule

## 4. Design

### Evidence

- Unit 14 S6: "before the item a `derive_breakpoints` row's `position` names, it runs the row's verb".
- Unit 14 §8 F3 rests on TOOL-dDeclaredLoop-19, lines 148 to 150, which say `opt-in` places nothing for this stage.
- Unit 4 §4 "The one commit" spells the walk as `core · record · distill · recommend · [landing review] · notify`.
- Unit 79 S3 fails the close on `unfired`, and unit 80 S4 and AC1 call the verb directly (report id 1).

### Supersedes

- Unit 14 S6's row condition: the step runs on every walk that reaches `item.deploy.notify`.
- Unit 14's Rollout line stands, and is true only with this step.
- Unit 14 AC3's last clause stands, now read at this step.
- Unit 80 S4's direct call, and the commands of unit 80 AC1 and AC2: each reads through `--deploy run`.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/loop/deploy_fixture.py`: S4

### Alternatives rejected

- **A planted `landing review` row at the default.** It places a review no policy asked for, and
  unit 14 §8 F3 keeps `not-placed` as the default's own word.
- **Passing `unfired` at the close term.** It reads a landing nobody walked as passed, which unit 79 AC3
  names red.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — one `read_landing` per walk, on a path that already runs once per landing.
- error / empty / loading states — unit 80 §4's table states each value, and S1 carries each exit.
- observability — the verb prints its own line on every value, and the walk prints the stop.
- risks — a walk stopped at this step under `owed` holds `deploy.notify`, as unit 14 §8 F5 chose.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — `help/deploy.md` already states when a landing review runs (unit 14 S7).

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-first-walk` runs `--deploy run <slug>` at the
  catalogue default with no direct call of the verb, `read-landing` prints
  `review<TAB>not-placed · review.deploy=opt-in`, `--deploy close` prints `not placed` and records its
  transition, and the stub's log holds no `--trigger`.
  Red when: the step is keyed on a `derive_breakpoints` row, so `review` stays `unfired` and the close
  holds.
- **AC2** — When the same case runs under `review.deploy = "owed"`, `--deploy run` exits 3 with
  `item.deploy.notify` unrun, and the stub's log holds one `--trigger`.
  Red when: the walk passes the review, or fires it after the notice.
- **AC3** — When `--deploy run <slug> --to-land` runs in that case, the stub's log holds no
  `--deploy review` line.
  Red when: the step runs ahead of the landing, with no landing record to read.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `review-first-walk`, its failing case the step keyed on a `derive_breakpoints` row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 1 (BLOCKER, item B1) of the round-3 spec audit.

## 10. Reuse audit

The seam extended is `run_deploy_items` (unit 4 S1), with the arms of `run_deploy_review` (unit 80).
`python tools/codebase-map/reuse_lookup.py "run a verb at a fixed step of an ordered walk regardless of policy"`
ranked the name-stem helper `run` and no walker of items, because `tools/loop/` is specced and unbuilt,
so no existing seam fits outside the parent's own module. The recall probe surfaced units 14, 1 and 79,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "does the deploy walk call the landing review at the default policy" --terms "landing review breakpoint run_deploy_items opt-in not-placed walk deploy.recommend deploy.notify derive_breakpoints"`

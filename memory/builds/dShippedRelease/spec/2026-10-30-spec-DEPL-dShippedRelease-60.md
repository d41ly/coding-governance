# DEPL-dShippedRelease-60 — `--deploy review` reads its own field first, so a re-walk neither re-fires nor overwrites a disposal

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 4 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`, HIGH,
item H5, which stands beside id 83. Unit 14 S1 reads no current field: a placed row always fires
`--trigger`, sets `review` to `pending` and exits 3. Unit 4 S1 resumes by re-running every item, so
after `dispose-landing` the walk overwrites `disposed` with `pending` and holds again. A landing
under `review.deploy = owed` can never pass.

## 2. Scope (IN)

- **S1** — S1 of unit 14 gains a first step. `run_deploy_review` reads the `review` field through
  `read_landing`. `disposed · …` and `not-placed · …` print the value and exit 0 with no
  `--trigger`. `pending` prints the pin and exits 3 with no `--trigger`. Only `pending` reached by
  this verb's own write proves a fired trigger: the write follows `--trigger`'s exit 0. Observed by
  AC1, AC2.
- **S2** — The whole cycle is one fixture: exit 3, `dispose-landing`, `--deploy run` reaches
  `deploy.close`, and the field still reads `disposed`. Observed by AC1.

## 3. Non-goals (OUT)

- What the close term believes of the field: DEPL-dShippedRelease-73.
- Idempotence of the other items: unit 4 S1's claim stands for them.

### Edges

- **consumes-from** `DEPL-dShippedRelease-14` — `run_deploy_review`, `dispose-landing` and the field's values
- **hands-off** `DEPL-dShippedRelease-78` — the `pending` arm of S1, which that unit re-reads for review id 83

## 4. Design

### Evidence

- Unit 14 S1 has two arms, no row and a row that fires; S4 is the only idempotence the spec states.
- Unit 4 S1: every item is idempotent, so a re-run or a second node's run resumes by re-running.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1
- `tools/loop/deploy_fixture.py`: the case of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a kill between `--trigger` and the write fires a second trigger on the re-run; the harness
  reads one subject and one report, so it costs a duplicate run.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-rewalk` runs a placed review to exit 3,
  disposes it and re-runs `--deploy run`, the walk reaches `deploy.close`, and `read-landing` still
  prints `review<TAB>disposed`, with one `--trigger` in the stub's log.
  Red when: the re-walk overwrites `disposed`, so `deploy.close` holds for ever.
- **AC2** — When `--deploy review` runs twice with no disposal, the second run exits 3 and the
  stub's log holds one `--trigger`.
  Red when: every walk fires another review.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · `review-rewalk`, its failing case the first step cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 4 (HIGH, item H5) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`

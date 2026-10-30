# DEPL-dShippedRelease-72 — only an admission exit 0 lands, and every other exit stops with nothing pushed

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 7 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 78 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H16. Unit 12 S3 defines exits 0 and 3 and S6 says exit 5 on 3, while unit 11's AC12 exits
2 on an invalid policy value and a traceback exits 1. Its §4 reads fail-closed and conflicts with
S6's exact rule, and AC9's `unreachable` has no producer before admission. So a dead remote, a
refused policy read or a crash lands past the queue and past an `owner-orders` hold, with only the
turn left to guard.

## 2. Scope (IN)

- **S1** — The lander. S6's rule is inverted: only exit 0 from `check_landing_admitted` admits. Exit
  3 stops as `held`, exit 5. Exit 4 stops as `unreachable`, exit 1. Exit 2 and every other exit stop
  as `refused`, exit 1, naming the exit. Each writes its outcome record and pushes nothing. S6's
  three skip paths keep running before admission. Observed by AC1, AC2.
- **S2** — `admit`. S3 gains exit 2, a refused read naming the key, and exit 4, an unreachable
  remote. Observed by AC2.

## 3. Non-goals (OUT)

- The records-only arm: DEPL-dShippedRelease-59.
- The turn: unit 12 S4 stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-12` — S3, S6 and the class table, and the lander's admission call

## 4. Design

### Evidence

- Unit 12 S6 prints `no landing turn` on three skip paths, and §4 "The turn, in order" reads `check_landing_admitted → exit 5 if not`.
- Unit 11 AC12 and `run_deploy_parents` exit 2 on a refused read.

### Files touched (estimate)

- `tools/push-main.sh`: S1
- `tools/push-main.test.sh`: the arm of §7
- `tools/loop/deploy_items.py`: S2

## 5. Production-readiness checklist

- security — deny by default: the lander lands only on a positive answer.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a broken loop kit stops landings on that node until repaired; each exit names itself, and
  `no landing turn` still covers a kit that is absent.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — the lander's header states the exits; unit 12's `help/loop.md` lists the
  classes, unchanged.

## 6. Acceptance criteria

- **AC1** — When `bash tools/push-main.sh --land --slug fx` runs with `admit` stubbed to exit 1, and
  again to exit 2, it exits 1 naming the exit, and the remote's tip does not move.
  Red when: a crash in admission lands past the queue.
- **AC2** — When `python deploy_items.py admit --slug fx` runs under a committed
  `landing.order = "nonsense"` it exits 2 naming the key, and against a dead remote it exits 4.
  Red when: a refused read or a dead remote reads as admitted or as held.
- **AC3** — When the stub exits 3, the lander exits 5 with outcome `held`.
  Red when: inverting the rule lost the held answer.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/push-main.test.sh · covers AC1 AC3 · a stubbed `deploy_items.py` beside the lander, its failing case `exit 5 on 3` alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 78 (HIGH, item H16) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-12's outcome and queue code.
`python tools/codebase-map/reuse_lookup.py "append an entry to a ref chain and skip or tombstone an entry"`
ranked name-stem helpers (`skip`, `build_self_chain`, `resolve_entry`, `read_chain_clauses`) and no
ref-held queue, since unit 12's is specced and unbuilt, so no existing seam fits outside it. The
recall probe surfaced scout B's queue row and report item H15, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a queue ref let a refused or held head leave so other builds land" --terms "landing queue entry tombstone refused held admission fail closed exit turn lease"`

# DEPL-dShippedRelease-68 — the late records landing passes the lander after the tombstone, from a tree of its own

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 11 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 73 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H12. When the close is not due at the one commit, `deploy.close` lands the transition
copy alone through unit 4 S7's `--land --slug`. By then `deploy.unlease` has tombstoned the build
lease, TOOL-dPlacedRequest-15 S2 answers a terminal lease with a refusal, and S13's wake runs under
a cadence lease with no clean tree on a branch holding the SHA. The red landing,
`after-release-verifies` with `close-only`, and an open review each cannot land their copy, so the
build never finishes closing on its safety paths.

## 2. Scope (IN)

- **S1** — The mode. `$LANDER --land --slug <slug> --records-after-close` skips the build-lease
  fence, printing `none · terminal build`, and takes the turn. The lander refuses it, exit 1 pushing
  nothing, unless `--claims` reads the build lease terminal and `test_records_landing` holds.
  Observed by AC1, AC2.
- **S2** — The tree. `run_late_records_landing <slug> <sha>` in `tools/unattended/unattended.sh`
  makes a detached worktree of the advertised tip under `<git common dir>/gov/close-wake/<slug>`,
  commits the transition's copy on a branch `records/<slug>`, runs `--prepare --slug` and that
  landing, and takes the worktree away. The session's own tree is not read, so a wake's clean-tree
  exit 2 cannot arise. Observed by AC1.
- **S3** — The route. `run_deploy_close` calls S2 when its copy is not on the default branch and the
  build lease is terminal; exit 5 holds as `records — held · landing turn`, exit 3, and the wake
  re-declares. Observed by AC1, AC3.

## 3. Non-goals (OUT)

- The first records landing: unit 4 S7 and DEPL-dShippedRelease-59.
- TOOL-dPlacedRequest-15's fence: read, not changed.

### Edges

- **consumes-from** `DEPL-dShippedRelease-4` — `run_deploy_close`, S7, S13's wake and the tombstone of S8
- **consumes-from** `DEPL-dShippedRelease-59` — `test_records_landing`, the one test of a records-only tree

## 4. Design

### Evidence

- Unit 4 §4 "The one commit" names this as the one case of a second records commit, deviation 42; S13 says the build holds no lease by then.
- TOOL-dPlacedRequest-15 S2 and S3: a terminal lease answers the refusal line, and `--land --slug` on `refused` exits 1 and pushes nothing (report id 73).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `run_late_records_landing` | function, `tools/unattended/unattended.sh` | `sh.function`, OK by `--suggest` at writing |
| `--records-after-close` | lander flag | none |

### Files touched (estimate)

- `tools/push-main.sh`: S1
- `tools/push-main.test.sh`: the refusal arm
- `tools/unattended/unattended.sh`: S2
- `tools/loop/deploy_items.py`: S3
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — the mode is admitted only by the lease's terminal state and a records-only range, both
  read at the moment of the landing.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — a dead worktree add exits 2 naming the path, and the wake
  re-declares.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `memory/guides/UNATTENDED-VERBS.md`, rendered from its template, gains the mode; the
  render is unit 4's file.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-late-close` runs an unlease and then a
  close due later, the transition's copy reaches the default branch and `deploy.close` records T10.
  Red when: a safety path can never land its copy, so the build never closes.
- **AC2** — When `bash tools/push-main.sh --land --slug fx --records-after-close` runs with a
  product change in the range, or with the lease live, it exits 1 and the remote's tip does not
  move.
  Red when: the mode lands product past the fence.
- **AC3** — When a planted lander exits 5 in `--case engine-late-close-held`, `--deploy close` exits
  3 printing `records — held`.
  Red when: a held turn reads as a closed build.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC3 · `engine-late-close`, its failing case the plain `--land --slug` · none

New arm: tools/push-main.test.sh · covers AC2 · a product file in the range, its failing case the records test cut out · none

## 8. Open questions

- **F1 — How does a copy land after the tombstone?** Options: (a) a lander mode that skips the build
  fence on a terminal lease, for a records-only tree; (b) land under the cadence lease with no
  `--slug`. (b) takes no turn, so it races every other landing. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 73 (HIGH, item H12) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`

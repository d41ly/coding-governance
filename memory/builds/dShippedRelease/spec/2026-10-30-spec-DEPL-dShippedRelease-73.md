# DEPL-dShippedRelease-73 — `check_landing_review` re-derives its pass from sources the field does not control

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 82 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H17. Unit 14 S2 passes any `disposed · …` or `not-placed · …` value by its text, unit 1
S6 lets any session set `review` through `--deploy field`, and AC2 itself plants a disposed field as
the pass. A build under `review.deploy = owed` can write its own pass and close with no review.

## 2. Scope (IN)

- **S1** — `not-placed`. `check_review_field(sha, value, root)` in `tools/loop/deploy_items.py`
  passes a `not-placed · …` value only when `derive_breakpoints` still returns no `landing review`
  row for the landing. Observed by AC1.
- **S2** — `disposed`. It passes a `disposed · <n> finding(s) · <report path>` value only when
  `git cat-file -e <advertised tip>:<report path>` finds the report on the default branch and that
  blob holds a `## Verdict` line. Observed by AC2.
- **S3** — Any other reading holds, printing `held · check_landing_review · forged`.
  `check_landing_review` calls S1 and S2 and adds no rule. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The field's own write: unit 1 S6 stands; the term is what stops trusting it.
- A signature over the field: §8 F1.

### Edges

- **consumes-from** `DEPL-dShippedRelease-14` — `check_landing_review` and S5, the records landing that puts the report on the default branch

## 4. Design

### Evidence

- Unit 14 S5 lands the review record with the records landing, so an honest report is on the default branch before the close term reads it (report id 82).
- Unit 14 S2 names a forged or absent field as held, and AC2's plant is the disposed value itself.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_review_field` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — the term's inputs now sit outside the reviewed session's reach: the tip's tree and the
  policy at the landing.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a report edited on the default branch to add a `## Verdict` line would pass; that edit
  lands through the lander, gated.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-forged-not-placed` sets `not-placed · x`
  under `review.deploy = "owed"`, `--deploy close` exits 3 printing `forged`.
  Red when: a build writes its own pass under `owed`.
- **AC2** — When `--case review-forged-disposed` sets `disposed · 0 finding(s) · <no such report>`,
  `--deploy close` exits 3 printing `forged`; with the report on the tip and a `## Verdict` line it
  passes.
  Red when: a disposal naming no report closes the build, or an honest one holds.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · both forged cases, their failing case the value read by its prefix · none

## 8. Open questions

- **F1 — How is the field checked?** Options: (a) re-derive from the breakpoints and the default
  branch; (b) sign the field. (b) needs a key the session under review does not hold, and a mandate
  owns no such key. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 82 (HIGH, item H17) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`

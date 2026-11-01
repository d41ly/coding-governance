# TOOL-dIndexedDesign-39 — unit 35's coverage stage lands inside unit 16's pass, so no commit of the build holds a six-entry `SPEC_LENSES`

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 5 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-39-deviation-391.md](../build/2026-10-28-build-TOOL-dIndexedDesign-39-deviation-391.md) | deviation | — |
| [2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**, the item's only id.
`TOOL-dIndexedDesign-16` S8 (order 3) adds a sixth `coverage` entry to `SPEC_LENSES` and re-renders
`tools/workflows/tier2-review.js`. The unguarded `verifier fan-out` leg (`tools/gate-legs.json:1595-1603`)
feeds every committed harness exporting `meta` to `tools/hooks/agent-cap.js`, which admits a lens
receiver only up to `MAX_LENSES = 5` (`agent-cap.js:461`, `:929`). `TOOL-dIndexedDesign-35` removes the
sixth entry, but at order 4, one pass after the commit that adds it. Its Rollout and
`TOOL-dIndexedDesign-38` §8 F1 both rest on that six-lens state having landed.

This unit carries the skeptic's corrected fix. Unit 35's S1 to S4 are built inside unit 16's own pass
commit, so the commit that adds the `coverage` argument also adds the coverage stage, and no commit of
this build holds six spec lenses. Its own pass, at order 5, observes every commit of the build against
the hook. It repairs `TOOL-dIndexedDesign-35` and takes order 5, one above unit 35's 4.

## 2. Scope (IN)

- **S1** — The co-landing, an act ahead of this unit's order. Unit 16's pass commit carries unit 35's S1
  to S4 beside unit 16's S8: `COVERAGE_BRIEF`, `phase('Coverage')`, the `only` mode's skipped lenses and
  the share rule. Unit 16 S8's brief is written straight into `COVERAGE_BRIEF`, and no
  `key: 'coverage'` entry is ever written to `SPEC_LENSES`. The pass's `--dispatch` row already declares
  the three workflow files, which unit 16's Files touched names. Its commit subject names
  `TOOL-dIndexedDesign-16` and this unit's id. Observed by AC1 and AC3.
- **S2** — Unit 35's own pass, at order 4, builds only what S1 left to it: its S5 and the observation of
  its AC1 to AC4. It rewrites none of S1 to S4. Observed by AC3.
- **S3** — The window restated. From unit 16's pass tip on, the rendered harness is admitted, so the window
  unit 35's Rollout and unit 38 §8 F1 describe is only the lack of a `coverage-lens` reading. It is not a
  denied harness. Unit 35's acceptance ledger carries the note `TOOL-dIndexedDesign-39 S3` under its AC1
  answer, naming `check-verifier-fanout.sh`. Observed by AC4.
- **S4** — The proof. At this unit's pass, every commit of the build that changes the rendered harness is
  fed to the hook through the leg's own script, and a staged six-entry copy is fed beside them to show
  the probe can fail. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- `MAX_LENSES` and the hook's rules: unchanged. Raising the bound is an owner turn (M3 veto 3).
- Unit 35's stage design, unit 16's argument and binding: their specs. This unit moves when unit 35's
  S1 to S4 land, and nothing else.
- The coverage stage's bookkeeping: `TOOL-dIndexedDesign-44`, report id 26.
- Unit 35's S5 arm and the leg's denied-half fixture: report ids 7 and 20, LOW, batched into
  `TOOL-dIndexedDesign-46`.
- How the run passes the reading window: `TOOL-dIndexedDesign-38` §8 F1, the owner's. S3 corrects its
  premise only.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — S8's `coverage` argument and brief, in whose pass commit S1 lands unit 35's stage (id 1)
- **consumes-from** `TOOL-dIndexedDesign-35` — its S1 to S4, which S1 builds inside unit 16's pass, and its S5 and criteria, which its own pass keeps (id 1)
- **hands-off** `TOOL-dIndexedDesign-38` — its §8 F1 premise, which S3 restates as the lack of a reading once unit 16's pass tip admits the harness (id 1)
- **hands-off** `TOOL-dIndexedDesign-53` — AC1's commit list, which that unit re-derives at its own pass, the last of the build to change the harness (id 21)

## 4. Design

### Evidence

- `tools/gate-legs.json:1595-1603` holds the `verifier fan-out` leg with no `guard` key, so it runs on
  every bar. `tools/workflows/check-verifier-fanout.sh:172-179` selects each listed `*.js` exporting
  `meta`, and `:200-205` pipes each to `node agent-cap.js --only=scripts`. Given file arguments it judges
  only those (`:159`, its header's second usage line).
- `tools/hooks/agent-cap.js:461` sets `MAX_LENSES = 5`; `:929` admits a receiver only when
  `topLevelArgs(inner).length <= MAX_LENSES`. Read 2026-10-28.
- BUILD-METHOD M6 runs no bar inside a pass, so the six-lens commit would surface at the close rather
  than at unit 16's pass, as the report's caveat says. S1 removes the state, not just its observation.
- `tools/unattended/unattended.sh:13737-13745` refuses a `--dispatch` whose `consumes-from` producer is
  not CLOSED. This unit's two producers sit at orders 3 and 4, both before its own.

### Inventory

Minted: no identifier. One sequencing act, one ledger note and one recorded probe.

### Migration

None: no commit of this build exists yet.

### Rollout

S1 lands in unit 16's pass, order 3, ahead of this unit's order. Unit 16's Edges block names it, and
that is where its builder reads it. S2 is unit 35's pass, order 4. S3 and S4 are this unit's own pass at
order 5, beside `TOOL-dIndexedDesign-44`, `TOOL-dIndexedDesign-36` and `TOOL-dIndexedDesign-7`. This
unit writes only the ledgers, so its write set meets none of theirs. The leg reads green at every pass
tip from unit 16's on.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.js` its render, and
  `tools/workflows/tier2-review.test.sh`: S1, in unit 16's pass
- `memory/builds/dIndexedDesign/build/`: S3's ledger note and S4's recorded probe

### Alternatives rejected

- **Leave the window, since no bar runs between passes.** Lost to the confirmed finding. The six-lens
  commit stays in history, and the premise of unit 38 F1 stays false.
- **Raise `MAX_LENSES` to 6.** Lost to M3 veto 3: an owner-ratified security bound.
- **Move unit 35 to order 3.** Lost to the build-order region. Units sharing an order are still two
  passes and two commits, so the first can land six entries.

## 5. Production-readiness checklist

- security — keeps the owner-ratified fan-out bound true at every commit.
- perf / scale — none: one probe per harness commit, a handful of node runs.
- error / empty / loading states — AC1 refuses an empty commit list, which would mean S1's commit was
  not found.
- observability — the recorded probe names each commit and its verdict.
- risks — unit 16's builder must read S1 from its Edges block. AC3 reads the commit, so a missed
  co-landing is visible at this unit's pass.
- testing — AC1 to AC4 by `git`, the leg's own script and `grep`. No arm moves.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git log --format=%H <base>..HEAD -- tools/workflows/tier2-review.js` lists the commits
  that change the render, each one's blob is written by `git show` to the run's scratch and passed to
  `bash tools/workflows/check-verifier-fanout.sh <file>`, and every run exits 0. Unit 16's pass commit
  is in the list.
  Red when: a commit's harness is denied, or the list is empty.
  figure: the list is DERIVED from the run's pinned BASE at this unit's pass.
- **AC2** — When a scratch copy of the current render with a sixth `SPEC_LENSES` entry is passed to the
  same `check-verifier-fanout.sh`, it exits 1 and its output names `SPEC_LENSES` as not one of the
  bounded forms, the denial the report's re-probe recorded.
  Red when: the six-entry copy is admitted, so AC1's green measures nothing.
- **AC3** — When `git show <p> -- tools/workflows/tier2-review.template.js` runs at unit 16's pass commit
  `<p>`, it adds `COVERAGE_BRIEF` and `phase('Coverage')`. When
  `git log -S "key: 'coverage'" <base>..HEAD -- tools/workflows/tier2-review.template.js` runs, it prints
  no commit.
  Red when: the stage lands after the argument, or a `coverage` lens entry was ever written.
- **AC4** — When `grep -n "TOOL-dIndexedDesign-39 S3"` runs over unit 35's acceptance ledger, it prints
  the note under AC1's answer, and that line names `check-verifier-fanout.sh`.
  Red when: the note is missing or stands as its own `- AC` line.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `memory hygiene`

## 8. Open questions

- **F1 — How is a co-landing bound, when no order or edge can put two units' items in one commit?**
  Options: (a) S1 as an act ahead of this unit's order, named in unit 16's and unit 35's Edges and this
  Rollout, which unit 16's builder reads, with AC3 reading the commit. (b) A new header verb such as
  `lands-with`, read by `--dispatch`. (c) Leave the two passes and accept one six-lens commit. (b) adds a
  public surface to the driver and a governance carrier, an owner turn (veto 2). (c) leaves the
  confirmed finding open, which the severity rule forbids. RESOLVED (agent, 2026-10-28, delegated): (a),
  rung 3, the one survivor; unit 38 S2 already acts ahead of its order the same way. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 1
  (HIGH, item H1), on the skeptic's corrected fix, repairing TOOL-dIndexedDesign-35's Rollout and the
  premise of TOOL-dIndexedDesign-38 §8 F1.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-53, promoted by the round-1 spec audit of units 39 to 46; nothing else
  moved.

## 10. Reuse audit

The seam is the `verifier fan-out` leg's own script, `tools/workflows/check-verifier-fanout.sh`, given
file arguments. AC1 and AC2 call it, so no second feeder of the hook is written. The probe
`python tools/codebase-map/reuse_lookup.py "land two units' changes in one pass commit so an unguarded leg is never red at a pass tip"`
ranked `legs`, `leg`, `units`, `changed` and `build_commit`. None is a co-landing or sequencing seam,
so no existing seam fits beyond the leg's script and the act-ahead form unit 38 S2 uses. The recall
query also returned ask TOOL-aDeferredBar-14, which has the fold pass run unguarded repo legs before its
commit. That is another build's ask, and nothing here builds it.

Recall terms used: `python tools/memory-recall/query.py "how does a repair land before the pass that breaks an unguarded leg" --terms "repair unit order pass tip unguarded leg verifier fan-out SPEC_LENSES MAX_LENSES coverage stage window"`

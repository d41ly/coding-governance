# TOOL-dCalibratedLens-23 — the instruction-eval seed lands held, and a guarded edit's owed replay is recorded before the close bar

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 13 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-23-deviation-231.md](../build/2026-11-02-build-TOOL-dCalibratedLens-23-deviation-231.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 4, HIGH, item H5 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Unit 10's
`instruction-eval` leg exits 1 whenever a case is `owed`; its S5 lets the seed land with
`**Replayed:** none`, owed by definition, and its AC6 accepts `owed`. The leg is held on the default
push bar, but this repository's unattended close bar exports `GATE_FULL=1 GATE_SELFTESTS=1`
(`memory/guides/UNATTENDED-PROTOCOL.md`, `.unattended.conf` `SELFTESTS_OWED_PATHS="tools/"`), so an
owed seed reds the close. Units 8 and 1 then edit guard paths (`unattended-build.template.js`,
`tier2-review.template.js`, `lenses.toml`) and name neither the leg nor a replay. This unit makes the
seed land held, states who records the replay a later guarded edit owes and when, and proves both
verdicts on the landed leg. It repairs `TOOL-dCalibratedLens-10`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text (each at rev-2,
  its §4 "Amendments (round-1 spec audit)", id 4): unit 10 S5 — the seed's `**Replayed:**` and
  `**Baseline:**` are the adjudicated score TOOL-dFairHearing-25's verdict record states for the
  design-audit replay of the runtime record, a build-run precondition, and `none` is not admitted at
  landing; its AC6 reds on `owed`. Units 8 and 1 name `instruction-eval` in their §7 prose: each edits a
  guard path, so the seed is owed from its pass, and ONE replay of every owed case is recorded by the
  main loop, through the procedure unit 10 S8 writes into `tools/workflows/README.md`, after the last
  unit of the build that edits a guard path has built (unit 1, order 16) and before the close bar.
  Observed by AC1.
- **S2** — The proof, at this unit's order: `python tools/workflows/evals/check_evals.py` over the
  tree prints `instruction-eval — design-audit-runtime-record · held` and exits 0. Observed by AC2.
- **S3** — The owed path and its discharge, a `--fixture` plant `close-bar` of `replay_scorer.py
  --instance instruction-eval`: in a scratch repository it copies the seed case, commits an edit to a
  guarded `tools/workflows/tier2-review.template.js`, and runs `check_eval_suite`: one `owed` line naming
  that path, exit 1; then `--record` with a planted candidate and matches at the seed's baseline: `held`,
  exit 0. Observed by AC3.

## 3. Non-goals (OUT)

- Running a replay inside the leg or inside a unit pass: unit 10 §3, unchanged. The replay is the main
  loop's, recorded once, because each design-audit replay costs about 0.81 M tokens (spec-10 §4
  Evidence) and a replay per guarded unit would pay it twice for one close.
- A verdict that holds an owed case without reddening the bar, the review's alternative. A leg that
  cannot red on a moved load would certify nothing about the edit it guards.
- The guard's extension to `tools/workflows/lenses.toml`: id 8 (`TOOL-dCalibratedLens-30`), which units
  13 and 1 meet.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-10` — `check_evals.py`, `check_eval_suite`, the seed case and `replay_scorer.py --record`; without them there is no leg to observe and no replay to record

## 4. Design

### Evidence

- spec-10 S3 (owed when `**Replayed:**` is `none` or a load moved), S5 (`none` and `0/59` admitted),
  AC6 (`held` or `owed`), §4 "The guard" (`tier2-review.template.js`, `unattended-build.template.js`).
- Guard-path edits after unit 10 (order 12), read from the Files touched of the later specs: unit 8
  (order 14) `tools/workflows/unattended-build.template.js`; unit 1 (order 16)
  `tools/workflows/tier2-review.template.js` and `tools/workflows/lenses.toml`; units 11, 13 and 14
  edit none.
- `run-gates.sh:3249-3251` holds every `subject = kit` / `chunk = selftests` leg when `GATE_SELFTESTS` is
  empty, as the skeptic re-probed; the close bar sets it.

### The order of the close

```
unit 1 built (last guard-path edit)  ->  replay recorded (main loop, README procedure, --record)
  ->  check_evals.py: every case held  ->  the close bar
```

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `close-bar` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/workflows/replay_scorer.py` — S3, the plant

### Alternatives rejected

- **A replay per guarded unit (8 and 1).** Two design-audit replays for one close, the second
  overwriting the first's `**Replayed:**`.
- **The seed at `none` until the first replay.** It is the defect: an owed seed reds the close bar.

## 5. Production-readiness checklist

- security — no new surface; `--record` writes one case file through its temp file and `os.replace`.
- perf / scale — one replay per build close, about 0.81 M tokens; none per unit.
- error / empty / loading states — a seed with no adjudicated score is a build-run precondition that
  stops unit 10, never a seed landed owed.
- observability — `check_evals.py` names every owed case and the paths that moved.
- risks — a later build editing a guard path owes its own replay; the leg names it.
- testing — the plant of S3 and the tree observation of S2.
- migration — N/A: the suite is new in unit 10.
- user docs — the procedure is unit 10 S8's README section.

## 6. Acceptance criteria

- **AC1** — When `grep -n '^- \*\*id 4 · '` runs over the specs of units 10, 8 and 1, each prints its
  §4 "Amendments (round-1 spec audit)" bullet, unit 10's admitting no seed at `**Replayed:** none`.
  Red when: a guard-path editor names no leg, or the seed may still land owed.
- **AC2** — When `python check_evals.py` runs from the workflows kit's `evals` directory over the tree
  after this unit's pass, it prints the seed's `held` line and exits 0.
  Red when: the seed lands owed or fell.
  fixture: the seed's score is TOOL-dFairHearing-25's verdict record, a build-run precondition.
- **AC3** — When `python replay_scorer.py --instance instruction-eval --fixture --plant close-bar`
  runs from the workflows kit directory, it prints one `owed` line naming `tools/workflows/tier2-review.template.js` and exit 1, then
  `held` and exit 0 after the planted `--record`.
  Red when: a moved guard path leaves the case held, or a recorded replay leaves it owed.

## 7. Gates

`review-replay selftest` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The leg `instruction-eval` is not in the manifest at base and is named here in prose.

New arm: tools/workflows/replay_scorer.py · covers AC3 · the `close-bar` plant, staged red by a check that reads a moved guard path as held · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 4 (HIGH, item H5) of the round-1 spec audit;
  units 10, 8 and 1 amended at the disposal (their rev-2).

## 10. Reuse audit

The seam extended is unit 10's own suite: `check_eval_suite` and `replay_scorer.py --record`, with the
seed's score taken from TOOL-dFairHearing-25's verdict record rather than re-derived. `python
tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an unread line, never
the walk's exit"`, run once for the set, ranked name stems only; `replay_scorer.py` is absent at base,
so no code seam fits beyond the sibling and parent specs. The recall probe returned
TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`

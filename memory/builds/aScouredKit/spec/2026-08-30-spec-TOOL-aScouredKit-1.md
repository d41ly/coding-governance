# TOOL-aScouredKit-1 — wave 1: dead, unwired, duplicated, inefficient, and lying instruments

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-1 · base 14e21399 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md) | diff-review | TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-dead-code.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-dead-code.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-duplication.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-duplication.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-inefficiency.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-inefficiency.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-instruments.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-instruments.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-unwired.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-unwired.md) | research | — |
| [2026-08-30-review-TOOL-aScouredKit-1-wave1-report.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-report.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Run the shipped whole-repo audit harness over the kit and land its report as a joined record, so the
first four of the owner's five axes have an answer on disk that cites paths and commands.

## 2. Scope (IN)

- S1. One `Workflow` run of `tools/workflows/drift-audit-code.js`, primed with the Tier-0 drift
  numbers, the open backlog as `byDesign`, and the kit layout as `stack`.
- S2. The report renamed to hygiene check 5's grammar under `memory/builds/aScouredKit/reviews/`,
  carrying its `**Serves:** diff-review` binding line and a `## Verdict:` opening line.
- S3. Every confirmed finding triaged into exactly one of: a unit of this build, a backlog row, or a
  parked entry with its reason.

## 3. Non-goals (OUT)

- Fixing findings. A fix is its own unit with its own spec, at the tier its risk earns.
- The hardcoded-value, govkit-convergence and prose axes — those are `TOOL-aScouredKit-2`.
- Editing `drift-audit-code.js`. Its lens array must stay a ≤5-element literal or `agent-cap.js`
  can no longer prove the fan-out bounded.

## 4. Design

The harness already exists and already covers four of the five lenses this axis needs, including the
one the owner named by example: its dead-code lens opens by requiring the reviewer to read whatever
computes a fan-in metric and establish what it structurally cannot see. That is the
`reuse_lookup.py`-could-not-see-Python class, generalized.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Record | `memory/builds/aScouredKit/reviews/` | the wave-1 report plus five per-lens writeups |
| Roster | `memory/builds/aScouredKit/README.md` | units added by `--rescope` |
| Backlog | `memory/backlog/TOOL.md` | rows for findings not built here |

### Alternatives rejected

Writing a new whole-corpus review harness. `drift-audit-code.js` is project-agnostic, takes every
repo fact through `args`, and is already on the merge bar via `check-verifier-fanout.sh`. A second
implementation of the same orchestration is the duplication class its own lens 3 hunts.

## 5. Production-readiness checklist

- security — N/A, the run reads and writes records only.
- perf / scale — the fan-out is bounded at 5 by the harness's own inlined helper.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a lens returning no findings is a recorded answer, not a failure.
- observability — the report file and five per-lens writeups are the trace.
- risks — a lens re-reporting a tracked row wastes a verify slot; mitigated by `byDesign`.
- testing + left-shift gates — `bash tools/run-gates/run-gates.sh` at the push boundary.
- migration / rollback — N/A, additive records.
- user docs — N/A, no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the wave-1 run completes, `memory/builds/aScouredKit/reviews/` holds a report whose
  filename matches hygiene check 5 and whose first line is `## Verdict:` — proven by
  `bash tools/memory-tree/check-memory-hygiene.sh` staying green.
- **AC2** — When the report is read, every finding carries a `file:line` a reader can open, verified
  by `git ls-files --error-unmatch` on each cited path.
- **AC3** — When triage completes, every confirmed finding is named by a unit id in the build
  README's `roster:units` region, a row in `memory/backlog/TOOL.md`, or a `--park` entry in `RUN.md`.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `python3 tools/memory-tree/gen_build_index.py
--check` · `python3 tools/memory-tree/gen_build_index.py --check-format` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "adversarial review of the whole kit for dead code and
hardcoded values"` ranked `tools/workflows/drift-audit-code.js` reachable through the
`workflow-scripts` inventory key and the `codebase-map` affordance seam. Read directly, it is the
seam: five primed lenses over the WHOLE repo at a base sha, `byDesign` for the tracked set, bounded
fan-out already marked for `agent-cap.js`. This unit EXTENDS it by supplying args; it writes no code.

Recall terms used: `adversarial review dead code hardcoded prefix govkit convergence deploy adopt
wire kit flexible owner-adjustable`. The query surfaced `TOOL-aRootedPrefix-1`,
`TOOL-aGradedDoorway-2`, `TOOL-aFlaggedScaffold-3` and `TOOL-aFlaggedScaffold-5` as the prior art on
these exact classes; all four are tracked and go into `byDesign` rather than being re-found.

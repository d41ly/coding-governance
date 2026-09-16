---
slug: aRatifiedRulings
node: a
opened: 2026-09-13
streams: tooling
roster: TOOL
parents: aLeakedHandle
authorized-by: prompt
ids: TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4
---

# aRatifiedRulings — the four owner rulings from aLeakedHandle, built

## The problem this build exists to solve

`aLeakedHandle` landed on 2026-09-10 with three decisions parked for the owner and one inherited
from `aJoinedCanon`. On 2026-09-13 the owner ruled on all four, recorded as
`TOOL-aLeakedHandle-6` through `-9` in `memory/DECISIONS.md`. Each ruling is a change to a
mechanism this repo already ships, and none of them has been built.

One is a method change: a blocker on a converged review subject is disposed, never re-rounded. One is
a checker change: check 23 stops reporting the file `--brief` itself staged. One is a cost
restructure: the hygiene self-test stops re-running the whole checker once per arm. One reopens a
backlog row: the rc=137 tail gets its no-ceiling branch. The rulings are the mandate; the trace and
the parks that motivated them live under `builds/aLeakedHandle/`.

## Expected improvements

- The review loop's terminal state has a documented second exit, and check 37's refusal names it.
- The brief path leaves the check-23 lines whose pass commit carries its row; real undeclared
  writes keep firing. Unit 2's ledger: 5 of 29 lines clear, 23 lose the brief, 1 keeps it by construction.
- `memory-hygiene self-test` runs inside its 900 s ceiling under a full concurrent bar, measured.
- A leg killed while running unbounded reports how long it ran.

## Detriments if this is not built

- Four owner rulings sit in the decision log as text, which is the two-answers class one file over.
- The hygiene self-test stays red on every `GATE_SELFTESTS=1` run, and the held-leg drift class
  `TOOL-aBoundedCeiling-10` names keeps collecting instances.
- The next run that hits a late blocker on a converged subject re-derives the same park.

## Build-level rules

- **Each ruling is one unit and cites its ruling id in section 1.** The ruling is the authority; the spec is the work.
- **The 900 s ceiling is not touched by this build.** Unit 3 makes the suite cheaper and re-measures; whether the number then moves is a separate decision with a measurement behind it.
- **Unit 1 edits a governance carrier under its declared byte budget.** `BUILD-METHOD.md` M1 states the cap; the edit trades or it does not land.
- **Every new gate arm has its failing case observed RED first**, and asserts a positive artifact that it ran.
- **Unit 4's red case is fixture-only, and says so.** Every leg declares a ceiling, so the branch cannot be observed against a real leg; the ruling accepted that.
- **A pass runs the fast diff-scoped gates and NOTHING held.** Owner, 2026-09-13, after unit 2 ran five hours stacking suite runs. No self-test, no held leg, no bar inside a pass; the full bar is close's and the push boundary's, per M6. A unit whose SUBJECT is a suite runs it once, alone.

## Parked decisions

- **Unit 3's wall-clock ratio and the full-bar row** (parked in `RUN.md`, 2026-09-13). The one after
  run the per-pass rule allows read 775.7 s against the spec's quiet 598.7 s, ratio 1.296 over AC2's
  0.8, on a box carrying thirteen sibling `run-gates.sh` bars; the trace puts the changed region at
  0.59 of its §4 seconds and every untouched region at 1.3-9.2×, and the invocation count fell 20 to
  13 with zero `git archive`. The paired quiet re-measure and the `GATE_FULL=1 GATE_SELFTESTS=1`
  bar are the closing pass's; whether the count alone is the claim is the owner's. Candidate C's
  figures sit in the spec's §4 for the day the loaded row reads red.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aRatifiedRulings-1` | CLOSED | a converged subject's later blocker is disposed, never re-rounded — M4 and check 37 |
| 2 | `TOOL-aRatifiedRulings-2` | CLOSED | check 23 excludes the path a brief row names |
| 3 | `TOOL-aRatifiedRulings-3` | CLOSED | one checker run serves several hygiene self-test arms |
| 4 | `TOOL-aRatifiedRulings-4` | CLOSED | the rc=137 tail for a leg with no declared ceiling |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-09-13 · streams tooling
ids TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aRatifiedRulings-1 — a converged subject's later blocker is disposed, never re-rounded](spec/2026-09-13-spec-TOOL-aRatifiedRulings-1.md) | — | 2 | CLOSED | rev-4 | 2026-09-13 |
| [TOOL-aRatifiedRulings-2 — check 23 stops reporting the brief `--brief` staged, by the path its row names](spec/2026-09-13-spec-TOOL-aRatifiedRulings-2.md) | — | 2 | CLOSED | rev-5 | 2026-09-14 |
| [TOOL-aRatifiedRulings-3 — the hygiene self-test's project-key arms stop re-running the checker over the whole corpus](spec/2026-09-13-spec-TOOL-aRatifiedRulings-3.md) | — | 2 | CLOSED | rev-6 | 2026-09-14 |
| [TOOL-aRatifiedRulings-4 — a leg killed with no ceiling in play names the seconds it ran](spec/2026-09-13-spec-TOOL-aRatifiedRulings-4.md) | — | 1 | CLOSED | rev-4 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 12 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aLeakedHandle](../aLeakedHandle/README.md)
- **Child builds:** [aProbedUnit](../aProbedUnit/README.md)
<!-- /gen:build-edges -->

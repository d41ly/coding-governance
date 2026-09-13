---
slug: aRatifiedRulings
node: a
opened: 2026-09-13
streams: tooling
roster: TOOL
status: OPEN
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
- Thirty corpus lines of check-23 noise clear, and the class keeps firing for real undeclared writes.
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

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aRatifiedRulings-1` | MISSING | a converged subject's later blocker is disposed, never re-rounded — M4 and check 37 |
| 2 | `TOOL-aRatifiedRulings-2` | MISSING | check 23 excludes the path a brief row names |
| 3 | `TOOL-aRatifiedRulings-3` | MISSING | one checker run serves several hygiene self-test arms |
| 4 | `TOOL-aRatifiedRulings-4` | MISSING | the rc=137 tail for a leg with no declared ceiling |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-13 · streams tooling
ids TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aLeakedHandle](../aLeakedHandle/README.md)
<!-- /gen:build-edges -->

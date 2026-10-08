---
slug: dLadderedRemote
node: d
opened: 2026-10-08
streams: tooling
roster: TOOL
ids: TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6
---

# dLadderedRemote — every kit probe finds the remote by the lander's ladder, not by the name origin

## The problem this build exists to solve

inCMS adopted gov 40a8b8c3, and from then on every core push from its node `d` went red in the
`gov-bar` leg. The red is `drift-audit records` exiting 2 with "cannot resolve a default branch".
Node `d` names its inCMS remote `incms`. Its `refs/remotes/incms/HEAD` is set and
`branch.main.remote` is `incms`, so the repository is fully determined. The probe only asks about
`origin`. The workaround exports `GOV_DEFAULT_BRANCH=main`, which drops the report to the local
`refs/heads/main`. During a landing that ref is the tip under test, so the red goes away and the
report stops meaning anything. The lander fixed this class once, in `TOOL-aRepatriatedFork-8` S1.
Every other probe still spells `origin`, and a scan finds the same literal in eleven kits and two
shipped git hooks.

## Expected improvements

- A node whose only remote is not named `origin` gets graded answers from drift-audit, the
  codebase-map baseline assert, the bar's scope base, the verdict epoch, check 27, the unattended
  liveness reader, the run log, the playbook render and both shipped git hooks.
- Several remotes with none chosen is one refusal, worded once, naming `GOV_REMOTE`, at every site.
- A literal `origin` ref cannot come back into kit code, because a ban leg reds it.

## Detriments if this is not built

- inCMS node `d` lands with `GOV_DEFAULT_BRANCH=main` exported, so its drift report grades the
  push against itself.
- The codebase-map shrink-only assert prints UNGRADED on that node, and every scoped bar there runs
  in full.

## Build-level rules

Classification at kickoff: all four units MISSING, then READY once authored. Scope is the whole
class the ban predicate finds (owner, 2026-10-08). The review harness's `base` becomes required
rather than waived (owner, 2026-10-08). No `spec-audit:` is declared (owner, 2026-10-08). The
passes are authored inline and sequenced, not delegated. Order: the ladder, then the ban observed
RED at 40a8b8c3, then the consumers and the harness edit, which turn it green.
The `tools/unattended/` self-test suites are NOT run, under the owner's standing instruction of
2026-08-23. Unit 2's unattended edits are verified by a hermetic probe, and the suite command is
handed to the owner. AC7, the adopter's own landing without `GOV_DEFAULT_BRANCH`, is observable only
in inCMS on node `d`. It is an adopter Definition-of-Done item, not a gov one.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dLadderedRemote-1` | INPROGRESS | the ladder as two canonicals in the lib dir, parity rows and one truth table both must print |
| 2 | `TOOL-dLadderedRemote-2` | INPROGRESS | every site reading a literal `origin` carries the ladder inline and keeps its own fallback beneath it |
| 3 | `TOOL-dLadderedRemote-3` | INPROGRESS | a ban leg on literal `origin` refs in kit code, observed RED at 40a8b8c3 |
| 4 | `TOOL-dLadderedRemote-4` | INPROGRESS | the tier-2 review harness requires `base` instead of defaulting to `origin/main` |
| 5 | `TOOL-dLadderedRemote-5` | INPROGRESS | the closing review's minors: a tighter ban, an unambiguous ladder, prose naming the ladder |
| 6 | `TOOL-dLadderedRemote-6` | INPROGRESS | the round-2 minors: the ban's lost defaults, variables and argv; the guard's message and branch read |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 6 unit(s) · node d · opened 2026-10-08 · streams tooling
ids TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dLadderedRemote-1 — the remote ladder has one canonical per language, and one truth table holds both](spec/2026-10-08-spec-TOOL-dLadderedRemote-1.md) | 1 | 2 | INPROGRESS | rev-1 | 2026-10-08 |
| [TOOL-dLadderedRemote-3 — a ban leg reds a literal origin ref in kit code](spec/2026-10-08-spec-TOOL-dLadderedRemote-3.md) | 2 | 2 | INPROGRESS | rev-3 | 2026-10-08 |
| [TOOL-dLadderedRemote-2 — every probe that read a literal origin carries the ladder inline and keeps its own fallback beneath it](spec/2026-10-08-spec-TOOL-dLadderedRemote-2.md) | 3 | 2 | INPROGRESS | rev-3 | 2026-10-08 |
| [TOOL-dLadderedRemote-4 — the tier-2 review harness requires a diff review's base instead of defaulting to origin/main](spec/2026-10-08-spec-TOOL-dLadderedRemote-4.md) | 3 | 2 | INPROGRESS | rev-1 | 2026-10-08 |
| [TOOL-dLadderedRemote-5 — the closing review's minors: a tighter ban, an unambiguous ladder, and prose that names the ladder](spec/2026-10-08-spec-TOOL-dLadderedRemote-5.md) | 4 | 2 | INPROGRESS | rev-2 | 2026-10-08 |
| [TOOL-dLadderedRemote-6 — the round-2 minors: the ban's lost defaults, variables and argv, and two small honesty fixes](spec/2026-10-08-spec-TOOL-dLadderedRemote-6.md) | 5 | 2 | INPROGRESS | rev-1 | 2026-10-08 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 3 record folder(s).

Ids no record names: TOOL-dLadderedRemote-6.

Ids no `spec-audit` record has ever named: TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dLadderedRemote-1` | no |
| 2 | `TOOL-dLadderedRemote-3` | no |
| 3 | `TOOL-dLadderedRemote-2`, `TOOL-dLadderedRemote-4` | yes |
| 4 | `TOOL-dLadderedRemote-5` | no |
| 5 | `TOOL-dLadderedRemote-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

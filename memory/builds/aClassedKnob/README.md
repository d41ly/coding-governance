---
slug: aClassedKnob
node: a
opened: 2026-10-07
streams: tooling
roster: TOOL
ids: TOOL-aClassedKnob-1 TOOL-aClassedKnob-2 TOOL-aClassedKnob-3
---

# aClassedKnob — the emitted pre-push and push-main self-tests pass in an adopter

## The problem this build exists to solve

Two adopters, inCMS and NicoCares, hold their adoption landings on gov's own bytes. The
`pre-push self-test` leg that gov's push-main kit emits as a repo-subject leg fails two arms there.
H49 finds four knobs the runner reads and nobody classified, which also fails in gov, unseen because
the leg is guarded on `.githooks/`. IR AC11 asserts gov's own inherited-red policy, `land` with a bound
of 10, against whatever repository the suite runs in, so an adopter declaring `park` can never pass
it. Separately, `push-main self-test` arm 2d plants a claim-push lock three seconds out and reds
whenever a loaded host takes longer than that to reach it. After those landed, nc's push boundary
refused `verdict epoch`: its pull wrote gov's engine bytes in two commits, bump first, and the
topological rule read the bump as older than the change it dates.

## Expected improvements

- Both adopters' `pre-push self-test` leg is green on gov's bytes, with no adopter edit.
- Arm 2d's verdict does not depend on how long the lander takes to reach the lock.

## Detriments if this is not built

- Both adopters' unattended runs stay HELD with code owner-decision.
- A red arm in an emitted leg teaches adopters to waive the leg, which hides the next real red.

## Build-level rules

Units 1 and 2 are Tier-1, test-only edits to emitted suites: neither hook nor lander behaviour
moves, and they touch disjoint files. Unit 3 changes one gate's verdict in adopters only, opened at
the adoption session's request after 1 and 2 landed. Out of scope, noted for the adopter's backlog and not built here:
inCMS's asks on the full-green stamp predicate, `GATE_LEGS` leaking into nested fixture runs, and the
shell-hygiene leg's registry argument.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aClassedKnob-1` | CLOSED | H49 classifies the four memory-pause and census knobs; IR AC11 reads the repository's own policy |
| 2 | `TOOL-aClassedKnob-2` | CLOSED | arm 2d releases its lock after the lander has reached it, not on a wall-clock deadline |
| 3 | `TOOL-aClassedKnob-3` | CLOSED | verdict epoch reads a vendored engine against the install receipt, not the pull's commit order |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-10-07 · streams tooling
ids TOOL-aClassedKnob-1 TOOL-aClassedKnob-2 TOOL-aClassedKnob-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aClassedKnob-1 — the pre-push self-test classifies every runner knob and reads the adopter's own policy](spec/2026-10-07-spec-TOOL-aClassedKnob-1.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-07 |
| [TOOL-aClassedKnob-2 — push-main arm 2d holds its lock until the lander has reached it](spec/2026-10-07-spec-TOOL-aClassedKnob-2.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-07 |
| [TOOL-aClassedKnob-3 — the verdict epoch reads an adopter's vendored engine against its install receipt](spec/2026-10-07-spec-TOOL-aClassedKnob-3.md) | 2 | 1 | CLOSED | rev-1 | 2026-10-07 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aClassedKnob-1 TOOL-aClassedKnob-2 TOOL-aClassedKnob-3.

Ids no `spec-audit` record has ever named: TOOL-aClassedKnob-1 TOOL-aClassedKnob-2 TOOL-aClassedKnob-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aClassedKnob-1`, `TOOL-aClassedKnob-2` | yes |
| 2 | `TOOL-aClassedKnob-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

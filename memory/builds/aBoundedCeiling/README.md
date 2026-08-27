---
slug: aBoundedCeiling
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 TOOL-aBoundedCeiling-7 TOOL-aBoundedCeiling-8 TOOL-aBoundedCeiling-9 TOOL-aBoundedCeiling-10 TOOL-aBoundedCeiling-11 TOOL-aBoundedCeiling-12 TOOL-aBoundedCeiling-13
---

# aBoundedCeiling — a leg that cannot hang forever, and a landing that pays for the bar once

## The problem this build exists to solve

Make the merge bar's cost a VERDICT rather than a complaint, and a hang a RED rather than a wedge, in
a way that ships to every adopter of the run-gates kit and not only to this repository. Nothing
anywhere had a deadline, so any slow thing became an unbounded thing — which is why moving the
self-tests off the bar treated the symptom and the same hang reappeared on `unattended.sh --close`,
in a repo that does not run gov's bar at all.

## Expected improvements

- A hung leg is KILLED and reported RED naming itself, instead of wedging the whole bar silently.
- A hung `--close` is bounded too, in whatever gate command a project declares — the case observed
  running 3h19m on this node with its launching session already dead.
- An unbounded leg is COUNTED on every run, so a manifest quietly losing its bounds is visible.
- Adopters get both, because the bound lives in the kit rather than in this repo's configuration.

## Detriments if this is not built

- A leg that stops returning takes the bar with it, reports nothing, and is indistinguishable from a
  slow one — measured at 6858 s on this build's own landing.
- `--close` waits forever on a gate that will never answer, with no owner turn to interrupt it.
- Cost stays a complaint rather than a verdict, so slowness is only ever worked around.

## Build-level rules

Three units live: `-1` per-leg ceilings, `-6` the bounded runner, `-5` the deployer half. `-5` was
RETIRED at landing on owner instruction to merge at 2.5 of 3; `TOOL-aBoundedCeiling-13` carries its
remaining scope. Three planned units were dropped before any spec existed: one needed an owner ruling
on pre-push predicate 5, one had its premise refuted (the guard bypass is load-bearing for the green
stamp), and one was refused because the two ceiling mechanisms differ on the behaviour they would
share. No unit may return the unattended kit's `*.test.sh` legs to `tools/gate-legs.json` — owner
ruling, 2026-08-23.

## Parked decisions

Four, all recorded in `RUN.md` with the options seen and the reason each was refused: the `--close`
double bar, which needs a ruling on pre-push predicate 5; six abandoned processes on this node, left
alone because they are another repository's work; whether to land at 2.5 of 3 units, since resolved
by the owner; and the two Definition-of-Done overrides that landing took.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBoundedCeiling-1` | 2 | per-leg wall-clock ceilings in the leg manifest, enforced by the runner |
| 2 | `TOOL-aBoundedCeiling-5` | 2 | the ceiling travels to adopters through the deployer |
| 3 | `TOOL-aBoundedCeiling-6` | 2 | the close's gate run cannot outlive a declared bound |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 TOOL-aBoundedCeiling-7 TOOL-aBoundedCeiling-8 TOOL-aBoundedCeiling-9 TOOL-aBoundedCeiling-10 TOOL-aBoundedCeiling-11 TOOL-aBoundedCeiling-12 TOOL-aBoundedCeiling-13

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBoundedCeiling-1 — a leg declares how long it may take, and the runner holds it to it](spec/2026-08-27-spec-TOOL-aBoundedCeiling-1.md) | 1 | 2 | CLOSED | rev-5 | 2026-08-27 |
| [TOOL-aBoundedCeiling-6 — the close's gate run cannot outlive a declared bound](spec/2026-08-27-spec-TOOL-aBoundedCeiling-6.md) | 1 | 2 | CLOSED | rev-3 | 2026-08-27 |
| [TOOL-aBoundedCeiling-5 — the ceiling travels, so an adopter's bar is bounded too](spec/2026-08-27-spec-TOOL-aBoundedCeiling-5.md) | 2 | 2 | WONTDO | rev-3 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBoundedCeiling-1`, `TOOL-aBoundedCeiling-6` | yes |
| 2 | `TOOL-aBoundedCeiling-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

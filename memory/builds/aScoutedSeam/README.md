---
slug: aScoutedSeam
node: a
opened: 2026-10-11
streams: tooling+kickoff+deployer
roster: TOOL+KICK+DEPL
ids: DEPL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3
---

# aScoutedSeam — a reuse scout reads the code before any spec is written, and its seams bind

## The problem this build exists to solve

Build sessions in gov, inCMS and NicoCares keep rebuilding what already exists: image fields beside
a media picker, page CSS beside a token layer, a fifth conf parser beside four. The reuse tooling
never prevented it. The lookup matches names, adopters almost never run it, it cannot see design
tokens or a host repository, and its answer stops at the spec, graded on shape. The failure analysis
and the benchmark under [build/](build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md) measure it.

## Expected improvements

- On opt-in, orientation runs a scout that reads the code and pins MUST seams on the card.
- The brief, the spec and the builder all carry those seams, and a spec cannot silently drop one.
- A diff-time check catches a duplicate written after the spec.
- A package build sees its host repository's design vocabulary.

## Detriments if this is not built

- Adopters keep shipping parallel implementations the owner consolidates by hand afterwards.
- The reuse obligation stays a §10 sentence a citation of the wrong seam satisfies.
- Design work keeps hardcoding values beside the tokens meant for them.

## Build-level rules

- **Classification (M2)**: five units, MISSING at open, one mechanism each.
- The design is the benchmark's verdict: one checklist scout plus a design pass, merged
  deterministically, with no skeptic or judge agent, plus a diff mode. The M1c trial then made the
  checklist read a generated house index first, sketch the implementation and take a convention
  census ([trial](build/2026-10-11-build-TOOL-aScoutedSeam-1-7-m1c-trial.md)). Two shapes are rejected on
  measurement: the five-lens fan-out with skeptics, and the name-matching lookup as the mechanism.
- Layered on aOrientedCast: this build owns the `gov-reuse-scout` role's body, its `reads` and
  `returns`, and the `reuse` harness. aOrientedCast owns the catalogue grammar, the renderer, the
  spawn guard, the harness wiring and `skills/session-kickoff/` until its KICK units land.
- One delta from the contract agreed with aOrientedCast: the harness now takes `index`, the house
  index path. The attended router's stage 2 therefore runs `gen_map.py --house-index` before the
  harness, as kickoff does. aOrientedCast confirmed the delta on 2026-10-11 and placed the stage 2
  edit in `TOOL-aScoutedSeam-1` (S9 and S10).
- The kickoff unit builds after aOrientedCast's KICK units; whoever lands second reconciles.
- Opt-in is the owner's: a dated README key or a dated project default, never a run's own.
- One kit-version bump per touched kit, after that kit's last unit.

## Parked decisions

None. The open forks are each spec's §8.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aScoutedSeam-1` | the reuse scout: a checklist role and a harness running a code and a design pass, merged into a capped `## reuse` section |
| 2 | `KICK-aScoutedSeam-1` | kickoff asks once, runs the scout on opt-in, and carries its seams onto the card and into the brief |
| 3 | `TOOL-aScoutedSeam-3` | the scout's diff mode: a landed diff checked against the tree and the `## reuse` seams |
| 4 | `TOOL-aScoutedSeam-2` | a spec's §10 names every MUST seam its brief carries, or overrides it with a reason, and check 12 grades it |
| 5 | `DEPL-aScoutedSeam-1` | adopters get the scout and a resolved host tree, and the adopter-side gaps the research found are filed |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 5 unit(s) · node a · opened 2026-10-11 · streams tooling+kickoff+deployer
ids DEPL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aScoutedSeam-1 — the reuse scout: a checklist role and a harness running a code and a design pass, merged into a capped `## reuse` section](spec/2026-10-11-spec-TOOL-aScoutedSeam-1.md) | 1 | 2 | SPECCED | rev-8 | 2026-10-18 |
| [KICK-aScoutedSeam-1 — kickoff asks once, runs the scout on opt-in, and carries its seams onto the card and into the brief](spec/2026-10-11-spec-KICK-aScoutedSeam-1.md) | 2 | 2 | SPECCED | rev-4 | 2026-10-18 |
| [TOOL-aScoutedSeam-3 — the scout's diff mode: a landed diff checked against the tree and the `## reuse` seams](spec/2026-10-11-spec-TOOL-aScoutedSeam-3.md) | 3 | 2 | SPECCED | rev-4 | 2026-10-18 |
| [TOOL-aScoutedSeam-2 — a spec's §10 names every MUST seam its brief carries, or overrides it with a reason, and check 12 grades it](spec/2026-10-11-spec-TOOL-aScoutedSeam-2.md) | 4 | 2 | SPECCED | rev-2 | 2026-10-18 |
| [DEPL-aScoutedSeam-1 — adopters get the scout and a resolved host tree, and the adopter-side gaps the research found are handed over](spec/2026-10-11-spec-DEPL-aScoutedSeam-1.md) | 5 | 2 | SPECCED | rev-4 | 2026-10-18 |
<!-- /gen:build-units -->

Records: 92 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aScoutedSeam-1` | no |
| 2 | `KICK-aScoutedSeam-1` | no |
| 3 | `TOOL-aScoutedSeam-3` | no |
| 4 | `TOOL-aScoutedSeam-2` | no |
| 5 | `DEPL-aScoutedSeam-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

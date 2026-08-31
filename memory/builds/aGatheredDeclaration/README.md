---
slug: aGatheredDeclaration
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8
authorized-by: prompt
---

# aGatheredDeclaration — one declared file, one gate entry point, and every ceiling opt-in

## The problem this build exists to solve
The gate bar is DECLARED in three places and EXECUTED from two, and neither split is visible to the
owner who has to adjust it. Legs sit in JSON that cannot carry the reasoning for a row, concurrency
sits in a separate knob table, and opt-in has no key at all — it is inferred from `subject = "kit"`.
The runner parses NO arguments, so there is no way to run one leg: every check costs the whole bar,
which on this tree has a 26-minute floor. Ceilings are enforced unconditionally on all 86 legs and
have cost killed legs, reds and re-runs; the turnstile ships enabled and once wedged a landing 6858 s
behind three dead tickets. Two adopters prove the schema is unsettled — inCMS runs its own 863-line
runner over a richer manifest, NicoCares runs this kit over a manifest declaring almost nothing. The
prompt record holds the measurements.

## Expected improvements
- One owner-readable, commented `gate-legs.toml` declares legs, opt-in, ceilings, guards, lanes AND
  the profile table, so adjusting the bar is one file and every number keeps its argument beside it.
- `run-gates.sh` grows a real argument surface, so a single leg can be run by name and the manifest
  can be printed — the shard the bar has never had.
- Ceilings become owner opt-in and default OFF, which converts a class of killed-leg reds into
  evidence.
- The turnstile ships disabled, so no adopter inherits a queue that can wedge their landings.
- One upgrader migrates any adopter's manifest and its tests onto the canonical declaration.

## Detriments if this is not built
- Owners keep editing three files to change one bar, and JSON keeps silently deleting the reasoning.
- Every check keeps costing the whole bar, so the bar keeps being skipped rather than sharded.
- Adopters keep inheriting enforcement defaults that have measurably cost landings in this tree.
- The two adopter dialects keep diverging, and each new adopter picks a third.

## Build-level rules
- **Reuse before invention: the runner already exists.** `tools/run-gates/` is a kit with an adopter
  and 1480 lines of measured behaviour. Nothing here builds a second runner.
- **inCMS is prior art, not a competitor.** Its `optIn`, `phase`, `cwd` and its `INCMS_GATE_UNBOUNDED`
  banner discipline are harvested into the canonical schema. Its 863-line runner is not ported.
- **A knob may never turn a leg into a PASS or a SKIP.** `gate-profiles.txt`'s governing invariant
  survives the move verbatim; ceilings going OFF produces strictly MORE evidence, never less.
- **Ceilings off must announce themselves twice and durably** — a banner before the first leg and a
  line in the summary — so a green earned unbounded is never mistakable for one earned bounded.
- **Every new gate and every changed refusal has its failing case observed RED first.**
- **Nothing lands outside this repository.** The adopters are reviewed and an upgrader is shipped;
  migrating each one is that repo's own build, on its own bar (owner ruling, 2026-08-31).
- **The spec-audit loop ended NON-CONVERGENT at round 4, and no blocker was promoted.** Blocker
  counts ran 5, 4, 3, 4; four is not strictly smaller than three, so under `BUILD-METHOD.md` M4 the
  loop STOPPED and there is no round 5. M4 promotes every blocker STILL STANDING at the exit, and
  all four were closed by the round-4 fold, so none stands and none was promoted. Three of the four
  were `amendment-leaves-its-other-half-standing` in the round-3 fold's own text — editing residue
  in these specs, where the fold IS the fix and there is no unit of work left to spec. The fourth
  was a real design contradiction and is resolved in unit 2 S10. Promoting a stale paragraph to a
  numbered unit would be ceremony this method's own budget rule argues against.
- **Round 4's report was written by this run, not by the harness.** Its synthesis agent died on a
  session limit after every finder and skeptic had returned, so the record was reconstructed from
  the run journal by the same agent that authored the specs it grades. The conflict is stated in
  that record's opening section rather than hidden, and the adjudicated count went AGAINST this
  run's interest — four ends the loop where two would have continued it.

## Parked decisions
None. One AMENDMENT, recorded in `RUN.md`: the round-1 spec audit returned BLOCKED with five
blockers, and finding F9 showed unit 2 was carrying a dispatcher rewrite it had priced as a format
change. Lanes and the tool probe became `TOOL-aGatheredDeclaration-8` rather than being built
inside a migration whose whole claim is behaviour-neutrality.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aGatheredDeclaration-1` | 1 | the adopter review: what inCMS and NicoCares declare and execute today, and the schema union it implies |
| 2 | `TOOL-aGatheredDeclaration-2` | 2 | `gate-legs.toml` — the single commented declaration, its reader, and the migration of this repo's 86 legs plus the profile table |
| 3 | `TOOL-aGatheredDeclaration-3` | 2 | the runner's argument surface: `--list`, `--leg`, `--manifest`, `--help` — sharding by name |
| 4 | `TOOL-aGatheredDeclaration-4` | 2 | ceiling enforcement becomes owner opt-in, default OFF, announced twice and durably |
| 5 | `TOOL-aGatheredDeclaration-5` | 2 | the turnstile beacon ships disabled, enabled by a declared variable |
| 6 | `TOOL-aGatheredDeclaration-6` | 2 | the readers move: govkit emitter, pre-push, drift-audit, codebase-map, and the carriers that name the entry point to a session |
| 7 | `TOOL-aGatheredDeclaration-7` | 2 | the upgrader: migrate any adopter's manifest and its tests onto the declaration |
| 8 | `TOOL-aGatheredDeclaration-8` | 2 | lanes, the tool probe, and the dispatcher they need — split out of unit 2 at the round-1 audit fold |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 8 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aGatheredDeclaration-1 — the adopter review, and the schema union it implies](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-1.md) | 1 | 1 | INPROGRESS | rev-1 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-2 — `gate-legs.toml`, the one declaration the bar is read from](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-2.md) | 2 | 2 | INPROGRESS | rev-5 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-3 — the runner's argument surface: `--list`, `--leg`, `--manifest`](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-3.md) | 3 | 2 | INPROGRESS | rev-5 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-4 — ceiling enforcement becomes owner opt-in, default OFF](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-4.md) | 4 | 2 | INPROGRESS | rev-5 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-5 — the turnstile beacon ships DISABLED](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-5.md) | 5 | 2 | INPROGRESS | rev-4 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-6 — every reader moves, and the second entry point closes](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-6.md) | 6 | 2 | OPEN | rev-5 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-7 — the upgrader: any adopter's manifest and its tests, onto the declaration](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-7.md) | 7 | 2 | OPEN | rev-5 | 2026-08-31 |
| [TOOL-aGatheredDeclaration-8 — lanes, the tool probe, and the dispatcher they need](spec/2026-08-31-spec-TOOL-aGatheredDeclaration-8.md) | 8 | 2 | OPEN | rev-2 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 9 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aGatheredDeclaration-1` | no |
| 2 | `TOOL-aGatheredDeclaration-2` | no |
| 3 | `TOOL-aGatheredDeclaration-3` | no |
| 4 | `TOOL-aGatheredDeclaration-4` | no |
| 5 | `TOOL-aGatheredDeclaration-5` | no |
| 6 | `TOOL-aGatheredDeclaration-6` | no |
| 7 | `TOOL-aGatheredDeclaration-7` | no |
| 8 | `TOOL-aGatheredDeclaration-8` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

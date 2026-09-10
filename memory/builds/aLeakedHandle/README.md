---
slug: aLeakedHandle
node: a
opened: 2026-09-10
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3 TOOL-aLeakedHandle-4
---

# aLeakedHandle — two reds traced to their causes, and the reporting that made one of them unreadable

## The problem this build exists to solve

A `GATE_FULL=1 GATE_SELFTESTS=1` bar on node `a`, 2026-09-10, returned RED at 2 of 104 legs.
Neither red is new. The root-cause trace under `build/` carries the evidence; this slot states
the shape only.

`unattended kit gate` deadlocked on a pipe whose write end nobody closed, and burned 4168 s
before an operator killed it. `memory-hygiene self-test` hit its 900 s ceiling while the gate
that exists to catch an unsafe ceiling passed green, because a leg that never passes acquires
no evidence row at all.

And the runner printed a declared ceiling where the elapsed time belongs, so one red was
reported at four times its real cost.

## Expected improvements

- The hung leg returns a verdict instead of holding a pool slot until its ceiling.
- The pipe-EOF class is refused by a gate rather than remembered by a gotcha file.
- A leg that times out contributes evidence, so its ceiling stops being unconstrained.
- An externally killed leg is reported as killed, with the seconds it actually ran.
- A wrong number stops entering diagnosis, which is how `TOOL-dRetiredFork-40` was misread twice.

## Detriments if this is not built

- The unattended leg keeps costing up to 4 h 27 m of wall clock per full bar, silently.
- The next instance of the pipe class is found the same way: by hand, from `/proc`, after an hour.
- Ceilings keep being declared against evidence that structurally excludes the legs that need it.
- Every operator kill, OOM and CI cancel keeps reading as a full-ceiling timeout.

## Build-level rules

- **Each red gets its own spec.** Three mechanisms, three units, no shared diff.
- **The class is gated, never the instance.** Fixing one reader and scanning one file certifies coverage this build does not have.
- **Every gate here has its failing case observed RED before it lands.** Staged break, confirmed red, unstaged.
- **No ceiling is re-declared by this build.** `aJoinedCanon` parked that question for the owner on 2026-09-07 and it is still theirs; this build fixes the evidence pipeline, not the number.
- **A contended measurement is not a regression.** `TOOL-aReapedSpinner-23` was withdrawn for exactly that inference, and a concurrent unattended run held this box during the bar.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aLeakedHandle-1` | CLOSED | the pipe whose write end the subshell never closed, and the gate for its class |
| 2 | `TOOL-aLeakedHandle-2` | CLOSED | a timeout is evidence, so a ceiling stops being held above nothing |
| 3 | `TOOL-aLeakedHandle-3` | MISSING | a killed leg reports the seconds it ran, not the ceiling it did not reach |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-09-10 · streams tooling
ids TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3 TOOL-aLeakedHandle-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aLeakedHandle-1 — the pipe whose write end nobody closed, and the gate for its class](spec/2026-09-10-spec-TOOL-aLeakedHandle-1.md) | 1 | 2 | CLOSED | rev-5 | 2026-09-10 |
| [TOOL-aLeakedHandle-2 — a run that reached a leg's ceiling is evidence, not a discarded failure](spec/2026-09-10-spec-TOOL-aLeakedHandle-2.md) | 2 | 2 | CLOSED | rev-4 | 2026-09-10 |
| [TOOL-aLeakedHandle-3 — a killed leg reports the seconds it ran, not the ceiling it did not reach](spec/2026-09-10-spec-TOOL-aLeakedHandle-3.md) | — | 1 | SPECCED | rev-2 | 2026-09-10 |
<!-- /gen:build-units -->

Records: 8 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aLeakedHandle-1` | no |
| 2 | `TOOL-aLeakedHandle-2` | no |

Unordered: `TOOL-aLeakedHandle-3`.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

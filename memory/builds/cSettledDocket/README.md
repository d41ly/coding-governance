---
slug: cSettledDocket
node: c
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: KICK-cSettledDocket-1 TOOL-cSettledDocket-1 TOOL-cSettledDocket-2 TOOL-cSettledDocket-3 TOOL-cSettledDocket-4 TOOL-cSettledDocket-5 TOOL-cSettledDocket-6
---

# cSettledDocket — the six items cBriefedPilot parked

Node `c` · opened 2026-08-16 · streams tooling.

cBriefedPilot shipped 23 units and left six things on the backlog rather than sweeping them into a
build that had already grown twice. Each was filed with the measurement that found it. This build
is those six, and nothing else: the roster below is the whole of it, and a seventh idea is a row in
`memory/backlog/TOOL.md`, not a unit here.

Five are defects with one right answer. One — unit 2 — is a CONTRACT FORK the owner resolves, and
it is specced with both branches costed rather than decided in the design pass.

## Why these six together

They are not a theme, they are a debt. But two pairs share a mechanism, and building them together
is cheaper than building them apart:

- Units 4 and 5 both concern an assertion count nobody derives, at two scales. Unit 4 makes ONE
  suite's count whole; unit 5 makes every bar suite HAVE one, behind a leg. The M4 audit is why unit
  5 is a leg: its original premise — that one named suite had no counter — was false, and the real
  population is 12 silent suites across 4 spellings.
- Units 3 and 6 are both the frozen-versus-live class. Unit 3 is a gate that skips a whole document
  class; unit 6 is the standing fixture that would have caught all three instances cBriefedPilot met.
  They share a theme and NOT a constant: the M4 audit refuted an `ARMS_FLOORS` dependency between
  them, since that pin covers gate scripts and `check-arms.py` excludes `*.test.sh` outright.

<!-- gen:build-index -->
**Build status:** CLOSED · 6 unit(s) · node c · opened 2026-08-16 · streams tooling · ids KICK-cSettledDocket-1 TOOL-cSettledDocket-1 TOOL-cSettledDocket-2 TOOL-cSettledDocket-3 TOOL-cSettledDocket-4 TOOL-cSettledDocket-5 TOOL-cSettledDocket-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-cSettledDocket-1 — a `--park` verb, so a refused decision has somewhere the gate reads](spec/2026-08-16-spec-cSettledDocket-1.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cSettledDocket-2 — `DIRECTIVES_EXTRA` is waivable and unshowable at once](spec/2026-08-16-spec-cSettledDocket-2.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cSettledDocket-3 — a rule called machine-checked that holds for one tier out of two](spec/2026-08-16-spec-cSettledDocket-3.md) | CLOSED | rev-3 | 2026-08-16 |
| [TOOL-cSettledDocket-4 — the hygiene suite's floor covers its helpers and not its file](spec/2026-08-16-spec-cSettledDocket-4.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cSettledDocket-5 — one leg: every self-test prints a count, in one shape, against a floor](spec/2026-08-16-spec-cSettledDocket-5.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-cSettledDocket-6 — a standing fixture for the frozen-versus-live class](spec/2026-08-16-spec-cSettledDocket-6.md) | CLOSED | rev-2 | 2026-08-16 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->

## Units

<!-- roster:units -->
| # | Unit | Tier | Mechanism | Depends on |
|---|---|---|---|---|
| 1 | `TOOL-cSettledDocket-1` | 2 | a `--park` verb: the fourth writer of a parked entry, so a decision refused mid-run has a route the gate reads | — |
| 2 | `TOOL-cSettledDocket-2` | 2 | `DIRECTIVES_EXTRA` is waivable and unshowable at once; the fork is whether the join covers EXTRA or projects get a row source | — |
| 3 | `TOOL-cSettledDocket-3` | 2 | move hygiene check 12's `Tier-1` skip BELOW the terminal-fork and §9-rev assertions, so `TEMPLATE-SPEC`'s machine-checked claim is true for every tier | — |
| 4 | `TOOL-cSettledDocket-4` | 1 | count the ~50 INLINE assertion sites in the hygiene suite, so its floor covers the whole file rather than its helpers | — |
| 5 | `TOOL-cSettledDocket-5` | 2 | one leg: every bar self-test prints a count in one shape against a floor, with a shrink-only registry seeded from the 12 that do not | — |
| 6 | `TOOL-cSettledDocket-6` | 1 | a standing frozen-versus-live fixture: move the world around a terminal record and assert silence | — |
<!-- /roster:units -->

## Provenance

Each unit is one cBriefedPilot backlog row, carried over with its measurement:

| Unit | Row | What was measured |
|---|---|---|
| 1 | `TOOL-cBriefedPilot-30` | the protocol declares four parked kinds and `park()` has three callers, none of them mid-run |
| 2 | `TOOL-cBriefedPilot-31` | `directives()` composes EXTRA; check 16 arm A joins only CORE |
| 3 | `TOOL-cBriefedPilot-32` | with the skip neutralised and the REAL gate run: 2 fail §8, 2 fail the §9 rev-log, of 18 terminal Tier-1 specs |
| 4 | `TOOL-cBriefedPilot-34` | 60 `st=1` sites, 8 of them behind counting helpers |
| 5 | `TOOL-cBriefedPilot-35` | the row was WRONG — that suite counts. Re-measured over the population: 12 of 27 suites print no count, in 4 spellings, and 3 carry a floor |
| 6 | `TOOL-cBriefedPilot-38` | three separate predicates joined a frozen historical value to a live present one |

## Risks

1. **Unit 3 is the one that can red other people's work.** Lifting the Tier-1 skip subjects every
   Tier-1 spec to the terminal-fork and §9-rev assertions. Measured by RUNNING the gate with the cut
   neutralised: 2 fail §8 and 2 fail the §9 rev-log, of 18 terminal Tier-1 specs, and the two groups
   need DIFFERENT repairs. rev-1 of that spec reported 4-and-0 from a Python reimplementation and
   had the attribution inverted for half the files — re-measured at build time, by running the gate.
2. **Unit 2 has no safe default.** Both branches change a published contract. It is specced, not
   taken, and the build sequences it after the units that cannot block.
3. **Unit 4 touches 60 call sites in a file that is itself a gate's proof.** A mechanical sweep that
   miscounts turns a floor into a lie in the file whose whole subject is a count that was a lie.

## Non-goals

- `TOOL-aStandingWrit-2`, `-6` and `-7`. They are the architectural bounds on what the unattended
  kit can assert, not parked items of cBriefedPilot, and each needs its own build.
- Re-opening D6. `TOOL-cBriefedPilot-28` says what evidence would re-open it; none has been gathered.
- Landing cBriefedPilot. That is an owner decision and is not this build's to take.

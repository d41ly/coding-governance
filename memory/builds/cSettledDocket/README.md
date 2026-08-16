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

- Units 4 and 5 are the same missing thing in two suites: an assertion count nobody derives. Unit 4
  finishes the count `TOOL-cBriefedPilot-23` started in the hygiene suite; unit 5 gives the one
  remaining self-test leg a count at all. The helper shape is identical.
- Units 3 and 6 are both the frozen-versus-live class. Unit 3 is a gate that skips a whole document
  class; unit 6 is the standing fixture that would have caught all three instances cBriefedPilot met.

<!-- gen:build-index -->
**Build status:** OPEN · 6 unit(s) · node c · opened 2026-08-16 · streams tooling · ids KICK-cSettledDocket-1 TOOL-cSettledDocket-1 TOOL-cSettledDocket-2 TOOL-cSettledDocket-3 TOOL-cSettledDocket-4 TOOL-cSettledDocket-5 TOOL-cSettledDocket-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-cSettledDocket-1 — a `--park` verb, so a refused decision has somewhere the gate reads](spec/2026-08-16-spec-cSettledDocket-1.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-cSettledDocket-2 — `DIRECTIVES_EXTRA` is waivable and unshowable at once](spec/2026-08-16-spec-cSettledDocket-2.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-cSettledDocket-3 — a rule called machine-checked that holds for one tier out of two](spec/2026-08-16-spec-cSettledDocket-3.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-cSettledDocket-4 — the hygiene suite's floor covers its helpers and not its file](spec/2026-08-16-spec-cSettledDocket-4.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-cSettledDocket-5 — the one self-test leg that reports no count at all](spec/2026-08-16-spec-cSettledDocket-5.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-cSettledDocket-6 — a standing fixture for the frozen-versus-live class](spec/2026-08-16-spec-cSettledDocket-6.md) | OPEN | rev-1 | 2026-08-16 |

Records live under `spec/`.
<!-- /gen:build-index -->

## Units

<!-- roster:units -->
| # | Unit | Tier | Mechanism | Depends on |
|---|---|---|---|---|
| 1 | `TOOL-cSettledDocket-1` | 2 | a `--park` verb: the fourth writer of a parked entry, so a decision refused mid-run has a route the gate reads | — |
| 2 | `TOOL-cSettledDocket-2` | 2 | `DIRECTIVES_EXTRA` is waivable and unshowable at once; the fork is whether the join covers EXTRA or projects get a row source | — |
| 3 | `TOOL-cSettledDocket-3` | 2 | move hygiene check 12's `Tier-1` skip BELOW the terminal-fork and §9-rev assertions, so `TEMPLATE-SPEC`'s machine-checked claim is true for every tier | — |
| 4 | `TOOL-cSettledDocket-4` | 1 | count the ~50 INLINE assertion sites in the hygiene suite, so its floor covers the whole file rather than its helpers | — |
| 5 | `TOOL-cSettledDocket-5` | 1 | give `manifest-check.test.sh` a counter and a floor: it is the one self-test leg with no executed-count signal | — |
| 6 | `TOOL-cSettledDocket-6` | 1 | a standing frozen-versus-live fixture: move the world around a terminal record and assert silence | 3 |
<!-- /roster:units -->

## Provenance

Each unit is one cBriefedPilot backlog row, carried over with its measurement:

| Unit | Row | What was measured |
|---|---|---|
| 1 | `TOOL-cBriefedPilot-30` | the protocol declares four parked kinds and `park()` has three callers, none of them mid-run |
| 2 | `TOOL-cBriefedPilot-31` | `directives()` composes EXTRA; check 16 arm A joins only CORE |
| 3 | `TOOL-cBriefedPilot-32` | 4 of 15 Tier-1 terminal specs would fail the §8 rule if the skip were lifted |
| 4 | `TOOL-cBriefedPilot-34` | 60 `st=1` sites, 8 of them behind counting helpers |
| 5 | `TOOL-cBriefedPilot-35` | zero `PASS`/assertion output and zero counter increments in the file |
| 6 | `TOOL-cBriefedPilot-38` | three separate predicates joined a frozen historical value to a live present one |

## Risks

1. **Unit 3 is the one that can red other people's work.** Lifting the Tier-1 skip subjects every
   Tier-1 spec in the corpus to the terminal-fork and §9-rev assertions. Measured at 4 of 15 before
   this build's own merge with main; the number is re-measured in the spec and again at build time,
   because main added specs while cBriefedPilot ran.
2. **Unit 2 has no safe default.** Both branches change a published contract. It is specced, not
   taken, and the build sequences it after the units that cannot block.
3. **Unit 4 touches 60 call sites in a file that is itself a gate's proof.** A mechanical sweep that
   miscounts turns a floor into a lie in the file whose whole subject is a count that was a lie.

## Non-goals

- `TOOL-aStandingWrit-2`, `-6` and `-7`. They are the architectural bounds on what the unattended
  kit can assert, not parked items of cBriefedPilot, and each needs its own build.
- Re-opening D6. `TOOL-cBriefedPilot-28` says what evidence would re-open it; none has been gathered.
- Landing cBriefedPilot. That is an owner decision and is not this build's to take.

---
slug: aPairedLexer
node: a
opened: 2026-08-30
streams: tooling
roster: TOOL
ids: TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3
---

# aPairedLexer — the three views `aLexedStripper` left behind

## The problem this build exists to solve
`aLexedStripper` fixed the view rule 2 reads and the view `_identifier_tokens` reads, and filed three
rows for the views it did not touch. All three reproduce against the shipped code at `14e21399` and
each is measured in this build's records rather than inferred from its predecessor.

The severe one is `TOOL-aLexedStripper-4`. Rule 3 `capFindings` reads `blankLiterals`, whose mode is
carried across lines, so an unterminated template literal blanks everything below it and the rule
sees nothing. Isolated by deny-message: a bounded receiver with a cap of **500** DENIES with the
template terminated and **ADMITS** below an unterminated one. That is a fail-open on the only
mechanical control against an unbounded agent burst, and it is why this build exists rather than
waiting.

## Expected improvements
- The fan-out guard stops admitting an unbounded cap below an unterminated template literal.
- Lens prose naming a primitive stops being read as a call, closing the last of the class
  `aLexedStripper` removed from rule 2.
- The map's definition probe stops swallowing definitions after a block-opener written in a line
  comment, which costs the `d41ly/incms` adopter 14 definitions across 9 files today.

## Detriments if this is not built
- A guard with a known, reproduced fail-open ships to every adopter, and the shape that triggers it
  is an ordinary editing accident rather than an attack.
- The map keeps under-indexing a layer the charter makes a Definition-of-Ready input, and the
  adopter's 14 stay invisible with no symptom but a coverage gap.

## Build-level rules
- **Every unit is measured against the SHIPPED code before it is specced**, and the measurement
  names which RULE fired rather than only the exit code. The first fixture for `-4` showed all-DENY
  and proved nothing, because an unbounded receiver made rule 2 deny first and mask rule 3.
- **A null result is a claim.** `aLexedStripper` recorded two findings as refuted on fixtures that
  could not reach their mechanism, and both were real. Any "does not reproduce" here states the
  isolation that makes it meaningful.
- **Never widen a guard's blind spot to fix its false positives**, and never narrow its reach to fix
  a fail-open. Both directions get a fixture in the same commit as the change.
- **A fix keyed to POSITION is not a fix.** `aLexedStripper` red the bar on a waiver keyed to a line
  number that its own edit moved.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aPairedLexer-1` | 2 | rule 3 stops being blind below an unterminated template literal (was `TOOL-aLexedStripper-4`) |
| 2 | `TOOL-aPairedLexer-2` | 2 | rule 1 stops reading prose in a template literal or block comment as a call (was `TOOL-aLexedStripper-3`) |
| 3 | `TOOL-aPairedLexer-3` | 2 | the map's definition probe strips line comments before block ones (was `TOOL-aLexedStripper-7`) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-08-30 · streams tooling
ids TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPairedLexer-1 — rule 3 stops being blind below an unterminated template](spec/2026-08-30-spec-TOOL-aPairedLexer-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-08-30 |
| [TOOL-aPairedLexer-2 — rule 1 stops reading a lens prompt as a call](spec/2026-08-30-spec-TOOL-aPairedLexer-2.md) | 2 | 2 | SPECCED | rev-1 | 2026-08-30 |
| [TOOL-aPairedLexer-3 — the definition probe strips comments in one pass](spec/2026-08-30-spec-TOOL-aPairedLexer-3.md) | 3 | 2 | SPECCED | rev-1 | 2026-08-30 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPairedLexer-1` | no |
| 2 | `TOOL-aPairedLexer-2` | no |
| 3 | `TOOL-aPairedLexer-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

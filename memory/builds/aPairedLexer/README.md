---
slug: aPairedLexer
node: a
opened: 2026-08-30
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3 TOOL-aPairedLexer-4 TOOL-aPairedLexer-5 TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12
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
- **Measure against SHIPPED code before speccing, and name the RULE that fired**, not the exit code.
  Unit 4's first fixture showed all-DENY and proved nothing: an unbounded receiver made rule 2 deny
  first, masking rule 3.
- **A null result is a claim.** Two findings were recorded refuted on fixtures that could not reach
  their mechanism, and both were real. State the isolation that makes it meaningful.
- **Never widen a guard's blind spot to fix a false positive**, nor narrow its reach to fix a
  fail-open. Both directions, one commit.
- **A fix keyed to POSITION is not a fix** — a line-numbered waiver, moved by its own edit, thrice.
- **Stop mitigating a missing model; build the model.** Three revisions of one function each shipped
  a fail-open, all three compensating for one absence: the views modelled no regex literal. Each
  mitigation died to a different spelling of the one ambiguity, and each passed every existing arm.
- **An accepted ceiling can be a SYMPTOM.** The block-comment blind spot was priced twice as its own
  problem and retired for free once regex literals were modelled. Price a ceiling against its CAUSE.
- **Units 6-12 exist because the round-2 loop went NON-CONVERGENT**: 2 blockers, then 5. Not
  strictly smaller, so M4 STOPS the loop and PROMOTES every standing blocker to a unit — specced,
  built, closed, audited as a SPEC not re-reviewed as a diff. The owner promoted the 2 HIGHs too.
  All seven classified MISSING.
- **A fix that removes its own fixture's TRIGGER is unverified.** Repairing the lexer (7, 8) removes
  the trigger units 9-11 rely on, making three live defects look fixed — measured. Their fixtures use
  an AMBIGUOUS-position trigger, surviving both repairs. Unit 6 lands first: it holds whatever the
  heuristic decides.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aPairedLexer-1` | 2 | rule 3 stops being blind below an unterminated template literal (was `TOOL-aLexedStripper-4`) |
| 2 | `TOOL-aPairedLexer-2` | 2 | rule 1 stops reading prose in a template literal or block comment as a call (was `TOOL-aLexedStripper-3`) |
| 3 | `TOOL-aPairedLexer-3` | 2 | the map's definition probe strips line comments before block ones (was `TOOL-aLexedStripper-7`) |
| 4 | `TOOL-aPairedLexer-4` | 2 | both views model REGEX LITERALS, which retires the block-comment ceiling and closes review D2-D5 |
| 5 | `TOOL-aPairedLexer-6` | 2 | `renderCodeView` gains the per-line `dirty` half, so a DECLINED slash announces itself (round-2 D3) |
| 6 | `TOOL-aPairedLexer-7` | 2 | start of input becomes a REGEX position — `'})]'.includes('')` is `true`, so it was a division position (round-2 D1) |
| 7 | `TOOL-aPairedLexer-8` | 2 | the regex/division test decides on the previous TOKEN, not the previous character, in one shared predicate (round-2 D2) |
| 8 | `TOOL-aPairedLexer-9` | 2 | rule 3 keeps the paren-safe view for join work and uses the fallback ONLY for `intConsts` bindings (round-2 D4) |
| 9 | `TOOL-aPairedLexer-10` | 2 | the cross-check iterates the UNION and DELETES a name only one view binds, instead of exempting it (round-2 D5) |
| 10 | `TOOL-aPairedLexer-11` | 2 | rule 2 calls the same corrected merge as rule 3, from one helper (round-2 D6) |
| 11 | `TOOL-aPairedLexer-12` | 2 | `render_comment_free` blanks comment text INSIDE a template span, so a phantom span cannot RESURRECT a comment (round-2 D7) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 4 unit(s) · node a · opened 2026-08-30 · streams tooling
ids TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3 TOOL-aPairedLexer-4 TOOL-aPairedLexer-5 TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPairedLexer-1 — rule 3 stops being blind below an unterminated template](spec/2026-08-30-spec-TOOL-aPairedLexer-1.md) | 1 | 2 | SPECCED | rev-2 | 2026-08-30 |
| [TOOL-aPairedLexer-2 — rule 1 stops reading a lens prompt as a call](spec/2026-08-30-spec-TOOL-aPairedLexer-2.md) | 2 | 2 | SPECCED | rev-2 | 2026-08-30 |
| [TOOL-aPairedLexer-3 — the definition probe strips comments in one pass](spec/2026-08-30-spec-TOOL-aPairedLexer-3.md) | 3 | 2 | SPECCED | rev-2 | 2026-08-30 |
| [TOOL-aPairedLexer-4 — both views model regex literals, and the ceiling retires](spec/2026-08-30-spec-TOOL-aPairedLexer-4.md) | 4 | 2 | SPECCED | rev-1 | 2026-08-30 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aPairedLexer-4.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPairedLexer-1` | no |
| 2 | `TOOL-aPairedLexer-2` | no |
| 3 | `TOOL-aPairedLexer-3` | no |
| 4 | `TOOL-aPairedLexer-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

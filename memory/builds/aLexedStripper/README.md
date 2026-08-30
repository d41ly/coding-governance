---
slug: aLexedStripper
node: a
opened: 2026-08-30
streams: tooling
roster: TOOL
ids: TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-3 TOOL-aLexedStripper-4 TOOL-aLexedStripper-5 TOOL-aLexedStripper-6 TOOL-aLexedStripper-7
authorized-by: prompt
---

# aLexedStripper — two kit scanners stop reading prose as code

## The problem this build exists to solve
Two shipped kits scan source with regexes that do not know what language they are reading, and both
mis-read ordinary prose as code. `codebase-map`'s `_identifier_tokens` applies C comment syntax to
every language: a MIME glob in a Python docstring opened a span that swallowed 674 lines, taking one
file to 18.8% recall. `agent-cap`'s lens counter reads template prose as bracket structure, denying
a correct five-lens harness. Both were found by the `d41ly/incms` adopter and filed there as gov
asks, because both files are role `engine` in that tree. Measurements, and everything else this
build learned, are in `build/2026-08-30-build-TOOL-aLexedStripper-2-base-measurements.md`.

## Expected improvements
- The reuse audit the charter mandates can see Python, TypeScript and shell identifiers again.
- A correct five-lens harness stops being denied for its English, here and in every adopter.
- Both fixes land UPSTREAM, so adopters take them by re-pull with no role flip and no local delta.

## Detriments if this is not built
- Every DoR reuse audit in both trees keeps reading a corpus with most identifiers deleted, and
  reports "no existing seam fits" for seams that are there.
- Adopters keep writing lens prose around a counter's punctuation bugs, following a gotcha whose
  prescribed remedy is measured to fix nothing.

## Build-level rules
- **Upstream is the side.** The adopter's blocker — flip the role, insert a delta, red kit-sync,
  wait on a BLOCKED receipt migration — is a property of THEIR tree. In gov both files are `engine`.
- **A stripper is a lexer, not a regex chain.** Comments and strings exclude each other and no
  ordering of separate passes expresses that.
- **Never widen a guard's blind spot to fix its false positives.** A view that blanks anything can
  hide a fan-out; this build shipped that defect twice before measuring it.
- **Both instruments are measured before and after over the same real corpus**, and every fix is
  gated by its own failing case observed RED first.
- **A null result is a claim.** "It did not reproduce" and "it was contention" each owe the same
  evidence a positive finding does. Both were wrong here until tested.

## Parked decisions
Two entries in `RUN.md`, and the second corrects the first. Landing publishes five
`TOOL-aGradedDoorway-7` commits this build did not author, already on local main before the session
began. The first entry justified that partly on their blocking another session; that reason measured
the WRONG REPOSITORY and is withdrawn. The decision stands on the two that survive: they are already
merged to the trunk with the charter's `--no-ff` landing shape, and `--landed` records
`unpushed-at-landing` so the fact is visible rather than silent.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aLexedStripper-1` | 2 | `_identifier_tokens` becomes one language-aware pass over a per-suffix comment/string profile |
| 2 | `TOOL-aLexedStripper-2` | 2 | `agent-cap`'s bounded-receiver view becomes a line-aligned, interpolation-preserving `renderCodeView` |
| 3 | `TOOL-aLexedStripper-5` | 2 | an unterminated scan falls back to the view it replaced, so a backtick in a regex literal stops denying a legal script |
| 4 | `TOOL-aLexedStripper-6` | 2 | a seventh profile field: an f-string replacement field is code, not string |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-08-30 · streams tooling
ids TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-3 TOOL-aLexedStripper-4 TOOL-aLexedStripper-5 TOOL-aLexedStripper-6 TOOL-aLexedStripper-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aLexedStripper-1 — `_identifier_tokens` becomes one language-aware pass](spec/2026-08-30-spec-TOOL-aLexedStripper-1.md) | 1 | 2 | CLOSED | rev-3 | 2026-08-30 |
| [TOOL-aLexedStripper-2 — `agent-cap`'s lens counter reads a template-aware view](spec/2026-08-30-spec-TOOL-aLexedStripper-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-08-30 |
| [TOOL-aLexedStripper-5 — an unterminated scan falls back to the view it replaced](spec/2026-08-30-spec-TOOL-aLexedStripper-5.md) | 3 | 2 | CLOSED | rev-3 | 2026-08-30 |
| [TOOL-aLexedStripper-6 — a seventh profile field: the interpolation pair](spec/2026-08-30-spec-TOOL-aLexedStripper-6.md) | 4 | 2 | CLOSED | rev-3 | 2026-08-30 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aLexedStripper-5 TOOL-aLexedStripper-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aLexedStripper-1` | no |
| 2 | `TOOL-aLexedStripper-2` | no |
| 3 | `TOOL-aLexedStripper-5` | no |
| 4 | `TOOL-aLexedStripper-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

---
slug: aSurfacedLexicon
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
ids: TOOL-aSurfacedLexicon-1 TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-10 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-15 TOOL-aSurfacedLexicon-16
---

# aSurfacedLexicon — the lexicon stops grading two surfaces and starts declaring all of them

## The problem this build exists to solve

The kit promises a per-purpose vocabulary across a project's surfaces plus an owner-configurable
naming convention. It grades two surfaces — function definitions against `VERBS`, type names against
`BANNED_SUFFIXES` — and enforces no naming convention at all: there is no camel/snake/kebab/pascal
predicate anywhere in `tools/lexicon/`.

The half that exists has a measured contribution of zero. Since `.lexicon.conf` landed on 2026-08-16
this repo added 136 definitions and zero offenders, and the gate refused nothing across three firings
and three pin raises. `TOOL-dScaffoldedMirror-16` recorded it: the DECLARATION constrains what gets
written, the ENFORCEMENT contributes nothing. Adding surfaces without fixing that ordering buys more
of the same.

## Expected improvements

- A declared surface set, so "per surface" names something a checker enumerates rather than two
  hardcoded extractor calls.
- A convention predicate per (language, surface) with shipped defaults — the half of the stated
  purpose that has never existed.
- An adoption path a 14,000-definition repo keeps rather than waives.
- A recorded answer to whether vocabulary and convention belong in one tool.

## Detriments if this is not built

- Every adopter reading the kit's README gets a naming-convention promise the code does not carry.
- The three open `TOOL-aFlaggedScaffold` rows keep it installing broken on real adopters, so the zero
  enforcement contribution has a second cause nobody has separated from the first.
- `dScaffoldedMirror` stays DEFERRED with 22 ids, several of them this rebuild's early phases, and
  the next session here re-derives the same diagnosis.

## Build-level rules

- **The anti-mirror rule survives the rebuild.** The corpus is admitted as evidence for exactly one
  thing: which spellings become debt. No predicate's standard may be derived from the population it
  grades. `TOOL-dScaffoldedMirror-8` and the `canon.py` header carry the reasoning.
- **Frozen is a posture, not a wall.** Owner ruling this session: the canon ships frozen and the owner
  can unfreeze it. The unfreeze must be visible on every run and recorded where a later reader finds
  it, because a quiet unfreeze is the mirror defect with an extra step.
- **Measure, never estimate.** The prior research pass estimated one predicate's population at 484;
  the kit's own extractor measured 6. Every number in this build carries the command that produced it.
- **A new predicate is not landed until its failing case has been observed.** Stage the break,
  confirm RED, unstage. §7, and it binds hardest on a predicate this repo has never run.
- **No new bar leg without its wall-clock ceiling and its `testsuite-count-waivers.txt` row.**
- **A kit self-test may not be added to the bar.** Owner ruling of 2026-08-23.

## Parked decisions

- **RULED, not parked: P3 goes and the other two stay.** The design pass measured the import-direction
  predicate at 44 of 548 imports judgeable, a green line overstating its reach twelvefold, with its
  pin written once as `"0"` across 17 commits. Vocabulary and convention stay in one tool because they
  share one corpus walk and one declaration. All ten open questions are ruled in the owner-rulings
  record; four went against the recommendation and the unit count is 13, not 11.
- **The three `TOOL-aFlaggedScaffold` govkit defects are out of scope and in the way.** `-3` cannot
  land a source gov started shipping, `-4` crashes with a traceback on a large adopter under Windows,
  and `-5` calls a kit adopted on the exit code alone. A rebuilt kit that ships through the same
  installer inherits all three. Routing around them is this build's problem; fixing them is not.
- **Retirement was never recorded.** The session that concluded the tool is better retired than
  maintained left no in-repo record — searched across `DECISIONS.md`, all four backlog shards, every
  build README, and the recall index. The closest record, `TOOL-dScaffoldedMirror-16`, concluded the
  opposite. This build proceeds on the owner's rebuild instruction and notes that its evidence is
  not available here.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 0 | `TOOL-aSurfacedLexicon-1` | 2 | measure the shipped kit against the five goals, then design and adversarially judge the rebuild |
| 1 | `TOOL-aSurfacedLexicon-2` | 2 | delete P3, keep its one real constraint on the declarations leg |
| 1 | `TOOL-aSurfacedLexicon-3` | 2 | one corpus walk, two passes, two fewer modes |
| 2 | `TOOL-aSurfacedLexicon-4` | 2 | the CELLS and PINS declaration grammar, and the two-sided pin equality |
| 3 | `TOOL-aSurfacedLexicon-5` | 2 | the convention predicate — set membership over an affix-stripped core |
| 3 | `TOOL-aSurfacedLexicon-9` | 2 | the owner-declarable PATTERNS block |
| 4 | `TOOL-aSurfacedLexicon-6` | 2 | the three cell refusals and the per-cell coverage report |
| 4 | `TOOL-aSurfacedLexicon-13` | 2 | the prefix selector, routing a subset of a cell to a second convention |
| 4 | `TOOL-aSurfacedLexicon-14` | 2 | a real shell parser, arming the shell function cell |
| 5 | `TOOL-aSurfacedLexicon-7` | 2 | P1 splits into DEBT and UNRULED, and DEBT names its replacement |
| 6 | `TOOL-aSurfacedLexicon-8` | 2 | `--suggest` becomes surface-aware and answers in the declared convention |
| 6 | `TOOL-aSurfacedLexicon-10` | 2 | `--expand`, the one-time widening the canon bounds |
| 6 | `TOOL-aSurfacedLexicon-11` | 2 | the canon overlay and its stamp |
| 7 | `TOOL-aSurfacedLexicon-12` | 2 | the conf rewrite, the owed records, and the spec-template cell line |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 14 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aSurfacedLexicon-1 TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-10 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12
ids TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-15 TOOL-aSurfacedLexicon-16

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSurfacedLexicon-1 — the design pass: measure the kit, then design and judge its rebuild](spec/2026-09-04-spec-aSurfacedLexicon-1.md) | 0 | 2 | CLOSED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-2 — delete P3, keep its one real constraint](spec/2026-09-04-spec-aSurfacedLexicon-2.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-3 — one corpus walk, two passes, two fewer modes](spec/2026-09-04-spec-aSurfacedLexicon-3.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-4 — the CELLS and PINS declaration grammar](spec/2026-09-04-spec-aSurfacedLexicon-4.md) | 2 | 2 | SPECCED | rev-3 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-5 — the convention predicate](spec/2026-09-04-spec-aSurfacedLexicon-5.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-9 — the owner-declarable PATTERNS block](spec/2026-09-04-spec-aSurfacedLexicon-9.md) | 3 | 2 | SPECCED | rev-2 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-13 — the prefix selector, routing a subset of a cell to a second convention](spec/2026-09-04-spec-aSurfacedLexicon-13.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-14 — a real shell parser, arming the shell function cell](spec/2026-09-04-spec-aSurfacedLexicon-14.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-6 — the three cell refusals and the per-cell coverage report](spec/2026-09-04-spec-aSurfacedLexicon-6.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-7 — P1 splits into DEBT and UNRULED, and DEBT names its replacement](spec/2026-09-04-spec-aSurfacedLexicon-7.md) | 5 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-10 — `--expand`, the one-time widening the canon bounds](spec/2026-09-04-spec-aSurfacedLexicon-10.md) | 6 | 2 | SPECCED | rev-2 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-11 — the canon overlay and its stamp](spec/2026-09-04-spec-aSurfacedLexicon-11.md) | 6 | 2 | SPECCED | rev-2 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-8 — `--suggest` becomes surface-aware and answers in the declared convention](spec/2026-09-04-spec-aSurfacedLexicon-8.md) | 6 | 2 | SPECCED | rev-2 | 2026-09-04 |
| [TOOL-aSurfacedLexicon-12 — the conf rewrite, the owed records, and the spec-template cell line](spec/2026-09-04-spec-aSurfacedLexicon-12.md) | 7 | 2 | SPECCED | rev-3 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: TOOL-aSurfacedLexicon-10 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7
TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9.

Ids no `spec-audit` record has ever named: TOOL-aSurfacedLexicon-1 TOOL-aSurfacedLexicon-10 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5
TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-7 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 0 | `TOOL-aSurfacedLexicon-1` | no |
| 1 | `TOOL-aSurfacedLexicon-2`, `TOOL-aSurfacedLexicon-3` | yes |
| 2 | `TOOL-aSurfacedLexicon-4` | no |
| 3 | `TOOL-aSurfacedLexicon-5`, `TOOL-aSurfacedLexicon-9` | yes |
| 4 | `TOOL-aSurfacedLexicon-13`, `TOOL-aSurfacedLexicon-14`, `TOOL-aSurfacedLexicon-6` | yes |
| 5 | `TOOL-aSurfacedLexicon-7` | no |
| 6 | `TOOL-aSurfacedLexicon-10`, `TOOL-aSurfacedLexicon-11`, `TOOL-aSurfacedLexicon-8` | yes |
| 7 | `TOOL-aSurfacedLexicon-12` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

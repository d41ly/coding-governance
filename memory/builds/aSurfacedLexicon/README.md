---
slug: aSurfacedLexicon
node: a
opened: 2026-09-04
streams: tooling
status: OPEN
roster: TOOL
ids: TOOL-aSurfacedLexicon-1
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

- **Whether the three current predicates belong in one tool with a convention gate is open.** Verb
  vocabulary, banned type suffixes and forbidden import directions are three unrelated questions
  wearing one kit name, and adding a fourth may be the wrong move. Put to the design pass rather than
  assumed either way.
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

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aSurfacedLexicon-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

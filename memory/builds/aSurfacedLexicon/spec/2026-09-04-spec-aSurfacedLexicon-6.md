# TOOL-aSurfacedLexicon-6 — the three cell refusals and the per-cell coverage report

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Give the (language, surface) cell matrix its refusals, so a declared cell that grades nothing reds
instead of reporting a reassuring zero, and an ungraded population with no cell row reds instead of
being silently skipped. The same unit makes every declared cell — dark rows included — appear in one
report that prints each cell's population RULE beside its count, because a count with no denominator
context reads as coverage when it is only a scope.

## 2. Scope (IN)

- **S1** — `UNDECLARED CELL`: a (extension, surface) pair with a non-empty population and no `CELLS`
  row is a refusal. This is the cell-level sibling of the shipped `UNDECLARED EXTENSIONS` arm at
  `tools/lexicon/lexicon.py:524`, which grades extensions and cannot see a surface.
- **S2** — `DEAD CELL`: a declared, armed cell whose population is zero is a refusal. Today the same
  fact is printed and does not red: `tools/lexicon/lexicon.py:745-747` emits `armed but grading
  nothing (reported, not a refusal)` and the current tree prints `.js suffix=0` on every green run.
  S2 promotes that line to a verdict and re-keys it from `(extension, predicate)` onto the declared
  cell.
- **S3** — the per-cell report: one row per `CELLS` row, in declaration order, including every `dark`
  row, printed on green as well as red. A declared cell absent from the report is a reporting bug and
  the report's own row count is asserted against the parsed `CELLS` row count.
- **S4** — every report row carries the POPULATION RULE that selected its denominator, as a short
  declared string beside the count, not the count alone. Owner ruling Q6 makes this obligatory rather
  than cosmetic, because `py.constant` arms on a population its own predicate selects.
- **S5** — the `py.constant` cell ships armed at the public-simple-assignment population with its
  rule string, and `.lexicon.conf` carries all three measured readings in a comment so the next
  session reads them instead of re-deriving them.
- **S6** — both refusals land with their failing case OBSERVED, and S2's costs nothing to stage:
  `js.type` is a zero population in this tree today.
- **S7** — a liveness assertion on the report itself: a run whose cell report has zero rows REFUSES
  rather than printing an empty table under a green line.

## 3. Non-goals (OUT)

- The `CELLS:` and `PINS:` block grammar. That is `TOOL-aSurfacedLexicon-4`, and this unit consumes
  the parsed rows rather than parsing them.
- The convention predicate itself, its six forms and its AMBIGUOUS verdict. That is
  `TOOL-aSurfacedLexicon-5`. This unit refuses cells; it does not grade names.
- The pin comparison in either direction. Owner ruling Q2 made the ratchet two-sided and that lives
  with the pin block in `TOOL-aSurfacedLexicon-4`.
- Deleting the shipped per-extension `DEAD PROBE` arm. Whether it survives alongside `DEAD CELL` is
  the first fork in section 8, and either answer is a separate edit.
- Draining the seven `py.file` violations. Owner ruling Q3 files those as their own unit.

## 4. Design

### Data model

A cell is the pair already keyed at `tools/lexicon/lexicon.py:546`, widened from
`(extension, predicate)` to `(extension, surface)` where surface is the closed set `function`,
`type`, `file`, `constant`. Each declared cell resolves to a record carrying four fields: the cell
key, the declared convention, the arms (`vocab`, `notail`), and a POPULATION RULE.

The population rule is a pair — a selector the engine runs, and a short human string the report
prints. The string is DECLARED beside the selector in the engine, never derived from a docstring:
a rule string derived from prose rots the moment the selector is edited and nothing compares them.

### Inventory

The report prints one row per declared cell. The row shape carries, in order: the cell key, the
declared convention or `dark`, the graded count, the denominator the rule selected FROM, and the rule
string. For the cell owner ruling Q6 arms, that reads as `py.constant screaming 331 graded of 527
module-body targets (rule: public simple assignments)`.

The denominator is the WIDER population the rule narrowed, not the graded count restated. A row whose
graded count equals its denominator is legal and common — `py.function` grades all 925 — and the
point of printing both is that `py.constant` does not.

### The three verdicts, and which population each selects

`UNDECLARED CELL` selects (extension, surface) pairs the extractors produced a non-empty population
for, minus the pairs `CELLS` declares. `DEAD CELL` selects declared non-dark cells whose graded count
is zero. The report selects every `CELLS` row and refuses none of them. The three populations are
deliberately different: two of them can be empty in a healthy tree and the third cannot, which is why
only the third carries the liveness assertion in S7.

A `dark` cell row is a declared refusal and is exempt from `DEAD CELL` by construction — its
population is zero because nothing extracts it, and redding that would make the honest declaration
the failing one. It still prints a report row, which is the whole reason dark is written down.

### The measured populations this unit ships

Re-measured on this worktree at `d0a18683` on 2026-09-04 by a scratchpad `ast` walk over the 47
tracked `.py` files that `git ls-files` returns, module body only, leading and trailing underscores
stripped before the screaming test. The rule in each row's first column IS the reading that produced
its numbers.

| Population rule | graded | satisfying screaming | violations |
|---|---|---|---|
| All module-body assignment targets, tuple unpack included | 527 | 419 | 108 |
| Simple single-`Name` targets only | 432 | 413 | 19 |
| Public simple targets, no leading underscore | 331 | 331 | 0 |

The research record states the first row as 539 rather than 527. Its screaming numerator of 419
reproduces exactly and its denominator does not; adding module-body `for`, `with` and augmented
targets moves the denominator to 560 rather than to 539, so the 12-target gap is UNRECONCILED and the
conf comment carries the re-measured 527 with the reading that produced it.

The third row is what owner ruling Q6 arms, and the reason the rule string is not optional is visible
in the table: the clean zero belongs to the population defined by excluding the leading underscore,
and the leading underscore is what correlates with mutable module state in this corpus.

### Files touched (estimate)

`tools/lexicon/lexicon.py` for the two refusals and the report, `tools/lexicon/selftest.py` for the
staged-break arms, `.lexicon.conf` for the `py.constant` row and its comment. No new module: the
research record's zero-new-top-level-modules constraint holds here because `govkit update` classifies
by iterating the receipt, so a file gov newly ships is outside the classification space.

### Alternatives rejected

Printing the count alone and putting the rule in the README. Rejected under owner ruling Q6: the
mitigation is the line the reader sees on the run, and a README is not on the run.

Deriving the rule string from the selector function's docstring. Rejected because that is a second
carrier of one fact with no gate comparing them, which is the class this build exists to close.

Making `DEAD CELL` a warning rather than a refusal. Rejected: the shipped code already warns, on
every green run, and the warning has stood for the whole life of the declaration without anything
changing. A warning nobody acts on is the green-by-absence class wearing a different label.

## 5. Production-readiness checklist

- security — N/A. The unit adds no write path, no network call and no new input surface; it reads the
  declaration the engine already reads.
- perf / scale — the report is a walk over declared rows, bounded by the `CELLS` block, and the two
  refusals reuse the corpus walk that already runs. The `lexicon naming predicates` leg's ceiling is
  300 s in `tools/gate-legs.json`; the addition is not expected to approach it and the landing run
  must confirm rather than assume.
- a11y — N/A. A CLI gate with no user interface.
- i18n — N/A. Machine-facing output in one language, and the wider non-ASCII identifier gap is filed
  as review finding D25 against `subtokens.py` rather than owned here.
- error / empty / loading states — the empty case IS the product: a zero-row report refuses (S7), a
  zero-population armed cell refuses (S2), and a dark row prints as a refusal rather than as absence.
- observability — every declared cell appears on every run, green included, with its count, its
  denominator and its rule.
- risks — the leg guard gap in section 8's second fork is the live one: the failing case this unit
  ships is a conf edit, and the leg that grades conf content is not selected by a conf-only diff.
- testing + left-shift gates — both refusals get a staged-break arm in `tools/lexicon/selftest.py`,
  and S2's break needs no staging at all in this tree.
- migration / rollback — the conf gains rows and a comment; reverting the commit reverts the
  declaration with it. No stored state, no artifact, nothing to migrate.
- user docs — `tools/lexicon/README.md` gains the three verdicts and what each does NOT check, and
  the rendered Skill's byte-compare on the `lexicon wiring` leg forces the re-render if a placeholder
  moved.

## 6. Acceptance criteria

- **AC1** — When a `js.type pascal` row is added to `.lexicon.conf` and nothing else is staged,
  `python tools/lexicon/lexicon.py --check` exits non-zero naming `js.type` as a DEAD CELL; with the
  row removed it exits `0`. The population is zero across the 11 tracked `.js` files, measured by
  `python tools/lexicon/lexicon.py --check` today, which prints `.js suffix=0` and exits `0`.
- **AC2** — When a `class Cap {}` definition is staged into a tracked `.js` file while no `js.type`
  row is declared, `python tools/lexicon/lexicon.py --check` exits non-zero naming `js.type` as an
  UNDECLARED CELL; unstaging it returns the run to `0`.
- **AC3** — When `python tools/lexicon/lexicon.py --check` runs green, the cell report prints one row
  for every row of the `CELLS` block in `.lexicon.conf`, dark rows included, and a `tools/lexicon/selftest.py`
  arm asserts the printed row count equals the parsed row count.
- **AC4** — When the report prints the constant cell, the row carries the graded count, the wider
  denominator and the rule string in one line, and a `tools/lexicon/selftest.py` arm reds on a row
  carrying a count with no rule string.
- **AC5** — When `.lexicon.conf` is read, its constant-cell comment carries all three measured
  readings — 527 against 419, 432 against 413, and 331 against 331 — each with the reading that
  produced it, and a `tools/lexicon/selftest.py` arm asserts the armed row names the third.
- **AC6** — When the cell report's row source is emptied so it would print no rows,
  `python tools/lexicon/lexicon.py --check` REFUSES naming the empty report rather than exiting `0`;
  the break is staged, the RED observed, and the break unstaged.
- **AC7** — When the existing per-extension arm is exercised by declaring an armed extension the
  corpus contains no definitions for, `python tools/lexicon/lexicon.py --check` still prints its
  `DEAD PROBE` refusal, so this unit is proven not to have replaced it by accident.
- **AC8** — When only `.lexicon.conf` changes in a diff, `bash tools/run-gates/run-gates.sh` selects
  the `lexicon naming predicates` leg. Today it does not: that leg's guard in `tools/gate-legs.json:931`
  names `tools/`, `skills/session-kickoff/`, `.githooks/` and `.claude/`, and the conf is at the repo
  root. Observed by running the bar over a conf-only diff before and after the guard edit.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no gate leg, so it owes no wall-clock ceiling row and no
`testsuite-count-waivers.txt` entry. It adds arms to the existing `lexicon selftest` leg, whose
declared ceiling is 880 s; the landing run must re-measure that leg rather than assume the arms are
free, and the current cost is UNVERIFIED here because the research pass did not run it.

## 8. Open questions

- **F1 — does the shipped per-extension `DEAD PROBE` arm survive beside `DEAD CELL`, or is it
  subsumed?** `DEAD CELL` is strictly finer wherever a cell is declared: it fires on `js.type` where
  `DEAD PROBE` cannot, because `DEAD PROBE` sums the verb and suffix populations per extension at
  `tools/lexicon/lexicon.py:610` and `.js` keeps a healthy 122 functions. But the two select different
  populations at the edges — an armed extension with no `CELLS` row at all is invisible to `DEAD CELL`
  and visible to `DEAD PROBE`. Recommendation: keep both, and make the report say which arm owns which
  population, because a refusal whose scope a reader has to derive is the class this build is closing.
- **F2 — widen the `lexicon naming predicates` guard to include the declaration, or leave the conf to
  the wiring leg?** The leg that grades conf CONTENT is not selected by a conf-only diff, and the
  failing case this unit ships is a conf-only diff. The `lexicon wiring` leg carries an empty guard
  and does fire, but it byte-compares the rendered Skill and does not run the predicates.
  Recommendation: add the declaration to the predicates leg's guard in this unit, because the
  alternative is a refusal whose own acceptance criterion cannot be reproduced by the bar that owns
  it. The cost is that every conf edit now pays the predicates leg, which is a 300 s ceiling and
  measured far below it.
- **F3 — which population does the constant cell arm on?** Three readings are defensible and only one
  yields a clean zero, and it is clean because the predicate selects the names it grades.
  RESOLVED (owner, 2026-09-04): arm it on the 331 public simple targets, with the per-cell report
  printing the population rule beside the count as the non-optional mitigation. Recorded in the
  build's owner-rulings record as Q6.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, from the rebuild research record's unit U5 plus owner ruling
  Q6, which adds the population-rule obligation and the constant cell that makes it load-bearing.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a declared check whose graded population is zero
and report each cell's population rule"` ranks `check` and `report` as seams, and the affordance line
for `run-gates` under the stems `declar` and `popul`. None of them is the seam this unit extends. The
seam is inside the lexicon kit and the probe surfaced it obliquely rather than by name: the verdict
half extends `run` in `tools/lexicon/lexicon.py`, which already owns three refusal populations
(`UNDECLARED EXTENSIONS` at `:524`, `DEAD PROBE` at `:612`, `DEAD SNIFFER` at `:665`) and one
report-only line at `:745`. This unit adds a fourth and a fifth refusal to that same list and promotes
the report-only line, rather than adding a checker beside it. The retrieval run also named
`vacuous-selector-empty-population.md` in the gotcha inventory, which is the class both refusals
belong to, and `TOOL-dScaffoldedMirror-3`, whose ruling already established the shape this unit's
report follows — print the graded count, the excluded count and the rule that excluded them, on every
run.

Recall terms used: `python tools/memory-recall/query.py "why does the lexicon refuse an armed check
whose population is zero, and what must a per-cell report print beside a count" --terms "lexicon DEAD
PROBE vacuity armed cell green-by-absence population denominator coverage sniffer graded pin refusal"
--k 8`.

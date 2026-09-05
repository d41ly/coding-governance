# TOOL-aSurfacedLexicon-5 — the convention predicate

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Build the naming-convention predicate the kit's README has promised since adoption and never shipped:
a classifier that answers which case conventions an identifier satisfies, and a verdict that reds when
the convention its cell declares is not among them. Verified at writing time, no case-style predicate
exists anywhere in `tools/lexicon/` — the only case-aware code is `run_suggest`'s re-caser at
`tools/lexicon/lexicon.py:837-838`, which re-cases an answer rather than grading a name.

## 2. Scope (IN)

- **S1** — six anchored regexes over a stripped core, held as one `_FORMS` mapping in
  `tools/lexicon/subtokens.py`: `snake`, `screaming`, `camel`, `pascal`, `kebab`, `dot`. Each is a
  single anchored pattern. `dot` is a classifier form only; the declarable convention set is
  `TOOL-aSurfacedLexicon-4`'s and holds the other five plus `dark`.
- **S2** — affix strip BEFORE classification, lifted verbatim from the prototype record:
  `_AFFIX = re.compile(r"^(_*)(.*?)(_*)$", re.DOTALL)`. Leading and trailing underscores are privacy
  markers, not case. This is the largest single source of false positives the prototype found, and
  without it `__init__` and `_build_index` are reported as snake violations.
- **S3** — `classify(name)` returns the SET of forms the core satisfies, lifted verbatim:
  `return {k for k, rx in _FORMS.items() if rx.match(core)}`. Set-valued, never a single label.
- **S4** — the verdict rule: a name violates a cell when the declared convention is NOT IN its set,
  never when it is not the set's first or only member. The message names what the name DOES satisfy,
  in the prototype's observed shape `VIOLATION  loadUserData  satisfies camel, not snake`.
- **S5** — the AMBIGUOUS verdict. A name whose core is non-empty and whose set is empty REDS, with a
  message distinct from `VIOLATION`, per the owner's Q7 ruling. It ships exercised only by a staged
  fixture, because the measured in-corpus population is zero.
- **S6** — file cells grade the basename up to its FIRST dot. `map_extractors.template.py` grades on
  `map_extractors`; `check-arms.test.sh` grades on `check-arms`.
- **S7** — the classifier is `subtokens.py`'s SIBLING, not its consumer. `subtokens()` lowercases at
  `subtokens.py:26`, so its output cannot answer a case question. Both live in the same module,
  neither calls the other, and the module docstring gains the sentence saying so.
- **S8** — the alternate-cell teeth line. Every run prints, per armed cell, how many names the OTHER
  conventions would violate, so a cell that only ever passes cannot be mistaken for one that has been
  tested.

## 3. Non-goals (OUT)

- The declaration grammar. `CELLS` and `PINS` parsing, the closed surface and convention sets, and the
  extension-absent-from-`LANGS` refusal are `TOOL-aSurfacedLexicon-4`.
- The `UNDECLARED CELL` and `DEAD CELL` refusals, the per-cell coverage report, and Q6's requirement
  that a `py.constant` row print its population RULE beside its count. All belong to the cell-refusal
  unit, which owns population sizes.
- `--suggest` re-casing to the declared convention. That is the surface-aware suggest unit.
- The prefix and decorator selector Q10 added to the build, and the shell parser Q5 added. Both route
  a SUBSET of a cell's population to a different convention, and neither is reachable from a
  classifier that sees one name at a time.
- Deciding which cells ship armed. This unit builds the predicate; the conf rewrite arms it.
- Anything about non-ASCII identifiers. The research record files an unreviewed finding that
  `subtokens.py` is ASCII-only; the classifier this unit adds inherits that exposure and does not
  widen it, and it needs its own backlog row rather than a quiet fix here.

## 4. Design

### Data model

`classify(name) -> set[str]` over a core produced by `read_core(name)`. Three verdicts per graded
name, and the third is the one Q7 created.

| Verdict | Condition | Reds |
|---|---|---|
| SATISFIED | declared convention is in the set | no |
| VIOLATION | set is non-empty and the declared convention is not in it | yes |
| AMBIGUOUS | core is non-empty and the set is empty | yes, with a distinct message |

The six forms, each a single anchored regex over the stripped core. `dot` earns its place by keeping
a dotted name out of AMBIGUOUS and by letting a message name what a dotted name does satisfy.

| Form | Matches | Does not match |
|---|---|---|
| `snake` | `build_index`, `run`, `x2` | `buildIndex`, `Build_Index` |
| `screaming` | `PIN_KEYS`, `RUN` | `Pin_Keys`, `pin_keys` |
| `camel` | `buildIndex`, `run` | `BuildIndex`, `build_index` |
| `pascal` | `BuildIndex`, `Run` | `buildIndex`, `Build_Index` |
| `kebab` | `check-arms`, `run` | `checkArms`, `check_arms` |
| `dot` | `gate.legs`, `run` | `Gate.Legs`, `gate_legs` |

`run` appears in four rows deliberately. Re-measured on this worktree, `classify("run")` returns
`camel`, `dot`, `kebab` and `snake`, which is the whole argument for set membership in one name.

### Why the set is load-bearing rather than defensive

Three separate measurements of "names satisfying two or more conventions" exist and they agree once
the population is named, which is worth stating because the three figures look like a disagreement.

| Population | Multi-convention names | Source |
|---|---|---|
| py functions + py types + js functions, 1086 names | 255 | research record, its `m1.py` |
| py functions + py types + js functions seen by two regexes, 1064 names | 245 | prototype record |
| py functions + py types only, 964 names | 235 | re-measured for this spec on this worktree |

The three populations differ by exactly their JavaScript half, and the prototype record already
confesses that its JS extraction sees 100 of the 122 definitions the kit's own `js-regex` pattern set
finds. A single-label classifier reports a violation for every one of these names the moment the
declared cell is not the label it happened to pick. At 235 in the Python half alone, that is a
predicate that gets waived in its first week rather than one that ships.

### Why the stem splits at the first dot

Re-measured for this spec over the 213 files in the armed file cells: first-dot and last-dot stems
classify differently on 65 of them. Under first-dot stemming `py.file` violates on 7 of 47 and
`sh.file` on 4 of 89, which are exactly the offender lists the research record names. Under last-dot
stemming the same run reports 11 and 49.

The `sh.file` jump from 4 to 49 is the decisive one. There are 46 tracked `*.test.sh` scripts
(`git ls-files '*.test.sh' | wc -l`), and last-dot stemming turns every one of them into a kebab
violation because the stem then retains an interior dot. Adding the three frozen dated build-repro
scripts gives 49. So the rule is not cosmetic: last-dot stemming would red this repo's entire shell
test suite plus every template the kit ships, on day one, for having a compound extension.

Two figures in this section disagree with their sources by one and by three, and both are recorded
rather than reconciled. The research record puts the graded-file disagreement at 64 where this run
measures 65, and the prototype record puts last-dot `py.file` at 8 where this run measures 11. Both
deltas are UNVERIFIED; the `sh.file` figure of 49 reproduces exactly, and it is the one the rule turns
on.

### Inventory

Identifiers this unit mints, each with its cell.

| Identifier | Cell | Role |
|---|---|---|
| `_AFFIX` | `py.constant` | the leading and trailing underscore strip |
| `_FORMS` | `py.constant` | the six anchored regexes |
| `read_core` | `py.function` | strip affixes, return the core |
| `classify` | `py.function` | the set of forms the core satisfies |
| `check_convention` | `py.function` | one name against one declared convention, returning a verdict |
| `read_stem` | `py.function` | basename up to the first dot |

`read` is the declared verb for "pull bytes or records from a named source" and `check` for "assert a
predicate and return a verdict", so `read_core`, `read_stem` and `check_convention` need no
consultation. `classify` is NOT in the declared table, which this unit records rather than papers
over: it is one of the 418 UNRULED offenders the P1 split is being built to report, it is the name the
prototype used, and renaming it to fit is the reflex the charter's naming bullets call a synonym list.
It stays and it is reported.

### Rollout

The predicate lands inert. It is reachable only from a cell declared in `CELLS`, and no cell is armed
until the conf rewrite unit pastes the matrix. So this unit can land, be gated by its own fixtures and
be reverted without moving a single verdict on the bar — which is the dark-landing rule applied to a
predicate rather than to a feature.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/lexicon/subtokens.py` | `_AFFIX`, `_FORMS`, `read_core`, `classify`, `read_stem`, `check_convention`, and the sibling-not-consumer paragraph in the docstring |
| `tools/lexicon/lexicon.py` | call the predicate from the corpus walk per armed cell, and print the verdict and teeth lines |
| `tools/lexicon/selftest.py` | red and green fixtures per verdict, the staged-break arm, the teeth arm, the stem arm |
| `tools/lexicon/README.md` | the convention paragraph, replacing a promise with a description |

ESTIMATE, and marked as one for the reason the research record gives: nothing comparable ships, so a
line count would be a guess. The prototype's own classifier is nine lines plus six patterns, which is
a floor for the classifier alone and says nothing about the walk or the report.

### Alternatives rejected

- **A single-label classifier.** Rejected on the measurement in `### Why the set is load-bearing`.
- **Last-dot stems.** Rejected on the 46 shell test scripts and the 49-violation result.
- **Classifying the output of `subtokens()`.** Impossible rather than merely wrong: that function
  lowercases at `subtokens.py:26`, so `BuildIndex` and `build_index` are indistinguishable after it.
  The convention check reads the raw name, which is why S7 makes the relationship explicit in the
  docstring instead of leaving a future reader to rediscover it.
- **Reusing `case_collisions` in `tools/gate-lint/ps-hygiene.py:110-116`.** It is the closest existing
  case-aware predicate in the tree and it answers a different question: it groups PowerShell
  identifiers by their lowercased form to find names that collide under case-insensitive comparison.
  It classifies nothing and has no notion of a convention.
- **Reusing `run_suggest`'s re-caser at `lexicon.py:837-838`.** It makes a replacement token inherit
  the case of the token it replaces. It reads a name's case in order to copy it, never to grade it,
  and it has no vocabulary of named conventions to grade against.

## 5. Production-readiness checklist

- security — N/A. Pure functions over identifier strings already read from tracked files.
- perf / scale — six anchored regex matches per graded name. The measured graded population is 964
  Python definitions plus 213 filenames on this corpus, so the cost is bounded by the corpus walk that
  already runs, not by the classifier. The `lexicon naming predicates` ceiling of 300 s is not at risk.
- a11y — N/A. No user interface.
- i18n — a known gap, inherited and not widened. `subtokens.py` is ASCII-only, so an accented
  identifier grades on a truncated core and a fully non-ASCII name is skipped with no report. The
  anchored `[a-z]` and `[A-Z]` classes here have the same blind spot. It needs its own backlog row,
  named in §3 as out of scope, and this line is the record that the exposure was seen and not fixed.
- error / empty / loading states — an identifier with no word characters at all produces an empty
  core, which is fork F1. Every other state is one of the three verdicts, and each is printed.
- observability — the teeth line of S8 is the observability requirement, not a nicety: a cell printing
  zero violations and nothing else is indistinguishable from a cell that cannot fail.
- risks (concurrency, data-loss, rollback hazards) — none for this unit. It writes nothing and lands
  inert per `### Rollout`. The build-wide concurrency risk lives in the pin block, which is
  `TOOL-aSurfacedLexicon-4`'s fork.
- testing + left-shift gates — the staged break is the DoD, not the fixtures. Both the prototype's
  breaks are re-staged into the real kit and observed RED, then unstaged and observed back at
  baseline. The AMBIGUOUS arm has no in-corpus instance and is exercised by a staged fixture, which
  every report of it must say. No new bar leg is added, so no ceiling and no
  `memory/project/testsuite-count-waivers.txt` row is owed.
- migration / rollback — additive. Revert is one module plus one call site, and no declaration
  references the predicate until the conf rewrite arms a cell.
- user docs — `tools/lexicon/README.md` replaces the standing convention promise with a description of
  what actually ships, including that shell and markdown are dark and why.

## 6. Acceptance criteria

- **AC1** — When `def loadUserData` is staged into a tracked `.py` file, `python
  tools/lexicon/lexicon.py --check` REDS `py.function` with the message `VIOLATION  loadUserData
  satisfies camel, not snake`; when unstaged, the same command returns to the baseline counts. The RED
  is observed and recorded before this unit is called done.
- **AC2** — When `class user_record` is staged into a tracked `.py` file, `--check` REDS `py.type`
  with `VIOLATION  user_record  satisfies snake, not pascal`; unstaging returns to baseline.
- **AC3** — When the tree is graded with nothing staged, `python tools/lexicon/lexicon.py --check`
  reports `py.function` at 0 violations of 925 and `py.type` at 0 of 39, and `__init__` and
  `_build_index` are among the passing names rather than the offenders. Re-measured on this worktree
  at base `d0a18683`.
- **AC4** — When the tree is graded with nothing staged, the same command reports `py.file.conv 7`
  naming exactly `tools/check-spec-tokens.py`, `tools/gate-lint/ps-hygiene.py` and the five other
  hyphenated basenames, and `sh.file.conv 4`. This is the gate's failing case observed IN THE TREE
  rather than staged.
- **AC5** — When `def FAMILY_of` is staged, an identifier whose core is non-empty and whose
  convention set is empty, `--check` REDS with a message naming AMBIGUOUS and NOT the word
  VIOLATION. Re-measured on this worktree, 0 of the 964 Python definitions and 0 of the 1086
  identifiers the research record graded return an empty set, so this arm has NO in-corpus population
  and its only exercise is this staged fixture. Every report of a green run states that.
- **AC6** — When `py.function` is re-declared as `camel` in a scratch declaration, `--check` reports
  691 violations of 925. Re-measured for this spec. This is the teeth arm, and it is what makes the
  0-of-925 result in AC3 a measurement rather than an assertion about nothing.
- **AC7** — When the tree is graded, all 46 files matched by `git ls-files '*.test.sh'` pass
  `sh.file`, and a build using last-dot stems instead reports `sh.file.conv 49`. Re-measured for this
  spec.
- **AC8** — When `classify` is asked about `run`, it returns a set containing at least `snake`,
  `camel` and `kebab`; when asked about `_build_index` it returns a set containing `snake`. Both are
  selftest arms on the function directly, so the set contract is gated at the seam and not only
  through the report.
- **AC9** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after this unit, the rendered
  Skill still byte-matches, so the `lexicon wiring` leg stays green. This unit changes no placeholder.

## 7. Gates

- `lexicon naming predicates` — chunk `declarations`, subject `repo`, ceiling 300 s. Where the
  verdicts in AC1 through AC7 are observed on the bar.
- `lexicon selftest` — chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, ceiling 880 s.
  Carries every fixture, including the AMBIGUOUS arm that has no corpus instance. It is invisible to
  the push bar, so this unit's DoD runs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` rather
  than trusting the push boundary.
- `lexicon wiring` — chunk `wiring`, subject `repo`, guard empty, ceiling 330 s. AC9's leg.
- `codebase-map kit selftest` — its guard includes `tools/lexicon/`, so editing `subtokens.py` selects
  it. It asserts a cross-kit contract on the lexicon's own constants and must be seen green under
  `GATE_SELFTESTS=1` in the same commit.
- The memory-tree hygiene leg, for this spec.

## 8. Open questions

**F1 — a name with NO word characters at all: AMBIGUOUS, or ungradeable?**

Q7 ruled on the name that HAS characters and satisfies no convention, and that ruling is settled: it
reds with a distinct message, and S5 builds it. It did not rule on the name whose core is EMPTY after
the affix strip, and the two collide with an existing documented contract.

`leading_verb` in `subtokens.py:34-38` states the opposite answer for the sibling predicate: a name
with no word characters returns the empty string, "which the caller must treat as UNGRADEABLE rather
than as a violation: a name with no leading token is not a name that chose the wrong verb." Applying
Q7's ruling literally makes the same identifier ungradeable for vocabulary and a RED for convention,
from two functions in one module, which is a distinction a reader would have to derive.

Re-measured on this worktree, the population is **zero**: 0 of the 964 Python definitions have an
empty core, and 0 have a non-empty core with an empty convention set. So this fork cannot be decided
by looking at the corpus, and any arm built for it is synthetic — the same property the owner rulings
record already accepts for the selector unit.

- **Ungradeable, matching `leading_verb`.** One rule for "no word characters" across both predicates
  in one module. Costs the ability to notice a definition literally named `_`, which is legal Python.
- **AMBIGUOUS, extending Q7's ruling.** One rule for "the classifier has nothing to say", regardless
  of why. Costs a divergence from `leading_verb` that has to be written down in both docstrings.

**Recommendation: ungradeable, matching `leading_verb`, with the divergence closed by making both
functions say so.** Q7's ruling is about a name that chose no convention; a name with no characters
did not choose anything, and the sibling predicate in the same file already has the answer. Whichever
way this goes, the arm is a synthetic fixture and the report must say the population is zero.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Classifier shape, affix strip and first-dot stemming lifted from
  the prototype record. Every number re-measured on this worktree at base `d0a18683` rather than
  inherited, which is what surfaced the three multi-convention figures as one population question and
  put two source deltas on record as UNVERIFIED. Fork F1 found by reading `subtokens.py:34-38` against
  the Q7 ruling.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "classify an identifier's case style as the set of snake
camel pascal kebab conventions it satisfies"` returns `case_collisions` in
`tools/gate-lint/ps-hygiene.py`, `classify` in `tools/memory-tree/check-arms.py`, `classify_row` and
`classify_outcome` in `tools/govkit/govkit.py`, and `run_case` in `tools/lexicon/selftest.py`. Every
one of them is at fan-in 0 or 1, so the lookup surfaced NO seam at its own threshold of 3.
**No existing seam fits, and the evidence is a direct source check as well as the lookup:**
`grep -inE "snake|camel|pascal|kebab|screaming" tools/lexicon/*.py` returns only `run_suggest`'s
re-caser at `lexicon.py:837-838` and selftest fixtures, so the kit contains no convention predicate
to extend. The two nearest candidates are rejected by name in `§4 Alternatives rejected` —
`case_collisions` groups identifiers by their lowercased form to find case-insensitive collisions and
classifies nothing, and `check-arms.classify` sorts gate arms. What this unit EXTENDS rather than
creates is `tools/lexicon/subtokens.py`, chosen because the classifier must read the raw name that
module's existing splitter deliberately lowercases, and because the research record's zero-new-modules
rule makes a new top-level file the shape that broke an adopter's entry points for six days.

Recall terms used, verbatim: `python tools/memory-recall/query.py "why must the naming convention
classifier return a set rather than a single label and what decided the first-dot filename stem"
--terms "lexicon convention casing snake camel pascal kebab classifier set membership affix strip
filename stem ambiguous"`. It returned 37 hits. The load-bearing ones are this build's own prototype
and research records, which carry the classifier code and the population figures, plus two rounds of
spec-audit findings on an earlier lexicon unit that red exactly the failure this spec's `### Data
model` table is written to avoid: a spec that describes a helper's return shape in prose, never
enumerates the membership, and leaves an implementer to red an acceptance criterion the spec broke.

# TOOL-aSurfacedLexicon-5 — the convention predicate

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 3

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
- **S5** — the AMBIGUOUS verdict. A name whose set is empty REDS, with a message distinct from
  `VIOLATION`, per the owner's Q7 ruling as extended by F1: the empty core reds under the same
  message rather than being skipped. The NON-EMPTY-core half ships exercised only by a staged
  fixture, because its measured in-corpus population is zero — 0 of the 1017 Python definitions at
  base `6c670b02`. The EMPTY-core half has a live in-corpus population of NINE, the tracked files
  whose basename begins with a dot, listed under `### The empty-core population` in §4.
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
- Fixing non-ASCII identifiers. The research record files an unreviewed finding that `subtokens.py`
  is ASCII-only, and this non-goal used to claim the classifier "does not widen" that exposure. **It
  does widen it, and the claim is struck.** `read_core`'s `_AFFIX` is an anchored DOTALL strip, so a
  non-ASCII core survives it whole rather than being truncated; the six ASCII-anchored forms then
  match none of it, and the name REDS as AMBIGUOUS instead of being passed over. Measured:
  `read_core("变量")` returns `"变量"`, non-empty, so the verdict fires. Fixing that is still out of
  scope and still owes its own backlog row. What changes is why the row is owed: for a red this unit
  creates, not for a gap it merely inherits.

## 4. Design

### Data model

`classify(name) -> set[str]` over a core produced by `read_core(name)`. Three verdicts per graded
name, and the third is the one Q7 created and F1 widened.

| Verdict | Condition | Reds |
|---|---|---|
| SATISFIED | declared convention is in the set | no |
| VIOLATION | set is non-empty and the declared convention is not in it | yes |
| AMBIGUOUS | the set is empty, whether or not the core is | yes, with a distinct message |

**The AMBIGUOUS condition was `core is non-empty and the set is empty` at rev-1, and that left a
HOLE.** An empty core is then none of the three: not SATISFIED, not a VIOLATION because the set is
empty, and not AMBIGUOUS because the core is. It falls through every row and the classifier prints
nothing at all. F1's ratified answer closes the hole with no fourth row and no fourth message, which
is the form written above.

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
| py functions + py types only, 964 names at `d0a18683` | 235 | re-measured for this spec at rev-1 |
| the same population at `6c670b02`, 1017 names | NOT re-measured | see the note below |

The Python population MOVED between rev-1's base and this revision's: 976 `py.function` plus 41
`py.type` is 1017 definitions over 49 tracked files at `6c670b02`, against 925 plus 39 over 47 files
at `d0a18683`. Counts from the same reconstruction rev-1 used — the kit's Python-AST definition
extraction over `git ls-files "*.py"` — which rev-1 validated independently by reproducing AC6's
camel figure byte for byte. The multi-convention count was not re-run at the new base, so 235 of 964
is left standing as a rev-1 figure and is NOT restated as current. The argument does not turn on the
third significant figure.

The three populations differ by exactly their JavaScript half, and the prototype record already
confesses that its JS extraction sees 100 of the 122 definitions the kit's own `js-regex` pattern set
finds. A single-label classifier reports a violation for every one of these names the moment the
declared cell is not the label it happened to pick. At 235 in the Python half alone, that is a
predicate that gets waived in its first week rather than one that ships.

### Why the stem splits at the first dot

Re-measured at base `6c670b02`. Under first-dot stemming `py.file` violates on 8 of 49 and `sh.file`
on 5 of 94. Under last-dot stemming the same run reports 12 and 53. Denominators from
`git ls-files "*.py" | wc -l` and `git ls-files "*.sh" | wc -l`; violation counts from the classifier
run over those two sets.

The `sh.file` jump from 5 to 53 is the decisive one. There are 49 tracked `*.test.sh` scripts
(`git ls-files "*.test.sh" | wc -l`), and last-dot stemming turns every one of them into a kebab
violation because the stem then retains an interior dot. So the rule is not cosmetic: last-dot
stemming would red this repo's entire shell test suite plus every template the kit ships, on day one,
for having a compound extension.

**Rev-1's reconciliation of that figure COLLAPSED and is restated rather than patched.** It read "46
tracked scripts plus 3 frozen dated build-repro scripts = 49", arithmetic that closed exactly. At
this base the two numbers are 49 tracked `*.test.sh` scripts and 53 last-dot `sh.file` violations, a
remainder of 4 whose composition this run did not enumerate. The remainder is therefore UNVERIFIED.
What the rule turns on survives the collapse untouched: every one of the 49 test scripts is a
last-dot violation and a first-dot pass, which is a ten-fold swing on its own.

One figure pair in this section is UNVERIFIABLE and is marked so rather than repeated. Rev-1 wrote
"the 213 files in the armed file cells: first-dot and last-dot stems classify differently on 65 of
them". The 65 reproduces, but over 210 files, and no constructible file set yields both 213 and 65
together. Both halves of that pair are UNVERIFIED, alongside the two source deltas rev-1 already
recorded: the research record puts the graded-file disagreement at 64, and the prototype record puts
last-dot `py.file` at 8 where this run measures 12.

### The empty-core population

Rev-1 recorded this unit's empty-core population as ZERO and built the F1 arm as synthetic on that
basis. **The zero is true of the Python definitions and false of the filename half of this unit's own
scope**, which S6 puts squarely in scope by grading a file cell on the basename up to its FIRST dot.
NINE tracked files have a basename beginning with a dot, so every one of them stems to the EMPTY
STRING. Measured with `git ls-files | awk -F/ "{print \$NF}" | grep "^\." | sort -u`:
`.codebase-map.conf`, `.codebase-map.conf.example`, `.gitattributes`, `.gitignore`, `.lexicon.conf`,
`.memory-tree.conf`, `.memory-tree.conf.example`, `.unattended.conf` and `.unattended.conf.example`.

Under F1's ratified answer each of those reds as AMBIGUOUS the moment its cell is armed — that is
`conf.file`, `example.file`, `gitattributes.file` and `gitignore.file`. All four are dark in `LANGS`
today, so nothing reds when this unit lands and the population stays latent.

**Hand-off to the conf-rewrite unit, which owns the arming.** Arming any of those four cells without
first deciding a dotfile stem rule reds nine correctly-named files. The decision is that unit's, not
this one's, and it has exactly two honest shapes: a stem rule that gives a dot-leading basename a
non-empty core, or an explicit declaration that those cells stay dark and why. Note plainly what the
red would be saying: `.gitignore` is correctly named by every convention anyone would want to
declare, and it would still read AMBIGUOUS, because the classifier is being handed nothing to
classify. Surfacing that at arming time rather than swallowing it is the whole point of the ratified
answer — under the rejected one the same arming would skip all nine silently while the per-cell
coverage report showed the cell clean.

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
- **Last-dot stems.** Rejected on the 49 shell test scripts and the 53-violation result.
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
- perf / scale — six anchored regex matches per graded name. The measured graded population at base
  `6c670b02` is 1017 Python definitions, 976 `py.function` plus 41 `py.type`, over the 49 files
  `git ls-files "*.py" | wc -l` reports, plus the basenames of the armed file cells. The cost is
  bounded by the corpus walk that already runs, not by the classifier. The `lexicon naming
  predicates` ceiling of 300 s is not at risk.
- a11y — N/A. No user interface.
- i18n — a known gap, and this unit WIDENS it. Rev-1's line here was wrong twice over and both halves
  are struck. It said an accented identifier "grades on a truncated core": nothing is truncated,
  because `_AFFIX` is `^(_*)(.*?)(_*)$` under `re.DOTALL`, an anchored strip of underscores at both
  ends and nothing else. It said a fully non-ASCII name is "skipped with no report": measured,
  `read_core("变量")` returns `"变量"`, which is non-empty, so the six ASCII-anchored forms match none
  of it and the name REDS as AMBIGUOUS. So the classifier turns a silent blind spot into a red one,
  which is a widening of the exposure and not an inheritance of it. §3 records the same correction
  and still routes the fix to its own backlog row; this line is the record that the widening was
  seen, measured and shipped deliberately.
- error / empty / loading states — an identifier with no word characters at all produces an empty
  core, which was fork F1 and is now ratified as AMBIGUOUS under Q7's message. Every state is one of
  the three verdicts, and each is printed; the fall-through that printed nothing is closed in §4.
- observability — the teeth line of S8 is the observability requirement, not a nicety: a cell printing
  zero violations and nothing else is indistinguishable from a cell that cannot fail.
- risks (concurrency, data-loss, rollback hazards) — none for this unit. It writes nothing and lands
  inert per `### Rollout`. The build-wide concurrency risk lives in the pin block, which is
  `TOOL-aSurfacedLexicon-4`'s fork.
- testing + left-shift gates — the staged break is the DoD, not the fixtures. Both the prototype's
  breaks are re-staged into the real kit and observed RED, then unstaged and observed back at
  baseline. The AMBIGUOUS arm has no in-corpus instance and is exercised by a staged fixture, which
  every report of it must say. That statement now applies to the NON-EMPTY-core half only. The
  EMPTY-core half has a live in-corpus population of nine tracked dotfiles, per `### The empty-core
  population`, so its arm is a real red held latent by four dark cells rather than a synthetic one.
  No new bar leg is added, so no ceiling and no `memory/project/testsuite-count-waivers.txt` row is
  owed.
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
  reports `py.function` at 0 violations of 976 and `py.type` at 0 of 41, and `__init__` and
  `_build_index` are among the passing names rather than the offenders. Re-measured at base
  `6c670b02` over the 49 files `git ls-files "*.py" | wc -l` reports; rev-1's denominators, 925 and
  39 at `d0a18683`, are stale and are corrected here rather than hedged. The zero itself is unchanged
  — only the denominator moved.
- **AC4** — When the tree is graded with nothing staged, the same command reports `py.file.conv 8`
  naming exactly `aiosqlite-seam-conftest.py`, `check-arms.py`, `check-kit-placeholders.py`,
  `check-recall.py`, `check-spec-tokens.py`, `merge-rows.py`, `ps-hygiene.py` and `settings-merge.py`,
  and `sh.file.conv 5`. Re-measured at base `6c670b02`; rev-1's `7` and `4` are stale, and
  `tools/check-kit-placeholders.py` is the basename that joined the Python list. Denominators are 49
  and 94, from `git ls-files "*.py" | wc -l` and `git ls-files "*.sh" | wc -l`. This is the gate's
  failing case observed IN THE TREE rather than staged.
- **AC5** — When `def FAMILY_of` is staged, an identifier whose core is non-empty and whose
  convention set is empty, `--check` REDS with a message naming AMBIGUOUS and NOT the word
  VIOLATION. Re-measured at base `6c670b02`, 0 of the 1017 Python definitions return a non-empty core
  with an empty set, so THIS arm has no in-corpus population and its only exercise is the staged
  fixture; every report of a green run states that. **That statement is scoped to the non-empty core
  and no further.** The empty-core arm is AC10 and its in-corpus population is nine, not zero.
- **AC6** — When `py.function` is re-declared as `camel` in a scratch declaration, `--check` reports
  736 violations of 976. Re-measured at base `6c670b02`; rev-1's `691 of 925` is stale. This is the
  teeth arm, and it is what makes the 0-of-976 result in AC3 a measurement rather than an assertion
  about nothing.
- **AC7** — When the tree is graded, all 49 files matched by `git ls-files "*.test.sh"` pass
  `sh.file`, and a build using last-dot stems instead reports `sh.file.conv 53`. Re-measured at base
  `6c670b02`; rev-1's `46` and `49` are stale. Rev-1 also reconciled the two numbers as "46 tracked
  scripts plus 3 frozen dated build-repro scripts = 49"; at 49 and 53 that arithmetic no longer
  closes and it is RESTATED rather than patched — the remainder of 4 is UNVERIFIED and this criterion
  does not claim to account for it. What the criterion actually gates is the pair: every test script
  passes first-dot and fails last-dot.
- **AC8** — When `classify` is asked about `run`, it returns a set containing at least `snake`,
  `camel` and `kebab`; when asked about `_build_index` it returns a set containing `snake`. Both are
  selftest arms on the function directly, so the set contract is gated at the seam and not only
  through the report.
- **AC9** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after this unit, the rendered
  Skill still byte-matches, so the `lexicon wiring` leg stays green. This unit changes no placeholder.
- **AC10** — the empty-core verdict, which F1 ratified and which would otherwise land ungated. When a
  definition literally named `_` is staged into a tracked `.py` file — an identifier whose core is
  empty after the affix strip — `python tools/lexicon/lexicon.py --check` REDS it as AMBIGUOUS under
  the same message AC5 asserts, and NOT as a VIOLATION, and NOT by printing nothing. The RED is
  OBSERVED and recorded before this unit is called done, and unstaging returns the run to baseline.
  A second arm calls the predicate directly: `read_core("_")` returns the empty string and the
  verdict for it is AMBIGUOUS. Unlike AC5 this arm is NOT population-free: the in-corpus population is
  the nine tracked dot-leading basenames of `### The empty-core population`, latent only because all
  four of their file cells are dark in `LANGS` today. Every report of this arm says nine, not zero.

## 7. Gates

- `lexicon naming predicates` — chunk `declarations`, subject `repo`, ceiling 300 s. Where the
  verdicts in AC1 through AC7 and AC10 are observed on the bar. AC10 joined this list when F1 was
  ratified; a range left reading `AC1 through AC7` after a criterion is appended is the
  amendment-leaves-its-other-half-standing class, and it is why this clause enumerates rather than
  spans.
- `lexicon selftest` — chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, ceiling 880 s.
  Carries every fixture. AC5's AMBIGUOUS arm has no corpus instance and AC10's has nine, latent
  behind four dark file cells — one word for both would be wrong about one of them. It is invisible to
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

`leading_verb` appears to state the opposite answer for the sibling predicate. `def leading_verb` is
at `subtokens.py:29` and the sentence at issue spans `:32-34`: a name with no word characters returns
the empty string, "which the caller must treat as UNGRADEABLE rather than as a violation: a name with
no leading token is not a name that chose the wrong verb." Rev-1 cited that as `:34-38`, which is
wrong by five lines and is corrected here and in §9. Applying Q7's ruling literally makes the same
identifier ungradeable for vocabulary and a RED for convention, from two functions in one module,
which is a distinction a reader would have to derive.

**Two claims rev-1 built this fork on were measured FALSE, and both are struck rather than hedged.**

First, "`leading_verb` returns the empty string for a name with no word characters" is wrong on part
of its own stated domain. Measured: `leading_verb("__")` and `leading_verb("_")` do return `""`, but
`leading_verb("1")` returns `"1"` and `leading_verb("2x")` returns `"2"`, because `_SUBTOKEN_RE`
includes `[0-9]+`. The function's own docstring names `1` among its empty-return examples, so the
authority this fork leaned on is wrong about one of the three cases it lists. The answer rev-1 called
already-implemented is DOCUMENTED, not implemented.

Second, "one rule for 'no word characters' across both predicates" is unreachable by either option,
because the two predicates do not agree on what the phrase MEANS. `leading_verb` runs ASCII subtoken
classes over `identifier.lstrip("_")`, stripping LEADING underscores only. `read_core` runs
`^(_*)(.*?)(_*)$` under `re.DOTALL` over BOTH ends and over any character class at all. They agree on
pure-underscore names and on the empty string and diverge everywhere else: `变量` gives
`leading_verb` `""` but `read_core` `"变量"`; `café_x` gives `"caf"` against `"café_x"`; `1` gives
`"1"` against an empty form set. So the alignment ungradeable was chosen to buy does not exist to be
bought.

**And the population is not zero.** Rev-1 measured 0 of the Python definitions with an empty core and
0 with a non-empty core and an empty set, and that half re-measures unchanged at base `6c670b02`: 0
and 0 of 1017. But S6 puts filenames in this unit's scope, and nine tracked files have a dot-leading
basename whose first-dot stem is the empty string. They are enumerated with their command under
`### The empty-core population`. So the fork has a live in-corpus population of NINE, and rev-1's
"any arm built for it is synthetic" applies to the Python half only.

- **Ungradeable, matching `leading_verb`.** One rule for "no word characters" across both predicates
  in one module — unavailable, per the divergence above. Costs the ability to notice a definition
  literally named `_`, which is legal Python, and silently skips the nine dotfiles whenever one of
  their cells is armed, while the per-cell coverage report shows the cell clean. Needs a fourth
  verdict row and a fourth message to close §4's fall-through.
- **AMBIGUOUS, extending Q7's ruling.** One rule for "the classifier has nothing to say", regardless
  of why. Costs a divergence from `leading_verb` that has to be written down in both docstrings —
  which, per the second refutation above, is owed under BOTH options and so is not a differential
  cost. Closes §4's fall-through with no new row and reuses Q7's already-ruled message.

**Rev-1 recommended ungradeable. That recommendation is OVERTURNED and the mark below ratifies
AMBIGUOUS.** Both premises it rested on are false: the sibling predicate does not have the answer, it
merely documents one, and the one-rule alignment is unavailable either way. The paragraph is left
here as the record of what was argued, not as a live recommendation — the reasoning stands corrected
above and the mark decides. Neither option was vetoed; the pick turns on the nine-file population and
on the verdict-table hole, both of which rev-1 missed. Whichever way it had gone, this fork owed an
acceptance criterion and had none; AC10 is now that criterion.

**RESOLVED (agent, 2026-09-04, delegated): F1 — AMBIGUOUS, extending the Q7 ruling; an empty core
reds with Q7's message rather than being skipped as ungradeable.**

NO OPTION IS VETOED, and that has to be said plainly. No §6 criterion observes this fork's outcome:
AC5 is Q7's arm over the NON-empty core `FAMILY_of`, AC8 is `run` and `_build_index`, both cores
non-empty. No §3 non-goal is touched, no dependency, no surface, no write path. Both options clear
the ladder, so the pick is the feature-richness test and the tie-breaks, and it goes AGAINST the §8
recommendation.

Stated-AC count ties at zero, so it turns on follow-ups left open, and AMBIGUOUS leaves strictly
fewer. Both of §8's premises for ungradeable are false under measurement. First, "the sibling
predicate already has the answer": `leading_verb`'s docstring names `1` among its empty-return
examples, and `leading_verb('1')` returns `'1'`, because `_SUBTOKEN_RE` includes `[0-9]+`. The
answer being adopted is DOCUMENTED, not implemented. (The cite is wrong too — `def leading_verb` is
at `:29` and the quoted sentence spans `:32-34`; `:34-38` starts two lines late.) Second, "one rule
for 'no word characters' across both predicates" is unachievable by this choice, because the two do
not agree on what the phrase MEANS: `leading_verb` runs ASCII subtoken classes over
`identifier.lstrip("_")` — LEADING underscores only — while `read_core` runs `^(_*)(.*?)(_*)$`
DOTALL over both ends and any character class. They agree only on pure-underscore names and the
empty string, so ungradeable buys that narrow intersection and leaves three documented disagreements
standing. Its stated cost for AMBIGUOUS — a divergence written into both docstrings — is owed under
BOTH options and is not a differential cost.

And the fork has a LIVE IN-CORPUS POPULATION OF NINE that nobody measured. S6 is in scope here —
"file cells grade the basename up to its FIRST dot" — and nine tracked files have a basename
beginning with a dot, so every one stems to the EMPTY STRING: `.codebase-map.conf`, `.gitattributes`,
`.gitignore`, `.lexicon.conf`, `.memory-tree.conf`, `.unattended.conf`, and the three `*.conf.example`
files under `tools/`. All four extensions are already declared in LANGS. "The population is zero" is
true of the Python DEFINITIONS and false of the filename half of this unit's own scope. That
denominator is `1017` at the run's base `6c670b02` (976 function + 41 type, by an `ast` walk over
the 49 files `git ls-files "*.py"` returns) and was `964` at `d0a18683`, where this mark was
drafted; the count of empty cores is 0 at both, so only the denominator moved.

That population decides it. Under ungradeable, arming any of those cells silently skips nine files
while the per-cell coverage report shows the cell clean — the green-by-absence class and the
"a skip must announce itself" rule, both charter-level. Under AMBIGUOUS the same arming reds nine
files with Q7's already-specced distinct message, forcing the dotfile stem rule to be decided
deliberately rather than by omission. AMBIGUOUS also closes §4's verdict-table hole with no new row:
as specced an empty core is neither SATISFIED, nor VIOLATION (set empty), nor AMBIGUOUS (core
empty), and falls through all three printing nothing. Ungradeable needs a fourth row and a fourth
message. Tie-break 2 confirms rather than decides: AMBIGUOUS reuses Q7's ruled message and the
prototype's existing `if not core: return set()` branch, adding nothing.

Deliberate residual: `.gitignore` is correctly named and would read AMBIGUOUS. Every affected cell
is `dark` today so nothing reds on landing, and the right answer at ARMING time is a dotfile stem
rule or an explicit dark declaration — a decision the conf-rewrite unit owns and which AMBIGUOUS
surfaces instead of swallowing. This fork must also gain a §6 criterion; as it stands the choice
lands ungated, which is a gate nobody has ever seen fail.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Classifier shape, affix strip and first-dot stemming lifted from
  the prototype record. Every number re-measured on this worktree at base `d0a18683` rather than
  inherited, which is what surfaced the three multi-convention figures as one population question and
  put two source deltas on record as UNVERIFIED. Fork F1 found by reading `subtokens.py:29` and its
  docstring at `:32-34` against the Q7 ruling. (That cite read `:34-38` as written at rev-1 and is
  corrected here; `def leading_verb` is at `:29`.)
- rev-2 · 2026-09-04 · F1 ratified AGAINST this spec's own §8 recommendation: an empty core reds as
  AMBIGUOUS under Q7's message, not as ungradeable. The status base is RE-PINNED from `d0a18683` to
  `6c670b02`, because every figure this revision writes was measured there. Neither option was
  vetoed; the pick turns on nine tracked dotfiles whose first-dot stem is empty, a live in-corpus
  population §8's "zero" missed by counting Python definitions only, now enumerated with its command
  in `### The empty-core population` and handed off to the conf-rewrite unit as a dotfile stem rule
  it must decide before arming `conf.file`, `example.file`, `gitattributes.file` or
  `gitignore.file` — `.gitignore` is correctly named and would still read AMBIGUOUS. §8's two
  premises struck as measured false: `leading_verb("1")` returns `"1"` despite its own docstring
  naming `1` as an empty-return case, and the two predicates disagree on what "no word characters"
  MEANS, so the one-rule alignment is unavailable either way. §4's verdict table had a
  fall-through hole for the empty core and is fixed with no new row; the fork landed ungated and
  AC10 is now its criterion, requiring an observed RED on a staged empty-core name. §5's i18n bullet
  is struck as doubly wrong — nothing is truncated and a fully non-ASCII name reds rather than being
  skipped — and §3's non-goal now says plainly that this unit WIDENS the ASCII-only exposure and owes
  a backlog row for a red it creates. AC3, AC4, AC6 and AC7 re-measured at the new base, each with
  its command: 0 of 976 and 0 of 41; `py.file.conv 8` of 49 and `sh.file.conv 5` of 94; 736 camel
  violations of 976; 49 tracked `*.test.sh` and 53 last-dot violations. AC7's "46 plus 3 frozen
  scripts = 49" reconciliation collapsed at those numbers and is restated with the remainder of 4
  marked UNVERIFIED rather than patched. §4's "213 files, 65 differ" pair is marked UNVERIFIED: the
  65 reproduces over 210 files and no constructible set yields both.

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

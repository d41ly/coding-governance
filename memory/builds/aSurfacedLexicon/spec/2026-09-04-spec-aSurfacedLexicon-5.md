# TOOL-aSurfacedLexicon-5 — the convention predicate

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-6 |

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
- Deciding which cells ship armed. This unit builds the predicate and arms NOTHING. The arming
  boundary is two units and not one: `TOOL-aSurfacedLexicon-6` arms the FIRST cell, `py.constant`, at
  build order 4, and `TOOL-aSurfacedLexicon-12` pastes the rest of the matrix at order 7. Rev-2 wrote
  "the conf rewrite arms it", which read as an absolute and was contradicted by a sibling one order
  after this one — a reader of rev-2 would have refused the conf edit unit 6 requires.
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

**All six went to the gate rather than to judgement**, which rev-2 did for one of them and inferred
for the rest. `python tools/lexicon/lexicon.py --suggest <name>`, run per identifier at `693bcf96`:
`read_core`, `read_stem` and `check_convention` each answer `OK — ... leads with <verb>, which the
declaration carries`, while `classify`, `_AFFIX` and `_FORMS` each answer `... is not in the declared
table, and no row bans it by name`. Three refusals, not one. Only one of the three costs anything,
and the next subsection is the measurement that says which.

`classify` STAYS, which this unit records rather than papers over: it is the name the prototype used,
and renaming it to fit is the reflex the charter's naming bullets call a synonym list. The
disposition is ratified elsewhere and is not re-derived here — `memory/backlog/TOOL.md` row
`TOOL-aResumedRelay-1` is OPEN and already refused a rename for this same engine-name class on the
scoping-not-spelling argument. What rev-3 adds is that keeping the name COSTS something, which rev-2
did not budget.

### The pin this unit raises

`VERB_OFFENDER_PIN` has ZERO headroom, and rev-2's argument for `classify` was built on not knowing
it. Measured at `693bcf96`: `python tools/lexicon/lexicon.py --check` prints
`P1 verb graded=1045 offenders=461 waived=0` and exits 0, and `grep -n VERB_OFFENDER_PIN
.lexicon.conf` returns `461`. Rev-2 reasoned that `classify` is already among the unruled offenders
the P1 split reports, which does not save it: P1 counts offenders per OCCURRENCE and not per distinct
name, so a new definition is a new offender however many namesakes it has.

Staged and measured rather than predicted. With all six identifiers appended to
`tools/lexicon/subtokens.py` as bare definitions, the same command prints
`P1 verb graded=1049 offenders=462`, exits 1, and leads with
`lexicon: verb offenders 462 over pin 461`. Restoring the file returns it to
`graded=1045 offenders=461` and exit 0.

**Two numbers in that measurement move for different reasons, and separating them is the whole
budget.** `graded` moves by FOUR because P1 grades function definitions, so `read_core`, `classify`,
`check_convention` and `read_stem` all enter the population. `offenders` moves by ONE because only
`classify` leads with an undeclared token. `_AFFIX` and `_FORMS` are module-body assignments, which
P1 does not grade at all — their `--suggest` refusals are real and cost this landing nothing. The
other two pins do not move either: the same staged run prints `P2 suffix graded=41 offenders=0` and
`P3 layer graded=557 offenders=0`, unchanged.

So the landing commit raises the pin `461` -> `462` in the conf's existing RAISED-by-name comment
form, naming `classify` as the sole arrival and carrying the command that measured it. That is AC11,
and it is why `### Rollout` no longer claims this unit moves no verdict. The leg an unbudgeted pin
would have red is `lexicon naming predicates` — the same leg §7 nominates — so the omission would
have red this unit's own verification route on its own landing commit.

### Rollout

**The predicate lands INERT as code and NOT inert on the bar, and rev-2 conflated those two.** The
first half stands: the predicate is reachable only from a cell declared in `CELLS`, the tracked
declaration carries no `CELLS` block at all — `grep -nE '^[A-Z]+:' .lexicon.conf` returns `VERBS:`
and `LAYERS:` and nothing else — and this unit adds none. Arming belongs to the two units §3 now
names, at build orders 4 and 7.

**One verdict on the bar DOES move, so rev-2's "without moving a single verdict" is struck.** The
`def classify` this unit mints is a P1 verb offender against a pin with zero headroom, so the landing
commit raises that pin. The arithmetic, the staged measurement and the criterion are
`### The pin this unit raises` and AC11.

**Every criterion phrased against an ARMED cell is therefore measured in a scratch declaration, and
each one now says so.** A scratch declaration is a `CELLS` block written into the working-tree
`.lexicon.conf` and never committed: `main()` resolves the root with `git rev-parse --show-toplevel`
and `run()` opens `root / CONF_NAME`, so the engine takes no `--conf` flag and no fixture repo is
needed. The corpus is still the real tracked tree, which is why AC3, AC4, AC6 and AC7 keep the tree's
own denominators. AC6 already took this route at rev-2 and the other seven criteria now match it;
rev-2 phrased them against the bar's own declaration, where none of them could be observed at all.

**What is DEFERRED, named rather than implied.** The STANDING verdict for each cell against the
tracked declaration is not this unit's to observe, because this unit arms nothing:
`py.constant` is `TOOL-aSurfacedLexicon-6`'s at order 4, and every other cell —
including the four file cells whose dotfile stem rule `### The empty-core population` hands off — is
`TOOL-aSurfacedLexicon-12`'s at order 7. What is NOT deferred is the observed-RED obligation. Both
staged breaks, AC1's `loadUserData` and AC10's `_`, are observed RED against a scratch declaration
before this unit is called done, which is where "a new predicate is not landed until its failing case
has been observed" is actually discharged. Deferring the failing case to the arming unit would have
been the same rule broken quietly, and it is the reason the scratch route was taken over the
alternative of pulling `CELLS` rows into this unit's scope.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/lexicon/subtokens.py` | `_AFFIX`, `_FORMS`, `read_core`, `classify`, `read_stem`, `check_convention`, and the sibling-not-consumer paragraph in the docstring |
| `tools/lexicon/lexicon.py` | call the predicate from the corpus walk per armed cell, and print the verdict and teeth lines |
| `tools/lexicon/selftest.py` | red and green fixtures per verdict, the staged-break arm, the teeth arm, the stem arm |
| `tools/lexicon/README.md` | the convention paragraph, replacing a promise with a description |
| `.lexicon.conf` | `VERB_OFFENDER_PIN` `461` -> `462` in the RAISED-by-name comment form, `classify` named as the sole arrival (AC11). NO `CELLS` row: this unit arms nothing |
| `memory/map/generated/symbols.json` | regenerated by `python tools/codebase-map/gen_map.py --write` in the same commit (AC12) |
| `memory/map/features/lexicon.md` | dossier prose refreshed on touch, per the charter DoD. No new claim is owed — see AC12 |

The last three rows are rev-3's, and each closes a way this unit would have red a leg it never named.

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
  zero violations and nothing else is indistinguishable from a cell that cannot fail. At rev-2 that
  requirement was scope with NO criterion, so an implementation shipping no teeth line at all passed
  all ten criteria — the section defeating green-by-absence, shipping green by absence. AC6 is now
  its criterion and observes the printed line rather than the figure behind it.
- risks (concurrency, data-loss, rollback hazards) — it writes no runtime state, but it is NOT
  verdict-neutral on the bar, and rev-2 claimed it was. The AC11 pin raise is an edit to the tracked
  declaration, so a revert of this unit must revert the pin with it: leaving `462` standing over a
  population that shrank back to 461 reds `lexicon naming predicates` under
  `TOOL-aSurfacedLexicon-4`'s two-sided equality. The build-wide concurrency risk lives in the pin
  block, which is that same unit's fork, and this raise is a second writer to it.
- testing + left-shift gates — the staged break is the DoD, not the fixtures. Both the prototype's
  breaks are re-staged into the real kit and observed RED, then unstaged and observed back at
  baseline. The AMBIGUOUS arm has no in-corpus instance and is exercised by a staged fixture, which
  every report of it must say. That statement now applies to the NON-EMPTY-core half only. The
  EMPTY-core half has a live in-corpus population of nine tracked dotfiles, per `### The empty-core
  population`, so its arm is a real red held latent by four dark cells rather than a synthetic one.
  No new bar leg is added, so no ceiling and no `memory/project/testsuite-count-waivers.txt` row is
  owed.
- migration / rollback — additive. Revert is one module plus one call site while this unit stands
  alone, and the AC11 pin raise reverts with it per the risks bullet above. It stops being free at
  build order 4: `TOOL-aSurfacedLexicon-6` arms `py.constant` on the `screaming` form this unit
  mints — read at its rev-2, whose S5 calls that row the build's FIRST armed cell and calls this
  unit's `_FORMS` mapping a hard prerequisite for it — so a revert from that order onward takes an
  armed cell down with the predicate. Rev-3 left this bullet saying no declaration references
  the predicate until the conf rewrite arms a cell, the absolute §3 and `### Rollout` had already
  struck one revision earlier.
- user docs — `tools/lexicon/README.md` replaces the standing convention promise with a description of
  what actually ships, including that shell and markdown are dark and why.

## 6. Acceptance criteria

**Every criterion below that grades an ARMED cell names the declaration it is measured against**, per
`### Rollout`. That declaration is a scratch `CELLS` block in the working-tree `.lexicon.conf`, never
committed, because this unit arms nothing and the bar's own declaration has no cell for these
criteria to grade. Rev-2 phrased seven of them against the tracked declaration, where none of the
seven — including both observed-RED obligations — could be observed at all. The corpus is unchanged
either way, so every denominator below is still the real tracked tree's.

- **AC1** — With a scratch declaration arming `py.function snake` and `def loadUserData` staged into
  a tracked `.py` file, `python tools/lexicon/lexicon.py --check` REDS `py.function` with the message
  `VIOLATION  loadUserData  satisfies camel, not snake`; unstaging the definition returns the run to
  that scratch declaration's baseline, and removing the scratch block returns it to the tracked one.
  The RED is observed and recorded before this unit is called done. This is one of the two
  observed-RED obligations `### Rollout` refuses to defer.
- **AC2** — With a scratch declaration arming `py.type pascal` and `class user_record` staged into a
  tracked `.py` file, `--check` REDS `py.type` with `VIOLATION  user_record  satisfies snake, not
  pascal`; unstaging returns to that declaration's baseline.
- **AC3** — With a scratch declaration arming `py.function snake` and `py.type pascal` and nothing
  staged, `python tools/lexicon/lexicon.py --check` reports `py.function` at 0 violations of 976 and
  `py.type` at 0 of 41, and `__init__` and `_build_index` are among the passing names rather than the
  offenders. Re-measured at `693bcf96` by an `ast` walk over the 49 files `git ls-files "*.py"`
  returns, stripping affixes with S2's `_AFFIX` before matching: 976 function definitions, 41
  classes, 0 snake violations. Rev-1's denominators, 925 and 39, are stale and were corrected at
  rev-2; the zero itself has never moved.
- **AC4** — With a scratch declaration arming `py.file snake` and `sh.file kebab` and nothing staged,
  the same command reports `py.file.conv 8` naming exactly `aiosqlite-seam-conftest.py`,
  `check-arms.py`, `check-kit-placeholders.py`, `check-recall.py`, `check-spec-tokens.py`,
  `merge-rows.py`, `ps-hygiene.py` and `settings-merge.py`, and `sh.file.conv 5`. Re-measured at
  `693bcf96` by first-dot stemming over `git ls-files "*.py"` and `git ls-files "*.sh"`, whose
  denominators are 49 and 94. Rev-1's `7` and `4` are stale, and `tools/check-kit-placeholders.py` is
  the basename that joined the Python list. This is the failing case observed over the real tracked
  population rather than staged: the eight are genuinely there, and only the declaration grading them
  is scratch.
- **AC5** — With a scratch declaration arming `py.function snake` and `def FAMILY_of` staged — an
  identifier whose core is non-empty and whose convention set is empty — `--check` REDS with a
  message naming AMBIGUOUS and NOT the word VIOLATION. Re-measured at `693bcf96`, 0 of the 1017
  Python definitions return a non-empty core with an empty set, so THIS arm has no in-corpus
  population and its only exercise is the staged fixture; every report of a green run states that.
  **That statement is scoped to the non-empty core and no further.** The empty-core arm is AC10 and
  its in-corpus population is nine, not zero.
- **AC6** — the teeth arm, and at rev-3 it observes the SHIPPED line rather than the figure behind
  it. With a scratch declaration arming `py.function snake` and nothing staged, `--check` reports
  that cell at 0 violations of 976 AND prints S8's teeth line beside the row, and that line reports
  736 for `camel` over the same 976. A second arm in `tools/lexicon/selftest.py` REDS when an armed
  cell's row carries a violation count with no teeth figure beside it. Re-measured at `693bcf96` by
  the same `ast` walk as AC3, matching the camel form against the affix-stripped core: 736 of 976.
  Rev-1's `691 of 925` is stale. **Rev-2's version asserted only the 736, from a one-off
  re-declaration of `py.function` as `camel`** — a hand-run experiment producing the number the teeth
  line would print, which an implementation shipping no teeth line at all satisfied. That left S8 as
  the only scope item in this spec with no criterion, which is H3 of the round-1 audit; folding the
  observation into this criterion closes it here rather than adding an eleventh arm for a line AC6
  was already about. This is also what makes AC3's 0-of-976 a measurement rather than an assertion
  about nothing.
- **AC7** — With a scratch declaration arming `sh.file kebab` and nothing staged, all 49 files matched
  by `git ls-files "*.test.sh"` pass, and the same declaration built on last-dot stems instead
  reports `sh.file.conv 53`. Re-measured at `693bcf96`; rev-1's `46` and `49` are stale. Rev-1 also
  reconciled the two numbers as "46 tracked scripts plus 3 frozen dated build-repro scripts = 49"; at
  49 and 53 that arithmetic no longer closes and it is RESTATED rather than patched — the remainder
  of 4 is UNVERIFIED and this criterion does not claim to account for it. What the criterion actually
  gates is the pair: every test script passes first-dot and fails last-dot.
- **AC8** — When `classify` is asked about `run`, it returns a set containing at least `snake`,
  `camel` and `kebab`; when asked about `_build_index` it returns a set containing `snake`. Both are
  selftest arms on the function directly, so the set contract is gated at the seam and not only
  through the report.
- **AC9** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after this unit, the rendered
  Skill still byte-matches, so the `lexicon wiring` leg stays green. This unit changes no placeholder.
- **AC10** — the empty-core verdict, which F1 ratified and which would otherwise land ungated. With a
  scratch declaration arming `py.function snake` and a definition literally named `_` staged into a
  tracked `.py` file — an identifier whose core is empty after the affix strip — `python
  tools/lexicon/lexicon.py --check` REDS it as AMBIGUOUS under the same message AC5 asserts, and NOT
  as a VIOLATION, and NOT by printing nothing. The RED is OBSERVED and recorded before this unit is
  called done, and unstaging returns the run to that declaration's baseline. This is the second of
  the two observed-RED obligations, and it is the reason `### Rollout` takes the scratch route rather
  than deferring the failing case to whichever unit arms `py.function`.
  A second arm calls the predicate directly: `read_core("_")` returns the empty string and the
  verdict for it is AMBIGUOUS. Unlike AC5 this arm is NOT population-free: the in-corpus population is
  the nine tracked dot-leading basenames of `### The empty-core population`, latent only because all
  four of their file cells are dark in `LANGS` today. Every report of this arm says nine, not zero.
- **AC11** — the pin, and unlike every criterion above it is measured against the TRACKED declaration,
  because that is where the cost lands. `VERB_OFFENDER_PIN` moves `461` to `462` in `.lexicon.conf`
  in the SAME commit that adds `classify`, written in that file's existing RAISED-by-name comment
  form, naming `classify` as the sole arrival and carrying
  `python tools/lexicon/lexicon.py --check` as the command that measured it. The failing case is
  observed FIRST and was staged at spec time: with the definitions in place and the pin unmoved, that
  command prints `lexicon: verb offenders 462 over pin 461` and exits 1; with the pin moved it exits
  0. No other pin moves — `SUFFIX_OFFENDER_PIN` and `LAYER_OFFENDER_PIN` stay at `0`, and the same
  staged run confirms it at `P2 suffix graded=41 offenders=0` and `P3 layer graded=557 offenders=0`.
  The arithmetic and the graded-versus-offender split are `### The pin this unit raises`.
- **AC12** — the generated map artifact. When the four new public module-level defs land in
  `tools/lexicon/subtokens.py`, `python3 tools/codebase-map/test_codebase_map.py` exits 0 on the
  commit that adds them, because `python tools/codebase-map/gen_map.py --write` ran in the same
  commit. The failing case is observed FIRST and was staged at spec time: appending a two-line
  `read_core` to that file and running the checker prints `FAIL test_generated_artifacts_are_fresh`
  and `STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write` and exits 1;
  removing it returns rc 0. `memory/map/generated/symbols.json` already indexes `subtokens` and
  `leading_verb` from this file, which declares no `__all__`, so a new public def lands in the
  artifact by the same rule; `_AFFIX` and `_FORMS` do not, being a leading-underscore name and a
  module-body assignment. **The coverage arm is NOT implicated and the staged run is the evidence:**
  it reported the freshness failure alone, with no unclaimed-inventory-key violation, so the dossier
  owes prose refreshed on touch and no new claim. Saying which of the leg's two arms bites is the
  point — the leg carries no `guard` key at all, so an unregenerated artifact reds the push.

## 7. Gates

- `lexicon naming predicates` — chunk `declarations`, subject `repo`, guard
  `["tools/", "skills/session-kickoff/", ".githooks/", ".claude/"]`, ceiling 300 s. A diff touching
  `tools/lexicon/subtokens.py` selects it. **It does NOT observe the cell verdicts, and rev-2 said it
  did.** This leg runs the engine against the repo's OWN `.lexicon.conf`, which this unit leaves with
  no `CELLS` block, so it has no armed cell for AC1 through AC7 or AC10 to grade — the whole of B1 in
  the round-1 audit. What it observes here is AC11, the pin raise, and it is the leg an unbudgeted
  `classify` would have red on this unit's own landing commit. The scratch-declaration verdicts are
  observed by the direct command each criterion names, and their standing coverage is
  `lexicon selftest` below.
- `lexicon selftest` — chunk `selftests`, subject `kit`, guard `["tools/lexicon/"]`, ceiling 880 s.
  Carries every fixture. AC5's AMBIGUOUS arm has no corpus instance and AC10's has nine, latent
  behind four dark file cells — one word for both would be wrong about one of them. It is invisible to
  the push bar, so this unit's DoD runs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` rather
  than trusting the push boundary.
- `lexicon wiring` — chunk `wiring`, subject `repo`, guard empty, ceiling 330 s. AC9's leg.
- `codebase-map kit selftest` — chunk `selftests`, subject `kit`, guard
  `["tools/codebase-map/", "tools/lib/", "tools/lexicon/"]`, ceiling 300 s, so editing `subtokens.py`
  selects it. It asserts a cross-kit contract on the lexicon's own constants and must be seen green
  under `GATE_SELFTESTS=1` in the same commit.
- `codebase-map coverage + freshness` — chunk `declarations`, subject `repo`, NO `guard` key at all,
  ceiling 300 s. **Rev-2 omitted it and named the guarded kit selftest above in its place**, which is
  a different question on a leg no push-boundary run reaches without `GATE_SELFTESTS=1`. This one runs
  on every bar including the push, and its freshness arm byte-compares
  `memory/map/generated/symbols.json` against a live re-derivation. AC12 is its arm and the regen is
  the work. Every leg fact in this section is read from `tools/gate-legs.json` as JSON rather than
  from prose beside it.
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
- rev-3 · 2026-09-04 · the round-1 spec audit's B1, B2, H2, H3 and M1 folded, every figure re-run at
  `693bcf96` rather than copied from the report. B1 was a contradiction inside this spec:
  `### Rollout` said the predicate lands inert while seven criteria graded armed cells on the
  tracked declaration,  and both could not be true. **Resolved by keeping the inert landing and re-phrasing AC1-AC5, AC7 and
  AC10 against a scratch `CELLS` block, the route AC6 already used**, with §7's first clause corrected
  to match — that leg reads the repo's own declaration and observes none of those verdicts. Rollout
  now names what is DEFERRED to the two arming units and states that the observed-RED obligation is not
  among it. B2 costs a budget line: `VERB_OFFENDER_PIN` has zero headroom at `461` and offenders count
  per occurrence, so `def classify` takes the count to `462` and reds the same leg §7 nominates.
  Staged all six identifiers and measured `graded 1045 -> 1049` against `offenders 461 -> 462` — four
  functions enter the population, one is an offender, and `_AFFIX` and `_FORMS` are module-body
  assignments P1 does not grade, so their `--suggest` refusals cost nothing. `.lexicon.conf` joins
  Files touched, AC11 is the pin raise, and Rollout's "without moving a single verdict on the bar" is
  struck. H2: the four new public defs stale `memory/map/generated/symbols.json` on an UNGUARDED leg —
  staged one def and saw `STALE symbols.json` and rc 1 — so the regen joins Files touched, AC12 is its
  arm, and the staged run's silence on the coverage arm is recorded as the reason no new dossier claim
  is owed. H3: S8's teeth line had no criterion and could ship absent; folded into AC6, which now
  observes the printed line rather than the 736 behind it. M1: §3's "the conf rewrite arms it" read as
  an absolute a sibling contradicts, and now names `TOOL-aSurfacedLexicon-6` at order 4 for
  `py.constant` and `TOOL-aSurfacedLexicon-12` at order 7 for the rest.
- rev-4 · 2026-09-04 · round-2 defect D6: the amendment rev-3 made in §3 and `### Rollout` left a
  THIRD carrier standing in §5, whose migration bullet still said no declaration references the
  predicate until the conf rewrite arms a cell. Rewritten to the two-unit boundary the other two
  sections already carry, and to say what a revert costs from build order 4 onward. The whole file
  was re-grepped for the same absolute rather than the one line the finding named —
  `grep -n -iE "conf rewrite|arms a cell|arms nothing|inert|until |references the predicate"` over
  this spec returns no fourth. `TOOL-aSurfacedLexicon-6` was OPENED at its rev-2 rather than
  asserted: its status header reads order 4, its S5 arms `py.constant` as the build's first armed
  cell and names this unit's `screaming` form a hard prerequisite, and its `### Rollout` names
  `TOOL-aSurfacedLexicon-12` as the order-7 conf rewrite. Both specs agree on which unit arms the
  first cell and when. No figure moved, so nothing was re-measured.

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

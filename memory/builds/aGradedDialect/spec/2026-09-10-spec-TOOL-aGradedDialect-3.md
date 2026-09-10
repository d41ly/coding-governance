# TOOL-aGradedDialect-3 — the TypeScript extractor: a tokenizer, a definition locator, and a coverage mode it has to earn

**Status:** CLOSED · rev-4 · 2026-09-10 · node a · Tier-2 · base d1357673 · streams tooling · order 3 · ratified 2026-09-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-build-TOOL-aGradedDialect-3-acceptance.md](../build/2026-09-10-build-TOOL-aGradedDialect-3-acceptance.md) | journal | — |
| [2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md](../prompts/2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md) | journal | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-prompt-TOOL-aGradedDialect-3-brief.md](../prompts/2026-09-10-prompt-TOOL-aGradedDialect-3-brief.md) | journal | — |
| [2026-09-10-review-TOOL-aGradedDialect-1-diff-round1.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-diff-round1.md) | diff-review | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round1.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round1.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round2.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round2.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round3.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round3.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |

<!-- /gen:spec-records -->

## 1. Goal

Build the reader `TOOL-aGradedDialect-1` picked — a tokenizer plus a definition locator, stdlib-only,
inside the lexicon kit — so `.ts` and `.tsx` stop being dark. The coverage mode it ships under is
MEASURED against `TOOL-aGradedDialect-2`'s floor rather than declared, because a `parser` label over
a probe-grade reading is the defect this build's README names as its own bar.

## 2. Scope (IN)

- **S1** — `scan_ts_tokens`, the tokenizer: every CODE token and nothing that is not code, over the
  constructs §4 enumerates. Observed by **AC1**.
- **S2** — `parse_ts_defs` and `parse_tsx_defs`, the locator, returning `(functions, types, imports)`
  and registered in `PARSERS` under the ids `ts-tokens` and `tsx-tokens`. Observed by **AC2**.
- **S3** — the refusals: a `SyntaxError` naming the construct and its line for a source that cannot
  be tokenized, and a header that enumerates every refusal. Observed by **AC3** and **AC4**.
- **S4** — the conformance arm that scores the reader against the frozen fixtures and the oracle
  answers `TOOL-aGradedDialect-2` commits, and compares the result to that unit's declared floor.
  Observed by **AC5**.
- **S5** — the mode verdict this unit hands `TOOL-aGradedDialect-4`, printed beside the number that
  decided it. Observed by **AC6**.
- **S6** — the dispatch that makes a tokenizer-shaped reader REACHABLE under the `probe` mode token,
  which today refuses it before it runs. Observed by **AC7**.
- **S7** — the kit hygiene this unit's own edits owe: the offender pins re-measured rather than
  raised, and the rendered Skill re-rendered. The kit VERSION stamp is deliberately not here —
  `TOOL-aGradedDialect-5` §8 F2 allocates it, and two units claiming one bump with neither observing
  it is how a stamp gets bumped twice or not at all. Observed by **AC8**.
- **S8** — `DEFINITION_SNIFF` in `tools/lexicon/lexicon.py` widened to the definition forms §4's
  locator table returns. Measured 2026-09-10 against the shipped regex, six of them sniff NEGATIVE:
  `export interface Props`, `export type Id =`, `export enum`, `export const Card: React.FC = () =>`,
  `const pick = <T,>(x) =>` and `export default function App()`. Because `extractor_carriers` is
  populated by `if funcs or types_`, a `types.ts` carrying only an `interface` and a `type` — a
  near-universal shape in a real TypeScript tree — lands in `blind` and appends the ratified
  `DEAD SNIFFER` problem, which REDS the run. So the first adopter file arming this feature reds
  their gate on the run right after `--scaffold`, which is the feature's only intended consumer
  path. Cited to `TOOL-dScaffoldedMirror-6` S6, which ratified that refusal. Observed by **AC9**.

## 3. Non-goals (OUT)

- **No fixtures, no oracle, no floor.** `TOOL-aGradedDialect-2` owns the extraction procedure, the
  on-disk fixture format and the floor number. This unit consumes all three and authors none of them,
  which is the ordering that answers `TOOL-dScaffoldedMirror-13`'s fixture objection.
- **No declaration surface.** `KNOWN_EXTS`, what `scaffold_lexicon.py` proposes for a TypeScript
  tree, and the cell matrix are `TOOL-aGradedDialect-4`'s. This unit produces a mode VERDICT and two
  parser ids; the declaration that spends them is that unit's.
- **No records.** `LEXICON.md`, the kit README, the backlog row and the map dossier are
  `TOOL-aGradedDialect-5`'s.
- **No `imports` population.** The locator returns an empty list for it, and §4 gives the reason. It
  is a refusal rather than an omission, on the precedent `parse_shell_defs` set for shell types.
- **Not an interpreter.** No type resolution, no module graph, no evaluation of what it reads. It
  tokenizes and locates, exactly as the shell reader does.
- **No verdict on `js-regex`.** Whether the shipped `.js` probe set should also retire is a different
  population and a backlog row, per `TOOL-aGradedDialect-1` §3.

### Edges

- **consumes-from** `TOOL-aGradedDialect-1` — the picked mechanism, and the construct census the
  refusal list is derived from. Without it the reader's shape is a preference rather than a pick, and
  §4's refusals would be imagined instead of priced against a measured corpus.
- **consumes-from** `TOOL-aGradedDialect-2` — the frozen fixtures, their on-disk format, and the
  declared floor. Without the floor there is no number for the mode claim to clear, and AC5 and AC6
  cannot be observed at all.
- **hands-off** `TOOL-aGradedDialect-4` — the mode verdict and the two parser ids, for `KNOWN_EXTS`
  and the scaffold proposal to spend. The tokenizer's JSX knowledge is REACHABLE but deliberately not
  exposed: the return shape stays `(functions, types, imports)`, so a per-definition returns-JSX flag
  is a shape change that unit's own fork has to spec rather than a thing this unit pre-builds.
- **hands-off** `TOOL-aGradedDialect-5` — the refusal list and the mode verdict as the sentences that
  replace the `.ts`/`.tsx` ruling, and two further record obligations §8 F1 creates: the kit README's
  modes table says a `probe` extractor IS a regex pattern set, which stops being true, and the map
  dossier claims the inventory keys §4 mints. This unit therefore does not land alone against
  `codebase-map coverage + freshness`.

## 4. Design

The seam is `tools/lexicon/lexicon.py`. The reader lands beside `_python_defs` and `parse_shell_defs`
and is reached through the `mode` dispatch in `extract_text`, which is unchanged for `parser` and
widened for `probe` by §8 F1. Every share quoted below is measured 2026-09-10 by
`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`
§4.2 against `C:/projects/incms/main`, and is PINNED with that date rather than re-derived here.

### Data model

A token is `(kind, text, line)`, the shape `scan_shell_tokens` already emits. `kind` is `word` for an
identifier, keyword or numeric literal, and `op` for the punctuation the locator needs: `( ) { } [ ]
= : ; , < > =>` and `@`. Everything else is consumed as a word break and emitted as nothing.

A string, a template literal's TEXT, a comment, a regex literal and JSX text are CONSUMED and emit no
token at all. That is the whole reason this is not a regex: a `function` keyword inside a template
literal or a JSX text child is data, and a same-line pattern cannot tell it from code.

The tokenizer carries a state STACK rather than a set of flags, because the constructs nest: a
template literal holds a `${}` expression which may hold another template literal, measured in 43.6%
of files.

### The constructs, and how each is read

| construct | files carrying it | how the tokenizer reads it |
|---|---|---|
| template literal | 90.3% | a backtick span; its text is consumed, and `${` pushes a code state |
| JSX element | 72.2% | opened by `<` at expression position; text children consumed; `{` pushes a code state |
| generic call or declaration | 56.6% | `<` and `>` emitted as ops; the locator skips balanced runs |
| nested template expression | 43.6% | the same stack, one level deeper — no second code path |
| regex literal | 24.9% | `/` decided by the previously EMITTED token, never by a lookahead pattern |
| `satisfies` operator | 2.9% | an ordinary word; it changes no definition form |
| decorator | 0.1% | `@` emitted as an op and not interpreted |
| overload signature | 0.0% | a declaration with no body; §5 says why its arm is a fixture rather than a corpus read |

Two spans are pushed as SUPPRESSED code states: a template `${}` expression and a JSX `{}` expression
container. Their contents are tokenized so the state machine stays honest about nesting and
terminators, and the locator returns no definition from inside them. That is the ported shape —
`scan_shell_tokens` treats `${…}` and `$((…))` as opaque — and its cost is bounded rather than
assumed: an object-literal method or an initializer-bound arrow written inside such a span is counted
by the oracle and missed here, and AC5's score is where that cost is paid and reported.

### The definition forms the locator recognises

Mirroring the oracle's set verbatim, so recall and precision are comparable form for form.

| form | goes to |
|---|---|
| `function <name>`, including `export`, `export default` and `async` | functions |
| a class or object-literal method, and a `get` or `set` accessor | functions |
| `constructor` | functions, under the literal name the oracle records |
| `const`, `let` or `var` bound to an arrow or a function expression | functions |
| a property or property assignment initialised to an arrow or a function expression | functions |
| `class`, `interface`, `type` and `enum` | types |

Member position is decided by a block-kind stack rather than by a control-keyword stop-list. A
statement block, a class body and an object literal are distinguishable to the tokenizer and are not
distinguishable to a regex, which is why the regex arm in `TOOL-aGradedDialect-1` needed the
stop-list at all.

### Inventory

| identifier | kind | cell that grades it | verdict |
|---|---|---|---|
| `scan_ts_tokens` | function in `lexicon.py` | `py.function` | `--suggest` answered OK on 2026-09-10 |
| `parse_ts_defs` | function in `lexicon.py` | `py.function` | `--suggest` answered OK on 2026-09-10 |
| `parse_tsx_defs` | function in `lexicon.py` | `py.function` | `--suggest` answered OK on 2026-09-10 |
| `test_ts_sentinel`, `test_ts_constructs`, `test_ts_refusals`, `test_ts_conformance` | functions in `selftest.py` | `py.function` | `--suggest` answered OK on `test_ts_sentinel`; the four mirror the `test_shell_*` arms the leg already grades green |
| `ts-tokens`, `tsx-tokens` | `PARSERS` keys | none | data keys, graded by no cell — named here so the absence is declared rather than discovered |

`parse_tsx_defs` is one line calling `parse_ts_defs` with JSX lexing on. Two public names and one
header, because the selftest asserts a docstring and a `functools.partial` carries none.

### Two ids rather than one reader plus a path

`extract_text` is handed source TEXT and a mode, never a path — `drift_report.py` calls it
positionally against git blobs at two shas and has no file to look at. The pattern-set id is already
the field that says WHICH parse, which the engine's own comment beside `PARSERS` states. So `.ts` and
`.tsx` take two ids over one reader: `.ts` lexes `<T>(x) => x` as a generic arrow, `.tsx` lexes `<T>`
as a JSX element, and one lexer mode necessarily mis-reads one of the two populations.

### Files touched (estimate)

| file | why |
|---|---|
| `tools/lexicon/lexicon.py` | the tokenizer, the locator, two `PARSERS` rows, the FOUR armedness-predicate edits F1 names, and the `DEFINITION_SNIFF` widening S8 owns |
| `tools/lexicon/selftest.py` | the sentinel, the construct arms, the refusal arms, the end-to-end arm, the conformance arm |
| `.lexicon.conf` | only if the new names move an offender pin, and then as a RE-MEASURED value |
| `.claude/skills/lexicon/SKILL.md` | re-rendered because its own gate byte-compares it against the declaration; the version placeholder it carries is bumped by `TOOL-aGradedDialect-5` |

### Alternatives rejected

| option | the reason it loses |
|---|---|
| a `ts-regex` entry in `PATTERN_SETS` | `TOOL-aGradedDialect-1` killed it on a pre-registered test: two plausible regex sets disagree on 22.4% of the function population |
| one parser id, with the extension passed in | `extract_text`'s positional contract is frozen and it is handed text, never a path |
| JSX lexing enabled for both extensions | generics appear in 56.6% of files, and `<T>(x) => x` is a generic arrow in `.ts` and an element in `.tsx` |
| a real `imports` list | the corpus walk discards the third element, and the only import consumer reads the kit's own Python directly, so it would be an ungraded population and a fixture obligation for nothing |
| a new mode TOKEN for "tokenizer but incomplete" | the engine's own comment refuses it: `LANG_MODE_RANK` reads an unknown mode as absent, so a strengthening edit would fire a weakening finding |

## 5. Production-readiness checklist

- security — the reader never evaluates, expands or executes what it reads, and imports stdlib only;
  the kit's self-containment refusal reds on any import that is neither stdlib nor a sibling file. It
  treats adopter source as untrusted TEXT and returns names and line numbers.
- perf / scale — the reader is a single pass per file and the fixtures are bounded by
  `TOOL-aGradedDialect-2`'s corpus size. The wall-clock ceiling this unit must stay under is the
  `lexicon selftest` row in `tools/gate-legs.json`, READ there and deliberately not typed here: an
  earlier revision stated 300 s against a manifest that declares roughly three times that, which is
  a number typed beside the source that owns it and is what this build's README forbids.

- error / empty / loading states — three states and no fourth. A file that tokenizes returns a list,
  possibly empty for a file that defines nothing. A file that does not tokenize RAISES, which
  `scan_corpus` surfaces as a named refusal. A file that cannot be read is already a separate refusal
  and stays separate, because an unreadable file is not an unparseable one.
- observability — the green `lexicon OK` line prints a mode for every DECLARED extension, dark ones
  included, and prints nothing at all on a red run; both halves of "every run prints the mode per
  armed extension" were wrong and round 3 said so. What carries the mode on a failure is the
  conformance arm's own printed verdict, which reports the measured score beside the floor rather
  than a boolean, so a run says by how much it cleared or missed.
- risks — the reader is hand-written and its blind spots are whatever the fixtures do not carry, and
  the fixtures come from ONE adopter tree, so a construct absent there is untested rather than
  proven. The overload-signature refusal is the named instance: 0.0% of that corpus, so its arm is a
  frozen fixture in the kit and can never be a corpus read. The second risk is rot — the mode verdict
  is measured once, and the conformance arm on the kit suite is what keeps it from surviving an edit
  that invalidates it.
- testing — a frozen sentinel is the kit-side vacuity arm, since the corpus-side `DEAD PROBE` arm is
  defeated by a corpus with nothing to find. Beside it: one arm per definition form, one per construct
  that defeats a line regex, one per refusal with a needle no sibling refusal's message contains, one
  end-to-end arm over a fixture declaration, and the conformance arm. The refusals with no runtime
  behaviour are observed as docstring assertions, the shape `test_shell_refusals` already uses.
- migration — none. Both extensions are dark today, so this adds a graded population and empties
  none, which `LANG_MODE_RANK` reads as a strengthening. No adopter declaration is rewritten by this
  unit; `TOOL-aGradedDialect-4` owns what the scaffold proposes to a new tree.
- user docs — none in this unit. `TOOL-aGradedDialect-5` owns every reader-facing carrier and takes
  the refusal list and the mode verdict from here.

## 6. Acceptance criteria

- **AC1** — When `tools/lexicon/selftest.py` runs, the tokenizer arms return no definition for a
  `function` keyword inside a template literal, a regex literal carrying a brace, JSX text carrying a
  fat arrow, or a nested template expression.
  `cost:` those arms live in the `lexicon selftest` leg, which the bar HOLDS as a `selftests` chunk,
  so this unit's Definition of Done runs `GATE_SELFTESTS=1`.
  Red when: a word token escapes a string, template span, comment, regex literal or JSX text, so one
  of those arms reports a name that no definition site produced.
- **AC2** — When `tools/lexicon/selftest.py` runs its frozen TypeScript sentinel through
  `parse_ts_defs`, every recognised definition form comes back once, at the line its NAME sits on,
  and the types list carries the class, the interface, the type alias and the enum.
  Red when: a form is located at its body's line rather than its name's, which still reads as
  coverage and points a reader at the wrong line.
- **AC3** — When each unterminated construct is fed to `parse_ts_defs`, it raises `SyntaxError`
  naming that construct and the line it opened on, and no row's needle is a substring of another's.
  Red when: a construct returns a list instead of raising, or two rows share a needle, so one refusal
  firing first scores a pass for a sibling that is unarmed.
- **AC4** — When `tools/lexicon/selftest.py` reads `parse_ts_defs.__doc__`, every refusal this unit
  implements is named there, including the two that have no runtime behaviour to stage.
  Red when: a refusal ships with no line in the header, which is the half no runtime arm can observe.
- **AC5** — When the conformance arm runs the reader over the frozen fixtures `TOOL-aGradedDialect-2`
  commits, it prints function and type recall and precision against the recorded oracle answers, and
  compares each to that unit's declared floor.
  `figure:` DERIVED at observation time from the fixtures; no score is written into this spec.
  `fixture:` the fixtures and the floor are `TOOL-aGradedDialect-2`'s and are absent from the tree
  today, so until that unit lands this criterion cannot be observed and the arm REFUSES rather than
  reporting a score.
  Red when: the arm reports a score over an empty or absent fixture set, which is the
  fixture-passes-by-finding-nothing class this build's README names.
- **AC6** — When the conformance arm finishes, it prints the mode this unit hands
  `TOOL-aGradedDialect-4` — `parser` at or above the floor and `probe` below it — beside the measured
  number that decided it.
  Red when: it prints `parser` under a below-floor score, which is the label-over-the-reading defect
  the build README names as its own acceptance bar.
- **AC7** — When a fixture declaration arming a `probe` row whose pattern-set id names a parser is
  graded end to end, the run reads that corpus and reports the extension as armed, rather than
  refusing the row as a set the kit does not ship.
  The same run's printed `coverage — armed` line COUNTS that fixture's `.ts` files, which is the
  reporting half of F1's four sites and is asserted separately: a row can extract correctly and still
  be tallied unarmed, and a criterion that observed only the extraction would not see it.
  Red when: the run refuses with the unshipped-set message, which is what `tools/lexicon/lexicon.py`
  does today and is the entire reason §8 F1 exists. Red also when the extension extracts but the
  coverage line does not count it, which is the two reporting sites disagreeing with the two
  dispatch sites.
- **AC8** — When `python tools/lexicon/lexicon.py` runs over this repo after the unit lands, it exits
  0, and any movement in `VERB_OFFENDER_PIN` is a re-measured value committed beside the names that
  moved it.
  Red when: a pin is RAISED to absorb a new name rather than the name being changed, which turns a
  two-sided equality into a rubber stamp.
- **AC9** — When `tools/lexicon/selftest.py` grades a fixture tree whose only `.tsx` file defines
  exactly one typed const arrow and one `interface`, and whose only `.ts` file defines exactly one
  `export type` and one `export enum`, the run reports an EMPTY `blind` set and prints no
  `DEAD SNIFFER` problem.
  `fixture:` a new fixture in `selftest.py`; the tree this repo tracks carries zero `.ts` files, so
  no bar over gov's own corpus can observe this and a fixture is the only route.
  The same run FIRST asserts a positive: it reports non-zero graded populations for `ts` and `tsx`,
  with both fixture files appearing as extractor carriers. An empty `blind` set is only evidence once
  something was extracted — an unarmed fixture produces the same empty set and would satisfy a pure
  negative.
  Red when: `DEFINITION_SNIFF` is narrowed BACK to the rows shipped before this unit, and the arm
  reports the fixture's carriers as blind. Rev-3 said dropping `interface` alone was enough and
  measured against this fixture it is not: each file sniffs positive through TWO of the widened
  rows — the `.tsx` file through `interface` AND through the const row, because its arrow carries a
  type annotation, and the `.ts` file through `type` AND through `enum` — so no single row's
  removal blinds either, and the staged break reverts the whole three-row widening, which blinds
  both. Red also when `blind` is empty over ZERO extractor
  carriers, which is the fixture proving nothing rather than the sniffer agreeing. The arm is written per ARMED LANGUAGE rather than per
  file: the fixture table is the whole declaration and the `LANGS` rows, the `CELLS` rows and the
  assertions are all derived from it, so a language added there inherits the check instead of
  rediscovering the refusal.
## 7. Gates

`lexicon selftest` · `lexicon naming predicates` · `lexicon wiring` · `codebase-map kit selftest` · `memory hygiene`

`lexicon selftest` is a `selftests` chunk with a `kit` subject, so an ordinary bar HOLDS it and AC1
through AC7 and AC9 are observed only under `GATE_SELFTESTS=1`. AC8 is the exception: it is the
`lexicon naming predicates` leg, which an ordinary bar runs. That is stated here rather than left to be
discovered, because this is KIT work and the 2026-08-23 owner ruling says a kit's Definition of Done
is the one that owes those legs.

New arm: `tools/lexicon/selftest.py` · a tokenizer that emits a word out of a template literal, a locator that misses a recognised form, a refusal that returns a list instead of raising · none

New arm: `tools/lexicon/selftest.py` · the conformance run scoring below the declared floor while the printed mode still reads `parser` · none — the floor is `TOOL-aGradedDialect-2`'s declared number and this unit does not move it

New arm: `tools/lexicon/selftest.py` · `DEFINITION_SNIFF` narrowed back to the rows shipped before this unit, so the types-only fixture reports its carriers as blind and the run prints `DEAD SNIFFER` · none

## 8. Open questions

- **F1 — how does a tokenizer-shaped reader become reachable under the `probe` mode token?** Today it
  cannot: `extract_text` reaches `PARSERS` only under `mode == "parser"`, and `scan_corpus` refuses a
  `probe` row whose pattern-set id is not a regex set, one line before the extension can be graded at
  all. So the build README's rule that whatever ships declares `parser` or `probe` is mechanically
  false for half of its own vocabulary, and a below-floor reading would have nowhere to go.
  Four options were weighed. Widen the probe dispatch so the pset id selects the READER and the mode
  token carries only the STANDING. Ship `dark` below the floor instead. Mint a new mode token. Ship a
  regex set alongside so `probe` has something to run.
  RESOLVED (agent, 2026-09-10, delegated): widen the dispatch. A new mode token is refused by the
  engine's own comment, since `LANG_MODE_RANK` reads an unknown mode as absent and a strengthening
  edit would fire a weakening finding. A regex set is `TOOL-aGradedDialect-1`'s candidate C1 and lost
  its pre-registered test. `dark` empties a graded population the drift signal reads as a weakening,
  and it contradicts the build-level rule above. The survivor trips no M3 veto: no new dependency, no
  new install location, no signature change, and no governance carrier moves. It is also the reading
  the modes table's own third column already carries, and the one `LANG_MODE_RANK` already ranks.
  FOUR edit sites, not two, and the count is the correction: the armedness predicate — "is this
  (extension, mode, pset) actually graded by something" — is spelled at four places in
  `tools/lexicon/lexicon.py`, and an earlier revision named only the two that DISPATCH. The two
  dispatch sites are the `probe` branch of `extract_text`, which reaches `PARSERS` when the id names
  one, and the matching refusal in `scan_corpus`, which skips such an id. The two REPORTING sites are
  the coverage-fraction walk and the armed-extension tally, which decide armedness independently and
  would otherwise count a `probe`-declared parser as unarmed while the extractor read it — the
  fraction and the extraction disagreeing about the same file. All four call ONE derived helper so
  they cannot diverge again. `_probe_defs` and the `parser` branch are untouched. The cost is a record: the kit README's modes
  table names a `probe` extractor as a regex pattern set, which stops being true, and that sentence
  is handed to `TOOL-aGradedDialect-5` in §3's Edges rather than left standing beside code that
  contradicts it.
- **F2 — is a definition inside a template expression a REFUSAL or a bug?** A `${}` span holds real
  code, so an object-literal method or an initializer-bound arrow written there is a definition the
  oracle counts. Two options: suppress those spans and declare the refusal, or tokenize into them and
  locate there.
  RESOLVED (agent, 2026-09-10, delegated): suppress and declare. The refusal's cost is not argued
  away — it is priced by AC5 against the floor, so a suppression that costs too much reds the mode
  claim rather than passing quietly. Locating inside those spans buys recall the fixtures may not
  even exercise, at the price of the nesting the tokenizer is most likely to get wrong. Tie-break:
  reuse of the seam §10 names, since `scan_shell_tokens` already treats `${…}` and `$((…))` as opaque
  spans and this is that ratified design ported rather than a second answer to the same question.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft.
- rev-2 · 2026-09-10 · S7 · S8 · §4 · §5 · §8 · AC7 · AC9 · folded spec-audit round 2. NEW S8 and
  AC9: arming TypeScript walks into the ratified `DEAD SNIFFER` refusal, because six of §4's
  definition forms sniff negative against the shipped `DEFINITION_SNIFF` and a types-only module
  therefore lands in `blind` — the first adopter file after `--scaffold` would red their gate. §8 F1
  named two edit sites and the armedness predicate lives at four; the two REPORTING sites are now
  named and all four route through one derived helper, with AC7 gaining the coverage-line clause
  that observes them. S7 and Files-touched no longer claim the kit version stamp, which
  `TOOL-aGradedDialect-5` §8 F2 allocates and which neither unit was observing. §5's perf row stated
  a 300 s leg ceiling against a manifest declaring roughly three times that, and now points at
  `tools/gate-legs.json` instead of restating it. §7's held-leg sentence named AC1 through AC7 and was the
  amendment's other half once AC9 arrived; it now names AC9 too and states that AC8 alone rides the
  ordinary bar. §7 also gained the `New arm:` line for AC9's staged break, which every other arm in
  this unit already carried.
- rev-4 · 2026-09-10 · §7 · AC9 · the build's own divergences, changed here before the code. TWO.
  AC9's Red-when claimed a single-row narrowing of `DEFINITION_SNIFF` would blind the fixture, and
  measured against the fixture AC9 itself specifies it does not: both files sniff positive through
  two of the widened rows each, so the staged break reverts the whole widening. §7's matching
  `New arm:` line carried the same claim and moves with it. SECOND, the conformance arm's reader
  lookup: `read_ts_readers` read `KNOWN_EXTS`, which §3 forbids this unit to touch, so the SKIP
  could not have been removed without changing what that function reads. It now reads `PARSERS`
  against the two ids S2 names, which is the honest source — `KNOWN_EXTS` is the DECLARATION and
  `TOOL-aGradedDialect-4`'s, and a floor measurable only after the declaration landed would be
  measured by the unit that spends the verdict rather than the one that earns it. The arm scores
  under the `probe` mode token for the same reason: the token cannot change the reading, so the
  weaker one costs nothing and stops the run passing over a dispatch that only works for `parser`.
- rev-3 · 2026-09-10 · §5 · AC9 · folded spec-audit round 3, the disposal round. AC9 was a pure
  NEGATIVE — an empty `blind` set — which an unarmed fixture satisfies exactly as well as a widened
  sniffer does, so it now asserts non-zero graded populations for both extensions FIRST and carries
  a second Red-when for the zero-carrier case. §5's observability row claimed every run prints the
  mode per armed extension; the real line prints per DECLARED extension and only on a green run.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "extract function and type definitions from a source file
for a language the kit does not parse"` ranked `extract` at fan-in 6 and `extract_text` at fan-in 2,
both in `tools/lexicon/lexicon.py`, which is the dispatch this unit extends. The seam this unit
builds on is that file's `scan_shell_tokens` and `parse_shell_defs` pair together with the `PARSERS`
table beside them — the ratified precedent for a hand-written reader in this kit — and the extension
point is the `mode` dispatch in `extract_text`. Verified against source on 2026-09-10: both functions
exist at that path, `PARSERS` is keyed by pattern-set id, and `extract_text` reads `pset` under
`parser` and under `probe` by two different rules, which is what §8 F1 is about. Two probe caveats
are recorded rather than left implicit. The probe reports `unscanned layers: .sh`, so no claim here
rests on its silence about shell. A second phrasing of the same question — "tokenize a source file
and locate its function and type definition sites" — ranked NEITHER of those two functions, which is
the miss half of the probe-failure taxonomy and the reason the phrasing above is written down.

Recall terms used: `lexicon typescript tsx probe parser dark PATTERN_SETS coverage extractor
PascalCase React casing tokenizer adopter`

<!-- gov:kit lexicon@1.3 -->
# lexicon — a declared naming vocabulary, gated

An OPT-IN kit that gates two naming predicates against a per-repo DECLARATION, and refuses an import
that would make the kit itself non-portable. It is inert until `.lexicon.conf` exists at the repo
root, and removing that file un-adopts it.

**What it is for, since it is not typo-catching.** A closed verb table makes "which verb is this"
answerable only when a function has ONE responsibility. A name that will not fit the table is
reporting an unclear responsibility or a seam in the wrong place. That is the whole value.

**It USED to say that value was not measurable, and that the kit was opt-in because of it.** The
first half is superseded by `TOOL-dScaffoldedMirror-17`: `drift-audit`'s
`lexicon_marginal_offense_rate` derives offenders-added per definition-added between the commit that
adopted the declaration and HEAD, both operands produced by this kit's own extractor at both shas.
The kit stays OPT-IN — that did not change — but it is opt-in because adopting a vocabulary is a
choice, not because nobody could tell whether it works.

## The two predicates

| | Asserts | Scope |
|---|---|---|
| **P1** | every function or method DEFINED in the corpus leads with a verb from the declared `VERBS` table | definition sites |
| **P2** | no type DEFINED in the corpus ends with a declared `BANNED_SUFFIXES` entry | definition sites only — never an imported type, a parameter name, or a parameter type |

## The declaration grammar

`.lexicon.conf` is the sibling `KEY=VALUE` form plus BLOCK keys — a `KEY:` header followed by indented
rows, ending at the first non-indented line. Blank lines inside a block are skipped rather than
terminating it. The declared block keys are `BLOCK_KEYS` in `lexicon_conf.py` and are not counted
here; a header outside that set is a refusal by name, not a silent skip.

| Block | Row | Means |
|---|---|---|
| `VERBS` | `<verb>  <gloss>` | the closed verb table P1 grades against; the gloss carries the NOT clause |
| `CELLS` | `<ext>.<surface>[+<kind>:<literal>]  <convention> [vocab]` | which case convention this (language, surface) cell asks for |
| `PINS` | `<cell>.<predicate>  <count>` | the declared offender count for one cell and one predicate |
| `CANON` | `[-]<representative>  <alternative>...` | the OWNER's overlay over the frozen shipped canon; see below |

`surface` is one of `function` `type` `file` `constant`; `convention` is one of `snake` `screaming`
`camel` `pascal` `kebab` `dark`; `predicate` is one of `debt` `unruled` `conv`. A token
outside its closed set names the file and the line. `dot` is deliberately NOT a declarable
convention: it is a classifier form the report uses so a dotted name is reported as satisfying
something, and no language convention is "identifiers contain dots".

Three refusals are CROSS-BLOCK and run after the whole file is parsed, because `LANGS` may be
declared below `CELLS` and a reader that refuses on line order refuses a legal file. A `CELLS` row
naming an extension `LANGS` does not declare reds; a `PINS` row naming a cell with no `CELLS` row
reds; and a `decorator` selector on a language `LANGS` declares `probe` or `dark` reds, naming both,
because decorators come from a real parse and that subset could only ever be empty.

### The selector — routing a SUBSET of a cell to a second convention

A `CELLS` row key may carry ONE selector clause, `+<kind>:<literal>`, with `kind` in `prefix`
`decorator`. It splits the cell's population in two: the names the selector matches are graded ONCE,
against the selector's own convention and its own pin, and they LEAVE the parent cell's population.
The parent keeps its own row and grades the complement.

```
CELLS:
  py.function                     snake

  py.function+prefix:Test         pascal

PINS:
  py.function.conv                0

  py.function+prefix:Test.conv    2
```

It exists for the languages whose case is a function of ROLE rather than of surface — Go's export
rule, React's PascalCase components — where one `(language, surface)` cell would red half a correct
codebase, and the only honest alternative is declaring the language `dark`.

- **A routed name is graded once**, never against both conventions. Grading it twice would make
  every routed name a guaranteed violation of one of the two cells.
- **A name matching TWO selectors is REFUSED**, naming both literals, and is graded by neither. A
  verdict that depends on which row the reader saw first is not a declaration. That refusal plus
  `DEAD CELL` covers an overlapping pair completely: two selectors that CAN both match either do
  both match some name, or one of them selected nothing and reds as a dead cell.
- **A selector matching NOTHING reds** as a `DEAD CELL`, like any other cell grading an empty
  population.
- **A selector'd cell with no `PINS` row of its own reads as a pin of `0`.** It never inherits the
  parent's count, and its offenders are never folded back into the parent's row — the two ratchet
  separately, in both directions.
- **The literal carries no dot**, because a `PINS` row key is `<cell>.<predicate>` split on the dot.
  A dotted decorator (`@app.route`) is matched on its LAST segment, so it is selectable as `route`.
- There is no regex kind, and no suffix or infix kind. A predicate language over names is a second
  grading language inside a naming gate; the two motivating populations use a prefix.

The selector row prints directly beneath its parent, with its own count, denominator and rule, so a
routed subset is visible rather than a silent subtraction from the row above it.

**Pin rows are BLANK-SEPARATED, and the reader refuses a dense pair.** That whitespace is a merge
property rather than a formatting preference: two branches each draining a neighbouring cell conflict
when the rows are adjacent, and neighbouring cells are the likeliest concurrent pair because related
cells sit together. One blank line gives git the context line that makes those merges clean. A
comment line between two rows satisfies the rule too.

**Every pin is a TWO-SIDED equality.** A count that falls reds exactly as one that rises does. The
rise names the new offenders; the fall prints the exact replacement row to paste, because the two
directions call for opposite actions. A one-sided ratchet lets a pin sit above a corpus that already
drained under it, which is a number nobody is obliged to re-measure and therefore a number nobody
re-measures.

## The convention predicate

A `CELLS` row arms it. For every name in that cell's population the classifier strips leading and
trailing underscores — they are privacy markers, not case — and reports the SET of forms the
remaining core satisfies. Three verdicts and no fourth:

| Verdict | When | Reds |
|---|---|---|
| `SATISFIED` | the declared convention is IN the set | no |
| `VIOLATION` | the set is non-empty and the declared convention is not in it | yes, naming what the name DOES satisfy |
| `AMBIGUOUS` | the set is EMPTY, whether or not the core is | yes, under a message distinct from `VIOLATION` |

**The set is the design, not a defensive shape.** `run` satisfies `snake`, `camel`, `kebab` and
`dot` at once, and hundreds of this repo's Python definitions satisfy two or more forms, so a
single-label classifier reports a violation for every one of them the moment the declared cell is
not the label it happened to pick. A VIOLATION is therefore "the convention is not IN the set", never
"it is not the set's first member".

**The classifier is `subtokens()`'s sibling, not its consumer.** That splitter LOWERCASES, so
`BuildIndex` and `build_index` are indistinguishable after it and no case question survives it. The
convention check reads the RAW name. The two also disagree about what "no word characters" means and
the divergence is deliberate: `leading_verb` calls such a name UNGRADEABLE, the convention check reds
it as AMBIGUOUS. A name that is nothing but underscores is a legal Python definition and skipping it
would be a skip wearing a pass's clothes.

**A `file` cell grades the basename up to its FIRST dot.** `map_extractors.template.py` grades on
`map_extractors` and `check-arms.test.sh` on `check-arms`. Last-dot stemming would keep the interior
dot and red every compound extension in a tree on day one — measured here, 5 violations become 53,
and 49 of the arrivals are this repo's own shell test scripts. The consequence to know before arming
one: a DOT-LEADING basename stems to the empty string and reds AMBIGUOUS, so `.gitignore` is
correctly named by every convention anyone would declare and would still red. That is the classifier
saying it was handed nothing to grade, and the answer at arming time is a dotfile stem rule or an
explicit `dark` declaration — not a silent skip.

**Every armed cell also prints TEETH**: how many of the SAME names each other convention would have
failed. A cell reporting zero violations and nothing else is indistinguishable from a cell whose
predicate never ran, and the teeth are what tell the two apart on a green run.

**Every row also prints the POPULATION RULE that selected its denominator**, because a count with no
rule beside it reads as coverage when it is only a scope:

    lexicon: py.constant.conv <bad> of <graded> against screaming — violation <v>, ambiguous <a>,
    teeth camel=<n> kebab=<n> pascal=<n> snake=<n>;
    population <graded> of <denominator> (rule: public simple module-body assignments)

The figures are PLACEHOLDERS on purpose. This block carried a literal transcript, and all five of
its numbers were already wrong on the day it landed — while `.lexicon.conf` carries the same two
figures under a selftest arm that reads them out of the conf by anchored regex and compares them
against what `--check` prints. One gated carrier and one ungated copy of one fact, disagreeing, in
the file an adopter reads first (closing review M6). For the real numbers run the gate:
`python {kit}/lexicon.py`.

The denominator is the WIDER population the rule narrowed, not the graded count restated. A row
whose two figures are equal is legal and common — every `function` cell narrows nothing — and the
point of printing both is that `py.constant` does. The rule string is DECLARED beside its selector
in `CELL_POPULATION_RULES`, never derived from a docstring: two carriers of one fact with no gate
comparing them is the class this kit exists to close.

`screaming` and `pascal` are declarable; `dot` is a classifier form only. A surface in the closed
set with no row in `CELL_POPULATION_RULES` is an `UNRULED SURFACE` refusal — the cell would grade
nothing while reporting a clean zero, which a skip that looks like a pass always does. `sh.function`
is this declaration's first armed cell, over the 607 definitions the shell tokenizer reads, against
`snake`; `py.constant` is its second.

## The three cell refusals, and what each does NOT check

**`DEAD CELL`** — a declared, armed cell whose population rule selected NOTHING. It replaces a
report: the engine printed `armed but grading nothing` for the whole life of the declaration and
nothing ever acted on it, which is the green-by-absence class wearing a different label. Two
exemptions, both the same argument — an empty population is evidence only where a non-empty one was
possible. A `dark` row is a declared refusal to grade, so its zero is the declaration working. An
extension the corpus carries no file of is an `INERT DECLARATION`, which this engine already
reports one arm over; redding a cell for it would make two refusals disagree about one tree.
**It does not check** an armed EXTENSION with no cell row at all — that is `DEAD PROBE`, which is
still shipped and is not subsumed.

**`DEAD CELL REPORT`** — the report's own liveness, asserted as PARITY against the parsed `CELLS`
block rather than as "more than zero", so it catches the single row that goes missing as well as the
table that empties. **It does not check** a declaration carrying no `CELLS` block at all: that is a
legal inert state every adopter passes through, and refusing it would red every tree that installed
this kit before the block existed.

**`UNDECLARED CELL`** — an (extension, surface) pair the extractors produced a non-empty population
for, with no `CELLS` row. It **REFUSES**, and it ships that way: `UNDECLARED_CELL_ARMED` is `True` in
`lexicon.py`, flipped there in the same commit that first wrote a full matrix into a declaration.
It landed report-only for exactly one build order, because arming it against a declaration whose
matrix was still incomplete would have refused populations nobody had ruled on yet. **It does not
check** a declaration carrying no `CELLS` block at all — the same boundary `DEAD CELL REPORT` draws
above, and for the same reason: that is the inert state every adopter passes through, and refusing
it would red every tree that installed this kit before cells existed. Declare your FIRST cell and
the matrix becomes yours to complete; from there an undeclared population reds and is named.
**It does not check** the `file` and `constant`
surfaces. Their populations are computed by a declared cell's own selector, so an undeclared one of
those has no population to be non-empty and this arm cannot see it — the run says so on the line
below the list, every time. A reader who takes that list for the whole undeclared population is
reading a scope as a coverage claim.

## ...and the refusal that is not a predicate

Every `--check` and `--measure` run also asserts that the kit is SELF-CONTAINED: every non-relative
import in a `.py` file beside `lexicon.py` names either a stdlib top-level module or another `.py`
file in that same directory. It is not declared, not waivable and not pinned, because it is a
property of the KIT rather than of your corpus — an install that imports a neighbour kit stops
working the moment somebody takes this one on its own, which is why `subtokens.py` is a PORT of a
`codebase-map` function rather than an import of it.

There was a third DECLARED predicate, `P3 layer`, reading a `LAYERS` block of forbidden import
directions. `TOOL-aSurfacedLexicon-2` deleted it: 164 engine lines and 29 self-test arms, four review
rounds of blockers in its glob matcher and its import resolver, to enforce one declared rule whose
offender pin never left `"0"`. The refusal above is what it was really holding, and it is stronger —
it refuses ANY foreign module, not one named directory — while resolving nothing and globbing
nothing. A `LAYERS` block in an existing `.lexicon.conf` is now an unknown block key and the reader
REFUSES it by name; delete the block and the `LAYER_OFFENDER_PIN` scalar beside it.

The refusal carries its own liveness assertion: a walk that judges ZERO imports reds as `DEAD PROBE`
rather than reporting a clean zero, because zero offenders over an empty population is exactly what a
broken probe prints. Every run prints the population it judged for the same reason.

## Coverage modes — the law this obeys

`map_extractors.py` refuses to ship a regex extractor for shell and declares that language dark
instead, because a regex over shell definitions would look like coverage while silently skipping
what it forgot. Every extension present in the corpus therefore carries a DECLARED mode, and an
undeclared one is a named refusal.

| Mode | Extractor | Standing |
|---|---|---|
| `parser` | a real parse | complete over its extension |
| `probe` | whatever the pattern-set id names | incomplete BY CONSTRUCTION, reported as such every run |
| `dark` | none, declared explicitly | named every run, never silently absent |

**The mode token carries the STANDING and the pattern-set id selects the READER.** That middle row
used to read "a regex pattern set", and it stopped being true when `TOOL-aGradedDialect-3` §8 F1
widened the dispatch: a tokenizer-shaped reader that honestly MISSED its conformance floor now has
somewhere to run, under the mode that promises incompleteness rather than under the one that
promises a complete parse. `resolve_extractor` in `lexicon.py` is the one place that question is
answered, for all four sites that ask it. So a `probe` guarantees you the incompleteness and the
per-run report, never a particular implementation.

Which reader runs is the `LANGS` row's pattern-set id and never a second mode token: `python-ast` is
`ast`, `shell-tokens` is the tokenizer below, and `PARSERS` in `lexicon.py` is the whole list. **No
count of them is written here** — this paragraph opened with one for two releases and the dict grew
underneath it, which is a figure typed beside the population that owns it. A `parser` row naming an
id that is in neither catalog is a refusal, not a
fallthrough to Python. A new mode TOKEN was the other shape available and it is refused:
`drift-audit` ranks `parser` above `probe` above `dark` and reads an unknown mode as ABSENT, so
a language moving from `dark` to a freshly named mode would score as a weakening and fire a
ratchet finding on a strengthening edit.

### `shell-tokens` — what it reads, and the three things it refuses

A tokenizer rather than a regex, and the reason is measured rather than argued. Over the 94
tracked `.sh` files in this repo the naive same-line pattern reads 608 definitions, and a
heredoc-aware refinement of the SAME pattern reads substantially fewer — two regex readings of one
population, each wrong where the other is not. Only the naive count is quoted, because an earlier
revision of this page and the engine header each carried a figure for the REFINEMENT and the two
disagreed — one fact, two carriers, no gate between them. The reason both used to give for the
omission, that the refinement was never committed, is false: it ships as a runnable snippet in the
unit-14 spec under `memory/builds/aSurfacedLexicon/spec/`, landed in this same build, and either
figure re-derives from it. Corrected at the closing review (M5).

The refinement loses real definitions to a `grep` for a merge conflict marker, whose run of `<` it
takes for a heredoc opener; the naive pattern gains a JavaScript `function f() { … }` sitting inside
a `<<'EOF'` body. A number a second regex moves by half is not a population.

It tracks single quotes, double quotes as a STATE, `$'…'`, backslash escapes and line
continuations, `#` comments at a word boundary, `${…}` and `$((…))`, backticks, command
substitution as suspended-string-state code with its own nesting, heredocs with quoted and
unquoted delimiters in both the plain and `<<-` forms, and here-strings. It recognises four
definition forms: `name() { … }`, `function name { … }`, `function name() { … }` and the
subshell body `name() ( … )`, with the body free to open on a later line.

It REFUSES three things, and the header of `parse_shell_defs` is where they are enumerated
because two of them have no runtime behaviour to observe. A file it cannot tokenize RAISES
naming the construct and the line — never a partial list, and never an empty one, because an
unreadable file under an armed declaration is a broken corpus. A definition built by `eval` or
arriving by `source` is NOT found: there is no definition site to grade. A definition inside a
heredoc BODY is not a definition. It returns empty lists for types and imports, which shell has
neither of in any sense this kit grades.

It is not an interpreter and is not a step toward one: it tokenizes and locates, and never
evaluates, expands or runs what it reads.

`dark` is the honest cheap declaration, not a cop-out: most extensions in a tree carry no
definitions at all, and declaring them dark is what makes the undeclared-extension refusal
meaningful rather than noisy.

### Arming a language this kit does not ship

`PATTERN_SETS` holds the shipped regex sets and `js-regex` is the only one in it. **TypeScript is no
longer on the list of languages this reaches for**: `.ts` and `.tsx` ship as declared extensions with
their own readers, and what they read and refuse is `parse_ts_defs`'s header and `LEXICON.md`'s
`.ts`/`.tsx` section. A Go, Rust or C# adopter is still where a TypeScript one used to be — the whole
vocabulary-and-convention apparatus grades nothing for them until something is declared, and the
alternative is editing `PATTERN_SETS` inside `lexicon.py`, which is an `engine`-role file the next
`apply` overwrites.

Declare the extractor instead. A `PATTERNS:` block holds one row per
`<pattern-set-id>.<functions|types|imports>`, and the rest of the row is one Python regex, taken
verbatim to end of line and compiled with `re.M` exactly as the shipped sets are:

    LANGS="... go:go-regex:probe"

    PATTERNS:
      go-regex.functions  ^\s*func\s+(?:\([^)]*\)\s*)?([A-Za-z_]\w*)
      go-regex.types      ^\s*type\s+([A-Za-z_]\w*)

EXACTLY ONE CAPTURING GROUP per row, and it captures the NAME. Zero groups, two groups, a regex that
does not compile, or a repeated row key is a refusal naming the file and the line — never a dropped
row. The kit reads group 1 and nothing else, so a zero-group row would raise mid-walk with no line
number and a two-group row would confidently grade the wrong half of every name it matched.

Rows merge over the shipped sets PER KEY. A `js-regex.types` row replaces that one list and leaves
`functions` and `imports` standing, which is what lets an adopter FIX a shipped regex without
disarming the rest of the set; a row naming an unshipped id builds a new set whose unnamed parts are
empty. Nothing mutates the shipped constant, and every run prints which shipped keys a declaration
replaced, so a set weakened rather than emptied is read rather than inferred.

THE BOUNDARY. This buys grading, never a lexer. **The kit does not decline to run an adopter's own
extractor** — a declared set is compiled and walked exactly as a shipped one is, by the same corpus
walk, the same coverage fraction and the same measured pins. What a declaration cannot hand itself is
the `parser` standing: that is EARNED by a reader scored against a conformance corpus, never granted
by writing the token. A declared set is a `probe` on exactly the terms the
table above states — incomplete by construction, reported as such every run — and the law at the top
of this section still binds: if a regex over a language would look like coverage while silently
skipping what it forgot, `dark` is the honest declaration. Two vacuity arms watch a declared set: an
extension whose declared extractor finds nothing across a corpus that CONTAINS it is `DEAD PROBE`,
and an extension declared in `LANGS` that the corpus carries no file of at all is reported
`INERT DECLARATION` — a different state, reported differently, because a declaration arming a
language the repo does not have was previously skipped in silence.

## What every run reports, and what a zero there means

Every run prints one line per predicate — `graded`, `offenders`, `waived` — on GREEN as well as on
red, because a green line carrying a file count and no population cannot be told apart from a run
that found nothing to look at.

`graded` is per (extension, PREDICATE), never per extension. Those were summed once, and the fold hid
a real state: an extension can be armed, report a healthy total, and have one of its predicates
grading ZERO. A pair in that state is NAMED every run and does **not** red:

```
lexicon: armed but grading nothing, UNDECLARED as a cell (reported, not a refusal;
a DECLARED cell at zero is a DEAD CELL refusal above): .js suffix=0, .sh suffix=0
```

**That is a report on purpose, and the reason is the difference between two things a single tree
cannot separate.** A language with no classes in THIS repo is not an extractor that has gone inert —
it is a repo that does not write classes, which is ordinary and permanent. Redding it would leave no
discharge but declaring the whole extension dark, which buys a green bar by deleting real coverage.
The inert case is owned by the frozen sentinels below, which CAN tell the two apart. What this line
buys is that the zero is visible rather than folded away.

Every run also prints the COVERAGE FRACTION — the armed share of the tracked files that carry a
definition at all:

```
lexicon: coverage — armed 140 of 141 definition-carrying file(s) (99.3%)
```

**What it does NOT measure is extraction QUALITY.** It answers "is this file's language graded by
anything", not "is it graded well". A `probe` extension counts as armed on exactly the same terms as
a `parser` one, while the modes table above says a probe is incomplete by construction — so a repo
can raise this number by declaring a regex set and grade no better than before. The fraction exists
to make one specific move visible: flipping an armed extension to `dark` is a one-string edit that
empties a graded population, and before this line nothing in the output moved when it happened.

The denominator comes from a deliberately BROAD, deliberately INCOMPLETE sniffer that reads every
tracked file regardless of its declaration — it has to, since a denominator built from the armed
extractors would be the numerator. It answers one boolean per file and feeds one printed line; no
predicate reads it. Prose and data formats are excluded, because a fenced code block in a tutorial is
an example rather than a definition, and counting those made a number that moved when somebody wrote
documentation.

## Vacuity is armed on BOTH sides

A predicate that selects an empty population passes green forever and tells you nothing. The
corpus-side arm is `DEAD PROBE`: a `parser` or `probe` language whose definition population is empty,
against a corpus that contains that extension, is a refusal. That arm is itself defeated by an empty
corpus, so the kit-side arm is a frozen SENTINEL fixture per shipped pattern set in `selftest.py` —
a pattern set that goes inert fails there.

## Supply — how the table reaches whoever is writing the name

The declaration is the half of this kit with a measured record, and the measurement is NOT written
here: `python tools/drift-audit/drift_report.py` derives `lexicon_marginal_offense_rate` live, over
the window from the declaration's adoption commit to HEAD, splitting fresh files from pre-existing
ones. A figure typed into this paragraph was wrong within a week of being written and nothing caught
it, which is the rule this repo breaks most often — a value stated in prose beside the source that
owns it rots between changes. Read it from the signal.

```bash
python tools/lexicon/lexicon.py --suggest <identifier> --as <ext>.<surface>   # one line, no corpus pass
bash tools/lexicon/adopt-lexicon.sh --render             # re-render the Skill after a declaration edit
```

`--suggest` answers from the declaration FIRST and the shipped canon second, in that fixed
precedence, and from no corpus at all. Off-table, it names the REPLACEMENT and quotes the negative
that bans what you tried — `use load_remote — the declaration says load, NOT fetch: read a store
into memory` — which is why the NOT clauses are the product rather than decoration. Where no row
bans the token by name the canon answers instead, and the line says which source spoke.

**`--as` is REQUIRED and takes a full `<ext>.<surface>` cell** (`TOOL-aSurfacedLexicon-8`). The
surface is the whole question: it decides which predicates are armed on the name and which convention
the answer is spelled in. A surface-blind suggestion is how this verb answered `loadUserData` for a
cell declaring snake — a name its own gate reds — so the flag is not defaulted, because a default
answers the surface question silently for a caller who did not think about it.

At most three checks run, in this order: the banned TAIL on the surface P2 grades, the leading
TOKEN on the surface P1 grades, and the CONVENTION always. The re-casing is applied to whatever name
the earlier checks produced, so the printed name is legal under every armed predicate of that cell at
once. On a `file` cell the argument is a BASENAME OR A PATH and the graded string is `read_stem`'s —
the basename up to its FIRST dot, the grader's own seam rather than a second stemming rule — and the
stemming happens BEFORE the selector routing, so a routed cell claims the same name here that it
claims at the gate.

**Which predicates are armed is a property of the SURFACE, never of a per-cell flag.** P1 grades
every extracted function and P2 every extracted type, whatever any `CELLS` row says, so this verb
reads `PREDICATE_SURFACES` and not the row. It used to gate both checks on `vocab` and `notail`, and
a declaration arming neither — this repo's, and every scaffolded one — got `OK` here for names the
merge bar reds on (closing review B2). `vocab` survives as what it always graded: the per-cell
DEBT/UNRULED ratchet. `notail` had no reader but that defect and is gone from the grammar.

Four refusals are distinct and separately worded, because a caller who typed a cell that does not
exist, a `dark` cell, a key that is not a cell, and a BARE SURFACE have four different problems. The
bare-surface refusal is a MENU: it lists the declared cells carrying that surface. A cell whose row
carries a `prefix` selector is routed FROM THE NAME, the way the grader routes it; a `decorator`
selector cannot be resolved from an identifier at all, so such a cell answers in the parent's
convention and SAYS SO rather than answering confidently.

The re-caser is SPAN-ANCHORED and it REFUSES rather than inventing. It builds from
`_SUBTOKEN_RE.finditer` spans and regenerates exactly two things — the separator the convention
supplies, and the case of a span's first character where the convention demands a different one. A
name carrying a character outside a span that the target convention does not itself re-supply (`$`,
an accented letter) is NOT re-spelled; the verb prints its finding and says why. Separators ARE
re-supplied, which is why `fetch_remote --as js.function` comes back as `loadRemote` and not as a
refusal. Rebuilding a tail from `subtokens()` instead returns `getUserURLs` as `readUserUrLs`, a name
with zero unseen characters, so the loss there is CASE and no unseen-character rule would catch it.

**It is not a gate, structurally.** It cannot exit 1, it prints no pin, and nothing in
`scaffold_lexicon.py` imports it — so what the corpus DOES has no code path to becoming what it
SHOULD do. A promise would not survive a refactor; the absence of a return path does.

`TOOL-aSurfacedLexicon-3` deleted two further modes: a per-FILE reading, which reported how the
corpus already spelled one file's objects, and a pre-adoption report over the shipped canon. Nothing
in this kit restores a per-FILE reading. The per-NAME half is back:
`TOOL-aSurfacedLexicon-7` wired `--suggest` to the canon, which is the DEBT half below. The
pre-adoption reading survives, further down.

### DEBT and UNRULED — the two halves of a P1 offender

A P1 offender is a definition whose leading token the declaration does not carry, and until
`TOOL-aSurfacedLexicon-7` that was the whole message. A gate that says no and nothing else gets
waived rather than obeyed, so the offender is now CLASSIFIED against the shipped canon:

| Class | The test | What the line says |
|---|---|---|
| DEBT | the token is a key of `canon.build_form_index()` | the replacement identifier, its representative, and that verb's gloss |
| UNRULED | it is not | that no cluster holds it, plus how many definitions corpus-wide lead with it |

The distinction is the product. DEBT is a rename the kit can hand you. UNRULED is a scoping question
no vocabulary can answer: the token either names a responsibility the table should carry, or the
function does more than one thing. The site count is what tells those apart — a token with one site
is a name to fix, one with eighteen is a house idiom that joins the table or gets renamed everywhere.

**`--suggest` reads the two sources in a fixed precedence.** The declaration's own inverted `NOT`
clauses win, because the owner wrote that negative and the canon did not; only where no row bans the
token by name is the canon asked. Where the canon's representative is not itself a declared `VERBS`
row it is still proposed, and the line says the row is owed — suppressing the advice would leave the
author with a refusal and nothing else, which is the defect this path exists to close.

**A `vocab` flag on a `CELLS` row splits that cell's ratchet in two**, `<cell>.debt` and
`<cell>.unruled`, both two-sided equalities like every other pin. `--measure` emits the pair for
every armed `vocab` cell, blank-separated because `PINS` refuses two adjacent rows, and a cell with
no `CELLS` row gets no pin row at all. The scalar `VERB_OFFENDER_PIN` keeps grading the whole
population beside them: it is a single bucket over two populations, so a rename moving a definition
from DEBT to UNRULED inside one cell holds the total and greens there while both cell rows red.

### The canon door — a `CANON:` overlay, and the stamp that records it

The canon ships FROZEN, and freezing it is what stops a proposed table becoming a mirror of the code
it grades. But welded is not frozen: `canon.py` is `role = "engine"`, so an adopter who disagrees
with a cluster cannot edit it and cannot durably re-role it either. The door is a block in the
declaration, which is the file the owner already curates.

| Row | Direction |
|---|---|
| `load  hydrate rehydrate` | the representative is shipped — REPLACES that cluster's alternatives |
| `frobnicate  frob fnord` | the representative is new — ADDS a cluster |
| `-measure` | a leading minus — DELETES a shipped cluster, and takes no alternatives |

`canon.build_clusters` merges the block over the shipped tuple and refuses four things: a minus row
naming no shipped cluster, a minus row carrying alternatives, any row carrying no alternative, and a
merge that would leave one form in two clusters. A minus row naming nothing is a refusal rather than
a no-op on purpose — a typo that quietly changed nothing would still count as an owner declaration
on the posture line, which is a posture that lies in the one place this door exists to make honest.

**The unfreeze is stamped or it is refused.** A `CANON:` block with an empty `canon_unfrozen`, or one
carrying a date and a node but no REASON, reds `bash {kit}/adopt-lexicon.sh --check` — a leg
with no guard, so a conf-only commit reaches it. **And it prints on every run**, green as well as
red, above the counts and above a `--suggest` answer. There is no state in which the canon is
quietly overridden.

**The honest limit.** No machine check can tell a considered overlay from a mirror. An owner may
unfreeze the canon and fill the block from their corpus's commonest spellings, reinstating precisely
the defect `canon.py` closes, and the difference is why the rows were chosen — which the tool cannot
see. What the door buys is visibility and attribution, not proof: the choice is one tracked line, it
is attributed to a node and a date, it is refused without a reason, and it is printed on every run.
The blast radius is bounded by the canon grading nothing — it decides what may be PROPOSED and how
an offender is labelled — so an unfrozen canon cannot legalise a name by itself. Only a `VERBS` row
a human wrote does that.

A second limit, smaller and concrete: an ADDED cluster has no GLOSS. A `CANON:` row declares a
cluster and a gloss is a `VERBS` row's job, so the advice half prints the negative alone until the
owner writes the matching row.

One consequence worth meeting on purpose rather than as a surprise: both P1 pins are two-sided
equalities and an overlay moves definitions between the DEBT and UNRULED buckets, so the first run
after declaring one reds until those rows are re-pasted. The run says so, naming the overlay as the
cause rather than leaving a bare mismatch to be read as a fault in the ratchet.

`scaffold_lexicon.py` may never emit a `CANON:` block header, and that is asserted on the
`lexicon naming predicates` leg rather than promised here. The scaffold derives from the corpus; an
overlay it proposed would be the mirror arriving through the one door built for a human.

### Reading a repo BEFORE you adopt

The scaffold takes the DESTINATION path as its argument and derives the repo it reads from
`git rev-parse` independently, so pointing it outside the tree gives you the whole reading —
languages, all measured pins, the proposed verb table and the rename debt adopting it would owe —
and writes nothing into the repo itself:

```bash
python tools/lexicon/scaffold_lexicon.py /tmp/proposed.lexicon.conf
```

Read `/tmp/proposed.lexicon.conf`, decide, and only then scaffold into the repo for real.

### The rendered Skill

`SKILL.template.md` renders into `.claude/skills/lexicon/SKILL.md`, carrying the whole table so an
agent has it without opening the conf. It is a GENERATED second carrier and its gate re-renders and
byte-compares, so a declaration edit nobody re-rendered REDS with `DRIFTED`. The leg
(`lexicon wiring`) carries NO guard — its answer changes when the declaration moves, and a
kit-directory guard would leave exactly that edit unchecked.

### Which leg grades the declaration

`lexicon wiring` does, and that is a correction rather than a description. `lexicon naming
predicates` runs the engine over the corpus, but it is guarded on `tools/` and three sibling
directories while `.lexicon.conf` sits at the repo ROOT — so a branch whose entire diff was the
declaration skipped the only leg that would have graded it. Raising `VERB_OFFENDER_PIN`, flipping a
cell to `dark`, or deleting a `PINS` row together with its cell all landed with no verdict computed,
and the gate's own red text tells an author to produce exactly that commit shape.

The guard could not simply be widened. `govkit` partitions every declared guard into classes —
memory-root-relative, verbatim-repo-root, renamed, exempt, kit-relative — and a root-level conf falls
into none of them, so declaring one reds `govkit selfcheck` instead of scoping anything; that ruling
is written into this kit's `kit.toml` and was struck twice during the build. What was left was
`adopt-lexicon.sh --check`, which is the argv of the leg with the empty guard and already reads the
declaration on every bar. It now runs `lexicon.py` too and fails on a non-zero grade. The guarded leg
stays as the fast fail on a `tools/` diff. Closing review B1.

## Waivers

The waiver registries beside this file are keyed on the matched **TEXT** rather than on
`<path>:<line>`. Keying
on position means any edit ABOVE a waived line unpins it, which reds a merge that touched nothing
the waiver guards — that was hit on `install-prefix-waivers.txt`'s first real merge. A waiver whose
text is gone reds as STALE, so a registry cannot quietly outlive what it excuses. Shrink-only.

## Adopting

```bash
bash tools/lexicon/adopt-lexicon.sh --scaffold   # derive a PROPOSED table + measure the pins
bash tools/lexicon/adopt-lexicon.sh --check      # the drift mode
python tools/lexicon/lexicon.py                  # the gate
python tools/lexicon/lexicon.py --list           # every offender, waived or not (authoring aid)
```

`--scaffold` asks your corpus ONE question per concept — does any spelling of this have a live
definition site — and seeds the concepts that answer yes. It takes the SPELLING from the kit's own
frozen canon, never from your code, so the corpus cannot promote a habit it already has and cannot
nominate a verb the canon does not hold. Two questions, two deciders: which concepts, and what each
is called.

The seed is still marked `PROPOSED` and **wants curating before you ratify** — the canon's negatives
are generic, your domain rows are missing, and a starting vocabulary is not a curated one. `--check`
reds while `ratified` is empty, so an uncurated seed cannot reach the merge bar disguised as a
vocabulary.

`--scaffold` also seeds the `CELLS` matrix — one row per `(language, surface)` pair the walk
actually extracted — and the `.conv` pin each armed row measures to. The CONVENTIONS there are
prescriptive, taken from each language's own published style and never from a ranking of what your
corpus already does; a pair the kit has no prescription for is seeded `dark`, which is a declared
refusal to grade rather than a gap. Arming one is a one-word edit and `--measure` reprints the pins
it moves. Before the closing review the seed emitted no matrix at all, so a fresh adopter's first
`--suggest` — the one command the Skill it had just installed documents — exited 2 with
"Declared cells: none" (B3).

Pins are MEASURED against the adopting corpus at scaffold and are never inherited: a pin copied from
a larger tree is either vacuous or permanently red.

### Expanding — the second and last supported transition

`--scaffold` refuses once a declaration exists, so an adopter who later needs a concept the seed
missed had no tool-supported route at all: they edited the table by hand with nothing bounding what
they added. `--expand` is that route, and the bound is the same one the seed had.

```bash
bash {kit}/adopt-lexicon.sh --expand           # propose; writes NOTHING
bash {kit}/adopt-lexicon.sh --expand --stamp   # record the widening, once
```

It proposes cluster representatives with a live site in your corpus that your table does not yet
declare — and nothing else. A leading token no cluster holds cannot enter a proposal by any path,
which is why the run also prints an UNRULED TAIL below the proposals under a header saying, in
words, that those are not candidates and never will be. That tail is the interesting half on most
trees: it is what your corpus would have nominated if frequency were allowed to decide, and the
whole design is that it is not. Read it as a work list — a token near the top is a house idiom that
either earns a hand-written row with a hand-written negative, or gets renamed everywhere.

Nothing is written to the `VERBS:` block. You paste the rows you mean, and you sharpen each
negative first, because the reader reds a row that carries none — a hand-pasted row is born failing
the gate until a human writes the thing that makes it a definition rather than a synonym.

Every row you paste moves a pin. `--measure` prints the ones this declaration produces.

`--expand --stamp` records the widening as a single `expanded="<date> <sha>"` scalar and refuses a
second run afterwards. It refuses to stamp a dirty tree, because the sha's whole job is to name the
tree the proposal was measured against and a worktree with uncommitted TRACKED changes has no such
sha. Untracked files are deliberately not dirt here: this kit's own fixtures copy it in untracked,
so a refusal built on `git status --porcelain` could never be exercised at all.

Once is the design, and the honest bound on it is written into the refusal: clearing that line
re-opens the transition and nothing running under your own uid can stop you. What the stamp buys is
a visible edit in a tracked file, never a lock.

## Uninstalling — the ORDER matters

Once the verb table is declared as a `codebase-map` inventory, "removing an optional kit must not red
a different optional kit's gate" is not achievable as a property, only as a PROCEDURE. Every
degradation route reds the map leg on its own: an extractor returning `[]` makes every dossier claim
stale, removing the `EXTRACTORS` entry makes the dossier claim an id outside `inventory_ids()` and
`map_lib` raises, and the generated artifacts move either way. So the order is the mechanism:

1. **Remove the dossier's `lexicon-verbs` claims** — `memory/map/features/lexicon.md`, the
   `gate-legs`/`kits` block. Claims first, or the next step orphans them.
2. **Remove the `lexicon-verbs` entry** from `map_extractors.py:EXTRACTORS`.
3. **Re-render** `memory/map/generated/` (`python tools/codebase-map/gen_map.py --write`).
4. **Delete `.lexicon.conf`** and drop the kit's legs from the gate manifest.

Between steps 2 and 4 the engine reports `NOT ADOPTED` and exits 0, and the two `drift-audit` signals
report NOT ASKED rather than a clean zero.

**The mid-teardown safety arm.** `bash tools/lexicon/adopt-lexicon.sh --check` NAMES an orphaned
`lexicon-verbs` extractor — a conf deleted while the extractor remains, i.e. step 4 done before
step 2. That is the state a hurried uninstall actually lands in, and it is the one the map gate
reports least legibly.

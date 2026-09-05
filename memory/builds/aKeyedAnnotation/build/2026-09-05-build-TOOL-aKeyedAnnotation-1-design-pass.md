**Serves:** research TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4
**Commissions:** TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4

# Should code annotations be governed, keyed and read by the orientation tooling? — the adversarial answer

Design pass for `aKeyedAnnotation`, node a, 2026-09-05. Five primed lenses over the tree, 36
findings, judged. Every number below is either reproduced in this record's own census script or
carries the command that produced it; none is authored twice.

Run the census before reading any figure as current:

```bash
python memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py
```

## The verdict in four sentences

The premise that "nothing scans the annotations" is false: `tools/drift-audit/drift_report.py`
already reads a bare unit id out of product source and treats it as evidence that a unit shipped,
and `tools/memory-tree/gotchas.py` already links a source path to its bug classes from anchors
DERIVED out of the memory records, so two of the three orientation kits are wired to code
annotations today and need no grammar to be. The third, `tools/codebase-map/`, forecloses it: its
identifier tokenizer splits on the hyphen and strips comments deliberately, so an id cannot survive
as a token there in any language, and the sibling build `aWeighedCompass` measured that kit's
retrieval half at zero added recall for more bytes — feeding annotation prose into it is a
regression nothing grades. Worse than useless, MANDATING annotation actively destroys the one
working consumer, and this was observed rather than argued: appending a single SPECCED spec's id to
one tracked source file drives `non_terminal_specs_cited_by_product_source` from `ok` to
`OVER PIN — gateable`, because that oracle's whole discriminating power is that annotation is today
sparse and LATE. So the honest answer is that this repo does not have an annotation problem needing
a program; it has a boundary problem worth a page of prose, four small corrections to consumers
that already exist, and a firm refusal to build the obvious thing.

## 1. Q1 — does integration make sense at all?

**Mostly no, and the parts that already work must be protected from the parts that sound
appealing.**

**The blocking finding, reproduced on this tree.** `signal_spec_status` at `drift_report.py:466`
runs `git grep -l -w -F <the spec's own id> -- PRODUCT_GLOBS` and reads a hit as "this unit
demonstrably shipped". `PRODUCT_GLOBS` (`drift_signals.py:20`) is `tools skills .claude …` — every
file an annotation would live in. Staged break, run in this worktree and reverted:

```
baseline    non_terminal_specs_cited_by_product_source   2  45  ok (pin 2, drain it)
+ one line  non_terminal_specs_cited_by_product_source   3  45  OVER PIN 2 — gateable
reverted    non_terminal_specs_cited_by_product_source   2  45  ok (pin 2, drain it)
```

The line appended was a comment carrying one SPECCED spec's own id and nothing else. The lens that
found this also measured why it happens: citation correlates with terminal status, and the SPECCED
column is empty. Mandate annotation at write time and that column fills, the signal saturates, and
the only available remedy is raising a pin that `drift-audit`'s own ratchet list is built to flag as
a weakening. **A convention that requires an id in a comment when the work is written would trade
the repo's one working "did this actually ship" instrument for a decoration.**

**The second consumer needs nothing either.** `gotchas.py` derives a record's anchors from the
backticked path tokens in the record's own body (`ANCHOR_RE`, `gotchas.py:49`) and resolves them by
substring-both-ways plus basename equality (`selectable`, `:181`). `--for-paths
tools/unattended/lib-unattended.sh` returns five anchor-selected classes plus the universals; the
same command over `tools/codebase-map/map_lib.py` returns zero anchored classes, so the selector
discriminates rather than returning everything. The one hand-written `[[wiki-link]]` in all of
tracked source is already reachable from that file's path without existing, and the record the
mechanism selects (`two-guards-one-question-two-answers`) is a closer match to what that comment
describes than the record the human hand-linked. A source-side link grammar would be a second answer
to a question a shipped, derived, zero-maintenance mechanism already answers — which is the class
that comment itself names.

**The third consumer is structurally closed.** `_IDENT_TOKEN_RE` at `map_lib.py:631` is
`[A-Za-z_$][\w$]*`, so a unit id never survives as one token: in an undeclared suffix it fragments
into a generic `TOOL` token that would inflate fan-in for anything sharing that name, and in a
declared one the comment is stripped first, by design and with the rationale in the docstring.
Admitting hyphens re-baselines every fan-in figure the map reports. And `TOOL-aLexedStripper-7` is
open against the OTHER stripper in that file, which over-strips and feeds the committed
`symbols.json` — a prerequisite for any work in there, not a fold.

**What survives the attack.** One narrow thing, and it is not a grammar: the grep at
`drift_report.py:466` can only resolve ids a human already wrote, so nothing today notices when a
written id resolves to nothing.

The discriminator that makes this cheap was proposed by one lens and verified here, and it is better
than the lens claimed. Take every id cited by tracked source that no record defines, and keep only
those whose SLUG anchors at least one record in the corpus. At this base that turns sixty
unresolvable citations into **two findings and fifty-eight filtered fixtures, with zero waiver rows**
— because a fixture slug (`tOne`, `aFoo`, `zFix`) anchors nothing anywhere, while a real slug does. A
path-based split cannot reach that: this repo puts selftest arms inside product modules, so the
fixture ids are not confined to test files.

The two survivors are the same build — the unattended kit's `dUnstalledConvoy` — and they are worse
than a typo. Its records run 1 to 19 and resume at 23, so **its seq 20, 21 and 22 were minted, two of
them cited from code (in `tools/unattended/lib-unattended.sh` and `tools/unattended/unattended.test.sh`),
and none of the three was ever recorded** — a closing review's findings that exist only as pointers.
Both citations describe reproduced defects, and following either gets you nothing. That is worth a
report-only signal, and it is still not worth a gate.

**This record deliberately does not spell those two ids, and the reason is a finding.** Writing them
here would make them CITED in the memory corpus, and the memory-side orphan check counts exactly
that: cited and never defined. Naming them moved that count off its floor of zero against a pin the
kit's own ratchet list treats as weakening upward, verified by doing it and reading
`python tools/memory-tree/corpus_ids.py --report`. So **the memory tree cannot document a dangling id
without either defining it or waiving it** — a catch-22 that falls out of the design and that nothing
records. The escape used here is the repo's own preference: derive rather than author. The build and
the seq range are named in prose, which no grammar matches, and the census script names the ids at
runtime. Unit 3's signal has the same property by construction, because it derives its findings and
commits none of them.

## 2. Q2 — what should an annotation say?

The lens that graded the corpus found the load-bearing asymmetry, and it changes the design: **the
id and the evidence are two largely disjoint practices here, not one.** Over substantial comment
blocks under `tools/`, roughly one in twenty carries both an id and a measurement verb; the two
single-bearing populations are each several times larger, and the id-only half is the half whose
content is nearest zero. Both real dangling pointers sit in exactly that shape — a bare
trailing parenthetical appended to a sentence that has already stated the incident, and which reads
perfectly with the id deleted.

**So the evidence is the required part and the id is the optional pointer, not the reverse.**

### The MUST / MAY / MUST NOT list

**MUST carry** the counterfactual: what was tried, or what the obvious reading would do, and what it
actually did. An annotation that only restates the code is the code again.

**MAY carry:**
- the producing unit's id, as a trailing pointer;
- a `WHAT THIS DOES NOT CHECK` clause naming the file that owns each adjacent question;
- a `ponytail:` ceiling and its upgrade path;
- a number, under exactly one of three dispositions below.

**MUST NOT carry:**
- a present-tense count of a live derived population;
- a value another file declares;
- a restatement of the class its memory record owns;
- a second spelling of a rule already spelled in the same file;
- an assertion with no observation behind it.

### The three dispositions of a number in a comment

This resolves the apparent conflict between the charter's ban on derived counts in prose and the
several hundred measurement-bearing comment blocks that are the best writing in the tree. A number
is safe in a comment when it is:

- **FROZEN** by its conditions — the population, sha or node+date is named beside it, so the figure
  describes an experiment and cannot go stale. `tools/memory-recall/bench.py` and
  `tools/drift-audit/drift_signals.py` both do this well.
- **GATED** by a pin — the number is a declared value a checker compares, not prose.
- **POINTED** at its owner — the reasoning stays, the digits go to the file that declares them.

The counter-example found in the sweep is a present-tense count of a live derived population written
with no sha and no conditions; it is wrong the day that population changes and nothing notices.

### The one-line test

**Delete the id, and the block must still be worth reading.** Every strong block in the tree passes
it; the one dangling citation fails it, which is why nobody noticed the dangle for the id's whole
life.

### Two rewrites, from real lines

`tools/unattended/lib-unattended.sh:12` —

> BEFORE: a sentence ending `A closing review reproduced that with two controls`, followed by a
> bare id in parentheses and nothing else. (The id is paraphrased rather than quoted, for the reason
> §1 gives: quoting it would cite it.)
>
> AFTER: name the two controls in the comment — a pass whose only commit was its own declaration
> read closed to the driver and open to the leg, and one product commit made both read closed — and
> keep the id as a trailing pointer. The evidence then survives the id, whatever happens to it.

`tools/check-template-size.sh:86` —

> BEFORE: the sentence spells the kickoff engine's byte cap inline while
> `tools/template-size-limits.txt` declares it as a row.
>
> AFTER: drop the digits, keep the reasoning about the positional beating the environment. The
> comment two lines up already routes to the owning file.

## 3. Q3 — what is it keyed on?

**The full unit id — family, slug and seq — written once, with the coarse build key DERIVED from it
by capture group. Not a new tag, not a second regex, not a pair of written keys.**

The repo already ships exactly one id grammar (`ID` / `ID_RE` in `tools/memory-recall/extract.py`),
consumed by `corpus_ids.py` through `grammar(root)` and mirrored by drift's `_OWN_ID`. Every tracked
spec under the builds tree carries an H1 the grammar matches; none is unkeyed. So the assembly
question Q3 asks is already answered, and the answer costs zero new bytes of grammar: one pass with
that regex over every tracked file assembles memory and code into one index in a couple of seconds,
and a single-id lookup in either direction is about a tenth of a second by `git grep`.

**Reconciliation with the recorded slug rejection.** `drift_report.py:432` and
`tools/drift-audit/README.md:163` record that keying the spec signal on the slug over-flagged 107 of
126, because every id of a build shares the slug and one shipped unit made all fourteen siblings look
stale. That verdict stands and this design does not disturb it, because the pair already exists as a
projection rather than as two tokens: `drift_report.py:711` splits the matched id into group 1 (the
unit, for unit-level questions) and group 2 (the slug, for build-level ones), with the comment
stating why no second written token is needed. **The slug is legal as a capture of a matched id and
illegal as a search term.** The keying lens measured that distinction from the annotation side: the
slugs cited by product source span far more defined ids than cited ones, reproducing the same
inflation shape from the other end.

**Every other candidate fails on a measurement, not on principle.**

| Candidate | Why it fails here |
|---|---|
| bare build slug | not a distinguishable lexeme in source — hundreds of legitimate non-id occurrences in prose, `FAMILY-slug` without a seq, and path segments, outnumbering genuine citations more than two to one |
| slug + seq, no family | not unique — dozens of defined pairs carry more than one family, because seq is 1-up per (session, family). Resolving an annotation by constructing a spec filename is ambiguous for one unit in twenty |
| file path | the only key that has actually moved: many renames under the builds tree, and even intact it resolves to a median of eleven memory documents. A hint, not a key |
| `[[wiki-link]]` | signal-to-noise of one against several hundred. The dominant false form is not TOML but the POSIX class `[[:space:]]` in shell and awk; a scanner would need a lexer to serve a population of one |
| a new `gov:` marker | see §5 — it solves three real rot paths and is still refused, because the thing it makes possible is the thing §1 says must not be built |

**Two latent divergences the key must not inherit.** Drift's `_OWN_ID` is hand-typed rather than
taken from the shipped grammar, and it cannot match the ratified correction-id form the shipped
grammar was widened to admit — today no spec H1 uses that form, so it costs nothing yet and will
cost silently later. And the recorded `-F`-without-`-w` prefix hazard still applies: a scanner
written with substring matching over-attributes roughly one product-cited id in eighteen, because
many ids are strict digit-prefixes of a sibling.

## 4. Q4 — which tools change, and what does each cost?

**Three of the four kits should not change at all.** `codebase-map` is out of scope (tokenizer
forecloses it, and its stripper has an open defect). `memory-recall` must not receive source files:
its declared-source chunker matches only a bare assignment, so a type-annotated Python declaration —
which is where this tree's load-bearing declarations live — is invisible to it; and the recall floor
pin names the `records` set, so growing the `chunks` half cannot move the gated number, which is the
could-not-fail shape the charter bans. `memory-tree`'s check 14 must not be widened: its orphan pin
sits at its floor with an empty waiver, and a path-scoped source population is wrong in whichever
direction it is set, because this repo puts selftest arms inside product modules.

**What does change is small, and every piece rides a seam that already exists.**

| Kit | Change | Cost |
|---|---|---|
| `drift-audit` | make the existing annotation reader correct: take `_OWN_ID` from the shipped grammar, exclude test globs from the shipped-evidence oracle, and stop the pin comment from citing the ids it counts | no new leg; the `drift-audit records` leg is unguarded and already on every bar |
| `drift-audit` | one report-only signal for a source-cited id that resolves to no record, keyed on slug-resolvability | ~ten lines beside the signal registry; no gate, no waiver |
| `codebase-map` | make the dossier `decisions` field live — print it in the reuse audit, pin the empty ones shrink-only | rides the coverage leg, which is unguarded and among the cheapest on the bar |
| prose | the annotation convention, written once, plus the deletions it prescribes | none |

**The `decisions` field is the finding that most changes the shape of the answer.** The code→decision
link this pass was asked to invent already exists in the codebase-map dossier schema: `parse_dossier`
requires the key and shape-checks every entry against the project id grammar. It is empty in most
dossiers, no consumer reads it, and an empty list passes validation — a vacuous selector, so nothing
has ever failed on it and nobody fills it. An orienting agent running the reuse audit gets a seam
with no "why", and the field that would carry the "why" is sitting there, validated and inert.
**That is the integration worth building, and it is not an annotation.**

## 5. What NOT to do, on this evidence

- **Do not mandate an annotation when work is written.** It breaks the spec-status oracle, observed.
- **Do not add a source-side orphan check to the memory hygiene gate.** Its pin is at its floor with
  an empty waiver; a path-scoped population needs dozens of waiver rows on day one, which is how a
  new gate arrives already disarmed. It also converts a records-only leg into one that reds on an
  ordinary source edit, and the guarded self-tests around that kit cost hundreds of seconds per
  touching commit. A gate whose steady state can be reddened by editing a comment gets bypassed.
- **Do not declare source files into the recall corpus.** The chunker cannot read them, the floor pin
  cannot see the damage, and the sibling measurement already puts that half of the ensemble at zero
  added recall.
- **Do not un-strip comments in `codebase-map`.** Precision there is already low; adding prose tokens
  to a fail-open ranking makes orientation worse and nothing grades it.
- **Do not invent a `[[…]]` or `gov:` annotation grammar.** The repo already has two ungoverned
  annotation grammars; a third is the two-answers class at the grammar level. The marker idea is the
  strongest rejected proposal in this pass and its own §6 entry records why it was rejected anyway.
- **Do not consolidate documents.** Not this pass's question, but the sibling build measured
  cross-carrier duplication as negligible and the "not restated here" discipline as working; this
  record follows it.

## 6. The strongest idea this pass refused, and why

One lens proposed a marked annotation in the existing `gov:` namespace rather than a bare id. It is
the best rejected idea here and deserves its record, because it genuinely fixes three rot paths at
once: the spec-status oracle could filter marked lines and keep its meaning, a source-side orphan
population becomes marked lines instead of a file glob that no path predicate gets right, and a
fixture id cannot accidentally join the population.

It is refused for three reasons, in order of weight. It is a **second id grammar** in a repo whose
own catalogue names that class. It buys correctness for a mandate that §1 says must not exist — with
annotation left voluntary, the oracle needs no filter and the orphan population is one row. And that
namespace has **no closed set**: ten kinds are in use with their own consumers and nothing grades the
vocabulary, so a misspelled marker is silence from every reader, which is what a passing check prints.
Closing that hole is worth doing on its own merits and is filed as a backlog row; it is not a
prerequisite for anything here, because nothing here adds an eleventh kind.

## 7. Ranked recommendations

| # | Change | Cost it removes | Shape | Risk |
|---|---|---|---|---|
| 1 | Repair the dangling source citations, rewriting each comment so its evidence survives the id | two pointers that have resolved to nothing for their whole life, and an unrecorded id triple behind them | two comments plus a backlog row | none |
| 2 | Write the annotation convention once — the MUST/MAY/MUST-NOT list, the three dispositions of a number, the delete-the-id test | every future annotation argued from scratch; the id-only shape that carries nothing | prose | it rots if it restates anything the charter owns |
| 3 | Take `_OWN_ID` from the shipped grammar and narrow the shipped-evidence oracle off test globs | one key with two answers, latent; a `.test.sh` citation certifying a spec as shipped | small kit change | moves a signal's population — re-measure the pin in the same commit |
| 4 | Make the dossier `decisions` field live: print it in the reuse audit, pin the empty ones shrink-only | a validated, inert field that already owns the code→decision link | kit change + one check, no new leg | the pin must be measured on this corpus, never copied |
| 5 | One report-only drift signal for a source-cited id resolving to no record, gated on slug-resolvability | the class that produced recommendation 1, unobserved | ~ten lines, report-only | none — it gates nothing |
| 6 | Delete the mechanism paragraphs that records absorbed verbatim from call-site comments | the same paragraph served twice into one context window | three deletions | none |
| 7 | Close the `gov:` marker vocabulary with one leg, observed RED on a typo | a misspelled marker reading as silence from every consumer | one leg | adjacent — backlog row, not a unit here |
| 8 | Report per-source chunk yield in the recall extractor; a present-but-zero-yield declaration is a refusal | a declared corpus member contributing nothing, silently — true of one declared source today | one counter | adjacent — backlog row, not a unit here |

Rows 1 through 6 become this build's four units. Rows 7 and 8 become backlog rows: both are real,
neither is on this build's path, and folding them in would widen a design pass into a kit sweep.

## 8. What this pass could not measure

- **Whether an annotation ever prevented a rebuild.** No record ties a session's orientation to a
  comment it read. The sibling build hit the same wall from the retrieval side and could establish
  existence, not rate; nothing here improves on that.
- **The adopter population.** Every measurement is against this repo, whose annotation density is
  plainly unusual. A convention that suits a tree where most substantial comment blocks carry real
  reasoning may be noise in a tree where they do not, and no adopter corpus was available.
- **Whether the id-only annotations are read at all.** That they carry little was measured; that
  nobody follows them was not. A reader who does follow one gets the record, which is the whole
  value being argued about.
- **The verify stage did not complete.** Five lenses returned; the adversarial batch judged eight of
  the thirty-six findings before the session limit ended the run, and the synthesis agent never ran.
  The remaining findings were judged by hand against the tree, with the headline observation
  re-reproduced independently. Eight findings carry a skeptic's verdict; the rest carry mine.

**Serves:** journal TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

# Spec brief — aGradedDialect, all five units

ONE file for the whole roster on purpose. M2 requires the sub-specs to AGREE on scope, interface,
ordering and acceptance, and an author who has read only their own unit cannot check three of those
four. Read the section for your unit, and read the others well enough to know where your edges are.

## What is already decided, and may not be re-litigated

`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`
is the research record. It resolved the mechanism fork against measurement, and its §5 pick is
settled: **a tokenizer-plus-locator inside the kit, the `shell-tokens` design ported to TypeScript.**
Three candidates lost, each to a test written down before it ran. Do not reopen that fork; cite it.

The figures every spec will want, all measured 2026-09-10 against `C:/projects/incms/main`,
read-only, and all re-derivable from the record's §6 snippets:

- 6550 tracked files, 656 `.ts`, 601 `.tsx`; 5017 function/method and 1369 type definitions.
- The shipped `js-regex` set pointed at TypeScript: functions 76.1% recall, types **0.6%** recall.
- A best-faith TypeScript regex set: functions 85.8% recall at 86.5% precision, types 100% recall at
  76.0% precision. It disagrees with the shipped set on 22.4% of the function population.
- Constructs a reader must survive: template literals 90.3% of files, JSX 72.2%, generics 56.6%,
  nested template expressions 43.6%, regex literals 24.9%. Decorators 0.1%. Overload signatures 0%.
- Casing: `.ts` functions 94.8% camel; `.tsx` functions 69.4% camel and 30.3% pascal; types over 99%
  pascal in both.
- P1 against the kit's shipped canon: 13.7% of `.ts` and 11.2% of `.tsx` definitions lead with a
  canon verb.

**A number you restate, you own.** Cite it as measured on that date by that record, or derive it. A
spec that types a figure beside the thing that owns it is the class this repo names most often.

## The house rules that bite hardest here

- Every cutoff in `.memory-tree.conf` is LIVE for a 2026-09-10 filename: `### Edges`, the §7 leg
  line, the §5 declared row set, the §2 scope-to-AC join, `Red when:` on every criterion, a
  backticked witness on every criterion, `§9` scope tokens from rev-2, a `base` sha that resolves,
  and §10's two facts with the probe result BEFORE the terms line.
- §10's recall terms for this build, already composed and re-runnable:
  `lexicon typescript tsx probe parser dark PATTERN_SETS coverage extractor PascalCase React casing
  tokenizer adopter`. The seam is `tools/lexicon/lexicon.py:parse_shell_defs` and its `extract_text`
  dispatch — cite it by path; "no existing seam fits" would be false here.
- The `base` sha for every spec in this build is `d1357673`.
- Tier-2 for units 2, 3 and 4. Unit 5 is Tier-1 — it moves records and no mechanism.

## The five units

### TOOL-aGradedDialect-1 — the research and the pick

Already discharged by the record above; its spec exists to carry the decision in the form §8 and §9
can be read from, not to redo the work. Tier-2. Its §8 records the mechanism fork as
`RESOLVED (agent, 2026-09-10, delegated)` and names the three losers with the test that killed each.

### TOOL-aGradedDialect-2 — the conformance corpus

The oracle and the frozen fixtures. **Order matters and is the point:** the fixtures are extracted by
`typescript@5.9.3`, which this build does not ship and did not write, and they are frozen BEFORE the
extractor exists — so no fixture can have round-tripped through the reader it grades. That is
`TOOL-dScaffoldedMirror-13`'s fixture objection answered structurally rather than promised.

In scope: the extraction procedure and the on-disk fixture format; a bounded, committed sample drawn
from real adopter files rather than authored; and the FLOOR unit 3's `parser` claim must clear,
declared here as a number with a reason rather than inherited. Out of scope: the extractor, and
vendoring anything from the adopter tree that is not needed to grade a definition site. Watch the
`fixture-passes-by-finding-nothing` class — a fixture set carrying no hard construct proves nothing,
so the sample is selected to CONTAIN template literals, JSX, generics and regex literals in the
proportions §4.2 of the record measured.

### TOOL-aGradedDialect-3 — the extractor

A tokenizer plus a definition locator, stdlib-only, living beside `_python_defs` and `_shell_defs`
and reached through the same `mode` dispatch in `extract_text`. Return shape `(functions, types,
imports)`, unchanged. Read `parse_shell_defs` first: its header enumerates its refusals and that is
the pattern to copy, not merely the code.

Its header enumerates what it REFUSES, from the record's evidence: definitions inside a template
expression, a computed method key with no name to grade, and whatever else the fixtures expose. A
file it cannot tokenize RAISES naming the construct and the line — never a partial list and never an
empty one. **`parser` is earned, not declared:** if it does not clear unit 2's floor against the
oracle, it declares `probe` and reports incomplete every run. Both outcomes are acceptable; a
`parser` label over a probe-grade reading is not.

### TOOL-aGradedDialect-4 — the declaration surface

`KNOWN_EXTS`, what `scaffold_lexicon.py` proposes for a TypeScript tree, and the cell matrix. Three
of the four casing rows are answered by a per-extension declaration and no exception list.

**The fourth is a genuine fork and it belongs in this spec's §8, not in prose.** `.tsx` functions
split 69.4% camel / 30.3% pascal by ROLE, a React component being a function that returns JSX. The
kit README names this exact population as the selector's motivating case, and the two shipped
selector kinds — `prefix` and `decorator` — cannot reach it. The record's §5 already refuses a
`case:` selector kind as vacuous, with the reason; do not re-propose it. Weigh what remains: a
parse-derived selector kind keying on whether the definition returns JSX, against declaring
`tsx.function` dark and saying so. Resolve it by M3's rule and mark it in §8's shape.

Also in scope: whether `.tsx` counts as a distinct `LANGS` extension or an alias, and what the
adopter is told about P1 on a corpus where 87% of definitions do not lead with a canon verb. That
last one is a DOC obligation, not a predicate change.

### TOOL-aGradedDialect-5 — the records

Tier-1. `tools/lexicon/LEXICON.md`'s `.ts`/`.tsx` ruling REPLACED rather than amended — it currently
says the kit does not read TypeScript, and leaving that beside code that does is the
`two-answers-to-one-question` class. The kit README's "Arming a language this kit does not ship"
section is now partly false and is rewritten to say what ships. `TOOL-dScaffoldedMirror-13` moves off
DEFERRED against its own revisit test, citing this build. The map dossier
`memory/map/features/lexicon.md` claims new keys for whatever units 2 to 4 minted.

No mechanism, no gate arm of its own. If this unit finds itself designing something, the finding is a
rescope, not a quiet widening.

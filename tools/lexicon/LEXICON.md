<!-- gov:kit lexicon@1.3 -->
# LEXICON.md — how to write the table this gate reads

The engine grades against `.lexicon.conf`. This file is how a human decides what goes in it. It is
the counterpart to the kit's `README.md`, which describes the machinery; nothing here is a rule the
gate enforces, and that is deliberate — a vocabulary is a judgement, and the gate only holds you to
the judgement you recorded.

## A verb table is a scoping instrument, not a spelling one

The question the table makes answerable is "which verb is this?", and it is answerable only when the
function does ONE thing. So the table earns its cost at the moment it *fails*: a name that will not
fit is telling you the responsibility is unclear or the seam is in the wrong place. If your reflex
on a refusal is to add a verb, the table is doing nothing — you have converted a design signal into
a synonym list.

## Write the NEGATIVE definitions

A row with only a positive gloss is decoration. The rows that carry weight are the ones pinned by
what they are NOT:

```
build   create a new value and return it — NOT `create`, which is reserved for side-effecting setup
load    read from a store into memory — NOT `fetch`, which implies a network call
remove  detach without destroying — NOT `delete`, which is irreversible
set     assign a known value — NOT `update`, which implies a diff against prior state
```

The pair is what makes the boundary checkable by a reader. Without it, two verbs drift into synonyms
and the table stops being closed in any sense that matters.

## How the table reaches whoever is writing the name

A gate that only REFUSES teaches the table one rejected commit at a time. The failure mode this kit
actually attacks is ABSENCE — an author who would have used your verb if they had known it — so the
declaration is delivered two ways, and neither of them is the gate.

- **The rendered Skill.** `adopt-lexicon.sh --render` writes `.claude/skills/lexicon/SKILL.md` from
  the declaration, rows and negatives included, so an agent carries the table without opening the
  conf. Its own gate re-renders and byte-compares, so an edit nobody re-rendered reds.
- **`python tools/lexicon/lexicon.py --suggest <name>`** answers ONE identifier from the declaration
  FIRST and the kit's frozen canon SECOND, in that fixed precedence and from no corpus at all:
  whether its leading verb is declared, and if not, which row's NOT clause names it and what that
  row means — or, where no row names it, which cluster the canon holds it in. The suggestion keeps
  your separator, case, acronyms and digits — it hands back a name you can type, not one you have to
  edit.

There used to be a third: a per-FILE reading, which listed the OBJECTS a file already defined so a
new function in it could be named alongside its neighbours. `TOOL-aSurfacedLexicon-3` deleted it, and
no unit in that build restores a per-FILE reading. The per-NAME half is back:
`TOOL-aSurfacedLexicon-7` wired `--suggest` to the canon, which is why a token the declaration does
not name now gets a replacement instead of a list of verbs. That is the size of the remaining gap,
stated rather than softened.

## DEBT and UNRULED — which refusals the kit can answer

An off-table leading token splits in two, and the split is what tells you what to DO about it.

- **DEBT** — the canon holds a cluster for the token, so it is a spelling of a concept the kit
  already names. The gate hands you the replacement identifier and the gloss. This is a rename.
- **UNRULED** — no cluster holds it. Nothing can name the replacement, because the question is not
  how to spell the concept but whether it *is* one. The gate gives you the token's site count
  instead: one site is a name to fix, twenty is a house idiom that either earns a `VERBS` row or
  gets renamed everywhere.

The corpus decides which spellings become DEBT and NOTHING else. It never decides what a concept is
called — that is the canon's, and the canon was written without reading your code. Reversing those
two is how a naming gate becomes a mirror of the habits it exists to grade.

Read the table when you are naming something, not when a gate stops you.

## Do not inherit somebody else's table

`--scaffold` reads YOUR corpus to decide which concepts are live in it, and takes what each concept
is CALLED from the kit's frozen canon. Inheriting another repo's ratified table skips the first half:
you get somebody else's concept set, which is a vocabulary for a domain you are not in. Seed from
your own corpus, delete what you did not mean, write the negative definitions your domain needs, then
stamp `ratified`.

The seed cannot exceed the canon's cluster count, and is usually well under it — only a concept with
a live definition site enters. That ceiling is `CLUSTERS` in `tools/lexicon/canon.py`; this sentence
deliberately does not restate the number, because the sentence it replaced said "twenty-five verbs is
the seed size" and the canon has never held twenty-five. If curation takes you past forty rows, the
table is describing the code rather than constraining it.

## Banned suffixes

A type named `…Manager` is a type nobody scoped. The seeded eight are prescriptive and safe to
inherit, unlike the verb table. Scope is DEFINITION sites only: a blanket ban breaks on contact with
imported names and with parameters, and Go's `context` is the standing example.

## `.ts` and `.tsx` — what a TypeScript tree can declare

The answer used to be "nothing". It is not "nothing" any more, and this section exists because
`LEXICON.md` was silent on the question for the whole life of the kit while a deferred ruling
promised to answer it here.

`KNOWN_EXTS` in `lexicon.py` carries `ts` and `tsx`, and the mode on both rows is **`parser`**. Read
it there rather than trusting this sentence — that dict is the one declaration, and a mode written
into prose beside it is the copy that rots. The token is `parser` because the reader EARNED it: a
frozen conformance corpus drawn from a real third-party TypeScript tree grades every record it
holds, and the label is whatever the score allows. `probe` was the other outcome and would have
shipped instead. **No figure from that measurement is quoted here.** The conformance arm in
`selftest.py` prints the agreement count, the per-side recall and precision, the refusal share and
the mode those earn, on every run — a number typed into this page could disagree with the arm that
computes it, and this page would be the copy nobody re-ran.

**Two extensions, two pattern-set ids** — `ts-tokens` and `tsx-tokens`, both reaching
`parse_ts_defs` with the lexer switched. `<T>(x) => x` is a generic arrow in one dialect and an
element in the other, so one lexer mode necessarily mis-reads one of the two populations. There is
no alias mechanism: an undeclared `tsx` is dark, and silently so.

**The cells `--scaffold` seeds**, all four prescriptive and none of them read off your corpus:
`ts.function` camel, `ts.type` pascal, `tsx.type` pascal, and `tsx.function` **`dark`**. That last
one is a declared refusal rather than a gap. A `.tsx` function's case is decided by its ROLE — a
React component is PascalCase and a plain helper is camelCase — and this kit reads no roles, so a
single convention over that cell would red correct code whichever one it picked. Arm it if your tree
has a rule the kit cannot see. **That reason is spelled twice on purpose, and this copy is the
lesser one:** the scaffolder emits it as a comment directly beside the row, which is where an
adopter meets it, and this page states it for a reader deciding whether to adopt at all — who has no
conf yet. If the two ever disagree, the emitted comment is the one to trust.

### The six refusals, each beside what compensates for it

**`parse_ts_defs`'s own header is the enumeration and this page is the PAIRING.** The header owes you
all six because three have no runtime failure to stage; what this page adds is the check that keeps
each one from being a silent hole. So the direction of truth runs one way: a refusal the header
gains and this list does not is a defect HERE, and a row here the header does not carry is fiction.

1. **A source it cannot tokenize** — an unterminated string, template literal, `${` substitution,
   comment, regex literal, block or JSX element. It RAISES, naming the construct and the line, and
   never returns a partial or empty list. *Compensating check:* `scan_corpus` turns the raise into a
   named refusal, so an unreadable file under an armed declaration reds instead of laundering `[]`
   into a clean run.
2. **A definition inside a template `${…}` or JSX `{…}` expression container** is suppressed rather
   than located. *Compensating check:* every such name is a recall miss against the conformance
   oracle, so the cost is PRICED by the floor the arm above enforces — a suppression that cost too
   much would take the `parser` label away rather than passing quietly.
3. **An overload signature** — a `function` declaration ended by `;` with no body — is not a
   definition. *Compensating check:* the same floor. TypeScript itself reports the implementation, so
   the oracle records the implementation and a reader that returned both would score as spurious.
4. **A name constructed by `eval`, by a decorator, or arriving through an `import`** is not found.
   *Compensating check:* none is owed, and that is the honest answer rather than a missing row —
   there is no definition SITE to grade, so no naming rule could apply to it. `parse_shell_defs`
   refuses `eval` and `source` on exactly this ground.
5. **A computed or string-literal property key** — `[k]: () => …`, `"on-change": () => …`. *Compensating
   check:* the floor again. The oracle drops computed keys before they reach a record, for the same
   reason: this kit names a definition by its identifier and there is none to name.
6. **Imports come back as an empty list.** *Compensating check:* the corpus walk discards the third
   element and the only import consumer — the self-containment refusal — reads this kit's own Python
   directly, so nothing reads a list that would otherwise be an ungraded population with a fixture
   obligation. The three-list return shape is unchanged.

Refusals 2, 3 and 5 therefore share ONE compensating check, and stating it three times is
deliberate: they are three separate ways to lose a name and the floor is what makes each of them
affordable rather than each of them being argued away.

## Layers — there is no longer anything to declare

`LAYERS` declared an intended architecture as a forbidden import direction, and it is DELETED
(`TOOL-aSurfacedLexicon-2`). It cost a glob dialect, a module index and an import resolver to
enforce, and across its whole life in this repo it graded one declared rule whose offender pin never
moved off `"0"`. What it was really holding — the kit imports nothing outside the standard library
and its own directory — is now a refusal the engine derives from its own source on every run, so
there is no declaration to write and none to get wrong.

If your `.lexicon.conf` still carries a `LAYERS:` block or a `LAYER_OFFENDER_PIN` scalar, delete
both: the reader refuses an unknown block key by name rather than ignoring it.

## Pins are a starting position, not a target

The two offender pins are MEASURED at scaffold and are a TWO-SIDED EQUALITY. A count that rises reds
and a count that FALLS reds too, printing the replacement row, because a drain nobody records leaves a
pin no tree can meet again. A non-zero day-one pin is
honest; `ORPHAN_ID_PIN` is the precedent for a pin that is legitimately non-zero on arrival. What the
kit does NOT have is a guard against lowering a pin for the wrong reason — a `probe`-mode extractor
that matches less than it should produces a smaller offender set that looks like repair. The mode is
declared and reported on every run so a reader can see which languages are incomplete, and nothing
refuses the lower automatically. That limit is recorded rather than papered over.

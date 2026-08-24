<!-- gov:kit lexicon@1.1 -->
# lexicon — a declared naming vocabulary, gated

An OPT-IN kit that gates three naming predicates against a per-repo DECLARATION. It is inert until
`.lexicon.conf` exists at the repo root, and removing that file un-adopts it.

**What it is for, since it is not typo-catching.** A closed verb table makes "which verb is this"
answerable only when a function has ONE responsibility. A name that will not fit the table is
reporting an unclear responsibility or a seam in the wrong place. That is the whole value.

**It USED to say that value was not measurable, and that the kit was opt-in because of it.** The
first half is superseded by `TOOL-dScaffoldedMirror-17`: `drift-audit`'s
`lexicon_marginal_offense_rate` derives offenders-added per definition-added between the commit that
adopted the declaration and HEAD, both operands produced by this kit's own extractor at both shas.
The kit stays OPT-IN — that did not change — but it is opt-in because adopting a vocabulary is a
choice, not because nobody could tell whether it works.

## The three predicates

| | Asserts | Scope |
|---|---|---|
| **P1** | every function or method DEFINED in the corpus leads with a verb from the declared `VERBS` table | definition sites |
| **P2** | no type DEFINED in the corpus ends with a declared `BANNED_SUFFIXES` entry | definition sites only — never an imported type, a parameter name, or a parameter type |
| **P3** | no module under a declared layer imports from a layer the declared direction forbids | tracked source |

P3 with an empty `LAYERS` reports `NOT ARMED` and **reds**. It never passes green over an absent
declaration: an unarmed predicate that exits 0 is indistinguishable from a satisfied one.

## Coverage modes — the law this obeys

`map_extractors.py` refuses to ship a regex extractor for shell and declares that language dark
instead, because a regex over shell definitions would look like coverage while silently skipping
what it forgot. Every extension present in the corpus therefore carries a DECLARED mode, and an
undeclared one is a named refusal.

| Mode | Extractor | Standing |
|---|---|---|
| `parser` | a real parse (Python `ast`) | complete over its extension |
| `probe` | a regex pattern set | incomplete BY CONSTRUCTION, reported as such every run |
| `dark` | none, declared explicitly | named every run, never silently absent |

`dark` is the honest cheap declaration, not a cop-out: most extensions in a tree carry no
definitions at all, and declaring them dark is what makes the undeclared-extension refusal
meaningful rather than noisy.

## What every run reports, and what a zero there means

Every run prints one line per predicate — `graded`, `offenders`, `waived` — on GREEN as well as on
red, because a green line carrying a file count and no population cannot be told apart from a run
that found nothing to look at.

`graded` is per (extension, PREDICATE), never per extension. Those were summed once, and the fold hid
a real state: an extension can be armed, report a healthy total, and have one of its predicates
grading ZERO. A pair in that state is NAMED every run and does **not** red:

```
lexicon: armed but grading nothing (reported, not a refusal): .js suffix=0
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
lexicon: coverage — armed 54 of 128 definition-carrying file(s) (42.2%)
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

The declaration is the half of this kit with a measured record. Since it landed, this repo added 136
definitions and zero offenders over a window in which the gate refused nothing — so the mechanism
that works is CONTEXT DELIVERY, and the failure mode it attacks is ABSENCE rather than randomness.

```bash
python tools/lexicon/lexicon.py --suggest <identifier>   # one line, no corpus pass, ~45 ms
python tools/lexicon/lexicon.py --brief <path>           # how the corpus already spells this file's objects
bash tools/lexicon/adopt-lexicon.sh --render             # re-render the Skill after a declaration edit
```

`--suggest` answers from the declaration alone. Off-table, it names the REPLACEMENT and quotes the
negative that bans what you tried — `use load_remote — the declaration says load, NOT fetch: read a
store into memory` — which is why the NOT clauses are the product rather than decoration.

`--brief` keys on the OBJECTS the file already names and reports every leading token live for each
across the corpus, flagging any object spelled more than one way. Not a directory histogram: one
adopter test directory carries 750 distinct off-table leading tokens, so a truncated list shows about
1% of the vocabulary and the truncation that bounds the cost voids the signal. On a `dark` extension
it REFUSES, because an empty "established here" section reads as invent-freely.

**Neither verb is a gate, structurally.** Neither can exit 1, neither prints a pin, and nothing in
`scaffold_lexicon.py` imports either — so what the corpus DOES has no code path to becoming what it
SHOULD do. A promise would not survive a refactor; the absence of a return path does.

### The rendered Skill

`SKILL.template.md` renders into `.claude/skills/lexicon/SKILL.md`, carrying the whole table so an
agent has it without opening the conf. It is a GENERATED second carrier and its gate re-renders and
byte-compares, so a declaration edit nobody re-rendered REDS with `DRIFTED`. The leg
(`lexicon skill wiring`) carries NO guard — its answer changes when the declaration moves, and a
kit-directory guard would leave exactly that edit unchecked.

## Waivers

Three registries beside this file, keyed on the matched **TEXT** rather than `<path>:<line>`. Keying
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

`--scaffold` derives a verb table from your own corpus by leading-token frequency and marks it
`PROPOSED`. **Curate it before ratifying.** A derived table is a mirror of the code, which is the one
shape a naming gate must not have; the rows that make it worth gating are the NEGATIVE definitions a
human writes — `build` not `create`, `load` not `fetch`. `--check` reds while `ratified` is empty, so
an uncurated seed cannot reach the merge bar disguised as a vocabulary.

Pins are MEASURED against the adopting corpus at scaffold and are never inherited: a pin copied from
a larger tree is either vacuous or permanently red.

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

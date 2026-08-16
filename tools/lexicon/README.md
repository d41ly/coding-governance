<!-- gov:kit lexicon@1.0 -->
# lexicon — a declared naming vocabulary, gated

An OPT-IN kit that gates three naming predicates against a per-repo DECLARATION. It is inert until
`.lexicon.conf` exists at the repo root, and removing that file un-adopts it.

**What it is for, since it is not typo-catching.** A closed verb table makes "which verb is this"
answerable only when a function has ONE responsibility. A name that will not fit the table is
reporting an unclear responsibility or a seam in the wrong place. That is the whole value, and it is
not measurable — which is why the kit is opt-in rather than required.

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

## Vacuity is armed on BOTH sides

A predicate that selects an empty population passes green forever and tells you nothing. The
corpus-side arm is `DEAD PROBE`: a `parser` or `probe` language whose definition population is empty,
against a corpus that contains that extension, is a refusal. That arm is itself defeated by an empty
corpus, so the kit-side arm is a frozen SENTINEL fixture per shipped pattern set in `selftest.py` —
a pattern set that goes inert fails there.

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

## Uninstalling

Delete `.lexicon.conf` and remove the kit's legs from the gate manifest. The engine then reports
`NOT ADOPTED` and exits 0.

*(An integration that declares the verb table as a `codebase-map` inventory adds a teardown ORDER to
this section. That integration is a separate, currently blocked unit — see the build record — so the
order is not written here yet, and the kit as it stands has no cross-kit coupling to unwind.)*

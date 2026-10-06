# lexicon — a declared naming vocabulary, gated

```toml
feature = "lexicon"
title = "Naming predicates over a per-repo DECLARATION — a closed verb table, a banned-suffix list and a set-valued case-convention classifier — plus a self-containment refusal, portable into a repo whose language set is unknown"
status = "shipped"
streams = ["tooling", "playbook"]
decisions = []

[claims]
gate-legs = [
  "lexicon naming predicates",
  "lexicon selftest",
  "lexicon wiring",
  "playbook placeholder catalogue",
  "placeholder-catalogue self-test",
]
kits = ["lexicon"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = ["lexicon"]
gotcha-classes = ["armed-but-unreachable-rule.md", "naming-leg-grades-what-python-named.md",
  "line-keyed-registry-reds-on-a-file-that-grew.md"]
guides = []
backlog-shards = []
lexicon-verbs = [
  "add",
  "arm",
  "cmd",
  "build",
  "check",
  "derive",
  "extract",
  "init",
  "load",
  "main",
  "measure",
  "parse",
  "print",
  "read",
  "remove",
  "render",
  "resolve",
  "run",
  "scan",
  "seed",
  "set",
  "test",
  "write",
]
[paths]
globs = [
  "tools/lexicon/*",
  "tools/check-placeholders.sh",
  "tools/check-placeholders.test.sh",
  "tools/govkit/entries/check-placeholders.kit.toml",
]
```

## Constraints & why

**The verb table is a SCOPING instrument, not a spelling one.** "Which verb is this?" is answerable
only when a function does one thing, so a name that will not fit is reporting an unclear
responsibility or a seam in the wrong place. That is the whole value. The kit is OPT-IN — the engine
reports `NOT ADOPTED` and exits 0 with no `.lexicon.conf` present — and the value is measurable:
`drift-audit`'s `lexicon_marginal_offense_rate` measures it (`TOOL-dScaffoldedMirror-17`).

**TWO QUESTIONS, TWO DECIDERS.** Companion §12 bans a gate whose vocabulary is a hand-kept mirror
of the codebase's own identifiers, so the scaffold never ranks the corpus's leading tokens
(`TOOL-dScaffoldedMirror-8`). The corpus decides MEMBERSHIP — does any spelling of this concept have
a live definition site. What it is CALLED comes from `canon.py`, frozen clusters whose element 0 is
the representative unconditionally. The corpus cannot promote a spelling and cannot nominate a verb
the canon does not hold, so the seed is prescriptive at the moment it is written.

**FROZEN IS NOT WELDED, and the difference is one declared block.** `canon.py` is `role = "engine"`,
so an adopter who disagrees with a cluster could not edit it and could not durably re-role it either
— a posture nobody chose. `TOOL-aSurfacedLexicon-11` opens a door in the file the owner already
curates: a `CANON:` block whose rows REPLACE, ADD or (with a leading minus) DELETE a cluster, merged
by `canon.build_clusters` at the cluster TUPLE rather than inside the form index, because two of the
canon's three accessors iterate `CLUSTERS` themselves and never call that index. The unfreeze is
refused without a reason-bearing `canon_unfrozen` stamp on the wiring leg, and it PRINTS on every
run of the engine, green as well as red — a quiet unfreeze would be the mirror defect with an extra
step. What the door buys is visibility and attribution, never proof: no machine check can tell a
considered overlay from one filled from the corpus's commonest spellings, and the kit says so in
both `.lexicon.conf` and its README rather than leaving a reader to find it.

The `ratified` arm is the second half: a canon-sourced seed is a starting vocabulary and not a
curated one, so it ships `PROPOSED` with `ratified` empty and reds until a human stamps it.

**Vacuity is pushed back on three ways.** The corpus-side arm is `DEAD PROBE`: a `parser` or
`probe` language whose definition population is empty against a corpus containing that extension is a
refusal. That arm is itself defeated by an empty corpus, so the kit-side arm is a frozen SENTINEL
fixture per shipped pattern set in `selftest.py`. The third is `check_self_containment`'s own
`DEAD PROBE`: a self-containment walk that judges NO imports reds rather than reporting the clean
zero a broken probe prints.

**No construction-based proof can establish that a declared rule can fire.** A synthetic derived
from a target's PATH round-trips through the resolver's own reading, so it certifies a blind
resolver REACHABLE; correctness rests on an OBSERVED failing case and fixtures in the PRODUCTION
shape. The layers predicate that taught this was deleted by `TOOL-aSurfacedLexicon-2`. See
`armed-but-unreachable-rule`.

**Coverage is DECLARED per extension, and an undeclared one is a named refusal.**
`map_extractors.py` refuses to ship a regex extractor for shell and declares that language dark
instead, because a regex over shell definitions looks like coverage while silently skipping what it
forgot. That law binds here. `dark` is the honest cheap declaration for the many extensions that
carry no definitions at all, and declaring them is what makes the undeclared-extension refusal
meaningful rather than noisy.

**A predicate that is satisfied and one that was never asked must not produce the same exit code.**
`check_self_containment` derives its own population and REDS as `DEAD PROBE` when that population is
empty, because zero offenders over zero imports is exactly the clean green a broken walk prints. Its
walk root is a PARAMETER so that arm can be staged; a predicate that can only read its own installed
directory has a liveness arm nobody can run.

**P2 is scoped to DEFINITION sites only.** A blanket suffix ban breaks on contact with imported names
and with parameters — Go's `context` is the standing example — so an imported `ThingManager` and a
`widget_manager` parameter are both green while a `class ThingManager` definition reds.

**Waivers key on the matched TEXT, never `<path>:<line>`.** Position keying means any edit ABOVE a
waived line unpins it, reddening a merge that touched nothing the waiver guards
(`TOOL-aSealedCaravan-1`). A waiver
whose text is gone reds as STALE, so a registry cannot quietly outlive what it excuses.

**`.lexicon.conf` is in the corpus leg's guard, and `lexicon wiring` still grades it unguarded.**
govkit's guard partition has a `root-conf` class taking every descriptor's `[config] file`, and govkit
selfcheck reds a guarded bar leg whose argv names one its guard lacks. TOOL-dDerivedDocket-21.

**`check-placeholders.sh` asserts what is true of a SOURCE, not of a render.** In this repo the
shipped playbook file IS the un-instantiated template and carries placeholders permanently by
design, so a bare leg asserting "no placeholder survives" would red on its own landing commit. The
bare mode therefore grades the version MARKER — present, and exactly one — while the survival
predicate lives in `--check <a> <b>` and runs only over fixtures. The render-side owner of survival
already exists and stays where it is: `tools/govkit/entries/playbook.kit.toml`'s
`playbook-placeholders` hole.

**ONE file carries the `governance-template` marker, so there is no marker LOCKSTEP**: a comparison
over a population of one is not a comparison. The gate derives the carrier count instead of
asserting one.

**`--offenders` is a key per offender, for the bar's red attribution.** No `path:line`, no count, no
cut, a repeat carrying `#<k>`; its exit is `--check`'s. `TOOL-dDerivedDocket-23`.

## Shared seams

`tools/lexicon/lexicon_conf.py` is the ONE reader of `.lexicon.conf`. Every consumer of the
file — the engine, the bash adopter, `map_extractors.py`'s `lexicon-verbs` inventory, and the two
`drift-audit` signals — and every one of them reaches it through this reader: the bash side calls
`--print-verbs`, and both Python consumers `sys.path`-insert the kit rather than growing a parser. The grammar is the sibling
`KEY=VALUE` form PLUS indented block keys, because a closed verb table with prose meanings cannot fit
a line-based conf and `map_lib.load_conf()` has no multi-line support.

That reader also decides WHICH LANGUAGES ARE ARMED. `PATTERN_SETS` in `lexicon.py` sits in an
`engine`-role file an upgrade overwrites, so an adopter with a language it lacks has no shipped
extractor to reach for. A `PATTERNS:` block in the declaration carries `<pattern-set-id>.<part>` rows, and
`resolve_pattern_sets` merges them over the shipped constant PER KEY into a new mapping that every
reader takes: the engine's one corpus walk, the coverage fraction, the scaffold's measured pins, and
`drift-audit`'s two lexicon signals. The shipped constant is never mutated — `selftest.py` compares
its frozen sentinels against it to prove every SHIPPED set has a fixture, so shipped and resolved
have to stay two names. The two out-of-kit read sites are why this is a seam: testing membership
against the shipped constant passes a declared language over while each signal reports a clean
number with `live` still true. TOOL-aSurfacedLexicon-9.

`tools/lexicon/subtokens.py` is a PORT of `map_lib.subtokens()`, not an import, and the direction of
truth is deliberate: the lexicon owns its copy so the kit ships self-contained and an adopter taking
it without `codebase-map` gets a working kit. The parity leg that keeps the two honest is
gov-internal and never ships — a shipped parity leg would compare against a file the adopter does not
have, so it would red forever or be silently skipped, and a silently skipped parity leg is the drift
the gate exists to catch. `tools/lib/resolve-python.sh` is the precedent for that shape.

That module now holds TWO predicates that never call each other, and the reason is worth carrying:
`subtokens()` LOWERCASES, so no case question survives it, and `TOOL-aSurfacedLexicon-5`'s convention
classifier therefore reads the RAW name as its SIBLING rather than consuming its output. The two also
disagree about what "no word characters" MEANS — `leading_verb` strips leading underscores and runs
ASCII subtoken classes, `read_core` strips underscores at both ends and nothing else — so the same
name is UNGRADEABLE for vocabulary and AMBIGUOUS for convention. One rule across both was never
available: they agree only on pure-underscore names and the empty string.

A per-definition FACT reaches the grader beside the population and never inside it. `extract`
returns `(name, line)` pairs that another kit unpacks positionally, so the shape is frozen; the
`decorator` selector answered that with an additive accessor keyed on the definition site, and the
`returns:jsx` selector (`TOOL-aGradedDialect-10`) rides the same seam — `extract_jsx_defs` marks
every declared `.tsx` function whose VALUE is an element, `scan_routes` reads both accessors
through one `marks` dict, and the lexer's one new token kind is walked past by every definition
arm — measured on the conformance corpus and the adopter tree, not argued from the token's
text. The rule for which definitions carry the mark, and what each clause of it
cost on the adopter corpus, is `parse_ts_source`'s header; a third accessor takes the same shape.

## Gaps

- **No pin-direction guard.** A `probe`-mode pin can be lowered on incomplete evidence — fixing ten
  real violations and an extractor that quietly matches less produce the same smaller number. CUT
  deliberately on two independent defects: guarding on the COUNT would refuse legitimate repair,
  inverting the shrink-only doctrine, and it needs a previous-value baseline the conf does not carry.
  It would serve `drift-audit` and `memory-tree` too, so it is filed as a shared follow-up rather than
  this kit's private mechanism. What survives is weaker and honest: the mode is declared and reported
  every run, so a reader can see which languages are incomplete, and nothing refuses the lower
  automatically. Related: `TOOL-aNumeralWarden-3`.
- **The verb table is closed only by CONVENTION — narrowed, not closed, by `--expand`.** Growth now
  has one supported route and that route is BOUNDED: `TOOL-aSurfacedLexicon-10` proposes only cluster
  representatives with a live site, so a leading token the frozen table does not hold cannot enter a
  proposal by any path, and `--expand --stamp` records the widening as a scalar that refuses a second
  one. Two holes stay open and are the reason this bullet survives. An owner may still paste any row
  by hand — the mode writes nothing to the block, deliberately — and clearing the stamp re-opens the
  transition, which the refusal itself says out loud. And nothing notices when a verb outlives the
  code that justified it: expansion is one-way, and there is no contraction verb. Wiring
  the table into the `codebase-map` ratchet and the `drift-audit` signal set is `TOOL-dClosedLexicon-2`,
  which is CLOSED and whose wiring is LIVE: `memory/map/generated/inventories.json` carries the
  `lexicon-verbs` inventory and `tools/drift-audit/drift_report.py` carries the signals.
- **No `memory/gotchas/` class for naming violations.** Companion §7 requires a failing case OBSERVED
  before a gate lands, and a class authored ahead of its first instance is the gate-discipline error
  this repo names. The first confirmed P1 or P2 finding becomes one.
- **`check_self_containment` resolves nothing, so its reach is narrow.** It reads an import's
  top-level name and asks whether a `.py` file of that name sits beside the engine: it judges the
  KIT's own directory and no other population, and follows no path alias, `exports` map or barrel.
- **A predicate's correctness concentrates in its helpers, and end-to-end fixtures do not reach
  them** — the finding `TOOL-aSurfacedLexicon-2` recorded when it deleted the layers predicate. A
  predicate that NEEDS helpers buys a maintenance surface; the replacement refusal has none.
- **Opt-in has no retirement condition.** `lexicon_marginal_offense_rate` measures offenders-added
  per definition-added between the declaration's adoption commit and HEAD, both operands derived by
  this kit's own extractor (`TOOL-dScaffoldedMirror-17`), and P1 stays (`TOOL-dScaffoldedMirror-16`).

## Reuse affordance

seam: lexicon.subtokens — reuse to split an identifier into lowercase word pieces across camelCase,
snake_case, kebab, path and digit boundaries, keeping acronym runs intact; extend by calling
`leading_verb` when the FIRST token is the question, and note that an identifier with no word
characters returns `""` and must be treated as ungradeable rather than as a violation. Do NOT reach
for it to answer a CASE question — it lowercases, so `BuildIndex` and `build_index` are one string
after it; `classify` in the same module is the sibling for that, returning the SET of case forms an
affix-stripped core satisfies rather than a single label.
seam: lexicon.text-keyed-waivers — reuse the shape whenever a waiver registry must survive edits to
the file it waives: key each row on the MATCHED TEXT, red when a row's text is absent from the
current findings, and never on `<path>:<line>`, which unpins on any edit above the waived line.
seam: check-placeholders.subject-split — reuse whenever a predicate is true of a RENDER but false of
the SOURCE that generates it: put the source-side question on the bar and give the render-side
question an explicit target-pair argument exercised only by fixtures, so neither mode can be pointed
at the population it would be wrong about.

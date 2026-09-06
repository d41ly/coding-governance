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
reports `NOT ADOPTED` and exits 0 with no `.lexicon.conf` present — but NOT because the value is
unmeasurable: `TOOL-dScaffoldedMirror-17` superseded that premise and `drift-audit`'s
`lexicon_marginal_offense_rate` measures it. This file carried the dead claim TWICE and `-7`
superseded only the copy in Gaps, which is this repo's own "a fix naming more than one carrier lands
in only one" class, inside the fix for it.

**TWO QUESTIONS, TWO DECIDERS — and this paragraph used to hold the answer to only one.** Companion
§12 bans a gate whose vocabulary is a hand-kept mirror of the codebase's own identifiers, and until
`TOOL-dScaffoldedMirror-8` the scaffold was exactly that: it ranked the corpus's leading tokens and
adopted the top rows, so a repo that already called everything `get` was certified as calling it
`get`. What the corpus now decides is MEMBERSHIP — does any spelling of this concept have a live
definition site. What it is CALLED comes from `canon.py`, twenty frozen clusters whose element 0 is
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

The `ratified` arm survives and is no longer the RESOLUTION, only the second half: a canon-sourced
seed is a starting vocabulary and not a curated one, so it ships `PROPOSED` with `ratified` empty and
reds until a human stamps it. This paragraph and the one above it were the SAME claim in two
carriers, and the round-1 fix rewrote the other; that is this file confessing to the class it
confesses to two paragraphs down, twice.

**Vacuity is pushed back on three ways.** The corpus-side arm is `DEAD PROBE`: a `parser` or
`probe` language whose definition population is empty against a corpus containing that extension is a
refusal. That arm is itself defeated by an empty corpus, so the kit-side arm is a frozen SENTINEL
fixture per shipped pattern set in `selftest.py`. The third is `check_self_containment`'s own
`DEAD PROBE`: a self-containment walk that judges NO imports reds rather than reporting the clean
zero a broken probe prints. The third USED to be `UNSELECTIVE LAYERS RULE`, over a declared rule
whose globs selected nothing; it went with the predicate that read it.

**P3 IS DELETED, and its failed reachability proof is the record worth keeping.** The predicate,
its `LAYERS` declaration, its glob dialect and its import resolver were removed by
`TOOL-aSurfacedLexicon-2`; nothing below describes live code. The kit's first real declaration named
a hyphenated directory no import could resolve into, so P3's offender pin read a confident 0 that no
edit could move. The first fix ADDED a construction-based reachability proof, and a review measured
it a tautology: every synthetic derived from a target's PATH round-tripped through the resolver's own
path-mirroring reading, so restoring the pre-fix blind resolver still certified the rule REACHABLE.
It was removed rather than patched. What P3's correctness rested on was `resolve_import`, an OBSERVED
failing case, and fixtures in the PRODUCTION shape — a hyphenated directory reached by a bare-stem
import, which is precisely the shape a path-shaped fixture cannot represent. The transferable half
outlived the predicate: no construction-based proof can establish that a declared rule can fire. See
`armed-but-unreachable-rule`.

**Coverage is DECLARED per extension, and an undeclared one is a named refusal.**
`map_extractors.py` refuses to ship a regex extractor for shell and declares that language dark
instead, because a regex over shell definitions looks like coverage while silently skipping what it
forgot. That law binds here. `dark` is the honest cheap declaration for the many extensions that
carry no definitions at all, and declaring them is what makes the undeclared-extension refusal
meaningful rather than noisy.

**A predicate that is satisfied and one that was never asked must not produce the same exit code.**
The written form of that used to be `P3 NOT ARMED`, over an empty `LAYERS` block nothing could
derive a proposal for. With the declaration gone the same rule binds the refusal that replaced it:
`check_self_containment` derives its own population and REDS as `DEAD PROBE` when that population is
empty, because zero offenders over zero imports is exactly the clean green a broken walk prints. Its
walk root is a PARAMETER so that arm can be staged; a predicate that can only read its own installed
directory has a liveness arm nobody can run.

**P2 is scoped to DEFINITION sites only.** A blanket suffix ban breaks on contact with imported names
and with parameters — Go's `context` is the standing example — so an imported `ThingManager` and a
`widget_manager` parameter are both green while a `class ThingManager` definition reds.

**Waivers key on the matched TEXT, never `<path>:<line>`.** Position keying means any edit ABOVE a
waived line unpins it, reddening a merge that touched nothing the waiver guards; that was hit on
`install-prefix-waivers.txt`'s first real merge and is tracked as `TOOL-aSealedCaravan-1`. A waiver
whose text is gone reds as STALE, so a registry cannot quietly outlive what it excuses.

**`check-placeholders.sh` asserts what is true of a SOURCE, not of a render.** In this repo the
shipped playbook file IS the un-instantiated template and carries placeholders permanently by
design, so a bare leg asserting "no placeholder survives" would red on its own landing commit. The
bare mode therefore grades the version MARKER — present, and exactly one — while the survival
predicate lives in `--check <a> <b>` and runs only over fixtures. The render-side owner of survival
already exists and stays where it is: `tools/govkit/entries/playbook.kit.toml`'s
`playbook-placeholders` hole.

**ONE file carries the `governance-template` marker as of v3.0, and the marker LOCKSTEP died with the
second carrier.** It is not weakened, it is gone: a comparison over a population of one is not a
comparison. The count has been miscounted in both directions — a spec once reached "three" through a
review fold, when the deploy-time catalogue's only `vN.N` was prose and a gate built to three would
have compared a literal against a real version and redded forever. Both miscounts were caught only by
measuring, which is why the gate derives the count instead of asserting one.

## Shared seams

`tools/lexicon/lexicon_conf.py` is the ONE reader of `.lexicon.conf`. FOUR consumers now need the
file — the engine, the bash adopter, `map_extractors.py`'s `lexicon-verbs` inventory, and the two
`drift-audit` signals — and every one of them reaches it through this reader: the bash side calls
`--print-verbs`, and both Python consumers `sys.path`-insert the kit rather than growing a parser. The grammar is the sibling
`KEY=VALUE` form PLUS indented block keys, because a closed verb table with prose meanings cannot fit
a line-based conf and `map_lib.load_conf()` has no multi-line support.

That reader now also decides WHICH LANGUAGES ARE ARMED, which moved a seam. `PATTERN_SETS` in
`lexicon.py` used to be the whole answer, and it sits in an `engine`-role file an upgrade
overwrites — so an adopter with TypeScript, Go or C# could only declare their language `dark`.
A `PATTERNS:` block in the declaration now carries `<pattern-set-id>.<part>` rows, and
`resolve_pattern_sets` merges them over the shipped constant PER KEY into a new mapping that every
reader takes: the engine's one corpus walk, the coverage fraction, the scaffold's measured pins, and
`drift-audit`'s two lexicon signals. The shipped constant is never mutated — `selftest.py` compares
its frozen sentinels against it to prove every SHIPPED set has a fixture, so shipped and resolved
have to stay two names. The two out-of-kit read sites are the reason this is a seam and not a
detail: both tested membership against the shipped constant and skipped, so a declared language was
passed over file by file while each signal reported a clean number with `live` still true.
TOOL-aSurfacedLexicon-9.

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

## Gaps

- **No pin-direction guard.** A `probe`-mode pin can be lowered on incomplete evidence — fixing ten
  real violations and an extractor that quietly matches less produce the same smaller number. CUT
  deliberately on two independent defects: guarding on the COUNT would refuse legitimate repair,
  inverting the shrink-only doctrine, and it needs a previous-value baseline the conf does not carry.
  It would serve `drift-audit` and `memory-tree` too, so it is filed as a shared follow-up rather than
  this kit's private mechanism. What survives is weaker and honest: the mode is declared and reported
  every run, so a reader can see which languages are incomplete, and nothing refuses the lower
  automatically. Related: `TOOL-aNumeralWarden-3`.
- **The verb table is closed only by CONVENTION.** Nothing stops it growing a verb per exception until
  it is a synonym list, and nothing notices when a verb outlives the code that justified it. Wiring
  the table into the `codebase-map` ratchet and the `drift-audit` signal set is `TOOL-dClosedLexicon-2`,
  which is CLOSED and whose wiring is LIVE: `memory/map/generated/inventories.json` carries the
  `lexicon-verbs` inventory and `tools/drift-audit/drift_report.py` carries the signals. This line
  said BLOCKED on a parked scope fork until `TOOL-aSurfacedLexicon-12` read the three carriers of
  that unit's status against each other and against the tree.
- **No `memory/gotchas/` class for naming violations.** Companion §7 requires a failing case OBSERVED
  before a gate lands, and a class authored ahead of its first instance is the gate-discipline error
  this repo names. The first confirmed P1 or P2 finding becomes one.
- **P3 RESOLVED an import to candidate PATHS and was never a full module resolver — history, not a
  live gap.** It tried the dotted-namespace-as-path reading, the last segment as a module stem
  against the tracked corpus, and relative specifiers normalised against the importer's directory. It
  did NOT follow build-tool path aliases, `package.json` `exports` maps, or re-export barrels, so an
  aliased import into a forbidden layer was never caught. The version before that compared the raw
  namespace against a path glob and was structurally incapable: the first real rule declared — naming
  a HYPHENATED directory no module name can contain — could never match, and P3 reported an
  unfalsifiable 0. `check_self_containment` inherits none of this, because it resolves nothing: it
  reads an import's top-level name and asks whether a `.py` file of that name sits beside the engine.
  What it inherits instead is a narrower reach — it judges the KIT's own directory and no other
  population, which is the whole of what the deleted rule was ever relied on for.
- **P3 TOOK three adversarial rounds and four blockers to get right, all in two helper functions,
  and that is the finding this kit paid for.** Every one lived in `_glob_match` or `resolve_import`,
  and none was visible to an end-to-end fixture — reverting the `_glob_match` rewrite verbatim left
  all 48 fixture arms green while the live gate stayed at exit 0. The last two were a `<dir>/*` glob
  whose earlier wildcard was escaped literally, so nesting stopped below depth 1, and importer-local
  precedence applied to fully-qualified dotted imports where the language grants none. Both were
  fixed, each pinned by a CASE TABLE row keyed to its defect, and all of it was deleted with the
  predicate by `TOOL-aSurfacedLexicon-2` — 164 engine lines and 29 arms for one declared rule whose
  pin never left `"0"`. The transferable finding survives the code: a predicate's correctness
  concentrates in its helpers and fixtures do not reach them, so a predicate that NEEDS helpers is
  buying a maintenance surface. The replacement refusal has none, which is the argument for its
  shape. P1, P2 and the placeholder gate were never implicated.
- **Both halves of this bullet are SUPERSEDED, and it is rewritten rather than trimmed because it
  carried two dead premises in one sentence.** It read "the benefit is unmeasurable by construction,
  which is why the kit is opt-in and why the retirement condition is written down: retire P1 if it
  goes unused across two adopters." `TOOL-dScaffoldedMirror-17` kills the first — `drift-audit`'s
  `lexicon_marginal_offense_rate` measures offenders-added per definition-added between the
  declaration's adoption commit and HEAD, both operands derived by this kit's own extractor.
  `TOOL-dScaffoldedMirror-16` kills the second: F4 is superseded, P1 stays and is strengthened, and
  no later session may close it on that condition. Opt-in survives; the REASON for it does not.

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

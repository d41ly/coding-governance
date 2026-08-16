# lexicon — a declared naming vocabulary, gated

```toml
feature = "lexicon"
title = "Three naming predicates over a per-repo DECLARATION, portable into a repo whose language set is unknown"
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
rendered-skills = []
gotcha-classes = ["armed-but-unreachable-rule.md"]
guides = []
backlog-shards = []
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
responsibility or a seam in the wrong place. That is the whole value and it is not measurable, which
is exactly why the kit is OPT-IN rather than required — the engine reports `NOT ADOPTED` and exits 0
with no `.lexicon.conf` present.

**The seed is DERIVED and then FROZEN, and the freeze is checkable.** Companion §12 bans a gate whose
vocabulary is a hand-kept mirror of the codebase's own identifiers. A prescriptive verb table is the
inverse and is safe — but `--scaffold` derives its proposal from the adopter's corpus, so for one
moment it IS the banned shape. The resolution is procedural: mark it `PROPOSED`, leave `ratified`
empty, and red until a human stamps it. Without that arm an unedited seed reaches the merge bar
disguised as a curated vocabulary.

**Vacuity is pushed back on three ways, and the third is narrower than it first shipped.** The
corpus-side arm is `DEAD PROBE`: a `parser` or `probe` language whose definition population is empty
against a corpus containing that extension is a refusal. That arm is itself defeated by an empty
corpus, so the kit-side arm is a frozen SENTINEL fixture per shipped pattern set in `selftest.py`.
The third is `UNSELECTIVE LAYERS RULE` — a rule whose FROM or TO glob matches no tracked file.

**Reachability itself is NOT proved, and the failed attempt is the more useful record.** The kit's
first real declaration named a hyphenated directory no import could resolve into, so P3's offender
pin read a confident 0 that no edit could move. The first fix added a construction-based reachability
proof, and a review measured it a tautology: every synthetic derived from a target's PATH round-trips
through the resolver's own path-mirroring reading, so restoring the pre-fix blind resolver still
certified the rule REACHABLE. It was removed rather than patched. What P3's correctness rests on is
`resolve_import`, an OBSERVED failing case, and fixtures in the PRODUCTION shape — a hyphenated
directory reached by a bare-stem import, which is precisely the shape a path-shaped fixture cannot
represent. See `armed-but-unreachable-rule`.

**Coverage is DECLARED per extension, and an undeclared one is a named refusal.**
`map_extractors.py` refuses to ship a regex extractor for shell and declares that language dark
instead, because a regex over shell definitions looks like coverage while silently skipping what it
forgot. That law binds here. `dark` is the honest cheap declaration for the many extensions that
carry no definitions at all, and declaring them is what makes the undeclared-extension refusal
meaningful rather than noisy.

**An unarmed predicate REDS.** An empty `LAYERS` reports `NOT ARMED` and exits non-zero; there is no
derived proposal for P3 because a frequency count cannot observe intended architecture. A predicate
that is satisfied and one that was never asked must not produce the same exit code.

**P2 is scoped to DEFINITION sites only.** A blanket suffix ban breaks on contact with imported names
and with parameters — Go's `context` is the standing example — so an imported `ThingManager` and a
`widget_manager` parameter are both green while a `class ThingManager` definition reds.

**Waivers key on the matched TEXT, never `<path>:<line>`.** Position keying means any edit ABOVE a
waived line unpins it, reddening a merge that touched nothing the waiver guards; that was hit on
`install-prefix-waivers.txt`'s first real merge and is tracked as `TOOL-aSealedCaravan-1`. A waiver
whose text is gone reds as STALE, so a registry cannot quietly outlive what it excuses.

**`check-placeholders.sh` asserts what is true of a SOURCE, not of a render.** In this repo the
shipped playbook files ARE the un-instantiated templates and carry placeholders permanently by
design, so a bare leg asserting "no placeholder survives" would red on its own landing commit. The
bare mode therefore grades the CATALOGUE against the measurement — coverage, per-file tallies, the
shared-placeholder declaration, and the marker lockstep — while the survival predicate lives in
`--check <a> <b>` and runs only over fixtures. The render-side owner of survival already exists and
stays where it is: `tools/govkit/entries/playbook.kit.toml`'s `playbook-placeholders` hole.

**TWO files carry the `governance-template` marker, not three.** `customize.md` is the deploy-time
catalogue, is exempt from the shipped surface, and its only `vN.N` is prose. A gate built to "three"
would compare a literal against a real version and red forever. That miscount reached a spec through
a review fold and was caught only by measuring.

## Shared seams

`tools/lexicon/lexicon_conf.py` is the ONE reader of `.lexicon.conf`. Three consumers need the file —
the engine, the bash adopter, and (when its unit unparks) `map_extractors.py` — and the bash side
calls `--print-verbs` rather than reimplementing the grammar. The grammar is the sibling
`KEY=VALUE` form PLUS indented block keys, because a closed verb table with prose meanings cannot fit
a line-based conf and `map_lib.load_conf()` has no multi-line support.

`tools/lexicon/subtokens.py` is a PORT of `map_lib.subtokens()`, not an import, and the direction of
truth is deliberate: the lexicon owns its copy so the kit ships self-contained and an adopter taking
it without `codebase-map` gets a working kit. The parity leg that keeps the two honest is
gov-internal and never ships — a shipped parity leg would compare against a file the adopter does not
have, so it would red forever or be silently skipped, and a silently skipped parity leg is the drift
the gate exists to catch. `tools/lib/resolve-python.sh` is the precedent for that shape.

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
  which is BLOCKED on a parked scope fork — the two ways to declare those signals differ in what gets
  built, and one of them changes a shipped kit's public surface.
- **No `memory/gotchas/` class for naming violations.** Companion §7 requires a failing case OBSERVED
  before a gate lands, and a class authored ahead of its first instance is the gate-discipline error
  this repo names. The first confirmed P1 or P2 finding becomes one.
- **P3 resolves an import to candidate PATHS, but it is not a full module resolver.** It tries the
  dotted-namespace-as-path reading, the last segment as a module stem against the tracked corpus, and
  relative specifiers normalised against the importer's directory. That covers the shapes this tree
  and its adopters actually write. It does NOT follow build-tool path aliases, `package.json`
  `exports` maps, or re-export barrels, so an aliased import into a forbidden layer is not caught.
  The earlier version compared the raw namespace against a path glob and was structurally incapable:
  the first real rule declared — naming a HYPHENATED directory no module name can contain — could
  never match, and P3 reported an unfalsifiable 0.
- **P3 took three adversarial rounds and four blockers to get right, all in two helper functions.**
  Every one lived in `_glob_match` or `resolve_import`, and none was visible to an end-to-end
  fixture — reverting the `_glob_match` rewrite verbatim left all 48 fixture arms green while the
  live gate stayed at exit 0. The last two were a `<dir>/*` glob whose earlier wildcard was escaped
  literally, so nesting stopped below depth 1, and importer-local precedence applied to
  fully-qualified dotted imports where the language grants none. Both are fixed and each is pinned
  by a CASE TABLE row keyed to the defect. The transferable finding is that a predicate's
  correctness concentrates in its helpers, and fixtures do not reach them: extend the tables, not
  just the fixtures. P1, P2 and the placeholder gate were never implicated.
- **The benefit is unmeasurable by construction**, which is why the kit is opt-in and why the
  retirement condition is written down rather than left to argument: retire P1 if it goes unused
  across two adopters.

## Reuse affordance

seam: lexicon.subtokens — reuse to split an identifier into lowercase word pieces across camelCase,
snake_case, kebab, path and digit boundaries, keeping acronym runs intact; extend by calling
`leading_verb` when the FIRST token is the question, and note that an identifier with no word
characters returns `""` and must be treated as ungradeable rather than as a violation.
seam: lexicon.text-keyed-waivers — reuse the shape whenever a waiver registry must survive edits to
the file it waives: key each row on the MATCHED TEXT, red when a row's text is absent from the
current findings, and never on `<path>:<line>`, which unpins on any edit above the waived line.
seam: check-placeholders.subject-split — reuse whenever a predicate is true of a RENDER but false of
the SOURCE that generates it: put the source-side question on the bar and give the render-side
question an explicit target-pair argument exercised only by fixtures, so neither mode can be pointed
at the population it would be wrong about.

# TOOL-aRuledFrontispiece-3 — dependency edges between builds, declared once and rendered both ways

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

A build that continues, blocks or supersedes another records that relation nowhere machine-readable,
so it survives only in whichever prose block an author happened to write it into. This unit adds one
authored front-matter key naming the builds a build depends on, derives the reverse direction from
it, and renders both into a generated region of the slot contract `TOOL-aRuledFrontispiece-1` defines.

## 2. Scope (IN)

- **S1** — build README front matter gains one authored key, `parents:`, holding zero or more build
  slugs separated by spaces. The key is OPTIONAL: `REQUIRED_KEYS` in `gen_build_index.py` does not
  move, so every tracked build README stays legal with no edit. The population is read from
  `python tools/memory-tree/gen_build_index.py --check`, never spelled here — this build's own folder
  postdates `base 96141aed`, and a figure written into prose is how the two counts in this build
  drifted apart in the first place.
- **S2** — the CHILD set is DERIVED and never authored. A build's children are every build whose
  `parents:` names it. `collect` already parses every build's front matter in one pass, so the
  inversion is built from data that function is already holding.
- **S3** — a generated region, opened by `<!-- gen:build-edges -->` and closed by
  `<!-- /gen:build-edges -->`, renders both directions, each slug as a relative link to that build's
  README. It is spliced by `apply_optional_region`, the create-or-splice helper
  `TOOL-aRuledFrontispiece-2` introduces at position 3 over the `apply_region`
  `TOOL-aRuledFrontispiece-1` parameterises — never by a second splicer and never by a second presence
  probe.
- **S4** — the marker pair is never hand-inserted. `--write` CREATES a missing generated-region pair at
  the slot position the contract defines, and `TOOL-aRuledFrontispiece-1` owns that behaviour and
  builds at position 1, so this unit ships a renderer and its refusals and no insertion of its own. A
  README carrying ONE edges marker is not a missing pair: it keeps every refusal `apply_region` makes
  today.
- **S5** — three refusals, each naming the README and the offending slug: a `parents:` slug that is
  not a tracked build folder; a build naming its own slug; and the same slug twice in one value. A
  fourth was specified at rev-1 — a non-empty `parents:` with no pair to render into — and S4 removed
  the state it fired on, so it is gone rather than kept as an unreachable branch.
- **S6** — arms in `--selftest`, one positive and one negative per refusal, plus a two-build fixture
  proving the child set inverts, plus a fixture proving a build with no edges in either direction
  renders the region's empty state rather than no region.
- **S7** — the `--write` output over the tracked corpus lands in this unit's own commit. S4's creation
  reaches every build README, so a fresh render stops equalling the committed bytes the moment this
  renderer exists; deferring the re-render would leave hygiene check 9 red from this unit's tip until
  some later one, which is the M6 violation the build README's ordering section re-sequenced this
  build to avoid.

## 3. Non-goals (OUT)

- Transitive closure and cycle detection. The render is one hop in each direction and nothing walks
  the graph, so a cycle renders as two ordinary rows and costs nothing.
- Authoring the child set. §4 records why deriving it is the same call `TOOL-aMouldedFolio-1` made
  about `ids:`.
- Fixing the order among generated regions. `TOOL-aRuledFrontispiece-1` places them as a block after
  the plan pair; which generated region comes first is `TOOL-aRuledFrontispiece-6`'s format leg, at
  position 11.
- Edges to anything that is not a build: a spec id, a decision id, a backlog row, another repository.
- Changing `LIVE.md` or the ledger shards. Fork 8 resolved those to no change, and §4 verifies the
  mechanism that makes it true rather than restating the resolution.
- Inserting the `gen:build-edges` marker pair into any README by hand. The generator creates a missing
  pair at the slot position the contract defines, and `TOOL-aRuledFrontispiece-1` owns that behaviour;
  this unit renders into a pair it never places.
- Declaring the edges themselves. `parents:` is authored, so every value in the corpus is an author's
  assertion; this unit ships the key, the derivation, the region and their refusals, and declares no
  edge for a build it does not own.
- The kit version bump and the closing corpus re-render. `TOOL-aRuledFrontispiece-10`, at position 10
  of the order, owns both; this unit carries only the re-render its own renderer causes, per S7.

## 4. Design

### Data model

| Field | Class | Written by | Cardinality |
|---|---|---|---|
| `parents:` | authored | nobody | 0..n build slugs, space-separated |
| the child set | derived | `collect`, by inverting every `parents:` | 0..n, never spelled in a file |
| the edges region | generated | `apply_optional_region`, on the edges marker pair | one per build README |

The encoding is the BARE BUILD SLUG, which fork 4 resolved and which fork 8's byte-neutrality
depends on. `rosters` at `gen_build_index.py:260` keys a build's roster on the id's OWN slug
component: its pattern is the declared family alternation followed by `-([A-Za-z0-9]+)-\d+`, so only
a complete family-slug-sequence token joins a roster. A bare slug matches nothing, joins no roster,
and leaves every `ids:` line where it is. `render_live` and `render_shards` read only the slug, the
derived status, `node`, `opened`, `streams` and `len(roster)` — none of which this unit moves — so
`memory/LIVE.md` and both ledger shards are byte-identical after the change. That is fork 8, verified
at source rather than assumed.

**Why these keys are not the front-matter schema that was refused.** The decision recorded as
`TOOL-aMouldedFolio-1` at `memory/DECISIONS.md:39` refused a declarative doc-contract engine and
refused keeping `ids:` authored-and-validated, on the ground that parity and freshness gates are
TRUTH-BLIND: both stay green over a self-consistent wrong render. Its operative rule, stated in §4 of
the census under `memory/builds/aMouldedFolio/build/`, is that where content is derivable it must be
GENERATED, because that converts a truth question into a freshness question the gates can answer.

The rule is applied here twice, in both of its directions.

The child set IS derivable — it is the inverse of `parents:` over the corpus — so it is derived.
Authoring it would put two answers to one question in two files that no gate could reconcile, which
is the `ids:` defect reproduced one relation over.

The parent set is NOT derivable. No tracked artifact records that one build continues another; the
relation exists only where a person asserts it. So the choice here is authored-or-absent, not
authored-or-derived, and the trade the refusal rejected — keep the authored value AND bolt a
validator onto it — has no derived alternative it is losing to.

No schema engine is added, either. `parse_front_matter` at `gen_build_index.py:159` already accepts
arbitrary keys: it stores every `key: value` line it reads and errors only when a member of
`REQUIRED_KEYS` is missing. It also already validates four specific keys against four INDEPENDENT
sources — `slug` against the folder name, `opened` against a date shape, `status` against
`STATUS_TOKENS`, and in `collect` `streams` against `DISCIPLINES` and `roster` against `FAMILIES`.
The `parents:` check is one more of that kind: each slug must be a tracked build folder, decided
against `git ls-files`. A referential check whose source of truth sits outside the document is the
opposite of the shape that was refused, which was a declared shape validated against itself.

**The falsification, recorded rather than smoothed.** This unit does not close truth-blindness for
the edge relation. Nothing checks that a declared edge is the RIGHT edge, and OMISSION is entirely
invisible: a build with a real parent and no `parents:` key is green forever. None of the four
enforcement shapes the census inventoried fits — byte-parity and freshness are the blind ones, a
ratchet needs a watched input, and a shrink-only pin needs a measured population, which an omitted
edge does not have. The limit is accepted and named. If a derivation for the parent relation is ever
found, this key must become derived, and that is the condition under which this design is wrong.

### Inventory

Three sites move, plus the pair's two marker constants, and one site deliberately does not. An
earlier revision said four moved and then listed three.

`parse_front_matter` is unchanged: arbitrary keys already parse, so the new key needs no parser edit.

`collect` gains the read, the per-build validation and the inversion. It already holds every build's
front matter in one loop, so the child map is one pass over the same list, and both sets land on each
build dictionary beside `roster` and `kinds`.

A `render_edges` function joins `render_region` and returns the region text between the edges
markers. It renders each direction as a row of relative links of the shape already used by
`render_shards`, so a reader following one lands on a real README.

`plan` splices it through `apply_optional_region`, and adds no probe of its own. That helper is
introduced one position earlier by `TOOL-aRuledFrontispiece-2` — its §4 Inventory carries the
contract — and it counts the pair's two markers with the same column-0 equality `apply_region` uses:
both counts zero means the pair is absent, and the helper inserts it at the slot position
`TOOL-aRuledFrontispiece-1` defines before splicing; any other count delegates straight to
`apply_region`, so a README carrying only a closing marker is a named failure rather than a silent
skip. A second presence probe written here, one commit after a shared one landed, would be the
two-implementations class this build exists to close, and the two would drift the first time either
side of the pair changed.

### Migration

The corpus moves in this unit's own commit, and an earlier revision of this section said it did not.
No tracked README carries a `gen:build-edges` pair, so under S4 every build README gains one the first
time `--write` runs after the renderer exists, and hygiene check 9 compares committed bytes against a
fresh render. S7 puts that re-render here rather than in a later unit.

No `parents:` key exists in the corpus yet, so on that first pass every region renders its empty
state and the added bytes are the pair, the header and one empty-state line per README. The artifact
COUNT does not move: the region lands inside files this render already produces and creates none.
`TOOL-aRuledFrontispiece-5`, at position 6, installs the byte cap after this unit, so it measures a
corpus that already carries this region rather than predicting one.

`tools/unattended/check-unattended.sh` check 8 is unaffected, verified rather than assumed: it names
`<!-- gen:build-index -->` and its closer explicitly when it slices the build README, so a second
region under a different marker name never enters that comparison.

### Alternatives rejected

**A link-wrapped id, such as a markdown link whose text is another build's unit id.** Rejected: it is
a CITE. `corpus_ids.walk` collects every id-shaped match on every line into `cites`, and check 14
reds any id in `cites` that is absent from `defs` unless it is listed in
`memory/project/id-orphan-waiver.txt`. That registry holds 5 rows against a seed of 4 and
`ORPHAN_ID_PIN="5"` is shrink-only, so an edge naming a unit that has no spec either reds outright or
demands a waiver row the pin forbids. It also collides with the build README's own rule that a
planned unit may not be named by id before its spec lands.

**A bare id in a leading pipe cell, such as a table row opening with another build's unit id.**
Rejected, and it fails twice. `A_TABLE` at `tools/memory-recall/extract.py:118` matches a line
opening with a pipe, optional backticks or asterisks, then an id — reached from `corpus_ids._anchor`
through `extract.anchor_at`. A bare id in cell 1 therefore ANCHORS: it DEFINES that id, the
definition lands in `def_builds` keyed by THIS build's folder, and check 13 reds the id as claimed by
two build folders. Separately, `rosters` skips a build's README only for its OWN slug, so the foreign
id is read here and joins the OTHER build's roster, and `--write` then rewrites that build's `ids:`
line. The second failure is silent until that build is next rendered.

The two are genuinely different, which is why both are listed: the bracket in a markdown link is not
admitted by `A_TABLE`'s optional-marker class, so a link-wrapped id in a pipe cell cites without
anchoring. That is why the existing generated unit table is safe and a bare-id table would not be.

**Authoring both directions, one key each.** Rejected as the two-answers-to-one-question class in
miniature: two files could declare opposite edges and no gate on the bar could tell which was right.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · its `--selftest` arms ·
`tools/memory-tree/HYGIENE.template.md`, whose rule 9 spells the front-matter key list at line 140,
with `memory/HYGIENE.md` re-rendered from it by
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render` and never hand-edited — that harness
byte-pairs the two after substituting this install's prefix, and its declared direction is template to
live copy · every tracked build README, as the `--write` output S7 lands in this commit.

## 5. Production-readiness checklist

- security — N/A. The new key is read from a tracked file the generator already reads whole, and no
  value crosses a trust boundary.
- perf / scale — one extra pass over the build list that `collect` has already built in memory.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Slugs and markers are ASCII literals.
- error / empty / loading states — an absent key, an empty value and a build with no children are all
  legal and each is an arm; a build with no edges in either direction renders the region's empty
  state, which is what every README shows on this unit's first `--write`.
- observability — every refusal names the README and the offending slug, never a count alone.
- risks — the derived child set is only as complete as the authored parent sets, so an omitted
  declaration silently removes an edge in both directions; §4 records that as an accepted limit with
  no instrument that fits.
- testing + left-shift gates — arms in the generator's `--selftest`, plus AC6 over the real corpus for
  S4 and S7; the binding format leg is `TOOL-aRuledFrontispiece-6`.
- migration / rollback — one `git revert` of this unit's commit, which carries the engine change, the
  rendered `HYGIENE.md` pair and the corpus re-render together, so no half state is reachable.
- user docs — the key joins rule 9's front-matter list in `HYGIENE.md` and its kit template together.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs over the corpus at this
  unit's tip, it exits 0, and the artifact count it prints equals the count the same command prints at
  this unit's PARENT commit. Both counts are read from the gate, never from a figure quoted in a
  document: this build's own folder was created after `base 96141aed` and adds one artifact, so the
  base count is not the comparand.
- **AC2** — When a fixture build declares `parents:` naming a slug that is not a tracked build folder,
  `--check` fails naming that README and that slug.
- **AC3** — When a fixture build declares its own slug in `parents:`, `--check` fails naming that
  README and that slug.
- **AC4** — When two fixture builds are rendered and the second declares the first as a parent,
  `--write` renders the first build's edges region naming the second as a child, with no `children:`
  key present in either file.
- **AC5** — When a fixture build carries only the closing edges marker, `--check` fails with the
  wording `apply_region` already uses for an unequal marker count, and the message names that README.
- **AC6** — When `--write` runs over the tracked corpus at this unit's tip, every build README carries
  exactly one `<!-- gen:build-edges -->` pair, `git diff` shows no change outside those pairs, and a
  second `--write` leaves the tree clean under `git diff --exit-code`. This is the corpus observation,
  not a fixture: it is what S4's creation and S7's re-render assert together.
- **AC7** — When `--write` runs over a corpus carrying edge declarations, `memory/LIVE.md` and every
  file under `memory/ledger/` are byte-identical to their state at this unit's PARENT commit, checked
  with `git diff --exit-code -- memory/LIVE.md memory/ledger/`. Fork 8 is the claim, and the parent is
  the comparand for the same reason AC1 gives.
- **AC8** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at this unit's tip, checks 13
  and 14 report nothing new and `memory/project/id-orphan-waiver.txt` still holds 5 rows.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it passes and its arm
  count is strictly greater than at `base 96141aed`.
- **AC10** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs at this unit's tip, it
  passes with no `--render` left to do, so `memory/HYGIENE.md` is the render of the edited
  `tools/memory-tree/HYGIENE.template.md` and not a hand-edit.

## 7. Gates

`python tools/memory-tree/gen_build_index.py --selftest` · hygiene checks 9 and 13-16 via
`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
for the paired `HYGIENE.md` edit · `bash tools/memory-tree/marker-contract.test.sh`, because a third
marker pair enters the contract that test drives · `bash tools/unattended/check-unattended.sh`, whose
check 8 slices the build README by marker name · `bash tools/memory-tree/check-verdict-epoch.sh`,
which `TOOL-aRuledFrontispiece-10` discharges for the whole build at position 10.

## 8. Open questions

none — fork 4 resolved the encoding to build slugs and fork 8 resolved the live index and the ledger
to no change, and §4 verifies the mechanism behind both rather than restating them.

The build README's park P1, how many directions are authored, is RESOLVED (owner, 2026-08-16): one
authored `parents:` key, children derived. This spec already ships that shape, so nothing here
changes; the resolution is recorded because §4 argued the derivation from `TOOL-aMouldedFolio-1`
rather than from a decision made for this build, and a later reader needs to know it was decided
rather than defaulted.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit. `plan` was to grow a second presence probe one commit
  after `TOOL-aRuledFrontispiece-2` lands a shared one; §4 Inventory and S3 now splice through that
  unit's `apply_optional_region` and add no probe. The marker pair's insertion was deferred to the
  retrofit unit, which never carried it — the set's largest blocker — so S4 states that the generator
  creates a missing pair and cites `TOOL-aRuledFrontispiece-1` as its owner, new S7 lands the corpus
  re-render that creation causes in this unit's own commit, and S5 drops the fourth refusal because
  the state it fired on no longer exists. Restated the paired `HYGIENE.md` edit as a template edit
  followed by `--render`, the direction `kit-dogfood-parity.test.sh` declares, and added AC10 for it.
  Retargeted AC1 and AC7 onto this unit's parent commit rather than a base the build's own folder
  postdates, and replaced the byte-identity AC with a corpus observation. Recorded park P1's
  resolution. Corrected §4 Inventory's own count, which said four sites move and then listed three.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `front matter schema refused
derived truth-blind anchor cite orphan waiver roster slug component marker region build edges
dependency`.

The map probe for "render a derived edge list between build folders into a marker-delimited region"
returned `apply_region`, `render_region`, `render_live` and `render_shards` in `gen_build_index.py`
as the only marker-region and build-render seams in the corpus, plus the marker-contract gate leg. No
seam exists for an inter-build relation of any kind.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| splice into a named marker pair, optionally | `apply_optional_region`, introduced by `TOOL-aRuledFrontispiece-2` | REUSE unchanged — this unit adds a call, not a probe and not a second splicer |
| place a pair a README does not carry | the slot-position insertion `TOOL-aRuledFrontispiece-1` ships | REUSE unchanged — this unit spells no position of its own |
| decide whether an id-shaped token joins a roster | `rosters` at `gen_build_index.py:260` | REUSE unchanged — it is the reason a bare slug is inert, and this unit reads it rather than editing it |
| render a relative link to another build's README | `render_shards` at `gen_build_index.py:549` | REUSE THE SHAPE — the same link form, resolved from the build folder instead of the ledger |
| accept a new front-matter key | `parse_front_matter` at `gen_build_index.py:159` | REUSE unchanged — arbitrary keys already parse, so the parser needs no edit |
| refuse an unknown build slug | none | BUILD — the check is membership in the tracked build-folder set, which no existing predicate exposes |

The claims that `rosters` matches only a full family-slug-sequence token, that `parse_front_matter`
accepts arbitrary keys, that `A_TABLE` does not admit a bracket, and that check 8 of the unattended
kit names the build-index markers explicitly were each verified against source at writing time.

# TOOL-aMouldedFolio-2 — the build README's `ids:` becomes derived, and its mechanical prose joins the generated region

**Status:** CLOSED · rev-3 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling · ratified 2026-08-11

## 1. Goal

Stop authoring the one build-README field that has no rule, no validator and a measured live error,
by deriving it from the id corpus instead. The same change absorbs two prose blocks that restate
machine-known facts, so the README's authored surface shrinks to the narrative that genuinely needs
a human.

## 2. Scope (IN)

- **S1** — `ids:` in every build README is DERIVED. A build's ROSTER is every id of the form
  family-slug-sequence where the slug is that build's directory name and the sequence is all digits,
  occurring anywhere in the READ SET defined in §4. `--write` rewrites the front-matter value;
  `--check` reds when a committed value differs from the roster.
- **S2** — an EMPTY roster is a named failure naming the build, never a silent blank and never a
  fallback to the authored value. No build has an empty roster today, so this branch guards a
  regression rather than a live case.
- **S3** — the `Node · opened · streams` restatement line and the `Records live under …` boilerplate
  paragraph move inside the generated region, rendered from the same front matter the region already
  reads.
- **S4** — the full roster is rendered ONLY in the build README's region. The live index and the
  ledger shards carry the roster's COUNT in place of the id list, because those two artifacts are in
  the entry-budget population and the README region is not.
- **S5** — the build-index selftest gains a positive and a negative arm per new branch: the empty
  roster, a revision-suffixed anchor that must not join a roster, an id appearing only in an excluded
  artifact that must not join a roster, the self-reference exclusion, and a families-mismatched
  fixture that must RED rather than render empty rosters.

## 3. Non-goals (OUT)

- No prose template for the authored narrative. Measured: 17 of 25 READMEs carry no section heading
  at all, so a shape rule would describe eight files and invent one for the rest.
- No change to the corpus module. rev-2 scoped an accessor there; §4 records why the measurement
  removed the need.
- No new gate leg, and no change to any existing gate's predicate or exemption set. The entry budget
  is obeyed by rendering less, never by widening the exemption.
- No repair of the colliding decision rows, and no repair of the hygiene arms sentence. The review
  established that the derivation touches neither: a roster is a SET, so a duplicated id does not
  change it. The owner's ratified "unit 1 repairs what it touches" therefore selects nothing here.
- No change to the unit count, the unit table, or what counts as a unit.
- No change to the id grammar, the orphan pin, or the waiver registry's contents.
- No adopter-facing work. Unit 7 owns delivery.

## 4. Design

### Data model

A build's ROSTER is the set of ids matching the pattern built from the declared family alternation,
the build's own directory name as a literal, and a digits-only sequence, found anywhere in the READ
SET.

The **read set** is every tracked file under the memory root, MINUS three exclusions:

1. the build's own README — because the field being written must not be an input to the value
   written, or a wrong value defends itself forever;
2. the generated live index and the generated ledger shards — because both are rendered FROM the
   field, so including them is the same self-reference one hop out;
3. nothing else. The rotated log is IN: rotation is a storage event, and a build does not lose an id
   because its decision row aged out.

Three properties make this simpler than the two earlier drafts, and each was measured rather than
reasoned:

- **The digits-only sequence is the only filter needed.** All 42 ids it drops are revision-suffixed
  anchors of the form sequence-plus-letter, and dropping them alone yields the ratified counts.
- **The rotated log needs no exclusion.** Excluding it changes exactly two builds and changes them
  wrongly, removing one real id from each.
- **Occurrence and definition agree.** Over 26 builds the two rules produce identical rosters on 21,
  and the five that differ are exactly the five orphan-waived builds, where occurrence finds the id
  and definition finds none. So the weaker rule is not weaker in practice, and it costs neither the
  sibling kit's anchor grammar nor a subprocess.

| Build | Units | Roster |
|---|---:|---:|
| aUnmannedHelm | 7 | **10** |
| aMendedLedger, aDrainedSluice, aFoldedQuarry | 8, 9, 7 | **9** each |
| aBatchedTribunal | 3 | **8** |
| aCandidStub | 1 | **6** |
| aNumeralWarden | 1 | **4** |
| the five orphan-waived builds | 0 | **1** each |

**Units and roster are different quantities and the design keeps them different.** A unit is a spec
carrying a parseable status header; a roster member is an id that exists in the record. For the
unattended build those are 7 and 10, because three of its ids have no spec at all. Rendering them as
one number would re-create the motivating defect inverted. The invariant that DOES hold, and that S5
arms, is containment: every unit id is a member of its build's roster, measured at zero violations.

Why not the corpus module's definition map, which rev-2 scoped an accessor for: reaching it means
`walk()`, whose first statement loads the sibling recall kit's grammar unconditionally and which
shells out for a pattern this design no longer needs. That would promote an optional kit into a hard
prerequisite of index generation, which hygiene check 9 calls on every run, and break adopters who
are green today. The family alternation this design does need is already loaded and already
validated against by the renderer.

### Inventory

| Function | Change |
|---|---|
| `collect` | computes the roster per build over the read set |
| `render_region` | renders the full roster; adds the two absorbed prose blocks |
| `render_live`, `render_shards` | render the roster COUNT, not the list |
| `parse_front_matter` | `ids` stays required; its value is no longer read for rendering |
| `do_write` | rewrites the front-matter value from the roster |
| `do_check` | reds on a committed value differing from the roster |
| the selftest | the arms in S5 |

One module changes. The read set is assembled from the tracked file list the module already obtains,
so the exclusions are a path predicate, not a new source.

### Migration

Every build's front-matter value is rewritten by the tool. No file is hand-edited for S1, so the
migration cost is one command.

### Rollout

One commit: the module change, the regenerated artifacts and the selftest arms land together,
because the regeneration is what makes the change observable and check 9 fails if they are split.

### Files touched (estimate)

| File | Why |
|---|---|
| the build-index module | S1 through S5 |
| 25 build READMEs, the live index, both ledger shards | regenerated |
| the hygiene engine | the kit version constant and its kit marker both live on one line there, not in the project conf |
| the shipped hygiene rule set and its installed copy | the version marker on line 1 of each, which the kit-version gate pairs against that constant |
| the kickoff manifest | the audit stamp, because the files above sit on its watch pathspec |

### Alternatives rejected

- **Derive from the walker's per-build map.** Ratified first, withdrawn on measurement: it is a units
  index that blanks six builds and narrows ten.
- **Import the full walker, or add an accessor beside it.** rev-2's design; withdrawn because the
  measurement above removed the need for anchor recognition entirely, and reaching that module costs
  a cross-kit and a shell dependency on a path check 9 always runs.
- **Render the full roster into the live index and the shards.** Measured at 316 to 435 characters
  against a 300-character entry budget on four builds, with nothing grandfathered.
- **Widen the entry budget's exemption set.** A gate widened to fit a renderer is the gate answering
  to the code.
- **Scan the whole memory root including the README and the generated indexes.** Rejected: the value
  would be an input to itself, which is how a wrong value survives every regeneration.

## 5. Production-readiness checklist

| Concern | Position |
|---|---|
| Self-reference | The read set excludes the field's own file and both artifacts rendered from it, so no input to the roster is downstream of the roster. |
| Empty population | Two granularities. A PRECONDITION that the read set matched at least one id anywhere, and a per-build POPULATION. Precondition non-zero with every roster empty is one named failure; a single empty roster is its own named failure. |
| Wrong grammar | A families list that matches nothing yields empty rosters everywhere, which is what a clean corpus would also yield. The precondition above converts that silence into a red, and S5 arms it with a mismatched-families fixture. |
| Entry budget | The full roster goes only where no cap applies. The capped artifacts carry a count, bounded by two digits. S5 asserts the longest rendered line in the capped artifacts stays under the cap. |
| Cost | One additional pass over the already-read tracked memory files, with one compiled pattern per build. No subprocess and no sibling-kit import, so the added cost is a fraction of the module's current run. |
| Idempotence | Two consecutive writes produce identical bytes. |
| Ordering | The roster renders sorted by family, then by numeric sequence, so a two-digit sequence does not sort before a one-digit one. |
| Failure visibility | A per-build failure names the build and the offending value, and the walk does not abort on the first bad build. |
| Reversibility | The prior values are in git; reverting the module and regenerating restores the bytes. |

## 6. Acceptance criteria

- **AC1** — the unattended build's README region names all ten roster ids, and continues to state
  seven units. The two are labelled as different quantities and are not required to agree.
- **AC2** — every unit id is a member of its build's roster, across every build.
- **AC3** — hand-editing a front-matter roster to a wrong value and running the checker reds with a
  message naming that build; running the writer restores it.
- **AC4** — adding a plausible but never-minted id to a build's own README front matter does NOT put
  it in that build's roster, and the writer removes it.
- **AC5** — a revision-suffixed anchor is absent from every roster; the build whose unfiltered count
  is 38 renders 8.
- **AC6** — an id whose only occurrence is in the generated live index or a ledger shard is absent
  from every roster.
- **AC7** — the region for a build carrying the absorbed prose renders it, and no README retains a
  hand-authored copy of either block outside the markers.
- **AC8** — every rendered line of the live index and of both ledger shards is under the entry-budget
  cap, measured after regeneration, and the hygiene run is green.
- **AC9** — the writer is idempotent: a second consecutive run writes zero changed bytes.
- **AC10** — a fixture whose families list matches nothing reds with the precondition's named message,
  rather than rendering 26 empty rosters.
- **AC11** — with the sibling recall kit absent and every corpus pin blank, the checker still runs and
  every roster still derives.
- **AC12** — every new failure branch has a positive arm in the build-index selftest naming that
  branch's own text. The shell harness meta-gate does not reach this module, so the selftest is the
  arming instrument and the meta-gate is not evidence either way.

## 7. Gates

The full bar, `bash tools/run-gates.sh`, green at the push boundary, on a QUIESCENT tree. The
affected legs are the memory hygiene run, the build-index selftest, the kit-dogfood parity leg once
the shipped rule set's marker moves, the verdict-epoch and kit-version pair once the engine moves,
and the kickoff-manifest ratchet because those files are watched. The corpus-ids selftest and the
harness arms meta-gate are NOT affected, and neither is evidence for any acceptance criterion here.
The recurring-bug-class checklist runs over the diff before review.

## 8. Open questions

- **RESOLVED (owner, 2026-08-11): which roster semantics.** The full roster, not the units. Ratified
  against a premise about the walker's per-build map that measurement withdrew; resolved in favour of
  the owner's INTENT by keying on the id's own slug.
- **RESOLVED (owner, 2026-08-11): blast radius.** Unit 1 repairs what it touches, and the review
  established the derivation touches neither recorded defect, so this unit carries no repair.
- **RESOLVED (owner, 2026-08-11): adopter reachability.** Folded into this build as unit 7.
- **RESOLVED (review, 2026-08-11): what the capped artifacts show.** A count, not the list.
- **RESOLVED (measurement, 2026-08-11): definition or occurrence.** Occurrence over an
  exclusion-bounded read set. The two rules agree on 21 of 26 builds and the five that differ are the
  orphan-waived builds, so the rule that costs no cross-kit dependency loses nothing.

## 9. Revision log

- rev-1 · 2026-08-11 · first draft from the ratified route.
- rev-2 · 2026-08-11 · Tier-2 review fold: 38 raw findings, 19 confirmed, 8 blockers, 0 unverified.
  The roster overflowed the entry budget on four builds, so the capped artifacts now carry a count.
  The derivation as worded was a different function than the one measured. The planned import carried
  a cross-kit and a shell dependency into a function every hygiene run calls. AC1 demanded units and
  roster agree, which is unsatisfiable and would have re-created the motivating defect inverted.
- rev-3 · 2026-08-11 · design simplification, from three measurements taken while preparing the
  build. The digits-only filter alone reproduces the ratified counts, so the append-only exclusion is
  unnecessary — and it was also wrong, removing one real id from each of two builds. Occurrence over
  a bounded read set equals definition on 21 of 26 builds and differs only on the five orphan-waived
  ones, where it is the better answer, so the corpus-module accessor scoped in rev-2 is withdrawn
  entirely and no cross-kit or shell dependency is acquired. The empty-roster fallback is withdrawn
  with it: no build has an empty roster under this rule, so the branch becomes a named failure
  instead of a silent fallback. Self-reference is newly identified and excluded — the earlier drafts
  would have scanned the very field they write.

## 10. Reuse audit

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| The declared family alternation | the project conf, already loaded and already validated against by this module | REUSE; no second declaration |
| The tracked file list | the list this module already obtains | REUSE; the exclusions are a predicate over it |
| Splice a generated region into an authored file | the module's region applier | REUSE unchanged for S3 |
| Byte-compare a generated artifact | hygiene check 9 | REUSE; no new leg |
| Bound a failure population | the hygiene engine's two-granularity guard | PATTERN reused, not the function: it is shell and guards path selectors, and this module is Python and has none |
| Name a failure without a stack | the module's own failure type | REUSE unchanged; rev-2's cross-module reconciliation is moot now that no second module is called |

Nothing is duplicated. The corpus module's definition map answers a larger question at the cost of
two dependencies this module must not acquire, and §4 records the measurement showing the larger
answer is not needed.

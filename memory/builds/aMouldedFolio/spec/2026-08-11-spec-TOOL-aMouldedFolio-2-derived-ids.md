# TOOL-aMouldedFolio-2 — the build README's `ids:` becomes derived, and its mechanical prose joins the generated region

**Status:** SPECCED · rev-2 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling · ratified 2026-08-11

## 1. Goal

Stop authoring the one build-README field that has no rule, no validator and a measured live error,
by deriving it from the id corpus instead. The same change absorbs two prose blocks that restate
machine-known facts, so the README's authored surface shrinks to the narrative that genuinely needs
a human.

## 2. Scope (IN)

- **S1** — `ids:` in every build README is DERIVED. A build's ROSTER is every id whose slug component
  equals the build directory name and whose sequence component is all digits, taken from definition
  sites in the tracked memory corpus OUTSIDE the append-only region. `--write` rewrites the
  front-matter value; `--check` reds when a committed value differs from the derivation.
- **S2** — where the derivation is EMPTY, the authored value is preserved untouched, and every id it
  names must appear in the orphan waiver registry. An empty derivation whose id is not waived is a
  named failure, not a silent pass.
- **S3** — the `Node · opened · streams` restatement line and the `Records live under …` boilerplate
  paragraph move inside the generated region, rendered from the same front matter the region already
  reads.
- **S4** — the full roster is rendered ONLY in the build README's region. The live index and the
  ledger shards carry the roster's COUNT in place of the id list, because those two artifacts are in
  the entry-budget population and the README region is not.
- **S5** — the derivation is exercised by a positive and a negative arm per new branch in the
  build-index selftest, including the empty-derivation fallback, the unwaived-orphan refusal, the
  append-only exclusion, and a wrong-root fixture that must RED rather than fall back.
- **S6** — the corpus module gains a narrow importable accessor returning the id-to-paths definition
  map alone, with no grammar and no shell dependency, so the renderer can reuse the one definition of
  "a definition" without inheriting the citation analysis it does not need.

## 3. Non-goals (OUT)

- No prose template for the authored narrative. Measured: 17 of 25 READMEs carry no section heading
  at all, so a shape rule would describe eight files and invent one for the rest.
- No new gate leg, and no change to any existing gate's predicate or exemption set. The entry budget
  is obeyed by rendering less, never by widening the exemption.
- No repair of the colliding decision rows, and no repair of the hygiene arms sentence. The review
  established that the derivation touches neither: a roster is a SET, so a duplicated id does not
  change it. The owner's ratified "unit 1 repairs what it touches" therefore selects nothing here.
  Both stay open in the research record.
- No change to the unit count, the unit table, or what counts as a unit.
- No change to the id grammar, the orphan pin, or the waiver registry's contents.
- No adopter-facing work. Unit 7 owns delivery.

## 4. Design

### Data model

A build's ROSTER is the set of ids satisfying all three conditions:

1. the id's slug component equals the build directory name;
2. the id's sequence component is entirely digits;
3. the id has at least one definition site — a row anchor or a recording's first-level heading —
   in the tracked memory corpus, at a path the append-only classifier does NOT match.

Condition 2 excludes revision-suffixed anchors. Condition 3 excludes the rotated log. Both were
implicit in rev-1's measurements and stated in neither, which made rev-1's table irreproducible from
its own prose: the unfiltered reading gives one build 38 ids where the table said 8.

The append-only region is not re-spelled here. The hygiene engine already owns that classification
and prints it on demand, and the accessor in S6 takes the pattern as a parameter so the renderer
passes what the engine printed rather than a second literal.

| Build | Units | Roster | Unfiltered |
|---|---:|---:|---:|
| aUnmannedHelm | 7 | **10** | 10 |
| aBatchedTribunal | 3 | **8** | 38 |
| aCandidStub | 1 | **6** | 6 |
| aDrainedSluice | 9 | **9** | 15 |
| aMendedLedger | 8 | **9** | 11 |
| aRootedPrefix | 1 | **3** | 7 |
| aDeployScout and four others | 0 | **0** | 0 |

**Units and roster are different quantities and the design keeps them different.** A unit is a spec
carrying a parseable status header; a roster member is a defined id. For the unattended build those
are 7 and 10, because three of its ids have no spec at all. Rendering them as one number would
re-create the motivating defect inverted. The invariant that DOES hold, and that S5 arms, is
containment: every unit id is a member of its build's roster, measured at zero violations today.

The five builds with an empty roster are exactly the five ids in the orphan waiver registry. An id
defined nowhere is what the orphan check counts, and a build whose only spec is a legacy-named
recording has no anchor line to define it. S2's fallback is therefore bounded by a registry the bar
already grades, and it drains when those builds gain a conforming spec.

### Inventory

| Function | Change |
|---|---|
| corpus module | S6: a narrow accessor returning the id-to-paths definition map, parameterised by an exclusion pattern, with no grammar or shell dependency |
| `collect` | computes the roster per build from that accessor |
| `render_region` | renders the full roster; adds the two absorbed prose blocks |
| `render_live`, `render_shards` | render the roster COUNT, not the list |
| `parse_front_matter` | `ids` stays required; its value is an input only for the empty case |
| `do_write` | rewrites the front-matter value where the roster is non-empty |
| `do_check` | reds on a committed value differing from the roster |
| `main`, the selftest's arm helper | catch the corpus module's failure type as well as the local one |

The renderer must not import the existing full walker. That walker calls the grammar loader on its
first statement, unconditionally, which hard-requires the sibling recall kit even when every corpus
pin is blank — the documented OFF state — and it shells out to the hygiene script for the
append-only pattern. Importing it would promote an optional sibling kit into a hard prerequisite of
index generation, which hygiene check 9 calls on every run, and would break adopters who are green
today. It would also void rev-1's stated reason for preferring an import over a subprocess, since
the walker subprocesses anyway. S6 exists to give the narrow thing instead.

The two modules define two different failure types, and the renderer's entry point catches only its
own. A failure raised inside the accessor would therefore surface as a stack trace, reopening the
named-error guarantee the renderer's own docstring records as closed. Both call sites catch both.

### Migration

Twenty builds have their front-matter value rewritten by the tool; five keep theirs. No file is
hand-edited for S1, so the migration cost is one command.

### Rollout

One commit: the module change, the regenerated artifacts and the selftest arms land together,
because the regeneration is what makes the change observable and check 9 fails if they are split.

### Files touched (estimate)

| File | Why |
|---|---|
| the corpus module | S6, the narrow accessor |
| the build-index module | S1, S3, S4, the failure-type reconciliation, the selftest arms |
| 25 build READMEs, the live index, both ledger shards | regenerated |
| the hygiene engine | the kit version constant and its kit marker both live on one line there, not in the project conf |
| the shipped hygiene rule set and its installed copy | the version marker on line 1 of each, which the kit-version gate pairs against that constant |
| the kickoff manifest | the audit stamp, because the files above sit on its watch pathspec |

### Alternatives rejected

- **Derive from the walker's per-build map.** Ratified first, withdrawn on measurement: it records a
  slug only when the defining file sits under that build's directory, so it blanks six builds and
  narrows ten — the units-only reading the owner had already declined.
- **Import the existing full walker.** Rejected above: cross-kit hard dependency, a shell dependency,
  and roughly five times the runtime on a function check 9 calls unconditionally.
- **Render the full roster into the live index and the shards.** Rejected: measured at 316 to 435
  characters against a 300-character entry budget on four builds, with no slack and nothing
  grandfathered.
- **Widen the entry budget's exemption set to admit those rows.** Rejected: the budget is a real
  constraint on files meant to be skimmed, and a gate widened to fit a renderer is the gate answering
  to the code instead of the reverse.
- **Keep the value authored and validate it.** Leaves an authored field as the source of a fact the
  corpus already knows, and needs several files repaired by judgment before the check can go green.

## 5. Production-readiness checklist

| Concern | Position |
|---|---|
| Empty population | The renderer has no emptiness guard today. S5 adds a two-granularity assertion in the module itself: a PRECONDITION that the corpus defines at least one id at all, alongside the per-build population. Precondition non-zero with every roster empty is one named failure, not twenty waiver messages and five silent fallbacks. |
| Wrong-root grammar | A derivation bound to the wrong root yields an empty classification, which is what a clean corpus also yields. S5 arms a fixture whose families do not match the tree; it must RED rather than fall back. |
| Entry budget | The full roster goes only where no cap applies. The capped artifacts carry a count, whose width is bounded by two digits. S5 asserts the longest rendered line in the capped artifacts stays under the cap. |
| Cost | The narrow accessor skips the grammar load and the subprocess that dominate the full walker. Budget the added cost per generator invocation and assert it stays a fraction of the hygiene run; the accessor is memoised per process so one run pays once. |
| Idempotence | Two consecutive writes produce identical bytes. |
| Ordering | The roster renders sorted by family then by numeric sequence, so a two-digit sequence does not sort before a one-digit one. |
| Failure visibility | A per-build failure names the build and the offending value, and the walk does not abort on the first bad build. |
| Reversibility | The prior values are in git; reverting the module and regenerating restores the bytes. |

## 6. Acceptance criteria

- **AC1** — the unattended build's README region names all ten roster ids, and continues to state
  seven units. The two are labelled as different quantities and are not required to agree.
- **AC2** — every unit id is a member of its build's roster, across every build.
- **AC3** — hand-editing a front-matter roster to a wrong value and running the checker reds with a
  message naming that build; running the writer restores it.
- **AC4** — for each of the five waived builds, the writer leaves the authored value byte-unchanged.
- **AC5** — removing one of those five ids from the waiver registry reds with a message naming the id
  and the build, rather than silently blanking the field.
- **AC6** — a revision-suffixed anchor and an anchor whose only definition site is in the append-only
  region are both absent from every roster; the build with 38 unfiltered ids renders 8.
- **AC7** — the region for a build carrying the absorbed prose renders it, and no README retains a
  hand-authored copy of either block outside the markers.
- **AC8** — every rendered line of the live index and of both ledger shards is under the entry-budget
  cap, measured after regeneration, and the hygiene run is green.
- **AC9** — the writer is idempotent: a second consecutive run writes zero changed bytes.
- **AC10** — a failure raised inside the accessor surfaces as the module's own named error line, never
  as a stack trace.
- **AC11** — with the sibling recall kit absent and every corpus pin blank, the checker still runs and
  the roster still derives.
- **AC12** — every new failure branch has a positive arm in the build-index selftest naming that
  branch's own text. The shell harness meta-gate does not reach this module, so the selftest is the
  arming instrument and the meta-gate is not evidence either way.

## 7. Gates

The full bar, `bash tools/run-gates.sh`, green at the push boundary, on a QUIESCENT tree. The
affected legs are the memory hygiene run, the build-index selftest, the corpus-ids selftest, the
kit-dogfood parity leg once the shipped rule set's marker moves, the verdict-epoch and kit-version
pair once the engine moves, and the kickoff-manifest ratchet because those files are watched. The
harness arms meta-gate is NOT affected and is not evidence for AC12. The recurring-bug-class
checklist runs over the diff before review.

## 8. Open questions

- **RESOLVED (owner, 2026-08-11): which roster semantics.** The full roster, not the units. Ratified
  against a stated premise that the walker's per-build map yields it; measurement showed that map is
  a units index. Resolved in favour of the owner's INTENT by deriving from the id's own slug. rev-2
  adds the two filters the measurement used and rev-1 failed to state.
- **RESOLVED (owner, 2026-08-11): blast radius.** Unit 1 repairs what it touches. The review
  established that the derivation touches neither recorded defect, so rev-2 carries no repair.
- **RESOLVED (owner, 2026-08-11): adopter reachability.** Folded into this build as unit 7.
- **RESOLVED (review, 2026-08-11): what the capped artifacts show.** A count, not the list. The full
  roster lives in the README region, which carries no cap.

## 9. Revision log

- rev-1 · 2026-08-11 · first draft from the ratified route.
- rev-2 · 2026-08-11 · Tier-2 review fold: 38 raw findings, 19 confirmed, 8 blockers, 0 unverified.
  Three blockers changed the design. The roster overflowed the entry budget on four builds, so S4
  now renders a count in the capped artifacts. The derivation as worded was a different function than
  the one measured, so the data model states the digit-sequence and append-only filters. The planned
  import carried a cross-kit and a shell dependency into a function every hygiene run calls, so S6
  adds a narrow accessor instead. AC1 demanded units and roster agree, which is unsatisfiable and
  would have re-created the motivating defect inverted; it is split, and containment replaces
  equality. S5's repairs left scope because the derivation touches neither. The failure-type
  reconciliation, the emptiness precondition, the sort rule, the cost row and the corrected
  files-touched table are all review findings.

## 10. Reuse audit

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| Decide what counts as a definition | the corpus module's existing anchor and heading recognition | REUSE via S6's accessor; a second definition would be the two-answers class |
| Classify the append-only region | the hygiene engine's printed classifier | REUSE by passing it in, rather than spelling a second literal |
| Splice a generated region into an authored file | the build-index module's region applier | REUSE unchanged for S3 |
| Byte-compare a generated artifact | hygiene check 9 | REUSE; no new leg |
| Waive a known-absent id | the orphan waiver registry and its shrink-only pin | REUSE as the bound on S2's fallback |
| Bound a failure population | the hygiene engine's two-granularity guard | PATTERN reused, not the function: it is shell and guards path selectors, and the module being changed is Python and has none |
| Name a failure without a stack | the build-index module's own failure type | REUSE, extended to catch the corpus module's type at both call sites |

The one thing deliberately not reused is the full corpus walker, and the Design section states why:
it answers a larger question at the cost of two dependencies this module must not acquire.

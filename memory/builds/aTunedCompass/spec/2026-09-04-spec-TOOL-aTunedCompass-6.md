# TOOL-aTunedCompass-6 — the reuse probe ranks its neighbour pool before it truncates it

**Status:** CLOSED · rev-5 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aTunedCompass-6-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aTunedCompass-6-acceptance-ledger.md) | journal | — |
| [2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round1.md) | diff-review | TOOL-aTunedCompass-1 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round2.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round2.md) | diff-review | TOOL-aTunedCompass-1 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-4-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-4-spec-audit-round2.md) | spec-audit | TOOL-aTunedCompass-4 TOOL-aTunedCompass-9 |

<!-- /gen:spec-records -->

## 1. Goal

Move the neighbour cap in `tools/codebase-map/reuse_lookup.py` to AFTER the ranking, so the twelve
neighbour slots go to the twelve the ranking would keep rather than to the twelve whose names sort
earliest. The cap is currently spent on a criterion nobody chose, and a high-fan-in neighbour whose
name sorts late is discarded before it can ever be ranked.

## 2. Scope (IN)

- **S1** — the reorder at `tools/codebase-map/reuse_lookup.py` (`:243`). The neighbour pool is
  ranked first and the cap applies to the ranked list. The line after it, `:246`, already sorts the
  whole shortlist by seed-ness then descending fan-in, and this unit makes the cap read that same
  ordering instead of an alphabetical accident.
- **S2** — the ordering key is stated once and read twice, not retyped. The cap must not acquire a
  second key that can drift from the shortlist sort.
- **S3** — seeds are untouched. They are not capped today and are not capped after this unit, and
  their ordering is unchanged.
- **S4** — an arm in `tools/codebase-map/selftest.py` over a synthetic corpus where a high-fan-in
  candidate sorts after the cap boundary and a zero-fan-in candidate sorts before it. The arm's red
  is observed against the shipped ordering before the arm is written.
- **S5** — the probe's output header states what the neighbour ranking does NOT mean. Twelve
  high-fan-in names read as twelve seams to everybody who did not write the ranker, and
  `TOOL-aScouredKit-16` already records that the fan-in count resolves no symbols.
- **S6** — the before-and-after over the phrase corpus is produced by a COMMITTED replay harness, not
  a one-off. F2 resolved this: the harness is a tracked, registered, on-demand script that no merge-bar
  leg runs, on the same split the owner ruled for a kit's self-tests. §4 says what it grades. It lands
  at `tools/codebase-map/replay-phrases.py`.
- **S7** — that path is claimed EXPLICITLY in `tools/codebase-map/kit.toml` as
  `role = "project-owned"`. The kit's `[[files]] include = "**" role = "engine"` rule means an
  unclaimed new file under this directory ships verbatim to every adopter, and `govkit.py`'s
  `LANDABLE_ROLES` is `(engine, seed)`. What would ship here is a harness that parses THIS repo's
  build records for probe phrases — useless to an adopter and exactly the shape
  `memory/gotchas/pin-copied-from-another-corpus.md` names. The memory-recall kit already withholds
  its three gov-only files this way, and that precedent is the one being copied.
- **S7b** — the SECOND carrier, because the first covers only half the install surface. A
  `project-owned` role withholds a file from `govkit apply` and from nothing else —
  `tools/memory-recall/kit.toml` says exactly that in its own words, and pays for it with an explicit
  `rm -f` step in the runbook. This kit's documented copy-install is a plain `cp -r`
  (`WIRE-INTO-PROJECT.md` §3b step 1), which the descriptor does not reach, so the harness needs a
  matching removal step there and a line in that runbook's adopter inventory. One carrier alone is a
  withholding that reads as complete and is not.
- **S8** — the harness DECLARES a wall-clock ceiling, and the SCRIPT ITSELF enforces it: it self-times
  and exits non-zero on a breach. That is the whole enforcement, stated because "the runner that owns
  it reds on a breach" left the enforcing component unnamed and uncreated — this suite is on no leg,
  so there is no other runner to inherit it from. The unattended kit's on-demand runner carrying its
  own budget is the precedent. This repo reds a suite arriving without a ceiling, and F2's resolution
  names the obligation explicitly.

## 3. Non-goals (OUT)

Two adjacent questions are deliberately outside this unit, and each stays a backlog row because each
needs its own measurement before its own design.

- Whether to index private symbols. `TOOL-aWeighedCompass-13` owns it. The symbol index drops every
  name beginning with an underscore, and a private helper is the internal seam a reuse audit hunts
  for, but admitting them changes the size and the precision of every arm at once.
- Whether to demote the name-stem seed arm. `TOOL-aWeighedCompass-14` owns it. That arm is the
  reason the probe returns unrelated symbols sharing a stem, and it is a SEED-side question; this
  unit touches only neighbours.

Also out:

- Not changing `NEIGHBOUR_CAP`'s value. Raising it buys more of the same bytes and leaves the
  criterion wrong.
- Not changing the neighbour PREDICATE. What makes a candidate a neighbour stays `same file as a
  hit` or `same kind`. §8 F1 is where that decision is put to the owner.
- Not fixing the fan-in signal itself. `TOOL-aScouredKit-16` records that it counts bare identifier
  tokens with no symbol resolution; S5 discloses that rather than repairing it.
- Not making the phrase-set replay a merge-bar leg. It grades a corpus and costs a probe per phrase.
  It is on no bar and runs on demand, which is F2's resolution; S8 gives it the declared ceiling that
  status obliges, so "no ceiling anyone has declared" is no longer the reason and is no longer true.

## 4. Design

### The defect, at source

`tools/codebase-map/reuse_lookup.py` (`:243`) iterates `sorted(neighbours.items())[:NEIGHBOUR_CAP]`,
which is an alphabetical slice. `_rank` computes fan-in per surviving name, and only then does
`:246` sort the shortlist by seed-ness, descending fan-in and name. So the ranking runs on a pool
the alphabet has already chosen. This is proven at source and needs no fixture to demonstrate.

### What the cap actually selects today, measured on this corpus

Measured at BASE on node a, against the probe phrase this spec's own §10 records:

| Figure | Value |
|---|---|
| candidates in the corpus | 645 |
| neighbour pool for that phrase | 634 |
| symbols of kind `class` | 28 |
| symbols of kind `function` | 616 |
| `NEIGHBOUR_CAP` | 12 |

Every class name in this corpus begins with an uppercase letter and every function name does not,
and an ASCII sort orders every uppercase name before every lowercase one. So whenever the seed set
contains a single class, the twelve neighbour slots are filled from the 28 class names before any of
the 616 function names is considered, and no function can be a neighbour at all. The live probe run
confirms it: all twelve neighbours returned were classes with initials in the range A to D.

### What the reorder selects instead, measured on the same phrase

| Ordering | The twelve retained | Fan-in sum |
|---|---|---|
| alphabetical, shipped | `Affordance` through `DuplicatedContent` | 8 |
| by fan-in, after this unit | `main`, `read_text`, `key`, `run`, `resolve`, and seven more | 271 |

The two sets do not overlap at all, and the highest fan-in anywhere in the 634-strong pool is 37,
against a maximum of 4 among the twelve the shipped code keeps.

### What that measurement does to the claim, said plainly

The reorder is a strict improvement against the stated ranking key. It is NOT obviously an
improvement against the question a reader is asking. `main`, `run`, `key`, `search` and `write` are
generic, and they are exactly the names an unresolved token count inflates, which is the defect
`TOOL-aScouredKit-16` records. On this evidence the reorder trades alphabetical noise for fan-in
noise, and the honest framing is that it makes the ranking DO what it says while leaving open
whether what it says is worth doing.

The unit is still worth building for two reasons that survive that framing. The cap is currently
spent on a criterion nobody chose, which is a defect regardless of what the right criterion is. And
nothing can price the neighbour arm while its pool is truncated before the ranking runs, so this
reorder is the precondition for every later decision about neighbours.

### The acceptance instrument, in two layers

The durable layer is S4's synthetic arm. It is deterministic, costs nothing, and fails if the
ordering regresses. It proves the MECHANISM.

The corpus layer is S6's replay, and it is the one that answers whether the right thing moved. The
parent build left a graded phrase corpus behind: specs record a literal probe phrase, and each
spec's §10 also names the seam its author chose. That pairing is the ground truth, and it is the
better of the parent's two, because it grades against a seam a human picked rather than against
every file a unit happened to edit, and it needs no commit-to-id join.

The replay runs each recorded phrase against the shipped ordering and against the reordered one at
the same base sha, and reports hit rate, hit@5, hit@10 and the upper-median rank of the first correct
path, before and after. A neutral or negative delta is a legal result and is recorded as the result.
The reorder touches only the neighbour tail of each shortlist, so a small delta is the expected
outcome and a large one would itself be worth explaining.

Two costs the replay carries, stated because they are not obvious. The parent's harness lived in a
session scratchpad and is not in the tree, so it is rebuilt rather than re-run. And the phrase
extraction is not a one-line grep: 186 tracked records under the build tree carry a literal
invocation, but only 74 hold the phrase on a single line inside double quotes, so a parser that
joins wrapped invocations is the difference between grading 74 phrases and grading the parent's 133.

### Files touched (estimate)

`tools/codebase-map/reuse_lookup.py`, `tools/codebase-map/selftest.py`,
`tools/codebase-map/map_lib.py` for the `KIT_CODEBASE_MAP_VERSION` marker AC7 asserts,
`memory/map/features/codebase-map.md` for the dossier refresh §5 owes,
`tools/codebase-map/replay-phrases.py` as the committed harness S6 names,
`tools/codebase-map/kit.toml` for the `project-owned` rule S7 requires so that harness does not ship,
`WIRE-INTO-PROJECT.md` for the copy-install removal step and adopter-inventory line S7b requires, and
the generated map artifacts under `memory/map/generated/` that adding a tracked Python file to a kit
directory re-renders — `codebase-map coverage + freshness` reds if they are stale in the same commit.
Seven source files plus the regenerated artifacts, and one record under this build's folder holding
the replay's output.

rev-3 resolved F2 to a committed harness and left this table at four files naming no script, §3
still calling the replay unceilinged, and S6 still describing the one-off the owner rejected — so a
builder could not tell which file to create, and `TOOL-aTunedCompass-10`'s own criterion depends on
an artifact this unit's scope did not produce.

### Alternatives rejected

Raising `NEIGHBOUR_CAP` instead of reordering was rejected. It leaves the selection criterion
alphabetical and adds bytes to a probe already costing about 10.8 KB per run.

Dropping the cap entirely was rejected on the same byte evidence, with a 634-strong pool behind it.

Sorting the `neighbours` dict by fan-in as it is built was rejected. Fan-in would then be computed
in two places and the ordering key would exist twice, which is the drift S2 exists to prevent.

## 5. Production-readiness checklist

- security — N/A. A read-only ranking over an index the probe already builds.
- perf / scale — `_rank` runs over the whole neighbour pool rather than over twelve of it, so fan-in
  is computed 634 times instead of 12 on a probe of this shape. Fan-in is an index lookup and the
  probe already computes it for every seed, but the replay must report the wall-clock delta rather
  than assume it is free.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — an empty neighbour pool must stay an empty section rather than
  becoming a refusal; the probe already handles a shortlist with seeds only.
- observability — the probe logs to its own lookups file, and the replay reads recorded phrases
  rather than that log, so nothing new has to be recorded for this unit to be gradeable.
- risks — the real risk is a reader treating twelve high-fan-in generic names as twelve seams. S5
  answers it in the output rather than in a spec nobody rereads.
- testing + left-shift gates — S4 is the gate. The class is "a selection that happens before the
  ranking that is supposed to select", and the arm covers that class rather than this instance.
- migration / rollback — no data. Reverting is a one-line move of the slice.
- user docs — the `codebase-map` dossier under `memory/map/features/` is refreshed in the same
  commit per the DoD, because the ranking it describes changes.

## 6. Acceptance criteria

- **AC1** — When the arm in `tools/codebase-map/selftest.py` runs over a synthetic corpus holding a
  high-fan-in neighbour whose name sorts after the cap boundary, that neighbour is in the
  shortlist, and a zero-fan-in neighbour sorting before the boundary is not. The same arm is
  observed RED against the shipped `sorted(neighbours.items())[:NEIGHBOUR_CAP]` before it is
  written.
- **AC2** — When `python tools/codebase-map/reuse_lookup.py` is run on the phrase this spec's §10
  records, before and after, the twelve retained neighbours change from the twelve alphabetically
  first to the twelve highest by fan-in, and the two sets do not intersect. The RELATION is the
  criterion. The two fan-in sums this spec quoted at rev-3, 8 and 271, were measured at base
  `c4fcf5ad`, on a tree that does not contain this unit's own new harness file; that file adds symbols
  to the index the probe builds, so a literal re-measured after the unit lands need not reproduce
  either number, and pinning them would make the criterion fail for a reason that is not a defect.
  Both halves are run at ONE tree state and the figures recorded beside the result.
- **AC3** — When the same replay is inspected, the SEED half of the shortlist is byte-identical
  before and after, which is the observation that `_rank` and the seed arm were not disturbed.
- **AC4** — When the replay over the recorded phrase corpus runs, graded against the seam each
  spec's own §10 names, it records hit rate, hit@5, hit@10 and the upper-median rank of the first correct
  path for both orderings, in a record under `memory/builds/aTunedCompass/build/`, together with
  the phrase count it actually graded. A neutral or negative delta is recorded as the result.
- **AC5** — When `python tools/codebase-map/reuse_lookup.py "<any phrase>"` runs, its header names
  what the neighbour ranking does not mean, alongside the `recall partial` line it already prints.
- **AC9** — When `git ls-files` is run against the harness path S6 names, it returns that path; the
  script prints its declared wall-clock ceiling when invoked with no arguments; and — the observation
  that matters — with the ceiling temporarily set below the measured wall clock, the script EXITS
  NON-ZERO, restored before landing. A ceiling whose breach was never observed is an assertion about
  nothing, which is this repo's own rule about a gate that has only ever been seen to pass. The path
  is spelled in S6 and in §4
  and deliberately NOT backticked here: `python tools/check-spec-tokens.py` joins every path-shaped
  backticked token in a §6 bullet against `git ls-files`, so a criterion naming a file its own unit
  has yet to create reds the bar before the unit is built. Observed: it did, on this spec, at fold
  commit `5bc5b3f9`.
- **AC10** — When `python tools/govkit/govkit.py selfcheck` runs and when an `apply` is performed
  against a scratch target, the harness is NOT written into that target, and
  `tools/codebase-map/kit.toml` names it with an explicit `project-owned` role. The observation that
  matters is the apply, not the descriptor: the descriptor is the mechanism and the absent file is
  the property.
- **AC11** — When `cp -r`-style copy-installation is followed per `WIRE-INTO-PROJECT.md` §3b, the
  harness does not arrive in the target either. `project-owned` withholds a file from `govkit apply`
  ONLY — `tools/memory-recall/kit.toml` says so in its own words and pays for it with an explicit
  `rm -f` step in that runbook — so the descriptor alone leaves the copy path open, and this kit's
  §3b step 1 is a plain `cp -r`. The runbook gains the matching removal line.
- **AC6** — When `python3 tools/codebase-map/selftest.py` and
  `python3 tools/codebase-map/test_codebase_map.py` run, both are green.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it is green with
  `KIT_CODEBASE_MAP_VERSION` moved.

## 7. Gates

The legs this unit must keep green when it is built, by their `tools/gate-legs.json` names:
`codebase-map kit selftest`, `codebase-map coverage + freshness`, `codebase-map adopter e2e`,
`kit version markers`, `lexicon naming predicates`, whose guard covers `tools/`,
`spec tokens (a spec's own names resolve)`, and `govkit selfcheck`, which is the leg grading the
descriptor S7 edits.

The last two were added at rev-5 and both were live omissions rather than tidying. The spec-tokens
leg is `subject = repo` with no guard, so it runs on every bar, and rev-4's own new criteria turned
it RED on two untracked backticked paths — a spec must name the leg its acceptance section can
break. And a unit that edits a `kit.toml` owes the leg that grades kit descriptors. The full bar is
`bash tools/run-gates/run-gates.sh`. `codebase-map kit selftest` and `codebase-map adopter e2e` have
the KIT as their subject, so this repo's standing ruling holds them off the ordinary bar and this
unit's Definition of Done owes them under `GATE_SELFTESTS=1`, which is what the charter requires of
kit work. This unit adds no new leg; it adds one arm to a suite that is
already a leg, and S6's replay is deliberately not wired as one.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): the predicate moves, but as its own unit.** The owner first chose to
narrow `same kind` rather than ship the reorder alone, then chose to split that narrowing into a
separate unit so M2's one-mechanism rule holds. This unit therefore keeps the reorder alone and its
scope is unchanged; what changes is that the predicate is no longer deferred to a backlog row but is
`TOOL-aTunedCompass-10`, which sequences immediately after this unit and lands in the same pass. The
two are not provably disjoint under M6, so they are sequenced rather than parallel.

**F2 RESOLVED (owner, 2026-09-05): commit the replay harness as an on-demand script that no bar runs.** The
owner did not take this fork's recommendation of a recorded one-off, and the reason is that the
owner's answer to F1 makes the measurement load-bearing: a unit that changes the neighbour predicate
needs a re-runnable before-and-after, not a method somebody must rebuild. It takes the same split
this repo's owner ruled for a kit's self-tests — in the tree, registered, run on demand, on no leg —
and it therefore owes a declared wall-clock ceiling like any suite here.

- **F1 — does the reorder ship alone, or does the neighbour PREDICATE move with it?** Measured
  above: the `same kind` arm admits 634 of 645 candidates for a phrase whose seeds include one
  class, so the neighbour pool is very nearly the whole corpus and no cap over it selects
  meaningfully by any key. The reorder therefore changes WHICH noise a reader gets rather than
  removing noise.
  Options: ship the reorder alone and open the predicate as its own row; narrow `same kind` in this
  unit, for instance to same kind AND same kit directory; hold the reorder until the predicate is
  decided.
  Recommendation: ship alone. The reorder is proven at source and must not wait on a design that
  has no measurement yet, and narrowing the predicate changes what a neighbour IS, which is a
  different unit with a different acceptance. The counter-argument is honest and is why this is a
  fork: shipping alone lands a change whose measured effect on this corpus is to substitute one set
  of low-value names for another, and an owner may reasonably want the two decided together.

- **F2 — is the replay harness committed, or a recorded one-off?** The parent's harness is not in
  the tree, so the instrument is rebuilt either way. A committed harness makes AC4 reproducible from
  the tree by anyone; it is also a new maintained surface with a phrase parser, a ground-truth
  extractor and no declared ceiling.
  Options: rebuild it in a scratchpad and record only its output and its method; commit it under the
  codebase-map kit; commit it and register it as an on-demand script that no bar runs.
  Recommendation: the recorded one-off, with the method written out in enough detail to rebuild. The
  durable regression protection is S4's arm, and a grading harness earning a permanent home is its
  own unit with its own cost argument. The cost of that pick is stated rather than hidden: AC4's
  numbers would then be reproducible from the record's method and not by running a tracked file.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The pool sizes, the kind counts, and both twelve-name sets
  were measured at BASE on node a; the precision and hit-rate figures are cited from the parent
  build's findings record and were not re-derived.
- rev-2 · 2026-09-05 · M2 cross-read. Files touched named two files while AC7 asserted a marker in
  `tools/codebase-map/map_lib.py` and §5 promised a dossier refresh, neither of which was listed;
  `TOOL-aTunedCompass-8` carries both for the same kit and was the document that agreed with itself.
  §7 also named two `subject = kit` legs without the `GATE_SELFTESTS=1` clause its siblings state.
- rev-3 · 2026-09-05 · both forks resolved by the owner. The predicate narrowing becomes
  `TOOL-aTunedCompass-10` rather than a backlog row, so the non-goals now name a sibling unit; the
  replay harness is committed as an on-demand script with a declared ceiling.
- rev-4 · 2026-09-05 · round-1 spec audit folded, finding B3 — and B3 is precisely rev-3's second
  clause never leaving §8. The resolution committed a tracked, registered, on-demand harness with a
  declared ceiling; S6 still described the recorded one-off the owner had rejected, §3 still called
  the replay unceilinged, §4 Files-touched named four files and no script, and no criterion observed
  the harness at all. A builder could not tell which file to create or where the ceiling lived, and
  `TOOL-aTunedCompass-10`'s AC4 depends on an artifact this unit's scope did not produce. S6 now names
  `tools/codebase-map/replay-phrases.py`; S7 claims it `project-owned` in `tools/codebase-map/kit.toml`,
  because that kit's `include = "**" role = "engine"` rule would otherwise ship a harness that parses
  THIS repo's build records to every adopter — the defect
  `memory/gotchas/pin-copied-from-another-corpus.md` names, and the reason the memory-recall kit
  withholds its own three files; S8 carries the ceiling; AC9 and AC10 observe the path, the ceiling
  and the withholding, with AC10 asserting on the APPLY rather than on the descriptor.
- rev-5 · 2026-09-05 · round-2 spec audit folded, findings B2, H5, M3, M4, M5 and M6 — every one of
  them created by rev-4's own fold. B2 was the sharp one: rev-4's two new criteria put untracked
  backticked paths in §6, and the `spec tokens (a spec's own names resolve)` leg is `subject = repo`
  with no guard, so the bar went RED at commit `5bc5b3f9` and the waiver registry is shrink-only, so
  it could only be reworded. AC9 now names the harness without backticking a path its own unit has yet
  to create; M4's `tools/govkit/govkit.sh`, which has never been tracked at any revision, becomes
  `python tools/govkit/govkit.py selfcheck` with the hedge dropped. A third hit of the same class, in
  unit 8, was found by re-running the leg rather than by the review. H5 — `project-owned` withholds a
  file from `govkit apply` and nothing else, while this kit's documented install is a plain `cp -r`,
  so S7b adds the runbook carrier and AC11 observes it. M5 — S8 said "the runner that owns it reds on
  a breach" and no scope item created that runner; the script now self-times, and AC9 observes the RED
  rather than the printed number. M3 — AC2 pinned two fan-in sums measured at base on a tree without
  this unit's own new file, which changes the index; the criterion is now the relation. M6 — §7 gained
  `govkit selfcheck`, the leg that grades the descriptor S7 edits, and the spec-tokens leg its own
  acceptance section had just broken; Files-touched gained the runbook and the regenerated map
  artifacts.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "rank candidate reuse seams by fan-in before truncating
the shortlist"` ranks `fan_in` and `seam_fanin_threshold`, both in `tools/codebase-map/map_lib.py`
and both marked SEAM at fan-in 3, above `assemble_shortlist` in
`tools/codebase-map/reuse_lookup.py`. `assemble_shortlist` is the seam this unit edits and the two
map_lib functions are the ones it must keep calling unchanged, which is the correct answer: the
ranking key already exists and this unit moves a slice relative to it rather than adding a
mechanism. The probe's own run is also the exhibit in §4, since its twelve neighbours were the
twelve alphabetically-first class names in the corpus.

`python tools/memory-recall/query.py "how was the reuse probe's neighbour cap chosen and what does
its ranking order buy" --terms "codebase-map reuse_lookup neighbour cap fan-in seam threshold
ranking name stem shortlist precision probe"` returned 40 hits. Three bind. The parent's own row
states the defect and names the one-line shape. A second row records the precision figure and the
sizes behind it. The third is `TOOL-aScouredKit-16`, which measures the fan-in signal itself as
mostly unresolved tokens, and it is the record that turns this unit's §4 from a straightforward
improvement into F1.

Recall terms used: `codebase-map reuse_lookup neighbour cap fan-in seam threshold ranking name stem
shortlist precision probe`.

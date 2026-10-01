**Serves:** spec-audit TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13

# dDerivedDocket — spec audit of topic group G2, the derived backlog core, round 3

*Node `d`, 2026-09-20. The third Tier-2 adversarial pass over the eight live G2 specs: the ask parser
and status fold (unit 6), the generated family view (7), the hygiene engine in builds mode (8), the
transition-merge audit (9), the row driver's shard-into-view refusal (10), the migration planner
(11), the relocation tools (12), and the straggler hooks and inventory (13). Unit 14, retired at
WONTDO, was not a subject. This is a FOLD review, regrounded on `fb07ca25`: origin/main moved 210
commits past the original BASE `abac6d59`, HEAD merges it in, and every spec re-verified its claims
there and moved its header base under a section 9 line reading `regrounded on fb07ca25`. Code claims
below are judged at HEAD. The pass was aimed at the text no reviewer has seen — every section 9 line
dated after the round-2 record — and at whether each round-2 fix holds. Four primed finder lenses ran
and all four returned; a skeptic stage prompted to REFUTE each finding ran in five batches and all
five returned; then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief's roster and edge tables, and the round-2 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round2.md`.
Sibling specs outside G2 were read wherever an edge or an interface named them, units 34 and 35 most
of all. Every entry below was re-checked against the spec text and, where it rests on the behaviour
of a tool, against source at HEAD; the sites read are named in each entry. The eight blobs below were
confirmed equal to the working tree before this report was written.*

**Round: 3.** Range at base `fb07ca25`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-6.md@e87ce42cab186ff76f9e5032a7ef2f2fe016a154`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-7.md@176128b4ea289998d910c4e6a9810328d5582a14`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-8.md@8eae24a1e1f5ec5f6d2a2e8850912e7c7b044fd4`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-9.md@2e638a3bc0f0d7bb4d7bda565fbadeba82ff5d4a`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-10.md@dcd7ee0253eb979560bb52eec35cd58dc57be92d`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-11.md@b4d57fda6fcbd5512c20fb3c4c80f252628632dc`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-12.md@1e7be906228d5383720ccf7b092989c2a3170733`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-13.md@aa54b18d2516cfea7fbdfccb9ad59b1604baae0a`

## Verdict: CLEAN WITH FIXES

No blocker stands, and none stood in round 2 either. Two HIGH defects stand, carrying three raw ids
between them, and both are the same shape at root: a criterion written about a tree state that this
build's own later units destroy before the criterion is allowed to run.

- H1 (ids 12, 26) is unit 8 AC10, the ONLY criterion proving the hygiene engine moved nothing for a
  shards adopter. Its new permission line defers the comparison to "once after the last unit is
  terminal", by which point unit 9 has added check 25's announcement lines to the same engine and
  unit 34 has flipped this repo out of shards mode. Run as scheduled it must fail, for changes unit 8
  did not make, over a tree that is no longer the subject.
- H2 (id 19) is unit 9's watched path set. It is the whole of `<MEMORY_ROOT>/archive/`, which at HEAD
  also holds the rotated decision log. Running the real `extract.anchor_at` over
  `memory/archive/DECISIONS.2026-08-10.md` returns 79 anchored ids, every one of which reads as a NEW
  row on a shards-mode straggler that rotated its decision log. Check 25 then reds on that node
  naming decision ids, and the only remedy it prints is a `RELOCATED` row per decision id.

Four MEDIUM defects and four LOW follow, one raw id each. Nothing below stops the switch-over or its
landing; H1 costs the build its one darkness proof, and H2 produces a false red on a routine
straggler action.

**No decision is needed from the owner.** Every entry names a fix the fold can apply locally, which
is the difference between this round and round 1. H1 is the only one whose fix must be chosen between
two shapes, and both shapes are stated in the entry.

Convergence under `memory/guides/BUILD-METHOD.md` M4: the blocker count held at 0 and the high count
moved from 0 defects to 2 defects (3 ids), while the confirmed total fell from 37 to 11 and the
distinct-defect count from 22 to 10. By blockers the loop would end; by highs it does not. Both highs
are cheap folds, so a round 4 over this group is not obviously earned by volume — but the fold that
closes H1 and H2 changes criteria in units 8, 9 and 13, and that fold's own text is unreviewed
surface, which the closing diff review should take as its index.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero here is
evidence and not the artefact of a missing lens: a "no confirmed finding" below means four lenses and
a skeptic stage found nothing, which is evidence and not proof. One group of two ids, 12 and 26,
describes one defect and is merged into H1; the pipeline's duplicate count of 0 comes from its own
exact-match dedupe, which does not see a restatement.

## Review shape

Raw 31, confirmed 11, refuted 20, unverified 0. Precision 0.35, which is below the ~0.5 floor section
8 of the charter sets: a round 4 over this group should tighten lens priming or narrow scope before
it adds agents. Precision fell from round 2's 0.66, which is the expected direction over a surface
that has now been audited twice — the cheap defects are gone and the lenses spend more of their fan
on text that holds. The 20 refuted findings are not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 2 | 3 |
| MEDIUM | 4 | 4 |
| LOW | 4 | 4 |
| Total | 10 | 11 |

**Severity is adjudicated here, not copied from the finders**, on the scale rounds 1 and 2 used.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written for a reason visible only across specs,
  or it ships a layer that stays inert while its suite reads green.
- MEDIUM covers three kinds: a contradiction between specs with a bounded or visible consequence; a
  declaration whose absence reds a leg at the post-build bar; a claimed mechanism that does not exist.
- LOW is a rule whose break no criterion can see, where the reachable harm is small.

Two findings move against their finder's label. Ids 12 and 26 were both filed high and are merged
into one HIGH item rather than counted as two defects. Id 30 was filed low and stays LOW; its impact
argument overstated the drift by one row, corrected in the entry.

Three observations about the confirmed set.

- **The fold-text share has fallen sharply.** Round 2 put 35 of 37 ids in round-1 fold text. This
  round the split is 6 to 5: ids 1, 9, 12, 16, 17 and 26 sit in text a section 9 line dated after the
  round-2 record introduced, and ids 3, 8, 13, 19 and 30 sit in text that was already there at the
  round-2 blob and that no prior round named. Each provenance claim was checked by reading the
  round-2 blob directly with `git cat-file -p`. This is what convergence looks like in this build:
  the fold is no longer the dominant defect source, and the residue is old text the earlier lenses
  walked past.
- **The deferral rule is the new cluster.** H1 (12, 26) and L3 (17) are one mechanism seen twice —
  RUN.md's ratified "(a) every attributed suite runs once at VERIFYING, after the last unit" applied
  to criteria whose subject is THIS tree, which unit 34 changes out from under them. Every criterion
  in this build that carries a permission line and names "this tree" is in that class, and only these
  two were caught here. A sweep over the whole spec set for that pair of phrases is the cheapest way
  to find the rest.
- **The criterion-gap class persists, smaller.** M2, M3, M4 and L1 are each a declared behaviour with
  no criterion that reads it, the class
  `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` records. Round 2 found ten
  such ids; this round finds four.

## Round-2 fixes: what this round found against them

All four lenses returned, so "no confirmed finding" here means the fix survived a complete pass. It
does not certify the fix.

| Round 2 | Spec | Round-3 reading | Round-3 entries |
|---|---|---|---|
| M1 | 11, 12 | no confirmed finding | none |
| M2, M3, M4 | 34 | unit 34 is G5's subject; not graded here | none |
| M5 | 9 | no confirmed finding against the restated edge | none |
| M6 | 9, 13 | no confirmed finding | none |
| M7 | 9 | holds: S11 pins the interim ceiling and its basis; the same class is still open in unit 10 | M1 |
| M8 | 11 | no confirmed finding | none |
| M9 | 13 | no confirmed finding | none |
| M10 | 13 | holds for the four carriers it named; a fifth carrier was never in scope | L4 |
| M11, M12, M13 | 9, 11, various | no confirmed finding | none |
| L1 | 12 | partial: the fold added the exit-1 half and left the exit-0 half unobserved | L1 |
| L2, L3 | 12, 13 | no confirmed finding | none |
| L4, L5 | 13 | holds: the guard and the ceiling basis both landed | none |
| L6 | 10 | holds for the mutation sweep; the fold's new section 7 field contradicts S8 | L2 |
| L7, L8 | 8, 6 | no confirmed finding | none |
| L9 | 7, 11 | holds: unit 11 AC7 now reads the prospective view size; the census item added beside it is unobserved | M2 |

Unit 6 carries no confirmed finding at all this round, from a full four-lens fan. That is the
strongest reading any subject in this group has had, and it is worth saying plainly, because unit 6
was the round-1 and round-2 workhorse.

## High

### H1 — unit 8's only darkness proof is deferred to a moment at which neither thing it compares still exists (12, 26)

**Where.** Unit 8 section 6 AC10 and its permission line, against unit 8 section 2 S10, unit 9
section 2 S6 and S7, and unit 34 section 2 S1, S4 and S6.

AC10 compares the BASE hygiene engine and this unit's engine over THIS REPO and requires the two
outputs to be byte-identical. Its permission line reads: "both runs are the `memory hygiene` leg's
command, which no pass runs (build method M6), so the pass returns the comparison to the main loop,
which makes it once after the last unit is terminal."

**Verified.** Three legs, each read at the blob pinned above.

- Unit 8 S10 scopes the property to "before and after THE UNIT" — "the engine's full output over this
  repo is identical before and after the unit, finding for finding and line for line". The permission
  line moves the single observation to after the LAST unit. Those are different moments and the spec
  states both.
- Unit 9 (order 9, after this unit) S6 puts check 25 in `check-memory-hygiene.sh` when not `--staged`,
  which is exactly AC10's invocation, and S7 requires that on a shards-mode HEAD it "prints that it is
  dormant and why", every line prefixed `memory-hygiene: check 25 `. AC10's own Red-when names that
  signature: "any builds-mode branch runs under `shards`, including a new announcement line". So by
  the deferral moment the comparison must red, for a change unit 8 did not make.
- Unit 34 (order 34) S4 declares `BACKLOG_MODE="builds"` in `.memory-tree.conf`, S1 removes the
  authored shard files after the conservation proof, and S6 deletes the three backlog archives. So at
  the deferral moment "over this repo" is not a shards tree at all, and the BASE engine has no shards
  subject left to grade.

Unit 8 mentions check 25 nowhere, and the permission line pins neither the engine version nor the
tree state. Whoever executes it at VERIFYING reads a red that is unit 9's by design, and either
waives AC10 or edits unit 9. Either way S10 — the unit's whole darkness guarantee, the one thing
proving an adopter on shards sees nothing until it switches — is observable nowhere in the build.

The asymmetry is real and worth naming: the sibling dark proofs stay in their own passes. Unit 6
AC12 and unit 7 AC13 both read "on this tree after the unit" and are unaffected. Unit 8 is the one
that moved.

**Fix.** Pin the comparison to two blobs and a shards-mode tree rather than to a moment. State in
AC10 that the main loop checks out this unit's parent commit and this unit's own commit, runs the
engine of each over a scratch checkout of this repo at that commit, and compares — so no later unit
of this build can enter the comparison. The alternative, equally acceptable, is to keep the run
inside unit 8's own pass over the still-shards tree and record in the permission line why that one
real-tree run is admitted against build method M6. Either way, add a sentence to S10 naming unit 9's
check 25 lines as text this comparison must not see, so the next fold does not re-defer it.

**Left-shift gate.** A spec-lint arm over `memory/builds/*/spec/` that reds when a criterion's text
names "this tree" or "this repo" AND its permission line defers the run past the unit's own pass,
unless the line also pins a sha or a scratch checkout. Run the predicate over the corpus first and
print hits and near-misses: it should hit unit 8 AC10 and unit 9 AC5 (L3 below) and miss unit 6 AC12
and unit 7 AC13, which name the unit's own tree state. The deeper form is the rule the charter
already states — a check whose subject a later step mutates is not a check, it is a schedule.

### H2 — unit 9's delta watches the whole archive directory, so a routine decision-log rotation reds check 25 on every node (19)

**Where.** Unit 9 section 2 S3 and S4, with section 4 "The walk, and what it costs" step 5.

S3's transition predicate and S4's delta both watch `<MEMORY_ROOT>/backlog/` and
`<MEMORY_ROOT>/archive/`, the second as a whole directory, and section 4 step 5 runs one
`git log --name-only` over those two paths. `memory/DECISIONS.md` is in neither.

**Measured at HEAD.** `.memory-tree.conf:429` declares `ROTATION_MODE="cut"`, so rotating the
decision log writes a new `memory/archive/DECISIONS.<date>.md` — a routine, sanctioned action on any
node. Running the real `extract.anchor_at` over the existing
`memory/archive/DECISIONS.2026-08-10.md` returns 79 anchored ids; the same function over a charter
snapshot in that directory returns 0. Those 79 ids have no watched-file version at the merge base, so
on a shards-mode straggler they read as NEW rows: S4 emits one delta entry per id, S5 finds none
accounted, and check 25 reds naming decision ids. The only remedy check 25 prints is a
`- RELOCATED · <id> · by <sha> · kept|dropped|amended: why` row in some `BACKLOG.md`. Handed to unit
12, the classification table's first row files each of those as an ask in `builds/<slug(id)>/BACKLOG.md`.

The build already knows the rule and applies it everywhere else. `row_grammar.row_docs` refuses the
broad reading in its own docstring — not "every `.md` under `archive/`", because that sweeps in the
frozen charter snapshots and the retired ledger shards. Unit 13 S1 narrows HAS-DELTA to "backlog
shards or a family-named backlog archive", and unit 13 section 4 and AC3 spell the reason, that a
decision-log rotation on a pre-flip branch has nothing to relocate, with an arm that reds if HAS-DELTA
"reads unit 9's whole archive directory". So the divergence is recorded, deliberately, in unit 13 —
and its consequence for unit 9 is recorded nowhere. Unit 9 has no such arm, no narrowing, and no open
question covering it.

**Fix.** Scope the archive half of S3's predicate and S4's delta to the family-named rotated
archives — the family alternation of `check-memory-hygiene.sh --print-rotated-archive-ere`, which is
the population `row_grammar.row_docs` and unit 13 section 8 F4 already use. State in section 4 Data
model that the decision log, its archives, the retired ledger shards and the charter snapshots are
outside the delta, and say why, so the next reader does not widen it back.

**Left-shift gate.** A new arm in `transition-audit.test.sh`: a fixture straggler that rotates its
decision log across a transition merge yields zero delta entries. Observe it RED first with the
archive selector widened to the whole directory — that staged break is the whole point, since a
zero-entry assertion over a fixture with no decision log passes for the wrong reason. The class-level
form is a predicate that reds whenever a kit module selects files under `<MEMORY_ROOT>/archive/` by
directory rather than through the rotated-archive ERE the kit already publishes.

## Medium

### M1 — unit 10's new leg declares no ceiling, which reds the gov canary on the first bar after the unit (13)

**Where.** Unit 10 section 2 S6 and section 6 AC8; section 4 Inventory; section 7.

S6 declares the `row-driver view refusal` leg with chunk `declarations`, subject `repo` and no
guard. No section of the spec declares a `ceiling` for it: the sole `ceiling` hit in the whole file
is an unrelated line about unit 8's cost exception. AC8 reads the subject, the chunk, the guard, the
dossier claim, the `[[exempt_leg]]` row and govkit selfcheck, and never the ceiling row.

**Verified at HEAD.** `tools/run-gates/run-gates.gov.test.sh:261` appends "%s declares no ceiling, so
it runs unbounded and a hang in it wedges the bar" for any leg row lacking the key, and exits 1. All
106 rows in `tools/gate-legs.json` carry a ceiling today — 106 of 106, derived by reading the file,
not counted in prose. So the leg as specified lands red on the `run-gates gov canary` leg at the
`GATE_SELFTESTS=1` bar.

This is the same class the build has already fixed twice, which is what makes it a MEDIUM rather than
a note. Unit 9 S11 pins an interim 900 s with its basis, the `memory-hygiene self-test` sibling, and
its AC10 Red-when spells the exact failure ("the leg declares no ceiling, which the `run-gates gov
canary` leg reds under `GATE_SELFTESTS=1`"). Unit 13 S8 pins its own the same way and lists `leg
ceilings clear their evidenced maximum` in section 7. Unit 10 does neither.

**Fix.** S6 declares an interim `ceiling` in `tools/gate-legs.json` with its basis — a named sibling
`declarations`/`repo` leg — re-declared from the post-build bar's first reading as
`tools/run-gates/ceiling-margin.txt` sizes it via `derive-ceilings.py --write`, in the same words unit
9 S11 and unit 13 S8 use. AC8 reads the ceiling row back. Section 7 gains `leg ceilings clear their
evidenced maximum`.

**Left-shift gate.** A spec-lint join over `memory/builds/*/spec/`: every spec that introduces a new
row in `tools/gate-legs.json` must name a `ceiling` for it in section 2 and read it back in one
criterion. The mechanical half already exists at the tree level as block G6, so the spec-side arm is
the same predicate one level up — "gate the CLASS, not the instance" applied to the spec corpus, and
the third instance of this class in three rounds argues for it.

### M2 — unit 11's census derives an archive-citation figure that no criterion observes, and cites three that do not (1)

**Where.** Unit 11 section 2 S3, against section 6 AC1, AC2 and AC7.

S3's last derived item is "the rows whose text cites a backlog archive by path", cited to AC1, AC2
and AC7. None of the three reads it. AC1 grades copy choice, the wrapped-row join and the
unreadable-line refusal. AC2 grades the two-live-copies blocker. AC7 grades the oversized slug, the
README-less filing homes and the prospective view sizes. No other criterion reads it either: AC8
grades record naming, Serves lines and byte-identity; AC9 grades exit 0, the summary and a clean tree.
The nearest thing to coverage, AC6's per-normalization count, is a different output and S3 does not
cite it.

**Why it matters beyond a mis-citation.** The spec makes the figure load-bearing in its own words:
section 3's hands-off to unit 34 names "the size, filing-home and archive-citation findings its commit
must absorb". Unit 34 section 4's fifth normalization rewrites exactly those citations. So the
population nobody measured is the population unit 34 is told to rewrite, and after ruling D8 deletes
the family archives each unrewritten citation is a dead backticked path that check 15 reds on the
switch-over's first run (unit 8 S7). The impact is softer than it first reads, because unit 34
section 4 normalization 5 says the writer "derives the population at flip time rather than trusting
this count" — but a declared census output that another unit's hands-off names can today be absent
entirely with every criterion green, and that is the defect.

**Provenance.** This text is not in the round-2 blob `274830...`. The round-2 L9 fold, which added
the prospective view-size derivation and AC7's clause reading it, added this item beside it and gave
it no criterion.

**Fix.** Extend AC7 with a fixture ask row whose text backticks a family-archive path: the census
names that row with its file and line, and the count appears in the census summary. Add the Red-when
the finding names — the archive-citation finding is omitted while the size and filing-home findings
still print, which no other criterion can see.

**Left-shift gate.** A spec-lint arm that parses each section 2 item's "Observed by AC*n*" list and
reds when the named criteria's text does not mention the item's own derived output. It will not be
exact, so run it as printed near-misses rather than a red at first, over the whole spec corpus: this
is the third round in which "cited to a criterion that does not read it" has produced confirmed
findings, and the pattern is mechanically visible.

### M3 — unit 7's `--asks --status` filter is declared and exercised by no criterion anywhere in the set (3)

**Where.** Unit 7 section 2 S12, against section 6 AC11 and AC17.

S12 declares `--asks [FAMILY|ID] [--all] [--status <token>] [--build <slug>] [--json]` and cites
AC11 and AC17. AC11 runs `--asks EXMP-aFoo-3`, `--asks TOOL --all --json` and `--asks --build aFoo`.
AC17 runs `--asks TOOL --all --json` only. Neither runs the `--status` filter, and no Red-when
mentions it.

**Verified across the set.** Grepping every spec for `--status`: every other hit is the unattended
kit's unrelated `--status` mode (units 4, 16, 20, 22, 27, 28, 29, 30) or unit 7's own OUT line about
the derived-terminal unit's `--status`. No sibling exercises this filter. So the option can ship
unimplemented, can filter on the legacy token instead of the derived one, or can silently accept an
unknown token, and both cited criteria stay green. This is the one print mode that answers "what is
BLOCKED right now" without a full table, which is what makes the silent-accept case the dangerous
one: an unknown token printing zero rows at exit 0 reads as "nothing is blocked".

This text was already present at the round-2 blob `076b3b...`, so it is not fold damage — it is
surface two prior rounds walked past.

**Fix.** Add to AC11 a `--asks TOOL --status BLOCKED` run over a fixture holding one BLOCKED and one
OPEN ask: only the BLOCKED row prints, the exit is 0, and an unrecognised token refuses by name
rather than printing an empty set. The Red-when writes itself — an unknown token prints zero rows at
exit 0.

**Left-shift gate.** A spec-lint arm that extracts every long option from a section 2 CLI synopsis
and reds when the option string appears in no criterion in the same spec. Run it over the corpus and
print hits and near-misses first: it will find more than this one, and each hit is either a missing
criterion or an option that should not be in the synopsis.

### M4 — unit 13's "does nothing when the library is absent" is asserted for every adopter and observed by nobody (8)

**Where.** Unit 13 section 2 S4, against section 6 AC4, AC5 and AC7.

S4's closing sentence is "The block does nothing when the library is absent. Observed by AC4 and
AC5." AC4 pushes a PRE-FLIP feature branch with the library present. AC5's removal arm removes the
AUDIT MODULE — its words are "with the audit module removed from both trees" — not
`straggler-guard.sh`. AC7 is the FLIPPED-false case, library still present. No criterion runs any
hook with the library absent.

**Verified at HEAD.** Section 3 does not withhold this as a non-goal; it positively asserts it —
".githooks/pre-push ships verbatim through the push-main kit, so its new block is inert wherever the
library is absent" — and `tools/govkit/entries/push-main.kit.toml` confirms `.githooks/pre-push` is
shipped verbatim to every adopter while the library is gov-only. Section 4's design paragraph on
resolving the audit pins a skip line for an unresolvable module and says nothing about an absent
library. So a block that sources the library unguarded, or runs its predicates with the library's
functions undefined, reds no criterion here and refuses every push in every adopter that took the kit
and not the gov-only library. The unobserved path is every adopter's push, not a corner case.

**Fix.** Add a criterion, or a case on AC7, that pushes from a fixture whose `.githooks/` holds the
new `pre-push` and no `straggler-guard.sh`: the push lands, the block prints nothing, and the hook's
exit is the one it had at BASE. Red when the missing library aborts the hook. It is one clause on an
existing criterion.

**Left-shift gate.** The durable form belongs in the shipped-surface leg rather than in this spec: an
arm in `install-prefix (shipped surface)` that, for each file a kit ships verbatim, runs it in a
fixture holding only that kit's own shipped files and asserts the exit is unchanged. That reds any
future verbatim-shipped hook that reaches for a gov-only helper, which is the class rather than this
instance.

## Low

### L1 — unit 12's dry run has two exit halves and the fold observed only one (9)

**Where.** Unit 12 section 2 S9, against section 6 AC7 and AC14.

S9 says the dry run "exits 0 only when the plan would write", which is two assertions, and cites AC7
and AC14. AC7 asserts that the plan and the table print and `git status --porcelain` is unchanged —
no exit status at all. AC14's dry run exits 1 with a NEEDS-HUMAN entry standing; its second half,
"with the amendment removed and `--confirm`… it writes", is a WRITE run, not a dry run. So neither the
clean-plan exit 0 nor the empty-plan non-zero is observed.

Round 2's L1 named this rule. The fold answered it by adding the cutoff clause and the AC14 citation,
which covers the exit-1 half; the zero half is still unobserved. Grepping the set, only unit 34 and
DEPL-1 use `--dry-run`, both as consumers: unit 34's landing reconcile step 4 re-runs without
`--dry-run` only when the dry run did not exit 1, and DEPL-1's adopter runbook does the same. A
constant exit therefore reads as a park condition and stalls the routine landing at its ingest step
with nothing red anywhere.

**Fix.** Assert in AC7 that a dry run over a plan holding no NEEDS-HUMAN entry and no unconfirmed
status change exits 0, and that a dry run whose plan would write nothing exits non-zero naming the
empty plan. Red when the exit is constant, so unit 34 step 4 cannot tell the two cases apart.

**Left-shift gate.** In the relocation selftest, a control arm that asserts the three dry-run exits
are not all equal — the cheap mutation-style check that catches a constant return, which no
per-case assertion can see. Stage the constant and observe it RED before wiring it.

### L2 — unit 10's S8 and its new section 7 field describe two different suites, and only one can be built (16)

**Where.** Unit 10 section 2 S8, against section 7's `New arm:` third field and section 6 AC1 and AC3.

S8 says the replay arms are "each driven through a real `git merge` in a scratch repository with the
driver wired". Section 9's closing consolidation, which produced the new section 7 field, says the
opposite for two of them: "the arms of AC1 and AC3, which drive the driver through `run`, move it",
while "the arms of AC2, AC4, AC5 and AC10 are git merges over a fixture repository rather than `run`
cases". AC1 ("drives a three-way") and AC3 (the unimportable-predicate case) read as direct calls,
and AC2 alone carries the `fixture:` line naming `git config merge.rows.driver`.

**Verified against the suite at HEAD.** `run()` at `tools/memory-tree/merge-rows.test.sh:136` invokes
the driver directly with four positional arguments — a `run` case is not a git merge — and line 1598
floors `nruns`, the executed-`run` population, at 40. So following S8, AC1 and AC3 become git-merge
fixtures, no `run` case is added, and the floor the new third field promises to raise "by the
executing cases these arms add" moves by zero: the field then names a floor nothing touches. Following
section 7, S8 is false for two of its own arms. The two statements cannot both be built.

S8 itself is unchanged since the round-2 blob; the contradiction is new, created by the field the fold
added.

**Fix.** S8 distinguishes the two arm shapes explicitly: direct three-way `run` invocations for the
view-against-shard refusal and the unimportable-predicate case, and real `git merge` fixtures with the
driver wired for the three merge shapes, the two `BACKLOG.md` concurrency pairs and the two
re-rendered views.

**Left-shift gate.** None worth building for this instance — it is one sentence against another inside
one file. The generalisable half is already this build's own rule, which unit 10 section 9 states
better than a lint could: a section 7 field that names a floor must name which added cases move it,
and a field that moves no floor returns to `none`.

### L3 — unit 9's before-the-flip observation is deferred to after the flip (17)

**Where.** Unit 9 section 6 AC5 and its permission line.

AC5's first half reads "When `bash tools/memory-tree/check-memory-hygiene.sh` runs on this tree before
the flip, it prints check 25's dormant line and exits 0 on that account", and its permission line
defers that run to "the one post-build bar".

**Verified.** Unit 34 S4 sets `BACKLOG_MODE="builds"` on this tree, unit 34 is order 34 against unit
9's order 9, and RUN.md records the ratified rule that every deferred run happens once at VERIFYING
after the last unit. So at the one post-build bar this tree is in builds mode, where check 25 prints
the liveness line and not the dormant one, and the deferred half grades something the criterion does
not describe. What survives in the pass is the by-hand shards-mode scratch fixture, which is
explicitly not "this tree" and so does not answer AC5's own Red-when — "the dormant branch prints
nothing, which reads exactly as a clean audit" — for this repository. Unit 9's rev-5 entry made the
deferral and did not reconcile it against unit 34's flip.

This is H1's mechanism at lower stakes, which is why it is LOW: a real observation of the dormant
branch does survive, on a fixture. Fold both in one pass.

**Fix.** Have AC5 state that the real-tree dormant observation is made during unit 9's own pass, while
this tree is still shards-mode, and reserve the post-build bar for the run's exit code. Or drop the
real-tree half, make the shards-mode scratch fixture the whole criterion, and say so.

**Left-shift gate.** The H1 arm covers this one too — the same spec-lint predicate over "this tree"
plus an unpinned deferral. Build it once.

### L4 — the drift-audit kit's signals table is never updated, so the kit documents itself short (30)

**Where.** Unit 13 section 2 S6, section 4 Files touched, and section 5 user docs.

S6 adds the `backlog_stragglers` drift signal. Section 4 Files touched names
`tools/drift-audit/README.md` only among "the other drift-audit version carriers (S11)", the
`gov:kit drift-audit@` marker. Section 5 user docs names the recipe those layers print, and hands the
memory-tree README to unit 36, which covers `tools/memory-tree/README.md` only. So the kit README's
`## The signals` table at `tools/drift-audit/README.md:103-117` — the reader-facing enumeration, one
row per signal — is never touched.

**Verified at HEAD.** That table is hand-kept: no gate binds it, `drift_report.py` and `selftest.py`
never read it, and the only tooling that reads that README at all is `check-kit-versions.sh`, which
reads the version marker alone. The gap is already live at BASE, which demonstrates the drift rather
than excusing it — `backlog_rows_outliving_closed_specs` is implemented at `drift_report.py:1633` and
registered at `drift_signals.py:260`, and it is absent from the table. Unit 34 S10 adds three more
signals and retires one, and names that README nowhere. The only other unit touching it, unit 21,
scopes its edit to the base ladder.

**One correction to the finding's arithmetic.** The retired signal is not in the table, so the drift
the build adds is four rows, not five: one from unit 13 and three from unit 34, on top of the one
already missing at BASE. Section 5's own rule is the standard being broken — a user-facing change
owes its page.

**Fix.** Name the README's `## The signals` table in section 4 Files touched as a content edit,
distinct from the S11 marker edit; add it to section 5 user docs; and extend AC8 or AC9 to read the
row back, so the doc edit has a criterion. Unit 34 owes the same for its three.

**Left-shift gate.** The right gate is not a spec-lint but a kit-level join, and it kills the class
including the row already missing at BASE: a `drift-audit selftest` arm that reads the first column of
the `## The signals` table and joins it against the implemented signal set in BOTH directions — a
signal with no row, and a row naming no signal. That is the same bidirectional shape check 22 already
uses for the unattended kit's section 8 key table, so the pattern is in the repo and proven.

**Serves:** spec-audit TOOL-dDerivedDocket-37

# dDerivedDocket — spec audit of topic group G6, the hands-off payload join, round 1

*Node `d`, 2026-09-16. A Tier-2 adversarial pass over the one spec of topic group G6. That spec is
unit 37, which adds a fourth population to `tools/check-spec-tokens.py`: every backticked payload
token of a `**hands-off**` edge bullet must occur in the text of the sibling spec the bullet names.
Unit 37 is not in the design record's roster. The run adopted it after the round-1 fold, under
section 11 of `memory/guides/UNATTENDED-PROTOCOL.md`. The adoption is recorded in the spec's own §1
and in `memory/builds/dDerivedDocket/RUN.md`'s rescope row at 2026-09-14T09:07:47Z. It followed a
probe that found three hands-off tokens a sibling never named: units 7, 10 and 13 handing units 11,
DEPL and 35. All three were fixed in those specs before unit 37 was written.*

*Four primed finder lenses ran, then a skeptic stage prompted to REFUTE each finding in five batches,
then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the protocol's section 11, `memory/guides/BUILD-METHOD.md` M3 and M4, and the build-pass brief
`memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md`. Five
questions were put to the spec. Is the join decidable? Is it correct against
`tools/check-spec-tokens.py` and `tools/check-spec-tokens.test.sh` at BASE? Is it consistent with
check 12's edge grammar in `tools/memory-tree/check-memory-hygiene.sh`? Do its measured claims
reproduce over the tracked specs at HEAD `282e0a6b`? Are its criteria observable?*

*Every high below was re-checked against source before it was written down, and the sites read are
named in each entry. Every tool, conf and guide cited is byte-identical between `abac6d59` and
`282e0a6b`. The only paths those commits touch outside this build's folder are `memory/LIVE.md`,
`memory/ledger/2026-09.md` and `memory/backlog/TOOL.md`. Other sessions were editing other specs of
this build while this report was written. Every measurement here therefore reads committed blobs at
`282e0a6b` through `git show`, never the working tree.*

**Round: 1.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-37.md@d011b3e16ad47b89f8309f6f36cb4949d7fd8013`

## Verdict: CLEAN WITH FIXES

No confirmed finding is adjudicated a blocker, so the verdict is CLEAN WITH FIXES by the blocker
count. The join itself holds up. Once its target lookup is re-keyed, it is decidable. It reuses the
checker's existing selection and waiver machinery correctly. The measurement behind its verb and
cutoff choices also reproduces. What does not hold up is the unit's evidence that the join works.
Three HIGH defects stand, carried by seven confirmed findings.

- **H1** (1, 10, 20, 32). AC7 names `tools/check-testsuite-counts.sh` as the witness that the floor
  rose. That leg runs nothing and compares no count, so AC7's own Red-when cannot fire. This is the
  third recorded instance of this class against this leg, and the second against this very suite.
- **H2** (9). `order 39` builds unit 37 last. By then, step 4 of the brief has closed every spec that
  carries a hands-off bullet. S6's real-tree pass and AC6 therefore grade zero bullets.
- **H3** (21, 31). The join finds its target with a filename glob one directory deep. Check 12
  resolves a unit by its H1 id at any depth, and the spec format allows family-less names, name tails
  and sub-folders. A later spec set that uses those legal forms gets every hands-off counted silent
  and none graded.

Three MEDIUM defects are carried by four findings.

- **M1**: a function name whose verb is not declared, which reds the lexicon leg's equality pin.
- **M2**: S6 and §5 tell a session to grow a shrink-only registry.
- **M3**: a new conf key with no decision about the shipped example carrier.

Three LOW defects are carried by four findings.

Every defect is in the document this round read, so the disposition M4 prescribes is FOLD for all of
them. Two folds should be decided rather than folded silently, and each takes a §9 line.

- H2's route: move the unit ahead of every unit whose spec carries a hands-off bullet, or pin S6 and
  AC6 to a named sha where those specs are live.
- M3's route: add the key, blank, to the shipped example, or take TOOL-aJoinedCanon-7's declared
  exception and say why the aJoinedCanon closing review's F2 does not reach this key.

M4's loop re-arms only on a blocker count, so round 2 is not owed. The folded text is still
unreviewed surface (`memory/gotchas/fold-text-is-unreviewed-surface.md`). H3's fold rewrites the
join's identity key, and that is the one fold this report recommends re-reading before unit 37
builds.

Review shape: raw 37, confirmed 15, refuted 22, unverified 0, precision 0.41. That precision is below
the ~0.5 floor `AGENTS.md` §8 sets, and the review-shape section says what that implies. The run
integrity section below reads complete.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero. The finding set is therefore complete for
what the four lenses were primed to hunt. That is not a claim that unit 37 holds no other defect. It
is a claim that nothing was lost between the lenses and this page. The pipeline's duplicate count of
0 comes from its own exact-match dedupe. On reading, four groups of confirmed findings each describe
one defect from several lenses: 1/10/20/32, 21/31, 11/19 and 15/35. Each group is folded into one
entry below, and every count on this page stays per finding id.

## Review shape

Raw 37, confirmed 15, refuted 22, unverified 0, precision 0.41. The 15 confirmed ids collapse to 9
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 7 | 3 |
| MEDIUM | 4 | 3 |
| LOW | 4 | 3 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 to G5
reports used, so the six groups' counts compare.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert or broken while its suite reads green. In each case the fold is local to
  one or two specs, or needs one decision.
- MEDIUM covers three things: a contradiction with a bounded consequence, a declaration a spec owes,
  and a rule whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small. Having no live instance today
  does not by itself make a defect LOW: H3 has none, and it disables the unit's purpose for a legal
  input class.

Against the finders' ratings, three findings move.

- **Up to HIGH: 32**, from medium. It is the same defect as 1, 10 and 20. The class has twice been
  adjudicated HIGH against this same leg: `TOOL-aLoosenedCeiling-1`'s review, finding 5, and
  `TOOL-aJoinedCanon-1`'s spec audit round 2, H7.
- **Up to HIGH: 31**, from medium. It is the same defect as 21. Built as specified, the join fails
  open over any later build whose specs use a legal name form, and that is the unit's whole stated
  purpose.
- **Down to MEDIUM: 19**, from high. It is the same defect as 11. G5 round 1's M7 put this class at
  MEDIUM: a declaration or name that reds a leg at the post-build bar, with a one-line fold.

**Precision 0.41 is the lowest of this build's nine audit runs.** The others were G1 0.56 and 0.63,
G2 0.57 and 0.66, G3 0.64, G4 0.53, and G5 0.75 and 0.61. `AGENTS.md` §8 says to tighten scope and
priming before adding agents below ~0.5, and to match intensity to the richness of the target. Four
lenses ran over one 262-line spec and returned 37 raw findings. Even the 15 survivors carry 9 distinct
defects, so more than a third of them are repeats. This report infers that the fan was too wide for a
single small subject: a one-spec group should take two or three lenses. The refuted set was not
re-read for this report, so that inference rests on the counts alone.

**The dominant class is again `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`.**
Findings 1, 10, 20 and 32 are that class outright. Finding 9 is its population form: a criterion
whose command runs, over a population the build will have emptied by the time it runs. That makes 5
of the 15.

## Findings index

| Id | Severity | Entry | Address |
|---:|---|---|---|
| 1 | HIGH | H1 | §6 AC7; §2 S8; §7 `New arm:` rows |
| 10 | HIGH | H1 | §6 AC7; §7 Gates |
| 20 | HIGH | H1 | §6 AC7; §2 S8 |
| 32 | HIGH | H1 | §6 AC7 |
| 9 | HIGH | H2 | status header `order 39`; §2 S6; §6 AC6 |
| 21 | HIGH | H3 | §4 The selection; §2 S2 and S5 |
| 31 | HIGH | H3 | §4 The selection; §2 S2 |
| 11 | MEDIUM | M1 | §4 Inventory; §7 Gates |
| 19 | MEDIUM | M1 | §4 Inventory; §7 Gates |
| 29 | MEDIUM | M2 | §2 S6; §5 risks; §4 Files touched |
| 30 | MEDIUM | M3 | §2 S3; §4 Files touched |
| 33 | LOW | L1 | §7 `New arm:` rows; §2 S8 |
| 15 | LOW | L2 | §3 Consumes-from bullets; §8 F2, against §8 F1 |
| 35 | LOW | L2 | §3 Consumes-from bullets; §8 F2 |
| 34 | LOW | L3 | §4 The selection; §2 S1 |

The one spec path is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-37.md`.
Every section sign and bare line number below refers to it at blob `d011b3e1`.

## Blockers

None. No finder rated a finding BLOCKER, and none is adjudicated one here. The nearest is H2. Its
fold is a reorder that the spec's own Edges value, `none`, already permits, so it needs no mechanism
the set lacks.

## High

### H1 — AC7's witness runs nothing, so the floor can stay at 20 while arms land (1, 10, 20, 32)

**Where.** §6 AC7 (`:199-203`), §2 S8 (`:64-65`) and §7's five `New arm:` rows (`:213-217`). Read
against `tools/check-testsuite-counts.sh:22` and its `compliant()` at `:66-78`, and
`tools/check-spec-tokens.test.sh:15` and `:195-202`.

**Defect.** AC7 says that `bash tools/check-testsuite-counts.sh` "reports the spec-tokens suite's
printed count at or above its `FLOOR_ASSERTIONS` pin". It also says the pin "equals the arm count
before this unit plus the arms it adds". The leg can observe neither. Its header says "IT RUNS
NOTHING". Its usage line says "silent + exit 0 = good", and it ran silent with exit 0 on this tree.
`compliant()` makes three `grep -qE` checks and nothing else.

- The file carries a `PASS ($n assertions)` echo in the agreed shape.
- The file pins a non-zero `^FLOOR_ASSERTIONS=[0-9]+$`.
- The file references `$FLOOR_ASSERTIONS` somewhere.

It never executes the suite, never reads the pin's value, and never compares that value with a count.
The suite's own runtime check, at `tools/check-spec-tokens.test.sh:196`, is
`[ "$total" -lt "$FLOOR_ASSERTIONS" ]`. That fails only when the pin sits ABOVE the executed count.

**Impact.** AC7's Red-when reads "arms land without raising the pin". Suppose the pin stays at 20
while this unit's arms land. The suite executes about 30 assertions, passes its own floor test and
prints `PASS`, and the testsuite-counts leg stays silent. No command AC7 names can go red on its own
Red-when. S8's increment cannot be counted either. The suite runs one assertion per `arm` call, with
20 calls against a pin of 20 at BASE. §7 lists five `New arm:` rows, but AC1 to AC5 describe ten or
eleven separate observations: a red and a green in AC1, two cases each in AC3 and AC4, and three in
AC5. A pin of 25 would therefore leave five or six of this unit's assertions deletable with every
leg green.

**Fix.**

- Re-witness AC7 with the suite's own output at the post-build `GATE_SELFTESTS=1` bar: its
  `PASS (<n> assertions)` line.
- Add a static check that the `FLOOR_ASSERTIONS=` value in `tools/check-spec-tokens.test.sh` equals
  `grep -c '^arm "' tools/check-spec-tokens.test.sh` on the post-build tree, and that both equal that
  printed n.
- State the move as a number once the arms are enumerated: 20 at BASE plus the exact count of `arm`
  calls this unit adds.
- Give AC7 the `permission:` line AC1 carries, deferring it to that bar.
- Keep `testsuite counts (every bar self-test prints one)` in §7 as the shape witness only, and say
  so. L1's fold, which fills the `New arm:` floor fields, belongs in the same edit.

**Left-shift.** This is the third instance of one miscited witness, after `TOOL-aLoosenedCeiling-1`
finding 5 and `TOOL-aJoinedCanon-1` spec-audit round 2 H7. Round 2 H7's proposed class gate never
landed: make `compliant()` require a comparison that reds when the pin and the executed count
disagree in either direction. Until a backlog row owns that gate, add a line naming this leg to
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, which today does not mention
it. The line: `check-testsuite-counts.sh` asserts shape and never a count, so a criterion about a
floor's value observes the suite itself. Class item 1 below.

### H2 — built last, the unit grades a population its own build has already closed (9)

**Where.** The status header's `order 39` (`:3`), §2 S6 (`:55-59`) and §6 AC6 (`:193-198`). Read
against step 4 of the build brief's "Before the commit", the checker's LIVE regex at
`tools/check-spec-tokens.py:64`, the `order` values in this build's status headers at `282e0a6b`, and
§8 F3.

**Defect.** The checker's LIVE regex admits OPEN, SPECCED, INPROGRESS and BLOCKED. Step 4 of the
brief has every pass set its own spec to `CLOSED` in the same commit as its code. The build's orders
run to PLAY at 37, DEPL at 38 and unit 37 at 39, so unit 37 builds last. The population at HEAD was
measured with S1's own selection: 107 hands-off bullets, 128 payload tokens, 0 silent and 0 hits. All
107 bullets sit in this build's specs, and no live spec in any other build carries one, as F3 says.
Unit 37's own Edges block is `none`. At unit 37's commit, then, no live spec carries a hands-off
bullet. S6's `--list` grades nothing, and its clause "a hit in a live spec of this build is fixed in
that spec" has no spec to reach. AC6's `figure:` line records that "specs close as the build
proceeds". It does not record that the population reaches zero at the unit's own position.

**Impact.**

- The arm lands without once grading a real bullet. Its only graded inputs are fixtures the builder
  wrote, the population-of-none shape of `memory/gotchas/vacuous-selector-empty-population.md`.
- The post-build bar grades zero as well, whatever the order, because every spec of this build is
  CLOSED by then.
- AC6's Red-when half "a live hit remains unfixed and unwaived" cannot fire. Its other half, a key
  that is misspelled or blank, still can, so the criterion is not wholly dead.
- §1 motivates the unit with this build's own corpus, and the unit never grades that corpus.

**Fix.** Two routes. Decide between them and record the choice in a §9 line.

- **(a) Reorder.** Give unit 37 an `order` ahead of every unit whose spec carries a hands-off bullet.
  Its Edges block is `none`, so check 12's order arm has nothing to compare. S6 and AC6 then grade
  the bullets live at unit 37's commit, and AC6 requires the graded bullet count to be above zero,
  derived at observation. The §9 line should also say what grading happens after that. Units run no
  gate legs, and the post-build bar grades zero. A later pass's rev bump that breaks a hands-off
  token is therefore graded only where a pass runs `python tools/check-spec-tokens.py`, which the
  brief already lists as a checker a pass may run.
- **(b) Pin a snapshot.** Keep `order 39`, and run S6 and AC6 in a scratch worktree at a named sha
  where the build's specs are live, `282e0a6b` for instance. Require a bullet count above zero there.
  This grades a snapshot, not the tree the unit lands on.

Route (a) grades what the build actually carries. Route (b) keeps the build order untouched.

**Left-shift.** A documented spec-audit check. A criterion that grades "the real tree" states its
population at the unit's own `order` position, derived from the statuses earlier passes will have
written, never at BASE. Its liveness half is the vacuous-selector rule: the criterion requires a
graded count above zero. Class item 2 below.

### H3 — the target is resolved by filename, where check 12 and the format key a unit by its H1 id (21, 31)

**Where.** §4 The selection, whose pseudocode reads
`target spec = memory/builds/<b>/spec/*-spec-<target>.md` (`:98`), §2 S2 (`:41-44`) and S5
(`:52-54`). Read against check 12's unit-id read at `tools/memory-tree/check-memory-hygiene.sh:1533-1534`
and its population registration at `:1586-1588`. Also read against `memory/TEMPLATE-SPEC.md:3-4` and
`:118-123`, the engine's `REC_TAIL='(-[a-z0-9][a-z0-9-]*)?'` at `:364`, and the checker's own spec
population regex at `tools/check-spec-tokens.py:168`, which is any depth.

**Defect.** The pseudocode finds the target with a glob one directory deep over
`-spec-<target>.md`. That works only when a spec's filename ends in its full `FAMILY-slug-seq` id
and sits directly under `spec/`, and the format requires neither.

- `memory/TEMPLATE-SPEC.md` scans specs "at any depth — sub-spec folders are scanned too".
- It makes the `-<FAMILY>-` qualifier optional.
- The hygiene engine admits a name tail.
- Check 12 takes a unit's id from its H1 line and registers every post-cutoff Tier-2 spec at any
  depth.

At `282e0a6b`, 19 of the 75 non-terminal specs, DEFERRED included, are not named
`<date>-spec-<H1 id>.md` directly under `spec/`. Counting only the 66 specs the checker's LIVE regex
admits, the figure is 12. Across all 621 tracked `*-spec-*` files, 183 are not in the plain one-deep
`<date>-spec-<FAMILY>-<slug>-<seq>.md` form, and 21 sit in a sub-folder. Two examples:

- `memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-11.md`, whose H1 is
  `TOOL-dScaffoldedMirror-11`;
- `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md`,
  whose H1 is `TOOL-aMendedLedger-2`.

Family-less names were used as recently as 2026-09-04 (the aSurfacedLexicon set) and on node `d` on
2026-08-25 (`dPromptedSeam-4`). S5's waiver key names a `<source id>` that the spec never defines for
such files either.

**Impact.** Take a later build whose specs use any of these legal forms. Every hands-off to a live
sibling is counted "silent (target not a live spec in the build)". Check 12's reciprocity join grades
those same edges correctly. The payload is never graded, S4's line gives the wrong reason for the
silence, and the leg stays green over the whole build. The unit's stated purpose, "a later spec set
gets the answer from the bar", fails open for that set. No live instance exists today: every live
hands-off bullet is in this build, whose specs use the plain form.

**Fix.** Resolve both ids the way check 12 does. Read the H1 `# <UID> ` of every tracked spec under
`memory/builds/<b>/spec/` at any depth and build a per-build map from uid to file. Look the target up
in that map, and apply the LIVE test to the file it returns. Take the source id from the source
spec's H1, and say so in S5. Add a `tools/check-spec-tokens.test.sh` arm, next to AC3's, whose target
has a family-less, tailed filename in a `spec/units/` sub-folder. That bullet must be graded and must
red on a missing token, not be counted silent.

**Left-shift.** The new arm is the instance gate. The class is a join claiming to follow a sibling
check's grammar while keying identity differently. The documented check: a spec saying it follows
check 12 names check 12's identity key, the H1 uid, and its population, any depth. Class item 3
below.

## Medium

### M1 — `grade_handoffs` leads with an undeclared verb and reds the lexicon pin (11, 19)

**Where.** §4 Inventory (`:122-125`) and §7 Gates (`:209-211`). Read against `.lexicon.conf:165`,
`tools/lexicon/lexicon.py:2758-2768`, and the gate manifest's `lexicon naming predicates` row.

**Defect.** §4 Inventory names one function, "`grade_handoffs`, in the `py.function` cell, leading
with a declared verb". `grade` is not declared. Asked on this tree,
`python tools/lexicon/lexicon.py --suggest grade_handoffs --as py.function` answers that `grade` is not
in the declared table. It lists the declared verbs as add, arm, build, check, cmd, derive, extract,
init, load, main, measure, parse, print, read, remove, render, resolve, run, scan, seed, set, test and
write. Top-level `tools/*.py` files are in the lexicon's parser population: `--list` reports offenders
in `tools/settings-merge.py`, and already one in `tools/check-spec-tokens.test.sh`. The tree reads
`P1 verb graded=2111 offenders=983`. `VERB_OFFENDER_PIN="983"` is an equality in both directions, and
`lexicon.py` reds on a count above the pin as well as below it. The leg's guard includes `tools/`, and
§7 does not list it.

**Impact.** Built as named, the unit moves the offender count to 984 and reds
`lexicon naming predicates` at the one post-build bar. Neither the pre-commit hook nor any criterion
runs the lexicon, so nobody sees it before then. The same edit makes the adoption premise false. §1
says "nothing measured gets worse", and protocol section 11 condition 2 excludes any worsened pin.

**Fix.** Rename the function with a declared verb and confirm it with `--suggest`. `check_handoffs`
answers OK for `py.function` on this tree, and `scan_handoffs` fits a population walk. Add
`lexicon naming predicates` to §7.

**Left-shift.** The class is a §4 Inventory that names an identifier and its cell and asserts the
cell's verdict without asking. That is decidable. A spec-tokens join could run
`lexicon.py --suggest <name> --as <cell>` over every backticked identifier an Inventory line pairs
with a backticked cell, and red on a refusal. Run the predicate over the live corpus first, printing
hits and near-misses, before wiring it. Class item 4 below.

### M2 — S6 and §5 grow a registry that is recorded shrink-only (29)

**Where.** §2 S6 (`:57-59`), §5 risks (`:154-156`) and §4 Files touched (`:127-131`). Read against the
header of `memory/project/spec-token-waivers.txt`, the `memory/map/features/spec-tokens.md` dossier,
the OPEN row `TOOL-aKeyedAnnotation-9` in `memory/backlog/TOOL.md`, and protocol section 11 condition
2.

**Defect.** S6 says a hit in another build's live spec "takes a waiver row naming the build". §5 risks
says the merging session "fixes the bullet or waives the edge". The registry's header says:
"SHRINK-ONLY: the count may fall, never rise, so a new hit cannot be waived away quietly". The
dossier calls it the shrink-only exception registry and tells a writer to extend by shape, never by a
waiver row. `TOOL-aKeyedAnnotation-9` says absorbing a class there "is not available". The registry's
own rows show the rule being kept: the pass that added the two hook-path rows recorded that the net
count fell from 24 to 23. The registry holds 22 rows at `282e0a6b`.

**Impact.** A session following S6 or §5 raises a shrink-only count, and no gate enforces the header.
That breaks protocol section 11 condition 2, under which unit 37 was adopted. S6's foreign branch is
empty today, because no live spec outside this build carries a hands-off bullet. The §5 straggler
path is the real exposure.

**Fix.** Rewrite S6 and §5 risks so that a foreign or straggler hit is fixed at the source bullet or
at the target spec. A waiver row is allowed only when the same commit retires another row, so the
count does not rise. Cite the registry header and `TOOL-aKeyedAnnotation-9`. Delete "or waives the
edge". Keep the registry out of Files touched except under that offset rule.

**Left-shift.** Make the header a gate. `tools/check-spec-tokens.py` already reads the registry, so
it can compare the row count with a high-water pinned in that header and red on a rise. That turns a
comment into the shrink-only rule it claims to be, for every population the checker grades. Class
item 5 below.

### M3 — the new cutoff key has no decision about the shipped example carrier (30)

**Where.** §2 S3 (`:45-48`) and §4 Files touched (`:127-131`). Read against
`tools/memory-tree/.memory-tree.conf.example:130` and the aJoinedCanon closing diff review
(`memory/builds/aJoinedCanon/reviews/2026-09-07-review-TOOL-aJoinedCanon-1-diff-review-round1.md`, F2,
CONFIRMED and FIXED in `65913fd3`). Also read against the OPEN row `TOOL-aJoinedCanon-13`,
`TOOL-aJoinedCanon-7` §4, and unit 15's list of carriers in this build.

**Defect.** S3 writes `SPEC_HANDOFF_CUTOFF` into `.memory-tree.conf` alone, "in the idiom of
`SPEC_LEGLINE_CUTOFF`". That idiom has two carriers. `SPEC_LEGLINE_CUTOFF` is also read only by
`tools/check-spec-tokens.py`, yet the shipped example carries it blank at `:130`. The aJoinedCanon
closing review's F2 added it there because "the build's own rule 3 requires both carriers". That
overrode the exception `TOOL-aJoinedCanon-7` §4 had declared. The same review filed
`TOOL-aJoinedCanon-13`, still OPEN, to widen the example-parity arm to every tool that reads
`.memory-tree.conf`. Unit 15 in this same build names both carriers for its key. Unit 37 names one
and says nothing about the other.

**Impact.** The choice is left to the builder, on a copy-installed kit file, and neither answer is
priced. Landing the key in one carrier contradicts the standing fix and reds once
`TOOL-aJoinedCanon-13` lands. Following the precedent mid-pass edits a shipped file that §1's no-veto
claim treated as untouched.

**Fix.** Make S3 decide, citing F2 and `TOOL-aJoinedCanon-13`, and record the choice in a §9 line.

- **(a)** Add `SPEC_HANDOFF_CUTOFF=""` with the adopter comment its siblings carry to
  `tools/memory-tree/.memory-tree.conf.example`. List the file in Files touched, with any kit version
  movement `bash tools/check-kit-versions.sh` requires. Check the edit against M3 veto 2, and park it
  if the veto trips.
- **(b)** Take `TOOL-aJoinedCanon-7`'s exception, and say why F2's reasoning does not reach a key
  whose only reader is exempt from shipping in `tools/govkit/registry.toml`.

**Left-shift.** `TOOL-aJoinedCanon-13` is the class gate, and it is already filed. Class item 6
below.

## Low

### L1 — every `New arm:` row says no floor moves, and S8 says it rises (33)

**Where.** §7 (`:213-217`) and §2 S8 (`:64-65`). Read against `memory/TEMPLATE-SPEC.md:193`.

**Defect.** The format defines the third field of a `New arm:` row as "assertion floor to move, or
none". All five rows say `none`. S8 and AC7 both raise `FLOOR_ASSERTIONS` in the same suite. Several
rows also stage more than one case, and AC5's row stages three, so S8's "number of arms added" cannot
be read off §7.

**Impact.** A builder who reads §7 alone may leave the pin unmoved. Given H1, nothing would catch
that.

**Fix.** Set each row's third field to `FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh`, and
state how many `arm` calls each row adds. S8's increment then becomes their sum. This folds with H1.

**Left-shift.** Class item 1 below.

### L2 — the reason given for skipping consumes-from assumes a reciprocity check 12 does not enforce for Tier-1 (15, 35)

**Where.** §3's Consumes-from bullets entry (`:72-77`) and §8 F2 (`:227-231`), against §8 F1
(`:221-226`). Read against `tools/memory-tree/check-memory-hygiene.sh:1517`, `:1788-1790` and
`memory/TEMPLATE-SPEC.md:163-165`.

**Defect.** §3 says "Reciprocity (check 12) already forces every consumes-from edge to have a
hands-off at the producer", and F2 repeats it. Check 12 does not force that in two cases.

- A Tier-1 spec is skipped at `:1517` before the edge arm, so its consumes-from bullets are never
  parsed.
- The reciprocity join skips any target outside the registered population at `:1790`, under the
  comment "ABSENCE IS NOT DISAGREEMENT". So a Tier-2 consumes-from that names a Tier-1 producer
  forces nothing.

F1 says the same thing in this spec: "Check 12 is silent on a Tier-1 target". At `282e0a6b`,
`DEPL-dDerivedDocket-1` is Tier-1 and declares eight consumes-from edges, and all eight happen to be
mirrored. Eight of the 107 hands-off edges target DEPL. No consumes-from names a Tier-1 producer.

**Impact.** The gap is latent. If a producer drops its hands-off to the Tier-1 runbook, neither check
12 nor this arm grades that payload, and S7's docstring limits will not say so. The decision to
exclude consumes-from still stands on its own evidence: the 12 measured false positives, which
reproduce at HEAD.

**Fix.** Narrow the §3 and F2 sentence to consumes-from edges between Tier-2 specs dated on or after
`SPEC_EDGES_CUTOFF`. Name what is left over in S7's docstring limits: a Tier-1 consumer's edges, and
edges to a Tier-1 or grandfathered producer.

**Left-shift.** A documented check. A rationale that leans on another gate's guarantee cites that
gate's population limit alongside it. Class item 3 below.

### L3 — S1's bullet shape is narrower than check 12's, and what it skips is not counted (34)

**Where.** §4 The selection (`:91-108`) and §2 S1 (`:34-40`). Read against
`tools/memory-tree/check-memory-hygiene.sh:1547`, `:1557` and `:1564-1565`.

**Defect.** §4 says "the bullet shape is the one check 12's SHAPE arm accepts". It is narrower.

- Check 12 accepts a `-` or `*` marker followed by any run of spaces or tabs (`:1557`).
- It accepts a target id with no backticks (`:1564-1565`).
- It finds Non-goals by heading text (`:1547`), where S1 says only "inside §3".

S1 matches only `- **hands-off** ` followed by a backticked id. A bullet check 12 accepts and S1 does
not is neither graded nor counted silent. `TOOL-aJoinedCanon-7` §1 recorded this same defect for §7,
where an author opted out of the only check without being told. At `282e0a6b`, no such bullet exists.
Every one of the 111 live hands-off lines is either S1's shape or an `external` bullet.

**Impact.** Small today. A later author's `* **hands-off**` bullet would drop out of grading, and S4's
line would not show it. The charter's §7 rule "A skip must announce itself" exists to prevent exactly
that.

**Fix.** Reuse check 12's verb regex and target parse, and find Non-goals by heading text. If that is
not done, count the bullets check 12 accepts but S1 skips, and print that count on S4's line. Add an
arm with a `* **hands-off**` bullet.

**Left-shift.** The arm. Class item 3 below.

## Left-shift, by class

1. **A witness cited for a count it cannot read** (H1, L1). This is the third recorded instance
   against `tools/check-testsuite-counts.sh`. The class gate `TOOL-aJoinedCanon-1` round 2 proposed
   is still unlanded: `compliant()` requires a comparison that reds when the pin and the executed
   count disagree in either direction. Until that lands, the gotcha names this leg. At spec-audit
   time the documented check is to read the header of every leg a criterion names as its witness,
   before accepting the criterion.
2. **A criterion over a population the build empties first** (H2). Step 4 of the brief closes specs
   as passes land, and the checkers grade only LIVE specs. A criterion that grades "the real tree"
   states its population at its own `order`, and requires a count above zero.
3. **A join that says it follows check 12 and keys differently** (H3, L2, L3). Identity by filename
   where check 12 uses the H1 uid; a shape narrower than check 12's; a reciprocity guarantee check 12
   does not make for Tier-1. The documented check: a spec that cites another check's grammar quotes
   that check's identity key, its accepted shape and its population limit, each with a line number.
4. **A §4 Inventory that asserts a naming verdict without asking** (M1). The decidable join is in
   M1's left-shift. Price it over the corpus before wiring it.
5. **A registry's discipline stated in a comment and enforced nowhere** (M2). A high-water pin
   compared by the checker that reads the registry.
6. **A conf key reaching one carrier** (M3). `TOOL-aJoinedCanon-13`, already filed.

## Outside the confirmed set

Two observations came out of re-measuring the spec's claims for this report. Neither was put to a
skeptic, so neither is counted above.

**§1's "131 hands-off payload tokens" does not reproduce at any commit.** With S1's own selection,
the pre-fold tree `aea85743` reads 78 bullets, 72 tokens and 2 hits. Both `18cf0c1b` and `282e0a6b`
read 107 bullets, 128 tokens and 0 hits. The fold and the three fixes landed together in `18cf0c1b`,
so the post-fold, pre-fix tree §1 describes was never committed, and its figure cannot be checked.
Over the same specs at HEAD, with the same exclusions, the consumes-from join grades exactly 131
tokens. The tree cannot say whether §1's figure counted the other verb. F3's 107 bullets and §3's
twelve consumes-from misses do reproduce, and the misses split eight and four as §3 describes.

**§4 Alternatives rejected cites M3 veto 3 for a shipped surface.** Veto 3 in
`memory/guides/BUILD-METHOD.md` is "widens a security, data or write surface". A new public surface is
veto 2. The alternative is rejected either way, so the conclusion does not change. If the fold
touches that paragraph, it should cite the veto that applies.

## What this round did not cover

- Units other than 37 were read only where this report cites them: units 7, 10, 13 and 15, DEPL and
  PLAY. The three fixes the orchestrator made to units 7, 10 and 13 before unit 37 was written belong
  to those specs' own group reviews and fold records. They are not reviewed here.
- The design record and the owner mandate contain nothing about unit 37, because the unit postdates
  both. Whether the adoption was right was judged against protocol section 11 alone.
- Re-measured for this report, at `282e0a6b` unless named otherwise:
  - S1's selection, with bullets, tokens, silent count and hits, at `aea85743`, `18cf0c1b` and
    `282e0a6b` (H2, Outside the confirmed set);
  - the naming forms of tracked and non-terminal specs against their H1 ids (H3);
  - the lexicon verb signal, `--suggest` for `grade_handoffs` and `check_handoffs`, and the pin's
    two-sided comparison (M1);
  - `tools/check-testsuite-counts.sh`, run on this tree, silent with exit 0, and the suite's `arm`
    count against its pin (H1);
  - the waiver registry's header and row count (M2), and the example conf's line 130 (M3);
  - hands-off edges to Tier-1 targets, and consumes-from edges from Tier-1 and to Tier-1 producers
    (L2);
  - hands-off lines outside S1's shape (L3).
- The self-test suite itself was not run. The brief holds it for the post-build bar.

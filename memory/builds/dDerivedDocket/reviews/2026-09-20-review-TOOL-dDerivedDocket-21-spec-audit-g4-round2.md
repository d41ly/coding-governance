**Serves:** spec-audit TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31

# dDerivedDocket — spec audit of topic group G4, the kit's stop causes, round 2

*Node `d`, 2026-09-20. A Tier-2 adversarial FOLD pass over the eight specs of topic group G4, the
kit's own stop causes: remote-relative bases and root-conf guards (unit 21), red attribution (23),
the inherited-red policy (24), runner hygiene (25), honest verdicts under contention (26), review
durability (29), the unattended leg's checker defects (30) and the build-method carriers (31). Four
primed finder lenses ran, then a skeptic stage prompted to REFUTE each finding in five batches, then
this synthesis. The aim was the text nobody has read: every section 9 line dated after the round-1
report of 2026-09-14, which in this set means the rev-4 regrounding on `fb07ca25` and the closing
consolidation pass of 2026-09-20. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief's roster and edge tables, and the round-1 report
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md`.
Sibling specs were read wherever an edge or an interface named them, because contradiction BETWEEN
specs is in scope. Specs are judged at the pinned blobs below; CODE claims are judged at HEAD, which
merges `origin/main` at `fb07ca25`, 210 commits past the round-1 base `abac6d59`. Every entry in this
report was re-checked against the file or the source it names before it was written down, and the
sites read are named in each entry.*

**Round: 2.** Range at base `fb07ca25`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-21.md@7c7547c60b6788ef611ffd0ff1e983f1c9001468`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-23.md@f08d4b11f062cefb15d95471fb5e3828905bb65b`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-24.md@3585fbdd1dc2472ec4e41a11438bf620417389d8`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-25.md@a37607c2b1a7027713c5cefabc4c0de081a7852c`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-26.md@9c4a53a510ebb4b84643473e03812b9185e33706`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-29.md@763876aead6ebf0602791ffea375b8cc3849f645`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-30.md@f1e5d0707cf79cb18b3bc5b261e685a9a1b3d644`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-31.md@7d52a3d732e39663e30109e3c9db523e6ed9e4eb`

## Verdict: CLEAN WITH FIXES

No confirmed finding is adjudicated a blocker. Two HIGH defects stand, and both sit in the two units
whose folds round 1 singled out as the largest, units 23 and 26.

- **A criterion whose own fixture reads its `Red when:`** (H1). Unit 23 AC9 rebuilds two replays from
  the records' own descriptions and requires both to read OWN. One of the two cited lines describes a
  measurement that produces S(L) = S(R), which rule 5 classifies INHERITED — the verdict AC9 names as
  its failure. The record that actually establishes the claim was wrong, `TOOL-aStagedLane-6`, is
  cited nowhere in this build, and the rule the unit implements is written on that row alone.
- **A mechanism that cannot do what the design asserts it did** (H2). Unit 26 S5 reaps the timed-out
  attempt with `run_leg_reap` at a moment when the attempt's subshell has already exited, and both of
  that function's arms die on a dead root. Section 4 Calibration then asserts the residue is gone and
  AC11 requires the grandchild dead, so the unit ships with a criterion its own design cannot make
  green.

Neither fold needs a mechanism no spec in the set carries, which is why neither is a blocker. H1's is
a citation swap plus a fixture rebuilt from the measured pair on the backlog row. H2's names a root
the runner already records.

Below those, eleven MEDIUM and three LOW. The dominant class is unchanged from round 1 and is the
reason this pass was aimed at fold text: **a statement claiming an observation no criterion can
make.** Nine of the sixteen items are that class outright, and in seven of the nine the statement
names the criteria by number.

Two items are fold remnants in the strict sense — text the 2026-09-20 consolidation pass left behind
or introduced. Unit 30's reuse audit still states the pre-fold placement of the unattended suite run
that the same pass moved (M11), and unit 21's consolidation paragraph justifies a respell with two
claims that are both false when measured (L3).

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero, so nothing was lost between the lenses and
this page and the finding set is complete for what the four lenses were primed to hunt. That is not a
claim that G4 holds no other defect, and a zero anywhere on this page is never offered as evidence of
absence about the specs themselves — only about the pipeline.

The pipeline's duplicate count of 0 is its own exact-match dedupe. On reading, two groups of confirmed
findings each describe ONE defect: ids 16, 33 and 35 are the same sentence in unit 30 section 10, and
ids 13 and 21 are the same ungraded derivation in unit 30 AC3. Each group is one entry below, and the
counts on this page are stated both ways.

## Review shape

Raw 40, confirmed 19, refuted 21, unverified 0, precision 0.47. The 19 confirmed ids collapse to 16
distinct defects.

| Severity | Items | Raw confirmed ids | Ids |
|---|---:|---:|---|
| BLOCKER | 0 | 0 | — |
| HIGH | 2 | 2 | 32, 34 |
| MEDIUM | 11 | 14 | 2, 4, 5, 7, 8, 9, 11, 12, 13, 16, 21, 33, 35, 36 |
| LOW | 3 | 3 | 15, 38, 39 |
| **Total** | **16** | **19** | |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the round-1
report and the G1, G2 and G3 reports used, so the counts compare across groups and rounds.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert, or which admits or refuses a state against an owner ruling, while its
  suite reads green.
- MEDIUM covers three things: a contradiction between or within specs with a bounded consequence, a
  declaration or edge a spec owes, and a rule whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, four findings move.

- Up, from medium to HIGH: 32. The finder read it as a criterion gap. It is not one: the criterion
  exists and is well formed, and the mechanism section 4 names cannot satisfy it. That is the
  cannot-pass-as-written class the scale puts at HIGH, and it is the same class as round-1 H7.
- Up, from low to MEDIUM: 13, folded into the same item as 21, which the finder already put at
  MEDIUM. One defect takes one severity, and the false observation claim is the MEDIUM half.
- Down, from high to MEDIUM: 16, folded with 33 and 35 into one item. It is a stale sentence in a
  reuse audit contradicted by the section-2 statement that governs, with a bounded consequence — the
  MEDIUM contradiction class. It is not HIGH, because the operative text a builder implements from,
  S7 and AC9, is correct and consistent across both.

Precision at 0.47 is BELOW the ~0.5 floor `AGENTS.md` section 8 sets, and it is the lowest figure of
any G-group round so far (G4 round 1 was 0.53, G1 0.56, G2 0.57, G3 0.64). Section 8's remedy below
the floor is tighter scope and priming, not more agents. Two contributors are visible in the refuted
set and both are fold-review artefacts worth carrying into the remaining fold rounds: lenses
re-reported round-1 entries whose folds landed correctly, and lenses read section 9 revision lines as
normative statements and graded them against section 2. Prime the next fold round with the round-1
findings index as known-and-fixed, and state that section 9 records history rather than rules.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 32 | HIGH | H2 | 26 | section 2 S5; section 4 Calibration |
| 34 | HIGH | H1 | 23 | section 6 AC9; section 1; section 9 rev-4 closing |
| 2 | MEDIUM | M1 | 26 | section 2 S5; section 6 AC4, AC10, AC11 |
| 4 | MEDIUM | M2 | 26 | section 2 S6; section 4 The boundary check; section 5 |
| 5 | MEDIUM | M3 | 23 | section 4 The classifier rule 2; section 2 S2; section 6 AC14 |
| 7 | MEDIUM | M4 | 24 | section 2 S7; section 6 AC13 |
| 8 | MEDIUM | M5 | 21 | section 2 S8; section 6 AC8 |
| 9 | MEDIUM | M6 | 29 | section 2 S1; section 6 AC1 and AC12 |
| 11 | MEDIUM | M7 | 31 | section 2 S5; section 6 AC15 and AC8 |
| 12 | MEDIUM | M8 | 30 | section 2 S3; section 6 AC4 |
| 36 | MEDIUM | M9 | 31 | section 4 One declaration, two readers; section 2 S5; section 6 AC15 |
| 13 | MEDIUM | M10 | 30 | section 2 S2; section 6 AC3 |
| 21 | MEDIUM | M10 | 30 | section 2 S2; section 6 AC3 |
| 16 | MEDIUM | M11 | 30 | section 10 BASE paragraph, against section 2 S7 and section 6 AC9 |
| 33 | MEDIUM | M11 | 30 | section 10 BASE paragraph, against section 2 S7 and section 6 AC9 |
| 35 | MEDIUM | M11 | 30 | section 10 BASE paragraph, against section 2 S7 and section 6 AC9 |
| 15 | LOW | L1 | 25 | section 2 S5 carrier half; section 6 AC1 and AC7 |
| 38 | LOW | L2 | 24 | section 4 Alternatives rejected, second bullet |
| 39 | LOW | L3 | 21 | section 9 rev-4 closing paragraph; section 7 New arm lines |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number, so "unit 23" is `2026-09-14-spec-TOOL-dDerivedDocket-23.md`.

## Blockers

None. Two candidates were weighed and both were put at HIGH.

- H1 leaves unit 23's AC9 unable to pass on one of its two fixtures. The fold is a citation swap and a
  fixture rebuilt from a measured pair that already exists on `memory/backlog/TOOL.md:405`. No
  decision and no new mechanism.
- H2 leaves unit 26's AC11 unable to go green with the mechanism section 4 names. The fold names a
  root the runner already writes and a walk it already ships, so it is local text in one spec. It
  fails toward a noisy HOST exit rather than toward a wrong verdict, which is the safe direction.

## High

### H1 — unit 23 AC9's first replay reads the verdict its own `Red when:` calls the failure, and the record that proves the claim wrong is cited nowhere (id 34)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-23.md`, section 6
AC9 (lines 300-304); section 1 (lines 20-21); section 9 rev-4 closing consolidation paragraph
(lines 452-457).

**What.** AC9 replays the two reds recorded at `memory/builds/aStagedLane/RUN.md:51` and
`memory/builds/dCarriedReceipt/RUN.md:89`, "rebuilt as two-commit fixtures from the records' own
descriptions", and requires both to read `OWN`. Its `Red when:` is "either replay reads INHERITED,
which is the claim those runs made and got wrong". The aStagedLane line does not support that.

**Why it is real.** Verified on three limbs.

1. `memory/builds/aStagedLane/RUN.md:51` is the override entry making the claim: 463 verb offenders
   over a pin of 461, re-measured at 463 with the build's whole working set stashed. A two-commit
   fixture built from that description gives S(L) = S(R), which section 4 rule 5 classifies
   INHERITED — the verdict AC9 names as its failure, not the one it requires.
2. `TOOL-aStagedLane-6` (`memory/backlog/TOOL.md:405`, WONTDO) is the record that establishes the
   claim was wrong, and it is the only source of a fixture that can read anything but INHERITED: the
   463 was measured against the OLD base, `origin/main` had come down to 461/1045 and green by the
   landing, and the merged tree was 467/1059, six offenders of which four were the run's own.
3. `git grep aStagedLane-6 -- memory/builds/dDerivedDocket/` returns nothing. The row is cited
   nowhere in this build, in any unit.

The asymmetry is sharp, and it is why section 9's blanket claim fails. The sibling citation
`memory/builds/dCarriedReceipt/RUN.md:89` IS the corrective measurement — pristine main 382/384 and
green against a branch at 429, with the per-file delta entirely the build's — so rev-4's closing
sentence "Both lines were re-read at HEAD and carry what they are cited for" holds for one of the
two. The consolidation pass respelled both citations from the build root so
`tools/check-spec-tokens.py` would grade them, and that checker resolves existence and range only, so
the respell could not have caught this.

The uncited row also carries the rule this unit's entire design implements, and it appears in neither
unit 23 nor unit 24: "a 'not mine' claim measured against a base the world has moved past is
indistinguishable from a 'not mine' claim nobody measured. Re-measure at the landing, not at the
branch point." That sentence is the recorded basis for R being the remote's advertised tip, and the
design cites nothing for it.

**Fix.** Cite `TOOL-aStagedLane-6` in section 1, in AC9 and in section 10. Build AC9's first fixture
from its measured pair — R at 461/1045 and green, L at 467/1059 — and state in the criterion that a
replay against the BRANCH-POINT R reproduces the INHERITED reading `:51` recorded, because that
reproduction is the defect the unit exists to close and is worth an arm of its own. Add the row's
landing-versus-branch-point sentence to section 4 "The R run" as the recorded basis for R.

**Left-shift gate.** Extend `tools/check-spec-tokens.py` with a citation-role check for run-record
lines cited inside an acceptance criterion: the cited line must be reachable AND the criterion must
name the record id that owns the claim, not only the file and line. The checker's header already
concedes that "a citation naming a real line that argues the opposite passes"; this is that hole with
a concrete instance, and the narrow, gateable half is the missing id. Class:
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`.

### H2 — unit 26's retry-time reap is rooted at a pid that is already dead, so AC11 cannot go green (id 32)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-26.md`, section 2
S5 (lines 64-66); section 4 Calibration (lines 154-160); section 6 AC11 (lines 286-290).

**What.** S5 reaps the timed-out attempt's process tree with `run_leg_reap`
(`tools/run-gates/run-gates.sh:1001`) before the serial retry, and never says what pid that reap is
rooted at once `runleg` has written `.rc` and its subshell has exited.

**Why it is real.** Verified against source at HEAD.

- `$WORK/<i>.pid` holds `$BASHPID` of the backgrounded `runleg` subshell
  (`tools/run-gates/run-gates.sh:1367`), and S5 places the reap after the pool drains — by which
  point that subshell has written `.rc` and exited.
- `run_leg_reap` (`:1001-1016`) has exactly two arms, both rooted at that pid, and both die on a dead
  root. `remove_descendants` (`:445-473`) walks `scan_descendants` over a `ps -ef` snapshot from the
  root; for an exited root that yields the seed alone. That is not inference — the function's own
  comment documents the identical failure shape from `TOOL-aQuenchedHarness-1`, where a deleted
  snapshot made the walk return its seed and the wall's only liveness assertion decorative. The
  monitor arm resolves the msys pid through `tools/process-monitor/reap.py:311`, which returns
  `REFUSED — msys pid %d resolves to no census row; it may already have exited` and kills nothing.
- S5 cites `:1033` as its justification — the outstanding-leg reaper skips any leg that already has an
  `.rc` — without noticing that the skip's PRECONDITION is the same dead root. The existing caller
  skips those legs because there is nothing live to walk from.

The consequence is exactly what the unit is written to prevent. The timed-out attempt's orphaned
grandchildren survive into the retry and into the second spawn-cost measurement, which is the residue
section 4 Calibration asserts is "gone, and a high figure means another tenant"; the bar then exits 4
as HOST over its own leftovers, which is the outcome AC11's `Red when:` describes. Section 10 confirms
`run_leg_reap` exists and nothing more, so the spec offers no other handle: no live root, no
orphan-sweep route.

**Fix.** In section 4 Calibration, name the root the retry-time reap uses and what it does when that
pid is already dead — the recorded `<i>.pid` if the process-monitor scope walk can enumerate by
recorded root rather than by live ppid chain, otherwise a scope walk over the run's own declared root
— and say which of the two mechanisms `run_leg_reap` already gives survives a dead root. If neither
does, S5 must name the new one rather than borrowing a function whose contract excludes this case.

**Left-shift gate.** AC11 is already the right criterion and it is well formed; it needs its arm
STAGED at the fixture level rather than asserted, which section 7's own rule requires of a new gate.
Add to `tools/run-gates/run-gates.test.sh` an arm that runs the reap against a root pid that has
already exited and asserts the grandchild is dead, and confirm it RED before the fix. That arm is the
one that would have caught this at authoring time. Class:
`memory/gotchas/a-double-you-wrote-grades-nothing.md` — the mechanism was read from its call site, not
run against the state it will meet.

## Medium

### M1 — no criterion ever observes the spawn floor being WRITTEN (id 2)

**Address.** Unit 26, section 2 S5; section 6 AC4, AC10 and AC11.

S5's writer — measure once at start, fold into the minimum, tmp-then-rename into
`<git-common-dir>/gate-spawn-floor` — claims observation by AC4, AC10 and AC11, and none of the three
ever READS that file after a bar. AC4 plants 1 ms or removes the file, AC10 plants 1 ms, AC11 grades
the reap. A grep of section 6 finds no occurrence of `gate-spawn-floor` at all. With `GATE_SPAWN_CMD`
seamed to 50 ms the start measurement folds to min(1, 50) = 1, so the write leaves no trace any
criterion reads, and F4's rule that a retry compares against the floor AS READ means the no-floor arm
still ends FAIL naming the missing calibration whether or not the writer exists.

An implementation that omits the tmp-then-rename writer entirely passes AC4, AC10 and AC11. On a real
clone the floor then never appears, HOST is permanently unavailable, and the bar prints `GATE FAIL`
naming the missing calibration on every double timeout — the unit's whole host-attribution mechanism
dead behind a full green. Section 5's two floor states, unreadable treated as absent and announced and
unwritable leaving the old floor in force, are unobserved for the same reason.

**Fix.** Add a criterion, or a clause to AC4: after a fixture bar runs with NO floor file,
`gate-spawn-floor` exists and holds one `<per-spawn-ms><TAB><iso-utc>` line; after a second bar whose
seamed spawn is cheaper the figure falls to the new minimum and does not rise when it is dearer; with
the floor file read-only the bar announces and the previous line survives.

**Left-shift gate.** A spec-lint rule that an `Observed by AC<n>` claim naming a FILE PATH must be
satisfied by a criterion whose text contains that path. Cheap, mechanical, and it catches this class
wherever a statement names its own artefact. The same rule closes M6 and part of M2.

### M2 — the hook's `GATE_RUN_ID` pin has no criterion, and section 5 states its security property outright (id 4)

**Address.** Unit 26, section 2 S6 (hook half, line 82); section 4 The boundary check; section 5
security.

Grep finds `GATE_RUN_ID` at four places in the spec — S6, section 4, section 9 and section 10 — and
NONE of them is in section 6. The runner at BASE defaults `RUNID="${GATE_RUN_ID:-$(date -u ...)-$$}"`
(`tools/run-gates/run-gates.sh:1084`) and the hook pins nothing today, so both the pin and its
pre-removal are entirely new behaviour with no staged break. Section 5 states the property it buys:
"the hook's pinned id is removed before use, so a planted record cannot satisfy it".

An implementation that pins a fixed or derivable id and skips the removal passes AC5 — a fresh scratch
repo holds no planted directory, so the fake runner's push is still blocked — and passes AC12, which
grades the runner half. Yet a leftover `<git-dir>/gate-run/<id>/verdict` reading `verdict GREEN` from
any earlier run then satisfies the boundary check for a push whose runner wrote nothing. That is the
`TOOL-aSurfacedLexicon-25` shape this unit exists to close. Unit 24 S5 spells the same pin for the
inherited-stamp reader and inherits the gap.

**Fix.** Add a criterion: with a directory of the hook's computed id pre-planted carrying
`verdict GREEN`, and the stubbed runner writing nothing, the push is still blocked; and two
consecutive hook runs pin different ids.

**Left-shift gate.** Every security property stated in a spec's section 5 must name the criterion that
stages its break, and a spec-lint rule can require a criterion reference on each section 5 security
bullet. This is section 7's "a new gate is not landed until its failing case has been observed",
applied one level earlier — to the criterion rather than the gate.

### M3 — rule 2's fired-ceiling predicate gained two branches at rev-4 and AC14 still stages one (id 5)

**Address.** Unit 23, section 4 The classifier rule 2; section 2 S2; section 6 AC14 (lines 342-349).

Rev-4 split rule 2 into rc 124 under a positive bound, rc 137 under a positive bound whose `.sec` is
at or above it, and a bound-0 rc 137 sent on to rule 3. AC14's fixture still lists only "one that
timed out at 124 under a positive bound", and its `Red when:` names only a CONTENDED leg re-run at R.
Rev-2 recorded that "AC14 stages every classifier branch but the worktree failure" — a claim rev-4
falsified without touching the criterion.

The two ungraded branches fail in OPPOSITE directions, which is why this is not cosmetic. An rc-137
kill after an ignored TERM that is not read as CONTENDED gets re-run at R and can read INHERITED,
which unit 24's `land` policy lands over. A bound-0 rc 137 read as CONTENDED is never re-run and
blocks `land` on a self-kill or an OOM. Unit 26 section 1 says the predicate is spelled identically
there, and its AC9 plus the untouched `4h-nobound` arm stage both — so one copy of a duplicated
predicate is graded and the other is not, and the two can drift apart silently.

**Fix.** Extend AC14's leg list with an rc-137 leg under a positive bound whose `.sec` is at or above
it, reading CONTENDED with no R run, and an rc-137 leg under a bound of 0 falling through to rule 3,
mirroring unit 26 AC9's arms.

**Left-shift gate.** The durable fix is structural: a duplicated predicate is a single-source-of-truth
violation (section 12). If the predicate stays in two units, add a parity arm asserting that the two
implementations classify an identical rc/bound/`.sec` table identically, so neither copy can be
extended alone. That arm is cheaper than keeping two criterion sets in step by hand.

### M4 — S7 ties the consulted record to three conditions and AC13 stages a refusal for one (id 7)

**Address.** Unit 24, section 2 S7 (line 80); section 6 AC13 (lines 421-427).

S7 ties the consulted attribution record to the tree being closed by three conditions: record `head`
equals HEAD, `tree_clean yes`, and verdict `tree_moved no`. `tree_clean` occurs in exactly two places
in the whole spec — S7 itself and AC13's positive clause. AC13's only refusal arm is the moved HEAD,
and its proceed arm supplies all three conditions at once, so an implementation comparing `head` alone
passes both clauses.

The round-1 H2 fix's other two conditions are therefore unobserved. An override or `--abort` that
consults an all-INHERITED record produced on a DIRTY tree, or on a bar whose verdict reads
`tree_moved yes`, is admitted, and AC13 stays green. That is the i12 path with one extra step, and it
reaches `land` over a red the run may own. AC6 and AC7 grade attribution CONTENT (OWN, MIXED), not the
record's provenance; AC15 and section 4's decision table reach `tree_moved` for the `gates-green` item
and the pre-push hook, while S7's `--close --override gates-green` and `--abort --code
gate-red-out-of-scope` are a third path that runs no bar and always consults an earlier record.

**Fix.** Extend AC13 with two more arms: the same record with `tree_clean no`, and with verdict
`tree_moved yes`, each refusing with the same numbered code naming the condition that failed.

**Left-shift gate.** Where a statement lists N conditions, a criterion supplying all N at once grades
the conjunction and none of the conjuncts. Add the rule to the spec-audit checklist: an admission
predicate with N conditions owes N negative arms, one per condition held false alone. Round-1 H2's
fold is the instance that proves the fix does not carry itself.

### M5 — unit 21 AC8 carries no clause holding `KIT_MEMORY_TREE_VERSION` unmoved (id 8)

**Address.** Unit 21, section 2 S8 (lines 67-75); section 6 AC8 (lines 298-310); section 4 Files
touched (line 202).

S8's rule (a) — the unit that first changes a kit's shipped bytes in build order moves that kit's
version — points at this unit for memory-tree, because section 4 Files touched names
`tools/memory-tree/kit.toml`. S8 therefore declares a prose EXCEPTION handing that move to the
memory-tree docs unit so `check-verdict-epoch.sh`'s topological rule holds. AC8 grades the two
PARALLEL exceptions — a `git diff HEAD^ HEAD` clause for `KIT_DRIFT_AUDIT_VERSION` and an empty-diff
clause for `tools/workflows/`, the latter for a kit this unit touches no file in at all — and carries
nothing for `KIT_MEMORY_TREE_VERSION`, whose carriers are
`tools/memory-tree/check-memory-hygiene.sh:20` and the `gov:kit memory-tree@` markers in
`tools/memory-tree/*.template.md`.

A builder applying rule (a) mechanically bumps those, all of AC8 stays green, and
`tools/check-kit-versions.sh` cannot see it — it grades presence and constant-marker agreement only
(`:21`, `:130-147`). The landing range then holds two moves of one kit, which is the exact fault AC8's
`Red when:` names for the other two, and the verdict-epoch rule that places memory-tree's bump at or
after the range's last engine change breaks under a full green.

**Fix.** Add to AC8 the clause its two siblings already have: `git diff HEAD^ HEAD --
tools/memory-tree/` on this unit's build commit shows no change to the memory-tree version constant or
its `gov:kit` markers, and name that third case in the `Red when:`.

**Left-shift gate.** The real gate belongs in `tools/check-kit-versions.sh`: over a landing range, a
kit whose version constant moves in more than one commit is a refusal. That turns a per-spec criterion
into a ratchet the next build inherits, and it is the "gate the CLASS, not the instance" reading of
this finding.

### M6 — the skeptic half of write-before-return is ungraded (id 9)

**Address.** Unit 29, section 2 S1 (lines 28-33); section 6 AC1 (line 266) and AC12.

S1 has three halves: lens prompts naming `find-<lens>.json`, skeptic prompts naming
`verify-<first id>-<last id>.json`, and a REQUIRED `path` field on both finding schemas AND the
verdict schema. AC1 reads only "every traced `find:` prompt" and "both finding schemas"; AC12 counts
only `find-<lens>.json` files in the key directory. A grep for `verify-` and `verdict` across the whole
spec finds no criterion touching the skeptic write at all — AC5 grades reuse against a PLANTED
`verify-<a>-<b>.json` fixture, which is satisfied without any production write path existing.

So skeptic prompts that never name a file, or a verdict schema whose `path` is optional, pass AC1 and
AC12. No verify file is then written, S4's batch reuse can never match anything in production, and F3's
whole rationale — a dead synthesis not re-running every skeptic — is lost while AC5 stays green on the
fixture. S1's own "Observed by AC1 and AC12" is false for half of S1.

**Fix.** Extend AC1: every traced `verify:` prompt names a file under `review-lenses/` ending
`verify-<a>-<b>.json`, and the verdict schema lists `path` in `required`. Extend AC12 to require one
`verify-<a>-<b>.json` per batch that returned.

**Left-shift gate.** `memory/gotchas/a-double-you-wrote-grades-nothing.md` is the recorded class, and
its gateable form here is a rule for this build's criteria: a criterion whose fixture is PLANTED cannot
be the only observation of the mechanism that produces that fixture. Flag any criterion whose fixture
line says the file is planted and whose statement has no sibling criterion observing a real write.

### M7 — the shipped adopter default of `FORK_ITEM_CUTOFF` is staged nowhere (id 11)

**Address.** Unit 31, section 2 S5 (line 44); section 4 (lines 162-164); section 5 migration (line
261); section 6 AC15 and AC2.

S5 declares that a blank `FORK_ITEM_CUTOFF` means off in BOTH readers, and no criterion stages a blank
or an absent value. AC15 stages a quoted spelling with a trailing comment, a single-quoted one, a
repeated key, a bare value and the malformed `2026-09-15x`. AC2 stages a pre-cutoff spec under a SET
cutoff. AC8 explicitly sets gov's own cutoff later than every tracked spec date, so gov's own bar
cannot reach the off state either. Section 7's new-arm list for `marker-contract.test.sh` names no
blank case.

Blank is the shipped adopter default, and it is the ONE value a date comparison gets wrong by default:
every filename date sorts at or after the empty string, so the natural implementation turns per-item
grading ON for every spec in the tree. That reds a landed corpus in every adopter that installs the kit
without setting the key, and no criterion of this unit could catch it.

**Fix.** Add an arm to AC15 or AC2: with `FORK_ITEM_CUTOFF` blank, and again with the key absent from
the conf, both readers grade every fixture spec exactly as at BASE — the hygiene side silent and
`plan_state` READY — including a post-cutoff-dated one with an unmarked F2.

**Left-shift gate.** A conf key whose declared OFF state is the shipped default gets an arm at that
default, always. Add it to the memory-tree kit's own conf-contract suite so it binds for every future
key, not only this one: for each key the kit declares, one arm at its documented default value.

### M8 — the empty and doubled sentinel regions, the branch section 4 calls the join's liveness, are staged nowhere (id 12)

**Address.** Unit 30, section 2 S3 (lines 42-45); section 6 AC4 (lines 289-293); section 4 (lines
159-164).

S3 declares a `fail 22` branch for a sentinel region that is missing, REPEATED or EMPTY. AC4 stages one
removed key and one deleted sentinel — of the region branch's three trigger conditions, only "missing"
is staged, and section 7's new-arm list does not add the other two.

The doubled case is the demonstrable false green, and section 4 records the first-draft trap that
produced it: an over-wide extraction read 38 keys instead of 20, and a wider allow-list subtracts more,
leaving the `comm` difference empty and check 22 reporting green over a real mismatch. Section 4 itself
calls this branch "the join's liveness: a region that reads as empty would otherwise pass every key".
So the one condition the design names as load-bearing ships with its failing case never observed,
against section 7's own rule that a gate is not landed until its failing case has been seen — in the
very check written to remove a green-by-absence.

**Fix.** Extend AC4 with two arms: a present sentinel pair enclosing no key fails 22 naming the region,
and a doubled sentinel pair fails 22 naming the region. Each staged and seen RED.

**Left-shift gate.** Generalise it in the unattended kit's suite rather than in this criterion: for
every sentinel-delimited region any checker reads, an arm at empty and an arm at doubled. The class is
`memory/gotchas/green-bar-over-a-population-of-one.md` — a join over an empty set is the
population-of-zero version of it.

### M9 — unit 31's M11 fold claims a guard the recorded gotcha does not prescribe, and blank-on-no-match is indistinguishable from the declared off state (id 36)

**Address.** Unit 31, section 4 "One declaration, two readers"; section 2 S5 (line 51); section 6 AC15.

The text folded for round-1 M11 says it carries "the guard
`memory/gotchas/two-readers-of-one-config-one-re-derived.md` prescribes for a deliberate re-parse".
That record prescribes keeping the re-parse AND comparing it against the AUTHORITATIVE read, redding on
ANY difference, and separately "arm the parse as well as the read". The spec substitutes a
four-spelling fixture table.

The substitution leaves a live hole because blank is the declared off state. S5 scopes the refusal to
"a resolved value that is neither blank nor a date", so a legal sourced spelling the text reader does
not model — `export FORK_ITEM_CUTOFF="..."`, an indented assignment, an assignment inside a conditional
— resolves to blank, per-item grading goes silently OFF on the planning side, and the hygiene side,
which gets the value from the engine's own `.` of the same file
(`tools/memory-tree/check-memory-hygiene.sh:113`), keeps it ON. Two readers then grade one corpus under
two cutoffs with nothing red. That is precisely the class the gotcha records, from `.unattended.conf`'s
`BYPASS_BAN` going RC=1 to RC=0 while the leg printed that the scan ran. AC15's four cases are all
column-0 plain assignments the reader DOES match, so none of them can fail this way, and AC8 sets gov's
cutoff past every tracked spec so both readers are trivially off.

Note the constraint the fix must respect: F5 rejected sourcing because the driver must not execute a
second kit's conf (M3 veto 3). So the remedy is not a runtime compare.

**Fix.** Make the reader refuse, numbered, when a line assigning `FORK_ITEM_CUTOFF` exists in the file
but no value resolves from it. The leg's own name reader at `tools/unattended/check-unattended.sh:147`
already models the `export` prefix and leading whitespace and is the in-tree precedent. Add that case to
AC15, and state in section 3 why the gotcha's runtime compare against a sourced read is unavailable
here.

**Left-shift gate.** Add a conf-parse arm to the memory-tree kit's suite that feeds each declared key
the four sourced spellings a shell accepts — `export`, indented, quoted, conditional — and asserts the
text reader either resolves the same value or REFUSES. A silent blank is the outcome that must be
impossible, and this gate makes it so for every key rather than for this one.

### M10 — the derived `--only 28` skip list is ungraded, and S2 claims AC3 observes it (ids 13, 21)

**Address.** Unit 30, section 2 S2 (line 40); section 6 AC3 (lines 281-283); section 4 (lines 154-156);
section 8 F3.

S2 requires the `--only 28` skip list to be DERIVED from the file's own `# ---- check <n>` headers
rather than typed, and declares itself "Observed by AC3". AC3 pins only that `--only 28` exits 0 and
prints one skip line each for checks 30 and 31, and its `Red when:` names the conf-guard crash
(`MEMORY_ROOT: unbound variable`). `# ---- check <n>` appears exactly twice in
`tools/unattended/check-unattended.sh`, at checks 30 and 31, so a derived implementation and a
hand-typed `30 31` produce byte-identical output today and AC3 cannot tell them apart.

The derivation is the half S2 exists for. Section 4 chose it explicitly — "a check added later is
skipped and announced without anyone editing a list" — and F3 records the resolution without adding a
criterion that can fail on the typed form. Left ungraded, the next check added after the 28 region
either returns the `set -u` crash this unit closes or is skipped in silence, which is the class section
7's header rule exists to prevent.

**Fix.** Extend AC3, or add a criterion: with a fixture copy of the leg carrying an extra
`# ---- check 32` header after the 28 region, `--only 28` prints a THIRD skip line naming 32 with no
edit to any list. Give it a `Red when:` reading "the skip list is a literal, so a check added after this
unit is skipped in silence".

**Left-shift gate.** Where a statement chooses DERIVATION over a literal, the criterion must extend the
population, never re-read the current one. Add that as a spec-audit checklist line: a derived-set claim
whose criterion tests only today's members grades nothing. This is the same shape as
`memory/gotchas/green-bar-over-a-population-of-one.md` one level up — the population is two and the
property is about the third.

### M11 — unit 30's reuse audit still states the pre-fold placement of the unattended suite run (ids 16, 33, 35)

**Address.** Unit 30, section 10, third paragraph, last sentence (lines 519-521), against section 2 S7
(lines 68-71) and section 6 AC9 (lines 325-338).

Section 10 reads "section 2 S7 and section 6 AC9 run the unattended suites once at this unit's end
under D12-i8's lift, which predates both; that conflict is reported to the orchestrator and is not
decided here." S7 now reads "The unattended suites run once under unit 1's attribution at VERIFYING,
after the last unit, and they are on no bar leg; D12-i8's in-pass lift is parked", and AC9's
`permission:` line says the same. Section 9's rev-4 extension of 2026-09-20 records the move in those
exact terms. Section 10 was not swept with it.

The spec therefore states two placements for one run. The section 10 reading sends the pass at
`bash tools/unattended/run-unattended-gates.sh` INSIDE the pass, which `tools/unattended/gate-guard.js`
denies before VERIFYING — the refusal S7 was rewritten to avoid — and it records the position the
parked owner question rejected. Checked across the group: units 24, 25, 26, 29 and 31 carry the folded
wording everywhere, and their `permission:` lines read VERIFYING. Unit 30 is the only spec of the eight
holding the stale sentence.

Three findings reported this and they are one sentence, located in section 10's THIRD paragraph, not
its final one — the final paragraph is the `Recall terms used:` line.

**Fix.** Rewrite that sentence to say what S7, section 5 testing and AC9 now say: the gate-guard
conflict with D12-i8 is folded on its conservative reading, the attributed suite run moves to VERIFYING
after the last unit, and the ruling itself stays parked in RUN.md. Keep the aDeferredBar and aProbedUnit
provenance sentence and the report-to-the-orchestrator clause; drop "at this unit's end under D12-i8's
lift".

**Left-shift gate.** A spec-lint rule reachable with the existing token checker: a sentence in any
section that cites "section 2 S<n>" or "section 6 AC<n>" must not contradict a pinned phrase of the
statement it names. The cheap, mechanical form is a phrase-agreement check on the small closed
vocabulary this build already uses for run placement — `at this unit's end` versus `at VERIFYING` —
redding when one spec holds both. Class: `memory/gotchas/fold-text-is-unreviewed-surface.md`, which this
finding instantiates precisely: the pass that moved the rule did not re-read every section that states
it.

## Low

### L1 — the runner's own exit-code header gains exit 3, and no criterion reads it (id 15)

**Address.** Unit 25, section 2 S5 carrier half (lines 51-55); section 6 AC1 and AC7.

S5 requires the runner's exit-code header line at `tools/run-gates/run-gates.sh:3` and
`tools/run-gates/README.md` to gain exit 3, and declares itself observed by AC1 and AC7. AC1 grades
exit 3, the printed TREE MOVED line and the run record; AC7 grades exit 1 precedence with a failing leg.
Both are behaviour; neither reads file text. AC9 greps the README only for "at an empty dir". Section
7's legs and new arms are all canary or turnstile behaviour.

Unit 26's AC8 does read the README's exit-code section for "the precedence of exits 1, 3 and 4", which
covers the README half but in a LATER unit, so nothing in unit 25's own pass would notice. Nothing
anywhere reads the runner's own header line. A new exit code is a caller-facing contract, and the header
is where a reader of the runner meets it; landed without it, exit 3 exists only in behaviour and a
caller treats TREE MOVED as an undocumented status.

**Fix.** Add a clause to AC7, or a short criterion of its own: after this unit, the runner's header
exit-code line and the README's exit-code section both name exit 3 as TREE MOVED. Red when either stops
at exit 2.

**Left-shift gate.** A runner-level gate is better than a criterion here and it is small: assert that
every exit status the runner can return is named in its header block, deriving the status set from the
`exit <n>` sites. That is the derive-over-author form and it cannot go stale.

### L2 — the "sat for weeks" clause is not in the line it cites (id 38)

**Address.** Unit 24, section 4 Alternatives rejected, second bullet.

The bullet says "the lexicon red of 435 offenders sat for weeks under an unchanged checker
(`memory/builds/dFramedEntrypoint/RUN.md:41`)". That line reads "Nothing in this build caused it and
this build cannot see when it started, because the leg is GUARDED on `tools/`,
`skills/session-kickoff/`, `.githooks/` and `.claude/` … a red can sit in it for the length of any
build that does not touch them." It establishes that the red was not the run's and that its age is
UNKNOWABLE from that build — it explicitly declines the measurement the bullet attributes to it. No
record in the tree dates the 435-offender red; the only other mention is this build's own round-1 audit
repeating the citation.

The closing consolidation pass respelled this citation so `tools/check-spec-tokens.py` would grade it,
and that buys nothing here: the checker resolves existence and range, and its own header says "a
citation naming a real line that argues the opposite passes".

**Fix.** Drop "for weeks" and rest the bullet on what the line does record — a content-borne red under
an unchanged checker whose age the comparator cannot date — or cite a record that measured the duration.
The rejected alternative survives either way; only the duration clause is unsupported.

**Left-shift gate.** The same gate as H1's, at a lower stake: the token checker should grade a
citation's ROLE, not only its resolvability, at least to the extent of requiring that a quantitative
claim — "weeks", a count, a duration — be accompanied by the figure from the cited line. Until then this
is a documented manual check on the spec-audit checklist: a citation carrying a number must be read, not
resolved.

### L3 — the backticking rationale in unit 21's consolidation paragraph is false on both halves (id 39)

**Address.** Unit 21, section 9 rev-4 closing consolidation paragraph; section 7 New arm lines.

The closing pass backticked both `New arm:` suite paths "as every other spec of this build spells it and
as the token checker reads a path". Measured over `memory/builds/dDerivedDocket/spec/`: 81 `New arm:`
lines across 8 specs, 51 backticked and 30 bare — 27 excluding the three `.githooks/pre-push.test.sh`
rows — spread over units 22, 23, 24, 25, 26, 27, 28 and 37, four of them this group's own siblings that
the same closing round touched. So "as every other spec of this build spells it" is false. And
`tools/check-spec-tokens.py`'s `LEG_LINE` at `:94` matches only a line that is nothing but backticked
tokens and separators, which a `New arm:` line is not, while its `paths` join iterates
acceptance-criterion bullets only. No section 7 `New arm:` path reaches either join, so the checker
reads neither form. Backticking one actually pushes it into the BAR near-list as a token outside the
graded population.

The build now states two conventions for one field on a premise neither the corpus nor the checker
supports, and a later reader cannot tell which is the rule.

**Fix.** Either correct the rationale to say the backticking is a house-style choice no leg grades, or
record that the build owes the same respell in the 27 bare lines and name the units, so the convention
is one convention.

**Left-shift gate.** If the convention is to be one convention, gate it: extend
`tools/check-spec-tokens.py` to read section 7 `New arm:` lines and require one spelling. If it is not
worth gating, the rationale must not claim the checker enforces it — a claim about a gate that the gate
does not make is the same false-observation class as the rest of this report, aimed at a document rather
than at code.

## Do the round-1 fixes hold

This is a fold review, so the question is asked of round 1's 43 distinct defects as well as of the new
surface. The honest scope statement first: the four lenses swept all eight specs at the pinned blobs
with the round-1 report in hand, and NO round-1 entry was found re-opened — its fix reverted, or its
text restored. That is the sweep's result, not an exhaustive per-entry audit. A defect whose fold landed
in wording no lens re-read would not appear here, and the 0.47 precision says lens attention went
disproportionately to re-reporting folds that landed correctly rather than to finding what they broke.

What can be said positively, entry by entry, for the round-1 findings this round's evidence touches:

- **H2 (unit 24 S7, the record a refusal consults)** — the fold LANDED and is visible: S7 now ties the
  consulted record to three conditions, where round 1 found it tied to none. The fix is incomplete
  rather than wrong, because AC13 grades one of the three (M4 above).
- **M11 (unit 31 S5, two readers of one config)** — the fold landed as a fixture table, and it does NOT
  carry the guard it says it carries. The gotcha prescribes a compare that F5's veto makes unavailable,
  and the substitute leaves the blank-on-no-match hole (M9 above). This is the one round-1 entry whose
  fix I judge does not hold as written.
- **M23 (unit 30 S6 and AC8) and the check-26 flag arm** — the rev-4 regrounding rewrote the flag
  population around the `gov:argv-begin` sentinels and AC5 to AC7 stage it; no new defect was confirmed
  in that text this round.
- **The 2026-09-20 consolidation pass** is where three of this round's items sit: M11 (its unswept
  section 10 sentence in unit 30), L2 and L3 (two respells whose stated rationales do not hold). That is
  the expected shape — `memory/gotchas/fold-text-is-unreviewed-surface.md` — and it is why the remaining
  groups' closing passes should be re-read rather than trusted.

The rev-4 regrounding on `fb07ca25` is the largest block of new text in this set, and both HIGH items
sit in it or beside it: M3 is a predicate rev-4 split without touching its criterion, and H1 is a
citation the closing pass respelled without re-reading what it argues. Both are the same authoring
failure, which is worth stating once: **a pass that edits a rule must re-read every sentence that cites
the rule, and a pass that edits a citation must re-read the line it cites.** Neither is expensive; both
were skipped.

## Left-shift summary

Ten of the sixteen items above suggest a gate. Three of them are one gate, and it is the one this build
should build next, because it closes the class that has dominated every G-group round:

**A spec-lint rule that an `Observed by AC<n>` claim must be satisfiable by the criterion it names.**
The mechanical, zero-judgment form: when a statement names a file path, an env var, a conf key or a
numbered code, at least one criterion it cites must contain that token. M1, M2 and M6 are that rule
exactly; M5 and M10 are within reach of it. It belongs in `tools/check-spec-tokens.py`, beside the joins
already there, and it grades the specs of every future build rather than these eight.

The rest, in rough order of reach.

- `tools/check-kit-versions.sh` refuses a landing range holding two moves of one kit (M5).
- A conf-contract arm per declared key, at its documented default and at four sourced spellings (M7, M9).
- An empty-region and doubled-region arm for every sentinel-delimited region a checker reads (M8).
- A parity arm over the classifier predicate duplicated between units 23 and 26 (M3).
- A staged dead-root arm in `tools/run-gates/run-gates.test.sh` (H2).
- Citation-role grading in `tools/check-spec-tokens.py`, so a resolvable line that argues the opposite
  no longer passes (H1, L2). Until it exists, a documented manual check: a citation carrying a number
  must be READ.

Recall terms used: `spec audit fold review criterion gap Observed by AC attribution INHERITED OWN
gate-spawn-floor GATE_RUN_ID sentinel region FORK_ITEM_CUTOFF run_leg_reap VERIFYING gate-guard`

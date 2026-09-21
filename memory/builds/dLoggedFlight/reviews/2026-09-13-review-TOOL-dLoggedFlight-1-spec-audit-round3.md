**Serves:** spec-audit TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13

# dLoggedFlight — spec audit of the thirteen-unit set, round 3

*Node `d`, 2026-09-13, on `branch/unattended-build-transparency-ea83a5` at HEAD `e1e83acf`. That commit
is the rev-3 fold of the round-2 audit, and the specs' stated base is `9fac2b53`. No file under `tools/`
or `.githooks/` differs between those two commits, so every line a spec cites at base holds at HEAD.
This is ROUND 3 of the spec audit. It is a Tier-2 adversarial pass: four primed finder lenses, a skeptic
stage of five batches prompted to REFUTE each finding, and one synthesis, which is this record. The
earlier rounds are [round 1](2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) and
[round 2](2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md). The rev-3 fold touched units 1
to 4, 6, 8 to 11 and 13. Units 5, 7 and 12 are still rev-2, and their blobs differ from round 2's only by
the generated records row that bound round 2. Every claim this record makes in its own voice was
re-derived against the tree; the list is under "What this synthesis re-derived". Where a figure came
from verification and was not re-derived, the text says so.*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 3:** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md@988657be6ba5114f8f1bca691394d5f8c04f6fc1`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md@702616443667fb4bf972a52b1b372972b4626035`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md@2bf535dc7b5e24e65460d804e160f5dd889b210b`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md@e5de64d007683f713201767e99c7b953c8da14e3`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-5.md@53c2c9269fa59378de22f3d685af1a417b2e5c9e`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md@04474410f91b29093dc0ea38b50b5a9df4154357`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-7.md@6763c95fe40d761cb45f072fe1b08382efc7e123`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md@4164e33b841ee878a88c3877c87f8b80187ed55d`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md@758c0677e2bf6fcf3c8e4a0f6890691e0d891ea5`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md@01715b7ac0f8836b56fb3480ef8a4dd895a8d805`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md@92f8f8a3233de31ad9bc2c48f26b5ee300033b5a`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-12.md@3332a7dc52f4c668fb29a1f70845f3796c852a03`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md@7f3df5be79c102218025b10a9b224e1cabe5d1f3`.

## Verdict: CLEAN WITH FIXES

No blocker stands. No confirmed finding disputes the fold of round 2's blocker: runs are now keyed on
the commit that started them. Unit 8 §4 measures those keys as distinct for all six rotated builds, and
this synthesis confirmed that for the two it re-derived. Four highs remain, and each gives a wrong answer
on records this tree already holds:

- H1. The model calls dRatifiedSeam `no-progress`, "a run that built nothing". That run built two units
  and was merged. The label comes from its witness, which `--close` never rewrites.
- H2. RUN.md is reused across rotations, so reading its history as one run's history ends two rotated
  runs' windows before they start.
- H3. The landing push is made from the primary tree, so it joins no run. Every later landed run then
  reports its push writer as dead, or reports it alive without the landing push.
- H4. Nothing joins git's list of runs to the journal's list of STARTs.

Each of the four is a rule a fold can state, and none needs a mechanism the build lacks. So the design
stands, with fixes.

The fold dominates the finding set, more than in round 2. 21 of the 26 confirmed findings sit in text
the rev-3 fold wrote, or in text where it answered a round-2 finding only in part. In round 2 that was
24 of 36. The worst of them started in the round-2 record itself. H1 is the fold carrying out a premise
that record stated in its own voice, and the record had checked only half of that premise.

The review shape is stated in full below: raw 106, confirmed 26, refuted 80, unverified 0, precision
0.25. This synthesis adjudicates 0 BLOCKER, 4 HIGH, 12 MEDIUM and 4 LOW, over 20 items. The confirmed
blocker count by round is 4, then 1, then 0. Under `memory/guides/BUILD-METHOD.md` M4, a synthesis that
calls the design clean ends the spec audit. This one does, so fold these twenty items and stop. See
"Disposition" for the two checks this round's evidence says that fold owes itself. Nothing will review
it as a spec.

## Run integrity

- lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.

Every counter is zero, so the run is complete in the only sense the orchestration can certify: every
lens reported, and every finding reached a skeptic. Complete is not clean. The 26 confirmed findings are
a lower bound on the defects in this set, not a census of them. Units 5 and 7 drew no confirmed finding.
Unit 12 drew one, and only as a carrier of M12. That means nothing was found there, not that those units
are sound.

## Review shape

- raw 106, confirmed 26, refuted 80, unverified 0, precision 0.25.
- This report adjudicates **0 BLOCKER, 4 HIGH, 12 MEDIUM, 4 LOW**, over 20 items. Counted by raw
  finding instead of by item, the split is 0, 7, 15 and 4. The integers this synthesis returns are item
  counts, 0 and 4. That is the convention rounds 1 and 2 used in their `RUN.md` review rows (`blockers
  4`, then `blockers 1`), so the M4 convergence comparison compares like with like.
- Three folds combine 9 raw findings into 3 items: H1 (71, 72, 98, 99), M1 (15, 78) and M2 (18, 46, 50).
  Each of the other 17 is one item. The pipeline's duplicate count is zero because it discarded nothing
  as a duplicate. These folds are this synthesis grouping distinct findings that describe one defect,
  and every raw id stays in the header of the item that absorbed it.
- A fold takes the highest severity filed among its members, as in the earlier rounds. That raised raw
  50 from low to MEDIUM. No other finding moved, and no item sits above its highest filed member.
- Skeptics narrowed three survivors, and each item carries the narrowed claim. In raw 100 (M10), the
  gate's printed remedy does point at the hand route. In raw 24 (L1), the precedence half is weaker and
  the strictly-behind gap stands. In raw 18 (M2), the `:5021` point is secondary.
- Precision by round has been 0.58, 0.55 and 0.25. This round falls below the ~0.5 line in `AGENTS.md`
  §8, where the rule is to tighten scope and priming before adding agents. This synthesis received only
  the survivors, so it does not characterize the refuted 80.

## Findings

Unit N below means `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-N.md`. The
Origin column is this synthesis's reading of rev-3 at `e1e83acf` against rev-2 at `f698f6e6` and rev-1
at `1dd6f3da`:

- `fold` means the rev-3 fold wrote the defective text.
- `in part` means the fold answered a round-2 finding and left part of it standing.
- `missed` means the text predates rev-3 and no earlier round flagged it.

| # | Sev | Unit | Address | Origin | One line |
|---|---|---|---|---|---|
| H1 | HIGH | 13, 8 | 13 §1, §2 S1, §4, AC1, AC3; 8 §2 S6, §4, AC5 | fold | `--close` writes no witness, so a landed run reads "built nothing" |
| H2 | HIGH | 8 | §2 S2 window ends, with S1; AC1, AC16 | fold | a reused path's history ends a rotated run's window before it starts |
| H3 | HIGH | 8, 3, 11 | 8 §4, §2 S3, AC10; 3 §3; 11 §2 S2, S6 | missed; fold | the landing push comes from the primary tree, and pushes join by worktree |
| H4 | HIGH | 8 | §2 S1 against S2; AC1, AC9, AC15 | fold | git's runs and the journal's STARTs have no join |
| M1 | MEDIUM | 8 | §2 S8; AC17 | fold | attribution reads a unit and a phase that START does not carry |
| M2 | MEDIUM | 2 | §4 Placement; AC2 | fold; in part | AC2 grades the old exit population, and §4's two lists disagree on `:5021` |
| M3 | MEDIUM | 2 | §4 Placement; AC1, AC13 | missed | `VERB` is empty when `--phase` exits |
| M4 | MEDIUM | 8 | §2 S7; AC6 | fold | no fixture has lines of its own and a window holding the epoch |
| M5 | MEDIUM | 6 | §2 S8; AC8 | fold | the sentinel cannot see a write beside it, or any read |
| M6 | MEDIUM | 4 | §2 S1, S3; §4; AC1, AC2 | fold | the refusal line's remote fields meet no credential check |
| M7 | MEDIUM | 13 | §2 S3; AC3 | fold | one fixture per table row never exercises the act rule |
| M8 | MEDIUM | 8 | §2 S4; AC11 | fold | the ledger's exclusions have no negative fixture |
| M9 | MEDIUM | 8 | §2 S9; AC13 | fold | the no-START stand-in has no criterion |
| M10 | MEDIUM | 1, 3, 4 | 1 §2 S1, §4, §7; 3 §2 S6; 4 §2 S7, §4 | missed; fold | new registry rows raise a banned carried-prefix count no spec plans for |
| M11 | MEDIUM | 8, 9, 13 | 8 §2 S4; 9 §2 S4; 13 §2 S3 | fold | the driver's owed sets are retyped, on a premise the recorded rule contradicts |
| M12 | MEDIUM | 9, 10, 12, 8 | 9 §2 S1; 10 §2 S1, S6; 12 §2 S3; 8 §2 S1 | missed | the memory root is a literal in a kit that ships |
| L1 | LOW | 8 | §2 S6; AC5 | fold | "at or behind" is staged only at "equal" |
| L2 | LOW | 8 | §2 S4; AC11 | fold | two owner spellings and the near-miss boundary are unstaged |
| L3 | LOW | 10 | §2 S6; AC4 | fold | the one-call cost claim is tested by varying the wrong population |
| L4 | LOW | 2 | §4 Placement | missed | `check_slug` has no 64-character bound |

---

### H1 — HIGH — unit 13 §1, §2 S1, §4 and §6 AC1, AC3; unit 8 §2 S6, §4 and §6 AC5 — raw 71, 72, 98, 99

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** Both units now treat a witness at or behind the recorded `base:` as "a run that built
nothing". Unit 13 reports such a record as `no-progress` and leaves it out of the count, and unit 8 makes
it the anomaly kind `no-progress`, never `nonterminal-merged`. Both cite TOOL-cFinalBerth-2. That
decision compares the recorded base against HEAD at `--close`
(`memory/builds/cFinalBerth/spec/2026-08-13-spec-cFinalBerth-2.md:102-109`). It never compares the base
against the witness.

The witness is HEAD as of the last verb that wrote one. Four verbs write it: `--phase`
(`tools/unattended/unattended.sh:2237`), `--landed` (`:2415`), `--abort` (`:2541`) and `--preflight`
(`:2750`). `verb_close` (`:2914`) writes `phase LANDING` at `:3037` and writes no witness. So a run that
goes from preflight to `--close` without calling `--phase` keeps a witness equal to its base, however much
it built.

dRatifiedSeam is that run, and it is the one record both units name. Re-derived here:

- Its `RUN.md` reads LANDING, with witness and base both `a69e57d7`, written once at preflight `a156548f`.
- Its rows carry a brief and a dispatch for each of its two units, a `CONVERGED` review, and no override.
- Its product commits `26c52ba1` (govkit) and `532e6f2b` (workflows) are ancestors of `origin/main`.
  Both were merged by `4f268bce`, "Merge build dRatifiedSeam — the two owner rulings, built and reviewed".
- Today's driver refuses `--close` when the recorded base equals HEAD: "this run built nothing on top of
  the anchor" (`:988-990`). That refusal sits in the `authorization-reachable` item (`:3059-3074`). A
  LANDING record with no override therefore shows the witness is stale. It does not show the run was
  empty.

The premise came from the round-2 record. Its H4 re-derived that dRatifiedSeam's witness equals its
base, concluded that "one of unit 13's measured six is vacuous", and called that case a run "that died
before its first `--phase`". It never checked whether the run had built anything. Round 2 offered two
fixes, and the fold took the labelled one ("a run that built nothing") over the `unjudgeable` one.

**Impact.** Unit 13's signal hides the one record it exists to report: a run that landed but still reads
LANDING. Its §1 and §4 say five where the tree holds six. AC3's witness-equals-base fixture, "`no-progress`,
uncounted", locks the misreading in. In unit 8, `no-progress` is part of the closed anomaly vocabulary
that unit 9 publishes, so a committed record for this kind of run would say it built nothing, and
`nonterminal-merged` would never fire for it. AC1 ("5 or more") and AC5 (a hand-built equal fixture) both
pass. Every future run that reaches `--close` without a `--phase` after its last build commit will read
the same way.

**Why HIGH, not blocker.** Half of round 2's blocker ground applies here: the rule is false for the one
member of the population it names. The other half does not. This label keys nothing, names no file and
gates nothing: unit 13 is report-only (S2), and unit 8's kinds decide no verdict. The defect misreports
a run. It does not corrupt a key or wedge a landing, and the fix is one predicate shared by two units.

**Fix.**

1. Strike "a run that built nothing" from both units. Correct unit 13's §1 and §4, and unit 8's §4, to
   six merged records, citing the missing witness write in `verb_close`.
2. In unit 8, decide `no-progress` from the run's own commits, which the model already holds (S3):
   `no-progress` means no own commit after the run's start commit (S1). A witness at or behind its base,
   when the run has merged own commits, reads `nonterminal-merged`.
3. Unit 13 has no model, and within its three git calls (S5) it cannot see a run's own commits. Choose one
   of two routes and say which. It can read a witness at or behind its base as `unjudgeable`, with the
   reason "witness not re-written since preflight", counted separately and printed in the detail row.
   Or it can spend a declared fourth call on one log over the tracked run-state paths, judge from the
   last commit that touched each record, and restate S5.
4. Give unit 13's AC3 and unit 8's AC5 a fixture shaped like dRatifiedSeam: phase LANDING, witness equal
   to base, own commits merged. Unit 8 must read it `nonterminal-merged`, never `no-progress`. Unit 13
   must count it, or report it `unjudgeable` if it took the first route.

**Left-shift.**

- Round 2 wrote the synthesis rule this breaks, and then broke it: *a fix a review proposes that names a
  derivation is run over the population it claims before the review is recorded.* Round 2 ran the
  predicate half (witness equals base) and not the half the label asserts (built nothing). The sharper
  form: *a label that asserts a cause is measured against the evidence for that cause, not against the
  predicate that triggers it.*
- A gate. Each self-test builds its run-state fixtures from the driver's real verb sequences, here
  preflight followed by close with no `--phase`, rather than typing `witness:` lines by hand. This is
  the class `memory/gotchas/staged-break-substitutes-a-synthetic-value.md`.
- A gotcha record, anchored on every reader of the `witness:` field: *the witness is HEAD at the last
  witness-writing verb, and `--close` is not one.*

---

### H2 — HIGH — unit 8 §2 S2, the window-end bullets, with S1 and §6 AC1, AC16 — raw 74

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** The window-end rules read each run-state path's history as the history of one run. S1
itself says the opposite. Rotation keeps the path: `verb_preflight` runs `git mv -f` on the finished
record (`tools/unattended/unattended.sh:2658`) and re-scaffolds `RUN.md` at the same path (`:2686`). Only
a terminal record rotates (`:2568`). So `RUN.md`'s history carries each predecessor's terminal phase.

Two of the six rotated builds landed twice in a row, and each shows the problem. Re-derived here:

| build | `RUN.md` first reads `phase: LANDED` at | the rotation, which is the live run's start | the live run's own terminal write |
|---|---|---|---|
| aPacedTurnstile | `be6423b7`, 2026-08-19 | `2d03cb5a`, 2026-08-20 | `43a6c13e` |
| dUnstalledConvoy | `fcaeac2d`, 2026-08-21 | `02f8495e`, 2026-08-24 | `92cf4b02` |

Read literally, "for a terminal record, the commit that first wrote its terminal `phase:` into the file"
ends both of these live windows before their start commits.

Archives go wrong a different way. Every archive is terminal, so the terminal bullet applies before the
archived bullet. Read on the archive path without `--follow`, as S1 reads that path, the terminal bullet
returns the commit that added the archive. That is the rotation commit. For dUnstalledConvoy it comes
three days after the real terminal write, and it is also the successor's start commit. The archived
window and its successor's window then share a commit. S2 does not say windows are half-open, so this
contradicts AC1's "their windows are disjoint".

**Impact.** On rotated builds, the window is wrong, and the window is the base of everything unit 8
builds:

- The two live runs above get empty windows, so their timelines, coverage, owner positions, cost and
  attribution are empty.
- All six archived runs stretch to the rotation commit, and the gap between the terminal write and the
  rotation lands in the wrong run.
- Unit 9's integrity commitment is computed over the lines attributed to each run, so these errors reach
  committed records.

AC1 and AC16 stage only unrotated or non-terminal fixtures, and AC7's aLeakedHandle never rotated, so
every criterion passes.

**Why HIGH, not blocker.** No criterion of this build is left unable to pass, and no committed key
moves. The fix bounds a read the design already makes.

**Fix.** Bound every read of a path's history to the run's own interval: from its start commit (S1) up to
the next start commit. Read an archive's terminal write from `RUN.md`'s history inside that interval,
since the archive's bytes lived at `RUN.md` until rotation. State windows as half-open, `[start, end)`.
Add to AC16 a LANDED-after-LANDED fixture, rotated the way the driver rotates. Assert that the live window
runs from the rotation commit to the live run's own terminal write, and that the archive's window ends at
its own terminal write, before the rotation.

**Left-shift.**

- A real-population arm. Unit 10 S6 already derives every tracked run's start commit. Extend it to derive
  every window, and assert that each ends at or after its start and that windows within one build are
  pairwise disjoint. On this tree it would red on the two builds above today.
- A spec-audit rule: *a rule that reads a path's history names which era of the path it reads, whenever
  the path is reused.*
- H2 and H4 can share one fix: an interval function over `derive_run_starts`.

---

### H3 — HIGH — unit 8 §4, the join paragraph, §2 S3 and §6 AC10; unit 3 §3; unit 11 §2 S2 and S6 — raw 42

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`,
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md`.

**The defect.** Unit 8 joins push lines to a run by worktree inside the window, and does the same for
gate lines no push pinned (§4 and S3; AC10 says "the run's own worktree"). Unit 3 §3 states the same
rule. Unit 4 records `wt` as the tree the push was made from. Unit 11 S6 lands every run by the
protocol's route: merge in the PRIMARY tree, then run `tools/push-main.sh` there. So the landing push's
`wt` is always the primary tree, never the run's worktree.

The landing bar's verdict is lost along with the push. Its `gate_run` can be reached only through a
joined push line. Nothing in unit 8 says a run spans its own worktree and the primary tree's landing.
Meanwhile unit 11 S2's third placement still says the re-render after `--landed` lets the record "gain
the landing facts".

**Impact.**

- This run's criteria still pass. AC6 reads `pushes.log` directly, and this run's post-landing coverage
  reads `partial` from the epoch alone.
- Every later landed run loses its push. If it pushes nothing from its own worktree, S7 finds no push
  line despite the run's activity and reads `pushes` as `dead`. If it does push from its worktree, it
  reads `present` without the landing push.
- The first case puts a false dead-writer signal into every such committed record. That teaches readers
  to discount the one state whose job is to flag a real dead writer.
- The re-render at unit 11's third placement gains nothing from the push journal.

**Why HIGH, not blocker.** The defect is wrong on the primary path of every later run, but it blocks no
criterion of this build, and the repair is a join rule.

**Fix.** Join a push line to a run by what it pushed, as well as by where it was pushed from: a `ref.<i>`
whose local sha is on the default branch and whose history contains the run's last own commit (see H1),
inside the window. Pull the landing gate line in through that push line's pinned `gate_run`. State in
unit 8 that a run spans its worktree and the primary tree's landing, and state in §4 what `pushes` reads
after landing. Carry the rule to unit 3 §3. Add an AC whose fixture lands from a worktree other than the
run's: the landing push and its pinned gate line join, and `pushes` does not read `dead`.

**Left-shift.** The class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`. The landing
route moved in rev-2, and the join written for the old route stayed in units 3 and 8. Round 2 found the
render-placement half of this (its H2), and this is the join half. The spec-audit rule: *when a spec
changes where an act happens, every join keyed on where is re-read.* Round 2's rule, that a criterion
observed at build end is walked on the route S6 selects, extends to consumers: unit 8 gains a fixture
built from S6's route.

---

### H4 — HIGH — unit 8 §2 S1 against S2; §6 AC1, AC9 and AC15 — raw 14

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** There are two ways of counting runs, and no rule joins them.

- S1 lists runs from git by start commit, and run k takes entry k.
- S2 starts a window at "the run's preflight START" and splits journal lines at successful preflight
  STARTs.

No rule says which journal START belongs to which git-derived run. The two lists have different lengths
in two cases. The first is a build whose early runs predate the journals and whose later runs have
STARTs. The second is a run made on another node, whose START sits in that machine's journal. Unit 9 §1
puts those at 30 of 50 runs. AC1 stages git alone, AC15 the journal alone, and AC9 a run with no START.

**Impact.** Matching the lists by position gives the first journal START to the oldest pre-journal run.
The windows and timelines then land on the wrong run. So does unit 9 S5's integrity commitment, which is
computed over "the journal lines attributed to this run". A committed record's runkey and its lines then
disagree, and no criterion can red.

**Why HIGH, not blocker.** The natural reading gives wrong committed records on mixed builds, but the
join is one missing rule and no criterion is left unable to pass.

**Fix.** State the join in S2. A successful preflight START belongs to the start commit its own call
made, which is the first start commit at or after its END within the slug. A START that matches no start
commit is named in coverage. Add an AC with three start commits in git history and preflights for only
the last two in `driver.log`. Assert that each START joins the right start commit and runkey, and that
the first run's window comes from git alone.

**Left-shift.** The spec-audit rule: *two enumerations of one population, taken from two sources, are
joined by a named key and never by position, and a criterion stages a population on which the two
sources disagree.*

---

### M1 — MEDIUM — unit 8 §2 S8; §6 AC17 — raw 15, 78

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** S8 attributes an event to "the unit and phase of the most recent driver START". Unit 2's
data model gives START the fields `verb slug wt kit pid phase_from oob sess.*`. `unit` and `phase_to` are
on END only. Read literally, no event ever gets a unit, and every event after `--phase X` carries the
phase before X.

S8 also leaves three cases open:

- Every keepalive fire runs `--status` in the same session, because unit 11 S3 says so and the
  scheduling store is session-scoped (`tools/unattended/unattended.sh:30-33`). So a START with no unit
  lands at every cadence tick. S8 does not say whether such a verb resets attribution.
- A killed verb has no END.
- AC17's fixture is typed by hand, so a START carrying `unit=` passes it.

**Impact.** On every run after this build, the attributed shares that the coverage block publishes
collapse, and nothing can red. A fixture in a shape the producer never writes grades nothing.

**Fix.** Attribute an event to the unit of the most recent unit-bearing END in the same session
(`--brief`, `--dispatch`, `--rescope` or `--review`), and to the phase of the most recent END's
`phase_to`. A START with no END contributes its `phase_from` and no unit. `--status`, `--resume` and
the other verbs that carry no unit do not reset the unit. Build AC17's fixture from the golden driver
lines in unit 1 §4, and stage a `--phase` move, a killed verb, and a heartbeat `--status` between a brief
and an event.

**Left-shift.** The runlog self-test asserts that every fixture line carries only the fields its
producer's data model lists: one field-set check per producer, beside the parse check unit 1 §4 already
runs over the golden lines. A START carrying `unit=` then reds.

---

### M2 — MEDIUM — unit 2 §4 Placement, third bullet; §6 AC2 — raw 18, 46, 50

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md`.

**The defect.** The fold of round 2's L4 widened §4's exit enumeration to both driver files, exempting
only `:74`, `:275`, `:276`, `:279` and `:310`, and the rev-3 log lists AC2 among the criteria it folded.
AC2's enumeration sentence did not change. It still reads "every `exit` after the install line in
`tools/unattended/unattended.sh`", the same text at `f698f6e6` and at `e1e83acf`, re-derived here. So
the criterion still grades the population L4 showed cannot see a verb body. Every `verb_*` function is
defined above the install at `:4925`, from `verb_phase` at `:2194` to `verb_close` at `:2914`.

§4's own two lists also disagree. Its marker-site list includes `:4973`, `:5009` and `:5015`, which are
`--plan` exits and are not journaled either. It leaves out `:5021`, the `--version` exit, as "not
journaled". The enumeration exempts only the five pre-install lines. `:5021` comes after the install
point and appears in neither list.

**Impact.**

- An unmarked exit added inside a verb body, or in `tools/unattended/lib-unattended.sh`, passes AC2. So
  §4's claim that such an exit "cannot slip past" has no criterion behind it.
- Built to the site list, the enumeration reds on `:5021` the first time it runs. Built to the exemption
  rule, `:5021` carries a marker the list says it does not.
- "Not journaled" cannot separate `:5021` from the `--plan` sites the list keeps.

**Fix.** Rewrite AC2's sentence to use §4's population and its exemption list. Add `:5021` to the
marker list and delete the carve-out sentence; a marker on an exit that is not journaled is harmless, as
the `--plan` sites already show. Stage RED with an unmarked `exit` inside a verb body above the install
line, and with one in `lib-unattended.sh`.

**Left-shift.** `memory/gotchas/fold-text-is-unreviewed-surface.md` names this shape: *a fold narrates a
revision that never happened.* Its practice applies: *verify a did-not-land claim by reading the BODY at
HEAD, never a revision log.* A mechanical form: for each rev-N log line that names an AC, the fold
record checks that `git diff` of that AC's text across the fold is non-empty. That check is report-only.

---

### M3 — MEDIUM — unit 2 §4 Placement, the END verb; §6 AC1 and AC13 — raw 76

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md`.

**The defect.** END "uses the parsed `VERB` and `SLUG`", and it reads `PH_SLUG` "for `--phase` only".
`VERB` starts empty (`tools/unattended/unattended.sh:4911`), and only the `--review` arm (`:4969`) and
the slug-verb arm (`:5026`) assign it. The `--phase` arm (`:5016-5020`) sets `PH_SLUG`, `PH_WANT` and
`PH_WIT` and exits inline without assigning `VERB`. So when the trap fires on the `--phase` exit, `VERB`
is empty. END writes an empty verb and cannot apply its own "`PH_SLUG` for `--phase` only" rule.

**Impact.** The design as written fails AC1's `--phase` END and AC13's `--phase` arm. The builder finds
this on the suite's first run, and then has to invent the repair.

**Fix.** Have END read the verb that START captured from `$1` at install, one value set once, so START
and END read the same source. Alternatively, have the `--phase` arm set `VERB=--phase`. Name the choice.
The first option is preferred because it leaves one answer to "which verb ran".

**Left-shift.** AC1 already checks every END nonce for a START. Extend that check by one field: every
END's verb equals its START's verb. The class is `memory/gotchas/spec-names-code-its-base-lacks.md`: the
spec names a variable its base does not set on one of the paths the spec covers.

---

### M4 — MEDIUM — unit 8 §2 S7; §6 AC6 — raw 16

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** Under S7, `partial` is a window that contains the epoch, and `present` needs a window
that starts after it. AC6's `partial` run sits in a journal that "holds only other runs' lines", so it
has no lines of its own. AC6's `present` run has no stated relation to the epoch. No fixture stages a run
that has lines of its own and a window containing the epoch. That is this run's own case: unit 8 §4 says
its `driver` and `gates` sources read `partial`.

**Impact.** An implementation that reads `present` whenever a run has lines of its own passes AC6. This
run's public record would then claim full journal coverage for a window that began before the writers
existed.

**Fix.** Add to AC6 a run whose window contains the epoch and which has lines of its own, and assert
`partial`. State that the `present` fixture's window starts after the epoch.

**Left-shift.** Round 2's rule for classifications also applies to states: *each state is staged on each
side of each boundary it names, including the combination the run under construction occupies.*

---

### M5 — MEDIUM — unit 6 §2 S8; §6 AC8 — raw 17

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md`.

**The defect.** The fold of round 2's M10 points every root at scratch and adds a check that "a sentinel
file planted in a decoy real state root is untouched". That check cannot fail, for three reasons:

- A new extract written into the decoy root leaves the sentinel byte-identical.
- The AC never places the decoy where an un-redirected root would resolve. With every S8 variable aimed
  at scratch, nothing ever reaches the decoy.
- A read changes no file, so the "reads" half of the Red-when has nothing to observe.

**Impact.** If the self-test forgets to redirect one S8 variable, it writes into the operator's real
profile rather than the decoy, and AC8 stays green. Round 2's M10 defect survives its fold.

**Fix.** Use two layers:

1. The launcher sets the ambient roots, `HOME`, `USERPROFILE`, `LOCALAPPDATA`, `XDG_STATE_HOME` and
   `CLAUDE_CONFIG_DIR`, to a decoy tree.
2. The self-test's own redirection sends each arm to scratch.

An arm that forgets a redirection then falls through into the decoy. Snapshot the decoy's recursive
listing (path, size and mtime) before and after each arm, and red on any difference. Plant a decoy
transcript with a unique session id under the decoy `CLAUDE_CONFIG_DIR/projects`, and red if any arm's
output or store names that id.

**Left-shift.** Two recorded classes cover this: `memory/gotchas/fixture-passes-by-finding-nothing.md`
and `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. The rule: *a sentinel
observes only what it is placed to observe; an isolation check lists the whole tree and plants a canary
for reads.*

---

### M6 — MEDIUM — unit 4 §2 S1 and S3; §4 data model and inventory; §6 AC1 and AC2 — raw 19

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md`.

**The defect.** The fold of round 2's H3 gave the three pre-loop refusals, at `:95`, `:102` and `:108`,
an `ev=once` line carrying the remote fields and `lander`. S3's rule for those fields (never a URL,
`remote=` only when `$1` differs from `$2`, and `remote_unnamed=1` and `url_userinfo=1` for a bare
credentialed URL) is observed only by AC2. AC2's pushes run through the stdin loop and write START and
END pairs. AC1 checks only `decision` and `wt` on the `:95` line, and never stages `:102` or `:108`. The
inventory names `write_push_start`, `write_push_end` and `resolve_push_dirs`, and no writer for the
`once` line.

**Impact.** A separate code path writes fields derived from `$1` and `$2`. On the refusal path, a
credential in a bare push URL can reach `pushes.log` while every AC stays green. This is the security
property round 1's H5 established for this unit.

**Fix.** Add an AC2 arm that pushes the credentialed bare URL with the default branch misconfigured, so
the push takes `:95` or `:102`. Assert that the `once` line carries `remote_unnamed=1`, `url_userinfo=1`
and `lander=`, and that no line contains `pass`. Name the `once` line's writer in the inventory, or
state that the function that writes START renders the remote fields for both lines.

**Left-shift.** Charter §9 already names this shape as a sibling write path carrying a partial guard.
Make the suite's credential assertion ("no line contains `pass`") run over the whole journal after
every arm, not only after AC2's own two pushes. One refusal arm uses the credentialed URL, so every path
that writes remote fields comes under the same check.

---

### M7 — MEDIUM — unit 13 §2 S3 table; §6 AC3 — raw 21

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md`.

**The defect.** AC3 stages "one fixture record per row of the S3 table". Row 1 covers retire or
supersede, and row 4 covers five shapes. Nothing requires a `rescope · item add` fixture or a supersede
fixture. So the fold's rule, that "the act of a `rescope` row is the first word of its item field", is
never observed failing.

**Impact.**

- If row 4's fixture is a `review` row, an implementation that maps every `rescope` row to
  `retired-unit` passes.
- If row 1's fixture is a retire row, an implementation that knows only retire passes.
- The tracked run-state files, re-counted here, hold 74 `rescope · item add` rows, 10 retire rows and 1
  supersede row. Such a build would misclassify real records, and nothing could red.

**Fix.** Stage `rescope` retire, supersede and add as separate fixtures, asserting `retired-unit`,
`retired-unit` and `other`. Add one item whose second word is `retire`, to pin "first word".

**Left-shift.** The spec-audit rule: *a table row that holds alternatives is staged once per
alternative; one fixture per row certifies the row, not its members.* It is a sibling of round 2's M5
rule, that a qualifier is staged by its negation.

---

### M8 — MEDIUM — unit 8 §2 S4, the first ledger bullet; §6 AC11 — raw 22

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** The fold of round 2's L5 limits run-state ledger rows to the four owed kinds, plus the
`rescope` rows whose act is owed. AC11 stages "one row from each ledger source", and all of those rows
belong in the ledger. No fixture holds a `proposal`, `dispatch`, `brief` or `review` row, or a `rescope ·
item add` row, that must stay out.

**Impact.** An implementation that admits every parked or rescope row passes AC11. On this tree's
tracked records, re-counted here, that would bring 216 review rows, 119 dispatch rows, 79 brief rows and
74 rescope-add rows into Decisions. The review rows would also be counted twice, once here and once from
the separate review-round source. Unit 9's Decisions counts would then inflate, which is the double
count L5 described.

**Fix.** Add one row of each excluded kind, plus a `rescope · item add` row, to AC11's fixture. Assert
that none enters the ledger and that the per-source counts equal the fixture's.

**Left-shift.** An allow-list is staged with its complement. §5 promises both directions for the closed
constants and not for this filter. Once M11 extracts the owed sets from the driver, the negative fixture
enumerates `PARK_KINDS` minus `PARK_KINDS_OWED` instead of a typed list.

---

### M9 — MEDIUM — unit 8 §2 S9, the closing sentence; §6 AC13 — raw 23

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** S9 ends with the stand-in "for a run with no START, its start commit (S1) stands in",
and no criterion observes it. Every AC13 case sits around a preflight START or a terminal END. AC9
stages a run with no START, but only for its window. A run from before the journals also has no
`--close` END, so its `in-window` and `post-close` boundary is not staged either.

**Impact.** The stand-in governs every pre-journal run with local transcripts, which is the whole
existing corpus on node `d`. A model that leaves those positions undefined, or classes every turn
`pre-run`, passes AC13. AC7's run has no local transcript.

**Fix.** Add an AC13 fixture run with no START. Its first turn, before the start commit, reads `launch`.
A turn after the start commit and before the window end (S2) reads `in-window`, and a turn after the
window end reads `post-close`.

**Left-shift.** Round 2's M7 rule, *a classification into N classes names its boundaries, and its
criterion stages a case on each side of each*, extends to stand-ins: *a stand-in is a boundary too.*

---

### M10 — MEDIUM — unit 1 §2 S1, §4 Files touched and §7; unit 3 §2 S6; unit 4 §2 S7 and §4 Files touched — raw 100

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md`,
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md`.

**The defect.** Several planned rows land in `tools/govkit/registry.toml`: unit 1's new `[[entry]]`
(`descriptor = "tools/runlog/kit.toml"`), and the `[[exempt_leg]]` rows the rev-3 fold adds in units 1, 3
and 4. Together they push the file past its recorded carried-prefix count of 59
(`tools/install-prefix-carried.txt:47`) and add `runlog` to that row's kit list. Since
TOOL-dRetiredFork-17, that file is a ban list: `--write-ratchet` may lower a count but never raise one.
Its header says a fourth-column reason is written by "only a person … in the pass that needs it".

No spec lists `tools/install-prefix-carried.txt`. Unit 4's Files touched also leaves out
`tools/govkit/registry.toml`, although its S7 adds a row there. Verification simulated the count rising
by one once `tools/runlog/` is tracked; that simulation was not re-derived here. (Narrowed by its skeptic:
the gate's printed ROSE remedy does point at the hand route, so "the remedy is refused" overstated the
case. The planned write set still fails its own gate.)

**Impact.** `install-prefix (shipped surface)` is in unit 1's own §7 gates, and it reds on unit 1's
first commit. The builder then meets a red nobody planned for, whose route is a hand edit of the ban
list. The route exists: aReapedSpinner's unattended run raised this same row from 58 to 59, with a
reason, at `862b56e9`.

**Fix.** List `tools/install-prefix-carried.txt` in the Files touched of units 1, 3 and 4. State the
hand raise of the registry row, and extend its existing reason, that the file is the declared deployable
population, to cover `runlog`, following TOOL-dRetiredFork-17 and the precedent at `862b56e9`. Name any
new kit-file rows with their reasons. The finding also names unit 12, whose Skill and README add CLI
lines; this synthesis did not re-derive that clause. Add `tools/govkit/registry.toml` to unit 4's Files
touched.

**Left-shift.** A report-only spec check: when a live spec's Files touched names a path that has a row in
`tools/install-prefix-carried.txt` and does not name that file, print both. The spec-audit rule: *a spec
that lists a gate in §7 has walked its write set through that gate.*

---

### M11 — MEDIUM — unit 8 §2 S4, the first ledger bullet; unit 9 §2 S4, the ledger-source vocabulary; unit 13 §2 S3 table — raw 101

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`,
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md`.

**The defect.** The rev-3 fold copies the driver's `PARK_KINDS_OWED` and `PARK_ACTS_OWED`
(`tools/unattended/unattended.sh:369` and `:382`) into unit 8 and into unit 9's `RECORD_SCHEMA`
vocabulary, and unit 13's table spells `PARK_KINDS` (`:355`) again in drift-audit. The reason given is
"named here because the kit may not read another kit's constants". The recorded rules say otherwise:

- `tools/hooks/README.md:150`: "A replicated policy value is extracted or rendered from the one file
  that owns it."
- A withheld self-test may name gov paths if its carried row gives a hand-written reason. Two rows do
  exactly that: `tools/run-gates/run-selftests.test.sh` and
  `tools/process-monitor/adopt-process-monitor.test.sh`.
- The driver's own comment at `:407-415` records this exact failure, one set with two spellings.

Round 2's left-shifts for L5 (an arm that parses both constants) and M6 (a PAIRS row) were not taken,
and no reason for dropping them is recorded.

**Impact.** When the driver adds an owed kind or act, three copies silently disagree with it: the
model's ledger, `RECORD_SCHEMA`'s closed vocabulary and unit 13's table. Unit 10's schema leg then
refuses the new rows, or the renderer drops them, and nothing reds at the driver edit.

**Fix.** Strike the "may not read" premise. Add an arm to the withheld `tools/runlog/selftest.py` and
`tools/drift-audit/selftest.py`. Where `tools/unattended/unattended.sh` is present, the arm extracts
`PARK_KINDS`, `PARK_KINDS_OWED` and `PARK_ACTS_OWED` and compares them, in both directions, with the
model's sets, `RECORD_SCHEMA`'s ledger sources and unit 13's table. Where the file is absent, the arm
announces its skip. Give the literal its carried-row reason.

**Left-shift.** The class is `memory/gotchas/two-answers-to-one-question.md`. The fold-record practice
applies: *re-derive every citation the fold writes.* The premise states a rule, and one read of the
hooks README refutes it.

---

### M12 — MEDIUM — unit 9 §2 S1; unit 10 §2 S1 and S6; unit 12 §2 S3, step 1; unit 8 §2 S1 — raw 103

**Files.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md`,
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md`,
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-12.md` and
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

**The defect.** The runlog kit ships to adopters through unit 1 S1's registry entry, yet every spec
addresses the memory tree by the literal `memory/builds/...`. The recorded convention is the declared
root: `MEMORY_ROOT` in `.memory-tree.conf`. It is `memory` here, and drift-audit reads it as
`ctx.memory_root`. `tools/drift-audit/drift_report.py:1486-1491` records that the root is not always one
path segment, and that `docs/mem` is a real adopter value. No spec in the set mentions `MEMORY_ROOT`
(re-derived by grep).

**Impact.** Take an adopter with `MEMORY_ROOT=docs/mem`:

- `record --write` creates a stray `memory/builds/...` outside that adopter's memory tree, where hygiene
  check 21 never binds it.
- The model finds no run-state file.
- Unit 10's leg grades an empty population as "0 records (none committed yet)" and exits 0.
- The renderer and the leg agree on the wrong root, so unit 10's liveness assertion cannot catch it.

**Fix.** Put one resolver in `runlog_lib` that reads `MEMORY_ROOT` from `.memory-tree.conf` and refuses
an empty result. Units 8, 9 and 10 use it, and unit 13 uses drift-audit's existing `ctx.memory_root`.
Unit 12's Skill takes the root as a render token. Add an arm with a two-segment root fixture.

**Left-shift.** The class is `memory/gotchas/vacuous-selector-empty-population.md`. A leg that takes its
population from a glob asserts that the glob's root exists and is the declared one. An empty population
under a wrong root then reds instead of reporting zero.

---

### L1 — LOW — unit 8 §2 S6, `no-progress` and `nonterminal-merged`; §6 AC5 — raw 24

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

S6 says "at or behind", and AC5 stages only a witness equal to its base. An implementation that tests
only equality passes, and it gives a strictly-behind witness, such as one from a stale worktree base, the
wrong kind or none at all. No fixture holds both a refused `--landed` and a last parked row that unit
13's table matches, so it is undefined whether `refused-landing` or the table sub-class wins. (Narrowed
by its skeptic: the precedence half is weaker, because unit 13 S3 says the table cannot see refusals.
The strictly-behind gap stands.) H1 redefines `no-progress`, and whichever rule survives needs these
fixtures.

**Fix.** Add a strictly-behind fixture. State the precedence between `refused-landing` and the table,
and stage one fixture that carries both.

**Left-shift.** Round 2's M7 rule: "at or behind" names two cases, and each is staged.

### L2 — LOW — unit 8 §2 S4, the decision-log bullet; §6 AC11 — raw 26

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md`.

The rule matches `(owner` followed by `)`, `,` or `:`, plus "owner ruling" and "owner call". AC11 stages
`(owner, 2026-09-01)`, bare `(owner)` and `Owner ruling`. It stages neither `(owner:` nor "owner call",
and each appears once in `memory/DECISIONS.md`, re-counted here. No near-miss negative stages the
"followed by" boundary, such as `(ownership`. The report-only arm S4 adds over the tracked log appears in
no AC, although S4 says it is "Observed by AC3 and AC11".

**Fix.** Add an `(owner: …)` row, an "owner call" row, and a near-miss that must not count. Assert that
the report-only arm prints one hit count per spelling.

**Left-shift.** *A report-only arm is still an arm.* It gets a criterion that it ran and printed.

### L3 — LOW — unit 10 §2 S6, the cost clause; §6 AC4 — raw 27

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md`.

S6 claims "one extra git call for the whole population" to derive start commits. AC4 varies only the
number of `-runlog-` records, 1 against 100, not the number of builds carrying `RUN*.md`. Unit 8 S1
defines `derive_run_starts` per build. So a `git log --diff-filter=A` call per build passes AC4, and the
cost claim goes unobserved on a leg whose ceiling `tools/gate-legs.json` declares.

**Fix.** Make AC4's two fixture indexes also differ in the number of builds with run-state files, for
example 1 and 50, and assert equal git-call counts. Name the single population-wide log call in S6, and
give `derive_run_starts` a population form in unit 8.

**Left-shift.** *A cost claim names its scaling variable, and its criterion varies that variable, not a
neighbouring one.*

### L4 — LOW — unit 2 §4 Placement, the START slug grammar — raw 84

**File.** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md`.

§4 says the grammar `check_slug` enforces is "bounded at 64". `check_slug`
(`tools/unattended/unattended.sh:1060-1071`) has no length bound, re-derived here. Moving a 64-character
bound into the shared predicate adds a refusal to every slug verb, which §3's non-goals forbid. Keeping
the bound in START alone makes the second grammar §4 says it avoids.

**Fix.** Drop the bound, or record it as a deliberate new refusal with its own arm.

**Left-shift.** `memory/gotchas/spec-names-code-its-base-lacks.md`. A spec's claim about how an existing
function behaves is checked against that function at base. For a property rather than an identifier this
stays a documented reviewer check.

---

## Classes across the set

**The fold is again the dominant source, and the round-2 record supplied the worst premise.** Sorted by
origin, the 26 raw findings are:

- 19 in text the rev-3 fold wrote;
- 2 where the fold answered a round-2 finding only in part;
- 3 in rev-1 or rev-2 text that no round flagged;
- 2 that straddle.

That makes 21 of 26, against 24 of 36 in round 2. The shapes `memory/gotchas/fold-text-is-unreviewed-surface.md`
names all recur:

- a fold narrates a revision that did not happen (M2, where AC2 is logged as folded and is unchanged);
- a fold writes a premise it did not re-derive (M11's "may not read another kit's constants"; L4's
  bound is the same shape, from the rev-2 fold, and round 2 missed it);
- a fold answers one half of a finding (M5, where the sentinel isolates writes and observes neither);
- an amendment leaves its other half standing (H3).

The sixth shape that round 2 proposed also recurs. H1 is a fold carrying out a premise the review stated
in its own voice. This time the review had even written the rule against it. Its B1 left-shift said a
fix naming a derivation is run over its population before the review is recorded. Its H4 ran only the
predicate half. That supports adding the shape to the gotcha record, with this round as its second
instance.

**Run-state facts read as properties of the run, when they belong to the last verb that wrote them.**
Round 2's blocker was that rotation keeps `RUN.md`'s path. The fold fixed where runs start and left where
they end (H2). H1 is the witness version of the same mistake: the field is HEAD at the last verb that
writes it, and `--close` does not write it. Both would be caught by building fixtures from the driver's
real verb sequences instead of typing run-state lines by hand. A gotcha record anchored on the model and
on drift-audit's run-record reader should name both facts.

**Joins specified from one source's side.** H3 joins on worktree while the landing happens in another
tree. H4 has two run enumerations and no key between them. M1 reads a field from the line that does not
carry it. The model's value is its joins, and each of these was written looking at one source. The
spec-audit rule under H4 covers all three: *name the join key, and stage a population the two sources
disagree on.*

**Criteria that stage one side, still.** M4, M7, M8, M9, L1, L2 and L3 each observe a neighbouring case
of the rule their scope item names: one fixture per row instead of per alternative, positives without the
complement, "equal" standing in for "at or behind". This is round 2's "Observed by ACn, where ACn
observes something else" class, and the fold's new criteria reproduced it.

**Recorded rules not consulted, again.** H1 cites TOOL-cFinalBerth-2 for a comparison it does not make.
M11 contradicts the replicated-value rule in `tools/hooks/README.md`. M10 does not plan for
TOOL-dRetiredFork-17's ban list. M12 does not follow the `MEMORY_ROOT` convention that drift-audit
records. Round 1 named this class. Round 2 found it in five items, and this round finds it in four.

**The lenses' yield is falling.** Precision went 0.58, 0.55 and then 0.25, and 80 of this round's 106
raw findings were refuted. The confirmed set still changes code: all four HIGH items would produce wrong
records. But the share of raw findings that survive a skeptic has fallen by more than half, so each
confirmed finding now costs more than twice the skeptic work it did. `AGENTS.md` §8 says to tighten scope
and priming before adding agents. For the closing diff review of this build, that means priming the
lenses with the four HIGH folds, not the whole set.

## Disposition

Under `memory/guides/BUILD-METHOD.md` M4, this round's clean-with-fixes verdict ends the spec audit.
Fold the twenty items, with a rev bump and a §9 line on each spec touched, and do not re-review them as a
spec audit. The closing diff review (M8) is then the first to see the fold, and it will see it as code.

This round's evidence says the fold owes itself two checks before it commits, and neither needs an agent:

1. Run every fix that names a derivation or a population claim over the tracked population, and record
   the output in the spec's §4. That covers H1's progress rule over the seven non-terminal records, H2's
   windows over the six rotated builds, H4's join over any build with both git and journal runs, and
   M7's and M8's counts. This is the check round 2's H4 skipped.
2. For each rev-4 log line that names an AC, confirm `git diff` shows that AC's text changed (M2's shape).

## What this synthesis re-derived

- The thirteen blob shas at HEAD `e1e83acf`; that no file under `tools/` or `.githooks/` differs from
  base `9fac2b53`; and that units 5, 7 and 12 differ from their round-2 blobs only by one generated
  records row.
- These lines in `tools/unattended/unattended.sh`:
  - the four witness writers at `:2237`, `:2415`, `:2541` and `:2750`;
  - `verb_close` writing only `phase LANDING` at `:3037`;
  - the recorded-base refusal at `:988-990` and its call in the `authorization-reachable` item at
    `:3059-3074`;
  - the `--phase` arm at `:5016-5020`, and the only `VERB` assignments, at `:4911`, `:4969` and `:5026`;
  - every `exit` from `:4973` to `:5059`;
  - `check_slug` at `:1060-1071`;
  - `PARK_KINDS`, `PARK_KINDS_OWED` and `PARK_ACTS_OWED` at `:355`, `:369` and `:382`, and the
    two-spellings comment at `:407-415`;
  - the rotation gate at `:2568`, the move at `:2658` and the re-scaffold at `:2686`;
  - the session-scoped keepalive comment at `:28-33`.
- dRatifiedSeam's phase, witness and base; its `RUN.md` history; its brief, dispatch, review and
  override rows; and the ancestry to `origin/main` of `26c52ba1`, `532e6f2b`, `fe285844` and `4f268bce`.
- The base-against-HEAD table in the cFinalBerth-2 spec at the cited lines.
- The archive and live phases of all six rotated builds. For aPacedTurnstile and dUnstalledConvoy, the
  first `phase: LANDED` write in `RUN.md`'s history, the rotation commit and each live run's own terminal
  write. That aLeakedHandle never rotated.
- The phase, witness and base of all seven non-terminal records at HEAD.
- AC2's enumeration sentence in unit 2, byte-identical at `f698f6e6` and `e1e83acf`.
- The carried-prefix row for `tools/govkit/registry.toml` (count 59, its reason and the raise at
  `862b56e9`, a run with a `RUN.md`), the ban header, and the carried rows of the two withheld suites M11
  cites.
- The replicated-value rule at `tools/hooks/README.md:150`.
- `MEMORY_ROOT=memory` in `.memory-tree.conf`, `tools/drift-audit/drift_report.py:1486-1491`, and the
  absence of `MEMORY_ROOT` from all thirteen specs.
- The parked-row kind and rescope-act counts over the tracked run-state files, and the owner-spelling
  counts in `memory/DECISIONS.md`.
- The rev-2 absence of the clauses classified `fold`, checked by grep at `f698f6e6`, and the rev-1 and
  rev-2 text of the clauses classified `missed` or straddling.
- The `gotchas.py --for-diff 04a4e5af..e1e83acf` selection, which picks two anchored classes and five
  universal ones. Four of them name shapes confirmed here: `fold-text-is-unreviewed-surface`,
  `amendment-leaves-its-other-half-standing`, `two-answers-to-one-question` and
  `staged-break-substitutes-a-synthetic-value`.

## What this pass did not cover

- The 80 refuted findings are not reproduced or characterized here.
- Units 5 and 7 drew no confirmed finding, and unit 12 drew one only as a carrier of M12. Nothing found
  there is not the same as sound.
- Three things come from verification and were not re-derived. The first is M10's simulated count rise
  and its unit 12 clause. The second is how many git calls a hypothetical per-build `derive_run_starts`
  would make (L3). The third is which driver version dRatifiedSeam closed under: H1 cites today's driver
  for the recorded-base refusal.
- No code exists yet. The specs were audited against tool and hook files byte-identical to base
  `9fac2b53`.
- No finding reopens the owner's 2026-09-13 rulings in the README. H3 is about joins, not about the
  landing route that unit 11 S6 records.
- The worktree's index held staged edits this synthesis did not make: a build-brief prompt and the
  records rows that bind it. This synthesis read every subject at HEAD, where each blob matches its pinned
  sha, and it staged nothing.
- This record is not yet bound into the build index. The specs' records regions and the README's records
  line need re-rendering in the commit that lands it, as they were for rounds 1 and 2.

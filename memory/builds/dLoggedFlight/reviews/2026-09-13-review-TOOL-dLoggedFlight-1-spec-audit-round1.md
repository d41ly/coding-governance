**Serves:** spec-audit TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13

# dLoggedFlight — spec audit of the thirteen-unit set, round 1

*Node `d`, 2026-09-13, on `branch/unattended-build-transparency-ea83a5` at HEAD `1dd6f3da`, against the
specs' stated base `9fac2b53`. No file under `tools/` or `.githooks/` changed between those two commits,
so every line number a spec cites at base holds at HEAD. A Tier-2 adversarial pass: four primed finder
lenses, a skeptic stage of five batches prompted to REFUTE each finding, and one synthesis, which is this
record. The synthesis re-derived against the tree every claim it states in its own voice: the thirteen
blob shas; the trap block at `tools/run-gates/run-gates.sh:1041-1044` and its post-trap `exit 2` sites at
`:1093` and `:1182`; every exit and git-dir resolution in `.githooks/pre-push`; the worktree `commondir`
contents and the primary tree's lack of one; the owner-ruling text in `tools/unattended/kit.toml`; every
`memory/DECISIONS.md` row cited; `render()` and the placeholder defaults in
`tools/unattended/adopt-unattended.sh`; `check_slug`; the drift-audit `Git` helper; the aLeakedHandle
parked-row count; and the owner-spelling counts in the decision log. It also re-ran three shell probes
rather than trusting their verdicts: the double `cleanup` (H1), `-nt` against a missing file (M5), and
signal deferral under a trap (M18). A figure that came from verification and was not re-derived here says
so where it appears.*

**Reviewed subjects, each pinned at the blob it was read at — ROUND 1:** `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md@ac3a76727dd34150c5334bbcfdf0be5a5afa75fd`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md@f40cb7d29cdd4e3e2796e59743e2efd8005b8761`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md@3dd64b93e3b116acda4a66c8b8c87d2d168a0083`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md@94a9ecb4bb5c34854f520004ebc811413c4b7a6e`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-5.md@4aeabb437bfd846f21ae093f7ef3f8785b59c1a4`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md@d91879f04695ee7ef277975c09203f4ba2ea5848`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-7.md@6b47d81ffcfc9a348ddec0fc7c3c5140d9b6c443`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md@347cf9a1f07882f4c2ba516e9d04860af90568ae`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md@1bf7ff0ba9c25423ec02428a477ab217996669c8`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md@09e34f816ef87e0d07fce7e5e458d0f8a327a31b`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md@8bf9fe1ff3c10e0d6d72ab6926a2c681978783f9`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-12.md@9d2e0f240c017790187215fceb6a34c32ab895a2`, `memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md@ae1e2da1cfc1bbbe79dfddd82d61849c71e51b6e`.

## Verdict: BLOCKED

Four blockers stand, in four different places, and two of them land on the same acceptance criterion.
Unit 11 AC5 is the build's only end-to-end observation: this run renders and commits its own record, and
unit 10's schema leg grades it at the push. As written, that record has no filename, because unit 9
derives the name from a preflight nonce this run never wrote (B2). Its mandated sections are refused by
the allow-list meant to admit them, because unit 9's closed schema omits every value class its own
`## Coverage`, `## Decisions` and owner-turn rows are made of (B3). A third, independent reason sits at
medium: the push the criterion is observed at has no route on which the bar actually runs (M20).

The other two blockers are local. Unit 8 defines `dead` in a way its own AC6 and AC7 cannot both satisfy
on this tree once unit 2 lands, and the missing rule decides what every committed record's coverage block
says (B1). Unit 2 puts an unattended self-test on the merge bar and into the adopter payload. The
2026-08-23 owner ruling and the closed TOOL-aQuenchedHarness-3 both removed exactly that, and the spec
cites neither (B4).

Ten highs sit beside them, and the dominant shape is one this repo has filed before: a scope item that
says "Observed by ACn" where ACn observes something else. Eight items are that shape outright, and two
more carry it in a clause. The second cluster is a spec that reads the tree it cites wrongly at a named
line. Unit 3's claim about how its signal traps exit is false, and building on it writes two lines for
every killed bar (H1). Unit 4 takes a git dir from a line that runs after the point where it is needed,
and names no fallback for the primary tree the lander pushes from (H2). The third cluster is a figure
graded against the node instead of the subject: five absolute wall-clock floors inside held self-tests
contradict TOOL-cSteadyMetronome-1, and two of them cannot see their own stated failing case (H9).

The design is not in dispute. One grammar and one reader, producers that spend no process on the hot path
(unit 2's xtrace exec-count criterion is the right instrument and the set should use it more widely), a
closed public schema enforced twice, and a report-only drift signal whose §4 reasons about the owner's
worktree landings correctly: none of that needs revisiting. What fails is the joins between units, and
the observation of what each unit promises.

## Run integrity

- lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.

Every counter is zero, so the run is complete in the only sense the orchestration can certify: every lens
reported and every finding reached a skeptic. A complete run is still not a clean bill. The 53 confirmed
findings are a lower bound on the defects in this set, not a census of them. The pipeline's duplicate
count is zero because it discarded nothing as a duplicate. The folding below is this synthesis grouping
DISTINCT findings that describe one defect from different lenses, and every raw id stays named in the
header of the item that absorbed it.

## Review shape

- raw 92, confirmed 53, refuted 39, unverified 0, precision 0.58.
- Adjudicated in this report: **4 BLOCKER, 10 HIGH, 21 MEDIUM, 3 LOW**, over 38 items. Counted by raw
  finding instead of by item, the same split is 8, 17, 25 and 3.
- Nine folds take 24 raw findings into 9 items: B1 (4, 33, 66), B2 (5, 31, 59), H1 (1, 36, 55), H2 (11,
  34, 56), H3 (2, 43), H9 (75, 78, 79), M1 (9, 44, 61), M4 (14, 50) and M12 (23, 40). The other 29 are
  one item each. Raw 14 carries a second clause about the key pattern; it corroborates H4 and is counted
  once, under M4.
- Four items were raised to BLOCKER at adjudication, and each item states its ground. B1 was filed high,
  high and medium, and B2 high three times. B3 and B4 were each filed high. The grounds are, in order: a
  pair of criteria that cannot both pass, a landing criterion with no input, a closed schema that refuses
  the sections it mandates, and a criterion satisfiable only by reversing a standing owner ruling.
- A fold takes the highest filed severity among its members. That raised raw 36, 11, 34, 43, 78 and 79
  from medium to HIGH, and raw 44 and 50 from low to MEDIUM. No finding was lowered.
- Precision 0.58 clears the ~0.5 threshold in `AGENTS.md` §8. This synthesis received the survivors only,
  so it does not characterize the refuted 39.

## Findings

| # | Sev | Unit | Address | One line |
|---|---|---|---|---|
| B1 | BLOCKER | 8 | §2 S6, §6 AC6 and AC7, §4 | `dead` has no epoch, so AC6 and AC7 cannot both pass once unit 2 lands |
| B2 | BLOCKER | 9, 11, 8 | 9 §2 S1, §5 · 11 S5/AC5 · 8 §4 | the runkey comes from a nonce this run and every pre-build run lack |
| B3 | BLOCKER | 9, 10, 11 | 9 §2 S4 against S3 · 10 §2 S2 | the closed allow-list omits the values the mandated sections are made of |
| B4 | BLOCKER | 2 | §2 S10, §4 Inventory, §6 AC9 | an unattended self-test goes on the bar and to adopters, reversing a ruling |
| H1 | HIGH | 3 | §2 S1 and S3, §4 ¶1, §6 AC3 | `cleanup` runs twice on every signal, so a killed bar writes two lines |
| H2 | HIGH | 4, 3 | 4 §2 S1 and S5, §4 ¶2, §6 AC5 · 3 §2 S4 | no git dir exists where START is written, and no primary-tree fallback |
| H3 | HIGH | 1, 2, 3, 4 | 1 §2 S2 against §6 AC2 | the journal location contract is observed by no criterion anywhere |
| H4 | HIGH | 1, 2, 6 | 1 §4 key row · 2 §4 START · 6 §2 S1 | the key grammar rejects its own example and its main producer's keys |
| H5 | HIGH | 4 | §2 S1 and S2, §5, §6 AC2 | a push to a bare URL writes the credential as the remote name |
| H6 | HIGH | 8 | §2 S2 against §6 AC2, §4 ¶2 | the timeline joins, the model's core, have no criterion |
| H7 | HIGH | 6 | §2 S3 and S4 against §6 AC2-AC4 | usage dedupe, six event kinds, the tool classes and both flags are unobserved |
| H8 | HIGH | 5 | §2 S2 against §6 AC1 | nothing ties the enumerated secret classes to rows of the table |
| H9 | HIGH | 1, 5, 6, 8, 10 | AC4, AC4, AC8, AC8, AC4 | absolute wall-clock floors as RED conditions, against a recorded decision |
| H10 | HIGH | 6 | §2 S8, §6 AC8 | a self-test graded over the operator's private transcript store |
| M1 | MEDIUM | 3 | §3 bullet 3, §4 ¶2 | the exit table misplaces `:1093` and omits `:1182` |
| M2 | MEDIUM | 3 | §2 S2 | the `run` key's exact join and the `fail.<i>` cap are unobserved |
| M3 | MEDIUM | 4 | §2 S1 `lander` | only `lander=1` is defined; unit 8 keys on `lander=0` |
| M4 | MEDIUM | 1, 4 | 1 §4 length and unknown-key rows · 4 §2 S1 | the 2048-byte cap has no owner, and twenty refs overflow it |
| M5 | MEDIUM | 2 | §2 S5, §6 AC4 | `-nt` is true with no stamp, so a first call reads `oob=1` |
| M6 | MEDIUM | 8 | §2 S5 | two anomaly kinds and one sub-class set are defined nowhere |
| M7 | MEDIUM | 8 | §2 S4 | four of five conformance items have no rule and no criterion |
| M8 | MEDIUM | 8 | §2 S3 against §6 AC3 | four of six ledger sources are unobserved |
| M9 | MEDIUM | 8 | §2 S3, the decision-log split | `OWNER RULING` is the minority spelling of an owner ruling |
| M10 | MEDIUM | 5 | §6 AC3 against §2 S4 | the literal-credential grep is narrower than the property it guards |
| M11 | MEDIUM | 7 | §6 AC3, §2 S1 | AC3 never reads M10, and M10 never places the trailer |
| M12 | MEDIUM | 13 | §2 S1 against S5, §6 AC1 and AC4 | two git calls cannot read file contents at HEAD |
| M13 | MEDIUM | 4 | §4 exit list against §2 S3 and §3 | five refusal exits before the stdin loop are unlisted |
| M14 | MEDIUM | 8, 6, 9 | 8 §2 · 6 §3 · 9 §2 S4 | the owner-turn position classes have no producing unit |
| M15 | MEDIUM | 12, 8, 6 | 12 §1, §2 S2 and S3 · 8 §2 | the Skill promises cost answers the model never carries |
| M16 | MEDIUM | 9 | §2 S6 against 10 §2 S2 | no overflow rule for sections that are never elided |
| M17 | MEDIUM | 4 | §2 S5, §6 AC5 | the stderr line on a failed write is dropped |
| M18 | MEDIUM | 2, 4 | 2 §2 S2, §3, §4 · 4 §2 S3 | a trapped signal waits for the foreground child, up to an hour |
| M19 | MEDIUM | 11 | §2 S1, §5, §6 AC1, §10 | a blank rendered key, on a precedent that is not one |
| M20 | MEDIUM | 11 | §2 S5, §6 AC5 | the push AC5 is observed at is refused, or bypassed, on the sanctioned route |
| M21 | MEDIUM | 7 | §3 bullet 3, §7 | shipped memory-tree bytes move at an unchanged version |
| L1 | LOW | 2 | §4 Placement, the START slug | a second slug grammar, narrower than `check_slug` |
| L2 | LOW | 12, 11 | §3 Edges | consumed interfaces missing from the edge graph |
| L3 | LOW | 9 | §5 perf / scale | the stated render ceiling is observed by nothing |

---

### B1 — BLOCKER — unit 8 §2 S6, §6 AC6 and AC7, §4 ¶1 — raw 4, 33, 66

**The defect.** S6 defines `dead` as "a source with zero lines while the run's own rows prove activity",
and AC6 pins it: twelve parked rows beside an empty `driver.log` read `dead`, not `absent`. AC7 requires
`runlog.py model aLeakedHandle --json` to report that run's journal sources as `absent` "on this tree".
aLeakedHandle carries 22 parked rows (counted here) and no journal lines. Unit 8 is order 8. By the time it
is built, unit 2 has landed on this branch and this run's own later verbs have written `driver.log` into
the shared common dir. That file exists and holds zero aLeakedHandle lines, beside 22 rows proving
activity, which is AC6's shape exactly. Read per run, S6 yields `dead` and AC7 reds. Read per file, AC6
and AC7 agree, but then a writer that died during one run reads `absent`.

§4's premise ("the corpus's first 50 runs have no journals at all") stops being true on the building node
the moment unit 2 lands. Nothing in the spec separates "this run predates the writer" from "the writer
died". This synthesis adds one case the findings did not name: this run straddles the writers' landing, so
its window contains the first line each journal ever received. None of the four states describes a source
that started mid-window, and this run's own committed record will need one.

**Why blocker.** The two criteria cannot both pass. The implementer must therefore invent the missing rule,
and that rule decides what the coverage block, which §5 calls "the model's own liveness statement", says
in every committed record unit 9 renders.

**Fix.** Give S6 an epoch per source: the time of the first line in that producer file, or the landing
commit of that producer's writer, which is tracked and survives journal loss. A run whose window ends
before the epoch reads `absent`. A run whose window starts after it, with zero lines, reads `dead`. A
window that contains the epoch gets a named fifth state, such as `partial`, carrying the epoch, or the spec
says which of the four it takes. Restate AC7 as "`absent` because the window predates the epoch", and add
a fixture pair over one journal that holds only other runs' lines, once for a window before its epoch and
once for a window after.

**Left-shift.** A model self-test arm that pins the coverage state of a pre-writer run and a post-writer
run over the same fixture journal. The class is already catalogued as
`memory/gotchas/two-guards-one-question-two-answers.md`. It did not fire for this audit because the
spec-set diff touches only `memory/builds/`; see "Classes across the set" for the measurement and the
fix. The spec-audit rule to add beside it: *an acceptance criterion observed "on this tree" is evaluated
against the tree as it will stand after every earlier-ordered unit has landed, not against the base.*

---

### B2 — BLOCKER — unit 9 §2 S1 and §5; unit 11 §2 S5 and §6 AC5; unit 8 §4 — raw 5, 31, 59

**The defect.** S1 names each record `…-runlog-<runkey>.md`, where `<runkey>` is "the first 8 hex of the
sha256 of the run's preflight nonce". A nonce exists only in unit 2's driver START line. The run-state
file carries none: this run's `## Run facts` hold `witness`, `phase`, `branch-sha`, `branch-ref`, `mode`,
`anchor-kind`, `keepalive`, `anchor-url`, `anchor-sha`, `anchor-ref` and `base`. This run's preflight was
committed at `2f11f32d`, before any writer existed, so its preflight START line will never exist. §5
nevertheless says a run with no journals renders "from its run-state file and git". Unit 11 S5 and AC5
require this run to render and commit its own record. Unit 8 §4's window starts at "its preflight START,
or its first parked row", and this run has neither: its `## Parked` section is still empty.

**Why blocker.** The one record the build must produce to satisfy its own landing criterion has no input
for its filename. Every run before the writers is unrenderable as specified, and `record --write` either
cannot name the file or hashes nothing and collides.

**Fix.** Derive the runkey from a tracked fact that is fixed at preflight, never rewritten, and unique per
preflight. The commit that created the run-state file meets all three, and a rotation is a `git mv` that
`--follow` reaches. `base:` and `anchor-sha:` are fixed but can repeat when a run is aborted and restarted
before either ref moves. `witness:` must not be used, because it moves with every phase: this run's own
file shows it moving from the preflight commit to `1dd6f3da` at REVIEWING. Keep the nonce as a refinement
or drop it. Add a journal-less fixture to AC1, state this run's key in unit 11 S5, and give unit 8 §4 a
window-start fallback: the creating commit's time.

**Left-shift.** AC1's journal-less fixture is the gate. The spec-audit rule: *a derived identifier names
its input for every population the spec says it serves.* §5 says journal-less runs render, so the
population list alone would have exposed the missing input.

---

### B3 — BLOCKER — unit 9 §2 S4 against §2 S3; unit 10 §2 S2; unit 11 §6 AC5 — raw 32

**The defect.** S4 says the record carries ONLY verb names, phase names, check numbers, anomaly kinds,
conformance states, shas, this build's unit ids, integers, durations, UTC timestamps, repo-relative paths
of tracked files, and workflow labels. S3 then mandates sections built from values outside that list:

- `## Coverage` is made of `present`, `absent`, `dead` and `not-local`, and of source names;
- `## Decisions` is "counts per ledger source", so it holds ledger-source names;
- S4 itself mandates owner turns "as counts per position class", so it holds `launch`, `pre-run`,
  `in-window` and `post-close`;
- a timeline carrying gate and push lines needs verdict tokens (`GREEN`, `RED`, `REFUSED`, `NONE`) and
  push decisions.

Unit 10 S2 refuses "a cell outside the allow-list". A correctly rendered record is therefore refused by
the leg, and unit 11 AC5, where this run's record passes that leg at landing, cannot pass.

**Why blocker.** `RECORD_SCHEMA` is the security control both enforcement points share, and it is
inconsistent as specified. Resolving it means deciding what else a PUBLIC record may carry, under a
build-level rule the owner ruled on 2026-09-13. That is a design decision a builder should not make while
debugging a red leg.

**Fix.** Enumerate each missing class in S4 and in `RECORD_SCHEMA` as a CLOSED vocabulary, never a free
label: coverage states, source names, ledger-source names, owner-turn position classes, gate verdict
tokens, push decision tokens and conformance item names. Make unit 10 AC1's clean fixture carry one value
of each class.

**Left-shift.** Produce unit 10 AC1's clean fixture with unit 9's `render_record` from a model fixture that
populates every S3 section, instead of hand-writing it. A render-then-grade arm turns any renderer-versus-leg
disagreement into a red. Unit 10 §4 already promises that ("a disagreement between the two is itself a
finding"), and it currently has no arm.

---

### B4 — BLOCKER — unit 2 §2 S10, §4 Inventory and Files touched, §6 AC9 — raw 74

**The defect.** S10 and AC9 put the new `tools/unattended/runlog-writer.test.sh` on the merge bar as a held
`kit`/`selftests` leg in `tools/gate-legs.json`. `tools/unattended/kit.toml:109-114` records the opposite
as an owner ruling: "THIS KIT'S SELF-TESTS ARE NOT GATE LEGS, and that is an owner ruling rather than an
omission", ending "they run on the owner's demand, never on the merge bar, here and in every adopter
alike". `tools/run-gates/selftest-budgets.txt` carries six unattended suites that appear in NEITHER
`tools/gate-legs.json` NOR `tools/unattended/kit.toml` for that reason, and `AGENTS.md` names unattended as
the first kit to take the ruling.

The file half fails too. `tools/unattended/kit.toml:10` ships `include = "**"` as `engine`, and only the
`project-owned` rule at `:13-33` withholds a self-test. That rule is TOOL-aQuenchedHarness-3, CLOSED, whose
title is that a self-test never reaches an adopter, as a leg or as a file. Unit 2 adds no such claim, so
the suite ships to every adopter. The build README records the owner's 2026-09-13 answer as the writer
getting "its own small suite", which is a suite, not a leg. Neither the ruling nor the closed unit is
cited.

**Why blocker.** AC9 can be satisfied only by reversing a standing owner ruling without saying so, and
unit 2 is order 2, so every later producer builds on it.

**Fix.** Follow the six-suite precedent. Add no `tools/gate-legs.json` leg. Add the suite to
`tools/unattended/kit.toml`'s `project-owned` include list, and declare it as a non-held row in
`tools/run-gates/selftest-budgets.txt`, which that file's header allows for a row whose argv names a
tracked file. Run it directly, not through `run-unattended-gates.sh --selftests`, which drives the suites
the standing instruction says not to run. AC9 becomes: `bash tools/unattended/runlog-writer.test.sh`
passes at `FLOOR_ASSERTIONS` inside its budget row. The other route is an explicit owner reversal,
recorded in `memory/DECISIONS.md` and parked for the owner, not assumed.

**Left-shift.** The ruling is carried by two comments and one file header. This synthesis found no leg
that refuses a manifest row whose argv names a `tools/unattended/*.test.sh`, and the budgets checker is
the natural home for one, because it already asserts the declared self-test population in both
directions. Add that refusal, stage it RED with this unit's own proposed row, and cite the ruling in the
failure text.

---

### H1 — HIGH — unit 3 §2 S1 and S3, §4 ¶1, §6 AC3 — raw 1, 36, 55

**The defect.** §4 states: "The signal traps at `:1042-1044` exit with 130, 143 and 129, so `$?` on entry to
`cleanup` is the real status on those paths." At base the traps are `trap 'cleanup; exit 130' INT`,
`trap 'cleanup; exit 143' TERM` and `trap 'cleanup; exit 129' HUP`, beside `trap cleanup EXIT` at `:1041`.
A signal therefore runs `cleanup` from the signal trap, and the `exit` then fires the EXIT trap, which runs
`cleanup` again. This synthesis reproduced it on node `d` with the same trap shape. With a foreground
child, the two entries read `rc=0` and then `rc=143`. Blocked in `wait`, both read `143`. The runner
blocks on `wait -n` (`:1646`), so both lines will usually read `rc=143`. AC3 asks only that "its line reads
`verdict=NONE rc=143`", and it passes on a double write.

**Impact.** A writer placed in `cleanup` "before its existing work" (S1) appends two `ev=once` lines for one
killed bar. Unpaired lines are never deduplicated. Unit 8 then counts two bar runs for one run id, and the
killed-bar signature and the `red-behind-zero` join both read a phantom.

**Fix.** Either guard the writer with a flag set on first entry and pass the status explicitly
(`trap 'RUNLOG_RC=143; cleanup; exit 143' TERM`), or reduce the signal traps to a bare `exit N` so the EXIT
trap runs `cleanup` once. Correct §4's premise. AC3 sends TERM, INT and HUP in turn and asserts exactly
ONE `gates.log` line per killed bar, with `rc` 143, 130 and 129. Units 2 and 4 are not affected: their
traps are specified as bare `exit 128+n`.

**Left-shift.** A gotcha record for the shape, *a signal trap that calls the EXIT handler and then exits
runs the handler twice*, anchored on `tools/run-gates/run-gates.sh`, so `gotchas.py --for-paths` puts it on
the checklist of the next change to the runner. The spec-audit rule: *a claim about control flow at a
cited line is re-derived by running the shape, not by reading it.* It took three lines of bash to settle.

---

### H2 — HIGH — unit 4 §2 S1 and S5, §4 ¶2, §6 AC5; the same omission in unit 3 §2 S4 — raw 11, 34, 56

**The defect.** §4 says the hook "already resolves `$(git rev-parse --git-dir)` at `:157` and `:202`" and
takes the common dir "from that value's `commondir` file". At base, `.githooks/pre-push:33` unsets
`GIT_DIR`, the stdin loop is `:115-117`, and the skip exits are `:119` and `:120`. The only git-dir
resolutions come later: `:157` is an inline substitution inside the refuse-raw test and is never stored,
and `:202` is `gd=`. START is written "after the stdin loop" and carries `lander=`, which is read from the
git dir, and the skip-path ENDs need the journal root. Both are written before any git-dir value exists.

§4 also names only the `commondir` file. In the primary tree `.git/commondir` does not exist (checked
here; in this linked worktree it holds `../..`). Unit 2 §4's table states the fallback, "the git dir
itself", and units 3 and 4 omit it. The primary tree is where every lander push comes from, because
`tools/push-main.sh:63-66` refuses any branch but the default. S5 claims "no added process spawn" and
names AC5 as its observer, but AC5 counts no execs, and S5 omits the first-mkdir carve-out units 2 and 3
state.

**Impact.** Implemented literally, every lander push resolves no journal root and records nothing. That is
the `full`, `scoped` and `refuse-*` population the unit exists to record. Alternatively the implementer
adds a `git rev-parse` spawn that nothing measures.

**Fix.** Before the stdin loop, and after the `cd "$top"` at `:49`, resolve the git dir from `$top/.git`
(a directory, or the `gitdir:` line of the file). Resolve the common dir as the git dir itself, else
`<git-dir>/<commondir contents>`, as unit 2 §4 does. State this in §4 of both unit 3 and unit 4, add the
first-mkdir carve-out, and add an xtrace exec-count criterion on the skip-nondefault and full paths, run
from a linked worktree and from a primary-tree clone with no `commondir` file.

**Left-shift.** This is `memory/gotchas/two-readers-of-one-config-one-re-derived.md`: three shell producers
each re-derive one resolution, and the reader uses a fourth method. Kits cannot import each other, so the
gate is a shared fixture instead: each producer suite runs its resolver over the same two layouts,
primary and linked, and asserts the same absolute path H3's criterion asserts for the reader.

---

### H3 — HIGH — unit 1 §2 S2 against §6 AC2; the unit 2, 3 and 4 suites — raw 2, 43

**The defect.** S2, the journal location contract (`runlog` under the git COMMON dir, one file per
producer), says "Observed by AC2". AC2 round-trips value escaping through `parse_line` and nothing else.
AC5 prints a path and asserts nothing about where it points. No criterion in the set runs the reader or
any producer from a linked worktree, the one layout where the git dir and the common dir differ. Unit 2's
sandbox, unit 3's scratch repo and unit 4's work clone are all plain repositories. The reader resolves with
`git rev-parse --path-format=absolute --git-common-dir`, and the three producers resolve with builtin
`commondir` reads. This build runs from a linked worktree.

**Impact.** A producer that writes under `.git/worktrees/<name>/runlog/` passes every criterion in the
set, and the model then reads `absent` or `dead` for lines that exist.

**Fix.** Add a criterion to unit 1: from a primary tree and from a linked worktree, `resolve_journal_root`
returns the same absolute `<common-dir>/runlog`, and `journal` names that path. Add an arm to the unit 2,
3 and 4 suites that writes from a linked worktree and asserts the line lands in
`<common-dir>/runlog/<producer>.log` and nowhere under `.git/worktrees/`.

**Left-shift.** The S-to-AC token check described under "Classes across the set". S2's backticked tokens
(`runlog`, `driver.log`, `gates.log`, `pushes.log`) share none with AC2's (`parse_line`,
`<kit>/runlog_lib.py`).

---

### H4 — HIGH — unit 1 §4 Data model key row; unit 2 §4 Data model and §2 S6; unit 6 §2 S1 — raw 30, and the key-pattern clause of raw 14

**The defect.** The key rule is `[a-z][a-z0-9_.]*`, and the example on the same row is
`sess.CLAUDE_CODE_SESSION_ID`, which that rule rejects. Unit 2's START emits `sess.<NAME>`, where NAME is
an uppercase `[A-Z_]` environment-variable name drawn from `RUNLOG_SESSION_VARS`. A `check_line` built to
the stated rule counts every driver START that carries a session field as a bad line. Unit 6 S1 then finds
no session ids. No unit 1 criterion uses a dotted uppercase key, so nothing reds before integration. Unit
6 S1 also never names which `sess.*` key holds the Claude Code session id, which depends on a conf value
an adopter declares.

**Fix.** Restate the grammar as `[a-z][a-z0-9_]*(\.[A-Za-z0-9_]+)?`, or have unit 2 lowercase NAME. Add a
unit 1 AC2/AC3 fixture carrying `sess.CLAUDE_CODE_SESSION_ID=<uuid>`, `fail.1=` and `ref.1=`. Name the key
the extractor reads in unit 6 S1.

**Left-shift.** A golden-line fixture in unit 1's self-test: one line copied from each producer spec's data
model, parsed with no bad-line count. This is the charter's contract-first rule, applied to a grammar
three producers depend on. The class is `memory/gotchas/two-answers-to-one-question.md`: a grammar and its
own example are two statements of one rule.

---

### H5 — HIGH — unit 4 §2 S1 and S2, §5 security, §6 AC2 — raw 3

**The defect.** S1 writes "the remote NAME from `$1`". When a push uses no named remote, git passes the URL
as both `$1` and `$2` (githooks(5), pre-push). So `git push https://user:tok@host/repo` writes the
credential into `remote=`, which S2 promises "is never written" and §5 claims ("no URL, so no credential").
AC2 does not say which remote form it pushes to, so a named-remote fixture passes. Unit 5's redaction is
scoped by its own §3 to extractor and narration text, not to journal values. Unit 1's `journal` prints
parsed lines as JSON, and unit 8 §5's claim that "the model holds free text only from tracked, public
sources" becomes false too.

**Why HIGH, not blocker.** The path is reachable only by a push to a bare, credential-bearing URL, which
neither the lander nor any documented flow in this repo makes, and unit 9's closed schema keeps `remote`
out of the committed record. It is still the one path in the set where a secret is persisted and then
printed into an agent's context, against a guarantee the spec states and its criterion cannot see.

**Fix.** Write `remote` only when `$1` differs from `$2`. Otherwise omit it and set `remote_unnamed=1`,
keeping `url_userinfo`. AC2 pushes once through a named remote whose URL carries `user:pass@` and once to
the bare URL, and asserts `pass` appears in neither line. State in unit 5 §3 whether journal values are in
its scope.

**Left-shift.** The two-form AC2 is the gate. The spec-audit rule: *a guarantee of the form "X is never
written" gets one arm per SOURCE of X, including the degenerate caller contract where two positionals are
equal.*

---

### H6 — HIGH — unit 8 §2 S2 against §6 AC2; §4 ¶2 — raw 6

**The defect.** AC2 observes own-commit filtering and time order beside phase moves. Nothing observes the
rest of S2: gate lines joined by worktree and window, or exactly by `gate_run`; push lines; unit dispatches
and briefs; merges naming the slug; and, from the extractor, owner turns, compactions, limits and idle gaps
of 15 minutes or more. §4 makes a falsifiable claim, "a bar run in another worktree at the same minute is
never attributed", and no criterion observes it.

**Impact.** The joins are the model's core, and a wrong join flows unchallenged into unit 9's public
record.

**Fix.** Add a criterion with two gate lines at the same minute from two worktrees, plus one carrying a
`gate_run` pinned by a push line, asserting that only the run's own worktree line and the pinned line
join. Add one fixture line per remaining timeline item, including idle gaps of 15 and 14 minutes.

**Left-shift.** The S-to-AC token check: S2's backticked `gate_run` does not appear in AC2, which names
only `build_run_model`. The spec-audit rule: *a §4 sentence phrased as a guarantee ("is never
attributed") becomes an acceptance criterion or is deleted.*

---

### H7 — HIGH — unit 6 §2 S3 and S4 against §6 AC2-AC4 — raw 7

**The defect.** S3 names AC2 to AC4 as its observers. Those cover uuid dedupe and order, owner turns and
keepalive, and a background call's end. Nothing observes token usage deduplicated by `requestId` and split
into main loop, direct agents and workflow agents, although cost is in the unit's title and the README's
expected improvements. Compactions, API errors, session limits, hook denials, workflow runs and agent
spawns are unobserved. S4 names AC3, which checks only that no free text is persisted. It does not check
the tool classes, or the destructive-git and piped-driver flags that unit 8's anomalies consume.

**Fix.** Add criteria for three things. A `requestId` repeated across records, with usage in the main,
subagent and workflow files, counts once and splits three ways. One fixture per event kind. One fixture
per class and flag, for example `git reset --hard` flagged destructive and an `unattended.sh` call piped
to `tail` flagged piped.

**Left-shift.** §4's data model already enumerates `kind` as a closed list. A self-test arm asserting that
every listed `kind`, and every S4 class, has at least one fixture that produces it makes the population
drive the arms, so a new kind without a fixture reds.

---

### H8 — HIGH — unit 5 §2 S2 against §6 AC1 — raw 8

**The defect.** AC1 iterates whatever rows the table holds. Nothing ties S2's enumerated classes to rows:
PEM blocks, JWTs, Cookie and Set-Cookie, connection-string `Password=`, `AccountKey=`, SAS `sig=`, the
PowerShell env table and the rest. §7's floor is "raised by the rule count" only after landing, so a table
that omits a class at landing passes AC1, AC2 and AC4. This unit IS the control, and §5 says so.

**Fix.** Give each S2 class a fixed id. Add a criterion that every listed id is present with a positive
and a negative, staged RED by deleting one row.

**Left-shift.** That criterion is the charter §7 shape of a declared population asserted in both
directions: every S2 class id has a row, and every row's id is an S2 class.

---

### H9 — HIGH — unit 1 §6 AC4; unit 5 §2 S5 and §6 AC4; unit 6 §6 AC8; unit 8 §2 S8 and §6 AC8; unit 10 §2 S4 and §6 AC4 — raw 75, 78, 79

**The defect.** Five criteria make an absolute wall-clock floor a RED condition inside a held self-test:
under 1 s for 100,000 lines, under 1 s for 50,000 strings, over 100 MB/s and under 64 MB, under 3 s for the
largest model, and under 5 s for 100 records. TOOL-cSteadyMetronome-1 records that "a gate asserts what the
SUBJECT does, never what the NODE does", retiring an elapsed-time check that blocked three pushes over a
tree it had passed. TOOL-aPooledSweep-1 adds that "a contended clock cannot grade a budget". Held
self-tests run in the concurrent pool, and the header of `tools/run-gates/selftest-budgets.txt` records one
leg varying 5.5x at the median and 47.1x at worst under contention.

Two of the floors also cannot see their own stated failing case. Verification measured about 0.0185 s per
git call on node `d`, consistent with the per-exec tax `memory/gotchas/process-creation-is-the-suite-cost.md`
records. At that rate, per-commit reads over the 95 commits of the largest run cost about 1.8 s, under unit
8's 3 s floor, and per-record reads over 100 records cost about 1.9 s, under unit 10's 5 s floor. Those two
figures come from verification and were not re-derived here. The set already knows the better instrument:
unit 2 §5 chooses "exec counts from an xtrace, which is deterministic where wall time on this node is not",
and unit 13 AC4 counts git calls.

**Fix.** Convert each red condition to a deterministic count, and print the wall time report-only:

- unit 1 AC4: one split per line, with no per-line subprocess and no per-line regex compile, counted
  through a shim;
- unit 5 AC4: regex invocations bounded by the strings the prefilter admits, counted;
- unit 8 AC8: git subprocess calls constant in N commits, one log and one blob batch;
- unit 10 AC4: git calls constant over 100 records.

The README's Performance rule ("each consumer and suite states a wall-clock ceiling, measured on node `d`")
is met by each leg's declared ceiling and budget row, which is the charter's sanctioned cost verdict. It
does not require per-arm floors.

**Left-shift.** A spec-audit arm refusing the literal shapes `floor is PINNED` and `floors are PINNED` in a
live spec's §6, plus an `under <n> s` clause inside a criterion that carries a Red-when. Four of this set's
five hits carry the first shape. The shape also occurs in at least one earlier build's spec, so the arm
needs a forward-only cutoff, the way check 22 has one.

---

### H10 — HIGH — unit 6 §2 S8, §6 AC8 — raw 76

**The defect.** AC8 names no other command, so by the unit's own preamble it is an arm of the kit
self-test. Its fixture is "the largest local session tree on the node running the build", which is the
operator's private `~/.claude/projects` store, graded at over 100 MB/s and under 64 MB. The subject is
the node, not the tree. On another node, an adopter or a fresh clone there is no subject and no announced
skip, so the arm is green by absence. Where the largest local tree is small, a hold-everything reader
stays under 64 MB, so the arm cannot fail. Where transcripts do exist, a kit self-test reads real session
files.

**Fix.** Generate a synthetic session tree of fixed size in scratch. Assert the streaming property
structurally, as a bounded count of tuples or records resident. Move the real-tree rate and memory
reading to a report-only command outside the self-test that grades nothing.

**Left-shift.** The class is `memory/gotchas/fixture-inherits-ambient-machine-state.md`. The gate: the
runlog self-test points `CLAUDE_CONFIG_DIR` and `--transcripts` at its own scratch tree before any arm
runs, so a real-store read is impossible by construction, not by care.

---

### M1 — MEDIUM — unit 3 §3 bullet 3, §4 ¶2 — raw 9, 44, 61

§4 lists `:1093` among "the exits before `:1041`", and §3 says "a failed `mkdir` of the run dir" writes
no line. At base, `:1093` (the run-record `mkdir` failure, `exit 2`) comes after `trap cleanup EXIT` at
`:1041`. So does `:1182` (the manifest parse failure, `exit 2`), which the list omits. Both come before the
header is written. By S3 ("every exit after the trap is installed writes a line") both write
`verdict=NONE rc=2` with empty header keys, lines the spec says never exist. §5 correctly pairs `NONE` with
a signal `rc` as the killed signature. The exit table is what is wrong.
**Fix.** Move `:1093` into the post-trap list, add `:1182`, and state the line each writes. Alternatively,
have the writer skip when the run dir or header is absent, and assert no line. Either way, add an arm.
**Left-shift.** A suite arm driven by the population: every `exit` after the `trap cleanup EXIT` line is
enumerated by a grep in the suite, and each must map to an arm, so a new post-trap exit without one reds.
Unit 2 §5 names the same guard for the driver.

### M2 — MEDIUM — unit 3 §2 S2 — raw 10

The `run` key is the gate side of unit 4's exact `gate_run` join, and no criterion checks it equals a
pinned `GATE_RUN_ID`. Unit 4 AC4 stubs the bar through `GOV_GATE_CMD`, so the real runner's line is never
seen with a pinned id, and a wrong key silently falls back to the window join. The 20-name `fail.<i>` cap
and `fail_more` are unexercised, because the scratch manifest has two legs.
**Fix.** AC1 runs with `GATE_RUN_ID=push-1-1` and asserts `run=push-1-1`. Add an arm with 21 failing legs:
`fail.20` present, `fail.21` absent, `fail_more=1`.
**Left-shift.** One end-to-end join arm that runs the real runner under the real hook in a scratch repo
and asserts the push END's `gate_run` equals the `gates.log` line's `run`. It is the only arm that sees
both halves of the join the two units exist to provide.

### M3 — MEDIUM — unit 4 §2 S1, the `lander` field — raw 12

S1 defines only "`lander=1` when the `push-main-active` marker exists", and no criterion asserts the field
either way. The build's own convention is absence when false: unit 2 AC4's `oob` and unit 4's own
`url_userinfo`. Unit 8 S5's `push-outside-lander` keys on `lander=0`, so an omitted key never fires it.
**Fix.** Always write `lander`, as 1 or 0. AC1 asserts `lander=1` on the marker push and `lander=0` on the
other two.
**Left-shift.** H4's golden-line fixture carries `lander=0`. The spec-audit rule: *every key-value a
consumer spec keys on appears with that value in the producer's data model.*

### M4 — MEDIUM — unit 1 §4 line-length and unknown-key rows; unit 4 §2 S1 — raw 14, 50

No criterion observes the 2048-byte cap or "unknown keys preserved", and no producer spec carries the
truncation duty the grammar hands them. Unit 4 records up to 20 `ref.<i>` values of about 120 bytes each
for `refs/heads/main`, and about 180 for longer names, which comes to roughly 2.4 to 3.6 KB before the
START line's other fields. Truncating values cuts the remote-ref and sha fields unit 8's
`push-outside-lander` reads.
**Fix.** In unit 1, state the truncation order: whole indexed fields drop into `<key>_more` before any
value is cut. Lower unit 4's ref ceiling to what fits, which is about ten at the longer measured value.
Add a unit 1 fixture line with dotted and unknown keys, asserting they come back preserved, and a unit 4
arm pushing 21 long-named refs, asserting `ref_more` and a line of 2048 bytes or less.
**Left-shift.** Every producer suite asserts the byte length of its largest fixture line against the cap.
Kits cannot import each other, so each suite asserts it locally, but against the one number unit 1 owns.

### M5 — MEDIUM — unit 2 §2 S5, §6 AC4 — raw 16

S5 compares RUN.md against "the stamp the previous END left", and never states the no-stamp case.
Reproduced here: both `[[ a -nt missing ]]` and `[ a -nt missing ]` are true. So the first logged call
for a slug in a worktree reads `oob=1`, and so does a run resumed in a new worktree and every run in
flight at upgrade, this one included. Unit 8's `out-of-band-edit` anomaly then fires falsely in this
build's own committed record.
**Fix.** No stamp means `oob` is absent, or `oob=unknown`. Add that arm to AC4.
**Left-shift.** AC4's no-stamp arm, plus a gotcha record for `-nt` against a missing right-hand file, so
the next shell comparison of mtimes meets it on the checklist.

### M6 — MEDIUM — unit 8 §2 S5 — raw 17

`converged-on-blocked` and `multi-run-session` are named and defined nowhere. A grep of the tree finds
them only at unit 8 lines 60-61. The protocol has CONVERGED review exits but no BLOCKED phase to anchor
the first. `nonterminal-merged` is "sub-classified by its last act" with no sub-class set. AC5 asks for a
fixture "staging each anomaly kind", so for these kinds the implementer writes both the rule and the
fixture that satisfies it, and the kinds reach a public record with invented semantics.
**Fix.** Define each kind with its trigger and evidence fields. Give `nonterminal-merged` unit 13's
sub-classes (`surfaced-park`, `retired-unit`, `no-rows`, `other`), so one concept has one vocabulary
across two units.
**Left-shift.** A self-test arm over the model's closed anomaly enum, asserting in both directions that
every kind has a written definition and a fixture.

### M7 — MEDIUM — unit 8 §2 S4 — raw 18

Four of the five conformance items have neither a MET, UNMET or UNJUDGEABLE rule nor a criterion: phases
walked, a GREEN bar at the close's head before `--close`, keepalive attested reaped, and the review loop
reaching an exit. AC4 observes only brief-before-build, and UNJUDGEABLE is never exercised. The
GREEN-at-head item also depends on the gate join H6 finds unobserved. This block is a headline section of
the public record.
**Fix.** State each item's rule and evidence source. Add a criterion per item, including one UNJUDGEABLE
case, such as a close with no `gates.log` line for its head.
**Left-shift.** Arms driven by the population: every item crossed with every state it can take has a
fixture.

### M8 — MEDIUM — unit 8 §2 S3 against §6 AC3 — raw 19

AC3 observes `Decided:` trailers and the owner-before and agent-inside spec marks. Four ledger sources have
no criterion: parked decisions, rescope acts and overrides; review rounds with their verdict path;
decision-log rows; and unmet acceptance-ledger lines. "Each entry points at its source" is observed only
for trailers.
**Fix.** Extend AC3's fixture with one row per source, asserting each entry's file and line, or sha.
**Left-shift.** The same population-driven arm: every ledger source S3 lists has a fixture row.

### M9 — MEDIUM — unit 8 §2 S3, the decision-log split on `OWNER RULING` — raw 87

No guide defines an `OWNER RULING` prefix convention. Counted here, 8 lines of `memory/DECISIONS.md` carry
it, 16 carry a parenthesised `(owner` form, and 30 mention the owner at all. Owner rulings from real
unattended runs use the other spellings: TOOL-dTieredTribunal-7 reads "(owner, 2026-08-26)", and other rows
read "(owner: …)" or "owner calls". Splitting on the prefix classifies the majority as decisions the run
took, which is AC3's own Red-when, and AC3 never exercises a decision-log row.
**Fix.** Classify on every observed owner spelling, including the §8-style `(owner, <date>)`, and name the
split as heuristic in the model's `method` field. Add an AC3 fixture row using `(owner, <date>)` that must
count as owner.
**Left-shift.** Charter §7's rule, "run a candidate gate predicate over the real tree before wiring it, and
print hits AND near-misses", applied here as a committed report of decision-log rows by owner spelling. The
unit's evidence is the classifier's output over the real corpus, not a fixture the author wrote.

### M10 — MEDIUM — unit 5 §6 AC3 against §2 S4 — raw 21

S4 promises no committed file carries a live-looking credential literal. AC3's grep covers the GitHub,
AWS and `sk-ant-` shapes only. S2's own classes include anchored `sk-` keys beyond `sk-ant-`, vendor
prefixes, `AccountKey=`, JWTs and PEM blocks, several of which push protection blocks, and a literal
positive for any of them passes AC3. Unit 6 AC6 plants "a credential" in a fixture under the kit with no
template rule.
**Fix.** Derive AC3 from the table: run `scan_secrets` over every tracked file under the kit and expect
zero hits outside the template column. State that unit 6 AC6's planted credential is template-expanded at
test time.
**Left-shift.** That derivation is the gate. The table then checks the repository that ships it, and
covers the fixtures of later units with no further edit.

### M11 — MEDIUM — unit 7 §6 AC3, §2 S1 — raw 22

AC3 builds its own commit with two `Decided:` trailers and checks git parses them. It never reads M10's
text, so its Red-when ("the grammar written in M10 is not the one git parses") cannot fire. Git parses
trailers only in the message's last paragraph, and every agent commit ends with the mandated
`Co-Authored-By:` trailer. M10's clause ("one line per choice, on the commit") never says the lines
belong in that final trailer block, and a `Decided:` paragraph written above it is invisible to
`%(trailers:key=Decided)`. §3 says nothing refuses a run that left none, so unit 8's harvest undercounts
silently.
**Fix.** M10 says the lines go in the trailer block beside `Co-Authored-By:`. AC3 builds its commit body
from the rendered M10's own example, and adds a negative arm showing a `Decided:` line mid-body is not
harvested.
**Left-shift.** The class is `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. The
gate: unit 8's harvest also counts body lines beginning `Decided:` that git did not parse as trailers,
and reports them as a coverage defect. A harvest that can undercount silently carries its own near-miss
count.

### M12 — MEDIUM — unit 13 §2 S1 against S5, §6 AC1 and AC4 — raw 23, 40

S1 reads each tracked `RUN*.md` at HEAD, and AC1 reds if the function reads the working tree. S5 and AC4
allow exactly two git calls in total, a `rev-list` of the base and a `cat-file --batch-check` over the
witnesses, and `--batch-check` returns type and size, never content. The kit's own at-sha reader,
`_read_defs_at_sha` in `tools/drift-audit/drift_report.py`, spends an `ls-tree -r` plus a
`cat-file --batch`. The `Git` helper offers only `run`, `is_commit` and `is_ancestor`, with no shared
cached reader to absorb the cost. A faithful S1 therefore makes a third call and reds AC4, or reads the
working tree, which AC1 forbids. No fixture makes the working tree differ from HEAD, so AC1's Red-when
cannot fire either.
**Fix.** Restate S5 and AC4 with the calls that meet S1. That means either three calls (`rev-list`, one
enumerate-and-read at HEAD, one witness check), or two, with the witness check folded into a
content-returning `cat-file --batch` over `HEAD:<path>` and witness names. Add an AC1 arm with an
uncommitted edit to a RUN.md that HEAD does not carry, asserting it is not counted.
**Left-shift.** The classes are `memory/gotchas/two-guards-one-question-two-answers.md` and
`memory/gotchas/armed-but-unreachable-rule.md`. The spec-audit rule: *every Red-when names the fixture
that produces it.*

### M13 — MEDIUM — unit 4 §4 exit list against §2 S3 and §3 — raw 35

§4 lists the gating exits as `:119`, `:120`, `:140-150`, `:157-160` and `:164-169`, plus the bar's
pass-through. It omits five `exit 1` refusals before the stdin loop, `:47`, `:51`, `:95`, `:102` and
`:108`, each of which blocks the push. S3's decision vocabulary has no value for them, and §3 excludes only
`--no-verify`. This synthesis adds one refinement from the tree. `:47` (no top level) and `:51` (cannot
`cd` to it) run before any root is known, so no journal line is possible there. `:95`, `:102` and `:108`
are default-branch refusals that run after `top` is known, and a line is writable.
**Fix.** Give `:95`, `:102` and `:108` a decision such as `refuse-default-branch`, set before each exit,
with one covered in AC1. Name `:47` and `:51` in §3 as refusals that cannot be logged, and say why.
**Left-shift.** The population-driven exit arm from M1, applied to the hook: every `exit` in
`.githooks/pre-push` maps to a decision or to a named exemption.

### M14 — MEDIUM — unit 8 §2, the missing S item; against unit 6 §3 bullet 3 and unit 9 §2 S4 — raw 37

Unit 6 §3 hands the owner-turn position classes (launch, pre-run, in-window, post-close) to the run
model. Unit 9 S4 renders owner turns as counts per position class, and the build README's rule requires
"owner turns as counts and positions". No S item or criterion in unit 8 builds them, and the names occur
only in unit 6 §3 and unit 9 S4. The classes also depend on the run window, which B2 finds undefined for
this run.
**Fix.** Add a unit 8 S item that classifies each owner turn by position against the run window, with a
criterion over a fixture holding one turn per class.
**Left-shift.** The spec-audit rule: *every hand-off names something the receiving spec's §2 builds.* The
mechanical half: a term a sending spec's §3 or Edges hands on must appear in the receiving spec's §2.

### M15 — MEDIUM — unit 12 §1, §2 S2 and S3; against unit 8 §2 and unit 6 §2 S3 — raw 38

The Skill's goal, trigger (S2) and AC2 promise answers about cost, and its procedure (S3) answers through
`model <slug>`, narration and citations. Unit 8 carries no usage or cost item. A grep for usage, cost,
token and `requestId` over units 8 and 9 finds nothing. Unit 6 S3 extracts usage, but H7 finds its dedupe
and split unobserved. The README's "what a run costs" improvement has no path from extract to answer.
**Fix.** Add a unit 8 S item and criterion that join usage totals, split three ways, to the run, and take
H7's unit 6 criterion. Otherwise, drop cost from unit 12's goal and trigger.
**Left-shift.** M14's hand-off rule, plus a README-level one: *each expected improvement names the unit
whose acceptance criterion observes it.*

### M16 — MEDIUM — unit 9 §2 S6 against unit 10 §2 S2; §6 AC6 — raw 39

The 24 KB cap is hard, because unit 10 refuses anything larger. Only the timeline elides. Anomalies,
conformance and the summary never do. Conformance grows with units (several items each, and this build
has thirteen), and anomalies are per occurrence with evidence, so idle-gap and `oob` noise alone can reach
dozens in a long run. AC6 grows only the timeline. No rule covers non-elidable sections that exceed the
cap, so a plausible input has no valid output, and unit 11 AC5 grades this run's record at the push.
**Fix.** State an overflow rule that keeps the cap reachable, such as aggregating anomalies and
conformance by kind with counts past N rows. Add an AC6 fixture with many units and many anomalies.
**Left-shift.** The renderer derives the worst-case size of its non-elidable sections from the model's
bounded enumerations, and an arm renders that declared worst case under the cap.

### M17 — MEDIUM — unit 4 §2 S5, §6 AC5, against the build README's build-level rules — raw 42

The README rule is "a failed write says so on stderr". Unit 2 (S9, AC8) and unit 3 (S5, AC5) each carry it
and assert a stderr line. Unit 4 S5 and AC5 keep only "rc and stdout unchanged", so a failed `pushes.log`
write is silent. That is the unobserved-push condition this unit exists to end.
**Fix.** S5 prints one stderr line, and AC5 asserts a `pre-push: run log` stderr line.
**Left-shift.** The spec-audit rule: *every build-level rule maps to a criterion in each unit it binds.*
A README rule restated by hand in three specs drifted in the third.

### M18 — MEDIUM — unit 2 §2 S2, §3 and §4; unit 4 §2 S3 — raw 62

Trapping TERM, HUP and INT changes when the process dies, not only the `rc` it logs: bash defers a trapped
signal until the running foreground child returns. Reproduced here on node `d`: TERM ended an untrapped
script running `sleep 4` in 0.33 s, and one with `trap 'exit 143' TERM` in 4.05 s. The driver runs
`$GATE_CMD` in the foreground through `run_bounded`, bounded by `GATE_BOUND` at a default of 3600 s, and
the hook runs the whole bar in the foreground at `.githooks/pre-push:292-293`. After units 2 and 4, a TERM
sent to a driver in `--close`, or to a hook mid-push, does not stop it until the gate returns. Unit 2 §3
says "no change to any existing refusal", and both §4s present the traps as logging only.
**Fix.** State the latency change and accept it explicitly. Or run the long child in the background and
`wait` on it, which a trapped signal interrupts at once. That is the shape `tools/run-gates/run-gates.sh`
already uses at `:1646`. Add an arm that times a TERM delivered during a long child.
**Left-shift.** A gotcha record for the deferral, anchored on both files, beside H1's record for the
double handler. Both are properties of bash traps that every reader of these three scripts will otherwise
re-learn.

### M19 — MEDIUM — unit 11 §2 S1, §4 Inventory, §5 migration, §6 AC1, §10 — raw 81

`RUNLOG_CLI` is specified as a rendered placeholder whose blank value turns the section off, "following the
`RECALL_CLI` precedent". `RECALL_CLI` and `MAP_CLI` are optional keys the driver reads. `render()` in
`tools/unattended/adopt-unattended.sh` substitutes neither: it substitutes `KIT_DIR`, `TOOL_ROOT`,
`MEMORY_ROOT`, `LANDER`, the three keepalive keys, `ANCHOR_SCOPE` and `AUTH_PARAM`. Pre-setting a rendered
key empty is the failure TOOL-aWrittenMethod-1 recorded ("absence-of-placeholder is not presence-of-value …
default the key to its own token so an undeclared value reds"), which the adopter enforces at `:123-126`.
The only two exceptions, `ANCHOR_SCOPE` (TOOL-aPromptedMandate-5) and `AUTH_PARAM` (TOOL-aNamedGesture-1),
each took a named decision and derive an effective value. `render()` has no conditional sections, so every
adopter's blank `RUNLOG_CLI` renders the section's commands with an empty program span, and AC1 tests only
this repo's value.
**Fix.** Correct the precedent: `AUTH_PARAM` is the rendered-key precedent, not `RECALL_CLI`. Either keep
the placeholder default, so an undeclared value reds, and state the adopter migration, or record a third
exception with its reason, as the two precedents did. In the second case, add a criterion that renders
with `RUNLOG_CLI` blank and asserts an announced skip containing no empty command span.
**Left-shift.** The unattended kit's self-tests are not run, so the refusal belongs in the adopter's own
`--check`, which the `unattended skill wiring` leg runs. A key listed in `optional_keys` AND substituted by
`render()` must be a named exception or default to its own token.

### M20 — MEDIUM — unit 11 §2 S5, §6 AC5 — raw 82

AC5 is observed "when the push boundary's bar runs on this build's landing". The owner-sanctioned route in
the build README is a `--no-ff` merge and push from this worktree's detached head. The tracked hook refuses
any default-branch push lacking `push-main-active` in `$(git rev-parse --git-dir)` (`.githooks/pre-push:157`,
TOOL-aLeasedGauntlet-1), and does so before any bar runs. In this worktree the git dir is
`.git/worktrees/<name>`. The only writer of that marker is `tools/push-main.sh`, which refuses a detached
head at `:63-66`. Protocol §6 and `BYPASS_BAN` forbid `--no-verify`, which would run no bar anyway. On
the sanctioned route the push is either refused or bypassed, and neither runs the bar, unless the run
creates the marker by hand, which the spec does not name.
**Fix.** Observe AC5 on the merged tree before the push: run the `runlog record schema` leg directly, or
the full bar, and record that verdict. State in the spec which push mechanics the landing uses, given the
raw-push refusal. If the only route needs `--no-verify` or a hand-made marker, park it as an owner
decision.
**Left-shift.** The spec-audit rule: *a criterion observed "at the push" names the command that runs at
the push, on the route the build will actually take.* The landing mechanics of a worktree landing belong
in the protocol once, not re-derived per build.

### M21 — MEDIUM — unit 7 §3 bullet 3, §7 — raw 84

The unit changes shipped memory-tree bytes. `tools/memory-tree/BUILD-METHOD.template.md` opens with
`<!-- gov:kit memory-tree@2.69 -->`, yet the unit declines a version move on verdict-epoch grounds alone.
TOOL-dMuffledSentinel-3 (2026-09-12) records that an adopter refused a pull whose shipped bytes moved at an
unchanged version, and that gov bumped two kits for exactly that reason. Units 2, 3 and 13 bump their kits
for the same reason. Unit 7 omits `kit version markers` from §7.
**Fix.** Bump memory-tree from 2.69 to 2.70 across its carriers per `tools/check-kit-versions.sh`, and add
the leg to §7. Otherwise cite TOOL-dMuffledSentinel-3 and state why template prose is exempt from the
adopter-vintage rule.
**Left-shift.** A leg that compares each kit's shipped-file blob set against the set recorded at its last
version move, and reds when bytes move at an unchanged version. TOOL-dMuffledSentinel-3's ledger names the
gap. Check the TOOL backlog for an existing row before filing a new one.

### L1 — LOW — unit 2 §4 Placement, the START slug sentence — raw 70

START takes its slug only when `$2` matches `^[A-Za-z]{2,64}$`. `check_slug` at
`tools/unattended/unattended.sh:1060-1070` admits a letter followed by letters, digits or dashes, which is
hygiene check 4's build-folder grammar. For a valid adopter slug such as `auth-v2`, or a one-letter slug,
START loses its slug, so S4's `phase_from` and S5's `oob` never run. Pairing is by nonce and END carries
the parsed slug, so the knock-on to units 6 and 8 is smaller than first filed.
**Fix.** Validate START's slug with `check_slug`'s grammar plus a length bound, or state the narrowing as
deliberate.
**Left-shift.** Reuse the function. Its own header says the slug is validated "against the SAME grammar
hygiene check 4 enforces … not by a second one".

### L2 — LOW — unit 12 §3 Edges against §2 S3 steps 2 and 5; unit 11 §3 Edges — raw 52

Unit 12 consumes unit 8's `model` command and coverage block but declares edges only to units 6 and 9, and
unit 8 hands off only to unit 9. Unit 11 consumes unit 2's protocol paragraph (S4) and unit 10's schema
leg (S5, AC5) but declares only unit 9. `TEMPLATE-SPEC.md` makes Edges required so that a criterion
resting on another unit is declared, not grepped for.
**Fix.** Add consumes-from 8 to unit 12, and consumes-from 2 and 10 to unit 11, with the matching hands-off
lines.
**Left-shift.** `gen_build_index.py` already parses Edges for the build order. It can also report a spec
whose §2 or §6 names another unit id of the same build with no matching Edges line. The command-name half
stays a checklist item.

### L3 — LOW — unit 9 §5 perf / scale, against §6 and the README Performance rule — raw 54

§5 states "under 1 s for the largest run" and no criterion observes it, while the README asks for each
consumer's ceiling to be measured.
**Fix.** Not with a wall-clock RED arm, for H9's reason. Either print the render time report-only from an
arm, or state the render's bound structurally (it reads only the model and makes no git call per row) and
observe that by a call count. The leg's budget row carries the measured ceiling.
**Left-shift.** H9's arm. This item is the case that shows why the arm needs the `under <n> s` clause as
well as the `PINNED` one.

---

## Classes across the set

**"Observed by ACn" where ACn observes something else.** H3, H6, H7, H8, M2, M4, M7 and M8 are this shape
outright, and H2 and M17 carry it in a clause. It is the cheapest class here to gate, and the mechanism
already exists one step later in the lifecycle: check 23 requires a ledger answer to share a backticked
token with the criterion it answers. The same test applied to spec §2 would require each S item to share a
backticked token with each AC it names. Checked by hand, it reds unit 1 S2 against AC2, unit 8 S2 against
AC2 and unit 5 S2 against AC1. This synthesis did not run it over the other S items. A shared token proves
no semantics, so the check's header must say it catches only the gross miss.

**The gotcha catalogue did not reach this audit.** `python tools/memory-tree/gotchas.py --for-diff
9fac2b53..1dd6f3da` selects 3 anchored classes, because the spec-set diff touches only `memory/`.
`python tools/memory-tree/gotchas.py --for-paths` over eight of the files the specs plan to touch selects 9
anchored classes. Among those 9 are `two-readers-of-one-config-one-re-derived` (the shape of H2 and H3)
and `two-guards-one-question-two-answers` (the shape of B1 and M12). A spec audit should run `--for-paths`
over the union of its specs' "Files touched" lists. Otherwise the checklist is chosen by the files a spec
IS, when the defects live in the files it plans to change.

**This run as its own test subject.** B1 (AC7 on this tree), B2, B3, M5 and M20 all fail on the run that
is building the logger. The set treats that run as its end-to-end observation without asking whether its
rules cover a run that began before its own writers existed. They do not, in five places.

**Recorded decisions not consulted.** B4, H9, M19 and M21 each contradict a ratified decision that a
`memory-recall` query over this unit's own recall terms would plausibly have returned. M9 contradicts the
decision log's actual spelling. Each spec's §10 cites a recall term list, and none cites a decision id
that list returned.

## What this pass did not cover

- The design research record under `memory/builds/dLoggedFlight/build/` was not a pinned subject. Its
  measured figures (1600 of 1600 intact concurrent appends, the 258.5 M-character streaming run, the 86 of
  86 keepalive joins) are taken as the specs report them.
- The 39 refuted findings are not reproduced or characterized here.
- No code exists yet. The specs were audited against the tree at `1dd6f3da`, whose tool and hook files are
  byte-identical to base `9fac2b53`.
- No finding re-opens the owner's 2026-09-13 rulings in the README: the local-store split, the closed
  schema, the worktree landing, and the do-not-run rule for the unattended suites. B4 and M20 are about
  specs that fail to honour two of them, not about the rulings.

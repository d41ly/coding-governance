**Serves:** spec-audit TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15

# aGraftedHelix — Tier-2 spec audit of units 10 to 15, ROUND 1

*Node `a`, 2026-10-04, ROUND 1 for these six subjects. Units 10 to 14 are the promotions of the
first spec audit's blockers and highs, and unit 15 is the adopted harness first-call trap. Four lenses
ran: underspecification, contradiction, unstated assumption and prior art. Every finding in the body
survived a skeptic prompted to REFUTE it. The seven findings the skeptics refuted appear only in the
appendix. The author of this report confirmed that each pinned blob below is the blob at HEAD
(`14e5f2655`). Three rows were spot-checked in the tree. For H1, `cmd_write` calls
`plan(..., create_missing=True)` at `tools/memory-tree/gen_build_index.py:2306`. For H3, the holder
row calls `write_lease` at `tools/unattended/unattended.sh:6596-6599`. For L7,
`tools/unattended/lib-unattended.sh` defines `build_commit` at `:846` and `read_attribution_tokens`
at `:809`, and `find_build_commit` appears there only as the historical `_find_build_commit` in a
comment. The other rows carry the skeptics' verified text and were not re-derived here.*

**Reviewed at ROUND 1, each subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-10.md`@`0ac3b99109573249b317f1ebe1fd575719435a3c`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md`@`92eb5e19141724dd84cf4c2e983dc23733fa2821`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md`@`aacbc04ed455b4b05e2eea5a85ddcf633986289e`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-14.md`@`320a34b0224ae669f08a5275d0d3184baa7b5c76`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-13.md`@`eb8eba2d5c442b47dff1f797861115b4b80f5d47`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md`@`dbe7b0c10d26e1fce17802f1d56fb6baecc75983`.

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER, so every spec is buildable as written. The verdict is not
CLEAN, because thirty confirmed findings stand and four of them are HIGH.

- H1 (id 21): unit 15's commit stage stages the authored specs before the generator rewrites them.
  The commit therefore holds pre-render blobs, and the resolver's dirty-tree refusal fires on the very
  first call the unit exists to fix.
- H2 (id 16): unit 14's fixture row restates a base row, so unit 6's check 28 reds the same branch.
  Depending on landing order, AC1 is unsatisfiable or the permanent arm cannot fail.
- H3 (id 22): unit 11 states no read-before-write order for the holder row's `write_lease`, so a
  holder whose session id changed can read its own claim as foreign `live`.
- H4 (id 31): unit 12's arm keeps a hand-typed copy of the claim write table. The round-1 audit made
  it a gate only on condition that it derives that table.

Seventeen findings are MEDIUM and nine are LOW. Adjudicated, the thirty confirmed findings form
twenty-six items. Four merges were made, each within one binding grade: ids 15 and 17 (both medium,
one remedy defect seen from two routes), ids 9 and 18 (both medium, the same unobserved refusal
site), ids 23 and 24 (both medium, the same fixture assumption in units 13 and 14), and ids 30 and 37
(both low, the same dead citation). Two findings carry a grade note: id 20 restates id 8 at a lower
binding grade, and id 24's check-28 half is id 16's mechanism at a lower binding grade.

Disposition, per `memory/guides/BUILD-METHOD.md`: every CONFIRMED finding is disposed by severity.
Each HIGH is promoted to a unit whose mechanism closes it, audited as a SPEC. Each MEDIUM and LOW is
folded into its spec as a rev bump with a §9 line. H2, H3 and H4 sit on units that are themselves
round-1 promotions, so promoting them extends that chain. The method bounds a chain of promotions by
precision against the review protocol's floor. This round's precision, stated for that rule to read,
is 0.81.

## Review shape

Intensity full. Raw 37, confirmed 30, refuted 7 (ids 1, 2, 3, 4, 5, 13 and 32), unverified 0
(0 uncertain), precision 0.81.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 4 | 4 |
| MEDIUM | 14 | 17 |
| LOW | 8 | 9 |
| **total** | **26** | **30** |

By lens, raw then confirmed: underspecification 14 and 8, contradiction 6 and 6, unstated
assumption 10 and 10, prior art 7 and 6.

By unit, counting confirmed findings by the spec each one is anchored on: unit 10 holds 4, unit 11
holds 2, unit 12 holds 1, unit 13 holds 3, unit 14 holds 3 and unit 15 holds 17. Id 16 is anchored
on unit 14 and names unit 6 too.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 25 judged sound, 5 judged UNSOUND (ids 14, 16, 33, 34 and 35), 0 with
  no fix proposed, and 0 NOT JUDGED. An unjudged fix would be the finder's proposal and nothing more;
  none occurs here. For each UNSOUND fix this report writes the skeptic's corrected fix and never the
  rejected one.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 3 were RE-GRADED by the skeptic, all from high down to medium: ids 15, 23 and 24.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but no
checklist was swept, no intent was supplied, and every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the six
specs against themselves, against each other, against the round-1 audit record and against the
tree, not against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from these specs. A round-2
caller should pass the output of `python tools/memory-tree/gotchas.py --for-paths` over the specs'
Files-touched paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| A double stands in for the step whose outcome the unit exists to change | 21, 7, 6 | a real-git or traced-prompt arm in the owning suite |
| A refusal's remedy loops, or names a false cause | 15, 17, 19, 25, 29 | an arm that follows each remedy once as written |
| A fixture not pinned clean, or one that inherits ambient state | 16, 23, 24, 28, 14 | an "only offending check is N" assertion in the hygiene suite |
| A decision branch or refusal site with no criterion | 8, 20, 9, 18, 10 | the round-1 table-row-to-AC join over spec §4 |
| An identity fact copied without a stated order or one shared stamp | 22, 26 | arms in the driver suite |
| A population typed by hand rather than derived | 31 | a live derivation in the arm itself |
| An `Observed by` claim that no criterion reads | 11, 12 | a §10 checklist entry, and a candidate spec lint |
| A prior ruling, ask or method step the spec did not engage | 33, 34, 35, 36 | a §10 checklist entry |
| A locator or citation that names nothing real | 27, 30, 37 | a spec-tokens extension |

Ids appear in more than one class where the defect has two faces. Each id still sits in exactly one
graded item below.

# HIGH

## H1 · id=21 — the commit stage stages the authored specs before the generator rewrites them, so the commit holds pre-render blobs

- **Address:** TOOL-aGraftedHelix-15 §4 "The commit stage (S1, S3)", prompt step 3 ("stage each path
  that step 2 did not list and that is changed now").
- **Defect:** `gen_build_index.py --write` calls `plan(create_missing=True)`
  (`gen_build_index.py:2306`). That renders the `gen:spec-records` region into every tracked spec
  carrying a status header, and adds the region pair where it is missing (`:2088-2107`).
  `render_spec_records` always writes content, including an explicit "*No record names this unit.*".
  After step 3's `git add`, the authored specs are tracked, so `--write` rewrites them. Step 3 then
  re-stages only paths that step 2 did not list. Step 2 listed the specs, so their rendered bytes
  stay unstaged.
- **Impact:** the commit holds each authored spec's pre-render blob while the working tree holds the
  rendered one. The resolver's `HEAD:` against `hash-object` compare (template 804-811) then throws
  the dirty-tree refusal on the first call, which is the call this unit exists to fix. A fresh
  re-invoke counts the specs `alreadyPresent`, skips the stage, and meets the same throw. If the hook
  grades the stale staged region instead, the stage returns `committed: false`. Every AC uses a
  commit double, so none observes the real commit. Commit `14e5f2655` shows the generator rewriting
  the region of every sibling spec. The run refuses rather than shipping a wrong result, but the
  unit's goal fails on its main path, and its ACs certify the prompt rather than the outcome.
- **Fix — the skeptic judged it SOUND:** in step 3, after `--write`, re-stage the authored spec paths
  as well, so the stage set is the authored specs plus every path changed now that step 2 did not
  list. Add a post-commit step: `git status --porcelain -- <spec paths>` must print nothing, else
  return `committed: false`. AC1 should assert that the traced prompt orders the specs re-added after
  `--write`.
- **Left-shift gate:** one arm that runs the stage's git sequence for real in a scratch repository.
  Author a spec with no region, run steps 2 to 4 with the real generator, commit, and assert that
  `git status --porcelain` over the spec is empty and that `git rev-parse HEAD:<spec>` equals
  `git hash-object <spec>`. Observe it RED with the specs' re-stage removed from step 3. Add a §10
  checklist entry: "a double that stands in for the one step whose outcome the unit exists to change
  certifies the prompt, not the outcome."

## H2 · id=16 — unit 14's fixture row restates a base row, so unit 6's check 28 reds the same branch and check 27's block cannot be isolated

- **Address:** TOOL-aGraftedHelix-14 §4 "The fixture", §6 AC1 and §5 risks, against
  TOOL-aGraftedHelix-6. Both units sit at build step 6 with no edge between them.
- **Defect:** unit 14's branch adds a row "restating" a base row under a new id. In this build's own
  usage that is a content duplicate: unit 6's AC10 calls a same-text third row "a third row restating
  them" and expects check 28 to red it. Check 28 is always on, has no conf key, and grades the added
  set against the merge-base, so the branch run also prints `check 28:` and exits 1. Unit 14 §5 says
  AC2's clean-main run "separates check 27's red from theirs". That is false for check 28, because on
  `main` the added set is empty and check 28 cannot fire.
- **Impact:** the outcome depends on landing order. If unit 6 lands first, AC1's staged-break
  observation ("the same run exits 0") cannot be made. If unit 14 lands first, then once unit 6 lands,
  the permanent arm (a non-zero exit plus a `check 27:` line) stays green with check 27's `status=1`
  deleted. That is a could-not-fail arm, the shape this unit exists to close.
- **Grade note:** the binding grade is HIGH and this item keeps it. The could-not-fail branch has the
  rubric's blocker shape, a check that certifies what it does not check. It is HIGH because it needs
  one landing order, and because the close's staged break would likely expose it. Id 24 (in M3) is
  the same fixture seen from the other side, at medium.
- **Fix — the skeptic judged the finder's fix UNSOUND; the corrected fix:** pin the branch row as a
  paraphrase whose unit-6 content key differs from the base row's while still clearing the 0.125
  floor. Make AC1 and the arm assert that the branch run prints no `check 28:` line. Declare
  `consumes-from TOOL-aGraftedHelix-6` on unit 14, so that check 28 is present when that absence is
  asserted. Keep the bare exit-code assertion, because it is the only observation of `status=1`.
- **Left-shift gate:** the arm's "no `check 28:` line" assertion. As a class gate, the hygiene suite's
  engine arms should share one helper that asserts the run's ONLY offending check is the one under
  test, as the `_b1` precedent does (`check-memory-hygiene.test.sh:2706-2739`). Add a §10 checklist
  entry: "two specs that add checks at the same order, where one's fixture can trip the other's
  check, declare an edge."

## H3 · id=22 — the holder row's `write_lease` moves the lease facts in the middle of the call, and unit 11 states no order for it

- **Address:** TOOL-aGraftedHelix-11 §4 "The rule", row "holder renewals at --resume".
- **Defect:** the holder row calls `write_lease` from the environment when `lease-utc` is absent or
  the recorded session or pid differs from the caller's (`unattended.sh:6596-6599`). `write_lease`
  (`:5557-5572`) resets session, pid, host and `lease-utc`. Unit 11 §4 states the before/after order
  only for the `--replaces` block, and gives the holder row just "the record's lease facts". Unit 1
  S7 puts the claim read and its check 90 before any local write, so `mine` is decided before
  `write_lease`. A builder who also copies the facts before `write_lease` writes the OLD session into
  the claim, or finds no write due. `write_lease` then moves the record's session.
- **Impact:** on the next holder call the claim matches neither `mine` (the session differs) nor
  `same session` (the claim's session is not the environment's). It reads as foreign `live`, check
  90 fires, and the run must `--abort --code claim-lost`. A pid-only mismatch also resets `lease-utc`
  on every such call, so a claim write falls due on each one and the renewal throttle is bypassed.
  AC1 runs the follow-up `--resume` only under the lease's own session, so no criterion drives a
  changed session. The path is narrow, and the consequence is a live run wrongly declared lost.
- **Fix — the skeptic judged it SOUND:** state the order for the holder row as for `--replaces`:
  `mine` is decided against the facts as they stood before the row's `write_lease`, and the write
  copies the facts after it. Add an arm: `--resume --keepalive-id <recorded id>` under a changed
  `CLAUDE_CODE_SESSION_ID` exits 0, and the claim's `session` follows the record.
- **Left-shift gate:** that arm. Add a §10 checklist entry: "a rule that copies facts from a record
  names, at every call site that rewrites the record, whether it reads before or after the rewrite."

## H4 · id=31 — unit 12's arm keeps a hand-typed copy of the write table, so it cannot see a verdict or mode added later

- **Address:** TOOL-aGraftedHelix-12 §2 S3; §3 "A spec lint joining a decision table's rows to
  criteria".
- **Defect:** the round-1 audit's M8 (id=46) made this arm a gate "provided it derives its cell list
  from the section 4 table rather than from a second typed copy". Spec 12 S3 has the arm hold its own
  row per cell. Its only completeness check is that "its own table holds rows x columns cells", which
  catches a row dropped from the arm but not a verdict or mode added to `check_claim_writable`. §3
  then calls the arm "the class gate for this table", and says nothing about M8's proviso or about
  deriving from the implementation.
- **Impact:** built as written, the arm covers the 32 cells correctly today. A later verdict or mode
  would leave it green while the record still calls it the class gate, which misleads the next
  change. It is the "gate the class, not the instance" and "derive, never a second copy" shape that
  charter §7 and §12 name.
- **Fix — the skeptic judged it SOUND:** derive the row and column sets from the implementation. For
  example, expose the verdict and mode enumerations as one constant the arm reads, or extract
  `check_claim_writable`'s case labels. Then assert that the arm's typed outcomes cover exactly that
  derived set, and observe RED once by adding a phantom verdict. Otherwise, state in §3 that M8's
  condition is unmet, and record the manual check in §5 risks instead of calling the arm a class gate.
- **Left-shift gate:** the derived-set assertion is itself the gate. Add a §10 checklist entry: "an
  arm that enumerates a table compares its rows against a live derivation, never against its own
  length."

# MEDIUM

## M1 · id=15, id=17 — the remedy names a fresh re-invoke or a resume with `subjects`, and neither route fills `specPath` for units copied pathless from `--plan --paths`

- **Address:** id 15: TOOL-aGraftedHelix-15 §4 "The remedy (S5)" and §2 S5, against §2 S4 and §4
  "The resolver's notAtHead, and the pathless refusal"; also §4 "Alternatives rejected" T2. Id 17:
  §4 "The remedy (S5)" row 2, against §3 "Committing beside caller-pinned subjects" and §2 S2 and S6.
- **Defect:** the first call's `units` come from `--plan <slug> --paths`, which unit 15's own §4 shows
  printing an EMPTY path for a MISSING unit.
  - The fresh route (id 15). After an S3 refusal, the stage committed nothing and the fill never ran.
    The caller commits by hand and re-invokes with the same arguments, as the remedy says. The writers
    then count the existing spec `alreadyPresent` (template ~640), so `authoredIds` is empty, no
    commit stage runs and no fill happens. S4's pathless pre-check refuses "naming the ids", and that
    refusal ends in the same remedy. §4's stated reason, "the resolver reads HEAD live", is false for
    pathless units, because the pathless refusal fires before the resolver spawns. T2's "(a) passes"
    verdict, on which §8 F1 chose (a), rests on the same false step.
  - The resume route (id 17). S2 fills `specPath` only from the commit stage, and §3 and §4 "Trigger"
    skip that stage whenever `args.subjects` is an array. Caller `subjects` also bypass S4's pre-check
    (template 773). The cached writers still say `authored`, the units keep their empty `specPath`,
    and the unchanged `owed` filter (template 1635-1640) needs `u.specPath`. At a clean unattended
    round where every audit unit was authored, `owed` is empty and "covered NO unit" throws, ending in
    remedy row 2 again. Re-running the resume replays the cached clean `workflow:` result into the
    same throw. AC3's log line "left uncommitted" is also false on this route, because the caller
    committed them.
- **Impact:** a stuck caller, misled by the refusal's own remedy. In the `auditIds` non-empty row the
  remedy offers a fresh re-invoke only, so it loops outright. Every step is a named THROW, with no
  wrong result, no false certification and no data loss.
- **Grade note:** id 15 was graded high by the finder and medium by the skeptic. The binding grade is
  medium, and this report agrees with it.
- **Fix — the skeptic judged both fixes SOUND:**
  - Id 15: make `resumeRemedy` (all three rows) say to rebuild `units` from
    `bash tools/unattended/unattended.sh --plan <slug> --paths` after committing, so every unit
    carries its committed `specPath`. Have the S4 pathless refusal name that command as its cause. Add
    a criterion and a §7 arm: a fresh call over pathless units whose specs are committed ends in the
    pathless THROW naming `--plan`. Correct T2's verdict text. An alternative is for the writers to
    return `{id, path}` for `alreadyPresent`, and for the S2 fill to read it too.
  - Id 17: the remedy names refreshing `units` from `--plan <slug> --paths` before the resume, as for
    id 15. Add an arm: a resume with `subjects` over pathless authored units at a clean round. Make
    the AC3 log line say "left to the caller" rather than asserting that the specs are uncommitted.
- **Left-shift gate:** the two arms above. Add a §10 checklist entry: "a refusal's remedy is followed
  once as written, by an arm, and must not end in the same refusal."

## M2 · id=9, id=18 — the clean-round no-unit refusal and the audit-OFF remedy form have no criterion, though S5 says AC6 observes them

- **Address:** TOOL-aGraftedHelix-15 §2 S5 (remedy table row 1, and the clean-round no-unit site),
  against §6 AC4 and AC6 and §7's fourth new arm.
- **Defect:** S5 claims "Observed by AC6", but no criterion pins either part. AC4 never sets
  `specAudit` absent, and AC1's base call carries the audit, since its trace runs to
  `agent:audit:subjects`. So AC4's four refusals run with the audit present and the row-1 form is
  never observed. AC5 and AC6 also run with the audit present. The clean-round no-unit refusal
  currently reads "Commit the authored specs and re-invoke" (template ~1643-1645). AC6's grep for
  "re-invoke with the same arguments" cannot see that text, and neither AC6 nor §7's fourth arm
  drives that refusal.
- **Impact:** a build that leaves the clean-round refusal's old text in place passes every criterion
  and arm. That site then keeps the resume-replay trap the unit exists to remove: an operator who
  resumes after it replays the cached audit `workflow:` result and meets the same refusal. A build
  that emits the audit-present form everywhere would offer an audit-OFF caller a resume with
  `subjects`. The skeptic notes that the template's args block refuses `subjects` beside no
  `specAudit` by name, so that path ends in a named refusal rather than a cached replay.
- **Fix — the skeptic judged both fixes SOUND:**
  - Id 9: run AC4 once with `specAudit` absent, and assert that the message names a re-invoke without
    `resumeFromRunId` and carries no `git ls-tree`. Add the clean-round no-unit refusal to AC6,
    asserting that it carries `resumeFromRunId` and the row-appropriate form.
  - Id 18: add to AC6 and to §7's fourth arm a clean-round double with no owed unit, ending in a THROW
    that carries `resumeFromRunId` and, under `auditIds`, no `git ls-tree`.
- **Left-shift gate:** a source-level join. Every `throw` in the template whose text asks for a commit
  must build its tail from the one remedy constant. Grep the throw sites, compare them against the
  constant's call sites, and observe RED by leaving one site's literal text in place. Add a §10
  checklist entry: "an `Observed by ACn` claim names a criterion that drives that exact site."

## M3 · id=23, id=24 — the engine-arm fixtures of units 13 and 14 are not pinned green under every other check, so the staged break cannot be observed

- **Address:** id 23: TOOL-aGraftedHelix-13 §4 "The fixture", §2 S3 and §5 risks. Id 24:
  TOOL-aGraftedHelix-14 §4 "The fixture".
- **Defect:** AC1's staged break, in which the run with the block's `status=1` deleted exits 0,
  requires the branch fixture to be green under every other check. Neither spec says so.
  - Unit 13 S3 points at `c6run`, which asserts only rc != 2 (`check-memory-hygiene.test.sh:2285-2291`)
    over a deliberately red caps tree. §5 says other checks may red and that "AC2's clean run is what
    separates check 28's red from theirs". That is false, because AC2 runs on `main`, where the
    duplicate gotcha does not exist. A gotcha added on the branch must also pass
    `gotchas.py --check` (checks 17-19), which means a regenerated index and a gate declaration.
  - Unit 14's fixture adds a row "restating" a base row and leaves the wording unpinned. A verbatim
    restatement, which is the natural reading and the one unit 9's own selftest fixtures use, reds
    check 28 as well. Unit 14 §5 repeats unit 13's "AC2 separates" sentence, and nothing requires the
    new id to pass checks 13-16.
- **Impact:** built on the cited seam, or with §5's tolerance of other reds, the branch run exits
  non-zero whatever the block under test does. The staged break then cannot be observed. Because AC1
  itself demands an exit of 0 under the break, the pass stalls instead of landing a false arm.
- **Grade note:** both findings were graded high by the finder and medium by the skeptic. The binding
  grade is medium for both, and this report agrees. Id 24's check-28 half is the same mechanism as H2
  (id 16), which is HIGH because it also names the landing order that turns the arm into one that
  cannot fail. Folding H2 closes that half.
- **Fix — the skeptic judged both fixes SOUND:**
  - Id 23: build the fixture on the otherwise-clean precedent `_b1`
    (`check-memory-hygiene.test.sh:2706-2739`): charter, README, `stale-header-waiver.txt`, and
    `gen_build_index.py --write` plus the gotchas index regenerated on both commits. Assert, as `_b1`
    does, that the main run exits 0 and that the branch run's only offending check is 28. Delete §5's
    "AC2 separates" sentence.
  - Id 24: specify a restatement that differs in `derive_content_key` but still clears the red:0.125
    near-match floor. Assert that the branch run's only offending check is 27, and that `main` exits 0
    on an otherwise-clean tree, as `_b1` does.
- **Left-shift gate:** the shared "only offending check is N" helper named under H2. Add a §10
  checklist entry: "an arm whose red half is an exit code asserts which check produced it."

## M4 · id=7 — no criterion reads the resolver-prompt instruction that makes a real resolver fill `notAtHead`

- **Address:** TOOL-aGraftedHelix-15 §2 S4 (the resolver prompt instruction), with no §6 criterion;
  §6 AC5.
- **Defect:** only the resolver prompt's instruction makes a real resolver fill `notAtHead`. AC5's
  double returns `notAtHead` whatever its prompt says, AC2 checks only the committed path in that
  prompt, and the §7 arm's staged break deletes the `notAtHead` branch rather than the instruction.
- **Impact:** a build that omits the instruction passes everything. A real resolver then returns no
  subjects and an empty `notAtHead` on the disposal-fold re-invoke path that §3 names. The rewritten
  empty-subject refusal then says none exists on disk and the units' paths are wrong, which is a false
  diagnosis, and a partial set would audit only the resolved half. The path is narrow and the effect
  is contained.
- **Fix — the skeptic judged it SOUND:** extend AC5: the traced `agent:audit:subjects` prompt carries
  `notAtHead` and the does-not-resolve-at-HEAD instruction. Staged break: delete the instruction in
  the copy, and the probe's prompt check reds.
- **Left-shift gate:** that prompt check. Add a §10 checklist entry: "an agent double that returns a
  field whatever its prompt says cannot observe the instruction that makes a real agent return it;
  read the traced prompt."

## M5 · id=6 — AC8 compares a second render with the first, so a hand-edited committed render cannot red it

- **Address:** TOOL-aGraftedHelix-15 §6 AC8, against §2 S7.
- **Defect:** AC8's stimulus is "the template is re-rendered", and its observation is that "a second
  render" leaves porcelain unchanged. Read the way every other AC's "When X" is read, the observer
  runs both renders. The first overwrites a hand-edited committed render and the second is
  idempotent, so the red-when "a render was edited by hand" cannot fire.
- **Impact:** the pass's own check certifies render parity without testing it. Only the close's
  `review-protocol parity` leg would catch the drift, so the effect is contained to the pass's own
  check.
- **Fix — the skeptic judged it SOUND:** replace the two-render clause with: at the pass's commit,
  `bash tools/workflows/check-protocol-parity.test.sh` (check mode, its default) exits 0. That script
  covers the `unattended-build.js` pair. Alternatively, require one `--render` at the committed tree to
  leave `git status --porcelain tools/workflows/` EMPTY.
- **Left-shift gate:** the parity script in check mode, already a leg at the close. Add a §10
  checklist entry: "an idempotence check that runs the writer twice cannot see a hand edit the first
  run overwrote."

## M6 · id=8 — the out-of-folder half of validation row 4 has no criterion

- **Address:** TOOL-aGraftedHelix-15 §6 AC4, against §2 S3 and §4 "Validation" row 4.
- **Defect:** §4's validation table refuses "a path outside the build's spec folder". S3 omits that
  case. AC4's four runs drive only null, `committed: false`, a 7-hex sha and a missing id, and the §7
  arm counts "the four commit-stage refusals". Nothing observes the outside-folder refusal.
- **Impact:** a stage that accepts any returned path writes it into `specPath` (S2). The resolver then
  pins whatever blob sits there, so the audit grades a file that is not the authored spec while every
  AC stays green. It needs an agent that mislocates a spec its own prompt confines to
  `memory/builds/<slug>/spec/`, so the path is unlikely and the effect is contained.
- **Fix — the skeptic judged it SOUND:** add a fifth AC4 run. The commit double returns
  `specs: [{id: 'A-tB-1', path: 'memory/builds/other/spec/x.md'}]`, and the run ends in a THROW naming
  `A-tB-1` with no `agent:audit:subjects` line.
- **Left-shift gate:** the round-1 class gate, a join of every row of a §4 decision table to an AC or
  to an explicit `unreached` mark. L1 (id 20) is the same defect and closes with this fold.

## M7 · id=10 — the caller-supplied-path rule of the path fill has no criterion

- **Address:** TOOL-aGraftedHelix-15 §4 "The path fill (S2)", the caller-supplied-path rule, with no
  §6 criterion.
- **Defect:** where the caller supplied a different `specPath`, the rule is that a log line names both
  paths and the committed path wins. AC1 and AC2 both use a unit with no `specPath`, so a build written
  as `if (!u.specPath) u.specPath = path`, or one where the caller's path wins, passes every
  criterion.
- **Impact:** built that way, the resolver tries the caller's stale path. That path does not resolve
  and is not on disk, so it is omitted from the subjects and is not in `notAtHead` either. If other
  units resolve, the unit goes unaudited and is rostered with the stale path. The path is narrow and
  the effect is contained.
- **Fix — the skeptic judged it SOUND:** add an AC2 case. The unit carries
  `specPath: memory/builds/tB/spec/old.md` and the commit double returns a different path. The
  resolver prompt and the roster carry the committed path, and the log names both.
- **Left-shift gate:** the same table-row-to-AC join as M6, applied to a rule stated in §4 prose.

## M8 · id=27 — step 1 locates a spec by a status header that never carries the unit id

- **Address:** TOOL-aGraftedHelix-15 §4 "The commit stage (S1, S3)", prompt step 1.
- **Defect:** step 1 finds each id's spec as "the file under memory/builds/<slug>/spec/ whose status
  header carries the id". The status header is the `**Status:**` line, and `HDR_RE`
  (`gen_build_index.py:162-166`) parses it as token, rev, date, node, Tier, base, order and streams,
  with no unit id. `parse_spec_text` keys the id from the H1 line (`H1_RE`, `:167` and `:503-508`) and
  falls back to the basename. All six specs in this set show line 3 without the id.
- **Impact:** an agent that follows the locator literally matches no file and returns `specs` without
  the authored ids, so S3's fourth validation throws on every call. Otherwise the stage relies on the
  agent improvising a lookup the spec does not pin. A throw is a refused stage with a remedy, and the
  specs stay on disk, so the effect is contained.
- **Fix — the skeptic judged it SOUND:** locate by the H1 `# <id> —` line, which is the generator's
  own key, or by the `-spec-<id>.md` basename.
- **Left-shift gate:** H1's real-git arm, which drives the prompt against a real spec file, would
  observe this. Add a §10 checklist entry: "a locator in a prompt names the parser's own key, checked
  against one real file."

## M9 · id=35 — the commit stage drops the per-pass bug-class checklist the caller used to owe after the spec commit

- **Address:** TOOL-aGraftedHelix-15 §4 "The commit stage (S1, S3)", "The prompt", steps 1 to 6.
- **Defect:** BUILD-METHOD M6 counts "a spec authored" as a pass and owes
  `gotchas.py --for-diff HEAD~1..HEAD` after every pass commit, to be acted on before the next pass.
  The unattended Skill (`SKILL.template.md:736`) says the same. Steps 1 to 6 end at the commit and the
  sha, and no step or hand-out line carries the checklist. Before this unit, the caller made the spec
  commit and owed the checklist after it. §5 "migration" now has the audit-OFF caller "find nothing to
  commit", so on that route nothing names the checklist between the spec commit and the first
  dispatch. Run over the existing spec commit `14e5f2655`, the checklist selects 8 anchored
  spec-relevant classes, so it is not empty for a spec-only diff.
- **Impact:** a spec-class gotcha the checklist would name reaches the build pass unread. The effect
  is contained, because M8 runs the checklist over BASE..HEAD at every closing round. The skeptic
  notes that one part of the finding misreads the registry: "states no rule the method does not" is
  about adding rules, not omitting them.
- **Fix — the skeptic judged the finder's fix UNSOUND; the corrected fix:** add step 7: after the
  commit, run `CHECKLIST` and return its stdout in a new optional `checklist` field of
  `SPEC_COMMIT_SCHEMA`. The program then routes that output to whoever acts on it. On the audit route,
  append it to the checklist the audit receives, beside unit 3's resolver checklist. On the audit-OFF
  route, carry it in the hand-out, with the stage's sha and the instruction to act on it before the
  first dispatch. AC1 asserts that the traced prompt names `gotchas.py --for-diff HEAD~1..HEAD` and
  that the hand-out carries the field.
- **Left-shift gate:** a §10 checklist entry: "moving a step from the caller into the program moves
  every obligation the method attaches to that step; list them from BUILD-METHOD before writing the
  prompt."

## M10 · id=25 — check 91 reads a refusal file that a failed connect never rewrites

- **Address:** TOOL-aGraftedHelix-10 §2 S2 and §4 "A clone with no recorded remote HEAD".
- **Defect:** S2 has check 91 carry "the token the hook left in `<git-dir>/pre-push-refusal`". That
  assumes the file belongs to this push. The hook clears it only when the hook runs
  (`.githooks/pre-push:327-334`), and git starts pre-push only after it has connected and matched
  refs. A claim push that times out (124) or cannot connect leaves whatever an earlier push wrote,
  such as `gate-red` or `raw-push` from a refused landing. `tools/push-main.sh:121-123` clears the file
  before its own push for exactly this reason; the driver as specified does not. Unit 1 discards
  stderr in `observe_remote` and counts both cases as NOT COMPLETED, so the file is the driver's only
  way to tell them apart.
- **Impact:** check 91 names a stale refusal token, and possibly the `git remote set-head` remedy, for
  a network failure. The operator is sent to fix the wrong thing. The effect is a misleading
  diagnostic on one failure path.
- **Fix — the skeptic judged it SOUND:** remove `<git-dir>/pre-push-refusal` before every claim push,
  as push-main does, and cite a token only when the file exists after the push.
- **Left-shift gate:** an arm that seeds the file with `gate-red`, points the claim push at an
  unreachable remote, and asserts that check 91 names no token. Add a §10 checklist entry: "a file
  another program writes is cleared before the call it is read after."

## M11 · id=26 — the claim's `lease-utc` is stamped separately from the record's, so the two never agree

- **Address:** TOOL-aGraftedHelix-11 §2 S1 and §4 "The rule", first row.
- **Defect:** S1 has `--preflight` and `run_takeover` write "the values the call records into the
  lease", and `lease-utc` is one of the copied fields. `write_lease` stamps `lease-utc` itself with
  `date -u` (`unattended.sh:5569`) and takes only the file and the keepalive id. Unit 1's call-site
  table puts both claim writes before `write_lease`, and §4's inventory changes no function except
  `write_claim_beat`. So the claim's stamp must be computed earlier and separately, and it differs
  from the record's by the claim push's latency.
- **Impact:** under S2 the holder's next renewal sees a differing field and pushes at once, and until
  then `--claims` publishes a stamp the record does not hold. The `mine` test compares only keepalive
  and session, so the claim's identity stays correct. The cost is one redundant push per take and a
  briefly wrong published stamp.
- **Fix — the skeptic judged it SOUND:** compute the lease stamp once per call, pass it to both
  `write_claim` and `write_lease` (which then takes it as an argument), and list that change in the
  inventory. Alternatively, exclude `lease-utc` from S2's "a field differs" comparison.
- **Left-shift gate:** an arm: after `--preflight`, the claim's `lease-utc` equals the record's byte
  for byte, and the next `--resume` pushes nothing.

## M12 · id=28 — unit 14's fixture inherits `GOV_DEFAULT_BRANCH` from the shell

- **Address:** TOOL-aGraftedHelix-14 §4 "The fixture".
- **Defect:** AC2 (exit 0 on `main`) assumes the base derivation finds `main`. Unit 9 derives
  `<branch>` from `GOV_DEFAULT_BRANCH`, falling back to `main`, and reds an armed run with no
  resolvable base ("no mainline base", unit 9 AC7). Unit 9 AC14 makes the hygiene dispatch inherit
  that variable deliberately. The fixture is a scratch repository holding only `main`, and §4 never
  pins or unsets the variable. The hygiene suite mentions it only in the dict-key exemption list at
  `check-memory-hygiene.test.sh:2524-2529`, and run-gates does not pin it either.
- **Impact:** on any node or shell that exports `GOV_DEFAULT_BRANCH` naming a branch other than
  `main`, the armed fixture reds on `main` for an ambient reason. Exporting that variable is the
  documented remedy both the hook and push-main print, so an adopter of the copy-installed kit may
  well have it set. The result is a false red in a test arm.
- **Fix — the skeptic judged it SOUND:** run both engine commands under `GOV_DEFAULT_BRANCH=main`, or
  with `env -u GOV_DEFAULT_BRANCH`, and state that in §4.
- **Left-shift gate:** the repository already guards this class elsewhere: `migrate_backlog.py`'s
  selftest pops the ambient value, and `check-wiring.test.sh` and `push-main.test.sh` unset it. Have
  the hygiene suite's prologue do the same once, and add one arm that sets the variable to a non-main
  name and observes the fixture still green. Unit 13's fixture should be checked for the same
  dependency in the same fold.

## M13 · id=33 — unit 13 declines the round-1 H4 class gate without engaging TOOL-aDeferredBar-8, and no documented check replaces it

- **Address:** TOOL-aGraftedHelix-13 §3 "Extending check-arms.py to count a delegated dispatch block";
  §10. TOOL-aGraftedHelix-14 §3 inherits it.
- **Defect:** spec 13 declines H4's class gate, which would have `check-arms.py` count a delegated
  block that sets `status=1` with no `fail <n>` call. §10 cites only TOOL-cSpliceWarden-6 and
  TOOL-aCollapsedScan-10. It never cites TOOL-aDeferredBar-8, which is OPEN at
  `memory/backlog/TOOL.md:56` and asks for a second `check-arms.py` discovery signature for refusals
  the `fail()` signature misses. `check-arms.py:73-74` discovers only the `fail <n> "` and `fail() {`
  shapes. No spec in the set files H4's checklist entry, and `memory/gotchas/` has no presence-probe
  class. The skeptic corrects two overstatements: the decline is recorded, in spec 13's §3 and in the
  fold commit `6d361e728`'s Decided trailer; and filing no ask is not a defect, because the owner
  mandate and the README build rule forbid filing asks.
- **Impact:** under charter §7 the class has neither a gate nor a documented check. The class is live:
  it occurred twice in this build (units 6 and 9), and check 24's block remains unarmed. No shipped
  behaviour moves, but the next delegated check can again land outside the arms floor.
- **Fix — the skeptic judged the finder's fix UNSOUND; the corrected fix:** cite TOOL-aDeferredBar-8
  in §10. In §3's non-goal, name the delegated dispatch block (it sets `status=1` with no `fail <n>`
  call: checks 24, 27 and 28) as a second signature that ask must cover. Because the owner mandate
  forbids backlogging, either adopt the class gate into this build (extend `check-arms.py` and give
  check 24's block an engine arm), or record the decline under the build README's "Parked decisions"
  with the M3 veto that blocks it. Add the presence-probe class record under `memory/gotchas/` ("grep
  -n <word> over a source file is a presence probe, not an observation"), with backticked anchors on
  `tools/memory-tree/check-memory-hygiene.sh` so the checklist selects it.
- **Left-shift gate:** the `check-arms.py` extension is the gate. If it is declined, the gotcha record
  is the documented check, and its selection by `gotchas.py --for-paths
  tools/memory-tree/check-memory-hygiene.sh` is the observation that it is wired.

## M14 · id=34 — unit 10 declines the round-1 B1 class gate, and the documented check that covers it is not selected for driver diffs

- **Address:** TOOL-aGraftedHelix-10 §3 "The suite's other arms".
- **Defect:** spec 10 declines B1's class gate, which would have the unattended suite's fixture
  builder wire `core.hooksPath` to the tracked hooks and leave `GOV_DEFAULT_BRANCH` unset by default.
  The decline is reasoned. But no spec in the set carries B1's checklist entry ("a fixture made by git
  clone --local carries no core.hooksPath") or H1's ("a spec's claim about which hook branch a push
  takes names the invocation it was measured with"). `tools/unattended/unattended.test.sh:477` still
  exports `GOV_DEFAULT_BRANCH=main` for every arm. The general class already exists as
  `memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md`, but it is anchored only to govkit:
  `gotchas.py --for-paths tools/unattended/unattended.sh tools/unattended/unattended.test.sh` selects
  23 classes and not this one.
- **Impact:** a reviewer of a driver diff that adds a push never sees the documented check, so the next
  such spec can repeat the round-1 BLOCKER. Charter §7's left-shift for a confirmed blocker class is
  unmet where it matters. The effect is contained to future driver pushes, because this unit's own
  claim block is hook-wired.
- **Fix — the skeptic judged the finder's fix UNSOUND; the corrected fix:** extend
  `memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md` with the B1 instance. A `git clone
  --local` fixture carries no `core.hooksPath`, and `tools/unattended/unattended.test.sh` exports
  `GOV_DEFAULT_BRANCH=main`, so every push a spec adds to the driver is to be observed through the
  tracked hook with that variable unset. Write the paths as backticked anchors so `gotchas.py` selects
  the record for `tools/unattended/` diffs. Name that edit as a spec 10 scope item, and file no ask.
- **Left-shift gate:** after the edit, the same `gotchas.py --for-paths` command over the two driver
  files selects the record. That is the observation that the documented check is wired.

# LOW

## L1 · id=20 — validation row 4's out-of-folder branch has no observed failing case

- **Address:** TOOL-aGraftedHelix-15 §4 "Validation" table row 4, against §6 AC4 and §7's third new
  arm.
- **Defect:** row 4 refuses both a missing `authoredIds` member and "a path outside the build's spec
  folder". AC4 drives only the missing-id half, and §7's third arm counts "the four commit-stage
  refusals", which are the table's four rows. So the out-of-folder branch has no observed failing case.
- **Impact:** if that branch is omitted or broken, a path outside `memory/builds/<slug>/spec/` is
  filled into `specPath` and handed to the resolver and the roster, and nothing reds. A stray path
  needs the agent to err as well as the branch to be missing.
- **Grade note:** the binding grade is LOW and this item keeps it. It is the same defect as M6 (id 8),
  which carries a binding MEDIUM grade for the same consequence. I would grade it MEDIUM to match. The
  two skeptics weighed the likelihood differently, and the rubric grades the consequence, not the
  likelihood. Folding M6 closes this item.
- **Fix — the skeptic judged it SOUND:** add a fifth AC4 run, with `specs` naming `A-tB-1` at a path
  outside the spec folder, which must end in a THROW naming `A-tB-1`. Name that case in §7's third
  arm.
- **Left-shift gate:** as M6.

## L2 · id=19 — the empty-subject refusal states a false cause when the writers refused every audit unit

- **Address:** TOOL-aGraftedHelix-15 §4 "The resolver's notAtHead" (the empty-subject refusal's new
  cause), against §2 S4.
- **Defect:** the new cause asserts "every audit unit carried a path, none resolved at HEAD and none
  exists on disk, so the paths in units are wrong". S4's pre-check exempts units in `specRefused`, and
  `auditUnits` does not filter refused units (template 770-772). When live writers refuse every audit
  unit and those units carry no path, the all-dead throw does not fire, because `liveWriters` > 0. The
  resolver then returns no subjects and no `notAtHead`, and the refusal states that false cause.
- **Impact:** the run still refuses correctly, and the DEGRADED line names the real cause. Only the
  diagnosis is wrong.
- **Fix — the skeptic judged it SOUND:** state the cause only over audit units outside `specRefused`,
  or refuse before the resolver when every audit unit is in `specRefused`, naming those refusals.
- **Left-shift gate:** M1's §10 entry covers the class, a refusal whose stated cause is followed once
  by an arm.

## L3 · id=11 — S6 lists six carriers, and AC7 checks three of them

- **Address:** TOOL-aGraftedHelix-15 §2 S6 (the header fan paragraph, the SPEC-stage comment, the
  hand-out and owed comments, meta), against §6 AC7.
- **Defect:** AC7 checks the writers' prompt sentence, the new header paragraph and the README. It does
  not check the header line "the caller commits once after they return" (template line 107), the
  hand-out comment that says this program cannot fix the empty `specPath` (line 1534), the clean-round
  owed comment, or meta's description and Spec detail, all of which S6 requires to change.
- **Impact:** comments that contradict the code beneath them, and a stale meta description, could
  survive. Behaviour is unaffected.
- **Fix — the skeptic judged it SOUND:** add to AC7:
  `grep -c "the caller commits" tools/workflows/unattended-build.js` prints 0 (the new writers'
  sentence avoids that phrase). Also grep the hand-out comment for "commit stage" and meta's
  description for "commit".
- **Left-shift gate:** a §10 checklist entry, shared with L4: "an `Observed by` line names only the
  ACs that read that carrier." A candidate spec lint would join each S-item's `Observed by ACn` to the
  paths that AC reads; run it over the existing specs first and print hits and near-misses.

## L4 · id=12 — unit 10 S3 says AC1 observes the `write_claim` header comment, and nothing reads it

- **Address:** TOOL-aGraftedHelix-10 §2 S3 ("Observed by AC1").
- **Defect:** AC1 observes only the preflight's exit, `ls-remote`, the absence of a refusal file and
  the `pushes.log` decision. Nothing reads the comment. At base the driver holds none of
  `write_claim`, `skip-nondefault` or `GOV_BRANCH_GATE_CMD`, so a grep scoped to the header would be a
  real observation.
- **Impact:** the restatement of the hook branch that unit 1 lacks could ship missing while S3 reads as
  observed. Behaviour is unaffected.
- **Fix — the skeptic judged it SOUND:** add a grep to AC4, for example that the `write_claim` header
  names `skip-nondefault`, `<name>/HEAD` and `GOV_BRANCH_GATE_CMD`. Alternatively, relabel S3 as NOT
  OBSERVED.
- **Left-shift gate:** as L3.

## L5 · id=14 — unit 13's AC1 names an engine path the fixture does not hold, and leaves open which file the staged break edits

- **Address:** TOOL-aGraftedHelix-13 §6 AC1 (the command path and the staged-break location).
- **Defect:** AC1 runs `bash tools/memory-tree/check-memory-hygiene.sh` "at the root of the fixture's
  branch". §4 builds the fixture in the `c6run` shape, which runs the kit's own engine with its cwd at
  the fixture, and that fixture has no `tools/` directory. "Deleted in the working tree" also does not
  say which file the staged break edits. Unit 14 says "the fixture's copy".
- **Impact:** taken literally, the pass check names no file. Read the other way, the staged
  `status=1` deletion edits the tracked engine in the real worktree. A builder would notice, since no
  `check 28:` line prints, so the defect is contained to the wording.
- **Fix — the skeptic judged the finder's fix UNSOUND; the corrected fix:** state that the engine runs
  by its worktree path with cwd at the fixture root, as `c6run` does. Make the staged break in a
  scratch copy of the whole kit directory, copying `tools/memory-tree/*.sh` and `*.py` the way the
  suite's `kit21` arm does, then run the copy's engine. Never edit the tracked file.
- **Left-shift gate:** a §10 checklist entry: "a staged break names the copy it edits; the tracked
  file is never the subject of a break."

## L6 · id=29 — unit 10 S2 calls the `set-head` remedy "the hook's own", and the hook never writes it where the driver can read it

- **Address:** TOOL-aGraftedHelix-10 §2 S2.
- **Defect:** in the default-branch refusal at `.githooks/pre-push:413-420`, the "Fix once: git remote
  set-head <remote> -a" line goes only to stderr. `write_refusal` writes just `<token><TAB><why>`, and
  the why text names no remedy. Unit 1 sends every network call through `observe_remote`, which
  discards stderr.
- **Impact:** a builder who looks for the remedy in the hook's output finds nothing and must compose
  it anyway. AC3 checks only that the message names `git remote set-head`, so the shipped behaviour is
  the same either way.
- **Fix — the skeptic judged it SOUND:** state that the driver composes `git remote set-head <name> -a`
  itself for the `default-branch` token. The driver already holds `<name>` from S1.
- **Left-shift gate:** none beyond the fold; the class is M10's, a driver reading another program's
  output, and its §10 entry covers it.

## L7 · id=30, id=37 — spec 15 cites `find_build_commit`, which does not exist

- **Address:** TOOL-aGraftedHelix-15 §4 "The commit stage" (the `Pass: none` paragraph after step 6),
  §4 "Alternatives rejected" T3, and §10.
- **Defect:** `tools/` defines no function named `find_build_commit`. The function is `build_commit`
  (`tools/unattended/lib-unattended.sh:846`), lifted from check-pass-order's `_find_build_commit` (the
  comment at `:823`). Spec 15 cites the dead name three times. The two skeptics agree that the
  exclusion the spec credits is real: `build_commit` skips a commit confined to the build folder, the
  resolved generated indexes and the shared records. `read_attribution_tokens` (`:809`) separately
  maps a `Pass: none` trailer to no unit token, and is the filter that fires first. So the stated
  reason is correct but incomplete, and crediting the exclusion is the conservative reading.
- **Impact:** a reader who greps for the cited seam finds only a historical comment. The spec-tokens
  run recorded for spec 15 did not flag the name. There is no behavioural effect.
- **Fix — the skeptic judged both fixes SOUND:** rename the citation to `build_commit`. Name
  `read_attribution_tokens`'s handling of a `Pass: none` trailer as the filter that keeps the spec
  commit out of pass-order history first, and keep `build_commit`'s exclusion as the second, since
  both skeptics found it sufficient on its own.
- **Left-shift gate:** the spec-tokens leg passed a dead function name. A candidate extension resolves
  every backticked `snake_case` identifier that a spec calls a function against definitions in the
  tree. Run that predicate over the existing specs before wiring it, and print hits and near-misses
  (charter §7).

## L8 · id=36 — spec 15 answers an OPEN ask and carries no `advances` verb for it

- **Address:** TOOL-aGraftedHelix-15 status header; §3 last bullet ("A closes verb on
  TOOL-aHoistedPass-35").
- **Defect:** §3 and §10 both say S2 answers the OPEN TOOL-aHoistedPass-35
  (`memory/backlog/TOOL.md:112`), but the status line carries no `advances`. §3 justifies only the
  absence of `closes`. The harness's `renderCloses` governs `closes` only and says nothing that bars
  `advances`. The round-1 audit confirmed the identical omission on unit 5 as L8 (id=45), and unit 5
  was fixed by adding `advances`.
- **Impact:** the generated asks view keeps TOOL-aHoistedPass-35 OPEN with no linked spec, so whoever
  plans it next cannot see that S2 already answers it on every route where the commit stage runs.
- **Fix — the skeptic judged it SOUND:** add `advances TOOL-aHoistedPass-35` to the status header.
  That claims no closure, which is the concern §3 raises.
- **Left-shift gate:** this is the second instance in one build. A candidate lint: a spec whose §3 or
  §10 says it answers an OPEN ask carries `advances` or `closes` for it. Until that exists, add a §10
  checklist entry with the same text.

## What a fold should do first

1. Unit 15, the commit stage. H1 first: re-stage the specs after `--write`, check the post-commit
   status, and add the real-git arm. Then rewrite the remedy constant and every site that uses it in
   one pass, which closes M1 and M2. Fix the step-1 locator (M8) and add the checklist step (M9) in
   the same prompt edit.
2. Units 13 and 14, the engine-arm fixtures. Fold H2, M3, M12 and L5 together: one `_b1`-shaped,
   otherwise-clean fixture, a paraphrased branch row, an "only offending check is N" assertion, a
   pinned `GOV_DEFAULT_BRANCH`, and unit 14's declared edge on unit 6.
3. Unit 11, the lease identity. Fold H3 and M11 together: state the read-before-write order at the
   holder row, and compute one lease stamp per call.
4. Unit 12, the write table (H4). Derive the cell set from `check_claim_writable` before the arm is
   written, because the arm's completeness assertion depends on it.
5. Unit 10 (M10, M14, L4, L6), then the remaining single-AC additions in any order.

H1 to H4 are promoted under the method rather than folded. A round-2 audit of their promotion specs
should run with a checklist swept and an intent supplied. This round had neither.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md:section 6 (AC1, AC2) against section 2 S1, section 4 'The rule' row 3, section 8 F1 | high | - | refuted | The scenario is already observed by a criterion this unit consumes. Unit 1 AC18 runs `--resume <slug> --replaces <old> --keepalive-id <new>` and asserts the claim's keepalive is <new> and that a following `--resume <slug> --keepalive-id <new>` exits 0, once with CLAUDE_CODE_SESSION_ID unset; its arm is in unattended.test.sh (unit 1 section 7, 'the replace and re-bind writes') and the main loop runs that suite at VERIFYING (unit 11 section 7). A build of unit 11 that copies identity from the read claim inside the --replaces block writes the old keepalive back, and that arm reds on exactly the check-90 wedge F1 resolves against. The only extra field the finding names, lease-utc, is not part of the mine test (keepalive AND session), so a stale lease-utc changes no verdict. Unit 11's own ACs not repeating AC18 is not a defect in the design. The fix is unsound because --dispatch takes no --keepalive-id (unattended.sh header: `--dispatch <slug> --pass <id> --writes <path>`), so its following call is refused at argv whatever the claim says, and the --replaces block is a driver-suite --resume path, not the tick fixture's. | unsound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md:section 6 AC1 (against section 1 and section 2 S1) | high | - | refuted | The posited implementation contradicts unit 1's ordering, which unit 12 observes rather than changes. Unit 1 S5: at --preflight check 89 joins the preconditions through status and the claim write runs AFTER the write gate, so an 89 stops before any push. Unit 1 S7: run_takeover's claim decision is the 89, made by the one check_claim_writable call before write_lease. A wrong cell (take instead of refuse) therefore shows as a non-89 exit plus a created or changed run-state file, both of which AC1 reads. Pushing and then exiting 89 would need two disagreeing decisions, which is not this unit's subject. S3's per-cell arm also records whether the claim ref's sha moved for every cell, these four included (section 4 'The reachers': ls-remote before and after), so a moved ref is observed. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md:section 6 fixture paragraph and AC1 | medium | - | refuted | The fixture definition rules out an absent lease session. AC1's fixture is a run whose --liveness reads LIVE, and the liveness derivation (tools/unattended/unattended.sh, the verdict chain after derive_last_move) returns UNBOUND when the record's session is absent, before it can reach LIVE. A LIVE fixture therefore carries a non-absent session; the existing tick suite seeds RUN.md with `session: $SID`, a UUID literal (resume-tick.test.sh:80 and :167). The env-copy defect then writes absent against a non-absent lease, and AC1's positive clause reds as its red-when says. | sound |
| 4 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md:section 2 S1 (status writes and LANDING re-bind) with no section 6 criterion | medium | - | refuted | S1 does overstate what AC1 and AC2 observe, but the impact the finding claims does not occur. A HELD record's --resume goes through run_takeover with mode held: verb_resume's HELD branch calls `run_takeover <slug> <rel> <KID> held <phase>`. The take-over column takes a foreign held claim (unit 1 section 4 table), so a --hold that wrote another session's id cannot make the holder's next resume refuse with check 90. --landed and --abort leave a terminal claim, which the next --preflight takes whatever session it names. The LANDING re-bind writes the lease from its own environment, so its env and its lease facts agree. That leaves no behavioural consequence, only a traceability line that claims too much. The fix is unsound because it covers --hold alone, and its second clause cannot fail: the following resume of a HELD record runs the take-over column, which takes a foreign held claim. | unsound |
| 5 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md:section 2 S3 and section 4 'The reachers' (no closed unreached set) | medium | - | refuted | An unreached cell does not certify anything. S3 makes it carry its reason, and section 5 states that the skip announces itself, which is charter section 7's rule. Section 5 testing and section 7 also require every cell to be observed RED with its branch of check_claim_writable reverted, so a reachable cell marked unreached leaves a branch whose staged break was never seen red. The finding's example of an unreachable cell, mine at preflight, is reachable: the fixture seeds a claim carrying the keepalive and session the preflight is about to record. A closed list in advance would be a strengthening, not the fix for a defect. | sound |
| 6 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 6 AC8 (against section 2 S7) | medium | medium | confirmed | AC8's stimulus is 'the template is re-rendered' and its observation is that 'a second render' leaves porcelain unchanged. Read the way every other AC's 'When X' is read, the observer runs both renders. The first overwrites a hand-edited committed render and the second is idempotent, so the red-when 'a render was edited by hand' cannot fire. The kit's parity script defaults to --check (check-protocol-parity.test.sh, MODE=--check) and covers the unattended-build.js pair. The `review-protocol parity` leg in section 7 catches the drift at the close, so the effect is contained to the pass's own check. | sound |
| 7 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 2 S4 (resolver prompt instruction) with no section 6 criterion; AC5 | medium | medium | confirmed | Only the resolver prompt's instruction makes a real resolver fill notAtHead (section 4). No criterion reads it. AC5's double returns notAtHead whatever its prompt says, AC2 checks only the committed path in that prompt, and the section 7 arm's staged break deletes the notAtHead branch, not the instruction. A build that omits the instruction passes everything. A real resolver then returns no subjects and an empty notAtHead on the disposal-fold re-invoke path section 3 names. The rewritten empty-subject refusal would then say none exists on disk and the units' paths are wrong, which is a false diagnosis, and a partial set would audit the resolved half. That is a narrow path and the effect is contained. | sound |
| 8 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 6 AC4 (against section 2 S3 and section 4 'Validation' row 4) | medium | medium | confirmed | Section 4's validation row 4 refuses a path outside the build's spec folder. S3 omits that case, AC4's four runs are null, committed false, a 7-hex sha and a missing id, and the section 7 arm counts 'the four commit-stage refusals'. Nothing observes the outside-folder refusal. A build that omits it writes the returned path into specPath (S2), and the resolver pins whatever blob sits there. That needs an agent that mislocates a spec its own prompt confines to memory/builds/<slug>/spec/, so the path is unlikely and the effect is contained. | sound |
| 9 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 2 S5 (remedy table row 1, clean-round no-unit site) with no section 6 criterion | medium | medium | confirmed | S5 claims 'Observed by AC6', but no criterion pins either part. AC4 never sets specAudit absent. AC1's base call carries the audit, since its trace runs to agent:audit:subjects, so AC4's four refusals are naturally run with the audit present and the row-1 form is never observed. AC5 and AC6 run with the audit present. The clean-round no-unit refusal (template ~line 1643) currently reads 'Commit the authored specs and re-invoke', which AC6's grep for 're-invoke with the same arguments' does not match, and no AC drives that refusal. The §7 arms also cover only the dirty-tree remedy site. One impact detail is overstated. With specAudit absent, the template's args block refuses `subjects` by name ('is present beside no specAudit'), so a wrong row-1 remedy leads to a named refusal, not a cached replay. The effect is a wrong remedy, which is contained. A clean-round site that kept the bare 're-invoke' is the replay trap under a resume. | sound |
| 10 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'The path fill (S2)' caller-supplied-path rule, no section 6 criterion | medium | medium | confirmed | §4 'The path fill' states the rule: where the caller supplied a different path, a log line names both and the committed path wins. AC1 and AC2 both use a unit with no specPath, so a build written as `if (!u.specPath) u.specPath = path`, or one where the caller wins, passes every criterion. Built that way on this path, the resolver tries the caller's stale path. That path does not resolve and is not on disk, so it is omitted from subjects and is not in notAtHead either. If other units resolve, the unit goes unaudited and is rostered with the stale path. The path is narrow: a caller-supplied path for a unit the writers authored. The effect is contained. | sound |
| 11 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 2 S6 (header fan paragraph, SPEC-stage comment, hand-out and owed comments, meta) against AC7 | low | low | confirmed | S6 lists six carriers and claims 'Observed by AC7'. AC7 checks only the writers' prompt sentence, the new header line and the README. The template's header fan line 107 ('the caller commits once after they return'), the hand-out comment at line 1534 ('this program cannot fix it'), the clean-round owed comment, and meta's description and Spec detail (neither contains 'commit' today) are all unchecked. These are comments and metadata only, with no behavioural effect. | sound |
| 12 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-10.md:section 2 S3 ('Observed by AC1') | low | low | confirmed | S3 says the write_claim header comment is 'Observed by AC1'. AC1 observes only the preflight's exit, ls-remote, the absence of a refusal file and the pushes.log decision, and nothing reads the comment. A missing comment would ship while S3 reads as observed. There is no behavioural effect. At base the driver holds none of write_claim, skip-nondefault or GOV_BRANCH_GATE_CMD, so a grep scoped to the write_claim header is a real observation. | sound |
| 13 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md:section 6 AC1 (take-over over foreign `terminal`) | low | - | refuted | The cell is the take-over against a foreign `terminal` claim, and `terminal` is a verdict, not a status: unit 1's write table keys its rows on the verdict. AC1 drives that cell through a `landed` claim, which unit 1's verdict table maps to `terminal`, so the cell S1 names is observed. Whether `aborted` also derives `terminal` belongs to the verdict table (unit 1's status-to-verdict mapping). That is a different table from the claim write table this unit's scope ('every cell of the claim write table') and its non-goal ('Changing a cell. The table is unit 1's') confine it to. The finding asks for coverage of the verdict derivation, not of a write-table cell. | sound |
| 14 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-13.md:section 6 AC1 (command path and staged-break location) | low | low | confirmed | §4 builds the fixture as 'a scratch git repository holding the hygiene suite's minimal tree', the c6run shape. c6run runs `bash "$SCRIPT"` (the kit's own engine) with its cwd at the fixture, and the fixture has no tools/ directory. AC1's literal `bash tools/memory-tree/check-memory-hygiene.sh` 'at the root of the fixture's branch' therefore names a file that does not exist. 'Deleted in the working tree' leaves open whether the staged break edits the tracked engine. Unit 14 says 'the fixture's copy'. A builder would notice, since no `check 28:` line prints, so the defect is contained to the wording. | unsound |
| 15 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'The remedy (S5)' and section 2 S5, against section 2 S4 / section 4 'The resolver's notAtHead, and the pathless refusal'; also section 4 'Alternatives rejected' T2 | high | medium | confirmed | The mechanism holds against the template. Unit 15's own §4 says `--plan --paths` prints an EMPTY path for a MISSING unit, so the first call's units are pathless. On an S3 refusal the stage committed nothing and the fill never ran. The caller commits by hand and re-invokes fresh with the same args, as the remedy says. The writers' prompt then counts the existing spec alreadyPresent (template line ~640), so authoredIds is empty, no commit stage runs and no fill happens. S4's pathless pre-check then refuses 'naming the ids', and that refusal ends in the same remedy. §4's stated reason, 'the resolver reads HEAD live', is false for pathless units, because the pathless refusal fires before the resolver spawns. Only §3's non-goal mentions re-reading `--plan --paths`. Neither the remedy constant nor the pathless refusal is required to say it, and no AC drives a fresh re-invoke. In the `auditIds` non-empty row the remedy offers a fresh re-invoke only, so it loops outright. In the empty row the resume-with-subjects branch is an exit, though it hands out a pathless roster. Severity is medium, not high: every step is a named THROW, with no wrong result, no false certification and no data loss. The effect is a stuck caller misled by the refusal's own remedy. | sound |
| 16 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-14.md:section 4 'The fixture', section 6 AC1 and section 5 risks, against TOOL-aGraftedHelix-6 (same build step 6, no edge between them) | high | high | confirmed | Unit 14 §4 has the branch add a row 'restating' a base row under a new id. In this build's usage that means a content duplicate: unit 6's AC10 calls a same-text third row 'a third row restating them' and expects check 28 to red. Unit 6's check 28 is always on, has no conf key and grades the added set against the merge-base, so a verbatim branch row also prints `check 28:` and exits 1. Unit 14 §5's claim that AC2's clean-main run 'separates check 27's red from theirs' is false for check 28, because on main the added set is empty and check 28 cannot fire. Units 6 and 14 share build step 6 with no edge between them. If 6 lands first, AC1's staged-break observation ('the same run exits 0') fails. If 14 lands first, the permanent arm (non-zero exit plus a `check 27:` line) stays green with check 27's status=1 deleted once 6 is present, which is a could-not-fail arm. The close's staged break would likely expose it, but the spec as written yields either an unsatisfiable AC or an arm that cannot fail. | unsound |
| 17 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'The remedy (S5)' row 2 (resume with `subjects`), against section 3 'Committing beside caller-pinned subjects' and section 2 S2 / S6 | medium | medium | confirmed | Unit 15 §2 S2 fills specPath only from the commit stage's `specs`. §3 and §4 'Trigger' skip that stage whenever `args.subjects` is an array, and S4's pathless pre-check sits inside the resolver branch, which caller `subjects` bypass (template line 773). So on remedy row 2 the cached writers still say `authored`, the units keep the empty specPath the caller copied from `--plan --paths` (spec §4 shows that verb printing an empty path for a MISSING unit), and the unchanged `owed` filter (template 1635-1640) needs `u.specPath`. At a clean unattended round where every audit unit was authored, `owed` is empty and the 'covered NO unit' throw fires. Under S5 that throw ends in the same remedy, and re-running the resume replays the cached clean `workflow:` result into the same throw. AC3's 'left uncommitted' log is also false on that route. The effect is contained: the fresh re-invoke named beside it ends in S4's pathless refusal, which points at `--plan --paths`. | sound |
| 18 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 2 S5 ('Observed by AC6'), against section 6 AC6 and section 7's fourth new arm | medium | medium | confirmed | S5 lists the clean-round no-unit refusal among the sites that end in the remedy and says 'Observed by AC6'. §4 says it 'ends the same way'. AC6 drives only the empty-subject refusal and the dirty-tree refusal, and §7's fourth arm names the notAtHead, partial, pathless and empty refusals plus the dirty-tree remedy, never the clean-round one. AC6's grep for 're-invoke with the same arguments' cannot see the current text, which is 'Commit the authored specs and re-invoke' (template 1645). A build that leaves that site unchanged passes every criterion and arm, and that site keeps the resume-replay trap the unit exists to remove. | sound |
| 19 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'The resolver's notAtHead' (the empty-subject refusal's new cause), against section 2 S4 | low | low | confirmed | S4's pre-check exempts units in `specRefused`. `auditUnits` does not filter refused units (template 770-772), and the resolver prompt skips a unit with no path. When live writers refuse every audit unit and those units carry no path, the all-dead throw does not fire because `liveWriters` > 0. The resolver then returns no subjects and no `notAtHead`, and the empty-subject refusal states the new cause from §4: 'every audit unit carried a path ... so the paths in units are wrong'. That cause is false here. The run still refuses correctly, and the DEGRADED line names the real cause, so only the diagnosis is wrong. | sound |
| 20 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'Validation' table row 4, against section 6 AC4 and section 7's third new arm | low | low | confirmed | Row 4 of the §4 Validation table refuses both a missing `authoredIds` member and 'a path outside the build's spec folder'. AC4 drives only the missing-id half, and §7's third arm counts 'the four commit-stage refusals', which are the table's four rows. So the out-of-folder branch has no observed failing case. The effect is contained and unlikely to bite: the prompt tells the agent to look under `memory/builds/<slug>/spec/`, so a stray path needs the agent to err as well as the branch to be missing. | sound |
| 21 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 "The commit stage (S1, S3)", prompt step 3 | high | high | confirmed | Verified in gen_build_index.py. `cmd_write` calls `plan(create_missing=True)` (line 2307), and that renders the `gen:spec-records` region into every tracked spec carrying a status header, adding the pair when it is missing (2088-2107). `render_spec_records` always writes content, an explicit '*No record names this unit.*' included. After step 3's `git add`, the authored specs are in that population, so `--write` rewrites them. Step 3 then re-stages only paths 'that step 2 did not list'. Step 2 listed the specs, which were untracked at the time, so their rendered bytes stay unstaged. The commit then holds pre-render blobs while the working tree holds rendered ones. The resolver's `HEAD:` vs `hash-object` compare (template 804-811) throws the dirty-tree refusal on the very first call this unit exists to fix. A fresh re-invoke counts the specs `alreadyPresent`, skips the stage, and meets the same throw. If instead the hook grades the stale staged region, the result is `committed: false`. Every AC uses a commit double, so none sees this. Commit 14e5f2655 shows the generator rewriting the region of every sibling spec. The run refuses rather than shipping a wrong result, but the unit's goal fails on its main path, and its ACs certify the prompt and not the outcome. | sound |
| 22 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md:section 4 "The rule", row "holder renewals at --resume" | high | high | confirmed | The holder row at unattended.sh 6595-6600 calls `write_lease` from the environment when `lease-utc` is absent or the recorded session or pid differs. `write_lease` (5557-5572) resets session, pid, host and lease-utc. Unit 11 §4 states the before/after order only for the `--replaces` block, and gives the holder row just 'the record's lease facts'. Unit 1 S7 puts the claim read and its check 90 'before any local write', so `mine` is decided before `write_lease`. A builder who also copies the facts before `write_lease` writes the OLD session into the claim, or finds no write due. `write_lease` then moves the record's session. On the next holder call the claim matches neither `mine` (session differs) nor `same session` (the claim's session is not the env's), so it reads as foreign `live`, check 90 fires, and the run must abort `claim-lost`. The finder's specific route, `mine` decided after `write_lease`, is ruled out by unit 1, but the unstated order reaches the same wrong outcome. AC1 runs the follow-up `--resume` only under the lease's own session, so no criterion drives a changed session. The path is narrow, and the consequence is a live run wrongly declared lost. | sound |
| 23 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-13.md:section 4 "The fixture", section 2 S3 and section 5 risks | high | medium | confirmed | AC1's staged break, where the run with `status=1` deleted exits 0, requires the branch fixture to be green under every other check. The spec never says so. S3 points at `c6run`, which asserts only rc != 2 (test.sh 2285-2291) over a deliberately red caps tree. §5 says other checks may red and that 'AC2's clean run is what separates check 28's red from theirs'. That is false, because AC2 runs on `main`, where the duplicate gotcha does not exist. A gotcha added on the branch must also pass `gotchas.py --check` (checks 17-19, template 2460-2465), which means a regenerated index and a gate declaration. Built on the cited seam with the tolerated reds, the branch exits non-zero whatever check 28's block does. The effect is contained: AC1 itself demands an exit of 0 under the break, so the pass stalls instead of landing a false arm. The spec misdirects the builder; it does not certify a false green. | sound |
| 24 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-14.md:section 4 "The fixture" | high | medium | confirmed | Unit 6, at the same order 6, adds check 28 with no arming knob. Check 28 reds any decision row added since the merge-base whose `derive_content_key` equals another identity's. Unit 9 §3 leaves exact duplicates to check 28 and does not exempt them from check 27. Unit 14's fixture adds a row 'restating' a base row and leaves the wording unpinned, so a verbatim restatement, the natural reading and the one unit 9's own selftest fixtures use, reds check 28 as well. With the check-27 block's `status=1` deleted, the branch still exits 1, so AC1's break cannot be observed. Unit 14 §5 repeats unit 13's wrong 'AC2 separates' sentence, and nothing requires the new id to pass checks 13-16. As with 23, AC1's own exit-0 demand turns this into a stalled pass rather than a false arm. | sound |
| 25 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-10.md:section 2 S2 and section 4 "A clone with no recorded remote HEAD" | medium | medium | confirmed | Spec 10 S2 and the section 4 paragraph 'A clone with no recorded remote HEAD' have check 91 carry 'the token the hook left in <git-dir>/pre-push-refusal'. Nothing in spec 10 or unit 1 says when that file belongs to this push, and unit 1 never mentions the file. The hook clears it only when the hook runs (.githooks/pre-push:327-334). Git starts pre-push only after it has connected and matched refs, so a push that cannot connect, or times out before the hook runs, leaves whatever an earlier push wrote. tools/push-main.sh:121-123 documents the same file as 'cleared by it on every run and by this script before every push', because of this. The driver cannot tell a hook refusal from a network failure except through the file, since unit 1 discards stderr in observe_remote and counts both as NOT COMPLETED. So a driver built as written cites a stale token, and possibly the set-head remedy, for a network failure. The effect is a misleading diagnostic on one failure path, which is contained. | sound |
| 26 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-11.md:section 2 S1 and section 4 "The rule", first row | medium | medium | confirmed | Spec 11 S1 says the claim carries 'the identity the run's lease record holds once the call is done', and it says --preflight and run_takeover write 'the values they record into the lease'. lease-utc is one of the copied fields. write_lease stamps lease-utc itself with date -u (unattended.sh:5569 at base 5266d22e) and takes only (file, keepalive-id). Unit 1's call-site table puts both claim writes before write_lease: '--preflight ... before rotation' and 'run_takeover, before write_lease'. The claim's stamp therefore has to be computed earlier and separately, and it differs from the record's by the push latency. Under S2 every later renewal compares the claim with the record's lease-utc, so the holder's first call finds a differing field and pushes at once. Until then, --claims publishes a stamp the record does not hold. The spec's own invariant does not hold for this field. The cost is one redundant push per take plus a briefly wrong published stamp. The mine test compares only keepalive and session, so the claim's identity stays correct, and the effect is contained. | sound |
| 27 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 "The commit stage (S1, S3)", prompt step 1 | medium | medium | confirmed | Step 1 of spec 15's commit-stage prompt locates each spec as the file 'whose status header carries the id'. In this repo the status header is the '**Status:**' line. HDR_RE (gen_build_index.py:162-166) parses that line as token, rev, date, node, Tier, base, order and streams, with no unit id. The id comes from H1_RE on the '# <id> —' line, falling back to the basename (gen_build_index.py:167 and 503-508). All six specs in this set show line 3 without the id. An agent that follows the step literally matches nothing, so the fourth validation, an authoredIds member with no specs entry, throws. The alternative is that the agent improvises a lookup the spec does not pin. A throw is a refused stage with a remedy, and the authored specs stay on disk, so the effect is contained. | sound |
| 28 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-14.md:section 4 "The fixture" | medium | medium | confirmed | Spec 9 S2 derives the base from origin/<branch>, then <branch>, where <branch> is GOV_DEFAULT_BRANCH or main. An armed run with no resolvable base reds with 'no mainline base' (spec 9 AC7). Spec 9 AC14 makes the hygiene dispatch inherit that variable deliberately. The fixture in spec 14 section 4 is a scratch repo holding only 'main', and section 4 never pins or unsets the variable. The hygiene suite mentions GOV_DEFAULT_BRANCH only in the dict-key exemption list at check-memory-hygiene.test.sh:2524-2529, and run-gates does not pin it either. Exporting GOV_DEFAULT_BRANCH=<branch> is the documented remedy that both the hook and push-main print. An adopter of the copy-installed memory-tree kit whose default branch is not main may therefore have it set. Under that value, AC2's clean run reds for an ambient reason. The repo already guards this class elsewhere: migrate_backlog.py's selftest pops the ambient value, and check-wiring.test.sh and push-main.test.sh unset it. The result is a false red in a test arm, which is contained. | sound |
| 29 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-10.md:section 2 S2 | low | low | confirmed | In the default-branch refusal at .githooks/pre-push:413-420, the 'Fix once: git remote set-head <remote> -a' line goes only to stderr. write_refusal writes just '<token><TAB><why>' to the file, and the why text names no remedy. Unit 1 sends every network call through observe_remote, which discards stderr (unit 1 spec section 4 Evidence, and section 5 security). So the driver cannot read the remedy from the hook, as S2's phrase 'the hook's own remedy' suggests. The builder must compose the remedy, and the driver already holds <name> from S1. AC3 only checks that the message names 'git remote set-head', so the shipped behaviour is the same either way. The cost is builder confusion, which makes this low. | sound |
| 30 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 "The commit stage" (`Pass: none` paragraph), section 4 T3, section 10 | low | low | confirmed | tools/ has no function named find_build_commit. The function is build_commit (lib-unattended.sh:846). Its header says it was lifted from check-pass-order.sh, where it was called _find_build_commit. Spec 15 cites find_build_commit three times (section 4 at line 159, T3 at line 297, and section 10 at line 482). The exclusion the spec describes does belong to build_commit (lines 833-845), so that part of the prose is accurate. read_attribution_tokens (:809) separately maps a 'Pass: none' trailer to no unit token. The finding is therefore half wrong when it says the folder exclusion is not what keeps the commit out, because both mechanisms do. The cited name is still wrong. The spec-tokens run recorded for spec 15 did not flag it, so this is a citation error with no behavioural effect. | sound |
| 31 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md:section 2 S3; section 3 'A spec lint joining a decision table's rows to criteria' | high | high | confirmed | The round-1 audit's M8 (id=46, review record lines 436-437) made the arm a gate 'provided it derives its cell list from the section 4 table rather than from a second typed copy'. Spec 12 S3 has the arm hold its own row per cell, and its only completeness check is that 'its own table holds rows x columns cells'. That check is tautological about the population: it catches a row dropped from the arm, not a verdict or mode added to check_claim_writable. Section 3 then declares 'this arm is the class gate for this table'. It declines only the spec-prose lint, and says nothing about M8's proviso or about deriving from the implementation, so no non-goal withholds the finding. Built as written, the arm covers the 32 cells correctly today. A later verdict or mode would leave it green while the record still calls it the class gate. That misleads the next change, which is high under the rubric. It is also the 'gate the class, not the instance' and 'derive, never a second copy' shape that charter sections 7 and 12 name. | sound |
| 32 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-12.md:section 3 'The resume matrix'; section 10 | medium | - | refuted | TOOL-dDerivedDocket-40 (memory/builds/dDerivedDocket/BACKLOG.md:7 and :410) is a KEEP ask, 'still wanted after this build closes, outside its goal'. It was declined under unattended protocol section 11 test 1, which is the adoption rule for a DISCOVERY joining a running unattended build. It is not a ruling against the shape, so there are no 'two records giving opposite answers'. The finder's own fix concedes that section 11 does not bind a --review promotion. The decline's second reason was 'a scan over this repo's spec text would be a real-tree assertion in a shipped suite', and it does not reach spec 12's arm, which reads no spec text. Spec 12 cites the ask exactly as the audit's M8 instructed: as prior art in section 10 with no header verb, plus 'this arm moves neither its guide nor its leg' in section 3. Section 7 already says the unattended suites are not on the bar, so 'class gate' is loose wording, not a defect. | sound |
| 33 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-13.md:section 3 'Extending check-arms.py to count a delegated dispatch block'; section 10 (inherited by TOOL-aGraftedHelix-14 section 3) | medium | medium | confirmed | Spec 13 section 3 (blob eb8eba2d) declines the round-1 audit's H4 class gate, which is to extend check-arms.py to count a delegated dispatch block. Section 10 cites only TOOL-cSpliceWarden-6 and TOOL-aCollapsedScan-10. It never cites TOOL-aDeferredBar-8, which is OPEN at memory/backlog/TOOL.md:56 and asks for a second check-arms.py discovery signature for refusals the fail() signature misses. That is the same tool and the same kind of gap. check-arms.py:73-74 discovers only the `fail <n> "` and `fail() {` shapes. No spec in the set files H4's section 10 checklist entry, and memory/gotchas has no presence-probe class. Under charter section 7 the class therefore has neither a gate nor a documented check. The class is live: it occurred twice in this one build (units 6 and 9), and check 24's block remains unarmed. Spec 14 section 3 defers to spec 13, so it inherits the gap. Two parts of the finding are overstated. The decline is recorded in spec 13's own section 3 and in the fold commit 6d361e728's Decided trailer, so 'recorded nowhere' is too strong. And 'files no ask' is not a defect, because the owner mandate (prompt record 1-0, 'do not backlog anything') and the README build rule ('never filed as asks') forbid filing asks. The effect is contained: no shipped behaviour moves, but the next delegated check can again land outside the arms floor. | unsound |
| 34 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-10.md:section 3 'The suite's other arms' | medium | medium | confirmed | Spec 10 section 3 'The suite's other arms' (blob 0ac3b991) declines B1's class gate, which would wire the fixture builder's core.hooksPath and leave GOV_DEFAULT_BRANCH unset by default. The decline is reasoned. But no spec in the set carries B1's checklist entry ('a fixture made by git clone --local carries no core.hooksPath') or H1's ('a spec's claim about which hook branch a push takes names the invocation it was measured with'). tools/unattended/unattended.test.sh:477 does still export GOV_DEFAULT_BRANCH=main for every arm. The finding misses one thing: the general class already exists as memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md. That record is anchored only to govkit, though. `gotchas.py --for-paths tools/unattended/unattended.sh tools/unattended/unattended.test.sh` does not select it (verified: 23 classes, none of them this one). So a reviewer of a driver diff that adds a push never sees the documented check. Charter section 7's left-shift for a confirmed BLOCKER class is therefore unmet where it matters. The effect is contained to future driver pushes, because this unit's own claim block is hook-wired. | unsound |
| 35 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'The commit stage (S1, S3)', 'The prompt' steps 1-6 | medium | medium | confirmed | BUILD-METHOD M6 counts 'a spec authored' as a pass and owes `gotchas.py --for-diff HEAD~1..HEAD` after every pass commit, to be acted on before the next pass. The unattended Skill (SKILL.template.md:736) says the same, 'after every commit'. Spec 15 section 4's prompt steps 1-6 end at the commit and the sha, and no step or hand-out line carries the checklist. Before this unit, the caller made the spec commit and owed the checklist after it. Section 5 'migration' now has the audit-OFF caller 'find nothing to commit', so on that route nothing names the checklist between the spec commit and the first dispatch. Running it over the existing spec commit 14e5f2655 selects 8 anchored spec-relevant classes (e.g. observed-by-claim-no-arm-discharges, fold-text-is-unreviewed-surface), so it is not empty for a spec-only diff. One part of the finding is a misreading: the registry's 'states no rule the method does not' is about adding rules, not omitting them. The effect is contained, because M8 runs the checklist over BASE..HEAD at every closing round. | unsound |
| 36 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:status header; section 3 last bullet ('A closes verb on TOOL-aHoistedPass-35') | low | low | confirmed | Spec 15's status line (blob dbe7b0c1, line 3) carries no `advances`. Section 3's last bullet and section 10 both say S2 answers the OPEN TOOL-aHoistedPass-35 (memory/backlog/TOOL.md:112). Section 3 justifies only the absence of `closes`, saying the writer's roster carried no closes list. The harness's renderCloses governs `closes` only and says nothing that bars `advances`. This build's own round-1 audit confirmed the identical omission on unit 5 as L8 (id=45, graded LOW), and unit 5's header now reads 'advances TOOL-aSurfacedLexicon-22'. The only consequence is the generated asks view, so it is low. | sound |
| 37 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-15.md:section 4 'The prompt' (paragraph after step 6); section 4 'Alternatives rejected' T3; section 10 | low | low | confirmed | `find_build_commit` is not defined anywhere in tools/. The function is `build_commit` at tools/unattended/lib-unattended.sh:846, lifted from check-pass-order's `_find_build_commit` (comment at :823), and spec 15 cites the dead name three times. One part of the finding is wrong: the path exclusion the spec credits is real and sufficient. build_commit skips a commit confined to the build folder, the resolved GENERATED_INDEXES and SHARED_RECORDS, and the stage stages only specs and generator outputs. read_attribution_tokens (:809) emptying a `Pass: none` commit's tokens is simply the filter that fires first. So the stated reason is correct but incomplete, and the claimed danger (a reader concluding that staging outside the exclusion is safe) runs backwards, because crediting the exclusion is the conservative reading. The defect is a dead citation, so it is low. | sound |

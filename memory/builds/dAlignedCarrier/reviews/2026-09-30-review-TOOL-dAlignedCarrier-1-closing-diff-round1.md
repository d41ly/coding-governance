**Serves:** diff-review TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6

# dAlignedCarrier: Tier-2 closing diff review of units 1 to 6, round 1

*Node `d`, 2026-09-30, the unattended build's closing review under `memory/guides/BUILD-METHOD.md`.
Harness: `tools/workflows/tier2-review.js`, with four primed finder lenses, five skeptic batches
prompted to REFUTE each finding, and this synthesis. The lens brief was the recurring-bug-class
checklist that `python tools/memory-tree/gotchas.py --for-diff 87c245b3..3c45a567` selected
(40 anchored classes plus 6 universal). Each unit's acceptance ledger is under
`memory/builds/dAlignedCarrier/build/`.*

**Range reviewed: `87c245b3e950cbf7bc46b8216db8b4e4fba253dd...3c45a567159e7156bd40a5189fd61c2ac3365d9a`**
(branch `run/dAlignedCarrier`, 35 files, +2483/−167).

**Round: 1.**

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. Two items are MEDIUM and two are LOW, and every confirmed
finding sits in unit 6's surface. Both mediums are the same kind of failure: the Close sequence
that unit 6 wrote into the Skill does not do what it says when followed literally. Under `in-place`,
which is this repo's mode, the move into `VERIFYING` leaves the run-state file half-staged, so the
next step refuses. Under `primary`, which is the kit default, the export the notice prescribes pays
for a guard-scoped self-test run, not the flagged bar the notice says is owed. This report folds
nothing. Each item is owed a fix under unit 6's spec before the build lands, and the fold is owed a
round 2.

## Review shape and run integrity

- **Raw 10, confirmed 9, refuted 1, unverified 0, precision 0.90**, which is 9 / (9 + 1).
- **Refuted:** one raw finding, id 5, did not survive its skeptic. Its text did not reach this
  synthesis, so it is recorded here as a count only.
- **Adjudicated tally by item:** 4 items. That is 0 BLOCKER, 0 HIGH, 2 MEDIUM (M1, M2) and 2 LOW
  (L1, L2).
- **Adjudicated tally by raw confirmed finding:** 0 BLOCKER, 0 HIGH, 6 MEDIUM (ids 2, 3, 4, 6, 7,
  9) and 3 LOW (ids 1, 8, 10). That totals 9, and every confirmed id is in exactly one item.
- **Merges:** the harness reported 0 duplicates, and it only counts identical findings. This
  synthesis merged findings that different lenses reported for the same defect: M1 is ids 2, 4, 6
  and 9, M2 is ids 3 and 7, and L2 is ids 8 and 10. A merged item takes the highest severity any of
  its members earned on adjudication, and the per-item notes below say where that moved a raw label.
- **Run integrity:** lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. No
  contradictory verdict was demoted to unverified, no spurious verdict was discarded, and there were
  0 duplicates. Every counter is zero, so **this run is complete**, and the finding set is the
  lenses' whole result, not one missing a dead lens's share.
- **What the synthesis checked itself:** it re-read every cited site at `3c45a567` and re-pinned
  the line numbers below. It reproduced L1's rename behaviour in a scratch repository under the
  session scratchpad, and it observed M1's half-staged record live in this worktree.

## Findings

| # | Sev | Where | What | Raw ids |
|---|---|---|---|---|
| M1 | medium | `tools/unattended/unattended.sh:4221` | `verb_phase` stages the record before it writes the witness, so the new Close step commits half the record | 2, 4, 6, 9 |
| M2 | medium | `tools/unattended/unattended.sh:7127` | under `primary`, the notice's remedy buys a guard-scoped self-test run, not the flagged bar | 3, 7 |
| L1 | low | `tools/unattended/unattended.sh:7117` | the owed-bar range read is blind to a rename out of a declared prefix | 1 |
| L2 | low | `tools/unattended/check-unattended.sh:2942` | check 45's header still names the in-place close as the announcer | 8, 10 |

### M1 — the VERIFYING move stages half the record, and the Close step commits that half

**Where:** `tools/unattended/unattended.sh:4218-4222` (`verb_phase`). The Skill sentences that
depend on it are `tools/unattended/SKILL.template.md:909` and `:935`. The arm that hides it is
`tools/unattended/unattended.test.sh:8757`.

**Defect.** `verb_phase` runs `set_fact phase` (4218), then `stage_or_fail` (4221), then
`set_fact witness` (4222). The staged blob pairs the new phase with the PREVIOUS phase's witness,
and the new witness line stays unstaged. The witness is normally HEAD, and HEAD has normally moved,
so this is the common case. The ordering predates this diff (base `87c245b3`, line 4210, from
TOOL-aBoundedVerdict-15 S1). Unit 6 made it load-bearing when it wrote "commit the record the move
stages" (909) and "a move stages the record" (935).

**Impact.** Follow the Close section literally under `in-place`: move, commit what is staged, then
prepare. The commit leaves ` M RUN.md`. `push-main.sh --prepare` refuses any non-empty porcelain at
`tools/push-main.sh:451-455`, which is before `--close`'s check 62 is ever reached. The committed
`VERIFYING` record carries the prior phase's witness. Line 935 blames that refusal on a SECOND
move, but the first move already causes it. This build shows the state right now: after its
`--phase dAlignedCarrier REVIEWING`, `git status` reads `MM memory/builds/dAlignedCarrier/RUN.md`.
The index holds `phase: REVIEWING` with witness `fd3ac307`, and the worktree holds witness
`3c45a567`. The damage is bounded. The refusal names the path and one `git add` recovers it. For a
non-terminal phase, checks 5 and 6 require only that the witness resolves, so the stale witness
flips no verdict.

**Adjudication: MEDIUM.** Raw ids 2 and 4 were confirmed as low, and ids 6 and 9 as medium. The
item takes medium because the documented close sequence fails on its first step in this repo's own
declared mode. The arm that should catch this runs its own `add -A`, which does the staging the
Skill says the move does, so that arm cannot fail on this.

**Fix.** Move `stage_or_fail "$rel" || return 1` below `set_fact "$rel" witness "$wit" || return 1`.
The move still stages, so TOOL-aBoundedVerdict-15 S1's property holds, and Skill lines 909 and 935
become true as written. **For this run:** the fixed driver's next move stages the leftover witness
line along with everything else. With the unfixed driver, `git add` the record before the
`VERIFYING` commit.

**Left-shift gate.**

- **Unit-6 arm:** commit only the staged set before `records: VERIFYING`, which means dropping the
  `add -A` at `unattended.test.sh:8757`. Then assert
  `same "the VERIFYING move leaves nothing unstaged" "$(ipgit diff --name-only)" ""`.
- **TOOL-aBoundedVerdict-15 arm:** near `unattended.test.sh:2652`, assert an empty unstaged diff
  too, not only a non-empty cached one.
- **The class:** a static predicate in `check-unattended.sh` that no function calls `set_fact` on a
  file after its last `stage_or_fail` of that file. Per §7, run the predicate over `unattended.sh`
  first and print hits and near-misses before wiring it in.

### M2 — under `primary`, the prescribed export does not pay the flagged bar

**Where:**

- The notice at `tools/unattended/unattended.sh:7127`.
- The two gates-green bar invocations: `:7505` under `primary`, which carries no `GATE_FULL`, and
  `:7497` under `in-place`, which carries `GATE_FULL=1`.
- The same remedy in `tools/unattended/SKILL.template.md:948-954` ("under either mode"), in the
  `SELFTESTS_OWED_PATHS` row at `tools/unattended/PROTOCOL.template.md:458` and
  `memory/guides/UNATTENDED-PROTOCOL.md:458`, and in the comments on that key in `.unattended.conf`
  and `tools/unattended/.unattended.conf.example`.

**Defect.** Unit 6 moved the notice to the `VERIFYING` move under every `LANDER_MODE`. Its remedy
is to export `GATE_SELFTESTS=1` into the one `--close`, "whose bar inherits it". Under `in-place`
the close adds `GATE_FULL=1`, so the inherited flag completes the pair. Under `primary` the bar runs
with no `GATE_FULL`. `changed()` at `tools/run-gates/run-gates.sh:262` returns early only on
`GATE_FULL`. `GATE_SELFTESTS=1` lifts the hold (`run-gates.sh:1749-1756`), but every guarded
self-test leg whose guard path the branch did not move against the merge-base still reports
`skip`. A skeptic counted 57 of 61 self-test legs as guarded at `3c45a567`. Under `primary` the push
is a separate lander command. Its pre-push forces `GATE_FULL`, but it does not inherit a flag that
was exported only into `--close`, so nothing on that path pays the pair. The base notice (base
`87c245b3`, line 7057) named `GATE_FULL=1 GATE_SELFTESTS=1`. It could leave `GATE_FULL` implicit
because it announced only from the in-place close. Spec 6's F3 reasoned only about inheriting the
exported flag and missed the absent `GATE_FULL`.

**Impact.** `LANDER_MODE` defaults to `primary` (`unattended.sh:528`). A default adopter doing kit
work follows the notice, and gates-green records MET over a bar that skipped the self-tests of every
kit the branch did not move. Meanwhile the notice, the Skill and the protocol row all say the flagged
bar was paid. The touched kit's own guarded self-tests still run, which is why one skeptic rated
this low. This repo declares `in-place` and is not affected.

**Adjudication: MEDIUM.** It silently under-pays a Definition-of-Done clause on the kit's default
mode, and the shipped text claims the clause was paid (two answers to one question).

**Fix, and the fork it carries.** TOOL-dDerivedDocket-70 rules that the main loop exports
`GATE_SELFTESTS=1` and that the driver never sets it. That ruling names one flag. Two fixes keep the
ruling and make the text true, and the fold must record which one it takes:

- **(a) Recommended, and the confirmed findings' own fix.** Name `GATE_FULL=1 GATE_SELFTESTS=1` as
  the export in the notice, the Skill's Close paragraph and export line, the protocol row, and both
  conf comments. That spelling is redundant but harmless under `in-place`, so one spelling serves
  both modes. The driver still sets neither flag, and gate-guard already admits both prefixes from
  `VERIFYING`. This extends the ruled remedy by one flag, so record it as a decision that cites 70.
- **(b) Narrow the claim instead.** Under `primary`, the notice says the export buys a guard-scoped
  self-test run and names the pair as what the Definition of Done owes.

**Left-shift gate.** Exercise the remedy instead of reading it. Add a suite arm with a stub
`GATE_CMD` that writes its own environment to a file. Run the arm under both `primary` and
`in-place`. Take the export the `VERIFYING` notice printed, apply it to `--close` exactly as printed,
and assert that the stub saw both `GATE_FULL=1` and `GATE_SELFTESTS=1`. An arm that only greps the
notice text would pass on today's wording, because the wording is what is wrong.

### L1 — the owed-bar range read cannot see a rename out of a declared prefix

**Where:** `tools/unattended/unattended.sh:7117`, in `print_selftests_owed`. The function's header
claim that it breaks is at `:7097`.

**Defect.** `_touched=$(GIT diff --name-only "$_b" HEAD 2>/dev/null)` is a porcelain diff, and
porcelain diffs detect renames by default. `GIT()` at `tools/unattended/lib-unattended.sh:54` pins
neither `--no-renames` nor `core.quotePath`. A rename is therefore named by its destination only.
The synthesis reproduced this: after `git mv tools/k/a.sh memory/a.sh`, the default name-only diff
prints `memory/a.sh` alone, and `--no-renames` prints `tools/k/a.sh` too. A range whose only touch
on a declared prefix is moving a file OUT of it announces nothing, which falsifies the new line 7097
promise of "one flagged bar more than owed, never one fewer". Two weaker arms have no live
population:

- **A quoted path.** A non-ASCII path quoted under `core.quotePath` would miss the prefix match, but
  zero tracked paths under `tools/` carry one.
- **A failed diff.** One would read as an empty range, the fallback-fabricates-the-passing-value
  shape, but it is close to unreachable, because `rev-parse` has just verified the base.

**Reach is narrow.** A skeptic found no move out of `tools/` among 197 renames on `main`. A real
relocation also usually edits an in-kit reference, and that edit trips the prefix anyway.

**Fix.** Replace line 7117 with
`_touched=$(GIT -c core.quotepath=off diff --no-renames --name-only "$_b" HEAD 2>/dev/null) || { echo "unattended: the run's range ${_b:0:8}..HEAD could not be diffed, so whether the flagged bar is owed is unanswerable here, not no"; return 0; }`.

**Left-shift gate.** Add an arm to `unattended.test.sh` that commits a rename out of a declared
prefix and nothing else, then expects the notice. For the class, the predicate is "a porcelain
`diff --name-only` whose output is prefix-matched carries `--no-renames`". The synthesis ran it by
hand over the kit. The only other porcelain site that decides a touched set is `unattended.sh:1010`
(`resolve_hold_streak`), and it is a benign near-miss: it asks only whether anything besides two
named paths changed, and a rename still surfaces its destination. The `diff-tree` sites are
plumbing with rename detection off by default: `check-unattended.sh:3676` and `:3738`,
`lib-unattended.sh:673`, and `unattended.sh:9547`. A ban scoped this way has one hit today, the
defect itself.

### L2 — check 45's header still says the in-place close announces the owed bar

**Where:** `tools/unattended/check-unattended.sh:2942`, which is the header, plus the blank-key echo
at `:2949` and the fail-45 message at `:2960`.

**Defect.** The header describes `SELFTESTS_OWED_PATHS` as "the self-test surface the in-place
close derives its announcement from". After unit 6, only two places announce. One is the move into
`VERIFYING` (`unattended.sh:4227`) and the other is resume orientation (`:6190`), both under every
mode. The close announces nothing, as its own comment at `unattended.sh:7483-7486` says. Spec 6's
non-goal exempted check 45 because its fail MESSAGE "stays true". That reason covers the message,
not the header, and nobody weighed the header. This is two-answers-to-one-question and
amendment-leaves-its-other-half-standing, one file over from the premise check 47 was added to
catch. The blank-key echo's "no landing range" is loosely mode-agnostic, and the fail message is
incomplete rather than false, so those two parts are weak.

**Fix.** Reword the header to "the self-test surface the move into VERIFYING derives its notice
from, over the run's range from its pinned BASE, under every LANDER_MODE". Optionally, change "no
landing range" to "no run's range" at `:2949`, and "an in-place landing of kit work" to "a run of
kit work" at `:2960`.

**Correction to raw finding 10's fix.** That fix says the fail-45 arm needs no change, and that is
wrong. The arm at `tools/unattended/check-unattended.test.sh:4164` is a `hit` on the FULL message,
because `hit` is `grep -qF` of the whole string (line 78). The string includes "an in-place landing
of kit work", so editing the message strands the arm unless both change in the same commit
(arm-literal-strands-on-message-edit).

**Left-shift gate.** Check 47 already scans every shipped kit file for one retired premise, using a
regex at `check-unattended.sh:5482`. Generalise it into a short table of retired premises and add
this one: "in-place close" near "announce". The next copy of the old site then reds. Run the new
pattern over the tree first and print hits and near-misses. Where a regex would be too loose, add a
§10 checklist entry instead: a unit that moves WHERE something happens greps every comment that
names the old site, not only the messages its non-goals list.

## What the finding set does not contain

No confirmed finding touches units 1 to 5. None touches the security model's read-only property of
`--status` and `--plan`, and none touches the `GIT_GRAFT_FILE=/dev/null` export. This run's
integrity counters are all zero, so that absence is the four lenses' own result, not the shadow of a
lens that died. It is evidence at the depth those lenses went, not proof. The one refuted finding
is not described here because its text did not reach this synthesis.

## Fold order and round 2

1. **M1.** The driver line and the two arms, because a fix to M2's text is only testable once the
   Close sequence itself works.
2. **M2.** Record the fork, then change the text in its five carriers, then add the env-recording
   arm.
3. **L1**, then **L2**, the latter with its arm literal in the same commit.

A round 2 over the fold diff is owed. M1 and M2 change the driver and the Skill's binding Close
section, and fold text is unreviewed surface until something reviews it.

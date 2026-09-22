**Serves:** diff-review TOOL-dPolishedVitrine-1 TOOL-dPolishedVitrine-14

# dPolishedVitrine — Tier-2 diff review, round 3

*Node `d`, 2026-09-13. An adversarial pass over two units. The first is `TOOL-dPolishedVitrine-1`
after round 2's fold. That fold split the consumer migration in `WIRE-INTO-PROJECT.md` into three
blocks, derived the pins from `plan` and from each kit's regenerate exit, gave the review-harness
regenerate `--tracked-only`, gave selfcheck arm 7l its negative half, and made the govkit
selftest's `[-PV]` arms cut the three blocks out of the runbook and run them through a pre-commit
hook written from core's receipt rule. The second is the new unit `TOOL-dPolishedVitrine-14`, which
makes `brief-recorded` announce, and not grade, a unit built while its build's run-state record was
already terminal. The shape was four primed finder lenses, five skeptic batches prompted to REFUTE
each finding, and one synthesis. Round 2's confirmed set, R2-1 to R2-8, went to the lenses as prior
findings. The brief asked three things. Is each round-2 finding fixed? Does the runbook converge at
both real consumer shapes? And did the fold or the new unit regress anything, above all a
`brief-recorded` predicate that lets a unit built during a run escape, or a skip that reads as a
pass? Every `file:line` below was re-opened at the tip in this worktree before it was written down.
The consumer and fixture reproductions quoted are the skeptics' own. Where this synthesis ran or
read something itself, the text says so.*

**Range reviewed: `d36549fb...c9bc0b2a99e36f4f555bf1dd1c87c55b67aea13f`** (tip `c9bc0b2a`, branch
`cld/derived-harness-paths`, 24 files, +2470/-265). Round 3. The range runs from round 2's recorded
tip to HEAD. It holds the round-2 fold (`694d4d4e`, `a7ca1b5e`, `72ac1a96`) with its records commit
`f1e58789`, and then `TOOL-dPolishedVitrine-14` in `0690b3fc`, `8f22b419`, `e99df7d8` and `c9bc0b2a`.

## Verdict: BLOCKED

One BLOCKER. For the third round running, it is the consumer migration failing at inCMS core on a
commit-time gate that the `[-PV]` fixture does not carry. Round 2's R2-1 was core's pre-commit
receipt check. The fold modelled that check, and the runbook now passes it. This round's R3-1 is
core's `commit-msg` hook, which refuses every commit that lacks a `Co-Authored-By: Claude` trailer.
None of the runbook's three commits carries one, so block 1 can never land at core.

There are ten distinct defects in all: 1 blocker, 3 high, 4 medium and 2 low. Eight are in the
runbook's migration section and two are in `TOOL-dPolishedVitrine-14`. Of round 2's eight findings,
six are fixed on the fixtures their fixes name. R2-1 is fixed for its mechanism but not for its
class, and R2-4 is partly fixed. The runbook does not converge as written at either consumer. At
core, R3-1 refuses block 1's commit on every attempt. At both consumers, R3-2 stops block 3 after
its first commit has landed, and the recovery drops two receipt rows without a FLAG.
`TOOL-dPolishedVitrine-14` carries one HIGH: a wrong build-commit pick lets a unit built during a
live run skip grading (R3-4).

## Review shape

Raw 20 · confirmed 12 · refuted 8 · unverified 0 · precision 0.60.

The twelve confirmed findings include two co-reported duplicate pairs. Raw ids 6 and 16 are the
missing commit trailer. Raw ids 9 and 13 are the project-owned pin exclusion. Merging those leaves
**10 distinct defects**, R3-1 to R3-10 below, and each names the raw ids it absorbs. This synthesis
did the merge, so it is separate from the pipeline's own duplicate count in the integrity section.
The eight refuted findings did not reach synthesis, and nothing of them is carried here.

As in rounds 1 and 2, the severity counts are over distinct defects, so the blocker count compares
like with like across rounds. By raw id: 6 and 16 are BLOCKER; 1, 12 and 17 are HIGH; 3, 7, 8, 9
and 13 are MEDIUM; 10 and 19 are LOW. Four raw findings moved from the severity their lens gave
them:

- Raw ids 6 and 16 were filed HIGH. They are raised to BLOCKER, and R3-1 says why.
- Raw id 12 was filed MEDIUM. It is raised to HIGH, and R3-2 says why.
- Raw id 1 was filed MEDIUM. It is raised to HIGH, and R3-4 says why.

Five raw findings need a correction or a caveat, and the text below carries each one:

- Raw id 12 said step 6 drops the two rows silently. Its skeptic corrected this. Step 6 refuses on
  govkit's D6 guard after the step-5 commit has already landed, and the silent drop happens one
  recovery later.
- Raw id 17 said the parity leg's claim to red a stale render is false at core. It is, because
  core's gate manifest does not wire that leg: `grep -c protocol-parity` over core's
  `scripts/gate-legs.json` returns 0 here, and 1 over NicoCares'. Adding core's leg is a hand-off
  item that spec §3 already lists, so the sentence is false today rather than by design.
- Raw id 10 carries its skeptic's caveat. At this vintage NicoCares' harness edits look disjoint
  from gov's hunks, so NicoCares probably never reaches the path it describes.
- Raw ids 9 and 13 are latent at both consumers. Every project-owned row that records a commit is
  unedited today.

## Run integrity

- Lenses: **4/4 returned, 0 DIED.**
- Skeptic batches: **5/5 returned, 0 DIED.**
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and the
  pipeline removed 0 duplicates.
- 0 findings are left UNVERIFIED, so nothing in this report is outstanding for lack of a skeptic
  verdict.

The run is COMPLETE. No lens died, so the zero counts above are measurements rather than gaps, and
"found clean" below means the area was read.

## Round 2's findings, fixed or not

| Round 2 | Status at `c9bc0b2a` | What says so |
|---|---|---|
| R2-1 BLOCKER, step 1's commit wedged at core's pre-commit | **FIXED for its mechanism, NOT for its class.** Block 1 commits only what `update` staged, together with the receipt (`WIRE-INTO-PROJECT.md:1104-1105`). Block 3 stages the renders once their rows are `rendered` (`:1131-1135`). The `[-PV]` arms commit through a pre-commit written from `check_receipt.py`'s rule (`tools/govkit/selftest.py:8615-8645`). Round 2's class gate asked that the fixture carry the consumer's commit-time gate. It carries one of core's two, and the other refuses every commit (R3-1). | Read here. Core's `.git/incms-hooks` holds both `pre-commit` and `commit-msg`, also read here. |
| R2-2 MEDIUM, declined renders were pinned as current | **FIXED.** A render is pinned only when its kit's regenerate ran at exit 0 (`:1054-1055`). The bootstrapped fixture carries a kit that declines its regenerate (`:1220`). `ran_ok()` still reads block 1's log whenever block 2 or block 3 runs, and R3-3 and R3-5 both depend on that. | Read here. |
| R2-3 MEDIUM, the regenerate created a document nobody installed | **FIXED.** The argv carries `--tracked-only` (`tools/workflows/kit.toml:88`). Block 1's parity check runs under it (`WIRE-INTO-PROJECT.md:1099`). A file that step 1 created is flagged and never staged (`:1051-1052`). A tracked file that another kit's regenerate modifies or deletes is the uncovered half of the same class (R3-2). | Read here. The govkit-level report of created files is filed under `DEPL-dPolishedVitrine-2`. |
| R2-4 MEDIUM, the Done criterion could not be met | **PARTIAL.** Done is restated, and it warns against the bare re-adopt (`:1207-1215`). `pv-q` starts with unattributed rows. But block 2's count misses forked rows at core (R3-8), and the remedy the paragraph names, "run block 3 again", rewinds bases after a later update (R3-5). | Read here. |
| R2-5 LOW, the pin set came from the old receipt | **FIXED.** Rendered destinations come from `plan` (`:1032-1037`). The check flags every row new to the receipt (`:1073-1074`). That widened check added a STOP, which the pin rule's role exclusion can trip (R3-6). | Read here. |
| R2-6 LOW, a conflicted step 1 carried on | **FIXED.** Step 1 stops on update's exit code or on a conflict (`:1043-1046`). A rendered destination is never pinned to a recorded commit (`:1058`). The recovery text for a harness conflict names the wrong blob (R3-9). | Read here. |
| R2-7 LOW, three carriers called a flag-off update silent | **FIXED.** All three now say the row still prints `re-rendered` (`tools/workflows/check-protocol-parity.test.sh:26`, `tools/workflows/README.md:30`, spec `:260`), in `kit.toml:69-73`'s form. Arm 7l's negative half fails any sentence that calls a flag-off run silent without naming `re-rendered` (`tools/govkit/govkit.py:2025-2031`). | `govkit.py selfcheck` was run here and exited 0, reporting "11 sentence(s) naming `update` and a re-render, and 3 calling a flag-off run silent, across 2 kit(s)". |
| R2-8 LOW, the F3 fold left the refusal standing | **FIXED.** The spec's rev line lists every `refus` clause with its disposition (spec `:515-524`), and the README bullets now say that the parity script skips (`memory/builds/dPolishedVitrine/README.md:26`, `:36-38`). | Read here. |

## Does the runbook converge at the two consumers?

**inCMS core: no, not as written.**

- R3-1 refuses block 1's commit on every attempt.
- If R3-1 is fixed by hand, R3-2 stops block 3 at step 6 after its first commit.
- If core takes its routine flag-off pull of the 1.8 vintage before migrating, R3-3 makes block 1
  unreachable.
- On a Windows node without Python UTF-8 mode, R3-7 crashes every block.
- R3-8 makes block 2's count, and so the Done claim, off by two forked rows.
- R3-6 is latent over core's 6 project-owned rows that record a commit.

These parts of core's shape were read here: the receipt is schema 3 at prefix `scripts`, with 56
rows carrying `"evidence": "unattributed"`; `OWNED_BY_TARGET` and the `--diff-filter=ACMR` staged
compare in `scripts/check_receipt.py:38` and `:96`; and the hooks path set. No confirmed finding
touches memory-tree flat or the divergence map, and this synthesis did not trace the migration
through either.

**NicoCares: no, not as written, for a smaller reason.**

- It has no receipt hook and no `commit-msg` rule. Its hooks path holds `post-checkout`, `pre-commit`
  and `pre-push`, and none of them names the trailer (read here). So R3-1 does not reach it.
- R3-2 stops block 3 at step 6 there as it does at core, because NicoCares tracks both spellings of
  the two fixture records (read here).
- The blocks call `update`, `plan` and `adopt` and never `apply`, which NicoCares forbids.
- NicoCares' harness carries nc carve-out 13/25, a cap of 4
  (`vendor/nicocares-package/scripts/workflows/unattended-build.js:123`, `:375`). Step 1's render
  overwrites it with the template's cap of 5 (`tools/workflows/unattended-build.template.js:123`),
  and the runbook's local-edit paragraph (`WIRE-INTO-PROJECT.md:1200-1205`) is the documented way
  back. Both were read here. Between block 1 and that carry, NicoCares' tree holds a cap-5 harness.
  No confirmed finding covers that window, and this synthesis did not trace it through NicoCares'
  `agent-cap.js` or its carve-out census.

## Findings

| # | Sev | Where | One line | Raw ids | Origin |
|---|---|---|---|---|---|
| R3-1 | **BLOCKER** | `WIRE-INTO-PROJECT.md:1105` | no runbook commit carries the attribution trailer, and core's `commit-msg` refuses all three | 6, 16 | pre-existing, hidden in round 2 by R2-1 |
| R3-2 | HIGH | `WIRE-INTO-PROJECT.md:1106` | the render list is every unstaged change, and at both consumers it holds two deletions; block 3 stops after its commit | 12 | round-2 fold |
| R3-3 | HIGH | `WIRE-INTO-PROJECT.md:1047` | no way in for an install that a flag-off update already moved to the vintage | 17 | round-2 fold |
| R3-4 | HIGH | `tools/unattended/check-brief-recorded.sh:344` | TERM 0 reads the phase at a wrongly picked build commit, so a unit built during a live run skips grading | 1 | `TOOL-dPolishedVitrine-14` |
| R3-5 | MEDIUM | `WIRE-INTO-PROJECT.md:1129` | block 3 replays the pins made at migration time, and Done tells the operator to replay them | 3 | round-2 fold |
| R3-6 | MEDIUM | `WIRE-INTO-PROJECT.md:1059` | the pins leave project-owned rows out and the check stops on them, so an edited one wedges block 2 | 9, 13 | round-2 fold |
| R3-7 | MEDIUM | `WIRE-INTO-PROJECT.md:1020` | the helper decodes govkit's output as UTF-8, which govkit does not write on Windows | 7 | round-2 fold |
| R3-8 | MEDIUM | `WIRE-INTO-PROJECT.md:1072` | the count misses forked rows that `adopt` cannot attribute | 8 | round-2 fold |
| R3-9 | LOW | `WIRE-INTO-PROJECT.md:1156` | the conflict recovery says "the blob its receipt row records", which is `oid`, the edited bytes | 10 | round-2 fold |
| R3-10 | LOW | `tools/unattended/.unattended.conf.example:249` | the conf example drops the condition that HEAD must still carry the claim | 19 | `TOOL-dPolishedVitrine-14` |

---

### R3-1 — BLOCKER · `WIRE-INTO-PROJECT.md:1105` · no commit the runbook makes can land at core

The mechanism, step by step:

- Core's `core.hooksPath` is `.git/incms-hooks`, which holds `commit-msg` beside `pre-commit`, as
  read here. The hook is tracked at core's `.githooks/commit-msg`. It exits 1 unless some line of
  the message begins `Co-Authored-By: Claude`, case-insensitive. It exempts only an in-progress
  merge, revert or cherry-pick, and it deliberately treats a human commit the same as an agent one.
  This was also read here.
- The runbook commits three times with a bare `-m`: in block 1 at `:1105`, and in block 3 at
  `:1135` and `:1142`. None of the three carries the trailer.
- So at core, block 1 prints `STOP: that commit was refused.` after `update --write` has already
  written. The recovery the runbook gives (`:1153-1154`) is to return the tree to HEAD and run
  block 1 again, which reaches the same refusal.
- Block 1's subshell exits before its last line, so `harness-migration-renders.z` is never written.
  An operator who commits by hand with the trailer and carries on reaches block 3 without a render
  list. Block 3 then commits the receipt alone and leaves the renders unstaged.
- The hook names `git commit --no-verify` as the bypass for a human who wants no attribution. That
  bypass also skips core's pre-commit receipt check, the gate round 2's fold rebuilt the whole
  migration to pass. The runbook names neither way through.
- Gov's own charter requires the trailer on every agent commit (`AGENTS.md:185`, read here), and at
  core the operator is normally an agent. Pasted verbatim, the runbook breaks gov's own rule.

The fixture cannot see this. `write_pv_hook` (`tools/govkit/selftest.py:8637-8645`) writes a
`pre-commit` and nothing else, and `run_pv_commit` (`:8647-8652`) commits with a bare `-m`. The
`[-PV]` precondition calls the bootstrapped fixture "core's shape", and the runbook says "the text
you copy is the text that was tested" (`WIRE-INTO-PROJECT.md:1217-1218`). Both statements hold for
core's pre-commit only.

**Why BLOCKER, when both lenses filed it HIGH.** Round 2 raised R2-1 on this ground, and the ground
has not changed. Round 1 made the hand-off to core wait on a sequence that converges. The sequence
handed still does not converge at core as written, and it offers no documented way through. It is
also the class R2-1's left-shift gate named, a fixture that passes because it lacks a gate the
consumer has, and the fold closed that class for only one of core's two commit-time hooks. Two
things keep it from being worse: it fails loudly, and nothing wrong is committed. Update's writes
wait uncommitted in the tree.

**Fix.** Add a fourth operator variable, `TRAILER`, set beside `GOV`, `KIT` and `PY`. Commit at all
three sites as `git commit -q -m "<subject>" ${TRAILER:+-m "$TRAILER"}`, which puts the trailer in
its own paragraph and needs no `--trailer` support (that flag needs git 2.32 or later). Say in the
prose that a target with a commit-msg rule must set it, and name core. Mirror the change in spec §4
Rollout.

**Left-shift gate.** Add a `commit-msg` to `write_pv_hook` that copies core's rule. Run the three
blocks through it twice: once without `TRAILER`, where block 1 must STOP, and once with it, where
the migration must converge. For the class, stop adding one hook per round. Add a `[-PV]`
PRECONDITION that lists every hook core installs that fires on a plain `git commit`. Read here, core
installs `commit-msg`, `post-checkout`, `post-merge`, `pre-commit`, `pre-merge-commit` and
`pre-push`, and of those `pre-commit` and `commit-msg` fire on a plain commit. The PRECONDITION
asserts that each is modelled, or is named out of scope with a reason.

### R3-2 — HIGH · `WIRE-INTO-PROJECT.md:1106` · the render list is every unstaged change, and at both consumers it holds two deletions

The mechanism, step by step:

- `git diff --name-only -z` at `:1106` records every tracked change left unstaged after block 1's
  commit, not just the renders. Block 3 stages the whole list (`:1133-1134`).
- Block 1 runs with `GOVKIT_RERENDER=1`, and both consumers are behind the new vintage in
  `tools/unattended` (17 and 18 changed files, per the skeptic). So the unattended kit's
  `[[regenerate]]` runs as well: `bash {kit}/adopt-unattended.sh` (`tools/unattended/kit.toml:106-107`).
  Its fixture-record repath (`tools/unattended/adopt-unattended.sh:434-457`, read here) `mv`s each
  `tools~unattended~fixture-pieces~<n>~piece.md.md` onto its `scripts~` name.
- Both consumers track both spellings of both records (`git ls-files` at core and at NicoCares, run
  here). The skeptic checked that the twins are byte-identical after the body rewrite. The `tools~`
  files are `engine` rows in both receipts. Their removals exist only in the worktree, so `:1106`
  records them, and block 3's `git add --pathspec-from-file` stages a deletion for each. The skeptic
  reproduced this in a scratch repo.
- Core's pre-commit compares only `--diff-filter=ACMR` staged paths (core `scripts/check_receipt.py:96`,
  read here), and NicoCares has no receipt arm. So the step-5 commit lands at both consumers, under
  the subject "the build harness is rendered".
- Step 6's re-adopt then runs with the same pins. Those pins still name the two `tools~`
  destinations, because block 2 derived them from an index that still held both files. The files
  are no longer tracked, so govkit's D6 guard (`tools/govkit/govkit.py:8154-8165`, read here)
  refuses: `STOP: adopt refused.`, after the deletion commit has landed. Re-running block 3 refuses
  again, this time at step 5, for the same reason.
- The way out is to re-run block 2, which the runbook allows "as often as a STOP needs" (`:1166`).
  That rebuilds the pins without the two paths. The check skips `not-installed` rows (`:1070-1071`)
  and never walks the old receipt. The next block 3 then drops both rows with no FLAG.

So the Done line at `:1207-1208`, "every row block 2 did not flag keeps the attribution it had", is
false at both consumers, and the next `update` re-lands both files as unclaimed sources. Step 1's
FLAG (`:1051-1052`) covers only files a regenerate CREATED, which was R2-3's case. A tracked file
that a regenerate MODIFIES or DELETES outside the rendered set is the other half of that class, and
nothing flags it.

**Why HIGH, when the lens filed it MEDIUM.** The lens took the end state to be a silent drop at step
6. The skeptic corrected the mechanism: step 6 refuses after a commit, and the silent drop comes one
recovery later. That makes this the one defect in this round that stops the migration as written at
BOTH named consumers, unconditionally, and convergence at both is the question this round was asked.
It is not a BLOCKER, for two reasons. The runbook's own advice to re-run block 2 does lead to
convergence. And the two files it drops are duplicates that the unattended adopter removes on
purpose.

**Fix.** Record only the renders. Write the list as `git diff --name-only -z --diff-filter=M`
intersected with the destinations that `plan` at this vintage resolves as `rendered`. Block 1 can
run `plan` itself, or block 2, which already holds the plan, can do the intersection. Any other
dirty tracked path, deletions included, either STOPs by name, or is restored with `git checkout --`
and FLAGged. In check mode, also FLAG every old-receipt row that `adopt` no longer measures as
installed. Mirror the change in spec §4 Rollout step 2, which says "The regenerate's changes to
tracked files are recorded by name".

**Left-shift gate.** Give the `[-PV]` fixture a second kit whose `[[regenerate]]` deletes one
tracked `engine` file and edits another. Give the fixture hook core's `--diff-filter=ACMR`. Today
the fixture hook counts a staged deletion as a mismatch (`tools/govkit/selftest.py:8630`,
`'(deleted)'`), so it refuses a commit that core accepts, and the arm would stop at a different
place from core. Assert that block 1 or block 2 STOPs naming both paths, and that no receipt row
disappears without a FLAG.

### R3-3 — HIGH · `WIRE-INTO-PROJECT.md:1047` · no way in for an install that a flag-off update already moved

The mechanism, step by step:

- Block 1 STOPs unless update's output holds a `ran review-harness: … -> exit 0` line (`:1024-1028`,
  `:1047`).
- govkit runs a `[[regenerate]]` only for `touched_kits` (`tools/govkit/govkit.py:6680-6681` and
  `:7336`, read here). Those are the kits with a row acted on in this run, or with an unclaimed
  landing.
- A consumer whose receipt already sits at the introducing vintage has neither. It got there by a
  flag-off `update --write`, which is core's own documented pull procedure. Core's `CLAUDE.md` says
  to run `update --target <repo>` read-only first and then with `--write`, and never mentions the
  flag. That run lands the template, writes gov's `tools/`-spelled render into the still-`engine`
  row, stamps the row at the new vintage, and prints `re-rendered`.
- Block 1's `GOVKIT_RERENDER=1 update --write` then finds nothing in review-harness to act on and
  runs no regenerate. It STOPs with "the review-harness regenerate did not run at exit 0". Returning
  to HEAD and retrying changes nothing, and the runbook gives this install no way in.
- Meanwhile nothing at core reds the `tools/`-spelled harness. `tools/workflows/kit.toml:73`,
  `tools/workflows/README.md` and spec §4 Rollout `:261` all say the parity leg reds a stale render
  at the next bar. Core's gate manifest does not wire that leg (checked here), so the sentence holds
  only once that hand-off item lands.

`DEPL-dPolishedVitrine-2` already records the govkit root cause: a regenerate that did not run is
never retried. That row is OPEN and unbuilt, so until it lands the runbook has to cover this state
itself.

**Why HIGH.** It needs one particular order, a routine flag-off pull before the migration. But that
order is the consumer's documented default, and gov's 1.8 will reach core through exactly that pull
unless the hand-off gets there first. From that state the migration cannot be reached as written.
It is not a BLOCKER, because telling the consumer to migrate instead of pulling avoids it, and a
careful operator can find the escape of reverting the pull commit.

**Fix.** When `update` acted on no review-harness row, have block 1 run the kit's declared
regenerate argv itself, `bash "$KIT/check-protocol-parity.test.sh" --render --tracked-only`, and
let `ran_ok()` accept that exit code in place of update's `ran` line. Say at the top of the section
that, for the vintage that introduces review-harness 1.8, this migration replaces the routine pull.
Qualify the parity-leg sentence in `kit.toml`, the README and spec §4 with "where that leg is wired".

**Left-shift gate.** A `[-PV]` arm that first runs a flag-off `update --write` on the bootstrapped
fixture and commits it through the hooks, then runs the three blocks, and asserts that the harness
ends `rendered` and `pinned`.

### R3-4 — HIGH · `tools/unattended/check-brief-recorded.sh:344` · a wrongly picked build commit lets a unit built during a live run skip grading

The mechanism, step by step:

- The leg takes each unit's build commit from the library's `build_commit` (`:332`, and
  `tools/unattended/lib-unattended.sh:207-282`, read here). That function returns the EARLIEST
  in-range commit whose subject names the id as a whole token and that touches a path outside the
  build folder and outside the conf's `GENERATED_INDEXES` and `SHARED_RECORDS`.
- TERM 0 (`:340-379`) reads the run-state phase at that commit (`:338`, `:344`). If the phase is
  terminal and a record at HEAD still makes the same claim, the unit is NOT GRADED.
- Suppose a commit made between runs names the id and comes before the real build. `build_commit`
  picks it. At that commit RUN.md still reads the previous run's terminal phase. The next run's
  preflight then retires that record to `RUN.<phase>.<8hex>.md`, after the picked commit. So the
  retired-record half of the corroboration (`:358-368`) finds, at HEAD, a record making the same
  claim that did not exist at the picked commit, and it honours the skip.
- The range is `merge-base(anchor, HEAD)` (`tools/unattended/unattended.sh:891`, read here), so a
  commit made between runs that was not yet pushed falls inside it.

The skeptic reproduced it in a scratch fixture:

1. Run 1 lands.
2. A hand commit `docs: ARCH-tBrief-1 approach notes` touches `docs/notes.md`.
3. Run 2's preflight retires run 1 and pins run 2's base before the hand commit.
4. Run 2 builds `ARCH-tBrief-1` in the commit `ARCH-tBrief-1: build the thing`, with no brief row.

At `c9bc0b2a` the leg exits 0 and prints `NOT GRADED — ARCH-tBrief-1 was BUILT at <hand commit>
while RUN.md read LANDED`. At `d36549fb` the same history exits 1 with `NO brief row`.

How far it reaches: NicoCares' `.unattended.conf` declares neither `SHARED_RECORDS` nor
`GENERATED_INDEXES` (read here). So at NicoCares, any records or spec commit that names the id and
touches `memory/LIVE.md`, the ledger or `core-asks.md` qualifies. Gov's conf declares both
(`.unattended.conf:206-207`, read here), which narrows it to commits that touch something else.
`pass-order` stays green whenever the spec predates the wrongly picked commit, so no other leg
notices.

**Why HIGH, when the lens filed it MEDIUM.** It contradicts the unit's own goal. Spec -14 §1 says
the unit "grades every unit built during a run exactly as before", and the owner's ruling is "check
only units built DURING a run". Here a unit built during a live run is not graded. A history that
used to fail closed now fails open, and it does so on the unattended landing bar, where by
construction no owner reads the NOT GRADED line. This is the escape the brief asked the lenses to
hunt. It is not a BLOCKER for two reasons. The history needs a commit made between runs that names
the id. And the skip is announced by id together with the commit it trusted, so a reader who looks
sees a commit that is not a build. The root cause, `build_commit` picking the earliest qualifying
commit, is shared with `pass-order` and older than this unit. What -14 changed is that a wrong pick
now decides a skip instead of a grade. This is not `TOOL-dPolishedVitrine-15`. That row files a
forged claim that stands at HEAD, and nothing here is forged.

**Fix.** Before honouring the skip, walk `build_c..HEAD` for the commits that `build_commit`'s own
predicate also accepts for this id: the subject names the id as a whole token, and the commit
touches a path outside the exclusions. If RUN.md carries a non-terminal phase at any of them, the
unit was worked on during a live run. Grade it at that commit and print why. Record the rule in
spec -14 §4, under the predicate and its boundary, and in the leg's header, which today states the
predicate only for a correct pick. `lib-unattended.sh` stays untouched, which keeps -14's non-goal.

**Left-shift gate.** A `misselect` fixture arm beside `rotated`
(`tools/unattended/check-brief-recorded.test.sh:452`), with this history: run 1 LANDED, an id-naming
hand commit that touches a non-excluded path, run 2's preflight retirement, and the build with no
brief row. Assert exit 1 and `NO brief row`. Observe the arm red against the leg at `c9bc0b2a`
before the fix lands.

### R3-5 — MEDIUM · `WIRE-INTO-PROJECT.md:1129` · block 3 replays the pins made at migration time, and Done tells the operator to replay them

The mechanism, step by step:

- Block 3's only precondition is the `harness-migration-ready` marker (`:1129`). Blocks 1 and 2
  clear it when they start (`:1014`, `:1111`). Block 3 never clears it, and it replays
  `harness-migration-pins.txt` exactly as written at migration time.
- The Done paragraph answers update's "NOT re-stamped" message with "Run block 3 again, which carries
  the pins" (`:1210-1212`). govkit prints that message on every update while any row is
  unattributed. Core's receipt holds 56 unattributed rows today (counted here), and round 2 found 48
  of them survive the pin rule. So at core the advice applies to every later update.
- `adopt --pin` sets `commit` and `gov_oid` to the pinned revision and marks the row `pinned`,
  without comparing that revision with the row's current commit (`tools/govkit/govkit.py:8114-8133`,
  read here).

Suppose a later update moves an edited engine row to a newer vintage. Re-running block 3 then
records that row's pre-migration base again, and pins the renders back to the migration vintage.
The receipt now asserts false bases, and the next three-way merge runs against a base older than
the file's gov content. The result is a spurious conflict, or a wrong merge that nobody sees.
Re-running block 2 first does not help, because `ran_ok()` still reads block 1's update log.

**Why MEDIUM.** Where the Done paragraph puts the advice, on the next update at the same vintage, it
is harmless. The harm needs a later update that moves an edited row, and an operator who reads "the
next update" as any later update. When it does happen it is silent, which is why it is the first
MEDIUM to fold.

**Fix.** Have block 2 write GOV's HEAD and the receipt's hash beside the pins. Have block 3 STOP
unless both still match, and on success remove `harness-migration-ready` and the pins file. Limit
Done's "run block 3 again" to the same vintage, inside the migration, and name `--allow-ungraded`
for any later update. Mirror the change in spec §4 Rollout `:253-257`.

**Left-shift gate.** A `[-PV]` arm that migrates at vintage B, moves gov to C with a change to an
edited engine row, runs `update --write`, and then runs block 3. Today that records the row's commit
at B. After the fix, block 3 must STOP and the row must keep C.

### R3-6 — MEDIUM · `WIRE-INTO-PROJECT.md:1059` · the pins leave project-owned rows out, and the check stops on them

The mechanism, step by step:

- Pins mode excludes `project-owned` and `generated` rows even when they record a `commit`
  (`:1058-1059`). Its stated reason, at `:1188-1189`, is that gov supplies no bytes for these rows
  and `adopt` re-synthesizes them. That is true only of `merged` and `attributes` rows, which are
  the ones adopt's S11 block builds (`tools/govkit/govkit.py:8167` onward, read here).
- `adopt` measures a project-owned row with the same attribution walk it uses for an engine row, and
  its `--pin` branch never looks at role (`:8114-8133`, read here). Round 2's `[-PV] R2-5` arm
  already shows an edited project-owned file coming back `unattributed`.
- Check mode STOPs on any row that recorded a base and comes back unattributed without one of its
  four reasons (`WIRE-INTO-PROJECT.md:1084-1090`). An edited project-owned row that recorded a
  commit ends there, with `STOP: the receipt recorded a base for X…`. Block 2 derives the same pins
  on every run, so re-running it changes nothing, and the runbook names no remedy.
- Project-owned is the role a consumer is meant to edit. Core's receipt-sync and its pre-commit both
  skip it, so nothing prompts a re-adopt after an edit. Core carries 6 such rows with a commit and
  NicoCares carries 1. All 7 are unedited today (per the skeptic, the index blob equals `gov_oid`),
  so neither consumer hits this yet.

The two modes of one program use two different role lists. That is the
`two-answers-to-one-question` class inside a single heredoc. Raw ids 9 and 13 reported it
separately.

**Why MEDIUM.** It is latent at both consumers today, and it fails loudly. It is not LOW, because
the edit that triggers it is ordinary use of the role, and nothing gets past the STOP.

**Fix.** Take `project-owned` out of the excluded tuple, so that a project-owned row that records a
commit is pinned to it, as `seed` and `forked` rows already are. Do the same for `generated` if its
rows carry a source that gov holds at their commit. Otherwise, have check mode FLAG rather than STOP
for any role the pin rule leaves out. Either way, keep one role list and have both modes read it.
Correct `:1188-1189`.

**Left-shift gate.** Give `pv-q` an edited project-owned file whose receipt row records a commit,
and assert that block 2 passes with that row `pinned`. The project-owned file `_pvS` in the fixture
today has no receipt row (`tools/govkit/selftest.py:8606-8609`). It exercises the new-to-the-receipt
branch, not this one.

### R3-7 — MEDIUM · `WIRE-INTO-PROJECT.md:1020` · the helper decodes govkit's output as UTF-8, which govkit does not write on Windows

The mechanism, step by step:

- `read()` (`:1019-1021`) opens each saved govkit output with `encoding="utf-8"`. govkit never
  reconfigures stdout: `tools/govkit/govkit.py` contains no `reconfigure`, `PYTHONUTF8` or
  `PYTHONIOENCODING`, grepped here. Every update line it prints carries `—`.
- On Windows outside Python UTF-8 mode, redirected stdout uses the ANSI code page. Measured here
  with `PYTHONUTF8=0` and `PYTHONIOENCODING` unset, that is `cp1251`. The skeptic reproduced the em
  dash being written as byte 0x97, and `read()` raising `UnicodeDecodeError` on it.
- So `step1`, `pins` and `check` each crash on their first `read()`. Block 1 dies after
  `update --write` has written, and every retry dies the same way.
- The `[-PV]` arms pass because `run_pv_block` inherits `os.environ`
  (`tools/govkit/selftest.py:8668-8672`), and this node exports `PYTHONUTF8=1` and
  `PYTHONIOENCODING=utf-8` (read here). Core's `help/maintenance.md:84` says of that setting that
  "Nothing sets this for you" on a fresh Windows machine (read here). `ABL-aTidalGrommet-32` records
  this masking class as open, per the skeptic.

**Why MEDIUM.** It depends on the node, and it fails loudly. But any fresh Windows node reaches it,
and the fixture cannot see it on the node where the fixture runs.

**Fix.** Run every govkit call in the blocks as `"$PY" -X utf8 …`, or `export PYTHONUTF8=1` at the
top of each subshell, which also covers the helper. Opening with `errors="replace"` works too,
because the regexes need only ASCII. In `run_pv_block`, remove `PYTHONUTF8` and `PYTHONIOENCODING`
from the environment, so the arm pins the fix.

**Left-shift gate.** The environment strip in `run_pv_block` is the gate. For the class, on Windows,
where it can fail, add a govkit selftest arm that runs the `[-PV]` blocks with `PYTHONUTF8=0` and
`PYTHONIOENCODING` unset, so a node's own settings cannot hide an encoding dependency again.

### R3-8 — MEDIUM · `WIRE-INTO-PROJECT.md:1072` · the count misses forked rows that `adopt` cannot attribute

The mechanism, step by step:

- `adopt` prints a row's key as `forked` whenever the role is `forked`, whatever its attribution
  found, and still writes `evidence: "unattributed"` when the walk misses
  (`tools/govkit/govkit.py:8147-8151`, read here). It prints the ` <- <sha>` suffix only when the
  row has a commit.
- Check mode skips every line whose key is not `unattributed` (`WIRE-INTO-PROJECT.md:1072-1075`).
  Its regex does not capture the suffix (`:1067`), so it cannot tell a forked row that has a base
  from one that does not.
- `update` withholds its stamp over every row whose evidence is `"unattributed"`, whatever its role.
- At core, `scripts/recall/extract.py` and `scripts/recall/query.py` are forked and unattributed.
  The skeptic ran a read-only `adopt --re-adopt` against core at `c9bc0b2a`, which left core's tree
  unchanged. It printed both files as `forked` with no `<- sha`, and its tally was
  `forked 2 … unattributed 55`.

So block 2's last line undercounts by those two rows at core, and the Done claim that the next
update withholds its stamp "over exactly the rows block 2's last line counted" is false there.

**Why MEDIUM.** No bytes move. But this is the Done check R2-4 asked for, and it is false at the
consumer it was written for. An operator whose count does not match is one step away from the bare
re-adopt the runbook warns against.

**Fix.** In check mode, count a row as unattributed when its key is `unattributed`, or when its key
is `forked` and the line has no ` <- <sha>` suffix. That means capturing the suffix in the regex. A
better fix has `adopt` print its evidence separately from the rung-or-fork key, and the check parse
that. That is a govkit change, and it belongs with `DEPL-dPolishedVitrine-1`.

**Left-shift gate.** Add a forked, commit-less row to `pv-q`, and assert that block 2's count equals
the number of rows the next `update` names when it withholds its stamp.

### R3-9 — LOW · `WIRE-INTO-PROJECT.md:1156` · the conflict recovery names the wrong blob

`:1155-1156` says to restore a conflicted harness "to the blob its receipt row records". A receipt
row records two blobs. In govkit's own vocabulary, `oid` is the target's blob and `gov_oid` is
gov's (`tools/govkit/govkit.py:3859`, per the skeptic), and `adopt` writes `oid` from the target's
index. So in an adopt-measured receipt, `oid` is the edited bytes. NicoCares' harness row has `oid
6aa46ddb` against `gov_oid 75763c4e`. The skeptic's diff shows that `6aa46ddb` carries nc carve-out
13/25, the cap of 4, and the `scripts/` driver relocation. Restoring to `oid` recreates the
conflict, and the operator goes round block 1 again.

**Why LOW.** The skeptic judged gov's harness hunks at this vintage (lines 3, 76 and 228) disjoint
from NicoCares' edits (lines 123, 225 and 375), so NicoCares probably merges cleanly and never
reaches this path. The fix is one word.

**Fix.** Name the field and the command. Restore the harness to `gov_oid`, gov's blob at the row's
`commit`, with `git -C "$GOV" show <commit>:<source>`, and commit that before running block 1 again.

**Left-shift gate.** The `pv-tx` conflict arm's receipt came from `apply`, where `oid` equals gov's
bytes, and that is why it cannot see this. Add an adopt-bootstrapped twin of `pv-tx`, and run the
recovery as written through to a clean block 1.

### R3-10 — LOW · `tools/unattended/.unattended.conf.example:249` · the conf example drops the condition that HEAD must still carry the claim

The example says that a unit whose build commit carries a terminal record "owed no brief: the leg
announces it by id and does not grade it" (`:249-251`), with no condition attached. The leg's header
(`tools/unattended/check-brief-recorded.sh:46-52`) and the protocol row
(`tools/unattended/PROTOCOL.template.md:471`, and `memory/guides/UNATTENDED-PROTOCOL.md:471`) both
skip such a unit only while HEAD still carries that record's base, phase and witness. Otherwise the
leg prints GRADED ANYWAY and grades it (`:376-379`). All three were read here. One fact has three
carriers, and one of them dropped the condition: the `two-answers-to-one-question` class. An adopter
who sets `BRIEF_RECORDED_CUTOFF` from the example expects an unconditional exemption, and then sees
the leg red once a later edit or rotation leaves HEAD without the claim.

**Fix.** Add the clause, or replace the sentence with a pointer to the PROTOCOL row so that the fact
has one carrier.

**Left-shift gate.** None new. Retiring the second copy is the gate. Record it as a live instance of
the catalogued class.

---

## One fold for the runbook

R3-1, R3-2, R3-3 and R3-5 to R3-9 all touch `WIRE-INTO-PROJECT.md:999-1221` and their mirrors in
spec §4 Rollout. Their fixes interact, so here they are as one set of edits. This is a sketch.
Verify it through core's full commit-time hook set, on the bootstrapped fixture, before any consumer
is handed it.

1. **Operator variables.** Add `TRAILER` (R3-1). Run every govkit call as `"$PY" -X utf8`, or export
   `PYTHONUTF8=1` in each subshell (R3-7).
2. **Block 1.** When `update` touched no review-harness row, run the kit's declared regenerate argv
   and accept its exit (R3-3). Record only modified renders. Any other dirty tracked path, deletions
   included, STOPs by name or is restored and FLAGged (R3-2). Commit with the trailer (R3-1).
3. **Block 2.** Write GOV's HEAD and the receipt hash beside the pins (R3-5). Keep one role list for
   both modes, and pin project-owned rows that record a commit (R3-6). Count forked rows that have
   no base (R3-8). FLAG every old-receipt row that `adopt` no longer measures as installed (R3-2).
4. **Block 3.** STOP unless GOV's HEAD and the receipt hash still match block 2's. On success, clear
   the marker and the pins file (R3-5). Commit with the trailer (R3-1).
5. **Prose.** Limit Done's "run block 3 again" to the same vintage (R3-5). Correct the premise about
   project-owned rows (R3-6). Name `gov_oid` in the conflict recovery (R3-9). Say that this migration
   replaces the routine pull for the introducing vintage (R3-3). Qualify the parity-leg sentence in
   `tools/workflows/kit.toml:73`, `tools/workflows/README.md` and spec `:261` with "where that leg
   is wired" (R3-3).
6. **`[-PV]` arms.** Add a `commit-msg` hook and a hook-set PRECONDITION (R3-1). Give the fixture hook
   `--diff-filter=ACMR` and add a deleting regenerate (R3-2). Run a flag-off update before block 1
   (R3-3). Run a later-vintage update before block 3 (R3-5). Add an edited project-owned row with a
   commit (R3-6). Strip the UTF-8 variables from the environment (R3-7). Add a forked, commit-less
   row (R3-8). Add an adopt-bootstrapped conflict twin (R3-9).

For `TOOL-dPolishedVitrine-14`, apply the TERM 0 walk and the `misselect` arm (R3-4) and the conf
example clause (R3-10), each with its spec -14 §4 line.

## What was checked and found clean

These are measurements, not silence. All four lenses returned, so a zero here means the area was
read.

- **The -14 skip cannot read as a pass.** Every skipped unit prints its own NOT GRADED line, with
  the id, the commit, the phase and the record that still makes the claim
  (`tools/unattended/check-brief-recorded.sh:373`). A claim that HEAD does not bear out prints
  GRADED ANYWAY, and the unit is graded (`:376-379`). Both counts are printed on the liveness line
  even when they are zero. This synthesis ran the leg over this tree. It exited 0 and printed
  `graded 28 closed unit(s) … 0 unit(s) built after their run finished, not graded · 0 unit(s) built
  under a finished claim HEAD does not bear out, graded`. R3-4 is a skip that fires on the wrong
  population, and it is announced. It is not a silent one.
- **The -14 suite.** Run here, `bash tools/unattended/check-brief-recorded.test.sh` printed `88 arms,
  exit 0`, including the `reopened`, `copied` and `baseonly` arms that pin the corroboration and the
  claim parse.
- **`pass-order` untouched.** Checked here, `git diff d36549fb..c9bc0b2a` over
  `tools/unattended/check-pass-order.sh` and `tools/unattended/lib-unattended.sh` is empty. The
  unit's journal records the leg's stdout as byte-identical before and after on both bars. That was
  not re-run here.
- **The forged claim that stands at HEAD** is filed as `TOOL-dPolishedVitrine-15`, OPEN, with a
  candidate gate. It is not re-reported here.
- **Gov's own render.** Run here, `bash tools/workflows/check-protocol-parity.test.sh` printed
  `in parity — 2 rendered pair(s) match their templates for 'tools/workflows' (MEMORY_TREE_DIR
  'tools/memory-tree')` and exited 0.
- **Version carriers.** Run here, `bash tools/check-kit-versions.sh` exited 0.
- **Selfcheck arm 7l, both halves.** Run here, `python tools/govkit/govkit.py selfcheck` exited 0
  (R2-7 row above).
- **The fold's fixes to R2-2, R2-3 and R2-5 to R2-8** hold on their fixtures, read here and recorded
  in the table above. No lens reported a regression in govkit itself this round. The only govkit
  lines cited above belong to behaviour the runbook depends on.

## Disposition

Round 1 confirmed 1 blocker, round 2 confirmed 1, and round 3 confirms 1. Each of the three is the
consumer migration failing at core, and the last two are the same class: a fixture that passes
because it lacks a gate the consumer has.

`memory/guides/BUILD-METHOD.md` M8 says to fix every blocker and then re-review the FIX, and that a
blocker unfixable inside the mandate's scope is a park, not a waiver. R3-1 is fixable in scope. The
fix is a runbook variable, a spec mirror and a fixture hook. Under M4, the same file states a
convergence rule: a loop re-arms only when its confirmed-blocker count is STRICTLY SMALLER than the
round before, and a blocker still standing at the exit is disposed of by FOLD when it is a defect in
a document the review read. One, then one, then one is not smaller. If that rule governs this loop,
R3-1 is a FOLD into `WIRE-INTO-PROJECT.md`, spec §4 and `write_pv_hook`, and the fold is not
re-reviewed. Either way, the fold should model core's whole commit-time hook set at once, not one
hook per round, because that is the only thing that ends this class rather than its latest instance.

The HIGH and MEDIUM defects are folds to this build's own files: the runbook, both specs, the leg,
the conf example and the `[-PV]` and `brief-recorded` arms. Two govkit improvements are already
filed and stay there: the withheld-stamp message and a separate evidence field (R3-8) belong with
`DEPL-dPolishedVitrine-1`, and a regenerate that runs when nothing touched its kit (R3-3's root)
belongs with `DEPL-dPolishedVitrine-2`.

The hand-off to core waits on R3-1, R3-2, R3-3 and R3-8, and on R3-7 for any Windows node without
UTF-8 mode. The hand-off to NicoCares waits on R3-2. NicoCares' re-pull of unattended 1.20 should
wait on R3-4, because NicoCares' conf declares no `SHARED_RECORDS` or `GENERATED_INDEXES`, which
widens the set of commits `build_commit` can wrongly pick there. Declaring both would narrow that
set, but it does not remove it.

## Scope and limits of this review

- Findings are anchored to this worktree at `c9bc0b2a`. Every cited line was re-read at the tip.
- This synthesis ran the parity leg, `check-kit-versions.sh`, `govkit.py selfcheck`,
  `check-brief-recorded.test.sh`, and `check-brief-recorded.sh` over this tree, and measured
  redirected stdout's encoding under `PYTHONUTF8=0`.
- It also read the following. At core: the hooks path and `commit-msg`, the `check_receipt.py`
  filter and owned roles, `help/maintenance.md`, the unattributed count in `.governance/install.json`,
  and the absence of a parity leg from `scripts/gate-legs.json`. At NicoCares: the installed hooks,
  the `.unattended.conf` exclusions, the parity leg in `scripts/gate-legs.json`, and the harness's
  cap carve-out. At both: the tracked fixture-record twins. In govkit: `touched_kits`, the `--pin`
  branch, D6, and adopt's key print.
- The scratch reproductions behind R3-2, R3-4, R3-7 and R3-8 are the skeptics'. They were not
  re-run here, and that includes the read-only `adopt` against core, the two-run fixture, and the
  byte 0x97 decode. The counts of changed unattended files at each consumer (17 and 18) and of
  project-owned rows with a commit (6 and 1) are the skeptics' too.
- The full govkit selftest, including every `[-PV]` arm, was not re-run here. The build's journal
  records it on two full bars.
- **The binding line names two units, on purpose.** Only `TOOL-dPolishedVitrine-1` and
  `TOOL-dPolishedVitrine-14` have a spec H1 in this build. The other ids the diff mentions are
  decision or backlog rows (`TOOL-dPolishedVitrine-13`, `TOOL-dPolishedVitrine-15` and the three
  `DEPL-dPolishedVitrine` rows), or NicoCares' `PKG-dPolishedVitrine-14`, which appears in prose.
  Record ids resolve against spec H1s, so naming any of those would bind nothing.
- Not covered: NicoCares' cap-4 window between block 1 and the carry into the template; how the
  migration interacts with core's divergence map and its flat memory tree; and a fresh `apply` at
  the tip. The eight refuted findings were not passed to this synthesis, so this report cannot say
  which areas they covered.
- This is a diff review, not a gate run. The build's AC ledgers are the bar.

**Serves:** diff-review TOOL-aRoutedQuill-3

# Tier-2 closing diff review — aRoutedQuill, ROUND 2

*Round 2 of the closing review (BUILD-METHOD M8) of the unattended build aRoutedQuill. It reviews the
FIX of round 1's one blocker, not the build again. Round 1
([round 1](2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md)) found B1: the
routed-commits leg (`tools/memory-tree/routed_commits.py`) was red in WHOLE mode because three
cutoff-day commits from a reconcile merge were not in `ROUTED_COMMIT_WAIVED`. The fix is commit
5b4f964d5. The range also holds the reconcile merge 8f493d467 of origin/main e6585db4 (aMeteredSweep
and aSparedSpawn). That merge's incoming content is another build's and is out of scope. Its conflict
resolution and the commits it makes reachable to this branch's gates are in scope. Node `a`,
2026-10-10.*

Reviewed range: `ff0b3dc327514e020eb47009de931d4dfd78c608...5b4f964d50a85656029a7bd6a58f795f7717661a` · ROUND 2

## Verdict: BLOCKED

One blocker survived, confirmed independently by all three lenses (raw 3, one item). The fix waives
exactly the three commits B1 named, and those waivers are correct. But the round-2 reconcile merge
8f493d467 brought in three more cutoff-day mints that touch `ROUTED_PATHS` and name no unit. So
`env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` still exits 1 at head. The fix
commit's message says the leg "now exits 0 (graded 39, 8 waived)". That is false for the tree it
ships in, so the record certifies a green the gate does not give. B1 and TOOL-aRoutedQuill-3 AC10
remain open. The synthesizer re-ran the leg at head and saw the same red (graded 45, 8 waived, rc=1).

## Review shape

Intensity light, raw 3, confirmed 3, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

Adjudicated tally: by item, 1 blocker, 0 high, 0 medium, 0 low. By raw confirmed finding, 3 blocker,
0 high, 0 medium, 0 low. The three findings describe one defect at one line, so they merge into one
item at their shared binding grade.

### Run integrity

- Lenses: 3/3 returned, 0 died.
- Skeptic batches: 3/3 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 3 judged sound, 0 judged unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.

This is NOT a full review. Intensity was light: the security and intent lenses were not run, so their
classes were swept only through checklist shares. No recurring-bug-class checklist was swept (it is
absent), and a zero count there is not evidence those classes are absent. One spec document was
supplied as `specs`, beside the range's commit messages. By-design items came from the caller's
byDesign.

## What was verified and holds

- The three prefixes the fix added (3d05f1ead941, 4e49aeb53a88, d31d7bc96461) resolve uniquely to
  the commits B1 named.
- The leg script is unchanged in the range, so RANGE mode still reads no waiver. A RANGE run
  `e6585db4..HEAD` exits 0.
- The reconcile's `memory/guides/SESSION-KICKOFF.md` stamp resolution kept the newer
  `last-body-change` (9bb7233), an ancestor of HEAD. origin/main moved only stamps there, so neither
  side's change was lost.

## Findings

### B1-r2 [blocker] — the waiver is incomplete for the tree it ships in (ids 1, 2, 3)

**Where:** `.memory-tree.conf:20` (`ROUTED_COMMIT_WAIVED`).

**Defect:** the reconcile merge 8f493d467 made three more aMeteredSweep mints reachable. Each has a
2026-10-09 commit date, touches `tools/`, is not a merge and names no unit. None is an ancestor of
base ff0b3dc32. All three are reachable from 8f493d467^2 (origin/main e6585db4), so this diff's merge
is what brought them in.

- d6aae9d18478: mint unattended 1.94 (2026-10-09T23:58).
- 22efab659eaf: mint kickoff-manifest 1.23, memory-tree 2.138, unattended 1.92 (2026-10-09T18:57).
- 670436cd5f16: mint kickoff-manifest 1.22, memory-tree 2.137, unattended 1.91 (2026-10-09T06:13).

**Impact:** the full bar's "routed commits name a specced unit" leg, which runs with
`GATE_PUSH_BASE` unset, is red at head. Every bar run that way reds on it, including a worktree or
branch bar, CI and main's own run once this lands. The fix commit's recorded figure (graded 39,
8 waived) was evidently taken before the reconcile, which added 6 graded commits. The actual figure at
head is graded 45, 8 waived, exit 1.

**Fix (judged SOUND by the skeptic, all three findings):**

1. Add `d6aae9d18478 22efab659eaf 670436cd5f16` to `ROUTED_COMMIT_WAIVED`. Take each prefix from
   `git rev-parse --short=12`, never by hand.
2. Extend the comment to name the three aMeteredSweep mints that arrived with the 8f493d467
   reconcile of origin/main e6585db4. d6aae9d1 was committed on main's side after main already had
   the leg, so reword the comment's "before the leg existed" so it does not claim that of every entry.
3. Re-run `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` at the actual
   post-commit HEAD. Confirm exit 0 with graded 45 and 11 waived, and quote that real summary line in
   the commit message, correcting the fix commit's figure.
4. Re-stamp the kickoff manifest after that.
5. Re-run the leg after every further reconcile merge before stamping a fix, because each merge from
   main can bring in more cutoff-day commits.

**Left-shift gate suggestion:** the class is "a record claims a gate result the tree at that commit
does not give", made likely here by a reconcile landing between the measurement and the commit. Two
options, cheapest first:

- A documented check in BUILD-METHOD's fix-round step: any commit message quoting a leg's summary
  line is measured at that commit's own HEAD, after the last merge in the range.
- A gate: after any merge commit on a build branch, the merge driver or post-merge hook runs
  `routed_commits.py` with `GATE_PUSH_BASE` unset and reds on new unwaived cutoff-day commits, so the
  waiver list is extended in the same session that brought them in.

review-shape kind=diff-review round=2 intensity=light at=synth raw=3 confirmed=3 refuted=0 unverified=0 blocker=3 high=0 medium=0 low=0 agents=7 out-tokens=25418

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | .memory-tree.conf:20 | blocker | blocker | confirmed | I reproduced it at HEAD 5b4f964d5 with a clean tree. `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` prints 'graded 45 ... 8 waived', then FAILED, naming d6aae9d1 (mint: unattended 1.94), 22efab65 (mint: kickoff-manifest 1.23 ...) and 670436cd (mint: kickoff-manifest 1.22 ...). It exits 1. None of the three is an ancestor of base ff0b3dc32. All three are ancestors of e6585db4, so the in-range reconcile merge 8f493d467 brought them in, which puts them in scope. That merge is exactly the 'no further post-cutoff commit' condition the task asked me to verify, and it fails. The fix commit's message says 'now exits 0 (graded 39, 8 waived)', which is not true at head. The routed-commits leg is still red in WHOLE mode, so TOOL-aRoutedQuill-3 AC10 is still unmet. That is a shipped record certifying a green the gate does not give. This is not a duplicate of B1: B1 named three different shas, and these three arrived with a different merge (8f493d467, not 8dea35478). The three prefixes the fix added are correct. The diff confirms 3d05f1ead941, 4e49aeb53a88 and d31d7bc96461 are the shas B1 named. | sound | - |
| 2 | seams | .memory-tree.conf:20 | blocker | blocker | confirmed | I reproduced it at head 5b4f964d5 by running `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py`. It exits 1 with 'graded 45 · 8 waived', and three commits fail as 'no unit id — names no unit': d6aae9d1 (mint unattended 1.94, committed 2026-10-09T23:58), 22efab65 (mint kickoff-manifest 1.23 / memory-tree 2.138 / unattended 1.92) and 670436cd (mint 1.22/2.137/1.91, owed by aMeteredSweep). None of the three is an ancestor of base ff0b3dc3. All three are ancestors of the reconcile merge 8f493d467, so this diff's merge is what made them reachable, and the defect is in scope rather than pre-existing. The fix commit's message says the leg 'now exits 0 (graded 39, 8 waived)'. That is false at head, so the fix certifies a green it does not have. The WHOLE-mode leg of the full bar is still red, B1 / TOOL-aRoutedQuill-3 AC10 is not closed, and the record misstates the gate. The three new waivers (3d05f1ead941, 4e49aeb53a88, d31d7bc96461) are correct for what they cover. The defect is the three omissions. | sound | - |
| 3 | verification | .memory-tree.conf:20 | blocker | blocker | confirmed | I reproduced it at HEAD 5b4f964d5. `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` prints 'graded 45 · ... · 8 waived' and FAILS on d6aae9d1, 22efab65 and 670436cd, all with 'names no unit', and it exits 1. Each of the three commits has a 2026-10-09 commit date, which is on or after ROUTED_COMMIT_CUTOFF. None is an ancestor of base ff0b3dc32, and all three are reachable from 8f493d467^2 (origin/main e6585db4). That makes the violation reachable only because of this diff's reconcile merge, so it is in scope and not pre-existing. The fix commit's message says the leg 'now exits 0 (graded 39, 8 waived)', which is false for the tree it ships in. B1 / AC10 (WHOLE-mode green) is therefore still unmet, and the commit message certifies a green the tree does not have. This is a new defect in the fix: the waiver is incomplete because the round-2 reconcile happened after the count was taken. It is not a re-raise of the original B1 shas, which do resolve and are waived. | sound | - |

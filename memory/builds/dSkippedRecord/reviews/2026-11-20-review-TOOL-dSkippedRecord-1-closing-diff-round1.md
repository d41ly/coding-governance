**Serves:** diff-review TOOL-dSkippedRecord-1

# Closing diff review, round 1: dSkippedRecord's diff, unit 1

Node `d` · 2026-11-20 · Tier-2 · on `branch/magical-lumiere-ba3d2a` · adversarial fan through `tier2-review.js`: 5 finder lenses (`gov-diff-reviewer`), then 3 skeptic batches (`gov-skeptic`), then this synthesis (`gov-synthesizer`). The range changes `write_run_record` in `tools/unattended/unattended.sh` so that an in-place `--close` tests the index with `GIT diff --cached --quiet` before its run-record commit. git's 1 commits, git's 0 prints a skip line, and any exit above 1 prints a refusal line, and every path returns 0. It adds a mode argument (`same`, `moved`, `addfail`, `difffail`) to `run_render_helper` in `tools/unattended/unattended.test.sh`, and the failed-stage modes fail one git call through a PATH `git` shim (red fix 26f99cdb0). It drops the `unattended.sh` row from `memory/project/stage-commit-sites.txt`. The rest is build records and regenerated views.

**Reviewed range:** `81657e77cae61a447ca8a404711bb7f1856cd8e9...1b1077a750798acaf584bfdd5722d1e18d18a860`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker, and none is HIGH or MEDIUM.
Two LOW defects stand, and neither changes behaviour.
The AC1 arm reads only the skip line's prefix, so the commit hash the line ends with is never checked (id 2).
The closed rev-1 spec still describes the failed-stage arms as `GIT` function overrides, which red fix 26f99cdb0 replaced with a PATH `git` shim (id 3).

## Review shape

- Intensity full. Raw 3, confirmed 2, refuted 1, merged 0, unverified 0 (0 uncertain). Precision 0.67.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by item: 0 BLOCKER, 0 HIGH, 0 MEDIUM, 2 LOW, which is 2 items.
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 0 HIGH, 0 MEDIUM, 2 LOW (ids 2, 3), which is 2 findings.
- Every confirmed finding keeps its binding grade.
- Intent input: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 51 items, acquired by the harness from `--for-diff 81657e77cae61a447ca8a404711bb7f1856cd8e9..HEAD`, each assigned to exactly one of 5 lenses (security 11, correctness 10, seams 10, verification 10, intent 10).
- By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 3/3 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 2 judged sound (ids 2, 3), 0 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 with no fix proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 1 (id 1). Same-address pairs shown: 0.
- Id 1 is not a twin of any confirmed finding. It concerns `run_render_helper` discarding `write_run_record`'s exit status, which is a different defect from id 2's unchecked hash in the skip line.
- Dispositions: unclassed refuse; 51 class slugs handed; 199 leg names read from `tools/gate-legs.json`.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Every counter above is zero where it must be zero, so this run is complete within the generic brief, the 2 specs and the commit messages.
- The zero counts on the security, correctness and seams lenses mean those lenses found nothing within that brief. Coverage is limited to what those inputs let the lenses hunt.

## Items

### 1. LOW: the AC1 arm never checks the commit hash the skip line ends with (id 2 LOW)

- **Where:** `tools/unattended/unattended.test.sh@3d57b113:17237`, the AC1 arm (lines 17236-17239). The line it tests is `tools/unattended/unattended.sh@acd06237:16597`.
- **What is wrong:** the new skip line ends with `the record was last committed at $(GIT log -1 --format=%h -- "$rec" 2>/dev/null)`.
- The AC1 arm checks only the prefix `unattended: run record unchanged`, plus `HEAD: same` and the absence of `its commit failed`.
- Because of the `2>/dev/null`, a failed log call or a wrong `$rec` ends the line in a blank `at ` and prints no error, and the arm still passes.
- In `same` mode, `run_render_helper` writes `lu-record.md` before `fixture`, so the record is committed and a real hash exists to compare against.
- Spec S1 says the skip line is observed by AC1, and the spec's observability answer says the line names the commit that last changed the record, so this is an observed-by claim that the arm discharges only in part.
- **Consequence:** an operator could see a blank or wrong commit reference in the skip line, and no test would catch it.
- The effect is limited to the wording of an informational line. No exit code or commit depends on it.
- **Grades:** id 2 is LOW, its binding grade.
- **Fix (judged SOUND by the skeptic):** in the `same` arm, also assert `hit "$out" "last committed at $(git log -1 --format=%h -- memory/builds/tRun/build/lu-record.md)"`, computed in the fixture repo after the helper returns.
- Or print the expected hash from inside the helper next to its `HEAD:` line, and assert the skip line carries it.
- **Left-shift gate:** add a bug-class checklist entry under `observed-by-claim-no-arm-discharges`. An arm that asserts an echo line containing a `$( … )` substitution must also assert the substituted value, or state why it cannot.

### 2. LOW: the closed rev-1 spec still describes the failed-stage arms as `GIT` function overrides (id 3 LOW)

- **Where:** `memory/builds/dSkippedRecord/spec/2026-11-20-spec-TOOL-dSkippedRecord-1.md@28818893:181`, the §4 mode table rows for `addfail` and `difffail` and the paragraph after them (lines 181-186). The revision log is at §9, line 305.
- **What is wrong:** the spec, marked `CLOSED · rev-1`, says `addfail` and `difffail` fail their git call through two `GIT` function overrides that pass every other argv to `git -c pins`.
- Red fix 26f99cdb0 replaced those overrides with a `git` shim written into `$lu_g/lu-shim` and put first on PATH, in the `case "$lu_mode" in addfail|difffail)` block of `tools/unattended/unattended.test.sh` near line 17206.
- The shim matches `<mode> -c <pin> -c <pin> add -A *` and the exact `diff --cached --quiet`, and execs the real git for every other call.
- The revision log holds only `rev-1 · initial draft`. Commit e56a3e698 touched the spec only to add the red-fix record rows.
- Only the acceptance ledger and the red-fix records mention the change.
- **Consequence:** anyone who reads the spec to extend or repair these arms will look for `GIT()` overrides that do not exist.
- They could also bring the overrides back, which would break the lexicon pins again.
- Behaviour is not affected. The test's own comment explains the choice ("A function override would add a shell definition, and the lexicon pins those"), which lowers the chance of misleading the next change.
- **Grades:** id 3 is LOW, its binding grade.
- **Fix (judged SOUND by the skeptic):** bump the spec to rev-2.
- Rewrite the §4 table rows for `addfail` and `difffail`, and the paragraph after them, to describe the PATH `git` shim. The shim matches `<mode> -c <pin> -c <pin> add -A *` and the exact `diff --cached --quiet`, and passes every other call to the real git.
- Add a revision-log entry that names red fix 26f99cdb0 and the lexicon-pin reason.
- Lines 181, 182, 184 and 186 are the only places `override` appears in the spec and brief, so this rewrite covers every stale mention.
- **Left-shift gate:** add a bug-class checklist entry under `amendment-leaves-its-other-half-standing`. A red-fix commit that changes how an arm stages its failure must amend the spec section that describes that arm, with a revision-log entry, before the spec is marked CLOSED.

review-shape kind=diff-review round=1 intensity=full at=synth raw=3 confirmed=2 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=0 low=2 agents=9 out-tokens=31307 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | verification | tools/unattended/unattended.test.sh:17217 | medium | low | refuted | The coverage gap is real: run_render_helper (unattended.test.sh:17217) discards write_run_record's status, and AC6's grep `return [1-9]` would miss `return "$dq"`. The consequence the finding claims cannot happen, though. write_run_record has one caller, unattended.sh:16886, `case "$_fact" in LANDING\|ABORTED) write_run_record "$SLUG" ;; esac`. Its status is never read, and the next line is `RUNLOG_CLEAN=1; exit "$status"`. The driver runs under `set -u` only, with no `set -e` (line 69). So if the skip or refusal arm were edited to `return 1` or `return "$dq"`, an in-place --close would still exit with $status. The no-verb-exit-moves rule is held by how the caller is built, not by the return value. The diff introduces no reachable wrong result, so the finding has no consequence. | instance | observed-by-claim-no-arm-discharges | - |
| 2 | verification | tools/unattended/unattended.test.sh:17237 | low | low | confirmed | The diff adds unattended.sh:16597, the skip line `... last committed at $(GIT log -1 --format=%h -- "$rec" 2>/dev/null)`. Because of the 2>/dev/null, a failed log call or a wrong $rec would end the line in a blank hash and print no error. The AC1 arm at unattended.test.sh:17236-17239 only checks the prefix `unattended: run record unchanged` plus `HEAD: same` and the absence of `its commit failed`. Nothing reads the hash. In `same` mode, run_render_helper writes lu-record.md before `fixture`, so the record is committed and a real hash exists to compare against. The gap is real and was introduced by this diff. Its effect is limited to the wording of an informational line, and no exit code or commit depends on it, so it is low. | sound | - | class:observed-by-claim-no-arm-discharges |
| 3 | intent | memory/builds/dSkippedRecord/spec/2026-11-20-spec-TOOL-dSkippedRecord-1.md:181 | low | low | confirmed | I confirmed this. The spec at HEAD is marked 'CLOSED · rev-1'. Section 4, lines 181-186, still describes `addfail` and `difffail` as `GIT` function overrides that pass every other argv to `git -c pins`. Its revision log, section 9 line 305, holds only 'rev-1 · initial draft'. Red fix 26f99cdb0 changed the arms, and e56a3e698 touched the spec only to add the red-fix record rows. The code, in the `case "$lu_mode" in addfail\|difffail)` block of unattended.test.sh near line 17206, writes a `git` shim into `$lu_g/lu-shim` and puts it first on PATH. The shim matches `<mode> -c <pin> -c <pin> add -A *` and the exact `diff --cached --quiet`, and execs the real git for every other call. So the spec describes a mechanism that was never built. This diff caused the drift. I graded it low because only the record is wrong and behaviour is not affected. Also, the test carries its own comment explaining the choice ('A function override would add a shell definition, and the lexicon pins those'), so the next person changing this code is unlikely to be misled. The fix is sound: 'override' appears in the dSkippedRecord spec and brief only at lines 181, 182, 184 and 186. The proposed fix rewrites the two table rows and the paragraph after them and adds a rev-2 log entry, which covers every stale mention. | sound | - | class:amendment-leaves-its-other-half-standing |

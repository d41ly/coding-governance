**Serves:** diff-review TOOL-dSafePassage-95

# Closing diff review, round 7: dSafePassage, the round-6 fix unit TOOL-dSafePassage-95

2026-11-01 · Tier-2 · on `branch/unattended-dsafepassage-567339` · adversarial fan through `tier2-review.js` (5 finder lenses, then 4 skeptic batches, then this synthesis). This round reviews the unit promoted from round 6 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-94-closing-diff-round6.md`). It does not review round 6's subject again. 95's round-1 spec audit (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-95-spec-audit-round1.md`) was folded into the spec before the build.

**Reviewed range:** `638be1f8b58d1e144f9159ee82d1bfe13341d3b6...744d2551799b37a538cfe1868bd52ed39e3fdc4a`. **ROUND 7.**

## Verdict: CLEAN WITH FIXES

No blocker and no high. One medium and two lows remain, all in the new `[dSP-95]` lines and the staging of `steps94` in `check_floor_bash`. None of them changes the bar's verdict today. The medium is a check whose label claims more than it tests.

Subjects reviewed:

- 95 edits only `check_floor_bash` in `tools/govkit/selftest.py`.
- The stand-in path is held in one name, `stand94 = stub92.joinpath(...)`, so the `[dSP-71] AC4` hand-picked-copies guard reads no hit. This was round 6's item 1, a red `govkit selftest` leg.
- The third `[dSP-94]` check also requires the bytecode precondition and the pinned mtime.
- Two `[dSP-95]` checks use a sentinel to observe the bash-cache restore on the return path and on the raise path.
- `steps94` is staged through `build_staged_copy` inside a guarded load.
- The second `[dSP-94]` check counts the anchor once.
- Corrections to 94's spec text are in 95's section 4.

Review shape: intensity full, raw 4, confirmed 3, refuted 1, unverified 0 (0 uncertain), precision 0.75. Adjudicated tally by item: 3 items, 0 blocker, 0 high, 1 medium, 2 low. By raw confirmed finding: 3 findings, 0 blocker, 0 high, 1 medium (id 1), 2 low (ids 2, 4).

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

### Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 3 judged sound, 0 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intent: no spec was supplied to the fan. `context` was the caller's statement, read beside the range's commit messages.
- Checklist: none was swept, because none exists. A zero count is not evidence that the project's recurring bug classes are absent.
- By design: the caller's byDesign list (the AC4 guard, `joinpath`, node a, the held units).

Every lens and every skeptic batch returned, so the run's integrity counts are all zero.

## MEDIUM

### 1. The two `[dSP-95]` restore checks never read what the read returned, so each passes on a path it did not run (id 1)

**Where:** `tools/govkit/selftest.py:4516` (return path) and `:4517-4518` (raise path), both added in this range.

**What is wrong:** `read_fallback_argv` (`:4470-4484`) restores `steps._BASH` in a `finally`, so the memo comes back whether `resolve_shell_argv` returns or raises. The raise-path check tests only `getattr(steps94, "_BASH", None) == sentinel94` and never looks at `cut94`. The return-path check tests only `us._BASH == bash87` and never looks at `argv94`.

**Consequence:** 95's own Measured row 228 (the `steps._BASH = None` cut) shows the copy's read returning `['dsp95-sentinel', 'x']` without raising. In that run only the first and second `[dSP-94]` checks read FAIL. "The read that raises gives the copy's bash cache back" reads ok on a run where nothing raised. The suite is red today only because the paired second `[dSP-94]` check is red. If that check is loosened or moved, the raise-path check certifies a path it never ran.

**Fix (skeptic judged it SOUND):** tie each check to the path its label names. At `:4517` use `isinstance(cut94, OSError) and getattr(steps94, "_BASH", None) == sentinel94`. At `:4516` use `argv94 == ["bash", "x"] and us._BASH == bash87`. Each detail string should name `cut94` or `argv94`. The probe the build must run: stage the `steps._BASH = None` cut and see the raise-path `[dSP-95]` line read FAIL.

**Left-shift gate:** for each new selftest check whose label names a path ("that raises", "on return"), the build's break-staging must include a break that takes the other path and turns that check red by itself. Record it as a Measured row the spec's AC cites.

## LOW

### 2. The raise-path `[dSP-95]` check does not assert the read raised (id 4)

**Where:** `tools/govkit/selftest.py:4517-4518`.

**What is wrong:** this is the raise-path half of item 1, reported by the intent lens. S3 (spec lines 42-45 and 161-166) and the label say this check observes the raise path. Its condition holds whenever the sentinel comes back. A probe ran `read_fallback_argv`'s logic over a stand-in whose `resolve_shell_argv` returns. It printed `['bash', 'x'] False True`: the read did not raise, yet the condition held.

**Consequence:** contained. The suite stays red only through the second `[dSP-94]` check's `isinstance(cut94, OSError)`, and a copy that never loaded reads None and fails. Read alone, this check's ok does not show what its label claims. An edit to the `[dSP-94]` condition would drop the raise-path guarantee without anyone noticing.

**Fix (skeptic judged it SOUND):** `isinstance(cut94, BaseException) and getattr(steps94, "_BASH", None) == sentinel94`, with the detail naming `cut94`. To confirm it, stage a copy whose `resolve_shell_argv` returns, and see this check read FAIL by itself. Item 1's stricter `isinstance(cut94, OSError)` form also satisfies this item, so one edit closes both.

**Why a separate item:** ids 1 and 4 describe one defect at one line. Their binding grades differ (medium and low), and findings are merged only within one binding grade, so this item stays separate. Do not count it as a second defect.

**Left-shift gate:** the same gate as item 1.

### 3. `steps94` staging fails on a reused `tmp`, giving three false FAILs (id 2)

**Where:** `tools/govkit/selftest.py:4495-4496`, which calls `build_staged_copy(tmp / "dsp94-narrowed", ...)`. `build_staged_copy` (`:3646`) calls `shutil.copytree` without `dirs_exist_ok`.

**What is wrong:** when `tmp/dsp94-narrowed/govkit` already exists, `copytree` raises `FileExistsError`. At base the copy was compiled in memory and nothing was written under `tmp`. Every other write `check_floor_bash` makes under `tmp` tolerates a reused directory: `mkdir(exist_ok=True)` at `:4442` and `:4528`, and `rmtree(ignore_errors=True)` at `:4537`.

**Consequence:** observed. Rerunning AC1's command on a used scratch dir printed `FAIL [dSP-95] the staged copy of upgrade_steps.py loads — FileExistsError(17, ...)`. It then printed FAIL on the second `[dSP-94]` check (AttributeError) and on the raise-path `[dSP-95]` check (None). All three point at the copy, not at the stale directory. The bar is unaffected: it calls `check_floor_bash` once, inside a fresh `TemporaryDirectory` (`:5523`), and AC1 uses a fresh `tempfile.mkdtemp()`. Only a manual rerun or a break-staging loop that reuses `tmp` hits this.

**Fix (skeptic judged it SOUND):** put `shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)` ahead of the `build_staged_copy` call, or stage under a fresh `tempfile.mkdtemp(dir=tmp)`. Leave `build_staged_copy`'s shared semantics unchanged.

**Left-shift gate:** a bug-class checklist entry: "a selftest arm that writes under `tmp` must run twice on one `tmp` and read the same." Turn it into a gate by having the selftest run `check_floor_bash(tmp)` twice in one directory and compare the FAILURES lists.

## Refuted

Id 3 (verification, `tools/govkit/selftest.py:4515`) claimed that the anchor-count conjunct had never been seen red by itself. Measured row 227 of 95's spec contradicts that claim: narrowing `check_runs`' anchor in `upgrade_steps.py` itself leaves `anchor count 0` while `cut94` is an OSError. The gap that remains is in how the evidence is attributed. The count-2 case in a copy that compiles is not measured on its own. That gap does not affect the check's behaviour and is not an item.

review-shape kind=diff-review round=7 intensity=full at=synth raw=4 confirmed=3 refuted=1 unverified=0 blocker=0 high=0 medium=1 low=2 agents=10 out-tokens=61449

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | seams | tools/govkit/selftest.py:4517 | medium | medium | confirmed | This diff added the defect: at 744d25517 both restore checks are new (selftest.py:4516-4518). read_fallback_argv (4470-4484) puts the memo back in a `finally`, so the memo is restored whether the call returns or raises. The check at 4517-4518 reads only `getattr(steps94, "_BASH", None) == sentinel94` and never looks at cut94. It prints ok whenever the memo comes back, including runs where the copy's read returned. Spec 95's own Measured row 228 (the `steps._BASH = None` cut) records exactly this. Only the first and second [dSP-94] read FAIL, the second naming the returned ['dsp95-sentinel', 'x']. The [dSP-95] 'the read that raises' line is not in the FAIL list, so it read ok on a run where nothing raised and the memo never changed. The return-path check at 4516 is the same: it never reads argv94. The overall verdict is still correct today, because the paired second [dSP-94] check is red on those runs. So the effect is contained, but the label vouches for a path the check did not run. Not covered by any BY DESIGN item, which are about the AC4 guard, joinpath, node a and the held units. | sound | - |
| 2 | seams | tools/govkit/selftest.py:4495 | low | low | confirmed | The defect is real, and this diff introduced it. In tools/govkit/selftest.py, build_staged_copy (line 3646) calls `shutil.copytree(HERE, dst, ignore=...)` without dirs_exist_ok, so it raises FileExistsError when `tmp/dsp94-narrowed/govkit` already exists. At base 638be1f8b, steps94 was compiled in memory from HERE/upgrade_steps.py and nothing was written under tmp. This range added the copytree at 4495-4496. Every other write check_floor_bash makes under tmp tolerates a reused dir: fake87 uses mkdir(exist_ok=True) at 4442, stub92/steps uses exist_ok at 4528, and __pycache__ is removed with rmtree(ignore_errors) at 4537. So this function could be rerun on the same dir at base, and that is now broken. On a rerun, the guarded load at 4500-4501 records a FAIL. steps94 then stays an empty ModuleType. read_fallback_argv then returns an AttributeError, so the second [dSP-94] check fails at 4515, and getattr(..., None) fails the raise-path [dSP-95] check at 4518. That gives three false FAILs, as the finder says. The reach is narrow. The bar's only call is check_step_isolation -> check_floor_bash(tmp) at 4427, inside a fresh TemporaryDirectory (around 5522). Spec AC1 also uses a fresh tempfile.mkdtemp(). Only a manual rerun on a reused scratch dir hits it. Nothing wrong ships and the bar is unaffected, so the effect is limited to a misleading diagnostic on an off-contract rerun: low. | sound | - |
| 3 | verification | tools/govkit/selftest.py:4515 | low | - | refuted | The claim is that the count conjunct has never been seen red by itself, and that the appended-anchor row is the only break measured for it. The spec contradicts both. Row 227 of 95's spec Measured table (memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md) narrows check_runs' anchor in upgrade_steps.py itself. In that run src94 holds no anchor, so the replace at selftest.py:4496 changes nothing. The staged copy is then the narrowed source, it compiles, and its spawn's OSError escapes, so cut94 is an OSError and `isinstance(cut94, OSError)` is true. The second [dSP-94] check still reads FAIL naming `anchor count 0`. Spec lines 239-240 say this directly: at 94 that break failed only the first check, and it now fails the second as well 'because the narrowed text leaves the anchor at zero'. So the conjunct `src94.count(anchor94) == 1` has a recorded red that it alone produced. What is true: the duplicate-anchor case (count 2 in a copy that compiles) is not measured on its own, and the §10 arm row that credits the red to 'a second anchor appended' cites a run where the copy also fails to compile. That is a gap in how the evidence is attributed, with no effect on what the check does, and does not establish the finding's claim as written. | sound | - |
| 4 | intent | tools/govkit/selftest.py:4517 | low | low | confirmed | I read selftest.py:4470-4518. read_fallback_argv restores `steps._BASH = held` in a `finally` (4483-4484), so that line runs whether resolve_shell_argv returns or raises. The second [dSP-95] check (4517-4518) only tests `getattr(steps94, "_BASH", None) == sentinel94`. If the copy's call returned instead of raising, that condition would still hold. Nothing in the check itself shows the raise path was taken, even though its label and spec S3 (spec lines 42-45, 161-166) say it observes that path. The diff added this check, so the finding is in scope, and nothing in the BY DESIGN list covers it. The consequence is contained. The suite still goes red, because the second [dSP-94] check at 4514-4515 requires `isinstance(cut94, OSError)`. A copy that never loaded also fails, because getattr then reads None. So no wrong verdict ships. The real problem is that the check's ok, read on its own, does not show what its label claims, and an edit to the [dSP-94] condition would silently drop the raise-path guarantee. That is low. | sound | - |

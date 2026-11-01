**Serves:** diff-review TOOL-dSafePassage-90 TOOL-dSafePassage-91

# Closing diff review, round 4: dSafePassage, the round-3 fix units TOOL-dSafePassage-90 and -91

Node `d` · 2026-11-01 · Tier-2 · on `branch/unattended-dsafepassage-567339` · adversarial fan through `tier2-review.js` (5 finder lenses, then 4 skeptic batches, then this synthesis). This round reviews the units promoted from round 3 (`memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md`). It does not review round 3's subject again. The spec audit is `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md`.

Subjects reviewed:

- 90: in `tools/govkit/govkit.py` `_cmd_update`, the samefile arm no longer feeds the occupancy test. `in_place`, the exact spelling, decides both the refusal and the move. The one `r.fail` names one of three causes: a case-only rename, a link or filesystem alias, or an occupied destination. `[dSP-90]` reads the target's index and bytes.
- 91: the pre-write snapshot records a renamed row's destination only when it differs from the row's own path. `FIXTURE_FILES` and `derive_policy_adopter` in `tools/govkit/upgrade_walk.py` come with a plant-root grader over every kind. `set_environ` and `check_floor_bash` are in `tools/govkit/selftest.py`.

**Reviewed range:** `112e587eafb65a6ab62c80100e6ff48412cadba9...2e6d48453881b97b7dd0f9a8f981b0beb28b7595`. **ROUND 4.**

## Verdict: CLEAN WITH FIXES

There is no blocker. There is one high: the new `[dSP-91 L2]` check goes red falsely on a Windows host that has the WSL launcher but no distribution, and the hosted `windows-latest` runner is such a host (item 1). Two mediums and one low follow it. Three of the four defects are in the new `[dSP-91 L2]` and `set_environ` work in `selftest.py`. The fourth is a refusal text that 90 added and no gate ever triggers. The current product code behaves correctly in every item. The defects are in a check, in gate coverage and in a record. Two fixes were judged sound. Two were rejected, and for each of those this report gives the skeptic's corrected fix.

Review shape: intensity full, raw 4, confirmed 4, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 4 items, of which 0 are blocker, 1 high, 2 medium and 1 low. By raw confirmed finding: 4 findings, of which 0 are blocker, 1 high (id 1), 2 medium (ids 2, 3) and 1 low (id 4). No findings were merged, so each item covers one finding.

### Run integrity

- Lenses: 5 of 5 returned, 0 died. Skeptic batches: 4 of 4 returned, 0 died.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 2 judged sound, 2 judged unsound, 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 left ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were `gov-diff-reviewer`, the skeptic batches `gov-skeptic`, and the synthesis `gov-synthesizer`.
- Intent: no spec was supplied to the fan. `context` was the caller's statement, read beside the range's commit messages.
- Checklist: none was swept, because none is present. The zero counts on the security and seams lenses are not evidence that this project's recurring bug classes are absent.
- By design: the caller's byDesign list.

## HIGH

### 1. `[dSP-91 L2]` goes red falsely on a Windows host with the WSL launcher and no distribution (id 1)

**Where:** `tools/govkit/selftest.py:4464`, the positive needle `("bash" in tail or "python-floor.sh" in tail)` in `check_floor_bash`.

**What is wrong:** when GOV_BASH is unset, `tools/govkit/steps/python_floor.py:36` passes the bare `bash` argv to subprocess through `resolve_shell_argv` (`upgrade_steps.py:425-440`). The Windows loader resolves that argv to `C:/Windows/System32/bash.exe` before it searches PATH. On a host that has no WSL distribution, the launcher prints "Windows Subsystem for Linux has no installed distributions ... wsl.exe --list --online", mostly in UTF-16. This is recorded in `memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md:39` and in spec TOOL-aMendedFleet-98:67-71. `run_step_isolated` (`upgrade_steps.py:1795-1805`) decodes the output as UTF-8 with errors=replace, so a NUL lands between every character. Even the ASCII form of the message has no `bash` in it. If the message goes to stdout, the witness tail, which is stderr only, is empty. In each case the needle misses, although the stub did fall back to bare bash. The finder ran the check's exact predicate over the message in ASCII and in UTF-16 decoded as UTF-8, and both returned False. On node `d`, which has the `claude-u26` distribution, the check reads ok only because a distribution is installed. Spec 91 §4 measured rev-2 only on node a, which has a distribution (rc 127). Its Alternatives text names only the with-distro case and the no-bash `FileNotFoundError` case.

**Consequence:** `govkit selftest` goes red in the remote-ci held job (`runs-on: windows-latest`) and on any node without a distribution, even when the fallback works correctly. `remote-ci.yml:15` says the held job blocks nothing, and this is a false red, not a false green. It is still high because it misleads the next change: whoever reads the held run next will chase a fallback that is not broken.

**Fix (judged SOUND by the skeptic):** strip NULs from the tail before matching (`tail = got["tail"].replace("\x00", "")`). Accept the launcher's "Windows Subsystem for Linux" text as a third positive needle, because bare bash resolving to that launcher means the fallback reached the loader. Keep the three negative needles. The build must observe this case red before the change and green after it. Either run `check_floor_bash` with a fake System32 directory on PATH whose `bash.exe` prints the UTF-16 no-distribution text, or run the check on the hosted runner.

**Left-shift gate:** make that fake-launcher arm a permanent `[dSP-91 L2]` sibling in the selftest, so the no-distribution host is measured on every node and not only on the hosted runner. Add a checklist entry for this class: a check that greps a child process's output for a word must be measured on every host shape the bar runs on, including a launcher that answers in UTF-16.

## MEDIUM

### 2. The link-or-alias refusal text 90 added is never triggered by any gate (id 2)

**Where:** `tools/govkit/govkit.py:11113-11124`, the `_alias and not _case` branch of `_cmd_update`'s refusal. Its only arm is `[dSP-90]` at `tools/govkit/selftest.py:13129-13147`.

**What is wrong:** at base `112e587ea`, `govkit.py:11078` counted a samefile alias as the row's own file, so the "under another name (a link or a filesystem alias)" text did not exist. 90 adds that text. `[dSP-90]` runs only a case-only rename (`git mv moved/demo/keep.txt moved/demo/Keep.txt`) and checks only for the case-only text. In `selftest.py`, "under another name" appears only in unrelated fixture strings at 16168-16191, and `os.link` does not appear at all. Spec 90 (lines 229-320, AC1) says only the one-off `p90_probe.py` fourth line checks the hard-link behaviour, and it records that "S2's check was not run inside the govkit selftest".

**Consequence:** if the code regressed to `_case = _alias` (the rev-1 form the spec measured red as M5), or if the alias text were deleted, the bar would stay green. Take an adopter whose own hard link or symlink sits at gov's new name, for example `linked.txt` linked to `keep.txt`, and gov then renames `keep.txt` to `linked.txt`. After such a regression, that adopter would be told the cause is case folding and to re-run on a case-sensitive checkout. The effect is contained: the refusal still fires and no bytes move. Only the remedy text would be wrong.

**Fix (judged SOUND by the skeptic):** add a `[dSP-90]` sibling to the DEPL-dCarriedReceipt-11 block in `selftest.py` that copies p90's hard-link case. Build a fresh `build_rename_gov` and target. In the target, `os.link` `pinned/demo/linked.txt` to `pinned/demo/keep.txt` and commit it. Then, in gov, `git mv keep.txt linked.txt` and run `update --write`. Assert exit 1, `under another name (a link` in stdout, `case-only rename is on a case-insensitive filesystem` not in stdout, and keep.txt's bytes unchanged. Stage it red once with `_case = _alias`.

**Left-shift gate:** the new arm is the gate for this case. For the class, add a checklist entry: every distinct refusal text a unit adds needs an arm in the bar that triggers it. A spec's one-off probe does not count as that arm.

### 3. `[dSP-91 L2]`'s positive needle is satisfied by the traceback's echo of python_floor.py:36 (id 3)

**Where:** `tools/govkit/selftest.py:4466-4468`, the predicate `("bash" in tail or "python-floor.sh" in tail) and "python_floor.py:" not in tail and` no Refusal or Set GOV_BASH.

**What is wrong:** line 36 of `tools/govkit/steps/python_floor.py` is `return subprocess.run(steps.resolve_shell_argv(["bash", ...]))`. When anything on that line raises, Python's traceback echoes the source line, and that line contains `bash`. The exclusion `python_floor.py:` matches only the stub's own LookupError message. A traceback frame reads `python_floor.py", line 36`, so the exclusion never matches it. The tail is the last 20 lines of stderr (`upgrade_steps.py:1798`), so the echoed line always falls inside it. The finder reproduced this. A scratch `python_floor.py` whose `steps.resolve_shell_argv(["bash", ...])` raised (AttributeError, and RuntimeError('none')) gave a tail on which this exact predicate returned True.

**Consequence:** suppose a regression makes resolve_bash's no-candidate branch raise something other than Refusal, such as StopIteration or IndexError, or makes the fallback re-raise `from None`. The fallback would be dead and `[dSP-91 L2]` would still read ok. `[dSP-87 AC5]` would stay green too, because with GOV_BASH set it never takes that branch. The spec folded in the audit's M3 so that this check would catch exactly that regression. The effect stays inside one selftest, and the current code is correct.

**Fix (REJECTED by the skeptic; the skeptic's corrected fix):** grade the tail for a crash, not for the word bash. Fail if the tail holds `Traceback` and its last line is not a `FileNotFoundError` or `OSError` (a failed spawn of bare bash). Fail on `python_floor.py:`, `upgrade_steps.Refusal` or `Set GOV_BASH`. Do not require the spawn error's text to name bash. Keep the finder's probe: make resolve_bash's no-candidate path raise RuntimeError in a scratch tree and record `FAIL [dSP-91 L2]`. That probe reads `ok` today. Build this together with item 1's fix, since both edit the same predicate.

**Left-shift gate:** commit the RuntimeError regression as a mutation arm beside `[dSP-91 L2]`, so the check's red state is measured on every run. Add a checklist entry: a needle that greps a traceback-bearing tail must not match text the traceback can echo from the source line that raised.

## LOW

### 4. The record says `set_environ` holds all four environment uses in selftest.py, and two hand-typed copies remain (id 4)

**Where:** `tools/govkit/selftest.py:292` (`set_environ`), the 91 commit message, and spec 91's rev-2 L3 note. The remaining copies are GOVKIT_NO_REMOTE_PROBE at `selftest.py:6358-6366` and GOV_BASH at `selftest.py:18418-18432`.

**What is wrong:** the commit message and the L3 note say `set_environ` "holds all four environment uses in selftest.py". `set_environ` is used only at :3787, :4422, :4452 and :4462. Two single-key save-and-restore copies remain, and they already existed at the base (:6339 and :18383). Nothing in this range is blamed on those copies. Only the claim is new. The spec's S3 body is precise: "the three hand-typed copies of this loop in check_step_isolation" plus the new `check_floor_bash`. AC7's guard greps only the literal `os.environ.get(k) for k in`, so it cannot see a single-key copy.

**Consequence:** behaviour does not change. The next person to add an environment arm will read the claim, and AC7's green result, as proof that the file uses one helper, while the GOV_BASH copy at :18418 is still hand-typed.

**Fix (REJECTED by the skeptic; the skeptic's corrected fix):** narrow the spec and ledger wording to "the three copies in check_step_isolation and the new check_floor_bash". A commit message cannot be edited, so record the correction in the next record or ledger entry. Optionally, move :6358 and :18418 onto `set_environ`. `set_environ({"GOVKIT_NO_REMOTE_PROBE": None})` keeps the semantics of :6358. For :18418, put only GOV_BASH in `set_environ` and keep its `_BASH` restore. If a guard is wanted, write a predicate over the real tree with an allow-list for the two deliberate, unrestored suite-wide seam sets at :5407 (main) and :6373. One example is an `os.environ.get(` paired with a later `os.environ[...] =` restore outside `set_environ`. Run it over the real tree first.

**Left-shift gate:** a pattern guard is optional, as described in the fix above. The class goes in the checklist either way: a record's summary claim about a whole file must match the spec body's scope, and an AC guard that backs such a claim must match the pattern, not one spelling of it.

review-shape kind=diff-review round=4 intensity=full at=synth raw=4 confirmed=4 refuted=0 unverified=0 blocker=0 high=1 medium=2 low=1 agents=10 out-tokens=89422

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/govkit/selftest.py:4464 | high | high | confirmed | I read selftest.py:4457-4467. With GOV_BASH unset, the PATH keeps the System32 and WindowsApps entries and drops every other directory holding bash. tools/govkit/steps/python_floor.py:36 then spawns resolve_shell_argv(['bash', ...]). That function (upgrade_steps.py:425-440) returns the bare argv when resolve_bash refuses, so the Windows loader picks C:/Windows/System32/bash.exe ahead of PATH. run_step_isolated (upgrade_steps.py:1795-1805) decodes as UTF-8 with errors=replace, and for the witness phase the tail is stderr only, with no stdout fallback. On a host with the launcher but no distribution, the census (aMendedFleet held-red-census:39) and spec TOOL-aMendedFleet-98:67-71 record that bare bash on windows-latest prints the WSL 'no installed distributions' text, mostly in UTF-16. That text contains neither 'bash' nor 'python-floor.sh'. Decoded as UTF-8 it has a NUL between every character, and if it goes to stdout the tail is empty. In each of those cases the positive needle misses, so [dSP-91 L2] goes red even though the fallback reached the loader. Spec 91 section 4 shows that rev-2 was measured only on node a, which has a distribution (rc 127, 'No such file or directory'), and its Alternatives text names only the with-distro case and the no-bash FileNotFoundError case. The check is new in this range (TOOL-dSafePassage-91), so it is in scope. None of the by-design items covers it. Severity: the false red reaches every hosted held run and any node without a distribution. remote-ci.yml:15 says the held job blocks nothing, and the failure is a false red rather than a false green. So it fits high as a defect that misleads the next change, not blocker. | sound | - |
| 2 | verification | tools/govkit/govkit.py:11113 | medium | medium | confirmed | At base 112e587ea, govkit.py:11078 counted a samefile alias as the row's own file (`own_file = ... or ndp.samefile(_own)`), so the other-name refusal text did not exist. This diff adds it at govkit.py:11113-11124: `_alias` picks the 'under another name (a link or a filesystem alias)' text whenever `not _case`, so the defect is in scope. The selftest has one arm for this code, `[dSP-90]` at selftest.py:13129-13147. That arm only runs a case-only rename (`git mv moved/demo/keep.txt moved/demo/Keep.txt`) and only checks for the case-only text. I grepped selftest.py: 'under another name' appears only in unrelated fixture strings at 16168-16191, and `os.link` does not appear at all, so nothing creates a link at the rename destination. The spec itself says the hard-link behaviour is checked only by the one-off p90_probe.py fourth line (spec 90 lines 229-320, AC1). It also records that 'S2's check was not run inside the govkit selftest'. So a regression to `_case = _alias`, which the spec measured as M5, or the loss of the alias text would leave the bar green. Nothing in the BY DESIGN list covers this gap: its case-sensitive-link note is about wording, not about missing coverage. The effect is contained: the refusal still fires and no bytes move. Only the remedy text would be wrong, so medium. | sound | - |
| 3 | intent | tools/govkit/selftest.py:4466 | medium | medium | confirmed | The check is new in this diff: the base selftest.py has no dSP-91 lines. Its predicate, at selftest.py:4466-4468, is `("bash" in tail or "python-floor.sh" in tail) and "python_floor.py:" not in tail and no Refusal/Set GOV_BASH`. Line 36 of tools/govkit/steps/python_floor.py is `return subprocess.run(steps.resolve_shell_argv(["bash", ...]))`. Python's traceback echoes that source line, which contains `bash`. The exclusion `python_floor.py:` only matches the stub's own LookupError message. A traceback frame reads `python_floor.py", line 36`, so the exclusion never matches one. The tail is the last 20 lines of stderr (upgrade_steps.py:1798). I reproduced it: a scratch python_floor.py whose `steps.resolve_shell_argv(["bash", ...])` raises RuntimeError('none') gave a tail on which this exact predicate returned True. So any non-Refusal raise in resolve_bash or resolve_shell_argv kills the fallback, and [dSP-91 L2] still reads ok. That is the regression the spec's M3 fold meant this check to catch. The effect stays inside one selftest and the current code is correct, so medium. | unsound | - |
| 4 | intent | tools/govkit/selftest.py:292 | low | low | confirmed | I confirmed this. The 91 commit message says `set_environ` "holds all four environment uses in selftest.py", and the spec's rev-2 L3 note says the same. The tree has more than that. selftest.py:6358-6366 pops GOVKIT_NO_REMOTE_PROBE and restores it by hand. selftest.py:18418-18432 saves `keep_env = os.environ.get("GOV_BASH")`, sets the variable, then pops or restores it in a finally block, which is the same save-and-restore pattern. `set_environ` is used only at :3787, :4422, :4452 and :4462. The spec's S3 body is precise: "the three hand-typed copies of this loop in check_step_isolation" plus the new check_floor_bash. So the record overclaims only in its summary wording, which this diff introduced. The two copies themselves are pre-existing: at the base they sit at :6339 and :18383, and nothing here is blamed on them. AC7's second grep matches only the literal `os.environ.get(k) for k in`, so it cannot see a single-key copy. Its stated red, "the save-and-restore loop is typed again", covers only that one spelling. Behaviour does not change, so the consequence is a misleading record and nothing more: low. | unsound | - |

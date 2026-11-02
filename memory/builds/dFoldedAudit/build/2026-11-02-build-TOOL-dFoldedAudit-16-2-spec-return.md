# dFoldedAudit — unit 16's spec return

**Serves:** journal TOOL-dFoldedAudit-16

I've written the spec for TOOL-dFoldedAudit-16 at Tier-2, header `OPEN · order 160 · base 74274869`. Nothing is committed. Memory hygiene checks 12 and 25 pass on it, graded through a scratch copy of the index. Section 8 has no open forks.

**Shell hygiene (scope items S1 to S4).** The five rows trace to eleven sites this build added, and every one can take its no-fork form, so no registry row is raised.
- **Driver, `pure-fn-subst` 43 to 41:** the two new `$(review_exit_note spec-…)` calls at `unattended.sh:13026-13027`. `review_exit_note` will also leave its sentence in a global, `_exitnote`, and still print it. That follows the driver's existing convention at `unattended.sh:1414-1421`. The two older calls stay as they are, so the row's stated reason stays true.
- **Driver suite:** seven `$(cat …)` reads become `$(<…)`, and two values are built with `printf -v`, bringing the rows back to 17 and 23.
- **Harness suite:** `run_strict_fa3` builds its argument with `printf -v`, like the helper above it. FA12's no-THROW check uses the suite's own `hasnt_` helper, bringing the rows back to 66 and 62.

The scratch-guard hook blocked me from running the leg, so I took the counts from the scanner's own functions, run over BASE and HEAD. With the edits applied in memory, every row comes back to its registered count.

**Drift pin (S5): the brief's `36 -> 38` comment alone would still fail.** The drift report compares against `refs/remotes/origin/main`, which already pins 37 for `SPEC_AC_ORDER_CUTOFF` (TOOL-dSafePassage-34). That commit isn't on this branch. So the history line has to state both `36 -> 38` and `37 -> 38`, and the spec writes it that way. It still names both keys and the decision row, as the brief asks.

**For you:**
- **Run at the close:** the two acceptance commands are the legs' own commands, which the hook won't let a role agent run. AC1 (shell hygiene) and AC8 (`drift_report.py --check`) are yours. The builder gets direct checks it can run: greps, small probe scripts in §4, and a `git diff` showing the registry unchanged.
- **Merging `origin/main`:** this will conflict on the pin. The merged tree arms 38 keys now and 39 once `SPEC_FOLD_CUTOFF` arms, so the merge has to set 39 under a `37 -> 39` line. The spec hands this off rather than doing it.
- **Check 21 is red until the commit:** hygiene check 21 fails on the four records that cite TOOL-dFoldedAudit-16. It only counts committed specs, so your commit clears it.
- **Check 27 flags the decision row:** it reports your row at `memory/DECISIONS.md:244` as a near-match to TOOL-dTrueNorth-28, and suggests naming it or adding `supersedes`, `coexists-with` or `disputes`. I didn't touch that file.
- **Still to run:** `tools/check-spec-tokens.py`, as the brief says.

The section 7 leg line names the two flagged legs, the five suites the touched folders require, and `unattended kit gate`.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-02-spec-TOOL-dFoldedAudit-16.md

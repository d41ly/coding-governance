# TOOL-dTotalRecall-75 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-75
**Caused-by:** TOOL-dTotalRecall-75

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`8b31081acce8bec56dfc2bee10555baf29f3251f` on node a, 2026-11-24. This pass's commit touches no path of the `watch:`
line, so each read below holds at its tip. The `kickoff-manifest ratchet` leg's own verdict, C9's age condition with it,
is the main loop's pass legs', and §7's other legs are the close's.

§B re-read at the base, over the watched commits since `491dfe31c`: those of §4's table and `408d05723`, unit 70's.
The pointer map, the gate commands, the tier rule, the families and id protocol, the conf lines it names, and the traps
hold. No claim of the build's watched edits is stale: none corrected. One dated correction, the 2026-11-10 one on
`--act defer`, has met its prune condition: its fix, `3e8557dc6` and `17308b6c3`, is on `origin/main`. The build's
watched edits did not make it so, and S1 and §8 F1's grant do not reach it, so it stands and is reported.

**Evidences:** TOOL-dTotalRecall-75
- AC1 — `git rev-list --count --no-merges <last-body-change>..HEAD -- <each path of the watch: line>` — printed 0 over the 11 watched paths, and `git merge-base --is-ancestor` of unit 69's pass commit `f7011dd6f` and the new value exited 0; over the old value `491dfe31c` the same call exited 1, so the read can red (DERIVED 2026-11-24, these commands).
- AC2 — `grep -cE '^last-body-change: [0-9a-f]{40}$' memory/guides/SESSION-KICKOFF.md` — printed 1; W and S are both `408d05723`, so W is an ancestor of S; the new value is an ancestor of HEAD, exit 0 (DERIVED 2026-11-24, these commands).
- AC3 — `git show <this unit's pass commit> -- memory/guides/SESSION-KICKOFF.md` — read before the commit as the staged diff: one `-last-body-change:` line and one `+last-body-change:` line, no line below the `manifest-audit` block and so no `last-audit:` change; the commit's `Decided:` trailer names each claim re-read and `none corrected` (DERIVED 2026-11-24, this diff).

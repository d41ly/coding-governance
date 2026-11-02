# dFoldedAudit — unit 17's rev-3 spec-writer return

**Serves:** journal TOOL-dFoldedAudit-17

Run direct/a3540089a140ed628, summarized from its task notification.

- Rev-3 merges in the run worktree. The branch guard refuses only when the git dir equals the common dir (`.githooks/pre-commit:75-77`), and in a linked worktree they differ. The clone, the driver copy and the fast-forward are gone. A new stop subsection covers failures: any failed step before M ends the unit with `git merge --abort`, and a refused F is reported with no reset. The probes are written to a scratch folder outside the worktree.
- S7: the floor line is `SESSION-KICKOFF.md:219` on main. It was added in `1f7d1966`, whose parent is `201eb127`. The kit's spelling of the record line is used. `<n>` is derived at each commit, because the builder's 13 does not match the kit's count, which is 1 from the branch tip and 15 across both sides.
- `docs-undocumented.txt` sits outside the conflicted hunk and merges clean.
- S8 lists the four build-index renders.
- The `:1405` citation is corrected, and the trailer is the charter's.
- The worktree's hooks are the primary tree's `.githooks`. That pre-commit is byte-identical to the branch's.
- Hygiene exits 1 on two findings. Check 9 reads this build's README as stale; the dispatcher re-renders it. Check 23 flags TOOL-dFoldedAudit-16's unevidenced criteria, which predate this pass.

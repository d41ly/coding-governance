# TOOL-dGroundRules-19 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-19

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edits in the worktree, by the kit's own code over its scratch fixtures:
`check_policy.run_fixture(<case>)` called in process for each case below, never the leg, every
fixture repository under the system temp directory, short-named and removed by the case. The guard's
admission of gov's own regenerated mirror is the commit after this one, made through the pre-commit
hook.

**Evidences:** TOOL-dGroundRules-19
- AC1 — `python check_policy.py --fixture guard-mirror-render` — `run_fixture("guard-mirror-render")`, the case that command runs, committed a catalogue row, `mirror --write` printed "policy: mirror written · 263 keys", and with the mirror staged alone `guard.py --staged` exited 0 printing "policy-guard: admitted · .governance/policy.json · equals its render at HEAD". 2 assertions, 0 wrong.
- AC2 — `--fixture guard-mirror-beside-catalogue` — `run_fixture("guard-mirror-beside-catalogue")` committed the row, ran `mirror --write`, moved the row back into the index with `git reset --soft HEAD~1` and staged the mirror beside it: `guard.py --staged` exited 1 printing "policy-guard: refused · .governance/policy.json · the mirror renders HEAD: commit the policy file or catalogue first, then regenerate", then the remedy line naming `git restore --staged --worktree .governance/policy.json`. 2 assertions, 0 wrong.
- AC3 — `guard-other-paths` — `run_fixture("guard-other-paths")`, its mirror plant appending a newline to the committed mirror by hand: `guard.py --staged` exited 1 printing "policy-guard: refused · .governance/policy.json · differs from its render at HEAD" and the remedy naming `git restore --staged --worktree .governance/policy.json`; the instruction-manifest and deploy plants still refused as before. 3 assertions, 0 wrong.
- AC4 — `--fixture guard-mirror-branch-green` — `run_fixture("guard-mirror-branch-green")` committed the row on branch `side`, ran `policy.py mirror --write`, `guard.py --staged` exited 0 printing "equals its render at HEAD", the mirror was committed, and `policy.py mirror --check` at the new HEAD exited 0 printing "policy: mirror fresh". 3 assertions, 0 wrong.
- AC5 — `grep -n "regenerate"` — over `help/policy.md` it printed line 116, "- **An agent may also commit the mirror it regenerated, in a commit of its own.** ...", and line 128 naming the refusal "the mirror renders HEAD: commit the policy file or catalogue first, then regenerate", both in the section "Who may change the policy file", which no longer says every agent change to the mirror is refused.

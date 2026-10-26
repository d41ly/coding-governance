# TOOL-dGroundRules-19 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-19

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edits in the worktree, by the kit's own code over its scratch fixtures:
`check_policy.run_fixture(<case>)` called in process for each case below, never the leg, every
fixture repository under the system temp directory, short-named and removed by the case.

On gov's own tree, after the pass commit `729e51286` and the help follow-up `d88f7ddda`,
`policy.py mirror --check` named `actions.free` stale, `mirror --write` rendered 259 keys, and with
`.governance/policy.json` staged alone `python tools/policy/guard.py --staged`, run directly, exited 0
printing "policy-guard: admitted · .governance/policy.json · equals its render at HEAD"; that mirror
is `1345b7f90`, fresh by `mirror --check`, 259 `{rev}` and no branch sha8. The pre-commit hook did
NOT judge `1345b7f90`, whatever its message says: this worktree's `core.hooksPath` is the primary
checkout's `.githooks`, whose `pre-commit` carries no policy guard block until this build lands on
`main`.

The three follow-up commits after the pass (`d88f7ddda`, `1345b7f90`, `5d49772dd`) each ran under
their own `--dispatch` row but carried `Pass: none`, which closes no row, so those rows stayed open
and refused the next unit that declared `tools/policy/policy.py` beside the mirror (check 49). The
main loop's commit adding this paragraph carries `Pass: TOOL-dGroundRules-19` and closes them.

**Evidences:** TOOL-dGroundRules-19
- AC1 — `python check_policy.py --fixture guard-mirror-render` — `run_fixture("guard-mirror-render")`, the case that command runs, committed a catalogue row, `mirror --write` printed "policy: mirror written · 263 keys", and with the mirror staged alone `guard.py --staged` exited 0 printing "policy-guard: admitted · .governance/policy.json · equals its render at HEAD". 2 assertions, 0 wrong.
- AC2 — `--fixture guard-mirror-beside-catalogue` — `run_fixture("guard-mirror-beside-catalogue")` committed the row, ran `mirror --write`, moved the row back into the index with `git reset --soft HEAD~1` and staged the mirror beside it: `guard.py --staged` exited 1 printing "policy-guard: refused · .governance/policy.json · the mirror renders HEAD: commit the policy file or catalogue first, then regenerate", then the remedy line naming `git restore --staged --worktree .governance/policy.json`. 2 assertions, 0 wrong.
- AC3 — `guard-other-paths` — `run_fixture("guard-other-paths")`, its mirror plant appending a newline to the committed mirror by hand: `guard.py --staged` exited 1 printing "policy-guard: refused · .governance/policy.json · differs from its render at HEAD" and the remedy naming `git restore --staged --worktree .governance/policy.json`; the instruction-manifest and deploy plants still refused as before. 3 assertions, 0 wrong.
- AC4 — `--fixture guard-mirror-branch-green` — `run_fixture("guard-mirror-branch-green")` committed the row on branch `side`, ran `policy.py mirror --write`, `guard.py --staged` exited 0 printing "equals its render at HEAD", the mirror was committed, and `policy.py mirror --check` at the new HEAD exited 0 printing "policy: mirror fresh". 3 assertions, 0 wrong.
- AC5 — `grep -n "regenerate"` — over `help/policy.md` it printed line 116, "- **An agent may also commit the mirror it regenerated, in a commit of its own.** ...", and line 128 naming the refusal "the mirror renders HEAD: commit the policy file or catalogue first, then regenerate", both in the section "Who may change the policy file", which no longer says every agent change to the mirror is refused.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: guard.py breaks. (a) input-equality loop emptied -> guard-mirror-beside-catalogue `guard.py --staged · WRONG: exit 1` (via the render's uncommitted-changes refusal, not the input-equality reason); render and branch-green stay green. (b) mirror shape staged out -> all three `WRONG: exit 1` (1 wrong each). GREEN 75, 75, 76 assertions, 0 wrong.

# TOOL-dGroundRules-31 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-31

No merge bar, no gate leg, no fixture case of `check_policy.py` and no self-test suite ran in this
pass; a role hook refuses them. AC1 and AC2 were observed by hand over the case's own flow: a scratch
clone of this branch at `209857453` under `%TEMP%` with this pass's files committed over it, the
clone's deployer `apply --kits policy,run-gates,memory-tree` into a fresh committed target whose
`.governance/deploy.toml` names the clone, and then the case's steps run one by one with the installed
kit. AC3 and AC4 ran the worktree's `adopt-policy.sh` over scratch targets under `%TEMP%`. Every
scratch directory was removed after. The two `New arm:` lines' red-first observations, the case
`python check_policy.py --fixture adopter-fresh-target` itself, `limit-fresh-target-spawn`,
`adopter-suite` and the §7 legs are the close's.

**Evidences:** TOOL-dGroundRules-31
- AC1 — `mirror deferred` — the deployer's `apply` exited 0 with `CONFIGURE policy: adopter exit 0 — adopted` (at HEAD it exited 1 on the mirror's refusal); the installed `adopt-policy.sh --scaffold` then printed `adopt-policy: mirror deferred · .governance/policy.toml has uncommitted changes · commit, then re-run --scaffold`, exited 0, and the target held no `policy.json`. The case `python check_policy.py --fixture adopter-fresh-target` now asserts the three, and its run is owed at the close.
- AC2 — `python policy.py mirror --check` — after `git add -A` and the commit, and the memory-tree adopter's re-run (exit 0), the installed `--scaffold` printed `policy: mirror written · 254 keys · policy 43fa1bb1 · catalogue 79782691` and exited 0, `policy.json` was present, and the installed `python policy.py mirror --check` printed `policy: mirror fresh`, exit 0; once committed, the installed `regen.py --check` printed `regen: 5 declared · 5 fresh · 0 stale`, exit 0.
- AC3 — `.agent-cap.conf` — over a committed target whose policy file is committed, with an uncommitted `.agent-cap.conf` holding `cap = 3`, `bash adopt-policy.sh --scaffold --target <t>` printed `adopt-policy: mirror deferred · .agent-cap.conf has uncommitted changes · commit, then re-run --scaffold` and exited 0; with the file removed it printed `policy: mirror written` and exited 0.
- AC4 — `uncommitted changes` — a scratch copy of `adopt-policy.sh` beside a `policy.py` staged to print `policy: refused - a planted mirror refusal` and exit 2 on `mirror`, over a committed target with a committed policy file: `bash adopt-policy.sh --scaffold --target <t>` printed `policy: the policy mirror could not be rendered in <t>; the line below says why`, then the planted line, and exited 1. `check-arms.py --report` reads that `exit 1` as `ARMED reasoned` by `adopt-policy.test.sh`, and `--emit-floors` prints `tools/policy/adopt-policy.sh:4:4`, the row `.memory-tree.conf` now carries.
- AC5 — `grep -n "mirror deferred" policy.md` — printed line 86, the quoted `adopt-policy: mirror deferred · <file> has uncommitted changes · commit, then re-run --scaffold`, a line of the "Start a file in another repository" bullet, the page's install text until `TOOL-dGroundRules-34` puts it under `## Install`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture adopter-fresh-target. deferral branch staged out -> `WRONG: the deployer's apply --kits policy,run-gates,memory-tree exited 1`. GREEN `223 assertion(s) executed · 0 wrong`. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: adopt-policy.test.sh with adopt-policy.sh at 6fec8045b^: `FAIL --scaffold where the mirror refuses otherwise refuses`, `... over a committed target writes the file`, `... defers the mirror over the uncommitted file`, `... over a kept file renders again`; GREEN rc 0.

# TOOL-dGroundRules-6 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-6

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed on the built
tree before the commit, by scratch probes that import `check_policy` and call `run_guard_case` or
`run_fixture("<case>")` in process, never the leg, and by scratch repositories driving a copy of the
pre-commit hook, never the pre-commit suite. Every fixture repository sat under the system temp
directory, `pol-` or `pg-` prefixed. The thirteen `guard-*` cases took 16 s together on node a. The
naming lexicon ran and read P1 verb offenders 1213, the pin. The red-first observation of each
`New arm:` line, the policy legs and the branch-guard self-test are left for the close.

**Evidences:** TOOL-dGroundRules-6
- AC1 — `python check_policy.py --fixture guard-admits-raise` — `run_fixture("guard-admits-raise")`
  ran `guard.py --staged` over `big.md` raised 100 to 120 with its `# RAISED 100 -> 120, ...` comment
  and one decision row: exit 0, stdout "policy-guard: admitted · budgets."big.md" 100 -> 120 · its
  change record attached"; 1 assertion, 0 wrong.
- AC2 — `--fixture guard-lowered` — exit 1, "policy-guard: refused · .governance/policy.toml ·
  budgets."big.md" is a lowering: 100 -> 90", then the remedy line.
- AC3 — `--fixture guard-two-raised` — exit 1, "policy-guard: refused · .governance/policy.toml · 2
  keys changed; one cap raised is the one agent shape".
- AC4 — `--fixture guard-class-row` — exit 1, "budgets."docs/*/" is not a measured-file cap: a class
  row or no file tracked at HEAD".
- AC5 — `--fixture guard-beside-change` — exit 1, "2 keys changed" (`budgets.enforce` set beside the
  raise); `--fixture guard-beside-path` exit 1, "policy-guard: refused · .governance/deploy.toml ·
  an agent's commit may change .governance/policy.toml alone among the guarded paths".
- AC6 — `--fixture guard-no-record` — exit 1 naming both "no RAISED 100 -> 120 argument above the
  cap" and "no memory/DECISIONS.md row in this commit"; `guard-no-argument` exit 1 naming only the
  RAISED argument, and `guard-no-row` exit 1 naming only the decision row, each case's judge
  asserting the other reason absent.
- AC7 — `--fixture guard-other-paths` — three plants, each alone, each exit 1: the mirror rewritten,
  naming `.governance/policy.json` with the remedy "git restore --staged --worktree
  .governance/policy.json"; `.governance/instructions.toml` added, naming it; and
  `.governance/deploy.toml` changed, naming it. `guard-new-row` exit 1, "a key was added:
  budgets."new.md""; `guard-removed-row` exit 1, "a key was removed: budgets."small.md"".
- AC8 — `--fixture guard-merge-side` — `MERGE_HEAD` resolved after `git merge side` conflicted;
  concluded with `git checkout --theirs` the guard exited 0 printing nothing; with a third text it
  exited 1, "no RAISED 55 -> 70 argument above the cap" and "no memory/DECISIONS.md row"; 3
  assertions, 0 wrong.
- AC9 — `GOV_KITROOT=tools` — a scratch repository under `%TEMP%/pg-ac9` with `core.hooksPath`
  naming a copy of `.githooks/pre-commit`, the guard and its list at `tools/policy/`, the resolver
  tracked at `tools/lib/` and `GOV_KITROOT=tools` in `.githooks/gate-env.sh`: `git commit` of a
  lowered cap from this run's shell exited 1 printing "policy-guard: refused · .governance/policy.toml
  · budgets."big.md" is a lowering: 100 -> 90"; a commit staging only `other.txt` exited 0 with 0
  lines matching `policy guard` or `policy-guard`. A second scratch repository with a stand-in guard
  saw exit 1 and exit 2 each refused after the stand-in ran, an index tracking no resolver refused
  with "policy guard REFUSING — .governance/policy.toml staged and no python launcher to judge them.",
  and an exit-0 stand-in admitted. The owner's half, `admitted on the owner's terminal proof` at a
  terminal, needs a terminal this run's shell lacks; the owner observes it.
- AC10 — `grep -c "resolve(" guard.py` — printed `0` under `tools/policy/`, and
  `grep -nE "^\s*(import|from)\s+policy\b" guard.py` printed nothing there.
- AC11 — `grep -vE "^\s*(#|$)" guarded-paths.txt` — under `tools/policy/` it printed exactly four
  lines: `.governance/policy.toml`, `.governance/policy.json`, `.governance/instructions.toml`,
  `.governance/deploy.toml`.
- AC12 — `grep -n "RAISED"` — over `help/policy.md` it printed lines 101, 109 and 119, and
  `grep -n "terminal"` lines 95 to 97, all inside "Who may change the policy file".

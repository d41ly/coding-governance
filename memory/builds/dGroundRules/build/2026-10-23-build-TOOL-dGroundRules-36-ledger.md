# TOOL-dGroundRules-36 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-36

No merge bar, no gate leg and no self-test suite ran in this pass. The criteria were probed on a
`git clone --shared` of the branch under `%TEMP%/g36` carrying the changed `check_policy.py`, by
`python tools/policy/check_policy.py --fixture adopter-fresh-target` there, with each literal staging
applied by a script under the run's scratchpad. Every run also printed
`policy-fixture: guard-trace · WRONG .git/index · not under the policy fixtures guard`: the git
directory is `TOOL-dGroundRules-38`'s, not this unit's. The first run of the probe found that a
text-mode pipe on Windows hands `check-ignore` each non-final path with a trailing CR, so no rule
matched and the plant printed `0 ignored read(s) set aside`; the query now writes bytes, and the runs
below are after that fix. Owed at the close: AC3's `--fixture` run on the built tree after the
deviation-78 sweep and `TOOL-dGroundRules-38`, and the new arm's red-first observation (AC1, AC2).

**Evidences:** TOOL-dGroundRules-36
- AC1 — `PLANT_IGNORED` — after it, the run printed `policy-fixture: guard-trace · 8 source read(s)`, then `policy-fixture: guard-trace · 1 ignored read(s) set aside`, and no `guard-trace` line naming `probe.pyc`; `155 assertion(s) executed · 1 wrong`, the one being `.git/index`.
- AC2 — `PLANT_IGNORED` and `UNIGNORE` — the run printed `policy-fixture: guard-trace · 0 ignored read(s) set aside` and `policy-fixture: guard-trace · WRONG probe.pyc · not under the policy fixtures guard`; `156 assertion(s) executed · 2 wrong`.
- AC3 — owed at the close. On the unplanted copy, before the sweep, the run printed `policy-fixture: guard-trace · 0 ignored read(s) set aside`, so the count line prints at 0; its only `guard-trace` `WRONG` was `.git/index`, which `TOOL-dGroundRules-38` removes.
- AC4 — `derive_guardable_reads` staged to call `git-no-such-program-36` — the AC1 command printed `policy-fixture: guard-trace · WRONG: git check-ignore did not run: [WinError 2] The system cannot find the file specified, so no read was joined to the guard`, naming `check-ignore`; a direct call with a top outside any repository raised `git check-ignore exited 128: fatal: not a git repository`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: probe.pyc planted, *.pyc out of .gitignore -> `guard-trace · WRONG probe.pyc · not under the policy fixtures guard`; ignore restored -> `1 ignored read(s) set aside`, `223 assertion(s) executed · 0 wrong`.

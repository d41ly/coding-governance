# TOOL-dGroundRules-2 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-2

No merge bar, no gate leg and no self-test suite ran in this pass, apart from the lexicon's
`--suggest`, which the builder role may run. The two fixture cases were observed by a scratch probe
that imports `check_policy` and calls `run_reader_landed("reader-landed")` and
`run_reader_parsed("reader-parsed")` in process. Each case builds its repositories under the system
temp directory and runs `policy.py get` in them as a subprocess. Each case was also run against a
scratch copy of the kit with one break staged in the copy's `policy.py`, and each one went red. The
`policy fixtures` and `policy check` legs, and the red-first observation for each `New arm:` line,
are left for the close.

The cost section 5 left UNVERIFIED was measured in process over this worktree on this Windows host.
A `resolve` at `--rev HEAD` took 91 ms per call over 10 calls, and one at the landed revision took
183 ms, because it also runs the remote ladder's git calls. Both include loading the catalogue.
Section 5's estimate was tens of milliseconds, so the real cost is several times that. No consumer
calls the reader in a loop.

Section 4 says every git call runs with git's location variables removed. Only an in-process probe
observed that: with `GIT_DIR` exported to a nonexistent repository, `derive_landed_revision` still
read this worktree's landed sha, and `GIT_DIR` was restored afterwards. No fixture case asserts it.
The bug-class checklist selected `rule-stated-with-no-check-that-fails`, and adding a
`git-dir-exported` scenario to `reader-landed` was the fix. The session's scratch-guard refused
that edit because the unit was already CLOSED, so the arm is still owed.

**Evidences:** TOOL-dGroundRules-2
- AC1 — `reader-landed` — `get budgets.enforce` printed `warn`, `--rev HEAD` printed `refuse`.
  This is the `remote` scenario: a bare remote whose `main` sets `warn` and `3`, and a clone with
  an unpushed commit and a working-tree edit, both setting `refuse`. In that clone, `--explain`
  printed the line below, where `0b092b49` is the clone's `refs/remotes/upstream/main`:
  `policy: budgets.enforce · file · set in .governance/policy.toml at 0b092b49, upstream/main, the landed revision`
  Staged break (with no `--rev`, the copy reads local HEAD): `get budgets.enforce` printed
  `refuse`, and the case printed `WRONG` on 5 of its 11 lines.
- AC2 — `nosuchrev` — `get budgets.enforce --rev nosuchrev` in the same clone exited 2 and printed
  nothing on stdout. On stderr it printed:
  `policy: refused · .governance/policy.toml:0 · nosuchrev names no commit in this repository`
- AC3 — `reader-parsed` — the plant whose first line is `touch <marker>` exited 2 with:
  `policy: refused · .governance/policy.toml:1 · not TOML at c034ab8f: Expected '=' after a key in a key/value pair (at line 1, column 7)`
  The plant whose comments carry `$(touch <marker>)` and a backticked `touch` printed `warn`. The
  case printed `the marker does not exist` and `0 wrong`. Staged break (the copy's `resolve` runs
  the text through a resolved bash): the case printed `WRONG: the marker exists`.
- AC4 — `not a catalogue key` — `get runtime.agents-in-flite` in AC1's clone exited 2 with:
  `policy: refused · <the kit's absolute path>/catalogue.toml:0 · runtime.agents-in-flite is not a catalogue key`
  `get budgets.` exited 2 with `"budgets." is not one TOML key`, and `get runtime.agents-in-flight`
  printed `3`. Staged break (`read_catalogue_row` answers a row it does not match): the unknown key
  was refused as `is not set` instead, and the case printed `WRONG` on 1 of its 11 lines.
- AC5 — `GOV_REMOTE` — with `GOV_REMOTE` unset, `get budgets.enforce` exited 2 carrying the ladder's text.
  This is the `two-remote` scenario: two fetched remotes and no upstream. The refusal ended:
  `this repository has 2 remotes (mirror upstream). Name it: export GOV_REMOTE=<remote>.`
  With `GOV_REMOTE=mirror` it printed `refuse`, the second remote's value. The first remote holds
  `warn`.
- AC6 — `local main` — `get budgets.enforce` printed `warn`, and `--explain` printed `local main` and `no remote`.
  This is the `no-remote` scenario: local `main` commits `warn` and the working tree sets `refuse`.
  The `--explain` line ended `at 5cb21cd8, local main: this clone has no remote`.
- AC7 — `grep -c 'git remote'` — over `policy.py` printed `1`, and `grep -c '^def resolve_remote'` printed `1`.
  The one `git remote` match is `derive_landed_revision`'s docstring, which names `resolve_remote`
  as the module's one remote read. A probe stubbed `policy.resolve_remote` to return a refusal.
  `derive_landed_revision(".")` then raised a `Refusal` carrying its text:
  `policy: refused · .governance/policy.toml:0 · STUBBED LADDER REFUSAL TEXT`
- AC8 — `grep -c tomllib` — printed `0` for each of the four files. The four files are
  `tools/unattended/unattended.sh`, `.githooks/pre-push`, `tools/push-main.sh` and
  `tools/run-gates/post-merge.sh`. At the build commit `39ab8431a`, `git diff HEAD~1 HEAD --` over
  the same four paths printed 0 bytes.
- AC9 — `policy.py get` — `grep -n 'policy.py get'` over `policy.md` under `help/` printed lines 8 and 24.
  `grep -n 'policy.md' help/README.md` printed line 7.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: (1) --fixture reader-landed: read_revision reads local HEAD in place of derive_landed_revision -> 5 of 11 lines WRONG (e.g. `remote · get budgets.enforce · WRONG: exit 0`, two-remote `WRONG: exit 2`), reds AC1 AC5 AC6; AC2 AC4 stay green; GREEN 11 lines none WRONG. (2) --fixture reader-parsed: text run through bash -> `marker · no line of either file ran · WRONG: the marker exists`; GREEN `the marker does not exist`. Single-case runs exit 1 on the guard-trace "no source read was traced" line at HEAD too (not a case line).

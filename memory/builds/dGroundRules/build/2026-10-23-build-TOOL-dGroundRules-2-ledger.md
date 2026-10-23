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

**Evidences:** TOOL-dGroundRules-2
- AC1 — `reader-landed` — the `remote` scenario built a bare remote whose `main` sets `warn` and
  `3`, and a clone with an unpushed commit and a working-tree edit, both setting `refuse`. In the
  clone, `get budgets.enforce` printed `warn`, `--rev HEAD` printed `refuse`, and `--explain` printed
  `policy: budgets.enforce · file · set in .governance/policy.toml at 0b092b49, upstream/main, the
  landed revision`, where `0b092b49` is the clone's `refs/remotes/upstream/main`. Staged break
  (no `--rev` reads local HEAD): `get budgets.enforce` printed `refuse`, and the case printed
  `WRONG` on 5 lines.
- AC2 — `nosuchrev` — the same clone's `get budgets.enforce --rev nosuchrev` exited 2, printed nothing
  on stdout, and printed `policy: refused · .governance/policy.toml:0 · nosuchrev names no commit in
  this repository` on stderr.
- AC3 — `reader-parsed` — the plant whose first line is `touch <marker>` exited 2 with `policy:
  refused · .governance/policy.toml:1 · not TOML at c034ab8f: Expected '=' after a key in a
  key/value pair (at line 1, column 7)`. The plant whose comments carry `$(touch <marker>)` and a
  backticked `touch` printed `warn`. The case printed `the marker does not exist` and `0 wrong`.
  Staged break (the copy's `resolve` runs the text with a resolved bash): it printed `WRONG: the
  marker exists`.
- AC4 — `not a catalogue key` — in AC1's clone, `get runtime.agents-in-flite` exited 2 with
  `policy: refused · <the kit's absolute path>/catalogue.toml:0 · runtime.agents-in-flite is not a
  catalogue key`. `get budgets.` exited 2 with `"budgets." is not one TOML key`.
  `get runtime.agents-in-flight` printed `3`. Staged break (`read_catalogue_row` answers a row it
  does not match): the unknown key was refused as `is not set` instead, and the case printed `WRONG`.
- AC5 — `GOV_REMOTE` — the `two-remote` scenario has two fetched remotes and no upstream. With
  `GOV_REMOTE` unset, `get budgets.enforce` exited 2 carrying the ladder's text
  `... this repository has 2 remotes (mirror upstream). Name it: export GOV_REMOTE=<remote>.` With
  `GOV_REMOTE=mirror` it printed `refuse`, the second remote's value; the first remote holds `warn`.
- AC6 — `local main` — the `no-remote` scenario has local `main` committing `warn` and a working
  tree setting `refuse`. There, `get budgets.enforce` printed `warn`, and `--explain` printed `... at
  5cb21cd8, local main: this clone has no remote`.
- AC7 — `grep -c 'git remote'` — over `policy.py`, `grep -c '^def resolve_remote'` printed `1` and
  `grep -c 'git remote'` printed `1`. The one match is `derive_landed_revision`'s docstring, which
  names `resolve_remote` as the module's one `git remote` read. A probe stubbed
  `policy.resolve_remote` to return a refusal: `derive_landed_revision(".")` raised a `Refusal`
  carrying its text, `policy: refused · .governance/policy.toml:0 · STUBBED LADDER REFUSAL TEXT`.
- AC8 — `grep -c tomllib` — over `tools/unattended/unattended.sh`, `.githooks/pre-push`,
  `tools/push-main.sh` and `tools/run-gates/post-merge.sh`, `grep -c tomllib` printed `0` for each
  file. Before the commit, `git diff HEAD --` over the same four paths printed 0 bytes, and the commit
  does not stage any of them.
- AC9 — `policy.py get` — `grep -n 'policy.py get'` over `policy.md` under `help/` printed lines 8
  and 24, and `grep -n 'policy.md' help/README.md` printed line 7.

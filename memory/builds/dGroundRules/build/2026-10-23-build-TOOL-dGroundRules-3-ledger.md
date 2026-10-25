# TOOL-dGroundRules-3 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-3

No merge bar, no gate leg and no self-test suite ran in this pass, apart from the naming lexicon,
which the builder role may run and which named no offender in `tools/policy/`. The `resolution-order`
case was observed by a scratch probe that imports `check_policy` and calls
`run_resolution_order("resolution-order")` in process. It builds one repository per scenario under
the system temp directory and runs `policy.py get` in each as a subprocess, at `--rev HEAD`. The
same probe re-ran `reader-landed` and `reader-parsed`, 14 observations and 0 wrong, so removing the
interim refusals moved no reader observation. The `policy fixtures` leg and the red-first
observation for this unit's `New arm:` line are left for the close.

Each staged break below was made in a scratch copy of the kit's `policy.py`, never in the tracked one,
and the case reran over the copy.

**Evidences:** TOOL-dGroundRules-3
- AC1 — `resolution-order` — the `file-sets` scenario plants `budgets.enforce = "refuse"`, and
  `get budgets.enforce --rev HEAD --explain` printed `refuse` with this stderr line:
  `policy: budgets.enforce · file · set in .governance/policy.toml at d4bb6f85, --rev HEAD`
  Staged break (the tuple reordered, default first): it printed `warn`, and `file-sets` and
  `preset-overridden` printed `WRONG`.
- AC2 — `runtime.agents-in-flight` — in the same repository, `get runtime.agents-in-flight --rev HEAD --explain`
  printed `6` with this stderr line:
  `policy: runtime.agents-in-flight · default · not set in .governance/policy.toml at d4bb6f85, --rev HEAD; the catalogue default`
- AC3 — `is absent at` — the `file-absent` scenario commits no policy file, and
  `get budgets.enforce --rev HEAD --explain` printed `warn` with this stderr line:
  `policy: budgets.enforce · default · .governance/policy.toml is absent at fb96c446, --rev HEAD; the catalogue default`
  Staged break (an absent file given the unset reason): `file-absent` printed `WRONG`.
- AC4 — `not applied until dKeptSession` — the `preset-named` scenario plants only `preset = "strict"`,
  and `get budgets.enforce --rev HEAD --explain` printed `warn` with this stderr line:
  `policy: budgets.enforce · default · not set in .governance/policy.toml at 838b09a9, --rev HEAD; the catalogue default; the file names preset strict, not applied until dKeptSession adds presets to this reader`
  The `preset-overridden` scenario adds `budgets.enforce = "refuse"` and printed `refuse`, with the
  source `file`. Staged break (the preset clause removed): `preset-named` printed `WRONG`.
- AC5 — `catalogue.toml` — the `no-default` scenario copies `policy.py` and the catalogue into the
  fixture's own kit directory and removes the `default` line from that copy's `budgets.enforce` row.
  Its policy file sets only `runtime.agents-in-flight`. `get budgets.enforce --rev HEAD`, run from
  the copy, exited 2 with nothing on stdout, and printed on stderr:
  `policy: refused · C:/Users/daily-agent/AppData/Local/Temp/pol-agwjfset/kit/catalogue.toml:0 · the row budgets.enforce carries no default, so budgets.enforce has no value to read`
  Staged break (a missing default read as an invented value): it exited 0 and printed `invented`,
  and `no-default` printed `WRONG`.
- AC6 — `python -c` — importing `policy` from `tools/policy/` and printing
  `[f.__name__ for f in policy.RESOLUTION_ORDER]` printed `['read_file_value', 'read_default_value']`.
  `grep -n RESOLUTION_ORDER` over the kit's Python finds one assignment, at `policy.py:454`, and one
  loop over it, in `resolve`.
- AC7 — `grep -n 'RESOLUTION_ORDER\|catalogue default'` — run over `help/policy.md`, it printed lines
  39, 40, 43, 44 and 46. These are the "Where a value comes from" paragraph, which states the order
  and gives the reason `--explain` prints for the `file` source and for each `default` case.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture resolution-order, RESOLUTION_ORDER = (read_default_value, read_file_value) -> file-sets and preset-overridden `get budgets.enforce --rev HEAD --explain · WRONG: exit 0 · stdout 'warn'` (2 of 6), reds AC1 AC4. GREEN `76 assertion(s) executed · 0 wrong`.

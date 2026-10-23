# TOOL-dGroundRules-4 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-4

No merge bar, gate leg or self-test suite ran in this pass. The one exception is the naming lexicon,
which the builder role may run. It read `P1 verb offenders=1213`, and `--offenders` named `__str__`
and `validate` as the only offenders under `tools/policy`.

The two new outcome cases were observed by a scratch probe. It imports `check_policy` and calls each
case's function in process, `STRICT_FROM` set where the case reads v2. Each case builds its own
repositories under the system temp directory and runs `policy.py get` and `policy.py check` in them
as subprocesses, every read at `--rev HEAD`. The same probe re-ran `reader-landed`, `reader-parsed`
and `resolution-order` over the new `resolve`: 20 observations, 0 wrong. It also re-ran
`adopter-fresh-target`, which printed 2 `WRONG` lines before the first commit: `arm_on_invalid`
reports `HEAD names no commit` there. The spec hands that case to TOOL-dGroundRules-21 (its section 3,
"arm_on_invalid over an unresolved HEAD"), so the `policy fixtures` leg reds on it until that unit
lands.

No staged break was run in this pass. The red-first observation for this unit's three `New arm:`
lines, and the `policy fixtures` and `policy check` legs, are left for the close.

**Evidences:** TOOL-dGroundRules-4
- AC1 — `validate` — a `python -c` probe importing `policy.py` printed
  `[Problem(line=2, key='budgets.enforce', why='"refuze" is not one of ["warn", "refuse"]')]` for
  `enforce = "refuze"`, `[]` for `"warn"`, and `[Problem(line=2, key='', why='Invalid value (at line 2, column 11)')]`
  for `enforce = ` with no value.
- AC2 — `on-invalid-classes` — the `absent` scenario commits no policy file.
  `get budgets.enforce --rev HEAD --explain` printed `warn`, with
  `policy: budgets.enforce · default · .governance/policy.toml is absent at c1347671, --rev HEAD; the catalogue default`,
  and `check --rev HEAD` exited 0, naming the file as absent.
- AC3 — `last-valid` — in the `malformed-after-valid` scenario, V sets `refuse` and C's line 2 is
  `enforce = refuse`. `get budgets.enforce --explain` printed `refuse`, with
  `policy: budgets.enforce · last-valid · .governance/policy.toml at df0b9fbc is invalid, line 2: Invalid value (at line 2, column 11); read from the last valid revision e2d703dd: ...`.
  e2d703dd is V's sha8. `policy.py check` exited 0, printing
  `policy: check · every key falls back to the last valid revision · ...` with V's sha8.
- AC4 — `arm_on_invalid` — the `malformed-alone` scenario commits one malformed revision.
  `get budgets.enforce` and `check` each exited 2 with
  `policy: refused · .governance/policy.toml:2 · Invalid value (at line 2, column 11); no valid revision of the file precedes 54fe6ed5`.
  `arm_on_invalid` over that repository reported 1 finding, `.governance/policy.toml:2`, and 0
  findings once a valid file was committed on top. Over this worktree it reported 0 findings,
  `.governance/policy.toml at a5e02684 is valid`.
- AC5 — `runtime.agents-in-flight` — the `missing-key` scenario's valid file sets only
  `budgets.enforce`, and `get runtime.agents-in-flight --explain` printed `6` with source `default`,
  `not set in .governance/policy.toml at 603caf23, --rev HEAD; the catalogue default`.
- AC6 — `refuze` — in the `out-of-set` scenario, C sets `enforce = "refuze"` and `agents-in-flight = 3`.
  `get budgets.enforce` printed `refuse` with source `last-valid`, its reason naming `line 2` and V's
  sha8 ed177976. `get runtime.agents-in-flight` printed `6` with source `last-valid` and
  `not set in .governance/policy.toml at ed177976 ...; the catalogue default`.
- AC7 — `policy-file.on-invalid` — in the `refuse-then-malformed` scenario, V sets `refuse` and C is
  malformed. `get budgets.enforce` and `check` each exited 2 with
  `policy: refused · .governance/policy.toml:2 · Invalid value (at line 2, column 11); policy-file.on-invalid is refuse at 9523c5e0`.
- AC8 — `"never"` — in the `on-invalid-out-of-set` scenario, V sets `refuse` and C sets `"never"`.
  `get budgets.enforce`, `get policy-file.on-invalid` and `check` each exited 2 at line 2,
  `policy-file.on-invalid: "never" is not one of ["last-valid", "refuse"]; policy-file.on-invalid is refuse at 9523c5e0`.
  In `on-invalid-out-of-set-unset`, V sets only `enforce = "refuse"` and C sets `enforce = "warn"`
  and `"never"`. `get budgets.enforce` printed V's `refuse` with source `last-valid`, the problem
  named at line 5.
- AC9 — `--strict-from` — with `STRICT_FROM` set to `memory/builds/dClosedLoop/build/`, the
  `on-invalid-strict` case named the one file it read and printed
  `246 strict cell(s) in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md · population 111 key(s), 135 excluded`.
  It then printed each of the 135 excluded keys with why, the dotted prefixes among them `leases`,
  `review.build`, `review.design` and `verdict`. Its last line was
  `each of the 111 key(s) read strict's value from last-valid at the malformed revision`,
  113 assertions with 0 wrong, in 27.5 s. The count was derived at observation, 2026-10-24.
  Given a scratch directory under `%TEMP%` holding no such file directly (one sat in a subdirectory),
  the case printed `WRONG: ... holds 0 file(s) whose name ends -architecture-v2.md, not one: (none)`.
  Given one holding two, it printed `... holds 2 file(s) ... not one: a-architecture-v2.md, b-architecture-v2.md`.
  A directory that does not exist read as 0, red too. With no `STRICT_FROM`, the case printed
  `NOT RUN · no --strict-from <dir> names the directory holding v2's architecture record, ...` with 0
  assertions.
- AC10 — `python -c` — loading `tools/gate-legs.json` printed `policy check | guard: (absent)` and
  `policy fixtures | ... argv: ['python', '{prefix}/policy/check_policy.py', '--fixture', '--strict-from', 'memory/builds/dClosedLoop/build/']`.
  The search of every row's `argv` and `guard` strings, over 144 rows, for `[A-Z]+-[a-zA-Z]+-[0-9]+`
  printed nothing.
- AC11 — `agents-in-flite` — in the `unknown-key` scenario, V sets `refuse` and C sets `enforce = "warn"`
  and `[runtime]` `agents-in-flite = 3`. `get budgets.enforce --explain` printed `refuse` with
  `policy: budgets.enforce · last-valid · .governance/policy.toml at 368ad911 is invalid, line 5: runtime.agents-in-flite: no catalogue row matches this key; read from the last valid revision ed177976: ...`.
- AC12 — `grep -n 'on-invalid'` — run over the help page, it printed line 52, the "When the file is
  invalid" paragraph, and line 89, the key's table row. `grep -n 'policy.py check'` printed line 63,
  the "Check the committed file" paragraph.

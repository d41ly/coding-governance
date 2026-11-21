# KICK-dKeptSession-2 — acceptance ledger

**Serves:** journal KICK-dKeptSession-2

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` case ran in this
pass. The `policy fixtures` leg and the other legs the spec's section 7 names were not run as
commands. The criteria were observed on win32 at the pass's base `c2c9d3d6` by probes of the unit's
own code: `policy.py get --explain` and `policy.py mirror --print` run as commands in scratch
repositories under `%TEMP%`, each a one-commit repository read at `--rev HEAD` with the policy text
the criterion names; a scratch copy of the kit holding `policy.py`, `budgets.py`, `presets.py`,
`catalogue.toml` and `caps.toml` and no `presets.toml`; an in-process probe script over
`policy.read_revision` and `policy.resolve_read` that reads what `preset-every-key` reads, outside
the fixture; and the `grep` commands the criteria spell. Each new name, `read_preset_value`,
`read_kit_presets`, `read_preset_assignment`, `derive_declared_presets`, `run_preset_every_key` and
the nested `read_outcome`, was passed by `lexicon.py --suggest --as py.function`, and
`python tools/lexicon/lexicon.py` exited 0.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` run of
`resolution-order` and of the new `preset-every-key` case among them; and the RED-first observation
of the `New arm:` line in `tools/policy/check_policy.py`, `preset-every-key`, the rewritten
`preset-named` and `preset-overridden`, `preset-declared` and `preset-store-absent`, on its staged
break, `read_preset_value` dropped from `RESOLUTION_ORDER` in a copy of the kit, and green once
restored.

**Evidences:** KICK-dKeptSession-2
- AC1 — `get hooks.bypass --rev HEAD --explain` in a repository whose file sets only `preset =
  "strict"`: exit 0, `refused` on stdout, `policy: hooks.bypass · preset · preset strict at
  <sha8>, --rev HEAD` on stderr.
- AC2 — the same read where the file adds `[hooks]` `bypass = "allowed"`: exit 0, `allowed`, source
  `file`, `set in .governance/policy.toml at <sha8>, --rev HEAD`.
- AC3 — the in-process probe printed, for each of `velocity`, `standard`, `strict` and `guarded`,
  246 assigned key(s) of which 246 read from `preset` at the preset's value (DERIVED from each
  preset's assignment at c2c9d3d6), and 25 `never` key(s) but `preset` of which 25 read as the
  absent file reads them (DERIVED from the store's `never` list at c2c9d3d6), placeholder segments
  read at `fixture`. `get review.max-rounds` under `velocity` printed `2` from `preset`. Its red side,
  the same probe with `RESOLUTION_ORDER` set in process to the file and the default steps alone: each
  preset read 0 of 246 assigned key(s) from `preset` (DERIVED, that probe), the first wrong
  `charter.override` reading `explicit-override` from `default`.
- AC4 — `get runtime.agents-in-flight` in a repository whose file sets only `[budgets]` `enforce =
  "refuse"`: exit 0, `6` from `default`, `not set in .governance/policy.toml at <sha8>, --rev HEAD;
  the catalogue default`, no preset clause.
- AC5 — in a repository whose file declares `[presets.ours]` with `extends = "strict"` and
  `"hooks.bypass" = "allowed"` and sets `preset = "ours"`: `get hooks.bypass --explain` printed
  `allowed`, `preset · preset ours at <sha8>, --rev HEAD`; `get leases --explain` printed `refuse`,
  `preset · preset ours at <sha8>, --rev HEAD`. `derive_declared_presets` over `parse_policy`'s
  leaves of a table adding an unquoted `leases.granularity = "unit"` returned it re-nested,
  `{'ours': {'extends': 'strict', 'hooks.bypass': 'allowed', 'leases': {'granularity': 'unit'}}}`.
- AC6 — `grep -rn "until dKeptSession" tools/policy/ help/policy.md` printed nothing, exit 1.
- AC7 — `grep -n "preset" policy.md` in `help/` printed line 69, the order's bullet naming the value
  the file sets, then the preset the file names, then the catalogue default, and lines 72 and 73,
  the `preset` and `default` reasons.
- AC8 — `mirror --print` in the `strict`-named repository: its `hooks.bypass` entry read `{'reason':
  'preset strict at {rev}', 'source': 'preset', 'value': 'refused'}`.
- AC9 — the scratch kit copy carrying `presets.py` and no `presets.toml`, run as `policy.py get
  hooks.bypass --rev HEAD` in the `strict`-named repository: exit 2, an empty stdout (`wc -c` 0, DERIVED, that run), one stderr
  line opening `policy: refused ·`, naming the kit copy's `presets.toml` at line zero and saying the preset store does
  not read (No such file or directory), no traceback, the refusal re-raised across the `__main__` module. With `presets.py`
  removed from that copy too, a file naming no preset read `budgets.enforce` as before, and the
  `strict`-named file refused with one line naming `presets.py`.

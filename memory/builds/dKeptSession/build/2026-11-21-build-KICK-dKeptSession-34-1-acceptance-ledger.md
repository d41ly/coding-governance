# KICK-dKeptSession-34 — acceptance ledger

**Serves:** journal KICK-dKeptSession-34

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` run ran in this
pass. The `policy fixtures` leg and the other legs the spec's section 7 names were not run as
commands. The criteria were observed on win32 at the pass's base `66b51be7` by in-process probes of
the unit's own code: `run_preset_every_key` and `run_preset_derived_cap` called from a `python -c`
script in `tools/policy/`, each building its own scratch repositories under `%TEMP%` as the case
does, with `GOV_REMOTE`, `GOV_DEFAULT_BRANCH` and the `GIT_*` variables unset as `run_fixture` unsets
them. The one new name, `run_preset_derived_cap`, is a `run_` verb the lexicon declares, and
`python tools/lexicon/lexicon.py` exited 0.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` run of
`preset-every-key` and of the new `preset-derived-cap` case among them; and the RED-first
observation of the `New arm:` line in `tools/policy/check_policy.py`, `preset-every-key`'s third
class and `preset-derived-cap`, on its staged break, a copy of the step answering a value for an
unassigned row, and green once restored. That break reaches `preset-derived-cap` only through a
kit copy, since `budgets.py` runs as its own process.

**Evidences:** KICK-dKeptSession-34
- AC1 — `run_preset_every_key` printed one line per preset, `velocity`, `standard`, `strict` and
  `guarded`, each reading 246 assigned key(s) from the preset (DERIVED from each preset's
  assignment at 66b51be7), 25 never key(s) as the absent file (DERIVED from the store's `never`
  list less `preset` at 66b51be7) and 7 unassigned derived row(s) refused as the absent file
  (DERIVED from `derive_derived_rows` at 66b51be7: the six rows `presets.py check` names unassigned
  and `review.<stage>` read at `review.fixture`, a key no preset holds), every read as wanted, and
  returned 4 assertions with 0 wrong (DERIVED, that probe). The unassigned rows read the absent
  file's refusal, type `DerivedDefault` and reason, `budgets.*` read at the census's first cap as
  one quoted segment.
- AC1, red side — the same probe with `RESOLUTION_ORDER` set in process to a copy of the step that
  answers the value 7 from `preset` (PINNED 2026-11-21, the staged value) for an unassigned derived
  row outside `never`: every preset's line read WRONG, the first naming `roles.effort.fixture`
  read from `preset`, the absent file's `DerivedDefault` refusal beside it; 4 assertions, 4 wrong
  (DERIVED, that probe). With `runtime.agents-in-flight` dropped in process from the store's `never`
  list, every preset's line read WRONG naming the preset and that key, unassigned and neither a
  never key nor a derived row; 4 assertions, 4 wrong (DERIVED, that probe).
- AC2 — `run_preset_derived_cap` picked `guide-bytes`, the census's first `switch` row that is no
  family and whose home is not `limits:` (DERIVED from `caps.toml` at 66b51be7). With an empty
  policy file `budgets.py resolve --explain guide-bytes` exited 0 with the one row
  `guide-bytes\t-\twarn\tnone` (PINNED 2026-11-21, the spec's figure, matched) and the stderr line
  `budgets: guide-bytes · budgets.enforce is warn · budgets.guide-bytes has no value: ...`; under
  `preset = "strict"` it exited 0 with `guide-bytes\t-\trefuse\tnone` and the line `budgets:
  guide-bytes · budgets.enforce is refuse · ...`. The two rows' value and source are `-` and `none`
  each; 3 assertions, 0 wrong (DERIVED, that probe).

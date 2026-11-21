# KICK-dKeptSession-33 — acceptance ledger

**Serves:** journal KICK-dKeptSession-33

No merge bar, no self-test suite and no gate leg ran in this pass. The `policy check`, `policy
fixtures`, `lexicon naming predicates`, `memory hygiene`, `spec tokens` and the other legs the
spec's section 7 names were not run as commands. The criteria were observed on win32 at the pass's
base `df316539` by probes of the unit's own code: `presets.py check` and `presets.py load` run as
commands in the policy kit; the spec's `python -c` probe over `derive_preset_assignment`; the unit's
own case run as `python check_policy.py --fixture presets-derived`; `run_arm(ARM["arm_presets"])`
called in process over gov's tree; `check_presets` and `check_repo_presets` called in process over
edited copies of the parsed store; and the `grep` commands the criteria spell. Each new name,
`derive_derived_rows`, `derive_literal` and `run_presets_derived`, was passed by `lexicon.py
--suggest --as py.function`.

Owed to the close: every leg the spec's section 7 names; the `policy fixtures` run of
`presets-complete`, `presets-pairs`, `presets-repo` and `presets-core-only`, whose shared plant runner
`check_store_plant` now names a place of the store's own lists where a plant's preset is None; and the
RED-first observation of the `New arm:` line, the `presets-derived` case's four plants in
`tools/policy/check_policy.py`, on its staged break and green once restored.

**Evidences:** KICK-dKeptSession-33
- AC1 — `python presets.py check` — in the policy kit, exit 0 printing `velocity`, `standard`,
  `strict` and `guarded`, each `241 of 241 presettable key(s)`, then `presets: check · unassigned ·
  6 derived row(s) · roles.effort.<role>, roles.effort.<workflow>.<stage>, roles.effort.default,
  roles.model.<role>.<harness>, review.<stage>.effort, budgets.*`, then `check · green · 0
  finding(s)` (241 DERIVED at df316539 plus this pass). Its red side, in process: `check_presets`
  over a copy with `velocity`'s `maintain.fixes` deleted returned one finding, `preset.velocity ·
  maintain.fixes`, `lacks this presettable key`.
- AC2 — `python check_policy.py --fixture presets-derived` — exit 0, 8 checks of the case, 0 wrong:
  `budget-cap` named `preset.strict · budgets."coding-governance-agents.template.md"`, `not a
  presettable key: its row's default is derived`; `derived-text` named `preset.velocity ·
  maintain.fixes`, the derived text `is the row's derived default text, not a value`; `stage-cut`
  named `preset.guarded · review.test`, `lacks this key, which preset velocity assigns`;
  `literal-widened` named `literal · hooks.bypass`, naming no catalogue row whose default is derived
  and that the never list lacks; each copy put back read `0 finding(s)`, its load halves `not graded · the loop
  kit does not resolve`. In process, `run_arm(ARM["arm_presets"], <repository root>, KIT)` answered
  `0 finding(s) · 4 preset(s), 241 presettable key(s) each · by-key half 4 load(s) · row-named half 0
  refused pair(s) graded`, and `check_repo_presets` over a `[presets.ours]` table extending `strict`
  admitted `maintain.fixes = ["reap"]` and refused `"budgets.foo" = 3`, `not a presettable key`.
- AC3 — the spec's probe — printed `['reap', 'regenerate stale'] owed`; with `standard` it printed
  the six fixes `['reap', 'prune landed', 'regenerate stale', 'defer dormant', 'records-only fixes',
  'close finished run records'] opt-in`. `python presets.py load strict` exited 0 printing `presets:
  load strict · loaded · 246 key(s)`; `velocity`, `standard` and `guarded` each loaded 246 key(s).
  Its red side, in process: `standard`'s `maintain.fixes` set to `["reap"]` returned one finding,
  `is not the row's default` naming the six members; `standard`'s `review.design` set to `owed`
  returned none, the §8 F3 relaxation.
- AC4 — `grep -n "maintain.fixes" policy.md` in `help/` printed line 135 of the Presets section,
  naming `maintain.fixes` with the six review stage keys from `review.plan`; `grep -n
  "literal" README.md` in the policy kit printed line 35, the `presets.toml` row naming the `literal`
  list.

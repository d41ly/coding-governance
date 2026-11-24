# KICK-dKeptSession-1 — acceptance ledger

**Serves:** journal KICK-dKeptSession-1

No merge bar, no self-test suite and no gate leg ran in this pass. The `policy check`, `policy
fixtures`, `loop guard fixtures`, `loop factories fixtures`, `loop review bounds fixtures`, `docs`,
`core kinds` and `help reference pages` legs were not run as commands. The criteria were observed on
win32 at the pass's base `022a28ab` by probes of the unit's own code: `python -c` calls importing
`policy`, `presets`, `check_policy`, `factories` and `docs_leg` from their kits' directories; the
four `presets-*` case functions and `run_arm` called in process, their scratch repositories under a
short temp directory; `factories.run_fixture` called in process for the two preset plants over one
`build_source_snapshot` clone of the working tree; `presets.py check`, `presets.py load` and `guard.py
--expansion` run as commands; and the `grep` commands the criteria spell. The committing pass
re-applied that change at `e3c71b84`, whose `tools/` and `help/` trees equal `022a28ab`'s, and
re-observed AC1, AC4 and AC5's `validate` half, AC8, AC9, AC11 and AC12 there by the same probes,
each reading as recorded below; AC2, AC3, AC6, AC7 and AC10 stand on the first observation.

Owed to the close: every leg the spec's section 7 names; AC5's two `review_bounds.py --fixture`
plants, `count-above` and `no-driver`, which this pass did not touch; AC13's installed `--check`
lines in `adopter-fresh-target`, which installs through the deployer; and the RED-first observation
of both `New arm:` lines, the four `presets-*` cases and `adopter-fresh-target`'s halves check in
`tools/policy/check_policy.py`, and the `preset-new` and `preset-from-unknown` plants in
`tools/loop/factories.py`.

**Evidences:** KICK-dKeptSession-1
- AC1 — `python presets.py check` — in the policy kit, exit 0 printing `velocity`, `standard`,
  `strict` and `guarded`, each `239 of 239 presettable key(s)`, then `check · green · 0 finding(s)`.
- AC2 — `presets-complete` — `run_presets_complete` returned 8 checks, 0 wrong: `key-cut` named
  `preset.strict · hooks.bypass` lacking the key, `value-refused` `preset.guarded · hooks.bypass`
  with `"maybe"`, `default-moved` `preset.standard · leases.expiry-hours` with 25 off the default 24,
  `fifth-table` `preset.extra · preset` the `of` lacks; each copy put back read `0 finding(s)`, its
  load halves `not graded · the loop kit does not resolve`.
- AC3 — `presets-pairs` — the `velocity-pair` plant named `preset.velocity ·
  review.design.round-count`, 5 above `review.max-rounds` 2 under preset velocity; unplanted green.
- AC4 — `presets-pairs` — `presets.py check` over the planted copy exited 1 with that finding; the
  file whose one revision is `preset = "standard"` and `review.design.round-count = 4` read `policy:
  check · .governance/policy.toml at <sha> is valid`, exit 0. `validate` over that text in process
  returned no problem.
- AC5 — `presets-repo` — `extends-strict` exit 0 `is valid`; `extends-lax` exit 2 naming
  `presets.ours.extends` at line 4 and no valid revision; `never-key` exit 2 naming
  `presets.ours."policy-file.guard"`, a key presets never touch. In process, `validate` over a file
  declaring `[presets.ours]` beside a copy of `policy.py`, `budgets.py`, the catalogue and the census
  with no `presets.py` returned one problem, key `presets`, naming `presets.py`; the same copy
  admitted `preset = "strict"` with no table. The two `review_bounds.py` plants are owed.
- AC6 — `presets-core-only` — over the register copy without `point.flow.release`, `load standard`
  exited 0 `loaded · 239 key(s)`, `load strict` exited 2 with one refusal naming `build.closes`,
  `after-release-verifies` and `point.flow.release`; unplanted `arm_presets` read `0 finding(s)`,
  `by-key half 4 load(s) · row-named half 2 refused pair(s) graded`.
- AC7 — `presets-core-only` — `absent-by-key` named `preset.standard · build.closes`; `accept-all`
  named `preset.strict · build.closes`, the rule refusing and the load admitting.
- AC8 — `grep -n -A2 '^key = "build.closes"' loop.toml` — printed lines 2331 to 2333, the value
  `after-release-verifies` and the point `point.flow.release`.
- AC9 — `policy-check: arm_presets · 0 finding(s)` — `run_arm(ARM["arm_presets"], <repository
  root>, KIT)`, the call `python check_policy.py --repo .` makes per arm, answered `0 finding(s) · 4
  preset(s), 239 presettable key(s) each · by-key half 4 load(s) · row-named half 0 refused pair(s)
  graded`, then the row-named half's `presets-core-only · not graded` line, `TOOL-dDeclaredLoop-2
  S8 admits after-release-verifies`. The four `presets.py load` commands over the shipped register
  each printed `loaded · 239 key(s)`. The command itself, the `policy check` leg's, is owed.
- AC10 — `preset-new` — the factory exited 0, its gate `arm_presets` green over 5 presets, wrote
  `presets.toml` and `catalogue.toml`; `core.py kinds` printed `17 registered, 4 pending` and green;
  the case printed `gate green · kind.preset off the pending list`. `preset-from-unknown` exited 2
  naming `'nope'`, porcelain clean.
- AC11 — `grep -n "never touch\|pair rule\|core-only" policy.md` — printed help lines 124, 130 and
  152, one in each of the presets section's three paragraphs; `grep -c 'policy/presets.py#'
  usage.toml` printed 2. In process, the page's two `presets.py` commands checked `tested` against
  their rows, and both anchors carry the rows' fingerprints, `daa13502` and `8cba698f`. The
  factory's own row, `script:{prefix}/loop/factories.py#preset`, joined at the committing pass, its
  `help/loop.md` anchor carrying the fingerprint `docs_leg.py --fingerprints` printed, `50dec72b`.
- AC12 — `guard.py --expansion` — fed `build.closes="after-release-verifies"` exit 0 with no line;
  fed `x` exit 2 printing `loop-guard: refused · stdin:1 · "x" is not <key>=<toml value>`.
- AC13 — `extract_arm_rows` — over the README, its names equal `ARMS` in order, `arm_presets` opening
  `finding`, each row's word equal to its arm's `empty`. The installed `--check` is owed.
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `presets-complete`: the store check answers no finding
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `presets-pairs`: the pair rule answers no finding
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `presets-repo`: the preset half of a policy file answers no problem
- seen-red — `policy fixtures` — red `f6a0d7aaf` — green `f6a0d7aaf` — `presets-core-only`: no preset is loaded
- seen-red — `loop factories fixtures` — red `45016a2c4` — green `45016a2c4` — `preset-from-unknown`: an unknown `--from` not refused before the write
- seen-red — `loop factories fixtures` — red `45016a2c4` — green `45016a2c4` — `preset-new`: the factory leaves the catalogue row without the name

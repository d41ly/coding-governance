# KICK-dKeptSession-20 — acceptance ledger

**Serves:** journal KICK-dKeptSession-20

This pass built the scenario's preset slot at the base `3c3ce4f1` on win32: the `preset` and
`overrides` fields of the scenario schema, `derive_slot_policy`, `check_scenario_policy` and the
`slots` verb in `tools/loop/scenario.py`, the `slot` and `pairs` verbs in `tools/policy/presets.py`,
and `read_scenario_value` with the `build` keyword and `get --build` in `tools/policy/policy.py`. No
merge bar, no self-test suite and no gate leg ran in this pass: `scenario.py check --selftest`, the
`loop scenario fixtures` leg, was not run, nor any leg the spec's section 7 names. Each plant below
was run alone as the unit's own CLI, `python tools/loop/scenario.py --fixture --plant <case>`, over
the scratch `build_scenario_base` builds under the host temp directory and removes after.

Owed to the close: every leg the spec's section 7 names; the `loop scenario fixtures` leg's wall time
before and after the three plants, against its declared ceiling in `tools/gate-legs.json`, which AC1's
cost line asks the builder to record and which only that leg's run can measure; and the RED-first
observation of the `New arm:` line over `tools/loop/scenario.py`, the plants staged red by a
`RESOLUTION_ORDER` without `read_scenario_value` and a `run_check` without `check_scenario_policy`.

**Evidences:** KICK-dKeptSession-20
- AC1 — `--plant slot-builds` exited 0 (DERIVED, that run) and closed `loop: fixture · slot-builds ·
  held`. Both moves out of `none` recorded. `get hooks.bypass --build tFix --explain` exited 0
  printing `refused`, its explain line giving source `preset` and the reason `scenario
  scenario.adopter.strict-slot preset strict` at the scratch's sha; the same read for `tFix2` printed
  `allowed` with source `preset` and a reason naming `scenario.adopter.velocity-slot preset velocity`;
  and `get review.max-rounds --build tFix2` printed `2` (DERIVED, that run), velocity's value where
  the file's own preset, standard, holds 3 (DERIVED, a `derive_preset_assignment` probe over
  `presets.toml`). The plant ran in 10 seconds of wall time (DERIVED, `time` over that run).
- AC2 — in the same run `get hooks.bypass --explain` with no `--build`, and with `--build tNone`, each
  exited 0 printing `allowed` with source `preset` and the reason `preset standard`, the file's own
  preset.
- AC3 — in the same run, once the plant committed `[hooks]` `bypass = "allowed"` beside `preset =
  "standard"`, `get hooks.bypass --build tFix --explain` printed `allowed` with source `file`.
- AC4 — `--plant slot-refused` exited 0 (DERIVED, that run) and closed `held`: the scratch's
  `scenario.py check` exited 1 (DERIVED, that run) printing `loop: refused ·
  scenario.adopter.never-key · runtime.agents-in-flight · a key presets never touch`. The plant ran in
  3 seconds of wall time (DERIVED, `time` over that run).
- AC5 — the same `check` printed a refusal naming `scenario.adopter.pair-break` and
  `review.design.round-count`, its reason reading that `review.design.round-count` 4 is above
  `review.max-rounds` 2 under that scenario and that the pair rule holds `review.max-rounds` at or
  above `review.design.round-count` (DERIVED, that run). `python tools/loop/scenario.py check` over
  this tree, whose pack carries no slot, exited 0 printing `loop: scenarios composed · 5 scenario(s) ·
  0 repository` (DERIVED, that run).
- AC6 — `--plant slot-conflict` exited 0 (DERIVED, that run) and closed `held`: with `tFix` moved out
  of `none` under `precision=high` and `pace=fast` and no policy file, `get hooks.bypass --build tFix`
  exited 2 (DERIVED, that run) with one refusal line naming `scenario.adopter.strict-slot`,
  `scenario.adopter.velocity-slot` and the slot's preset under `flow.scenario-conflict = refuse`;
  once the plant committed `scenario-conflict = "declared-order"` under `[flow]` the same read with
  `--explain` exited 0 printing `allowed`, the reason naming `scenario.adopter.velocity-slot preset
  velocity`, the later scenario. The plant ran in 8 seconds of wall time (DERIVED, `time` over that
  run).
- AC7 — `help/policy.md`'s "Where a value comes from" bullet names the four sources in the order the
  file, a build's scenario, the preset and the default, and shows `python tools/policy/policy.py get
  <key> --build <slug>`; `help/loop.md`'s "Your own scenario" paragraph carries the slot's sentence
  naming `preset` and `overrides`; the loop kit README's scenario section lists `preset` and
  `overrides` among the schema's seven fields (DERIVED, `scenario-schema.toml`'s `[[field]]` rows);
  and the `policy.py#get` row of `tools/govkit/usage.toml` holds `--build=`, the page's `get` anchor
  carrying the row's new fingerprint `f4d25789` (DERIVED, `docs_leg.derive_usage_fingerprint` over
  the row with `{prefix}` read as `tools`, the same probe reproducing the old anchor `af650e87`).
- §8 F4 probe — `policy.read_revision('.', 'HEAD', build='tFix')` with the loop kit's lookup made to
  miss raised a Refusal whose reason carries the lookup's own; with no build the read's `build` is
  None.
- Verb probes — over an empty scratch directory, `presets.py slot` exited 1 (DERIVED, that probe) with
  one refusal per bad override key: a key presets never touch, a key no catalogue row matches and a
  value `check_value` refuses; a preset outside the shipped names exited 1 (DERIVED, that probe); and
  `pairs` over non-JSON stdin exited 2 (DERIVED, that probe).
- Naming — `python tools/lexicon/lexicon.py` exited 0 (DERIVED, that run) with its P1 offender count
  unchanged from the base's run.
- seen-red — `loop scenario fixtures` — red `45016a2c4` — green `45016a2c4` — `slot-builds`: the read order without `read_scenario_value`
- seen-red — `loop scenario fixtures` — red `f6a0d7aaf` — green `f6a0d7aaf` — `slot-refused`: a key presets never touch read unchecked
- seen-red — `loop scenario fixtures` — red `45016a2c4` — green `45016a2c4` — `slot-conflict`: the read order without `read_scenario_value`

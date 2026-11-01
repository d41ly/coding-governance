# TOOL-dTendedCadence-18 — five gateable drift signals as core legs, the reading tree, and the remote-CI reading's liveness

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 6 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0499@2480b868 whole
**Carries:** node:policy-key.maintain.reading-tree
**Carries:** node:policy-key.maintain.dead-after

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 |
| [2026-11-01-build-TOOL-dTendedCadence-18-deviation-181.md](../build/2026-11-01-build-TOOL-dTendedCadence-18-deviation-181.md) | deviation | — |
| [2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md) | research | TOOL-dTendedCadence-5 TOOL-dTendedCadence-7 TOOL-dTendedCadence-12 TOOL-dTendedCadence-17 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 |
| [2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-1 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 |

<!-- /gen:spec-records -->

## 1. Goal

Five drift signals decide whether a change may merge, yet the core bar reaches them only through the
observability kit's `drift-audit records` leg (`tools/gate-legs.json:1052-1068`), so a core leg depends
on an expansion (gap-maint-09). A reading also varies with the tree it is taken in (gap-maint-10), and
the remote-CI signal is dead on a node without `gh` and is never asked under `--check`
(gap-maint-11). This unit moves `ledger_rows` to a memory leg, `non_terminal_specs` and `closed_specs`
to a flow leg, and `handkept` and `cutoff_keys_armed` to an instruction leg, each at Test's leg-pack
point through one extracted signal-leg factory; takes repo-scoped readings as `maintain.reading-tree`
says, in a clean checkout at the base SHA or in the node's worktree; and registers the remote-CI
reading with its liveness, dead past `maintain.dead-after` readings and filed to its source.

## 2. Scope (IN)

Build-run preconditions, each an ancestor's spec built before this build run: TOOL-dDeclaredLoop-1 S1
(the loop kit `tools/loop/`, `layer = "layer.flow"`); TOOL-dWitnessedBar-11 S1-S3 and S8
(`leg_factory.py new`, `[[gate_leg]]` rows, packs), PLAY-dOrderedCharter-19 S12 (the `pack` key) and
TOOL-dWitnessedBar-28 S10 (the slot line `slot point.flow.leg-pack · filled`); TOOL-dWitnessedBar-13
S1-S2 (the ledger factory block `legacy_ledger_py`, `[[ledger]]`), -14 (the `ratchet` pack's `never
gains` over every `shrink-only` and `ceiling` population) and -16 S8 (`drift-pins.txt`,
`drift-baselines.txt`); and, in this build, TOOL-dTendedCadence-8 (the `[[reading]]` rows),
TOOL-dTendedCadence-4 (`derive_reading_owner`, `read_policy_value`) and TOOL-dTendedCadence-14 (the
`band` field).

- **S1** — The factory, I12 as this unit settles it: the canonical block `# >>> signal_leg_py` in
  `tools/lib/signal_leg.py`, carried inline by every module that runs a moved signal and by
  `drift_report.py`, and held to its canonical by a `PARITY_ROWS` row
  `signal_leg_py|$ROOT/$KIT_REL/signal_leg.py|$KIT_REL/signal_leg` in
  `tools/lib/resolve-python.test.sh` (`:168-187`), the route `tools/lib/` contents take into
  copy-installed kits. It holds two halves (§4 "The block"):
  - the judge, `run_signal_leg(signals, bounds)`: `signals` a list of I4 records, `bounds` a dict from
    signal name to an integer ceiling or a set of offender ids, a name it lacks taking the record's own
    `tolerance`. It prints `<signal> <value> of <of> · ok` or `· over` for a live record, an `over`
    id-set record followed by one `  new <id>` or `  stale <id>` line per moved id,
    `<signal> · not asked: <why>` and `<signal> · dead probe: <why>`, and returns 1 when a gateable
    record is over or dead, 2 when a record has neither a bound nor a tolerance, 0 otherwise; and
    `render_signal_offenders(signals, bounds)`, the `<signal>\t<detail key>` keys of I5 for exactly the
    records `run_signal_leg` reds, moved out of `render_drift_offenders` (`drift_report.py:3985-4020`)
    with `derive_row_identity` (`:3746`) and `extract_unlocated` (`:3734`);
  - the context the moved bodies run in, moved verbatim from `drift_report.py`: `Git` (`:460-479`),
    `load_conf` (`:122`), `parse_conf_text` (`:149`), and the id grammar's ladder `_resolve_ident`,
    `_read_families` and `_build_local_ident` (`:588-700`).

  `render_drift_offenders` keeps its name and calls the block for the over and dead keys, adding its
  ratchet keys. Observed by AC1, AC2, AC3 and AC6.
- **S2** — The five moved, each body verbatim but for the context it reads, its signal name unchanged
  (I4), into the home §8 F1 settles, in drift-audit's record shape:

  | Signal | Body at this base | Home module, function | Bound | Pack |
  |---|---|---|---|---|
  | `ledger_rows_contradicting_git` | `signal_ledger`, `drift_report.py:506` | `tools/memory-tree/memory_signals.py`, `measure_ledger_rows` | tolerance 0 | `memory` |
  | `non_terminal_specs_cited_by_product_source` | `signal_spec_status`, `:713` | `tools/loop/flow_signals.py`, `measure_spec_citations` | the id set | `flow` |
  | `closed_specs_with_no_product_commit` | `signal_closed_specs_untraceable`, `:1038` | `tools/loop/flow_signals.py`, `measure_untraceable_specs` | the id set | `flow` |
  | `handkept_inventories_disagreeing_with_source` | `signal_handkept`, `:884` | `tools/playbook/instruction_signals.py`, `measure_handkept` | tolerance 0 | `instruction` |
  | `cutoff_keys_armed` | `build_cutoff_keys_armed`, `:2158` | `tools/playbook/instruction_signals.py`, `build_cutoff_keys_armed` | its ceiling row | `instruction` |

  Each module runs as `python <module> [--offenders] [--selftest]`, prints through `run_signal_leg`
  and exits as it returns; `--offenders` prints `render_signal_offenders`'s keys and exits the same;
  `--selftest` runs the arms S9 moves. `ledger_rows_contradicting_git` reads `not asked: no in-flight
  ledger` when `<memory root>/project/in-flight/` is absent, where at this base it reads dead and
  `DECLARED_EMPTY` excuses it (`drift_signals.py:149-160`; §8 F3). `cutoff_keys_armed` stays gateable
  only where a ceiling row bounds it, as at `drift_report.py:2174`. Observed by AC1, AC2, AC3.
- **S3** — The bounds, each in its home as a ledger population registered by a `[[ledger]]` table in
  that kit's `kit.toml` (TOOL-dWitnessedBar-13 S2), so the `ratchet` pack's `never gains` holds each
  against its base (TOOL-dWitnessedBar-14):
  - `flow-signal-baselines`, `shrink-only`, key `signal` · `id`, home `tools/loop/flow-signal-baselines.txt`,
    seeded with the three ids of `BASELINES` at this base (`drift_signals.py:373-406`):
    `TOOL-aBatchedLintel-1`, `TOOL-dNarrowedAnchor-1`, `TOOL-aMooredAnchor-1`;
  - `instruction-signal-pins`, `ceiling`, key `signal`, home `tools/playbook/instruction-signal-pins.txt`,
    seeded `cutoff_keys_armed` at 36 (`drift_signals.py:351`).

  `handkept` and `ledger_rows` keep tolerance 0, which a ledger count cannot hold. The drift-audit rows
  of the five leave `drift-pins.txt` and `drift-baselines.txt` in the same commit. Observed by AC2 and AC3.
- **S4** — The declarations each moved body reads leave drift-audit's project layer:
  - `handkept`'s population becomes data, a `[[handkept]]` table in any kit's `kit.toml`: `record` (a path
    from that kit's directory), `heading` (the heading whose table's first-column backticked names are
    the claim set) and `source` (a table of that same descriptor whose rows' `name` values are the
    source set). `read_handkept_inventories(root)` in `instruction_signals.py` reads every installed
    kit's descriptor beside it with `tomllib`; drift-audit declares the one row `HANDKEPT` holds today
    (`drift_signals.py:233-236`), its README's `## The signals` table against its `[[reading]]` names
    (§8 F2). No kit declaring a row reads `not asked: no kit declares a hand-kept inventory`;
  - the flow signals' declarations, `PRODUCT_GLOBS`, `EVIDENCE_GLOBS`, `TRACE_CUTOFF`, `TRACE_GLOBS`
    and `TRACE_WAIVER` (`drift_signals.py:28-110`), move with their values, gov's `EVIDENCE_GLOBS` still
    built on `PRODUCT_GLOBS` (`:95`), to the loop kit's project layer `tools/loop/flow_layer.py`,
    `project-owned`, seeded from `tools/loop/flow_layer.template.py` as drift-audit seeds its own
    (`tools/drift-audit/kit.toml:42-49`). drift-audit's one remaining reader of `PRODUCT_GLOBS`,
    `--escape-ratio` (`drift_report.py:4308`), reads it from that layer through the inline
    `resolve_kit_dir`, an expansion reading a core kit's declaration, so the list is spelled once. The
    three holes naming them leave drift-audit's descriptor (`kit.toml:102-124`) for the loop kit's, as
    `flow-product-globs`, `flow-trace-cutoff` and `flow-evidence-globs`.

  **Readers:** by name: `tools/drift-audit/drift_report.py` (`load_project_layer`'s required names,
  `:198`; `Ctx`, `:3555-3575`, `:3587-3588`; `main`'s hand-kept ordering, `:4316-4320`; `:4308`),
  `tools/drift-audit/drift_signals.py` (`:23-110`, `:149-160`, `:215-236`, `:277`, `:351`, `:373-406`,
  `:451-452`, `:459`), `tools/drift-audit/drift_signals.template.py` (`:14`, `:33-37`, `:93-115`),
  `tools/drift-audit/kit.toml` (`:102-124`), `tools/drift-audit/selftest.py`, `tools/drift-audit/README.md`
  (`:85`, `:103`, `:124-129`, `:146`, `:252`), `tools/drift-audit/SKILL.template.md` with its render
  `.claude/skills/drift-audit/SKILL.md`, `memory/project/trace-waiver.txt` (its comment at `:2`), each
  found by `git grep` for the names at base · by value: `signal_shrink_only`'s `RATCHETS` reader, which
  loses the `handkept` and `cutoff_keys_armed` rows (`drift_signals.py:451-452`, `:459`), and
  `--check`'s `BASELINES` stray-key refusal (`drift_report.py:4332-4337`), which loses its two keys.
  Observed by AC3 and AC4.
- **S5** — The legs. Six `[[gate_leg]]` rows through `leg_factory.py new`, each `subject = "repo"` and
  carrying its pack, the slot line `slot point.flow.leg-pack · filled` announcing the point (I13):
  `memory drift signals` and `memory drift signals selftest` in `tools/memory-tree/kit.toml`, `pack =
  "memory"`; `flow drift signals` and `flow drift signals selftest` in `tools/loop/kit.toml`, `pack =
  "flow"`; `instruction drift signals` and `instruction drift signals selftest` in
  `tools/playbook/kit.toml`, `pack = "instruction"`. Each signals leg's `argv` runs its module,
  `signature` adds `--offenders`, `history_depth = "full"` as the records leg's (`kit.toml:95-100`),
  and its fallback row carries `chunk = "declarations"` and `ceiling = 540`, PINNED from the records leg
  (`tools/gate-legs.json:1066-1067`) until `measure_legs.py` reads it; each selftest leg runs
  `--selftest`, guarded by its module and its population file. `tools/gate-legs.json` is their render.
  Observed by AC5.
- **S6** — `drift-audit records` stays (§8 F4), its `--check` no longer reaching the five: `SIGNALS`
  (`drift_report.py:3521-3538`) holds none of them, their bodies leave the module, and the leg keeps
  grading what remains: the ratchet and language-mode findings (`:4360-4363`), any gateable signal still
  there (the lexicon's until TOOL-dMindYourWords-16 moves them) and admission (TOOL-dTendedCadence-4).
  The five `[[reading]]` rows TOOL-dTendedCadence-8 wrote leave `tools/drift-audit/kit.toml`, since a
  leg's witness is not a reading (layer-expansions:191-195).
  **Readers:** by name: `tools/drift-audit/drift_report.py` (`SIGNALS`, `:506-712`, `:713-831`,
  `:884-940`, `:1038-1185`, `:2158-2182`), `tools/memory-tree/gen_build_index.py` (`read_landed_unclosed`,
  `:1929-1965`, which calls `signal_spec_status` through drift-audit's `Ctx`), `.lexicon.conf` (`:11`,
  `signal_ledger` named as an example of leading tokens) and the generated
  `memory/map/generated/symbols.json`, re-rendered · by value: `read_landed_unclosed`, re-pointed to
  `measure_spec_citations` in the loop kit's `flow_signals.py` with its `evidence_files` check kept
  (`:1960-1964`); the `drift-audit records` leg, whose verdict no longer reads the five.
  Observed by AC4 and AC9.
- **S7** — The reading tree, I14 as this unit settles it: `resolve_reading_tree(root, base_sha, mode)`
  in `drift_report.py`, a context manager yielding the root repo-scoped readings are taken in. Under
  `clean-base` it adds a detached worktree of `base_sha` with the argv `add_scratch_worktree` runs
  (`git worktree add --detach <path> <sha>`, `tools/run-gates/lib-attribute.sh:59`) at
  `<git-common-dir>/maintain-read/<sha12>`, under the common dir as that helper's comment places one
  (`:56-58`), and takes it down on exit with the argv `remove_scratch_worktree` runs (`:63`), printing
  the path when it cannot; under `worktree` it yields `root`. `base_sha` is `resolve_base_ref`'s sha
  (`drift_report.py:3667`). The mode
  is `read_policy_value("maintain.reading-tree", root)`; its `PolicyRefused` takes `worktree`, the
  behaviour before this unit, printed once. Observed by AC7.
- **S8** — The reading pass and its liveness. `python drift_report.py --readings`, the call the Maintain
  walk makes (TOOL-dTendedCadence-1 S4): repo-scoped readings run as the base's own engine,
  `<tree>/<kit rel>/drift_report.py --json`, inside the tree S7 yields, and node-scoped ones in place;
  it is never offline, so `remote_ci_red_streak` is asked (`:3391-3393`); each record carries `tree`,
  `clean-base <sha8>` or `worktree`; and it appends the history rows `--check` appends
  (`write_drift_history`, `:3794`), their `sha` the tree the repo-scoped readings were taken at. The
  remote-CI row of `[[reading]]` declares `live = "gh"`, the command its liveness needs. A record dead
  for at least `maintain.dead-after` readings, the streak `derive_dead_streaks` counts (`:3882`), takes
  the band `dead` (TOOL-dTendedCadence-14 S3) and `file_to`, the layer `derive_reading_owner` derives
  for its row, the source TOOL-dTendedCadence-15 files it to; its status reads `DEAD PROBE for <k>
  readings — past maintain.dead-after <n>, its source <owner>`. The limit is
  `read_policy_value("maintain.dead-after", root)`; its `PolicyRefused` judges no streak and the
  `# dead-for-N:` header says `limit not read: <why>`. Observed by AC7 and AC8.
  **Readers:** `DEFAULT_DEAD_READINGS_LIMIT` and the project key `DEAD_READINGS_LIMIT` it defaults are
  replaced by `maintain.dead-after` · by name: `tools/drift-audit/drift_report.py` (`:3863`,
  `:3866-3880`, `:4285`), `tools/drift-audit/drift_signals.template.py` (`:182-190`),
  `tools/drift-audit/README.md` (`:172`), `tools/drift-audit/selftest.py` (`:487`, `:3917`) · by value:
  the status branch `k >= dead_limit` (`drift_report.py:4410`) and the `# dead-for-N:` header
  (`:4391`), which read the policy value. `DEAD_FILED` stays, for TOOL-dTendedCadence-15.
- **S9** — The arms. drift-audit's arms over the five (`tools/drift-audit/selftest.py`, each
  `read_one_signal` call naming one) move to their home modules' `--selftest`; drift-audit's suite gains
  the reading-tree and dead-after arms. Observed by AC1, AC2, AC3, AC7, AC8.
- **S10** — The two catalogue rows, `maintain.reading-tree` and `maintain.dead-after`
  (`tools/policy/catalogue.toml:1145-1149`, `:1163-1167`), gain their `summary` and `usage`, values and
  defaults unchanged, and `policy.py lists --write` drains both from
  `tools/policy/unsummarised-keys.txt` (`:112`, `:120`). Observed by AC10.
- **S11** — The docs: `help/maintain.md` gains a section "The reading tree and liveness" naming both keys,
  `--readings` and the `dead` band; the drift-audit README's signal table points at the three legs for
  the five; the memory-tree, loop and playbook READMEs each name their leg. Observed by AC11.

## 3. Non-goals (OUT)

- The lexicon's three signals: TOOL-dMindYourWords-16, re-pointed at S1's factory by ask TOOL-dTendedCadence-26.
- Filing a dead reading or an over-pin offender: TOOL-dTendedCadence-15 (`maintain.file`).
- The leg factory, the `pack` key, the ledger factory and the `ratchet` pack: their parents, called.
- `DEAD_FILED`, retired by the unit that files dead readings, TOOL-dTendedCadence-15.
- Ageing a dead streak per period rather than per SHA: the history counts one reading per SHA
  (`drift_report.py:3882-3885`), so a repository with no landing ages no streak; that rule stays.
- The `shrink_only_lists_not_shrinking` signal and every report-only reading: they stay readings.

### Edges

- **consumes-from** `TOOL-dTendedCadence-8` — `[[reading]]`, the rows S6 takes the five out of and whose `live` field S8 sets on the remote-CI row
- **consumes-from** `TOOL-dTendedCadence-4` — `derive_reading_owner`, the source S8 names for a dead reading, and `read_policy_value`
- **hands-off** `TOOL-dTendedCadence-7` — `run_signal_leg`, the factory its leg prints through, and `maintain.reading-tree`, the tree its repo half reads
- **hands-off** `TOOL-dTendedCadence-15` — `run_signal_leg`, the factory its red leg prints through; a reading dead past its limit reaches its filing with the source it is filed to
- **hands-off** `TOOL-dTendedCadence-5` — `maintain.reading-tree`, the tree its repo-scoped reading is taken in
- **hands-off** `TOOL-dTendedCadence-12` — `maintain.reading-tree`, the tree its repo-scoped reading is taken in
- **hands-off** `TOOL-dTendedCadence-16` — `maintain.reading-tree`, the tree its readings sit beside, node-scoped ones read in place
- **hands-off** `TOOL-dTendedCadence-1` — `maintain.reading-tree`, through the reading pass the walk calls, and the liveness that makes a reading `dead`
- **consumes-from** external — TOOL-dDeclaredLoop-1 S1, TOOL-dWitnessedBar-11, -13, -14, -16 and -28 S10, PLAY-dOrderedCharter-19 S12, each specced and unbuilt at base; TOOL-dMindYourWords-16, not an ancestor, re-pointed by ask TOOL-dTendedCadence-26
- **hands-off** `TOOL-dTendedCadence-42` — the move of `PRODUCT_GLOBS`, whose two missed adopter instructions that unit redirects (review id 31)
- **hands-off** `TOOL-dTendedCadence-46` — `resolve_reading_tree`, the scratch tree that unit's disposal probe runs in (review id 43)
- **hands-off** `TOOL-dTendedCadence-48` — the signal table's moved rows, the shared scratch-tree helper and its path, the carriers row, the legs' dossiers and the manifest re-stamp, which the minors batch repairs (review ids 18, 29, 35, 36, 37, 47)

## 4. Design

### Evidence

The five are the gateable signals drift-audit computes for itself, each `"gateable": True` or gated by
its pin (`drift_report.py:544`, `:762`, `:926`, `:1177`, `:2174-2177`), reached by `--check`
(`:4364-4366`) through the leg `drift-audit records` (`tools/gate-legs.json:1052-1068`). The design
draws the line: a signal that decides a position is a core witness, and each of the five moves to the
layer whose records it grades (layer-expansions:189-195). TOOL-dMindYourWords-16 makes the same move
for the lexicon's signals; this is the kind's second instance, so the charter's reuse rule extracts the
factory (the spec brief's settled 6). Repeated readings at one (head, base, signal) differed in 14 of
108 groups (gap-maint-10), which `drift-history.tsv` can measure because it keeps `base_sha` (`:3758`).
The remote-CI signal is not asked under `--check` or `--offenders` (`:3391-3393`), and reads dead with
no `gh` (`:3343-3344`).

### The block

```
tools/lib/signal_leg.py      # >>> signal_leg_py ... # <<< signal_leg_py
  judge:    run_signal_leg(signals, bounds) -> 0 | 1 | 2
            render_signal_offenders(signals, bounds) -> [<signal>\t<key>]
            derive_row_identity, extract_unlocated
  context:  Git, load_conf, parse_conf_text, _resolve_ident, _read_families, _build_local_ident
carried inline by: drift_report.py, memory_signals.py, flow_signals.py, instruction_signals.py
```

The ratchet half of today's judge leaves rather than moves: a raised ceiling row or a gained
id is the `ratchet` pack's `never gains` (TOOL-dWitnessedBar-14), so the block applies the bound and
never the raise. That narrows I12, which was proposed as applying `RATCHETS` too.

### The pass

```
--readings ── maintain.reading-tree ──┬─ clean-base: worktree add --detach <common>/maintain-read/<sha12> <base>
                                      │              <tree>/…/drift_report.py --json   (repo rows)
                                      └─ worktree:   in place                          (repo rows)
            node rows in place ── merge by row scope ── history rows ── dead streak ≥ maintain.dead-after → band dead
```

### Inventory

Names this unit mints, each asked of `lexicon.py --suggest <name> --as py.function` at this base and
answered OK: `run_signal_leg`, `render_signal_offenders`, `measure_ledger_rows`,
`measure_spec_citations`, `measure_untraceable_specs`, `measure_handkept`, `read_handkept_inventories`,
`resolve_reading_tree`; `build_cutoff_keys_armed` keeps its conforming name. Modules:
`signal_leg.py`, `memory_signals.py`, `flow_signals.py`, `instruction_signals.py`, `flow_layer.py`;
the `py.file` cell is undeclared at this base. Block: `signal_leg_py`. Row kind: `[[handkept]]`.
Populations: `flow-signal-baselines`, `instruction-signal-pins`. Legs: the six of S5. Holes:
`flow-product-globs`, `flow-trace-cutoff`, `flow-evidence-globs`. Record fields: `tree`, `file_to`. CLI mode: `--readings`.

### Migration

gov's values move verbatim: the five flow declarations to `tools/loop/flow_layer.py`, the three ids
and the ceiling of 36 to their populations, the README row to drift-audit's `[[handkept]]` table. An
adopter's update seeds `flow_layer.py` from its existing `drift_signals.py` where that file declares
the five names, through the loop kit's adopter, so no adopter's flow signals go unasked on update.

### Rollout

One commit moves each signal, its bound, its declarations, its arms and its leg together, so no bar
runs with a signal in both places or in neither.

### Files touched (estimate)

- `tools/lib/signal_leg.py` (new)
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/memory_signals.py` (new)
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/README.md`
- `tools/loop/flow_signals.py` (new)
- `tools/loop/flow_layer.template.py` (new)
- `tools/loop/flow_layer.py` (new, gov's project layer)
- `tools/loop/flow-signal-baselines.txt` (new)
- `tools/loop/kit.toml`
- `tools/loop/adopt-loop.sh`
- `tools/loop/README.md`
- `tools/playbook/instruction_signals.py` (new)
- `tools/playbook/instruction-signal-pins.txt` (new)
- `tools/playbook/kit.toml`
- `tools/playbook/README.md`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/drift-pins.txt`
- `tools/drift-audit/drift-baselines.txt`
- `tools/drift-audit/kit.toml`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/drift-audit/SKILL.template.md` (rendered to `.claude/skills/drift-audit/SKILL.md`)
- `tools/gate-legs.json` (rendered by `leg_factory.py --write`)
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt` (rendered by `policy.py lists --write`)
- `memory/project/trace-waiver.txt`
- `memory/map/features/playbook.md`
- `memory/map/generated/` (re-rendered by `gen_map.py --write`)
- `.lexicon.conf`
- `help/maintain.md`

### Alternatives rejected

- **A third copy of the move, each module with its own judge.** Rejected by the charter's reuse rule at
  the kind's second instance (settled 6).
- **The bounds left in drift-audit's `drift-pins.txt`.** Rejected: a core leg reading an expansion's file
  is the dependency gap-maint-09 names, and a pin in a kit that no longer computes its signal is a value
  nothing reads (TOOL-dMindYourWords-16 §4 "Alternatives rejected").
- **The reading tree inside the running engine, its own signals over a scratch root.** Rejected: the
  engine's project layer and kit code then come from the node's tree, not the base, so a reading at a
  SHA does not reproduce, the property the history's own comment says node-local state lacks
  (`drift_report.py:3860-3862`).
- **Declared-empty kept for `ledger_rows`.** Rejected by §8 F3: an absent ledger is derivable, and an
  exemption list is a typed fact beside it.

## 5. Production-readiness checklist

- security — the scratch worktree is created under the git common dir from a resolved SHA, never from
  a ref name an input supplies, and removed on every exit path; no network call is added (`gh` was
  already called by the report outside `--check`).
- perf / scale — the three legs each run a subset of what `drift-audit records` ran; `--readings` costs
  one worktree add and one engine run at the base, inside the Maintain walk only.
- error / empty / loading states — no ledger: `not asked`; empty globs: `not asked`; no hand-kept row:
  `not asked`; a worktree that cannot be removed: its path printed; no policy kit: `worktree` and no
  streak judged.
- observability — each leg's lines and keys; `tree` and `file_to` on every `--readings` record.
- risks — the bar loses nothing it graded: each signal keeps its bound and its tolerance, now in its
  home; an adopter without the loop kit has no flow leg until it installs it, where today the two
  signals ran inside drift-audit.
- testing — §7's New arm lines; the fixtures of §6.
- migration — §4 "Migration".
- user docs — `help/maintain.md` and the three home READMEs (S11).

## 6. Acceptance criteria

The move fixture is a clone of this repository at the build commit under `%TEMP%/mv`, its remote
removed so the policy reader and the base ladder read the local default branch, each case committing
its plant there. The tree fixture is the same clone with a branch `side` checked out one commit ahead
of the default branch, whose `memory/LIVE.md` holds 3 `dormant` rows where the default branch's
holds 1. Each command runs with the fixture as its working directory.

- **AC1** — When `python memory_signals.py` runs from `tools/memory-tree/` with a planted in-flight
  ledger file under the memory root's project/in-flight/ whose row claims "not merged" for a landed
  SHA, it prints `ledger_rows_contradicting_git 1 of 1 · over` and exits 1; with the directory absent
  it prints `ledger_rows_contradicting_git · not asked: no in-flight ledger` and exits 0.
  Red when: an open claim on a landed SHA reads `ok`, or an absent ledger reds.
- **AC2** — When `python flow_signals.py` runs from the loop kit's directory on the build commit, it
  prints both flow signals `· ok` and exits 0; after a commit adding a non-terminal spec whose id
  product source cites, it prints `non_terminal_specs_cited_by_product_source` `· over` with one
  `  new <id>` line and exits 1.
  Red when: a new offender reads `ok`, or the baseline's own ids read `over`.
- **AC3** — When `python instruction_signals.py` runs from `tools/playbook/` on the build commit, it
  prints `cutoff_keys_armed 36 of` and `· ok`, and `handkept_inventories_disagreeing_with_source 0 of`;
  after a commit arming one more `_CUTOFF` key in a root conf it prints `cutoff_keys_armed 37 of` and
  `· over` and exits 1; after a commit adding a README signal-table row no `[[reading]]` row names,
  `handkept` reads `· over`.
  Red when: an armed key past the ceiling, or a stale hand-kept row, reads `ok`.
- **AC4** — When `grep -c "def signal_ledger\|def signal_spec_status\|def signal_closed_specs_untraceable\|def signal_handkept\|def build_cutoff_keys_armed" drift_report.py`
  runs in `tools/drift-audit/`, it prints 0, and `python drift_report.py --json` in the move fixture
  lists none of the five signal names.
  Red when: drift-audit still computes one of the five.
  cost: a full report, under the records leg's 540 s ceiling (PINNED, `tools/gate-legs.json:1067`).
- **AC5** — When `grep -n 'pack = "memory"\|pack = "flow"\|pack = "instruction"' kit.toml` runs in each
  of `tools/memory-tree/`, `tools/loop/` and `tools/playbook/`, it finds the two legs of that home, and
  `python leg_factory.py --list` lists all six with their pack.
  Red when: a leg lacks its pack, or a home declares none.
  fixture: needs TOOL-dWitnessedBar-11 built; before it, the grep is the observation.
- **AC6** — When `git grep -l "^# >>> signal_leg_py"` runs, it lists `signal_leg.py` in the shared
  primitives' directory, `drift_report.py` and the three home modules, and `grep -n "signal_leg_py|" resolve-python.test.sh`
  in `tools/lib/` finds the parity row.
  Red when: a module runs a moved signal without the block, or the row is missing.
- **AC7** — When `python tools/drift-audit/drift_report.py --readings` runs in the tree fixture, the
  `live_builds_without_activity` record reads value 1 and `"tree": "clean-base <sha8>"`, the default
  branch's; with `maintain.reading-tree = "worktree"` committed to the default branch it reads 3 and
  `"tree": "worktree"`; and `git worktree list` shows only the fixture afterwards.
  Red when: a clean-base reading takes the node's tree, or leaves its scratch worktree behind.
- **AC8** — When `--readings` runs with `PATH` holding only the directories of `git` and `python`, and
  the history holds k − 1 earlier readings at distinct SHAs with `remote_ci_red_streak` dead, its record
  reads `"band": "dead"` and a `file_to` layer for each k of 5, 10 and 20 under
  `maintain.dead-after` set to k, and with k − 2 earlier readings it does not.
  Red when: the planted node without `gh` is never dead past its limit, or is dead before it.
- **AC9** — When `python tools/drift-audit/drift_report.py --check` runs on the build commit, it exits 0
  and names none of the five on stderr, and `grep -c "signal_spec_status" gen_build_index.py` in
  `tools/memory-tree/` prints 0.
  Red when: the records leg still grades one of the five, or the index still imports drift-audit's body.
  cost: as AC4.
- **AC10** — When `grep -n 'read_policy_value("maintain.reading-tree"\|read_policy_value("maintain.dead-after"' drift_report.py`
  runs in `tools/drift-audit/`, it finds both readers, and `grep -c "^maintain.reading-tree$\|^maintain.dead-after$" unsummarised-keys.txt`
  in `tools/policy/` prints 0.
  Red when: a key has no literal reader or no summary.
- **AC11** — When `grep -n "The reading tree and liveness\|maintain.dead-after" maintain.md` runs in
  `help/`, each matches.
  Red when: the page omits the section or a key.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `policy fixtures` · `tier2-review self-test` · `govkit acceptance matrix` · `playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates` · `straggler-guard arms` · `memory hygiene`

New arm: tools/memory-tree/memory_signals.py · covers AC1 · its `--selftest`, the moved ledger arms with a planted open claim on a landed SHA and an absent ledger, staged against a module that is absent at this base · none
New arm: tools/loop/flow_signals.py · covers AC2 · its `--selftest`, the moved spec-status and traceability arms with a planted new offender against the baseline population, staged against a module that is absent at this base · none
New arm: tools/playbook/instruction_signals.py · covers AC3 · its `--selftest`, the moved cutoff and hand-kept arms with a planted armed key past the ceiling row and a stale table row, staged against a module that is absent at this base · none
New arm: tools/drift-audit/selftest.py · covers AC7 AC8 · the reading-tree arm over a planted reading that differs between the two trees, and the dead-after arm over planted histories at each value of the key, staged against an engine with neither · none
New arm: tools/lib/resolve-python.test.sh · covers AC6 · the `signal_leg_py` parity row, staged by one byte changed in an inline copy · none

## 8. Open questions

- **FACT-QUESTION · F1 — Which kit is each owner's home?** Probe: `grep -n 'layer = "layer.flow"'
  memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-1.md` and the layer table of
  layer-instruction:225-236. Observed: TOOL-dDeclaredLoop-1 S1 specs `tools/loop/` with `layer =
  "layer.flow"`, the core engine the table calls "the loop kit, to be built"; `memory-tree` is Memory's
  core engine and `playbook` Instruction's. Liveness: no specced kit declaring `layer.flow` would leave
  the flow pair homeless, the case the spec brief anticipated. RESOLVED (agent, 2026-11-01, delegated):
  memory to `tools/memory-tree/`, flow to `tools/loop/`, instruction to `tools/playbook/`.
  widens: none · relaxes: none
- **F2 — `handkept` reads drift-audit's own README; what does an instruction leg read?** (a) A
  `[[handkept]]` table any kit declares, drift-audit declaring its README against its `[[reading]]`
  names; (b) the probe function moved, still importing drift-audit's project layer; (c) `handkept` left
  in drift-audit. (b) keeps the core leg depending on the expansion, the gap itself, and (c) fails the
  clause's "`handkept` ... by instruction". Rung 3, the most feature-rich survivor: any kit's hand-kept
  inventory is graded, and with no observability kit the leg reads `not asked`. RESOLVED (agent,
  2026-11-01, delegated): (a). grants: PLAY-dClosedLoop-3 the `[[handkept]]` descriptor table, the clause's
  own move of `handkept` to instruction. widens: none · relaxes: none
- **FACT-QUESTION · F3 — Does `ledger_rows` still need its declared-empty entry?** Probe: `ls
  memory/project/in-flight` at this base and the comment at `drift_signals.py:150-155`. Observed: the
  directory does not exist, and the entry exists only because the probe reads dead when it is absent.
  Liveness: a directory present and empty would still need the entry, and the probe would show it.
  RESOLVED (agent, 2026-11-01, delegated): an absent ledger reads `not asked`, derived, and the entry
  leaves `DECLARED_EMPTY`; a present, empty ledger reads dead. widens: none · relaxes: none
- **F4 — Once `--check` grades none of the five, does `drift-audit records` stay, move or retire?** (a)
  It stays, grading what remains: ratchets, language-mode findings, the lexicon's signals until they
  move, and admission; (b) it retires once the lexicon's signals move too; (c) it moves to a pack. (b)
  leaves admission and the ratchet findings with no leg, and (c) gives an expansion's own declarations
  a core pack. Rung 3, the survivor whose population is never empty. RESOLVED (agent, 2026-11-01,
  delegated): (a); its name, argv and every reader stay. widens: none · relaxes: none
- **F5 — What does a clean-base reading run?** (a) The base's own engine from the scratch checkout;
  (b) the node's engine pointed at the scratch root. (b) reads the node's kit and project layer, so the
  reading is not a function of the base SHA, the property gap-maint-10 measures the lack of. Rung 3.
  RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 42, 46, 48); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: TOOL-dMindYourWords-16 S1-S5, the first instance of this move, whose line grammar
the block keeps; the parity-block route for `tools/lib/` contents (`tools/lib/resolve-python.test.sh:168-241`);
the five bodies, the offender keys and the context they read, moved rather than rewritten
(`drift_report.py:460-479`, `:506`, `:588-700`, `:713`, `:884`, `:1038`, `:2158`, `:3734-3751`,
`:3985-4020`); the ledger factory and the `ratchet` pack for the bounds (TOOL-dWitnessedBar-13, -14);
`add_scratch_worktree`'s argv and placement (`tools/run-gates/lib-attribute.sh:56-59`) and
`resolve_base_ref` (`drift_report.py:3667`) for the tree; `derive_dead_streaks` (`:3882`) and the history
writer (`:3794`) for liveness. The probe `python tools/codebase-map/reuse_lookup.py "move a gateable
drift signal out of the drift engine into its owner kit's gate leg"` returned name stems only (`legs`,
`leg`, `resolve_kit_dir`, `kit_rel`, `DriftError`), none of them a signal-to-leg move, so no existing
seam fits the factory itself and it is extracted over the seams above. Where scout C's record disagrees
with source at this base: it places the records leg at `:1052-1068` (the object opens at `:1052`, its name
at `:1053`), `DECLARED_EMPTY`'s entry at `:156` (`:149-160`), and calls the flow kit "to be built",
which TOOL-dDeclaredLoop-1 S1 has since specced; its `:3521`, `:3863`, `:3882`, `:3384` and
`lib-attribute.sh:59` hold.

Recall terms used: `python tools/memory-recall/query.py "how do drift-audit's gateable signals move to
core legs owned by memory flow and instruction" --terms "gateable drift signal core leg pack ledger_rows
handkept cutoff_keys_armed non_terminal_specs closed_specs reading-tree dead-after gh"`

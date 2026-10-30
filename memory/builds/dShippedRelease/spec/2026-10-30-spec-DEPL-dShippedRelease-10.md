# DEPL-dShippedRelease-10 — the kit factory, its conformance gate, and one version and one wiring verdict

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 1 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0420@7a9716bf whole
**Carries:** node:item.kits.version

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-9-reuse-scout-e.md](../build/2026-10-30-build-DEPL-dShippedRelease-9-reuse-scout-e.md) | research | DEPL-dShippedRelease-9 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

Kit is the last of foundations C3's seventeen kinds with no factory or gate worth the name: 30
descriptors carry 27 top-level keys, nothing validates a key (`gap-tool-07`), and wiring and version
lockstep are each judged several ways (`gap-tool-02`). This unit lands the kit schema, the `new kit`
factory, the core `kit conformance` gate over the whole population, the one version check, the one
wiring verdict, and `item.kits.version`, the row and slot for what `cmd_mint` already does.

## 2. Scope (IN)

- **S1** — The schema, `tools/playbook/kit-schema.toml` (I3): a `[kind]` table with `name = "kit"` and
  one `[[field]]` row per top-level descriptor key, in PLAY-dOrderedCharter-36 S1's grammar, adding
  `type` (`text`, `list`, `table`, `rows` or `bool`) and `required` (`every` or `optional`). It holds
  today's 27 keys and the keys of S2, read through `read_kind_schema`
  (`tools/playbook/row_checks.py`, PLAY-dOrderedCharter-36 S1). No row declares `widens`, so every
  field reads fixed, and the `kind.kit` row carries no `schema` key, so an overlay table naming a kit
  stays refused (PLAY-dOrderedCharter-35 S10). Observed by AC1.
- **S2** — The P28 fields (§8 F3). Two new list keys, `records` (each a `name` of
  `tools/memory-tree/record-kinds.toml`) and `policies` (each a `name` of
  `tools/policy/catalogue.toml`), filled on every descriptor at the pass from the record registry's
  `writer` column and the literal reader census. `layer` and `optional` stay PLAY-dOrderedCharter-16
  S2's; `declares` and `uses` stay on `tools/playbook/layers.toml`'s rows; `units` stays on
  PLAY-dOrderedCharter-9's `instructions.toml`. A third key, `resolves`, lists the sibling homes a
  kit probes and degrades without (§8 F8), and a fourth, `dates`, lists paths outside the kit's claim
  whose moves its version dates (§8 F5). Observed by AC2 and AC5.
- **S3** — The gate. `python tools/playbook/kit_factory.py --conform`, leg `kit conformance`, grades
  every descriptor `check_layers.read_descriptors` returns (PLAY-dOrderedCharter-16 §4), by the arms
  of §4 "The arms", each a red naming the descriptor and key. It runs where govkit is absent, as
  TOOL-dWitnessedBar-45 S3 requires of a shipped verb, and a registry a tree does not hold prints one
  `not graded here` line naming the arm. An empty population refuses. The leg is a `[[gate_leg]]`
  row of `tools/playbook/kit.toml` carrying `enforces` with every tag of the kind's `binds`.
  Observed by AC1, AC2, AC3 and AC5.
- **S4** — The factory. `python tools/playbook/core.py new kit <name> --layer <tag>`, which runs the
  kind row's `factory`, writes `tools/<name>/kit.toml`, a `README.md` carrying the `gov:kit` marker, a
  module holding the version constant, and the `[[entry]]` row of `tools/govkit/registry.toml`. It
  refuses a name that fails `seg` or is taken, and refuses what `--conform` would refuse.
  Observed by AC4.
- **S5** — The kind row. The `kind.kit` row of `tools/playbook/kinds.toml` (PLAY-dOrderedCharter-7
  S4) gains `population`, `factory` and `gate`, and its `kind` row leaves
  `tools/playbook/core-pending.txt`. Observed by AC6.
- **S6** — The readers. `read_kit_rows(root, ids=None)` returns the descriptor rows in install order,
  through `order_by_needs` (TOOL-dDeclaredLoop-12 S5) over each row's `requires`, whose
  `needs_graph_py` inline block `tools/playbook/kit_factory.py` carries, the parity arm finding a copy
  by its marker, so a core reader reaches the order with no govkit. `read_python_floor(root)` returns the one declaration
  `tools/lib/python-floor.txt` through `read_floor` (TOOL-dSafePassage-11 S1), refusing where the
  file is absent or malformed. Observed by AC7 and AC8.
- **S7** — The `none` rule (§8 F4). `version_from = { none = … }` is refused unless the kit ships no
  bytes. Each of the nine surviving entries of §4 "The version constants" gains a constant and a
  `version_from` row. Observed by AC3 and AC9.
- **S8** — The one version check, `python tools/govkit/govkit.py version [--base <rev>]`, leg
  `kit version (one check)`, an `[[exempt_leg]]` row because versions are minted in gov alone.
  `cmd_version` replaces `cmd_epoch` and calls `derive_version_findings`: well-formedness of each entry's value
  (arm 5's rule), every marker against its constant (arm 5c's), the epoch state
  (`derive_epoch_state`, `tools/govkit/govkit.py:13363`), each `dates` path, and the template marker's
  presence and form (`tools/check-placeholders.sh`'s default mode). Observed by AC9 and AC10.
  **Readers:** by name: `tools/govkit/govkit.py` (`cmd_epoch`, the `epoch` dispatch at `:14079`, the
  usage at `:13602`, the comments at `:773`, `:2236`, `:13330`, `:13424`, `:13463`),
  `tools/govkit/selftest.py`, `tools/gate-legs.json`, `tools/govkit/registry.toml`,
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt` · by value: the `epoch:`
  lines of `tools/govkit/selftest.py`, rewritten; `tools/push-main.sh` reads `mint`, which keeps its
  verb and its `derive_epoch_state` call.
- **S9** — The four folded checks go. Leg `kit version markers`, the `check-kit-versions` entry (a
  `[[retired]]` row of `tools/govkit/registry.toml`, successor `none`, TOOL-dSafePassage-1 S2) and
  `tools/check-kit-versions.sh`; leg `verdict epoch (kit version dates the engine)`, its self-test leg,
  and `tools/memory-tree/check-verdict-epoch.sh` with its suite; leg
  `kit epoch (shipped bytes move, the version moves)`; leg `playbook placeholder catalogue` and that
  script's default mode, whose `--check` survival mode stays for the `playbook-placeholders` hole;
  selfcheck arms 5, 5b and 5c.
  Observed by AC9 and AC11.
  **Readers:** by name: `.governance/deploy.toml`, `.memory-tree.conf` (`ARMS_FLOORS`),
  `WIRE-INTO-PROJECT.md`, `tools/check-testsuite-counts.sh`, `tools/drift-audit/README.md`,
  `tools/drift-audit/drift_report.py`, `tools/gate-legs.json`,
  `tools/govkit/entries/check-kit-versions.kit.toml`,
  `tools/govkit/entries/check-placeholders.kit.toml`, `tools/govkit/govkit.py`,
  `tools/govkit/registry.toml`, `tools/govkit/selftest.py`, `tools/govkit/subject-pins.tsv`,
  `tools/memory-recall/recall_conf.py`, `tools/memory-tree/README.md`, `tools/memory-tree/kit.toml`,
  `tools/memory-tree/hygiene-parity.test.sh`, `tools/memory-tree/row_grammar.py`,
  `tools/policy/kit.toml`, `tools/process-monitor/kit.toml`, `tools/run-gates/README.md`,
  `tools/run-gates/ceiling-evidence.txt`, `tools/unattended/check-brief-recorded.sh`,
  `tools/unattended/check-pass-order.sh`, `tools/unattended/check-unattended.sh`,
  `tools/workflows/README.md`, `memory/project/spawn-idiom-sites.txt`,
  `memory/project/substitution-fed-loops.txt`, `memory/project/testsuite-count-waivers.txt`,
  `memory/project/unarmed-branches.txt`, `memory/map/features/memory-tree-hygiene.md`,
  `memory/map/features/govkit.md`, `memory/map/features/lexicon.md`,
  `memory/map/features/testsuite-counts.md`, each by a git grep at the pass · by value: the
  `--closure` verb of `tools/memory-tree/import_walk.py` (PLAY-dOrderedCharter-16 S5), whose one
  caller leaves and which leaves with it while `derive_import_closure` stays for its other reader;
  arm 5b's comparison in `tools/govkit/govkit.py`, which compared gate rows with the registry and has
  no gate left to compare.
- **S10** — The one wiring verdict (§8 F6). `tools/run-gates/kit_wiring.py`, leg
  `kit wiring (every descriptor's check)`, a `[[gate_leg]]` row of `tools/run-gates/kit.toml`, reads every tracked
  descriptor through `regen.read_descriptors`, resolves each `[check]` argv through
  `regen.resolve_argv`, runs the twelve rows and prints one line per kit, red when any row exits
  non-zero. A `[check.gov]` table replaces a row's argv where the tree holds govkit (the `exists:`
  test of TOOL-dWitnessedBar-45 S1), `agent-instructions` carrying `--aliases claude` there.
  Observed by AC12.
  **Readers:** by name: the eleven legs `agent-instructions wiring`, `memory-recall skill wiring`,
  `drift-audit wiring`, `process-monitor wiring`, `runlog skill wiring`, `cleanup skill wiring`,
  `unattended skill wiring`, `run-gates wiring`, `lexicon wiring`, `playbook render wiring` and
  `roles render wiring` retire from `tools/gate-legs.json`, `tools/govkit/subject-pins.tsv`,
  `tools/run-gates/ceiling-evidence.txt`, `tools/agent-instructions/kit.toml`,
  `tools/memory-recall/kit.toml`, `tools/drift-audit/kit.toml`, `tools/process-monitor/kit.toml`,
  `tools/runlog/kit.toml`, `tools/branch-reconcile/kit.toml`, `tools/unattended/kit.toml`,
  `tools/run-gates/kit.toml`, `tools/lexicon/kit.toml`, `tools/playbook/kit.toml`,
  `tools/roles/kit.toml`, with their prose in `tools/branch-reconcile/README.md`,
  `tools/lexicon/README.md`, `tools/lexicon/adopt-lexicon.sh`, `tools/lexicon/selftest.py`,
  `tools/process-monitor/adopt-process-monitor.sh`, `tools/roles/README.md`, `tools/runlog/README.md`,
  `tools/check-wiring.sh`, `.githooks/pre-commit`, `.githooks/pre-commit.test.sh` and six
  `memory/map/features/` dossiers · by value: `tools/govkit/matrix.py:80`, which keys an expected line
  by leg name and re-keys to the new leg, and `tools/govkit/selftest.py` (`:16286-16303`), whose
  planted leg name moves with it.
- **S11** — `item.kits.version` (§8 F9). One `[[item]]` row in `tools/loop/loop.toml`, §4 "The item",
  `actor = "command:kits.version"`, and the point `point.flow.version` added to the `uses` of
  `layer.distribution` in `tools/playbook/layers.toml`. `run_minter` (`tools/push-main.sh:802`) is
  the slot, unchanged but for one sentence: its no-deployer line names the version check rather than
  the push bar's epoch legs, which S9 ends. Observed by AC13.
- **S12** — The docs. A section "The kit factory" in `tools/playbook/README.md`, and a page
  `help/kits.md` with its row in `help/README.md`, stating what `new kit` writes and which legs an
  adopter loses at update. NOT OBSERVED as behaviour: prose.

## 3. Non-goals (OUT)

- `purpose`, `installable`, `why_not_installable`, the `[[inline]]` rows and the `kit.toml` for
  govkit and lib: DEPL-dShippedRelease-21, which adds its rows to this schema.
- The runbook: DEPL-dShippedRelease-9 reads `read_kit_rows`.
- The `integrations` kit: DEPL-dShippedRelease-15 creates it with this factory.
- The rendered-destination check. `check_install_targets` (TOOL-dWellOiledMachine-14) already grades
  a literal `.claude/` in a descriptor; this gate does not repeat it.
- `check-wiring.sh`'s session and class arms and its hook-pack arms: TOOL-dWellOiledMachine-10 builds
  on that script, which stays.
- Moving `layer`, `declares`, `uses` or `units` onto a new home.
- A reverse join of `records` and `policies`: S3 grades that each name resolves, and does not grade
  that a kit lists every key it reads.

### Edges

- **hands-off** `DEPL-dShippedRelease-21` — `kit-schema.toml`, to which that unit adds `purpose`, `installable` and `[[inline]]`
- **hands-off** `DEPL-dShippedRelease-9` — `kit-schema.toml` and `read_kit_rows`, the fields and the order its runbook renders
- **hands-off** `DEPL-dShippedRelease-26` — `kit-schema.toml` and `read_python_floor`, the floor the factory reads for the platform matrix
- **hands-off** `DEPL-dShippedRelease-17` — `read_kit_rows`, the order a fresh install walks
- **hands-off** `DEPL-dShippedRelease-25` — `read_python_floor`, the value the receipt records
- **consumes-from** external — PLAY-dOrderedCharter-7 S4 to S6 (`kinds.toml`, `core.py new`, `core-pending.txt`), PLAY-dOrderedCharter-16 (`check_layers.py`, `layers.toml`, `read_descriptors`), PLAY-dOrderedCharter-36 (`read_kind_schema`), TOOL-dWitnessedBar-11 and -45 (the leg factory, `exists:`), TOOL-dDeclaredLoop-12 (`loop.toml`, `needs_graph.py`), TOOL-dSafePassage-1 (`[[retired]]`), TOOL-dSafePassage-11 (`python-floor.txt`, `read_floor`), TOOL-dTotalRecall-1 (`record-kinds.toml`), each specced and unbuilt at this base, so each is a build-run precondition

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `git ls-files` finds 30 descriptors with 27 top-level keys, PINNED 2026-10-30; `govkit.py` holds no
  known-key set for them.
- Selfcheck arm 5 is `tools/govkit/govkit.py:2119`, 5b `:2164`, 5c `:2222`; `read_descriptors` is
  `:13238` and `regen.read_descriptors` `tools/run-gates/regen.py:108`, which reads `tools/*/kit.toml`
  only.
- `cmd_mint` is `:13497`, reached by `run_minter` (`tools/push-main.sh:802`), whose two announced
  skips are `:805` and `:810`.
- Twelve descriptors declare a `[check]` argv and eighteen declare `none`; eleven of the twelve
  duplicate a leg, and `policy`'s does not, PINNED 2026-10-30.
- `check-verdict-epoch.sh:194`'s `DELEGATES` names one path outside memory-tree's claim,
  `check-spec-tokens.py`, and `$_recall`, which is why `dates` exists (§8 F5).
- A candidate `requires` predicate, `resolve_kit_dir` calls naming another kit's home in a kit's own
  non-test files and absent from `requires` and `requires_if`, finds 21 edges over 10 kits, PINNED at
  `5d1c82ac` by a regex in the run's scratch. The pass re-derives them with
  PLAY-dOrderedCharter-16's `probe` detector.

### The arms

| Arm | Red on | Source |
|---|---|---|
| population | zero descriptors: a refusal, never a green | `[gate]` |
| unknown key | a top-level key no `[[field]]` row names | `gap-tool-07` |
| required | a `required = "every"` field absent | layer-expansions:448 |
| type | a value off its `type` | `gap-tool-07` |
| records | a member with no registry row | layer-expansions:448 |
| policies | a member with no catalogue row | layer-expansions:448 |
| version | `version_from` absent, or `none` on a kit shipping bytes | layer-expansions:449 |
| requires | a `probe` edge to a home named by none of `requires`, `requires_if`, `optional` or `resolves` | research-distribution-b's fifth check |
| resolves | a `resolves` row with no such edge | `[derive]`, both ways |

`layer` and the point joins stay `check_layers.py`'s, and this gate does not re-grade them.

### The schema

```toml
# tools/playbook/kit-schema.toml
[kind]
name = "kit"

[[field]]
name = "version_from"
shape = "scalar"
type = "table"
required = "every"

[[field]]
name = "records"          # each joined to tools/memory-tree/record-kinds.toml
shape = "set"
type = "list"
required = "optional"
```

`check_row_fields(rows, schema, where)` joins `read_kind_schema` in `tools/playbook/row_checks.py`:
the unknown-key, required and type arms, generic over any `[[field]]` file (§8 F2).

### The kind row

```toml
[[kind]]
tag = "kind.kit"
owner = "dShippedRelease"
binds = ["principle.p28", "principle.p16"]   # the row PLAY-dOrderedCharter-7 writes; read, not typed here
population = "python {prefix}/playbook/kit_factory.py --list"
factory = "python {prefix}/playbook/kit_factory.py new"
gate = "kit conformance"
```

### The version constants

| Entry | Carrier | Constant |
|---|---|---|
| `agent-instructions` | `adopt-agent-instructions.sh` | `KIT_AGENT_INSTRUCTIONS_VERSION` |
| `gate-lint` | `sh_hygiene.py` | `KIT_GATE_LINT_VERSION` |
| `check-agent-cap-restatement` | its script | `KIT_CHECK_AGENT_CAP_RESTATEMENT_VERSION` |
| `check-install-prefix` | its script | `KIT_CHECK_INSTALL_PREFIX_VERSION` |
| `check-line-length` | its script | `KIT_CHECK_LINE_LENGTH_VERSION` |
| `check-microformats` | its script | `KIT_CHECK_MICROFORMATS_VERSION` |
| `check-placeholders` | its script | `KIT_CHECK_PLACEHOLDERS_VERSION` |
| `check-testsuite-counts` | its script | `KIT_CHECK_TESTSUITE_COUNTS_VERSION` |
| `push-main` | `push-main.sh` | `KIT_PUSH_MAIN_VERSION` |

Each opens at `1.0`, and `mint` moves it from then on. The tenth entry, `check-kit-versions`, retires.

### The item

```toml
[[item]]
tag = "item.kits.version"
step = "step.test"
actor = "command:kits.version"
needs = ["item.test.merge"]
inputs = ["layer.distribution:the kit descriptors"]
allowance = "the prepared merge's version carriers"
returns = "none"
outcomes = ["minted", "clean", "skipped", "refused"]
witness = { class = "hook-record", by = "the version check's verdict at the push boundary" }
owner = "dShippedRelease"
[item.routes]
minted = "item.test.select"
clean = "item.test.select"
skipped = "item.test.select"
refused = "item.test.merge"
```

`refused` routes to `item.test.merge`, whose own refusal names the minter's, as layer-expansions:456
states. The row owes a count in `step.test`'s table (TOOL-dDeclaredLoop-12 §4), and the `kits.version`
command row of the command kind.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `tools/playbook/kit-schema.toml`, `tools/playbook/kit_factory.py`, `tools/run-gates/kit_wiring.py`, `help/kits.md` | files | none |
| `read_kit_rows`, `read_python_floor`, `check_row_fields`, `read_check_rows`, `cmd_version`, `derive_version_findings` | functions | `py.function`, each OK by `--suggest` at `5d1c82ac` |
| `records`, `policies`, `resolves`, `dates`, `[check.gov]` | descriptor keys | none |
| `kit conformance`, `kit version (one check)`, `kit wiring (every descriptor's check)` | legs | none |
| the nine constants of §4 | constants | `sh.constant` or `py.constant`, screaming |

### Migration

Additive on descriptors; govkit ignores a key it does not read. An adopter's update drops the retired
legs from its manifest and its `check-kit-versions` claim through TOOL-dSafePassage-1 S4's `withdrawn`
arm, and `_cmd_update` reports a file gov has stopped shipping and writes an order
(`tools/govkit/govkit.py:13624`).

### Rollout

Live at landing. The leg set loses sixteen and gains three; each ceiling is measured at the pass.

### Files touched (estimate)

- `tools/playbook/kit-schema.toml` (new), `tools/playbook/kit_factory.py` (new): S1, S3, S4, S6
- `tools/playbook/row_checks.py`: `check_row_fields`
- `tools/playbook/kinds.toml`, `tools/playbook/core-pending.txt`: S5
- `tools/playbook/layers.toml`, `tools/playbook/kit.toml`, `tools/playbook/README.md`: S3, S11, S12
- `tools/run-gates/kit_wiring.py` (new), `tools/run-gates/kit.toml`: S10
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/govkit/registry.toml`,
  `tools/govkit/matrix.py`, `tools/govkit/subject-pins.tsv`: S8, S9, S10
- `tools/check-kit-versions.sh` (removed), `tools/govkit/entries/check-kit-versions.kit.toml`
  (removed), `tools/memory-tree/check-verdict-epoch.sh` (removed),
  `tools/memory-tree/check-verdict-epoch.test.sh` (removed), `tools/check-placeholders.sh`,
  `tools/check-placeholders.test.sh`: S9
- every descriptor under `tools/*/kit.toml` and `tools/govkit/entries/`: S2, S7, S10
- `tools/agent-instructions/adopt-agent-instructions.sh`, `tools/gate-lint/sh_hygiene.py`,
  `tools/check-agent-cap-restatement.sh`, `tools/check-install-prefix.sh`, `tools/check-line-length.sh`,
  `tools/check-microformats.sh`, `tools/check-testsuite-counts.sh`, `tools/push-main.sh`: S7, S11
- `tools/memory-tree/import_walk.py`: S9
- `tools/loop/loop.toml`: S11
- `tools/gate-legs.json`: rendered by `tools/run-gates/leg_factory.py` from the declarations
- `tools/run-gates/ceiling-evidence.txt`, `.memory-tree.conf`, `.governance/deploy.toml`,
  `memory/project/spawn-idiom-sites.txt`, `memory/project/substitution-fed-loops.txt`,
  `memory/project/testsuite-count-waivers.txt`, `memory/project/unarmed-branches.txt`: S9
- `help/kits.md` (new), `help/README.md`, `WIRE-INTO-PROJECT.md`: S12, S9

### Alternatives rejected

- **The gate as more selfcheck arms.** Rejected by PLAY-dOrderedCharter-16's own test: govkit is an
  expansion, so the core's contract would live in the layer it constrains; and `selfcheck` runs
  nowhere an adopter is, which TOOL-dWitnessedBar-45 S3 requires of a shipped gate.
- **A `tools/lib` inline schema block shared by the leg, role and kit kinds.** Rejected by reading the
  three grammars: `role-schema.toml` keys rows on `key` (TOOL-dBoundRoles-2 §4) and the other two on
  `name`, and a third inline primitive for a thirty-line loop costs a parity row per site.
- **A shrink-only ledger for the 21 `requires` edges.** It needs two more inline copies and a
  registration to hold a list that `resolves` states outright.
- **Folding `check-wiring.sh`'s install arms into govkit.** Rejected: govkit never reaches an adopter
  (`tools/govkit/registry.toml:301`), so an adopter's SessionStart would lose its only in-tree report.

## 5. Production-readiness checklist

- security — no new secret, write or egress path: `--conform` reads, `kit_wiring.py` runs the argvs
  the bar's legs ran before it, and `new kit` writes only under the named home and one registry row.
- perf / scale — `--conform` is one pass over 30 descriptors plus a detector walk of tracked kit
  files; `kit wiring` costs the sum of eleven legs it replaces, in one leg.
- error / empty / loading states — an empty population refuses; a missing registry prints `not
  graded here` naming the arm; a `[check]` that cannot resolve a token reds naming the kit.
- observability — one line per kit and per arm, on green and red.
- risks — one leg replaces eleven, so a red's attribution moves to the kit named in its line, and
  the legs' guards go; a wiring failure now costs the whole leg's run. The cost is measured at the
  pass and the ceiling states it.
- testing — the `--fixture --plant` cases of §6 and the arms of §7.
- migration — §4 "Migration".
- user docs — `help/kits.md`.

## 6. Acceptance criteria

- **AC1** — When `python kit_factory.py --conform` runs on the tree it exits 0 and prints the
  descriptor count; with `--fixture --plant unknown-key` it exits 1 naming the key and descriptor,
  and with `--plant missing-required` and `--plant wrong-type` likewise; with `--plant no-descriptors`
  it exits 2.
  Red when: an unvalidated key passes, or an empty population reads green.
  figure: the count is DERIVED; 30 is PINNED at `5d1c82ac`.
- **AC2** — When `--fixture --plant unresolved-record` and `--plant unresolved-policy` run, each exits
  1 naming the member; when the fixture's registries are absent it exits 0 printing `not graded here`
  for each of the two arms.
  Red when: a name no registry holds passes, or a missing registry reds a kit that cannot have it.
- **AC3** — When `--fixture --plant none-version` runs, a descriptor shipping one file under
  `version_from = { none = "x" }`, it exits 1 naming the entry; with a descriptor shipping nothing it
  exits 0.
  Red when: `none` passes on a kit that ships bytes.
- **AC4** — When `python core.py new kit fixture-kit --layer layer.memory` runs in a scratch copy, the
  four files and the registry row exist and `python kit_factory.py --conform` exits 0 there; a second
  run exits non-zero naming the duplicate; `--layer layer.nosuch` exits non-zero.
  Red when: the factory writes a kit its own gate refuses.
  fixture: a scratch copy under `%TEMP%/<short-name>`; the tree holds none.
- **AC5** — When `--fixture --plant undeclared-edge` runs, a kit calling `resolve_kit_dir` on a
  sibling home it names nowhere, it exits 1 naming both; with `--plant stale-resolves` it exits 1
  naming the row.
  Red when: an undeclared sibling edge passes, or a declared one outlives its code.
- **AC6** — When `python core.py kinds` runs it names `kind.kit` with its factory and gate, and
  `grep -c "kind.kit" core-pending.txt` prints 0.
  Red when: the kind stays pending, or the gate leg's `enforces` lacks a `binds` tag.
- **AC7** — When `python kit_factory.py --list` runs it prints `memory-tree` before `memory-recall`;
  with `--fixture --plant requires-cycle` it exits non-zero naming the cycle.
  Red when: the order ignores `requires`, or a cycle falls back to alphabetical.
- **AC8** — When `python -c` calls `read_python_floor` on the tree it returns the bytes of
  `python-floor.txt`; on a fixture whose file holds `3` it exits non-zero naming the file.
  Red when: a second floor is typed, or a malformed value reads as a floor.
  fixture: TOOL-dSafePassage-11's file at the build run's base.
- **AC9** — When `python tools/govkit/govkit.py version` runs on the tree it exits 0; on a scratch
  repository with a shipped byte moved and no bump it exits 1 at `--base` and names the entry; with a
  marker one value behind its constant it exits 1 naming the file; with a malformed constant it exits
  1; with the template marker removed it exits 1.
  Red when: any of the five checks it folds is lost.
- **AC10** — When a scratch repository moves a path a descriptor lists under `dates` with no bump,
  `python tools/govkit/govkit.py version --base <rev>` exits 1 naming that entry.
  Red when: a delegate outside the kit's claim moves a verdict undated.
- **AC11** — When `git grep -c` runs for `kit version markers`, `kit epoch (shipped`,
  `verdict epoch (kit` and `playbook placeholder catalogue` over `tools/gate-legs.json`, each prints 0,
  and `python tools/govkit/govkit.py selfcheck` exits 0; on a fixture receipt claiming `check-kit-versions`,
  `update` carries the claim out through the `[[retired]]` row and exits 0.
  Red when: a retired leg survives, or a receipt naming the entry refuses the update.
- **AC12** — When `python kit_wiring.py` runs on the tree it prints twelve kit lines and exits 0;
  with one fixture descriptor's `[check]` exiting 1 it exits 1 naming that kit; in a fixture with no
  govkit a `[check.gov]` row is not read, and with one it replaces the argv.
  Red when: one kit's red is lost in the verdict, or gov's override leaks into an adopter's tree.
  figure: twelve is PINNED at `5d1c82ac` and DERIVED at the run.
- **AC13** — When `python loop_lib.py --check` runs it exits 0 with `item.kits.version` in the
  program; `grep -c "point.flow.version" layers.toml` prints at least 2, the declaring row and the
  `uses`; and a fixture with no govkit prints `slot point.flow.version · not-installed` naming the
  version check.
  Red when: the row fails the program check, or the fallback names a leg that no longer exists.

## 7. Gates

`micro-format gate selftest` · `line-length gate selftest` · `shell-hygiene selftest` · `agent-instructions self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `placeholder-catalogue self-test` · `transition-audit arms` · `straggler-guard arms` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `govkit selfcheck` · `run-gates adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `kit placeholders (a declared token its adopter substitutes)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the playbook-render selftest runs `kit_factory.py --fixture` under every plant, its failing case `unknown-key` · none
New arm: tools/govkit/selftest.py · covers AC9 AC10 AC11 · scratch repositories for the five folded checks and a `dates` move, its failing case a moved shipped byte with no bump; the D-arm plants of 5, 5b and 5c move here · none
New arm: tools/run-gates/adopt-run-gates.test.sh · covers AC12 · a scratch target applied with two kits, one `[check]` staged to exit 1 · none
New arm: tools/loop/loop_lib.py · covers AC13 · `check_program` over a fixture row whose route names no item · none

## 8. Open questions

- **F1 — Where the gate lives.** Options: (a) `tools/playbook/`, a core home beside `check_layers.py`;
  (b) new selfcheck arms in govkit; (c) a new kit. layer-expansions:446 says "kit conformance, core",
  PLAY-dOrderedCharter-16 rejected a core contract inside govkit, and (c) is a new install location,
  veto 2. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the survivor that runs at an adopter. widens: none · relaxes: none
- **F2 — What is extracted at the kit schema.** It is the fourth `[kind]` and `[[field]]` file, after
  `item-schema.toml`, `leg-schema.toml` and `role-schema.toml`. Options: (a) one generic
  `check_row_fields` beside `read_kind_schema`, every kit schema read through that one reader; (b) a
  `tools/lib` inline block re-pointing the leg and role kinds; (c) a copy of `load_role_schema`. A kit
  may not import a sibling kit (TOOL-dGroundRules-1 §4), so (a) serves the playbook kit's kinds and
  leaves `leg_factory.py` and `roles_lib.py` their own reads; (b) fails on `role-schema.toml`'s
  different row key; (c) is what `[reuse]` forbids. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Which P28 fields stay on a descriptor.** layer-expansions:448 lists `layers`, `declares`,
  `uses`, `records`, `policies` and `units`, while PLAY-dOrderedCharter-16 S2 and §8 F2 chose one
  `layer` key and rows on `layers.toml`, and PLAY-dOrderedCharter-9 per-kit `instructions.toml`.
  Options: (a) `records` and `policies` here, the others where the landed parents put them; (b) all
  six on descriptors, restating two parents. (b) spells one fact twice. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, `[one-fact]`. widens: none · relaxes: none
- **F4 — The ten `version_from = {none}` entries.** Options: (a) refuse `none` now and give nine a
  constant, the tenth retiring; (b) leave them until the first release. layer-expansions:449 states
  the rule and `gap-deploy-11` counts the ten as a defect. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1. widens: none · relaxes: none
- **F5 — The one version check against `gap-tool-02`'s five.** Options: (a) one function behind one
  leg, the four other checks and arm 5c retired, `check-verdict-epoch.sh` included, with a descriptor
  `dates` key carrying its out-of-claim delegates; (b) keep that script beside a new check. Under (b)
  the gap stays open. PLAY-dOrderedCharter-16 AC1 pins the script's stdout across that unit's own
  lift, an observation made at its pass, so a later retirement contradicts nothing it states;
  TOOL-dTrueNorth-25 S2's closure rule survives as the whole kit's shipped set plus `dates`. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, `gap-tool-02` and fates:107, :177. widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 the retirement of the `check-kit-versions` entry and four legs
- **F6 — The one wiring verdict.** Options: (a) one leg iterating `[check]`, `check-wiring.sh` staying
  as the session repair tool; (b) also folding its install arms into govkit, as fates records; (c)
  keep the eleven legs. (c) leaves the gap. (b) strips an adopter of its only in-tree report, since
  govkit does not ship, and TOOL-dWellOiledMachine-10 extends that script. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F7 — How gov's `--aliases claude` survives one iterator.** Options: (a) a `[check.gov]` table
  mirroring TOOL-dWitnessedBar-11's `[gate_leg.gov]`; (b) a default change in the adopter. (b) moves
  an adopter's behaviour to suit gov. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F8 — `requires` closure over a tree with 21 undeclared edges.** Options: (a) a `resolves` key
  declaring soft edges, the arm both ways, each edge read at the pass and sent to `requires` only
  where a miss refuses; (b) a shrink-only ledger; (c) drop the arm. (c) loses research-distribution-b's
  fifth check; (b) is heavier for the same list. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F9 — Where a Distribution item's row lives.** Options: (a) `tools/loop/loop.toml`, owner
  dShippedRelease, the point on `layers.toml`; (b) a row in `tools/govkit/`. `check_program` reads one
  file, and the slot is `point.flow.version` (PLAY-dOrderedCharter-17 §4). The tag's middle segment is
  the packet's node name, a program rather than a step, and `step = "step.test"` carries the step;
  TOOL-dDeclaredLoop-12's `check_program` binds no tag segment to `step`. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, pin C1's row home. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 10, `gap-tool-02`, `gap-tool-07`,
  layer-expansions:441-456, research-distribution-a:158-175, research-distribution-b:100-115, scout
  E's rows and disagreements 11-14, and the spec brief's I3.

## 10. Reuse audit

The seams extended are `read_kind_schema` (`tools/playbook/row_checks.py`, PLAY-dOrderedCharter-36
S1), `read_descriptors` and the `probe` detector of `check_layers.py`, `core.py new` and the kinds
register, `derive_epoch_state` (`tools/govkit/govkit.py:13363`), `derive_marker_basis`, and
`regen.read_descriptors` with `regen.resolve_argv` (`tools/run-gates/regen.py:108`, `:125`).
`python tools/codebase-map/reuse_lookup.py "conformance gate grading every kit descriptor's fields
and generating a conforming kit"` ranked name-stem hits (`resolve_kit_dir`, `read_descriptors`,
`check_conformance` in `tools/runlog/model.py`, `derive_marker_basis` absent); none is a schema
checker, so the seam is the parents' specced reader. Scout E's row holds at source with these
corrections: `kit-schema.toml` is the fourth schema of the shape, not the third, since
`item-schema.toml` (TOOL-dDeclaredLoop-24 S2) came first; arm 5b exists at `:2164`, which the gap
does not count; `check-verdict-epoch.sh`'s `DELEGATES` reaches outside the kit, so `derive_epoch_state`
alone does not subsume it; and the recall hit calling the fold "selfcheck arms plus a P28 arm"
(research-distribution-b:92) was overtaken by PLAY-dOrderedCharter-16's rejected alternative.

Recall terms used: `python tools/memory-recall/query.py "how does a kit factory and conformance gate validate descriptor keys and one version check" --terms "kit.toml descriptor factory conformance gate kind.kit selfcheck version_from lockstep check-kit-versions wiring verdict P28"`

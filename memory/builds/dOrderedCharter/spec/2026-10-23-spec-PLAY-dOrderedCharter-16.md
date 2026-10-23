# PLAY-dOrderedCharter-16 — the layer register, the layer contract and the check that the core never depends on an expansion or an optional component

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 2 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0046@bd068162 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md) | research | PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-16-deviation-161.md](../build/2026-10-24-build-PLAY-dOrderedCharter-16-deviation-161.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-16-deviation-162.md](../build/2026-10-24-build-PLAY-dOrderedCharter-16-deviation-162.md) | deviation | — |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

The product has no layer model: kits declare no layer, the core depends on optional kits, and no
contract says what a layer is, so an expansion cannot be added or removed mechanically
(`gap-found-17`, closed by this unit with PLAY-dOrderedCharter-17). This unit lands the layer
register, the layer contract each layer fills, a factory that writes a conforming layer row, and one
check over the tree: every edge from a core kit to a non-core kit, found by kind, is red unless the
core kit declares it as an optional slot with a named fallback, and an expansion using a point
another expansion declares is red (EX-1). It lands after PLAY-dOrderedCharter-18 has moved every
name a core memory-tree module imported from the recall kit (P28, v2 `[layers]`; DA-H3, DA-M7, M8).

## 2. Scope (IN)

- **S1** — The layer register, `tools/playbook/layers.toml`: one `[[layer]]` row per layer, with
  `tag`, `kind` (`core`, `optional` or `expansion`), `of` (the core layer an `optional` row belongs
  to), `definition`, `declares` (the extension points it declares) and `uses` (those it attaches at),
  plus one top-level `shared` list of tool directories that hold inline-copied primitives and no
  layer (`lib`) and a `homes` list on a row for a tool directory that has no descriptor (`govkit`).
  Rows at landing: the five core layers, the three expansions, and the optional rows
  `layer.memory.map`, `layer.memory.recall`, `layer.memory.lexicon` and `layer.flow.leg-packs`.
  Observed by AC8.
- **S2** — The layer row in each kit descriptor (shared interface S20): `layer = "<tag>"` beside
  `requires_if` in each of the 29 `kit.toml` files, and `optional = [{ part, point, fallback }]` on a
  core kit for each edge it is allowed to keep. A kit's engine membership is derived from these keys,
  never typed in the register. Observed by AC8.
- **S3** — The layer contract and its conformance gate. Each row's tag is `layer.<seg>(.<seg>)*`
  (shared interface S4's shape); its kind is in the closed set; an `optional` row's `of` names a core
  row; its definition is non-empty; each point it `uses`, and each `point` a descriptor's `optional`
  row names, is declared by exactly one core row; a core row has at least one kit; every descriptor's `layer` names a row; every tool directory is a
  descriptor's home, a row's `homes` entry or a `shared` entry. Each violation is a red naming the
  row or descriptor. The contract's other items, a layer's instruction units, record kinds,
  policies and gates, join when their registries land (§3). Observed by AC7 and AC8.
- **S4** — The layer kind's factory: `check_layers.py --new <tag> --kind <kind> [--of <tag>]
  --definition <text>` appends a row that passes S3 to `layers.toml` and prints the descriptor key a
  kit adds to join it; it refuses a tag already registered or one S3 would red. Observed by AC9.
- **S5** — The AST import walk, lifted from `tools/memory-tree/check-verdict-epoch.sh:222-263` into
  `tools/memory-tree/import_walk.py` at its second instance. It yields each import a Python file
  makes, at any depth, by kind: `import`, `from`, and `dynamic` for a literal `__import__("<n>")`,
  `importlib.import_module("<n>")` or `importlib.util.spec_from_file_location(_, <literal path>)`.
  `check-verdict-epoch.sh` calls it and keeps its own reading, static kinds only, so its output on
  the tree is unchanged. Observed by AC1.
- **S6** — The dependency check, `tools/playbook/check_layers.py`. Its population is every edge from a
  file a core kit ships to a non-core kit, derived over the tree by kind, each kind with its own
  detector and its own planted red:

  | Kind | What it reads |
  |---|---|
  | `import` | `import` and `from` names that resolve to a `.py` file in a non-core kit's home and not in the importer's own directory |
  | `dynamic` | `__import__` and `importlib` loads with a literal name or path |
  | `probe` | a `resolve_kit_dir` call, Python or shell, whose home argument is a non-core kit's home, and a path literal naming one |
  | `copy` | a `shutil.copy*`, `copytree` or shell `cp` whose source names a non-core kit's file |
  | `shell` | a shell line that runs a path under a non-core kit's home |
  | `requires-if` | a `requires_if` row of a core descriptor naming a non-core kit |

  A file a kit ships is one its descriptor does not withhold (`role = "project-owned"`). An edge is
  allowed when the source kit's `optional` rows name its file as `part`; every other edge is a red
  naming the file, line, kind and target kit. Observed by AC2 to AC5.
- **S7** — EX-1's arm: a point one row `uses` that a non-core row `declares` is a red naming both
  rows, and so is a point declared by a non-core row at all. Observed by AC6.
- **S8** — The leg `layer dependencies (the core never depends on an expansion)` in
  `tools/gate-legs.json`, chunk `declarations`, and the rows a new leg owes: an `[[exempt_leg]]` row
  in `tools/govkit/registry.toml`, since it grades gov's own kit sources, a row in
  `tools/govkit/subject-pins.tsv`, a row in `tools/run-gates/ceiling-evidence.txt` from the measured
  run, and the name in `memory/map/features/playbook.md`'s legs. Observed by AC10.
- **S9** — The check's fixture, `check_layers.py --fixture --plant <case>`, building a scratch tree of
  three kits under a three-row register, one plant per S6 kind, plus `unslotted`, `slotted`,
  `ex1-pair`, `no-layer`, `unknown-layer` and `undeclared-point`. Observed by AC2 to AC7.

## 3. Non-goals (OUT)

- Moving the recall names into memory-tree: PLAY-dOrderedCharter-18's, which lands first. The moved
  names are check 27's eight; the id grammar's `grammar_for`, `anchor_at` and `repo_root`, which
  `backlog.py`, `corpus_ids.py`, `merge-rows.py` and `transition_audit.py` import; `recall_conf.resolve`
  and its `Conf.digest`, which `transition_audit.py` calls; and `extract.grammar_for`, which
  `gen_build_index.py` imports.
- Curing the edges the check finds on today's tree: PLAY-dOrderedCharter-17's. Until it lands the
  leg is red over the tree, and both land in this build's one landing (§4 "### Rollout").
- Rendering a slot's three states: PLAY-dOrderedCharter-17 declares them, dBoundRoles renders them.
- The slug grammar on the moved parser, and the check's population drawn from the kit-to-layer map's
  optional rows when that map becomes a dTotalRecall record: dTotalRecall extends both.
- A layer's instruction units, record kinds, policies and gates as contract items: they join when the
  instruction-unit registry (PLAY-dOrderedCharter-9) and the kinds register (PLAY-dOrderedCharter-7)
  land, each by its own unit.
- Edges from a file no descriptor claims, such as `tools/check-spec-tokens.py`: not graded, and said.
- JavaScript `require` edges: the hooks and workflows kits are core and reach no non-core kit by
  `require` today (`git grep -n "require(" -- tools/hooks tools/workflows` names no non-core home);
  stated as a gap the check prints.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-18` — the moved `grammar_for`, `anchor_at`, `repo_root`, `recall_conf.resolve` and `Conf.digest` in `tools/memory-tree/id_grammar.py`; without the move the check is red on five memory-tree modules for a reason this unit does not cure
- **hands-off** `PLAY-dOrderedCharter-17` — every edge the check finds on today's tree, each made an `optional` row with a named fallback or moved into the core, and the three slot states
- **hands-off** `PLAY-dOrderedCharter-7` — the layer kind registered in the kinds register, its gate held to the conformance-gate contract, and the layer leg's `enforces` row
- **hands-off** `PLAY-dOrderedCharter-10` — the `layer` namespace, whose declaring source is `tools/playbook/layers.toml`
- **hands-off** `PLAY-dOrderedCharter-19` — `tools/playbook/layers.toml` and the descriptor `layer` key, which the `owned` arm reads
- **hands-off** `PLAY-dOrderedCharter-15` — the layer register's declared points, which the write command's arms read
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 43 and 63, which that batch unit corrects after this unit lands, each by the item its report id names
- **hands-off** `PLAY-dOrderedCharter-55` — `import_walk.derive_import_closure`, over which the tag index's extractor version is hashed (round-2 id 19)

## 4. Design

### Data model

```toml
# tools/playbook/layers.toml
shared = ["lib"]

[[layer]]
tag = "layer.memory"
kind = "core"
definition = "the trail, what happened in a build, and the library, what generalizes beyond one"
declares = ["point.memory.record-home"]
uses = []

[[layer]]
tag = "layer.memory.recall"
kind = "optional"
of = "layer.memory"
definition = "the record finder for why-questions"
declares = []
uses = []

[[layer]]
tag = "layer.distribution"
kind = "expansion"
definition = "the product's delivery across a repository boundary"
homes = ["govkit"]
declares = []
uses = ["point.runtime.install-target"]
```

```toml
# a core kit's descriptor
layer = "layer.memory"
optional = [{ part = "gen_build_index.py", point = "point.observability.signal", fallback = "the column renders not-installed" }]
```

The rows' definitions are v2 `[layers]`' table cells; the points are the eight
`layer-expansions.md` `[core-points]` names, each spelled `point.<layer>.<seg>`. The `point` words
are a stand-in: a later build registers a `point` namespace and the shape check joins it then.

The kit-to-layer assignment is `layer-instruction.md`'s `[layers]` table ("Kits mapped to layers",
lines 222-243), read as written: playbook, agent-instructions, roles, workflows, memory-tree,
run-gates, push-main, session-kickoff, unattended, hooks and process-monitor core; codebase-map,
memory-recall and lexicon `optional` of memory; gate-lint and pytest-parallel-guardrails `optional`
of flow (`layer.flow.leg-packs`, "verdict leg packs"); runlog, drift-audit and branch-reconcile
observability; govkit distribution. An entry the table does not name, the `check-*` scripts and
`settings-merge`, takes the layer of the leg or merge it serves, written in the pass commit's
`Decided:` trailer.

### The walk

`import_walk.scan_imports(path)` returns `[(name, line, kind)]` for one file; `derive_import_closure(kit,
files)` is `check-verdict-epoch.sh`'s closure, moved verbatim with its message strings, and the shell
gate runs `"$_ve_py" "${_kit}import_walk.py" --closure "$_kit" $SCAN`. A lexer bug in the walk moves
both gates at once, which is the point of one copy.

### The check

```
python tools/playbook/check_layers.py                 # the leg: S3, S6, S7 over the tree
python tools/playbook/check_layers.py --list          # every edge found, allowed or not, by kind
python tools/playbook/check_layers.py --new <tag> --kind <kind> [--of <tag>] --definition <text>
python tools/playbook/check_layers.py --fixture --plant <case>
```

Kits are read from `tools/*/kit.toml` and `tools/govkit/entries/*.kit.toml` with `tomllib`; an
entry's files are its `[[files]]` includes, a directory kit's are its home. The check reaches
`import_walk.py` through `resolve_kit_dir("memory-tree", "import_walk.py", here)`, core to core. Every
line opens `layers:`; the summary carries layers, kits, edges by kind, allowed and red, DERIVED at the
run. It prints, every run, what it does not read: computed paths, JavaScript, and files no descriptor
claims.

### Inventory

Minted: `tools/playbook/layers.toml` with keys `shared`, `tag`, `kind`, `of`, `definition`,
`declares`, `uses`, `homes`; the kind words `core`, `optional`, `expansion`; the descriptor keys
`layer` and `optional` with `part`, `point`, `fallback`; the modules `tools/playbook/check_layers.py`
and `tools/memory-tree/import_walk.py`; the functions `read_layers`, `read_descriptors`,
`derive_edges`, `check_layers`, `build_layers_fixture`, `scan_imports`, `derive_import_closure`; the flags
`--list`, `--new`, `--kind`, `--of`, `--definition`, `--fixture`, `--plant`, `--closure`; the leg
named in S8; the prefix `layers:`. Naming cells: each function is checked with
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Additive: two keys per descriptor, which govkit reads by name and ignores otherwise (`git grep -n
"d.get(\"layer\")" -- tools/govkit` finds no reader today). An adopter receives `layers.toml` with the
playbook-render kit and no leg, since the leg is gov's.

### Rollout

Live at landing. The leg is red over the tree from this pass until PLAY-dOrderedCharter-17's pass;
no gate runs between passes (BUILD-METHOD M6), and the close runs the bar once over both.

### Files touched (estimate)

- `tools/playbook/layers.toml` (new)
- `tools/playbook/check_layers.py` (new)
- `tools/memory-tree/import_walk.py` (new)
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/agent-instructions/kit.toml`, `tools/branch-reconcile/kit.toml`, `tools/codebase-map/kit.toml`, `tools/drift-audit/kit.toml`, `tools/gate-lint/kit.toml`, `tools/hooks/kit.toml`, `tools/lexicon/kit.toml`, `tools/memory-recall/kit.toml`, `tools/memory-tree/kit.toml`, `tools/playbook/kit.toml`, `tools/process-monitor/kit.toml`, `tools/pytest-parallel-guardrails/kit.toml`, `tools/roles/kit.toml`, `tools/run-gates/kit.toml`, `tools/runlog/kit.toml`, `tools/unattended/kit.toml`, `tools/workflows/kit.toml`
- `tools/govkit/entries/check-agent-cap-restatement.kit.toml`, `tools/govkit/entries/check-install-prefix.kit.toml`, `tools/govkit/entries/check-kit-versions.kit.toml`, `tools/govkit/entries/check-line-length.kit.toml`, `tools/govkit/entries/check-microformats.kit.toml`, `tools/govkit/entries/check-placeholders.kit.toml`, `tools/govkit/entries/check-testsuite-counts.kit.toml`, `tools/govkit/entries/check-wiring.kit.toml`, `tools/govkit/entries/kickoff-manifest.kit.toml`, `tools/govkit/entries/playbook.kit.toml`, `tools/govkit/entries/push-main.kit.toml`, `tools/govkit/entries/settings-merge.kit.toml`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/map/features/playbook.md`
- `tools/memory-tree/check-verdict-epoch.test.sh`

### Alternatives rejected

- **The layer list typed in the register beside each kit.** Two places to keep in step; the kit's own
  descriptor declares its layer (P28, "a kit implements layers and declares which").
- **A grep of `resolve_kit_dir` alone.** It misses imports through `sys.path`, `importlib` loads and
  `requires_if` rows, the kinds the clause lists, and the walk's own comment names those as what it
  does not see (`check-verdict-epoch.sh:219-221`).
- **The check in govkit.** govkit is distribution, an expansion, so the core's own contract would live
  in the layer it constrains.

## 5. Production-readiness checklist

- security: read-only over the tree; `--new` writes only `tools/playbook/layers.toml`; the fixture writes in its own temp directory.
- perf / scale: one parse of every shipped `.py` file of the core kits and one line scan of their shell files, measured at the pass and set as the leg's `ceiling`.
- error / empty / loading states: an unreadable register or descriptor exits 2 naming it; a core layer with no kit is a red, never an empty pass; a kind with no edge prints `0` beside its name.
- observability: one summary line and one line per red.
- risks: a detector's false positive on a comment or a string; the line scan skips comment lines and the fixture's `slotted` plant keeps a legal edge green.
- testing: AC1 to AC10 and the fixture arm of §7.
- migration: §4 "### Migration".
- user docs: a section in `tools/playbook/README.md` naming the register, the two descriptor keys and the check.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs on the tree before and after the
  lift, its stdout is byte-identical; and when `scan_imports` from `import_walk.py`
  reads a planted file holding a function-nested `import x` and an `importlib.import_module("y")`, it
  returns an `import` row for `x` and a `dynamic` row for `y`, each with its line.
  Red when: the lifted walk changes the verdict-epoch gate's reading, or misses a nested or dynamic
  load.
  fixture: the planted file is written under the run's scratch path.
- **AC2** — When `python check_layers.py --fixture --plant import` runs, it exits 1
  naming the importing file, the line, kind `import` and the target kit; `--plant dynamic` exits 1
  naming kind `dynamic` for an `__import__` and again for an `importlib` load.
  Red when: an import nested in a function, or a dynamic load, is no edge.
- **AC3** — When `--plant probe`, `--plant copy` and `--plant shell` run, each exits 1 naming its kind:
  a `resolve_kit_dir` call to a non-core home, a `shutil.copyfile` of a non-core kit's module, and a
  shell line running a non-core kit's script.
  Red when: a path probe, a file copy or a shell reference is not an edge.
- **AC4** — When `--plant requires-if` runs, it exits 1 naming the core descriptor and the non-core
  kit its `requires_if` row names.
  Red when: a declared conditional dependency on a non-core kit passes.
- **AC5** — When `--plant unslotted` runs, a core module reading the fixture's map kit with no
  `optional` row, it exits 1; `--plant slotted`, the same edge with an `optional` row naming the
  module as `part`, exits 0 and `--list` prints the edge as allowed.
  Red when: an unconditional read of an optional component passes, or a declared slot is red.
- **AC6** — When `--plant ex1-pair` runs, one expansion row declaring a point and another expansion
  row using it, it exits 1 naming both rows and the point.
  Red when: expansions meet at an expansion's point.
- **AC7** — When `--plant no-layer`, `--plant unknown-layer` and `--plant undeclared-point` run, each
  exits 1 naming the descriptor or row.
  Red when: a kit with no layer, a layer tag no row holds, or a used point nobody declares passes.
- **AC8** — When `python check_layers.py --list` runs on the tree after
  PLAY-dOrderedCharter-17's pass, it names twelve layer rows, 29 descriptors each with a layer, and
  every edge allowed; on this unit's pass alone it prints at least the `gen_build_index.py` edge to
  `drift-audit` as red.
  Red when: the population is empty on today's tree, which would be a vacuous green.
  figure: the edge counts are DERIVED at the run; twelve and 29 are PINNED, measured 2026-10-23.
- **AC9** — When `python check_layers.py --new layer.fixture --kind expansion --definition "x"`
  runs in a scratch copy, `layers.toml` gains a row and the next plain run reds only on
  `layer.fixture` having no `uses` point declared by a core row if one is named; `--new layer.memory`
  exits non-zero naming the duplicate.
  Red when: the factory writes a row its own gate refuses, or a duplicate.
- **AC10** — When `git grep -n "layer dependencies" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/playbook.md`
  runs, each of the five files names the leg.
  Red when: the leg lands without a row one of its meta-gates owes.

## 7. Gates

`verdict epoch (kit version dates the engine)` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `agent-cap self-test` · `agent-instructions self-test` · `branch-reconcile selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `hook destinations self-test` · `lexicon selftest` · `measure-legs selftest` · `playbook render selftest` · `pre-push run-log line` · `pytest-guardrails self-test` · `recall floor` · `recall floor arms` · `review-join self-test` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `runlog selftest` · `scratch-guard self-test` · `shell-hygiene selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test`

New arm: tools/playbook/check_layers.py · covers AC8 · the new leg itself, its failing case staged by deleting one `optional` row PLAY-dOrderedCharter-17 writes · none
New arm: tools/playbook/adopt-playbook.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 · the playbook-render selftest runs `check_layers.py --fixture` under every plant of S9, asserting each exit and named line · none
New arm: tools/memory-tree/check-verdict-epoch.test.sh · covers AC1 · a case asserting the lifted walk's closure line equals the inline one's on a fixture kit · none

## 8. Open questions

- **F1 — Where the register and the check live.** Options: (a) `tools/playbook/`, beside the
  namespace and edge registries the brief places there, the walk lifted into `tools/memory-tree/`
  where its first instance is; (b) all in `tools/memory-tree/`, the core engine; (c) a new kit, a new
  install location. (c) fails veto 2. (b) puts the product's layer contract in the memory layer's
  kit, so a reader of instruction-layer registries looks in two homes. RESOLVED (agent, 2026-10-23,
  delegated): (a), rung 3, the survivor that keeps every registry the tag system joins in one home
  (shared interface S4). widens: none · relaxes: none
- **F2 — How an optional component's kit differs from a core kit of the same layer.** v2 `[layers]`
  makes memory core and its map, recall and lexicon optional, and the brief's S20 gives a descriptor
  one `layer` key. Options: a second descriptor key; an `optional` row kind in the register, the kit
  naming `layer.memory.recall`. RESOLVED (agent, 2026-10-23, delegated): the row kind, rung 3: one key
  per descriptor as S20 spells it, and the tag grammar's multi-segment form carries the parent.
  widens: none · relaxes: none
- **F3 — Whether the leg lands red until PLAY-dOrderedCharter-17.** Options: a shrink-only list of
  today's edges, drained by that unit; land the leg live, both units in one landing. A list is
  scaffolding the next unit deletes. RESOLVED (agent, 2026-10-23, delegated): live, rung 3, since no
  bar runs between passes and the build lands whole. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seams extended: the inline import walk of `tools/memory-tree/check-verdict-epoch.sh:206-263`,
lifted at its second instance rather than copied; `requires_if` rows as govkit selfcheck check 7
already parses them (`tools/govkit/govkit.py:2479-2502`), read here by the same field names;
`resolve_kit_dir` (`tools/lib/resolve_kit_dir.py:15`), whose home argument is the probe kind's
signal; and the kit-to-layer table of `layer-instruction.md:222-243`. `reuse_lookup.py "find every
import or path reference from one kit to another kit's files"` ranked `kit_rel`, `resolve_kit_dir`
(installs 72), `kit_dir` and `build_reference_index` (`tools/codebase-map/map_lib.py`, an optional
component's, so the core cannot import it): no layer or dependency check exists. The recall probe
returned the class record `memory/gotchas/core-depends-on-an-optional-part.md`, whose symptom, a
dependency hidden behind a guard that seems to degrade it, is why an edge is red unless declared as an
`optional` row rather than whenever it lacks a guard. Where the scout and source disagree: the scout cites the walk at `:222-266`; the python
body ends at `:263` and `:264-270` is the shell's exit mapping. A base-tree probe over the core kits'
shipped files found core-to-non-core edges beyond the nine the clause names: `.githooks/pre-push:947`
(lexicon), `tools/push-main.sh:809`, `tools/check-install-prefix.sh:201` and
`tools/run-gates/run-gates.sh:3008` (govkit), `tools/unattended/unattended.sh:12040` (codebase-map's
journal) and `tools/playbook/kit.toml:31,37` (govkit's files copied); the check's population is
derived, so they are found without being typed.

Recall terms used: `python tools/memory-recall/query.py "how does the core avoid depending on an optional kit or expansion" --terms "layer register core expansion optional component requires_if resolve_kit_dir import walk P28 EX-1 kit.toml"`

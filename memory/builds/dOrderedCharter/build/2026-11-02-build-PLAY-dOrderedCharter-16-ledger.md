# PLAY-dOrderedCharter-16 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-16

Each line is a probe this pass ran in the worktree or under the run's scratch path, and what it
printed. The check's plain run on the tree is the new leg itself, which a role agent may not run once
the leg is registered: the AC8 reading below was taken before `tools/gate-legs.json` named it. AC1's
byte-identity is observed here on the walk, not by running the verdict-epoch gate; the gate's own
reading, the new suite arm and the fixture arm in `adopt-playbook.sh --selftest` are the main loop's
at the close.

**Evidences:** PLAY-dOrderedCharter-16
- AC1 — `cmp` — the inline walk cut from `check-verdict-epoch.sh:281-318` and `import_walk.py --closure tools/memory-tree/` over the gate's scan set printed identical bytes, `the delegates' import closure is 12 sibling module(s) and 1 other scanned file(s), every sibling in DELEGATES`, both exit 0; on a scratch kit with a missing sibling and an unparsable one both printed the same three FAILED lines and exited 2; `scan_imports` on a planted file returned `('x', 3, 'import')`, `('y', 4, 'dynamic')` and `('z', 5, 'dynamic')` for a function-nested `import x`, an `importlib.import_module("y")` and a `__import__("z")`
- AC2 — `--fixture --plant import` — exit 1, `RED tools/corekit/core.py:9 · import · core kit corekit depends on non-core kit mapkit`; `--plant dynamic` exit 1 with `core.py:10 · dynamic` for the `__import__` and `core.py:11 · dynamic` for the `importlib` load
- AC3 — `--plant probe`, `copy`, `shell` — each exit 1: `core.py:9 · probe`, `core.py:10 · copy` (a `shutil.copyfile` of mapkit's `reader.py`), `run.sh:4 · shell` to expkit; the same file's comment line naming `tools/expkit/go.sh` is no edge
- AC4 — `--plant requires-if` — exit 1, `RED tools/corekit/kit.toml:4 · requires-if · core kit corekit depends on non-core kit expkit`
- AC5 — `--plant unslotted` exit 1 at `core.py:7 · import`; `--plant slotted` exit 0 and `--plant slotted --list` printed `layers: edge tools/corekit/core.py:7 · import · corekit -> mapkit · allowed`
- AC6 — `--plant ex1-pair` — exit 1, `RED row 'layer.exp' uses point.exp.hook, which 'layer.exp2' declares, a non-core row`, and `RED row 'layer.exp2' (expansion) declares point.exp.hook`
- AC7 — `--plant no-layer`, `unknown-layer`, `undeclared-point` — each exit 1: `descriptor tools/mapkit/kit.toml declares no layer`; `names layer 'layer.nowhere', which no row holds`; `row 'layer.exp' uses point.core.missing, which 0 core row(s) declare`; the control, no plant, exit 0 with `0 allowed, 0 red; 0 contract red(s)`
- AC8 — `check_layers.py --list` — 12 `layers: row` lines, 30 `layers: kit` lines each naming a layer, against 30 paths `git ls-files 'tools/*/kit.toml' 'tools/govkit/entries/*.kit.toml'` prints; the plain run exited 1 with `12 layer row(s), 30 kit descriptor(s); edges by kind: import 1 · dynamic 0 · probe 51 · copy 5 · shell 0 · requires-if 1; 0 allowed, 58 red; 0 contract red(s)`, `tools/memory-tree/gen_build_index.py:1959 · probe` and `:1965 · import` to drift-audit among the reds; every edge allowed is PLAY-dOrderedCharter-17's to observe
- AC9 — `--new layer.fixture --kind expansion --definition "x"` in a scratch copy of the kit — exit 0, the row appended with `declares = []` and `uses = []`, `layer = "layer.fixture"` printed; the check over the tree with that register read `13 layer row(s)` and `0 contract red(s)`; `--new layer.memory` exit 1, `REFUSED 'layer.memory' is already registered`; `--new layer.Bad` and an optional row `--of layer.nowhere` each exit 1 naming the refusal
- AC10 — `git grep -n "layer dependencies" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/playbook.md` — one hit in each of the five files

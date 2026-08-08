# codebase-map — the self-verifying feature/inventory map

```toml
feature = "codebase-map"
title = "Codebase map — CI-verified inventory claims + the reuse recall index"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["codebase-map coverage + freshness", "codebase-map kit selftest"]
kits = ["codebase-map"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
[paths]
globs = [
  "tools/codebase-map/*",
  "memory/map/*",
  ".codebase-map.conf",
]
```

## Constraints & why

The map is adopted here at a NON-CANONICAL install prefix. The kit's own convention is
`<repo-root>/codebase-map/`, and `map_lib.repo_root()` implements that convention by taking the kit
dir's grandparent. This repo puts every kit under `tools/`, so that grandparent is `tools/` and every
derived path is wrong by one segment. Two consequences are load-bearing:

- `tools/codebase-map/adopt-codebase-map.sh` cannot run here at all. It guards on
  `[ "$HERE" -ef "$ROOT/codebase-map" ]` and refuses. The adoption was therefore done by hand:
  conf, extractors, `gen_map.py --scaffold`, `--seed-affordance-baseline`, gate template copied to
  `GATE_FILE`.
- `tools/codebase-map/map_extractors.py` sets `CODEBASE_MAP_ROOT` from its own path at import, so
  every entrypoint that imports the project layer is correct with no environment set. That is
  `gen_map.py` and the gate; it is NOT `reuse_lookup.py` or `map_diff.py`. See `## Gaps`.

`baseline.toml` holds the initial backfill of 71 keys and is shrink-only: a new key must be claimed
in a dossier, never appended to the baseline. The gate proved this on its own first run — adding the
`codebase-map coverage + freshness` leg failed the coverage assert until this dossier claimed it.

## Shared seams

`map_lib.py` is the portable engine and is shared substrate rather than this feature's private code:
`gen_map.py`, `map_diff.py`, `reuse_lookup.py`, the gate and `map_extractors.py` all read it. It is
not glob-claimed by any other dossier, because exclusive glob ownership of a shared module is
impossible and the keyed plane already carries ownership through the keys each feature registers.

`tools/lib/resolve-python.sh` is inlined byte-identically into `adopt-codebase-map.sh`, which is the
repo-wide python-launcher seam rather than anything this feature owns.

## Gaps

- **`reuse_lookup.py` and `map_diff.py` are silently dark at this install prefix.** Neither imports
  the project layer, so both resolve the root to `tools/`, find no `.codebase-map.conf`, and return
  `corpus: 0 symbols | 0 inventory keys` then `no seam fits` — and `mapped 0/N` — with no notice that
  the corpus is empty rather than unmatched. Measured on this tree. This is the
  `vacuous-selector-empty-population` and `fixture-passes-by-finding-nothing` classes: a confident
  answer derived from an empty population. Workaround until the kit resolves a prefixed install:
  export `CODEBASE_MAP_ROOT` (the invocation is written out in `.codebase-map.conf`).
- **No feature dossiers beyond this one.** 69 of 71 keys sit in `baseline.toml`, so coverage is
  ratcheted but not yet described. The map enforces "nothing new goes unclaimed"; it does not yet
  answer "what is this repo made of".
- **bash is recall-dark.** It carries the product here — the gates, adopters and hooks — and
  `map_lib` ships no shell symbol extractor. Declared in `.codebase-map.conf` `RECALL_DARK_LAYERS`
  so `reuse_lookup.py` prints a partial-recall notice rather than a falsely confident miss.
- **`*.template.py` is excluded from the symbol layer** because a template and its instantiated twin
  define the same names in two files, and `fan_in()` counts the twin as a reference. Measured: with
  the templates indexed, two `test_*` functions outranked `walk_dir_keys` in the reuse shortlist.

## Reuse affordance

seam: map_lib — reuse for dossier/baseline parsing, deterministic rendering, coverage asserts and
fan-in ranking; extend via a new helper in `map_lib.py` plus its case in `selftest.py`.
seam: map_extractors.EXTRACTORS — reuse for declaring a new enumerable surface of this repo; extend
via a new key whose callable fails closed, then claim its keys in a dossier.

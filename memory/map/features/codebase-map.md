# codebase-map — the self-verifying feature/inventory map

```toml
feature = "codebase-map"
title = "Codebase map — CI-verified inventory claims + the reuse recall index"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["codebase-map coverage + freshness", "codebase-map kit selftest", "codebase-map adopter e2e"]
kits = ["codebase-map"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/codebase-map/*",
  "memory/map/*",
  ".codebase-map.conf",
]
```

## Constraints & why

The map is adopted at a NON-CANONICAL install prefix — every kit here lives under `tools/`, not at
the repo root the kit's convention assumed. That USED to be this feature's defining constraint: the
engine resolved the root as the kit dir's grandparent, so at this prefix every derived path was one
segment short, `adopt-codebase-map.sh` refused to run, and `reuse_lookup.py` and `map_diff.py`
answered confidently from an empty corpus.

The engine fixed it (the aRootedPrefix unit): `map_lib.resolve_root()` walks up for
`.codebase-map.conf`, bounded by `.git`. Every entrypoint is now correct here with no environment
set, the adopter runs, and its own e2e leg is on the bar. The former `CODEBASE_MAP_ROOT` workaround
in `map_extractors.py` is gone and must not be reintroduced — the kit's selftest now bans
`Path.resolve()` in kit code, because it follows a junction to the link target and would disagree
with `map_lib.kit_dir()` about the prefix stamped into byte-compared artifacts.

`baseline.toml` holds the shrink-only backfill of the keys no dossier claims yet: a new key must be claimed
in a dossier, never appended to the baseline. The gate proved this on its own first run — adding the
`codebase-map coverage + freshness` leg failed the coverage assert until this dossier claimed it, and
again when `codebase-map adopter e2e` arrived from main.

## Shared seams

`map_lib.py` is the portable engine and is shared substrate rather than this feature's private code:
`gen_map.py`, `map_diff.py`, `reuse_lookup.py`, the gate and `map_extractors.py` all read it. It is
not glob-claimed by any other dossier, because exclusive glob ownership of a shared module is
impossible and the keyed plane already carries ownership through the keys each feature registers.

`tools/lib/resolve-python.sh` is inlined byte-identically into `adopt-codebase-map.sh`, which is the
repo-wide python-launcher seam rather than anything this feature owns.

## Gaps

- **Two feature dossiers so far.** 69 inventory keys still sit in `baseline.toml`, so coverage is
  ratcheted but not yet described. The map enforces "nothing new goes unclaimed"; it does not yet
  answer "what is this repo made of". Read the live counts from `reuse_lookup.py`'s corpus header,
  never from this line — it is prose and this gap is exactly where prose rots.
- **bash is recall-dark.** It carries the product here — the gates, adopters and hooks — and
  `map_lib` ships no shell symbol extractor. Declared in `.codebase-map.conf` `RECALL_DARK_LAYERS`
  so `reuse_lookup.py` prints a partial-recall notice rather than a falsely confident miss.
- **`*.template.py` is excluded from the symbol layer** because a template and its instantiated twin
  define the same names in two files, and `fan_in()` counts the twin as a reference. Measured: with
  the templates indexed, two `test_*` functions outranked `walk_dir_keys` in the reuse shortlist.

## How the neighbour cap selects

- **The cap slices the RANKED pool, and the ordering key is stated ONCE.** `_shortlist_key` is read
  twice — to cap the neighbours, and to sort the shortlist that prints — because a retyped second
  copy is how the two came to disagree: the cap sliced `sorted(neighbours.items())`, which is
  ALPHABETICAL, while the sort below it ordered by fan-in. `_rank` therefore only ever saw the
  twelve names that sorted earliest, and the ranking ran on a pool the alphabet had already chosen.
  Measured at base `c4fcf5ad`: the twelve retained summed to fan-in 8, the twelve the ranking keeps
  sum to 271, and the two sets do not intersect.
- **What the reorder is worth, measured rather than assumed.** Replayed over 140 recorded probe
  phrases graded against the seam each spec's own §10 names: hit rate 0.579 → 0.600, while hit@5,
  hit@10 and the median rank of the first correct answer are all UNCHANGED at 0.371, 0.400 and 2.
  So the change is correct at source and its effect on the ranks a reader actually looks at is
  nil on this corpus. The instrument is `replay-phrases.py`, which is `project-owned` and on no leg.
- **The printed header discloses what the ranking does not mean.** Fan-in counts name tokens and
  resolves no symbols, so a high rank means "this name appears a lot", never "this is your seam".
- **The same-kind arm is DIRECTORY-SCOPED, and the axis is the defining file's own directory.** Kind
  alone admitted 619 of 648 kinded candidates — 95% — so no cap over it selected by anything.
  Scoped to the seed's directory the same pool falls to 134 / 133 / 101 / 81 across the four
  largest, a reach reduction of 4.6x to 7.6x. The axis is `os.path.dirname`, not a "kit" concept, so
  it needs no declaration and means the same thing in an adopter's tree.
- **What the narrowing COSTS, measured and not buried.** Replayed over the same 140 phrases, the
  hit rate falls 0.600 → 0.586: two phrases lose their hit, at ranks **31 and 27**. hit@5, hit@10
  and the median rank are unchanged, one phrase's rank improves and none worsens. So what the
  narrowing discards sat far below the twelve-slot cap, where no reader reaches; what it buys is a
  pool a cap can bound. A seed whose directory holds no other symbol of its kind gets an EMPTY
  neighbour list, which the reason string makes legible — measured here, no directory is in that
  state: all 18 (directory, kind) groups holding more than one symbol return a non-empty arm.

## Reuse affordance

seam: map_lib — reuse for dossier/baseline parsing, deterministic rendering, coverage asserts and
fan-in ranking; extend via a new helper in `map_lib.py` plus its case in `selftest.py`.
seam: map_extractors.EXTRACTORS — reuse for declaring a new enumerable surface of this repo; extend
via a new key whose callable fails closed, then claim its keys in a dossier.

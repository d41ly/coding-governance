# Build brief — TOOL-dRetiredFork-2

**Serves:** journal TOOL-dRetiredFork-2

## What the unit is

When a git hook invokes a kit generator, git's exported variables — `GIT_DIR`, `GIT_INDEX_FILE`,
`GIT_WORK_TREE` and siblings — reach the subprocess and point it at the wrong tree. gov carries the
HOOK-side scrub already (`.githooks/pre-push:25`) and not the generator-side one. NicoCares carries
both, as `nc carve-out 16/20` and `17/20` — one defect at two legs.

## What this pass does

1. S1 — a leak list plus a cleaned-environment builder in
   `tools/memory-tree/gen_build_index.py`, passed at the `run()` call site. `run()` is the SINGLE
   choke point: all seven git invocations go through it, so one `env=` covers every one.
2. S2 — the process-level pop in `tools/memory-recall/selftest.py`, ABOVE the `sys.path` insert.
3. S3 — one arm per file: export a `GIT_DIR` naming a decoy, observe the generator reading the real
   tree anyway. RED observed FIRST with the scrub reverted.
4. S4 — bump `KIT_MEMORY_TREE_VERSION` (SEVEN carriers) and `KIT_MEMORY_RECALL_VERSION` (constant in
   `recall_conf.py` plus the marker in `tools/memory-recall/README.md`, which
   `check-kit-versions.sh` pairs against it).

## A DIVERGENCE from S1, decided before coding

S1 says absorb `_clean_git_env` by name. gov's lexicon table has no `clean` verb, and the pin is
shrink-only, so absorbing that spelling would red the naming gate. `TOOL-dRetiredFork-1` set the
precedent one unit ago: absorb the MECHANISM, use gov's own helper and wording. The name is
`_build_git_env` — `build` is declared, "create a new value and return it", which is exactly what it
does. The spec is amended first with its section 9 line, per M2.

## The scrub list, taken from gov's own hook rather than re-derived

`GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES
GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX` — eight, matching `.githooks/pre-push`, so the two halves
of one defect cannot disagree about what leaks.

## Acceptance

AC1-AC4, run rather than asserted.

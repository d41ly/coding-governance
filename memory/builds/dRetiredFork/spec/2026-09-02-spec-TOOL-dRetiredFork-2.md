# TOOL-dRetiredFork-2 — the git-environment leak, one defect at two legs

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

Absorb the environment scrub NicoCares carries as `nc carve-out 16/20` and `17/20`. These are ONE
defect at two legs, and gov has absorbed only the hook-side half of it. When a git hook invokes a
kit generator, git's exported variables — `GIT_DIR`, `GIT_INDEX_FILE`, `GIT_WORK_TREE` and their
siblings — reach the subprocess and point it at the wrong tree. gov's `run()` in
`tools/memory-tree/gen_build_index.py` passes no `env` at all, so it inherits whatever the parent
exported.

## 2. Scope (IN)

- **S1** — Absorb `_GIT_ENV_LEAKS` and `_clean_git_env` from NicoCares
  `scripts/gen_build_index.py:199-222` into `tools/memory-tree/gen_build_index.py`, and pass the
  cleaned mapping at the `run()` call site.
- **S2** — Absorb the three-line process-level pop from NicoCares
  `scripts/memory-recall/selftest.py:30-42` into `tools/memory-recall/selftest.py`, above the
  `sys.path` insert.
- **S3** — One arm per file that sets a `GIT_DIR` pointing at a decoy and observes the generator
  reading the real tree anyway. Observed RED first, with the scrub reverted.
- **S4** — Bump `KIT_MEMORY_TREE_VERSION` and `KIT_MEMORY_RECALL_VERSION` with their paired markers.

## 3. Non-goals (OUT)

- A shared helper across the two kits. A copy-installed kit carries its own inline code by house
  rule; `tools/lib/` is gov-internal and never travels.
- The hook-side scrub in `.githooks/pre-push`. gov already carries it, which is why `nc carve-out
  15/20` is stale and `DEPL-dRetiredFork-7` strikes it from NicoCares' register rather than fixing it.

## 6. Acceptance criteria

- **AC1** — When `GIT_DIR` names a decoy directory, `python3 tools/memory-tree/gen_build_index.py
  --check` reads the real tree and exits `0`; with the scrub reverted the same invocation fails.
- **AC2** — When `GIT_INDEX_FILE` is exported, `python3 tools/memory-recall/selftest.py` exits `0`.
- **AC3** — With no git variables exported, both commands produce output byte-identical to their
  pre-change output. Compared across `python3 tools/memory-tree/gen_build_index.py --check` runs.
- **AC4** — `bash tools/check-kit-versions.sh` exits `0` after both bumps.

## 7. Gates

`memory hygiene` · `build-index selftest` · `memory-recall kit selftest` · `kit version markers`.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.

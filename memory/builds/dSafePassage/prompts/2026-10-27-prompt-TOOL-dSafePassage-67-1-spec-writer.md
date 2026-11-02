**Serves:** research TOOL-dSafePassage-67

# Brief: the fixture factory's scratch repositories stop inheriting the machine's commit signing and hooks

## The prompt

No owner prompt: TOOL-dSafePassage-26's builder (`wf_3808fd72-4fb`, dfcef45a7) found this while closing and could not fix it, because its unit was CLOSED. The run adopts it under M10.

## The brief

### Goal

Every repository `tools/govkit/fixture_target.py` builds is independent of the machine's global git config for commit signing and hooks, as it already is for `core.autocrlf`. A fixture can then not pass, fail or hang because of the developer's `commit.gpgsign` or `core.hooksPath`.

**What was found.** `build_scratch_gov` (`tools/govkit/fixture_target.py:27-34`) pins `user.email`, `user.name` and `core.autocrlf` and nothing else. `build_target` (`:37-60`) commits `base` through `run_git` (`:21-24`), which runs with `check=False`. On a machine with a global `commit.gpgsign = true` and no usable key, the base commit fails silently and the target has no commit. A global `core.hooksPath` runs the developer's hooks inside every scratch repository. Since TOOL-dSafePassage-5 and -26, every selftest target and every upgrade-walk target goes through this factory.

### Items

1. **Author `memory/builds/dSafePassage/spec/2026-10-27-spec-TOOL-dSafePassage-67.md`** as a Tier-2 micro-spec: `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 6`, `**Derived:** TOOL-dSafePassage-26`, and `consumes-from` TOOL-dSafePassage-5 and -26. One mechanism: the factory pins what it inherits. Decide from the code whether to pin in `build_scratch_gov`'s config loop, per command (`-c`), or both. Also decide whether `run_git` should refuse a failed git command, by reading its callers: a fixture that silently loses its base commit is the `fixture-passes-by-finding-nothing` class. A choice you cannot derive is a fork in §8, with a recommendation. Give it one acceptance criterion observed on a planted global config (for example `GIT_CONFIG_GLOBAL` pointing at a file that sets both keys), with a Red-when, and a `New arm:` line.
2. **Add its row** to the README's authored `roster:units` table, with `**Derived:**` set to TOOL-dSafePassage-26's build pass.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- The spec is conforming: status header, `**Derived:**` line, §6 with a Red-when, §7 with a `New arm:` line, §10 reuse naming `build_scratch_gov` as the seam.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit and no stage into the real index.

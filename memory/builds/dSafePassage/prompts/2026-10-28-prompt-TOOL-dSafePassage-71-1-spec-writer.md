**Serves:** research TOOL-dSafePassage-71

# Brief: govkit selftest's staged-break copies take every sibling module they import

## The prompt

There is no owner prompt. TOOL-dSafePassage-42's builder (`wf_0d19d150-3dd`, c9baa97c8) found this, and the main loop confirmed it by reading the code. The run adopts it under M10.

## The brief

### Goal

Every staged-break copy in `tools/govkit/selftest.py` that runs a copied `upgrade_steps.py` also carries every sibling module that the module imports. Such an arm then goes red on the break it plants, not on an import error. A later new import cannot quietly break such an arm again.

**What was found.**
- The `[dSP-36]` arm at `tools/govkit/selftest.py:3630-3642` copies only `govkit.py` into its rooted walk copy (`:3632`) and writes a patched `upgrade_steps.py` beside it.
- `upgrade_steps.py` now imports `fixture_target` (TOOL-dSafePassage-5's factory, routed through by TOOL-dSafePassage-26). The copy therefore dies with `ModuleNotFoundError: fixture_target` and never prints the `isolation: FAILED` the arm requires, so `govkit selftest` reds.
- TOOL-dSafePassage-42's own arm copies `fixture_target.py` as well, which fixes one instance only.
- `grep -n 'shutil.copy(HERE / ' tools/govkit/selftest.py` shows four hand-picked copies: `:3632`, `:3659` (a loop over named files), `:3718` and `:3925`. Read each one and say which of them run a copied `upgrade_steps.py`.

### Items

1. **Author `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-71.md`**:
   - Header: Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 10`, `**Derived:** TOOL-dSafePassage-42`, no `consumes-from` on CLOSED units (name them as read-and-closed, as TOOL-dSafePassage-70 does).
   - One mechanism: a single helper that builds a staged-break copy of the govkit directory, with every module the copied file imports. Either `copytree` of `tools/govkit/` minus caches, or a copy driven by the module's own import list; decide from the code and say why. Every affected arm goes through that helper.
   - The class check: a cheap predicate that reds when an arm hand-picks sibling files for a copy that runs `upgrade_steps.py`. Run the candidate over the real tree first and record the count.
   - One acceptance criterion observed without the suite: run the `[dSP-36]` arm's body (or its fixture runs) through the helper and show it goes red with `isolation: FAILED`. Name the Red-when and the `New arm:` line.
2. **Add its row** to the README `roster:units` table.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- The spec is conforming: status header, `**Derived:**`, §6 with a Red-when, §7 with a `New arm:` line, §10 reuse.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit, and no staging into the real index.

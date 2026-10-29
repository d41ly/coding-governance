**Serves:** journal TOOL-dSafePassage-89

# TOOL-dSafePassage-89 — acceptance ledger

The unit as built, at spec rev-3. Product writes: `tools/govkit/govkit.py` (S1: the
`@functools.lru_cache(maxsize=None)` line above `derive_tool_root` removed, its docstring gaining the
not-memoised sentence; `functools` stays imported for `read_tree_modes`) and `tools/govkit/selftest.py`
(S2: the `[dSP-89]` check after `check_upgrade_steps`'s last `[dSP-1 AC5]` check). No function added,
so `memory/map/generated/symbols.json` is not regenerated.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1, AC3 and AC4 were
observed on node a (Windows 11) from this worktree's root over its working copy. The §4 probe ran
with its `tempfile.mkdtemp` given `dir=` the run's scratch, since this run writes no temp file outside
it; nothing else in it differs from §4's text.

Owed at the close: AC2, the moved-clone walk, which needs the foreign-prefix leg's own
`set_tool_root` sourced out of `tools/run-gates/foreign-prefix.gov.test.sh` (a slice of a suite file
a unit pass does not run); the RED-first observation of §7's `New arm:` line, the `[dSP-89]` check of
`check_upgrade_steps` staged red by the `@functools.lru_cache(maxsize=None)` line kept above
`derive_tool_root`; and the §7 legs at the bar. The arm probe below re-memoised the function in
process and edited no file, so it does not discharge the arm's staged-break observation.

**Evidences:** TOOL-dSafePassage-89
- AC1 — `python <scratch>/root_probe.py <scratch>` — printed `before the move -> ('tools', 'tools/govkit/registry.toml')` and `after the move -> ('scripts', 'scripts/govkit/registry.toml')`.
- AC2 — owed at the close (above); not observed in this pass.
- AC3 — `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import govkit; print(hasattr(govkit.derive_tool_root, 'cache_info'))"` — printed `False`. HEAD's `govkit.py` (`be00fcf48`) still holds `@functools.lru_cache(maxsize=None)` directly above `def derive_tool_root`, the red side.
- AC4 — `git grep -n -F "[dSP-89]" -- tools/govkit/selftest.py` — printed one line, `tools/govkit/selftest.py:3356:    check("[dSP-89] a root whose tool root moved between two reads reads the moved registry",`, inside `check_upgrade_steps`.
- Arm body probe — `python <scratch>/arm_probe.py <scratch>`, the `[dSP-89]` check's body over a scratch dir — as built printed `(True, [('pinned', 'pinned/govkit/registry.toml'), ('moved', 'moved/govkit/registry.toml')], '')`; with `derive_tool_root` re-wrapped in `functools.lru_cache(maxsize=None)` in process it printed `(False, [('pinned', 'pinned/govkit/registry.toml')], 'pinned/govkit/registry.toml: no registry at the working tree, and the rows are read from no other population')`.

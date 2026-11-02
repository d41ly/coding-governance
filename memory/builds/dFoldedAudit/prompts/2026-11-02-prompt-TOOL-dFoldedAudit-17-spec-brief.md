# Spec brief — TOOL-dFoldedAudit-17: origin/main reconciled into the run branch

**Serves:** research TOOL-dFoldedAudit-17

## The brief

### Goal
Write TOOL-dFoldedAudit-17's spec at Tier-1: the run branch takes `origin/main` by one `git merge`, and the eight paths both sides changed are reconciled additively, so the close's `--prepare` meets no conflict. The owner asked for the merge by git on 2026-11-02. Read `build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md` first; its tags bind. Header `order 170`, status OPEN. Commit nothing.

### Items
1. The merge. In a scratch clone of the run branch under `%TEMP%`, `git fetch origin` and `git merge --no-ff origin/main`. A trial merge of `origin/main` at `8a5328a9` on 2026-11-02 conflicted on exactly the eight paths below. A later tip that conflicts on any other path stops the unit.
2. `.memory-tree.conf`: keep both blocks, main's `SPEC_AC_ORDER_CUTOFF` (TOOL-dSafePassage-34) first and this build's `SPEC_SUPERSEDE_CUTOFF` (TOOL-dFoldedAudit-4) after it, each unchanged.
3. `tools/check-spec-tokens.py`: the docstring keeps both join entries, `supersede` then `ac-order`. `main()` reads both cutoff keys and returns 1 when either read refuses.
4. `tools/check-spec-tokens.test.sh`: `FLOOR_ASSERTIONS` is 215, main's 203 plus this build's twelve. Main's two history lines are kept, and this build's line is re-based to read `203 -> 215`.
5. `tools/drift-audit/drift_signals.py`: `cutoff_keys_armed` is 39. Main's `36 -> 37` history line is kept, and this build's line reads `37 -> 39` under decision TOOL-dFoldedAudit-16, naming both keys. The decision row says 36 -> 38 because it was written before the merge. Its substance, a raise of two for these two keys, is unchanged, and the row is not rewritten.
6. `memory/map/features/spec-tokens.md`: keep both paragraphs, main's criterion-order key first.
7. `memory/guides/SESSION-KICKOFF.md`: keep the branch's later `last-audit` stamp and main's `last-body-change`. The manifest checker's own audit then passes, or the stamp is re-taken by its rule.
8. Generated files are re-rendered, never merged. `memory/map/generated/symbols.json` comes from the map generator's `--write`, and `.governance/policy.json` from `tools/policy/policy.py mirror --write`. The mirror reads the catalogue at HEAD, so it may need a follow-up commit after the merge commit. Any other generated index the hooks name is handled the same way.
9. Every commit on main's tree needs Python 3.15, because main's resolver floor is 3.15. Export `GOV_PYTHON=C:/Users/d41ly/AppData/Roaming/uv/python/cpython-3.15.0b1-windows-x86_64-none/python.exe` in each commit's shell.

### Acceptance
Each item is one Scope line with its observation:
- `git diff --check` and a conflict-marker grep over the eight paths find nothing.
- `python tools/check-spec-tokens.py` prints both the supersede and the ac-order report lines.
- `python tools/drift-audit/drift_report.py --check` prints no `cutoff_keys_armed` line.
- `policy.py mirror --check` exits 0.
- The map generator's `--check` exits 0.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass. §7 names the legs these files sit under: `spec-tokens`, `drift-audit records`, `codebase map`, `policy mirror`, `memory hygiene`. Take their exact names from `tools/gate-legs.json`.

### Non-goals
No behaviour change on either side, no rewritten decision row, and no write outside this build's `spec/`.

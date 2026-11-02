# Fix brief — TOOL-dFoldedAudit-17 at rev-2

**Serves:** research TOOL-dFoldedAudit-17

## The brief

### Goal
Revise TOOL-dFoldedAudit-17's spec to rev-2, folding the builder's divergence recorded in `build/2026-11-02-build-TOOL-dFoldedAudit-17-2-builder-return.md`. Keep the status at INPROGRESS. Commit nothing.

### Items
1. S1's clone copies the run repository's merge drivers after it sets `core.hooksPath`. That is `merge.rows.driver` and `merge.ours.driver`, read from `git -C <run repo> config --get-regexp '^merge\.'`. Without them the clone conflicts on three `.gitattributes`-routed paths besides the eight. The builder confirmed that with both drivers set, `git merge-tree --write-tree --name-only` prints exactly the eight paths.
2. The interpreter: `C:/Users/d41ly/AppData/Local/Programs/Python/Python315/python.exe` (3.15.2) replaces the nonexistent uv path. `python3` on PATH is also 3.15.2. Cite whichever the resolver's order reaches first.
3. The CLOSED flip stays with the main loop after the fast-forward, as §3 already states. The build brief's contrary sentence is withdrawn by the main loop's re-dispatch note, so the spec needs no change here beyond stating the flip once.
4. `origin/main` has moved to `84acebdc`. The builder found that none of the eight paths changed between `8a5328a9` and that tip, and that the figures hold: floor 215, pin 39, `last-body-change` `201eb127`. Record that reading in the conflict-set section. The rule for a later tip stays as written.

### Acceptance
Rev-2 with a §8 revision-log line for each item. S1 sets both drivers, the interpreter path exists, and AC1's expected set stays the eight.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No change to the resolutions themselves, and no write outside this build's `spec/`.

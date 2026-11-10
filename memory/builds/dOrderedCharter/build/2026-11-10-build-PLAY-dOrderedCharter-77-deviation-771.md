# PLAY-dOrderedCharter-77 deviation 771 — the overlay fixture's level-3 expectation reads the repository markers

**Serves:** deviation PLAY-dOrderedCharter-77

- **Departs from:** `PLAY-dOrderedCharter-77@rev-2` [Design]
- **Hand-off:** spec-to-code
- **Before:** S6 changes `tools/playbook/overlay.py` at `arm_policy_at_head` alone, and AC6 runs `python tools/playbook/overlay.py --fixture` expecting exit 0.
- **After:** `arm_add_level_3` in the same file also expects the `<!-- gov:repo -->` and `<!-- /gov:repo -->` lines around the repository unit it renders, the markers `render_playbook.py` writes around each run of repository units.
- **Cause:** builder discovery
- **Reason:** PLAY-dOrderedCharter-34 made the render mark each run of repository units, and the arm still expected the bare four lines, so the fixture failed one expectation before this pass touched it and AC6 could not read exit 0. The arm's claim, that the repository unit renders after gov's level-3 units, is unchanged.
- **Evidence:** with the old expectation restored in the worktree, `overlay.py --fixture --plant add-level-3` printed `FAILED · the level-3 repository unit renders after gov's level-3 units` and the six-line list; with this pass's expectation the whole fixture ended `overlay: fixture · green · 0 expectation(s) failed`.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-34

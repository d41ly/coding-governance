# TOOL-aMeasuredDrag-6 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-6

No merge bar and no self-test suite ran in this pass. The pass started at b4ef72d0. AC1, AC2 and AC3
ran as the spec's own block in Git Bash, saved to the session scratchpad as `md6-probe.sh`, in a clone
under the `md6` folder of `%TEMP%`. The clone was made from the worktree at b4ef72d0, and this pass's
five files were copied over it and committed there, so the clone's `HEAD` held this commit's content
and `HEAD^` was b4ef72d0. The ledger figures were then filled in. The build README and this spec's
records region were rendered by `--write` in a second clone, `md6r`, and copied back. `--write` never
ran in the worktree.

**Evidences:** TOOL-aMeasuredDrag-6
- AC1 — `rc=0` — `diff "$S/md6-write-before.txt" "$S/md6-write-after.txt"` printed nothing. Both
  files hold `rc=0` and `tree 6d1a450e2f7a4ccaaa7cbcc68a12d5061e108dab`, so the two renders left the
  same artifacts. An earlier run without the spec's CLOSED flip in the clone differed in one cell:
  LIVE.md's Landed-unclosed count for aMeasuredDrag read 1 after and 0 before. The new comment in
  `collect` cites this unit's id while the unit was open. With the flip in the same commit, the cell
  reads 0 both ways.
- AC2 — `collect` — `diff "$S/md6-collect-before.txt" "$S/md6-collect-after.txt"` printed nothing.
  Both end in `collect e1d5e24e275e1fe98488c787eb6a9e713f0e35026dc662c3463bf2f00bfd9942`, with the
  `aCarriedStopX` fixture committed in the clone. The probe can go red: with `if sep:` flipped to
  `if not sep:`, `collect` raised `Problem` on `memory/builds/aBatchedArm/README.md` and printed no
  `collect` line.
  **The spec's stated red does not fire.** With all three lookups mutated to
  `[q for q in tracked if q.startswith(f"{m}/builds/{slug}")]`, a key with no separator, the hash
  stayed `e1d5e24e…`. Every predicate re-tests `f"{m}/builds/{slug}/..."`, so a list that carries
  extra paths filters back to the same members. AC2 catches a list that drops a build's paths, not one
  that adds a prefix sibling's paths. This is reported for the spec writer, and the spec is left
  unedited.
- AC3 — `/usr/bin/true` — `collect` timed in the clone, `PYTHONHASHSEED` unset, one sample each:
  - after, this commit's generator: 10.18 s, PINNED at b4ef72d0 plus this pass's diff.
  - before, the generator of b4ef72d0: 12.41 s, PINNED at b4ef72d0.
  - spawn baseline: 0.275 s per 10 runs of `/usr/bin/true` before the timings and 0.316 s after,
    PINNED at b4ef72d0.
  The spec's figures are 11.46 s for `collect` and 0.28 s per 10 runs of `/usr/bin/true`, both
  PINNED at 6d98c39ca. The after time is below the before time. A first sample in `md6-probe.sh`
  read 10.07 s after and 42.72 s before, beside a 2.866 s baseline, PINNED at b4ef72d0. That machine
  was under load, so the second sample stands.

**Owed to the close (the main loop, after every unit is terminal):**
- No new arm. Spec §6 adds none, so no RED-first observation is owed.
- The gates in spec §6: `build-index selftest`, `tier2-review self-test`, `policy fixtures`, and
  `verdict epoch (kit version dates the engine)` at the push boundary.

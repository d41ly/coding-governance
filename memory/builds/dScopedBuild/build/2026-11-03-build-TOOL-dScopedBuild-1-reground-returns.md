**Serves:** research TOOL-dScopedBuild-1

# dScopedBuild — the re-ground writer's return, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground.md), extracted by script from the agent's transcript and not retyped. The cross-check record it folds is [`2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck`](2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck.md).

## Spec 1

I revised TOOL-dScopedBuild-1 to rev-4. The only content change is the §3 non-goal at sb1:108. Its owner was the executor (TOOL-dWellOiledMachine-6) and is now TOOL-dDeclaredLoop-3 S5's writer, `write_transition`, which the `build.exit` command item reaches through the loop kit's verb `python loop_transition.py record`. It is still a non-goal, the evidence sentence after it is unchanged, and no fork was opened or resolved.

**Re-reading both sides at `66c5b8dbf`:** row 1 holds, so nothing was refused.
- **wm6:** `grep -ci transition` prints 0. Lines 118-119 cover only a `reconcile` row's probe and its landed effect as the witness.
- **dl3:60:** names "The writer, `write_transition`" and the `loop_transition.py record` argv.
- **wm3:60:** names "the loop kit's verb `python loop_transition.py record`".
- **§3 Edges:** they don't name wm6 or the transition record, so I left them alone.

**Other changes:**
- The **Status:** line now reads `rev-4 · 2026-11-03`, with every other field unchanged.
- §9 has a new rev-4 line in the existing form, ending "by the brief prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground.md".

**Acceptance:**
- `wc -c` gives 28037, under 49152.
- `grep -n "the executor's (TOOL-dWellOiledMachine-6)"` prints nothing.
- The hygiene gate with `--staged` ran over a copy of the index with only this spec staged; I deleted the copy afterwards. It exits 1, on check 9 only: the build index needs a re-render. That one is yours: run `python tools/memory-tree/gen_build_index.py --write`. It lists `memory/LIVE.md`, `memory/builds/dScopedBuild/README.md` and `memory/builds/dShippedRelease/README.md` as stale. The dShippedRelease one probably comes from the worktree's existing uncommitted edit to `DEPL-dShippedRelease-4`, not from this spec. Nothing else the gate reports names my spec.

**Parent text that looks wrong:** I edited none of it; the cross-check record already parks both items.
- wm6:179's edge still says "the epoch read §8 F4 asks for".
- wm6 rev-5 cites F6 as `tr2:337-354`, but F6 runs from :340 to :357.

The only file I changed is `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dScopedBuild\spec\2026-11-01-spec-TOOL-dScopedBuild-1.md`. Nothing is committed or staged into the real index.

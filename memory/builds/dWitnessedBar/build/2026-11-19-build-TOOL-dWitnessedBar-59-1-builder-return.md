**Serves:** journal TOOL-dWitnessedBar-59

# TOOL-dWitnessedBar-59 — builder return 1 (run `wf_d197bf6c-a6a`), a divergence, nothing committed

## Why

DIVERGENCE: spec §4 "Files touched (estimate)" lists only `tools/govkit/selftest.py`. It leaves out `memory/builds/dWitnessedBar/README.md`, and the pass commit has to write that file. Flipping the spec's status to CLOSED makes `python tools/memory-tree/gen_build_index.py --write` rewrite the unit's row in the README's Units table from INPROGRESS to CLOSED. I saw this in a clean clone at base `59e882afd`, where the index wrote 1 artifact, that README. The brief also requires every file the index rewrites to go into the pass commit. When I declared the path with `bash tools/unattended/unattended.sh --dispatch dWitnessedBar --pass TOOL-dWitnessedBar-59 --writes memory/builds/dWitnessedBar/README.md`, it refused (rc=1): "UNATTENDED check 49 FAILED — --dispatch declares a path a sibling pass in the same group already declared ... memory/builds/dWitnessedBar/README.md also in 59e882af TOOL-dWitnessedBar-1". That refusal is binding, so I stopped. Other paths I checked: the codebase map was current (`gen_map.py --check` exit 0), `tools/govkit/selftest.py` is not on the kickoff manifest's `watch:` list, and the step code matches the spec's §4 Evidence, so nothing else diverges. What has to change: §4 Files touched must name `memory/builds/dWitnessedBar/README.md`, and order 23's two units cannot both hold it. Either units 1 and 59 run in sequence, with 59 after 1 lands and its reservation is released, or the README's regeneration goes to whichever of the two commits last.

## Summary

No commit. I restored every path I changed, so the worktree is back at base 59e882afd, with only the files that were already modified or staged when I started (help/reference/drive.md, help/reference/units.md, RUN.md). The `--brief` verb reported the brief already recorded and unchanged. The failed `--dispatch` wrote no row.

What was built and tested before the stop. In `check_inherited_red_step` in `tools/govkit/selftest.py` I added:
- An AC1 target, `ir59-ac1`: the up must write every-red.
- An AC2 target, `ir59-ac2`: the witness must exit 1 with `assigns` once and `not an assignment` nowhere, and the up must leave exactly `A=1\nB=2\n`.
- A parity row `INHERITED_RED=park\rINHERITED_RED=land\n`, labelled `lone-cr`, which also checks that the hook's value is `park\rINHERITED_RED=land`. The row-count check went from 11 to 12, and the WHAT IT DOES NOT CHECK comment no longer names a lone CR.

That diff is saved at C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/unit59-selftest.patch. The acceptance ledger draft is at C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/unit59-acceptance-ledger.md, ready for the next dispatch.

Checks that ran:
- `python -m py_compile` passed on the edited selftest.py.
- The scratch probe C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe59.py ran the step under `-I` over the AC1 and AC2 fixtures. It also cut `read_policy_key` from `.githooks/pre-push` the way the arm does, and ran it under the resolved bash after the K=plain sentinel read `plain`. This stands in for `govkit selftest`.
- On the live step, AC1, AC2 and AC3 all passed.
- A staged copy of the step, with its 5 `.split("\n")` calls changed to `.splitlines()`, failed all three. AC1 wrote own-mixed-contended. AC2's witness named `not an assignment` and its up kept ` INHERITED_RED=land`. AC3's read_value read `land`. That is the RED for the spec's New arm, seen in the probe only.

Still owed to the main loop at the close: the new arm's RED-first and GREEN observation inside the suite, plus the legs of §7 (govkit selftest, govkit refusal join, govkit acceptance matrix, recall floor arms, policy fixtures, memory hygiene).

Not run: the M6 `gotchas --for-diff HEAD~1..HEAD` check, because there was no commit to run it over. The clean clone (%TEMP%/c59, its worktree %TEMP%/c59w) and the fixture directory %TEMP%/ir59p are deleted.

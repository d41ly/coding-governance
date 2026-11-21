# TOOL-dSettledStage-3 — acceptance ledger

**Serves:** journal TOOL-dSettledStage-3

No merge bar, no self-test suite and no arm of `tools/push-main.test.sh` ran in this pass. The pass
started at f8ee4c5d9. Each probe ran from the worktree root in Git Bash, its fixture repositories
under `%TEMP%`: arm 45's body run by hand over a named lander, the two functions cut with arm 38's
`sed -n` idiom, and the attended lander run over a clone of this worktree at HEAD with a stub
pre-push hook that refuses, the built lander and arm 44's planted `regen.py` copied in and committed
first. The base lander is `git show 41e57fca5:tools/push-main.sh`.

**Evidences:** TOOL-dSettledStage-3
- AC1 — `index.lock` — the attended landing of the built lander over that clone minted, walked gov
  first, printed git's `Unable to create ... index.lock` line and then
  `push-main: could not stage the regenerated outputs. Aborted (no push).`, and exited 1; the probe
  then printed `locked=1`, `dirty=1` and `unpushed=1`, and no `gating + pushing` line was printed.
  This is a hand-built fixture of the lander, not arm 44; arm 44's own RED and GREEN are owed to the
  close, and the base lander's RED in this fixture was not re-run here.
- AC2 — `write_merge_fold` — over the built lander the hand-run arm 45 body printed `lock-dirty=1`,
  `lock-refuses=1`, `stage-rc=2`, `fold-rc=1`, `head=same`, `free-rc=0` and `free-moved=1`. Over
  the base lander it printed `stage-rc=1` and `fold-rc=0` under the same lock.
- AC3 — `git status` — with `.git/index` overwritten by garbage bytes `git status` exited 128, and
  the cut `write_staged_change` answered 2 over the built lander and 1 over the base lander.
- AC4 — `write_staged_change; staged=\$?` — the spec's three `grep -c` commands over the built
  lander printed what the criterion names for TOOL-dSettledStage-3: no site keeps
  `if write_staged_change; then`, and each site carries its call and its stage refusal.
- AC5 — `--no-verify|could not commit|could not fold` — `diff` of the base lander's `git grep`
  output against the built lander's `grep -E` output printed nothing.
- AC6 — `memory/project/unarmed-branches.txt` — the mint and gov-first stage refusals each have a
  row and the regen stage refusal has none; `check-arms.py --emit-pin` emitted exactly the mint and
  gov-first stage refusal signatures, so arm 44 arms the regen one.
- AC7 — `failed-stage-reads-as-nothing-staged` — `gotchas.py --for-paths tools/push-main.sh` names
  the class, and `memory/gotchas/INDEX.md`, `memory/map/features/push-main.md` and
  `memory/map/generated/MAP.md` each name it after `gotchas.py --write` and `gen_map.py --write`.
- AC8 — `write_staged_change() {` — its return-contract comment names `2 staging failed`, and the
  header paragraph the spec's `sed -n` prints says a stage which fails refuses the landing with no
  push.

**Also probed:** `bash -n` passed over `tools/push-main.sh` and `tools/push-main.test.sh`. No
function is minted, so the naming lexicon was not asked.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/push-main.test.sh` 44, covering AC1: RED with the lander of 41e57fca5 restored,
  GREEN once restored.
- New arm `tools/push-main.test.sh` 45, covering AC2: RED with the helper and fold of 41e57fca5
  restored, GREEN once restored.
- The gates section 7 names, the `push-main self-test` and `harness arms` among them.

**Observed at the close (main loop, 2026-11-19):** each RED ran in a clone under `%TEMP%` whose staged break was COMMITTED inside the clone, because the suite's fixtures clone the source repository's HEAD and never see a working-tree edit. Each GREEN ran in a clone at `8e2ad2e5a`, this build's last unit commit. Logs are in the session scratchpad.
- Arm 44 (AC1) — `FAIL — 44` with the `41e57fca5` lander committed in the clone: the landing reached the push over the locked stage. `ok — 44` at `8e2ad2e5a`.
- Arm 45 (AC2) — `FAIL — 45` with the `41e57fca5` lander committed in the clone; `ok — 45` at `8e2ad2e5a`.
- Inherited, not this build's: arms 37, 39 and 40 of `tools/push-main.test.sh` fail at the pristine base `12764ec21` as at `8e2ad2e5a` (DERIVED at observation). Arm 40's own plant step fails on node d at both (`plant-rc=1`). The suite is held, so the bar that landed `12764ec21` never ran it. Arm 26 fails at the base and passes at `8e2ad2e5a`, its mint commit's line-ending case being the class this build closes.

**Serves:** journal TOOL-dSafePassage-27

# TOOL-dSafePassage-27 — acceptance ledger

The unit as built, at spec rev-2. At this branch's HEAD the prepared path already took one snapshot
before the walk and kept it across the regeneration, under the name `rgsnap` (TOOL-dSafePassage-25,
deviation 170, whose follow-through names this unit). This pass renames it to the spec's `gfsnap` in
`cmd_prepare`, so §4's block is the code and `rgsnap` names only the attended path's regeneration
snapshot, and rewrites the comment above it. `tools/push-main.test.sh` gains arm 36, inside arm
34's govkit guard and behind the regen.py guard: a committed `regen.py` that exits 1 after a passing
walk refuses `--prepare` with the branch unmoved and an empty `git status --porcelain`, and the
retry with `regen.py` reverted exits 0 with a second parent. That is the `New arm:` line's arm.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed
by a hand-built copy of arm 36's fixture (scratch `probe27.sh`: a bare clone of this worktree's HEAD
under `%TEMP%/d27g` and `%TEMP%/d27r`, the lander under test copied in and committed on `main`, a
`feat` branch with the failing `regen.py`, then the retry), run once with this pass's lander and
once with the staged red (scratch `red27.py`: a lander copy whose regeneration refusal cleans
against a snapshot taken after the walk). On node d (Windows, Git Bash).

SPEC NOTE. As TOOL-dSafePassage-25's ledger recorded, the walk in gov's tree writes no before-image
and no order, so AC2's `ls-tree` over `.governance/steps .governance/outbox` reads `[]` on both
landers and is no coverage alone; the discriminating observation is the retry's exit, which the red
lander fails because the leftover receipt dirties the tree `--prepare` requires clean. Reading AC2's
`ls-tree` clause that way is TOOL-dSafePassage-42's hand-off (§3 Edges).

Owed at the close: `push-main self-test` with arm 36's RED-first observation (staged by `red27.py`'s
shape), `spec tokens`.

**Evidences:** TOOL-dSafePassage-27
- AC1 — this pass's lander: `could NOT be regenerated`, `fail-rc=1`, `unmoved=1`, `status-after-refusal=[]`, and no gov-first refusal line, so the walk passed. Red: `fail-rc=1`, `unmoved=1`, `status-after-refusal=[?? .governance/install.json]`.
- AC2 — this pass's lander: `retry-rc=0`, `merge=1`, `retry-governance=[.governance/deploy.toml .governance/install.json .governance/policy.json .governance/policy.toml]`, `steps-outbox=[]`. Red: `retry-rc=1`, `steps-outbox=[]`.
- AC3 — `git grep -n -e "gfsnap" -e "rgsnap" -- tools/push-main.sh` printed `cmd_prepare`'s `gfsnap` at its one assignment (1061), both refusal branches (1064, 1073) and the removal after `run_regen` (1078); `rgsnap` only at 1280, 1283 and 1287, the attended path; the attended path's own `gfsnap` (TOOL-dSafePassage-25) at 1261-1268.
- Syntax — `bash -n` over both files exits 0.

**Serves:** journal TOOL-dSafePassage-25

# TOOL-dSafePassage-25 — acceptance ledger

The unit as built, at spec rev-2. In `tools/push-main.sh`: the prepared path's refused gov-first
walk runs `remove_new_untracked "$rgsnap"` after its `git reset -q --hard "$t"`, against the snapshot
TOOL-dSafePassage-8 already takes before the walk (deviation 170); the attended path takes a `gfsnap`
before `run_gov_first`, runs `remove_new_untracked "$gfsnap"` after its reset on refusal, and
removes the snapshot on success. `tools/push-main.test.sh` arm 34 gains, after the planted refusal,
an empty `git status --porcelain`, then a retry with the plant removed that exits 0 and prepares a
merge whose `.governance` listing equals the clean run's: the `New arm:` line's arm.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed
by a hand-built copy of arm 34's fixture (scratch `probe25.sh`: a bare clone of this worktree's
HEAD under `%TEMP%/d25n`, the lander under test copied in and committed on `main`, a `feat`
prepare, a `plant` branch with the failing-witness row, then the retry), run once with this pass's
lander and once with the lander at HEAD~ (the mint's refusal shape) as the staged red. On node d
(Windows, Git Bash).

SPEC NOTE. In gov's tree the walk at this HEAD writes no before-image and no order, so
`.governance/steps` and `.governance/outbox` are empty in every prepared merge and AC2's `ls-tree`
over them reads an empty set on both landers: that comparison alone is no coverage. The arm compares
the whole `.governance` listing instead (a superset holding the receipt), and the discriminating
observation is the retry's exit, which the base lander fails because the leftover receipt dirties
the tree `--prepare` requires clean.

Owed at the close: `push-main self-test` with arm 34's RED-first observation (staged by a lander
copy whose gov-first refusal drops `remove_new_untracked`), `spec tokens`.

**Evidences:** TOOL-dSafePassage-25
- AC1 — this pass's lander: `clean-rc=0`, `govkit/planted-witness-fails`, `unmoved=1`, `status-after-refusal=[]`, the fixture's `git status --porcelain` after the refused `bash tools/push-main.sh --prepare --slug fx`, read as arm 34 reads it (`tools/push-main.test.sh:1276`). Red, the HEAD~ lander: `plant-rc=1`, `unmoved=1`, `status-after-refusal=[?? .governance/install.json]`.
- AC2 — this pass's lander: `retry-rc=0`, `retry-tree` and `clean-tree` both `[.governance/deploy.toml .governance/install.json .governance/policy.json .governance/policy.toml]`, `retry-merge=clean`; over `.governance/steps .governance/outbox` both read `[]`. Red, the HEAD~ lander: `retry-rc=1`.
- AC3 — `git grep -n -A3 "run_gov_first" -- tools/push-main.sh` printed the call at 1061 with `remove_new_untracked "$rgsnap"; rm -f "$rgsnap"` at 1063, and the call at 1261 with `remove_new_untracked "$gfsnap"; rm -f "$gfsnap"` at 1263; its other hits are the function's comment and definition.
- Syntax — `bash -n` over both files exits 0.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, `tools/push-main.test.sh` arm 34. The break was `brk-25` (`cf4c5b511`): cmd_prepare's gov-first refusal without `remove_new_untracked`, which is the mint refusal's shape. It gave `FAIL — 34 the prepared merge lacks gov's receipt …`, reading `plant-left=[?? .governance/install.json] retry-rc=1`. GREEN at `83817478f`: `ok — 34 …`.

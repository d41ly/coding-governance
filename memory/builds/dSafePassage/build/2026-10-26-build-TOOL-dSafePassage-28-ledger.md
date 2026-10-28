**Serves:** journal TOOL-dSafePassage-28

# TOOL-dSafePassage-28 — acceptance ledger

The unit as built, at spec rev-3. `tools/push-main.test.sh` gains arm 37 and its table
`PREPARE_REFUSALS`, one `stage|plant|expect` row per `return 1` line of `cmd_prepare` from its
`run_gov_first` call to its end, in source order: gov-first, regeneration, commit-tree
(`unplantable:`), merge-loss, compare-and-swap, final checkout (`unplantable:`). The arm derives
that count from the lander beside the suite and reds when it is zero or differs from the table's
rows. Each plantable row builds `build_regen_fixture`'s clone, plants its refusal on `feat`, runs
`--prepare --slug fx`, and asserts exit 1, the stage's own refusal line (so a case refused at an
earlier stage cannot pass for it), the branch where `expect` says, `feat` checked out, an empty
`git status --porcelain` and no untracked path under `.governance`. The two unplantable rows print a
`skip` line naming the gap on every run. The lander is unchanged.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. The arm was run alone by a
probe assembled from the suite file (scratch `mk37.sh` -> `probe37.sh`: the suite's header facts,
inline resolver, `ok`/`bad`, allow-hook, kit discovery, `build_regen_fixture`, then arm 37 verbatim),
fixtures under `%TEMP%/d28`, against this worktree's committed HEAD, on node d (Windows, Git Bash).
It stands in for the `push-main self-test` leg for this arm only.

Owed at the close: `push-main self-test` and `spec tokens`, and arm 37's RED-first observation on
each of its three staged breaks (§7): a lander copy with one extra `return 1` after the walk and no
row; a lander copy whose regeneration refusal cleans against a snapshot taken after the walk; the
compare-and-swap row's `expect` set to `old`.

**Evidences:** TOOL-dSafePassage-28
- AC1 — `awk '/^cmd_prepare\(\)/,/^}/' tools/push-main.sh | sed -n '/run_gov_first/,$p' | grep -c 'return 1'` printed `6`; the arm printed `ok — 37 cmd_prepare refuses 6 way(s) after the gov-first walk, and PREPARE_REFUSALS carries a row for each`; `git grep -n "PREPARE_REFUSALS" -- tools/push-main.test.sh` shows the table at 1351. Over a lander copy with one extra `return 1` after `rm -f "$gfsnap"` the same pipeline printed `7`, which the table's six rows red.
- AC2 — the probe printed `ok — 37 gov-first`, `regeneration`, `merge-loss` (`branch old`) and `compare-and-swap` (`branch moved`): `its own refusal exits 1 with the branch … and checked out, and leaves a clean tree`, `fail=0`. The `git grep` of the four stage names shows rows 1352, 1353, 1355 (`old`) and 1356 (`moved`). Staged red, the compare-and-swap row's `expect` set to `old` (scratch `red37.sh`): `FAIL — 37 compare-and-swap … rc=1 stage=refused branch=[a9ec715a…] old=[e90461af…] head=feat clean=1 governance=clean`, `fail=1`.
- AC3 — each plantable case printed `governance=clean`, `git ls-files --others --exclude-standard -- .governance` empty after the refusal.
- AC4 — the probe printed `skip — 37 commit-tree: no fixture fails git commit-tree or git update-ref without a lander switch, so this refusal is NOT covered` and `skip — 37 final checkout: no fixture fails the closing git checkout without a lander switch, so this refusal is NOT covered`.
- Syntax — `bash -n tools/push-main.test.sh` exits 0.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, `tools/push-main.test.sh` arm 37. The break was a lander copy with one extra refusal branch and no table row. It gave `FAIL — 37 cmd_prepare refuses 7 way(s) after the gov-first walk (0 means the anchor matched nothing), PREPARE_REFUSALS carries 6 row(s)`. Restored: `ok — 37 … 6 way(s)`. That one red makes the line observed; I did not stage its other two breaks or run the four per-row fixture landings.

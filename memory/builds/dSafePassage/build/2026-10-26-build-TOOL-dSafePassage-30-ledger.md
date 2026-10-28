**Serves:** journal TOOL-dSafePassage-30

# TOOL-dSafePassage-30 — acceptance ledger

The unit as built, at spec rev-3. In `tools/govkit/upgrade_steps.py`: `read_target_repositories`
returns one `{"git_dir", "reached_by"}` row per repository a git command run in the target can
enter, the target's own first: each gitlink (`ls-files -s -z`, mode `160000`) whose working
directory holds a `.git` entry, resolved by `rev-parse --absolute-git-dir` and walked again over
that repository's index, and every directory under the target's common dir's `modules/` holding a
`config`, at any depth, populated or not (a found submodule's own `modules/` walked likewise), each
listed once by its resolved path. A failing git call returns the call and its exit, which
`check_target_local_config` refuses on. `read_target_local_config` runs its read as
`git -C <target> --git-dir=<dir>` over each row, the dir relative to the target where it sits
inside it, so an origin reads `.git/modules/<name>/config`, and carries `reached_by` as a fourth
field; `check_target_local_config` appends `(submodule <path>)` to a submodule row's `<key> in
<file>`. The one `raise Refusal` site is unchanged. The `isolation` family gains a `status.py` step
program (`git status --porcelain` in the target) and the `submodule-filter`, `submodule-nested`,
`submodule-unpopulated` plants with their `-stub` twins. `tools/govkit/selftest.py`'s
`check_step_isolation` gains the six rows, tagged `[dSP-30]`. `help/upgrade-steps.md` "What a step
can reach" says the check reads each submodule's config. Deviation 171 records the gitlink read's
`core.fsmonitor=false`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, git 2.54.0.windows.1) by the fixture CLI or a `python` probe of the changed code;
fixture repositories sit under `%TEMP%`, with system and global config off.

Owed at the close: `govkit selftest` (the `[dSP-30]` rows and the New arm's RED-first observation,
staged by the `-stub` twins), `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`,
`recall floor arms`, `encoding posture`, `lexicon naming predicates`, `policy fixtures`, `spec tokens`.

**Evidences:** TOOL-dSafePassage-30
- AC1 — `fixture isolation --plant submodule-filter`, rc 1: `isolation: fixture/status · refused · fixture/status up: the target's own git config declares what git runs as a program or sends as a credential, filter.canary.clean in .git/modules/sub/config (submodule sub), so nothing was spawned: remove it, or run the step attended`, `isolation: filter canary: absent`. `--plant submodule-filter-stub`, rc 1: `isolation: fixture/status · up · ok`, `isolation: filter canary: present · filter-clean`. Red when: with `read_target_repositories` cut to its first row in process, the same plant printed `filter canary: present · filter-clean` and `isolation: FAILED · the step was not refused naming filter.canary.clean in .git/modules/sub/config (submodule sub)`.
- AC2 — `--plant submodule-nested`, rc 1: `... filter.canary.clean in .git/modules/sub/modules/inner/config (submodule sub/inner), so nothing was spawned ...`, `isolation: nested canary: absent`. `--plant submodule-nested-stub`, rc 1: `isolation: nested canary: present · filter-clean`. Red when: with the population cut to rows one level deep, `isolation: FAILED · the step was not refused naming filter.canary.clean in .git/modules/sub/modules/inner/config (submodule sub/inner)`.
- AC3 — `--plant submodule-unpopulated` (the submodule deinitialised, its `.git/modules/sub/config` kept), rc 1: `... filter.canary.clean in .git/modules/sub/config (submodule sub), so nothing was spawned ...`. `--plant submodule-unpopulated-stub`, rc 1: `isolation: fixture/status · up · ok`. Red when: with the `modules/` rows dropped, `isolation: FAILED · the step was not refused naming filter.canary.clean in .git/modules/sub/config (submodule sub)`.
- AC4 — `git grep -n -i "submodule" -- help/upgrade-steps.md` printed lines 52 to 55 and 67 inside "What a step can reach": "The check reads the config of every repository git can enter from yours, each submodule's included".
- Population probe — `read_target_repositories` over a scratch superproject holding a non-absorbed gitlink `emb` (its `.git` a directory in the work tree) returned the target's `.git` and `emb/.git` with `reached_by` `emb`, and `read_target_local_config` returned `('emb/.git/config', 'core.ignorecase', 'true', 'emb')`; over a directory outside any repository it returned `` `git -C <dir> rev-parse --absolute-git-dir` exits 128: fatal: not a git repository ``.
- Unbroken neighbours — `fixture isolation` (base) rc 0, `--plant hook` rc 0 `hook canary: absent`, `--plant local-filter` and `local-include` refused as before, `--plant local-fsmonitor` rc 1 `fsmonitor canary: absent` and `core.fsmonitor=false · not refused · git add exits 0` (deviation 171), `--plant local-fsmonitor-stub` and `local-filter-stub` rc 1 naming their canaries, `--plant callers` rc 0, `--plant token` rc 1 refused.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_isolation`, cut to `submodule-unpopulated`. Break: the `modules/` walk emptied (`walks = []`). RED: `FAIL [dSP-30] fixture isolation submodule-unpopulated exits 1, … — isolation: fixture/status · up · ok` with `isolation: FAILED · the step was not refused naming filter.canary.clean in .git/modules/sub/config (submodule sub)`. The dSP-53 and dSP-54 staged-copy arms also go red because their copy text no longer applies. GREEN restored: FAILURES=0, 45 ok.

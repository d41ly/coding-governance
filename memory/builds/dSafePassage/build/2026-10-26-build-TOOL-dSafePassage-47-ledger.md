**Serves:** journal TOOL-dSafePassage-47

# TOOL-dSafePassage-47 — acceptance ledger

The unit as built, at spec rev-3. S1 to S3 and S6 needed no code: TOOL-dSafePassage-45's pass
(c0952b6f9) built the walk's test as this unit's reading, per S5 ("whichever pass first builds the
walk's test builds this one"): `read_target_repositories` in `tools/govkit/upgrade_steps.py` takes a
`modules/` directory as a candidate by `HEAD` file beside `objects/` and `refs/` directories, runs no
git command to classify it, descends a non-candidate as a name segment and a candidate's own
`modules/` only; each candidate's `config --list` read refuses on any non-zero exit naming
`<c>/config` and the exit, through `read_target_local_config`'s one `raise Refusal`. The same commit
wrote S6's sentence into `help/upgrade-steps.md`. This pass adds S4's `submodule-name-slashed` plant
(a de-initialised submodule named `lib/x`, its config setting `filter.canary.clean`, so its
repository is reached only through the `lib/` segment) and §7's arm in `tools/govkit/selftest.py`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, git 2.54.0.windows.1) over this worktree, the fixture's own targets under `%TEMP%`.

Owed at the close: the RED-first observation of the `New arm:` line (the `[dSP-47]` checks in
`tools/govkit/selftest.py`'s `check_step_isolation`); `govkit selftest`, `govkit refusal join`,
`govkit acceptance matrix`, `govkit selfcheck`, `recall floor arms`, `encoding posture (text IO
names its encoding)`, `lexicon naming predicates`, `policy fixtures` and `spec tokens (a spec's own
names resolve)`.

**Evidences:** TOOL-dSafePassage-47
- AC1 — `python tools/govkit/upgrade_steps.py fixture isolation --plant submodule-ref-named-config` exited 0 and printed two population rows, `.../t/.git · reached by the target` and `.../t/.git/modules/sub · reached by sub`, none under `refs/`, `objects/` or `logs/`, then `isolation: fixture/status · up · ok`.
- AC2 — the same with `--plant submodule-config-malformed` exited 1 and printed `fixture/status · refused · ... ``git config --list`` over .git/modules/sub exits 128, so .git/modules/sub/config does not read: fatal: bad config line 14 in file .git/modules/sub/config, so nothing was spawned`. A scratch copy of the kit whose walk classifies by `git --git-dir=<c> rev-parse --git-dir`'s exit printed `fixture/status · up · ok` and `isolation: FAILED · the step was not refused naming .git/modules/sub/config as a file git cannot read, or it spawned`, exit 1.
- AC3 — the same with `--plant submodule-name-slashed` exited 1 and printed `refused · ... filter.canary.clean in .git/modules/lib/x/config (submodule lib/x), so nothing was spawned`. A scratch copy whose walk never descends a non-candidate printed `fixture/status · up · ok` and two `isolation: FAILED` lines naming `filter.canary.clean in .git/modules/lib/x/config (submodule lib/x)`, exit 1.
- AC4 — `awk '/^#+ What a step can reach/{f=1;next} /^#+ /{f=0} f' help/upgrade-steps.md` printed, at its line 31, `config git cannot read refuses the step, naming that config file`, the sentence c0952b6f9 wrote.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-47 rows and the dSP-45 AC9/AC10 rows they ride), the break was a walk classifying by the `rev-parse --git-dir` exit: `FAIL [dSP-45] AC9 AC10 fixture isolation submodule-config-malformed exits 1 and names .git/modules/sub/config or a file it includes does not read`, where the fixture prints `isolation: fixture/status · up · ok`, so the malformed repository was skipped. The two `[dSP-47] AC2 AC3 … walk copy reds …` arms also red, but only because their anchor text left the module. The `submodule-name-slashed` row holds, as the `no-descent` break would not. Restored, GREEN: 3 of 3 and 8 of 8 `ok`.

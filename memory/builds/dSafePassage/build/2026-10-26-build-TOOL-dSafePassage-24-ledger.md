**Serves:** journal TOOL-dSafePassage-24

# TOOL-dSafePassage-24 — acceptance ledger

The unit as built, at spec rev-3. In `tools/govkit/upgrade_steps.py`: `read_target_local_config`
runs `git -C <target> config --list --show-scope --show-origin --includes -z` under `build_step_env`
over a scratch made for the read, keeping the `local` and `worktree` rows as (file, key, value);
`check_target_local_config` returns each row whose key `TARGET_CONFIG_REFUSED` matches (§4 "Data
model", case-insensitive, `core.fsmonitor` excepted when its value is a git false), as
`<key> in <file>`, and a read git fails is its one entry, naming the exit. `run_step_isolated` raises
`Refusal` on any entry, after the attended and no-argv checks and before any spawn, naming the step,
the phase, each key and its file. The `isolation` fixture family gains `local-filter`,
`local-process`, `local-fsmonitor`, `local-include` and their `-stub` twins, which swap
`check_target_local_config` for an empty answer in the fixture process only. `refusal_join.py`'s
`BRANCH_PIN` moves 319 -> 320; `help/upgrade-steps.md` "What a step can reach" names the refused keys
and what is not covered. `tools/govkit/selftest.py`'s `check_step_isolation` gains the eight rows,
tagged `[dSP-24]`: the `New arm:` line's arm.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture isolation --plant <case>` on node d (Windows,
git 2.54.0.windows.1); its repositories sit under `%TEMP%`. Reds were staged by each `-stub` twin, and
for AC3 and AC4 also in place, then restored from a scratch copy.

SPEC NOTE, no departure in the code. AC4's red reads "the read runs without `--includes`". On git
2.54 that staging does NOT red: `git config --list` with no file option follows includes by default,
so dropping the flag still names the included key. The red was observed with `--no-includes` instead
(below). The code runs `--includes` as S1 says.

Owed at the close: `govkit selftest` (with `check_step_isolation`'s `[dSP-24]` rows and their
RED-first observation, staged by the `-stub` twins), `govkit refusal join`, `govkit acceptance
matrix`, `govkit selfcheck`, `recall floor arms`, `encoding posture`, `lexicon naming predicates`,
`spec tokens`.

**Evidences:** TOOL-dSafePassage-24
- AC1 — `--plant local-filter`, rc 1: `isolation: fixture/clean · refused · fixture/clean up: the target's own git config declares what git runs as a program or sends as a credential, filter.canary.clean in .git/config, so nothing was spawned: remove it, or run the step attended`, `isolation: filter canary: absent`, no `FAILED`. `--plant local-filter-stub`, rc 1: `isolation: fixture/clean · up · ok`, `isolation: filter canary: present · filter-clean`.
- AC2 — `--plant local-process`, rc 1: `... filter.canary.process in .git/config, so nothing was spawned ...`, `isolation: process canary: absent`. `--plant local-process-stub`, rc 1: `isolation: process canary: present · filter-process`.
- AC3 — `--plant local-fsmonitor`, rc 1: `... core.fsmonitor in .git/config, so nothing was spawned ...`, `isolation: fsmonitor canary: absent`, then with the value rewritten to false `isolation: fixture/clean · up · ok`, `isolation: core.fsmonitor=false · not refused · git add exits 0`. `--plant local-fsmonitor-stub`, rc 1: `isolation: fsmonitor canary: present · fsmonitor`. Red staged in place (the git-false set emptied): `isolation: FAILED · core.fsmonitor=false was refused: ...`. An in-process probe of `check_target_local_config` over a scratch repository also named `credential.helper`, `http.https://x.y/.extraheader`, `http.extraheader`, `diff.pdf.textconv`, `diff.pdf.command`, `diff.external`, `core.sshcommand`, `core.askpass`, a bare `core.fsmonitor` and `filter.lfs.smudge`, not `core.fsmonitor` = `0`, `Off` or empty, nor `merge.rows.driver`; a missing directory read `` `git config --list` exits 128: fatal: cannot change to ... ``; gov's own checkout read `[]`.
- AC4 — `--plant local-include`, rc 1: `... filter.canary.clean in C:/Users/DAILY-~1/AppData/Local/Temp/gk-iso-<x>/included.gitconfig, so nothing was spawned ...`, `isolation: include canary: absent`. `--plant local-include-stub`, rc 1: `isolation: include canary: present · filter-clean`. Red staged in place (`--no-includes`): `isolation: include canary: present · filter-clean`, `isolation: FAILED · the step was not refused naming filter.canary.clean in .../included.gitconfig`.
- AC5 — `git grep -n -e "filter.<x>.clean" -e "extraheader" -e "merge.<driver>.driver" -- help/upgrade-steps.md` printed lines 51, 53 and 56, all inside "What a step can reach".
- Unbroken neighbours — `fixture isolation` (base) rc 0, `--plant token` refused as before, `--plant callers` `one spawn site of a step argv, inside run_step_isolated`, `fixture walk` rc 0 `4 pending · 4 applied`.

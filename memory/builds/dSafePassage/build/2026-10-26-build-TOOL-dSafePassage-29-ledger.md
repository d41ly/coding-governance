**Serves:** journal TOOL-dSafePassage-29

# TOOL-dSafePassage-29 — acceptance ledger

The unit as built, at spec rev-4. In `tools/govkit/upgrade_steps.py`: `STEP_REFUSED_KEYS` replaces
TOOL-dSafePassage-24's `TARGET_CONFIG_REFUSED` regex, one (key pattern, value rule, what runs it)
row per pattern of §4 "Data model", 39 rows, `<x>` matching one or more segments; the value rules
are `any`, `not a git false` (`core.fsmonitor`, a bare key read as true) and `begins with !`
(`submodule.<x>.update`, `alias.<x>`). `STEP_UNREFUSED_KEYS` holds §4's seven exceptions with their
reasons. `check_target_local_config` refuses a row when any `STEP_REFUSED_KEYS` row matches its key
and its value; the one `raise Refusal` site is unchanged, so no new function and no `BRANCH_PIN`
move. The `isolation` family gains `local-gpg` and `local-hook` and their `-stub` twins, and the
fixture's `clean.py` now commits what it stages (identity passed with `-c`), so the signing program
and a config-declared pre-commit hook are reached. `tools/govkit/selftest.py`'s
`check_step_isolation` gains the four plant rows and the class arm over `git help --config`, tagged
`[dSP-29]`, and the `hook-stub` row's needle now reads the canary list by member, since the commit
adds the commit-time hooks to it. `help/upgrade-steps.md` "What a step can reach" names the
derivation, the refused class and the seven unrefused keys with their reasons.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, git 2.54.0.windows.1) by the fixture CLI or a `python` probe of the changed code;
fixture repositories sit under `%TEMP%`.

Owed at the close: `govkit selftest` (the `[dSP-29]` rows, the changed `[dSP-7]` `hook-stub` row, and
the New arm's RED-first observation, staged by the `-stub` twins and a table copy missing
`gpg.program`), `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall floor
arms`, `encoding posture`, `lexicon naming predicates`, `policy fixtures`, `spec tokens`.

**Evidences:** TOOL-dSafePassage-29
- AC1 — `fixture isolation --plant local-gpg`, rc 1: `isolation: fixture/clean · refused · fixture/clean up: the target's own git config declares what git runs as a program or sends as a credential, gpg.program in .git/config, so nothing was spawned: remove it, or run the step attended`, `isolation: gpg canary: absent`. `--plant local-gpg-stub`, rc 1: `isolation: fixture/clean · up · ok`, `isolation: gpg canary: present · gpg-program`.
- AC2 — `--plant local-hook`, rc 1: `... hook.canary.command in .git/config, so nothing was spawned ...`, `isolation: hook canary: absent`. `--plant local-hook-stub`, rc 1: `isolation: hook canary: present · hook-command`.
- AC3 — a `python -c` probe loading `upgrade_steps.py` by path, `read_target_local_config` swapped for rows in process, printed `core.editor`, `sequence.editor`, `core.gitproxy`, `remote.origin.uploadpack`, `submodule.sub.update` (once, the `!sh x` row) and `alias.x` refused; `submodule.sub.update = checkout`, `alias.y = log`, `core.fsmonitor = false`, `commit.gpgsign`, `column.clean` and `core.hookspath` not refused; a bare `core.fsmonitor` refused.
- AC4 — the arm's block executed in process over the real `git help --config`: `ok [dSP-29 AC4] git help --config: 43 executor-shaped key(s) kept, 36 matching STEP_REFUSED_KEYS and 7 STEP_UNREFUSED_KEYS, none matching neither` and `ok ... the arm names gpg.program`. With `git help --config` answering nothing: `FAIL ... 0 executor-shaped key(s) kept ... the listing kept no key`. With the real table's `gpg.program` row removed: `FAIL ... 35 matching STEP_REFUSED_KEYS ... matching neither: ['gpg.program']`.
- AC5 — `git grep -n -e "git help --config" -e "gpg.program" -e "core.hooksPath" -- help/upgrade-steps.md` printed lines 44, 52, 58 and 65, all inside "What a step can reach"; TOOL-dSafePassage-24 AC5's literals stay on the page.
- Unbroken neighbours — `fixture isolation` (base) rc 0, `--plant hook` rc 0 `hook canary: absent`, `--plant hook-stub` rc 1 naming `hook-post-index-change` and `hook-pre-commit`, `--plant credential` rc 0, `--plant local-filter` and `local-fsmonitor` refused as before, `--plant local-include-stub` rc 1 `filter-clean`, `--plant callers` rc 0.

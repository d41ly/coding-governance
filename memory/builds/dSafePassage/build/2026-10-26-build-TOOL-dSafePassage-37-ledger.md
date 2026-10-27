**Serves:** journal TOOL-dSafePassage-37

# TOOL-dSafePassage-37 — acceptance ledger

The unit as built, at spec rev-3. `tools/govkit/upgrade_steps.py`: `STEP_REFUSED_KEYS` gains
`gc.recentObjectsHook` (any value); `STEP_UNREFUSED_KEYS` gains `advice.ignoredHook` and
`uploadpack.packObjectsHook`; `build_step_env` adds the third command-scope pair
`protocol.ext.allow = never` and `GIT_CONFIG_COUNT` reads 3. `fixture isolation` gains
`local-recent-objects-hook` and `local-ext-transport` with their `-stub` twins, stepped by two new
fixture step programs, `gc.py` (an unreachable object, then `git gc -q --prune=now`) and `fetch.py`
(`git fetch -q origin`, its stderr and exit passed through). `tools/govkit/selftest.py`'s class arm
keeps a last segment ending in `hook`, and carries the `[dSP-37]` rows, the `build_step_env` pair
row and the base needle `GIT_CONFIG_COUNT 3`. `help/upgrade-steps.md`'s "What a step can reach"
names the third pair, the closed `ext::` transport, `gc.recentObjectsHook` and the two unrefused
keys, and no longer says the refused keys are the whole class git documents.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by the
unit's own CLI (`python tools/govkit/upgrade_steps.py fixture isolation --plant ...`) over its
scratch fixture under `%TEMP%` on node d (Windows, Git Bash, git 2.54.0.windows.1), by a scratch
`python` probe applying the class arm's predicate to `git help --config`, and by `git grep` over the
help page. They stand in for the `govkit selftest` leg's `check_step_isolation` rows for this unit
only.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `encoding posture`, `lexicon naming predicates`,
`policy fixtures`, `spec tokens`; and the new arm's RED-first observation (§7): the two `-stub`
twins and the table copy missing the `gc.recentObjectsHook` row must red the `[dSP-37]` rows.

**Evidences:** TOOL-dSafePassage-37
- AC1 — `--plant local-recent-objects-hook` exited 1 printing `fixture/gc · refused · fixture/gc up: the target's own git config declares what git runs as a program or sends as a credential, gc.recentobjectshook in .git/config, so nothing was spawned` and `recent-objects-hook canary: absent`, no `FAILED`. Red: `--plant local-recent-objects-hook-stub` exited 1 printing `fixture/gc · up · ok` and `recent-objects-hook canary: present · recent-objects-hook`. The key reads as git prints it, lowercased (TOOL-dSafePassage-45's reading).
- AC2 — `--plant local-ext-transport` exited 1 printing `fixture/fetch · up · failed · rc 128: fatal: transport 'ext' not allowed` and `ext-transport canary: absent`. Red: `--plant local-ext-transport-stub`, the step env lacking the pair, exited 1 printing `fixture/fetch · up · failed · rc 128: fatal: Could not read from remote repository.` and `ext-transport canary: present · ext-transport`. The base fixture printed `GIT_CONFIG_COUNT 3 · core.hooksPath holds []`, exit 0; `build_step_env` holds `GIT_CONFIG_KEY_2 = protocol.ext.allow`, `GIT_CONFIG_VALUE_2 = never`.
- AC3 — the predicate probe over `git help --config` (1005 non-blank lines) printed, with the suffix, `kept=46 refused=37 unrefused=9 neither=[]`, the kept set holding `advice.ignoredHook`, `gc.recentObjectsHook`, `uploadpack.packObjectsHook`, and with the `gc.recentObjectsHook` row out of a table copy it named `['gc.recentObjectsHook']`; `core.fsmonitorHookVersion` not kept. Red: without the suffix it printed `kept=43` and none of the three kept.
- AC4 — `git grep -n -e "gc.recentObjectsHook" -e "ext::" -- help/upgrade-steps.md` printed line 46 (a step can never use the `ext::` transport) and line 71 (`gc.recentObjectsHook` among the refused keys).
- No regression: `hook`, `hook-stub`, `credential`, `credential-stub`, `local-gpg-stub`, `local-fsmonitor`, `local-include` and `local-hook` each exited as before with no `isolation: FAILED`; `drop_pair` renumbers the three pairs.

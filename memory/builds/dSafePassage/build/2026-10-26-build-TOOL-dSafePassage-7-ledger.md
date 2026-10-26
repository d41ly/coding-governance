**Serves:** journal TOOL-dSafePassage-7

# TOOL-dSafePassage-7 — acceptance ledger

The unit as built, all in `tools/govkit/upgrade_steps.py`: `STEP_ENV_KEEP` and `build_step_env`
(S1), `resolve_step_argv` over govkit's `resolve_tokens` and `resolve_shell_argv` (S2),
`derive_step_mode` and `run_step_isolated`, the one spawn of a step argv, from gov's checkout root
(S3), `write_target_plants` and `read_plant_canaries` (S4), `check_needs_target` (S5), and
`fixture isolation [--plant <case>]` with the ten plants of §4 "Inventory" (S6), the `callers`
plant reading both files with `ast` through `read_step_spawn_sites` (S7). `help/upgrade-steps.md`
gains "What a step can reach" (S8). `tools/govkit/selftest.py` gains `check_step_isolation`, the
`New arm:` line's arm. `refusal_join.py`'s `BRANCH_PIN` moves 308 -> 310 by the two new refusals.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture isolation [--plant <case>]` on node d
(Windows, git 2.54.0.windows.1, Python 3.14); its scratch gov and target sit under `%TEMP%`. The
red half of AC1 and AC5 was staged by a scratch probe that imports the module by path and swaps
`build_step_env` for a parent copy, `resolve_step_argv` for one dropping `-I`, and
`derive_step_mode` for one that never reads `attended`. The `credential-stub` plant hands the step
the parent's `GIT_CONFIG_GLOBAL` and `GH_TOKEN` and leaves out the empty `credential.helper` pair,
since that pair, the contract's own credential value, resets the planted helper and would keep the
red from being observed; `hook-stub` leaves out the `core.hooksPath` pair the same way. Owed at the close: the `govkit selftest`
and `govkit refusal join` legs, and the RED-first observation of `check_step_isolation`.

**Evidences:** TOOL-dSafePassage-7
- AC1 — base run, rc 0: `fixture/clean · up · ok`; `env names outside the allowlist and the contract: none`; `GIT_CONFIG_COUNT 2 · core.hooksPath holds [] · sys.flags.isolated 1 · cwd <scratch>\gov`; `fixture/clean · isolated`. Red staged: a parent-copy environment printed `isolation: FAILED · names outside the allowlist reached the step: [... 'GH_TOKEN', ...]`, rc 1; an argv without `-I` printed `sys.flags.isolated 0` and `isolation: FAILED · the leading python ran without -I`, rc 1.
- AC2 — `--plant hook`, rc 0: `hook canary: absent`, with `post-index-change` and `pre-commit` planted under the target's own `core.hooksPath` `.githooks`, and clean's `git add` exiting 0. `--plant hook-stub`, rc 1: `hook canary: present · hook-post-index-change`.
- AC3 — `--plant module`, rc 0: `module canary: absent`, with `PYTHONPATH` naming the target in the parent. `--plant module-stub`, rc 1: `module canary: present · module-json.py, module-sitecustomize.py`.
- AC4 — `--plant credential`, rc 0: `credential canary: absent`; `token: absent`; `git credential fill exits 128 · credential.helper reads ['']`. `--plant credential-stub`, rc 1: `credential canary: present · credential-helper`; `token: present · GH_TOKEN reached the step`.
- AC5 — `--plant needs-target`, rc 1: `fixture/reaches · needs-target · its up exits 1 under the contract and no canary ran, so it needs target code: declare needs-target = true, under which it is attended`; `fixture/reaches-attended · attended`; `fixture/reaches-attended · own canary absent`. `--plant breach`, rc 1: `fixture/opens · breach · target code ran under the contract: adopter_only`. The base run prints `fixture/clean · isolated`. Red staged: a `derive_step_mode` that never reads `attended` printed `own canary present: it spawned` and two `isolation: FAILED` lines.
- AC6 — `--plant callers`, rc 0: `a spawn of a step argv at upgrade_steps.py:756, in run_step_isolated`; `one spawn site of a step argv, inside run_step_isolated`. Over a scratch copy of the pair with `def planted_spawn(row): return subprocess.run(row["up"])` appended, rc 1: `a spawn of a step argv at upgrade_steps.py:1155, in planted_spawn` and `isolation: FAILED · callers · 2 spawn site(s)`.
- AC7 — `--plant token`, rc 1: `fixture/token · refused · fixture/token: '{unknown}' holds {unknown}, which this run does not answer, so nothing was spawned`, and no report was written.
- AC8 — `git grep -n -e "core.hooksPath" -e "GIT_CONFIG_COUNT" -e "needs-target" -- "help/upgrade-steps.md"` names all three inside "What a step can reach" (lines 43, 44 and 49 to 57).

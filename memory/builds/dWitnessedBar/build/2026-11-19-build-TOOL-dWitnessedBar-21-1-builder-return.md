**Serves:** journal TOOL-dWitnessedBar-21

# TOOL-dWitnessedBar-21 — builder return 1 (run `wf_8888fc86-57d`), committed cd03e4e7544ab02745980926c1dfda82e99b9ba0

## Why

The spec was buildable as written. Every claim it makes about the code held at HEAD: verb_dispatch, check_commit_message, park, PARK_KINDS, check_unit_spec and _d_spec, load_spec_facts and SPEC_PATH, the gov:argv sentinels, the check 26 and 27 arms, resolve_leg_manifest, the census of 340 against a ceiling of 343, the three manifest legs and the held copies. All eight criteria were observed with the unit's own CLI and fixtures, and the spec is CLOSED in the pass commit.

## Summary

TOOL-dWitnessedBar-21 is built and committed in two commits. The pass commit is cd03e4e7544ab02745980926c1dfda82e99b9ba0 (trailer `Pass: TOOL-dWitnessedBar-21`, spec set to CLOSED, ledger and RUN.md included). After it comes 057c43cef92661175ceec8621074c844356eef20 (`Pass: none`). That second commit renames a nested fixture helper from `drive` to `run_driver`, because the gotchas checklist flagged that the naming leg grades nested helpers and the lexicon does not declare `drive`.

**What was built**
- **New module** `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/unattended/fix_keeps.py`:
  - `read_leg_files`, `read_acceptance_files` and `print_keeps` (`--keeps`, `--spec`).
  - Five fixture plants (`--fixture --plant`), each in a throwaway repository that drives a copy of the driver.
  - Four inline blocks, byte-identical to their canonical copies in tools/lib: `resolve_kit_dir`, `resolve_prefix_token`, `resolve_bash_py` and `git_env_leaks_py`.
- **Driver** `tools/unattended/unattended.sh`:
  - New flag `[--fix-of <red>]` in the header and the parser.
  - New helper `check_fix_keeps`, which holds the three new refusal sites (all check 49). The census is now 343 against a ceiling of 343, with 339 armed.
  - Called from `verb_dispatch` after the shape loop and before the budget draw and the dispatch row, and from `check_commit_message` for an open key that holds a `fix-of` row, before the undeclared-path refusal.
  - New `park "$rel" fix-of` site; `fix-of` added to PARK_KINDS.
- **Other edits:**
  - The `fix-of` kind joined `drift_report.py#_RUN_PARK_KINDS` and `model.py#PARK_KINDS`.
  - `record.py` gained `EXCLUDED_KINDS_BEFORE_FIX_OF`, and `EXCLUDED_KINDS_BEFORE_REFUSAL` now derives from it.
  - The verbs carrier paragraph went into `VERBS.template.md` and `UNATTENDED-VERBS.md`, which are still byte-identical.
  - `symbols.json` was re-rendered.
  - The arms went into `unattended.test.sh`.
  - The ledger is `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-21-1-acceptance-ledger.md`.

**Checks that ran** (each stands in for the gates named after it)
- **AC1:** `--keeps 'leg:memory hygiene'` printed only `tools/memory-tree/check-memory-hygiene.sh` on stdout. `leg:nope` exited 2 naming it.
- **AC2 to AC6:** all five plants printed PASS. Stands in for `unattended kit gate` and the new suite arm.
- **Red observation:** I ran the plants from a scratch copy of the kit with both `check_fix_keeps` calls deleted. `writes-test-file`, `commit-test-file` and `unknown-leg` all printed FAIL.
- **Shape refusal:** probed by sourcing the driver; it refused `bogus`, an empty red, `leg:`, and a red carrying the bypass flag.
- **AC7 and AC8:** the greps and the record probe gave the expected output (`True False`, and 1 for each file). Stands in for `drift-audit selftest`, `runlog selftest` and `runlog record schema`.
- **Arms census:** `check-arms.py --emit-floors` printed `unattended.sh:343:339`. Stands in for `harness arms`.
- **Inline parity:** a Python byte comparison of the four blocks. Stands in for `python resolver`.
- **Naming lexicon:** asked for every new name.
- **gotchas.py:** run over both commits and acted on.

**Owed to the main loop at the close**
- The new suite arm in `unattended.test.sh` (shape refusal plus the five plants) is written but not run, and its RED-first observation is still owed. The staged break is deleting the `check_fix_keeps` calls.
- Every leg in the spec's section 7. Check 26's suite half and check 27's call-site join can only be seen through `unattended kit gate`.
- Nothing timed out.

**Things the spec did not state** (recorded as `Decided:` trailers, not deviation records, because none departs from the carried clause)
- The module writes its notes to stderr with a `fix-of: ` prefix, including `fix-of: tests <tags>|none`, so stdout carries only the kept paths.
- The fixture finds bash with `resolve_bash_py` and strips git location variables with `git_env_leaks_py`.
- The shape refusal also rejects a red containing a line end or the bypass flag, so `park()` cannot refuse the `fix-of` row after the dispatch row is already written.

The commit hook printed an existing warn-only BUDGET WARN: `UNATTENDED-VERBS.md` is 117306 bytes against a 98304 budget. It was already over before this unit (115736 bytes); this unit's paragraph adds about 1.6 KB. I left the unrelated `help/` working-copy changes unstaged.

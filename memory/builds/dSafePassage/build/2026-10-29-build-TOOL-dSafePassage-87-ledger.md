**Serves:** journal TOOL-dSafePassage-87

# TOOL-dSafePassage-87 — acceptance ledger

The unit as built, at spec rev-4, S1 to S12. Product writes: `tools/govkit/upgrade_steps.py` (S1's
`..` refusal in `check_contained`, S4's `GOV_BASH` in `STEP_ENV_KEEP`, S6's remedy wording in
`read_image_paths` and the walk plant `truncated-image-held`), `tools/govkit/steps/python_floor.py`
(S4), `tools/govkit/upgrade_walk.py` (S2, S3, S7's `read_target_prefix`, S11's call and `shim-root`
grader, S12), `tools/govkit/shims.py` (S11's `troot` keyword), `tools/govkit/docs_leg.py` (S8's
`scripts-prefix` plant), `tools/govkit/selftest.py` (the `[dSP-87 AC1]`, `[dSP-87 AC5]` and two
`[dSP-87 AC6]` checks, the `truncated-image-held` fixture row and its `dSP-87` tag, the
`scripts-prefix` docs case), `tools/govkit/refusal_join.py` (`BRANCH_PIN` 334 -> 335),
`tools/lib/resolve-python.test.sh` (S9) and `help/upgrade-steps.md` (S10).
`memory/map/generated/symbols.json` regenerated for `read_target_prefix`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) from this worktree's root over its working copy, the probes of spec §4 copied from the
spec into the run's scratch and run with the temp root pointed at that scratch. Each staged break
was written into the working file by a scratch script that restored the original bytes in a
`finally`. AC8 and AC9 ran in a `git clone --no-hardlinks` of this branch's HEAD `10abda03c` under
`%TEMP%/p87`, the unit's working-tree files committed over it, then moved by the foreign-prefix leg's
own `set_tool_root scripts` and `write_declarations`, extracted with
`sed -n '/^set_tool_root() {/,/^# ---- ONE ROW/p'` and sourced with `TROOT=tools` and `PY=python`; it
re-spelled 227 declaration files. The walk's own temp root was `%TEMP%/p87t`, because the scratch
path is too long for the walk's inner clone. Both were removed after.

Owed at the close: the RED-first observation of each of §7's eight `New arm:` lines, in their suites
(`govkit selftest`, `upgrade-walk`, `docs`, `python resolver`), and the §7 legs at the bar. The
staged breaks below ran the unit's probes and CLIs, not the suites, so they do not discharge the
arms' in-suite observations. AC11's behaviour half, the gov-tree control's new assertion passing in
`resolve-python.test.sh`, is observable only by that suite and is owed there.

**Evidences:** TOOL-dSafePassage-87
- AC1 — `python <scratch>/contain_probe.py` — printed `a/../b -> refused: 'a/../b' holds a '..' segment, ...`, `lnk/../x -> refused: 'lnk/../x' holds a '..' segment, ...`, `lnk/x -> refused:` (a reparse point), `..\ESCAPED.txt -> refused: '..\ESCAPED.txt' is not a path inside the target, ...` and `a/b -> a/b`. With the `..` test staged out (`if False:`) the same probe printed `a/../b -> b` and `lnk/../x -> x`.
- AC2 — `git grep -n "^BRANCH_PIN = 335" -- tools/govkit/refusal_join.py` printed `:41`; `git grep -n -F "TOOL-dSafePassage-87"` printed the delta comment at `:42`. The delta was measured by `refusal_join`'s own matcher over `population()`: 473 at HEAD's blobs, 474 in the working tree, the one in `upgrade_steps.py` (89 -> 90).
- AC3 — `git grep -n -F -- '--no-renames'` printed one line, `upgrade_walk.py:952`, `check_tree_clean`'s status command; `git grep -n -F 'engine.py'` printed `:1026` and `:1048`, both inside `check_grade_tree_clean`. `check_graders()` printed `upgrade-walk: grader · tree-clean · ok` and last line `[]`. With the v1 parse staged back (no `-z`, no `--no-renames`, the ` -> ` split) it printed `upgrade-walk: grader · tree-clean · RED · tools/govkit/engine.py renamed into fixtures/release-0, it returned []`.
- AC4 — `git grep -n -F 'x.sh'` printed one line, `upgrade_walk.py:1026`, the `libf` of `check_grade_tree_clean`. With `lib` staged out of the pathspec, `check_graders()` printed `upgrade-walk: grader · tree-clean · RED · tools/lib/x.sh edited, it returned []`.
- AC5 — `python <scratch>/floor_probe.py` — printed `ok 0 ''`. With `GOV_BASH` staged out of `STEP_ENV_KEEP` it printed `failed 127 '/bin/bash: .../tools/lib/python-floor.sh: No such file or directory'`, the WSL launcher.
- AC6 — `git grep -n -F "[dSP-87 AC6]" -- tools/govkit/selftest.py` printed two lines, `:3153` and `:3163`, inside `check_upgrade_steps`. `python <scratch>/esc_probe.py` printed `[('demo/esc', 'third'), ('demo/ml', 'third')]`. Its argument a scratch copy of the kit whose `upgrade_steps.py` carries the arm's own mutant at its own anchor (anchor count 1), it printed `[('demo/esc', 'unlanded'), ('demo/ml', 'unlanded')]`.
- AC7 — `python tools/govkit/upgrade_steps.py fixture walk --plant truncated-image-held` — exit 0, printed `walk: held · rc 1 · remedy named` and `walk: held · after the remedy · fx/s2 applied · rc 0`, no `walk: FAILED`. With the refusal staged at its old words it printed `walk: held · rc 1 · remedy absent` and `walk: FAILED · an unparsable image under a holding witness did not stop the walk naming it and its remedy`, exit 1.
- AC8 — the `python -c` of AC8 from the moved clone's `scripts/govkit` printed `tools/memory-tree/README.md`, then `scripts/hooks/kit.toml`.
- AC9 — `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` from the same directory printed `upgrade-walk: release-0 applied by the pinned clone's own apply ... · exit 0 · receipt schema 3` and `upgrade-walk: release-0 · the policy adopter's re-run committed .governance/policy.json`, and no `is absent at release-0`; it then stopped at `read_steps` with `upgrade_steps.Refusal: tools/govkit/registry.toml: no registry at 8b9bc25e`, exit 1, the §3 hands-off to TOOL-dSafePassage-89.
- AC10 — `python tools/govkit/docs_leg.py --fixture --plant scripts-prefix` — exit 0, printed `docs: 6 classes · ... · commands 2 tested, 1 skipped, 0 unrowed · ...`. `--plant none` printed the same counts. With `check_page_command` staged to resolve against `"tools"` in place of `troot`, the plant exited 2 with `docs: REFUSED · the pages show commands and no page command was tested against a row`.
- AC11 — `git grep -n -F 'Traceback' -- tools/lib/resolve-python.test.sh` printed `:338`, the gov-tree control's assertion; `git grep -n -F '[ "$rc" != 2 ] || bad "the down over gov'` printed nothing.
- AC12 — `git grep -n -F` over `help/upgrade-steps.md` printed one line each: `segment even one` at `:327`, `GOV_BASH` at `:40`, `where none is committed` at `:212`.
- AC13 — `check_graders()` printed `upgrade-walk: grader · shim-root · ok` and last line `[]`. With `:565`'s call staged back to `read_shim_rows(ctx["clone"])` it printed `upgrade-walk: grader · shim-root · RED · gov's own row, its forwarder tools/demo/old.sh gone, read no red: []`.
- AC14 — `git grep -n -F 'resolve_tool_path(clone, gk.GOVKIT_DIR.name, "govkit.py")'` printed one line, `upgrade_walk.py:203`, inside `derive_release_engine`; `check_graders()` printed `upgrade-walk: grader · release-engine · ok`.

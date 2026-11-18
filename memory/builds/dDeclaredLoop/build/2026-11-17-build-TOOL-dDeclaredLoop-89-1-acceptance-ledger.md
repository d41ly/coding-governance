# TOOL-dDeclaredLoop-89 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-89

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-5 of the spec, over the working tree, by the first dispatch, which started from the
base `7d4a42868`. The `conf-read-forms` and both `no-own-conf-read` plants ran alone by
`--fixture --plant`, standing in for the `loop budget fixtures` and `loop breakpoint fixtures` legs; `python -c`
probes of `derive_conf_constants`, `derive_conf_rebinds` and `loop_lib.py`'s syntax tree and three greps
stood in for the rest. The sweep re-run at the base held every design claim; its stale figures are
deviation 893, and the conf-name predicate extracted as `check_conf_name` is deviation 894.
`derive_conf_constants` over the kit's own `loop_lib.py` answered the empty set after the edit, and
`derive_conf_rebinds` over it answered the empty set too. The lexicon offender pin read 1215 PINNED, the driver's refusal ceiling
343 PINNED, both shared records unwritten, no shell file and no watched kickoff path edited; the three
minted functions lead with declared verbs, checked with the lexicon's suggest verb, and the codebase
map was regenerated.

Owed to the close: every leg section 7 names and the three loop legs it keeps green; and RED-first, on
the one `New arm:` line: the `budget.py` `conf-read-forms` plant with `derive_conf_rebinds` staged to
answer the empty set, owed to exit 1 printing `MISSED` naming the global-loader, with-held-loader,
walrus-target, for-target and with-target rows.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant conf-read-forms` with `derive_conf_rebinds` answering the empty
set exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-89
- AC1 — `conf constant` — the plant exited 0 printing `line 2 conf constant` for `global-loader`, `with-held-loader`, `walrus-target`, `for-target` and `with-target`, `no hit` for `plain-global` and `docstring-loader`, every row 82, 86 and 87 wrote unchanged, then `held`; it ran in under 1 PINNED second by direct CLI. `no-own-conf-read` of `budget.py` and of `breakpoints.py` each printed `held`.
- AC2 — `derive_conf_constants` — over a scratch `loop_lib.py` the probe wrote with the ten shapes the criterion names, it answered exactly `CONF_G`, `FCONF`, `FH`, `KIT_CONF`, `PLAIN` and `WCONF`, never `COUNTER`, `NOTE`, `PEEK` or `LOCAL`.
- AC3 — `derive_conf_rebinds(tree, docs)` — its grep over the loop README printed 1, the grep for `load_tree_lib()` printed 1, and the `derive_conf_constants(` row piped to `grep -c "derive_conf_rebinds"` printed 1.
- AC4 — `NOT SEEN` — the docstring of `derive_conf_rebinds` held each of the nine strings the criterion greps for, checked by one `python -c` probe.
- AC5 — `load_tree_lib` — the one str constant naming the memory-tree kit's library file sits inside `load_tree_lib`, and `derive_conf_reads` and `derive_conf_constants` each call it; in a scratch copy of the loop and memory-tree kits whose library lacked `derive_docstring_ids`, `import loop_lib` exited 0 and a call of `derive_conf_constants` exited 1 printing `LoopError` and `govkit update --kits memory-tree`.

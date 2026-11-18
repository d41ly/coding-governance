# TOOL-dDeclaredLoop-88 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-88

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-6 of the spec, over the working tree, by the first dispatch, which started from the
base `64378f543`. The four new `guard.py` plants, the `push-merge-tree-fatal`, its unparseable-parent
twin, `push-merge-probe-failed`, `push-merge-probe-silent` and `push-merge-unrelated-histories` plants
ran alone by `--fixture --plant`, standing in for the `loop guard fixtures` leg; the `conf-read-forms`
and both `no-own-conf-read` plants ran the same way, standing in for the `loop budget fixtures` and
`loop breakpoint fixtures` legs; `python -c` probes of `derive_constant_charges`, `scan_glob_readers`,
`derive_conf_constants`, `run_merge_tree_usage` and `load_tree_lib`, and the two greps, stood in for
the rest. The glob-reader arm's planted module, its bytes read out of `cmd_selftest`, answered its
eight PINNED owners through the lifted walk, and `scan_glob_readers` over the live kit answered the
same five PINNED owners before and after the lift. `derive_conf_constants` over the kit's own
`loop_lib.py` answered the empty set. The sweep re-run at the base held every design claim; its stale
figures are deviation 883. The lexicon offender pin read 1215 PINNED, the driver's refusal ceiling 343
PINNED, both shared records unwritten, no shell file and no watched kickoff path edited; the one minted
function and the walk's nested helper lead with declared verbs, checked with the lexicon's suggest
verb, and the codebase map was regenerated. The docstring of `derive_docstring_ids` now names
`derive_constant_charges` as the walk that passes its ids over, since `scan_glob_readers` no longer
reads them itself.

Owed to the close: every leg section 7 names and the five loop legs it keeps green; and RED-first, on
the three `New arm:` lines: the four `guard.py` plants, each staged as its criterion's Red when; the
`budget.py` `conf-read-forms` plant, with the route's `LookupError` and import errors left to
propagate and with `derive_constant_charges` answering rule 4 for a module-level binding; and the
glob-reader arm of `gen_build_index.py --selftest`, with `derive_constant_charges` charging a
module-level binding to the module.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant conf-read-forms` with every function the unit's pass changed in
`tools/loop/loop_lib.py` swapped back to its pre-pass source exited 2, and 0 once restored: RED observed.
`python tools/memory-tree/gen_build_index.py --selftest` with every function the unit's pass changed in
`tools/memory-tree/gen_build_index.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED
observed.
`python tools/loop/guard.py --selftest` with every function the unit's pass changed in `tools/loop/guard.py`
swapped back to its pre-pass source exited 0, and 0 once restored: not reddened by this break, so not
observed.

**Evidences:** TOOL-dDeclaredLoop-88
- AC13 — `derive_constant_charges` — `grep -c "def scan_scope"` over `gen_build_index.py` printed 0 and `grep -c "^def derive_constant_charges"` over `tree_lib.py` printed 1; the probe over the five-place module answered `[('m', 4), ('m.K', 3), ('m.X', 2), ('m.f', 1)]`; `scan_glob_readers` over a scratch folder holding that module with a `:(glob)` needle answered `['m', 'm.K', 'm.X', 'm.f']`; `derive_conf_constants` over section 4's probe module answered `['A', 'B', 'CONF', 'D', 'G', 'GUARDED', 'SUFFIX']`; and the `conf-read-forms` plant printed `held`, every row units 82, 86, 87 and 89 wrote unchanged.
- AC16 — `LC_ALL` — with `guard.subprocess.run` swapped for a recorder answering exit 129, `run_merge_tree_usage()` recorded one call whose `env` mapped `LC_ALL` to `C` and `LANGUAGE` to the empty string, `os.environ` equal before and after; with `LC_ALL=de_DE.UTF-8` exported, `resolve_write_tree_support()[0]` printed `supported`.
- AC17 — `push-merge-probe-failed-trailered` — exit 0 printing `probe failed: start failed: fx stand-in`, `0 finding(s)`, `merge-tree runs: 0` and `all held`, 3 PINNED seconds worst of two direct-CLI runs.
- AC19 — `push-merge-conflicted-unparseable-parent` — exit 1 printing `does not parse at parent ` naming main's tip, `merge-tree runs: 1` and `all held`, no `Traceback`; `push-merge-probe-failed-unparseable-parent` exit 1 printing the same refusal, `merge-tree runs: 0` and `all held`, no `Traceback`; 3 PINNED and 6 PINNED seconds worst of two.
- AC26 — `push-merge-probe-signal` — exit 1 printing `probe failed: signal 9`, the `review.max-rounds` finding, `merge-tree runs: 0` and `all held`, no `Traceback`, 7 PINNED seconds worst of two.
- AC33 — `load_tree_lib` — the `conf-read-forms` plant's three `tree_lib` rows each printed a `LoopError` naming `govkit update --kits memory-tree`, the unlocatable row naming `looked in`, the blocked row `ModuleNotFoundError` and the unparseable row `SyntaxError`, then `held`, no `Traceback`; with `read_memory_tree` swapped to raise `LookupError`, `load_tree_lib()`, `derive_conf_constants` over a scratch `loop_lib.py` and `derive_conf_reads` over a scratch module beside it each raised `LoopError`; the `ast` probe found the `LookupError`, `ImportError` and `SyntaxError` handlers of the route inside `load_tree_lib` alone among the conf-read rule's functions, the one other `SyntaxError` handler there being the parse refusal of `derive_conf_constants` that unit 86 wrote, which wraps `ast.parse` and no load; `grep -c "^def load_tree_lib"` printed 1.

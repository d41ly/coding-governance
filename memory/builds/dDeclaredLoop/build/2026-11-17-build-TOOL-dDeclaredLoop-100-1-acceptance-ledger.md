# TOOL-dDeclaredLoop-100 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-100

No merge bar, no self-test suite and no gate leg ran in this pass. The criterion was observed on node `d`
(win32), at rev-2 of the spec, over the working tree, by the first dispatch, which started from the base
`9d4cef54f`, after units 97, 98 and 99 closed at order 50. The pass is an observation pass and writes no
product file. The spec's collection probe, an `ast` read run by `python -I -c` in `tools/loop/`, stands in
for nothing a leg runs: no leg reads the collection. Its staged break was observed over a scratch copy of
`loop_lib.py` outside the tree, with the spec's `fx_conf` line appended.

The sweep re-run at the base held every design claim: `tools/loop/loop_lib.py#TREE_LIB_SYMBOLS` holds
`derive_docstring_ids` and `derive_constant_charges`; `tools/loop/loop_lib.py#load_tree_lib` takes no
argument; no `read_tree_conf` and no `_is_under` is defined under `tools/loop/`;
`tools/loop/loop_lib.py#read_builds_dir` and `tools/loop/loop_lib.py#resolve_memory_root_source` call
`read_design_conf`; `tools/loop/kit.toml` requires the memory-tree and run-gates kits. Unit 97's
`CONF_READERS` names `parse_conf` as a declared conf reader, a constant and no loader-result read, and unit
99's `derive_conf_openers` adds no read on a loader result, so the collection is unchanged from unit 95's
observation. The item-and-criterion grep finds two lines each in the specs of units 90 and 99, unit 99 now
CLOSED; the edges grep finds the ten hands-off bullets; two positional rows name this spec, its
build-method rows, after the shrink the sweep foresaw; the lexicon offender pin reads 1215 PINNED; the
refusal ceilings name two unattended scripts and the loop folder holds no families file; the shared
records are the two the spec names; the kickoff manifest's watch line names no path under the build
folder or the loop kit. Every sibling spec the spec settles on is CLOSED. No function, constant, shell
file, shared record or watched kickoff path is written.

Owed to the close: every leg the spec's gates section names. This unit declares no `New arm:` line, so
it owes no RED-first observation.

**Evidences:** TOOL-dDeclaredLoop-100
- AC22 — `True` — the spec's collection probe run as `python -I -c` in `tools/loop/` with the arguments `loop_lib.py` and `.` printed `['derive_constant_charges', 'derive_docstring_ids'] True ('derive_docstring_ids', 'derive_constant_charges')`, PINNED 2026-11-17; over the scratch copy with `def fx_conf(t): return load_tree_lib().parse_conf(t, {})` appended, run with that copy's folder as the second argument, it printed `parse_conf` in the list and `False`.

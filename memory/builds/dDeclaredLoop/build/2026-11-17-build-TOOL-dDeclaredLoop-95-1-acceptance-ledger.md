# TOOL-dDeclaredLoop-95 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-95

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-3 of the spec, over the working tree, by the first dispatch, which started from the base
`1bb9bbd62`, after unit 94's rewrite of `load_tree_lib`. The pass is an observation pass and writes no
product file. The `no-confs` plant of `budget.py` ran alone by `--fixture --plant`, standing in for the
`loop budget fixtures` leg; an `ast` probe of the loop folder and a `python -I -c` import of `loop_lib`
stood in for nothing a leg runs. Each criterion's staged break was also observed, in scratch copies outside
the tree: `fx_conf` appended to a copy of `loop_lib.py` made the probe count 1 and the collection hold
`parse_conf`, and the absent branch of a copied `read_design_conf` raising `FileNotFoundError` made the plant
exit 1 printing `MISSED`.

The sweep re-run at the base held every design claim: `read_design_conf(` counts 7 PINNED calls across
the loop folder, two in `loop_lib.py` and one each in `adapt.py`, `loop_parents.py`, `loop_transition.py`,
`position.py` and `upstream.py`; `load_tree_lib` takes no argument and `loop_lib` holds no `read_tree_conf`;
`tools/loop/kit.toml` requires the memory-tree and run-gates kits; the symbol tier holds no `read_tree_conf`
row and one `read_design_conf` row; the edges grep finds 10 PINNED mirrored bullets; the lexicon offender
pin reads 1215 PINNED; the refusal ceilings name two unattended scripts and the loop folder holds no
families file; the shared records are the two the spec names; the kickoff manifest's watch line names 11
PINNED paths, none under the build folder or the loop kit; and no help page names `read_tree_conf`,
`parse_conf` or `TREE_LIB_SYMBOLS`. Two populations moved, both recorded in deviation 952 of this unit:
the item-and-criterion grep no longer finds the specs of units 96 and 97, and one positional row, not two,
names this spec. No function, constant, shell file, shared record or watched kickoff path is written.

Owed to the close: every leg section 7 names, the `loop budget fixtures` leg among them. This unit declares
no `New arm:` line, so it owes no RED-first observation.

**Evidences:** TOOL-dDeclaredLoop-95
- AC7 — `prints 0` — an `ast` probe run by `python -I` over every `*.py` of `tools/loop/`, counting each call whose callee name or attribute is `parse_conf`, printed 0, and `grep -c "read_design_conf(" loop_lib.py` printed 2, PINNED 2026-11-17.
- AC8 — `('derive_docstring_ids', 'derive_constant_charges')` — the `python -I -c` import in `tools/loop/` printed that tuple, and 90 AC4's collection over `loop_lib.py`, attributes read on a `load_tree_lib()` call or a name bound from one in the same function body, gave `derive_constant_charges` and `derive_docstring_ids`, a subset of it.
- AC9 — `root memory` — `python budget.py --fixture --plant no-confs` in `tools/loop/` exited 0 in 1.6 PINNED seconds and printed `root memory` and `held`, with no `Traceback`.

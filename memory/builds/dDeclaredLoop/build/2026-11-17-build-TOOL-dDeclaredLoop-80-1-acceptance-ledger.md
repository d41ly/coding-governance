# TOOL-dDeclaredLoop-80 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-80

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-6 of the spec, over the working tree: the `no-own-conf-read` plant of both modules and the four plants
calling the renamed staging, each run alone by `--fixture`, standing in for the `loop budget fixtures` and
`loop breakpoint fixtures` legs; `python -c` probes of `derive_conf_reads` and `derive_fixture_boundary`
standing in for nothing a leg runs; a scratch copy of the kit folder for AC1's red; the naming lexicon's
suggest verb for both minted names, standing in for `lexicon naming predicates`; the map generator's write,
standing in for `codebase-map coverage + freshness`; and `grep` probes. The section 5 sweep re-run at this
pass's base held its design claims: the lexicon offender pin at 1215 PINNED, `SHARED_RECORDS` not written,
no shell file edited, no verb, flag or plant added, no file on the kickoff watch list edited; its stale
figures are deviation 803.

The base probe, 76 AC1's mapping run over both modules at this pass's base before the first edit, one row
per hit with its enclosing top-level function: in `budget.py` 9 PINNED hits, every one `conf name` inside
`tools/loop/budget.py#run_budget_plant`, bounded; in `breakpoints.py` 8 PINNED hits, every one `conf name`,
7 PINNED inside `tools/loop/breakpoints.py#run_breakpoint_plant`, bounded, and 1 PINNED outside the boundary
in the pre-placement staging, which seeds a scratch tree and is S2's population, renamed
`tools/loop/breakpoints.py#write_pre_placement_plant`. No hit sat in a function that reads the module's own
repository.

Owed to the close: every leg section 7 names; the `loop budget fixtures` and `loop breakpoint fixtures`
legs, non-zero at the base on `no-own-conf-read` alone and owed 0 now; the `loop definition fixtures` leg,
whose module this pass edits, run by its argv once; and AC4. Owed RED-first: the `tools/loop/budget.py` arm,
`no-own-conf-read` over its own module and over the staged module, and the `tools/loop/breakpoints.py` arm,
`no-own-conf-read` and the four plants calling the renamed staging, each on its staged break.

**Evidences:** TOOL-dDeclaredLoop-80
- AC1 — `fixture boundary:` — `python budget.py --fixture --plant no-own-conf-read` printed `fixture boundary: 2 functions — write_budget_plant, run_budget_plant` and `held`, exit 0, and the same plant of `breakpoints.py` printed `fixture boundary: 2 functions — write_pre_placement_plant, run_breakpoint_plant` and `held`, exit 0: 76 AC1's owed exit 0. In a scratch copy of the kit folder whose two modules each gained a module-level `CONF = ".unattended.conf"` and `read_records_root(tree)` returning `(tree / ".memory-tree.conf").read_text()`, each copy's plant named both added lines as `conf name` and ended `MISSED 2 conf read(s)`, exit 1.
- AC2 — `read_planted_root` — a `python -c` probe writing the spec's staged module of four definitions to a scratch file answered `[(3, 'conf name'), (5, 'conf name')]` from `derive_conf_reads`, the lines inside `read_planted_root` and `fixture_rows`, and `['check_plant_root', 'build_fixture_tree']` from `derive_fixture_boundary`; `python budget.py --fixture --plant no-own-conf-read` printed that module's boundary line and its two hits among its rows, then `held`.
- AC3 — `write_pre_placement_tree` — `grep -c` printed 0 PINNED over `breakpoints.py`, and `grep -c "def write_pre_placement_plant"` 1 PINNED; `--plant pre-placement`, `--plant driver-pre-placement`, `--plant pre-placement-records-root` and `--plant unattended-root` of `python breakpoints.py --fixture` each printed `held`, exit 0.
- AC4 — `unset-driver-root` — owed at the close, after the passes of `TOOL-dDeclaredLoop-75`, `TOOL-dDeclaredLoop-79`, `TOOL-dDeclaredLoop-82`, `TOOL-dDeclaredLoop-86` and `TOOL-dDeclaredLoop-87`; not observed here.
- AC5 — `derive_fixture_boundary` — `grep -c` over `tools/loop/README.md` printed 2 PINNED, its own row and the `derive_conf_reads` row naming it.

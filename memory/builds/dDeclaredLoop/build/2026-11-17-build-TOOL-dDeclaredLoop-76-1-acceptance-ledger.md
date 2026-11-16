# TOOL-dDeclaredLoop-76 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-76

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-6 of the spec, over the working tree: the three added plants and both `confs-disagree` plants run alone
by `--fixture`, standing in for the `loop budget fixtures` and `loop breakpoint fixtures` legs, with both
`unattended-root` plants run alone the same way over the split resolver; `python -c` probes of
`derive_conf_reads` and of the plants' hits; and the `grep` probes, standing in for the `docs` leg. The
section 5 sweep re-run at this pass's base held its design claims: the lexicon offender pin at 1215 PINNED
with both new functions leading with a declared verb, no shell file edited, no verb or flag added and the
help anchors' fingerprints unchanged, no file on the kickoff watch list edited; its stale figures are
deviation 763.

Owed to the close: every leg section 7 names, and both plant legs, which exit non-zero on
`no-own-conf-read` alone until `TOOL-dDeclaredLoop-80`'s pass commit (section 8 F3). Owed RED-first: the
`tools/loop/budget.py` arm, `no-own-conf-read` and `root-source`, and the `tools/loop/breakpoints.py` arm,
`no-own-conf-read`, each on its staged break. A probe in this pass observed both budget breaks: the scratch
copy below named its added line, and `resolve_memory_root_source` rebound in process to guess the source
from the root made `root-source` print `MISSED tree answered`.

**Evidences:** TOOL-dDeclaredLoop-76
- AC1 — `conf name` — `python budget.py --fixture --plant no-own-conf-read` printed 8 PINNED hits and `python breakpoints.py --fixture --plant no-own-conf-read` 8 PINNED, every one `conf name` and none `reader call`, each plant ending `MISSED 8 conf read(s)` and exiting 1; the `ast` probe mapped all 8 PINNED budget hits to `tools/loop/budget.py#run_budget_plant`, and of the breakpoints hits 7 PINNED to `tools/loop/breakpoints.py#run_breakpoint_plant` and 1 PINNED to `tools/loop/breakpoints.py#write_pre_placement_tree`, each a function that seeds or asserts a scratch tree. In a scratch copy of the kit folder whose `budget.py` gained `(root / ".unattended.conf").read_text()` in `read_budget_value`, the copy's plant named that line as `conf name` among 9 PINNED hits. The exit 0 is owed at `TOOL-dDeclaredLoop-80`'s pass commit.
- AC2 — `SyntaxError` — a `python -c` probe of `derive_conf_reads` answered `[]` over a scratch module whose module, function, `async def` and class docstrings and a comment each name `.unattended.conf`; five hits over the module holding the five reads, the first three `reader call` and the last two `conf name`, the f-string's included; and raised `SyntaxError` over a module that does not parse.
- AC3 — `(records, .unattended.conf)` — `python budget.py --fixture --plant root-source` printed `('records', '.unattended.conf')`, `('records', '.memory-tree.conf')` and `('memory', 'default')` with `resolve_memory_root` answering `records`, `records` and `memory`, then `held`, exit 0; `--plant confs-disagree` of both modules printed `held`.
- AC4 — `grep -c ".unattended.conf"` — owed at the close, after `TOOL-dDeclaredLoop-75`'s pass; not observed here.
- AC5 — `no-own-conf-read` — `grep -c` printed 1 PINNED over `help/loop.md`, and over `tools/loop/README.md` `resolve_memory_root_source` 3 PINNED and `derive_conf_reads` 1 PINNED.

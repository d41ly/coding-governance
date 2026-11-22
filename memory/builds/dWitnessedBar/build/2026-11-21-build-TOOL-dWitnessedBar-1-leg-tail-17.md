# TOOL-dWitnessedBar-1 leg-tail 17 — python reads (a name never bound, an import outside its guard) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** python reads (a name never bound, an import outside its guard)
- **Hash:** 98fcd2fc56a6fdfdce818c936767ede707698073
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg python reads (a name never bound, an import outside its guard) | exit 1
py-reads: RED guard · codebase-map gate coverage · tools/memory-tree/backlog.py is imported and outside its guard
py-reads: RED guard · codebase-map gate coverage · tools/memory-tree/id_grammar.py is imported and outside its guard
py-reads: RED guard · codebase-map gate coverage · tools/memory-tree/legacy_ledger.py is imported and outside its guard
py-reads: RED guard · codebase-map gate coverage · tools/memory-tree/tree_lib.py is imported and outside its guard
py-reads: RED guard · recall floor · tools/memory-tree/coverage_join.py is imported and outside its guard
py-reads: RED guard · recall floor · tools/memory-tree/legacy_ledger.py is imported and outside its guard
py-reads: RED guard · recall floor arms · tools/memory-tree/coverage_join.py is imported and outside its guard
py-reads: RED guard · recall floor arms · tools/memory-tree/legacy_ledger.py is imported and outside its guard
py-reads: RED guard · codebase-map kit selftest · tools/memory-tree/backlog.py is imported and outside its guard
py-reads: RED guard · codebase-map kit selftest · tools/memory-tree/id_grammar.py is imported and outside its guard
py-reads: RED guard · codebase-map kit selftest · tools/memory-tree/legacy_ledger.py is imported and outside its guard
py-reads: RED guard · codebase-map kit selftest · tools/memory-tree/tree_lib.py is imported and outside its guard
py-reads: RED guard · memory-recall kit selftest · tools/memory-tree/coverage_join.py is imported and outside its guard
py-reads: RED guard · memory-recall kit selftest · tools/memory-tree/legacy_ledger.py is imported and outside its guard
py-reads: RED params · tools/loop/claim.py · read_claim_lines · root · undeclared site (1 measured, 0 kept)
py-reads: RED params · tools/loop/loop_lib.py · read_builds_dir · kit_dir · undeclared site (1 measured, 0 kept)
py-reads: guards, not read · a module reached through a subprocess, a python -c body, a data file a suite reads, a kit named by a computed string, a dynamic import
py-reads: names, not read · a name bound in one function and read in another, a read before its binding, an attribute, a name in a string or an eval, a Python script with no .py suffix
py-reads: params, not read · a lambda, a parameter read only through locals() or a string
py-reads: guards · 27 suites walked, 46 guarded legs of another head not read
py-reads: names · 216 files read, 0 star imports skipped
py-reads: params · 113 hits, 108 kept rows, 2 unlisted, 0 stale
```

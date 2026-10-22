# TOOL-dTrueNorth-25 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-25

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the one
function the pass mints, inside the gate's inline program (`--suggest print_line --as py.function`,
OK). Every criterion below was observed by a probe of the changed code at the working tree over
`6f90a8547`: AC1 and AC3 in a clone of this worktree under `%TEMP%/u25c`, this unit's four product
files copied in and committed there; AC2 and AC4 in a scratch repository under `%TEMP%/u25f`. Each
red-when was observed by running the base gate's bytes, `git show 6f90a8547:` of the gate, over the
same repository state: it exited 0 printing a clean verdict on each. The suite arms the `New arm:`
line names, and their RED-first observation, are owed to the close.

**Evidences:** TOOL-dTrueNorth-25
- AC1 — `check-verdict-epoch.sh` — in the clone, `bad.append((key, "runs past its one line"))` in
  `read_record` became `"runs past its single line"`, committed with no bump, and the clone's gate
  with that commit's parent as base exited 1 printing `moved: tools/memory-tree/deviation_join.py`.
  The base gate over the same range exited 0 printing `clean — no behaviour-bearing engine line moved`.
- AC2 — `design_lib.py` — the scratch repository held an engine carrying a
  `KIT_MEMORY_TREE_VERSION` line, a copy of the gate, a `design_lib.py` importing `newmod` inside a
  function, and `newmod.py`; the copy with the base commit as base exited 2 printing
  `tools/memory-tree/newmod.py is imported by tools/memory-tree/design_lib.py and is not in DELEGATES`.
  The base gate over the same commit exited 0 with a clean verdict.
- AC3 — `HEAD` — the clone's gate before the edit, with its `HEAD` as base, exited 0, printing the
  closure line at 13 sibling module(s), and its scanned list holds `deviation_join.py`,
  `routed_commits.py` and `backlog.py`. The probe's own `ast` walk over the same scan set, a script
  of its own, read 13 modules: the eleven kit modules §4 names, the checker and the recall kit's
  `extract.py`. Over the DELEGATES list before S1 that walk reached the three outside it, `backlog.py`
  by `row_grammar.py:270`, `deviation_join.py` by `gen_build_index.py:6244` and `routed_commits.py`
  by `deviation_join.py:127`.
- AC4 — `design_lib.py` — the same scratch repository with `design_lib.py` holding `def load(:`: the
  copy exited 2 printing that `tools/memory-tree/design_lib.py` does not parse, so its imports were
  not read, with the `SyntaxError` beside it. The base gate over that tree exited 0 with a clean verdict.
  With no launcher on `PATH`, the copy printed the note that the closure was not checked and exited 0.
- AC5 — `git grep -n "deviation_join.py" -- tools/memory-tree/README.md tools/memory-tree/asbuilt_view.py` —
  listed `README.md:28`, whose render's-code sentence now reads `asbuilt_view.py`, `design_lib.py`,
  `deviation_join.py` and the host calls, and `asbuilt_view.py:32`, the docstring's render's-code
  sentence, beside the two rows that already named the module, 26 and 27. Then
  `git grep -n "import closure" -- tools/memory-tree/README.md` listed line 29, the gate's row.

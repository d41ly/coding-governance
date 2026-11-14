# TOOL-dDeclaredLoop-58 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-58

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on
node `d` (win32) by the probe the spec's §4 "The probe the criteria share" spells, over the
repository `commit_trailers.build_fixture` planted from `tools/memory-tree/` under a short scratch
directory, and by the two `grep` commands of AC4 over the built tree. The pass base is `460e8456`.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of its one
`New arm:` line in `tools/memory-tree/routed_commits.py#run_selftest`, staged for one run by the
range `HEAD~3..HEAD` in the arm's spawn and, on win32, for one run by deleting the `reconfigure` call
from the memory-tree copy of the trailer CLI, each restored.

**Evidences:** TOOL-dDeclaredLoop-58
- AC1 — `tokens HEAD` — the probe over the planted fixture, the CLI's bytes matched to the shas
  `git rev-list HEAD` printed there, printed `[]`.
  figure: DERIVED, the expected shas are `git rev-list HEAD` over the fixture at observation time.
- AC2 — `tokens HEAD~3..HEAD` — the CLI exited 0 and wrote no byte; the probe printed one finding,
  which names the count read against the count expected and the shas git lists, and none naming a CR.
- AC3 — `sys.stdout.reconfigure(newline="\n")` — a scratch copy of the memory-tree trailer CLI
  without that line, run with `tokens HEAD` over the same fixture, wrote a CR on every line; the
  probe printed exactly one finding, `a CR reached the output`.
- AC4 — `check_lf_lines(` — the first `grep -n` showed the definition and one call inside
  `run_selftest` passing `out38`; the `grep -c` for the bare CR test over the same file printed `0`.

Also probed on the built tree: a scratch `python -c` that imports
`tools/memory-tree/routed_commits.py`, plants a fresh fixture and runs the arm's own spawn and
`run_git` read through the predicate printed `[]` for `tokens HEAD` and the one count finding for
`tokens HEAD~3..HEAD`. It stands in for the `routed-commits selftest` leg until the close.

# TOOL-aPrimedIndex-1 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-1

No merge bar and no self-test suite ran in this pass. Every criterion was observed directly on node
`a` against the working tree of this pass. The descriptor edits were applied by one binary-safe
patch whose every anchor had to match exactly once. Running the declared checks found a defect the
spec of TOOL-aPrimedIndex-2 did not foresee: Windows found WSL's `bash` before Git-Bash's, and that
`bash` cannot read a linked worktree's `.git` file, so eight checks first read "not a git repo".
That unit's reader now resolves each program on `PATH` before it runs it, and its spec takes the
change as rev-2. The check below ran through that corrected reader, copied into the kit directory
for the run and deleted afterwards. The close still owes the narrow guarded legs this unit's §7
names, every one a held self-test.

**Evidences:** TOOL-aPrimedIndex-1
- AC1 — `tomllib` — a `python -c` read of every tracked kit descriptor printed eleven items, one per row of §4's inventory: the build index's three rows joined into one, plus the memory-tree render's two identical rows joined into one. It printed `partial []`. Break: with the gotchas row's `check` line removed from a copy of `tools/memory-tree/kit.toml`, the same probe printed `partial: ['{memory_root}/gotchas/INDEX.md']`.
- AC2 — `check` — all eleven `check` argvs, run from the repo root through the reader, printed `regen: fresh` for ten items. The eleventh, the codebase map, read `STALE` only because the reader copy sat untracked in the kit directory while it ran (`gen_map.py` reads untracked files). With the copy removed, `gen_map.py --check` exited 0. 91 s concurrently.
- AC3 — `resolve_generated_indexes` — called from `tools/unattended/lib-unattended.sh` before and after the edit, it printed byte-identical pair lists. `cmp` of the two captures exited 0.
- AC4 — `python tools/govkit/govkit.py selfcheck` — it exited 0. It printed `generated outputs: 6 [[generated]] row(s) declared across the descriptors` and no `FAIL` line, so check 6c found the shell reader and tomllib in agreement on every row.
- AC5 — `grep -n "stage" tools/run-gates/README.md` — it printed eight lines. They cover the two tables' keys and the three stage meanings, in the new section "Generated outputs — declared by the kit that writes them".

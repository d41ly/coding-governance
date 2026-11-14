# TOOL-dDeclaredLoop-38 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-38

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on
node `d` (win32) over the repository `commit_trailers.build_fixture` planted from `tools/lib/`, under
a short scratch directory, each probe run once at the pass base `f261b589` and once on the built
tree. The pass base is `f261b589`.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of its one
`New arm:` line in `tools/memory-tree/routed_commits.py#run_selftest`, staged by deleting the
`reconfigure` call from the memory-tree copy for one run and restoring it.

**Evidences:** TOOL-dDeclaredLoop-38
- AC1 — `tr -cd '\r'` — `python commit_trailers.py tokens HEAD` and `--print-commits`, from the
  canonical copy inside the fixture, each redirected to a file: at base each file held a CR on
  every line; on the built tree each count printed `0`.
  figure: PINNED, measured 2026-11-14: 3 CRs in each file at base, 0 in each on the built tree, 3 lines in the `tokens` file.
- AC2 — `_SUBJ` — the loop statement of `tools/unattended/check-pass-order.sh`, fed
  `done < <(python <canonical copy> tokens HEAD)` with no stage after it, then the `case` on the
  fixture's HEAD against ` TOOL-tFix-2 `: no match at base, a match on the built tree.

Also probed on the built tree: the `commit_trailers_py` block reads byte-identical across the three
copies, and the `message` and `--fixture` verbs write no CR. A scratch `python -c` that imports
`tools/memory-tree/routed_commits.py` and runs the new arm's spawn over a planted fixture read no CR
in its bytes; it stands in for the `routed-commits selftest` leg until the close.

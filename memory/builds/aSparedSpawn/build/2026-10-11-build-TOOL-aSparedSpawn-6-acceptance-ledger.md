# Acceptance ledger — TOOL-aSparedSpawn-6

**Serves:** journal TOOL-aSparedSpawn-6

Node `a`, 2026-10-11, beside other worktrees' work, with one process spawn costing about 1.8 s. The
pass ran no bar, no suite, no held leg and no slice of a suite. A first pass on this unit was stopped
because its brief allowed slices; nothing it observed through a slice is cited here. Every check
below is the changed driver invoked directly, a checker run on the tree, or a suite predicate run on
its own over the real driver and a staged copy. `bash -n` passed on the driver, its suite and the
probe. The suite's new and changed arms were checked by reading; every criterion only a shard can
observe is owed at VERIFYING and says so.

**Evidences:** TOOL-aSparedSpawn-6
- AC1 — `2026-10-11-build-TOOL-aSparedSpawn-6-fork-probe.sh` — at 2026-10-11T07:50:15Z on node `a`,
  over the driver at `20defc263` before any driver line changed, 262 driver functions lifted and 20
  forks per cell: a fork cost 122.60 ms bare and 121.64 ms sourced when quiet, and 213.56 ms bare and
  230.57 ms sourced under eight background fork loops. The eight loaders were reaped with none
  alive, and the verdict was GO, under the 3000 ms stop price.
- AC2 — `bash -c '. tools/unattended/unattended.sh; declare -F load_driver_conf main'` — the source
  returned 0, both names printed, `declare` returned 0, and `.git/runlog/driver.log` held 39113
  lines before and after with no line naming the probe shell's pid.
- AC3 — `unattended.sh --version`, run as a process from a copy of HEAD's driver and from a copy of
  this pass's driver, each beside the unchanged library in one scratch directory — byte-identical.
  `grep -n '\$\$' tools/unattended/unattended.sh` found nothing. A probe file printed `$0` equal to
  `BASH_SOURCE[0]` when executed by a relative and an absolute path, so the three `--hold` remedy
  lines print the same bytes executed. This pass's `--dispatch` and `--brief` ran through the
  refactored driver as processes and exited 0. The `--hold` remedy fixture is a suite arm and is
  owed at VERIFYING.
- AC4 — `main --version` in the shell that sourced the driver — it returned 2, printed the refusal
  naming the leak, and the shell ran its next line.
- AC5 — `check-arms.py --report` — the driver's 369 rows, normalised with the line column dropped,
  are identical to the rows recorded before the driver changed: 369 branches, 360 armed.
  `check-arms.py --emit-floors` prints `374:360` for the driver where `.memory-tree.conf` holds the
  floor `362:348`; the row set is unchanged, so the emission is the one the unchanged rows give and
  the token does not move. It does not literally reproduce the token, and the gap predates this unit.
- AC6 — not run — owed at the owner's equivalence run: each shard once with
  `UNATTENDED_HARNESS=process` and once with `inproc`, compared by assertion count and sorted
  assertion multiset.
- AC7 — `unattended.sh --plan aSparedSpawn`, as a process and as `( load_driver_conf && main … )` in
  a shell that sourced the driver — 17 lines byte-identical, rc 0 and 0, `git status` unchanged. A
  grep of the parity rows against `VERBS_SLUG`, `VERBS_INLINE` and `--overlaps` found every verb
  carried by a row. The parity table itself and its staged `read_bound_key` break are owed at
  VERIFYING with shard 1.
- AC8 — the two tail predicates, each confirmed byte-identical to the suite's text and run alone —
  the top-level-exit scan found only the declared missing-library exit on line 90 of the real driver,
  and also line 731 in a copy staged with an undeclared `exit 3`. The namespace comparison read empty
  on two dumps of the 327 sourced definitions. It named `readme_of` and `verb_list` once one was
  doubled and the other unset, and read empty again after re-sourcing the driver. The arms inside
  their shard are owed at VERIFYING.
- AC9 — not run — owed at VERIFYING: the staged zero under `UNATTENDED_HARNESS=inproc` and the green
  process-mode shard are shard runs.

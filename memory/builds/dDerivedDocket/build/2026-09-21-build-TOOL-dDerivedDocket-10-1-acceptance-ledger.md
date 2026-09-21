# TOOL-dDerivedDocket-10 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-10

The driver's view-against-shard refusal, its class-keyed census for a per-build backlog, and the
repo-subject `--check` mode behind the new `row-driver view refusal` leg. AC6, AC8 and AC9 each
carry a `permission:` line deferring an observation to the run the main loop makes at `VERIFYING`;
those get no line here and the orchestrator writes them after that run.

NO MERGE BAR, NO GATE LEG AND NO `*.test.sh` SUITE RAN IN THIS PASS. Every arm below was observed
against a scratch fixture repository or a staged break, by hand. The arms of groups 48 to 53 were
exercised from a scratch harness assembled out of the suite's own bytes — its header, its `run` and
`never_worse` helpers, and the new groups verbatim — so what was observed is the text that ships,
not a paraphrase of it. Nine breaks were staged one at a time into `tools/memory-tree/merge-rows.py`
and the driver restored from a byte copy after each; every arm named below was seen RED under its
own break and green with the fix restored, which is AC9's in-pass obligation.

**Evidences:** TOOL-dDerivedDocket-10
- AC1 — `bash tools/memory-tree/merge-rows.test.sh` group 48 — ours a view rendered through the
  view layer's own renderer and this install's `GEN_HEADER`, theirs an authored shard with one
  incoming row. The driver exits 1, the written file opens `<<<<<<< ours`, closes
  `>>>>>>> theirs (refused: view vs shard)`, carries ours' view and theirs' incoming row, and
  stderr carries all six recipe lines verbatim — asserted line by line against
  `render_relocation_recipe`'s own output, with a liveness floor on the line count so an empty
  recipe cannot satisfy the loop. Staged RED (B1): the refusal's condition replaced by `if False:`
  reds the closing-marker arm and all six recipe-line arms.
- AC2 — `git config merge.rows.driver` — a fixture repository wired with the shipped
  `merge-rows.sh` wrapper, whose default branch switched `memory/backlog/TOOL.md` to a view after a
  straggler forked from the shard. `git merge --no-edit straggler`, `git merge --squash straggler`
  and `git rebase main` from the straggler each exit non-zero with `REFUSED` on stderr. Staged RED
  (B1): with the refusal gone all three print an ordinary postcondition failure instead and every
  arm reds by name.
- AC3 — `%A` — the driver copied into a scratch tree beside a deliberately unparseable
  `backlog.py`. With the view layer INTACT the same scratch driver merges an ordinary append
  collision clean, which is the liveness half; with it broken the driver exits 1, writes
  `<<<<<<< ours` and keeps theirs' `INCOMING` row. Staged RED (B9): the view layer imported at
  module scope kills the driver before `%A` is written, and both arms red on the ours-only file.
- AC4 — `git merge` over a fixture `BACKLOG.md` — two branches, one appending a `SEV` row for an
  ask and the other a `KEEP` for the same ask. The merge exits 0, each of the two rows and the ask
  itself appears exactly once, and the file carries no markers. Staged RED (B3): the keying forced
  back to `row_ids` counts one id three times against two and the whole file conflicts, which is
  the false contest this criterion exists to remove.
- AC5 — `%P` — the same fixture with two STATUS rows for one ask exits 1, fail-closed, as V4 would
  require anyway. And the audit line names its census: `census class-keyed` when `%P` is a
  `builds/<slug>/BACKLOG.md`, `census generic` when `%P` is omitted, and `census generic` when `%P`
  names an ordinary governed index. Staged RED (B4): `check_build_backlog` forced to answer True
  reds the two generic arms.
- AC7 — `--check` — four scratch repositories, each a real `git` tree. Removing
  `memory/backlog/*.md merge=rows` from a shards-mode fixture makes it exit 1 naming
  `memory/backlog/TOOL.md`, and the same fixture passes before the removal. A copy of the driver
  with the refusal disabled by `sed` makes it exit 1 naming the view-against-shard probe, with a
  guard that reds if the staged break changed no byte. Overriding one file's attribute in a NESTED
  `.gitattributes` is caught too, which is what `git check-attr` buys over a grep of the
  declaration. Staged RED (B5): the attribute comparison replaced by an empty list reds both the
  removal and the nested override; (B7): the probe's failure branch no longer returning 1 reds the
  disabled-refusal arm.
- AC10 — amended rev-6 — the criterion's middle clause, requiring `gen_build_index.py --write` to
  exit 0 over the merged view with the result byte-equal to a fresh render, was removed; §9's
  rev-6 item (2) records why, that it grades the view unit's data-loss guard which §3 puts OUT of
  this unit, and how to reverse it. What the criterion keeps was observed in
  `bash tools/memory-tree/merge-rows.test.sh` group 52: two views re-rendered with adjacent row
  changes are not refused and the driver prints its audit line, and a shard-against-shard merge
  over a VIEW base is not refused either. Staged RED (B2): the refusal keyed on `view_a or view_b`
  reds both arms of the re-render case.
- AC11 — `merge-rows.py --check` — a builds-mode fixture tracking two `builds/*/BACKLOG.md` files
  reports four governed paths and `mode builds`; overriding one of them reds naming
  `memory/builds/zTwo/BACKLOG.md`; a builds-mode fixture tracking none announces the empty half and
  passes. A sixth arm added this pass asserts the empty-population refusal against a fixture whose
  `MEMORY_ROOT` names a directory nothing is filed under. Staged RED (B6): the builds selector
  switched off drops the count to two and the override goes unseen; (B8): the empty-population
  refusal removed lets a zero-path run report `0 governed path(s)` at exit 0.

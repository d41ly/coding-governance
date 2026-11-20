# TOOL-dWitnessedBar-41 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-41

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed on node d, 2026-11-20, at base `386b3ebee`, by two scratch probes over
fixture repositories at `%TEMP%/w41a` and `%TEMP%/w41b` that ran this pass's runner and hook, by
`verdict_flow.py select --check` run over planted files, and by one probe that extracted
`check_tree_selection` from the hook and ran it under a counting stand-in for `check_selection_at_r`.
The two `New arm:` lines of spec section 7 were written and not run: their runs, their RED-first
observations and the section 7 legs are owed to the main loop at the close.

**Evidences:** TOOL-dWitnessedBar-41
- AC1 — `selection.1` and `selection` were written by a full run of this pass's `run-gates.sh` over a two-leg scratch clone, `GATE_SELECTION`
  naming a file outside it that held a `# planted` header, the TAB row `held · guarded · quarantine ·
  TOOL-x-7` ending in CRLF and a `not-held` row, held `guarded` as `(quarantine, TOOL-x-7)`, printed the
  `not-held` row as ignored, and wrote `selection 392504f4…` and `selection.1 guarded · quarantine ·
  TOOL-x-7` into `gate-verdict/<tree>`; `git hash-object --stdin` of that row TAB-separated
  and LF-terminated printed the same `392504f4…`. A second run with no `GATE_SELECTION` wrote
  `selection none` and no `selection.1`. The `run-gates evidence` arm is owed at the close.
- AC2 — `.githooks/pre-push` was run from a second, detached worktree of a clone whose R holds `verdict_flow.py`,
  a manifest giving leg `x` level `e2e` and a policy landing `unit integration` under
  `report-unrun`, with no run dir of the first worktree, over the merge of X: a GREEN record whose
  selection held `x · quarantine · TOOL-x-7` was not covered, the line naming `the bar's selection is
  not what <R> derives` and `adds x · quarantine · TOOL-x-7`, and the stand-in bar ran once; one whose
  selection held the `level` row R derives was covered with no bar run, as was one reading `selection
  none`. `verdict_flow.py select --check --selection <file> --rev <R>` exited 1 on the first rebuilt
  file and 0 on the second, and exited 2 given neither or both of `--run` and `--selection`. The
  extracted `check_tree_selection` ran its stand-in check once over two calls on one hash.
- AC3 — `selection.1` edited and `selection` deleted: the same hook over a record whose `selection.1` was edited after its hash was taken was not
  covered, naming `the recorded full tree verdict's selection rows do not hash to <sel8>, so a row was
  edited or lost`, and one with no `selection` key was not covered, naming `the recorded full tree
  verdict carries no selection, so it cannot say whether its bar held legs`; the bar ran once for
  each. The `pre-push self-test` arm is owed at the close.

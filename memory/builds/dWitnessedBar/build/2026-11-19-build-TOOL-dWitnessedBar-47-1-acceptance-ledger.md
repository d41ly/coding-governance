# TOOL-dWitnessedBar-47 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-47

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the canonical
`tools/lib/legacy_ledger.py seed` run in a scratch `git init` at `%TEMP%/w47s` with nothing committed,
and the two adopters each run once on a fresh `git init` target at `%TEMP%/w47da` and `%TEMP%/w47cm`
holding the kit under test and the memory-tree kit beside it, nothing committed, first with the
memory-tree copy as this pass leaves it and then with that copy restored from the pass's base. The two
`New arm:` lines of spec section 7, arm 8 of `tools/codebase-map/adopt-codebase-map.test.sh` and
section `2o`'s moved AC5 case, its untracked-directory case and its fresh drift-audit adopt in
`tools/lib/resolve-python.test.sh`, were written and syntax-checked with `bash -n` only; each still
owes its RED-first observation, which the main loop makes at the close, and so does every leg that
section names.

**Evidences:** TOOL-dWitnessedBar-47
- AC1 — `affordance-exempt.toml` — one `adopt-codebase-map.sh --scaffold` on the uncommitted target,
  its conf copied first, printed `seed: HEAD is unborn, rows carry the null SHA`, `armed
  memory/map/affordance-exempt.toml` and `Adopted.`, exit 0, and the file existed under
  `memory/map/`. One `adopt-drift-audit.sh` on its uncommitted target printed `drift-audit: armed
  tools/drift-audit/drift_signals.py`, exit 0, and `drift_signals.py` existed; `git log` still read no
  commit. With the base's tracked-file test restored in the memory-tree copy, the drift-audit adopt
  printed `unarmed tools/drift-audit/drift_signals.py home directory tools/drift-audit holds no
  tracked file`, exit 1, and wrote no file, and the codebase-map adopt printed `unarmed
  memory/map/affordance-exempt.toml home directory memory/map holds no tracked file`, exit 1.
- AC2 — `no directory` — `grep -n 'no directory' legacy_ledger.py` in `tools/lib/` named lines 35,
  471 and 479, the last the refusal `return "no directory %s" % parent`; the module docstring names the
  blind spot, a file name the hygiene check's structure check refuses inside an existing directory,
  written and red at that check's next run. The block is byte-identical in the three copies, read by a
  `python -c` cut between the `legacy_ledger_py` markers.
- AC3 — `unarmed p no directory` — `seed --population p`, the home `newdir/p.txt` and no `newdir`,
  printed `unarmed p no directory newdir`, exit 1, with `legacy_ledger: newdir/p.txt: no directory
  newdir; nothing written` on stderr, and `newdir` did not exist afterwards. With `newdir` made and
  nothing committed it printed `armed p 2`, exit 0, and wrote two rows stamped with the null SHA.
  Outside the criterion: `seed --home other/x.txt -- python -c 1` printed `unarmed other/x.txt no
  directory other`, exit 1, and created no `other`.

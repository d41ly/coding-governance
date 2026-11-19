# TOOL-dWitnessedBar-53 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-53

No merge bar, no self-test suite and no gate leg of this repository ran in this pass, the naming lexicon
excepted; the memory-hygiene suite that now carries the arm did not run. The criteria were observed through
a probe of the arm's own code on node d, 2026-11-19: a scratch `git init` at `%TEMP%/p53` built as S1 builds
it, the kit copied to `tools/memory-tree/` and staged, the example conf copied with `FOO_PIN="3"` appended
and left untracked, and the arm's python helper extracted from the suite itself by `sed` and run there for
its save, clear and compare modes. The `New arm:` of spec section 7 owes its RED-first observation at the
close (dropping `--others` from `read_root_confs`), and so does every leg that section names.

**Evidences:** TOOL-dWitnessedBar-53
- AC1 — `armed conf-scalar-pins` — the scaffold over the uncommitted target exited 0 and printed
  `armed conf-scalar-pins 1`, `git status` reading the conf `??`; P was `{conf-scalar-pins}`. The helper
  saved the home, `git add -A && git commit` ran, the helper removed the home, `legacy_ledger.py seed
  --population conf-scalar-pins` printed `armed conf-scalar-pins 1`, and the compare printed `compared
  conf-scalar-pins 1 rows`, exit 0. With the saved count tampered it printed `unequal conf-scalar-pins`, exit 1.
  Red with the defect: with `--others` dropped from the fixture's kit copy of `ratchet.py`, the scaffold
  printed `armed conf-scalar-pins 0` and the compare printed `unequal conf-scalar-pins: saved [], re-seeded
  [(('.memory-tree.conf', 'FOO_PIN'), 1)]`, exit 1. An empty P compares nothing and exits 0, so the arm's
  `[ -n "$_wp" ]` and its `grep -qx 'conf-scalar-pins'` carry S2. Owed at the close: the arm itself, run by
  the memory-hygiene self-test, and its RED-first observation.
- AC2 — `FOO_PIN` — before the commit the kit copy's `keys-not-scalar` printed `held · .memory-tree.conf TAB
  FOO_PIN TAB 1` and `pass`, exit 0, read in the first probe script before the role hook refused a direct
  run of that leg; after the refusal it was not run again, so the after-commit half is OWED at the close,
  through the arm's third assertion.
- AC3 — `FLOOR_ASSERTIONS` — `grep -n '^FLOOR_ASSERTIONS=' check-memory-hygiene.test.sh` reads 789 against
  785 in the parent commit's file, the arm's four `n=$((n+1))` counted by reading from the diff, beside a
  `RAISED 785 -> 789 by TOOL-dWitnessedBar-53` comment. Owed at the close: the suite's executed count.

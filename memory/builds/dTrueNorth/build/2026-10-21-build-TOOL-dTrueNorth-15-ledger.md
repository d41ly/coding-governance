# TOOL-dTrueNorth-15 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-15

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon included,
since the pass names no new function. Every
criterion was observed by a probe of the changed code: the generator's own CLI in a scratch clone of
the branch under the user temp directory, short-named, with this pass's four product and spec files
copied in and committed there, so the clone's tree is the pass commit's less its renders and this
ledger; and the green arm of check 29's `case`, read verbatim out of the engine at line 1662 and
evaluated over the verb's output in that clone. The probes stand in for the `build-index selftest`
and `memory hygiene` legs and the `memory-hygiene self-test` suite; those, with the new suite arm's
RED-first observation, are owed to the close.

**Evidences:** TOOL-dTrueNorth-15
- AC1 — `python3 tools/memory-tree/gen_build_index.py --check-coverage` — in the clone before the
  files were copied in, at `0c0d1bb0e`, it exited 0 and printed nothing; at the clone's commit of
  this pass's tree, where no measured chain spec is `INPROGRESS`, it exited 0 and printed one line:
  `build-index: coverage — check 29 graded 0 INPROGRESS chain spec(s) in 0 of 22 chain build(s) — nothing graded: no chain spec is INPROGRESS, and under the unattended harness a spec goes OPEN to CLOSED in its build commit, so this check grades attended builds only`.
- AC2 — `check 29 graded 1 INPROGRESS chain spec(s) in 1 of` — with this spec's header set to
  `INPROGRESS` in the clone and the coverage otherwise clean, the verb exited 0 and printed
  `build-index: coverage — check 29 graded 1 INPROGRESS chain spec(s) in 1 of 22 chain build(s)`.
  With a planted dTrueNorth row for an uncarried `cl-dClosedLoop-0599` in the as-built view as well,
  it exited 1, printing the refusal line naming this spec and `uncarried cl-dClosedLoop-0599` first
  and the same count line after it.
- AC3 — `New arm:` — the engine's green arm at `tools/memory-tree/check-memory-hygiene.sh:1662`,
  evaluated over AC1's output, printed
  `memory-hygiene: check 29: coverage — check 29 graded 0 INPROGRESS chain spec(s) in 0 of 22 chain build(s) — nothing graded: no chain spec is INPROGRESS, and under the unattended harness a spec goes OPEN to CLOSED in its build commit, so this check grades attended builds only`,
  so S2 needed no engine change. The new arm's own predicate, read out of
  `tools/memory-tree/check-memory-hygiene.test.sh` and run over that line with the fixture's one
  chain build substituted for 22, matched; over the silent output of the base verb it did not; and
  over the verb's output under `PYTHONIOENCODING=cp1252` it matched. The arm itself, RED on the base
  verb and GREEN here, is owed to the close.
- AC4 — `grep -n 'CHECK 29 GRADES ATTENDED BUILDS ONLY' memory/builds/dClosedLoop/BACKLOG.md` —
  printed one row, line 14, the `PLAY-dClosedLoop-20` ask; `grep -c 'SEV · PLAY-dClosedLoop-'` over
  the file counted 10, against 9 at `0c0d1bb0e` and 9 at `271aa59d`.

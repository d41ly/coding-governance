# TOOL-aLiftedCeiling-2 — acceptance ledger

**Serves:** journal TOOL-aLiftedCeiling-2

Each line is a probe the builder ran over the pass's working tree at rev-1 of the spec. No leg, suite or bar ran in the pass.
Where a line says "owed", the main loop observes it after every unit is terminal.

**The write.** In a fresh `git clone --local` of this worktree at 9ee033127, under a short temp path outside the repository and
with no run record in its git directory, the run-gates kit's write ran with the spec's `--reset`, `--observed` and `--how` in one
call under node a. Its summary named 1 dropped by --reset, 0 killed readings removed by --reset and 1 raised by --observed, and
the clone's diff was the one row replaced (DERIVED at 9ee033127). The generated evidence file was copied over this worktree's.

**Evidences:** TOOL-aLiftedCeiling-2
- AC1 — `1` — the spec's grep over the evidence file printed 1 (DERIVED at 9ee033127, over the copied-back file).
- AC2 — `1` — the evidence file's diff against 123123146 counts one added line and none deleted (DERIVED at 9ee033127, over the copied-back file).
- AC3 — `1` — the evidence file's diff against b28597c1f counts one added line and one deleted (DERIVED at 9ee033127, over the copied-back file).
- AC4 — `derive-ceilings.py --check` — owed: the role hook refused the ceiling check in this pass as the leg "leg ceilings clear
  their evidenced maximum" (PINNED, the hook's refusal in this pass).

**Owed to the close.** AC4, and every leg of the spec's Gates section. The spec declares no `New arm:` line.

**Main-loop observation at the close.** Over pass commit aeb5e0a6b in this worktree (DERIVED at aeb5e0a6b, the scratchpad log
al2-ac4.log).

- AC4 — `--check` — the ceiling check exited 0 with no failure line, and its outside-reading list carries the leg's row with the new
  source text naming the host load and the commit its race ran at.

# TOOL-aLiftedCeiling-3 — acceptance ledger

**Serves:** journal TOOL-aLiftedCeiling-3

Each line is a probe the builder ran over the pass's working tree at rev-1 of the spec. No leg, suite or bar ran in the pass.
Where a line says "owed", the main loop observes it after every unit is terminal.

**The write.** In a fresh `git clone --local` of this worktree at 5d336cf12, under a short temp path outside the repository and
with no run record in its git directory, the run-gates kit's write ran with the spec's `--reset`, `--observed` and `--how` in one
call under node a. Its summary named 1 dropped by --reset, 0 killed readings removed by --reset and 1 raised by --observed, and
the clone's diff was the one row replaced (DERIVED at 5d336cf12). The generated evidence file was copied over this worktree's.

**Evidences:** TOOL-aLiftedCeiling-3
- AC1 — `check-install-prefix.sh` — owed: a gate check, the leg "install-prefix (shipped surface)", which the main loop observes
  at the close. The pass's stand-in probe: a grep of the evidence file for the playbook kit's path counted 0 (DERIVED at 5d336cf12, over the copied-back file).
- AC2 — `1` — the spec's grep over the evidence file printed 1 (DERIVED at 5d336cf12, over the copied-back file).
- AC3 — `1` — the evidence file's diff against 123123146 counts one added line and none deleted (DERIVED at 5d336cf12, over the copied-back file).
- AC4 — `derive-ceilings.py --check` — owed: a gate check, the leg "leg ceilings clear their evidenced maximum", which the main
  loop observes at the close.

**Owed to the close.** AC1, AC4, and every leg of the spec's Gates section. The spec declares no `New arm:` line.

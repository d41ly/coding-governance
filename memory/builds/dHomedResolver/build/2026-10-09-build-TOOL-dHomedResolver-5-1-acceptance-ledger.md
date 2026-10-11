# Acceptance ledger — TOOL-dHomedResolver-5

**Serves:** journal TOOL-dHomedResolver-5

Built on `996609b2`. The new arms were run against the code as it stood at `04b0b239` first: the
three `--new-build` arms and the quoting arm failed there. The first try at the `--new-build` arm
used ask `EXMP-aFoo-3`, which grades not-ready in that fixture state, so the command refused on
readiness and two of the arms passed for the wrong reason; the arm now uses `EXMP-aFoo-10`, one of
the asks the wide mandate scaffolds at rc 0. The counting arm cannot be red against `04b0b239`,
whose guard already runs first, so it was run against a scratchpad mutant with the guard moved
below the write loop: it printed `writes=4`. The check-24 arm was run against a mutant whose
missing-home branch skips: it failed there. On this code every arm passes.

**Evidences:** TOOL-dHomedResolver-5
- AC1 — `_read_refusal` — over the `sc` fixture with an untracked archive prints `rc=1 folder=False` and `git add`, and `readme-contract.txt` gains no row; red at 04b0b239
- AC2 — `writes=0` — the refused `cmd_write` calls the writer zero times; `writes=4` against the guard-below-the-loop mutant
- AC3 — `shlex.quote` — the remedy reads `git add -- 'memory/archive/DECISIONS 2026-08-03.md'`; red at 04b0b239
- AC4 — `grep -n 'NOT OBSERVED'` — prints spec 1's S2 and S6 and spec 2's S4, amended in the spec commit at rev-2
- AC5 — `row_grammar.py --selftest` — the missing-home arm prints the `declares its live index at` finding; red against a mutant that skips the branch

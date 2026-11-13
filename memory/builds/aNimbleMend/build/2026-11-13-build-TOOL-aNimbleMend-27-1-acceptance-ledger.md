# Acceptance ledger — TOOL-aNimbleMend-27

**Serves:** journal TOOL-aNimbleMend-27

Built against spec rev-1 in one pass commit. Each line is a probe of the changed code the builder made in the pass, on node a. No suite, gate leg, pass-leg run or bar ran in the pass, and no arm was added. Owed to the main loop at the close: AC4, AC6, AC8 and AC9, the legs of the spec's Gates section, and the re-audit stamp of the kickoff manifest after its body edit. The spec header stays at INPROGRESS for the main loop to close.

**Evidences:** TOOL-aNimbleMend-27
- AC1 — `TZ=UTC0 printf -v` — the criterion's four greps printed 0, 0, 2 and 1, in its order.
- AC2 — `utc` — the criterion's command printed `utc` and then `pass-20261113T063759Z-1842`; in the same shell `PL_STARTED` read `2026-11-13T06:37:59Z`, byte for byte what `date -u` printed, the run id's stamp matched `date -u` likewise, and `TZ` was unset after the two lines.
- AC3 — `72 1` — the criterion's awk printed `72 1`, `156 1` and `74 1`, and its second command printed 0. That second command's source ran to the end: it wrote 426 lines and reported the three rows as registered at the new counts. (PINNED, 2026-11-13)
- AC4 — `':!*.test.sh'` — observed by the main loop on the pass applied to the tree, before its commit: the leg's own command exited 0. (PINNED, 2026-11-13)
- AC5 — `python tools/run-gates/pass_legs.py --check` — `--guards` for each of the five legs printed no line opening `py-reads: RED` and exited 0; `--apply` moved no row beyond the five guards and `--check` exited 0, both printing `pass-legs: 28 declared`.
- AC6 — `python tools/run-gates/py_reads.py` — observed by the main loop on the pass applied to the tree, before its commit: the command printed no line holding `RED` and exited 0. (PINNED, 2026-11-13)
- AC7 — `fork-count: ok manifest-check` — the criterion's grep printed `1` twice, the two bullets measuring 227 and 290 bytes; `--only manifest-check` printed `fork-count: ok manifest-check · measured 76 · ceiling 76`; `--only memory-hygiene` printed `RED`, measured 192 against 191, before the row moved and `fork-count: ok memory-hygiene · measured 192 · ceiling 192` three times after it. (PINNED, 2026-11-13)
- AC8 — `0 red` — observed by the main loop on the pass applied to the tree, before its commit: the whole fork-count run printed `7 passed · 0 red · 0 skipped`, and the staged manifest check exited 0 with no budget warning. (PINNED, 2026-11-13)
- AC9 — `gate-pass-legs.txt` — NOT OBSERVED, owed to the main loop: a role agent's hook refuses the pass-leg runner. `bash -n` over the adapter exited 0, which reads its syntax and not the `KITDIR` it resolves.

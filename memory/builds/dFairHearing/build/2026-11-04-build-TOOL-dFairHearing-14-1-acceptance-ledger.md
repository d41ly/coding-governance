# Acceptance ledger — TOOL-dFairHearing-14

**Serves:** journal TOOL-dFairHearing-14

Built against spec rev-5 and committed as pass commit `c2939c9a6`, at parent `fd056f697`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-14-1-builder-return.md` and the pass commit's message; nothing below was observed again for it. AC7's line was observed at the close. No suite, gate or bar ran in the pass: the `review-replay selftest` leg, the `New arm:` line's RED-first observations and the spec's other legs are owed to the close.

**Evidences:** TOOL-dFairHearing-14
- AC1 — `case_evidence` — with one case's sha blanked, `--experiment` exited 2 naming `incms-decor-texture` and `case_evidence`, and the unblanked control exited 0
- AC2 — `--experiment` — the real held-out file's first line read `frozen at b6c828a92ee5…`. A fixture repository under `%TEMP%/fh14`, since removed, exited 2 when the file had two commits, naming both, and a held-out id copied into the tuning cases exited 2 naming `gov-h-govkit-argv-walker`
- AC3 — `effort` — the run printed `arm m1b@medium: varies effort from m1b`; changing two keys exited 2 naming `effort, model`, and changing none exited 2 naming the arm
- AC4 — `parsed` — the parsed lines, 2 and 3, came before the first figure, line 5. A missing `dispatched` exited 2 naming the arm, and a count too low exited 2 with `19 parsed against 5 dispatched`
- AC5 — `labels rotated — recorded, not checked: no committed key` — a null key printed it, a rotating key read `labels rotated — checked`, and a constant label exited 2 naming arm `m1b` and `ARM-A`
- AC6 — `system.py` — the run printed `system tuning 21/23`, `system held-out 12/12` and `system pooled 33/35`. In the same probe `system.py system` printed 21/23 and 12/12 over the same blobs. It prints no pooled line, so the pooled figure was read against the 2026-10-18 record's stated number, the sum of the two, and not against the tool's output as the criterion words it
- AC7 — `check_experiment` — at the tip `948e4141b` an `ast` walk of the 120 tracked `*.py` under `tools/` found `check_experiment`, `check_held_out_frozen`, `check_one_variable`, `measure_parsed`, `check_judge_rotation` and `measure_union` defined in `tools/workflows/replay_scorer.py` alone, and `--selftest` printed `replay_scorer selftest: 29/29 arms`

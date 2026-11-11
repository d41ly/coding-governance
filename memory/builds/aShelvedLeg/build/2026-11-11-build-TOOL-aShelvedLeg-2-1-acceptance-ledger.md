# TOOL-aShelvedLeg-2 — acceptance ledger

**Serves:** journal TOOL-aShelvedLeg-2

Observed at the build tip 48f3377a7 on node a, 2026-11-11, by the spec's own §6 commands run verbatim from the worktree root. BEFORE is `5f066b0a`, as each criterion's red clause reads it. The unit adds no suite arm. The main loop also ran `run-selftests.sh --rank`, which no longer lists the leg's row as unrecognised (it exits 1 at base and tip for the 21 rows that already fail it), `run-selftests.sh --check`, which is clean, and `run-unattended-gates.sh --help`, which prints the reworded `--attribute` text.

**Evidences:** TOOL-aShelvedLeg-2
- AC1 — `tools/unattended/check-unattended.sh` — the grep prints exactly two lines, both in that file: :54, "READ-ONLY, which is what lets it run on the bar", and :2232, "`GATE_BOUND` is an hour".
- AC2 — `unattended.sh:4844` — the grep over the two files prints nothing, that sentence included.
- AC3 — `tools/unattended/` — the only non-comment change is the `--attribute` help: one `echo` line removed, two added.
- AC4 — `tools/unattended/check-unattended.sh` — the byte probe prints `4 0`, as at base.
- AC5 — `tools/unattended/kit.toml` — the HELD-comment range counts 1 `GATE_SELFTESTS=changed`, and the README section counts 1.
- AC6 — `tools/run-gates/selftest-budgets.txt` — the probe prints `4721 '' ('5', '3147')`.
- AC7 — `tools/run-gates/selftest-pooled-evidence.txt` — the range carries `rc only` once and `UNATTENDED check` once, no `likewise`; `^# no-trailer:` counts 3.
- AC8 — `python tools/memory-tree/gotchas.py --check` — exits 0; the index grep prints 3 and each `--declares` prints `declares: yes`.

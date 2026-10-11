# TOOL-aFrugalTurnstile-13 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-13

No merge bar, no runner and no self-test suite ran for this ledger. AC1 ran the TOOL-aFrugalTurnstile-7
scratch fixture (`f.sh`, case ac9) once against the hook at the previous commit `69426afd` and once
against the edited `.githooks/pre-push`: the previous hook printed `scoped <sha>` with no bar field
(RED), the edit printed the same line followed by a TAB and `bash tools/run-gates/run-gates.sh`. AC2
and AC3 ran the TOOL-aFrugalTurnstile-9/12 `case.sh` fixture (stub hook through core.hooksPath, stub
bar, `GATE_CMD="bash bin/bar.sh"`, a declared `GATE_POST_MERGE=local`) with two new cases, each run
against the driver at `69426afd` and against the edited `unattended.sh`. The close still owes, unrun:
the new AC1 assertion in `.githooks/pre-push.test.sh` and the reworked `run_pm_decide`, the new
AC2/AC3 block in `tools/unattended/unattended.test.sh` plus the TOOL-9 arms whose stub answers now
carry a bar field, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-13
- AC1 — `pre-push --decide <tip> <R>` — the edited hook's one stdout line read `scoped 9546add9…` then a TAB then `bash tools/run-gates/run-gates.sh`; at `69426afd` it read `scoped 9546add9…` with no TAB and no bar.
- AC2 — `not this close's bar` — with the stub answering `covered gate-bar-green@1234abcd`, a TAB and `bash tools/run-gates/run-gates.sh`, the edit printed `decided for 'bash tools/run-gates/run-gates.sh', not this close's bar 'bash bin/bar.sh'; running the full bar`, the stub bar saw `GATE_FULL=1` and a `kind full` record was written; at `69426afd` the close was met without a bar and the stub bar never ran.
- AC3 — `met without a bar` — with the stub's bar field equal to `GATE_CMD`, the edit printed `met without a bar: the boundary reads this tree as covered by gate-bar-green@1234abcd` and the stub bar did not run, as the previous driver also did.

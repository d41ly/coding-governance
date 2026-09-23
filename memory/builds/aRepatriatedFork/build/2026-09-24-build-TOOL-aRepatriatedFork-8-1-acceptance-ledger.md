# TOOL-aRepatriatedFork-8 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-8

Written at the main loop from the unit pass's return (commits `2c8842d6` and `43b98b1a`), because
the pass closed the unit without one and hygiene check 23 then named every criterion. Each line is
an observation that pass made with a fixture probe of real `git push` calls under `%TEMP%`, new code
first and a7c78ad2's bytes second. Nothing here was re-run to write it. No suite ran in the pass:
the lander, hook, run-log, bar and check-wiring suite arms it wrote are owed by the close.

**Evidences:** TOOL-aRepatriatedFork-8
- AC1 — `incms` — with the fixture's only remote named `incms`, the new lander lands at rc 0; a7c78ad2 exits 2
- AC2 — `.githooks/pre-push` — the new hook refuses the red bar with `gate RED`; a7c78ad2 refused earlier, unable to determine the default branch
- AC3 — `pre-push-refusal` — a raw default-branch push leaves the token `raw-push` in the file, and the file is gone after a lander landing
- AC4 — `tools/push-main.sh` — a red bar over a reachable remote is reported as a bar that RAN and is RED, naming `gate-last-summary.txt`; a7c78ad2 said it could not reach origin for a bar printing `connection`
- AC5 — `tools/push-main.sh` — with the remote unreachable and no token, the lander calls it unreachable only after the push-URL probe fails
- AC6 — `tools/push-main.sh` — an untracked superproject file is refused at rc 2; a7c78ad2 pushed it
- AC7 — `tools/push-main.sh` — a submodule holding only its own untracked files passes the lander and the hook; a moved submodule pointer is refused by both, the hook with token `dirty-tree`
- AC8 — `.githooks/pre-push` — a stub bar that commits during its run is refused with `head-moved` and the remote stays put; a7c78ad2 landed it
- AC9 — `GATE_PUSH_BASE` — the stub bar is handed the remote's pre-push sha; a7c78ad2 handed it the inherited value
- AC10 — `GOV_BRANCH_GATE_CMD` — a tracked red bar gives `gate-red`, an untracked one `bar-refused`, and an undeclared seam lets the push through; a7c78ad2 let all three through
- AC11 — `tools/check-wiring.sh` — the git grep for the gov-internal resolver library returns 0 hits, and in a `scripts/` fixture with no `tools/` directory each suite's prologue resolves its subject

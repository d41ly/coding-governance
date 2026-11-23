# TOOL-dQuietDisk-1 leg-tail 29 — pre-push run-log line failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** pre-push run-log line
- **Hash:** 44cf544cc846fc4506ef21e8ff7a9ec74df6dacf
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
hint: "git config set advice.graftFileDeprecated false"
AC7 [primary skip] external execs: baseline 6, writer on 6
AC7 [primary full] external execs: baseline 16, writer on 16
AC7 [worktree skip] external execs: baseline 6, writer on 6
AC7 [worktree full] external execs: baseline 16, writer on 16
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
FAIL BYP R lands: expected [0], got [1]
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
FAIL BYP by the bypass refusal, naming the commit: expected [1], got [0]
FAIL BYP START, the bypass line and END: expected [3], got [2]
FAIL BYP the bypass line names the commit under refused: expected [bypass|unwitnessed-commit|beb0d2072ef37772d5d9cc8753b8740152677b92|refused], got [<absent>|<absent>|<absent>|<absent>]
FAIL BYP END decision: expected [refuse-bypass|clean], got [refuse-bar|clean]
FAIL BYP the refusal token: expected [bypass-refused], got [bar-refused]
FAIL EXITS the scan sees as many sites as the table declares: expected [27], got [29]
FAIL EXITS every exit maps to a decision or a named exemption: expected [none], got [[refuse_wrong_shell || exit 2][write_refusal policy-unrecorded "$why"; RUNLOG_CLEAN=1; exit 1]]
FAIL EXITS every exit after the trap carries the clean-exit mark: expected [none], got [[refuse_wrong_shell || exit 2]]
FAIL EXITS every decision the table names was written by some arm: expected [none], got [[refuse-bypass]]
FAIL EXITS staged: an unarmed exit below the trap is caught: expected [[exit 3]], got [[exit 3][refuse_wrong_shell || exit 2][write_refusal policy-unrecorded "$why"; RUNLOG_CLEAN=1; exit 1]]
FAIL EXITS staged: and it carries no mark: expected [[exit 3]], got [[exit 3][refuse_wrong_shell || exit 2]]
FAIL EXITS staged: a decision exit without the mark is caught: expected [[RUNLOG_DECISION=refuse-raw; exit 1]], got [[RUNLOG_DECISION=refuse-raw; exit 1][refuse_wrong_shell || exit 2]]
FAIL EXITS control: a comment and a string are not exits: expected [none|none|none], got [[refuse_wrong_shell || exit 2][write_refusal policy-unrecorded "$why"; RUNLOG_CLEAN=1; exit 1]|none|[refuse_wrong_shell || exit 2]]
FAILED (263 assertions)
```

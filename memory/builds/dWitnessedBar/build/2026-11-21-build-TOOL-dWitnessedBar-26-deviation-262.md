# TOOL-dWitnessedBar-26 deviation 262 — the floor step's program back at its landed bytes, its refusal a traceback

**Serves:** deviation TOOL-dWitnessedBar-26

- **Departs from:** `TOOL-dWitnessedBar-26@rev-5 [§8 F8]`
- **Hand-off:** code-to-record
- **Before:** F8 resolved (a): the floor stub `tools/govkit/steps/python_floor.py` catches `resolve_shell_argv`'s Refusal, writes it as one `python_floor.py:` line and exits 2.
- **After:** the stub is at the bytes the landed row `lib/python-floor-3.15` names; where no bash resolves, the Refusal propagates and prints a traceback, exit 1, and no bare `bash` is spawned, since `resolve_shell_argv` raises (S7 stands).
- **Cause:** owner ruling
- **Reason:** the stub is the program of a landed upgrade row, and `step-rows-frozen` reds a moved byte of it; F8 was resolved without that rule, which surfaced at the landing's prepare. The owner chose option (a) of the parked decision `landing-python-floor-frozen` over shipping the one-line refusal as a new step: "Yes, fix both".
- **Evidence:** `python tools/govkit/upgrade_steps.py frozen` read 1 problem naming `lib/python-floor-3.15` at fb38204e5 and 0 at 871d58171.
- **Risk:** loosening
- **Approver:** owner, in the session that ran the landing, 2026-11-21, quoted in commit 871d58171
- **Follow-through:** ask TOOL-dWitnessedBar-112
- **Caused-by:** TOOL-dWitnessedBar-26

**Serves:** journal TOOL-dSafePassage-20

# TOOL-dSafePassage-20 — acceptance ledger

The unit as built: `resolve_recorded_introduced` in `tools/govkit/upgrade_steps.py`, beside
`set_step_state`, returning a 40-hex value unchanged, `None` for `UNLANDED` or `None`, and raising
`Refusal` naming anything else; `set_step_state` calling it first, so its validator sees only its
own domain; the dSP-20 arm inside `check_upgrade_steps` in `tools/govkit/selftest.py`, on that
function's existing `sp-land` scratch clone; and `BRANCH_PIN` in `tools/govkit/refusal_join.py`
moved 307 -> 308. S1's constant `UNLANDED` was already the reader's one spelling at this unit's
base (TOOL-dSafePassage-1), so S1 needed no code.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed
by a scratch `python` probe importing `upgrade_steps.py` by path. AC1 to AC3 were also observed by
the new arm's body, `check_upgrade_steps`, called in process outside the suite: 6 dSP-20 lines `ok`
and 0 failures. With `resolve_recorded_introduced` monkeypatched to the identity, the same body
printed FAIL on 4 of the 6 lines, so the arm can move. The arm's official RED-first observation and
the `govkit selftest` and `govkit refusal join` legs are owed at the close (the spec's `New arm:`
line). AC4 was read off the tree by `git grep`.

**Evidences:** TOOL-dSafePassage-20
- AC1 — `resolve_recorded_introduced` on `"a"*40`, `UNLANDED`, `None` and `"main"` — printed `['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', None, None]`, then `"main"` raised `Refusal`: "`introduced` 'main' is neither a 40-hex commit, the reader's 'unlanded' nor null".
- AC2 — `set_step_state({"schema": 4, "steps": []}, "s1", "unlanded", "applied")` — the row read `{'id': 's1', 'introduced': None, 'state': 'applied'}`; a second call with `"a"*40` left `{'id': 's1', 'introduced': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'state': 'applied'}`.
- AC3 — the arm `[dSP-20 AC3]` over `check_upgrade_steps`' `sp-land` clone (one row landed on `main`, one on the unmerged-into-main branch `feat`) — printed `ok   [dSP-20 AC3] the reader's rows pass through the writer: the landed row its commit, the unlanded one null`; with the mapping removed it printed FAIL naming "`introduced` 'unlanded' is neither a 40-hex commit nor null".
- AC4 — `git grep -n -F '"unlanded"' -- tools/govkit/upgrade_steps.py` — printed the one line `tools/govkit/upgrade_steps.py:84:UNLANDED = "unlanded"`.

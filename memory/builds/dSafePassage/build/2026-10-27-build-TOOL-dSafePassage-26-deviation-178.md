# TOOL-dSafePassage-26 deviation 178 — the lexicon statement AC47 counts sits on line 109 at the base, not 108

**Serves:** deviation TOOL-dSafePassage-26

- **Departs from:** TOOL-dSafePassage-26@rev-11 [§6 AC47]
- **Hand-off:** spec-to-code
- **Before:** AC47 says `python tools/lib/python_floor.py check --rev 3708a705` prints seven statements, `tools/lexicon/selftest.py:108` among them.
- **After:** the query prints seven statements, and the lexicon one is `tools/lexicon/selftest.py:109`; `tools/lib/resolve-python.test.sh` arm 1d asserts the seven and `:109`.
- **Cause:** builder discovery
- **Reason:** S49's case, `no declared Python floor`, is spelled on line 109 of `tools/lexicon/selftest.py` at `3708a705`; line 108 holds the docstring's `3.10+`, which names no `python` word for any alternative of `FLOOR_STATEMENT_RX` to match. The criterion's count and its red case, the count six, hold as written.
- **Evidence:** `git show 3708a705:tools/lexicon/selftest.py | grep -n "no declared"` printed `109:    with no declared Python floor, ...`; the query at `3708a705` printed seven lines ending `tools/settings-merge.py:3`, `tools/lexicon/selftest.py:109` among them (this unit's acceptance ledger, AC47).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-26, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-26

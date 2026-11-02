# TOOL-dSafePassage-53 deviation 1 — the absent class's handler continues the worklist rather than returning

**Serves:** deviation TOOL-dSafePassage-53

- **Departs from:** TOOL-dSafePassage-53@rev-2 [§4]
- **Hand-off:** spec-to-code
- **Before:** §4's handler is written for a recursive `walk(d)` whose `except FileNotFoundError` body is `return`, and AC1 reads that handler's body as one that "returns and raises nothing".
- **After:** `tools/govkit/upgrade_steps.py` walks `modules/` as the worklist TOOL-dSafePassage-51 built, so the handler's body is `continue`: that directory adds no candidate and the walk goes on to the next queued directory, which is what one `walk(d)` returning does. A `return` there would end `read_target_repositories` with the queue unread.
- **Cause:** builder discovery
- **Reason:** the spec's §4 is pseudo-code over a recursion the code at this branch's HEAD does not have; §4's Inventory mints no function, so the listing is not wrapped in one to make its handler literally return.
- **Evidence:** this unit's acceptance ledger, AC1: the `ast` probe printed `[('FileNotFoundError', ['Continue']), ('OSError', ['Raise'])]`, and AC3's `git init` repository returned its one row.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-53, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-51

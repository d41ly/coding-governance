# TOOL-dDeclaredLoop-1 deviation 1173 — the closing review's round-1 record states a fix-first exit and leaves its code cites unpinned

**Serves:** deviation TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117

- **Departs from:** dDeclaredLoop [the closing diff review's round-1 record]
- **Hand-off:** code-to-record
- **Before:** the round-1 record says every item is owed a fix, or a close deviation for the records items, before the close's merge bar and RED-first observations run, and it cites code by bare `path:line` beside its pinned sites.
- **After:** every item the round confirmed is promoted at the closing review's exit under the owner's 2026-10-04 rule `verb_review` quotes, item 1 to `TOOL-dDeclaredLoop-115`, item 2 to `TOOL-dDeclaredLoop-116` and items 3 to 6 batched to `TOOL-dDeclaredLoop-117`; each bare cite reads at the reviewed head bada76713, where the blobs are `help/policy.md@1482cecf`, `tools/loop/upstream.py@43147593`, `tools/loop/loop_lib.py@637ea901`, `tools/loop/adapt.py@1c930e56`, `tools/loop/guard.py@13a73d3e`, `tools/loop/breakpoints.py@790d996d`, `tools/loop/budget.py@ae3163cf`, `tools/memory-tree/build_records.py@e689f3e9`, `tools/loop/loop_parents.py@d078c52c`, `tools/loop/position.py@87072a03`, the unit 100 spec `@96299153` and the unit 99 spec `@c4913160`, so item 2's fourth site is `tools/loop/upstream.py@43147593:297`.
- **Cause:** review finding
- **Reason:** the closing diff review's round 2 confirmed both defects in the round-1 record (its items 1 and 2); a review record is persisted as written and never edited by hand, so this record carries the correction.
- **Evidence:** `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md`, items 1 and 2; the rescope add rows for `TOOL-dDeclaredLoop-115`, `TOOL-dDeclaredLoop-116` and `TOOL-dDeclaredLoop-117` in `memory/builds/dDeclaredLoop/RUN.md`; `tools/unattended/unattended.sh#verb_review`.
- **Risk:** editorial
- **Approver:** author, the builder pass of TOOL-dDeclaredLoop-117, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2

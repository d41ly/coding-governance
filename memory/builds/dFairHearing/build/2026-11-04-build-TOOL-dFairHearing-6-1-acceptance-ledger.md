# Acceptance ledger — TOOL-dFairHearing-6

**Serves:** journal TOOL-dFairHearing-6

Built against spec rev-2 at pass commit `a8546e186`. The main loop drafted this ledger at the close from the builder return and that commit's message. A scratch node runner holding the suite's `runReview`, its stubs and `runGradesArms`, over `tools/workflows/tier2-review.js`, passed 9 and failed 0, and over the parent render it passed 1 and failed 8, the pass being the repeated-id control. No suite, gate or bar ran in the pass: the `New arm:` line on `tools/workflows/tier2-review.test.sh`, with its floor raised from 451 to 460, and the spec's legs are owed to the close, which records the arm's RED and GREEN here under a `Pass: none` commit.

**Evidences:** TOOL-dFairHearing-6
- AC1 — `regraded` — the mixed item read `blockers` 1, `highs` 0 and `regraded` `[]`, and the arm in `runGradesArms` also asserts no log line naming a placement off the binding grade. An id repeated in a second item read `blockers` and `highs` null
- AC2 — `regraded` — id 2 graded `HIGH` read `highs` 1 and `regraded` `[2]`
- AC3 — `WARNING:` — the absent and the illegal grade each read `blockers` 2, with a warning naming `ids 2`
- AC4 — `{severity: 'MEDIUM', ids: [1, 2], grades: {'1': 'BLOCKER', '2': 'MEDIUM'}}` — that item read `blockers` 1, with a `WARNING:` line naming the item holding id 1
- AC5 — `grep -c 'merge findings of one binding grade only'` — it printed 0 over both files, the synthesis prompt carries `one item per defect` and `grades`, and the schema requires `grades`

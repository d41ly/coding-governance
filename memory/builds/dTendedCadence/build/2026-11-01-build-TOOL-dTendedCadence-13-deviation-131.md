# TOOL-dTendedCadence-13 deviation 131 — the recurring security review reads each landed range once, not the whole tree

**Serves:** deviation TOOL-dTendedCadence-13

- **Departs from:** `cl-dClosedLoop-0454@ef9a7f8a`
- **Hand-off:** design-to-spec
- **Before:** the recurring security review, a cadence item running dFairHearing's security lens over the landed tree as `maintain.security-review` says, weekly by default (NP-19)
- **After:** the recurring security review, a cadence item running dFairHearing's security lens over each period's landed range, from the last reviewed head to the landed tip, as `maintain.security-review` says, weekly by default (NP-19)
- **Cause:** design defect
- **Reason:** The clause reads the landed tree, and the lens it names cannot: dFairHearing's security lens runs inside the review harness, whose diff is `base...head` and whose skeptic refutes any defect "present unchanged at the base", so a review reads only what its range introduced. A whole-tree reading from the root commit is a range too, and at this base its diff is 9,736 files, past what a lens reads, so its record would certify a tree it did not read. The spec carries the clause's intent: every change that lands is read by the lens once, the range starting at the head the previous review recorded, so no landed change goes unreviewed after the first base. What it does not read is a defect that predates the first base, which the clause's whole-tree word would have reached. TOOL-dTendedCadence-13 §8 F1 records the options and the test that rejected each.
- **Evidence:** the diff, `tools/workflows/tier2-review.js:1081`; the skeptic's scope line, `:1159`; the pinned base, `:603`; the root-to-tip and one-week diff sizes, `git diff --shortstat` at `7e48dac3` (9,736 files, 2,011,940 insertions; 2,824 files, 318,605 insertions); the gap, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:431`; the new hash, `derive_clause_hash` (`tools/memory-tree/design_lib.py:169`) over the After text, `3bb6c0f8`, which returns `ef9a7f8a` over the Before text
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dTendedCadence's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0454@ef9a7f8a
- **Caused-by:** TOOL-dTendedCadence-13
- **Bound:** the clause's whole-tree reading of the landed tree at each review
- **Tier:** strongest, a bound the carried clause states in its text

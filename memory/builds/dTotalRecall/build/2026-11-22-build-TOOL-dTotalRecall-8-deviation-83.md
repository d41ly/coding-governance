# TOOL-dTotalRecall-8 deviation 83 — the code record loses its own re-timing and is not built

**Serves:** deviation TOOL-dTotalRecall-8

- **Departs from:** `cl-dClosedLoop-0219@927a3172`
- **Hand-off:** spec-to-code
- **Before:** the clause's core `code` record, re-timed as TOOL-dTotalRecall-8's first act, a cold derivation over 30 s or a record over 1 MB on either tree losing (the clause's own thresholds, `TOOL-dTotalRecall-8@rev-6` AC1).
- **After:** the record is not built: `python tools/playbook/code_record.py --time --tree b4137f4897595a1911ce59a73ce88b8a61785f6c` printed `seconds 10.80` and `bytes 10884519` (DERIVED, the builder's cold run at the pass base), about ten times the 1 MB line, so the unit is retired `WONTDO` by M2's AMEND as §8 F1 resolved, and its readers keep `git grep`.
- **Cause:** builder discovery
- **Reason:** the losing test the clause itself designs (§8 F1's loss route): no rendering of the record fits, since its smallest faithful parts each come near or over the line on their own (the builder's measurements in `2026-11-22-build-TOOL-dTotalRecall-8-1-builder-return`), and re-scoping AC1's line is the clause's to change, not this run's.
- **Evidence:** `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-8-1-builder-return.md`; the draft core kept as a patch beside the session; TOOL-dTotalRecall-8 §8 F1 and AC1.
- **Risk:** loosening
- **Approver:** author, the main loop following the spec's own RESOLVED loss route under the build's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0219@927a3172
- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-8-deviation-81
- **Caused-by:** TOOL-dTotalRecall-8

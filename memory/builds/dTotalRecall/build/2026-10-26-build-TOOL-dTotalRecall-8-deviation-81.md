# TOOL-dTotalRecall-8 deviation 81 — the code record's cold derivation re-timed at its own unit's first act, not at the build's first unit

**Serves:** deviation TOOL-dTotalRecall-8

- **Departs from:** `cl-dClosedLoop-0219@927a3172`
- **Hand-off:** design-to-spec
- **Before:** the clause, and v2's `[owed]` line 2033, re-time the `code` record's cold derivation "at this build's first unit", on gov's tree and on a planted adopter-scale fixture, a cold derivation over 30 s or a record over 1 MB on either losing.
- **After:** the re-timing is TOOL-dTotalRecall-8's first acceptance criterion, observed before any other code of that unit, at build order 3, after TOOL-dTotalRecall-1 (the registry the `code` kind lands its row in) and TOOL-dTotalRecall-13 (the extraction primitive the derivation runs through); the losing lines and both trees are unchanged.
- **Cause:** design defect
- **Reason:** the derivation the clause times runs through unit 13's primitive and registers in unit 1's registry, so at the build's first unit it does not exist; timing it there would mean building a throwaway derivation, which BUILD-METHOD M3 forbids a probe to do. The two units before it build no code-record code, so no losing record can be built before its re-timing, which is what "a losing record is never built" protects.
- **Evidence:** the spec brief's D1 (`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md`, "HEAD and the design differ"); TOOL-dTotalRecall-8 §2 S1, §6 AC1 and §8 F1; v2:2033.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of this spec run's writer group 1, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0219@927a3172
- **Caused-by:** PLAY-dClosedLoop-2

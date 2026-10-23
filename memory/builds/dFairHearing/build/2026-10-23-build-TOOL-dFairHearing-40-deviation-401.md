# TOOL-dFairHearing-40 deviation 401 — the round-5 spec audit promoted one batch unit for its 35 minors

**Serves:** deviation TOOL-dFairHearing-40

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-37`, the round-4 spec audit's promotions `TOOL-dFairHearing-33` to `TOOL-dFairHearing-37` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-40`, ordered at 26 after `TOOL-dFairHearing-38` and `TOOL-dFairHearing-39` at 25, the build's last order: one batch unit whose 35 §2 items close the round-5 minors on units 33 to 37, among them one build-wide version reading on `base.py`'s base at the build's last pass commit, an attempt checker that refuses a row it cannot place and counts a `failed` call as a void attempt, a void column re-derived from the record's evidence, and criteria a correct build can pass.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a MEDIUM or LOW to a unit whose mechanism closes it. This unit closes every MEDIUM and LOW of the round-5 spec audit, batched: MEDIUM ids 2, 3, 4, 12, 13, 14, 15, 18, 20, 21, 22, 25, 26, 27, 28, 31, 33, 35 and 38 (items M1 to M13) and LOW ids 5, 6, 7, 8, 9, 10, 16, 17, 23, 24, 29, 30, 34, 36, 37 and 39 (items L1 to L15). They are one unit because the build-wide version reading (id 2, item M1) reads every kit's version carrier and the quoting fix (id 36, item L13) writes one of them, `tools/workflows/tier2-review.template.js`, so no split clears M6 while the reading runs last. This is a spec run, so the unit is specced and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition). No audit names it: the owner stopped the spec-audit chain after round 5 (`memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`), so round 5's promotions close under a recorded override of `specs-audited` citing that record.
- **Evidence:** the round-5 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-40` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-40.md`; the owner's record, `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-40
- **Caused-by:** PLAY-dClosedLoop-2

# TOOL-dFairHearing-34 deviation 341 — the round-4 spec audit promoted a unit for the marker half of its high H1

**Serves:** deviation TOOL-dFairHearing-34

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-32`, the round-3 spec audit's promotions `TOOL-dFairHearing-28` to `TOOL-dFairHearing-32` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-34`, ordered at 23 after `TOOL-dFairHearing-31` at 22: every `gov:kit` marker in every file the build modified, read at the build's base and at `HEAD` and paired by kit, exiting 1 on a moved marker number and 2 on a refusal, with no typed directory list.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes the marker half of one confirmed high of the round-4 spec audit, item H1 (finding id 31, merged with id 22, whose constant half is `TOOL-dFairHearing-33`'s). Unit 31's probe diffs only `tools/hooks`, `tools/roles`, `.claude/skills/build` and `tools/workflows`, while unit 27 S15's rule covers every commit of the build. So a hand bump of the marker at `tools/check-wiring.sh:51` or `tools/memory-tree/HYGIENE.template.md:1`, both files the build edits, exits 0. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-4 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-34` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-34.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-34
- **Caused-by:** PLAY-dClosedLoop-2

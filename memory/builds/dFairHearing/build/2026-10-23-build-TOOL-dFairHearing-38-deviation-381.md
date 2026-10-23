# TOOL-dFairHearing-38 deviation 381 — the round-5 spec audit promoted a unit for the criterion half of its high H1

**Serves:** deviation TOOL-dFairHearing-38

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-37`, the round-4 spec audit's promotions `TOOL-dFairHearing-33` to `TOOL-dFairHearing-37` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-38`, ordered at 25 after `TOOL-dFairHearing-36` and `TOOL-dFairHearing-37` at 24: the `selected` half of unit 37 AC4 observed by unit 32 AC8's byte-identical comparison, re-run once over a staged copy of `gotchas.py` that ships the flag, and by a read of `main`'s `--for-diff` branch holding no `all-ungated` token, with no change to `gotchas.py`'s parser.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes the criterion half of one confirmed high of the round-5 spec audit, item H1 (finding id 1, merged with id 11, whose bug-class half is `TOOL-dFairHearing-39`'s). Unit 37 S4 and AC4 expect `gotchas.py --for-diff <range> --all-ungated` to exit 2 with argparse's `unrecognized arguments` on a `selected` verdict, but `gotchas.py` reads its arguments by hand: `main`'s `--for-diff` branch at `tools/memory-tree/gotchas.py:1335-1339` returns `cmd_for_diff(root, conf, argv[2])` and never reads `argv[3:]`, so the call exits 0 and AC4 cannot pass on a correct build. This is a spec run, so the unit is specced and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition). No audit names it: the owner stopped the spec-audit chain after round 5 (`memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`), so round 5's promotions close under a recorded override of `specs-audited` citing that record.
- **Evidence:** the round-5 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-38` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-38.md`; the owner's record, `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-38
- **Caused-by:** PLAY-dClosedLoop-2

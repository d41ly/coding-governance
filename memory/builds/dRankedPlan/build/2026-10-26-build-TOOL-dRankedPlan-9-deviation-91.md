# TOOL-dRankedPlan-9 deviation 91 — the intake log read from dPlacedRequest's typed request record until the hook lands, its stand-in named on the witness

**Serves:** deviation TOOL-dRankedPlan-9

- **Departs from:** `cl-dClosedLoop-0377@fd363a7f`
- **Hand-off:** design-to-spec
- **Before:** the session's intake log, which `entry.intake`'s prompt-submit hook writes (dWellOiledMachine's, PM-9), its owner-origin intake alone read as the request's ratification by `plan.ratification`
- **After:** the session's intake log, which `entry.intake`'s prompt-submit hook writes once dWellOiledMachine lands it and which until then is dPlacedRequest's request record and its `.typed` line, its owner-origin intake alone read as the request's ratification by `plan.ratification`, every witness read from the stand-in marked `log stand-in` in place of a `[[stand-in]]` row
- **Cause:** external
- **Reason:** No prompt-submit hook exists at base and dWellOiledMachine, which owns it, has no spec, so the predicate reads the one record of an owner's typed request that a parent of this build ships, TOOL-dPlacedRequest-19's, through its consent verb. That record is written by `--request` on its caller's word, so until the hook lands an agent in the typing session could record words the owner never typed, which is looser than a hook-written log. The brief's shared interface I7 asked for a `[[stand-in]]` row; TOOL-dDeclaredLoop-13 S8 reds a stand-in row naming no row item, and `item.entry.intake` has no `[[item]]` row and is in no move row of its table, so the stand-in is named by `INTAKE_STAND_IN` in `ratify.py` and the mark on each witness (TOOL-dRankedPlan-9 §8 F1, F3).
- **Evidence:** the clause, `memory/builds/dRankedPlan/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:29`; the stand-in's limit, `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md:72-74`; the stand-in row rule, `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-13.md:62-65` and its move rows at :136-155; no `UserPromptSubmit` in `.claude/settings.json` at `0689e7fa1`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dRankedPlan's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0377@fd363a7f
- **Caused-by:** TOOL-dRankedPlan-9

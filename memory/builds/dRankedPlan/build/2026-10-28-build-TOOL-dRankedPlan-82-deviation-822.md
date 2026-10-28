# TOOL-dRankedPlan-82 deviation 822 — TOOL-dRankedPlan-82's spec revised when its builder's role could not take the reading

**Serves:** deviation TOOL-dRankedPlan-82

- **Departs from:** `TOOL-dRankedPlan-82@rev-1`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dRankedPlan-82`'s spec as the revision at `TOOL-dRankedPlan-82@rev-1` reads it, in which the builder takes the reading R of the spec tokens leg alone and observes `derive-ceilings.py --check` red and green.
- **After:** at 01b547386, rev-2: R is the main loop's reading, 411.0 s, stated in the spec with its census, C is 830, AC1 and AC2 are observed by the main loop, AC3 and AC4 stay the builder's, and the header carries no build-order verb.
- **Cause:** builder discovery
- **Reason:** the builder dispatched at cc8880ae6 stopped without a commit because the role gate of `tools/hooks/scratch-guard.js` refuses both gate legs to `gov-builder`, whose allowlist in `.claude/roles.json` names only `lexicon naming predicates`. The revision moves who takes the reading and who observes the two legs; what the unit builds, one leg's ceiling and its evidence row, is unchanged.
- **Evidence:** the revision brief, `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-82-revision-brief.md`; the spec changed at 01b547386, past rev-1 (3820e5465).
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-112
- **Caused-by:** PLAY-dClosedLoop-2

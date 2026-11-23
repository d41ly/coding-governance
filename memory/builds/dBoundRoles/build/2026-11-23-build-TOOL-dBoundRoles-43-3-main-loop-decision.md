**Serves:** journal TOOL-dBoundRoles-43

# TOOL-dBoundRoles-43 — the main loop's decision on the builder's divergence of round one

The builder of round one (`wf_8b782681-749`) read the spec at rev-8 against the tree at `4fef02b6c`, wrote nothing,
and handed back one design question and four stale claims. The main loop read the question against source:
`tools/playbook/overlay.py#main` takes `check` and `--fixture` only, so the write verb §8 F17 waits on does not
exist, and the ask F17 says this run files in dOrderedCharter's backlog was never filed (DERIVED:
`git grep "verb writing rows through" -- memory` finds this spec alone). Each answer below is the option no worse
than the others on any principle (P18), decided rather than parked. Each binds over the spec as the owner's ruling
`2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling` does, and the builder records each departure in its deviation
record.

1. **S10, S23, AC10 and AC23 wait on the ask, as the owner ruled.** F17 is the owner's ruling of 2026-11-05: option
   (a), the verb asked of dOrderedCharter, with S10, S23 and AC23 waiting on it. Option (b), this unit adding the
   verb, was ruled out there. Option (c), the resolver import three landed step programs use
   (`tools/govkit/steps/kickoff_facts_to_overlay.py#load_overlay` among them), changes the owner's pick, which
   the main loop does not do on its own. The run files the ask now as `PLAY-dOrderedCharter-89` in
   `memory/builds/dOrderedCharter/BACKLOG.md`, with F17's own words. The pass builds every other item and answers
   AC10 and AC23 DEFERRED in its ledger, naming that ask. No other unit of this build consumes S10 or S23 (DERIVED:
   the `consumes-from` edges naming TOOL-dBoundRoles-43 sit in units 50, 58 and 64, on other items), so nothing
   else waits. The close surfaces the ask with the parked decisions, beside the resolver import the builder found,
   for the owner to weigh.
2. **The stale claims are mechanical.** These do not hold at the base, and each is recorded in the deviation record:
   - S19's "none in `scratch-guard.js`": the file holds the same receipt comment, and AC19 still holds.
   - S22's alias line: it is already gone.
   - S9: it already holds.
   - S32's eight readers: three remain.

widens: none · relaxes: S10, S23, AC10 and AC23 of this unit, deferred against PLAY-dOrderedCharter-89 as §8 F17
rules.

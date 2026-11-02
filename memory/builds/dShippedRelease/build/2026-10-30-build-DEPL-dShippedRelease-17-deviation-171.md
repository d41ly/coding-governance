# DEPL-dShippedRelease-17 deviation 171 — "one pass" on an empty repository ends at declared stops, since three values only the owner holds cannot be defaulted

**Serves:** deviation DEPL-dShippedRelease-17

- **Departs from:** `cl-dClosedLoop-0427@131c1447` [fresh install]
- **Hand-off:** design-to-spec
- **Before:** a fresh install of every kit in one pass, the kits' adopters ordered by their declared dependencies and seen on an empty repository
- **After:** the install and update hooks that call `adopt` and `test.seed`, attended, run by the owner items `kits.install-attended` and `kits.update-attended` beside the commands `kits.install` and `kits.update`, which walk the steps and close on dSafePassage's outcomes, each outcome seen on its planted walk (the owner's FK-5-1), and the shards-to-builds backlog migration as an update's upgrade step, run attended until no tree is left on shards (NP-22), and a fresh install of every kit in one process, the kits' adopters ordered by their declared dependencies, each ending at a declared outcome, a stop that waited only on a gov default continued in the run and a stop waiting on a value only the owner holds listed on one attended order, seen on an empty repository
- **Cause:** design defect
- **Reason:** The clause and `gap-deploy-27` read the gap as ordering, and two empty repositories measured it is not: `memory/` comes from the kickoff seed at LAND, before any adopter, and `process-monitor`, `playbook-render` and `unattended` stop for values an empty repository does not hold, `PROCMON_ROOTS`, a CI file and a project layer. Every option fails a bound (DEPL-dShippedRelease-17 §8 F1), so the fork rule's rung 6 relaxes one bound and M3 runs again. Inventing a default for those values reads a clean tree over a fence that matches nothing, so the bound relaxed is the strict reading of "every kit": every kit lands, its adopter ends at a declared outcome, the run needs no second invocation, and what the owner must still answer is one order rather than a problem count. Also follows through as: usage kits.install.
- **Evidence:** scout D disagreement 5, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md:134`; the refusal, `tools/process-monitor/adopt-process-monitor.sh:120-121`; rung 6, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:924`; DEPL-dShippedRelease-17 §8 F1
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, citing ER:328, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0427@131c1447
- **Caused-by:** DEPL-dShippedRelease-17
- **Bound:** every kit's adopter finishing with no owner's value on an empty repository
- **Tier:** strongest, a bound the carried clause states in its text

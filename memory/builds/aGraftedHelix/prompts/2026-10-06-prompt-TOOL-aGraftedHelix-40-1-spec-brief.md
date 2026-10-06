**Serves:** journal TOOL-aGraftedHelix-40..41

# Spec brief — TOOL-aGraftedHelix-40 and -41, adopted at VERIFYING

Tier-2, streams tooling. Spec `order` values: 40 is 24, 41 is 25. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states the twelve invariants that bind
both units. In your OWN return, name the specs you author in `authored` by their unit ids, never by
their paths.

The observation behind both units comes from the pooled sweep of the unattended suites at
`b04ab0da0`. Every unit of 39 was terminal at the time, and the sweep ran on a frozen clone. The
runner's own summary is the evidence: `sweep RED — 20 suite(s) ran concurrently; killed 0 · walled
1 · unrun 0 · unstarted 0 · mismatched 15`. Seventeen rows ran to their end with rc 0 and 0 FAIL; of
those, every MISMATCH is an executed count above a stale baseline. The remaining three rows are
these two units.

The per-row durations, as start offset and run time in seconds:
- driver selftest: started +0 and was killed by the run wall at 19871, with no verdict;
- gate shards 1 to 8: between 4724 and 7391 each, all finished by +10210;
- every other row: under 1200.

So for 2 h 40 m the pool ran one suite with seven lanes idle. Effective parallelism was about 3.7 of
8 lanes: 72,700+ s of suite time in 19,600 s of wall. Each suite ran 3 to 8 times slower than its
last serial measurement in `tools/run-gates/selftest-budgets.txt`. Those measurements date from
September, before this build grew the suites.

## TOOL-aGraftedHelix-40 — the two red arms

1. **playbook selftest**, `tools/unattended/check-playbook.test.sh`, BLOCKER 3's loop:
   `FAIL a legal shell spelling of BYPASS_BAN resolves to something no record can contain, and the
   leg says nothing: BYPASS_BAN="--no-verify"   # the flag the lander bans`. Read as shell, that
   value is `--no-verify` with a trailing comment. The arm was green in the pooled calibrate at
   `eb96ea8b2`, and since then only units 38 and 39 moved the kit. Reproduce it by slice on HEAD
   first. Find which reader of `BYPASS_BAN` now resolves the commented spelling differently from
   the shell that sources the conf, and fix it at that reader. Under
   `two-readers-of-one-config-one-re-derived`, check every other reader of the same key.
2. **resume-tick selftest**, `tools/unattended/resume-tick.test.sh`:
   `FAIL AC1 the tick returned well inside the 60 s launch, so it is detached: expected [yes], got
   [no: 21s]`. That is an elapsed-time threshold graded under an eight-wide pool. Decide by a slice
   run alone, and by one under induced load, whether the tick is still detached. If it is, the arm
   measures the node and not the detachment: replace the clock with a signal the detachment itself
   produces (`fixed-sleep-does-not-place-a-signal`). If it is not, fix the tick.

## TOOL-aGraftedHelix-41 — the driver suite's place in the sweep

The driver suite (`tools/unattended/unattended.test.sh`) already accepts `--shard <i>/<n>` at
`SHARD_ARITY=2`. The sweep registers it as ONE row, and that row now sets the sweep's floor alone.
Register it in the sweep as shards, the way the gate suite is registered. Size the arity from the
suite's own region costs: make the longest driver shard no longer than the longest gate shard, and
justify the number from measurement. Keep every invariant the shard mechanism already asserts:
- the floors per shard;
- the identity that the shards' counts sum to the unsharded count;
- a mis-cut shard fails rather than passing empty.

Re-declare the driver rows' serial budgets from fresh measurements on node a, each dated and
attributed in the budgets file's own grammar. Say whether `--serial` and the bar's own legs still run
the suite whole, and keep whichever runs it whole doing so if anything depends on that.

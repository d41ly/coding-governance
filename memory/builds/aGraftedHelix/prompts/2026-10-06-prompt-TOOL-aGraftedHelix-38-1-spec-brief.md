**Serves:** journal TOOL-aGraftedHelix-38

# Spec brief — TOOL-aGraftedHelix-38, adopted at VERIFYING

Tier-2, streams tooling, `order 22`. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states the twelve invariants that bind it.
In your OWN return, name the spec you author in `authored` by its unit id, `TOOL-aGraftedHelix-38`,
never by its path.

## What was observed

At VERIFYING, the owed unattended suites ran once as a pooled calibrate on a frozen clone at
`eb96ea8b2`, every unit of 37 terminal. 11 of 20 rows went red. The outputs are in that clone's
`.git/gate-logs/selftests/*.out`; the main loop will hand you the path. Three defects account for
every red arm read so far, and all three came in with this build's own units 32 to 36:

1. **Check 51 reds the real tree.** `bash tools/unattended/check-unattended.sh` at `eb96ea8b2`
   exits 1 with `tools/unattended/unattended.sh:6138 run_settle() writes a terminal phase and never
   calls write_claim`. Unit 31 built check 51 to read a `write_claim` call inside the same function
   as the terminal-phase write. Unit 36 then moved `--settle`'s claim write into a helper,
   `write_settle_claim`, which `run_settle` calls. The predicate does not follow the call. It is a
   merge-bar leg, so the bar reds. Every fixture that copies the real driver reds with it, which is
   most of the eight gate shards and the cross-component suite (arms 3, 3b and 5 and its fixture
   precondition).
2. **A parking function without a bypass-flag guard.** The driver selftest reds on one arm:
   `a function parks an entry with no bypass-flag guard anywhere in it: write_preflight_record()`.
   Unit 32 split `write_preflight_record` out of `verb_preflight`; the guard stayed behind in the
   caller.
3. **The arms-groups checker refuses the tracked suite.** Its selftest reds on 16 arms, starting
   with `T0 the tracked suite parsed into no groups: '0'`, `T0 no in_shard seam was counted: '0'`
   and `T0 the tracked run exited 2 — a refusal over the real suite`. Every AC1 to AC3 arm follows
   from that. The checker's parse of the gate suite no longer finds the structure it reads. Unit 34
   re-cut region 8 of that suite and hoisted 31 helpers; unit 36 added `read_topo` calls at the nine
   seams. One of them moved what the parser anchors on.

## What to decide

Fix each at its root, and give each a left-shift.

- **Check 51.** Decide how the predicate recognises a claim write it does not see inline: one level
  of call into a function that itself calls `write_claim`, the transitive closure over the file, or
  a declared helper list. Choose the one that cannot pass a terminal writer that writes no claim.
  Observe it red on a function that calls a helper that writes no claim.
- **The parking guard.** Decide whether `write_preflight_record` carries the guard, or the class
  rule follows the call the same way check 51 now must. If both checks share the question "does
  this function, or what it calls, do X", answer it ONCE, under the class
  `two-guards-one-question-two-answers`.
- **Arms-groups.** Find what the parser anchors on and what moved it. Fix the parser if the suite's
  new shape is legitimate; fix the suite if the parser's anchor was the contract. Observe the T0 arms
  green over the real tracked suite, and red under the break.

Before declaring the unit done, read EVERY failing arm in the clone's outputs, not only the ones
quoted here. Check each one against these three causes by slice. Any arm that none of them explains
joins this unit.

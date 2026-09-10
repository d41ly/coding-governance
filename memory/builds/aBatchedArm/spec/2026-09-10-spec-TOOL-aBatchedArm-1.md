# TOOL-aBatchedArm-1 — batch the gate self-test's arms by tree state

**Status:** OPEN · rev-1 · 2026-09-10 · node a · Tier-2 · base e9ed269b · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-prompt-TOOL-aBatchedArm-1.md](../prompts/2026-09-10-prompt-TOOL-aBatchedArm-1.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/check-unattended.test.sh` spends 293 full-program invocations to make 377
assertions, and 83 % of those invocations feed at most one of them. Group arms whose breaks do not
interfere onto ONE tree and ONE invocation, so the suite reaches its verdict in under 20 minutes
without deleting an assertion.

## 2. Scope (IN)

- **S1** — add one assertion helper, `emitted <check-numbers> <output>`, which grades the SET of
  check numbers a captured run emitted against the set the batch expects. Observed by **AC1** and
  **AC2**.
- **S2** — convert the batchable arms from one-reset-one-run-one-assertion into groups: one
  `reset_tree`, the group's mutations applied in sequence, one `out=$(run)`, one `emitted` call, then
  the group's existing `hit`/`miss`/`same` assertions against `$out` VERBATIM. Observed by **AC3**.
- **S3** — leave un-batched, each on its own tree, every arm whose break can truncate or relocate the
  run: the three check-1 branches that `exit` at `check-unattended.sh:114`, `:198` and `:385`; every
  arm asserting on exit code alone; every arm asserting the output is EMPTY; and the anchor,
  PATH-stub and remote-rewriting arms. Observed by **AC4**.
- **S4** — re-measure and re-declare `FLOOR_ASSERTIONS` and both per-shard floors against the
  converted suite, with the reading beside each number. Observed by **AC5**.
- **S5** — record the new wall-clock reading for both shards on a frozen clone, and update the row in
  `tools/run-gates/selftest-budgets.txt` with the reading it was taken from. Observed by **AC6**.

## 3. Non-goals (OUT)

- **Porting to `tools/lib/lib-selftest.sh`.** Closed by `TOOL-aPooledSweep-3`: that harness takes one
  POSITIVE substring and this suite asserts 101 negatives and 27 equalities. Re-opening it starts
  with the vocabulary `TOOL-aPooledSweep-7` enumerates, and that is a different build.
- **A declarative arm table with a partition solver and recorded goldens.** Rejected in §4 on the
  measurement: the helper reaches the same target with a local, mechanical edit per group and leaves
  every assertion byte-identical, which is what keeps the equivalence proof available.
- **Cutting spawns further.** `TOOL-aTracedSpawn-2` bounds it at roughly 2 s per invocation of real
  non-spawn work.
- **Raising `SHARD_ARITY` above 2.** A live owner ruling of 2026-08-29 permits it, and it is not
  needed once the invocation count falls; named as the follow-up if AC6 misses.
- **Repairing the suite's pre-existing RED.** `TOOL-aQuenchedHarness-9` and `TOOL-aHoistedPass-38`
  own those. This unit must not change any arm's verdict, red ones included.

### Edges

- **consumes-from** `none`
- **hands-off** `none`

## 4. Design

### Data model

A batch is a contiguous run of arms in the existing file, delimited as today by `reset_tree`. The
only new state is the expected check-number set, written as the helper's first argument.

```
reset_tree; mutA; mutB; mutC
out=$(run)
emitted "4 10 14" "$out"
hit  "$out" "<A's own failure text>"
hit  "$out" "<B's own failure text>"
miss "$out" "<C's near-miss text>"
```

`emitted` extracts `^UNATTENDED check ([0-9]+)`, sorts unique, and compares to its argument. It
increments the assertion counter like every other helper.

### Why the set and not a count

A count catches truncation and misses collateral. The eight-break probe of 2026-09-10 staged eight
breaks and emitted four checks, because one break tripped check 1 whose branch `exit`s — a count
would have caught that. It would NOT catch a break that additionally fires an unrelated check, which
is the failure mode that makes a batched arm pass for the wrong reason. The set catches both
directions, and it is cheap because all 178 branch signatures are unique and each belongs to exactly
one numbered check (verified 2026-09-10 with `check-arms.py`'s own normaliser: 0 collisions).

**What `emitted` does NOT check:** that a given check fired for the reason its arm intended. Two
branches under ONE check number are indistinguishable to it, which is why the per-branch `hit` lines
stay exactly as they are and this helper is added beside them rather than replacing them.

### Alternatives rejected

**A declarative arm table plus an offline partition solver and recorded golden sets.** This was the
author's own earlier recommendation. Rejected because it rewrites 377 assertions to reach a target a
one-helper edit reaches, and a rewritten assertion is what made `TOOL-aPooledSweep-3` close the port:
the equivalence proof is a per-assertion diff, and only an edit that leaves the assertion text
untouched keeps that proof available. The solver also has to be re-run whenever the checker changes;
the helper's expected set is re-derived by reading the failing output, which costs one run.

**A tree-state memo on `run()`.** Measured against the file rather than argued: 293 invocations visit
262 distinct states, so memoising repeats buys about 10 % and does not approach the target.

### Rollout

The conversion is mechanical and per-group, so it lands in tranches on the run's branch, each tranche
verified by the equivalence diff before the next begins. A tranche that changes any arm's verdict is
reverted rather than argued with.

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh`, `tools/run-gates/selftest-budgets.txt`, and this build's
records.

## 5. Production-readiness checklist

- security — N/A. The suite grades a checker against a scratch fixture; batching changes scheduling,
  not what any arm asserts.
- perf / scale — the whole unit. The figure is the suite's wall clock on a frozen clone.
- error / empty / loading states — an `emitted` call whose argument is malformed REFUSES by name
  rather than grading nothing; the empty-output arms stay unbatched by S3.
- observability — a failing `emitted` prints the expected set and the observed set, so the remedy is
  readable from the failure rather than by re-running arms singly.
- risks — the batching premise is false where callers short-circuit (`TOOL-aDrainedSluice-5` N17,
  reproduced here 2026-09-10). S3 is the mitigation and AC4 is its observation.
- testing — the equivalence diff of AC3 is the safety property; it must be observed non-empty on a
  deliberately mis-grouped tranche before it is trusted.
- migration — none. Reverting is restoring the file.
- user docs — N/A. The suite is developer-facing and its header carries the batching contract.

## 6. Acceptance criteria

- **AC1** — When a batch's tree fires exactly the checks its `emitted` call names, the helper passes
  and increments the assertion counter by one.
  Red when: the helper is silent on a mismatch, which is the green-by-absence shape this suite exists
  to refuse.
- **AC2** — When a break is added to a batch WITHOUT updating its `emitted` argument, the suite reds
  and the failure names both the expected and the observed set. Staged and observed before this unit
  lands, per `AGENTS.md` §7.
  Red when: the run passes, or the message names only one side of the comparison.
- **AC3** — When `check-unattended.test.sh` runs at both shard indices before and after the
  conversion, the per-assertion verdict inventory is IDENTICAL, red arms included.
  `cost:` two full shard pairs on a frozen clone, roughly 80 minutes each side.
  `figure:` DERIVED at observation time from the two logs, never pinned here.
  Red when: any arm's verdict flips in either direction, including a red arm that turns green.
- **AC4** — When the three check-1 `exit` branches, the exit-code arms and the empty-output arms are
  each staged, each reds on its OWN tree and none shares a batch with another arm.
  `fixture:` the suite's own scratch repo; no new fixture is needed.
  Red when: any of them is found inside a group, which the conversion's own review must catch.
- **AC5** — When the converted suite runs unsharded and at each shard index, the executed assertion
  count meets the re-declared `FLOOR_ASSERTIONS` and per-shard floors, and each number carries the
  reading it was set against.
  Red when: a floor is carried across from the unconverted suite, which is a number and not a floor.
- **AC6** — When both shards of the converted suite run on a frozen clone on an idle box, the LONGER
  shard completes in under 20 minutes, measured with `date +%s` around each and recorded.
  `figure:` DERIVED from that run and written into `tools/run-gates/selftest-budgets.txt`.
  Red when: the longer shard exceeds 20 minutes, which sends the unit to the `SHARD_ARITY` follow-up
  named in §3 rather than to a lowered target.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `testsuite counts self-test` · `line-length gate selftest`

New arm: `tools/unattended/check-unattended.test.sh` · a batch whose `emitted` argument omits a check
its tree fires, staged and observed RED then unstaged · floor to move: `FLOOR_ASSERTIONS`,
`FLOOR_SHARD_1`, `FLOOR_SHARD_2`, all three re-measured under S4.

## 8. Open questions

- **F1 · How many arms fit a batch before interference dominates?** Measured input: 237 of 298
  reset-delimited blocks carry no anchor, PATH-stub or env special, so 80 % are candidates. The group
  size is not a constant to pick — it is whatever `emitted` accepts without a mismatch, found by
  widening a group until it reds and stepping back one. RESOLVED (agent, 2026-09-10, delegated):
  widen empirically per group; no global size is declared, and the measured distribution goes in the
  build record rather than into this spec as a pinned figure.
- **F2 · Does the conversion need the pre-existing RED repaired first?** No, and the reason is the
  equivalence property: AC3 compares verdicts per arm, so a stable red is as good an oracle as a
  green. RESOLVED (agent, 2026-09-10, delegated): proceed against the red baseline, and record the
  baseline inventory as the artifact AC3 diffs against.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft. Records the reversal of this author's own earlier
  recommendation: a declarative arm table with a partition solver was proposed to the owner before
  `TOOL-aPooledSweep-3` and `TOOL-aTracedSpawn-2` had been read, and §4 rejects it on those readings.

## 10. Reuse audit

- **The seam is the suite's own assertion-helper block**, `tools/unattended/check-unattended.test.sh`
  lines 57 to 59, where `hit`, `miss` and `same` already share one counter and one failure idiom;
  `emitted` is a fourth helper in that block and not a new mechanism beside it. The sibling
  `tools/unattended/check-pass-order.test.sh:29-31` carries the same three helpers in a fork-free
  `case` spelling, which is the shape to copy if `emitted` is ever made fork-free too. Verified at
  source rather than cited: the reuse probe reports `unscanned layers: .sh` and can see no shell
  seam at all, so a "no seam fits" resting on it alone would have been unfounded.
- **The retrieval arguments, verbatim:**
  `python tools/codebase-map/reuse_lookup.py "batch staged breaks into one fixture and assert the emitted failure set"`
  and
  `python tools/memory-recall/query.py "why do the kit self-test suites re-run the whole program once per arm instead of batching, and what was decided about porting them to a pooled harness" --terms "selftest arm fixture batching pooled harness invocation spawn shard budget port reset_tree assertion floor"`.
  The second is what surfaced `TOOL-aPooledSweep-3`, `TOOL-aPooledSweep-7`, `TOOL-aTracedSpawn-2` and
  `TOOL-aDrainedSluice-5` N17, none of which the first could reach.

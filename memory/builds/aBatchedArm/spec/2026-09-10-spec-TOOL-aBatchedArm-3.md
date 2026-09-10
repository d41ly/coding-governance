# TOOL-aBatchedArm-3 — grade the gate self-test as eight declared shards

**Status:** OPEN · rev-1 · 2026-09-10 · node a · Tier-2 · base e9ed269b · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`unattended gate selftest` is the costliest row in the declared self-test population and the member
the pooled runner's wall clock cannot fall below. Its 293 invocations are already independent by
construction — the suite resets the tree before nearly every arm. Split them across eight declared
rows the runner's pool executes concurrently, so the suite's verdict arrives in under 20 minutes with
no assertion changed and no new oracle.

## 2. Scope (IN)

- **S1** — raise `SHARD_ARITY` from 2 to 8 in `tools/unattended/check-unattended.test.sh` and re-cut
  the two `in_shard` regions into eight, balanced by invocation count rather than by line count.
  Observed by **AC1**.
- **S2** — replace the single unsharded row in `tools/run-gates/selftest-budgets.txt` with eight
  rows, one per shard, each carrying its own measured budget. **Without this the arity raise buys
  NOTHING**, and that is the unit's central fact rather than a caveat. Observed by **AC3** and
  **AC4**.
- **S3** — declare eight per-shard assertion floors and re-measure `FLOOR_ASSERTIONS`, each number
  carrying the reading it was set against. Observed by **AC2**.
- **S4** — a shard-join assertion, so eight green shards constitute a whole-suite claim rather than
  eight claims about eight regions. Observed by **AC5**.

## 3. Non-goals (OUT)

- **Batching arms.** That is `TOOL-aBatchedArm-1`, which round 2 measured at 40 to 44 minutes on its
  own. It composes with this unit and does not substitute for it.
- **The group linter.** `TOOL-aBatchedArm-2`, and it grades the batching this unit does not do.
- **Repairing the suite's pre-existing RED.** `TOOL-aQuenchedHarness-9` and `TOOL-aHoistedPass-38`
  own those; 12 failures in shard 1 and 23 in shard 2 at BASE, measured 2026-09-10. This unit must
  not change any arm's verdict.
- **Sharding the sibling driver suite.** `TOOL-aTracedSpawn-1` records that it cannot even run
  unsharded (a bare `$1` in a double-quoted `case` under `set -u`); that is its own row.

### Edges

- **consumes-from** `none`
- **hands-off** `TOOL-aBatchedArm-1` — the conversion, which lands on top of this split and whose AC6
  grades the pair.

## 4. Design

### Why the arity constant is not the unit

Nothing in this tree invokes the suite with `--shard`. `tools/run-gates/selftest-budgets.txt:114`
declares its argv as `bash tools/unattended/check-unattended.test.sh` with no flag;
`tools/run-gates/run-selftests.sh` contains ZERO occurrences of the string `shard`; and
`tools/unattended/run-unattended-gates.sh:157` states the suites are run unsharded **on purpose**,
because the whole-suite claim exists only in a run with no `--shard` argument. So raising
`SHARD_ARITY` alone changes a constant nothing reads, and the 9067 s reading stays an unsharded
reading. The unit is the DECLARATION split; the constant is one line of it.

### Why the split is safe, measured rather than assumed

The suite's arms are already independent: 299 `reset_tree` calls across 298 blocks, so nearly every
arm starts from the pristine fixture. The residual risk is shell state crossing a region boundary,
and it was measured at BASE: **zero** variables are assigned only inside one `in_shard` region and
read in another. The helpers that do cross — `anchor_break` and `anchor_restore` — are already
hoisted into the prologue, which the file's own shard contract calls its HOIST SET.

The two regions today carry 106 and 187 invocations, a 36/64 split, so an even eight-way cut
re-partitions both rather than subdividing each in half. Target is roughly 37 invocations per shard.

### Rollout

S1 and S3 land together, because a re-cut region without its floor is a shard that cannot fail on
coverage. S2 follows once the floors are measured. S4 last, since a join over eight rows needs the
eight rows to exist.

### Alternatives rejected

**Batching alone.** Measured at 40 to 44 minutes unsharded, because excluding the control arms
`TOOL-dScriptedRepeat-15` S3 forbids batching leaves 95 blocks carrying 136 solo invocations. It
misses the target at 5, 7 and 10 blocks per batch.

**Cutting spawns.** `TOOL-aTracedSpawn-2` bounds it at roughly 2 s per invocation of real non-spawn
work, a ~586 s floor at 293 invocations before any spawn is removed.

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh`, `tools/run-gates/selftest-budgets.txt`, and this build's
records. S4 may touch `tools/run-gates/` depending on where the join predicate lands.

## 5. Production-readiness checklist

- security — N/A. Scheduling only; no arm's subject changes.
- perf / scale — the whole unit. The figure is the longest shard's wall clock on a frozen clone.
- error / empty / loading states — the suite already REFUSES an out-of-range or wrong-arity
  `--shard`; S1 must keep that refusal exact at the new arity.
- observability — each shard prints its own executed count against its own floor, so a shard that
  silently loses arms fails on coverage rather than passing quietly.
- risks — a cut that separates an arm from state a sibling established produces a GREEN that proves
  nothing. The measured zero cross-region coupling makes that unlikely and does not make it
  impossible, which is what AC1's union identity is for.
- testing — AC1 is the control and must be observed FAILING on a deliberately mis-cut region before
  the split is trusted.
- migration — none. Reverting is restoring the constant and one budget row.
- user docs — N/A. Developer-facing.

## 6. Acceptance criteria

- **AC1** — When `check-unattended.test.sh` runs at all eight shard indices and unsharded, the sum of
  the eight executed assertion counts equals the unsharded count, allowing for the declared
  `PROLOGUE_ARMS`.
  `figure:` DERIVED from the nine runs, never pinned here.
  Red when: the sums differ, which is an arm that belongs to no shard or to two.
- **AC2** — When an arm is deliberately moved into a shard that does not carry the state it depends
  on, that shard REDS. Staged and observed before the split is trusted, per `AGENTS.md` §7.
  Red when: the move runs green, which is a split that proves nothing.
- **AC3** — When `bash tools/run-gates/run-selftests.sh --kit tools/unattended --list` runs, it names
  eight `unattended gate selftest` rows and not one.
  Red when: it names one, which is the state today and the reason the constant alone is inert.
- **AC4** — When the eight rows run through the runner's pool on a frozen clone on an idle box, the
  LONGEST shard completes in under 20 minutes, measured with `date +%s` and recorded into
  `tools/run-gates/selftest-budgets.txt`.
  `figure:` DERIVED from that run.
  Red when: the longest shard exceeds 20 minutes, which sends the goal to `TOOL-aBatchedArm-1`'s
  batching on top rather than to a lowered target.
- **AC5** — When one shard row is deleted from the declaration, the join REDS naming the missing
  index.
  Red when: eight-minus-one rows report a whole-suite green, which is the silent-coverage-loss class
  `TOOL-aGradedDoorway-8` records as unshipped upstream.
- **AC6** — When the split lands, the per-arm `FAIL` set across the eight shards is identical to the
  unsharded `FAIL` set at the same commit, red arms included.
  `cost:` one unsharded run plus eight sharded runs on a frozen clone.
  Red when: any `FAIL` line appears or disappears, which is a verdict this unit changed and must not.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `testsuite counts self-test` · `run-gates canary`

New arm: `tools/unattended/check-unattended.test.sh` · a region deliberately mis-cut so an arm loses
its state, and a deleted shard row, each staged and observed RED then unstaged · floor to move:
`FLOOR_ASSERTIONS` plus eight new per-shard floors, all measured under S3.

## 8. Open questions

- **F1 · Where does the shard-join predicate live?** `TOOL-aGradedDoorway-8` records that it exists
  only in `tools/run-gates/run-gates.gov.test.sh:347-353`, the gov-only canary, and that shipping it
  with the kit is owed upstream. RESOLVED (agent, 2026-09-10, delegated): S4 uses the canary's
  predicate where it already binds for gov, and the kit-shipping half stays `TOOL-aGradedDoorway-8`'s
  row rather than being absorbed here — this unit needs the join to hold for THIS repo, not to ship
  it to adopters.
- **F2 · Eight, or fewer?** Eight is the owner's ruling of 2026-08-29 under `TOOL-aGradedDoorway-7`
  S2, "pick 8 and fix what breaks". RESOLVED (owner, 2026-08-29): eight. If AC1 cannot be satisfied
  at eight, the finding is recorded and the arity is lowered with the reading beside it, never raised
  to fit.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft, from round 2's measurement that batching alone lands at 40 to
  44 minutes. Added to the build by `--rescope --act add` under protocol §11 rather than parked: it
  makes the measured observable strictly better, makes nothing worse, and trips no M3 veto. Records
  one correction found while writing it — the arity constant alone is inert, because nothing in the
  tree invokes this suite with `--shard`, so the DECLARATION split is the unit and the constant is
  one line of it.

## 10. Reuse audit

- **The seam is the suite's own shard contract**, already implemented at
  `tools/unattended/check-unattended.test.sh:29-56`: `SHARD_ARITY`, the parsed `--shard <i>/<n>`
  flag, the arity and range refusals, and `in_shard()`. Nothing is invented here; the constant moves
  and the regions are re-cut. The declaration seam is `tools/run-gates/selftest-budgets.txt`, whose
  row grammar already carries a per-row argv, so eight rows need no format change. The join seam is
  `tools/run-gates/run-gates.gov.test.sh:347-353`, which F1 resolves to reusing rather than porting.
- **The retrieval arguments, verbatim:**
  `python tools/codebase-map/reuse_lookup.py "batch staged breaks into one fixture and assert the emitted failure set"`
  and
  `python tools/memory-recall/query.py "why do the kit self-test suites re-run the whole program once per arm instead of batching, and what was decided about porting them to a pooled harness" --terms "selftest arm fixture batching pooled harness invocation spawn shard budget port reset_tree assertion floor"`.
  Both were run for `TOOL-aBatchedArm-1` and cover this unit's subject, which is the same suite and
  the same cost question; they surfaced `TOOL-aPooledSweep-7`'s "dividing that one suite" follow-up,
  which is this unit. Not re-run for this spec, and that is stated rather than implied.

# TOOL-aShardedFloor-3 — the gate selftest, split by the same contract

**Status:** OPEN · rev-2 · 2026-08-21 · node a · Tier-2 · base 36d0ad3b · streams tooling

## 1. Goal

Split `unattended gate selftest` (`tools/unattended/check-unattended.test.sh`) into two bar legs by
`TOOL-aShardedFloor-2`'s contract, ADOPTED verbatim rather than reinvented. It must land with its
sibling: alone, either one buys 3.7 % because the other simply becomes the new floor.

## 2. Scope (IN)

- **S1** — the sibling's `--shard i/n` contract, adopted: same flag grammar, same parse-before-any-
  scratch-dir rule, same refusal set, same mode-selected floor, same cover arm.
- **S2** — ONE structural boundary, chosen by MEASUREMENT from two candidates and with the rejected
  timing recorded. Both candidates are block edges; neither separates an arm from its control.
- **S3** — this file's own hoists, which are not the sibling's.
- **S4** — two manifest rows carrying this leg's own three-entry `guard` array byte-identically. The
  identical-guard rule binds WITHIN a sibling pair, not across the two units — the driver's guard is
  a different array and stays that way.
- **S5** — a STATE comparison against the unsharded run at the boundary and at the end of each mode.
- **S6** — **both leg names, stated.** Shard 1 KEEPS `unattended gate selftest`, so it inherits its
  warm ledger row and still dispatches first; shard 2 is `unattended gate selftest shard B`. This is
  the sibling's naming resolution and it BINDS this file too, because the names are load-bearing
  twice — warm-ledger dispatch rank, and the codebase-map key swap. No digit-bearing parenthetical:
  the descriptor grammar refuses one.
- **S7** — `tools/unattended/kit.toml`: a second `[[gate_leg]]` row, as the sibling.

## 3. Non-goals (OUT)

No physical split, for its sibling's reason. No re-derivation of the shard contract — a second
spelling of it is the defect §12 exists to prevent. No third shard. No fix to the leaked
`refs/heads/ahead` this file pushes and never deletes: it is real, it is named as a risk, and
touching the fixture while splitting it makes the split unreviewable.

## 4. Design

§"Unit B" of [the research record](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md). Four things
bind and are stated here because a builder who trusts the earlier report cuts in the wrong place:

**"Its arms are genuinely independent" is FALSE at arm granularity.** The report's seam guidance is
half true. Arms chain inside blocks — a control editing a file an earlier commit created, five arms
riding one commit, a whole block restoring only at its end. What IS independent is the
`reset_tree`-led block, and the design rule is therefore "one boundary, at a block edge", never "cut
between independent arms".

**Do not write a count of those blocks into this spec.** The first brief said "~30" and the
derivation gives a different number. If a count is needed, the checker derives it.

**The candidate the source briefs named was off by one.** Cutting after the line they proposed
separates an arm from its control — the exact defect this design's own risk list forbids. The two
legal candidates are the end of the check block and the end of the lifecycle block; the second keeps
the un-restored `main`/origin state entirely inside shard one, which is the safer property, and the
first is the more balanced. **Time both, record both, and say which lost.**

**Do not pick by arm count.** One tokenisation splits nearly evenly while the git-operation weight
splits ~2:1 — and the bar's floor is the LARGER shard, so imbalance eats the win directly.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the win. `max(shard)` must be at most 55 % of the unsharded wall.
- a11y · i18n — N/A.
- error / empty / loading states — the sibling's five refusals, adopted.
- observability — each shard names its region and disclaims the other.
- risks — state leaks FORWARD across any boundary: this file pushes a ref to its origin and never
  deletes it, and leaves local `main` and origin `main` at a merge commit for a long stretch. **Settle
  this by RUNNING both shards, never by reasoning about it.** Separately, two controls lose their
  MEANING without failing: a "still clean after nine mutations" control is a control only if the nine
  mutations ran in the same process, and split away it degrades into a duplicate of the opening
  control. Name them in the header rather than pretending the split is free.
- testing + left-shift gates — the sibling's arms already cover the contract; this unit adds its own
  floors and its vector comparison.
- migration / rollback — as the sibling.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — each shard of `tools/unattended/check-unattended.test.sh` exits 0 and prints its PASS
  line. Satisfiable only with the corrected flag parsing, which is the sibling's contract.
- **AC2** — compare STATE, not verdicts. Capture `git ls-remote --heads "$ORIGIN"` and
  `git for-each-ref refs/heads refs/remotes` at the boundary and at the end of each mode, and
  require shard 2's capture to equal the unsharded run's at the same point, failing with both
  listings named. **The named negative:** run `--shard 2/2` with `refs/heads/ahead` planted and
  again with it absent and require a DIFFERENCE, naming the specific arm to break so two builders do
  not break two different ones — otherwise the arm does not read the leak and AC2 protects nothing.
  rev-1 required a per-arm PASS/FAIL vector, which fails twice: it has the SAME blindness to an arm
  passing for the wrong reason (PASS in both runs, vectors equal), and the artifact does not exist,
  because this suite's helpers print only on failure and a green run emits one PASS line with no
  per-arm vector to slice. The sibling's per-arm BYTE comparison belongs here too.
- **AC3** — the unsharded invocation of `tools/unattended/check-unattended.test.sh` still exits 0
  above its own `FLOOR_ASSERTIONS`.
- **AC4** — all FIVE refusals, each exiting 2, naming the argument, and running nothing:
  `--shard 3/2`, `--shard 1/3`, `--shard 0/2`, `--shard two`, and a bare `--shard`. rev-1 tested
  three and dropped `1/3` and `0/2` — the two a manifest edit or an off-by-one in the dispatcher
  produces, as opposed to the two a typist produces. Since refusal happens before the first scratch
  dir, an unarmed arity check means a shard that silently runs the WRONG region rather than one
  that refuses.
- **AC5** — the per-part floors sum to at least `FLOOR_ASSERTIONS`, asserted in every invocation;
  setting the sum one below reds all three modes.
- **AC6** — byte-identical `guard` arrays within THIS pair and the same chunk; a diff touching only
  the protocol document runs both shards or skips both.
- **AC7** — the threshold is DERIVED from the two candidate timings this spec already requires
  recording, not authored. rev-1 required 55 %, which this spec's own §4 refutes: the git-operation
  weight splits about 2:1, i.e. 66.7 %, and both legal boundaries sit AFTER the git-heavy region so
  neither can move that weight forward — while §3 forbids a physical split or a third shard. Record
  both candidates, take the better, and **if both miss the target, accept the imbalance and
  re-price the headline** rather than keeping a criterion nothing can satisfy. Witness: the two
  standalone walls of `tools/unattended/check-unattended.test.sh`, both recorded in the build record.
- **AC8** — `check-arms.py --check` green with the armed-floor pin unchanged.
- **AC9** — `check-testsuite-counts.sh` green, no new waiver row.
- **AC10** — `govkit selfcheck` green, with both S6 names claimed by `tools/unattended/kit.toml`.
  **No leg name is retired** — the sibling's resolution keeps shard 1's existing name, so one key
  arrives and none departs. rev-1's "any retired leg name absent" was a live signal that this file
  might intend the symmetric rename the sibling rejected.
- **AC11** — codebase-map coverage + freshness green in both directions in the same commit, with
  `memory/map/features/unattended.md` and the generated artifacts moved together.
- **AC12** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` green, with the charter sentence and
  both gov-canary arm halves moved in the same commit; the run record shows both shard legs as
  separate rows with separate input keys.
- **AC13** — the header of `tools/unattended/check-unattended.test.sh` states that a green shard leg
  is evidence about its own part only, and names where the whole-suite claim lives.
- **AC14** — `TOOL-aShardedFloor-2` ships in the SAME landing, witnessed by both pairs of rows
  existing in `tools/gate-legs.json` at one commit, or the win is 3.7 % instead of 27.6 %.
- **AC15** — the objective itself, observed, **with its three literals stated rather than chosen
  after measuring**. BASELINE: the 1001.3 s four-run mean recorded in
  `memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md` — the only
  candidate that IS a mean. MARGIN: at least 200 s, conservative against the 282-292 s the
  simulator predicts. N: at least 3 `GATE_FULL` bars at the same profile row and width. The witness
  is `<git-dir>/gate-run/<id>/*.leg`, whose rows carry per-leg start and end in nanoseconds.
  **RETENTION NOTE:** the runner keeps only the last five run dirs and sweeps older ones, so copy
  the `.leg` files aside before the sixth bar or the evidence is gone before it is read.

## 7. Gates

As `TOOL-aShardedFloor-2`. **This unit adds a second manifest ROW on an existing script plus its
descriptor row** — no new script and no new checking surface — and its own floors. Guard parity
within this pair is a DOCUMENTED MANUAL CHECK, not a gated one: the descriptor join reads names and
never a `guard` field. Tracked as `TOOL-aPacedTurnstile-12`; AC6 is its compensating observation.

## 8. Open questions

none — one fork is RESOLVED here and one is deliberately left to measurement. **Resolved:** the
boundary is chosen by the recorded timings of both candidates, not by argument, and if they tie the
safer candidate wins because it keeps the un-restored `main`/origin state inside one shard.
Resolver: this session. **Left to measurement, which is not a fork:** which of the two candidates is
faster. *(resolver: this session.)*

**One stray fact, RESOLVED here so the minute is spent once.** A comment in this file claims
`git clean -qfd` removes the copied kit and so the arm re-copies it. It does not: the kit is copied
early, COMMITTED, and `PRISTINE` is a later commit on the same history, so the file is TRACKED and
`clean` without `-x` cannot touch it. The independent proof is an arm that resets and edits the kit
with no re-copy and asserts green. The comment is wrong and the re-copy beside it is dead code.
Keep the surrounding warning: this comment's neighbours are not trustworthy.

## 9. Revision log

- rev-1 · 2026-08-21 · initial, from the design pass at
  [`build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md`](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md).
  Folded from the skeptic pass: the arms are NOT independent at arm granularity, the proposed
  boundary was off by one and separated an arm from its control, the flag must be parsed rather than
  position-read, and the count-equality acceptance was replaced with a per-arm vector comparison
  because the counters make the arithmetic pass over a genuinely wrong run.
- rev-2 · 2026-08-21 · M4 spec audit folded, record [`reviews/2026-08-21-review-TOOL-aShardedFloor-1.md`](../reviews/2026-08-21-review-TOOL-aShardedFloor-1.md), verdict BLOCKED, 40 confirmed of
  65. The high against this unit was **F3**: AC7's 55 % bound is refuted by this spec's own §4, and
  neither legal boundary can reach it. AC7 now derives its threshold and states the fallback. Also
  folded: rev-1's replacement per-arm vector had the same blindness as the count it replaced AND
  named an artifact this suite cannot produce, so AC2 compares STATE with a named negative (F7);
  AC15 carried none of its three literals and would have been graded after measuring (F4); both leg
  names are now stated and AC10's retired-name clause is resolved (F15); two of the five refusals —
  the two a machine produces rather than a typist — were dropped (F16); §7 implied no manifest row
  (F22); guard parity is a named manual check (F20); and §8's stray errand is resolved from source
  (F25).

## 10. Reuse audit

**The seam is `TOOL-aShardedFloor-2`'s contract, by construction** — this unit is that contract's
second instance, which is the whole reason the contract is written as prose in the sibling script
rather than invented twice. §12's rule is that a "kind" gets a factory at instance #2; here the
factory is a documented argument contract, because the two files share no code and a shell function
cannot be shared between two standalone test scripts without a third file the arms meta-gate would
then demand a sibling test for.

**The probe and its blindness** are the sibling's, and the same recall terms answer for both. Re-run
them at any reground:
`python tools/memory-recall/query.py "has this repo decided before how to split a long gate leg, and what constrains a test suite growing a second manifest row" --terms "shard gate leg manifest argv floor assertions armed branches sibling test suite split selftest chunk selftests guard"`

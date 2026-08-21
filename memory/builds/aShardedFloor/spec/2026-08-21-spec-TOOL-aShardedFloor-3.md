# TOOL-aShardedFloor-3 — the gate selftest, split by the same contract

**Status:** OPEN · rev-1 · 2026-08-21 · node a · Tier-2 · base 36d0ad3b · streams tooling

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
- **S5** — a per-arm PASS/FAIL VECTOR comparison against the unsharded run, not an assertion count.

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
- **AC2** — each shard's per-arm PASS/FAIL VECTOR equals the corresponding slice of the unsharded
  run at the same commit. A count equality is NOT sufficient and the spec says why: the counters
  increment unconditionally when reached and the only loop is fixed-iteration, so `n1 + n2 == n`
  passes even when a leaked ref makes a shard-two arm pass for a different reason. Additionally
  observe both shards at a commit where a known arm is deliberately broken, so the comparison is
  exercised RED as well as green.
- **AC3** — the unsharded invocation of `tools/unattended/check-unattended.test.sh` still exits 0
  above its own `FLOOR_ASSERTIONS`.
- **AC4** — `--shard 3/2`, `--shard two`, and a bare `--shard` each exit 2, name the argument, and
  run nothing.
- **AC5** — the per-part floors sum to at least `FLOOR_ASSERTIONS`, asserted in every invocation;
  setting the sum one below reds all three modes.
- **AC6** — byte-identical `guard` arrays within THIS pair and the same chunk; a diff touching only
  the protocol document runs both shards or skips both.
- **AC7** — `max(shard one, shard two)` standalone is at most 55 % of the unsharded standalone wall,
  with BOTH candidate boundary timings recorded including the rejected one.
- **AC8** — `check-arms.py --check` green with the armed-floor pin unchanged.
- **AC9** — `check-testsuite-counts.sh` green, no new waiver row.
- **AC10** — `govkit selfcheck` green and any retired leg name absent from the manifest.
- **AC11** — codebase-map coverage + freshness green in both directions in the same commit, with
  `memory/map/features/unattended.md` and the generated artifacts moved together.
- **AC12** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` green, with the charter sentence and
  both gov-canary arm halves moved in the same commit; the run record shows both shard legs as
  separate rows with separate input keys.
- **AC13** — the header of `tools/unattended/check-unattended.test.sh` states that a green shard leg
  is evidence about its own part only, and names where the whole-suite claim lives.
- **AC14** — `TOOL-aShardedFloor-2` ships in the SAME landing, witnessed by both pairs of rows
  existing in `tools/gate-legs.json` at one commit, or the win is 3.7 % instead of 27.6 %.
- **AC15** — the objective itself, observed: over the bars taken after the change, the mean span
  reconstructed from the per-leg run records is at least the predicted margin below the recorded
  pre-change mean, with both means and the run count quoted in the build record. The witness is
  `<git-dir>/gate-run/<id>/*.leg`, whose rows already carry per-leg start and end in nanoseconds, so
  this costs nothing but reading them.

## 7. Gates

As `TOOL-aShardedFloor-2`. This unit adds no gate leg and no gate arm beyond its own floors.

## 8. Open questions

none — one fork is RESOLVED here and one is deliberately left to measurement. **Resolved:** the
boundary is chosen by the recorded timings of both candidates, not by argument, and if they tie the
safer candidate wins because it keeps the un-restored `main`/origin state inside one shard.
Resolver: this session. **Left to measurement, which is not a fork:** which of the two candidates is
faster. A stray fact worth one minute first — a comment in this file claims `git clean -qfd` removes
the copied kit and so the arm re-copies it, but the kit was committed earlier and is therefore
TRACKED, so `clean` cannot touch it. Confirm in a scratch repo before trusting any other claim that
comment's neighbours make.

## 9. Revision log

- rev-1 · 2026-08-21 · initial, from the design pass at
  [`build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md`](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md).
  Folded from the skeptic pass: the arms are NOT independent at arm granularity, the proposed
  boundary was off by one and separated an arm from its control, the flag must be parsed rather than
  position-read, and the count-equality acceptance was replaced with a per-arm vector comparison
  because the counters make the arithmetic pass over a genuinely wrong run.

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

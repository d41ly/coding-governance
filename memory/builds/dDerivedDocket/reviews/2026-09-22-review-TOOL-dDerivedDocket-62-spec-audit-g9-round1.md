**Serves:** spec-audit TOOL-dDerivedDocket-62 TOOL-dDerivedDocket-63 TOOL-dDerivedDocket-64 TOOL-dDerivedDocket-61

# dDerivedDocket — spec audit of G9, the three units promoted at G8's exit and unit 61's fold text, round 1

*Node `d`, 2026-09-22. This is the first Tier-2 adversarial pass over `TOOL-dDerivedDocket-62`,
`TOOL-dDerivedDocket-63` and `TOOL-dDerivedDocket-64`. The G8 bounded exit promoted them from unit
61's B1, H1 and H2: 62 gives one answer per slug across worktrees, 63 restores the `--replaces` row's
precedence, and 64 puts the turnstile queue on the liveness clock. The pass also covers the FOLD TEXT
of `TOOL-dDerivedDocket-61`. That spec went from rev-2 to rev-6 by folding G8's nine mediums and two
further fixes, so every §9 line of 61 dated after the G8 record indexes text no review had read.

The three promoted specs were written in parallel against 61 rev-2 and reconciled afterwards. Unit 61
builds first, and 62, 63 and 64 build after it in that order, each on the driver 61 leaves. Code
claims are judged at HEAD `ac8f3ab7`, the merged tree. Each promoted spec is also judged against 61 AS
SPECIFIED, because 61 is not built. Contradiction between the four specs, and between them and the
CLOSED units whose code they change (`TOOL-dDerivedDocket-4`, `-5`, `-22` and `-28`), was in scope.

Four primed finder lenses ran and all four returned. A skeptic stage prompted to REFUTE each finding
ran in five batches and all five returned. This synthesis then re-read the load-bearing sites at HEAD
before writing each entry: `tools/unattended/resume-tick.sh:269`, `tools/unattended/unattended.sh`
at `:2398-2409`, `:5474`, `:5794`, `:5826` and `:5839`, `tools/unattended/SKILL.template.md:35`,
`tools/unattended/STOPS.template.md:185` and `:195`, the node's ref list and its scheduled tasks.*

**Round: 1.** Range at HEAD `ac8f3ab7`, each subject pinned at the blob it was read at:

- `memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-62.md@3b388faffc4e30c93a668516e1837236782e39e6`
- `memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-63.md@ab8f3639fd21a78b7b9c52f29c41ec99087bc055`
- `memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-64.md@c68b5a549151deefe27b974b08c53669bbb322a1`
- `memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-61.md@a55a808cb0a370db5cb7d2a7779591a63b06d27d`

## Verdict: CLEAN WITH FIXES

No blocker stands. The review found one HIGH, eight MEDIUM and five LOW: fourteen adjudicated items
carried by twenty raw confirmed findings. Every fix lies inside this run's authority. None needs an
owner turn. The one fix that may need a mechanism has a route in a unit of the set that already adds
a mechanism of its kind, and a second route that needs none. That is why the verdict is not BLOCKED
despite the high.

Read H1 first, because it answers the brief's central question yes. Unit 61 §4 says every refresh the
retired lease file took, except the one at `run_bounded`'s start, moves a signal `--liveness` already
reads. That is false while the orchestrator waits on a background Workflow. Sub-agents write under
`<sid>/subagents/`, which the transcript term never reads. Unit agents run `--dispatch` and `--brief`
in wave worktrees, whose clocks the run worktree never reads. Once 61's Rollout records this build's
session and pid, a wave that outlasts the 5400 s bound with no orchestrator commit reads STALE in the
run worktree itself. That is the one worktree unit 62 lets act. A registered resume tick would then
kill the orchestrator, and the Workflow with it. Unit 64 adds only the queue term. No resume tick is
registered on node `d` at writing, so the harm is latent, and the fold has to land before one is.

Each promoted unit closes its G8 finding as designed. What stands below H1 is this build's dominant
class again: a design argument with no criterion that can see it break. M1 and M2 are the two
placements unit 62 argues in order to close B1. Get either wrong and every criterion stays green
while B1's double drive returns. M3 is the same defect in 63's widening to an unknown clock.

The rest is what parallel authoring predicts: seams between the specs. They are M4 to M7. There are
also four fold remnants in 61 that contradict another passage of 61: M8, L3, L4 and L5.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero count below
is evidence and not an artefact of a missing lens.

Some raw ids describe one defect each from several addresses, and they are merged:

- 1 and 10 into M1;
- 14, 23 and 25 into M4;
- 2 and 9 into M5;
- 5 and 11 into M6;
- 19 and 24 into L4.

The pipeline's duplicate count of 0 comes from its own exact-match dedupe, which does not see a
restatement.

## Review shape

Raw 28, confirmed 20, refuted 8, unverified 0. Precision 0.71. That is above the ~0.5 floor that
charter §8 sets, and up from G8's 0.42. The 8 refuted findings are not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 1 | 1 |
| MEDIUM | 8 | 13 |
| LOW | 5 | 6 |
| Total | 14 | 20 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 to G8
reports used, so the groups' counts compare.

- BLOCKER means that, as specified, the unit cannot reach the outcome it names, and the set needs a
  decision or a mechanism no spec in it carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  property as delivered while it is not, where the reachable harm is a kill or a double drive.
- MEDIUM covers a contradiction with a bounded consequence, a declaration a spec owes, and a rule
  whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

One call moves against the finders' ratings, and two were weighed and left where they came in.

- Finding 14 came in LOW and is absorbed into M4, taking that item's MEDIUM. It is the Migration
  sentence that 23 and 25 show to be the premise of the regression.
- Finding 20 came in HIGH and stays HIGH. BLOCKER was weighed, since the harm lands on this build's
  own orchestrator, as G8 B1's did. It is not a blocker because route (b) of its fix needs no
  mechanism, and route (a) is one `derive_last_move` term of the kind unit 64 already adds. It is
  also G8 H2's class, a clock premise that a waiting process falsifies, and G8 rated that HIGH.
- Findings 5 and 11 came in MEDIUM and stay MEDIUM. HIGH was weighed, because AC3's aged half cannot
  pass on unit 62's driver as written. The criterion reds loudly and names its cause, and the defect
  is a fixture fact and an edge the spec owes, which is MEDIUM's definition.

## The brief's questions, answered

- **Does each promoted unit close its G8 finding?** Yes as designed. Each one leaves a gap in what
  observes the close.
  - Unit 62 closes B1 by route (a). Only the worktree whose checked-out branch is the record's run
    branch acts, and every other copy reads ELSEWHERE. G8's evidence was six wave worktrees on their
    own `worktree-wf_<id>` branches, and each of them reads ELSEWHERE by construction, because git
    refuses to check the run's branch out twice. Two placements the close depends on have no
    criterion (M1, M2). The guard also reaches past B1's population onto leaseless records (M4).
  - Unit 63 closes H1 for a fresh clock. The moved `--replaces` row sits above the same-session row,
    so the holder replaces its own job again. Its widening to an unknown clock has no criterion (M3).
  - Unit 64 closes H2 for a queued bar. The turnstile heartbeat becomes a clock term. Its AC3 cannot
    pass on unit 62's driver as written (M6). The silent-leg residual is correctly declined in 64 and
    wrongly called promoted in 61 (M8).
  - H1 is a sibling of G8 H2 that no unit carries.
- **Does exactly one unit own each behaviour and each re-asserted suite arm?** No, in three places.
  - Unit 61 AC10's later-record reading is flipped by unit 62, and neither spec owns the arm (M5).
  - Units 62 and 63 key on stop-contract rows only 61 writes, and 61's AC13 never witnesses one of
    them positively (M7).
  - Unit 62 leans on 61 S8's absolute branch scope, which 61 §4 itself breaks for a record naming
    neither branch fact (L3).
- **Can an out-of-session actor kill, relaunch or refuse a live or HELD run, in any worktree?** Built
  as specified, B1's sibling-copy paths close. One path stays open, three misbuilds reopen others, and
  one refusal is new.
  - The tick kills and relaunches a LIVE orchestrator in the run worktree itself while a Workflow
    outlasts the bound, and the matrix admits a take-over there (H1).
  - Two misbuilds of 62 pass every criterion and reopen B1. With ELSEWHERE placed after
    FINISHED-UNSTAMPED, a dead landing session is relaunched twice (M1). With the guard placed after
    the HELD block, a sibling copy takes a HELD run over (M2).
  - A misbuild of 63 at an unknown clock takes a restarted holder over, which is G8 H1 returning (M3).
  - Unit 62 refuses abandoned leaseless runs whose branch exists nowhere, with a remedy that cannot be
    followed (M4). Those runs are not live, so this touches the question only at its edge.
- **Does every criterion fail when its property breaks, and is any green before its unit acts?** Not
  yet. M1, M2, M3, M7, L1, L2 and L3 name criteria that cannot see the break they claim.
  - One family of criteria is green before its unit acts. Unit 63 AC5's zero-counts read 0 at 63's
    base whenever 61's pass never wrote the rows they retire (M7).
  - One Red-when cannot fire at all on the driver it builds on, 64 AC3's (M6).
- **Does any fold in 61 contradict another passage of 61?** Yes, in four places, all in text rev-3 or
  rev-4 wrote or left stale.
  - F1 and AC20 contradict §5 risk (2) on who carries the silent leg (M8).
  - S8's absolute branch scope contradicts §4's neither-branch sentence (L3).
  - S1's deletion of the `LEASE —` line contradicts refusal texts that still name it (L4).
  - F11's order 30 contradicts the header and rev-4 (L5).

  H1's refresh sentence is rev-3 fold text too, but it is false against the code rather than against
  another passage. Every confirmed finding against 61 lands in text dated after the G8 record, which
  is where the brief aimed.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---:|---|
| 20 | HIGH | H1 | 61 | §4 The one lease record, "Freshness is DERIVED"; §5 risks (1), (6) |
| 1 | MEDIUM | M1 | 62 | §2 S2; §4 verdict order; §6; §7 tick arm line |
| 10 | MEDIUM | M1 | 62 | §4 verdict order; §6 AC1 to AC3; §7 tick arm line |
| 3 | MEDIUM | M2 | 62 | §2 S4; §6 AC4, AC5, AC8; §7 driver arm line |
| 4 | MEDIUM | M3 | 63 | §2 S1, the "or unknown" clause; §6 AC1, AC2, AC4 |
| 14 | MEDIUM | M4 | 62 | §4 Migration, last bullet |
| 23 | MEDIUM | M4 | 62 | §2 S4; §4 matrix; §4 Migration |
| 25 | MEDIUM | M4 | 62 | §4 Migration; §8, no fork; §2 S4 |
| 2 | MEDIUM | M5 | 61 | §6 AC10, last sentence; §7 driver arm line |
| 9 | MEDIUM | M5 | 62 | §2 S8; §4 the awk-scan paragraph; §6 AC11 |
| 5 | MEDIUM | M6 | 64 | §6 AC3 and AC1's fixture line; §3 Edges |
| 11 | MEDIUM | M6 | 64 | §6 AC3; §3 the non-goal on which copy is graded |
| 6 | MEDIUM | M7 | 61 | §2 S11, the stop contract's §8 table; §6 AC13 |
| 12 | MEDIUM | M8 | 61 | §8 F1; §6 AC20 Red when; against §5 risk (2) |
| 7 | LOW | L1 | 61 | §2 S11, the Skill tick paragraph; §6 AC13 |
| 8 | LOW | L2 | 61 | §2 S7; §4 matrix holder row; §6 AC11 |
| 13 | LOW | L3 | 61 | §2 S8; §4 The pushed landing, re-bound; §6 AC23 |
| 19 | LOW | L4 | 61 | §2 S1; §4 matrix, working no-id row |
| 24 | LOW | L4 | 61 | §2 S11, S13; §6 AC13 |
| 28 | LOW | L5 | 61 | §8 F11 |

Spec paths below are abbreviated to their unit number. "Spec 61" is
`memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-61.md`, and specs 62, 63 and
64 are the siblings of that name. Each was read at the blob pinned in the range line above. A "spec
line" is a line of the spec file; a bare `:N` is a line of the code file last named.

## High

### H1 — the clock goes silent while the orchestrator waits on a Workflow, so the one worktree unit 62 lets act reads STALE (20)

**Address.** Spec 61 §4 "The one lease record", the paragraph beginning "Freshness is DERIVED", and
§5 risks (1) and (6). The premise reaches spec 62 §8 F1 and spec 64 §3, the non-goal on which
worktree's copy is graded. The paragraph is rev-3 fold text.

**What is wrong.** The paragraph says the retired file was refreshed by every writing verb, by the
start of `run_bounded` and by the holder's tick. It then says that all but the second of those move
a signal `--liveness` already reads, because "a writing verb moves a dirty write or a commit, and a
tick's turn appends to the session's own transcript". That rests on two premises the spec never
states, and neither holds while the orchestrator waits on a background Workflow.

- It assumes every writing verb runs in the worktree being graded. At HEAD, `stage_or_fail` calls
  `write_lease_for_record` (`tools/unattended/unattended.sh:2398-2409`). That refreshed the
  common-dir file from ANY worktree. Unit agents run `--dispatch` and `--brief` on the run's record
  from wave worktrees (`tools/workflows/unattended-unit.js:147` and `:154`). Their writes move those
  worktrees' clocks, and the run worktree's `--liveness` never reads those.
- It assumes the holder's transcript moves while the holder waits. `resolve_transcript_path`
  (`tools/unattended/unattended.sh:5474-5481`) reads only `<sid>.jsonl`. Sub-agents write under
  `<sid>/subagents/workflows/<wf>/`.

The skeptic stage measured this on node `d` on 2026-09-22. The orchestrating session's transcript,
`2588f719….jsonl`, did not move from 07:15:12Z to 07:34Z while this review's own Workflow agents
wrote under `subagents/workflows/wf_10a8ced7-955/`. Its user entries from 05:47Z to 07:15Z are task
notifications and Workflow launches only, with gaps of 34, 20, 18 and 22 minutes. None of them is a
keepalive wake, although a `3-59/10` cron sits in that transcript. At 07:34:04Z, `--liveness` in the
run worktree read `last-move 1220` with source `commit`. The orchestrator's own commits are the only
signal that moves there.

**Why it bites.** 61's Rollout records the orchestrator's `session`, `pid` and `lease-utc`. From then
on, any wave or review Workflow that outlasts `RESUME_STALE_BOUND`, 5400 s in gov, reads STALE in the
run worktree if the orchestrator makes no commit in that time. That happens in the one worktree unit
62 lets act. Two actors then reach it.

- The resume tick kills the recorded pid's tree, which is the orchestrator and its background
  Workflow, then relaunches.
- The matrix row "working, clock stale, an id" reads presumed-stopped. Any session's `--resume
  --keepalive-id` in that worktree takes the run over.

Nothing in the set covers this. Spec 62's route (a) discards the wave worktrees' clocks by design,
and those are exactly where the units write. Its F1 rejects the joined clock by weighing only the
other side, a sibling's commit keeping a dead holder fresh. Spec 64 adds only the turnstile term.
Spec 61 §5 risk (1) names a transcript that does not derive, not one that derives and sits still.
Risk (6) runs the opposite way. No criterion reaches the case.

Measured for this report on 2026-09-22: node `d` has no resume tick registered. `schtasks /query`
lists 416 tasks, and none of them matches `resume`, `unattended` or `tick`. The kill is latent until
someone registers one. 61's Rollout sentence "the stop-guard and the tick bind that session" is what
arms it.

**Fix.** Choose one of two routes. The choice is the orchestrator's act under the delegated M3 rule,
as G8 B1's route was.

- (a) Add a `derive_last_move` term for the recorded session's sub-agent transcripts: the newest
  mtime under `<projects>/<enc>/<sid>/subagents/`, labelled for example `subagent`. It fits in unit
  64 beside the gate-queue term, which has the same shape and the same class, or in a new promoted
  unit. Give it an arm. Age the commit and `<sid>.jsonl` past the bound and leave one fresh file
  under `<sid>/subagents/workflows/<wf>/`. `--liveness` then reads `stale: no` with
  `last-move-source: subagent`, and the matrix refuses at 58. The fold must also state whether a
  Workflow can outlive its session's process, because only if it cannot does the term keep a dead
  holder fresh for no longer than one bound.
- (b) State the residual in spec 61 §5 and spec 62 §8 F1, with the measured window. Make 61's Rollout
  say the tick is not registered while a Workflow runs.

Under either route, correct 61 §4's refresh sentence. The retired refresh reached every worktree
through `stage_or_fail`, and the transcript term misses sub-agents. Whichever route is chosen, keep
the tick unregistered on node `d` until the term or the stated rule has landed.

**Left-shift.** Add a documented check for any spec that retires a refresh, a heartbeat or a lease
write. Enumerate every writer of the retired signal by grep, here every caller of
`write_lease_for_record`. For each one, name the worktree and the process it runs in, and name the
replacement signal the reader sees from where the reader runs. A writer in another worktree or
another transcript is a gap unless the spec names it as a residual.

## Medium

### M1 — ELSEWHERE ahead of FINISHED-UNSTAMPED is argued but never observed, so the one acting verdict besides STALE can relaunch twice (1, 10)

**Address.** Spec 62 §2 S2; §4 "`--liveness`, and the verdict order", the bullet "ELSEWHERE precedes
FINISHED-UNSTAMPED"; §6 AC1 to AC3, AC6 and AC7; §7 the resume-tick arm line; §8 F8.

**What is wrong.** §4 orders the verdict chain TERMINAL, ELSEWHERE, FINISHED-UNSTAMPED, HELD,
UNBOUND, STALE, LIVE. It justifies ELSEWHERE's place ahead of FINISHED-UNSTAMPED: under in-place
landing, the primary tree carries the unobserved LANDING record once it fast-forwards. Of the
ordering arguments §4 makes, that is the only one that carries a kill, because
`tools/unattended/resume-tick.sh:269` acts on `STALE:*|FINISHED-UNSTAMPED:yes`.

No criterion reads a FINISHED-UNSTAMPED copy outside the holder worktree.

- AC1 and AC2 use a BUILDING copy.
- AC3 uses a HELD record beside a BUILDING copy.
- AC6 reads the matrix's `--resume` output, not `--liveness`.
- AC7 stubs the verdict.
- AC8 uses records that name no branch.

§7's tick arm is staged RED by a driver copy that drops the ELSEWHERE row. That tests whether the row
exists, not where it sits. F8 says "a new tick row can reach the walk only through `--liveness`,
whose verdict order AC1 observes". That overclaims, since AC1 observes ELSEWHERE against BUILDING
only.

**Why it bites.** A driver that slots ELSEWHERE anywhere after FINISHED-UNSTAMPED, just before STALE
for instance, passes AC1 to AC12. Suppose a landing session then dies between the in-place push and
`--landed`. It is killed and relaunched from the primary tree as well as from the run worktree. That
is two relaunches of one session, B1's class, reached through the one acting verdict other than
STALE. M5's arm makes this worse. As unit 61 wrote it, that arm is green only when FINISHED-UNSTAMPED
beats ELSEWHERE in a detached worktree, which pushes a builder of 62 toward the wrong order.

**Fix.** Add a criterion and a tick-suite arm over `add_sibling_worktree`.

- The fixture is an in-place LANDING record, derived LANDED and unobserved, aged past the bound. It
  is committed on the run branch and carried by a second worktree on another branch.
- In the sibling, `--liveness` prints `verdict: ELSEWHERE`. In the run worktree it prints `verdict:
  FINISHED-UNSTAMPED`.
- `resume-tick.sh --dry-run` prints exactly one `resumed · attempt 1`, for the run worktree, and
  `skip · ELSEWHERE` for the sibling.
- Stage it RED with a driver copy whose chain places ELSEWHERE after FINISHED-UNSTAMPED.

Name the arm in §7 and correct F8's sentence.

**Left-shift.** Every "X precedes Y" a spec argues for a verdict chain or a row order gets an arm
whose fixture makes X and Y true at once, staged RED by the swap. Make it a documented check at spec
audit: grep the spec for "precedes" and "ahead of", and pair each hit with the criterion that names
both sides.

### M2 — the guard's place ahead of the HELD rows has no criterion, so a sibling can take a HELD run over (3)

**Address.** Spec 62 §2 S4; §6 AC4, AC5 and AC8; §7 the driver arm line; §8 F9's last sentence.

**What is wrong.** S4 places `check_holder_worktree` directly after unit 61's observed-landing row
and ahead of the first HELD row, so the HELD rows refuse outside the holder worktree. In unit 61's
matrix the HELD rows come before the working rows. But AC4's fixture is committed "at a working
phase", and AC5 and AC8 reuse it. AC6 is a LANDING record. §7's staged RED is a copy of the guard
that always returns 0, and that copy cannot detect where the guard sits. F9 says "the guard over the
HELD and working rows is this unit's, observed by AC4, AC5 and AC8". For the HELD rows that is
false. §4 itself says a sibling copy may be HELD.

**Why it bites.** A guard placed at the head of the working branch, after the HELD block, passes every
criterion in the spec. A sibling whose copy reads HELD with its condition met can then run `--resume
--keepalive-id C` and take the run over from a stale copy through `run_takeover`. Unit 61 AC12 shows
that take-over for a HELD copy whose condition is met. This is B1's double drive reaching a HELD run
from another worktree, which is one of the cases the brief asks about.

**Fix.** Add a HELD arm to AC4.

- Move the record to HELD with its condition met, and commit it on `unit` before the linked worktree
  is added on `wave`.
- `--resume tRun --keepalive-id C` from session `T` in the linked worktree refuses at check 58 and
  names `refs/heads/unit`. Afterwards `git status --porcelain` is empty in both worktrees.
- The same call in the run worktree takes the run over.
- Stage it RED with a driver copy that calls `check_holder_worktree` only inside the working branch.

Correct F9's observation claim.

**Left-shift.** A guard specified by its POSITION in a row chain is staged RED by a misplaced copy, not
only by a disabled one. A disabled guard proves the guard exists. A misplaced one proves where it is.

### M3 — unit 63 widens the moved `--replaces` row to an unknown clock, and no criterion runs it there (4)

**Address.** Spec 63 §2 S1, the "or unknown" clause; §4's row table, row 2 "working, clock fresh or
unknown"; §6 AC1, AC2 and AC4. Against unit 61 §4's row text, "clock fresh", and unit 61 AC21.

**What is wrong.** S1 deliberately widens the moved `--replaces` row to "fresh or unknown", because
unit 61's table writes that row for a fresh clock alone. It gives a reason and claims the widening is
"Observed by AC1, AC2 and AC4". All three run `build_hold_fixture` on a live clock. AC3's aged call
is stale, not unknown. Unit 61's AC21 is the only arm with a dead clock, and it passes no
`--replaces`.

**Why it bites.** Build the moved block the way unit 61's row literally reads, conditioned on a fresh
return only, and it passes every criterion here. At an unknown clock, the holder's `--replaces` under
a restarted pid then reaches row 3 and is taken over through `run_takeover`. That is G8 H1's defect
returning under a dead probe. Under the recorded pid the call reaches row 4, whose check-58 text tells
a caller who passed `--replaces` to pass `--replaces`.

**Fix.** Add a criterion over AC1's fixture with unit 61 AC21's dead `date` stub first on `PATH`.

- `--resume tRun --keepalive-id kB --replaces k1` prints the UNKNOWN announcement and `keepalive
  replaced`, and prints no `taken over`.
- It records `keepalive: kB` and leaves the history-row count unchanged.
- Both hold under the prologue pid and under `CLAUDE_PID=999999998`.
- Stage it RED with a driver copy whose moved block tests the fresh return alone.

**Left-shift.** A row keyed "fresh or unknown" gets one arm per state it names. A documented check at
spec audit: every row cell that joins clock states with "or" names one criterion per state.

### M4 — unit 62's guard reaches unit 61's leaseless rows, turns F8's take-over into a refusal with no usable remedy, and says it fixes the opposite (14, 23, 25)

**Address.** Spec 62 §2 S4; §4 "The resume matrix"; §4 Migration, the bullet on `aClosedDocket` and
`aUnblockedFleet` (spec lines 337 to 340); §8, which has no fork for this. Against spec 61 §8 F13,
§4's no-lease matrix rows and AC22, and against `TOOL-dDerivedDocket-4` §8 F8. The backlog row F8
answers is `memory/backlog/TOOL.md:322`.

**What is wrong.** S4 calls `check_holder_worktree` ahead of every HELD and working row, and unit 61's
no-lease rows are working rows. Unit 4's F8, option (a), judged a leaseless working record by its
build folder's commit age: presumed-stopped past the bound, and "never a refusal outside the bound".
It cited the aUnblockedFleet decision that removed exactly that no-override refusal. Unit 61 rev-3
folded G8 M3 through F13 to keep F8.

62's Migration bullet then describes the two records it measured as follows: "Their `--resume`
refuses at 58 naming that branch, where under unit 61 alone it would claim a live session drives
them. That is the audit's M3 population". That was true of 61 rev-2. It is false at rev-5, the
revision 62 rev-3 says it re-grounded on, and at rev-6.

Re-measured at HEAD, both records are BUILDING and carry `keepalive` without `lease-utc`. Their build
folders were last committed on 2026-09-05 and 2026-08-31. `git for-each-ref` finds neither
`refs/heads/branch/aclosed-docket` nor `refs/heads/branch/unattended-builds-blocking-640d0d`, locally
or as a remote-tracking ref.

**Why it bites.** Under unit 61 both records meet the no-lease row past the bound and are taken over,
announced, which is what F8 decided. Under unit 62 both refuse at 58, and the refusal says to check
out a branch that exists nowhere. Meanwhile unit 4's F5 has `--preflight` refuse a different id over
a live record and point at `--resume`. An operator following the messages has no path to either
slug except fabricating a branch of that name. That is the no-override class the backlog row
records. Unit 4's F8 is superseded without a record.

The hazard the guard exists for never reached this population. A leaseless record carries no
session, so the tick never acts on it. No criterion covers a leaseless record whose run branch no ref
names. 62 also credits itself with M3, which its own §3 says is 61's fold.

**Fix.** Choose one of two.

- Call `check_holder_worktree` only for a record that carries `lease-utc`. That leaves unit 61's
  no-lease rows as 61 specifies them.
- Or record a §8 fork that supersedes unit 4 F8 and 61 F13 for callers off the run's branch, citing
  the backlog row. When `HW_REF` resolves to no local ref under `git rev-parse --verify -q`, either
  have the check-58 text say to recreate the branch by name, or let the call through with an
  announcement. No worktree on this node can hold that slug, so there is no local holder to
  double-drive against.

Either way, rewrite the Migration bullet. Under 61 these past-bound records are taken over from any
worktree. Under this unit they are refused off-branch, which is a deliberate narrowing to be listed in
§5 risks. Add an arm over a leaseless record past the bound whose run branch exists nowhere, read
from a worktree not on it, and state its expected output.

**Left-shift.** A comparison of the form "under unit N alone it would …" is re-derived against unit
N's CURRENT revision at every re-grounding, and the spec names that revision. A documented check: a
re-grounded spec lists each claim it makes about a sibling's behaviour with the sibling's rev it read.

### M5 — unit 61 AC10's later-record reading flips to ELSEWHERE under unit 62, and neither spec owns the arm (2, 9)

**Address.** Spec 61 §6 AC10, its last sentence, and §7's driver arm line, both rev-3 M6 fold text.
Against spec 62 §2 S2 and S8, §4's awk-scan paragraph, and §6 AC11.

**What is wrong.** AC10 reads its observation "From a second linked worktree `W2`, detached at the
landing commit". It ends: "A later LANDING record of the same slug, whose log names only the earlier
landing commit, still reads `FINISHED-UNSTAMPED`". The sentence names no worktree. §7's arm line
groups it under the reads "from a second" worktree "with an earlier run's line", which places it in
W2.

Under unit 62, a detached HEAD returns 1 from `resolve_holder_worktree`. The later LANDING record is
unobserved, so it is not TERMINAL. With ELSEWHERE second in the chain, the W2 copy reads ELSEWHERE.
62's S8 and scan paragraph retarget only an existing arm that "reaches a guarded row off the record's
branch", meaning the matrix's HELD and working rows, and a `--liveness` reading is neither.

**Why it bites.** At VERIFYING with 62 built, the arm reds under both 61 AC15 and 62 AC11 ("an
existing arm newly fails because of it"), and neither spec owns its re-assertion. 62's own remedy,
retargeting onto the run branch, cannot apply in W2 while W1 has that branch checked out. So the
builder of 62 improvises. Meanwhile the property the clause guards, that an earlier run's
observation never marks a new landing finished, goes unobserved unless someone re-reads it in W1.
The observed-landing readings from W2 survive only because TERMINAL precedes ELSEWHERE. The property
itself survives too, as "not TERMINAL". What breaks is who owns the arm.

**Fix.** Choose one of two, and fold it in both specs in one commit.

- State in 61 AC10 that the earlier-run clause is read in W1, the linked worktree on the run branch,
  which no later unit's ELSEWHERE reaches.
- Or widen 62 S8 and its scan paragraph to every existing `--liveness`, stop-guard or tick verdict
  reading taken from a worktree not on the record's run branch, retargeted one for one. Name 61
  AC10's later-record reading as the known member: it moves to W1, and W2's reading of the same
  record is re-asserted as ELSEWHERE.

**Left-shift.** A unit that changes a verdict for a population states which EXISTING arms read a
verdict in that population, not only which arms reach a guarded row. Make it a documented check: grep
the suites, and the criteria of every unit ordered before, for readings taken from a worktree that
the new verdict now covers.

### M6 — unit 64 AC3's fixture names no run branch, so on unit 62's driver the tick skips where the criterion expects a relaunch (5, 11)

**Address.** Spec 64 §6 AC3 and AC1's fixture line; §4's measurement, the fixture description at
spec lines 102 to 104; §3 the non-goal ending "No edge to that unit is declared, because this unit
extends nothing that unit writes and builds against unit 61's clock alone"; §3 Edges.

**What is wrong.** AC3 runs the tick over AC1's fixture, "the scratch repository of §4's
measurement". §4 describes that fixture as a conf and one committed BUILDING run-state file "carrying
the six lease facts with `host: absent`". It names neither `run-branch` nor `branch-ref`. Unit 62 is
ordered 32 and this unit 34. 62's S3 and AC8 print `skip · NO RUN BRANCH` wherever a verdict that
would act meets `holder-ref: absent`. So AC3's aged half, `resumed · attempt 1`, cannot occur on the
driver this unit builds on. Its Red-when, "the tick decides `resumed · attempt 1` for a record whose
only fresh signal is the heartbeat", cannot fire either. §3 declares no edge to 62, although §5 risk
(4) concedes that only the run-branch worktree acts after 62.

**Why it bites.** The pass's direct check reds for a reason unrelated to the unit, or goes green only
after a fixture edit nobody recorded. The worse response is that the builder bends the tick to pass
the criterion, which would undo 62's skip. The resume-tick suite's arm survives only if it runs over
`build_fixture`, which 62 S8 makes write `run-branch: refs/heads/main`. As written, the criterion
points it at AC1's fixture.

**Fix.** Give §4's minimal fixture, and so AC1's and AC3's, a `run-branch` fact naming the ref its
HEAD has checked out, and say so on the fixture line. Declare a consumes-from edge to
`TOOL-dDerivedDocket-62` naming the tick's NO RUN BRANCH row, and rewrite §3's "no edge" sentence.
Alternatively, run AC3 over the tick suite's `build_fixture`.

**Left-shift.** A criterion whose fixture feeds an actor that a unit ordered BEFORE this one changes
is re-read against that unit's rows at reconcile. Make it a documented check for parallel-authored
promotions: for each actor a criterion runs, list every unit ordered before that edits the actor, and
declare an edge or say why none is owed.

### M7 — unit 61 AC13 witnesses the stop contract only through zero-counts, and units 62 and 63 key on rows only 61 writes (6)

**Address.** Spec 61 §2 S11, the stop contract's §8 table becoming §4's re-keyed matrix; §6 AC13,
rev-3 M8 fold text. Against spec 62's placement of its row below "the re-bind row and its off-branch
row", and spec 63 AC5's greps.

**What is wrong.** S11 and §4 say "section 8's table becomes the matrix above". AC13 witnesses
`tools/unattended/STOPS.template.md` only through zero-counts. It has no positive grep for any
re-keyed row. One row of the retired table escapes every zero-count: the LANDING row at `:195`,
whose Lease cell reads `released … landed`. The witness `released <iso>` does not match the ellipsis;
it hits only `:174` and `:415`. The retired header at `:185`, with its `Lease` column, "released,
stale or absent" and "fresh and taken" match no witness either.

**Why it bites.** A pass that deletes only "refreshes the lease" passes AC13 and leaves the table's
Lease column with its retired rows standing. AC13's own Red-when names exactly that failure. Agents
then follow a matrix that describes the retired file.

Two later units edit rows only 61 writes. Unit 62 places its row below "the re-bind row and its
off-branch row". Unit 63 AC5 greps for "process restarted", "a new id, another session" and "block of
the leased row below". If 61's pass never wrote those rows, 63's positive greps red for want of 61's
text. Its zero-counts read green before 63 acts. That is the only criterion in the set this review
found green before its unit acts.

**Fix.** Add positive witnesses to AC13. Each prints 1 in `STOPS.template.md` at the build commit, for
the rows later units key on:

- "the recorded session, which is not";
- "block of the leased row below";
- "a new id, another session";
- the off-branch re-bind row's "naming the record" text;
- the observed-landing row.

Add zero-counts for "released … landed" and for the retired header `| Record | Lease |`.

**Left-shift.** When a later unit's criterion greps text an earlier unit writes, the earlier unit's
criterion carries a positive witness for that text. Make it a documented check at reconcile: for each
grep in a later spec's criteria that names a carrier, find the witness in the unit that writes it.

### M8 — unit 61 F1 and AC20 call the silent leg promoted, while 61 §5 and unit 64 keep it as nobody's (12)

**Address.** Spec 61 §8 F1, the G8 fold sentence, and §6 AC20's Red when, both rev-3 fold text.
Against spec 61 §5 risk (2), spec 64 §3's first non-goal, §8 F5 and its hands-off edge, and spec 27's
AC9 and §3 non-goal
(`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md`).

**What is wrong.** F1 says "The queued or silent bar and the second-worktree read are G8 H2 and G8 B1
below, both promoted". AC20 says a bar queued at the turnstile or a leg silent past the bound "(G8
H2) … Both are promoted". But 61's own §5 risk (2) keeps the silent leg as this unit's residual. 64
declines it: its §3 calls it "unit 61's §5 risk (2), unchanged here", F5 resolves no, and the
hands-off edge says "No unit in this build carries them". 27's AC9 and §3 non-goal repeat that the
silent or queued bar is "promoted to TOOL-dDerivedDocket-64".

**Why it bites.** H2's fix required the residual to be stated truthfully: any leg whose ceiling
exceeds the bound. The record now says two things about the silent leg. Two fold passages of 61 and
two of 27 say 64 carries it. 64 and 61 §5 say nobody does. G8 M1 asked whether the withdrawal of 27's
S11 left a half standing, and this gives it the wrong answer again. That is the mismatch 27's rev-9
fold was meant to remove.

**Fix.** Reword F1 and AC20's Red when. G8 H2 is the queued bar, promoted to 64. A leg silent past the
bound is §5 risk (2), carried by no unit in this build and handed off by 64. Make 27's AC9 and §3
non-goal say the same in the orchestrator's next fold of that spec.

**Left-shift.** Every "promoted" claim in a fold names the promoted unit's S-item or AC that carries
the property, so a claim with no carrier is visible at the claim. A documented check at the bounded
exit: grep every fold for "promoted" and resolve each hit to a carrier in the named spec.

## Low

### L1 — the Skill's "lease is refreshed" sentence survives AC13 (7)

**Address.** Spec 61 §2 S11 and §4, the Skill's tick paragraph; §6 AC13.

**What is wrong.** S11 has the Skill's tick paragraph drop its refresh claim. AC13's only Skill
zero-count is "Then record the new id". The sentence at `tools/unattended/SKILL.template.md:34-35`,
"That is how this session's lease is refreshed", has no witness. AC13's refresh greps cover the stop
contract, the dossier and the protocol, and the positive Skill witnesses (checks 10, 26 and 51) pass
with the sentence standing. AC13's Red-when fires on "a carrier still describes … its refresh".

**Why it bites.** The paragraph every tick reads can go on saying that its first act refreshes a lease
that no longer exists, and AC13 stays green. The command the agent runs is unchanged, so the harm is
a false rationale, not a wrong act.

**Fix.** Add `grep -c 'lease is refreshed' tools/unattended/SKILL.template.md`, printing 0 at the build
commit and 1 at its first parent. Fold it with M7 and L4 into one AC13 edit.

**Left-shift.** Derive a carrier's zero-count witnesses from S1's list of retired nouns, as G8 M8's
left-shift proposed, rather than listing phrases by hand.

### L2 — the holder row's session half is unobserved (8)

**Address.** Spec 61 §2 S7; §4 the matrix's first working row; §6 AC11.

**What is wrong.** S7 and §4's holder row re-record the lease when the record "names another session
or pid than the harness exposes". AC11 varies only `CLAUDE_PID`, P then Q, plus the leaseless case.
No criterion resumes with the recorded keepalive under a different `CLAUDE_CODE_SESSION_ID`.

**Why it bites.** A holder row that compares the pid alone passes AC11. A holder whose session id
changed keeps the old `session` fact, and the stop-guard and the tick bind a session id that no longer
drives the run.

**Fix.** Add to AC11: with `CLAUDE_CODE_SESSION_ID=S2 CLAUDE_PID=P`, `--resume <slug> --keepalive-id
k1` records session S2, prints the old and new values and stages the record.

**Left-shift.** A condition written "A or B" gets an arm for each disjunct. This is the same
documented check as M3's.

### L3 — S8 says the re-bind writes nothing off-branch, and §4 lets a record naming neither branch fact re-bind anywhere (13)

**Address.** Spec 61 §2 S8, against §4 "The pushed landing, re-bound", the sentence at spec line 330
that a record naming neither branch fact "re-binds as before and says the re-bind was not scoped";
§6 AC23. Both are rev-3 M5 fold text. Spec 62 §4, F5, F9 and §5 risk (3) lean on S8's absolute
("that unit already confines it").

**What is wrong.** S8 says the re-bind runs only on a branch where that landing's own `--landed` runs,
and from any other branch it writes nothing. §4 then makes an exception for a record naming neither
fact, with a new announcement. §4's matrix table has no row for it, AC8's and AC23's fixtures always
name a branch fact, and no §7 arm names the case.

**Why it bites.** Unit 62's Migration measured 25 records naming neither branch fact, LANDING among
them. For those, the re-bind stages the record from any worktree, including a re-run's pre-preflight
tick, which is G8 M5's harm. The not-scoped announcement can be dropped with every criterion green.

**Fix.** State the neither-fact exception in S8. Add an AC23 arm: a pushed, unobserved LANDING record
carrying neither branch fact, resumed with an id from another branch, re-binds and prints the
not-scoped announcement. Have 62's four passages cite the exception.

**Left-shift.** Every sentence that makes an exception to an S-item's absolute is echoed in that
S-item and named in a criterion. A documented check: grep a folded spec for "as before" and "except",
and resolve each hit to an S-item and an AC.

### L4 — driver refusal texts still name the deleted LEASE line and a refresh that no longer happens (19, 24)

**Address.** Spec 61 §2 S1, the deletion of `verb_status`'s `LEASE —` line; §2 S11 and S13; §4's
matrix row "working, clock fresh or unknown, no id"; §6 AC13.

**What is wrong.** At `tools/unattended/unattended.sh:5826` the no-id `fail 59` tells a refused
session to pass "the keepalive the LEASE line names". S1 deletes that line from `--status`, and S11
drops the Skill's LEASE-line rule. The HELD refusal at `:5794` still says the lease names "when it
was last refreshed", and 61 §4 says nothing refreshes the lease any more. §4's row pins no text, S11's
carrier list reaches the usage line and the "its four" comments but no refusal text, and AC13 greps
only carriers. Unit 63 rules refusal texts out as a non-goal.

**Why it bites.** After the pass, an agent refused at check 59 is pointed at a line `--status` no
longer prints. Finding 24 also claimed that rewording the text would red the arm at
`tools/unattended/unattended.test.sh:7200` with no remedy. That overstates it. Updating an expected
string in an existing arm is permitted, and the build has to rewrite other hit texts anyway, such as
`:5839`'s presumed-stopped text, which reads the deleted `LEASE_REFRESHED`.

**Fix.** Quote the replacement texts for `:5826` and `:5794` in §4, naming the record's `keepalive`
fact. Name the arm at `unattended.test.sh:7200` in S13 for a one-for-one retarget. Add `grep -c 'LEASE
line names' tools/unattended/unattended.sh` to AC13's zero-counts.

**Left-shift.** When a spec deletes an output line, grep the driver for every string that names it,
refusal texts included, and list each in the spec. The grep is cheap enough to be an AC13-style
witness itself.

### L5 — F11 still says order 30 (28)

**Address.** Spec 61 §8 F11, the rev-3 M9 fold text, against the status header and §9 rev-4.

**What is wrong.** F11 says "The status header's order 30 is also TOOL-dDerivedDocket-32's … This spec
does not move its own order". The header reads order 31, and rev-4 records the re-declaration from 30
to 31, alone. Unit 32's header is still order 30.

**Why it bites.** A live §8 entry states a false fact about the spec's own header. A reader checking
BUILD-METHOD M6 condition 3 from F11 would conclude that unit 61 still shares a step with unit 32.

**Fix.** Reword F11 to say the orchestrator re-declared this unit to order 31, alone, at rev-4, which
answers G8 M9, and drop the order-30 sentence.

**Left-shift.** A header-only revision greps its own spec for the old value before it is committed.
The header's order is a derived fact, so no passage in the body should restate it.

## Fold order

1. Fold H1 first, and before 61's Rollout records the session. Keep the resume tick unregistered on
   node `d` until the term or the stated rule has landed. If route (a) goes into unit 64, fold M6 in
   the same edit, because both change 64's fixtures and edges.
2. Fold M1, M2 and M4 together in spec 62, since all three edit S4 or §4's chain and add arms to AC1
   to AC4.
3. Fold M5 in specs 61 and 62 in one commit, so the arm has one owner at every revision.
4. Fold M7, L1 and L4 into one AC13 edit in spec 61. Fold M8 in spec 61 and in unit 27's next
   revision together.
5. Fold M3 in spec 63. Then fold L2, L3 and L5 in spec 61.

After the fold, re-review the fold text itself rather than trusting it. Every confirmed finding
against 61 in this round lands in text its own rev-3 to rev-6 folds wrote or left stale, which is the
pattern this repo's memory records from earlier round-2 audits.

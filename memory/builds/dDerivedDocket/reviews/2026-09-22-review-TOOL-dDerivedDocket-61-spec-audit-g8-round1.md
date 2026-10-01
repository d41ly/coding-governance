**Serves:** spec-audit TOOL-dDerivedDocket-61 TOOL-dDerivedDocket-27

# dDerivedDocket — spec audit of G8, unit 61's lease reconciliation and unit 27's rev-8 withdrawal, round 1

*Node `d`, 2026-09-22. This is the first Tier-2 adversarial pass over `TOOL-dDerivedDocket-61`, a NEW
and wholly unreviewed spec. It also covers the rev-8 amendment of `TOOL-dDerivedDocket-27`, which
withdraws that unit's S11 and AC9 in 61's favour.

Unit 61 exists because this build merged origin/main (`663a0dec`, 469 commits) at `c23d5701`, and
the merge kept two lease models side by side in the unattended kit. OURS is HELD: a per-slug lease
file under the git common dir, with a take-over matrix and `LEASE_STALE_AFTER` (unit 4), a scheduled
restart from HELD (unit 5), in-place landing (units 2 and 3) and LANDED derived from the advertised
tip (unit 22). THEIRS is the lease facts in the run-state file, a `--liveness` verdict, an OS resume
tick and a stop-guard, all from origin/main's aWokenSentinel build.

Code claims below are judged at HEAD `3eec5dee`, the merged tree, and never at the spec's own base
`285701d5`. The code read was `tools/unattended/unattended.sh`, `lib-unattended.sh`,
`check-unattended.sh`, `stop-guard.js` and `resume-tick.sh`, plus the protocol, verbs, stops and
Skill templates. Every sibling spec a subject names in an edge was read, because contradiction
BETWEEN specs is in scope. That meant above all units 4 and 5, whose designs 61 re-keys, and units 27
and 28, which build before it and touch the same driver.

Four primed finder lenses ran and all four returned. A skeptic stage prompted to REFUTE each finding
ran in five batches and all five returned. Then came this synthesis, which re-read the load-bearing
sites at HEAD before writing each entry and names those sites in the entry.*

**Round: 1.** Range at HEAD `3eec5dee`, each subject pinned at the blob it was read at:

- `memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-61.md@ba37390520e053edc6369b48419a5685bf2149e8`
- `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md@d2858cb57dcfc447af75e69c5956db32d0784ad1`

## Verdict: BLOCKED

The review found one blocker, two highs and nine mediums: twelve adjudicated items carried by
nineteen raw confirmed findings. Unit 61 must not build until B1 is designed.

B1 is the reason for the verdict. Unit 4 put the lease under the git COMMON dir so that every
worktree on the node sees the same one. Unit 61 moves it into the run-state file. A tracked file is
one COPY PER WORKTREE, and each copy is graded on its own worktree's clocks. The resume tick already
walks every worktree and acts on each copy separately. Six unit worktrees on this node carry this
build's record today, and the Rollout is the step that gives those copies a session to relaunch.

As specified, the tick can therefore kill and relaunch a HELD or live run from any stale sibling
copy. That defeats the unit's own title property. It would also put this build's orchestrator in the
kill path at the moment the unit lands. The fix needs a per-slug answer across worktrees, which no
spec in the set carries, and it needs a choice between two routes. That choice is the orchestrator's
act under the delegated M3 rule, as F1 was, so no owner turn is needed. It still has to be made
before the pass.

H1 and H2 each stop the unit passing, or stop it delivering what it claims.

- H1: the new same-session matrix row shadows `--replaces`, so the holder can no longer replace its
  own job. Three existing arms flip, because the suite exports one session for every call.
- H2: F1 was decided on a premise the runner contradicts. The turnstile queue writes no gate log, so
  the property unit 27 handed over is not delivered for a queued bar.

M1 is the other half of H2: unit 27's withdrawal text claims a transfer that did not happen.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero count below
is evidence and not an artefact of a missing lens. That includes the statement that no confirmed
finding names a criterion already green at HEAD before the unit acts.

Some raw ids describe one defect each from several addresses, and they are merged:

- 2, 17 and 37 into B1;
- 16, 30 and 41 into H1;
- 1, 18 and 31 into H2;
- 3 and 19 into M1.

The pipeline's duplicate count of 0 comes from its own exact-match dedupe, which does not see a
restatement.

## Review shape

Raw 45, confirmed 19, refuted 26, unverified 0. Precision 0.42, which is below the ~0.5 floor that
charter §8 sets.

The shortfall is concentration, not scatter. Eleven of the nineteen confirmed findings land on three
mechanisms: the lease's per-worktree reach, the matrix row order and the queued-bar clock. The lenses
found each of those two or three times over, from different addresses. The 26 refuted findings are
not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---:|---:|
| BLOCKER | 1 | 3 |
| HIGH | 2 | 6 |
| MEDIUM | 9 | 10 |
| LOW | 0 | 0 |
| Total | 12 | 19 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 to G7
reports used, so the groups' counts compare.

- BLOCKER means that, as specified, the unit cannot reach the outcome it names, and the set needs a
  decision or a mechanism no spec in it carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  property as delivered while it is not, where the reachable harm is a kill or a double drive.
- MEDIUM covers a contradiction with a bounded consequence, a declaration a spec owes, and a rule
  whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, three calls move.

- Findings 2, 17 and 37 came in HIGH and are adjudicated BLOCKER at B1. The fix needs a mechanism
  the set does not carry, and the harm lands on this build's own run at its Rollout.
- Finding 41 came in MEDIUM and is absorbed into H1, taking that item's HIGH. One row fix closes it
  along with 16 and 30.
- Findings 3 and 19 stay MEDIUM at M1. They are the 27-side text of the H2 defect, and correcting
  that text harms nothing further once H2 is fixed.

## The brief's questions, answered

- **Does 61 keep every property the matrix, HELD and the scheduled restart had?** No. It loses four:
  - the one-record-per-slug reach across worktrees (B1);
  - `--replaces` as the holder's own path (H1);
  - bar-long freshness for a queued bar (H2);
  - unit 4 F8's build-folder-scoped clock for a leaseless record (M3).

  The UNKNOWN announcement survives in text only, with no criterion (M4). HELD's carve-outs and the
  tick's HELD skip are designed soundly, but only for the run worktree's own copy.
- **Can an out-of-session actor still kill, relaunch or refuse a HELD run?** Yes. The tick can kill
  and relaunch one through a stale BUILDING copy in a sibling worktree, and the matrix can be
  reached from that copy too (B1).
- **Does the retired lease file have a migration, this build's own run included?** The file
  population is correctly measured empty: `<common-dir>/unattended` does not exist on node `d`. The
  gap is the build's own run. Live state contradicts the Rollout's matching-id premise (M2), and the
  Rollout is what arms the tick against the six wave-worktree copies (B1).
- **Does the pushed-landing re-bind work under both landing modes?** Partly. AC8 exercises both
  modes at the `read_landing_commit` site, and no confirmed finding shows the re-bind failing
  outright in either one. Three gaps remain:
  - the `check_clean` half has no criterion (M7);
  - under in-place, a pre-preflight tick re-binds a previous run's record and blocks the next
    `--preflight` (M5);
  - AC10's single-worktree fixture cannot observe whether the landed log is in the common dir (M6).
- **Does every criterion fail when its property breaks?** Not yet. AC20 stays green for a silent
  bar (H2), and M4, M6, M7 and M8 name criteria that cannot see the break they claim. No confirmed
  finding names a criterion that is green at HEAD before the unit acts, and the run is complete.
- **Did the 27 withdrawal leave a half standing?** Yes, in its text. S11's code half is cleanly
  withdrawn and the pinned `gate-backstop` fact correctly stays. But AC9's withdrawal and the §3
  non-goal claim that AC20 observes the whole property, and it does not (M1).

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---:|---|
| 2 | BLOCKER | B1 | 61 | §2 S3, S7; §4 Rollout; §6 AC20 |
| 17 | BLOCKER | B1 | 61 | §4 The one lease record; HELD in the three actors; Rollout |
| 37 | BLOCKER | B1 | 61 | §4 The one lease record; Rollout; Migration; §2 S7 |
| 16 | HIGH | H1 | 61 | §4 matrix, the same-session row above the `--replaces` row |
| 30 | HIGH | H1 | 61 | §4 matrix; §2 S7, S13; §7 driver arm line |
| 41 | HIGH | H1 | 61 | §4 matrix same-session row; The relaunched session; §2 S7 |
| 1 | HIGH | H2 | 61 | §8 F1; §6 AC20; §5 risks |
| 18 | HIGH | H2 | 61 | §8 F1; §5 risk (2); §6 AC20; §4 The one lease record |
| 31 | HIGH | H2 | 61 | §8 F1; §6 AC20; §5 risk (2) |
| 3 | MEDIUM | M1 | 27 | §6 AC9 withdrawn; §3 non-goal The lease's stale bound |
| 19 | MEDIUM | M1 | 27 | §3 non-goal; §6 AC9 withdrawn; against §1 and §2 S4 |
| 33 | MEDIUM | M2 | 61 | §4 Migration and Rollout; §8 F9 |
| 39 | MEDIUM | M3 | 61 | §4 matrix, the leaseless-rows collapse paragraph |
| 5 | MEDIUM | M4 | 61 | §2 S3; §4 matrix rows "fresh or unknown"; §5 error states |
| 23 | MEDIUM | M5 | 61 | §4 Where the text goes, the Skill tick paragraph; §6 AC13 |
| 7 | MEDIUM | M6 | 61 | §2 S10; §6 AC10 |
| 9 | MEDIUM | M7 | 61 | §2 S8; §6 AC8 |
| 8 | MEDIUM | M8 | 61 | §2 S11; §6 AC13 |
| 20 | MEDIUM | M9 | 61 | status header order 30; §8 F11 |

Spec paths below are abbreviated to their unit number. "Spec 61" is
`memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-61.md` and "spec 27" is
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md`. Each was read at the
blob pinned in the range line above. Sibling specs are named in full at first mention.

## Blockers

### B1 — the lease left the common dir and became one copy per worktree, so the tick and the matrix grade one slug many times (2, 17, 37)

**Address.** Spec 61 §4 "The one lease record", "HELD in the three actors", "Migration" and
"Rollout"; §2 S3 and S7; §6 AC4, AC7 and AC20, all of them single-worktree. Against
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-4.md` §4 "The lease" and KF7,
and against spec 61's consumes-from edge to `TOOL-dDerivedDocket-28`.

**What is wrong.** Unit 4 §4 put the lease file under the git common dir, "so every worktree on the
node sees the same one". Spec 61 makes the lease each worktree's own copy of the run-state file.
Every clock `derive_last_move` reads belongs to the CALLING worktree:

- HEAD's committer epoch and the newest dirty or untracked path, from `read_tree_clocks`;
- the newest file under that worktree's own `<git-dir>/gate-logs/` (`unattended.sh:5555`, derived
  from the per-worktree sidecar dir);
- a transcript path encoded from that worktree's own root (`resolve_transcript_path`, `:5463`).

`tools/unattended/resume-tick.sh` walks every worktree from `git worktree list` and reads each
worktree's index copy of the record. It grades each copy separately, with no per-slug join. On STALE
it kills the recorded pid's tree and launches `claude -p --resume <session>` with
`--dangerously-skip-permissions` in that worktree (header `:13-14`, and the kill in `run_kill_tree`
at `:163`). Its IN-FLIGHT and attempt state sits in a per-worktree resume log, so nothing dedupes
launches across copies.

Spec 61 does argue the multi-worktree walk, but only for the landed log. F5 rejects option (b)
because it is "invisible to the other worktrees the tick walks". The spec never makes the same
argument for the lease it moves out of the common dir.

Measured at HEAD on node `d`, 2026-09-22: `git worktree list` holds six `wf_*` unit worktrees. The
three sampled each carry a committed `memory/builds/dDerivedDocket/RUN.md` at phase `BUILDING` with
keepalive `00c7d786`. Today the record carries no `session` fact, so the tick skips every copy. The
Rollout records `session` and `pid` on the run branch. Every wave worktree branched after that
records commit inherits them. Concurrent waves are the owner's ruling of 2026-09-21, so such
worktrees are the normal population, not an accident.

**Why it bites, concretely.**

- The HELD carve-out holds only for the run worktree's own copy. Suppose the run is held in its own
  worktree while a lingering unit worktree still carries a BUILDING copy. That copy reads STALE on
  its own idle clocks: units run no gates, and the orchestrator's transcript does not resolve under
  that worktree's path encoding. The tick then kills the recorded pid's tree, which is the
  orchestrator, and relaunches the recorded session in the unit worktree. That session's `--resume`
  takes the new same-session row and drives the run from a stale copy. A live orchestrator waiting
  on a wave meets the same kill.
- The cross-worktree refusal is gone. Unit 27's pre-withdrawal AC9 (at `8f354565`) ran its
  `--status` and `--resume` "from a second WORKTREE, not a second clone, because the lease lives
  under the git common dir". Under spec 61, a `--resume` from a sibling worktree is judged on that
  worktree's clocks. A session there can take the slug over while the holder is live elsewhere, which
  is the double drive KF7 exists to stop.
- Unit 28's prune-race argument for its common-dir ledger rests on each of the four reaping verbs
  holding "the slug's lease". With one copy per worktree there is no single holder. Spec 61's edge to
  unit 28 says only that it "keeps each reap on the re-keyed row that holds the lease", and it never
  examines the race.
- Every criterion runs in one worktree, so the whole suite stays green over the hazard.

**Fix.** Add an S-item under which `--liveness`, the tick and the matrix give ONE answer per slug
across worktrees. There are two routes.

- Route (a), the smaller: act only in the worktree whose checked-out branch equals the record's
  `branch-ref` fact. The run-state file already carries that fact; this build's record names
  `refs/heads/branch/backlog-maintenance-mechanics-10588f`. Every other copy then reads a named
  non-holder verdict. The tick prints a named skip and kills nothing, and the matrix refuses with a
  numbered message naming the run's branch. This route also closes M5's pre-preflight re-bind.
- Route (b): `derive_last_move` takes the newest move across every worktree whose index names the
  same slug and session.

Then name the wave-worktree population in §4 Migration and Rollout. In the edge to unit 28, state
what its ledger race argument rests on now.

Add two-worktree arms to AC4 and AC7, and one new criterion. Its fixture is a linked worktree whose
HEAD carries an aged copy of a bound record, with a fresh gate log planted in the run worktree only.
There:

- `resume-tick.sh --dry-run` prints the named skip, and no `resumed` decision for either copy;
- `--resume --keepalive-id C` from the second worktree refuses;
- with a HELD record in one worktree and a stale working copy in the other, the tick kills nothing.

**Left-shift.** Make a linked worktree part of the tick suite's standing fixture. Every future tick
arm then runs over two copies of one record, and a per-copy grading cannot pass unseen. Also record
the class as a gotcha, so that `gotchas.py --for-diff` serves it to the next review of this kit. The
class: state moved from the git common dir into a tracked file becomes one copy per worktree, and
every actor that walks worktrees must join on the slug.

## High

### H1 — the same-session row shadows `--replaces`, so the holder can no longer replace its own job (16, 30, 41)

**Address.** Spec 61 §4 "The resume matrix, re-keyed", the rows at `:199` and `:200`; §4 "The
relaunched session"; §2 S7 and S13; §7's driver arm line; §8 F4. Against §3's consumes-from edge to
unit 4 ("keeps every row's property") and unit 4's F3 and F9.

**What is wrong.** The matrix is evaluated in order, and its first match wins. The row "working | a
new id, the recorded session, which is not `absent`" sits above the row "working, clock fresh | a
new id with `--replaces` naming the recorded keepalive". The first row's caller cell does not exclude
`--replaces`.

The holder's own `--resume --keepalive-id <new> --replaces <old>` always carries the recorded
session, because `write_lease` (`unattended.sh:5121`) records the holder's own
`CLAUDE_CODE_SESSION_ID`. Three consequences follow.

- The holder's own replacement goes through `run_takeover`. That costs a remote observation, a
  mandate re-verify, interrupted-act naming and a resume history row. It prints `lease replaced`
  (`:5642`), never `keepalive replaced` (`:5808`). The Skill says "Replace your OWN job only through
  `--replaces`", and that instruction now routes the holder into a take-over.
- A holder's `--replaces` naming an id it does not hold is taken over instead of refused at 58.
- The row also admits a recorded pid that is ALIVE and equal to `CLAUDE_PID`. That is the live
  holder itself, not a restart. The aWokenSentinel research §3.3 measured that a sub-agent sees its
  PARENT's session id, and unit 4 F3 rejected any identity readable by any session. So a holder's
  sub-agent that runs `--resume` with a fresh id takes the run over with no freshness test. The
  `keepalive` fact then names a job the holder's scheduler does not list, and check 53 grades the
  wrong id.

The `--replaces` row stays reachable only by a DIFFERENT session naming the recorded id. That is the
reverse of what F4's rejection of option (b) says `--replaces` means.

**Why it bites, concretely.** The unit cannot pass as written. `unattended.test.sh:409-410` exports
`CLAUDE_CODE_SESSION_ID=fixture-session` and `CLAUDE_PID=999999999`, a dead pid, for every `run()`,
and `build_hold_fixture`'s `--preflight` records exactly those. So every second-driver call in the
suite IS the recorded session, and the existing arms flip:

- unit 4's AC6 second-driver refusal (`:7180-7183`) becomes a take-over;
- unit 4's AC20 arm at `:7235-7237` expects `keepalive replaced` and gets `lease replaced`;
- the foreign `--replaces kX` refusal at `:7246-7249` takes the slug over where it expects "wrote
  nothing";
- unit 4's AC22 second-session arm flips the same way.

These are output and record assertions, not lease-file ones. S13's retarget covers only lease-file
assertions, so it does not reach them, and AC15 reds on "an existing arm newly fails".

**Fix.** One row change closes all three findings.

- Evaluate a call carrying `--replaces` BEFORE the same-session row, whatever its session. If it
  names the recorded keepalive, it runs `write_lease` and prints `keepalive replaced`. If it names
  another id, it refuses at 58 and leaves the file byte-unchanged.
- Limit the same-session row to a recorded pid that is NOT alive, which is the only case "the
  holder's process restarted" needs. A live recorded pid equal to `CLAUDE_PID` with a new id refuses
  at 58 and names `--replaces`, which is unit 4 F9's path.
- Cite F3, F9 and the sub-agent measurement in F4.
- State in S13 that every second-driver arm sets a distinct `CLAUDE_CODE_SESSION_ID`.
- Add three arms. The recorded session with `--replaces` naming the recorded keepalive prints
  `keepalive replaced` and runs no take-over. With `--replaces` naming another id, it refuses at 58
  and writes nothing. A live-and-equal pid with a new id refuses at 58.

**Left-shift.** Add a documented spec-audit check for every first-match table: for each row, name
every row above it whose caller cell also matches that row's callers. Once executed, the three new
arms are the regression gate for this class in this matrix.

### H2 — the turnstile queue writes no gate log, so F1's premise is false and a healthy queued bar reads STALE (1, 18, 31)

**Address.** Spec 61 §8 F1; §5 risk (2); §6 AC20; §4 "The one lease record", second paragraph.

**What is wrong.** F1 declines option (c) because "the gate-log term already moves while a bar
runs", and it says AC20 now delivers the property unit 27's AC9 guarded. §4 says every refresh the
retired file took "moves a signal `--liveness` already reads". That includes the refresh at
`run_bounded`'s start. The runner at HEAD contradicts both claims.

- A leg log is written only when a leg finishes (`tools/run-gates/run-gates.sh:1738-1742`).
- The turnstile's tickets, beacon and heartbeat live under the git COMMON dir (`:806-813`, with
  `ts_hb` at `:647`). They are not under the per-worktree `gate-logs` that `print_liveness` reads.
- Every gov profile row sets `timeout=0`, and `GATE_TURNSTILE_TTL` is set nowhere. So `TS_TTL=1800`
  and `TS_MAXWAIT = TS_TTL * 4 = 7200` s (`:632-638`). That is above gov's
  `RESUME_STALE_BOUND="5400"` (`.unattended.conf:74`).
- The driver's own derivation of that bound (`unattended.sh:536-545`) assumes a healthy bar is at
  most `GATE_BOUND` of silence. Unit 27 S4, at order 28 before this unit, retires that assumption. It
  bounds `gates-green` at wall + queue + margin, about eight hours in gov, precisely because the
  queue alone may wait 7200 s.

**Why it bites, concretely.** Once units 27 and 61 have both landed, consider a close queued for 5400
to 7200 s behind another worktree's bar. It moves none of the four signals, so it reads STALE. The
tick kills it and relaunches it. That brings back, through the tick, the contention kill unit 27's
goal exists to remove. New with this unit, another session's `--resume --keepalive-id` can also take
the slug over mid-queue.

Two earlier bounds covered this window. One was unit 27's withdrawn S11. The other was the retired
`max(GATE_BOUND, LEASE_STALE_AFTER)` of 7200 s, over a clock refreshed at `run_bounded`'s start.

No criterion can see the gap. The old AC9 scenario, a stub bar that sleeps and writes nothing, has no
arm. AC20 plants a fresh gate log inside the bound, so it is green. §5 risk (2) names one long leg
only, and the word "queue" appears nowhere in spec 61.

**Fix.** Re-open F1 on the corrected premise, as the orchestrator's delegated act, and take one of
two routes.

- Close the gap within option (a): give `derive_last_move` a signal the queued runner moves. That
  signal can be a per-worktree trace the waiter touches each tick, or the mtime of this worktree's
  own turnstile ticket under the common dir. Add an AC20 arm with every other signal aged past the
  bound and that signal fresh, which must read `stale: no`.
- Or state the residual truthfully in F1, in §5 risk (2), and in unit 27's AC9 and §3 (M1). The
  residual is a queue wait of up to `TS_MAXWAIT`, plus any leg whose ceiling exceeds the bound. Say
  plainly that the tick kills a close queued past 5400 s.

Whichever route is taken, add an AC20 arm over the old AC9 fixture: a stub gate that sleeps past
`RESUME_STALE_BOUND` and writes no `gate-logs` file, with its expected verdict stated.

**Left-shift.** The driver already prices a stale bound set too low: the NOTE at `unattended.sh:545`
fires when `RESUME_STALE_BOUND` is below `GATE_BOUND + UNIT_STALL_BOUND`. Once unit 27 S4 bounds the
bar by the backstop, that comparison's left term measures the wrong silence. Make it the pinned
backstop, so that a bound shorter than the bar's real worst-case silence announces itself on every
run. Also record the runner fact as a gotcha: a gate log is written at leg completion and never
during the turnstile wait, so a clock built on gate logs goes dark while a bar queues.

## Medium

### M1 — unit 27's withdrawal says AC20 observes AC9's property whole, and the silent-bar and second-worktree halves are left standing (3, 19)

**Address.** Spec 27 §6 AC9 (`:324-331`), §3 non-goal "The lease's stale bound" (`:102-105`), and
the §9 rev-8 entry (`:577-586`). Against spec 27 §1 and §2 S4.

**What is wrong.** The withdrawal says the property "that a bar running past the bound never reads
stale and a second session cannot take the slug over mid-bar, is observed by that unit's AC20".

The pre-withdrawal AC9, read at `8f354565`, staged a stub bar that sleeps past `GATE_BOUND` and
`LEASE_STALE_AFTER`, stays inside the backstop and writes nothing. It read `--status` and `--resume`
from a second worktree. AC20 plants a gate log in one worktree. Both halves of the old fixture are
therefore unobserved. Under spec 61 the silent bar reads STALE (H2), and the second worktree is
graded on its own clocks (B1). Spec 27's own S4 bounds the bar at wall + queue + margin, and during
the queue stretch the gate-log term cannot move.

The rest of the withdrawal is clean. S11's code half is gone, and the pinned `gate-backstop` fact
correctly stays. Rev-8's sentence that KF7's `max(backstop, declared bound)` is no longer delivered
here is true.

**Fix.** Reword AC9, the §3 non-goal and the rev-8 entry to say what unit 61 actually carries: legs
landing in the run's own worktree. Name the silent or queued bar and the second-worktree halves as
undelivered. Alternatively, cite the unit 61 criterion that observes each half, once H2 and B1 add
one. Fold this together with H2 and B1, so the two specs say the same thing.

**Left-shift.** Add a documented spec-audit check: a withdrawal that transfers a property to another
unit quotes the receiving criterion's fixture beside the withdrawn one. The check compares the
FIXTURES, not the property names.

### M2 — the Rollout relies on a keepalive match that live state contradicts (33)

**Address.** Spec 61 §4 Rollout (`:361-366`) and Migration (`:351-359`); §8 F9.

**What is wrong.** The Rollout assumes that the orchestrator's first `--resume <slug> --keepalive-id
<own id>` after the merge is a matching-id resume, which takes the holder row.

At HEAD, `memory/builds/dDerivedDocket/RUN.md` records `keepalive: 00c7d786`, with no `session`,
`pid` or `lease-utc`. That fact was written once, at the 2026-09-14 preflight `e7da7bf5`. The run's
live keepalive is `b5b0b444`, read from the scheduler listing at the time of writing. No
`<common-dir>/unattended` directory exists either. That fits the inference that no matching-id
resume has run on the lease-file driver since `315eb4bb`. So the match has never been exercised, and
§10 never checked it.

**Why it bites.** Under the re-keyed matrix the orchestrator's call falls in the row "working, clock
fresh, a new id, another session". The same-session row does not apply, because it requires a
recorded session and this record has none. The call therefore refuses at 58, on a clock the
orchestrator's own commits keep fresh. The Skill's Resume section tells a refused taker to reap the
job it just scheduled and stop. So the build's own run stops at the moment this unit lands. The one
way through, `--replaces 00c7d786`, is named nowhere in the Rollout.

**Fix.** Make the Rollout compare the scheduler listing with the recorded keepalive before relying on
the holder row. When they differ, prescribe `--resume <slug> --keepalive-id <live id> --replaces
00c7d786`, which H1's fix leaves reachable. Record the measurement in §10. Add an arm: a pre-lease
record resumed with a non-matching id on a fresh clock refuses with a message that names
`--replaces`.

**Left-shift.** Add a documented check: a Rollout premise about live run state is measured at spec
time, and its reading is recorded in §10 with date and node. §4 Migration already does this for the
file population.

### M3 — collapsing the leaseless rows silently supersedes unit 4's F8 clock (39)

**Address.** Spec 61 §4 "The resume matrix, re-keyed", the paragraph beginning "The four leaseless
rows of the retired matrix collapse" (`:206-209`). Against unit 4 §8 F8, and against the still-open
backlog row at `memory/backlog/TOOL.md:322`, which unit 4's revision log names as F8's source.

**What is wrong.** Unit 4's F8, option (a), judged a leaseless working record presumed-stopped by the
age of the newest commit touching its build folder, "never a refusal outside the bound". Spec 61's
clock is `read_tree_clocks` (`unattended.sh:5347-5360`) plus the gate logs and the transcript. That
means HEAD's committer epoch and the newest dirty path of the CALLING worktree, and none of it is
scoped to the run. S1 deletes `build_folder_age`. Spec 61 cites neither F8 nor the backlog row.

**Why it bites.** Take an abandoned leaseless working record whose session is absent, which is the
backlog row's population. Two such builds, aClosedDocket and aUnblockedFleet, are verified still
BUILDING and leaseless. Resumed from any active worktree, such a record meets the row "working, clock
fresh or unknown, a new id, another session". That row refuses at 58 with "a live session drives
this slug". The claim is false, and the refusal holds for as long as unrelated commits, writes or
gate runs keep that worktree inside 5400 s. `--liveness` itself grades the same record UNBOUND. A
dead leased holder is widened the same way, because the holder is no longer the only thing that
moves its clock.

**Fix.** Choose one of two:

- keep F8's scoping, so the commit term of the clock the matrix acts on is the newest commit
  touching the record's build folder;
- or record a §8 fork that supersedes F8, cites the backlog row and names the regression.

Add a criterion: an old leaseless record in a worktree with a fresh unrelated commit still reads
`presumed-stopped`. A slug-scoped clock would also narrow B1's exposure.

**Left-shift.** Add a documented check for re-keying specs: every row the re-key collapses cites the
consumed unit's fork that decided it, so a superseded decision is superseded in writing.

### M4 — the UNKNOWN clock S3 keeps has no criterion (5)

**Address.** Spec 61 §2 S3; §4 matrix rows "clock fresh or unknown"; §5 error / empty / loading
states; §6 AC3, AC4 and AC20.

**What is wrong.** S3 keeps `check_lease_fresh`'s return 2, UNKNOWN. The matrix and §5 treat a dead
probe as fresh, which declines a take-over. S3 says AC4, AC5 and AC20 observe it, but all three run
live clocks and none reaches return 2.

The only existing dead-probe arm on the resume path is at `unattended.test.sh:7424-7427`, which
expects fail 57 through `build_folder_age`. S1 deletes that function and its message, and the spec
states no retargeted expectation.

**Why it bites.** Suppose an implementation maps a dead `derive_last_move` to stale, or drops the
announcement. A dead probe then becomes an invitation to take over a live run, and every stated
criterion still passes. That is the reassuring-zero class, the one charter §7 requires a probe to
announce.

**Fix.** Add a criterion over AC3's fixture with a PATH-shadowed `date` that exits 1. In it:

- `--resume --keepalive-id C` from session `T` prints the UNKNOWN announcement, refuses at 58 and
  leaves the file byte-unchanged;
- a no-id resume refuses at 59;
- `--status` prints the UNKNOWN line and no `presumed-stopped`.

Name the arm as the retarget of the leaseless dead-clock arm.

**Left-shift.** The `harness arms` leg grades `fail` branches only, so a tri-state probe's non-fail
third state is ungraded by construction. Add a documented check: every tri-state return keeps one arm
per state.

### M5 — the Skill's new tick text is wrong under in-place, and a pre-preflight re-bind blocks the next preflight (23)

**Address.** Spec 61 §4 "Where the text goes", the Skill tick paragraph (`:316-322`); §6 AC13.
Against §4's re-bind and observed-landing matrix rows, and §5 risk (4).

**What is wrong.** The new text says a tick issued before `--preflight` refuses at its first act. It
names check 10 there, or check 26 "on a re-run build whose previous record is terminal", and AC13
requires `check 51` to be gone from the Skill.

Gov declares `LANDER_MODE="in-place"` (`.unattended.conf:23`). Under in-place, a landed record stays
recorded LANDING until the next `--preflight` retires it (`unattended.sh:4008-4016`).
`refuse_if_terminal --recorded` reads LANDING as non-terminal (`:2458-2471`). So check 26 never
fires for a re-run build's previous in-place record. Two cases follow.

- Observed landing: `--resume` prints nothing to resume and exits 0. The tick's second act,
  `--audit`, then refuses at fail 51, "already finished" (`:5392-5393`). The check-51 note is
  therefore still true, and AC13 forces it out.
- Unobserved landing: the re-bind row writes and stages the previous run's record with no identity
  test. That leaves the lease-only staged difference which §5 risk (4) says the next `--preflight`
  refuses at check 2. A re-run build's own preflight is then blocked by its keepalive's first tick.

**Fix.** Keep a check-51 sentence for an in-place previous record, and drop that grep from AC13. Skip
the re-bind row when the record's `branch-ref` is not the checked-out branch, which B1's route (a)
already supplies. Add an arm: a pre-preflight tick over an unobserved in-place landing writes
nothing.

**Left-shift.** Add a documented check: a zero-count grep that deletes a sentence from a carrier is
paired with an arm showing that the sentence's claim is now false.

### M6 — AC10's single-worktree fixture cannot tell the chosen common-dir log from the rejected per-worktree one (7)

**Address.** Spec 61 §2 S10; §4 "The read-back under in-place, and the observation"; §6 AC10; §8 F5.

**What is wrong.** AC10 runs on AC9's fixture, which is AC8's, and that fixture is the main worktree
of one scratch repository. There, `git rev-parse --git-dir` and `--git-common-dir` both answer
`.git`. A log written through `resolve_sidecar_dir` (`lib-unattended.sh:63`, per-worktree) therefore
passes AC10. Check 32 counts only the `rev-parse --git-dir` literal, and its header says it cannot
see this spelling (`check-unattended.sh:4938`). So reusing the per-worktree helper adds no count
either.

**Why it bites.** F5 chose the common dir precisely because a per-worktree log is invisible to the
other worktrees the tick walks, and AC10's own Red-when names that case. With a per-worktree log,
`--liveness`, `--status` and the tick in any other worktree whose HEAD carries the landing would
still read FINISHED-UNSTAMPED. The stop-guard would block and the tick would relaunch. That is the
measured defect S10 exists to fix.

**Fix.** Run AC10's in-place `--landed` in a linked worktree of the fixture. Read `--liveness`,
`--status` and the stop-guard from a second worktree checked out at the landing commit. Assert that
the log's path equals `$(git rev-parse --git-common-dir)/unattended/landed.<slug>.log`, and that no
file of that name exists under the linked worktree's own git dir.

**Left-shift.** Add a documented check, with a fixture helper beside it: any criterion whose property
is visibility across worktrees runs in a LINKED worktree. A main-worktree fixture collapses the two
directories into one.

### M7 — S8's `check_clean` half has no negative criterion (9)

**Address.** Spec 61 §2 S8; §4 "The pushed landing, re-bound, and the tolerance it needs"; §6 AC8;
§5 risk (4).

**What is wrong.** AC8's witness-edit control expects `not committed as it stands`. That text is
`DP_REASON` from `read_derived_phase` through `read_landing_commit` (`unattended.sh:1111`, suite
`:8926`), so the control observes the `read_landing_commit` site only.

The primary `--landed` branch, from `:4028`, calls `check_clean` and does not re-read the landing
commit before its terminal write. The other callers of `check_clean` (`:4545`, `:4785`) must stay
unexempted, and §5 risk (4) relies on that for `--preflight`. AC8's Red-when claims both sites.

**Why it bites.** Two simplifications pass AC8:

- a `check_clean` that exempts the whole run-state file, which lets a hand-edited witness or phase
  reach primary `--landed`'s terminal write;
- the exemption applied in every caller, which lets `--hold` and `--preflight` accept a dirty tree.

**Fix.** Add to AC8: under `primary`, the witness-edited fixture refuses at check 2. On the re-bound
fixture, `--preflight`, and `--hold` on a working copy, still refuse at check 2.

**Left-shift.** Add a documented check: a tolerance threaded through a shared predicate by an
optional argument is graded at every call site, once where it must hold and once where it must not.

### M8 — AC13 witnesses a fraction of S11's carrier edits (8)

**Address.** Spec 61 §2 S11; §6 AC13; §6 AC14.

**What is wrong.** The stop contract gets one witness, `per-slug`, and in
`tools/unattended/STOPS.template.md` that string occurs once, in the title. Nothing observes the
rest:

- in the stop contract: §4 item 3, "the lease's id when there is one" (`:84`); the §7 body; the §8
  table's "refreshes the lease" and "released … landed" (`:189-195`); §9 step 5; and §12's "keeps
  what it saw in the lease" (`:415`);
- the verb carrier's `--liveness` entry gaining HELD;
- the protocol's "refreshing the lease" (`:388`) and its hold clause at `:408`;
- the dossier's three lease sentences in `memory/map/features/unattended.md` (`:84`, `:91`, `:102`);
- the driver's `--resume` header, and the two "its four" comments. Those comments have no stated
  target: the driver makes seven `read_bound_key` calls at HEAD, and unit 27 adds `GATE_WALL`.

AC14 reads sizes only, and an unedited carrier passes it.

**Why it bites.** A pass that edits only the witnessed phrases is green while the stop contract's §8
table still describes the retired file, its refresh and its released-landed line. That table is the
matrix agents actually follow, and this case is AC13's own Red-when.

**Fix.** Add zero-count witnesses:

- for `released <iso>`, `refreshes the lease`, `in the lease first` and `keeps what it saw in the
  lease` in `STOPS.template.md`;
- for `refreshing the` in `PROTOCOL.template.md`;
- for `refreshes the lease`, `per-slug LEASE` and `in the lease` in the dossier.

Also require the verb carrier's `--liveness` entry to name HELD, and state the exact replacement text
for the "its four" comments.

**Left-shift.** Derive the witness list from S1's retired vocabulary instead of hand-picking phrases.
One grep over every carrier for the retired nouns (the lease file, its refresh, its release) must
read zero. Then a sentence nobody listed cannot escape.

### M9 — order 30 is shared with unit 32, contradicting F11's run-alone (20)

**Address.** Spec 61 status header (`:3`), against its own §8 F11. Against
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md`'s status header and §9
(`:680`), and against the generated build order in `memory/builds/dDerivedDocket/README.md`
(`:212`).

**What is wrong.** Units 32 and 61 both declare order 30. The README renders step 30 as those two
units with Parallel `yes`. F11 says the DECISIONS row makes this pass run alone under BUILD-METHOD
M6 condition 3. Spec 32's own §9 says the same of itself: it "runs at order 30, alone".

Commit `8f354565` set the convention that condition 3 keeps DECISIONS-appending units off any shared
wave, and unit 27 took its own order for that reason. Backlog `TOOL-dDerivedDocket-60` records that
`--dispatch` refuses to declare `memory/DECISIONS.md` at all.

**Why it bites.** One of two things happens. The orchestrator dispatches 61 in one wave with 32,
which breaks M6 condition 3 on a shared mutable record. Or `--dispatch` refuses the declaration at
wave time. Either way the ordering contradicts F11 and the build's own wave rule.

**Fix.** Give unit 61 an order no other unit declares, so its step holds one unit, and record the
move in its §9.

**Left-shift.** Have the build-order generator red, or render Parallel `no` with the conflict named,
when a step holds more than one unit and any spec in it names `memory/DECISIONS.md` in its Files
touched or says it runs alone. Two specs that each claim "alone" at one order can be detected from
their text.

## Low

None. No finder rated a finding LOW, and none is adjudicated one here.

## Fold order

1. Fold B1 first, because its route choice decides M5's fix text and narrows M3.
2. Fold H1 and H2 together, since both edit the matrix section and F1.
3. Fold M1 in the same commit as H2, so units 27 and 61 agree on what was carried.
4. Fold the remaining mediums, which are independent spec edits.

After the fold, re-review the fold text itself rather than trusting it. This repo's memory records
that 42 of 62 findings in an earlier round-2 audit were caused by the round-1 fold.

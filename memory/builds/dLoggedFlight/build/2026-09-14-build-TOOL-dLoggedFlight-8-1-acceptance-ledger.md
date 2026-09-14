# Acceptance ledger — TOOL-dLoggedFlight-8

**Serves:** journal TOOL-dLoggedFlight-8

Tier-2 · node d · 2026-09-14 · the build pass of the run model, against spec rev-4. The pass bumped
the spec to rev-5 for what building settled, and its section 9 line names each change. Every
criterion line is OBSERVED, and the gate legs are written as owed. `<suite>` is
`tools/runlog/selftest.py`, run directly and never through the gate runner. Its three timed runs at
the closing commit printed `774 passed, 0 failed (774 assertions, floor 774)` in 18.2 s each. No
gate leg was run, per the owner's instruction of 2026-09-13, and no suite that existed under
`tools/unattended/` before this build ran. Every history an arm reads is a scratch repository built
through one `git fast-import`, and every journal and extract is scratch. The exceptions are three
arms that read this tree and never write it: AC7, the decision-log report and the driver-source
arm.

## The criteria

**Evidences:** TOOL-dLoggedFlight-8

- AC1 — `derive_run_starts` (`test_model_ac1_ac16_rotation`) — a build rotated the way the driver
  rotates, with the archive at `archive_name_of`'s name and a fresh record in one commit, gave two
  runs. The archive came first, keyed on its own preflight, and the live record was keyed on the
  rotation commit, so the two keys differ. The archive's own creation commit is the live run's start,
  which the liveness check asserts, so the naive key would resolve both records to one commit. The
  population form gave the same runs in one call. The half-open windows were disjoint, and the live
  timeline held only its own commit. RED seen with the archive keyed on its creation commit.
- AC2 — `build_run_model` (`test_model_ac2_own_commits`) — commits naming the run's units were
  interleaved with two of another build, one of which names the slug without a unit. The timeline
  carried the two own commits and the two phase moves in time order, and the last own commit was the
  run's. RED seen with every era commit admitted.
- AC3 — `scan_decisions` (`test_model_ac3_ac11_ledger`) — the two `Decided:` trailers in the final
  block came back with the sha of their commit. The mid-body line counted as one near-miss. The
  marks read `owner-before` 1 and `agent-inside` 1, the agent's mark wrapping across two lines. RED
  seen with every mark counted inside, and with the near-miss count zeroed.
- AC4 — `check_conformance` (`test_model_ac4_ac12_conformance`) — a build commit a minute before its
  brief row read UNMET, and its evidence named both times. RED seen with the order test dropped.
- AC5 — `scan_anomalies` (`test_model_ac5_anomalies`) — a clean landed run, preflighted, dispatched,
  briefed, built, gated green, closed, merged, pushed through the lander and landed, reported
  nothing. Each of the twelve kinds fired alone on its own variant. The dRatifiedSeam shape read
  `nonterminal-merged`: its witness was written once by the preflight fact and its phase moved to
  LANDING by the close fact. So did a witness strictly behind its base. A run with no own commit
  read `no-progress`, naming its start and the window end. A refused `--landed` beside a last parked
  decision row read `refused-landing`, not the table's `surfaced-park`. Each sub-class fired on its
  own fixture, and both sets matched their fixtures in both directions. RED seen with a
  witness-equals-base exemption, with the refused `--landed` ignored, with `stalled` never firing,
  with a seven-minute idle threshold, and with the destructive rule removed.
- AC6 — `measure_coverage` (`test_model_ac6_coverage`) — a journal holding only another run's lines
  set the epoch to its first line. A window before it read `absent`. A window after it, with twelve
  parked rows and no lines of the run, read `dead`. A window holding it read `partial`, with or
  without lines of its own. A window after it read `present` with its own lines, and also with no
  line and no proof one was owed. A missing file read `absent`, and a missing transcript read
  `not-local`. All five states were produced. RED seen with a dead writer read as absent, and with
  lines checked before the epoch.
- AC7 — `python tools/runlog/runlog.py model aLeakedHandle --json` (`test_model_ac7_real_tree`) — on
  this tree, with its journals aimed at a scratch directory whose first line is dated three days
  after the run and its store and transcripts at scratch, the CLI exited 0. The parked-row counts
  matched the record, which holds review 6, decision 3, dispatch 10 and brief 3. The window ended at
  7d9e2d47, the commit that first wrote `phase: LANDED`, 2026-09-10 19:34:28 +0300, and did not reach
  9fac2b53 of 2026-09-13, the latest commit naming the slug. Driver and gates read `absent` by epoch
  and pushes by file. A local copy landed under the arm's store in `models/`. RED seen with the
  terminal write ignored. The arm's first run found a defect: a `--status` reading LANDED on both of
  its lines was taken for the terminal END and ended the window three days late. S2 now names the
  terminal END as the verb that moved the phase into a terminal one, and AC16 pins it on a fixture.
- AC8 — `build_run_model` with `subprocess.Popen` patched (`test_model_ac8_git_calls`) — runs of 10 and 100 own commits,
  each commit touching the record and the decision log, both modeled every own commit, and each cost
  6 git processes. RED seen with blobs read one call each, which printed 38 and 308.
- AC9 — `build_run_model` (`test_model_ac9_no_start`) — a run with no preflight START and no parked
  rows, its witness naming no commit, started at its start commit, with `start_from` git. A later
  commit naming the slug left the end at the terminal write, and for a non-terminal run at one second
  past the last record commit. The same held under a declared memory root of `records`. RED seen with
  the window started at the first own commit, and with the end taken from any era commit.
- AC10 — `build_run_model` (`test_model_ac10_joins`) — of two bars in the same minute from two
  worktrees, only the run's own joined, and the bar whose run id a push pinned joined through
  `gate_run`. The landing push from the primary tree joined through `pushed-sha`, and `pushes` read
  `present`. A push of a sha outside the run's history joined nothing. Gaps of 15 and 14 minutes
  yielded one idle gap, the 900 s one. RED seen with the worktree test dropped, with the pushed-sha
  key dropped, and with a 14-minute threshold.
- AC11 — `scan_decisions` (`test_model_ac3_ac11_ledger`) — one entry per source of `LEDGER_SOURCES`,
  with counts equal to the fixture's, and the parked entries named by record and line. Every excluded
  kind was counted and none entered: `proposal`, `dispatch`, `brief`, `review` and `rescope add`. The
  five owner spellings read as the owner's, and the `(ownership` near-miss and the run's own row did
  not. The review entry is the review record with its verdict line, and the ledger entry is the owed
  AC2 line, not the observed AC1 line. RED seen with a review row admitted, with the bare `(owner)`
  spelling lost, and with `(owners` matching. The report-only arm (`test_model_ac11_decision_log_report`)
  printed `(owner)=8 (owner,=7 (owner:=1 owner ruling=10 owner call=1 near-miss=0` over the tracked
  decision log. It was seen RED with the scan printing nothing.
- AC12 — `check_conformance` (`test_model_ac4_ac12_conformance`) — all five items in all three
  states came from eighteen fixtures, and the covered set equals the full product. A close with no
  gate line in its window read UNJUDGEABLE. The clean landed run, end to end, met
  `brief-before-build`, `phases-walked`, `green-at-close` and `keepalive-reaped`, and read
  `review-exited` UNJUDGEABLE with no review row. Its close head was the LANDING commit's parent.
  RED seen with the no-gate case reading MET.
- AC13 — `build_owner_positions` (`test_model_ac13_ac14_positions_usage`) — turns classed `launch`,
  `pre-run`, `in-window` and `post-close`. A turn at the start reads in-window and one at the close
  reads post-close. With no close, a turn after the terminal END reads post-close. With no START, a
  model over a scratch repository put a turn before its start commit in `launch`, one inside the
  window in `in-window`, and one after the window end in `post-close`. RED seen with the close
  inclusive.
- AC14 — `build_run_usage` (`test_model_ac13_ac14_positions_usage`) — usage before the window and at
  its end stayed out, and one request per split counted. RED seen with the window filter dropped.
- AC15 — `build_run_model` (`test_model_ac15_ac18_journal_join`) — a journal holding a refused
  preflight, a successful one, a status, a second successful preflight and a status gave runs whose
  timelines held exactly their own lines. The refused preflight sat in run one's lines and started
  nothing. RED seen with every line given to the live run, and with the rc test dropped.
- AC16 — `build_run_model` (`test_model_ac1_ac16_rotation`) — the archive's window ended at its own
  terminal write, and a non-terminal live window at one second past its last record commit. In the
  LANDED-after-LANDED fixture, the live window ran from the rotation to its own terminal write, past
  neither the predecessor's nor a later mention. A terminal END ended the window at that END, and a
  `--status` reading LANDED on both lines ended nothing. RED seen with the era bound dropped, and
  with the phase-from test dropped.
- AC17 — `derive_attribution` (`test_model_ac17_attribution`) — fixture lines copied from the golden
  driver pair: of eight calls, the pre-verb call went unattributed. Units split 2 and 3, the heartbeat
  keeping the brief's unit and the killed brief contributing none. Phases split BUILDING 6 and
  VERIFYING 1, the second session's move reaching only its own call. The shares were 7/8 of calls and
  65/75 of wall time. Every line the model arms wrote, and every golden line, carries only its
  producer's keys, and a stray `phase_from` on an END is caught. RED seen with the first-END test
  dropped, with points pooled across sessions, and with a unit-less END resetting the unit.
- AC18 — `build_run_model` (`test_model_ac15_ac18_journal_join`) — three start commits and
  preflights for the last two. Run one's window came from git alone, and each START joined the start
  commit its own call made, with that commit's runkey. A START after the last start commit was named
  in the coverage block and started no run. RED seen with STARTs joined by position, and with the
  unjoined START not cutting the segment.

## What else the pass carried

- **The golden lines, re-derived.** The driver, the gate runner and the pre-push hook were each run
  once in a scratch sandbox, by a probe kept outside the tree, and the fixture was corrected to what
  they wrote. The driver pair is now a refused `--brief`. The old pair was a `--phase` carrying
  `unit` and `checks=14`, and the writer never puts `unit` on a `--phase` END, which also cannot
  refuse on check 14. Every `t` now has six fraction digits and `dur_us` is the pair's real
  difference. On the gate line, `stage` is empty, `started` is an ISO stamp, `run` has the runner's
  shape and `wall_breach` is empty, as the runner writes them. The push line is unchanged apart from
  `t`.
- **The driver-source arm** (`test_model_driver_sets`) holds `PARK_KINDS`, `PARK_KINDS_OWED`,
  `PARK_ACTS_OWED` and `PHASES_TERMINAL` to the driver in both directions. It also holds the fixture
  scaffold, byte for byte, park()'s row format, and both driver writers' key sets against
  `PRODUCER_KEYS`. Each was seen RED. Its path literal takes a carried row, added at 1 with its
  reason, counted first with the gate's own pattern.
- **Real-population figures, re-measured** with the model itself and written into the spec's section
  4. They are unchanged except for the parked rows kept out, which moved from 489 to 510 with this
  build's own dispatch and brief rows. This node's driver journal holds 44 of this run's lines and no
  record-creating preflight, so the run models from git with `driver` reading `partial`. `gates`
  reads `absent` until the post-build gate run writes its first line.

## Staged RED

Thirty-six breaks of the model and three of the self-test's own copies, each loaded as a module
object from an edited string by a harness kept outside the tree. Each break turned its arm red, and
the unbroken control passed every arm the breaks aim at. The breaks are named per criterion above.

## The checklist over the slice commits

`gotchas.py --for-diff HEAD~1..HEAD` ran after each slice.

- `two-answers-to-one-question` was violated three times and each is fixed. The fixture's run-state
  writer and `PRODUCER_KEYS` were second statements of the driver's writers, and they are now held to
  its source. The README repeated S12's count of git processes, and now points at it.
- `staged-break-substitutes-a-synthetic-value`: the arms that read this tree read the real record,
  decision log and driver, and the attribution fixture is copied from the golden driver lines.
- `fold-text-is-unreviewed-surface`: rev-5 is fold text no review has read. The closing diff review
  of the build reads it.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `lexicon naming predicates`, `install-prefix (shipped surface)` and `govkit selfcheck`;
- `codebase-map coverage + freshness` and `memory hygiene`;
- `runlog selftest`, the leg that runs `<suite>`, and
  `every held leg is budgeted, every budget row resolves`, whose row this pass re-measured.

## Residue

- A killed verb cannot contribute a unit: a START carries no `unit` field in the driver's data model,
  so AC17's red condition is structurally unreachable, and the arm pins that the killed brief's unit
  never appears.
- The witness-behind-base variant was seen RED only through the equal-witness break. An ancestry
  rule would be caught by that variant, and no such rule was written to prove it.
- `PRODUCER_KEYS` for the gate runner and the pre-push hook is held to the golden lines, which this
  pass re-derived, and not to those writers' sources.
- On a run with no journal, `idle-gap` reads its sparse sources as idleness. The spec defines the
  kind over every source, and the model does not guess which gaps a journal would have filled.
- The runlog kit stays at 1.0, as the brief sets it, and no leg, fixture file or pin moved. The
  budget row now reads 19 s in the ranker's integer spelling, still under the 60 s floor.

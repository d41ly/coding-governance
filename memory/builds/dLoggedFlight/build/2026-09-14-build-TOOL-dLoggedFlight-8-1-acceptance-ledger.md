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
arm. The closing diff review's round-1 fold of B1 and H1 bumped the spec to rev-6 and added AC19,
whose line below that fold observed. Its fold of H2 and M5 bumped the spec to rev-7 and added AC20
and AC21, whose lines below that fold observed. Its fold of M1, M4 and M5's timeline bound bumped the
spec to rev-8, widened AC17 and added AC22 and AC23, whose lines below that fold observed. Its fold
of M2 and M3 bumped the spec to rev-9 and widened AC6, AC12 and AC13, whose lines below record what
that fold observed. Its fold of L2, L3 and L5 bumped the spec to rev-10 and widened AC1, AC2 and
AC6, whose lines below record what that fold observed; L3's refusal is observed under unit 10's
AC5.

## The criteria

**Evidences:** TOOL-dLoggedFlight-8

- AC1 — `derive_run_starts` (`test_model_ac1_ac16_rotation`) — a build rotated the way the driver
  rotates, with the archive at `archive_name_of`'s name and a fresh record in one commit, gave two
  runs. The archive came first, keyed on its own preflight, and the live record was keyed on the
  rotation commit, so the two keys differ. The archive's own creation commit is the live run's start,
  which the liveness check asserts, so the naive key would resolve both records to one commit. The
  population form gave the same runs in one call. The half-open windows were disjoint, and the live
  timeline held only its own commit. RED seen with the archive keyed on its creation commit. The
  fold of L3 found neither run marked `joint_add`, a rotation adding the archive and only modifying
  `RUN.md`. RED seen in place, restored by checksum, with every start marked.
- AC2 — `build_run_model` (`test_model_ac2_own_commits`) — commits naming the run's units were
  interleaved with two of another build, one of which names the slug without a unit. The timeline
  carried the two own commits and the two phase moves in time order, and the last own commit was the
  run's. RED seen with every era commit admitted. The fold of L5 added a whole-set commit spelling
  its units `X-xFixtureRun-1..2`, after unit 1's own build commit and before unit 2's. Its own-commit
  and timeline entries named both units, and it was unit 2's build commit while unit 1's stayed its
  own. `scan_unit_ids` ran a range to its end, named the first id alone for a backward range and for
  one past `UNIT_RANGE_MAX`, and ran a range of exactly that many to its end. RED seen in place,
  restored by checksum, five ways: the range tail ignored, which redded all five checks; each of the
  three uses back on the single-id pattern, each redding its own check; and the bound removed.
- AC3 — `scan_decisions` (`test_model_ac3_ac11_ledger`) — the two `Decided:` trailers in the final
  block came back with the sha of their commit. The mid-body line counted as one near-miss. The
  marks read `owner-before` 1 and `agent-inside` 1, the agent's mark wrapping across two lines. RED
  seen with every mark counted inside, and with the near-miss count zeroed. The rev-8 fold rebuilt
  its fixture the way the driver writes it: the preflight commit carries the preflight record and an
  `--abort` commit after the work carries the final one. It had written its final ABORTED record in
  the preflight commit, a shape no verb leaves, which closed its window at its own start once own
  commits were bounded by the window. The trailers, the decision-log rows and the ledger line then
  read zero.
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
  lines checked before the epoch. Widened at rev-9 by the fold of M2, and observed by it in
  `test_model_ac6_dead_through_model`. Through the model, the landed fixture staged with a journal
  older than the run and none of its own lines read that journal `dead`, naming its proof: the pushes
  with the driver journal, the window closed by the terminal END, and without it, closed by the
  terminal write; the gates; and the driver. With the run's own lines beside the older ones, each
  journal read `present`. RED seen with the pushes proof looked for among the window's moves, on both
  pushes rows. Before this fold no landed run's `pushes` could read `dead`. The fold of L2 hands
  `measure_coverage` the run's own driver lines over its whole segment. With none, windows after the
  epoch read `not-local`, with twelve parked rows and with none, each with a note, while lines of the
  run's own after its window kept `dead` and `present`. Through the model, each dead case with none
  of the run's verbs stages the owner's `--status` after the landing, and the landed fixture with
  older journals whose driver lines all name another build read `not-local` for all three. The same
  journals with that `--status` beside them read `dead` for all three, so one line of the run's own
  is the whole difference. A rotated build whose first run alone was driven here read its first
  run's driver `present` and its second's `not-local`, with a parked row in the second's window. RED
  seen in place, restored by checksum, three ways: the not-local branch removed; the key of the
  fold's first cut, any driver line naming the build, which read the second run `dead`; and the count
  taken inside the window alone, which read the post-landing `--status` cases `not-local`. That first
  cut keyed on any line naming the build, as the review proposed. The bug-class checklist over its
  commit named `join-key-widened-by-a-shared-location`, since an earlier run of the build is a
  location every later run of it shares. An early cut of the note check passed with the branch
  removed, since it quantified over no not-local state, and it now requires the two it expects.
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
  RED seen with the no-gate case reading MET. Widened at rev-9 by the fold of M3, and observed by it
  in `test_model_ac12_killed_close` and `test_model_ac12_rc_reads_exit`. A run whose `--close` END
  read `rc=0` and `exit=unclean`, as the driver's EXIT trap writes a verb killed mid-bar, after a
  GREEN bar at its head, had no close and read `green-at-close` UNJUDGEABLE. The same END reading
  `exit=clean` closed the run and read MET. The source arm parsed `model.py` and found every
  comparison on an END's `rc` in a condition that also reads its `exit`, a transcript call being its
  one exempt receiver. RED seen with the close taken on `rc=0` alone, which the behaviour arm and the
  source arm both caught, and with a stale exemption added to the arm's own table.
- AC13 — `build_owner_positions` (`test_model_ac13_ac14_positions_usage`) — turns classed `launch`,
  `pre-run`, `in-window` and `post-close`. A turn at the start reads in-window and one at the close
  reads post-close. With no close, a turn after the terminal END reads post-close. With no START, a
  model over a scratch repository put a turn before its start commit in `launch`, one inside the
  window in `in-window`, and one after the window end in `post-close`. RED seen with the close
  inclusive. Widened at rev-9 by the fold of M3, and observed by it in
  `test_model_ac12_killed_close`: in the killed-close run, its session made by the real extractor, an
  owner turn after the END and inside the window read `in-window`, and `post-close` once that END read
  `exit=clean`. RED seen with the close taken on `rc=0` alone.
- AC14 — `build_run_usage` (`test_model_ac13_ac14_positions_usage`) — usage before the window and at
  its end stayed out, and one request per split counted. RED seen with the window filter dropped.
  Since the rev-8 fold the filter is `check_in_window`, and it was seen RED again with that call
  dropped, and with the window closed at its end.
- AC15 — `build_run_model` (`test_model_ac15_ac18_journal_join`) — a journal holding a refused
  preflight, a successful one, a status, a second successful preflight and a status gave runs whose
  timelines held exactly their own lines. The refused preflight sat in run one's lines and started
  nothing. RED seen with every line given to the live run, and with the rc test dropped. Since the
  rev-8 fold it is on no run's timeline: run one landed before it, so it lies past run one's window,
  and the arm now asserts that. RED seen with the timeline's verbs taken from the whole segment.
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
  dropped, with points pooled across sessions, and with a unit-less END resetting the unit. Widened
  at rev-8 by the closing diff review's round-1 fold of M1, M4 and M5's timeline bound, and observed
  by that fold. The same session now also holds another build's `--brief` END, one more of the run's
  own verbs, and a call past the window's end. Of ten calls inside the window, eight were attributed.
  The pre-verb call and the call after the other build's END were not, and the call past the end was
  not counted. The run's next END attributed again with no unit, so units split 2 and 3 as before
  and never took the other build's. Phases split BUILDING 7 and VERIFYING 1, and the shares were
  8/10 of calls and 75/95 of wall time. With every END read as the run's and no window end, the other
  build's unit counted three times and the late call counted, which the liveness check asserts. RED
  seen with the window test dropped, with another run's END attributing its calls, and with another
  run's unit taken.
- AC18 — `build_run_model` (`test_model_ac15_ac18_journal_join`) — three start commits and
  preflights for the last two. Run one's window came from git alone, and each START joined the start
  commit its own call made, with that commit's runkey. A START after the last start commit was named
  in the coverage block and started no run. RED seen with STARTs joined by position, and with the
  unjoined START not cutting the segment.
- AC19 — `build_run_model` (`test_model_ac19_idle`, `test_zz_model_idle_invariant`) — added at rev-6
  by the closing diff review's round-1 fold of B1 and H1, and observed by that fold. The session was
  made by the real extractor from a transcript. Twenty minutes of two-minute calls between two
  timeline events and a 26-minute foreground call yielded no idle gap. The nineteen-minute silence
  yielded the one gap and the one `idle-gap`, at its start. The three silences an owner turn closed,
  opened and sat inside were kept out, and `idle` counted one fired and three near an owner turn. With
  the journal and no transcript, and on AC10's run with neither, nothing was judged, and the coverage
  said so. No gap of any model the arms built held a tool call. RED seen with the gaps read over the
  timeline alone, with the owner guard dropped, with owner turns put back among the events, and with
  idleness judged whatever the transcripts read.
- AC20 — `build_run_model` (`test_model_ac20_tree_holds`) — added at rev-7 by the closing diff
  review's round-1 fold of H2 and M5, and observed by that fold. The landed fixture now lands from
  the primary tree, its `--landed` there. The arm adds four more of the run's calls in that tree: a
  `--landed` refused before the close, an owner's `--status` and `--resume`, and a `--park` after
  the close. The run held its own worktree and a second one it first claimed mid-window, never the
  primary tree. Of eight bars, the run's three and the pinned one joined. These stayed out: two bars
  another run made in the primary tree, a raw push refused there with `lander=0`, and an `ev=once`
  refusal there. So did a bar made in the second worktree before the run's claim, and one made in
  the run's worktree after another build's preflight there. `journal_lines` held none of those
  lines, `push-outside-lander` did not fire, and the landing push still joined by `pushed-sha`, its
  pinned bar by `gate_run`. With no verb blind, the owner's `--status` claimed the primary tree, and
  the same lines joined and fired the anomaly. `TREE_BLIND_VERBS` drives the fixture both ways: each
  member has a call in the primary tree, and the one other verb there is blind by its phase. RED seen
  with the key taken from every tree any call ran in, as rev-6 took it; with each of `--status`,
  `--resume` and `--landed` in turn made a claim; with the phase test dropped; with the hold never
  ending; with the hold starting at the window start; and with a blind verb added that no call
  stages.
- AC21 — `build_run_model` (`test_model_ac21_nonterminal_end`) — added at rev-7 by the same fold, and
  observed by it. A run left BUILDING, its record on its branch and its last driver line the
  `--phase` at minute 6, committed its unit's work twenty minutes later, then barred it and pushed
  its branch from its own worktree, its session busy throughout and extracted by the real extractor.
  The window closed one second past the push's END, by last activity. The own commit, the bar and
  the push lay inside it, the bar and the push joined by tree, and `gates` read `present` with one
  line. None of these moved the end: a later bar in the primary tree, a bar in the run's worktree
  after another build's preflight there, a merge naming only the slug, and a later tool call in the
  run's session. A record-creating START that joined no commit, made between the bar and the push,
  ended the run's journal lines, and the window then closed one second past the bar. With no journal
  it closed one second past the own commit. RED seen with the tree lines dropped from the end, with
  the own commits dropped, with the end read the rev-5 way, with the merges naming the slug taken,
  with the session's events taken, and with the segment's end dropped. The session break also moved
  AC13's stand-in owner turn from `post-close` into the window. Since the rev-8 fold the later merge
  is read from git for the liveness check, and it is no longer on the timeline, which AC23 asserts.
- AC22 — `build_run_model` and `runlog.py verify` (`test_model_ac22_later_unit_commit`) — added at
  rev-8 by the closing diff review's round-1 fold of M1, M4 and M5's timeline bound, and observed by
  that fold. The landed fixture's record was rendered, and then a commit on the default branch
  naming unit 1 was made twelve minutes after the landing. The own commits, the last own commit (the
  landing merge) and `merged` did not move. The landing push still joined by `pushed-sha` and its
  bar by `gate_run`, and `verify` over the earlier render exited 0. The later commit descends from the
  start and lies in the run's open era, so an era bound alone takes it. A run left at LANDING pushed
  the default branch from the primary tree after its merge and a record commit on top, then made one
  more own commit on its branch. That push joined by `pushed-sha`, and a push of the default branch
  before the run's work reached it joined nothing. RED seen with own commits bounded by the era,
  which the own-commit check caught alone, and with a push tested against the last own commit,
  which the non-terminal push check caught alone. With both, as rev-7 had them, the landing push and
  its bar stopped joining and `verify` exited 1 reading "mismatch": M4's false tamper signal.
- AC23 — `build_run_model` (`test_model_ac23_window_bound`, `test_zz_model_window_invariant`) —
  added at rev-8 by the same fold, and observed by it. The landed fixture's session was made by the
  real extractor. It held a call around each verb, a call after another build's `--brief` END in the
  same session, and a call after the `--landed` END. The model counted seven calls, equal to its tool
  calls. The calls before the preflight START and after the `--landed` END were out, and the two
  after the other build's END were counted and unattributed. Units read `X-xFixtureRun-1` 3 and
  never the other build's. The LANDED write after the `--landed` END was off the timeline, where the
  `--landed` verb still carried LANDED. An owner's `--status` after the landing, from another session,
  was on neither the timeline nor the committed driver lines, and that session was not the run's.
  `phases-walked` read MET, and the other build's later verb in the session left `multi-run-session`
  at its one verb inside the window. On a git-only run whose LANDED write ended its window, the
  timeline held RUNNING and BUILDING and `phases-walked` read MET by the phase at the end. Every model
  the arms built passed both invariants, and so did the real aLeakedHandle model under AC7. RED seen
  with the timeline's commits and merges unbounded, which AC21's merge caught; with phase moves
  unbounded; with verbs, sessions or driver lines taken from the whole segment; with `shared_sessions`
  unbounded; with no closing phase in `phases-walked`; with points taken from the run's own verbs
  alone; and with the window closed at its end. Under the three timeline breaks and the closed end,
  the invariant arm redded as well and named the arm behind each violation; with the attribution
  window dropped, its call-count half did. One bound has no staged arm: a bar a joined push pinned
  is also bounded, and dropping that bound turned nothing red, because the hook pins the bar it ran
  for the pushed tree or a green it reuses for it, and no fixture shape puts one outside the window.
  The invariant arm would red on one.

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
The fold of M1, M4 and M5's timeline bound staged sixteen more breaks of the model, and the rev-7
own-commit logic as one combined break, each by rewriting `model.py` in place from a harness kept
outside the tree, clearing the bytecode cache, running the suite and restoring the bytes, which a
checksum confirmed after the last. Fifteen redded their arms. The sixteenth, the pinned bar's bound,
had no arm to red, which AC23's line explains. The suite then ran green three times directly, at
1186 of 1186 assertions, in 53.1 to 53.8 s each, under its 69 s budget row. The fold of M2 and M3
staged two more breaks of `model.py` the same way, running only the arms each aims at, and one of
the source arm's own exemption table: the pushes proof among the window's moves, the close on
`rc=0` alone, and a stale exemption. Each redded its arms, and the restored bytes matched their
checksums.

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
  CLOSED by the closing diff review's round-1 fold of H1: the model judges no idle gap unless every
  session's transcript is local, and its coverage says when it did not judge.
- The runlog kit stays at 1.0, as the brief sets it, and no leg, fixture file or pin moved. The
  budget row now reads 19 s in the ranker's integer spelling, still under the 60 s floor.
- The H2 and M5 fold leaves three things standing, each on purpose. The timeline still lists a merge
  naming only the slug that falls after a non-terminal window's end, and a terminal run's own
  commits after its window. Bounding every derived set by the window is the fold's next slice, with
  M1 and M4. Two runs that claim one tree in the same stretch both hold it, so a bar made there
  joins both. The schema leg's non-terminal end reads the record commits alone, which spec 10's S6
  now says. The first of the three is CLOSED by the fold of M1, M4 and M5's timeline bound: every
  timed set the model derives is bounded by the window through one predicate, and AC23 grades every
  model the arms build against it.
- The fold of M1, M4 and M5's timeline bound leaves S4's spec-mark split reading each spec at the
  era's end rather than the window's. The window's end needs the one blob read that places a
  terminal write, and that same read carries the specs, so bounding the split changes S12's calls.
  Spec 8's rev-8 line names the gap and routes it to round 2. The kit README lists it among what
  the model does not do.
- **Parked by the H2 and M5 fold: the session key has H2's shape.** The bug-class checklist over the
  fold's code commit named `join-key-widened-by-a-shared-location`. The class has a second instance
  in the same function: a run's sessions are every session any of its calls names, `--status` and
  `--resume` included. So another Claude session that looks at a run with `--status` joins it. Its
  tool calls, usage and owner turns would then count as this run's, and the in-window owner count
  is a committed fact. The options seen were three. Name sessions only from calls other than
  `--status` and `--resume`, which keeps a landing session, since a session is no shared location.
  Name them by the tree claim rule instead. Or keep the key and say so. None was taken, for three
  reasons. No review confirmed it. It moves the owner-turn, usage and attribution facts that the
  fold's next slice reworks for M1. And spec 8 would need a rule for it that no audit has read.
  That next slice, the fold of M1, M4 and M5's timeline bound, narrowed it by the window and no
  further. A session whose only call on the run comes after the run's end is no longer one of its
  sessions, which AC23 observes. One that calls `--status` inside the window still joins, and its
  calls after that `--status` END are attributed to the run, so the park stands.
- The fold of L2 leaves a writer broken for the whole of a run made here reading `not-local`, the
  same as a run made on another node. The model has no node identity, and only the run's own driver
  lines place it here. The kit README names it among what the kit does not check. The run's own
  lines are its journal segment as S2 reads it, so a `--status` made here inside another node's run
  is one of them and places that run here. The checklist over the key's commit named
  `join-key-widened-by-a-shared-location` for it: a `--status` is a visit and claims nothing. It is
  the parked session key's visit, below, met through the segment rather than the session, and it is
  left with that park rather than changing S2's segment inside a low's fold.
- The fold of L5 reads a range the way the memory-tree grammar reads one. A subject that continues
  an id with bare numbers, as two of this build's own spec-audit folds spell `-1..4, 6, 8..13`,
  names units 1 to 4 alone; the grammar reads it the same, and `scan_unit_ids` says so.

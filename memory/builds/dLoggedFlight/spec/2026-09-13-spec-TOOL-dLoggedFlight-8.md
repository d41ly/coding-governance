# TOOL-dLoggedFlight-8 — the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set

**Status:** CLOSED · rev-19 · 2026-09-20 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-8-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-8-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A run's evidence is spread across its run-state file, three journals, git, the build folder and, where
local, its transcripts. Join them into one model of one run: what it did and when, what it decided,
what it cost, whether it followed the method, what looks wrong, and how much of each answer the
sources actually support. Every later surface renders from this model rather than re-deriving it.

## 2. Scope (IN)

- **S1** Run starts. A build's runs are listed, oldest first, by the commit that STARTED each one:
  - the commit that first added its `RUN.md`;
  - then every commit that added a `RUN.<phase>.<8hex>.md` sibling, found with `git log --diff-filter=A`
    on that glob and WITHOUT `--follow`.

  The driver rotates a finished record with `git mv -f` and re-scaffolds `RUN.md` in the successor's
  preflight commit (TOOL-dClosedLexicon-11). So each rotation commit is also the successor's start, and
  a path's creation commit cannot tell an archive from its successor. Run k takes entry k: an archive
  takes the entry immediately before the commit that added it, and the live `RUN.md` takes the last.
  One function, `derive_run_starts`, owns this, and `TOOL-dLoggedFlight-9` reads its value rather than
  re-deriving it. It takes one build or the whole population and costs one git call either way: a
  single `git log --no-renames --diff-filter=A --name-only` over the run-state paths it is handed.
  `derive_run_eras` turns the starts into ERAS, run k's being the commits from its start up to the next
  start of the same build, or to HEAD for the last run. Every path is under the declared memory root,
  read through `resolve_memory_root` of `TOOL-dLoggedFlight-1`, never a `memory/` literal. A commit
  that ADDS a build's live `RUN.md` and one of its archives together leaves every run it holds on
  one start, since no earlier entry under the path names the archive's start. A squashed history
  leaves that shape, and so does a memory root or a build folder moved in one commit, which with
  renames off adds every record it moves; nothing here follows a path back past it.
  `derive_run_starts` marks each run whose start is such a commit `joint_add`, and the schema leg
  names the shape when it refuses the shared start (`TOOL-dLoggedFlight-10` S6). Observed by AC1,
  AC9 and AC18, and the mark by `TOOL-dLoggedFlight-10` AC5.
- **S2** Run windows. A window is half-open, `[start, end)`, and every read of a run-state path's
  history is bounded to the run's era (S1). Rotation keeps the path, so `RUN.md`'s history carries
  every predecessor's terminal write. An archive's own terminal write is read from `RUN.md` inside the
  archive's era, since its bytes lived there until rotation. A window starts at the run's preflight
  START in `driver.log`, or at its start commit when there is none. It ends at the first of these that
  applies:
  - the run's terminal END in `driver.log`: the END of the verb that moved the phase INTO a terminal
    one, its START having read a phase that was not terminal. A `--status` after a landing reads the
    terminal phase on both of its lines and ends nothing;
  - for a terminal record, the first commit in its era that wrote a terminal `phase:`;
  - for a non-terminal record, one second after its last event. Its events here are its journal
    lines, a read-only visit's excepted, the commits in its era that touched `RUN.md`, its own
    commits (S3) as the era holds them,
    a merge naming one of its unit ids among them, and the gate and push lines made from a tree it
    holds (S3) before the next run's journal lines begin. The second is a commit time's resolution,
    and it puts the run's last event inside its own half-open window. Four sources never move it.
    A read-only visit another session made does not, under the session rule below: such a visit
    always lands inside the end it would move, so one `--status` made days later stretched a stalled
    run's whole window to itself, and then named its own session.
    A merge naming only the slug does not, under the rule below for a commit that merely names it. A
    transcript event does not, because the run's session keeps working after the run and renders the
    record itself, so an end taken from the session would end at the render and move with every
    re-render. A push joined only by what it pushed does not, because every later push of the default
    branch carries the run's commits.

  Journal STARTs join git's runs by a named key, never by position. A successful record-creating
  `--preflight` START, paired with an END of `rc=0`, belongs to the start commit its own call made: the
  first start commit of its slug at or after that END. The run's journal lines run from that START to
  the next such START. A START that joins no start commit, as when its commit never reached this clone,
  is named in the coverage block and starts no run, and a refused preflight starts no run. No bound is
  taken from a commit that merely names the slug: commits keep naming a slug after its run ends.

  Once the window is known, every set the model derives from a timed source is bounded by it through
  ONE predicate, `check_in_window`, and by nothing wider: the timeline's events of every kind, the
  tool calls, attribution (S8), usage (S10), the own commits (S3) and every join that reads them, the
  driver lines the record commits to, the sessions the run names, and the other builds sharing them
  (S6). The run's verbs after its end, such as an owner's `--status` once it has landed, are not its
  events. A terminal run's closing phase write lies at or past its end, so it is not a timeline event
  either, and `end_from` says how the window closed. Two reads stay bounded by the era, as S1 and S4
  state them: the run-state history and the review records. Observed by AC1, AC9, AC15, AC16, AC18,
  AC21 and AC23.

  A run's SESSIONS are the sessions its in-window ACTS named, never the ones its visitors did. The
  verbs of `READ_ONLY_VERBS`, `--status` and `--audit`, only read the record, so a session whose
  every call on the run is one of those is not one of its sessions, and its owner turns, usage and
  tool calls are not the run's. That is a SECOND constant beside `TREE_BLIND_VERBS`, and a proper
  subset of it, because naming a session and claiming a tree are different questions: `--resume`
  continues the run and `--landed` lands it, so both are the run's own acts whatever session made
  them, while neither makes the tree it ran in the run's. The two members named here and that
  difference are the ONE copy of those sets in this spec, and AC24 pins both against the constants in
  both directions, so this sentence cannot drift from them. The same rule decides which calls move a
  non-terminal end above and which ENDs are attribution points (S8). A read IS the run's own when its
  START named a session one of the run's acts named, or named no session at all: on the shipped
  default `RUNLOG_SESSION_VARS` is blank, so the keepalive tick's `--audit` records none, and a rule
  that dropped every read would put a stalled run's heartbeats outside its own window and leave
  `stalled` unable to fire. Observed by AC24.
- **S3** The timeline. Observed by AC2, AC10, AC20 and AC22. It holds:
  - phase moves with their time and witness;
  - every driver verb with its rc, `exit` and checks;
  - the run's own commits: commits inside its window that descend from its start commit and name one
    of its unit ids, read from its `branch-ref:` where that ref resolves and from the default branch. A
    raw base-to-witness range was measured to be 82% other work, and the witness can be stale (S6), so
    neither bounds them. They are read from the era and then bounded by the window, because commits
    keep naming a unit id after the run has landed, and one such commit would otherwise become a
    terminal run's last own commit. A non-terminal window's end is taken past every one of them (S2),
    so the bound removes only commits made after a terminal run's end. A subject names every unit
    id it spells, and a contiguous range spelled `<id>..<m>` names each id from `<id>` to `<m>`, the
    range the memory-tree index generator expands in a Serves line. One reader, `scan_unit_ids`,
    serves the own commits, the units each commit carries and S5's build commit, so no use of it
    credits a whole-set commit to its first unit alone. A range ending below its start, or naming
    more than `UNIT_RANGE_MAX` ids, names its first id alone, so no subject can make the model's
    cost grow with what it spells;
  - merges naming the slug, inside the window;
  - push lines, joined by where they were pushed from OR by what they pushed. A line made inside the
    window from a tree the run holds joins, and so does one inside the window that pushes the default
    branch's ref to a local sha carrying, in its history, the run's last own commit made at or before
    the push's START. A push is tested against the run as it stood when the push began, never against
    an own commit made after it. The second key is how the landing push joins: the protocol's lander
    pushes from the primary tree (`TOOL-dLoggedFlight-11` S6), so a run spans its own worktree and that
    landing;
  - gate lines inside the window, joined exactly by `run=` where a joined push line pinned `gate_run`,
    and otherwise by a tree the run holds;
  - unit dispatches and briefs;
  - from the extractor where local: owner turns, compactions and limits;
  - the model's idle gaps, which S6 judges over every source, never over this timeline alone.

  The trees a run HOLDS key the two joins by tree above and S2's window end. A driver call CLAIMS the
  tree it ran in when it is a preflight, or when its verb is none of `--status`, `--resume`,
  `--audit` and `--landed` and its START read a phase before the close. `--status`, `--resume` and
  `--audit`, the stall probe, only read the record, so they run from any tree. `--landed`, and any verb run once the run has closed, belong to
  the landing, which runs in the primary tree every run lands from. The run holds each tree its own
  calls claimed, from its first claim there to the first claim there by another run's call after its
  own last one. So neither the owner's `--status` nor the run's own `--landed` makes the primary tree
  the run's, and a worktree a later run reuses stops being this run's at that run's first claim.
- **S4** The decision ledger. Observed by AC3 and AC11. Each entry points at its source, a file and
  line or a sha. It holds:
  - the run-state rows whose kind is in the driver's `PARK_KINDS_OWED`, and the `rescope` rows whose
    act, the first word of the item, is in its `PARK_ACTS_OWED` (TOOL-aBoundedVerdict-5). Every other
    row stays out: `proposal`, `dispatch`, `brief`, `review` and `rescope · item add`, since review
    rounds enter from their own source below. The model's copies of both sets, with `PARK_KINDS`, are
    held to the driver by an arm of the withheld self-test. It extracts them from the driver's source
    where that file is present and compares both directions, and announces its skip where it is not.
    A replicated policy value is extracted from the file that owns it (`tools/hooks/README.md:150`),
    and the arm's path literal takes a carried row with its reason;
  - review rounds with their verdict path: each review record the run's era commits added under the
    build's `reviews/`, with the line of its `## Verdict:` where it has one;
  - `Decided:` trailers from the run's commits (`TOOL-dLoggedFlight-7`), plus a near-miss count of body
    lines beginning `Decided:` that git did not parse as trailers;
  - spec section 8 marks split by resolver, owner or agent, and by whether the commit that introduced
    them falls inside the window. The split is the difference between each spec's marks at the run's
    `start^` baseline and its marks at the last RECORD commit at or before the window's end, or at
    that same baseline where no record commit is. Rev-8 read the second at the ERA's end, which for a
    build's last run is HEAD, so a mark added to one of its specs after the run counted as decided
    inside it. Every candidate rev is requested in the one `cat-file --batch` of S12, because the
    window is derived from the phases those blobs carry and so is not known when they are asked for;
    the choice is made afterwards. The granularity is therefore a record commit and not a second: a
    mark committed inside the window but after the run's last record commit reads as neither before
    the run nor inside it. Observed by AC26;
  - `memory/DECISIONS.md` rows the run's commits added, classified as the owner's when they carry
    `(owner` followed by `)`, `,` or `:`, or the phrase "owner ruling" or "owner call" in any case. The
    classification is named `heuristic` in the model's `method` field. A report-only arm prints its
    hits per spelling and its near-misses over the tracked decision log;
  - acceptance-ledger lines that are not met: in the ledgers the run's own commits touched, an
    acceptance line saying owed, not met or unmet. The test is named `heuristic` in `method`.
- **S5** The conformance block. Each item is MET, UNMET or UNJUDGEABLE, and each names its evidence.
  Observed by AC4 and AC12. The items and their rules are:
  - `brief-before-build`: per unit, a brief row and a dispatch row older than its build commit. The
    build commit is the unit's first own non-merge commit touching a path outside the memory root, so a
    spec commit that re-renders a generated index is not a build; the rule is named `heuristic` in
    `method`. UNJUDGEABLE when no unit has one;
  - `phases-walked`: the driver's phase moves include BUILDING before LANDING, or the run aborted. A
    terminal run's phase counts among them at its window's end, since the write that closed the
    window is not a timeline event (S2). UNJUDGEABLE until the run reaches LANDING;
  - `green-at-close`: judged at the last successful `--close` END, one reading `rc=0` and
    `exit=clean`. An unclean END's `rc` is whatever `$?` its EXIT trap saw, often 0, so a `--close`
    killed mid-bar is no close. A joined `gates.log` line with `verdict=GREEN` and `head` equal to the
    head `--close` ran at, older than that END. That head is the first parent of the commit recording
    the close's LANDING write, or HEAD while that write is uncommitted. UNJUDGEABLE when the journal
    holds no successful `--close` or no gate line exists in the window. Every rule in this spec that
    decides on an END's `rc` reads its `exit` beside it, and a source arm of the self-test holds
    `model.py` to that;
  - `keepalive-reaped`: the run-state fact `keepalive-reaped` is present and affirmative. UNJUDGEABLE
    before LANDING;
  - `review-exited`: every review subject's last row carries an exit token. UNJUDGEABLE with no review
    row, and before LANDING while a subject is still open.
- **S6** The anomaly set, a closed list of kinds, each with its trigger and evidence. Observed by AC5.
  - `nonterminal-merged`: the phase is not terminal and the run's last own commit (S3) is an ancestor
    of the default branch. The witness is not the test. It is HEAD at the last verb that writes one,
    which `--phase`, `--landed`, `--abort` and `--preflight` do and `--close` does not, so a run that
    went from preflight to `--close` keeps a witness equal to its base however much it built. The
    sub-class is `refused-landing` when the journal holds a refused `--landed` inside the window, since
    the table cannot see refusals. Otherwise it comes from the table of `TOOL-dLoggedFlight-13` §2 S3,
    cited and not restated.
  - `no-progress`: the phase is not terminal and the run has no own commit after its start commit. For
    a run still in flight this is its state so far, and the evidence names the start commit and the
    window end.
  - `out-of-band-edit`: a START with `oob=1`. A labelled `-source:` repair in the file is kept apart.
  - `refusal-loop`: one verb refused three or more times on one check.
  - `killed-verb`: a START with no END, or an END with `exit=unclean`.
  - `push-outside-lander`: a push line with `lander=0` naming the default branch's ref.
  - `red-behind-zero`: an extractor background bar call whose notification rc was 0, joined by time to
    a `gates.log` line with `verdict=RED`.
  - `destructive-git`: an extractor tool call flagged destructive.
  - `converged-on-blocked`: a review row whose verdict is `BLOCKED` and whose exit is `CONVERGED`.
  - `idle-gap`: fifteen minutes or more that no event of any source covers. The events are the
    timeline's, every event the run's session extracts hold, and each tool call over its whole span,
    from its start to its end, so a long bar or a stretch of workflow calls is busy and never idle.
    Owner turns are not among them, since a turn is the owner's act and not the run's. A stretch runs
    between two events inside the window, never from a window edge. It is judged only when the
    transcripts read `present`, because only then is every tool call seen and every owner turn known.
    Otherwise none fires, and the coverage block says idleness was not judged. A stretch with an owner
    turn inside it, or within fifteen minutes of either end, is kept out and counted. Its endpoints
    would place that turn to within the reply's latency, and owner turns are counts with no clock
    time (`TOOL-dLoggedFlight-9` S4).
  - `multi-run-session`: a session of the run's appearing, inside its window, in the START line of
    another slug's verb.
  - `stalled`: six heartbeat calls, `--status` or `--audit`, in a row with no head or phase change, one hour at the
    declared cadence.
- **S7** The coverage block. Observed by AC6 and AC7. Each source gets a state from
  `COVERAGE_STATES`, and each journal an EPOCH, the time of its producer file's first line:
  - `absent`: the file does not exist, or the window ends before its epoch;
  - `partial`: the window contains the epoch;
  - `present`: the window starts after the epoch, and the source holds lines for the run, or holds
    none while nothing the run's own rows prove required one and this node's driver journal holds
    some of the run's own lines;
  - `dead`: the window starts after the epoch and the source holds none while the run's own rows prove
    activity and this node's driver journal holds some of the run's own lines. The proof is named per
    journal: for `driver` a parked row in the window, since every row
    is a driver verb's write; for `gates` a LANDING write in it, which `--close` makes only after its
    bar; and for `pushes` the move into LANDED, which `--landed` makes only after the push. That move
    is the one that closes a landed run's window (S2), so it lies AT the window's end and never inside
    the half-open window. The pushes proof is therefore read at the end: from the terminal END's
    `phase_to` where a terminal END closed the window, and from the first terminal write's phase where
    that write did;
  - `not-local`: for the transcripts, no named session has an extract or a transcript on this machine,
    or the journal names no session and the store holds no extract attributed to the slug. For a
    journal, the window starts after its epoch, it holds none of the run's lines, and this node's
    driver journal holds none of the run's own lines either, over its whole journal segment (S2),
    inside the window or after it. Journals never leave their clone, so nothing then places the run
    on this node, and neither `present` nor `dead` can be said of a writer for a run it never saw.
    The key is the run's own lines and never a line naming its build, since a build's earlier run
    driven here would place a later one made elsewhere. A writer broken for the whole of a run made
    here reads the same, since the model has no node identity to tell the two apart.

  The run's own lines here are its own ACTS, by S2's session rule: a call of `READ_ONLY_VERBS` is a
  VISIT and places nothing, whatever session made it. Reading the whole segment, one `--status` made
  on a viewing node after another node's run landed was two lines of it, and the run's driver, gates
  and pushes all read `dead` there — the very symptom this state was added to remove. `--resume` and
  `--landed` are acts and do place the run, which is right: a node that resumed or landed a run saw
  it. Observed by AC25.

  The run-state file, git and the build folder read `present` or `absent`. The block also carries
  `idle`: whether idle gaps were judged (S6), how many fired, and how many were kept out near an
  owner turn, with a note naming the transcripts' state when they were not judged.
- **S8** Attribution, within one session, over the tool calls inside the window. An event takes the
  unit of the most recent unit-bearing END, from `--brief`, `--dispatch`, `--rescope` or `--review`,
  and the phase of the most recent END's `phase_to`. A START with no END contributes its `phase_from`
  and no unit. `--status`, `--resume` and every other verb that carries no unit leave the unit where
  it was. The ENDs read are every run's in the session, of any build, so a later END supersedes an
  earlier one whoever made it. An event whose most recent END or START belongs to another run is that
  run's work and is unattributed, and a unit another run's END set is never this run's. An END from a
  session that only READ the run's record is not one of the run's points either, by S2's session rule,
  so a visiting session's `--status` attributes nothing to the run it looked at. An event
  before the session's first END is unattributed. The coverage block reports the share of calls and
  of wall time attributed, and its count of calls is the model's in-window tool calls. Observed by
  AC17, AC23 and AC24.
- **S9** Owner turns by position, each extractor owner turn classed by boundary events. Observed by AC13.
  - `launch`: the session's first owner turn, when it precedes the run's preflight START.
  - `pre-run`: any other turn before that START.
  - `in-window`: from the START to the successful `--close` END of S5.
  - `post-close`: after that END, or after the terminal END when the run has no successful close, or
    after the window's end when it has neither. A killed `--close` is no boundary.

  For a run with no START, its start commit (S1) stands in.
- **S10** Cost: extractor usage totals for the window, split into main loop, direct agents and workflow
  agents. Observed by AC14.
- **S11** The CLI `runlog.py model <slug> [--run <n>] --json` prints the model, and a local copy is
  written beside the extracts. `--journals <dir>` and `--transcripts <dir>` read another directory's
  journals or transcripts. A session whose transcript is local is extracted in memory from it, and
  read from its store extract only where no transcript is, which `TOOL-dLoggedFlight-14` S1 made the
  order and this line used to state the other way round. Observed by AC7.
- **S12** Git cost: the model reads git in a number of calls that does not grow with the run's commit
  or record count. There are six: the run starts' one log (S1) and one ref listing, then one log over
  the own-commit range (S3) carrying bodies and trailers, one log over the build's run-state paths
  carrying name-status, and one `rev-list` of the descendants of the run's start commit with their
  parents. The push join's second key and the merged flag walk that one listing, so a push is tested
  against the own commit it followed (S3) at no extra call. One `cat-file --batch` carries blobs. A
  detached HEAD costs one more. The wall time is printed report-only. Observed by AC8.

  This is a bound on PROCESSES, and S4's split makes that explicit rather than implied: the blob
  VOLUME of that one batch grows with the units times the record commits, because every candidate rev
  of the split is requested before the window that chooses between them is known. Measured on this
  repository's own `dLoggedFlight` at 30 units and 50 record commits, the batch went from 110 requests
  and 1.36 MB to 1580 requests and 18.16 MB, and the whole model from 0.247 s to 0.392 s, at six git
  calls throughout. A cheaper derivation would have to split the batch and cost a seventh.

## 3. Non-goals (OUT)

- Rendering. `TOOL-dLoggedFlight-9` renders the committed record from this model.
- Judging a decision's quality. The ledger says what was decided and where; whether it was right is
  the owner's.
- Cross-run trends over the corpus. That is a follow-up once journals exist on several nodes.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the reader for every journal.
- **consumes-from** `TOOL-dLoggedFlight-2` — the driver's verb, phase, exit and oob lines.
- **consumes-from** `TOOL-dLoggedFlight-3` — the gate verdict lines.
- **consumes-from** `TOOL-dLoggedFlight-4` — the push lines and their gate run ids.
- **consumes-from** `TOOL-dLoggedFlight-6` — the session events, owner turns and usage, where local.
- **consumes-from** `TOOL-dLoggedFlight-7` — the trailer grammar the harvest reads.
- **hands-off** `TOOL-dLoggedFlight-9` — the committed record renders from this model, and reads its
  run starts.
- **hands-off** `TOOL-dLoggedFlight-11` — the push join by what was pushed, which lets the re-render
  after `--landed` see the landing push.
- **hands-off** `TOOL-dLoggedFlight-14` — the session resolution and coverage it reads fresh.
- **hands-off** `TOOL-dLoggedFlight-15` — the anomaly set it holds away from owner turns.
- **hands-off** `TOOL-dLoggedFlight-16` — `resolve_run_sessions` and `COVERAGE_STATES`, which gain the
  freshness test and the `stale` state.
- **hands-off** `TOOL-dLoggedFlight-17` — the transcripts coverage block, which gains `read`, and
  `derive_idle_gaps`' guard, which the refusal mirrors.
- **hands-off** `TOOL-dLoggedFlight-18` — the window's end sources; the window gains `shown_end` and
  keeps S2's bounding rule.
- **hands-off** `TOOL-dLoggedFlight-19` — `derive_idle_gaps`, which holds the idle slots the class
  gate classes.
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill runs `model` and reads its
  coverage block.
- **hands-off** `TOOL-dLoggedFlight-20` — the timeline, window and anomalies, each with the source the record keeps times from.
- **hands-off** `TOOL-dLoggedFlight-21` — `journal_lines`, which `verify` hashes as a time-ordered prefix
  with no floor.
- **hands-off** `TOOL-dLoggedFlight-24` — `derive_window` and `derive_record_commits`, which the model
  calls a second time for `record_window`, the schema leg's git-only window; `RunModel` gains the field.

## 4. Design

Every source reader returns `(items, coverage)`, and the join never fails on a missing source. It
marks the source's state and continues, because the corpus's first 50 runs have no journals at all and
must still model from their run-state files and git.

This run straddles the writers' landing. When its record is rendered before the landing push, `driver`
and `gates` read `partial`, since their files begin inside its window, and `pushes` reads `absent`,
since this node's first push line is the landing push itself.

Push lines join by where they were pushed from or by what they pushed (S3). So the landing push, made
from the primary tree, joins the run it lands, and the landing bar's gate line joins through that push's
pinned `gate_run`. After landing, `pushes` reads `present` for a run whose window starts after the
epoch. A bar run in another worktree at the same minute is never attributed. Nor is a bar or a push
another run makes in the primary tree while this run is open: the run's `--landed` and any `--status`
there claim nothing (S3), so only a pre-close verb of the run's own puts that tree in its key.

### Real-population measurements

Measured on this tree on 2026-09-13 when rev-4 was written, so each rule above is stated with its output
over the population it names. The build pass re-measured them on 2026-09-14 with the model itself, and
each bullet says where the figure moved.

- Rotated builds: 6. Under S1 all six give distinct keys for the archive and the live record, where a
  path's creation commit gives one key for both. Under S2's era rule, each archive's window ends at its
  own terminal write before the rotation, and each live window starts at the rotation. The rev-3 rule,
  which took the first terminal write anywhere in `RUN.md`'s history, ended all six live windows
  before their starts. Re-measured unchanged: six rotated builds of 51 with runs, each pair disjoint.
- Non-terminal records at HEAD: 7. Six have own commits on `origin/main` after their start commits and
  read `nonterminal-merged`: aClosedDocket 4, aCollapsedScan 8, aUnblockedFleet 5, dRatifiedSeam 3,
  dRetiredFork 52 and dSealedTally 8. dRatifiedSeam's witness equals its base because its run went from
  preflight to `--close`, which writes no witness. The seventh is this run, unmerged, whose own commits
  are on its branch, so it reads neither kind. Re-measured unchanged, with the sub-classes
  retired-unit, other, surfaced-park, other, surfaced-park and surfaced-park in that order.
- Parked rows over the tracked run-state files: review 217, decision 139, dispatch 119, rescope 85
  (add 74, retire 10 and supersede 1), brief 79, override 22 and abort 14. The ledger admits 186 and
  keeps out 489. Re-measured over 57 files: dispatch 132 and brief 87, so 510 are kept out. The growth
  is this build's own dispatch and brief rows, which the ledger excludes; the admitted 186 did not move.
- Decision-log spellings: bare `(owner)` 8, `(owner, ` 7 and `(owner:` 1, with "owner ruling" 10 and
  "owner call" 1 in any case. Near-misses of the `(owner<letter>` shape: 0. Re-measured unchanged by
  the report-only arm.
- Journal runs: none on this node yet, since the writers land with this build. So the join from START to
  start commit is exercised by AC18's fixture alone. Re-measured after unit 2: this node's driver
  journal holds 44 of this run's lines and no record-creating preflight, because this run's preflight
  predates its writer. The run therefore models from git with `driver` reading `partial`, and `gates`
  reads `absent` until the post-build gate run writes its first line.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/model.py` | module | none |
| `build_run_model`, `derive_run_starts`, `derive_run_eras`, `read_run_state`, `read_git_range`, `scan_decisions`, `check_conformance`, `scan_anomalies`, `measure_coverage`, `build_owner_positions`, `build_run_usage`, `derive_attribution` | functions | `py.function`, verb-led |
| `run_git`, `read_refs`, `read_blobs`, `read_journals`, `resolve_run_sessions`, `resolve_repo_root`, `scan_owner_spellings`, `render_model_json`, `render_model_summary`, `write_model_copy` and the private helpers | functions | `py.function`, verb-led |
| `RunModel` | type | `py.type` |
| `ANOMALY_KINDS`, `CONFORMANCE_ITEMS`, `CONFORMANCE_STATES`, `COVERAGE_STATES`, `MERGED_SUBCLASSES`, `OWNER_POSITIONS`, `SOURCE_NAMES`, `LEDGER_SOURCES` | closed constants | none |
| `cmd_model` | CLI subcommand | reserved `cmd` |

`SOURCE_NAMES` and `LEDGER_SOURCES` are the vocabularies `TOOL-dLoggedFlight-9` S4 names, spelled here
first so the record renders from the model's own names.

### Files touched (estimate)

`tools/runlog/{model.py,runlog.py,selftest.py,README.md}`, the golden lines in
`tools/runlog/fixtures/golden-lines.txt`, the carried row in `tools/install-prefix-carried.txt` for the
arm that reads the driver's source, and the self-test's budget row. The model's fixtures are built by
the self-test at run time, so no new fixture file is tracked.

### Alternatives rejected

- A run keyed on its run-state path's creation commit: rejected, since rotation modifies `RUN.md`
  rather than adding it, and all six rotated builds resolve both records to one commit.
- A window end at the last commit naming the slug: rejected, since `9fac2b53` names aLeakedHandle three
  days after it landed.
- Attribution by the extractor's sticky last-verb rule alone: rejected. It was measured as an
  unvalidated 93% upper bound, and one run with no `--phase` calls read RUNNING throughout. S8's rule
  keeps the session boundary the sticky rule ignored.
- A raw base-to-witness commit range: rejected, measured at 18% of commits being the run's own.

## 5. Production-readiness checklist

- security — the model holds free text only from tracked, public sources: commit subjects, trailers
  and ids. The extractor contributes none.
- perf / scale — a constant number of git calls, which AC8 counts.
- error / empty / loading states — every source's absence is a coverage state, not an exception. A run
  with no specs models with an empty unit table.
- observability — the coverage block is the model's own liveness statement.
- risks — heuristics in the joins and classifications, each named in the model's `method` field so a
  reader knows which answer is inferred.
- testing — every closed constant drives its fixtures in both directions, each rule is staged on both
  sides of each boundary it names, and an allow-list is staged with its complement. Rotated fixtures are
  built the way the driver rotates, and run-state fixtures the way its verbs leave them.
- migration — none.
- user docs — the kit README's model section, which points at `TREE_BLIND_VERBS` rather than
  listing its members.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `derive_run_starts` reads a fixture build rotated the way the driver rotates, with
  `git mv -f` of the finished record and a fresh `RUN.md` in one commit, the archive and the live record
  get distinct start commits, their half-open windows are disjoint, and neither run is marked
  `joint_add`.
  Red when: both records resolve to one commit, the live window contains the aborted run, or a
  rotation reads as a joint add.
- **AC2** — When `build_run_model` reads a fixture run holding commits naming its units interleaved with
  commits of another build, the timeline carries only its own commits, in time order, beside its phase
  moves. A commit whose subject spells both of a build's units as `X-<slug>-1..2` counts for both: its
  timeline entry and its own-commit entry carry both ids, and it is unit 2's build commit, being
  unit 2's first own commit outside the memory root.
  Red when: the foreign commits enter the run, or a range is read as its first id alone.
- **AC3** — When `scan_decisions` reads a fixture whose commits carry two `Decided:` trailers and one
  mid-body `Decided:` line, and whose specs carry one owner mark committed before the run and one agent
  mark committed inside it, the ledger lists both trailers with their shas and reports one near-miss. It
  counts the marks as owner-before and agent-inside.
  Red when: an owner ruling reads as a decision the run took, or the near-miss is not counted.
- **AC4** — When `check_conformance` reads a fixture unit whose build commit precedes its brief row,
  its `brief-before-build` item reads UNMET and names both times.
  Red when: the order check reads MET.
- **AC5** — When `scan_anomalies` reads fixtures staging each member of `ANOMALY_KINDS` and each member
  of `MERGED_SUBCLASSES`, it reports exactly that kind or sub-class with its evidence. Its run-state
  fixtures are built as the driver's verbs leave them. One is shaped like dRatifiedSeam: the witness
  written once by `--preflight`, `phase: LANDING` written by `--close`, and own commits merged. It reads
  `nonterminal-merged`. So does one whose witness is strictly behind its base with own commits merged.
  One with no own commit after its start reads `no-progress`. One holding both a refused `--landed` and
  a last parked row the table matches reads `refused-landing`. A clean fixture reports none. Every
  member has a fixture, and every fixture's kind is a member.
  Red when: any kind fires on the clean fixture, fails to fire on its own, has no fixture, a stale
  witness hides merged own commits, or the table wins over a refused `--landed`.
- **AC6** — When a fixture journal holds only other runs' lines, a run whose window ends before the
  journal's epoch reads `absent`, one whose window starts after it with twelve parked rows and lines
  of its own after the window reads `dead`, and one whose window contains it reads `partial`. With no
  line of its own anywhere in its segment, a window starting after the epoch reads `not-local`, with
  twelve parked rows or with none. When the run has lines of its own, a window containing the epoch
  still reads `partial`, which is this run's own case, and a window starting after it reads
  `present`. A fixture with no local transcript reads `not-local`. Every member of `COVERAGE_STATES`
  has a fixture, and every fixture's state is a member.
  Through `build_run_model`, the landed fixture staged with a journal older than the run and none of
  the run's own lines reads `dead` for that journal, naming its proof: the driver's by the run's
  parked rows, the gates' with no bar of the run's, and the pushes' with no landing push, both with
  the run's driver lines, where the terminal END closes the window, and without them, where the
  terminal write does. Each case with none of the run's verbs holds the owner's `--status` after the
  landing, a line of the run's segment outside its window. The same fixture staged with older
  journals whose driver lines all name another build reads `not-local` for all three, and so does
  the driver of a rotated build's second run when only its first run was driven here.
  Red when: a dead writer reads as a run that predates it, a window holding the epoch reads `present`
  because the run has lines, any state has no fixture, a landed run whose pre-push writer wrote
  nothing for its landing push reads `present` because its proof sat at the window's end, or a run
  made on another node reads `dead`.
- **AC7** — When `python <kit>/runlog.py model aLeakedHandle --json` runs on this tree, it prints a
  model whose parked-row counts by kind match the run-state file, whose window ends at the commit that
  first wrote `phase: LANDED`, and whose journal sources read `absent`.
  Red when: the counts differ from `memory/builds/aLeakedHandle/RUN.md`, or the window reaches a later
  commit that merely names the slug.
- **AC8** — When `build_run_model` builds fixture runs of 10 and of 100 commits, the count of git
  subprocess calls is the same for both.
  Red when: the git reads go per commit or per file.
- **AC9** — When `build_run_model` reads a fixture run with no preflight START and no parked rows, its
  window starts at its start commit. When a later records commit names the slug, the window end does
  not move.
  Red when: the window is undefined, starts at the witness, or grows with a later mention.
- **AC10** — When `build_run_model` joins a fixture holding two gate lines at the same minute from two
  worktrees and one line whose `run` a push line pinned, only the run's own worktree line and the pinned
  line join. A fixture run landed the way `TOOL-dLoggedFlight-11` S6 lands, merged and pushed from a
  worktree other than its own, joins its landing push line and that push's pinned gate line, and its
  `pushes` source does not read `dead`. Gaps of 15 and 14 minutes yield one `idle-gap`.
  Red when: the other worktree's bar is attributed, the landing push joins no run, or the 14-minute gap
  fires.
- **AC11** — When `scan_decisions` reads a fixture with one row from each ledger source of S4, plus one
  row of each excluded kind (`proposal`, `dispatch`, `brief` and `review`) and a `rescope · item add`
  row, each admitted entry names its file and line or sha, no excluded row enters, and the per-source
  counts equal the fixture's. Decision-log rows spelled `(owner, 2026-09-01)`, bare `(owner)`,
  `(owner: …)`, `Owner ruling` and `owner call` count as the owner's, and a near-miss `(ownership` row
  does not. The report-only arm over the tracked decision log runs and prints one count per spelling.
  Red when: a source is dropped, an excluded row enters, an owner spelling reads as the run's, the
  near-miss counts, or the report-only arm prints nothing.
- **AC12** — When `check_conformance` reads fixtures for each member of `CONFORMANCE_ITEMS` in each
  state it can take, including a close with no gate line in its window, it returns that state. When
  `build_run_model` reads a run whose `--close` END reads `rc=0` and `exit=unclean`, written the way
  the driver's EXIT trap writes a verb killed mid-bar, after a GREEN bar at the head it ran at, the
  run has no close and `green-at-close` reads UNJUDGEABLE. The same END reading `exit=clean` closes
  the run and reads MET. A source arm finds every comparison on an END's `rc` in `model.py` joined, in
  the same condition, to a read of that END's `exit`. A transcript call's `rc`, which no `exit`
  accompanies, is its one exempt receiver, and the exemption reds once it names no comparison.
  Red when: an item has no rule, the no-gate case reads MET, a killed `--close` closes the run, or a
  comparison on an END's `rc` reads no `exit`.
- **AC13** — When `build_owner_positions` reads a fixture with the session's first turn before the
  preflight, a second turn before it, one inside the window, one after the close, and a run with no
  close whose last turn follows its terminal END, each is classed as S9 states. In a run with no START,
  a turn before its start commit reads `launch`, one between the start commit and the window end reads
  `in-window`, and one after the window end reads `post-close`. In AC12's run with a killed `--close`,
  a turn after that END and inside the window reads `in-window`.
  Red when: a turn lands in the class across one of its boundaries, the stand-in included, or a
  killed `--close` END is taken as the close.
- **AC14** — When `build_run_usage` reads extractor usage spanning the window's edges, only usage inside
  the window counts, split three ways.
  Red when: usage outside the window is summed, or the split is lost.
- **AC15** — When `build_run_model` reads a fixture `driver.log` holding a successful preflight, verbs,
  a refused preflight, a second successful preflight and more verbs, it yields two runs whose timelines
  hold exactly their own lines, and the refused preflight starts no run.
  Red when: the live run takes every line of the slug, or the refused preflight starts a run.
- **AC16** — When `build_run_model` reads a fixture terminal record, an archived record and a
  non-terminal record, each window ends at the event S2 names for it. In a LANDED-after-LANDED fixture,
  rotated the way the driver rotates, the archive's window ends at its own terminal write before the
  rotation, and the live window runs from the rotation commit to the live run's own terminal write.
  Red when: a window ends at a slug mention, or a predecessor's terminal write ends a later run's
  window.
- **AC17** — When `derive_attribution` reads a fixture built from the golden driver lines of
  `TOOL-dLoggedFlight-1` §4, with known unit and phase splits, the reported shares equal the fixture's.
  The fixture stages an event before any verb, an event in a second session, a `--phase` move, a killed
  verb, and a heartbeat `--status` between a `--brief` and an event. It then stages, in the same
  session, another build's `--brief` END with an event after it, one more of the run's own verbs with
  an event after that, and an event past the window's end. The event after the other build's END is
  unattributed, the run's next END attributes again but with no unit, and the event past the end is
  not among the calls. Every fixture line carries only the fields its producer's data model lists.
  Red when: the pre-verb event is attributed, another session's END attributes an event, the heartbeat
  resets the unit, the killed verb contributes a unit, an event after another build's END is
  attributed or takes its unit, an event outside the window is counted, or a fixture line carries a
  field its producer never writes.
- **AC18** — When `build_run_model` reads a fixture build with three start commits in git history and
  successful preflights for only the last two in `driver.log`, each START joins the start commit its own
  call made and that commit's runkey, and the first run's window comes from git alone. A START whose
  commit is not in the fixture's history is named in the coverage block and starts no run.
  Red when: a START joins a run by position, or an unmatched START starts a run.
- **AC19** — When `build_run_model` reads a fixture run whose session transcript, extracted by the
  extractor, holds twenty minutes of short tool calls between two timeline events and one
  26-minute foreground call, neither stretch yields an `idle-gap`. A nineteen-minute silence more
  than fifteen minutes from every owner turn yields one. An owner turn closing a silence, one
  opening a silence, and one inside a silence a limit opened keep those three stretches out, and
  the coverage block counts three. With no local transcript the same run yields no `idle-gap`, and
  its coverage reads not judged. Across every model the self-test builds, no idle gap holds a tool
  call's start or overlaps its span.
  Red when: a busy stretch reads idle, a stretch next to an owner turn fires, a git-only run reports
  an idle gap, or an idle gap holds a tool call.
- **AC20** — When `build_run_model` joins the landed fixture, which lands the way
  `TOOL-dLoggedFlight-11` S6 lands, the run's calls in the primary tree are its `--landed`, a
  `--landed` refused before the close, an owner's `--status` and `--resume`, and a `--park` after
  the close. Four foreign lines made there inside the window then join nothing: two bars, a raw push
  refused with `lander=0`, and an `ev=once` refusal. The timeline and `journal_lines` hold none of
  them, and `push-outside-lander` does not fire. The landing push still joins by what it pushed, and
  its pinned bar by its id. When another run's preflight then runs in the run's own worktree, a bar
  made there before it joins and one made after it does not. When the run's own call first claims a
  second worktree mid-window, a bar made there after that call joins and one made before it does not.
  Red when: a line joins through a tree that only one of those calls in the primary tree put in the
  key, a reused worktree's later bar joins, or a tree's bar from before the run claimed it joins.
- **AC21** — When `build_run_model` reads a non-terminal fixture run whose own commit, bar and branch
  push, the last two made in its own worktree, come twenty minutes after its last driver line, the
  window closes one second past the push's END. All three lie inside it, the bar and the push join by
  tree, and the gates source counts the bar. None of these moves that end: a later bar made in the
  primary tree, a bar made in the run's worktree after another run's preflight there, a later merge
  naming only the slug, and a later tool call in the run's session. A record-creating START that
  joins no commit, made between the bar and the push, ends the run's journal lines, so the window
  then closes one second past the bar. With no journal, the window closes one second past the own
  commit, and the merge still moves nothing.
  Red when: the window closes at the last driver line, or a line from a tree the run does not hold,
  a line after the run's journal lines end, a merge naming only the slug, or a transcript event moves
  it.
- **AC22** — When `build_run_model` reads the landed fixture after a later commit on the default
  branch that names one of its unit ids, made after the landing, the run's own commits, its last own
  commit and its merged flag do not move, and the landing push still joins by what it pushed.
  `runlog.py verify` over the record rendered before that commit still reads `match`. When a
  non-terminal fixture pushes the default branch from the primary tree after its merge and then
  makes a later own commit on its branch, that push joins by what it pushed, and a push of the
  default branch made before the run's work reached it joins nothing.
  Red when: a commit after a terminal run's end becomes its last own commit, the landing push stops
  joining, `verify` reads a mismatch that no journal byte caused, or a push is tested against an own
  commit made after it.
- **AC23** — When `build_run_model` reads the landed fixture, its session holds a call after the
  `--landed` END and, inside the window, another build's `--brief` END with a call after it. The first
  call is not among the model's calls, and the second is counted and unattributed. Neither the LANDED
  write after the `--landed` END nor an owner's `--status` after it is on the timeline or among the
  driver lines the record commits to, and the other build's verb in the run's session after its end
  does not count toward `multi-run-session`. On a git-only run whose LANDED write ends its window,
  that write is not on the timeline and `phases-walked` still reads MET. In the non-terminal fixture
  of AC21, the later merge naming only the slug is not on the timeline. Across every model the
  self-test builds, every timeline event lies in `[start, end)` and the attribution's count of calls
  equals the model's tool calls.
  Red when: a call outside the window is counted, a call after another run's END is attributed, an
  event outside the window is on the timeline or counted as sharing a session, `phases-walked` stops
  judging a run by the write that ended it, or the two counts differ.
- **AC24** — `READ_ONLY_VERBS` is a proper subset of `TREE_BLIND_VERBS`, the two differing by
  `--landed` and `--resume`. When `build_run_model` reads the landed fixture whose journal holds a
  second session's in-window `--status`, and a store holding that session's extract with three tool
  calls and an owner turn inside the window, the run names one session, reads one extract, and answers
  exactly as it does over a store holding only its own extract, on sessions, owner positions, usage and
  attribution. With `READ_ONLY_VERBS` emptied the visitor joins and brings exactly the owner turns and
  calls its own acts made. When the non-terminal fixture's journal holds a foreign `--status` an hour
  after its last act, the window end does not move and the session is not named; emptied, that one
  visit stretches the window to itself. Six `--audit` heartbeats of the run's own, recording no
  session as the shipped default does, are its events: the window reaches them and `stalled` fires.
  The same six from a session the run never named move nothing and fire nothing.
  Red when: a read-only visit names a session, moves a non-terminal end, or contributes an
  attribution point; or the run's own session-less heartbeats stop being its events.
- **AC25** — When `build_run_model` reads the landed fixture whose three journals were kept through
  the run and hold nothing but another build's older lines, plus one post-landing `--status` made on
  the viewing node, every journal reads `not-local` with no proof. With the run's own `--park` in
  that same slot, all three read `dead` and name their proof, so the verb is all that differs. With
  `READ_ONLY_VERBS` emptied the read reads `dead` again, which is L2's own symptom. Both staged
  pairs hold the same number of lines and lie outside the window.
  Red when: a read-only visit places a run on this node, or an act stops placing one.
- **AC26** — When `build_run_model` reads a landed fixture whose unit's spec gains one section 8
  `RESOLVED` mark at a commit inside its window, the ledger holds one `inside` spec mark. With the
  same mark committed after the window's end it holds none, and with the mark carried from before
  the run it holds one `before`. All three cost six git calls, and all three carry the mark at HEAD
  with windows closing at the same end.
  Red when: a mark committed after the run counts as decided inside it, a mark the run inherited
  counts as its own, an in-window mark stops counting, or the split costs a git call.

## 7. Gates

`lexicon naming predicates` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

- **F1** How many heartbeats with no change make a run `stalled`? RESOLVED (agent, 2026-09-13,
  delegated): six, which is one hour at the declared ten-minute cadence, stored as a model constant
  and printed in the anomaly's evidence so a reader can see the rule.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S2 S3 S4 S5 S6 S7 S8 S10 · §4 · AC3 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC13
  AC14 · folded round-1 spec audit. B1: each journal gets an epoch and a `partial` state, and AC7 reads
  `absent` by epoch. B2's model half: a run with no START starts at its run-state file's creating
  commit. H6: the joins gain a criterion. M6: every anomaly kind is defined. M7: every conformance item
  gets a rule. M8 and M9: every ledger source and owner spelling gains a criterion. M11: the near-miss
  count. M14 and M15: owner positions and cost. H9: git calls are counted. L2: the hand-off to unit 12.
- rev-3 · 2026-09-13 · S1 S2 S4 S6 S7 S8 S9 S12 · §4 · AC1 AC5 AC6 AC7 AC9 AC11 AC13 AC15 AC16 AC17 ·
  folded round-2 spec audit. B1: runs are keyed on the commit that started them, since rotation
  modifies `RUN.md` (TOOL-dClosedLexicon-11). H1: window ends come from the run's own events, never a
  slug mention. H2's model half: the pre-push render's coverage is stated. H4: a witness at or behind
  its base is the kind `no-progress`, never merged (TOOL-cFinalBerth-2). M4: the bare `(owner)` spelling. M5: journal
  segmentation. M6: sub-classes cite unit 13's table. M7: the position boundaries. M8: the attribution
  rule. M9: every coverage state and sub-class is pinned. L5: the four owed kinds and two owed acts.
- rev-4 · 2026-09-13 · S1 S2 S3 S4 S6 S8 S12 · §4 · AC1 AC5 AC6 AC10 AC11 AC13 AC16 AC17 AC18 · folded
  round-3 spec audit. H1: progress comes from the run's own commits, since `--close` writes no witness.
  H2: windows are half-open and bounded to the run's era. H3: a push joins by what it pushed, so the
  landing push from the primary tree joins. H4: a START joins its start commit by a named key. M1:
  attribution reads END. M4, M8, M9, L1 and L2: the unstaged side of each rule gains a fixture. M11: the
  owed sets are held to the driver's source. M12: the memory root is resolved. L3: the population form
  of `derive_run_starts`.
- rev-5 · 2026-09-14 · S2 S4 S5 S7 S11 S12 · §4 · the build pass. S2: the terminal END is the verb
  that moved the phase INTO a terminal one, because a `--status` after a landing reads LANDED on both
  of its lines, and the AC7 arm saw it end aLeakedHandle's window three days late. A non-terminal
  window closes one second past its last event, so that event is inside it. S4: the review source is
  the review records the era added, each with its verdict line, and an unmet ledger line is a
  heuristic. S5: each item names its UNJUDGEABLE condition, and the build commit and the close's head
  are derived as stated; a build commit keyed on the build folder read every spec commit that
  re-renders the index as a build. S7: `present` covers a live source nothing was owed to, and dead's
  proof is named per journal, since rev-4 left a live source with no lines and no proof in no state.
  S11 gains `--journals` and `--transcripts`, and S12 counts its six processes. §4's figures are
  re-measured.
- rev-6 · 2026-09-14 · S3 S6 S7 · AC19 · folded the closing diff review's round-1 B1 and H1. H1: an
  idle gap is judged over every source, with a tool call covering its whole span, and only where the
  transcripts read `present`. Rev-5 judged gaps over the timeline alone, which read every busy
  stretch of this run as idle. B1: owner turns are not events of a gap, and a stretch within fifteen
  minutes of one is kept out and counted. A gap's start or end had placed an owner turn to the
  second, and dropping the turn alone would still place it to within the reply's latency. The
  review also proposed judging where the driver journal reads `present` or `partial`. Its verbs are
  already timeline events and it knows no owner turn, and a `partial` transcript hides a session's
  calls, so neither is enough to judge by.
- rev-7 · 2026-09-14 · S2 S3 · §4 · AC20 AC21 · folded the closing diff review's round-1 H2 and M5.
  H2: the join key by tree is the trees a run HOLDS. A tree is held from the run's first call there
  that claims it, which no `--status`, `--resume` or `--landed` does, and neither does any verb run
  after the close. It stops being held at another run's first claim there after the run's last one.
  Rev-6 keyed on every tree any of the run's calls ran in, so a `--landed` or an owner's `--status`
  in the primary tree made every bar and push there the run's for its whole window. M5: a
  non-terminal window closes one second past the run's last event over every source it owns: its
  journal lines, its record commits, its own commits, and the lines of the trees it holds. Rev-5
  read the first two alone, so this run's later commits and both of its bars fell outside its own
  window. The review also listed the merges naming the slug. S2 already takes no bound from a commit
  that merely names the slug, and such a merge is one, so only an own commit moves the end, a merge
  naming a unit id included. The review also proposed bounding a tree that has to stay in the key
  to the span between its first and last pre-close verb. A hold ending at the last verb would put the
  run's bars after that verb outside the window, which is the M5 defect, so the hold ends at the next
  run's claim instead. That bound still covers the tree the review meant, since the primary tree
  stays in the key only where the run's own pre-close verbs ran there. Transcript events are not a
  source of the end, because the session renders the record itself.
- rev-8 · 2026-09-14 · S2 S3 S5 S6 S8 S12 · AC17 AC22 AC23 · folded the closing diff review's round-1
  M1, M4 and M5's timeline bound, as one window discipline. S2: every set the model derives from a
  timed source is bounded by the window through one predicate. Rev-7 bounded some sets by the window,
  some by the era and some by nothing, so the record listed a merge made after its own end. S3 (M4):
  own commits are bounded by the window, and a push is tested against the last own commit made at or
  before its START. A commit naming a unit id after a landing had become the run's last own commit,
  unjoined the landing push, and made `verify` report a journal that had not changed. S8 (M1):
  attribution counts only the calls inside the window and reads every run's ENDs in the session. It
  had counted every call of every named session, and another build's later END never superseded the
  run's own. S5: the closing phase write is no longer a timeline event, so `phases-walked` reads a
  terminal run's phase at its end. S6: `multi-run-session` is bounded like every other set. S12: the
  fifth git call lists the start's descendants with their parents, so each push walks to the own
  commit it followed at no extra call. Not folded: S4's spec-mark split still reads each spec at the
  era's end, not the window's. That end needs the one blob read that places a terminal write, so
  bounding the split changes S12's calls, and it is left to round 2.
- rev-9 · 2026-09-14 · S5 S7 S9 · AC6 AC12 AC13 · folded the closing diff review's round-1 M2 and M3.
  M2: `pushes` could never read `dead`. Its proof was a LANDED move inside the window, and the window
  of a landed run ends at exactly that move, at its terminal END or its first terminal write, which a
  half-open window excludes. S7 now reads the pushes proof at the window's end, from the move that
  closed it. The `gates` proof is a LANDING write, which lies inside the window, so it stands. AC6
  gains a dead state staged through the model for each journal, since only the passing side was
  observed. M3: a `--close` END reading `rc=0` and `exit=unclean` counted as the close, so
  `green-at-close` could read MET with no LANDING ever written, and the END split in-window from
  post-close owner turns. The driver documents that an unclean END's `rc` is whatever its EXIT trap
  saw, and every other rule reading an `rc` already read `exit` beside it. S5 defines a successful
  close as `rc=0` with `exit=clean`, S9 takes its boundary from that close alone, and AC12 and AC13
  observe both, with a source arm over every comparison on an END's `rc`. The review also offered a
  close that moved the phase into LANDING as the test. A killed `--close` whose END read LANDING had
  written the phase and not finished, so the clean exit is the one test, as it is for every other
  rule here.
- rev-10 · 2026-09-14 · S1 S3 S7 · AC1 AC2 AC6 · folded the closing diff review's round-1 L2, L3
  and L5. L2: a run made on another node read `dead` for its driver, and for its gates and pushes
  once it had closed or landed. Journals never leave their clone, so its lines are nowhere here,
  and the model has no node identity. S7 now reads `present` and `dead` only where this node's
  driver journal holds some of the run's own lines, over its whole segment, and `not-local`
  otherwise, and the runlog Skill says so where it had said such journals read `absent`. The review
  proposed keying on any line naming the build. The fold's bug-class checklist named that key's
  shape, a location every run of the build shares: a build's earlier run driven here would place a
  later one made elsewhere, so the key is the run's own segment. The review also offered changing
  the Skill's text alone, and a `dead` that cannot be told from another node's run misleads whatever
  the Skill says. L3: a memory root moved in one commit adds the live record and every archive at
  once, so every run of a rotated build started at the move. S1 marks a run whose start added both,
  and the schema leg's refusal names the shape (`TOOL-dLoggedFlight-10` rev-7). Following the
  pre-move path was not taken. Every read the model makes is keyed on a path under the current root,
  the run-state history, its blobs, the specs, the ledgers and the decision log among them, so
  following the starts alone would turn a loud refusal into windows that are quietly wrong. L5:
  `TOOL-dLoggedFlight-1..13` read as unit 1 alone, which credited eight whole-set commits of this
  build to unit 1 on the timeline. S3 reads a range the way the index generator does, bounded by
  `UNIT_RANGE_MAX`, a bound the generator does without because an author types its Serves line.
- rev-11 · 2026-09-16 · S3 · S6 · the second origin/main reconcile: main added `--audit`, the stall probe the keepalive
  tick now runs. It reads the record like `--status`, so it claims no tree, and it is a heartbeat
  for `stalled`. The AC20 fixture takes it from `TREE_BLIND_VERBS`, and AC5 gains two stalled
  streaks, one of `--audit` and one mixed.
- rev-12 · 2026-09-16 · §3 · the edges to `TOOL-dLoggedFlight-14` and `-15`, the units closing
  review round 2 promoted at its NON-CONVERGENT exit.
- rev-13 · 2026-09-16 · §3 · the edges to `TOOL-dLoggedFlight-16` to `-19`, the units the spec audit
  of units 14 and 15, round 1, promoted at its BOUNDED exit. The edge to `-15` drops the window end,
  which moved to `-18`.
- rev-14 · 2026-09-16 · §3 · the edge to `TOOL-dLoggedFlight-20`: the owner's ruling of 2026-09-16
  keeps every journal and transcript time out of the committed record.
- rev-15 · 2026-09-16 · §3 · the edges to `TOOL-dLoggedFlight-21` and `-24`, units the spec audit of
  units 14, 16 and 20, round 1, promoted at its BOUNDED exit. `journal_lines`, the model's `window` and
  S2's bounding rule do not change.
- rev-16 · 2026-09-20 · S11 · §5 · folded R2-L4 of the closing diff review, round 2, and the staleness
  `TOOL-dLoggedFlight-14`'s pass found in S11. R2-L4: the kit README twice and the map dossier once
  listed three tree-blind verbs after rev-11 added `--audit` to the constant, so an adopter read that a
  keepalive tick's `--audit` claims a tree. All three now point at `TREE_BLIND_VERBS`, the way
  `METHOD["trees"]` already does, and no copy is left to gate. S11 stated the source order unit 14
  inverted.
- rev-17 · 2026-09-20 · S2 S8 · AC24 · folded R2-M1 of the closing diff review, round 2: a read-only
  visit joined the run's sessions. Rev-11 made `--status`, `--resume`, `--landed` and `--audit` blind
  for TREES and left all four naming SESSIONS, so another Claude session that ran `--status` on the
  run became one of its sessions, and its owner turns, usage and tool calls became the run's — in the
  facts that answer "what did it decide without asking me", with the in-window owner count committed.
  For a non-terminal window the same visit moved the end past itself, so it always landed inside the
  window it moved, and a stalled run visited days later stretched its whole window to the visit.
  Naming a session and claiming a tree are different questions, so S2 declares a SECOND constant,
  `READ_ONLY_VERBS`, a proper subset holding `--status` and `--audit`: `--resume` continues the run
  and `--landed` lands it, and both are the run's own acts. S8's attribution points follow the same
  rule. The review's finders proposed dropping every read from the end. A read with no session
  recorded is the keepalive tick's `--audit` on the shipped default, where `RUNLOG_SESSION_VARS` is
  blank, so that spelling would put a stalled run's heartbeats outside its own window and `stalled`
  could never fire; AC24 observes both halves. The park the unit 8 acceptance ledger left on this
  key is struck there, its first reason — that no review had confirmed it — spent.
- rev-18 · 2026-09-20 · S7 · AC25 · folded R2-L1 of the closing diff review, round 2: a visit placed
  another node's run here. Rev-10 keyed `not-local` on the run's own driver lines over its whole
  journal segment, and counted every call in it. A read-only visit is not one of the run's own lines,
  so a `--status` made on a viewing node after another node's run had landed put two lines in that
  segment and made its driver, gates and pushes read `dead` — L2's own symptom, reintroduced by one
  read, and lasting for ever because the last run of a build has an open segment. The count is now
  the run's ACTS, by S2's rule, so `--resume` and `--landed` still place a run on the node that
  resumed or landed it. The unit 8 acceptance ledger's residue on this is closed there, and the kit
  README's sentence saying a `--status` made here places another node's run is REPLACED rather than
  answered beside.
- rev-19 · 2026-09-20 · S4 S12 · AC26 · folded R2-L2 of the closing diff review, round 2: the
  spec-mark split read the era, not the window. Rev-8 left it there and gave a reason — that bounding
  it would change S12's calls — which round 2 refuted and this fold confirms: S12 counts PROCESSES,
  and every candidate rev rides the one `cat-file --batch`. The split is now taken at the last record
  commit at or before the window's end, so a `RESOLVED` mark added to a spec after the run is counted
  neither before it nor inside it; for a build's last run the era is open to HEAD, so every later
  edit of one of its specs had counted as the run's own decision, in a committed fact. What the fold
  does buy is BLOB VOLUME, units times record commits, and S12 now states that bound and the figures
  measured for it rather than leaving "constant git cost" to be read as constant cost. The split's
  granularity is a record commit, so a mark made inside the window but after the run's last record
  commit reads as neither; S4 says so.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "join run state git and journals into one run timeline"` found no
joiner. The nearest readers are the unattended driver's `--plan` region reader and drift-audit's git
helpers. The model reads the run-state file's own row grammar, `<ts> <kind> · item <item> · reason
<reason>`, as the driver writes it at `tools/unattended/unattended.sh:3911-3920`, and does not copy
the driver's parser. No existing seam fits.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

# TOOL-dLoggedFlight-8 — the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set

**Status:** SPECCED · rev-4 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

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
  read through `resolve_memory_root` of `TOOL-dLoggedFlight-1`, never a `memory/` literal. Observed by
  AC1, AC9 and AC18.
- **S2** Run windows. A window is half-open, `[start, end)`, and every read of a run-state path's
  history is bounded to the run's era (S1). Rotation keeps the path, so `RUN.md`'s history carries
  every predecessor's terminal write. An archive's own terminal write is read from `RUN.md` inside the
  archive's era, since its bytes lived there until rotation. A window starts at the run's preflight
  START in `driver.log`, or at its start commit when there is none. It ends at the first of these that
  applies:
  - the run's terminal END in `driver.log`;
  - for a terminal record, the first commit in its era that wrote a terminal `phase:`;
  - for a non-terminal record, the later of its last journal line and the last commit in its era that
    touched `RUN.md`.

  Journal STARTs join git's runs by a named key, never by position. A successful record-creating
  `--preflight` START, paired with an END of `rc=0`, belongs to the start commit its own call made: the
  first start commit of its slug at or after that END. The run's journal lines run from that START to
  the next such START. A START that joins no start commit, as when its commit never reached this clone,
  is named in the coverage block and starts no run, and a refused preflight starts no run. No bound is
  taken from a commit that merely names the slug: commits keep naming a slug after its run ends.
  Observed by AC1, AC9, AC15, AC16 and AC18.
- **S3** The timeline. Observed by AC2 and AC10. It holds:
  - phase moves with their time and witness;
  - every driver verb with its rc, `exit` and checks;
  - the run's own commits: commits inside its era that descend from its start commit and name one of
    its unit ids, read from its `branch-ref:` where that ref resolves and from the default branch. A
    raw base-to-witness range was measured to be 82% other work, and the witness can be stale (S6), so
    neither bounds them;
  - merges naming the slug;
  - push lines, joined by where they were pushed from OR by what they pushed. A line made from the
    run's worktree inside the window joins, and so does one inside the window that pushes the default
    branch's ref to a local sha with the run's last own commit in its history. The second key is how
    the landing push joins: the protocol's lander pushes from the primary tree
    (`TOOL-dLoggedFlight-11` S6), so a run spans its own worktree and that landing;
  - gate lines, joined exactly by `run=` where a joined push line pinned `gate_run`, and otherwise by
    the run's worktree inside the window;
  - unit dispatches and briefs;
  - from the extractor where local: owner turns, compactions, limits and idle gaps of 15 minutes or
    more.
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
  - review rounds with their verdict path;
  - `Decided:` trailers from the run's commits (`TOOL-dLoggedFlight-7`), plus a near-miss count of body
    lines beginning `Decided:` that git did not parse as trailers;
  - spec section 8 marks split by resolver, owner or agent, and by whether the commit that introduced
    them falls inside the window;
  - `memory/DECISIONS.md` rows the run's commits added, classified as the owner's when they carry
    `(owner` followed by `)`, `,` or `:`, or the phrase "owner ruling" or "owner call" in any case. The
    classification is named `heuristic` in the model's `method` field. A report-only arm prints its
    hits per spelling and its near-misses over the tracked decision log;
  - acceptance-ledger lines that are not met.
- **S5** The conformance block. Each item is MET, UNMET or UNJUDGEABLE, and each names its evidence.
  Observed by AC4 and AC12. The items and their rules are:
  - `brief-before-build`: per unit, a brief row and a dispatch row older than its build commit;
  - `phases-walked`: the driver's phase moves include BUILDING before LANDING, or the run aborted;
  - `green-at-close`: a `gates.log` line with `verdict=GREEN` and `head` equal to the head `--close`
    ran at, older than the `--close` END. UNJUDGEABLE when no gate line exists in the window;
  - `keepalive-reaped`: the run-state fact `keepalive-reaped` is present and affirmative;
  - `review-exited`: every review subject's last row carries an exit token.
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
  - `idle-gap`: fifteen minutes or more with no event of any source.
  - `multi-run-session`: one session id appearing in the START lines of two slugs' runs.
  - `stalled`: six heartbeat `--status` calls in a row with no head or phase change, one hour at the
    declared cadence.
- **S7** The coverage block. Observed by AC6 and AC7. Each source gets a state from
  `COVERAGE_STATES`, and each journal an EPOCH, the time of its producer file's first line:
  - `absent`: the file does not exist, or the window ends before its epoch;
  - `partial`: the window contains the epoch;
  - `present`: the window starts after the epoch and the source holds lines for the run;
  - `dead`: the window starts after the epoch and the source holds none while the run's own rows prove
    activity;
  - `not-local`: the transcripts are not on this machine.
- **S8** Attribution, within one session. An event takes the unit of the most recent unit-bearing END,
  from `--brief`, `--dispatch`, `--rescope` or `--review`, and the phase of the most recent END's
  `phase_to`. A START with no END contributes its `phase_from` and no unit. `--status`, `--resume` and
  every other verb that carries no unit leave the unit where it was. An event before the session's
  first END is unattributed. The coverage block reports the share of calls and of wall time
  attributed. Observed by AC17.
- **S9** Owner turns by position, each extractor owner turn classed by boundary events. Observed by AC13.
  - `launch`: the session's first owner turn, when it precedes the run's preflight START.
  - `pre-run`: any other turn before that START.
  - `in-window`: from the START to the `--close` END.
  - `post-close`: after the `--close` END, or after the terminal END when the run has no close.

  For a run with no START, its start commit (S1) stands in.
- **S10** Cost: extractor usage totals for the window, split into main loop, direct agents and workflow
  agents. Observed by AC14.
- **S11** The CLI `runlog.py model <slug> [--run <n>] --json` prints the model, and a local copy is
  written beside the extracts. Observed by AC7.
- **S12** Git cost: the model reads git in a number of calls that does not grow with the run's commit
  or record count. One log over the own-commit range (S3) carries bodies and trailers, one log over
  the build's run-state paths carries name-status, and one `rev-list` of the descendants of the run's
  last own commit gives the push join its second key. One `cat-file --batch` carries blobs. The wall
  time is printed report-only. Observed by AC8.

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
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill runs `model` and reads its
  coverage block.

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
epoch. A bar run in another worktree at the same minute is never attributed.

### Real-population measurements

Measured on this tree on 2026-09-13 when rev-4 was written, so each rule above is stated with its output
over the population it names. The build pass re-measures them.

- Rotated builds: 6. Under S1 all six give distinct keys for the archive and the live record, where a
  path's creation commit gives one key for both. Under S2's era rule, each archive's window ends at its
  own terminal write before the rotation, and each live window starts at the rotation. The rev-3 rule,
  which took the first terminal write anywhere in `RUN.md`'s history, ended all six live windows
  before their starts.
- Non-terminal records at HEAD: 7. Six have own commits on `origin/main` after their start commits and
  read `nonterminal-merged`: aClosedDocket 4, aCollapsedScan 8, aUnblockedFleet 5, dRatifiedSeam 3,
  dRetiredFork 52 and dSealedTally 8. dRatifiedSeam's witness equals its base because its run went from
  preflight to `--close`, which writes no witness. The seventh is this run, unmerged, whose own commits
  are on its branch, so it reads neither kind.
- Parked rows over the tracked run-state files: review 217, decision 139, dispatch 119, rescope 85
  (add 74, retire 10 and supersede 1), brief 79, override 22 and abort 14. The ledger admits 186 and
  keeps out 489.
- Decision-log spellings: bare `(owner)` 8, `(owner, ` 7 and `(owner:` 1, with "owner ruling" 10 and
  "owner call" 1 in any case. Near-misses of the `(owner<letter>` shape: 0.
- Journal runs: none on this node yet, since the writers land with this build. So the join from START to
  start commit is exercised by AC18's fixture alone, and the build pass re-measures it once unit 2
  lands.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/model.py` | module | none |
| `build_run_model`, `derive_run_starts`, `derive_run_eras`, `read_run_state`, `read_git_range`, `scan_decisions`, `check_conformance`, `scan_anomalies`, `measure_coverage`, `build_owner_positions`, `build_run_usage`, `derive_attribution` | functions | `py.function`, verb-led |
| `RunModel` | type | `py.type` |
| `ANOMALY_KINDS`, `CONFORMANCE_ITEMS`, `COVERAGE_STATES`, `MERGED_SUBCLASSES`, `OWNER_POSITIONS` | closed constants | none |
| `cmd_model` | CLI subcommand | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{model.py,runlog.py,selftest.py,README.md}`, fixtures under `tools/runlog/fixtures/`,
and the carried row in `tools/install-prefix-carried.txt` for the arm that reads the driver's source.

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
- user docs — the kit README's model section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `derive_run_starts` reads a fixture build rotated the way the driver rotates, with
  `git mv -f` of the finished record and a fresh `RUN.md` in one commit, the archive and the live record
  get distinct start commits, and their half-open windows are disjoint.
  Red when: both records resolve to one commit, or the live window contains the aborted run.
- **AC2** — When `build_run_model` reads a fixture run holding commits naming its units interleaved with
  commits of another build, the timeline carries only its own commits, in time order, beside its phase
  moves.
  Red when: the foreign commits enter the run.
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
  journal's epoch reads `absent`, one whose window starts after it with twelve parked rows reads
  `dead`, and one whose window contains it reads `partial`. When the run has lines of its own, a window
  containing the epoch still reads `partial`, which is this run's own case, and a window starting after
  it reads `present`. A fixture with no local transcript reads `not-local`. Every member of
  `COVERAGE_STATES` has a fixture, and every fixture's state is a member.
  Red when: a dead writer reads as a run that predates it, a window holding the epoch reads `present`
  because the run has lines, or any state has no fixture.
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
  state it can take, including a close with no gate line in its window, it returns that state.
  Red when: an item has no rule, or the no-gate case reads MET.
- **AC13** — When `build_owner_positions` reads a fixture with the session's first turn before the
  preflight, a second turn before it, one inside the window, one after the close, and a run with no
  close whose last turn follows its terminal END, each is classed as S9 states. In a run with no START,
  a turn before its start commit reads `launch`, one between the start commit and the window end reads
  `in-window`, and one after the window end reads `post-close`.
  Red when: a turn lands in the class across one of its boundaries, the stand-in included.
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
  verb, and a heartbeat `--status` between a `--brief` and an event. Every fixture line carries only the
  fields its producer's data model lists.
  Red when: the pre-verb event is attributed, another session's END attributes an event, the heartbeat
  resets the unit, the killed verb contributes a unit, or a fixture line carries a field its producer
  never writes.
- **AC18** — When `build_run_model` reads a fixture build with three start commits in git history and
  successful preflights for only the last two in `driver.log`, each START joins the start commit its own
  call made and that commit's runkey, and the first run's window comes from git alone. A START whose
  commit is not in the fixture's history is named in the coverage block and starts no run.
  Red when: a START joins a run by position, or an unmatched START starts a run.

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

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "join run state git and journals into one run timeline"` found no
joiner. The nearest readers are the unattended driver's `--plan` region reader and drift-audit's git
helpers. The model reads the run-state file's own row grammar, `<ts> <kind> · item <item> · reason
<reason>`, as the driver writes it at `tools/unattended/unattended.sh:3911-3920`, and does not copy
the driver's parser. No existing seam fits.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

# TOOL-dLoggedFlight-8 — the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set

**Status:** SPECCED · rev-2 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A run's evidence is spread across its run-state file, three journals, git, the build folder and, where
local, its transcripts. Join them into one model of one run: what it did and when, what it decided,
what it cost, whether it followed the method, what looks wrong, and how much of each answer the
sources actually support. Every later surface renders from this model rather than re-deriving it.

## 2. Scope (IN)

- **S1** Run segmentation and the window. A slug's runs are separated by the driver's successful
  record-creating `--preflight` calls and their pinned bases, and a rotated `RUN.<phase>.<8hex>.md` is a
  run of its own. A run's window starts at its preflight START. With none, it starts at the commit
  that created its run-state file, found with `git log --diff-filter=A --follow`. It ends at its
  terminal END, or at the last line or commit naming its slug. Observed by AC1 and AC9.
- **S2** The timeline. Observed by AC2 and AC10. It holds:
  - phase moves with their time and witness;
  - every driver verb with its rc, `exit` and checks;
  - the run's own commits, meaning first-parent commits on the run branch that name one of its unit
    ids, since a raw base-to-witness range was measured to be 82% other work;
  - merges naming the slug;
  - gate lines, joined exactly by `run=` where a push line pinned `gate_run`, and otherwise by worktree
    inside the window;
  - push lines, unit dispatches and briefs;
  - from the extractor where local: owner turns, compactions, limits and idle gaps of 15 minutes or
    more.
- **S3** The decision ledger. Observed by AC3 and AC11. Each entry points at its source, a file and
  line or a sha. It holds:
  - parked decisions, rescope acts and overrides from the run-state file;
  - review rounds with their verdict path;
  - `Decided:` trailers from the run's commits (`TOOL-dLoggedFlight-7`), plus a near-miss count of body
    lines beginning `Decided:` that git did not parse as trailers;
  - spec section 8 marks split by resolver, owner or agent, and by whether the commit that introduced
    them falls inside the window;
  - `memory/DECISIONS.md` rows the run's commits added, classified as the owner's when they carry any
    observed owner spelling: an `OWNER RULING` prefix, `(owner, <date>)`, `(owner:` or "owner call".
    The classification is named `heuristic` in the model's `method` field;
  - acceptance-ledger lines that are not met.
- **S4** The conformance block. Each item is MET, UNMET or UNJUDGEABLE, and each names its evidence.
  Observed by AC4 and AC12. The items and their rules are:
  - `brief-before-build`: per unit, a brief row and a dispatch row older than its build commit;
  - `phases-walked`: the driver's phase moves include BUILDING before LANDING, or the run aborted;
  - `green-at-close`: a `gates.log` line with `verdict=GREEN` and `head` equal to the head `--close`
    ran at, older than the `--close` END. UNJUDGEABLE when no gate line exists in the window;
  - `keepalive-reaped`: the run-state fact `keepalive-reaped` is present and affirmative;
  - `review-exited`: every review subject's last row carries an exit token.
- **S5** The anomaly set, a closed list of kinds, each with its trigger and evidence. Observed by AC5.
  - `nonterminal-merged`: the phase is not terminal and the witness is an ancestor of the default
    branch. Sub-classes follow `TOOL-dLoggedFlight-13`: `surfaced-park`, `retired-unit`, `no-rows` and
    `other`, plus `refused-landing` when the journal holds a refused `--landed`.
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
- **S6** The coverage block. Observed by AC6 and AC7. Each source gets a state, and each journal an
  EPOCH, the time of its producer file's first line:
  - `absent`: the file does not exist, or the window ends before its epoch;
  - `partial`: the window contains the epoch;
  - `present`: the window starts after the epoch and the source holds lines for the run;
  - `dead`: the window starts after the epoch and the source holds none while the run's own rows prove
    activity;
  - `not-local`: the transcripts are not on this machine.

  It also gives the share of calls and of wall time attributed to a unit and a phase.
- **S7** Owner turns by position: each extractor owner turn is classed `launch`, `pre-run`, `in-window`
  or `post-close` against the window and the `--close` END. Observed by AC13.
- **S8** Cost: extractor usage totals for the window, split into main loop, direct agents and workflow
  agents. Observed by AC14.
- **S9** The CLI `runlog.py model <slug> [--run <n>] --json` prints the model, and a local copy is
  written beside the extracts. Observed by AC7.
- **S10** Git cost: the model reads git in a number of calls that does not grow with the run's commit
  or record count, one log over the range with bodies and trailers and one `cat-file --batch` for
  blobs. The wall time is printed report-only. Observed by AC8.

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
- **hands-off** `TOOL-dLoggedFlight-9` — the committed record renders from this model.
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill runs `model` and reads its
  coverage block.

## 4. Design

Every source reader returns `(items, coverage)`, and the join never fails on a missing source. It
marks the source's state and continues, because the corpus's first 50 runs have no journals at all
and must still model from their run-state files and git. This run itself straddles the writers'
landing, so its journals read `partial`, and its record says so.

Gate and push lines join by worktree inside the window. A pinned `gate_run` joins exactly, so a bar run
in another worktree at the same minute is never attributed.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/model.py` | module | none |
| `build_run_model`, `read_run_state`, `read_git_range`, `scan_decisions`, `check_conformance`, `scan_anomalies`, `measure_coverage`, `build_owner_positions`, `build_run_usage` | functions | `py.function`, verb-led |
| `RunModel` | type | `py.type` |
| `ANOMALY_KINDS`, `CONFORMANCE_ITEMS`, `COVERAGE_STATES` | closed constants | none |
| `cmd_model` | CLI subcommand | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{model.py,runlog.py,selftest.py,README.md}` and fixtures under `tools/runlog/fixtures/`.

### Alternatives rejected

- Attribution by the extractor's sticky last-verb rule alone: rejected. It was measured as an
  unvalidated 93% upper bound, and one run with no `--phase` calls read RUNNING throughout.
- A raw base-to-witness commit range: rejected, measured at 18% of commits being the run's own.
- Splitting owner rulings on the `OWNER RULING` prefix alone: rejected, since 8 decision-log lines carry
  it against 16 carrying `(owner`.

## 5. Production-readiness checklist

- security — the model holds free text only from tracked, public sources: commit subjects, trailers
  and ids. The extractor contributes none.
- perf / scale — a constant number of git calls, which AC8 counts.
- error / empty / loading states — every source's absence is a coverage state, not an exception. A run
  with no specs models with an empty unit table.
- observability — the coverage block is the model's own liveness statement.
- risks — heuristics in the joins and classifications, each named in the model's `method` field so a
  reader knows which answer is inferred.
- testing — the closed kind, item and state lists each drive their fixtures in both directions, plus
  one model of a real past run.
- migration — none.
- user docs — the kit README's model section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `build_run_model` reads a fixture slug holding a rotated aborted record and a live one,
  it returns two runs whose facts come from their own files.
  Red when: the rotated record merges into the live run.
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
- **AC5** — When `scan_anomalies` reads fixtures staging each member of `ANOMALY_KINDS`, it reports
  exactly that kind with its evidence, and a clean fixture reports none. Every member has a fixture,
  and every fixture's kind is a member.
  Red when: any kind fires on the clean fixture, fails to fire on its own, or has no fixture.
- **AC6** — When a fixture journal holds only other runs' lines, a run whose window ends before the
  journal's epoch reads `absent`, one whose window starts after it with twelve parked rows reads
  `dead`, and one whose window contains it reads `partial`.
  Red when: a dead writer reads as a run that predates it, or the reverse.
- **AC7** — When `python <kit>/runlog.py model aLeakedHandle --json` runs on this tree, it prints a
  model whose parked-row counts by kind match the run-state file, with the journal sources `absent`
  because the run's window predates each journal's epoch.
  Red when: the counts differ from `memory/builds/aLeakedHandle/RUN.md`, or a source reads `dead`.
- **AC8** — When `build_run_model` builds fixture runs of 10 and of 100 commits, the count of git
  subprocess calls is the same for both.
  Red when: the git reads go per commit or per file.
- **AC9** — When `build_run_model` reads a fixture run with no preflight START and no parked rows, its
  window starts at the commit that created its run-state file.
  Red when: the window is undefined, or starts at the witness.
- **AC10** — When `build_run_model` joins a fixture holding two gate lines at the same minute from two
  worktrees and one line whose `run` a push line pinned, only the run's own worktree line and the pinned
  line join, and gaps of 15 and 14 minutes yield one `idle-gap`.
  Red when: the other worktree's bar is attributed, or the 14-minute gap fires.
- **AC11** — When `scan_decisions` reads a fixture with one row from each ledger source of S3,
  including a decision-log row spelled `(owner, 2026-09-01)`, each entry names its file and line or sha,
  and the `(owner, …)` row counts as the owner's.
  Red when: a source is dropped, or the owner spelling reads as the run's.
- **AC12** — When `check_conformance` reads fixtures for each member of `CONFORMANCE_ITEMS` in each
  state it can take, including a close with no gate line in its window, it returns that state.
  Red when: an item has no rule, or the no-gate case reads MET.
- **AC13** — When `build_owner_positions` reads a fixture with one owner turn before the preflight, one
  at launch, one inside the window and one after the close, each is classed as such.
  Red when: a turn after the close counts as in-window.
- **AC14** — When `build_run_usage` reads extractor usage spanning the window's edges, only usage inside
  the window counts, split three ways.
  Red when: usage outside the window is summed, or the split is lost.

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
  `absent` by epoch. B2's model half: the window starts at the run-state file's creating commit when
  there is no START. H6: the joins gain AC10. M6: every anomaly kind is defined, with unit 13's
  sub-classes. M7: every conformance item gets a rule and AC12. M8 and M9: every ledger source and
  owner spelling gains AC11. M11: the near-miss count. M14 and M15: owner positions and cost gain AC13
  and AC14. H9: AC8 counts git calls. L2: the hand-off to unit 12.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "join run state git and journals into one run timeline"` found no
joiner. The nearest readers are the unattended driver's `--plan` region reader and drift-audit's git
helpers. The model reads the run-state file's own row grammar, `<ts> <kind> · item <item> · reason
<reason>`, as the driver writes it at `tools/unattended/unattended.sh:3911-3920`, and does not copy
the driver's parser. No existing seam fits.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

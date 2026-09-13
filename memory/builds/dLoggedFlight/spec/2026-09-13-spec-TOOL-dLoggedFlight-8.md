# TOOL-dLoggedFlight-8 — the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A run's evidence is spread across its run-state file, three journals, git, the build folder and, where
local, its transcripts. Join them into one model of one run: what it did and when, what it decided,
whether it followed the method, what looks wrong, and how much of each answer the sources actually
support. Every later surface renders from this model rather than re-deriving it.

## 2. Scope (IN)

- **S1** Run segmentation. A slug's runs are separated by the driver's successful record-creating
  `--preflight` calls and their pinned bases, and a rotated `RUN.<phase>.<8hex>.md` is a run of its
  own. Where no driver lines exist, a run is its run-state file alone. Observed by AC1.
- **S2** The timeline. Observed by AC2. It holds:
  - phase moves with their time and witness;
  - every driver verb with its rc and checks;
  - the run's own commits, meaning first-parent commits on the run branch that name one of its unit
    ids, since a raw base-to-witness range was measured to be 82% other work;
  - merges naming the slug;
  - gate lines joined by worktree and window, or exactly by `gate_run`;
  - push lines, unit dispatches and briefs;
  - from the extractor where local: owner turns, compactions, limits and idle gaps of 15 minutes or
    more.
- **S3** The decision ledger. Observed by AC3. It holds:
  - parked decisions, rescope acts and overrides from the run-state file;
  - review rounds with their verdict path;
  - `Decided:` trailers from the run's commits (`TOOL-dLoggedFlight-7`);
  - spec section 8 marks split by resolver, owner or agent, and by whether the commit that introduced
    them falls inside the run;
  - `memory/DECISIONS.md` rows the run's commits added, split on the `OWNER RULING` prefix;
  - acceptance-ledger lines that are not met.

  Each entry points at its source: a file and line, or a sha.
- **S4** The conformance block, each item MET, UNMET or UNJUDGEABLE with its reason. Observed by AC4.
  The items are:
  - per unit, a brief and a dispatch before its build commit;
  - the phases walked;
  - a GREEN bar at the close's head before `--close`;
  - the keepalive attested reaped;
  - the review loop reaching an exit.
- **S5** The anomaly set. Observed by AC5. Each anomaly is a closed kind with its evidence:
  - `nonterminal-merged`, sub-classified by its last act;
  - `out-of-band-edit` (from `oob=1`), where a labelled `-source:` repair is kept apart;
  - `refusal-loop`, the same verb refused three or more times on one check;
  - `killed-verb`, a start with no end;
  - `push-outside-lander`, a default-branch ref pushed with `lander=0`;
  - `red-behind-zero`, a background bar call whose notification rc was 0 while its gate line was RED;
  - `destructive-git`;
  - `converged-on-blocked`;
  - `idle-gap`, `multi-run-session` and `stalled`, meaning N heartbeats with no head or verb change.
- **S6** The coverage block. It gives each source's state, `present`, `absent`, `dead` or
  `not-local`, with counts. `dead` is a source with zero lines while the run's own rows prove activity.
  It also gives the share of calls and wall time attributed to a unit and a phase. Observed by AC6.
- **S7** The CLI `runlog.py model <slug> [--run <n>] --json` prints the model, and a local copy is
  written beside the extracts. Observed by AC7.
- **S8** Performance: the model of the largest run in this repo builds in under 3 s, with git read in
  a bounded number of calls, one log over the range and one blob batch. Observed by AC8.

## 3. Non-goals (OUT)

- Rendering. `TOOL-dLoggedFlight-9` renders the committed record from this model.
- Judging a decision's quality. The ledger says what was decided and where; whether it was right is
  the owner's.
- Cross-run trends over the corpus. That is a follow-up once journals exist on several nodes.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the reader for every journal.
- **consumes-from** `TOOL-dLoggedFlight-2` — the driver's verb, phase and oob lines.
- **consumes-from** `TOOL-dLoggedFlight-3` — the gate verdict lines.
- **consumes-from** `TOOL-dLoggedFlight-4` — the push lines and their gate run ids.
- **consumes-from** `TOOL-dLoggedFlight-6` — the session events, where the transcripts are local.
- **consumes-from** `TOOL-dLoggedFlight-7` — the trailer grammar the harvest reads.
- **hands-off** `TOOL-dLoggedFlight-9` — the committed record renders from this model.

## 4. Design

Every source reader returns `(items, coverage)`, and the join never fails on a missing source. It
marks the source `absent` or `not-local` and continues, because the corpus's first 50 runs have no
journals at all and must still model from their run-state files and git. A run modelled from its
run-state file and git alone is the honest floor for every run before this build.

The window of a run runs from its preflight START, or its first parked row, to its terminal END, or
the last line naming its slug. Gate and push lines join by worktree inside the window. A pinned
`gate_run` joins exactly, so a bar run in another worktree at the same minute is never attributed.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/model.py` | module | none |
| `build_run_model`, `read_run_state`, `read_git_range`, `scan_decisions`, `check_conformance`, `scan_anomalies`, `measure_coverage` | functions | `py.function`, verb-led |
| `RunModel` | type | `py.type` |
| `cmd_model` | CLI subcommand | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{model.py,runlog.py,selftest.py,README.md}` and fixtures under `tools/runlog/fixtures/`.

### Alternatives rejected

- Attribution by the extractor's sticky last-verb rule alone: rejected. It was measured as an
  unvalidated 93% upper bound, and one run with no `--phase` calls read RUNNING throughout.
- A raw base-to-witness commit range: rejected, measured at 18% of commits being the run's own.

## 5. Production-readiness checklist

- security — the model holds free text only from tracked, public sources: commit subjects, trailers
  and ids. The extractor contributes none.
- perf / scale — a bounded number of git calls, which AC8 pins.
- error / empty / loading states — every source's absence is a coverage state, not an exception. A run
  with no specs models with an empty unit table.
- observability — the coverage block is the model's own liveness statement.
- risks — heuristics in the joins, each named in the model's `method` field so a reader knows which
  answer is inferred.
- testing — a fixture run per anomaly kind and per conformance item, each staged RED, plus one model
  of a real past run with its counts checked against the corpus reader's figures.
- migration — none.
- user docs — the kit README's model section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `build_run_model` reads a fixture slug holding a rotated aborted record and a live one, it returns two
  runs whose facts come from their own files.
  Red when: the rotated record merges into the live run.
- **AC2** — When `build_run_model` reads a fixture run holding commits naming its units interleaved with commits of another
  build, the timeline carries only its own commits, in time order, beside its phase moves.
  Red when: the foreign commits enter the run.
- **AC3** — When a fixture's commits carry two `Decided:` trailers and its specs carry one owner mark
  committed before the run and one agent mark committed inside it, the ledger lists both trailers
  with their shas and counts the marks as owner-before and agent-inside.
  Red when: an owner ruling reads as a decision the run took.
- **AC4** — When `check_conformance` reads a fixture unit whose build commit precedes its brief row, its conformance item reads UNMET
  and names both times.
  Red when: the order check reads MET.
- **AC5** — When `scan_anomalies` reads fixtures staging each anomaly kind in S5, it reports exactly that kind with its
  evidence, and a clean fixture reports none.
  Red when: any kind fires on the clean fixture, or fails to fire on its own.
- **AC6** — When a fixture run has 12 parked rows and an empty `driver.log`, the driver source reads
  `dead`, not `absent`.
  Red when: a dead writer reads as a run that did nothing.
- **AC7** — When `python <kit>/runlog.py model aLeakedHandle --json` runs on this tree, it prints a
  model whose parked-row counts by kind match the run-state file, with the journal sources `absent`.
  Red when: the counts differ from `memory/builds/aLeakedHandle/RUN.md`.
- **AC8** — When the model of the run with the most parked rows in this repo is built, it takes under
  3 s on node `d`.
  Red when: the git reads go per-commit or per-file.
  figure: the floor is PINNED; the measured time is printed.

## 7. Gates

`lexicon naming predicates` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

- **F1** How many heartbeats with no change make a run `stalled`? RESOLVED (agent, 2026-09-13,
  delegated): six, which is one hour at the declared ten-minute cadence, stored as a model constant
  and printed in the anomaly's evidence so a reader can see the rule.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "join run state git and journals into one run timeline"` found no
joiner. The nearest readers are the unattended driver's `--plan` region reader and drift-audit's git
helpers. The model reads the run-state file's own row grammar, `<ts> <kind> · item <item> · reason
<reason>`, as the driver writes it at `tools/unattended/unattended.sh:3911-3920`, and does not copy
the driver's parser. No existing seam fits.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

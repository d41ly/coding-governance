# TOOL-dLoggedFlight-9 — the committed per-run record: a closed-schema report and its JSON twin

**Status:** CLOSED · rev-9 · 2026-09-16 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-9-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-9-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A run's model is machine-local, and 30 of 50 runs were made on other nodes. Render the model into one
tracked record in the build folder that every node can read. It is structural only, because this repo
is public. Its machine-readable twin sits inside it, and its content is fixed enough that a schema
leg can prove nothing else got in.

## 2. Scope (IN)

- **S1** `runlog.py record <slug> [--run <n>] --write` writes
  `<memory-root>/builds/<slug>/build/<date>-build-<FAMILY>-<slug>-<seq>-runlog-<runkey>.md`, where
  `<memory-root>` comes from `resolve_memory_root` of `TOOL-dLoggedFlight-1`.
  `<FAMILY>-<slug>-<seq>` is the lowest unit id the record serves, which check 21's filename
  projection requires. `<runkey>` is the first 8 hex of the commit that STARTED the run, read from the
  model's `derive_run_starts` in `TOOL-dLoggedFlight-8` and never re-derived here, so the filename and
  the window cannot disagree. Every run has a start commit, journals or not, and rotation gives each
  run its own (TOOL-dClosedLexicon-11). A re-render of a run whose record already exists writes to that
  record's existing path, found by its runkey, so a later render date never makes a second file. A
  run-state file that was never committed has no start commit, and the command refuses with a named
  line. Observed by AC1.
- **S2** The head carries `**Serves:** journal <ids>`, listing the unit ids the run dispatched or
  closed, as ranges where contiguous, and only ids a spec H1 in this build defines. A unit was
  dispatched when a `dispatch` row of the run's own record names it, and closed when its spec status
  reads CLOSED and one of the run's own commits names it. A run with no spec-defined id writes no
  tracked record and says so, since an unbound record moves a shrink-only pin. Observed by AC2.
- **S3** The markdown has fixed headings in a fixed order. Observed by AC3. They are:
  - `## Summary`, one fixed template per line;
  - `## Timeline`, a table whose every row's first cell is a UTC timestamp;
  - `## Units`, a table whose first cell is the unit's order;
  - `## Decisions`, counts per ledger source, with shas and repo-relative record paths;
  - `## Conformance`, `## Anomalies` and `## Coverage`;
  - `## Data`, holding one fenced `json` block with the structural twin.

  No row leads with an id, because a leading id DEFINES it for checks 13 and 14. A section holds only
  the fact lines and tables `RECORD_SCHEMA` declares for it, and every other table's first cell is a
  1-up ordinal. The timeline carries no owner turn: S4 keeps owner turns to counts. `## Coverage`
  also says whether idle gaps were judged and how many were kept out near an owner turn, the model's
  `idle` entry of `TOOL-dLoggedFlight-8` S7. The `Data` twin is the markdown re-encoded, every fact
  and every shown row of every section, so the two cannot disagree.
- **S4** The closed schema, `RECORD_SCHEMA`, as value classes. Observed by AC4. The record carries only:
  - shaped values: verb tokens matching `^--[a-z-]{2,20}$`, phase tokens matching `^[A-Z]{3,12}$`,
    check numbers, shas, this build's own unit ids, integers, durations, UTC timestamps,
    repo-relative paths of tracked files, and workflow labels matching `^[a-z0-9-]{1,40}$`;
  - closed vocabularies, each a list `RECORD_SCHEMA` owns:
    - coverage states: `present`, `absent`, `partial`, `dead` and `not-local`;
    - source names: `run-state`, `driver`, `gates`, `pushes`, `git`, `transcripts` and `build-folder`;
    - ledger sources: `decision`, `abort`, `override`, `waiver`, `rescope-retire`, `rescope-supersede`,
      `review`, `trailer`, `spec-mark`, `decision-log` and `ledger`. The first six are the driver's
      `PARK_KINDS_OWED` and, prefixed `rescope-`, its `PARK_ACTS_OWED`, and the driver-source arm of
      `TOOL-dLoggedFlight-8` S4 holds them to the driver;
    - owner-turn positions: `launch`, `pre-run`, `in-window` and `post-close`;
    - gate verdicts: `GREEN`, `RED`, `REFUSED` and `NONE`;
    - the push decisions of `TOOL-dLoggedFlight-4`;
    - the conformance items, conformance states, anomaly kinds and merged sub-classes of
      `TOOL-dLoggedFlight-8`, with `no-progress` among the anomaly kinds;
    - review verdicts and exits;
    - the timeline's event kinds, the spec status tokens, what opened and closed the window, and
      `yes` and `no`.

  The shaped values add a sha256 digest, which S5 commits. A repo-relative path is one under the
  build's own folder in the declared memory root, the only paths the record carries. There is no free
  text, no absolute path, no session id, no host id and no command. A model value outside its field's
  class is written `-`, which also stands for an absent value, and the summary's `values withheld`
  line counts them. An UNKNOWN value is absent too, never the value that reads clean. The summary's
  counts derived from the transcripts, the owner turns per position, the three usage lines and the
  attributed calls, are `-` wherever the transcripts' coverage reads neither `present` nor `partial`,
  since the model counts zero of what it never read. A timeline `rc` is written beside a verb or a
  push only when its END reads `exit=clean`, and is `-` otherwise, because an unclean END's `rc` is
  whatever `$?` its EXIT trap saw (`TOOL-dLoggedFlight-8` S5). Observed by AC10. Owner turns appear
  as counts per position, with no clock time, and no rendered value may recover one. Before anything
  is written, the render compares every UTC the record would carry with the second of every owner
  turn the model holds, and each idle row's end too: its UTC plus its duration, and the second after,
  since both are truncated. On a match it refuses the whole record, naming where the time sits and
  never the time. The model already keeps an idle gap near an owner turn out (`TOOL-dLoggedFlight-8`
  S6). This check is the renderer's own, so a model that regressed still cannot publish one.
- **S5** The integrity commitment: the sha256, line count and first and last timestamps of the journal
  lines attributed to this run, so an edit to the journal made after the render is detectable on the
  producing node. `runlog.py verify <record>` recomputes them. A run with no journal lines records
  `commitment=none`, and `verify` on it exits 0 with a line saying there is nothing to verify.
  The model names the lines it attributed, by producer and line number, as `journal_lines`. `verify`
  rebuilds the model and hashes the committed number of those lines from the committed first
  timestamp on, so a line the run appends after the render is not an edit. A machine holding no
  journal of the run refuses, exit 2, rather than reporting a mismatch. Observed by AC5.
- **S6** A size cap of 24 KB, kept reachable for every input by a bound on every section that grows:
  - the timeline is elided beyond its first and last 30 rows, with the elided count stated;
  - anomalies and conformance aggregate by kind with counts past 20 rows each;
  - units aggregate by status with counts past 20 rows;
  - decisions aggregate by ledger source with counts past 20 entries, and review rounds past 20.

  When a record still exceeds the cap, the shown rows halve, the timeline's first, until it fits, and
  every elision is stated. The summary is never elided. The `Data` twin is elided and aggregated by
  the same rules and carries the same counts, so it can never exceed what the markdown shows.
  Observed by AC6.
- **S7** The command renders from the model, writes the file, and prints the one follow-up it cannot
  run itself: re-render the build index, which the render step of `TOOL-dLoggedFlight-11` runs and
  stages. The generator is found beside this kit by its file name, never spelled by path. It also
  prints that the commit subject names the slug, never a unit id. Observed by AC7.
- **S8** The render makes no git call per row, and no git call at all beyond the model's own. Its wall
  time is printed report-only. Observed by AC8.

## 3. Non-goals (OUT)

- A separate `.json` file. Any tracked file under `build/` is a check-21 record and needs a `Serves:`
  line in its first 12 lines, which valid JSON cannot carry. So the twin is a fenced block, not a file.
- Committing anything machine-local, such as the extracts, the full model or the journals.
- Choosing when to render. `TOOL-dLoggedFlight-11` puts the step into the unattended Skill.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — the model this record renders, and its run starts.
- **hands-off** `TOOL-dLoggedFlight-10` — the schema leg that holds every committed record to S3 and S4.
- **hands-off** `TOOL-dLoggedFlight-11` — the Skill step that renders, re-indexes and commits.
- **hands-off** `TOOL-dLoggedFlight-16` — `COUNTED_STATES` and AC10, which it relies on unchanged,
  and S4's coverage-state list, which gains `stale`.
- **hands-off** `TOOL-dLoggedFlight-17` — `scan_owner_times`, `render_record` and `write_record`,
  which gain the independently read owner turns.
- **hands-off** `TOOL-dLoggedFlight-15` — the refusal it extends to held rows.
- **hands-off** `TOOL-dLoggedFlight-18` — `build_summary_facts`, `measure_commitment` and
  `check_commitment`, whose window fact and commitment times change and whose template does not.
- **hands-off** `TOOL-dLoggedFlight-19` — `RECORD_SCHEMA`, whose `utc` slots the class gate reads.
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill reads this record first.

## 4. Design

The record is rendered by fixed templates from model fields. No model string reaches the file unless
its field is in `RECORD_SCHEMA`. So the renderer and the schema leg share one allow-list as DATA, and
the leg re-validates the committed bytes independently rather than trusting the renderer. The leg
re-derives each value's class from the committed record, not from the renderer's output.

A record serving N ids re-renders each served spec's records region and the README's records line.
That is why the index re-render is part of the commit, and why the command says so rather than
leaving a stale index for check 9 to find at the push.

The model gains three things this record needs and could not otherwise render without re-deriving
them. Each is additive, and none changes an answer unit 8's arms grade:

- `journal_lines`, the line numbers per producer of every journal line it attributed to the run, which
  S5 hashes;
- the extractor's workflow runs inside the window, each with its label, on the timeline, since S4
  admits workflow labels and the model carried none;
- a time on every anomaly that has one, so the anomalies table can say when.

`RECORD_SCHEMA` holds the vocabularies BY REFERENCE to the model's own closed lists wherever the model
owns one, so the record and the model cannot name two different sets. It declares each section's fact
lines as templates and each table's columns as classes, with the timeline's columns classed per event
kind. That is the data `TOOL-dLoggedFlight-10`'s leg validates the committed bytes against.

The rev-4 bounds did not fit the cap. They put 120 timeline rows in the markdown and the same 120 in
the twin, and a row pair measures about 140 bytes, so the timeline alone reached 17 KB before any
other section. The rev-5 bounds leave room for the rest, and the halving step keeps the cap for a
record whose cells are unusually wide, since a path's width has no bound of its own.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/record.py` | module | none |
| `render_record`, `write_record`, `derive_runkey`, `derive_serves`, `measure_commitment`, `check_commitment`, `resolve_record_path` | functions | `py.function`, verb-led |
| `render_serves`, `build_record_doc`, `render_markdown`, `render_twin`, `render_cell`, `parse_record` and the other private helpers | functions | `py.function`, verb-led |
| `RECORD_SCHEMA` | constant | none |
| `cmd_record`, `cmd_verify` | CLI subcommands | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{record.py,model.py,runlog.py,selftest.py,README.md}`. The record's fixtures are built
by the self-test at run time, from real models where a model is needed, so no fixture file is added.

### Alternatives rejected

- A JSON file beside the markdown: rejected by check 21 (see §3).
- A runkey from the driver's preflight nonce: rejected, since a run that started before the writers
  existed, this one included, has no such nonce.
- A runkey from the run-state path's creation commit: rejected, since all six rotated builds resolve
  their archive and their live record to one such commit.
- Owner-turn clock times: rejected as new public data about when the owner was at the keyboard.
- An idle row beside an owner turn: rejected with them, since its start or its end is the same datum,
  derived.

## 5. Production-readiness checklist

- security — the closed schema is the control, enforced twice: here by construction and in
  `TOOL-dLoggedFlight-10` over committed bytes.
- perf / scale — rendering is proportional to the model, with no git call per row (AC8).
- error / empty / loading states — a run with no specs writes no record and says why. A run with no
  journals renders from its run-state file and git, with its coverage block saying so and
  `commitment=none`.
- observability — the coverage block, and a summary line naming how many sources were present.
- risks — a public record describes timing and failure counts. That is already true of run-state rows
  and commit times; owner presence is kept out.
- testing — golden fixtures per section, each elision and aggregation rule, and each schema refusal
  staged RED.
- migration — none.
- user docs — the kit README's record section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `write_record` renders the two runs of a fixture build rotated the way the driver
  rotates, one run with journals and one with none, on one date, their file names differ in
  `<runkey>`. Each key equals that run's `derive_run_starts` value. Each name passes check 5's name
  grammar and check 21's projection, both typed into the self-test from `memory/HYGIENE.md` rather
  than taken from the renderer. The real gate's verdict over a committed record is owed to the
  `memory hygiene` leg of the bar that grades this run's own record (`TOOL-dLoggedFlight-11` S5),
  since this pass runs no gate. Re-rendering the first run on a later date rewrites its existing
  file. A never-committed run-state file refuses with a named line. With `MEMORY_ROOT=docs/mem` in the
  scratch tree's conf, the record is written under `docs/mem/builds/`.
  Red when: the two runs share a key, the name drops the family or the runkey, a re-render makes a
  second file, or the record lands outside the declared root.
- **AC2** — When `derive_serves` reads a fixture run that dispatched units 2, 3 and 5 of a build whose
  specs define 1 to 5, the record serves `…-2..3 …-5`. A fixture with no spec-defined id writes nothing
  and exits 0 with a `no spec-defined unit` line.
  Red when: an undefined id is served, or the unbound case writes a `none` record.
- **AC3** — When `render_record` renders a fixture model, every table row's first cell is a timestamp
  or an ordinal, and the headings match S3 in order.
  Red when: a row leads with a unit id.
- **AC4** — When `render_record` renders a fixture model populating one value of every class in S4,
  plus an absolute path, a session UUID, a command string and a free-text reason, every class value
  appears and none of the four intruders does.
  Red when: a closed-vocabulary value is refused, or any field outside `RECORD_SCHEMA` reaches the file.
  Where the driver's source is present, the driver-source arm finds the first six ledger sources equal
  to its owed sets in both directions, and where it is absent the arm prints its skip.
- **AC5** — When `python <kit>/runlog.py verify` reads a record whose journal was edited after the
  render, it exits 1 naming the mismatch, and exits 0 on the untouched journal. On AC1's journal-less
  record it reads `commitment=none` and exits 0 with its nothing-to-verify line.
  Red when: the commitment is computed over nothing and always matches, or `commitment=none` fails.
- **AC6** — When `render_record` renders a fixture run with 500 timeline rows, 60 units, 200 anomalies
  and 300 ledger entries, the record stays under 24 KB. It states every elided and aggregated count,
  keeps every anomaly kind that occurred, and its `Data` twin carries the same counts. A fixture
  whose every section sits at its bound with its widest values still fits, through the halving step.
  Red when: the cap is passed, an anomaly kind disappears, or the twin carries rows the markdown elided.
- **AC7** — When `record --write` runs, stdout names the index re-render command and the slug-only
  commit subject.
  Red when: the command exits silently, leaving a stale index.
- **AC8** — When `render_record` renders the 500-row fixture with `subprocess` patched to count, it
  makes zero calls, and it prints its wall time without grading it.
  Red when: the render reaches git per row.
- **AC9** — When `render_record` renders a model whose idle row starts in an owner turn's second,
  one whose idle row ends in one, and one whose idle row's truncated end falls the second before
  one, each refuses with a line naming no time, and `write_record` writes nothing. The same three
  with the owner turn three seconds further away render. A real model built from a transcript with
  an owner turn at a silence's start, one at its end and one inside it renders a record in which no
  UTC, and no UTC plus a duration, falls in any owner turn's second.
  Red when: a time in an owner turn's second reaches the text, a refusal names the time, or a near
  miss refuses.
- **AC10** — When `render_record` renders the landed fixture's model with no transcript on the
  machine, so its transcripts read `not-local`, every count the owner-turn, usage and
  attributed-calls facts carry is `-`. The same run with its session's extract, made by the real
  extractor, renders those counts as integers. A run whose `--close` END reads `rc=0` and
  `exit=unclean`, as the driver's EXIT trap writes a verb killed mid-bar, renders `-` in that
  Timeline row's `rc` cell, and the same END reading `exit=clean` renders its `0`.
  Red when: a count from a source the model never read renders as a zero, a known count renders as
  `-`, or a killed verb's `rc` reaches the Timeline.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness`

New arm: `tools/runlog/selftest.py` · each schema refusal, elision and aggregation rule staged RED · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S4 S5 S6 S8 · §4 · AC1 AC2 AC4 AC6 AC8 · folded round-1 spec audit B2 (a runkey
  every run has), B3 (`RECORD_SCHEMA` enumerates every closed vocabulary the sections are made of),
  M16 (anomalies and conformance aggregate past 40 rows) and L3 (the render's cost is a counted zero).
- rev-3 · 2026-09-13 · S1 S4 S5 S6 · AC1 AC5 AC6 · folded round-2 spec audit B1 (the runkey is the run's
  start commit, read from the model, since a path's creation commit is shared by an archive and its
  successor; a re-render keeps its file), M2 (units and decisions aggregate too, and the twin follows
  the markdown's elision), L1 (`commitment=none` and its `verify` are observed) and L5 (the ledger
  sources are the driver's four owed kinds and two owed acts).
- rev-4 · 2026-09-13 · S1 S4 · AC1 AC4 · folded round-3 spec audit M11 (the owed ledger sources are held
  to the driver's source) and M12 (the record's root is the declared memory root, with a two-segment
  fixture).
- rev-5 · 2026-09-14 · S2 S3 S4 S5 S6 S7 · §4 · AC1 AC6 · the build pass, before its code. S2 defines
  dispatched and closed. S3 names the declared facts and tables, the ordinal first cells, the timeline
  with no owner turn, and the twin as the markdown re-encoded. S4 adds the vocabularies the sections
  need, the digest S5 commits, the `-` a withheld value becomes and the path class. S5 reads the
  model's `journal_lines`, and `verify` hashes from the committed first line so an appended line is
  no edit. S6's rev-4 bounds measured over the cap once the twin doubles each row, so they fall to 30
  and 20, with a halving step. S7 finds the index generator rather than spelling a sibling kit's path.
  §4 lists the three additive model fields. AC1's hygiene clause is typed from `memory/HYGIENE.md`,
  with the gate's own verdict owed, because this pass runs no gate. AC6 gains the widest-cell fixture.
- rev-6 · 2026-09-14 · S3 S4 · §4 · AC9 · folded the closing diff review's round-1 B1. An idle row's
  start or end was an owner turn's time to the second, and the kit README accepted the end as
  residue, a narrowing of S4 no owner ruled. S4 now refuses a record carrying any time in an owner
  turn's second, an idle row's end included, and §4 rejects an idle row beside an owner turn with the
  clock times. S3's Coverage says whether idle gaps were judged. The README's residue line is struck.
- rev-7 · 2026-09-14 · S4 · AC10 · folded the closing diff review's round-1 M6 and the render half of
  M3. M6: with the transcripts `not-local`, the owner turns, the usage lines and the attributed calls
  rendered as zeros. An `in-window 0` reads as a run that never asked, which is the answer the runlog
  Skill routes "what did it decide without asking" to, and every adopter on the shipped default names
  no session. S4 now writes each such count as `-` unless the transcripts read `present` or
  `partial`, and the Skill's missing-transcript warning names those counts beside the usage it named
  already. The review preferred a schema-leg rule grading each count against the record's own
  Coverage row. `TOOL-dLoggedFlight-10` §3 keeps content truth out of that leg, and a count graded
  against a coverage state is content, so AC10 grades the renderer instead. M3's render half: the
  Timeline showed a killed verb's `rc`, which is its EXIT trap's `$?` and often 0, so S4 writes an
  `rc` only beside `exit=clean`.
- rev-8 · 2026-09-16 · §3 · the edges to `TOOL-dLoggedFlight-14` and `-15`, the units closing
  review round 2 promoted at its NON-CONVERGENT exit.
- rev-9 · 2026-09-16 · §3 · the edges to `TOOL-dLoggedFlight-16` to `-19`, the units the spec audit
  of units 14 and 15, round 1, promoted at its BOUNDED exit. The edge to `-14` left with that unit's
  S5, which moved to `-17`, and the edge to `-15` drops the layout table, which `-19` reads.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "render a build record under the build folder"` found the
build-index generator's record binding in `tools/memory-tree/gen_build_index.py:446-632`, which this
unit conforms to rather than extends. The name grammar and the `Serves:` rules were measured in a
sandbox by the records acquisition probe. No renderer for a per-run record exists.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

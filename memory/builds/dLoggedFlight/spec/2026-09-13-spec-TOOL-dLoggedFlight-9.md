# TOOL-dLoggedFlight-9 — the committed per-run record: a closed-schema report and its JSON twin

**Status:** SPECCED · rev-4 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

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
  closed, as ranges where contiguous, and only ids a spec H1 in this build defines. A run with no
  spec-defined id writes no tracked record and says so, since an unbound record moves a shrink-only
  pin. Observed by AC2.
- **S3** The markdown has fixed headings in a fixed order. Observed by AC3. They are:
  - `## Summary`, one fixed template per line;
  - `## Timeline`, a table whose every row's first cell is a UTC timestamp;
  - `## Units`, a table whose first cell is the unit's order;
  - `## Decisions`, counts per ledger source, with shas and repo-relative record paths;
  - `## Conformance`, `## Anomalies` and `## Coverage`;
  - `## Data`, holding one fenced `json` block with the structural twin.

  No row leads with an id, because a leading id DEFINES it for checks 13 and 14.
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
    - review verdicts and exits.

  There is no free text, no absolute path, no session id, no host id and no command. Owner turns
  appear as counts per position, with no clock time.
- **S5** The integrity commitment: the sha256, line count and first and last timestamps of the journal
  lines attributed to this run, so an edit to the journal made after the render is detectable on the
  producing node. `runlog.py verify <record>` recomputes them. A run with no journal lines records
  `commitment=none`, and `verify` on it exits 0 with a line saying there is nothing to verify.
  Observed by AC5.
- **S6** A size cap of 24 KB, kept reachable for every input by a bound on every section that grows:
  - the timeline is elided beyond its first and last 60 rows, with the elided count stated;
  - anomalies and conformance aggregate by kind with counts past 40 rows each;
  - units aggregate by status with counts past 40 rows;
  - decisions aggregate by ledger source with counts past 40 entries.

  The summary is never elided. The `Data` twin is elided and aggregated by the same rules and carries
  the same counts, so it can never exceed what the markdown shows. Observed by AC6.
- **S7** The command renders from the model, writes the file, and prints the one follow-up it cannot
  run itself: re-render the build index, which the render step of `TOOL-dLoggedFlight-11` runs and
  stages. It also prints that the commit subject names the slug, never a unit id. Observed by AC7.
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
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill reads this record first.

## 4. Design

The record is rendered by fixed templates from model fields. No model string reaches the file unless
its field is in `RECORD_SCHEMA`. So the renderer and the schema leg share one allow-list as DATA, and
the leg re-validates the committed bytes independently rather than trusting the renderer. The leg
re-derives each value's class from the committed record, not from the renderer's output.

A record serving N ids re-renders each served spec's records region and the README's records line.
That is why the index re-render is part of the commit, and why the command says so rather than
leaving a stale index for check 9 to find at the push.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/record.py` | module | none |
| `render_record`, `write_record`, `derive_runkey`, `derive_serves`, `measure_commitment`, `check_commitment`, `resolve_record_path` | functions | `py.function`, verb-led |
| `RECORD_SCHEMA` | constant | none |
| `cmd_record`, `cmd_verify` | CLI subcommands | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{record.py,runlog.py,selftest.py,README.md}` and fixtures.

### Alternatives rejected

- A JSON file beside the markdown: rejected by check 21 (see §3).
- A runkey from the driver's preflight nonce: rejected, since a run that started before the writers
  existed, this one included, has no such nonce.
- A runkey from the run-state path's creation commit: rejected, since all six rotated builds resolve
  their archive and their live record to one such commit.
- Owner-turn clock times: rejected as new public data about when the owner was at the keyboard.

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

- **AC1** — When `render_record` renders the two runs of a fixture build rotated the way the driver
  rotates, one run with journals and one with none, on one date, their file names differ in
  `<runkey>`. Each key equals that run's `derive_run_starts` value, and each passes check 5's name
  grammar and check 21's projection in `bash tools/memory-tree/check-memory-hygiene.sh` over a scratch
  tree. Re-rendering the first run on a later date rewrites its existing file. A never-committed
  run-state file refuses with a named line. With `MEMORY_ROOT=docs/mem` in the scratch tree's conf, the
  record is written under `docs/mem/builds/`.
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
  keeps every anomaly kind that occurred, and its `Data` twin carries the same counts.
  Red when: the cap is passed, an anomaly kind disappears, or the twin carries rows the markdown elided.
- **AC7** — When `record --write` runs, stdout names the index re-render command and the slug-only
  commit subject.
  Red when: the command exits silently, leaving a stale index.
- **AC8** — When `render_record` renders the 500-row fixture with `subprocess` patched to count, it
  makes zero calls, and it prints its wall time without grading it.
  Red when: the render reaches git per row.

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

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "render a build record under the build folder"` found the
build-index generator's record binding in `tools/memory-tree/gen_build_index.py:446-632`, which this
unit conforms to rather than extends. The name grammar and the `Serves:` rules were measured in a
sandbox by the records acquisition probe. No renderer for a per-run record exists.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

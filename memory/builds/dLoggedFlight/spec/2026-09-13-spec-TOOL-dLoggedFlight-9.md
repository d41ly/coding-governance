# TOOL-dLoggedFlight-9 — the committed per-run record: a closed-schema report and its JSON twin

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A run's model is machine-local, and 30 of 50 runs were made on other nodes. Render the model into one
tracked record in the build folder that every node can read. It is structural only, because this repo
is public. Its machine-readable twin sits inside it, and its content is fixed enough that a schema
leg can prove nothing else got in.

## 2. Scope (IN)

- **S1** `runlog.py record <slug> [--run <n>] --write` writes
  `memory/builds/<slug>/build/<date>-build-<FAMILY>-<slug>-<seq>-runlog-<runkey>.md`. `<FAMILY>-<slug>-<seq>`
  is the lowest unit id the record serves, which check 21's filename projection requires. `<runkey>` is
  the first 8 hex of the sha256 of the run's preflight nonce, so two runs of one build on one date never
  collide. Observed by AC1.
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
- **S4** The closed schema. The record carries only these values: verb names, phase names, check
  numbers, anomaly kinds, conformance states, shas, this build's own unit ids, integers, durations, UTC
  timestamps, repo-relative paths of tracked files, and workflow labels matching `^[a-z0-9-]{1,40}$`.
  There is no free text, no absolute path, no session id, no host id and no command. Owner turns
  appear as counts per position class, with no clock time. Observed by AC4.
- **S5** The integrity commitment: the sha256, line count and first and last timestamps of the journal
  lines attributed to this run, so an edit to the journal made after the render is detectable on the
  producing node. `runlog.py verify <record>` recomputes them. Observed by AC5.
- **S6** A size cap of 24 KB. The timeline is elided deterministically beyond its first and last 60
  rows, with the elided count stated. Anomalies, conformance and the summary are never elided.
  Observed by AC6.
- **S7** The command renders from the model, writes the file, and prints the one follow-up it cannot
  run itself: re-render the build index, which the render step of `TOOL-dLoggedFlight-11` runs and
  stages. It also prints that the commit subject names the slug, never a unit id. Observed by AC7.

## 3. Non-goals (OUT)

- A separate `.json` file. Any tracked file under `build/` is a check-21 record and needs a `Serves:`
  line in its first 12 lines, which valid JSON cannot carry. So the twin is a fenced block, not a file.
- Committing anything machine-local, such as the extracts, the full model or the journals.
- Choosing when to render. `TOOL-dLoggedFlight-11` puts the step into the unattended Skill.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — the model this record renders.
- **hands-off** `TOOL-dLoggedFlight-10` — the schema leg that holds every committed record to S3 and S4.
- **hands-off** `TOOL-dLoggedFlight-11` — the Skill step that renders, re-indexes and commits.
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill reads this record first.

## 4. Design

The record is rendered by fixed templates from model fields. No model string reaches the file unless
its field is in the closed schema's allow-list. So the renderer and the schema leg share one
allow-list, `RECORD_SCHEMA` in `tools/runlog/record.py`, and the leg re-validates the committed
bytes independently rather than trusting the renderer. The leg re-derives the schema from the
committed record, not from the renderer's output.

A record serving N ids re-renders each served spec's records region and the README's records line.
That is why the index re-render is part of the commit, and why the command says so rather than
leaving a stale index for check 9 to find at the push.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/record.py` | module | none |
| `render_record`, `write_record`, `derive_runkey`, `derive_serves`, `measure_commitment`, `check_commitment` | functions | `py.function`, verb-led |
| `RECORD_SCHEMA` | constant | none |
| `cmd_record`, `cmd_verify` | CLI subcommands | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{record.py,runlog.py,selftest.py,README.md}` and fixtures.

### Alternatives rejected

- A JSON file beside the markdown: rejected by check 21 (see §3).
- Owner-turn clock times: rejected as new public data about when the owner was at the keyboard.

## 5. Production-readiness checklist

- security — the closed schema is the control, enforced twice: here by construction and in
  `TOOL-dLoggedFlight-10` over committed bytes.
- perf / scale — rendering is proportional to the model; under 1 s for the largest run.
- error / empty / loading states — a run with no specs writes no record and says why. A run with no
  journals renders from its run-state file and git, with its coverage block saying so.
- observability — the coverage block, and a summary line naming how many sources were present.
- risks — a public record describes timing and failure counts. That is already true of run-state rows
  and commit times; owner presence is kept out.
- testing — golden fixtures per section, each elision rule and each schema refusal staged RED.
- migration — none.
- user docs — the kit README's record section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `render_record` renders two fixture runs of one build on one date, their file names
  differ in `<runkey>`, and each passes check 5's name grammar and check 21's projection in
  `bash tools/memory-tree/check-memory-hygiene.sh` over a scratch tree.
  Red when: the name drops the family or the runkey.
- **AC2** — When a fixture run dispatched units 2, 3 and 5 of a build whose specs define 1 to 5, the
  record serves `…-2..3 …-5`. A fixture with no spec-defined id writes nothing and exits 0 with a
  `no spec-defined unit` line.
  Red when: an undefined id is served, or the unbound case writes a `none` record.
- **AC3** — When `render_record` renders a fixture model, every table row's first cell is a timestamp or an
  ordinal, and the headings match S3 in order.
  Red when: a row leads with a unit id.
- **AC4** — When a fixture model carries an absolute path, a session UUID, a command string and a
  free-text reason, none of the four appears in the record.
  Red when: any field outside `RECORD_SCHEMA` reaches the file.
- **AC5** — When `python <kit>/runlog.py verify` reads a record whose journal was edited after the
  render, it exits 1 naming the mismatch, and exits 0 on the untouched journal.
  Red when: the commitment is computed over nothing and always matches.
- **AC6** — When `render_record` renders a fixture run with 500 timeline rows, the record stays under 24 KB and states the
  elided count, and every anomaly is present.
  Red when: an anomaly is elided, or the cap is passed.
- **AC7** — When `record --write` runs, stdout names the index re-render command and the slug-only
  commit subject.
  Red when: the command exits silently, leaving a stale index.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness`

New arm: `tools/runlog/selftest.py` · each schema refusal and elision rule staged RED · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "render a build record under the build folder"` found the
build-index generator's record binding in `tools/memory-tree/gen_build_index.py:446-632`, which this
unit conforms to rather than extends. The name grammar and the `Serves:` rules were measured in a
sandbox by the records acquisition probe. No renderer for a per-run record exists.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

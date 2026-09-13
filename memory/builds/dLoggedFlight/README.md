---
slug: dLoggedFlight
node: d
opened: 2026-09-13
streams: tooling
roster: TOOL
status: OPEN
authorized-by: prompt
ids: TOOL-dLoggedFlight-1
---

# dLoggedFlight — unattended runs recorded as they happen, and a record any node can read

## The problem this build exists to solve

An unattended run leaves a snapshot, not a sequence. Its run-state file keeps the latest phase with
no time, and its rows record only the driver verbs that succeeded. Refusals, gate verdicts, the close
checklist, landing attempts, compactions, resumes and owner messages leave nothing tracked, and no
record names the session that ran it. The transcripts hold the action sequence, but only on the
machine that ran the build, with the reasoning gone and most exit codes masked. So the owner cannot
say what a run did between two rows, why it stopped, what it decided unasked, or what it cost.

## Expected improvements

- Every driver verb, bar verdict and push leaves a line with its real exit code and its session.
- Each landed or aborted run commits a structural record that every node can read.
- The owner can ask what a run did, decided and cost, and get answers that cite their source.
- Runs left non-terminal after their build merged are reported rather than found by accident.

## Detriments if this is not built

- Runs made on other nodes stay unanalyzable here.
- Refusals, red bars and landing loops keep vanishing with the transcript.
- Decisions taken without a park keep going unrecorded.
- What a run costs stays unmeasured, the main loop's share included.

## Build-level rules

- **One mechanism per unit.** Each producer owns its own line; one reader parses every line.
- **The committed record has a closed schema**: no free text, no absolute paths, no session ids, and
  owner turns as counts and positions. A schema leg enforces it (owner, 2026-09-13).
- **A run log is evidence, never an input.** No verb or gate branches on one. Logging never changes a
  verb's exit status or stdout, and a failed write says so on stderr.
- **Performance is specified, then measured.** Each producer's spec states a process-spawn budget for
  its hot path, and each consumer and suite states a wall-clock ceiling, measured on node `d`.
- **Fully tested.** Every acceptance criterion is observed, never asserted, and every new gate or
  refusal has its failing case seen RED before it lands.
- **The unattended kit's existing self-test suites are not run** (the standing owner rule). The driver's
  log writer gets its own small suite instead (owner, 2026-09-13).
- **Local store split** (owner, 2026-09-13): run logs in the git common dir, transcript extracts under
  the user profile.
- **Landing** (owner, 2026-09-13): `--no-ff` merge and push from this worktree's detached head. The
  run-state record then ends at LANDING.
- **M2 classification at start:** all thirteen units are MISSING.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dLoggedFlight-1` | MISSING | the runlog kit and its line grammar: one format every producer writes, one reader every consumer parses |
| 2 | `TOOL-dLoggedFlight-2` | MISSING | the unattended driver writes a start and an end line for every run verb |
| 3 | `TOOL-dLoggedFlight-3` | MISSING | the gate runner writes one verdict line per bar run |
| 4 | `TOOL-dLoggedFlight-4` | MISSING | the pre-push hook writes one line per push |
| 5 | `TOOL-dLoggedFlight-5` | MISSING | one redaction table, applied once on read, with a staged positive per rule |
| 6 | `TOOL-dLoggedFlight-6` | MISSING | the transcript extractor: a run's action sequence, owner turns and cost |
| 7 | `TOOL-dLoggedFlight-7` | MISSING | the `Decided:` commit trailer, so a choice with no commit of its own has a home |
| 8 | `TOOL-dLoggedFlight-8` | MISSING | the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set |
| 9 | `TOOL-dLoggedFlight-9` | MISSING | the committed per-run record: a closed-schema report and its JSON twin |
| 10 | `TOOL-dLoggedFlight-10` | MISSING | the schema leg: a committed run record outside the closed schema reds the bar |
| 11 | `TOOL-dLoggedFlight-11` | MISSING | the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat |
| 12 | `TOOL-dLoggedFlight-12` | MISSING | the runlog skill answers questions about a run from its record and its local extracts |
| 13 | `TOOL-dLoggedFlight-13` | MISSING | drift-audit reports run records left non-terminal after their build merged |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-13 · streams tooling
ids TOOL-dLoggedFlight-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

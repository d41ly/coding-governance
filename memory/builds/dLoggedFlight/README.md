---
slug: dLoggedFlight
node: d
opened: 2026-09-13
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13
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
  verb's exit status, stdout or signal behaviour, and a failed write says so on stderr.
- **Performance is counted, not timed.** A producer's hot path adds zero process spawns, observed by
  an exec count; a consumer's cost is a counted call bound. Wall time is printed report-only, and each
  leg's budget row is the cost verdict.
- **Fully tested.** Every acceptance criterion is observed, never asserted, and every new gate or
  refusal has its failing case seen RED before it lands.
- **Gates run once, after every unit is built** (owner, 2026-09-13). A unit pass runs only the test
  file it writes. An AC observed by a gate leg is owed to that run.
- **The unattended kit's self-tests stay off the bar** (owner, 2026-08-23). The driver writer's new
  suite (owner, 2026-09-13) is withheld from adopters and run directly, never as a gate leg.
- **Local store split** (owner, 2026-09-13): run logs in the git common dir, transcript extracts under
  the user profile.
- **Landing.** The approved worktree push (owner, 2026-09-13) is refused by the pre-push hook without
  a bypass, so the build lands through `tools/push-main.sh` from the primary tree when that tree is
  idle, and parks otherwise. `TOOL-dLoggedFlight-11` records why.
- **M2 classification at start:** all thirteen units are MISSING.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dLoggedFlight-1` | CLOSED | the runlog kit and its line grammar: one format every producer writes, one reader every consumer parses |
| 2 | `TOOL-dLoggedFlight-2` | CLOSED | the unattended driver writes a start and an end line for every run verb |
| 3 | `TOOL-dLoggedFlight-3` | CLOSED | the gate runner writes one verdict line per bar run |
| 4 | `TOOL-dLoggedFlight-4` | CLOSED | the pre-push hook writes one line per push |
| 5 | `TOOL-dLoggedFlight-5` | CLOSED | one redaction table, applied once on read, with a staged positive per rule |
| 6 | `TOOL-dLoggedFlight-6` | CLOSED | the transcript extractor: a run's action sequence, owner turns and cost |
| 7 | `TOOL-dLoggedFlight-7` | CLOSED | the `Decided:` commit trailer, so a choice with no commit of its own has a home |
| 8 | `TOOL-dLoggedFlight-8` | MISSING | the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set |
| 9 | `TOOL-dLoggedFlight-9` | MISSING | the committed per-run record: a closed-schema report and its JSON twin |
| 10 | `TOOL-dLoggedFlight-10` | MISSING | the schema leg: a committed run record outside the closed schema reds the bar |
| 11 | `TOOL-dLoggedFlight-11` | MISSING | the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat |
| 12 | `TOOL-dLoggedFlight-12` | MISSING | the runlog skill answers questions about a run from its record and its local extracts |
| 13 | `TOOL-dLoggedFlight-13` | MISSING | drift-audit reports run records left non-terminal after their build merged |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 13 unit(s) · node d · opened 2026-09-13 · streams tooling
ids TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dLoggedFlight-1 — the runlog kit and its line grammar: one format every producer writes, one reader every consumer parses](spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md) | 1 | 2 | CLOSED | rev-6 | 2026-09-13 |
| [TOOL-dLoggedFlight-2 — the unattended driver writes a start and an end line for every run verb](spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md) | 2 | 2 | CLOSED | rev-6 | 2026-09-13 |
| [TOOL-dLoggedFlight-3 — the gate runner writes one verdict line per bar run](spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md) | 3 | 2 | CLOSED | rev-6 | 2026-09-13 |
| [TOOL-dLoggedFlight-4 — the pre-push hook writes one line per push](spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md) | 4 | 2 | CLOSED | rev-5 | 2026-09-13 |
| [TOOL-dLoggedFlight-5 — one redaction table, applied once on read, with a staged positive per rule](spec/2026-09-13-spec-TOOL-dLoggedFlight-5.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-14 |
| [TOOL-dLoggedFlight-6 — the transcript extractor: a run's action sequence, owner turns and cost](spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md) | 6 | 2 | CLOSED | rev-6 | 2026-09-14 |
| [TOOL-dLoggedFlight-7 — the `Decided:` commit trailer, so a choice with no commit of its own has a home](spec/2026-09-13-spec-TOOL-dLoggedFlight-7.md) | 7 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-dLoggedFlight-8 — the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set](spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md) | 8 | 2 | SPECCED | rev-5 | 2026-09-14 |
| [TOOL-dLoggedFlight-9 — the committed per-run record: a closed-schema report and its JSON twin](spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md) | 9 | 2 | SPECCED | rev-4 | 2026-09-13 |
| [TOOL-dLoggedFlight-10 — the schema leg: a committed run record outside the closed schema reds the bar](spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md) | 10 | 2 | SPECCED | rev-4 | 2026-09-13 |
| [TOOL-dLoggedFlight-11 — the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat](spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md) | 11 | 2 | SPECCED | rev-4 | 2026-09-13 |
| [TOOL-dLoggedFlight-12 — the runlog skill answers questions about a run from its record and its local extracts](spec/2026-09-13-spec-TOOL-dLoggedFlight-12.md) | 12 | 2 | SPECCED | rev-3 | 2026-09-13 |
| [TOOL-dLoggedFlight-13 — drift-audit reports run records left non-terminal after their build merged](spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md) | 13 | 2 | SPECCED | rev-4 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dLoggedFlight-1` | no |
| 2 | `TOOL-dLoggedFlight-2` | no |
| 3 | `TOOL-dLoggedFlight-3` | no |
| 4 | `TOOL-dLoggedFlight-4` | no |
| 5 | `TOOL-dLoggedFlight-5` | no |
| 6 | `TOOL-dLoggedFlight-6` | no |
| 7 | `TOOL-dLoggedFlight-7` | no |
| 8 | `TOOL-dLoggedFlight-8` | no |
| 9 | `TOOL-dLoggedFlight-9` | no |
| 10 | `TOOL-dLoggedFlight-10` | no |
| 11 | `TOOL-dLoggedFlight-11` | no |
| 12 | `TOOL-dLoggedFlight-12` | no |
| 13 | `TOOL-dLoggedFlight-13` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

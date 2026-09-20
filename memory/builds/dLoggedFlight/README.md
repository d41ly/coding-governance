---
slug: dLoggedFlight
node: d
opened: 2026-09-13
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-15 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-17 TOOL-dLoggedFlight-18 TOOL-dLoggedFlight-19 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30
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
  owner turns as counts and positions. A schema leg enforces it (owner, 2026-09-13). No journal
  or transcript time is committed (owner, 2026-09-16).
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
- **M2 classification:** units 1 to 13 MISSING at start; 14 to 30 MISSING when promoted or added.

## Parked decisions

- Whether a hygiene check should refuse a spec whose retirement inventory finds readers by name only.
  Parked in `RUN.md` on 2026-09-16 with its options and reason: it changes `memory/HYGIENE.md`, a
  governance carrier, so it is the owner's under BUILD-METHOD M3's second veto.
- Three spec-audit checks over spec prose, the class left-shifts of B1, H2 and M4 of the spec audit of
  units 25 to 27. Parked in `RUN.md` on 2026-09-20 with their options and reason: each needs its rule
  in `memory/TEMPLATE-SPEC.md`, a governance carrier, so M3's second veto makes them the owner's.
  Units 28, 29 and 30 carry the per-instance half of all three.
- The spec-audit promotion chain is bounded at round 7, decided in `RUN.md` on 2026-09-20 with its
  options and reason. Units 28, 29 and 30 were promoted at that round's BOUNDED exit and are built
  with no further audit round, under a Definition-of-Done override recorded at the close. Rounds 4 to
  7 each promoted over one class, the inventory of arms and fixtures a retirement touches, and the
  closing diff review over the real code is the first place a suite can actually reach it.

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
| 8 | `TOOL-dLoggedFlight-8` | CLOSED | the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set |
| 9 | `TOOL-dLoggedFlight-9` | CLOSED | the committed per-run record: a closed-schema report and its JSON twin |
| 10 | `TOOL-dLoggedFlight-10` | CLOSED | the schema leg: a committed run record outside the closed schema reds the bar |
| 11 | `TOOL-dLoggedFlight-11` | CLOSED | the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat |
| 12 | `TOOL-dLoggedFlight-12` | CLOSED | the runlog skill answers questions about a run from its record and its local extracts |
| 13 | `TOOL-dLoggedFlight-13` | CLOSED | drift-audit reports run records left non-terminal after their build merged |
| 14 | `TOOL-dLoggedFlight-14` | CLOSED | a session's live transcript is read before its store extract, on the named and the discovered path |
| 15 | `TOOL-dLoggedFlight-15` | WONTDO | a row an owner act can cause carries no time that places the act |
| 16 | `TOOL-dLoggedFlight-16` | CLOSED | an extract short of the window reads `stale`, and `partial` keeps its lower-bound meaning |
| 17 | `TOOL-dLoggedFlight-17` | WONTDO | the owner-time refusal re-reads every session the model read, and holds an idle row to the model's own guard |
| 18 | `TOOL-dLoggedFlight-18` | WONTDO | an owner-causable journal line sets neither the window's rendered end nor the commitment's times |
| 19 | `TOOL-dLoggedFlight-19` | WONTDO | every UTC slot of the record schema is classed against owner acts, and one arm reads every time a production render writes |
| 20 | `TOOL-dLoggedFlight-20` | MISSING | the committed record carries no time a journal or transcript produced |
| 21 | `TOOL-dLoggedFlight-21` | CLOSED | the commitment is a digest and a line count, and `verify` recomputes it from the time-ordered prefix of the run's journal lines |
| 22 | `TOOL-dLoggedFlight-22` | MISSING | the journal rows, the time columns and the owner-time refusal retire, with every arm, vocabulary and floor that reads them rewritten by name |
| 23 | `TOOL-dLoggedFlight-23` | MISSING | one self-test arm holds every time-bearing token a render writes to a public source, over classes and slots read from the schema and a fixture that reaches every conditional slot |
| 24 | `TOOL-dLoggedFlight-24` | CLOSED | the Summary window and its duration render the git-only window the schema leg derives |
| 25 | `TOOL-dLoggedFlight-25` | MISSING | the Summary window's closer names a terminal write its own commit carries, observed over real models at each of the Skill's render placements |
| 26 | `TOOL-dLoggedFlight-26` | MISSING | every count and value the record arms assert over a shared fixture builder is derived from what the builder placed, on row kinds the record keeps |
| 27 | `TOOL-dLoggedFlight-27` | MISSING | the Timeline's `withheld rows` fact counts each retired kind from a declared source, and renders `-` for a source the model did not read |
| 28 | `TOOL-dLoggedFlight-28` | MISSING | every expectation the record arms derive from a shared fixture builder is re-checked against a render with one kind of event removed |
| 29 | `TOOL-dLoggedFlight-29` | MISSING | each placement model is returned beside the repository state it was built from, and the arm re-derives the model from that state |
| 30 | `TOOL-dLoggedFlight-30` | MISSING | the replaced `known` test is observed gone from the renderer, and one arm re-points a declared source to prove the lookup decides the value |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 30 unit(s) · node d · opened 2026-09-13 · streams tooling
ids TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13
ids TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-15 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-17 TOOL-dLoggedFlight-18 TOOL-dLoggedFlight-19 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26
ids TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dLoggedFlight-1 — the runlog kit and its line grammar: one format every producer writes, one reader every consumer parses](spec/2026-09-13-spec-TOOL-dLoggedFlight-1.md) | 1 | 2 | CLOSED | rev-7 | 2026-09-14 |
| [TOOL-dLoggedFlight-2 — the unattended driver writes a start and an end line for every run verb](spec/2026-09-13-spec-TOOL-dLoggedFlight-2.md) | 2 | 2 | CLOSED | rev-7 | 2026-09-16 |
| [TOOL-dLoggedFlight-3 — the gate runner writes one verdict line per bar run](spec/2026-09-13-spec-TOOL-dLoggedFlight-3.md) | 3 | 2 | CLOSED | rev-6 | 2026-09-13 |
| [TOOL-dLoggedFlight-4 — the pre-push hook writes one line per push](spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md) | 4 | 2 | CLOSED | rev-6 | 2026-09-14 |
| [TOOL-dLoggedFlight-5 — one redaction table, applied once on read, with a staged positive per rule](spec/2026-09-13-spec-TOOL-dLoggedFlight-5.md) | 5 | 2 | CLOSED | rev-4 | 2026-09-14 |
| [TOOL-dLoggedFlight-6 — the transcript extractor: a run's action sequence, owner turns and cost](spec/2026-09-13-spec-TOOL-dLoggedFlight-6.md) | 6 | 2 | CLOSED | rev-9 | 2026-09-16 |
| [TOOL-dLoggedFlight-7 — the `Decided:` commit trailer, so a choice with no commit of its own has a home](spec/2026-09-13-spec-TOOL-dLoggedFlight-7.md) | 7 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-dLoggedFlight-8 — the run model: every source joined into one timeline, decision ledger, conformance block and anomaly set](spec/2026-09-13-spec-TOOL-dLoggedFlight-8.md) | 8 | 2 | CLOSED | rev-16 | 2026-09-20 |
| [TOOL-dLoggedFlight-9 — the committed per-run record: a closed-schema report and its JSON twin](spec/2026-09-13-spec-TOOL-dLoggedFlight-9.md) | 9 | 2 | CLOSED | rev-11 | 2026-09-16 |
| [TOOL-dLoggedFlight-10 — the schema leg: a committed run record outside the closed schema reds the bar](spec/2026-09-13-spec-TOOL-dLoggedFlight-10.md) | 10 | 2 | CLOSED | rev-9 | 2026-09-16 |
| [TOOL-dLoggedFlight-11 — the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat](spec/2026-09-13-spec-TOOL-dLoggedFlight-11.md) | 11 | 2 | CLOSED | rev-7 | 2026-09-16 |
| [TOOL-dLoggedFlight-12 — the runlog skill answers questions about a run from its record and its local extracts](spec/2026-09-13-spec-TOOL-dLoggedFlight-12.md) | 12 | 2 | CLOSED | rev-5 | 2026-09-16 |
| [TOOL-dLoggedFlight-13 — drift-audit reports run records left non-terminal after their build merged](spec/2026-09-13-spec-TOOL-dLoggedFlight-13.md) | 13 | 2 | CLOSED | rev-6 | 2026-09-16 |
| [TOOL-dLoggedFlight-16 — an extract short of the window reads `stale`, and `partial` keeps its lower-bound meaning](spec/2026-09-16-spec-TOOL-dLoggedFlight-16.md) | 14 | 2 | CLOSED | rev-3 | 2026-09-16 |
| [TOOL-dLoggedFlight-14 — a session's live transcript is read before its store extract, on the named and the discovered path](spec/2026-09-16-spec-TOOL-dLoggedFlight-14.md) | 15 | 2 | CLOSED | rev-4 | 2026-09-16 |
| [TOOL-dLoggedFlight-17 — the owner-time refusal re-reads every session the model read, and holds an idle row to the model's own guard](spec/2026-09-16-spec-TOOL-dLoggedFlight-17.md) | 16 | 2 | WONTDO | rev-1 | 2026-09-16 |
| [TOOL-dLoggedFlight-15 — a row an owner act can cause carries no time that places the act](spec/2026-09-16-spec-TOOL-dLoggedFlight-15.md) | 17 | 2 | WONTDO | rev-2 | 2026-09-16 |
| [TOOL-dLoggedFlight-18 — an owner-causable journal line sets neither the window's rendered end nor the commitment's times](spec/2026-09-16-spec-TOOL-dLoggedFlight-18.md) | 18 | 2 | WONTDO | rev-1 | 2026-09-16 |
| [TOOL-dLoggedFlight-19 — every UTC slot of the record schema is classed against owner acts, and one arm reads every time a production render writes](spec/2026-09-16-spec-TOOL-dLoggedFlight-19.md) | 19 | 2 | WONTDO | rev-1 | 2026-09-16 |
| [TOOL-dLoggedFlight-21 — the commitment is a digest and a line count, and `verify` recomputes it from the time-ordered prefix of the run's journal lines](spec/2026-09-16-spec-TOOL-dLoggedFlight-21.md) | 21 | 2 | CLOSED | rev-2 | 2026-09-16 |
| [TOOL-dLoggedFlight-24 — the Summary window and its duration render the git-only window the schema leg derives](spec/2026-09-16-spec-TOOL-dLoggedFlight-24.md) | 22 | 2 | CLOSED | rev-2 | 2026-09-16 |
| [TOOL-dLoggedFlight-25 — the Summary window's closer names a terminal write its own commit carries, observed over real models at each of the Skill's render placements](spec/2026-09-16-spec-TOOL-dLoggedFlight-25.md) | 23 | 2 | SPECCED | rev-3 | 2026-09-20 |
| [TOOL-dLoggedFlight-26 — every count and value the record arms assert over a shared fixture builder is derived from what the builder placed, on row kinds the record keeps](spec/2026-09-16-spec-TOOL-dLoggedFlight-26.md) | 24 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-dLoggedFlight-22 — the journal rows, the time columns and the owner-time refusal retire, with every arm, vocabulary and floor that reads them rewritten by name](spec/2026-09-16-spec-TOOL-dLoggedFlight-22.md) | 25 | 2 | SPECCED | rev-3 | 2026-09-16 |
| [TOOL-dLoggedFlight-27 — the Timeline's `withheld rows` fact counts each retired kind from a declared source, and renders `-` for a source the model did not read](spec/2026-09-16-spec-TOOL-dLoggedFlight-27.md) | 26 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-dLoggedFlight-20 — the committed record carries no time a journal or transcript produced](spec/2026-09-16-spec-TOOL-dLoggedFlight-20.md) | 27 | 2 | SPECCED | rev-3 | 2026-09-16 |
| [TOOL-dLoggedFlight-23 — one self-test arm holds every time-bearing token a render writes to a public source, over classes and slots read from the schema and a fixture that reaches every conditional slot](spec/2026-09-16-spec-TOOL-dLoggedFlight-23.md) | 28 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [TOOL-dLoggedFlight-28 — every expectation the record arms derive from a shared fixture builder is re-checked against a render with one kind of event removed](spec/2026-09-20-spec-TOOL-dLoggedFlight-28.md) | 29 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-dLoggedFlight-29 — each placement model is returned beside the repository state it was built from, and the arm re-derives the model from that state](spec/2026-09-20-spec-TOOL-dLoggedFlight-29.md) | 30 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-dLoggedFlight-30 — the replaced `known` test is observed gone from the renderer, and one arm re-points a declared source to prove the lookup decides the value](spec/2026-09-20-spec-TOOL-dLoggedFlight-30.md) | 31 | 2 | SPECCED | rev-1 | 2026-09-20 |
<!-- /gen:build-units -->

Records: 30 bound to this build, across 4 record folder(s).

Ids no record names: TOOL-dLoggedFlight-17 TOOL-dLoggedFlight-18 TOOL-dLoggedFlight-19.

Ids no `spec-audit` record has ever named: TOOL-dLoggedFlight-17 TOOL-dLoggedFlight-18 TOOL-dLoggedFlight-19 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30.
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
| 14 | `TOOL-dLoggedFlight-16` | no |
| 15 | `TOOL-dLoggedFlight-14` | no |
| 16 | `TOOL-dLoggedFlight-17` | no |
| 17 | `TOOL-dLoggedFlight-15` | no |
| 18 | `TOOL-dLoggedFlight-18` | no |
| 19 | `TOOL-dLoggedFlight-19` | no |
| 21 | `TOOL-dLoggedFlight-21` | no |
| 22 | `TOOL-dLoggedFlight-24` | no |
| 23 | `TOOL-dLoggedFlight-25` | no |
| 24 | `TOOL-dLoggedFlight-26` | no |
| 25 | `TOOL-dLoggedFlight-22` | no |
| 26 | `TOOL-dLoggedFlight-27` | no |
| 27 | `TOOL-dLoggedFlight-20` | no |
| 28 | `TOOL-dLoggedFlight-23` | no |
| 29 | `TOOL-dLoggedFlight-28` | no |
| 30 | `TOOL-dLoggedFlight-29` | no |
| 31 | `TOOL-dLoggedFlight-30` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

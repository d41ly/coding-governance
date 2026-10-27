# TOOL-dWellOiledMachine-81 — the stall line's reset read from the transcript's measured limit record, never from an unmeasured payload field

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 55 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-81-deviation-811.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-81-deviation-811.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 16, item H2, at HIGH. TOOL-dWellOiledMachine-65 S1 has `extractResetUtc(data)` read "the payload
field TOOL-dWellOiledMachine-6 S9's sidecar parser reads for the reset", but 6 S9 names no field, the
`StopFailure` payload was never measured (`tools/unattended/stall-recorder.js:26-30`, even `error` is
UNVERIFIED), and 65's §3 forbids measuring it. A builder must invent the field, 65 AC1's hand-made
payload is green by construction, and a real limit yields `reset=none`, so the hold never fires. This
unit rests the reset on a source this tree has measured: the session transcript's API-error record,
whose `quotaLimits.resetsAt` runlog already reads (`tools/runlog/extract.py:648-653`). It also puts
back the measurement 65 dropped, by recording which top-level keys the payload carried.

## 2. Scope (IN)

- **S1** — The reset from the transcript. `extractResetUtc(data)` in
  `tools/unattended/stall-recorder.js` reads the file `data.transcript_path` names, at most its last
  262144 bytes, and takes the LAST JSON line carrying `isApiErrorMessage: true` and a `quotaLimits`
  object whose `status` is `rejected`. Its `resetsAt`, an integer of epoch seconds, is rendered in
  extended ISO 8601 form with seconds and a trailing `Z` (as `2026-10-27T09:00:00Z`), the form `renderUtc` and the journal write. No
  `transcript_path`, an unreadable transcript, no such record, or a `resetsAt` that is not a positive
  integer gives `none`. The reading is runlog's (`tools/runlog/extract.py:648-653`): the same record,
  the same three keys. Observed by AC1, AC2.
- **S2** — The payload's shape recorded. The stall line gains
  `payload-keys=<the payload's top-level keys, sorted, comma-joined>`, each key kept only when it
  matches `[A-Za-z0-9_]+`, so the first real stall measures what `StopFailure` hands over without
  publishing any value. Observed by AC3.
- **S3** — The measured record pinned as a fixture. `tools/runtime/fixtures/stall/limit-transcript.jsonl`
  holds three lines: a user line, an assistant line, and one API-error line whose `quotaLimits` carries
  exactly the key set measured on node a (§4), its values replaced by fixture values and its
  `resetsAt` set to `1789000000`. Observed by AC1.
  **Readers:** by name: READER NOT IN TREE — the stall fixture file is created by this item. by value: NO VALUE READERS — its values are fixture values no product code reads.
- **S4** — The reader stays one. `supervise.py`'s hold (65 S2) reads `reset` from the line unchanged;
  no Python reader of the transcript is added, and `extractResetUtc` stays the one reader of the
  reset. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the hold, its ceiling or the hand-over: 65 S2, TOOL-dWellOiledMachine-6 S9 and
  TOOL-dWellOiledMachine-47 stand.
- No measurement of `StopFailure` values: S2 records key names only.
- The text corrections of spec 65 itself, the "basic form" label and its §3 and §5 lines, are findings
  12, 33 and 53, carried by the minors batch TOOL-dWellOiledMachine-90.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-65` — `extractResetUtc`, the stall line's `reset` field and the hold that reads it, which this unit grounds on the transcript's measured record
- **hands-off** `TOOL-dWellOiledMachine-91` — `extractResetUtc` and the stall fixture, which that unit bounds by session, record age and reset (finding 17)
- **hands-off** `TOOL-dWellOiledMachine-94` — S1's sentence, §10's seam, AC3's payload and the symbol render (findings 15, 24, 30, 31)

## 4. Design

### Evidence

- `quotaLimits` on an API-error transcript record, MEASURED 2026-10-27 on node a, read only, over
  `~/.claude/projects/**/*.jsonl`: 145 files carry it, and of the first 384 occurrences 361 read
  `{"status":"rejected","resetsAt":<10 digits>,"unifiedRateLimitFallbackAvailable":false,"rateLimitType":"five_hour","overageStatus":"rejected","overageDisabledReason":"org_level_disabled","isUsingOverage":false}`
  and 23 the same with `seven_day`. PINNED; re-derive with
  `grep -rhoE '"quotaLimits":\{[^}]*\}' --include=*.jsonl ~/.claude/projects`.
- The research record of this chain measured the same field: 650 occurrences in 208 files, every one
  `rejected` (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-platform.md:34`).
- runlog reads `quotaLimits.status`, `rateLimitType` and `resetsAt` from that record
  (`tools/runlog/extract.py:648-653`).
- `transcript_path` is read from a `Stop` payload by `tools/hooks/format-guard.js:496`; on
  `StopFailure` it is UNVERIFIED, which S2's key list measures at the first real stall, and its
  absence gives `none` (S1), never a guessed instant.
- `stall-recorder.js` exports `extractErrorClass` and runs `main` only as the main module
  (`tools/unattended/stall-recorder.js:91-92`), so `extractResetUtc` is testable by `require`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `payload-keys` | stall journal line key | none |
| `tools/runtime/fixtures/stall/limit-transcript.jsonl` | fixture | none |

### Files touched (estimate)

- `tools/unattended/stall-recorder.js`: S1, S2
- `tools/runtime/fixtures/stall/limit-transcript.jsonl`: S3
- `tools/unattended/stall-recorder.test.sh`: the arm in §7

### Alternatives rejected

- **A capability row naming the payload's reset field, refusing while unmeasured.** A session limit
  cannot be staged on demand, so the row would stay unmeasured and the hold would never fire; the
  transcript record is already measured.
- **The hold reading the transcript in Python through runlog's extractor.** The runtime kit would
  import the runlog kit across a copy-install boundary, and the hold would need the act session's
  transcript path, which the recorder is handed directly.

## 5. Production-readiness checklist

- security — the line carries an instant and key names, never payload or transcript text.
- perf / scale — one bounded read of 256 KiB per stall, on an event that fires once per refused turn.
- error / empty / loading states — every missing input gives `reset=none`, which 65's hold already
  handles.
- observability — `payload-keys` shows what the harness handed over.
- risks — a harness that renames `quotaLimits` reads `none` everywhere at once; runlog's limit reading
  breaks at the same moment, so the drift is visible in two places.
- testing — AC1 to AC4 and the arm in §7.
- migration — none: the line gains a key, and readers of `key=value` fields ignore one they do not
  read.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

- **AC1** — When `node -e "console.log(require('./stall-recorder.js').extractResetUtc({transcript_path: '<root>/tools/runtime/fixtures/stall/limit-transcript.jsonl'}))"`
  runs, it prints `2026-09-10T00:26:40Z`, the extended form of `1789000000`.
  Red when: the reset is read from a payload field the fixture does not carry, and `none` prints.
- **AC2** — When the same call names a transcript holding no API-error line, or no `transcript_path`,
  it prints `none`.
  Red when: an instant is invented for a payload with no limit record.
- **AC3** — When the recorder runs on a bound fixture session's payload carrying keys `session_id`,
  `transcript_path`, `error` and `bad-key`, `journal.py read --class stall --last 1` prints
  `payload-keys=error,session_id,transcript_path`.
  Red when: the key list is missing, or carries a key outside `[A-Za-z0-9_]+`.
- **AC4** — When `git grep -n "resetsAt" -- tools/runtime tools/unattended` runs, it names only
  `stall-recorder.js` and the fixture.
  Red when: a second reader of the reset appears.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/unattended/stall-recorder.test.sh · covers AC1 AC2 AC3 · the fixture transcript read by a recorder taking the reset from a payload field, and a payload key outside the key grammar · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  16 (H2).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-91, TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam reused is runlog's reading of the transcript's limit record
(`tools/runlog/extract.py:648-653`): the same record and keys, read in the recorder's language because
the recorder is the one place handed the transcript path. The probe
`python tools/codebase-map/reuse_lookup.py "read the session limit reset time from the transcript"`
ranked `read`, `read_text`, `read_conf` and `read_journal` by name stem, none a limit reader; the
recall query below ranked TOOL-dWellOiledMachine-65 first, the unit this one grounds.

Recall terms used: `python tools/memory-recall/query.py "where is the session limit reset time
measured" --terms "quotaLimits resetsAt rateLimitType rejected transcript StopFailure stall recorder
limit hold reset"`

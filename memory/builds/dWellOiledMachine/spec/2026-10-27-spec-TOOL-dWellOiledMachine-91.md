# TOOL-dWellOiledMachine-91 — the stall reset taken only from a limit record that is this session's, recent and still in force

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 56 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-91-deviation-911.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-91-deviation-911.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-2 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md`),
finding 17, item H1, at HIGH. TOOL-dWellOiledMachine-81 S1 has `extractResetUtc` take the LAST
rejected `quotaLimits` record in the transcript's final 256 KiB, and checks neither that its
`resetsAt` is still ahead nor that the record belongs to the stall being recorded. One transcript can
carry an earlier limit's record, so when the current record is not yet on disk, or the stall is not a
quota refusal, the recorder returns a past reset. TOOL-dWellOiledMachine-65's hold then relaunches at
once into the limit, the wake loop TOOL-dWellOiledMachine-47 exists to stop. This unit accepts a record
only when it is this session's, written within a bound of the hook firing, and its reset is still
ahead; anything else gives `none`. It also records, on the stall line, where the accepted record sat,
so the first real stall measures the flush ordering this spec cannot.

## 2. Scope (IN)

- **S1** — The freshness test. `readLimitRecord(data, nowMs)` in `tools/unattended/stall-recorder.js`
  reads the window 81 S1 reads and takes the LAST JSON line carrying `isApiErrorMessage: true` and a
  `quotaLimits` object whose `status` is `rejected`, as 81 S1 does. It accepts that record only when
  all three hold: its `sessionId` equals `data.session_id`; `resetsAt * 1000` is greater than `nowMs`;
  and `Date.parse(<its timestamp>)` lies within `RESET_RECORD_MAX_AGE_SECONDS` (300) of `nowMs`, either
  side. A record failing any test is refused, and no earlier record is tried, since an earlier one is
  older still. `nowMs` defaults to `Date.now()`, the hook's own clock. Observed by AC1, AC2, AC3, AC4.
- **S2** — One reader, two outputs. `readLimitRecord` returns `{reset, limitRecord}`: `reset` is the
  accepted `resetsAt` rendered by `lease.renderUtc(new Date(resetsAt * 1000))`
  (`tools/unattended/run-lease.js:206`), or `none`; `limitRecord` is `last` when the accepted record is
  the last JSON line of the window, `earlier` when accepted with later lines after it, `stale` when a
  rejected record was found and refused by S1, and `none` when there is no window or no such record.
  `extractResetUtc(data, nowMs)` returns `readLimitRecord(data, nowMs).reset`, so 65's and 81's caller
  is unchanged. Observed by AC1, AC5.
- **S3** — The measurement on the line. The stall journal line gains
  `limit-record=<last|earlier|stale|none>` beside 81 S2's `payload-keys`, so the first real stall shows
  whether the API-error record was already the transcript's last line when `StopFailure` fired.
  Observed by AC6.
- **S4** — The fixture dated. The API-error line of `tools/runtime/fixtures/stall/limit-transcript.jsonl`
  (81 S3) carries `sessionId` `fixture-session` and `timestamp` `2026-09-10T00:25:00.000Z`, 100 seconds
  before its `resetsAt` of `1789000000`. Spec 81 takes a rev bump at this unit's pass whose AC1 and AC2
  pass the clock `Date.parse('2026-09-10T00:25:20Z')` as the second argument, its §9 line naming this
  unit and finding 17, and the `stall-recorder.test.sh` cases observing 81 AC1 and AC2 pass the same
  clock. Observed by AC1, AC7.
  **Readers:** by name: READER NOT IN TREE — the fixture and `extractResetUtc` are TOOL-dWellOiledMachine-81's and -65's, unbuilt at HEAD. by value: `stall-recorder.test.sh`'s cases for 81 AC1 and AC2, which read the fixture's reset under the clock this item passes.

## 3. Non-goals (OUT)

- No change to which record is a limit record, the window size or the `none` rendering: 81 S1 stands.
- No change to the hold, its ceiling or the hand-over: 65 S2, TOOL-dWellOiledMachine-6 S9 and
  TOOL-dWellOiledMachine-47 stand.
- Re-pointing 65's and 47's plants to a transcript, and the narrowing of 81 AC4, are finding 18 (M13),
  carried by the minors batch TOOL-dWellOiledMachine-94, which plants a transcript dated by this unit's
  rule.
- No clock override in the hook's environment: the fixture cases pass `nowMs` through `require`.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-81` — `extractResetUtc`, the transcript window it reads, the stall fixture and the stall line's `payload-keys`, which this unit bounds by session, age and reset
- **hands-off** `TOOL-dWellOiledMachine-94` — the freshness rule, which the batch's re-pointed plants for 65 and 47 must satisfy by writing a transcript dated now with a reset an hour ahead (finding 18)
- **hands-off** `TOOL-dWellOiledMachine-97` — S4's rev bump of spec 81, AC7, the hands-off line to unit 94 and Files touched, amended before this unit builds (round-3 promotions audit, findings 6, 12, 19, 24 and 27)

## 4. Design

### Evidence

- An API-error transcript record carries `sessionId` and `timestamp` beside `quotaLimits`, MEASURED
  2026-10-27 on node a, read only, over one file of `~/.claude/projects/C--projects-coding-governance/`:
  its keys were `apiErrorStatus`, `cwd`, `entrypoint`, `error`, `gitBranch`, `isApiErrorMessage`,
  `isSidechain`, `message`, `parentUuid`, `perTurnEffort`, `quotaLimits`, `requestId`, `sessionId`,
  `timestamp`, `type`, `userType`, `uuid` and `version`, the timestamp in the form
  `2026-09-20T14:38:04.740Z`. PINNED; re-derive by reading the first `quotaLimits` line of any
  transcript under `~/.claude/projects` with `python -c "import json,sys; print(sorted(json.loads(sys.stdin.readline())))"`.
- 81 §4 measured 145 transcript files carrying the record and one node carrying hundreds of rejected
  records (`spec-81.md:67-71`), so a transcript holding an earlier limit's record is the ordinary case.
- runlog reads the same record and its `timestamp` (`tools/runlog/extract.py:648-653`, `:883`).
- `renderUtc` renders a `Date` at second precision with a trailing `Z`
  (`tools/unattended/run-lease.js:205-208`), and `stall-recorder.js` already calls it (`:74`).
- Whether `StopFailure` fires before or after the harness appends the turn's API-error record to the
  transcript is UNVERIFIED. S1's three tests make either ordering safe: a record not yet flushed leaves
  only older ones, which fail the age or reset test and give `none`. S3's `limit-record` value at the
  first real stall is the measurement.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `readLimitRecord` | function, `stall-recorder.js` | `read`, OK |
| `RESET_RECORD_MAX_AGE_SECONDS` | constant, `stall-recorder.js` | none |
| `limit-record` | stall journal line key | none |

### Files touched (estimate)

- `tools/unattended/stall-recorder.js`: S1 to S3
- `tools/runtime/fixtures/stall/limit-transcript.jsonl`: S4
- `tools/unattended/stall-recorder.test.sh`: the arm in §7 and S4's clock
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-81.md` (S4's rev bump)
- `memory/map/generated/symbols.json` (re-rendered by `python tools/codebase-map/gen_map.py --write`,
  since `readLimitRecord` joins the symbol tier)

### Alternatives rejected

- **A future reset alone.** It still takes another session's record from a shared or copied
  transcript, and an old seven-day record whose reset is still ahead would hold a run for days on a
  limit that is not the one that refused this turn.
- **Falling back to the last record that passes.** Any record before the last rejected one is older
  than it, so a fallback can only return a record further from this stall.

## 5. Production-readiness checklist

- security — the line gains one closed-vocabulary value; no payload or transcript text is published.
- perf / scale — the same single 256 KiB read 81 S1 makes; three comparisons on one record.
- error / empty / loading states — every refused or missing record gives `reset=none`, the state 65's
  hold already handles, and `limit-record` says which refusal it was.
- observability — `limit-record` on every stall line.
- risks — a harness that writes the API-error record more than 300 seconds before `StopFailure` fires
  reads `stale` every time; the first real stall's `limit-record` shows it, and the constant is the
  calibration knob.
- testing — AC1 to AC7 and the arm in §7.
- migration — none: the line gains a key, and readers of `key=value` fields ignore one they do not read.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

Each `node -e` call runs from `tools/unattended/` and passes the fixture path as
`{session_id: 'fixture-session', transcript_path: '<root>/tools/runtime/fixtures/stall/limit-transcript.jsonl'}`
unless it says otherwise.

- **AC1** — When `node -e` requires the recorder module beside it and prints `readLimitRecord` over the
  payload at `2026-09-10T00:25:20Z` as JSON, it prints `{"reset":"2026-09-10T00:26:40Z","limitRecord":"last"}`.
  Red when: a fresh record of this session is refused and `none` prints.
- **AC2** — When the same call passes the clock `Date.parse('2026-09-10T00:26:41Z')`, one second after
  the reset and 101 seconds after the record, it prints `{"reset":"none","limitRecord":"stale"}`.
  Red when: a reset already past is returned.
- **AC3** — When the call reads a scratch copy of the fixture whose `1789000000` is replaced by
  `1789003600`, under the clock `Date.parse('2026-09-10T00:30:01Z')`, 301 seconds after the record, it
  prints `{"reset":"none","limitRecord":"stale"}`.
  Red when: a record older than `RESET_RECORD_MAX_AGE_SECONDS` is accepted because its reset is ahead.
- **AC4** — When the call passes `session_id: 'other-session'` under the AC1 clock, it prints
  `{"reset":"none","limitRecord":"stale"}`.
  Red when: another session's record is accepted.
- **AC5** — When the call reads a scratch copy of the fixture with one user line appended after the
  API-error line, under the AC1 clock, it prints `{"reset":"2026-09-10T00:26:40Z","limitRecord":"earlier"}`;
  and `extractResetUtc(<payload>, Date.parse('2026-09-10T00:25:20Z'))` prints `2026-09-10T00:26:40Z`.
  Red when: the position is misread, or `extractResetUtc` and `readLimitRecord` disagree.
- **AC6** — When the recorder runs as a hook on a bound fixture session's payload carrying `cwd`,
  `hook_event_name`, `session_id` `fixture-session` and the fixture's `transcript_path`, with
  `CLAUDE_PROJECT_DIR` unset, `journal.py read --class stall --last 1` prints a line carrying
  `reset=none` and `limit-record=stale`, the fixture's reset being past on the real clock.
  Red when: the line carries no `limit-record` key, or a past reset.
- **AC7** — When `grep -c "2026-09-10T00:25:20Z" 2026-10-27-spec-TOOL-dWellOiledMachine-81.md` runs
  over spec 81 after this unit, it prints 2 or more, AC1's and AC2's clocks.
  Red when: 81's AC1 still calls `extractResetUtc` on the real clock, which reads the fixture as stale.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/unattended/stall-recorder.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the fixture cases staged against 81 S1's reader taking the last rejected record with no session, age or reset test · none

## 8. Open questions

- **F1 — Which tests make a limit record current?** (a) `sessionId` equal to the payload's, `resetsAt`
  ahead of the hook's clock, and a `timestamp` within 300 seconds of it; (b) `resetsAt` ahead alone, the
  finding's minimum; (c) `sessionId` alone. (b) accepts a still-running seven-day record from an
  earlier turn and another session's record in a shared transcript; (c) accepts this session's past
  limit, the exact defect. (a) is the most capable option and needs no new surface: the three keys are
  measured (§4). The 300-second bound is a ceiling far above a turn's close and far below a five-hour
  window, named as a constant so the first real stall's `limit-record` can move it. RESOLVED (agent,
  2026-10-27, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  17 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-3
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-97.

## 10. Reuse audit

The seams reused are 81 S1's window and record test, extended in place rather than beside it, and
`renderUtc` (`tools/unattended/run-lease.js:206`), which renders the reset as the recorder's journal
time already is. The probe `python tools/codebase-map/reuse_lookup.py "refuse a stale record read from
the tail of an append-only log"` ranked `read`, `read_text`, `records` and `read_conf` by name stem,
none a freshness test; the recall query below ranked TOOL-aWokenSentinel-4, the recorder's own spec,
and TOOL-dWellOiledMachine-81 first, the unit this one bounds. No existing freshness test over a
transcript record exists to reuse.

Recall terms used: `python tools/memory-recall/query.py "how fresh must the transcript limit record be
for the stall reset" --terms "quotaLimits resetsAt stale record freshness transcript StopFailure stall
recorder session timestamp"`

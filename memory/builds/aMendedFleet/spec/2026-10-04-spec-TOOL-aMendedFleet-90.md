# TOOL-aMendedFleet-90 — a report-only drift signal DEAD for N recorded readings is named for retirement or a filed ask

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 90

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

A report-only drift signal that cannot move prints `DEAD PROBE — signal cannot move, ignore its
value`, and it prints that on every run forever: `dangling_pointers_in_own_ledger` has done so since
the ledger shard it reads retired. The instruction to ignore the value is honest for one reading and
is how a dead probe survives for months. Once unit 48 persists every bar's readings, the report can
count how many recorded readings in a row a signal has been dead. This unit reads that count and,
past a declared limit, turns the status into a demand that names the two ways out: retire the signal,
or file an ask and declare it. It stays report-only.

## 2. Scope (IN)

- **S1** — THE READER. `derive_dead_streaks` in `tools/drift-audit/drift_report.py` reads the history
  file at the path unit 48's `resolve_history_path` returns, ONCE per run and before any write. It
  locates columns by the header line, never by position. Rows sharing `utc` and `sha` form one group;
  consecutive groups at the same `sha` collapse into one READING, the latest group winning, so a bar
  re-run at one commit does not age a signal. It returns, per signal, the number of trailing readings
  whose `state` is `dead`, a signal absent from a reading ending its streak, and the total reading
  count. A missing file, an unreadable one, or one with no header returns `None`. Observed by AC1.
- **S2** — THE DECLARATIONS, in the project layer, both read with the getattr-and-fallback the other
  optional keys use: `DEAD_READINGS_LIMIT`, an int, the engine default 10 when undeclared; and
  `DEAD_FILED`, a dict from signal name to the id of the ask filed for it, empty when undeclared.
  `tools/drift-audit/drift_signals.template.py` carries both with a comment, and this repo's
  `tools/drift-audit/drift_signals.py` declares neither, taking the defaults. A declared value of the
  wrong shape, a limit that is not a positive int or a `DEAD_FILED` that is not a str-to-str dict, is
  refused with exit 2 before any signal runs, as `RATCHET_LOOKBACK` and `BASELINES` are. The defaults
  are observed by AC2; the refusal by the build's direct check, which no criterion here names.
- **S3** — THE STATUS. In the human table, a report-only record that reads DEAD PROBE in this run and
  whose streak is at least the limit prints `DEAD PROBE for <k> readings — take it out of SIGNALS, or
  file an ask and declare it in DEAD_FILED`, or, when `DEAD_FILED` names it, `DEAD PROBE for <k> readings —
  filed <id>`. A gateable dead record, which `--check` already reds, and a record declared empty keep
  their status. The `--json` record gains `dead_readings`, the streak or `null` when S1 returned
  `None`. Observed by AC2.
- **S4** — LIVENESS. Every human run prints one header line under the report header, either
  `# dead-for-N: <r> readings recorded at <path> · limit <n>` or `# dead-for-N: no history at <path>,
  nothing judged`, so a reader that finds nothing says so rather than printing the old status as
  though it had looked. Observed by AC3.
- **S5** — A `DEAD_FILED` entry naming a signal that is not in `SIGNALS`, or one live in this run,
  prints one header line naming the entry and asking that it be taken out, so a filing cannot
  outlive the death it filed. Observed by AC4.
- **S6** — The rule moves no exit status in any mode; S2's refusal of a malformed declaration is a
  configuration error, not the rule. Observed by AC3.
- **S7** — The drift-audit README gains a paragraph beside the signal table naming the rule, the two
  keys and the history it reads, and stating that it is report-only because the history is node-local.
  Its layout table's `drift_signals.py` row lists both keys among the project-layer names, as units
  8, 53 and 56 do for theirs. Observed by AC5.
- **S8** — Self-test arms in `tools/drift-audit/selftest.py`: a fixture history with a streak at,
  below and broken before the limit, a repeated-sha group, a reordered header and a missing file; and a
  stale `DEAD_FILED` entry. NOT OBSERVED by a criterion here: the suite runs once at the close, and the
  arms are declared under `New arm:` in §7.
- **S9** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED by
  a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and §7
  names the legs that read it.

## 3. Non-goals (OUT)

- Making the rule red `--check`. §8 F1 keeps it report-only.
- Retiring a signal or filing an ask automatically. The report names the two acts; a person or a run
  takes one.
- Reviving the two signals that read DEAD today. `dangling_pointers_in_own_ledger` is unit 53's and
  `legs_retried_after_timeout` is unit 59's.
- Writing the history file, its header contract or its location, which are unit 48's; and the
  BASE-to-HEAD delta reader, which is unit 49's.
- Bumping the drift-audit kit version, owed once at the build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-48` — the history file, its header contract and
  `resolve_history_path`; without them S1 has nothing to read and every run prints S4's no-history
  line.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `8312d315`, whose bytes under `tools/drift-audit/` equal base `7af5f564`'s.

- `python tools/drift-audit/drift_report.py` printed two DEAD PROBE rows, both report-only:
  `dangling_pointers_in_own_ledger` and `legs_retried_after_timeout`. PINNED, measured 2026-10-04.
- The renderer in `main` prints DEAD PROBE for any record whose `live` is false and which
  `DECLARED_EMPTY` does not name, gateable or not; a gateable one is also collected into `dead` and
  reds `--check`. A report-only one has no consequence at all, which is the gap.
- No history exists on this tree: `git grep -n "drift-history" -- tools` finds nothing until unit 48
  lands, so every figure this unit reads is produced after it.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_dead_streaks` | function, `drift_report.py` | `py.function`; `--suggest derive_dead_streaks --as py.function` answered OK |
| `DEAD_READINGS_LIMIT` | project-layer key | none; the `py.constant` cell is undeclared |
| `DEAD_FILED` | project-layer key | none |
| `dead_readings` | JSON key of a record | none |

### Data model

A READING is the last group at one `sha` in a run of consecutive groups at that `sha`. A streak is
counted back from the newest reading and ends at the first reading whose row for the signal is
absent or carries any `state` but `dead`.

### Rollout

Unit 48 lands the file and unit 51 rewrites the same renderer's report-only branch; both are
ordered first, and this unit rebases onto them. The limit binds from the first bar after unit 48
lands, so no signal can reach it before ten bars have run on a node.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Count consecutive groups, not readings.** A node that re-runs a red bar five times at one commit
  would age every dead signal five readings in an hour, which measures retries rather than time.
- **Count calendar days dead.** A node that runs no bar for a month would see a signal age a month
  without one reading taken.
- **Auto-file an ask from the report.** The report is a seconds-tier reader with no write path into
  the backlog, and a filing written by a reader nobody approves is the inherited-red machinery's job,
  which unit 9 owns.

## 5. Production-readiness checklist

- security — N/A: reads a node-local file this kit writes; no new input crosses a boundary.
- perf / scale — one read of a file growing by about 19 rows a bar; reading a thousand bars is a few
  milliseconds.
- error / empty / loading states — S1's `None` and S4's no-history line; a row whose field count
  differs from the header's is skipped, so it neither extends nor ends a streak.
- observability — S4's line on every run.
- risks — the limit is a guess until history exists; ten readings is about two days of bars on node
  a. It is a project-layer key, so a node that finds it noisy declares another value in one line.
- testing — AC1 to AC5 here; the arms in S8.
- migration — N/A: nothing stored changes shape.
- user docs — S7.

## 6. Acceptance criteria

- **AC1** — When a `python -c` script imports `drift_report` from `tools/drift-audit` and calls
  `derive_dead_streaks` on a fixture history written under the scratchpad, it returns 3 for a signal
  dead in the last three readings and live before them, 0 for one dead and then live in the newest
  reading, 0 for one absent from the newest reading, and the same result when two groups share a
  `sha` and when the header's columns are written in another order; on a path that does not exist it
  returns `None`.
  Red when: a repeated-sha bar ages a signal twice, columns are read by position, or a missing file
  reads as zero streaks.
- **AC2** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path, a history of ten
  readings at ten shas, each with `legs_retried_after_timeout` dead, is written to the file
  `git rev-parse --git-common-dir` locates, and `python tools/drift-audit/drift_report.py` runs, that
  row's status reads `DEAD PROBE for 10 readings` and names `DEAD_FILED`; after the clone's project
  layer declares `DEAD_FILED` mapping that signal to `TOOL-aMendedFleet-59`, it reads
  `filed TOOL-aMendedFleet-59`; and `--json` carries `dead_readings` 10 for it.
  Red when: a signal dead past the limit still prints only `ignore its value`.
  fixture: needs a signal reading DEAD in a fresh clone; `legs_retried_after_timeout` does today,
  because a fresh clone holds no run records. If unit 59 makes it live there, the builder picks any
  record the clone reads DEAD and names it in the acceptance ledger.
- **AC3** — When the same clone holds no history file, `python tools/drift-audit/drift_report.py`
  prints the `# dead-for-N: no history` line, and `python tools/drift-audit/drift_report.py --check`
  returns the same exit status with the fixture history present and absent.
  Red when: an empty reader is silent, or the rule moves a verdict.
- **AC4** — When the clone's project layer declares `DEAD_FILED` mapping `no_such_signal` to any id,
  the report prints one header line naming `no_such_signal` and asking that the entry be taken out.
  Red when: a filing for a signal that does not exist, or is live, passes silently.
- **AC5** — When `grep -n "DEAD_READINGS_LIMIT" tools/drift-audit/README.md tools/drift-audit/drift_signals.template.py`
  runs, it hits each file.
  Red when: the rule ships with no documented knob.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · fixture histories with a streak at, below and broken before the limit, a repeated-sha group, a reordered header, a missing file and a stale `DEAD_FILED` entry, staged red by counting groups instead of readings · `CHECK_FLOOR` moves by the checks the arms add

## 8. Open questions

- **F1** — Does a signal DEAD past the limit red `--check`, or only report?
  Options: red the bar until the signal is retired or filed; report only. The history is node-local
  and never pushed, so a red would depend on how many bars a node happened to run: the same commit
  would pass on a fresh clone and fail on an old one, and the push boundary's recorded green could not
  be reproduced at its sha.
  RESOLVED (agent, 2026-10-04, delegated): report only, per S3 and S6. A verdict that does not
  reproduce at a sha is the defect the bar's fingerprint exists to refuse.
- **F2** — What ends a streak, and what is one reading?
  RESOLVED (agent, 2026-10-04, delegated): a reading is the last group at one `sha` in a run of
  consecutive groups at that `sha`, and a streak ends at any reading where the signal is not `dead`,
  absence included, per S1 and §4's data model.
- **F3** — What is N?
  RESOLVED (agent, 2026-10-04, delegated): 10 by default, declarable per project, per S2 and the §5
  risk line. No history exists to measure a better value against.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, split from unit 51's F1; the DEAD rows re-measured at
  `8312d315`.
- rev-2 · 2026-10-04 · S7 · M2 cross-read: units 8, 53 and 56 add their new project-layer keys to
  the README layout table's `drift_signals.py` row, and S7 left `DEAD_READINGS_LIMIT` and
  `DEAD_FILED` out of it, so that row would stop listing every key the layer may carry.
- rev-3 · 2026-10-06 · S2, S6 · build: a malformed declaration of either key is refused with exit 2,
  as the sibling optional keys are, rather than failing mid-table with a traceback; S6 binds the
  rule, which still moves no exit status, and a config refusal is not the rule.

## 10. Reuse audit

The seams extended are the renderer in `main` of `tools/drift-audit/drift_report.py`, whose DEAD
PROBE branch gains the streak, the getattr-and-fallback reads of optional project keys in `Ctx`, and
unit 48's `resolve_history_path` and header contract, which this unit reads and never re-derives.
`python tools/codebase-map/reuse_lookup.py "count consecutive dead readings of a drift signal from a
history file"` ranked generic readers first, `read_text`, `read_conf` and `read_journal` across other
kits, then `count_never_falls` in `tools/govkit/govkit.py`, a before/after predicate that a kit file
may not import; nothing reads a drift history, because none exists yet, so no existing seam fits
beyond the engine itself. The scan names `.sh` as unscanned; no shell file reads drift readings.
Recall returned unit 48, unit 51, `TOOL-dScaffoldedMirror-7`, whose liveness rule this follows, and
`TOOL-cTracedPromise-5` on a signal reading dead for an adopter. Where the report and the tree
disagree: the synthesis said DEAD probes stay dead forever, and that is still the state; two signals
read DEAD at `8312d315`.

Recall terms used: `python tools/memory-recall/query.py "what should happen to a report-only drift
signal that reads DEAD PROBE for many readings" --terms "drift-audit DEAD PROBE report-only liveness
readings retire file ask history drift-history.tsv signal"`

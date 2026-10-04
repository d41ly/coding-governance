# KICK-aMendedFleet-1 — the orientation card shows the last drift reading from the node's history

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams kickoff · ratified 2026-10-04 · order 76

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Drift readings reach nobody: the review found them on neither the session card nor the unattended
close. Unit 48 of this build makes every bar's `drift-audit records` leg append one group of rows,
one per signal, to `drift-history.tsv` in the clone's git common dir. This unit adds one `drift —`
cell to the orientation card that summarises the LAST group in that file: when it was read, at
which commit, how many signals read nonzero, how many probes were dead, and which signals those
were. The card reads a file and never runs the report, so the cell costs no spawn of any kit.

## 2. Scope (IN)

- **S1** — `derive_drift_line` in `skills/session-kickoff/manifest-check.sh` prints exactly one
  line, and `render_card` prints it after the `worktrees —` cell and before the `live —` cell, so
  `CARD_PARTS_AWK` files it in the startup part. The file is `drift-history.tsv` in the directory
  `git rev-parse --git-common-dir` names, the same directory `CARD_DIR` is derived under, read
  once. Observed by AC1.
- **S2** — The reading. Columns are located by the file's first line, the header unit 48 defines,
  never by position, each name compared with one leading `#` stripped, since the header opens
  `#utc`; the cell needs `utc`, `sha`, `signal`, `state`, `value` and `of`. Only the
  file's last 400 lines are read. The last group is every trailing row sharing the last complete
  row's `utc` and `sha`; a trailing line whose field count differs from the header's is skipped as
  a write in progress. Observed by AC1 and AC2.
- **S3** — The line. With a group:
  `drift — last bar <utc> at <sha8> · <HEAD|not HEAD> · <n> signals · <z> nonzero · <d> dead`,
  where `<n>` counts the group's rows, `<z>` the rows whose state is `live` and whose value is a
  positive integer, and `<d>` the rows whose state is `dead`. When `<z>` or `<d>` is above zero the
  line continues ` · ` and the names: dead signals first as `<signal> DEAD`, then nonzero ones as
  `<signal>=<value>/<of>`, largest value first, comma-separated, the whole line cut at 320 bytes
  with `…` and the count of names left out. `HEAD` means the row's sha equals the `HEAD` the card
  already derived. Observed by AC1.
- **S4** — The other forms, each one line and none changing the exit status:
  `drift — skipped: no drift-history.tsv in the git common dir` when the file is absent;
  `drift — skipped: drift-history.tsv holds no reading` when it holds a header and no complete row;
  `drift — UNKNOWN: drift-history.tsv header lacks <column>` naming the first missing column.
  Observed by AC2.
- **S5** — The cell spawns no Python and calls no drift-audit file; `--card --replay` prints the
  stored cell and reads the history file no more. Observed by AC3 and AC4.
- **S6** — The comment block above `render_card` names the cell and its source, and the map
  dossier `memory/map/features/session-kickoff.md` gains one sentence on it beside its startup-cell
  sentence. Observed by AC5.
- **S7** — Arms in `skills/session-kickoff/manifest-check.test.sh` over a fixture history: two
  groups, an absent file, a header missing a column and a truncated last line. NOT OBSERVED by a
  criterion here: the suite runs once at the close, and the arms are declared under `New arm:` in
  §7.

## 3. Non-goals (OUT)

- Writing the history file. That is unit 48, and the card never fills a missing file.
- Running `drift_report.py`. The review priced the cell at no cost, and a report run costs seconds.
- A trend, a delta against an earlier group, or a "rising" flag. The delta reader is unit 49 at the
  unattended close; the rising signal is another unit of this build.
- Re-reading the history on `--card --replay`. A replay prints the session-start card, which is the
  card's contract since `KICK-aReplayedCard-1`.
- The overlap cell and a stale-CLI note, which are unit 77 and the unit split from it.
- Any edit to `skills/session-kickoff/SKILL.md`, which is at its byte cap and needs none.
- Bumping the kickoff kit version, owed once at the build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-48` — the history file and its header contract; without it
  every card prints the absent-file form.

## 4. Design

### Evidence

Read at the worktree HEAD `efc4b0c9`, whose bytes under `skills/session-kickoff/` equal base
`7af5f564`'s.

- `render_card` prints, in order, the `orientation —` header, `node —`, `tree —`, `worktrees —`,
  `live —`, `recent —` with five log lines, and the READY sentinel. `CARD_PARTS_AWK` treats every
  line before the first non-log line after `recent —` as the startup part, so a new cell must sit
  before `recent —`.
- `CARD_DIR` is derived from `git rev-parse --git-common-dir` once per run; the card's cap is
  `CARD_CAP_BYTES`, 8192, and the card measured 1961 B in the design record of
  `KICK-aReplayedCard-1`, budgeted at about 1.6 s quiet. `TOOL-aReplayedCard-7` records about ten
  git spawns per card write.
- The live `aGraftedHelix` build's unit 2 adds a `claims —` cell "directly below `live —`" on its
  branch, unbuilt at the date. Placing this cell ABOVE `live —` keeps that build's adjacency
  criterion true after both land.
- Unit 48's spec defines the header `#utc sha base_ref base_sha signal state value of key_hash`,
  tab-separated, one group per `--check` run sharing `utc` and `sha`, written in one `write` call,
  states `live`, `dead`, `not-asked` and `declared-empty`, and about 19 rows a group. No such file
  exists on node a today, because unit 48 is unbuilt.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_drift_line` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest derive_drift_line --as sh.function` answered OK |
| `drift —` | card cell | none |

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/map/features/session-kickoff.md`

### Alternatives rejected

- **Run `drift_report.py --json` at session start.** Seconds per session, and a dirty tree's reading
  is not a bar's; the history holds only bar readings by unit 48's design.
- **Read the whole file.** It grows by one group a bar without rotation; a bounded tail read keeps
  the cell's cost flat. 400 lines hold about twenty groups at today's signal count.
- **Show only the counts.** A count of nonzero signals says something moved and not what; the
  names are the part a session acts on, and the 320-byte cut bounds them.

## 5. Production-readiness checklist

- security — reads one file under the git dir, which git never pushes; fields are printed, never
  evaluated or joined into a path.
- perf / scale — one `head` and one `tail` of a local file in one `awk` pass; no git and no Python
  spawn added.
- error / empty / loading states — the three S4 forms; a write in progress is skipped by S2.
- observability — the cell is the observation; the absent form names the file it looked for.
- risks — a group larger than 400 rows would be counted short; at about 19 signals that is twenty
  times today's size.
- testing — AC1 to AC5 here; the arms in S7.
- migration — N/A: a new cell; cards already on disk are replayed as they are.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When a scratch clone made by `git clone --local` under a short `%TEMP%` directory has a
  hand-written `drift-history.tsv` in its common git dir holding the unit 48 header and two groups,
  the second of three rows (one `live` at value 2 of 76, one `live` at 0, one `dead`), and
  `bash skills/session-kickoff/manifest-check.sh --card --write --session t76a` runs in that clone,
  stdout carries one line opening `drift — last bar` with the second group's `utc`,
  `3 signals · 1 nonzero · 1 dead`, the dead signal's name followed by `DEAD` and the live one as
  `=2/76`, and that line sits after the `worktrees —` line and before the `live —` line.
  Red when: the first group's `utc` is printed, or the line lands after `recent —`.
  cost: seconds, plus the clone.
- **AC2** — When, in that clone, the history file is renamed away and the card is written under a
  new session id, stdout carries `drift — skipped: no drift-history.tsv in the git common dir` and
  the exit status is 0; when the header's `signal` column is renamed, the line reads
  `drift — UNKNOWN` naming `signal`; and when a three-field line is appended to the restored file,
  the line still reports the second group's `3 signals`.
  Red when: an absent or malformed file fails the card write, or a partial row is counted.
- **AC3** — When `grep -n "drift_report" skills/session-kickoff/manifest-check.sh` runs, it prints
  nothing.
  Red when: the card fills its cell by running the report.
- **AC4** — When a third group is appended to the fixture history after AC1's write and
  `bash skills/session-kickoff/manifest-check.sh --card --replay --session t76a` runs, the printed
  `drift —` line is byte-identical to AC1's.
  Red when: the replay re-reads the history.
- **AC5** — When `grep -n "drift —" memory/map/features/session-kickoff.md` runs, it hits the new
  sentence.
  Red when: the card gains a cell its dossier never names.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `shell hygiene (a loop fed by a command substitution)` · `line length` · `kit epoch (shipped bytes move, the version moves)`

New arm: `skills/session-kickoff/manifest-check.test.sh` · covers AC1 AC2 AC4 · a fixture history with two groups, an absent file, a header missing `signal` and a truncated last line, staged red by deleting the `derive_drift_line` call · none

## 8. Open questions

- **F1** — Where on the card does the cell sit?
  Options: below `live —`, where the live `aGraftedHelix` build's unit 2 puts its `claims —` cell
  with an adjacency criterion; above `live —`; in the kickoff body. The body is authored, and the
  cell is a derived fact; below `live —` would break that build's criterion when both land.
  RESOLVED (agent, 2026-10-04, delegated): above `live —`, after `worktrees —`, per S1.
- **F2** — What does the line carry: the counts, or the counts and the names?
  Options: counts only; counts and every name; counts and names cut at a byte bound. The report asks
  for one line from the last row, and a count alone does not say what to look at.
  RESOLVED (agent, 2026-10-04, delegated): counts, then dead and nonzero names, cut at 320 bytes,
  per S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 76, report items [A#55] and
  [A#60], unit 48's header contract, and a read of `render_card` and `CARD_PARTS_AWK` at base.

## 10. Reuse audit

The seams extended are `render_card` and the `CARD_DIR` derivation in
`skills/session-kickoff/manifest-check.sh`, whose `live —` cell is the precedent for a cell that
reads a file another kit writes and prints `skipped:` when it is absent. The file and its header
are unit 48's. `python tools/codebase-map/reuse_lookup.py "read the last row of a tab separated
history file in the git common dir for a session start card"` returned generic readers, among them
`read_text` in `tools/memory-tree/gen_build_index.py`, `read_journal` in the runlog library and
`resolve_kit_dir`, and no reader of a drift history; it prints `unscanned layers: .sh`, so
`git grep -n "drift-history"` over `skills/` and `tools/` was the shell probe, and it found nothing.
Recall returned `KICK-aReplayedCard-1`, the card's no-fetch derived-cell contract, and
`TOOL-aReplayedCard-7`, the card's spawn cost, which is why S5 adds no spawn. Where the report and
the tree disagree: none; the card still carries no drift cell, and the history file is unbuilt.

Recall terms used: `python tools/memory-recall/query.py "should the session orientation card show
drift readings, and what may the card read at session start" --terms "orientation card session
start drift-audit drift-history derived cell no fetch budget kickoff render_card live"`

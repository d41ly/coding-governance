# TOOL-aMendedFleet-48 — drift readings append to a node-local history file

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 48

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every drift reading is thrown away. The report prints to stdout, and the only persisted trace is the
`drift-audit records` leg's per-leg log under `<git-dir>/gate-logs/`, overwritten by the next bar
and private to one worktree. So nothing can say whether a signal is rising, which reading a close
should compare against, or what the orientation card should show. This unit makes the `--check`
run, the mode that leg executes, append one row per signal to `drift-history.tsv` in the clone's git
COMMON dir, so every worktree of a node writes one history: the HEAD sha, the base ref and its sha,
the signal, its state, value and `of`, and a hash of its detail keys that changes when the members
change at an equal count.

## 2. Scope (IN)

- **S1** — Under `--check`, after every signal is computed and before the exit status is decided,
  `drift_report.py` appends one row per record in `SIGNALS` order to `drift-history.tsv` in the
  directory `git rev-parse --git-common-dir` names, resolved against the repo root. `--offenders`,
  `--json` and the plain table never write, so the bar's signature run at another tree writes
  nothing. Observed by AC1 and AC4.
- **S2** — A file that does not exist, or exists empty, first receives one header line naming the
  columns, `#utc`, `sha`, `base_ref`, `base_sha`, `signal`, `state`, `value`, `of`, `key_hash`,
  tab-separated. Readers locate columns by this header, never by position, and the header is the
  file's whole contract with them. Observed by AC1.
- **S3** — Field values. `utc` is one timestamp shared by every row of the write, so a write is a
  GROUP identified by `utc` and `sha`. `sha` is HEAD in full and `base_sha` the base ref's commit in
  full. The timestamp shape is the one `RUN.md` parked rows carry, `2026-10-04T17:56:18Z`. `state` is one of `live`, `dead`, `not-asked` and `declared-empty`, the four states the table
  already prints. `value` and `of` are the record's own. Observed by AC1.
- **S4** — `key_hash` is the first 16 hex digits of the SHA-256 of the record's detail rows, each
  reduced to the key `--offenders` already prints for a row (sorted-key JSON with line locators
  stripped, occurrence ordinal appended), sorted and joined by LF. It is `-` for any state but
  `live`. The unlocating step, today nested inside `render_drift_offenders`, moves to module level
  under the name `extract_unlocated`, so the two keys are one spelling. Observed by AC2.
- **S5** — The rows reach the file in ONE `write` call on a file opened for append in binary mode,
  LF-terminated and UTF-8, so concurrent bars on one node interleave whole groups at worst. A write
  that fails prints one stderr line naming the path and the error and never changes the exit
  status; a write that succeeds prints one stdout line naming the row count and the path, so a
  missing line is a visible miss rather than silence. Observed by AC3 and AC4.
- **S6** — The kit README gains a section naming the file, its columns, that it is node-local and
  never pushed, that only `--check` writes it, and that it grows by one group per bar with no
  rotation. Its layout table gains the file. Observed by AC5.
- **S7** — The kit selftest gains one arm: two `--check` runs in a fixture repo write one header and
  two groups, `--offenders` and `--json` write nothing, a changed detail member at an equal value
  moves `key_hash`, and a directory squatting on the file's name leaves the exit status unchanged.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arm is declared under
  `New arm:` in §7.

## 3. Non-goals (OUT)

- A reader of the file. The BASE-to-HEAD delta at the unattended close is
  `TOOL-aMendedFleet-49`; the orientation card's last-row line is a later unit of this build.
- Rotation or a size cap. At about 19 rows of about 120 B a bar, a thousand bars is about 2 MB;
  a cap is filed when a reading shows it is needed, not before.
- A "rising" signal, the lexicon kill rule and identity baselines, which read this history and are
  other units of this build.
- The fresh-file lexicon arm the synthesis mentioned beside the history. It is a second mechanism.
- Writing from `--json` or the plain table. Those are an operator's ad-hoc reads, often from a dirty
  tree, and a history mixing them with bar readings could not say which reading graded a commit.
- Bumping the drift-audit kit version here; it is owed once at the build's close.

### Edges

- **hands-off** `TOOL-aMendedFleet-49` — the delta reader of this file at the unattended close.
- **hands-off** external — the orientation card's last-row line, a later unit of this build that
  reads the header contract S2 defines.

## 4. Design

### Data model

```
#utc	sha	base_ref	base_sha	signal	state	value	of	key_hash
<utc>	<40-hex>	refs/remotes/origin/main	<40-hex>	run_records_nonterminal_but_merged	live	2	76	<16-hex>
```

One group per `--check` run; rows of a group share `utc` and `sha`. Nothing in a field can carry a
tab or a newline: signal names and refs are the engine's own, and the counts are integers.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `extract_unlocated` | function, hoisted to module level | Python function, verb `extract` |
| `build_history_rows` | function | Python function, verb `build` |
| `resolve_history_path` | function | Python function, verb `resolve` |
| `write_drift_history` | function | Python function, verb `write` |
| `HISTORY_FILE` | engine constant, `drift-history.tsv` | Python constant |
| `HISTORY_COLUMNS` | engine constant, the header tuple | Python constant |

### Rollout

The file appears on the first bar after this lands, in each clone, with no adopter action. A clone
whose common dir is read-only reports the S5 stderr line on every bar and is otherwise unchanged.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`

### Alternatives rejected

- Writing under the per-worktree git dir, where `gate-logs/` lives. Each worktree would keep its own
  history and a close running in a fresh worktree would find none; the common dir is what the recall
  and map logs already use for the same reason.
- JSON lines instead of TSV. The brief names a TSV, and a shell reader of a header-keyed TSV is one
  `awk`; a JSON reader in shell is not.
- Hashing only the rows `--check` would red on. That is `--offenders`' population and is empty for
  every report-only signal, so the hash could not see a member swap on most of the table.

## 5. Production-readiness checklist

- security — the file holds signal names, counts, refs and hashes, never detail text, so no path or
  record content leaves the report; it lives in the git dir, which git never pushes.
- perf / scale — one SHA-256 per signal over at most a few hundred short keys and one append; a
  `git rev-parse --git-common-dir` is the only new spawn.
- error / empty / loading states — S5's two lines; a missing common dir is the same stderr line.
- observability — the file is the observation; S5's stdout line is its liveness.
- risks — unbounded growth, quantified in §3; two bars writing at once on one node, bounded by S5's
  single write.
- testing — AC1 to AC4 observe a scratch clone directly; the selftest arm is S7's.
- migration — N/A — a new file; nothing existing changes shape.
- user docs — S6's README section.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --check` runs twice in a `git clone
  --local` of the tree into a short directory under `%TEMP%`, that clone's `drift-history.tsv` in its
  common git dir holds one header line spelling the nine S2 columns in order and two groups, each with as many rows
  as `--json` prints records, every row with nine tab-separated fields and a `state` in the S3 set.
  Red when: a second run writes a second header, a group misses a signal, or a field count differs.
  figure: DERIVED; the record count is whatever `--json` prints on the day.
- **AC2** — When `python -c` imports `drift_report` from `tools/drift-audit` and builds rows for two
  copies of one live record whose detail lists differ in one member, the two `key_hash` values
  differ; for two copies whose details differ only in a `:<digits>` line locator they are equal; and
  `render_drift_offenders` still prints the same keys for a gateable over-pin record as before the
  hoist.
  Red when: a member swap at an equal count hashes equal, or a moved line number reads as a change.
- **AC3** — When the scratch clone's `drift-history.tsv` is replaced by a directory and
  `python tools/drift-audit/drift_report.py --check` runs there, stderr carries one line naming the
  path and the error, and the exit status equals the status the same run returns with the file
  writable.
  Red when: a failed write changes the verdict or passes silently.
- **AC4** — When `python tools/drift-audit/drift_report.py --offenders` and then `--json` run in the
  scratch clone, the file's line count is unchanged; and when `--check` runs in a linked worktree of
  that clone, its rows land in the clone's common `drift-history.tsv`, and the linked worktree's
  private git dir holds no such file.
  Red when: a non-bar mode writes a row, or a worktree keeps a history of its own.
- **AC5** — When `grep -c "drift-history.tsv" tools/drift-audit/README.md` runs, it reports at least
  2, one in the layout table and one in the section.
  Red when: the README does not name the file a bar now writes.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · two `--check` runs, a non-writing mode, a member swap at an equal count and a directory on the file's name, in a fixture repo · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — Which modes write?
  RESOLVED (agent, 2026-10-04, delegated): `--check` alone, per S1 and §3. It is the leg's mode, so
  every row is a bar reading of a committed tree, and the signature mode never writes into another
  tree's history.
- **F2** — What does `key_hash` hash?
  RESOLVED (agent, 2026-10-04, delegated): every detail row, unlocated as `--offenders` does it, per
  S4. Hashing only the offender rows was rejected in §4 because it is empty for report-only signals.
- **F3** — Rotate the file?
  RESOLVED (agent, 2026-10-04, delegated): no. Growth is quantified in §3 and nothing reads more than
  the tail and two groups; a cap is a follow-up when a reading needs it.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The seams extended are both in `tools/drift-audit/drift_report.py`: `render_drift_offenders`, whose
nested unlocating step becomes the shared `extract_unlocated`, and `main`'s `--check` branch, where
every record is already computed. The common-dir location follows the precedent the unattended
driver reads at `<git-common-dir>/recall/queries.jsonl` and `<git-common-dir>/codebase-map/lookups.jsonl`.
`python tools/codebase-map/reuse_lookup.py "append drift signal readings to a history file in the
git common dir"` returned generic readers, `append_backlog` in the map kit and the runlog journal
reader, and no history writer for drift readings; `git grep -n "drift-history" -- tools` finds
nothing. Where the report and the tree disagree: the synthesis said readings persist "in a degraded
form, one overwritten text log per git dir", and that is still the state, under `gate-logs/`.

Recall terms used: `python tools/memory-recall/query.py "is any drift reading persisted across runs
as a history" --terms "drift-audit history readings persisted git-common-dir records leg gate-logs
overwritten tsv trend rising"`

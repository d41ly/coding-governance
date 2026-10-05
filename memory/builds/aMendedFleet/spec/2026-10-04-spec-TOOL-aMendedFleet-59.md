# TOOL-aMendedFleet-59 — timeout retries are grouped by leg across every git dir of the clone

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 59

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`legs_retried_after_timeout` sums the `retried` count of the run records under the CURRENT
worktree's git dir, and names no leg. The gate runner writes a run record into whichever git dir ran
the bar, so a session in a fresh worktree reads DEAD while its sibling worktrees hold the readings,
and a reader who wants to know WHICH leg keeps needing its retry must open `<i>.retry.leg` files by
hand. This unit makes the signal read every git dir of the clone, the common dir and each linked
worktree's, and report one detail row per leg: how often it was retried, how often it failed even on
its retry, and in how many git dirs. On node a that turns a DEAD reading into nine retries of
`straggler-guard arms` and three of `brief-recorded`, one of which failed after its retry.

## 2. Scope (IN)

- **S1** — THE POPULATION. `read_git_dirs` in `tools/drift-audit/drift_report.py` returns the
  clone's common dir, from ONE `git rev-parse --path-format=absolute --git-common-dir`, followed by
  every directory under its `worktrees/` in sorted order. A clone with no linked worktree returns the
  common dir alone. Observed by AC1 and AC3.
- **S2** — THE READING. `measure_legs_retried_after_timeout` reads every `gate-run/*/verdict` under
  every git dir S1 returns, summing `retried` as it does today, so `value` keeps its meaning and `of`
  becomes the number of run records read across them. It also reads every `<i>.retry.leg` row beside
  those verdicts, whose first tab field is the leg name and second the status the retry ended on.
  Observed by AC1 and AC2.
- **S3** — THE DETAIL. One row per leg, ordered by `retried` descending then name:
  `{"leg", "retried", "failed_after_retry", "git_dirs"}`, where `failed_after_retry` counts rows whose
  status is not `ok`. The record gains `git_dirs`, the number of git dirs holding at least one run
  record, and `unattributed`, the verdict sum minus the number of retry rows read, which is 0 when
  every counted retry names its leg. Observed by AC1 and AC2.
  **Readers:** by name: `tools/drift-audit/selftest.py` reads the record's `value`, `of`, `live` and
  `gateable`, and none of them changes meaning; the per-run detail rows it replaces are read by no
  program. by value: NO VALUE READERS — the signal is report-only and `--check` never reads it.
- **S4** — LIVENESS, unchanged in kind: `live` is true when at least one verdict across the git dirs
  carries the `retried` key. A clone where no git dir holds such a record still reads DEAD. Observed
  by AC3.
- **S5** — The comment block above the signal and the drift-audit README's row for it say the
  reading spans every git dir of the clone and names legs, and that a removed worktree takes its
  records with it. Observed by AC4.
- **S6** — Self-test arms in `tools/drift-audit/selftest.py`: a fixture with a run record under
  `.git/worktrees/<name>/gate-run/` beside one under `.git/gate-run/`, with retry rows for two legs,
  one ending `fail`. NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms
  are declared under `New arm:` in §7.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED by
  a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and §7
  names the leg that reads it.

## 3. Non-goals (OUT)

- A history. The runner keeps a handful of run directories per git dir and sweeps the rest, and
  `git worktree remove` deletes a worktree's git dir with its records; the reading stays a window.
- Raising or lowering any leg's ceiling. The reading is the input to that act; `straggler-guard arms`
  is named for the owner, not changed here.
- A pin or a gate. Report-only, as today.
- Reading another clone's or another node's git dirs.
- Sharing a parser with unit 58's gate-yield mode: see §8 F1.
- Bumping the drift-audit kit version, owed once at the close.

### Edges

- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/drift-audit/` and `tools/run-gates/`
equal base `7af5f564`'s.

- In this worktree `python tools/drift-audit/drift_report.py --json` reports the signal with value
  0, `of` 0 and `live` false: this worktree has never run a bar.
- Under the clone's common dir on node a, 26 run directories sit across the common dir and its 7
  worktree git dirs. Their verdicts sum `retried` to 12, and 12 `<i>.retry.leg` rows sit beside
  them, in 4 worktree git dirs: `straggler-guard arms` 9, all `ok`; `brief-recorded` 3, one `fail`.
  PINNED, measured 2026-10-04; S2 re-derives them.
- A `<i>.retry.leg` row is the leg row's shape: name, status, exit code, seconds, two clock stamps
  and the head sha, tab-separated, written by `tools/run-gates/run-gates.sh`.
- The review's figure was the same 9 retries of `straggler-guard arms` across 4 git dirs, plus
  `brief-recorded`; it reproduced exactly.

### Inventory

- `read_git_dirs` — cell `py.function`; the lexicon answered `use read_git_dirs` to the first
  spelling tried, from `python tools/lexicon/lexicon.py --suggest list_git_dirs --as py.function`.
- `git_dirs`, `unattributed`, `failed_after_retry` — JSON keys of the record; no naming cell grades
  them.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Read `git worktree list --porcelain`.** It names worktree paths, not their git dirs, and needs a
  second call per worktree to resolve one; the git dirs are the directories under `worktrees/`.
- **Read `<git-dir>/gate-ledger.tsv`.** It keeps one row per leg, the last observation, so it cannot
  count retries.
- **Change `value` to a count of distinct legs.** The value's meaning is what the README and the
  existing arms assert; the per-leg view is the detail's job.

## 5. Production-readiness checklist

- security — N/A: reads this clone's own git dirs; no new input.
- perf / scale — one git spawn as today, plus file reads bounded by the runner's own sweep.
- error / empty / loading states — an unreadable verdict or row is skipped as today; a git dir with
  no `gate-run/` contributes nothing; no record anywhere reads DEAD.
- observability — per-leg rows, `git_dirs`, and an `unattributed` count that is nonzero when a
  verdict counted a retry no row names.
- risks — a reading now moves when a sibling worktree runs a bar, which is the point.
- testing — AC1 to AC4 here; the arms in S6.
- migration — N/A: nothing stored changes.
- user docs — the README row in S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs in this worktree on node a,
  the `legs_retried_after_timeout` record reads `live` true, `git_dirs` at least 4 and `unattributed`
  0, and its detail carries a `straggler-guard arms` row whose `retried` equals the number of
  `.retry.leg` files under the common dir whose first field is that name, counted by
  `grep -l "^straggler-guard arms" -r --include=*.retry.leg` over `git rev-parse --git-common-dir`.
  Red when: the reading stays scoped to this worktree's git dir, or a leg's count disagrees with its
  rows.
  fixture: node a's common dir holds the records today; a fresh clone holds none.
  figure: DERIVED at observation time; 9 at writing, and the runner's sweep moves it.
- **AC2** — When the same record is read, its `brief-recorded` row carries `failed_after_retry` 1.
  Red when: a leg that failed on its retry reads like one that passed on it.
  figure: PINNED at writing, 2026-10-04.
- **AC3** — When, in a scratch repository under a short `%TEMP%` path with no run record anywhere,
  holding a copy of `tools/drift-audit/`, a `.memory-tree.conf` stub and `GOV_DEFAULT_BRANCH`
  naming its branch, its copy of `drift_report.py --json` runs, the record reads `live` false;
  and when a verdict carrying `retried 1` and one retry row are written under that repository's
  `.git/worktrees/w1/gate-run/r1/` and it runs again, `live` is true and `git_dirs` is 1.
  Red when: a record in a linked worktree's git dir is missed, or an empty clone reads 0 rather than
  DEAD.
  cost: seconds; the scratch repository is the only thing written.
- **AC4** — When `grep -n "legs_retried_after_timeout" tools/drift-audit/README.md` runs, its
  signal-table row says the reading spans every git dir of the clone and names legs.
  Red when: the README still says "this git dir".

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a fixture with run records in the common dir and a linked worktree's git dir and retry rows for two legs, staged red by reading the current git dir alone · `CHECK_FLOOR` moves by the checks the arms add

## 8. Open questions

- **F1** — The review says this grouping shares one parser with unit 58's gate-yield mode. Unit 58
  reads the gates journal through the runlog kit; this signal reads `<i>.retry.leg` rows inside the
  drift-audit kit. A kit file may not name a sibling kit by literal, so one module cannot serve both,
  and the two inputs share no shape beyond the leg name.
  RESOLVED (agent, 2026-10-04, delegated): no shared parser; both key their rows by the leg name the
  manifest spells. Unit 58's spec records the same.
- **F2** — Which git dirs are "every git dir"?
  Options: the common dir and every directory under its `worktrees/`; the git dirs `git worktree
  list` resolves. The first needs one spawn and includes a prunable worktree whose directory is gone
  from disk but whose git dir still holds records, which is a reading worth keeping.
  RESOLVED (agent, 2026-10-04, delegated): the common dir and its `worktrees/` directories, per S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's drift-audit item 8 ([#53]) and a count of
  the run records under node a's common dir at base.
- rev-2 · 2026-10-05 · AC3 runs the scratch repository's own copy of the kit: the report resolves
  its repo root from the script's location, so the worktree's copy run inside the scratch repository
  reads the worktree, not the scratch repository. Closed by the build pass.

## 10. Reuse audit

The seam extended is `measure_legs_retried_after_timeout` in `tools/drift-audit/drift_report.py`,
with its `_RUN_RECORD_DIR` and its verdict parsing reused as they are, and the run-record layout
`tools/run-gates/run-gates.sh` writes, read and not edited. `python
tools/codebase-map/reuse_lookup.py "read gate run records from every worktree git dir and group
timeout retries by leg"` returned `read_journal` in `tools/runlog/runlog_lib.py`, which reads one
producer file of another kit, and generic `read`, `git` and `run` helpers ranked by name fan-in; no
existing seam in the drift-audit kit enumerates a clone's git dirs, and the runlog kit's
`resolve_journal_root` resolves only the common dir and sits across a kit boundary. The scan names
`.sh` as unscanned; the one shell file involved is the writer, read for its row shape. Recall
returned `TOOL-aPromptedMandate-10`, that a timeout verdict cannot tell a spinning leg from a starved
one, which is why this reports and does not judge. Where the report and the tree disagree: nowhere;
9 retries across 4 git dirs re-measured exactly.

Recall terms used: `python tools/memory-recall/query.py "why does the timeout retry signal read only
one git dir and how are retries recorded" --terms "legs_retried_after_timeout retry.leg verdict
retried gate-run git-dir worktree ceiling timeout straggler-guard"`

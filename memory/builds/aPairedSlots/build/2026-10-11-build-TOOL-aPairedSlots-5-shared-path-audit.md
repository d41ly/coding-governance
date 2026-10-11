# Every path two concurrent bars on one repository both write

**Serves:** journal TOOL-aPairedSlots-5 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8

Audited on node a on 2026-10-11 against `tools/run-gates/run-gates.sh` as aFrugalTurnstile landed
it (origin/main `d19938f3`), before any code of this build. Two bars on two worktrees of ONE
repository share its git common dir and the host's temp root; each has its own worktree git dir.
The question per path: does a second concurrent writer lose, tear or corrupt anything?

## The predicates, run over the real tree

1. Every redirection, `mv`, `cp`, `rm` and `mkdir` in the runner whose target names `gd`, `GD`,
   `TS_COMMON`, `WORK_COMMON`, the health log, the ledger, the summary file, the run root, the run
   log, `TMPDIR` or `HOME`: 26 hits, every one classified below.
2. Every `gates.log`, `GOV_RUNLOG`, `drift-history` and `gate-full-green.shared` site in the runner.
3. Over every script a leg names in `tools/gate-legs.json`, and every `*.test.sh`, `selftest.py`
   and `test_*` file under `tools/`, `.githooks/` and `skills/` (135 files): a literal `/tmp/<name>`
   (86 code hits), an unassigned `$TEMP` or `$TMP` (1096 raw hits, 0 once assignments in the same
   file are honoured), `%TEMP%` (2), `${TMPDIR:-/tmp}/<name>` (4), a `$HOME/.` write (3) and
   `--git-common-dir` (47). Each surviving hit was read in context by a read-only agent and
   classified; its report is summarised under "Leg fixtures".

## The runner's own paths

| Path | Where | Writer | Disposition |
|---|---|---|---|
| `gate-ledger.tsv` | worktree git dir | read-merge-write at exit | per-worktree; S1 of TOOL-aPairedSlots-5 keeps it one bar's |
| `gate-run/<id>/`, `gate-run/current`, the pruning of old records | worktree git dir | per run | per-worktree; S1 |
| `gate-last-summary.txt`, `gate-last-failure.txt`, `gate-logs/` | worktree git dir | per run | per-worktree; S1 |
| `gate-full-green`, `gate-inherited-green` | worktree git dir | tmp then `mv` | per-worktree; S1 |
| `gate-queue-status`, `gate-queue-heartbeat` | worktree git dir | each queued tick | per-worktree; S1. The prompt placed the heartbeat in the common dir; the code writes `$gd`, the worktree git dir |
| `runlog/gates.log` | common dir | one `printf >>` line per bar | COLLIDES at long lines; fixed by TOOL-aPairedSlots-7 S1 (measurements below) |
| `health.log` | common dir | one short `>>` line per event; a tail-and-`mv` trim at 500 lines | append safe as measured; the trim COLLIDES; TOOL-aPairedSlots-7 S2 |
| `gate-full-green.shared` | common dir | `cp` to a FIXED `.tmp` name, then `mv` | COLLIDES on the staging name; TOOL-aPairedSlots-7 S3 |
| `gate-timings.tsv` | worktree and common dir | `rm -f` of a retired file | safe; removing an absent file twice is a no-op |
| `gate-work.*` and its `owner` record | ambient temp root | `mktemp -d`, then owner tmp-and-`mv` | per-bar; the sweep removes only a dir whose owner names THIS common dir and whose pid fails `kill -0`, so a live sibling withholds it. Safe while both bars run under one MSYS runtime, which shares the pid table; a runtime that does not would read the sibling as dead |
| `TMPDIR` for legs | `$WORK/tmp` | exported per bar | per-bar |
| process-monitor reap | leg pids in `$WORK/*.pid` | `reap.py --kill-msys <pid>` and `remove_descendants` | per-bar: both walk the DESCENDANTS of this bar's own leg pids, never a sibling's |
| `drift-history.tsv` | common dir | `drift_report.py --check`, leg `drift-audit records`, on every default bar | the append is one binary write, measured whole; the header-on-empty decision COLLIDES at creation; TOOL-aPairedSlots-7 S4 |

## The measurements behind the dispositions

Node a, Git-Bash, `$TEMP/apsx`, 2026-10-11. Three or four concurrent writers into one file.

| Writer | Line or group size | Written | Torn |
|---|---|---|---|
| `printf '…\n' >> f` | ~100 B | 4500 | 0 |
| `printf '…\n' >> f` | 600 B | 3200 | 0 |
| `printf '…\n' >> f` | 1000 B | 3200 | 0 |
| `printf '…\n' >> f` | 2000 B | 3200 | 146 |
| `printf '…\n' >> f` | 3900 B | 900 | 38 |
| `printf '…\n' >> f` | 8000 B | 900 | 365 |
| `printf '…\n' >> f` | 12000 B | 900 | 308 |
| `printf '…\n' \| cat >> f` | 2000 B | 900 | 0 |
| `printf '…\n' \| cat >> f` | 12000 B | 900 | 0 |
| python `open(f, "ab").write(group)` | 27 rows, ~4.6 KB | 24300 rows, 900 groups | 0 rows, 0 groups split |

The longest `gates.log` line on node a was 923 bytes, under the tear threshold measured here, but a
line grows with every failing leg's name, so the margin is not a property of the writer.

## Leg fixtures

COLLIDES:

- `tools/drift-audit/drift_report.py` `write_drift_history` — the header race above; TOOL-aPairedSlots-7 S4.
- `tools/process-monitor/adopt-process-monitor.test.sh` — the broken-monitor and throttle arms run
  the session hook against the REAL root and clear and write `procmon-stamp` in the real common dir.
  The leg is in the `selftests` chunk, held by default, so only `GATE_SELFTESTS=1` bars meet it; a
  live session's own hook writes the same file. TOOL-aPairedSlots-8.

Safe, by class:

- In a scratch fixture repository or `mktemp` dir: `check-wiring.test.sh` (8 sites, every one after
  `newrepo`), `push-main.test.sh`, `run-gates.runlog.test.sh`, `run-selftests.test.sh`,
  `runlog/selftest.py`, `memory-recall/selftest.py`, `check-unattended.test.sh`'s grafts,
  `stop-guard.test.sh`, `unattended.test.sh`'s common-dir sites, `codebase-map/selftest.py`.
- Unique per process: `check-unattended.test.sh`'s `/tmp/<name>.$$` sites,
  `check-playbook-parity.sh`'s `${TMPDIR:-/tmp}/pp.$$`, the hygiene checker's bare `mktemp`.
- Not a write: `manifest-check.sh`'s health-log resolver (never called by the leg),
  `manifest-check.test.sh`, `scratch-guard.test.sh`'s orientation read, `foreign-prefix.gov.test.sh`
  (reads the runner's floor file), `run-selftests.sh`'s usage text, `adopt-unattended.sh`,
  `check-unattended.sh`, `govkit/selftest.py`'s TOML answer, `lexicon/selftest.py`'s heredoc text,
  the workflow suites' JSON paths, `agent-cap.test.sh`'s path data.
- Read-only checks a concurrent writer could break: `memory-recall/selftest.py` reads the real
  `recall/queries.jsonl`, which no leg writes; a live session querying does, independent of bars.

## Near-misses, recorded so nobody re-audits them

- The memory-recall cache under the common dir is keyed per worktree and built for concurrent use.
- `gate-queue-heartbeat` was named by the prompt as a common-dir path; it is under the worktree git
  dir, so it needs nothing beyond S1.
- The scratch sweep's pid test assumes one pid table; two bars of one repository under two
  different MSYS runtimes are outside what any node runs today.

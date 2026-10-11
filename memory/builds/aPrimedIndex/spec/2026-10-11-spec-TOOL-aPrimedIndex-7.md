# TOOL-aPrimedIndex-7 — the regen verb's and the runner's review minors, batched

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close every MEDIUM and LOW finding of closing review round 1 that lands in the regen verb, the
runner or their documents, as the one batched unit the build method prescribes for minors over one
write set (M1, M2, M4, M5, M6, M7, M10, L1, L3, L4, and the README halves of H1 and L2).

## 2. Scope (IN)

- **S1** (M1) — `run_command` sends a child's output to a temporary file, not a pipe, so a timeout
  returns at the bound. On a timeout it kills the child's whole tree: `taskkill /F /T` on Windows,
  the process group on POSIX. Observed by AC1.
- **S2** (M2) — A write that exits non-zero is followed by its own check. A fresh check makes the
  write `declined`, which is reported and does not fail the stage. Observed by AC2.
- **S3** (M4) — `main` switches stdout to UTF-8 with `errors="replace"`, as `gen_map.py` does.
  Observed by AC3.
- **S4** (M5) — A `bash` argv runs under the bash the kit's `profile_bar.resolve_bash` finds by
  running each candidate against a tracked descriptor, never by `PATH` alone. Observed by AC3.
- **S5** (M6, M7) — Arm 1r gains three checks. A failed stage-1 write stops stage 2. A
  declined write lets stage 2 run. The runner's `--regen-list`, `--regen` and `--regen-check`
  hand-over is driven end to end. Observed by AC2 and AC4.
- **S6** (M10) — `build_items` refuses an item whose write or check script operand, the token after
  a `python`, `python3` or `bash` interpreter, is absent from the tree. The runner gives exit 2 from
  the verb, a refused declaration, its own remedy line, apart from exit 1, stale. Observed by AC5.
- **S7** (L3) — `--list` names each `[[regenerate]]` row it skips for carrying no `stage`, and the
  memory-tree descriptor's comment stops claiming the reader joins its duplicate row by argv.
  Observed by AC6.
- **S8** (L1, L4, H1 and L2 halves) — The unattended README's `[[generated]]` row-shape paragraph
  names the three keys. The runner header, its skip line and the run-gates README stop saying a skip
  never moves a verdict, and say the push boundary scrubs the knob (TOOL-aPrimedIndex-6). The README
  names govkit apply's verdict reads as a bar entry point that skips the preflight
  (DEPL-aPrimedIndex-1), and limits "the branch left where it was" to `--prepare`. Observed by AC6.

## 3. Non-goals (OUT)

- No `[[outcome]]` evaluation inside the verb: the check-after-a-failed-write rule is the review's
  stated minimum, and it needs no second reading of govkit's outcome grammar.
- No predicate gate over `subprocess.run` pipes or `shutil.which("bash")` across the tree; each is a
  gotcha class already (`bounded-through-a-pipe-is-unbounded`, `subprocess-resolves-a-different-shell`).
- The lander's findings are TOOL-aPrimedIndex-8's.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-2` — the verb being repaired.
- **consumes-from** `TOOL-aPrimedIndex-6` — the scrub the README and the skip line now state.

## 4. Design

### Data and flow

`run_command(argv, root, bound)` opens a `tempfile.TemporaryFile()` for the child's stdout and stderr,
starts it with `Popen` (POSIX: `start_new_session=True`), waits with `timeout`, and on expiry kills
the tree before reading the file back. `run_writes` runs a failed item's check; a check that exits 0
turns the item into `declined` and the stage continues. `build_items` resolves each argv's script
operand under the tree and refuses one that does not exist. The runner's preflight reads the verb's
exit: 1 prints the stale remedy, 2 prints `declaration refused — fix the descriptor it names`.

### Inventory

New in `regen.py`: `resolve_bash` is imported from `profile_bar.py` beside it; `check_operand` (verb
`check`) refuses a missing script; `run_tree_kill` (verb `run`; the closed table has no kill verb)
runs the platform's kill command over the child's tree and reports its outcome.

### Files touched (estimate)

- `tools/run-gates/regen.py`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `tools/memory-tree/kit.toml`
- `tools/unattended/README.md`
- `memory/map/generated/symbols.json`

## 5. Production-readiness checklist

- security: N/A — the same declared argvs run; the tree kill is scoped to the child's own pid.
- perf / scale: the temp file costs one file per command; a declined write costs one extra check.
- error / empty / loading states: declined, refused and timed-out items each print a named line.
- observability: `--list` announces skipped rows; the runner separates refused from stale.
- risks: `taskkill /T` follows Windows parentage, which MSYS forks can escape; the bound still returns
  because the output no longer rides a pipe the orphan holds.
- testing: arm 1r's new checks, each observed red on a break staged in the verb.
- migration: none.
- user docs: the two READMEs and the runner header (S8).

## 6. Acceptance criteria

- **AC1** — When a fixture check runs `bash -c 'sleep 8 & wait'` under `GATE_REGEN_BOUND=2`,
  `regen.py --check` prints the item's `timed out` verdict and returns in under 6 s. Red when: it
  returns only after the sleep, as the pipe version did at 8.1 s.
- **AC2** — When a fixture's stage-1 write exits 1 while its check exits 0, `regen.py --write`
  prints `declined` for it, runs stage 2, and exits 0; when the stage-1 check also exits 1 it prints
  `stopped after stage 1` and the stage-2 marker is never written. Red when: either outcome swaps.
- **AC3** — When `regen.py --check` runs with `PYTHONUTF8=0`, it prints `·` as UTF-8 and exits as it
  does otherwise; and `regen.py --list` run from PowerShell on node `a` reports every bash item fresh
  through `--check` in this linked worktree. Red when: the output is in the code page, or a bash item
  reads "not a git repo".
- **AC4** — When arm 1r drives `--regen-list` through the runner, the output equals the verb's;
  `--regen` then `--regen-check` exit 0 with no `gate queue:` line. Red when: an argument reaches the
  bar's setup.
- **AC5** — When a fixture descriptor's check names a deleted script, `regen.py --list` exits 2
  naming the missing path, and the runner prints `declaration refused`. Red when: the item lists, or
  the runner prints the stale remedy.
- **AC6** — When `regen.py --list` runs on this tree, it announces the memory-tree `[[regenerate]]`
  row it skips, and `grep -n "write" tools/unattended/README.md` shows the three keys. Red when: the
  skip is silent or the README still teaches the old shape alone.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC4 AC5 · fixtures for a slow check, a declined and a failed write, and a deleted script · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from closing review round 1's minors.

## 10. Reuse audit

The bash resolver is `resolve_bash` in `tools/run-gates/profile_bar.py`, in this same kit, which the
review named; it is imported rather than copied. The stdout switch follows `gen_map.py`. For the tree
kill, `reuse_lookup.py` on "kill a timed-out child process and its whole tree" returned
`run_kill` in `tools/process-monitor/reap.py`, which belongs to another kit: a copy-installed kit
cannot import it, so no existing seam fits, and the step is the platform kill the review names.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.

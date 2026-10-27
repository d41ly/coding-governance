# TOOL-dLinkedLibrary-61 — `--observe` kills the process tree at its bound and routes each run's output to a file

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 7 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |
| [2026-10-27-build-TOOL-dLinkedLibrary-61-deviation-611.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-61-deviation-611.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 24 at HIGH**, report item **H5**. No other id shares the item. The skeptic judged the
finder's fix unsound and corrected it; this unit builds the correction.

`TOOL-dLinkedLibrary-49` S2 bounds each run of `gotchas.py --observe` by the leg's `ceiling`, and its §5
says "the bound kills the child it started and nothing else". It states no rule for the process tree or
for where output goes. Most manifest legs are `bash` argv that start grandchildren, and
`tools/run-gates/regen.py:29-32` documents that an MSYS fork can escape Windows parentage. With a
`subprocess` timeout and captured pipes, the read after the kill waits for a grandchild that still holds
the pipe, so `--observe` blocks past its bound, the defect unit 49 exists to close, and its AC3 stub, one
sleeping process, stays green either way.

This unit runs each observed argv the way `regen.py` already runs a bounded command: output to a file,
never a pipe, and the whole process tree killed at the bound, carried inline under a parity row. It
repairs `TOOL-dLinkedLibrary-49` and builds one step after it (order 7).

## 2. Scope (IN)

- **S1** — The canonical block. `tools/run-gates/regen.py` wraps `run_tree_kill` (:249-267) between `#
  >>> tree_kill_py` and `# <<< tree_kill_py`, its body unchanged, so the kill it already uses becomes a
  block a second module can carry. Observed by AC2.
- **S2** — The observed run. `gotchas.py --observe` (`TOOL-dLinkedLibrary-24` S3, as unit 49 bounds it)
  carries the `tree_kill_py` block inline and starts each clean and planted run with `Popen`, its stdout
  and stderr to one temporary file under the scratch clone, stdin `DEVNULL`, and `start_new_session=True`
  on POSIX; it waits with the leg's ceiling, and on `TimeoutExpired` calls `run_tree_kill` and records
  `unobservable: past <n>s`, never reading a pipe. Observed by AC1.
- **S3** — The row. `PARITY_ROWS` (`tools/lib/resolve-python.test.sh:168-187`) gains
  `tree_kill_py|$ROOT/$RUNGATES_DIR/regen.py|$RUNGATES_DIR/regen`, the kit-file canonical shape the
  `mempause_sh` row (:179) already uses. Observed by AC2.

## 3. Non-goals (OUT)

- The verdict table, the bound's value and the status reading: `TOOL-dLinkedLibrary-49` S1 to S3,
  unchanged.
- How the leading `bash` or `python3` of an argv resolves: id 18 of the same audit, a minor, batched in
  `TOOL-dLinkedLibrary-64`.
- `regen.py`'s own `run_command`: unchanged; only its kill function becomes a block.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-49` — S2's bound on each `--observe` run, which this unit's S2 enforces over the process tree (id 24)
- **hands-off** `TOOL-dLinkedLibrary-67` — S2's observed `Popen` and AC1's `observe-tree-hang` plant, which unit 67 feeds resolved argv and rebuilds (id 2 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — `tree_kill_py`, the observer's output file and AC2, which unit 74 completes (ids 11, 26, 43, 31, 32 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/run-gates/regen.py:249-267`: `run_tree_kill` runs `taskkill /F /T /PID <pid>` on Windows and
  `os.killpg` on POSIX, then kills and reaps the child, each step best-effort.
- `tools/run-gates/regen.py:286-293`: "OUTPUT THROUGH A FILE, NEVER A PIPE", measured 6.5 s for `sleep 6
  & wait` under a 1 s bound when a pipe was read; the child starts with `start_new_session` on POSIX.
- `tools/lib/resolve-python.test.sh:179`: `mempause_sh`'s canonical is a kit file, the bar's runner, the
  precedent for a canonical outside `tools/lib`.

### Why a grandchild in the plant

A stub of one sleeping process is killed by a child-only kill, so it cannot tell the two rules apart.
`bash -c 'python -c "…sleep…"; true'` keeps bash as the parent, because a compound command is not exec'd
in place, and puts python one level down holding the output; only a tree kill with file-routed output
returns at the bound.

### Files touched (estimate)

- `tools/run-gates/regen.py`: S1
- `tools/memory-tree/gotchas.py`: S2, and the `observe-tree-hang` selftest case (`--selftest`, :833)
- `tools/lib/resolve-python.test.sh`: S3

### Alternatives rejected

- **`subprocess.run(timeout=…, capture_output=True)`.** Its post-kill read waits on a pipe a grandchild
  holds, the measured case at `regen.py:286-288`.
- **Importing `regen.py` from `gotchas.py`.** The memory-tree kit installs without the run-gates kit
  (`tools/memory-tree/kit.toml:7`, `requires = []`), so the import has no file to find in such an
  adopter.

## 5. Production-readiness checklist

- security — the observed argv runs in a scratch clone, as `TOOL-dLinkedLibrary-24` S3; the bound kills
  the process tree it started and nothing else.
- perf / scale — one temporary file per run in place of two pipes.
- error / empty / loading states — a run that cannot start records `unobservable: clean exit 127`, as
  unit 49's table reads a non-zero clean run.
- observability — the output file's tail is printed under a run past its bound.
- risks — `taskkill /T` reaches only processes still parented to the child; an orphan that escaped is
  left, and the verb still returns at the bound because no pipe is read.
- testing — the `observe-tree-hang` case of the module's `--selftest`, AC1.
- migration — none.
- user docs — none under `help/`: `memory/HYGIENE.md`'s `--observe` sentence (unit 49 S4) already names
  the bound.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --selftest` runs its `observe-tree-hang` case,
  `--observe` against a stub leg of `ceiling` 2 whose planted argv is `bash -c 'python -c "import os, time;
  open(\"<pidfile>\", \"w\").write(str(os.getpid())); time.sleep(10)"; true'`, it returns within 5 seconds,
  records `unobservable: past 2s`, and one second later the pid in `<pidfile>` names no live process; the
  selftest prints the case `ok`.
  Red when: the verb waits on the grandchild, or kills only the bash parent.
- **AC2** — When `grep -n "^tree_kill_py|" tools/lib/resolve-python.test.sh` runs, it prints the row, and
  the `tree_kill_py` blocks sliced from `tools/run-gates/regen.py` and `tools/memory-tree/gotchas.py` with
  `awk '/^# >>> tree_kill_py/,/^# <<< tree_kill_py/'` compare equal under `diff`.
  Red when: the copy drifts, or no row grades it.

## 7. Gates

`gotchas selftest` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py · covers AC1 · the `observe-tree-hang` selftest case, the failing case staged by a child-only kill with captured pipes · none
New arm: tools/lib/resolve-python.test.sh · covers AC2 · the `tree_kill_py` parity row, the failing case staged by one byte changed in the copy in gotchas.py · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 24 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Where does the kill live?** Options: (a) `regen.py`'s `run_tree_kill` as a parity-gated block
  carried inline; (b) a new canonical under `tools/lib`; (c) a second hand-written kill in `gotchas.py`.
  (c) is a copy with no gate (the charter's reuse rule); (b) moves a working function out of its kit for
  no reader beyond these two. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the most
  feature-rich survivor, tie-broken by reuse of the seam M5 found. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 24 (HIGH, item
  H5), on the skeptic's corrected fix.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-67, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is `run_tree_kill` and the file-routed `Popen` of `run_command` in
`tools/run-gates/regen.py:249-303`, with the `PARITY_ROWS` table that grades an inline copy. `python
tools/codebase-map/reuse_lookup.py "kill a timed out child process tree with output routed to a file"`
ranked `tree`, `read_git_output`, `load_map_tree` and `corpus_files`, each a name-stem match and none a
bounded runner, so the probe missed the seam and it was found by reading `regen.py`; the stale hit is
recorded here as the M5 rule asks.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`

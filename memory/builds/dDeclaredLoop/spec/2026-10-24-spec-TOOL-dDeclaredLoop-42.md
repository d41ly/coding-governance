# TOOL-dDeclaredLoop-42 — the acceptance re-run bounded on the clock, its commands run by bash, never cmd.exe

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 9 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-42-deviation-421.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-42-deviation-421.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 51 at HIGH**, its item **H17**, alone in that item; its shell-resolution half
is id 28 (item M21, MEDIUM), batched into `TOOL-dDeclaredLoop-56`. `TOOL-dDeclaredLoop-17` §4 "The
re-run" runs each command "through the platform shell" with its output captured and "a timeout kills
the command". Killing the shell leaves grandchildren holding the output pipe, so the read after the
kill blocks: the class `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` records, measured twice
in this repository. On Windows the platform shell is cmd.exe, which cannot run the bash-syntax
criteria every spec writes. A hung command then blocks `loop_witness.py acceptance` and the
`loop computed witness` leg indefinitely, and the `finally` worktree removal fails while a grandchild
holds the directory. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-17`.

## 2. Scope (IN)

- **S1** — Each command runs as the argv `[resolve_bash(), "-c", command]` with `shell=False`, never
  `shell=True`, `resolve_bash` carried inline in `tools/loop/loop_witness.py` from the copy
  `tools/govkit/govkit.py:1144` holds, the one paired with `resolve_shell_argv` that refuses the
  System32 and WindowsApps launchers. Observed by AC1.
- **S2** — Output goes to a file, never a pipe: stdout and stderr of each command are redirected to one
  file under the run's temporary directory and read after the process returns, which is the fix the
  gotcha names, so no surviving descendant can block the read. Observed by AC2.
- **S3** — The bound is on the clock: the command starts in its own process group
  (`start_new_session=True` on POSIX, `CREATE_NEW_PROCESS_GROUP` on win32); on timeout the group is
  killed (`os.killpg` with `SIGKILL` on POSIX, `taskkill /PID <pid> /T /F` on win32), the wait is
  bounded again by five seconds, and the command records exit `timeout`. Observed by AC2.
- **S4** — The worktree teardown never raises: `git worktree remove --force` in the `finally`, then
  `git worktree prune`; when removal fails because a survivor still holds the directory, the result
  names it as `leaked <path>` and the command's record carries it, and the call still returns.
  This supersedes `TOOL-dDeclaredLoop-17` §4's single `remove --force`. Observed by AC3.

## 3. Non-goals (OUT)

- Which bash is found on a node whose PATH carries the WSL launcher first, and the parity row for the
  inline copy: id 28's item in `TOOL-dDeclaredLoop-56`, which adds that row and its plants.
- Output normalisation before hashing: id 27's item in `TOOL-dDeclaredLoop-56`.
- Reaping a survivor the tree kill could not reach: `tools/process-monitor/reap.py` is the kit that
  proves each member died (its header records `taskkill /T` killing one of four MSYS descendants); the
  re-run reports the leak rather than taking a dependency on that kit.
- A lint over `shell=True` and unkilled timeouts in `tools/`, the finding's left-shift: not named by any
  clause of this build; the class is recorded at the close.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-17` — `run_witness_commands` in `tools/loop/loop_witness.py`, whose spawn, bound and teardown this unit replaces
- **hands-off** `TOOL-dDeclaredLoop-56` — the inline `resolve_bash`, which that unit's id 28 item puts under a parity row, and the file-backed run whose output its id 27 item normalises

## 4. Design

### Evidence

- The gotcha's measurement: `out=$(timeout 1 bash -c 'sleep 6 & exit 0')` returned after 6 s, and the
  same command redirected to a file returned in 0 s (`memory/gotchas/bounded-through-a-pipe-is-unbounded.md:39-40`).
- `tools/process-monitor/reap.py:12-13` records that `taskkill /PID <win> /T /F` killed one of four MSYS
  descendants, so the tree kill is best effort on win32 and the file redirect is what bounds the caller.
- `resolve_bash` refuses System32 and WindowsApps paths and accepts a candidate only if it runs
  (`tools/govkit/govkit.py:1144-1197`).

### The run of one command

```python
out = workdir / f"cmd-{i}.out"
with open(out, "wb") as fh:
    p = subprocess.Popen([bash, "-c", command], cwd=wt, stdin=subprocess.DEVNULL,
                         stdout=fh, stderr=subprocess.STDOUT, env=env, **group_kwargs)
    try:
        rc = p.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        run_group_kill(p)                       # killpg / taskkill /T /F
        try: p.wait(timeout=5)
        except subprocess.TimeoutExpired: pass
        rc = "timeout"
digest = sha256(out.read_bytes()).hexdigest()[:12]
```

### Files touched (estimate)

- `tools/loop/loop_witness.py`

### Alternatives rejected

- **`subprocess.run(..., capture_output=True, timeout=...)`.** It reads through pipes, and after the kill
  `communicate` waits for EOF a grandchild holds: the defect itself.
- **`shell=True`.** cmd.exe on win32 cannot run a criterion's bash syntax.

## 5. Production-readiness checklist

- security — no new surface; the commands are the caller's, run in a detached worktree as before.
- perf / scale — one file per command instead of a pipe; no extra spawn on the success path.
- error / empty / loading states — a timeout records `timeout`; a leaked worktree is named, never raised.
- observability — the record's `run` line carries `timeout`, and a leak its path.
- risks — on win32 a survivor may outlive the call; it is named, and the caller is no longer held by it.
- testing — AC1 to AC3 as plants of `loop_witness.py --selftest`; the arm under §7, observed at the close.
- migration — none: no acceptance record exists.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python loop_witness.py --selftest --plant bash-syntax` runs a command
  `true | grep -c x; exit 0` on win32, it records exit `0`.
  Red when: the command runs under cmd.exe, which cannot parse the pipeline and records a non-zero exit.
- **AC2** — When `--plant timeout-grandchild` runs the command `sleep 600 & wait` with a 2 s timeout, the
  call returns within 10 s and records exit `timeout`.
  Red when: output is read through a pipe, so the call waits for the grandchild for the full 600 s.
  figure: the 10 s bound is PINNED, five times the timeout plus the five-second second wait.
- **AC3** — When the same plant finishes, `git worktree list --porcelain` in the fixture names no
  worktree under the run's temporary directory, or the plant's result names the one left as
  `leaked <path>`.
  Red when: the `finally` raises on a held directory, so the call fails instead of returning its record.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_witness.py · covers AC1 AC2 AC3 · the `bash-syntax` and `timeout-grandchild` plants, staged against `TOOL-dDeclaredLoop-17`'s pipe-captured platform-shell run · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 51 (HIGH, item H17).

## 10. Reuse audit

The seams are `resolve_bash` (`tools/govkit/govkit.py:1144`), carried inline as the gotcha
`memory/gotchas/subprocess-resolves-a-different-shell.md` prescribes for copy-installed kits, and the
file-redirect fix of `memory/gotchas/bounded-through-a-pipe-is-unbounded.md`. `python
tools/codebase-map/reuse_lookup.py "run a command with a timeout and kill the process tree"` ranked
`tree`, `run`, `run_arms` and `run_git`, none a bounded tree-killing runner; `tools/process-monitor/reap.py`
kills a tree and proves each death, and is rejected in §3 as a dependency for a best-effort kill.

Recall terms used: timeout pipe grandchild process group killpg taskkill resolve_bash cmd.exe worktree prune

# TOOL-dFurnishedOrders-39 — the roles kit's one bounded runner writes its child's output to files, never a pipe, so a descendant holding stdout cannot outlive the bound, from one canonical block the run-gates kit already proves

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 08e30fef · streams tooling · order 24 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |
| [2026-10-27-build-TOOL-dFurnishedOrders-39-deviation-391.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-39-deviation-391.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |
| [2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`)
confirmed finding **id 27 at HIGH**, report item **H2**. Id 21 reports the same mechanism at MEDIUM
as item M16 and takes `TOOL-dFurnishedOrders-42`, which observes it on the posture read.

`TOOL-dFurnishedOrders-37` S12 makes `run_slot_reader` (`TOOL-dFurnishedOrders-29` S24) the roles
kit's one runner, with the run shape of `tools/roles/handoff.py:268-271`: `subprocess.run` with
`capture_output` and a `timeout`. On a timeout, CPython 3.14.5's `run()` kills the direct child and
then, on Windows, calls `communicate()` with no timeout, which waits until every holder of the pipe
closes it (`Lib/subprocess.py`, the `except TimeoutExpired` branch of `run`, read 2026-10-27). A child
that exits at once while a descendant keeps stdout open waits on the same pipe. So `breakpoints.py
list`, the `turns` read, a git read or the bash kickoff checker that leaves a descendant holding the
pipe holds `derive_attended`, and the dispatch that asked the owner door, with no bound, on this
project's platform. Unit 34 AC2 and unit 37 AC8 stub only a sleeping direct child, so both pass.

The run-gates kit met this defect and closed it: `run_command` (`tools/run-gates/regen.py:270-302`)
writes output to a `tempfile.TemporaryFile`, waits on the direct child with `Popen.wait(timeout)`,
and kills on expiry through `run_tree_kill` (`:249-267`), its comment recording 6.5 s under a 1 s
bound through a pipe. This unit makes that shape one canonical block both kits carry. It repairs
`TOOL-dFurnishedOrders-37` and builds one step after it (order 24).

## 2. Scope (IN)

- **S1** — One canonical block. `tools/lib/run_bounded.py` holds `run_bounded(argv, cwd, bound,
  env=None, merge=False)`, between `# >>> run_bounded_py` and `# <<< run_bounded_py` markers. It
  opens two `tempfile.TemporaryFile` sinks, or one when `merge` sends stderr into stdout; starts the
  child with `subprocess.Popen` and stdin from `DEVNULL`, in a new session on POSIX; waits with
  `wait(timeout=bound)`; on expiry runs `run_tree_kill`'s steps, moved into the block unchanged; then
  reads each sink from its start and decodes it as UTF-8 with `errors="replace"`. It returns
  `(status, out, err)`, status the exit code or `TIMEOUT`, and lets `OSError` from the start reach
  its caller. No `communicate()`, no `subprocess.PIPE` and no `capture_output` appear in the block.
  Observed by AC1 and AC3.
- **S2** — The run-gates kit carries it. `run_command` (`tools/run-gates/regen.py:270`) calls the
  inline copy with `merge=True` and keeps its own `python` resolution, `PWD` pop, `127` answer and
  timing; `run_tree_kill` lives inside the block. Its three callers (`:330`, `:388`, `:399`) see the
  same `(status, output, seconds)` they see at `08e30fef`. Observed by AC3.
- **S3** — The roles kit carries it. `run_slot_reader` (`tools/roles/roles_lib.py`, unit 29 S24, made
  the one runner by unit 37 S12) runs its child through the inline copy, so every roles subprocess,
  the posture read and the checker runs of `handoff.py` included, is bounded by its direct child's
  exit or the bound, whichever comes first. Its answers stay unit 29 S24's: an expired bound renders
  `timed out after <bound>s`. Observed by AC1 and AC2.
- **S4** — The parity row. `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS` gains
  `run_bounded_py|$ROOT/$KIT_REL/run_bounded.py|$KIT_REL/run_bounded`, so a copy that drifts from
  the canonical reds, and a population of copies that empties reds too (`:229`). Observed by AC3.

## 3. Non-goals (OUT)

- Reaping a descendant that outlives a child which exited 0: the call returns on the child's exit,
  and a lingering process is the process-monitor kit's to find. On expiry the block's tree kill is
  best-effort, as `run_tree_kill` documents; the bound does not rest on it, because `taskkill /T`
  walks the Windows tree and misses MSYS parent edges (`tools/process-monitor/reap.py:12-13`).
- The posture read observed under a descendant holding stdout, and a bound a test can lower: the
  minors batch `TOOL-dFurnishedOrders-42`, for ids 21 and 26.
- The card's shell bound: `TOOL-dFurnishedOrders-37` S13 and S14 already write the renderer's output
  to a scratch file (`skills/session-kickoff/manifest-check.sh:405-406`).
- The report's left-shift gates, the bug-class entry and the `capture_output` lint: no clause of this
  build names them; AC1's grep is this kit's instance of the lint.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-29` — `run_slot_reader` and its rendered answers, whose body S3 runs through the canonical block (id 27)
- **consumes-from** `TOOL-dFurnishedOrders-37` — S12's one runner and AC8's stub readers, which S3 bounds against a descendant holding stdout (id 27)
- **hands-off** `TOOL-dFurnishedOrders-42` — the file-backed `run_slot_reader`, whose bound a test lowers and whose posture read unit 42 observes under a descendant holding stdout (ids 26, 21)
- **hands-off** `TOOL-dFurnishedOrders-46` — the `run_bounded_py` block, `run_slot_reader` and the run-gates version move, which unit 46 S1 to S3, S9 to S13, S15 and S17 settle (ids 2, 3, 8, 29, 4, 11, 12, 17, 24, 30 of the fourth audit)

## 4. Design

### The block

```python
# >>> run_bounded_py -- canonical copy: run_bounded.py in gov's lib dir (byte-identical; gated)
def run_tree_kill(proc): ...            # regen.py:249-267, moved unchanged
def run_bounded(argv, cwd, bound, env=None, merge=False):
    with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        proc = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.DEVNULL, stdout=out,
                                stderr=subprocess.STDOUT if merge else err, env=env,
                                **({} if os.name == "nt" else {"start_new_session": True}))
        try:
            status = proc.wait(timeout=bound)
        except subprocess.TimeoutExpired:
            run_tree_kill(proc)
            status = "TIMEOUT"
        out.seek(0); err.seek(0)
        return (status, out.read().decode("utf-8", "replace"),
                err.read().decode("utf-8", "replace"))
# <<< run_bounded_py
```

### Why a file bounds what a pipe cannot

`wait()` returns when the direct child exits; it does not read. A pipe is drained by a reader that
blocks until every writer closes, and a descendant is a writer. A file has no reader to block: the
parent reads what was written once the child is gone. On Windows, `TemporaryFile` opens with
delete-on-close, so a descendant still holding the handle delays the file's deletion, never the
call.

### Inventory

Minted: `tools/lib/run_bounded.py`, the function `run_bounded`, the marker stem `run_bounded_py` and
its `PARITY_ROWS` row. `run_tree_kill` keeps its name and moves into the block.

### Migration

None: no stored data, and every caller's return shape is unchanged.

### Rollout

Live at landing, at order 24. `KIT_ROLES_VERSION` and the run-gates kit's version move for the kit
epoch leg.

### Files touched (estimate)

- `tools/lib/run_bounded.py`
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/regen.py`
- `tools/roles/roles_lib.py`
- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **A second copy of `regen.py`'s shape in `roles_lib.py`.** The charter's reuse rule extracts at a
  kind's second instance, and two ungated copies of a bound drift the way the pipe shape did.
- **Keep the pipe and add a tree kill.** `taskkill /T` killed one of four in the measured MSYS tree
  (`tools/process-monitor/reap.py:12-13`), and a child that exits 0 with a lingering descendant is
  never killed at all.
- **Import `regen.py` from the roles kit.** `<prefix>/lib/` and a sibling kit's module travel to no
  copy-installed adopter, which is why the inline-parity table exists.

## 5. Production-readiness checklist

- security — no new write path beyond two anonymous temp files per call, deleted on close; stdin
  stays `DEVNULL`.
- perf / scale — the call returns at the direct child's exit, or at the bound plus the kill grace of
  `run_tree_kill`.
- error / empty / loading states — a start failure is `OSError` to the caller, as both callers
  handle it today; an expired bound is `TIMEOUT`.
- observability — unchanged answers: regen's `TIMEOUT` verdict line, the roles slot's `timed out`.
- risks — a descendant that outlives a child's exit keeps running; AC2 leaves one alive for its own
  sleep length.
- testing — AC1 to AC3 by probes and stub children; the arms of §7 at the close.
- migration — none.
- user docs — none: no user-facing step changes.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -E "capture_output|stdout=subprocess\.PIPE|\.communicate\(" --
  'tools/roles/*.py'` runs, and the same pattern over the canonical run_bounded.py S1 creates in
  gov's lib dir, each prints nothing.
  Red when: any roles subprocess still reads its output through a pipe a descendant can hold.
  figure: it prints six lines at `08e30fef` (PINNED, measured 2026-10-27): `handoff.py:250`, `:270`,
  `:349` and `:994`, `check_roles.py:426` and `render_agents.py:113`, which unit 37 S26 routes through
  `run_slot_reader`; so it is red before units 37 and 39 are built.
- **AC2** — When `python -c` calls `roles_lib.run_slot_reader` with `bound=2` on a stub that starts
  `python -c "import time; time.sleep(30)"` with its stdout inherited, prints `x` and exits 0, the
  call returns in under 20 seconds with the stub's `x`; on a stub that starts the same sleeper and
  then sleeps 30 seconds itself, it returns in under 20 seconds with the `timed out` answer.
  Red when: the call waits for the sleeper, so a descendant holding stdout holds the owner door.
  fixture: two stub scripts under `%TEMP%`, built by the pass.
  figure: the 20-second verdict is RELATIVE to the 30-second sleeper, the form
  `skills/session-kickoff/manifest-check.test.sh:1741-1751` records for a loaded node; PINNED.
- **AC3** — When `bash -c` extracts the `run_bounded_py` block, by the `blk` awk of
  `tools/lib/resolve-python.test.sh:221`, from the canonical run_bounded.py S1 creates,
  `tools/run-gates/regen.py` and `tools/roles/roles_lib.py`, the three blocks compare equal with CRs
  dropped; and `python -c` calling `regen.run_command` on `bash -c "sleep 6 & echo y"` with bound 1
  returns in under 4 seconds.
  Red when: one copy drifts, or regen's own bound regresses to the pipe's 6.5 seconds.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `roles catalogue` · `roles adopter self-test` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` · `run-gates run-log line` · `pre-push run-log line` · `measure-legs selftest` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC2 · a stub that leaves a sleeper holding stdout and exits, and one that sleeps past the bound beside it, staged by restoring `capture_output` in the block · none
New arm: tools/lib/resolve-python.test.sh · covers AC3 · the `run_bounded_py` parity row over three copies, staged by editing one copy's decode line · none

## 8. Open questions

- **F1 — Where does the file-backed runner live?** Options: (a) a canonical block in `tools/lib/`,
  inlined byte-identical into `regen.py` and `roles_lib.py` under a `PARITY_ROWS` row; (b) a second
  copy in `roles_lib.py` with no parity; (c) the roles kit importing `regen.py`. (b) is the copy the
  charter's reuse rule forbids at a second instance; (c) reaches a sibling kit no copy-install
  carries. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the charter's `[reuse]` rule and
  the seam M5 found. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one repairs are unbuilt.** `TOOL-dFurnishedOrders-29` and `-37` are specced
  and unbuilt at `08e30fef`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on
  each at the pass and stops this unit if `run_slot_reader` is still absent then, rung 1, the
  brief's rule for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-2 promotions, id 27
  (HIGH, item H2, related to id 21 at MEDIUM).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-46, promoted from the spec audit of the round-3 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seam extended: `run_command` and `run_tree_kill` (`tools/run-gates/regen.py:249-302`), the one
file-backed bounded runner in the tree, made a canonical block under the inline-parity table
(`tools/lib/resolve-python.test.sh:168-187`, extracted by `blk` at `:221`), whose eighteen rows
already carry such blocks.
`python tools/codebase-map/reuse_lookup.py "run a subprocess under a wall-clock bound when a
grandchild holds its stdout"` ranked `run` (a SEAM, fan-in 102, a name-token count over many
suites), `run_git`, `run_arms` and `boundedParallel`, none a file-backed runner; and `git grep -n
"TemporaryFile" -- 'tools/*.py'` names `regen.py:289` alone, so no other seam fits. The recall probe returned the audit's H2 text and
TOOL-cMendedVintage-12, the same class closed in a shell reader by a scratch file, neither
disagreeing with source; the report's claim that `manifest-check.sh` writes to a scratch file holds
at `:405-406`.

Recall terms used: `python tools/memory-recall/query.py "how is a subprocess bounded when a
grandchild holds its stdout pipe on Windows" --terms "bounded runner pipe grandchild stdout timeout
communicate TemporaryFile run_slot_reader regen run_tree_kill"`

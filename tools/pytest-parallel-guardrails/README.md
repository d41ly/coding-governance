# pytest-parallel-guardrails — bounded, attributable parallel test runs

<!-- gov:kit pytest-parallel-guardrails@1.0 -->

Any pytest-xdist suite can wedge forever when a worker dies, and the death leaves no evidence:
execnet redirects a worker's fd 0/1 to devnull on every platform — on Windows fd 2 as well — so
the diagnostics that would explain the death are discarded microseconds before it. This kit makes
parallel runs **bounded** (a wedge becomes a fast, named failure), **attributable** (a dead worker
records its victim test and death mode), and **resilient** against one fully-diagnosed kill class
(an async driver's worker thread dying on a post to a closed per-test event loop).

Provenance: diagnosed and proven on a real 4300-test suite (2026-07-16) — a parallel run that hung
three-for-three under load completed clean twice in a row once the seam fix landed. Upstream
records: inCMS `ARCH-eGuidingConcierge-12/-19`, `ARCH-eVigilantCanary-1/-2`.

## What's in the kit

| File | What it is |
|---|---|
| `pyproject-snippet.toml` | The four-knob ini recipe — merge into `[tool.pytest.ini_options]` |
| `crashprobe.py` | Worker-death attribution plugin — arm while hunting, then remove |
| `aiosqlite-seam-conftest.py` | Conftest patch: aiosqlite worker survives closed-loop posts |
| `aiosqlite_worker_resilience.test-template.py` | Forced-race regression gate (rename to `test_*.py` when copying) |
| `pytest-parallel-guardrails.test.sh` | Kit self-test (rides the repo gate suite) |

## The four knobs (what each honestly does)

Merge `pyproject-snippet.toml` into your ini. **Size `timeout` first**: run `--durations=10`,
take the slowest legitimate test, multiply by ~7–10. The shipped 300/240/1800 fit a suite whose
slowest test is ~40 s.

- `timeout` + `timeout_method = "thread"` — the per-test bound, and the ONLY hang bound here. On
  Windows (no SIGALRM) and under the `thread` method everywhere, expiry ends the worker PROCESS
  via `os._exit(1)`; xdist reports `worker 'gwN' crashed while running '<test>'`. Accepted: a
  bounded, attributed kill beats an unbounded wedge.
- `--max-worker-restart=0` — the distribution-deadlock breaker. Without it, xdist respawns the
  dead worker and the controller<->worker IPC can enter a mutual wait it never leaves (observed:
  an hour at 0 CPU across 14 processes). Trade-off: no auto-retry on a transient worker death.
- `session_timeout` — a between-tests budget ONLY, **not a hang bound of any kind**: pytest-timeout
  compares it only after a test's runtest protocol completes, which a wedged test never does. It
  turns a slow-but-completing run red; nothing more.
- `faulthandler_timeout` — below `timeout`, so every hang dumps all thread stacks BEFORE the kill,
  via pytest's saved stderr dup (survives the worker fd redirection). The victim names itself.

## The diagnosis playbook (when a worker still dies and you don't know why)

1. Arm the probe: `PYTHONPATH=<this dir> pytest -p crashprobe ...` (or add this dir to your
   `pythonpath` ini, or `python -m pytest -p crashprobe` with the file in cwd — a bare
   `pytest -p crashprobe` with the file only in the rootdir does NOT import). Set
   `CRASHPROBE_DIR` somewhere convenient.
2. Loop the suite until the death recurs; `--max-worker-restart=0` names the victim test in the
   controller output.
3. Read `probe-<gwN>.log` for that worker:
   - an `os._exit` block = **your per-test timeout fired on a hung test** — the victim is usually
     innocent; the culprit is whatever poisoned shared state earlier on that worker;
   - a bare faulthandler C-traceback = **a native crash** (C extension segfault/abort);
   - neither, log just stops = the process was killed from outside (OOM killer, CI reaper) — check
     the RSS column trend first.
4. Know the evidence traps: Windows Event Viewer/WER shows nothing if WER is disabled (check
   `HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting : Disabled`); `os._exit` is not a
   fault, so WER never records it anywhere; absence of a `Fatal Python error` banner in a captured
   stream that goes to devnull proves nothing.
5. Remove the probe when done — it is a hunt tool, not a fixture.

## The aiosqlite closed-loop seam (one diagnosed kill class, fixed)

If your suite pairs pytest-asyncio function-scoped loops with aiosqlite (directly or via
SQLAlchemy), an op still in flight at loop close makes aiosqlite's worker thread double-post
`call_soon_threadsafe` onto the closed loop; the second `RuntimeError` escapes and the worker
thread DIES with the connection object live. Every later op on it — including `close()` — awaits
a future nobody resolves. Loop-side drains cannot win this race (the worker is not a task and can
post after `loop.close()`); unfixed upstream as of aiosqlite 0.22.1.

Adopt: copy the block in `aiosqlite-seam-conftest.py` into your `tests/conftest.py` (module
level), copy the test template beside it renamed `test_aiosqlite_worker_resilience.py`, and fix
its one marked import. The test forces the race deterministically — it is the gate that re-proves
the patch on every aiosqlite bump. Related hardening for the same stack (documented upstream, not
shipped here): SQLAlchemy's own docs mandate `poolclass=NullPool` for an engine shared across
event loops, and `asyncio_default_test_loop_scope = "session"` (pytest-asyncio ≥0.26) removes the
multi-loop pattern entirely at the cost of a suite-wide loop-semantics migration.

## Version

Kit version: `KIT_PYTEST_GUARDRAILS_VERSION = "1.0"` in `crashprobe.py`; the same version rides
the `gov:kit pytest-parallel-guardrails@1.0` markers in the artifacts adopters keep (this README,
the snippet, the seam patch, the test template), because the probe itself is expected to be
removed after a hunt.

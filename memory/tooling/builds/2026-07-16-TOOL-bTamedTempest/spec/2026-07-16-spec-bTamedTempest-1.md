# TOOL-bTamedTempest-1 — pytest-parallel-guardrails kit: bounded, attributable parallel test runs

**Status:** INPROGRESS · rev-2 · 2026-07-16 · node b · Tier-2 · base 770a1aa3 · review wf_d878c8a9-bb3

## 1. Goal

Any pytest-xdist suite can wedge forever when a worker dies: the controller and every surviving
worker enter a mutual wait, and the death itself leaves no evidence because the worker's stdout and
stderr file descriptors are redirected to devnull (on Windows, both). A per-test timeout cannot see
the deadlock, and the timeout itself KILLS the worker on Windows, so the guard and the mystery are
the same event. Ship a copy-in kit that makes any adopter's parallel runs bounded (a wedge becomes a
fast, named failure), attributable (a dead worker records its victim test and death mode), and
resilient against one fully-diagnosed kill class (an async DB driver's worker thread dying when it
posts a result to a closed per-test event loop).

The recipe (S2), the seam snippet (S4), and the forced-race gate (S5) were proven on a real
4300-test suite on 2026-07-16 — a run that hung three-for-three under load completed clean twice
in a row once the seam fix landed — and their source files are live in inCMS (upstream records:
ARCH-eGuidingConcierge-12/-19, ARCH-eVigilantCanary-1/-2). The probe (S3) is a RECONSTRUCTION of
the session diagnostic whose technique and captured output are recorded in ARCH-eVigilantCanary-1;
the original scratch file no longer exists on disk, so S3's fidelity gate is its own self-test plus
the record, not a byte-for-byte source.

## 2. Scope (IN)

- S1 — new kit directory `tools/pytest-parallel-guardrails/` with a `README.md` carrying the
  four-knob recipe rationale and the worker-death diagnosis playbook.
- S2 — `pyproject-snippet.toml`: the `[tool.pytest.ini_options]` recipe (`timeout`,
  `timeout_method`, `session_timeout`, `addopts = "--max-worker-restart=0"`,
  `faulthandler_timeout`) with generic, mechanically-honest comments.
- S3 — `crashprobe.py`: a stdlib-only pytest plugin that patches `os._exit` to record the victim
  test and all thread stacks before a timeout kill, arms `faulthandler` on a per-worker log file
  so a native crash is captured too, and logs per-test start/end with elapsed time and RSS. Works
  on Windows and POSIX. Loading (all verified forms): `PYTHONPATH=<kitdir> pytest -p crashprobe`,
  or a `pythonpath` ini entry plus `-p crashprobe`, or `python -m pytest -p crashprobe` from the
  directory holding the file — a bare `pytest -p crashprobe` with the file merely in the rootdir
  does NOT import (the console script does not put the rootdir on `sys.path`).
- S4 — `aiosqlite-seam-conftest.py`: a copy-in conftest snippet installing a protocol-identical
  `_connection_worker_thread` whose closed-loop posts are dropped instead of lethal.
- S5 — `aiosqlite_worker_resilience.test-template.py`: the deterministic forced-race regression
  gate an adopter copies beside the snippet (no timing lottery; also pins the patch is installed).
  Deliberately NOT named `test_*.py`: pytest's default `python_files` glob is fnmatch-based (`*`
  spans dots), so a `test_*.template.py` inside a vendored kit dir would be COLLECTED by a bare
  pytest crawl and error; the adopter renames to `test_*.py` when copying into their suite.
- S6 — kit plumbing: `pytest-parallel-guardrails.test.sh` self-test, a
  `KIT_PYTEST_GUARDRAILS_VERSION` constant in `crashprobe.py` PLUS
  `gov:kit pytest-parallel-guardrails@X.Y` doc-markers in the artifacts adopters KEEP (the
  pyproject snippet, the seam snippet, the test template) per the aKitHardener convention —
  crashprobe.py is a hunt-then-remove diagnostic, so it cannot be the only version home;
  registration in `tools/check-kit-versions.sh` (constant present AND constant/marker pair
  agrees), a self-test leg in `tools/run-gates.sh`, one-line kit listings in `AGENTS.md` and
  `README.md`, AND the new self-test path added to AGENTS.md's gate-suite "kit self-tests"
  enumeration (two AGENTS.md lists, not one).
- S7 — `parallel-coding-governance.domain-rules.md`: two new §10 recurring-bug-class entries
  (parallel-runner IPC deadlock after a worker crash; thread-posts-to-closed-loop) and one §11
  line (worker fd redirection + disabled-WER evidence caveats).

## 3. Non-goals (OUT)

- Not a published pytest plugin package — cg kits are copy-in by design, like every other kit here.
- No auto-adoption or wiring script; the README's adoption steps are the contract (matching
  `memory-tree/` before its adopt script existed).
- Not porting the upstream project's stack-specific choices (its event-drain fixture, its NullPool
  decision) — the README states the pattern and points at the SQLAlchemy docs instead.
- Not upstreaming the aiosqlite fix to omnilib/aiosqlite — encouraged in the README, out of scope.
- No change to `parallel-coding-governance.template.md` itself (the 32 KiB budget stays untouched;
  everything lands in the domain-rules companion and the kit).

## 4. Design

### Inventory

| File | Role |
|---|---|
| `tools/pytest-parallel-guardrails/README.md` | Recipe rationale · diagnosis playbook · adoption steps |
| `tools/pytest-parallel-guardrails/pyproject-snippet.toml` | The four-knob ini block, copy-in |
| `tools/pytest-parallel-guardrails/crashprobe.py` | Attribution probe plugin; carries the kit version constant |
| `tools/pytest-parallel-guardrails/aiosqlite-seam-conftest.py` | Resilient worker snippet, copy-in |
| `tools/pytest-parallel-guardrails/aiosqlite_worker_resilience.test-template.py` | Forced-race regression gate, copy-in (adopter renames to `test_*.py`) |
| `tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh` | Kit self-test (static) |
| `tools/check-kit-versions.sh` | +1 `need` line for the new constant |
| `tools/run-gates.sh` | +1 leg: the kit self-test |
| `AGENTS.md`, `README.md` | +1 kit-list line each |
| `parallel-coding-governance.domain-rules.md` | §10 +2 entries, §11 +1 entry |

### The four knobs (and what each honestly does)

- `timeout` + `timeout_method = "thread"` — the per-test bound. On any platform without `SIGALRM`
  (Windows always; the `thread` method everywhere) expiry ends the PROCESS via `os._exit(1)`,
  which xdist reports as `worker 'gwN' crashed while running '<test>'`. The kill is accepted; the
  point is it must be bounded, attributed, and never able to wedge the run.
- `addopts = "--max-worker-restart=0"` — the actual deadlock breaker. A dead worker fails the run
  fast instead of respawning into an IPC state the controller may never recover (observed: an
  hour at 0 CPU across 14 processes). Trade-off stated in the snippet: it also disables xdist's
  retry, so a transient worker death reds the run with no auto-retry.
- `session_timeout` — a between-tests budget ONLY, and NOT a hang bound of any kind.
  pytest-timeout arms no timer for it; expiry is compared only AFTER a test's
  `pytest_runtest_protocol` completes. A wedged test never reaches that comparison, so
  `session_timeout` cannot fire mid-hang OR mid-distribution-deadlock — all it does is turn a
  slow-but-COMPLETING run red at the budget. The per-test `timeout` is the only hang bound in
  the recipe; the snippet's comment says exactly this so adopters cannot mistake it for hang
  coverage.
- `faulthandler_timeout` — set BELOW `timeout` so every hang dumps all thread stacks through
  pytest's saved stderr dup (a channel that survives the worker fd redirection) before the kill.
  The victim test names itself instead of vanishing.
- Sizing note in the snippet: measure the suite's slowest legitimate test and size `timeout` to
  roughly 7–10× it; the shipped values (300/240/1800) fit a suite whose slowest test is ~40 s.

### crashprobe.py contract

- Load via one of the three verified invocations in S2 (`PYTHONPATH` env · `pythonpath` ini ·
  `python -m pytest`); a bare `pytest -p crashprobe` with the file only in the rootdir fails to
  import. Output directory: `$CRASHPROBE_DIR`, else the current directory; one
  `probe-<workerid>.log` per xdist worker (`master` when not distributed), line-buffered so a
  hard kill cannot lose the last lines.
- Arms `faulthandler.enable(file=<log>, all_threads=True)` in `pytest_configure` with
  `@pytest.hookimpl(trylast=True)` — NOT at import: pytest's builtin faulthandler plugin calls
  `enable(file=dup(stderr))` at configure time and `enable` is process-global last-wins, so an
  import-time arm would be silently superseded. Re-arming last, a native crash (segfault/abort)
  writes its C-level traceback into the per-worker log even where the worker's fd 2 is devnull
  (Windows; on POSIX workers fd 2 is untouched and the log capture is belt-and-suspenders).
  `faulthandler_timeout` is unaffected: `dump_traceback_later` takes its own file handle per
  call, independent of `enable`.
- Patches `os._exit` to first write the current test id, elapsed time, the caller's Python stack,
  and all thread stacks, then `fsync`, then call the real exit. A pytest-timeout thread-method
  kill is therefore recorded with its victim, distinguishable from a native crash (which
  faulthandler records instead) — the two death modes cannot be confused.
- `pytest_runtest_logstart/logfinish` hooks log every test with elapsed seconds and RSS
  (Windows: `GetProcessMemoryInfo` via ctypes; POSIX: `resource.getrusage` `ru_maxrss`, documented
  as a peak-not-current value). Stdlib only; no third-party imports.
- Diagnostic tool, not a permanent fixture: adopters arm it while hunting a crash, then remove it.
- Carries `KIT_PYTEST_GUARDRAILS_VERSION = "1.0"` (the kit-side greppable constant). Because the
  probe is removable, the DEPLOYER-side version signal lives as
  `gov:kit pytest-parallel-guardrails@1.0` markers in the three artifacts adopters keep (S6);
  `check-kit-versions.sh` asserts the constant and every marker agree, memory-tree-pair style.

### The aiosqlite seam snippet

- Replaces `aiosqlite.core._connection_worker_thread` at conftest import with a copy whose two
  `future.get_loop().call_soon_threadsafe(...)` posts guard `RuntimeError`: an undeliverable
  result (its awaiter's loop is closed, so it can never be woken) is dropped and the worker
  SURVIVES. Upstream 0.22.1 dies on the double-post and orphans the connection — every later op,
  including `close()`, then awaits a future nobody resolves.
- Preserves the 0.22.x queue protocol exactly: `(future | None, function)` tuples and
  `_STOP_RUNNING_SENTINEL`, sentinel honored even when its own post is undeliverable.
- Emits a one-time `warnings.warn` (never a failure) when the installed aiosqlite version is
  outside the tested `0.22.x` range, so an adopter on a future release re-verifies rather than
  trusting silently.
- The paired test template forces the exact race event-based (a worker blocked inside an op while
  the test closes the awaiting loop), asserts survival + continued usability + clean close, and
  pins the patch is installed. One import line is adopter-edited (their conftest path).

### Alternatives rejected

- A proper pytest plugin distribution: wrong shape for this repo; kits are vendored files.
- Shipping `asyncio_default_test_loop_scope = session` as the default recipe: structurally also
  kills the closed-loop class, but flips loop semantics for an entire suite — a per-adopter
  migration, documented in the README as the long-term simplification, not imposed.

## 5. Production-readiness checklist

- security — no network, no secrets, no exec; the probe writes plain-text logs to an
  adopter-chosen directory.
- perf / scale — probe overhead is two buffered writes per test; snippet overhead is two
  try/except frames per DB op; both negligible.
- a11y — N/A (developer tooling, no UI).
- i18n — N/A.
- error / empty / loading states — the self-test `py_compile`s every shipped `.py` AND
  import-executes `crashprobe.py` under a bare stdlib interpreter (with `CRASHPROBE_DIR` pointed
  at a temp dir), so a syntax regression in any file — and an import/side-effect regression in
  the probe on the gate's platform — cannot ship. Honest limits: the seam snippet is
  compile-checked only (importing it needs aiosqlite), and the probe's OTHER platform's branch is
  compile-checked only.
- observability — this kit IS the observability; its own failure mode (probe dir not writable)
  raises at import, visibly.
- risks — adopters cargo-culting 300 s onto a slower suite (mitigated: the sizing rule sits
  directly above the values in the snippet); aiosqlite protocol drift in a future release
  (mitigated: version advisory + the forced-race gate the adopter runs in THEIR env).
- testing + left-shift gates — kit self-test rides `run-gates.sh`; the adopter-side forced-race
  test is shipped as a template, not prose.
- migration / rollback — none; rollback = delete the kit dir and the two registration lines.
- user docs — the kit README is the user doc; AGENTS.md/README.md list the kit; WIRE-INTO-PROJECT
  gains one optional-step line (see §8 Q2).

## 6. Acceptance criteria

- AC1 — When `bash tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh` runs on a
  machine with only a stdlib Python, it exits 0, having verified: file inventory; `py_compile` of
  every shipped `.py`; an import-execution of `crashprobe.py` (bare stdlib, `CRASHPROBE_DIR` set
  to a temp dir, probe log actually created); the version constant; every `gov:kit` marker
  agreeing with the constant; the four knobs present in the snippet; and
  `faulthandler_timeout < timeout` compared numerically AFTER stripping `\r` (CRLF-checkout
  safe, check-template-size.sh precedent).
- AC2 — When `bash tools/run-gates.sh` runs, every pre-existing leg still passes and a new
  `pytest-guardrails self-test` leg appears and passes.
- AC3 — When `bash tools/check-kit-versions.sh` runs, it verifies `KIT_PYTEST_GUARDRAILS_VERSION`
  in `crashprobe.py` AND that every `gov:kit pytest-parallel-guardrails@` marker in the kept
  artifacts carries the same version; it fails on a missing/malformed constant or a drifted pair.
- AC4 — When a reader opens `AGENTS.md` or `README.md`, the kit list names
  `pytest-parallel-guardrails/` with a one-line purpose, and AGENTS.md's gate-suite
  "kit self-tests" enumeration includes `tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh`.
- AC5 — When a Tier-2 reviewer primes with domain-rules §10, the two new classes are present; §11
  carries the fd-redirection/WER-evidence line.
- AC6 — When the spec flips to CLOSED, `memory/tooling/DECISIONS.md` carries the
  TOOL-bTamedTempest-1 line, the ledger row is current, and memory hygiene (check 12 included)
  passes on the build folder.

## 7. Gates

- `bash tools/run-gates.sh` — all 13 existing legs, plus the new kit self-test leg (AC2).
- `tools/check-kit-versions.sh` extended (AC3) — rides run-gates.
- Memory hygiene incl. spec-format check 12 on this spec (AC6) — rides run-gates.

## 8. Open questions

- Q1 — aiosqlite version guard in the seam snippet: fail-closed or warn?
  Options: (a) raise at import outside `0.22.x` — safest but breaks adopter suites on any future
  patch release; (b) `warnings.warn` once and proceed — visible, never breaks a green suite whose
  own forced-race gate still passes. Recommendation: (b); the adopter-run gate is the real check.
  RESOLVED (owner-delegated flow, 2026-07-16): (b) warn.
- Q2 — mention the kit in `WIRE-INTO-PROJECT.md` now, or on first external adoption?
  Options: (a) one optional-step line now — runbook stays complete; (b) defer — runbook only
  documents the mandatory chain. Recommendation: (a); one line, no ordering impact.
  RESOLVED (owner-delegated flow, 2026-07-16): (a) one optional-step line now.

## 9. Revision log

- rev-1 · 2026-07-16 · initial draft.
- rev-2 · 2026-07-16 · folded review wf_d878c8a9-bb3 (11 confirmed / 4 refuted): session_timeout
  is not a hang bound of any kind; probe arms faulthandler in `pytest_configure(trylast)` (builtin
  plugin last-wins); verified loading invocations; version constant + `gov:kit` kept-artifact
  markers pair; test template renamed off the `test_*.py` glob; self-test import-executes the
  probe + strips `\r`; AGENTS.md gate-suite enumeration in scope; S3 provenance honesty; fd 2
  qualifier. §8 Q1→warn, Q2→WIRE line now (owner-delegated). Review record `reviews/`.

# TOOL-aMendedFleet-4 — the govkit acceptance matrix reads its children as UTF-8 on every host

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The `govkit acceptance matrix` leg is red on every remote CI push run, because `tools/govkit/matrix.py`
decodes its children's output with the locale codec. On the `windows-latest` runner that is cp1252,
while node a exports `PYTHONUTF8=1` and stays green. This unit makes the matrix host-independent, so
the push bar's first of three red legs goes green. Report `[A#1]`, brief unit 4.

## 2. Scope (IN)

- **S1** — `tools/govkit/matrix.py` sets `PYTHONIOENCODING=utf-8` in its own `os.environ` before
  `ROLE_ENV` is built, so every child it spawns, and every python grandchild a bash leg spawns,
  writes UTF-8 to its pipe whatever the host's code page. Observed by AC1.
- **S2** — Every `subprocess.run` capture in `tools/govkit/matrix.py` that today passes `text=True`
  passes `encoding="utf-8", errors="replace"` instead. These are four sites: the `git` and `run`
  helpers, `run_in_gov`, and shape 5's leg runner. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The other 38 files under `tools/` that capture with `text=True`: 261 sites across 39 files,
  `matrix.py`'s four included, PINNED 2026-10-04 from `git grep -c 'text=True' -- 'tools/*.py'`.
  Whether any of them reds the daily held job is `TOOL-aMendedFleet-7`'s census to find, per root
  cause; this unit fixes the leg the push bar reds.
- Making govkit itself reconfigure its stdout. The gotcha
  `memory/gotchas/fixture-inherits-ambient-machine-state.md` records that it prints an em dash in the
  ANSI code page outside UTF-8 mode; `tools/govkit/selftest.py` already grades that path with
  `PYTHONUTF8=0`. The matrix is a harness and declares its locale, as that gotcha asks a fixture to.
- Setting `PYTHONUTF8` in `.github/workflows/remote-ci.yml`. It would green the runner and leave the
  matrix red on any other Windows host outside UTF-8 mode.
- The other two push-bar reds: `TOOL-aMendedFleet-5` and `TOOL-aMendedFleet-6`.

### Edges

none

## 4. Design

### Evidence

Re-verified 2026-10-04, against the report's claim at `ac65de998`:

- Remote CI push run `37220352485` (main at `35438ba0a`, `windows-latest`, Python 3.12.10) reds
  `govkit acceptance matrix` with `govkit-matrix: 3 FAILED`, naming shape 5's arms for the legs
  `micro-format definitions`, `micro-format gate selftest` and `line length`, and one reader thread
  dies with `UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f` in `cp1252.py`.
- Those three legs are bash scripts that write their own UTF-8 literals. The matrix decodes them as
  cp1252, so `SCRATCH_EXPECT`'s `—` never matches, and an `0x8f` continuation byte kills the reader
  thread, leaving that stream `None`. The `playbook render` legs pass there because their python
  writes cp1252 into the pipe and the matrix decodes cp1252 back.
- So the report's remedy, decode UTF-8 explicitly, is half the fix: alone it would break the arms
  that pass today, whose python children write the locale codec. Forcing the children to UTF-8 is
  the other half. Probe, node a, 2026-10-04, under `PYTHONUTF8=0` (locale cp1251 here): a python
  child printing `—` writes `b'\x97'`, and with `PYTHONIOENCODING=utf-8` in its environment writes
  `b'\xe2\x80\x94'`; a locale-decoded capture of UTF-8 bytes does not contain `—`, a UTF-8 one does.
- The matrix leg's last recorded wall on node a is 378.819 s (`<git-common-dir>/gate-ledger.tsv`,
  PINNED from that row).

### Why `errors="replace"`

A strict decode on a reader thread does not raise in the caller: the thread dies and the stream
comes back `None`, which the arms then read as "printed no verdict". With `replace`, a stray byte
becomes U+FFFD and every arm still grades the text it was given.

### Files touched (estimate)

- `tools/govkit/matrix.py`

### Alternatives rejected

- **Decode UTF-8 at shape 5's runner only.** Its python children write the locale codec, so the
  `playbook render` arms would turn red where they are green today.
- **`python -X utf8` in the leg's argv in `tools/gate-legs.json`.** It fixes this repo's bar and
  leaves an adopter's copy of the leg on the old argv; the harness should declare its own locale.

## 5. Production-readiness checklist

- security — N/A: a test harness's decoding, no write path.
- perf / scale — no change; the same children run.
- error / empty / loading states — `errors="replace"` keeps a stray byte from turning a stream into
  `None`.
- observability — unchanged: the matrix still prints every failing arm with its captured text.
- risks — an arm that relied on locale-codec output would now see UTF-8; AC1 runs every arm.
- testing — AC1 is the matrix itself on a non-UTF-8 code page, observed RED on the base file first.
- migration — none.
- user docs — N/A: no operator-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `PYTHONUTF8=0 python tools/govkit/matrix.py` runs on node a, its last line is
  `govkit-matrix: all arms held`.
  Red when: run against the base file, the same command prints `FAILED` naming shape 5's arms for
  `micro-format definitions`, `micro-format gate selftest` and `line length`: the CI failure
  reproduced on a cp1251 host. The build pass observes that red before the edit.
  cost: about 378 s, the leg's last recorded wall.
  fixture: needs a host whose code page is not UTF-8 with UTF-8 mode off; node a's is cp1251, read
  with `PYTHONUTF8=0 python -c "import locale; print(locale.getpreferredencoding(False))"`.
- **AC2** — When `grep -c 'text=True' tools/govkit/matrix.py` runs, it prints `0`, and
  `grep -c 'encoding="utf-8", errors="replace"' tools/govkit/matrix.py` prints at least `4`.
  Red when: any capture still decodes with the locale codec.
- **AC3** — When the first remote CI push run after this build lands completes,
  `gh run view <id> --repo d41ly/coding-governance --log-failed` does not name `govkit acceptance matrix`.
  Red when: the leg still fails on `windows-latest`.
  permission: observable only after the landing push, which the close performs.

## 7. Gates

`govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; the report's remedy re-verified against CI run `37220352485`
  and widened to force the children's encoding.

## 10. Reuse audit

No existing seam fits: the fix is two kwargs and one environment line inside `tools/govkit/matrix.py`,
and the precedent is the gotcha `memory/gotchas/fixture-inherits-ambient-machine-state.md` with
`tools/govkit/selftest.py`'s `PYTHONUTF8=0` arm, which declare a harness's locale rather than
inheriting it. `python tools/codebase-map/reuse_lookup.py "decode a child process output as utf-8
regardless of the host code page"` ranked affordance-seam prose neighbours only (`run_bounded`,
`runlog_lib.parse_line`, `backlog.extract_row`), none of which spawns a child for this harness; no
shared capture helper exists to route the four sites through. `python tools/memory-recall/query.py`
returned `TOOL-dSettledRoster-3`, an earlier red of the same leg whose corrected root cause was a
different one (an interpreter-floor probe), and nothing on its codec.

Recall terms used: govkit acceptance matrix cp1252 locale codec utf-8 subprocess decode remote-ci windows-latest PYTHONUTF8

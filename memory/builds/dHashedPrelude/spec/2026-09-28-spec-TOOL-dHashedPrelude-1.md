# TOOL-dHashedPrelude-1 — the live-log baseline is captured above the first decorated arm

**Status:** SPECCED · rev-1 · 2026-09-28 · node d · Tier-2 · base 3cf05f29 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the memory-recall selftest's live-query-log guard able to fail. Its `before` digest is taken
inside `main()`, after every arm has already run, so the row it feeds brackets nothing and reports
ok whatever the arms did to the log.

## 2. Scope (IN)

- **S1** — The live-log path and its `before` digest are assigned at MODULE scope, textually above
  the first decorated arm and below `cleanup()`, which is the earliest point where
  `git_common_dir()` and `recall_conf` are both defined. Observed by AC1.
- **S2** — `main()` compares against those module-scope values instead of computing its own. The
  three outcomes it can report are unchanged: a matching digest is ok, a differing one is FAIL, and
  an unreachable repository yields the `(absent)` sentinel on both ends. Observed by AC2.
- **S3** — The assignment carries a comment stating what the guard does NOT check: that it is a
  whole-file digest and cannot tell an arm's write from another process's, that it covers one path
  and says nothing about the cache directory beside it, and that a log absent at both ends is
  indistinguishable from a protected one. Observed by AC3.
- **S4** — Nothing else in the file moves. The arms, their order, the arity assertion, the pin and
  the run-property rows appended after it are untouched, and `SELFTEST_ARMS` does not change,
  because no arm is added here. Observed by AC4.

## 3. Non-goals (OUT)

No permanent arm that writes to the real query log: the break that proves this works is staged into
the working tree, observed, and reverted. No change to `query.py`, `extract.py` or any arm's
behaviour. No second guard over the cache directory — the comment names that gap, it does not close
it. No change to how `repo_root()` resolves, which is the mechanism that makes an in-process arm
reach the real repository and is correct as it stands.

### Edges

- **hands-off** `TOOL-dHashedPrelude-2` — this unit creates the module-scope assignment that unit
  2's arm reads by name. That arm reds until this lands.
- **hands-off** `TOOL-dHashedPrelude-3` — this unit changes no count, so unit 3's README claim is
  unaffected by it and moves for unit 2's reason alone.
- **consumes-from** external — `git_common_dir()` and `recall_conf.repo_root()` as they stand.

## 4. Design

`check(name)` returns a decorator whose body calls `fn()` and appends the outcome to `_checks`. A
decorator body runs when the decorated statement is executed, so every arm in this file runs during
module import, before `__main__` dispatches to `main()`. The guard's `before` is the first statement
of `main()`. It is therefore a digest of the log as the arms left it, and the comparison holds by
construction.

The repair moves the two assignments, unchanged, to module scope. The earliest legal home is below
`cleanup()` and above the arms banner: `git_common_dir()` is defined above it and `recall_conf` is
imported at the top of the file, while the first `@check` is the next statement of consequence.

### Data model

Two module-level names replace the two locals. `_LIVE_LOG` is the path or `None`; `_LIVE_LOG_BEFORE`
is the hex digest or the absent-sentinel string. The leading underscore matches `_checks`, `_SWEPT`
and `_Skip`, which are this file's convention for run-level state.

### Files touched (estimate)

`tools/memory-recall/selftest.py`

### Alternatives rejected

Computing the digest immediately after the sibling imports, above `git_common_dir()`, would bracket
a few more statements but would have to re-derive the git common directory inline — a second copy of
a function this file already has. Rejected: every statement between the import block and `cleanup()`
is a definition, and no definition writes.

Converting `check()` into a registrar that defers execution to `main()` would fix the ordering at
its root and let the baseline stay where it is. Rejected as a larger change than this defect earns:
it rewrites the control flow of every arm in the file to move two lines, and each arm's failure
attribution moves with it.

## 5. Production-readiness checklist

- security — N/A. No new surface; the change reads one file the suite already read.
- perf / scale — one extra `sha256` of a 120 KB file at import time, on a suite whose arms spawn git.
- error / empty / loading states — S2's three outcomes are the state set, and each is preserved.
- observability — the ok row prints the first twelve hex characters of the baseline, as it does now.
- risks — the digest now runs at import, so anything importing this module pays it. Nothing does.
- testing — AC1 through AC4, with AC1's staged break as the liveness proof.
- migration — N/A. No stored state and no adopter copy: `selftest.py` is `project-owned` in
  `tools/memory-recall/kit.toml`.
- user docs — N/A here. The kit README is unit 3.

## 6. Acceptance criteria

- **AC1** — When an arm that appends one row to this repository's real query log is staged into the
  working copy and the suite is run, the row `the live query log is byte-identical after this run`
  reports FAIL and the process exits 1. The break is reverted immediately afterwards.
  Red when: the assignment is left inside `main()`, in which case that row reports ok and the exit
  status is 0 — the state observed on 2026-09-22.
  fixture: the break is hand-written into the working copy and never committed. The log it appends
  to is this repository's own, so the row is trimmed back out afterwards and AC4's digest reading is
  what proves it was.
- **AC2** — When the suite is run with no break staged, that same row reports ok and its detail is
  the first twelve hex characters of the baseline digest.
  Red when: `main()` recomputes its own `before`, which would make the row pass for the old reason
  rather than the new one.
- **AC3** — When the comment above the `_LIVE_LOG_BEFORE` assignment is read, it names three
  things the guard does not check: a concurrent writer, the `recall/cache/` directory beside the
  log, and a log absent at both ends.
  Red when: the comment states only what the guard does check, which is the state the gate-header
  rule exists to refuse.
- **AC4** — When `sha256sum` is taken over the live query log immediately before and immediately
  after every run this unit performs, the two readings are equal, and `SELFTEST_ARMS` still reads 71
  with no new line added to its provenance chain.
  figure: 71 is PINNED, read from the file at BASE. The digests are DERIVED at observation time.
  Red when: a run of this unit leaves a row in the log — the defect under repair reproducing itself
  during its own repair.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test`

New arm: none. This unit adds no arm; the failing case of the guard it repairs is staged by hand per
AC1 and reverted, and unit 2 is where that ordering acquires a permanent arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.

## 10. Reuse audit

No existing seam fits. The reuse probe over the phrase "capture a baseline hash of a file before a
test suite runs and compare it afterwards" returns `hash_file` in `tools/govkit/census.py` at fan-in
1 and `render_baseline` in `tools/codebase-map/map_lib.py` at fan-in 2, neither of which brackets a
run; its top-ranked seam is the name stem `run`, which the tool's own header warns means only that
the name is common. The mechanism this unit moves is two statements already in the file, so the
reuse question here is where they belong rather than what to call them.

Recall terms used: selftest live query log byte-identical guard arm count pin provenance chain
memory-recall kit version staged break

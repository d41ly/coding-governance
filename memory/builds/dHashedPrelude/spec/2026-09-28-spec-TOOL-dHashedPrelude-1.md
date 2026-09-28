# TOOL-dHashedPrelude-1 — the live-log baseline is captured above the first decorated arm

**Status:** SPECCED · rev-4 · 2026-09-28 · node d · Tier-2 · base 3cf05f29 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round2.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round2.md) | spec-audit | TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3 |

<!-- /gen:spec-records -->

## 1. Goal

Make the memory-recall selftest's live-query-log guard able to fail. Its `before` digest is taken
inside `main()`, after every arm has already run, so the row it feeds brackets nothing and reports
ok whatever the arms did to the log.

## 2. Scope (IN)

- **S1** — The live-log path and its `before` digest are assigned at MODULE scope, textually above
  the first decorated arm. Observed by AC1.
- **S2** — The guard's verdict becomes a function, `_build_live_log_row(live, before)`, returning the
  `(state, name, detail)` triple `_checks` holds. It is TOTAL over the four states the code can
  actually be in, which the rev-1 draft of this item got wrong:

  | state | today | after this unit |
  |---|---|---|
  | repo reachable, log present, digests equal | `ok`, detail is the first twelve hex | unchanged |
  | repo reachable, log present, digests differ | `FAIL`, detail `the gate wrote to it` | `FAIL`, detail carries BOTH digests |
  | repo reachable, no log file at either reading | `ok`, both ends the absent-sentinel | unchanged |
  | repository unresolvable | NO ROW AT ALL — `main()` guards the append on the path being set | `skip`, naming why it could not run |

  The fourth row is a ruling, not a preservation: a skip that looks like an absence is the
  green-by-absence class this build exists to close, showing up on the guard's own row. Observed by
  AC2 and AC5.
- **S3** — The assignment carries a comment stating what the guard does NOT check: that it is a
  whole-file digest and cannot tell an arm's write from a concurrent one by another session sharing
  this repository, that it covers one path and says nothing about the cache directory beside it,
  that a log absent at both readings is indistinguishable from a protected one, and that a write
  reverted before `main()` reaches the compare is invisible. Observed by AC3.
- **S4** — Nothing outside the live-log guard moves. The arms, their order, the arity assertion and
  the pin are untouched; `SELFTEST_ARMS` does not change, because no arm is added here. In every
  reachable-repository state the count of appended run-property rows is unchanged at five, and in
  the unresolvable state it rises from four to five, which is S2's ruling and nothing else.
  Observed by AC6.

## 3. Non-goals (OUT)

No permanent arm that writes to the real query log: the break that proves this works is staged into
the working tree, observed, and reverted. This unit adds no arm at all — `_build_live_log_row` is built
here so that unit 2's arms can reach the branches, and those arms are unit 2's. No change to
`query.py`, `extract.py` or any existing arm's behaviour. No second guard over the cache directory —
the comment names that gap, it does not close it. No change to how `repo_root()` resolves.

### Edges

- **hands-off** `TOOL-dHashedPrelude-2` — this unit creates the module-scope assignment, the
  unconditional append in `main()`, and the `_build_live_log_row` function that unit 2's two arms read
  and drive. Both arms red until this lands.
- **hands-off** `TOOL-dHashedPrelude-3` — this unit changes no count, so nothing in unit 3 depends
  on it.
- **consumes-from** external — `git_common_dir()` and `recall_conf.repo_root()` as they stand.

## 4. Design

`check(name)` returns a decorator whose body calls `fn()`, so every arm in this file runs during
module import, before `__main__` dispatches to `main()`. The guard's `before` is the first statement
of `main()`. It is therefore a digest of the log as the arms left it, and the comparison holds by
construction.

The repair moves the two assignments, unchanged, to module scope. Any point from the end of
`git_common_dir()` to the first decorated arm is legal, so this is a choice among about fifty lines
rather than a forced one: the site chosen is immediately above the arms banner, so the comment
reads as a preamble to the arms it brackets. The rev-1 draft called that site "the earliest point
where `git_common_dir()` and `recall_conf` are both defined", which was the opposite of true — it is
the latest such point.

`main()` then appends `_build_live_log_row(_LIVE_LOG, _LIVE_LOG_BEFORE)` unconditionally, in place of the
guarded branch that decides whether a row exists. One consequence worth naming: the number of
appended run-property rows stops depending on the environment, so the suite's summary denominator
becomes deterministic.

A second execution path exists and the rev-1 draft did not name it. One arm runs a full nested
selftest from an adopter layout, so this module is imported a second time inside that run, against a
fixture repository. The baseline is computed there too. It is inside the existing `try`, so a
fixture with no resolvable git repository yields the unresolvable state, which after S2 emits a
`skip` row rather than silence.

### Data model

Two module-level names replace the two locals. `_LIVE_LOG` is the path or the none-value;
`_LIVE_LOG_BEFORE` is the hex digest or the absent-sentinel string. The assignment is written
unannotated and spelled `_LIVE_LOG_BEFORE = `, because unit 2's arm anchors on those bytes. The
leading underscore matches `_checks`, `_SWEPT` and `_Skip`, this file's convention for run-level
state.

### Files touched (estimate)

`tools/memory-recall/selftest.py`

### Alternatives rejected

Computing the digest immediately after the sibling imports, above `git_common_dir()`, would bracket
a few more statements but would have to re-derive the git common directory inline — a second copy of
a function this file already has. Rejected: every statement between the import block and the arms
banner is a definition, and no definition writes, so the extra bracket covers nothing.

Converting `check()` into a registrar that defers execution to `main()` would fix the ordering at
its root and let the baseline stay where it is. Rejected as a larger change than this defect earns:
it rewrites the control flow of every arm in the file to move two lines, and each arm's failure
attribution moves with it.

Leaving the unresolvable state silent, and merely documenting it, was the rev-1 position. Rejected
on the round-1 audit's reading: a spec that says it preserves a state set it never opened is how the
wrong state gets preserved, and the charter already rules that a skip must announce itself.

## 5. Production-readiness checklist

- security — N/A. No new surface; the change reads one file the suite already read.
- perf / scale — one extra `sha256` at import time, over the live log, which measures 1,545,472
  bytes today and is append-only, so this figure rises. The suite spawns git per arm, so this is not
  the cost that matters.
- error / empty / loading states — S2's table is the state set. Three states are preserved and the
  fourth is ruled on; AC5 observes the one no existing criterion could reach.
- observability — the ok row prints the first twelve hex characters of the baseline, as it does now;
  the FAIL row gains the second digest so a failure names what it changed to.
- risks — the digest runs at import, so anything importing this module pays it, including the nested
  adopter-layout run. Nothing else imports it.
- testing — AC1 through AC5. AC1's staged break is the liveness proof; AC5's state is reachable only
  through `_build_live_log_row`, which is why S2 makes it a function.
- migration — N/A. No stored state and no adopter copy: `selftest.py` is `project-owned` in
  `tools/memory-recall/kit.toml`.
- user docs — N/A here. The kit README is unit 3.

## 6. Acceptance criteria

- **AC1** — When an arm that appends one row to this repository's real query log is staged into the
  working copy and the suite is run, the row `the live query log is byte-identical after this run`
  reports FAIL and the process exits 1. The break is reverted immediately afterwards.
  Red when: the assignment is left inside `main()`, in which case that row reports ok and the exit
  status is 0 — the state observed on 2026-09-22.
  fixture: the break is hand-written into the working copy and never committed. It must drive the
  real logging path rather than append a synthetic line by hand, because an arm that writes a
  simpler value proves the mechanism for the simpler value. The row it adds is trimmed back out
  afterwards, and AC4 is what proves it was.
- **AC2** — When the suite is run with no break staged, that same row reports ok and its detail is
  the first twelve hex characters of the baseline digest.
  Red when: `main()` recomputes its own `before`, which would make the row pass for the old reason
  rather than the new one.
- **AC3** — When the new assignment is read, the comment above it names four things the guard does
  not check: a concurrent writer in another session, the `recall/cache/` directory beside the log, a
  log absent at both readings, and a write reverted before the compare.
  Red when: the comment states only what the guard does check, which is the state the gate-header
  rule exists to refuse.
- **AC4** — When `sha256sum` and a row count are taken over the live query log immediately before
  and immediately after every run this unit performs, both readings are recorded, and any row
  present at the second reading and not the first is quoted with its `at` timestamp so a concurrent
  session's row is distinguishable from a suite write. `SELFTEST_ARMS` still reads 71 with no line
  added to its provenance chain.
  figure: 71 is PINNED, read from the file at BASE. The digests and row counts are DERIVED at
  observation time.
  Red when: a row appended between the two readings carries a timestamp from this run and a path
  this run's arms touched — the defect under repair reproducing itself during its own repair. The
  quoting requirement exists because this log is shared by every session on this node: rows 596 and
  597 arrived during this build's own kickoff from a query it did not issue, so equal digests cannot
  be assumed and unequal ones do not by themselves convict the suite.
- **AC5** — When `_build_live_log_row` is called with the path argument set to the none-value, it returns
  a triple whose state is `skip` and whose detail names the unresolvable repository; called with a
  path that does not exist and the absent-sentinel as the baseline, it returns an `ok` triple; and
  called with two differing digests, it returns a `FAIL` triple whose detail contains both digest
  prefixes rather than only the baseline.
  Red when: the unresolvable case returns no triple, which restores a row that is absent rather
  than a skip that announces itself; or the failing case reports only what the digest was, which
  is the detail the pre-unit code carried and which names nothing about what it became.
- **AC6** — When the body of `main()` is read after this unit, the guard's row is appended by a
  single unconditional `_checks.append(_build_live_log_row(...))` and no conditional on the log path
  being set survives anywhere in it.
  Red when: the module-scope assignment lands but the old conditional append is left in place, in
  which case the row is emitted twice, the summary prints one row more than the suite has, and
  both copies are green. Unit 2's ordering arm is what keeps this true afterwards.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test`

New arm: none. This unit adds no arm; the failing case of the guard it repairs is staged by hand per
AC1 and reverted, and unit 2 is where the ordering and the state set acquire permanent arms.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.
- rev-2 · 2026-09-28 · §2 S2 · §2 S3 · §2 S4 · §3 · §4 · §5 · AC3 · AC4 · AC5 · folded the round-1
  spec audit. S2 replaced a three-state claim the code does not have with the four real states and
  rules on the unresolvable one (D-2); the guard's verdict becomes `_build_live_log_row` so unit 2 can
  drive branches a suite run cannot reach. §4 corrects "earliest point", which named the latest such
  point (D-7), and adds the nested adopter-layout import path. §5's perf row priced a 120 KB file
  against a live log of 1,545,472 bytes (D-8). AC3 gains the fourth NOT-CHECKED item, AC4 gains the
  row-count and delta-quoting requirement after rows from another session appeared in the log during
  this build, and AC5 is new.
- rev-3 · 2026-09-28 · §2 S4 · §3 · AC5 · AC6 · folded the round-2 spec audit. S4's row-count
  clause named AC4 as its observer, which counts rows in the query log rather than rows in the
  suite's output; it now names AC6. AC6 is new: nothing in the three-spec set observed that
  `main()` appends the guard's row unconditionally, so a build that kept the old conditional
  beside the new append would emit the row twice and print a longer green summary. AC5 gains the
  differing-digest clause, which S2 had specified and no criterion reached.
- rev-4 · 2026-09-28 · §2 S2 · §4 · AC5 · the three helpers are renamed to lead with a verb
  the lexicon declares: `_resolve_live_log`, `_derive_live_log_digest` and
  `_build_live_log_row`. The originals led with `live`, which is not in the VERBS table, and
  `tools/lexicon/lexicon.py` reds on a shrink-only offender pin the three of them moved 982
  to 985. Names chosen with `--suggest`, not by guess. Behaviour is unchanged.

## 10. Reuse audit

No existing seam fits. The reuse probe over the phrase "capture a baseline hash of a file before a
test suite runs and compare it afterwards" returns `hash_file` in `tools/govkit/census.py` at fan-in
1 and `render_baseline` in `tools/codebase-map/map_lib.py` at fan-in 2, neither of which brackets a
run; its top-ranked seam is the name stem `run`, which the tool's own header warns means only that
the name is common. The mechanism this unit moves is two statements already in the file, so the
reuse question here is where they belong rather than what to call them. The one seam it does extend
is local and was found by reading the file rather than by the probe: `check_provenance_chain(src,
pinned)` is this file's own shape for a verdict computed by a function so an arm can drive it, and
`_build_live_log_row` takes it.

Recall terms used: selftest live query log byte-identical guard arm count pin provenance chain
memory-recall kit version staged break

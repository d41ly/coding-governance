# TOOL-dHashedPrelude-2 — two arms red when the live-log guard stops bracketing the arms

**Status:** SPECCED · rev-2 · 2026-09-28 · node d · Tier-2 · base 3cf05f29 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-3 |

<!-- /gen:spec-records -->

## 1. Goal

Gate what unit 1 establishes. The repair is a handful of statements in a 2745-line file with nothing
watching where they sit, so a later edit that moves the baseline back into `main()`, that adds a
decorated arm above it, or that restores a conditional append, puts the blind guard back with no
signal saying so.

## 2. Scope (IN)

- **S1** — An ordering arm, `test_the_live_log_baseline_is_taken_before_any_arm_runs`, asserts from
  source text that the module-scope baseline appears before the first decorated arm, and that the
  body of `main()` reads it rather than recomputing one. Observed by AC1 and AC2.
- **S2** — That arm takes its source as a parameter, defaulting to this file, so every failure
  direction is reachable from a synthetic string. This is the shape `check_provenance_chain(src,
  pinned)` already uses in this file, and its docstring states the same reason. Observed by AC4.
- **S3** — The arm asserts its own anchors are UNAMBIGUOUS before it compares them: each anchor is
  newline-anchored, and the arm reds if the unanchored form of an anchor resolves to a different
  offset than the anchored form, which is the condition that silently re-points the comparison.
  Observed by AC5.
- **S4** — A state arm, `test_the_live_log_row_is_total_over_its_four_states`, drives
  `_live_log_row` over all four states of unit 1's S2 table and asserts the state token of each.
  Observed by AC3.
- **S5** — Both arms are registered in `main()`'s `order` list so the declared-versus-ran assertion
  counts them, and `SELFTEST_ARMS` moves from 71 to 73 with the one provenance line its chain
  requires. Observed by AC6.
- **S6** — Each arm's docstring states why it reads source or calls the function directly rather
  than observing the suite's behaviour: the behavioural test is a write to the real query log, which
  this suite may not make. Observed by AC7.

## 3. Non-goals (OUT)

No behavioural arm, for the reason S6 records. No parser and no AST walk: substring searches answer
the question, and an AST import would be the only one in this file. No generalisation to the sibling
selftests — a kickoff sweep found that eight of them run arms at decoration time and none takes a
run-level baseline of a real file, so there is no second instance to cover. No change to `check()`
itself, and no change to the summary line, which is recorded as a backlog row instead.

### Edges

- **consumes-from** `TOOL-dHashedPrelude-1` — the module-scope assignment this unit's ordering arm
  reads by name, and the `_live_log_row` function its state arm calls. Without them both arms red,
  which is the correct verdict on a tree that has not landed unit 1.
- **hands-off** `TOOL-dHashedPrelude-3` — this unit changes the number of arms and therefore the
  number the suite reports, which is the occasion for unit 3's README claim to move.

## 4. Design

### Data model

No new state. Each arm returns a one-line detail naming what it measured, so a reader of a green row
can see which bytes were compared.

### Inventory

Two new module-level functions in this file's `test_*` cell:
`test_the_live_log_baseline_is_taken_before_any_arm_runs` and
`test_the_live_log_row_is_total_over_its_four_states`. Both follow the convention of
`test_the_selftest_pin_carries_an_unbroken_provenance_chain`, the file's existing self-referential
arm. One pinned constant moves rather than being minted: `SELFTEST_ARMS`, 71 to 73.

### The anchors, by their exact bytes

This is the part the rev-1 draft left to the implementer, and the round-1 audit measured what that
cost. The three anchors are NEWLINE-ANCHORED, and the leading newline is load-bearing rather than
decorative:

| anchor, as searched | offset today | line | the unanchored form resolves to |
|---|---|---|---|
| `\n@check(` | 14712 | 287 — the first decorated arm | offset 7955, line 145, inside `check_provenance_chain()`'s docstring |
| `\n_LIVE_LOG_BEFORE = ` | created by unit 1, near 14600 | above the arms banner | same site; the risk is a later mention above it |
| `\ndef main() -> int:` | 2634 by line | the definition | unique today, anchored anyway |

The first row is the whole reason S3 exists. `selftest.py:145` reads ``counting `@check(` decorators
by reading the source``, so an arm anchored on the bare string compares an offset inside a docstring
against the baseline's offset near 14600, concludes the baseline comes after the first arm, and reds
against a CORRECT file. An arm that fails on the thing it certifies is the class this build exists
to close, reproduced inside the closing mechanism. These offsets are DERIVED: S3 makes the arm
re-derive them every run instead of trusting this table.

### How each arm decides

The ordering arm compares three offsets in its `src` argument. If the baseline assignment is moved
into `main()`, the first occurrence of the assignment literal becomes this arm's own string constant,
which sits far below the first decorated arm, so the ordering assertion still fires — the arm
catches the relocation without needing the relocated statement to be findable.

That same property is why the not-found branch is not a guard against anything when `src` defaults
to this file: the arm's own source always contains both literals, so the search cannot return the
not-found value. The rev-1 draft claimed that branch as a defence against passing by finding
nothing, and claimed a rename would produce a not-found diagnostic. Neither was true — a rename
surfaces as an ORDERING failure pointing at the wrong cause. S2 is the fix: with `src` a parameter,
AC4 drives a synthetic source that lacks the literal and the branch becomes reachable and tested.

The state arm calls `_live_log_row` directly with each of the four inputs. Two of the four states
cannot be produced by running the suite in this repository at all, which is why unit 1 makes the
verdict a function rather than an inline branch.

### Files touched (estimate)

`tools/memory-recall/selftest.py`

### Alternatives rejected

Asserting the ordering by behaviour — write a row to a log, run the guard, expect FAIL — is the
strongest form and is rejected outright: the only log the guard watches is this repository's own,
and an arm that writes to it is the defect the guard exists to catch. Pointing the arm at a fixture
log instead does not work either, because the guard resolves its path from `repo_root()`, which
anchors on the kit file and ignores any directory an arm chdirs to.

Parsing the module with `ast` and comparing line numbers is more precise about what "before" means.
Rejected: it imports a module nothing else here imports, and it cannot see the case that matters
more — an assignment moved into `main()` is still an assignment, and the offset compare catches it
with two substring searches.

Driving the four states by running a patched copy of the suite in a subprocess was considered for
the state arm and rejected: it costs a full nested run per state to observe a three-field return
value that a direct call gives for nothing.

## 5. Production-readiness checklist

- security — N/A. The arms read one file already on disk and execute nothing.
- perf / scale — one read of a 151 KB file and a handful of substring searches, plus four direct
  calls. Below measurement noise on a suite that spawns git per arm.
- error / empty / loading states — with `src` a parameter, a missing literal is an assertion failure
  naming which one, and AC4 drives it. Under the default argument that branch is unreachable by
  construction, which §4 states rather than claiming a defence that does not exist.
- observability — each arm's detail line names what it measured.
- risks — the arms are anchored on literal names, so a rename reds them. That is intended and the
  docstrings say so, but it is the maintenance cost this unit adds.
- testing — AC1 through AC7. Every RED is observed against a synthetic source or a copy, never
  against the shipped file.
- migration — N/A. `selftest.py` is `project-owned` in `tools/memory-recall/kit.toml` and reaches no
  adopter.
- user docs — N/A here. The kit README is unit 3.

## 6. Acceptance criteria

- **AC1** — When the ordering arm is given a source in which the baseline assignment sits inside
  `main()`, it reports FAIL and its detail names the ordering it expected. Given this file it
  reports ok.
  Red when: the arm compares two offsets that are both inside its own source constants, in which
  case the relation never changes and the arm passes on every input.
- **AC2** — When the ordering arm is given a source whose module-scope baseline is present but whose
  `main()` body does not mention `_LIVE_LOG_BEFORE`, it reports FAIL.
  Red when: the arm asserts only the ordering, in which case a baseline that is never read passes.
- **AC3** — When the state arm runs, it asserts `_live_log_row` returns state `skip` for an
  unresolvable repository, `ok` for equal digests, `ok` for a log absent at both readings, and
  `FAIL` for differing digests, and the arm reports ok.
  Red when: the unresolvable input returns nothing, or returns `ok`, which is the row that would
  announce a protected log where none was read.
- **AC4** — When the ordering arm is given a synthetic source containing neither anchor, it reports
  FAIL with a message naming the literal it could not find — `_LIVE_LOG_BEFORE` or the decorator
  anchor — rather than an ordering complaint.
  Red when: the arm keeps its file-only default and the not-found branch stays unreachable, which is
  the state the rev-1 draft described as a guard.
  fixture: the synthetic source is a short string built in the arm; no file is written.
- **AC5** — When the ordering arm runs against this file, it asserts that each anchor occurs at
  least once in its newline-anchored form, and that for `@check(` the unanchored offset and the
  anchored offset differ — today 7955 against 14712.
  figure: both offsets are DERIVED by the arm at run time; the two numbers here are PINNED, measured
  on 2026-09-28 at BASE, and the arm does not read them.
  Red when: the arm hard-codes either number, which would make it a pin over a file that moves on
  every edit rather than a check that the anchor is unambiguous.
- **AC6** — When the suite is run, the row `the declared arm count matches its pin` reports ok with
  detail `73 == SELFTEST_ARMS`, and the row `the arm-count pin ends an unbroken provenance chain`
  reports ok.
  figure: 73 is PINNED here and DERIVED by that row's own detail at observation time. The summary
  line is deliberately not the instrument: it prints a count of check ROWS, which is 76 at BASE and
  78 after this unit, and it does not carry the declared arm count.
  Red when: an arm is defined but not added to `order`, which the arity assertion catches, or
  `SELFTEST_ARMS` is bumped without its provenance line, which `check_provenance_chain()` catches.
- **AC7** — When the docstrings of `test_the_live_log_baseline_is_taken_before_any_arm_runs` and
  `test_the_live_log_row_is_total_over_its_four_states` are read, each states that a behavioural
  test of its property would write to the real query log, and that this is why it reads source or
  calls `_live_log_row` directly.
  Red when: a docstring describes only what its arm does, leaving the next reader to re-derive why
  the obvious stronger test is absent and to write it.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test`

New arm: `tools/memory-recall/selftest.py` · the ordering arm's failing cases are three synthetic
sources — baseline inside `main()`, baseline unread by `main()`, and neither literal present — and
the state arm's is a `_live_log_row` return whose state token is wrong for its input · the
`SELFTEST_ARMS` pin moves 71 to 73 with its provenance line.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.
- rev-2 · 2026-09-28 · §1 · §2 S2 · §2 S3 · §2 S4 · §3 · §4 · §5 · AC1 · AC3 · AC4 · AC5 · AC6 ·
  folded the round-1 spec audit. §4 now names the exact anchor bytes and their measured offsets,
  which the draft left to the implementer: the bare `@check(` resolves to a docstring at line 145
  and would have made the arm red against a correct file, the round's blocker (D-1). S2 makes the
  source a parameter so the not-found branch is reachable and AC4 drives it, replacing a claimed
  defence that sat on an unreachable branch (D-4). A second arm and S4 come from unit 1's new
  `_live_log_row`, so the pin moves 71 to 73 rather than 71 to 72. AC6 reads the count off the pin
  row's own detail instead of the summary line, which counts check rows and not arms (D-5).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "capture a baseline hash of a file before a test suite
runs and compare it afterwards"` finds no existing seam fits for the ordering question: it ranks on
the name stem `run`, which its own header warns means only that the name is common.

The seam this unit extends is local and the probe does not index it: the suite already reads its own
source to grade what follows the `main()` definition, and `check_provenance_chain(src, pinned)`
already parses this file's comment block for the pin's history while taking its source as a
parameter so an arm can drive every failure direction. Both are source-text reads over this file
with no parser, which is the shape both new arms take, S2 included.

The occurrence census the rev-1 draft skipped, and which the audit identified as the reason the
blocker went unseen, is the table in §4: every anchor this design depends on was counted in the
target file before the arm was designed around it.

Recall terms used: selftest live query log byte-identical guard arm count pin provenance chain
memory-recall kit version staged break

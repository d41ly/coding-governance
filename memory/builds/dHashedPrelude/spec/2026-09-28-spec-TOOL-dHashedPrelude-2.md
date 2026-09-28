# TOOL-dHashedPrelude-2 — an arm reds when the live-log baseline stops preceding the arms

**Status:** SPECCED · rev-1 · 2026-09-28 · node d · Tier-2 · base 3cf05f29 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Gate the ordering unit 1 establishes. The repair is two statements in a 2745-line file with nothing
watching where they sit, so a later edit that moves the baseline back into `main()`, or that adds a
decorated arm above it, restores the blind guard and no signal says so.

## 2. Scope (IN)

- **S1** — A new arm asserts, from this file's own source text, that the module-scope baseline
  assignment appears before the first decorated arm. Observed by AC1.
- **S2** — The same arm asserts that the body of `main()` reads the module-scope baseline, so a
  baseline that exists but is ignored is a red rather than a pass. Observed by AC2.
- **S3** — The arm is registered in `main()`'s `order` list, so the declared-versus-ran assertion
  counts it, and `SELFTEST_ARMS` moves from 71 to 72 with the `71 -> 72 on 2026-09-28` line its
  provenance chain requires. Observed by AC3.
- **S4** — The arm's docstring states why it reads source rather than observing behaviour: the
  behavioural test is a write to the real query log, which this suite may not make. Observed by AC4.

## 3. Non-goals (OUT)

No behavioural arm, for the reason S4 records. No parser and no AST walk: two substring searches
answer the question, and an AST import would be the only one in this file. No generalisation of the
arm to the sibling selftests — a kickoff sweep found that eight of them run arms at decoration time
and none takes a run-level baseline of a real file, so there is no second instance to cover. No
change to `check()` itself.

### Edges

- **consumes-from** `TOOL-dHashedPrelude-1` — the module-scope assignment this arm reads by name.
  Without it the arm reds, which is the correct verdict on a tree that has not landed unit 1.
- **hands-off** `TOOL-dHashedPrelude-3` — this unit changes the number of arms the suite reports,
  which is the occasion for unit 3's README claim to move.

## 4. Design

The arm reads `__file__` and compares three offsets in the text: the module-scope assignment, the
first decorated arm, and the start of `main()`. The file already reads its own source this way,
partitioning on the `main()` definition to grade what follows it, so the idiom is this file's own
rather than a new one.

Two searches are deliberately anchored on literals the arm itself also contains. That is safe in one
direction and is the point in the other: if the assignment is moved into `main()`, the first
occurrence of the assignment literal becomes the arm's own string constant, which sits far below the
first decorated arm, so the ordering assertion still fires. A rename of the module-scope name
without a matching edit here reds too, with a message naming the missing literal — a red that
correctly forces whoever renames it to look at the arm.

### Data model

No new state. The arm returns a one-line detail naming the two offsets it compared, so a reader of
a green row can see which bytes were measured.

### Inventory

One new identifier, a module-level function in this file's `test_*` cell:
`test_the_live_log_baseline_is_taken_before_any_arm_runs`. It follows the convention of
`test_the_selftest_pin_carries_an_unbroken_provenance_chain`, the file's existing self-referential
arm. One pinned constant moves rather than being minted: `SELFTEST_ARMS`, 71 to 72.

### Files touched (estimate)

`tools/memory-recall/selftest.py`

### Alternatives rejected

Asserting the ordering by behaviour — write a row to a log, run the guard, expect FAIL — is the
strongest form and is rejected outright: the only log the guard watches is this repository's own,
and an arm that writes to it is the defect the guard exists to catch. Pointing the arm at a fixture
log instead does not work either, because the guard resolves its path from `repo_root()`, which
anchors on the kit file and ignores any directory an arm chdirs to.

Parsing the module with `ast` and comparing line numbers of the assignment and the first decorated
definition is more precise about what "before" means. Rejected: it imports a module nothing else
here imports, and it cannot see the case that matters more — an assignment moved into `main()` is
still an assignment, and the offset compare catches it with two `str.find` calls.

## 5. Production-readiness checklist

- security — N/A. The arm reads one file already on disk and executes nothing.
- perf / scale — one read of a 151 KB file and three substring searches, on a suite that spawns git
  per arm. Below measurement noise.
- error / empty / loading states — a missing literal on either side is an assertion failure naming
  which one, not a silent pass; this is the arm's own guard against passing by finding nothing.
- observability — the detail line names both offsets.
- risks — the arm is anchored on literal names, so a rename reds it. That is intended and the
  docstring says so, but it is the maintenance cost this unit adds.
- testing — AC1 through AC4. AC1's RED is observed against a copy of the file, never against the
  shipped one.
- migration — N/A. `selftest.py` is `project-owned` in `tools/memory-recall/kit.toml` and reaches no
  adopter.
- user docs — N/A here. The kit README is unit 3.

## 6. Acceptance criteria

- **AC1** — When the new arm runs against a copy of the suite whose baseline assignment has been
  moved back inside `main()`, the arm reports FAIL and its detail names the ordering it expected.
  Against the shipped file it reports ok.
  Red when: the arm compares offsets that are both inside its own source constants, in which case
  the relation never changes and the arm passes on every input.
  fixture: the RED is staged into a copy under the session scratchpad, never into
  `tools/memory-recall/`, so the shipped file is never the broken one.
- **AC2** — When the arm runs against a copy in which the module-scope baseline is present but
  `main()` computes its own digest instead, the arm reports FAIL.
  Red when: the arm asserts only the ordering, in which case a baseline that is never read passes.
- **AC3** — When the suite is run, the row `the declared arm count matches its pin` reports ok, the
  row `the arm-count pin ends an unbroken provenance chain` reports ok, and the summary line counts
  one more declared arm than it did at BASE.
  figure: the declared count is DERIVED from the run's own summary line; 71 and 72 are PINNED, read
  from the file at BASE and after the edit.
  Red when: the arm is defined but not added to `order`, which the arity assertion catches, or
  `SELFTEST_ARMS` is bumped without its provenance line, which `check_provenance_chain()` catches.
- **AC4** — When the docstring of `test_the_live_log_baseline_is_taken_before_any_arm_runs` is
  read, it states that a behavioural test of this property would write to the real query log,
  and that this is why the arm reads source.
  Red when: the docstring describes only what the arm does, leaving the next reader to re-derive
  why the obvious stronger test is absent and to write it.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test`

New arm: `tools/memory-recall/selftest.py` · a copy of the file with the baseline assignment moved
back into `main()`, and a second copy with the assignment present but unread · the `SELFTEST_ARMS`
pin moves 71 to 72 with its provenance line.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "capture a baseline hash of a file before a test suite
runs and compare it afterwards"` returns no seam for the ordering question and ranks on the name
stem `run`, which its own header warns means only that the name is common. The seam this unit
extends is therefore one the map does not index, because it is inside the file itself: the suite
already reads its own source to grade what follows the `main()` definition, and
`check_provenance_chain()` already parses this file's comment block for the pin's history. Both
are source-text reads over `__file__` with no parser, which is the shape this arm takes.

Recall terms used: selftest live query log byte-identical guard arm count pin provenance chain
memory-recall kit version staged break

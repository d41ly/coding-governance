# TOOL-dHashedPrelude-2 — two arms red when the live-log guard stops bracketing the arms

**Status:** CLOSED · rev-5 · 2026-09-28 · node d · Tier-2 · base 3cf05f29 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-28-build-TOOL-dHashedPrelude-1-1-acceptance-ledger.md](../build/2026-09-28-build-TOOL-dHashedPrelude-1-1-acceptance-ledger.md) | journal | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-3 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff-round2.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff-round2.md) | diff-review | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-3 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff.md) | diff-review | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-3 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-3 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round2.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round2.md) | spec-audit | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-3 |

<!-- /gen:spec-records -->

## 1. Goal

Gate what unit 1 establishes. The repair is a handful of statements in a 2745-line file with nothing
watching where they sit, so a later edit that moves the baseline back into `main()`, that adds a
decorated arm above it, or that restores a conditional append, puts the blind guard back with no
signal saying so.

## 2. Scope (IN)

- **S1** — An ordering arm, `test_the_live_log_baseline_is_taken_before_any_arm_runs`, asserts from
  source text that the module-scope baseline appears before the first decorated arm, that the body
  of `main()` reads it rather than recomputing one, and that `main()` appends the guard's row
  unconditionally. Observed by AC1, AC2 and AC3.
- **S2** — That arm takes its source as a parameter, defaulting to this file, so every failure
  direction is reachable from a synthetic string. This is the shape `check_provenance_chain(src,
  pinned)` already uses in this file, and its docstring states the same reason. Observed by AC5.
- **S3** — Before comparing any offsets, the arm asserts each anchor's OCCURRENCE COUNT in the
  source it was given: the baseline anchor exactly once, the `main()` anchor exactly once, the
  decorator anchor at least once. A count outside that reds naming the anchor, so a later duplicate
  at column 0 is caught here instead of silently re-pointing a comparison. Observed by AC6.
- **S4** — A state arm, `test_the_build_live_log_row_is_total_over_its_four_states`, drives
  `_build_live_log_row` over all four states of unit 1's S2 table, asserts the state token of each, and
  asserts the differing-digest row's detail carries both digests. Observed by AC4.
- **S5** — Both arms are registered in `main()`'s `order` list so the declared-versus-ran assertion
  counts them, and `SELFTEST_ARMS` moves from 71 to 73 with the one provenance line its chain
  requires. Observed by AC7.
- **S6** — Each arm's docstring states why it reads source or calls the verdict function directly
  rather than observing the suite's behaviour: the behavioural test is a write to the real query
  log, which this suite may not make. Observed by AC8.

## 3. Non-goals (OUT)

No behavioural arm, for the reason S6 records. Substring searches answer the ORDERING question and
`ast` answers the APPEND question; the split is in §4, and the draft that rejected `ast` outright
was wrong about the second half. No generalisation to the sibling
selftests — a kickoff sweep found that eight of them run arms at decoration time and none takes a
run-level baseline of a real file, so there is no second instance to cover. No change to `check()`
itself, and no change to the summary line. That deferral and one other are PARKED in this build's
README under "Parked decisions", with the question, the option seen and the reason it was
refused; neither is given a backlog id, because `memory/backlog/TOOL.md` sits at its shrink-only
row pin and a row cannot be added to it without draining two.

### Edges

- **consumes-from** `TOOL-dHashedPrelude-1` — the module-scope assignment this unit's ordering arm
  reads by name, the unconditional append it asserts, and the `_build_live_log_row` function its state arm
  calls. Without them both arms red, which is the correct verdict on a tree that has not landed
  unit 1.
- **hands-off** `TOOL-dHashedPrelude-3` — this unit changes the number of arms and therefore the
  number the suite reports, which is the occasion for unit 3's README claim to move.

## 4. Design

### Data model

No new state. Each arm returns a one-line detail naming what it measured, so a reader of a green row
can see what was compared.

### Inventory

Two new module-level functions in this file's `test_*` cell:
`test_the_live_log_baseline_is_taken_before_any_arm_runs` and
`test_the_build_live_log_row_is_total_over_its_four_states`. Both follow the convention of
`test_the_selftest_pin_carries_an_unbroken_provenance_chain`, the file's existing self-referential
arm. Three module-level anchor constants are minted beside them. One pinned constant moves rather
than being minted: `SELFTEST_ARMS`, 71 to 73.

### The anchors, by their exact bytes

Every anchor carries a LEADING NEWLINE, which makes it a column-0 anchor. Counted on the blob at
BASE:

| anchor, as searched | bare form | newline-anchored form |
|---|---|---|
| `@check(` | 72 occurrences; first at line 145, inside `check_provenance_chain()`'s docstring | 71 occurrences; first at line 287, the first decorated arm |
| `def main() -> int:` | 2 occurrences; first at line 2379, inside `src.partition(...)` | 1 occurrence, at line 2634 |
| `_LIVE_LOG_BEFORE = ` | created by unit 1 | 1 occurrence, above the arms banner |

LINE numbers are pinned here and byte offsets deliberately are not: a line number is identical
however the file is read, while an offset differs by the number of line endings preceding it. The
rev-2 draft of this section pinned offsets measured in a CRLF working copy and labelled them
"measured at BASE"; the blob at BASE is LF and gives different numbers for the same lines. That is
the class this repo files as a worktree smudge on a path no `eol` pin covers, and it reached a spec
whose whole subject is an anchor. `tools/**/*.py` carries no `eol=lf` pin today; proposing one is parked in this build's README,
because it is a repo-wide renormalize and not this build's to make.

What the leading newline buys, stated exactly: a literal written inside this file's own source with
a backslash-n escape — `"\n@check("` in the arm itself, `src.partition("\ndef main() -> int:")` at
line 2379 — is the two characters backslash and n, not a newline, so a real-newline search does not
match it. Verified: the bare form of the `main()` anchor occurs twice and the anchored form once.
The first row of the table is the reason the anchoring exists at all: an arm searching the bare
`@check(` compares an offset inside a docstring at line 145 against a baseline near line 285,
concludes the baseline comes after the first arm, and reds against a CORRECT file. An arm that fails
on the thing it certifies is the class this build exists to close, reproduced inside the closing
mechanism.

### How each arm decides

The ordering arm is given a source, counts its three anchors per S3, then compares offsets. A
relocation reds through the COUNT check rather than the offset check, and this is worth stating
because the rev-1 and rev-2 drafts both described the opposite mechanism: if the baseline assignment
is moved into `main()` it becomes indented, so the column-0 anchor matches nothing, the count is
zero, and the arm reds naming the anchor it could not find. The arm's own string constant does not
rescue the search, because it is written with an escape and is not a newline.

That makes the not-found direction reachable against a real relocation, and S2 makes it reachable
against a synthetic source as well, which is what AC5 drives. The rev-2 draft claimed that branch
was unreachable by construction; it is not, once the anchors carry newlines.

The `main()` clauses read the source after the `main()` anchor. One asserts `_LIVE_LOG_BEFORE`
appears there, so a `main()` that recomputes its own baseline reds. The other asserts the append is
unconditional — the row is appended with no surviving guard on the path being set — because a build
that keeps unit 1's module-scope assignment AND the old conditional append emits the live-log row
twice, prints a green summary one row longer than it should be, and no other criterion in this set
reaches that.

The state arm calls `_build_live_log_row` directly with each of the four inputs. Two of the four states
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
Rejected FOR THE ORDERING CLAUSE ONLY: it cannot see the case that matters more — an assignment
moved into `main()` is still an assignment, and the column-0 anchor catches it with a count.

For the APPEND clause the same rejection was wrong, and the closing diff review measured how wrong.
Three substring tests over `main()`'s raw text greened on seven ways of disabling the guard:
commenting the append out, which preserves its text by definition; an `if _LIVE_LOG:` wrapper; a
`try`/`except`; a renamed local; a duplicate; and `global _LIVE_LOG_BEFORE` plus a re-derive inside
`main()`, which restores the original defect exactly. Only outright deletion redded, and every
passing row returned a byte-identical detail string. A text search cannot see structure, so it
cannot see unconditionality, singleness, or which values the row is built from. The clause is now
an `ast` scan of `main()`'s DIRECT body statements — never `ast.walk`, because invisibility under
nesting IS the property — plus a check that the arguments are the module-scope pair and that
nothing rebinds the baseline inside the function.

Driving the four states by running a patched copy of the suite in a subprocess was considered for
the state arm and rejected: it costs a full nested run per state to observe a three-field return
value that a direct call gives for nothing.

Pinning byte offsets and asserting the arm reproduces them was the rev-2 design and is rejected: the
numbers depend on how the file is read, they move on every edit above them, and an acceptance
criterion resting on one couples a merge-bar leg to the current wording of an unrelated docstring.

## 5. Production-readiness checklist

- security — N/A. The arms read one file already on disk and execute nothing.
- perf / scale — one read of a 148,697-byte file (the blob at BASE; the CRLF working copy is
  151,442) and a handful of substring searches, plus four direct calls. Below measurement noise on a
  suite that spawns git per arm.
- error / empty / loading states — S3's count assertions are the not-found handling, and they red
  naming the anchor. AC5 drives them over a synthetic source and AC6 over this file.
- observability — each arm's detail line names what it measured.
- risks — the arms are anchored on literal names, so a rename reds them. That is intended and the
  docstrings say so, but it is the maintenance cost this unit adds.
- testing — AC1 through AC8. Every RED is observed against a synthetic source, never against the
  shipped file.
- migration — N/A. `selftest.py` is `project-owned` in `tools/memory-recall/kit.toml` and reaches no
  adopter.
- user docs — N/A here. The kit README is unit 3.

## 6. Acceptance criteria

- **AC1** — When the ordering arm is given a source in which the baseline assignment sits indented
  inside `main()`, it reports FAIL naming the baseline anchor it could not find at column 0. Given
  this file it reports ok.
  Red when: the arm searches the anchors without their leading newline, in which case the decorator
  anchor resolves into a docstring and the arm reds against a correct file.
- **AC2** — When the ordering arm is given a source whose module-scope baseline is present but whose
  `main()` body does not mention `_LIVE_LOG_BEFORE`, it reports FAIL.
  Red when: the arm asserts only the ordering, in which case a baseline that is never read passes.
- **AC3** — When the ordering arm is given a source whose `main()` still appends the guard's row
  under a conditional on the log path being set, it reports FAIL naming the surviving conditional.
  Red when: the arm checks only that the append exists, which both the correct build and the
  double-append build satisfy.
- **AC4** — When the state arm runs, it asserts `_build_live_log_row` returns state `skip` for an
  unresolvable repository, `ok` for equal digests, `ok` for a log absent at both readings, and
  `FAIL` for differing digests, and that the differing-digest detail contains both digest prefixes.
  The arm reports ok.
  Red when: the unresolvable input returns nothing or returns `ok`, which is the row that would
  announce a protected log where none was read.
- **AC5** — When the ordering arm is given a synthetic source containing none of the three anchors,
  it reports FAIL with a message naming an anchor — `_LIVE_LOG_BEFORE` or the decorator anchor —
  rather than an ordering complaint.
  Red when: the arm keeps a file-only default and the count assertions can only ever see this file.
  fixture: the synthetic source is a short string built inside the arm; no file is written.
- **AC6** — When the ordering arm runs against this file, it asserts the baseline anchor occurs
  exactly once, the `main()` anchor exactly once, and the decorator anchor at least once, and
  reports ok.
  figure: all three counts are DERIVED by the arm at run time. The counts in §4's table are PINNED,
  measured on the blob at BASE on 2026-09-28, and the arm does not read them.
  Red when: the arm asserts a count it hard-codes, which would pin a number that moves whenever an
  arm is added.
- **AC7** — When the suite is run, the row `the declared arm count matches its pin` reports ok with
  detail `73 == SELFTEST_ARMS`, and the row `the arm-count pin ends an unbroken provenance chain`
  reports ok.
  figure: 73 is PINNED here and DERIVED by that row's own detail at observation time. The summary
  line is deliberately not the instrument: it prints a count of check ROWS, which is 76 at BASE and
  78 after this unit, and it does not carry the declared arm count.
  Red when: an arm is defined but not added to `order`, which the arity assertion catches, or
  `SELFTEST_ARMS` is bumped without its provenance line, which `check_provenance_chain()` catches.
- **AC8** — When the docstrings of `test_the_live_log_baseline_is_taken_before_any_arm_runs` and
  `test_the_build_live_log_row_is_total_over_its_four_states` are read, each states that a behavioural
  test of its property would write to the real query log, and that this is why it reads source or
  calls `_build_live_log_row` directly.
  Red when: a docstring describes only what its arm does, leaving the next reader to re-derive why
  the obvious stronger test is absent and to write it.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test`

New arm: `tools/memory-recall/selftest.py` · the ordering arm's failing cases are four synthetic
sources — baseline indented inside `main()`, baseline unread by `main()`, a surviving conditional
append, and no anchor present — and the state arm's is a `_build_live_log_row` return whose state token or
detail is wrong for its input · the `SELFTEST_ARMS` pin moves 71 to 73 with its provenance line.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.
- rev-2 · 2026-09-28 · §1 · §2 S2 · §2 S3 · §2 S4 · §3 · §4 · §5 · AC1 · AC3 · AC4 · AC5 · AC6 ·
  folded the round-1 spec audit. §4 named the anchor bytes, which the draft left to the implementer:
  the bare `@check(` resolves to a docstring at line 145 and would have made the arm red against a
  correct file, the round's blocker. S2 made the source a parameter. A second arm and S4 came from
  unit 1's new `_build_live_log_row`, so the pin moves 71 to 73. AC6 read the count off the pin row
  instead of the summary line.
- rev-3 · 2026-09-28 · §2 S1 · §2 S3 · §3 · §4 · §5 · AC1 · AC3 · AC5 · AC6 · folded the round-2
  spec audit, whose subject was rev-2's own fold. S3 and rev-2's AC5 demanded opposite verdicts on
  the same observation and S3 named that criterion as its own observer, so an arm built to the pair
  could not exist; S3 is now about occurrence COUNTS and the offset assertion is gone. §4's offsets
  were measured in a CRLF working copy and labelled as measured at BASE, where the blob is LF and
  gives different numbers; the table now pins LINE numbers, which no read mode changes, and the
  offsets are gone from acceptance entirely. §4's relocation mechanism was rev-1 prose left standing
  under rev-2's anchoring and described a red that cannot happen; a relocated assignment is indented
  and reds through the count. The table's "unique today" cell for the `main()` anchor was false of
  the bare form, which occurs twice. AC3 is new: nothing in the set observed that `main()` appends
  the row unconditionally, and a build keeping the old conditional emits it twice and prints green.
  AC4 gains the both-digests clause. §3's two deferrals now name the backlog ids unit 3 writes.
- rev-4 · 2026-09-28 · §2 S4 · §4 · AC4 · the helper rename of unit 1 carried through here:
  the state arm drives `_build_live_log_row` and the ordering arm's source literal moves
  with it. Behaviour is unchanged.
- rev-5 · 2026-09-28 · §3 · §4 · AC3 · folded the closing diff review's BLOCKER. The append
  clause was three substring tests over `main()`'s raw text and greened on seven ways of
  disabling the guard, the original defect restored through `global` among them; only deletion
  redded, and every passing row printed a byte-identical detail. It is now an `ast` scan of
  `main()`'s direct body statements, so §3's blanket no-AST non-goal is amended to the ordering
  clause alone and §4 records why the first rejection was right for one half and wrong for the
  other. Observed: the new predicate passes the shipped file and reds all eight mutations,
  including a local-shadow case the old clause was never driven against. The state arm is
  renamed `test_the_live_log_verdict_is_total_over_its_states`; its previous name was an
  accident of the rev-4 blanket rename and said four states where there are five.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "capture a baseline hash of a file before a test suite
runs and compare it afterwards"` finds no existing seam fits for the ordering question: it ranks on
the name stem `run`, which its own header warns means only that the name is common.

The seam this unit extends is local and the probe does not index it: the suite already reads its own
source to grade what follows the `main()` definition, and `check_provenance_chain(src, pinned)`
already parses this file's comment block for the pin's history while taking its source as a
parameter so an arm can drive every failure direction. Both are source-text reads over this file
with no parser, which is the shape both new arms take, S2 included.

The occurrence census the rev-1 draft skipped is the table in §4. At rev-2 that census covered one
anchor and asserted "unique today" of a second without counting it; at rev-3 all three are counted,
in both the bare and the anchored form, on the blob rather than the working copy.

Recall terms used: selftest live query log byte-identical guard arm count pin provenance chain
memory-recall kit version staged break

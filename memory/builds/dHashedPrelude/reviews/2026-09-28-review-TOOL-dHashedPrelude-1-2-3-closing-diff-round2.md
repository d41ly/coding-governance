**Serves:** diff-review TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3

# dHashedPrelude — the closing diff review, ROUND 2: the fix itself

*Tier-2 adversarial review · 2026-09-28 · node d · ROUND 2 · subject: the ROUND-1 fix only, not the build.*

Reviewed range: `211d184dfc5397ceb800eb554d8d9e47f51ca6c5...86c636b4`

## Verdict: BLOCKED

Two routes restore the exact defect `TOOL-dHashedPrelude-1` was opened to close — the live-log guard
bracketing post-arm state against post-arm state and reporting `ok` forever — with the replacement
`ast` arm green and the leg exit 0. Both were driven against the shipped file in this round. The
round-1 BLOCKER is therefore narrowed rather than closed: the substring predicate greened on eight
disabling edits and the `ast` predicate greens on nine more, five of which end in a false `ok` or a
vanished row rather than an announced skip.

The structural move itself is the right one, and most of it holds: an aliased receiver, a walrus, a
conditional expression as the argument, and a `main` nested under a module-level `if` all red
correctly, which the substring version could not do. What ships broken is the scope of the
immutability claim, not the decision to make the claim structurally.

Separately, part (2) of the fix — the `(unreadable)` sentinel — is gated by nothing. Reverting it to
the pre-fix raising form leaves the suite green with a byte-identical detail string, measured.

## Review shape

Raw 33 · confirmed 30 · refuted 3 · unverified 0 · precision 0.91.

Adjudicated, stated both ways because the table below and the returned id list must agree:

| Severity | Items | Raw confirmed findings |
|---|---|---|
| BLOCKER | 2 | 2 |
| HIGH | 3 | 7 |
| MEDIUM | 8 | 18 |
| LOW | 1 | 3 |
| **Total** | **14** | **30** |

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates. No finder or verifier died, so a zero
count in this report is positive evidence of absence rather than an unexamined gap.

### How the code findings were adjudicated

Every code finding below was re-driven in this round rather than read. The ordering arm was extracted
from the shipped file by `ast`, its decorator stripped, and called with a mutated `src`; the state arm
and the two helpers were extracted the same way and driven with the producer swapped. The control
pair held throughout: the unmutated source greens, and `_LIVE_LOG_BEFORE = None` inside `main()` reds
with the arm's own message, so the harness is faithful and a GREEN below is the predicate's verdict
and not the harness's.

---

## BLOCKER 1 — an indirect rebind of `_LIVE_LOG_BEFORE` inside `main()` restores the original defect, arm green

`tools/memory-recall/selftest.py:2777-2783`

The ban sees only `ast.Global` and an `ast.Name` in `Store` context. A `globals()` subscript write is
neither: the `Store` node is an `ast.Subscript`, and the name appears only as a `Constant` string, so
no `Name` for `_LIVE_LOG_BEFORE` is ever in `Store` ctx.

Driven: `globals()['_LIVE_LOG_BEFORE'] = _derive_live_log_digest(_LIVE_LOG)` inserted immediately above
the append at line 2910 returns **GREEN**, with a detail byte-identical to the control's —
`1 unconditional append over ['_LIVE_LOG', '_LIVE_LOG_BEFORE']`. Runtime semantics confirmed
separately in isolation: a `globals()[k] = v` write inside a function IS seen by a later free-variable
read of `k` in the same call. So `main()` compares the post-arm digest against itself and the row
reports `ok` forever — the defect `TOOL-dHashedPrelude-1` closed, reachable again with both arms green.

The arm's own assertion message claims more than the predicate delivers: "main() assigns
`_LIVE_LOG_BEFORE`, so the value it compares is not the prelude's" is a claim about assignment, and
the enforcement behind it covers one spelling of assignment.

**Fix.** Inside the existing `ast.walk(fn)` loop, also refuse indirect module-state writes:

    assert not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in {"globals", "vars", "setattr", "exec", "eval"}), (...)

`main()` legitimately calls none of them, so a blanket ban costs nothing and needs no subscript
analysis.

**Left-shift gate.** The mutation set belongs in the repo, not in a commit message. Add a fixture
list of disabling edits beside the suite — one string per mutation, each applied to the shipped source
— and an arm that asserts the ordering arm REDS on every one of them. The arm that grades the guard
then has a guard of its own that fails when a route opens, instead of a prose count of mutations that
were driven once by hand. That also satisfies §7's "a new gate is not landed until its failing case
has been observed" for the predicate itself, permanently rather than at authoring time.

---

## BLOCKER 2 — a module-scope re-derive below the arms restores the original defect, arm green

`tools/memory-recall/selftest.py:2750` and `:2777`

The rebind scan is `ast.walk(fn)` over `main()` only, and the byte-anchor count at line 2727 pins the
single spelling `"\n_LIVE_LOG_BEFORE = "`. Anything that rebinds the baseline at module scope, after
the arms have run at decoration time, is outside both.

Driven, two spellings, both **GREEN**:

- `_LIVE_LOG_BEFORE=_derive_live_log_digest(_LIVE_LOG)` — no spaces, so the anchor count stays 1 —
  inserted immediately above `def main() -> int:`.
- `_LIVE_LOG_BEFORE, _spare = _derive_live_log_digest(_LIVE_LOG), None` in the same position.

Both keep `base < first` true, because the original assignment is still the first one. At runtime the
rebind executes at import, after every `@check` arm has already run, so `main()` reads a post-arm
baseline and the guard can only ever report `ok`. Same outcome as BLOCKER 1, one scope out.

**Fix.** Move the immutability claim onto the tree that is already parsed three lines below, and drop
the reliance on a byte spelling. Walk `tree.body` for every statement binding the name
`_LIVE_LOG_BEFORE` — `Assign` targets including `Tuple`, plus `AnnAssign`, `AugAssign`, `For`, `With` —
assert exactly one, and assert its `lineno` is below the `lineno` of the first `@check`-decorated
`FunctionDef`. That replaces the offset compare with the structural claim it was standing in for, and
makes the spelling irrelevant.

**Left-shift gate.** Same fixture-driven mutation arm as BLOCKER 1. Additionally: the offset compare
at 2733-2736 is the last text-search claim in this arm, and it is the one both blockers route around.
Converting it removes the class rather than the instance.

---

## HIGH 3 — the ban covers `_LIVE_LOG_BEFORE` but not `_LIVE_LOG`, so the guard becomes a permanent skip

`tools/memory-recall/selftest.py:2777-2783`

The two guarded lines sit in the same `ast.walk` loop and name one of the two symbols the adjacent
`names` assertion pins. The `names` check at 2773 compares identifier SPELLINGS, not bindings, so a
rebind of the first argument passes it.

Driven, both **GREEN** with the control's detail:

- `_LIVE_LOG = None` as a statement inside `main()`.
- `global _LIVE_LOG` plus the same assignment.

A third shape found in this round and not previously reported: `_checks = []` as a local at the top of
`main()` is **GREEN** too — the receiver itself is unguarded, and rebinding it discards every arm's
row, not just the guard's.

At runtime the local shadows the module value, `_build_live_log_row(None, <digest>)` returns at line
356 with `("skip", …, "the repository did not resolve, so nothing was bracketed")` — verified by
executing the shipped helpers directly — and `main()` computes `fails` from `FAIL` rows only (line
2941), so `return 1 if fails else 0` gives 0. The `memory-recall kit selftest` leg is
`python3 tools/memory-recall/selftest.py`, scored on exit code alone with no output parsing, so the
bar is green with the guard fully off, and the row states a reason that is false inside a resolvable
repository. That is §16's "a skip must announce itself" broken on the guard's own row: it announces a
skip, for the wrong reason.

Severity sits below the blockers only because a skip is visible in the summary's `, N skipped` note.
Nothing reads that note — grepped `tools/` for `checks passed`, no consumer outside the file.

**Fix.** Make the ban symmetric over the pair the row is built from:

    for bad in ("_LIVE_LOG", "_LIVE_LOG_BEFORE"):
        ... no ast.Global/ast.Nonlocal naming it, no ast.Name with that id in Store or Del ctx ...

and add `_checks` to the same set, since the receiver is as load-bearing as the arguments.

**Left-shift gate.** The fixture-driven mutation arm covers this too. Beyond it: `gate-legs.json`
carries no Python linter leg, so an F811-class redefinition or a shadowing local is ungated repo-wide.
A `pyflakes`-shaped leg over `tools/**/*.py` would catch the shadow class generically, and is cheap.

*(ids 2, 10, 25 — the same defect reported by three lenses.)*

---

## HIGH 4 — the append moved below `main()`'s `return` stays a direct body statement, so the row silently vanishes

`tools/memory-recall/selftest.py:2768`

The predicate asserts PRESENCE among direct body statements and says nothing about POSITION.
`_checks.append(_build_live_log_row(_LIVE_LOG, _LIVE_LOG_BEFORE))` relocated after
`return 1 if fails else 0` is unreachable dead code that `fn.body` still contains.

Driven: **GREEN**, detail byte-identical to the control. `ast` confirms the `Expr` is still a direct
body statement with the `Return` at a lower index, so `len(rows) == 1` holds and the args check passes.

At runtime the live-log row is never appended. The summary prints `len(_checks)` = 77 instead of 78,
and nothing pins that denominator: `assert len(order) == len(_checks)` at line 2890 runs BEFORE the
five run-property appends and counts declared arms only, and no gate leg or script outside
`selftest.py` reads the summary line. Green-by-absence on the guard's own row — the exact class this
build exists to close — restored inside the clause written to close it. The assertion message one line
below claims a totality it does not have: "a conditional, a try, a comment-out, a duplicate and a
deletion all land here".

**Fix.** Assert position as well as presence. Capture the append's index in `fn.body` alongside the
row, then `assert not any(isinstance(s, ast.Return) for s in fn.body[:idx])`. Two lines in the same
loop, and it makes "unconditional" mean "executed".

**Left-shift gate.** Pin the denominator. `SELFTEST_ARMS` pins the arm count; nothing pins the
run-property row count. Add a module constant for it and assert `len(_checks) == SELFTEST_ARMS +
SELFTEST_RUN_ROWS` before the print loop, with its own provenance line. A row that disappears then
reds on its own, without needing a predicate to anticipate the route.

---

## HIGH 5 — part (2) of the fix is ungated: reverting or mistyping the `(unreadable)` producer leaves the suite green

`tools/memory-recall/selftest.py:335-336`, asserted at `:2801`

The only unreadable input any arm supplies is the string literal on line 2801, handed in as `before`
next to `pathlib.Path(__file__)` — a file that exists and reads fine. That exercises the CONSUMER's
tuple-membership test at line 358 and never the producer's `except OSError` branch at 336.

Measured, three runs of the extracted state arm:

| producer | verdict | detail |
|---|---|---|
| shipped | GREEN | `skip / skip / ok / ok / FAIL, and the FAIL names both digests` |
| reverted to the pre-fix raising form | GREEN | byte-identical |
| sentinel typo'd to `(unreadble)` | GREEN | byte-identical |

So the sentinel's spelling, its deliberate distinctness from `(absent)`, and the no-raise property are
all unobserved. Delete part (2) of the fix and the suite stays green and the summary still reads 78/78.
This is the repo's own `a-double-you-wrote-grades-nothing` class and §7's "a new gate is not landed
until its failing case has been observed", inside the build that exists to close that class.

The typo case is the harmful one and is worth stating on its own: with a drifted producer literal, a
genuinely unreadable log falls through to the digest compare and the guard reports
`FAIL — the gate wrote to it: <hex> -> (unreadble)`. A false accusation of a write, on the guard's own
row. The sentinel is a bare literal written three times — producer at 336, consumer at 358, arm at
2801 — with nothing binding the three.

**Fix.** Drive the producer, and stop duplicating the literal.

1. Hoist `_UNREADABLE = "(unreadable)"` and `_ABSENT = "(absent)"` to module scope beside
   `_LIVE_LOG_ROW`, and use them in both functions and the arm.
2. A directory is portably present-but-unreadable. Confirmed on node `d` in this round:
   `pathlib.Path(tempfile.mkdtemp(...))` has `exists()` true and raises `PermissionError` from
   `read_bytes()`; POSIX raises `IsADirectoryError` or `PermissionError`. Both are `OSError`. Verified
   end to end against the shipped helpers: `_derive_live_log_digest(<dir>)` returns `'(unreadable)'`
   and `_build_live_log_row(<dir>, <hex>)` returns `skip`. The state arm already builds a tempdir at
   line 2804 — add the two assertions inside its existing `try`.

**Left-shift gate.** The second assertion above is itself the left-shift: it drives the producer and
the `after` side of the consumer in one call. Add the reverted-producer case to the mutation fixture
proposed under BLOCKER 1 so a future revert reds.

*(ids 17, 12, 32 — the producer's unreachability, the missing shared constant, and the sentinel's
drift risk are one defect with three faces.)*

---

## MEDIUM 6 — `next(...)` inspects the FIRST module-level `main`; Python binds the LAST, and a decorator replaces it

`tools/memory-recall/selftest.py:2750`

The arm asserts exactly one APPEND and never exactly one `main`. The `_ANCHOR_MAIN` count at 2727
pins `"\ndef main() -> int:"` — one annotation spelling of one signature — so anything with a
different signature is invisible to it.

Driven, three shapes, all **GREEN**:

- A second `def main(argv=None):` appended at module level above the `__main__` guard.
- `main = lambda: 0` after the def.
- A decorator (`@_swap`) on the real `main`, which the arm reads undecorated.

In each case `raise SystemExit(main())` at line 2949 resolves the LAST binding, the guard row is never
appended, and the arm certifies a function that does not run. The duplicated-definition shape is the
half-applied-merge signature specifically: a bad reconcile leaves exactly that behind.

No compensating control exists. The partition-based arm at line 2460 anchors on the same annotated
spelling, and `gate-legs.json` carries no Python linter, so an F811 redefinition is ungated here.

Ranked MEDIUM rather than HIGH because a merge-duplicated `def main() -> int:` with the identical
signature WOULD red on the anchor count; the routes above all require a deliberately different
signature. The inspection still targets the wrong node by construction.

**Fix.** Collect rather than `next`:

    mains = [n for n in tree.body
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "main"]
    assert len(mains) == 1, ...   # name the duplicate's lineno
    assert fn.decorator_list == [], ...

and additionally refuse a module-level `Assign`/`AnnAssign` storing the Name `main`. Including
`AsyncFunctionDef` also turns an `async def main` from a confusing anchor-count red into a named one.

**Left-shift gate.** A Python linter leg would catch the redefinition class generically, across the
whole kit rather than this one symbol. Without one, the `len(mains) == 1` assertion is the local
substitute and belongs in the mutation fixture.

*(ids 11, 19, 26.)*

---

## MEDIUM 7 — the fifth state is driven only through `before`; the `after` direction, which is the TOCTOU case the fix was written for, is undriven

`tools/memory-recall/selftest.py:2801`

Line 2801 passes a readable file as `live` and the sentinel as `before`, so `after` is always a real
digest. Measured: narrowing the guard at line 358 from `if "(unreadable)" in (before, after)` to
`if before == "(unreadable)"` leaves every assertion in that arm **GREEN** — the other four calls are
`(None, …)`, `(absent, absent)`, `(digest, same)` and `(digest, differing)`, none of which produces an
unreadable `after`.

Under that surviving mutation, a production run whose log becomes unreadable between the two readings
falls through to the digest compare. Measured directly: `_build_live_log_row(<dir>, <hex>)` under the
narrowed guard returns
`('FAIL', …, 'the gate wrote to it: aaaaaaaaaaaa -> (unreadable)')`. A false accusation of a write on
the guard's own row, and a contradiction of the fifth row spec 1 S2 now pins. Half the state this diff
added is a could-not-fail arm.

**Fix.** Covered by the second fix under HIGH 5 — `_build_live_log_row(<tempdir>, <hex baseline>)`
asserted to be `skip` drives the `after` end. The direction is drivable on both platforms, so this is
an omission and not a portability limit.

**Left-shift gate.** The mutation fixture again: a narrowed consumer guard is a one-line edit and
belongs in the same list as the reverted producer.

---

## MEDIUM 8 — the gate header gained no entry for the blind spot the new skip introduces

`tools/memory-recall/selftest.py:296-308`

The `WHAT THIS DOES NOT CHECK` block enumerates exactly four non-checks: a concurrent writer, the
cache tree, a log absent at both ends, a reverted write. The branch added at line 358 returns `skip`
whenever either endpoint is unreadable, which creates a fifth: an arm writes to the log and the log
then becomes unreadable before the compare, and the guard reports `skip` where the write earned a
`FAIL`.

Spec 1 S3 and AC3 both pin the list at four, and the acceptance ledger verifies exactly those four by
substring, so the header, its scope item and its acceptance all now describe a shorter list than the
code behaves by. §7 requires a gate's own header to state what it does not check, and this is the one
gate whose header is itself a graded artifact.

**Fix.** Add the fifth bullet — *A LOG UNREADABLE AT EITHER END. The compare is skipped, so a write
followed by a permission change or a lock is invisible.* — and lift spec 1 S3 and AC3 from four named
items to five, re-verifying the ledger's AC3 evidence.

**Left-shift gate.** AC3 is already graded by substring against the header's four items. Make the
grading predicate assert the COUNT of bullets in the block as well as their content, so a branch added
without a bullet reds instead of passing a subset match.

---

## MEDIUM 9 — spec 2 names the deleted symbol in three places, so AC8 binds a function that does not exist

`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md:36`, `:78`, `:229`

The rename to `test_the_live_log_verdict_is_total_over_its_states` landed in `selftest.py:2789`, in
`order` at 2888, in `memory/map/generated/symbols.json` (the old id was removed and the new one added,
verified in the diff) and in the acceptance ledger at line 64. It did not land in the spec that OWNS
the criterion.

Tree-wide grep: `test_the_build_live_log_row_is_total_over_its_four_states` survives only in spec 2 at
S4 (36), §4 Inventory (78) and AC8 (229), plus the round-1 review's own historical prose.

AC8 is the material one. It directs a reader to read the docstrings of two named arms; one of the two
names resolves to nothing, so the criterion cannot be executed as written. §9's rev-5 entry announces
the rename in the same file, which makes the spec self-contradicting rather than merely stale. The
round-1 review's Fix line at 226 told the fixer to standardise on the OLD spelling while the code went
the other way, which explains the split without excusing it.

Nothing gates it: the codebase-map ratchet grades `memory/map/features/` claims, not spec prose, and
the hygiene dead-path walk resolves cited PATHS, not function names.

**Fix.** Replace all three occurrences, then grep the build folder for the old stem and confirm only
the review records retain it. Add `§2 S4 · §4 · AC8` to spec 2's rev-5 entry, which currently claims
only `§3 · §4 · AC3`.

**Left-shift gate.** This is the gap the hygiene walk leaves. A spec-side symbol check is cheap and
generic: extract backticked `test_*` / `_*` identifiers from `memory/builds/**/spec/*.md` and assert
each resolves in `memory/map/generated/symbols.json`, with a declared exemption list for
historical citations in `reviews/`. That gates the CLASS — a record naming a symbol the tree no longer
has — rather than this rename.

*(ids 6, 14, 20, 30 — four lenses on one dead symbol.)*

---

## MEDIUM 10 — AC3 is false against the shipped predicate, and rev-5 claims an AC3 edit the diff does not contain

`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md:198-199` and `:272`

Verified in the commit: `git diff` on spec 2 contains hunks at the status header, the
`gen:spec-records` table, §3, §4's *Alternatives rejected* subsection and §9, and no hunk in §6 —
the diff does not contain the string `surviving conditional` at all. AC3 is byte-unchanged while §9's
rev-5 entry reads `§3 · §4 · AC3 · folded the closing diff review's BLOCKER`.

AC3 still requires the arm to report `FAIL naming the surviving conditional`. The shipped clause
emits ``{n} unconditional `_build_live_log_row` append(s) in main(), expected 1 — a conditional, a
try, a comment-out, a duplicate and a deletion all land here``. It names a count and a list of
candidate causes and identifies none of them, by construction: a direct-body scan cannot see what it
did not match. Confirmed in this round — the aliased-receiver, conditional-expression and walrus
mutations all produce that one byte-identical string.

So a CLOSED unit's acceptance criterion is unmet by its own code, while the changelog tells the next
reader the criterion was already revisited. A changelog that claims an edit it did not make is worse
than a stale criterion, because it stops the next reader from checking.

**Fix.** Rewrite AC3 to the property the predicate actually has — FAIL stating that `main()` holds N
unconditional appends where 1 is expected, distinguishing 0 from 2 — or make the message name the
offending statement's lineno and node type, which would let the old wording stand. Either way §9's
rev-5 entry must describe what was changed.

**Left-shift gate.** Gate the changelog against the diff. A `rev-N` entry names the sections it
amended; a check can assert that every section token in the newest entry corresponds to a hunk in the
commit that added it. That is the `amendment-leaves-its-other-half-standing` class, and it is
mechanically checkable at the pre-commit boundary where both halves are in hand.

*(ids 7, 27.)*

---

## MEDIUM 11 — the acceptance ledger quotes three verdict strings the shipped code can no longer emit

`memory/builds/dHashedPrelude/build/2026-09-28-build-TOOL-dHashedPrelude-1-1-acceptance-ledger.md:47-52`

- AC2's evidence quotes `main() does not read the module-scope baseline`.
- AC3's evidence quotes ``main() still guards the append with `if _LIVE_LOG is not None`; with the
  module-scope baseline in place that emits the row twice and both copies are green``.
- AC4's evidence quotes the return `skip / ok / ok / FAIL, and the FAIL names both digests`.

Measured: a grep over `tools/` for the first two returns nothing tracked — the only hit is a stale
untracked `__pycache__` blob. Both strings were deleted with the three substring clauses. The third is
dead too: line 2818 now returns `skip / skip / ok / ok / FAIL, and the FAIL names both digests`.

This is not defensible as frozen history. The same commit edited this very file's AC8 row to carry the
new arm name, so the ledger is maintained as a live record, and three of its rows were left quoting
output no run can reproduce. The build now carries recorded acceptance for criteria that no longer
correspond to any code.

**Fix.** Re-drive AC2, AC3 and AC4 against the new predicate and paste the strings it actually emits.
AC3's text needs MEDIUM 10's amendment first, or the re-driven evidence will contradict the criterion
it is filed under.

**Left-shift gate.** Same class as MEDIUM 9, different population. A ledger evidence line that quotes
a verdict string in backticks is an assertion about the tree; a check can extract quoted strings over
~40 characters from `**Evidences:**` blocks and assert each still occurs in the tracked source, with
an exemption marker for evidence that is deliberately historical. It would have caught all three here.

*(ids 13, 23.)*

---

## MEDIUM 12 — the fifth state has no acceptance criterion on either spec, and both state counts are stale

`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-1.md:27` and `:44`,
`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md:202`

The rev-5 hunk inserts the fifth S2 row — *log present but unreadable* — immediately above the
pre-existing sentence `Observed by AC2 and AC5`, so that clause now trails the new paragraph and
claims two observers for it. Neither observes it:

- Spec 1 AC2 (line 155) is about the `ok` row reporting the first twelve hex characters.
- Spec 1 AC5 (line 176) enumerates exactly three calls — the none-value, a nonexistent path with the
  absent sentinel, and two differing digests.
- Spec 2 AC4 (line 202) enumerates four returns and was not touched by rev-5.

Spec 1's rev-5 entry lists `§2 S2 · AC6` as its only edits, confirming AC5 was never amended. So the
one behaviour part (2) added is asserted in code at `selftest.py:2801` and observed by no criterion
anywhere. Combined with HIGH 5, nothing in code OR records would notice if the sentinel were deleted.

The count is stale alongside it: spec 1 line 27 opens S2 with `It is TOTAL over the four states`
directly above a table that now has five rows, and spec 2 carries the same figure at lines 37, 132,
163 and 175 (`four direct calls` — the arm now makes five).

Re-derived and correct, for contrast: 73 anchored `@check` decorators, `order` holds 73 elements,
`SELFTEST_ARMS = 73` at line 112, five direct `_checks.append` statements in `main()`'s body, summary
78. Every number this diff corrected checks out; the ones it missed are the state counts.

**Fix.** Extend spec 1 AC5 with the unreadable call and its `skip`, extend spec 2 AC4 to five states,
correct line 27 and spec 2 lines 37, 132, 163 and 175, and list `AC5` / `AC4` in the two rev-5 entries.

**Left-shift gate.** The `Observed by AC<n>` clauses are a machine-checkable link. A check can assert
that every scope item's cited AC exists and that no AC is cited by a scope item it does not mention —
the same both-directions discipline §7 already requires of a declared population. It would have caught
the fifth row inheriting a trailing sentence written for the four above it.

*(ids 8, 21, 28, 29.)*

---

## MEDIUM 13 — spec 2 §4 still describes the append clause as a source-text read

`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md:125` and `:132`

Verified against the commit: the only §4 hunk is at the *Alternatives rejected* subsection, twenty
lines further down. The *How each arm decides* paragraph is untouched and still reads
`The main() clauses read the source after the main() anchor. One asserts _LIVE_LOG_BEFORE appears
there`. The shipped arm does no such read: it parses the whole source, picks the module-level `main`
`FunctionDef`, and asserts on call arguments. `src.find(_ANCHOR_MAIN)` survives only to fill the
detail string.

Line 132 likewise still says `each of the four inputs. Two of the four states` where the arm now drives
five and its own `@check` title says five.

rev-5 claims `§4` amended, and it was — in a different subsection. §4 now carries two mutually
contradictory mechanism descriptions, and the stale one is the version the round-1 BLOCKER was raised
against. A reader reconstructing intent from the spec gets the implementation that was rejected.

**Fix.** Rewrite lines 125-131 to describe the `ast` scan of `main()`'s direct body statements, and
line 132 to five inputs and three unproducible states.

**Left-shift gate.** Not mechanically gateable as prose-versus-code, which is exactly why the
charter's rule is to point at the source rather than restate it. The durable fix is to shorten §4's
mechanism paragraph to a pointer at the arm's own comment block — the comment at `selftest.py:2740-2745`
already carries the rationale and cannot drift from the code it sits in.

---

## LOW 14 — seven `four states` statements survive the fifth state, two of them in the file this diff edited

`tools/memory-recall/selftest.py:347`, `:135`, `:2790`, `:2795`;
`memory/builds/dHashedPrelude/README.md:77`

- `_build_live_log_row`'s own docstring at 347: `so an arm can drive all four states. Two of them
  cannot be produced by running this suite` — five and three now, nine lines above the membership test
  the same diff added.
- The `SELFTEST_ARMS` provenance block at 135: `drives _build_live_log_row over all four of its
  states, two of which no run in this repo produces`. `check_provenance_chain()` matches only the
  `N -> M on <date>` lines, so this continuation prose is ungated and reads as authoritative.
- The state arm's own docstring at 2790 and 2795: `including two no run in this repo can produce` and
  `The fourth state is the one that used to emit NO ROW`.
- `README.md:77`, inside the authored `roster:units` region: `drives _build_live_log_row over its four
  states`, and it still describes the ordering arm as reding `when the append is still conditional` —
  a text-search description of an `ast` scan.

One function, two counts, one file. rev-5's stated reason for renaming the arm was that the old name
`said four states where there are five`; the same sentence was left standing in six other places.

**Fix.** Correct all five sites, or drop the count from the prose entirely and let the arm's own
derived detail (`skip / skip / ok / ok / FAIL`) carry it. The second is the charter's own preference —
no count of a derived population is written in prose.

**Left-shift gate.** §7's rule is already the gate: a number typed beside the thing it counts is wrong
on the next commit. A cheap generic check is a scan for small spelled-out cardinals adjacent to a
backticked identifier in `tools/` and `memory/builds/`, reported as a warning list rather than a red,
since the population is prose and a hard gate would be noisy. The stronger move is deletion.

*(ids 15, 24, 31.)*

---

## What was checked and found sound

Stated so the zero counts below are read as examined rather than unvisited — no lens or verifier died
this round, so absence here is evidence.

- **The structural move is correct where it is scoped correctly.** Four further mutations were driven
  in this round and all four RED: an aliased receiver (`_c = _checks`), a walrus in the append
  argument, a conditional expression as the argument, and `main` nested under a module-level `if`.
  The substring version could not have caught any of them.
- **The `ast.parse` introduces no new failure mode on the paths AC5 drives.** The `SyntaxError` handler
  at 2747 converts a parse failure into an `AssertionError` with the exception text, so a synthetic
  source that does not parse reds as a named assertion rather than an error. AC5's synthetic source
  (`nothing here at all\nnot one anchor`) reds earlier, on the anchor count, unchanged.
- **The non-UTF8 read is unchanged.** `errors="replace"` was already on the default read at 2722 and
  the diff did not touch it. A replacement character in the source would fail the parse, which the
  handler above names.
- **`ast.Name.ctx` and `ast.FunctionDef` are stable across supported versions.** The `AsyncFunctionDef`
  gap is real but it manifests as `fn is None` and a named assertion, not a silent pass; it is folded
  into MEDIUM 6's fix rather than reported separately.
- **The numbers this diff corrected are right.** 73 anchored `@check` decorators, `order` at 73,
  `SELFTEST_ARMS = 73`, five run-property rows, summary 78, and the symbols.json rename is complete in
  both directions. Re-derived independently in this round.

## Standing note on the leg that scores this

The `memory-recall kit selftest` leg is declared `chunk: selftests, subject: kit` in
`tools/gate-legs.json`, so it is HELD on a default bar and runs only under `GATE_SELFTESTS=1`. Every
"the arm greens and the bar stays green" statement above is therefore an understatement of exposure on
a default run, where the arm does not execute at all. That is the standing owner ruling and not a
finding; it is stated because the severity of a guard-of-the-guard defect reads differently once the
guard's own leg is opt-in.

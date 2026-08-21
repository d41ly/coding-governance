**Serves:** diff-review TOOL-dUnstalledConvoy-23 TOOL-dUnstalledConvoy-24 TOOL-dUnstalledConvoy-25

# Design review — the report pivot dissolves the stall and leaves the observability claim unfunded

**Reviewed range:** `6fcfe36...HEAD` (HEAD = `37abdf95`, 1 commit, 10 files, records + spec only). **ROUND: 1.**

## Verdict: BLOCKED

**Three blockers, six highs, six mediums, two lows.** This is the third adversarial pass over these
units. Round 1 (`2026-08-21-review-TOOL-dUnstalledConvoy-23-24-specs.md`) returned BLOCKED on a spec
written from review records rather than from the code. Round 2
(`2026-08-21-review-TOOL-dUnstalledConvoy-23-24-25-specs.md`) returned BLOCKED on a false claim about
`pass_commit`'s window and a spec-25 predicate that redded two-thirds of the corpus. This diff is
three specs, a gotcha record and the map bookkeeping — no product code — so every finding below is a
design defect: a scope item that cannot be built as written, an acceptance criterion a wrong
implementation also satisfies, or a claim about the base that is false.

**Both of round 2's headline blockers are genuinely closed.** The owner's resolution — check 23
becomes a REPORT that always runs and never fails the bar — dissolves the stall, the flip, the
rollback key and F1's entire dependency on the false in-band-exit sentence. rev-3 retracts that
sentence by name in the Goal. S3 now states the window's boundary and its ordering, and I traced arm
C under the inclusive upper bound: it survives. Spec 25 retires on its own measured dry-run rather
than on argument. That is three rounds of real repair, and it is worth saying before the list.

**What replaces them is a delivery class.** S1 routes check 23's entire output onto `report()`, which
is silent unless `GOV_UNATTENDED_REPORT=1`, and nothing in the shipped product sets it — not
`tools/gate-legs.json`, not `.githooks/pre-push`, not the driver, not the Skill, not the protocol.
Measured at `37abdf95`: the only setters in the tracked tree are inside `check-unattended.test.sh`.
So after S1, on every bar run, every pre-push run and every unattended run, check 23 emits zero
bytes. The accuracy work in S2–S6 and the arms in S9 land on output no operator receives, and §4's
"a report that is wrong is worse than no report, because it will be read" is false about the channel
S1 names. The unit that calls itself the observability change makes check 23
production-indistinguishable from a deleted check.

**And the left-shift that replaces retired spec 25 does not reach its own population.** Anchors in
`gotchas.py` are DERIVED from backticked path-like tokens in the body. The new record yields exactly
one — `lib-unattended.sh` — so it is selected by a diff touching one shell library and never by a
diff touching a spec. Measured on the commit that created it:
`python tools/memory-tree/gotchas.py --for-diff 6fcfe367..HEAD` prints `0 class(es) selected by an
anchor + 3 universal` over ten changed files, three of which are specs. Hygiene check 19 is green
anyway, because it only reds an empty or inert anchor set.

## Review shape

- **raw 42 · confirmed 30 · refuted 12 · unverified 0 · precision 0.71.**
- After dedupe the 30 confirmed collapse to **17 distinct defects: 3 BLOCKER, 6 HIGH, 6 MEDIUM, 2
  LOW.** Each section names the raw confirmed ids that reached it. Precision fell from 0.90 to 0.71
  across rounds, which is the expected shape over a target that has been hardened twice — §8's rule
  is that below ~0.5 you tighten scope before adding agents, and this is above it.
- Every code claim below was **re-verified against the tracked tree at `37abdf95`** before this
  report was written, not taken from the finder output: the report channel by reading
  `check-unattended.sh:211-218` and grepping every setter in the tree; the leg's wiring by reading
  `tools/gate-legs.json:578-586`; the fold and the no-commit branch by reading
  `check-unattended.sh:1090-1170`; `pass_commit` by reading `lib-unattended.sh:79-90`; the `drows`
  fixture and all sixteen check-23 assertions by reading `check-unattended.test.sh:1416-1613`; every
  `DISPATCH_GRADING` carrier by `git grep` over the tracked tree; the gotcha's reachability by
  RUNNING `gotchas.py --for-diff` and `--for-paths`; `BUILD-METHOD.md`'s generation by reading
  `adopt-memory-tree.sh:83` and `kit-dogfood-parity.test.sh:53`; and `grep -c`'s exit code by running
  it.
- **Not covered:** the full bar was not re-run. The diff is records-and-spec only and touches no
  gated artifact. That is an assumption, not an observation, and no finding below rests on it.

## Direct answers to the seven questions this review was asked

1. **Is the REPORT design buildable, and what happens to the exit status and the arms that assert
   check 23 FAILS?** The mechanism is buildable — `report()` exists at `check-unattended.sh:218` and
   behaves as S1 describes. The CHANNEL is not what S1 assumes: it is silent by default and no
   production caller opens it (**B1**). The exit status is fine, and AC9 pins it. Seven existing arms
   asserting fail text go RED the instant S1 lands, and nine `miss "check 23 FAILED"` assertions
   become permanently unfalsifiable — owned by no scope item (**H2**).
2. **Is `(own anchor, next anchor]` consistent with `pass_commit`'s exclusive lower bound?** The RULE
   is correct and nothing is double-graded: row 2's window opens after its own anchor, so a commit AT
   that anchor belongs to row 1 alone. Traced concretely on arm C below. The RATIONALE stated for it
   in §4 is inverted and argues for the exclusive bound the same paragraph rejects (**M1**). And one
   case goes ungraded in one row and mis-graded in another: a pass that commits AFTER the next anchor
   for the same unit (**M2**).
3. **Does deleting `DISPATCH_GRADING` break anything that reads it?** Not the adopter or its e2e arm
   — §5 says it does and that is false (**M5**). It does reach `kit.toml:38`'s `optional_keys` and
   `memory/guides/SESSION-KICKOFF.md:56`, neither of which any gate catches and neither of which any
   scope item or AC names (**H5**). The leg's two dark arms and the fixture's `DISPATCH_GRADING=1`
   also die and are named nowhere (**H2**).
4. **Does S2's union preserve arm C?** Yes, and I traced it. Arm C parks row 1 at `A0`, commits the
   offending `work/stray.txt` at `C1`, then parks row 2 at anchor `C1`. `pass_commit` skips the
   run-state-only declaration commit and returns `C1` for row 1. Under S3, row 1's window `(A0, C1]`
   contains `C1`; row 2's window `(C1, HEAD]` does not. So the union for `C1` is row 1's set alone,
   `work/one.txt`, and the finding survives. The inclusive upper bound is load-bearing here: under
   the exclusive reading round 2 traced, neither row owns `C1` and arm C flips green.
5. **Is spec 24's cross-tree read buildable, and do AC2 and AC3 distinguish?** Buildable —
   `runmd_of` (`unattended.sh:239`) and `fact` (`:246`) compose over `git worktree list --porcelain`,
   and the worktree-fixture precedent rev-3 now cites is real (`recall-opened.test.sh:100` does
   `git worktree add`). AC2 and AC3 DO discriminate as rewritten. §5 and F2 were not updated to match
   and now claim the negative arm pins a different state (**M6**).
6. **Which round-2 findings remain unaddressed?** Nine, tabulated at the end. Six are oversights, one
   (H1) is decided the other way without saying so, and two (H6, M2) are unowned for a third round.
7. **Did retiring spec 25 leave an AC depending on a gate that no longer exists?** Not in 23 or 24 —
   neither ever cited spec 25's gate. The damage is inside spec 25 itself: it retires on "a gotcha
   record and a documented check", the record landed, the documented check did not, and a WONTDO unit
   owes nothing to the ledger so nothing will ever land it (**H6**). The record that did land cannot
   reach a spec diff (**B3**).

---

# BLOCKERS

## B1 — S1 routes the whole unit onto a channel no production caller opens

*(raw confirmed ids 1, 35)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:20-23`, with the
claims that depend on it at `:57-58` (§4) and `:85-86` (§5).

`check-unattended.sh:217-218` reads:

```
REPORT=${GOV_UNATTENDED_REPORT:-0}
report() { [ "$REPORT" = 1 ] && printf 'unattended-report: %s\n' "$1"; return 0; }
```

The channel is silent at 0, and its own header at `:211-216` scopes it deliberately: "A check that
cannot compare says which arm went unexercised and why, and an operator asks for those by setting the
variable." That is a channel for SKIPS, not for comparison results.

Measured over the tracked tree at `37abdf95`, `GOV_UNATTENDED_REPORT` appears in exactly two files:
the definition and the comment in `check-unattended.sh`, and eight call sites inside
`check-unattended.test.sh`. Nothing else sets it. `tools/gate-legs.json:578-586` runs the leg as bare
argv with no env block. `.githooks/pre-push` adds none. The driver never invokes the leg.
`PROTOCOL.template.md` does not mention the flag at all, so an operator's only documentation for it
is a comment inside the script.

S1 deletes the `fail 23` branches and the dark announcement. After it, on the bar, at the push
boundary and inside an unattended run, check 23 produces **zero bytes whatever it finds**. §4's "a
report that is wrong is worse than no report, because it will be read" and §5's "this unit IS the
observability change" are both false about the channel S1 names, and §4:75-76's "It tells a reader
what a pass said versus what it did" names a reader the spec adds no scope item to create.

No acceptance criterion closes this. AC2, AC3, AC5 and AC6 are observed in
`check-unattended.test.sh`, which enables the channel itself; AC9 asserts exit 0; AC13 is the bar,
which prints nothing from this check either way. So the unit's entire deliverable is asserted only by
the fixture that turns on the mechanism under test.

One sub-claim in the raw finding is overstated and I am recording it rather than laundering it: the
dark announcement S1 deletes rides the SAME silent channel today, so no currently-visible output is
lost. That strengthens the point rather than weakening it — nothing production-visible changes in
either direction, which is what makes the check indistinguishable from a deleted one.

**Fix.** Make the channel an explicit S1 decision and pin it with an AC. Either (a) declare
`GOV_UNATTENDED_REPORT=1` on the `unattended kit gate` entry in `tools/gate-legs.json` so the bar
renders it and the per-leg log under `<git-dir>/gate-logs/` persists it, or (b) give check 23 its own
always-printed non-status prefix and amend the leg header's "Exit 0 + no output = clean / anything
printed is a violation" contract at `check-unattended.sh:6-13` in the same commit. Either choice must
reconcile `tools/unattended/cross-component.test.sh`, whose arm-3 and arm-3b assertions require the
leg's DEFAULT output to be exactly the empty string (`same "... output" "$out" ""`).

**Left-shift gate.** Add an AC observing a check-23 discrepancy in an invocation with **no
environment variable set** — the liveness assertion §7 demands, so a mechanism whose only witness is
its own fixture cannot ship. Generalise it as a leg: for every `report()` call site that reports a
COMPARISON RESULT rather than a skip, assert a production caller opens the channel. That is the
charter's "a probe that cannot move says so" applied to an output path instead of an input one.

## B2 — S2 never states the fold shape, and AC4 and AC2 then pin opposite implementations

*(raw confirmed ids 5, 23)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:24-27` (S2),
`:98-100` (AC2), `:103-105` (AC4).

S2 says the reported set is "the UNION of its rows whose window contains the commit" and stops. It
never says whether the fold MERGES same-anchor rows into one row, or emits every row and unions only
at the subset test. The two readings are not interchangeable, and each breaks a different criterion:

- **Merging fold.** `drows`' two same-anchor rows collapse to one, so AC4's "discards none, asserted
  by comparing the fold's row count against the file's" fails on the correct implementation.
- **Non-merging fold.** The `while IFS= read -r dsrow` loop at `check-unattended.sh:1130` runs once
  per row and emits TWO identical report lines for one pass, so AC2's "produces one naming the path"
  fails.

Neither AC names its fixture, so both are satisfiable by picking whichever fixture suits the half the
builder happened to read.

AC4 is worse than ambiguous: it observes nothing about this change at all. The fold key is
`<group> <unit>` and the group **is** the anchor sha — `unattended.sh:2318` parks `$grp $unit` where
`grp=$(GIT rev-parse --short=8 HEAD)`, and `check-unattended.sh:1131-1136` splits `dsgrp` back out and
feeds it to `pass_commit` as the anchor. So "one row per `(group, unit)` per distinct anchor" is a
restatement of the base behaviour at `check-unattended.sh:1121-1125`, where `row[k] = $0` only
overwrites on a key COLLISION. On a distinct-anchor fixture the criterion is green against the
untouched code and cannot enter AC12's red-first ledger — which claims without qualification that
every arm this unit adds was observed failing against the pre-fix code.

rev-2's AC3 at least scoped the probe to "a unit with rows at two anchors". rev-3 deleted that
qualifier, and the criterion became unsatisfiable alongside AC2. Round 2's H4 asked for the probe to
be deleted outright.

**Fix.** State the fold shape in S1 in one sentence — merged row, or per-row union at the subset test
— and name the consequence for the no-commit branch's path set, which is the second reader of that
value (see M3). Then **delete AC4's row-count probe** and re-aim AC4 at the property union actually
asserts: for a unit with two rows at one anchor, the graded set equals the union of both rows'
`reason` fields, observed by a commit touching a path present only in the FIRST row and asserted
silent, RED at base, with AC2 as its control. Move "distinct anchors are not folded together" into §3
as already-held.

**Left-shift gate.** A spec-time check that every acceptance criterion asserting a red-first ledger
entry names the fixture that produces the RED. AC12 currently makes a blanket claim over criteria
that cannot individually support it; requiring each criterion to carry its own red witness makes the
blanket claim derivable instead of asserted.

## B3 — The gotcha record replacing retired spec 25 cannot reach a spec diff

*(raw confirmed ids 20, 36)*

`memory/gotchas/spec-names-code-its-base-lacks.md:5,31` and the retirement that rests on it at
`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:46-48`.

Anchors are DERIVED, not declared: `tools/memory-tree/gotchas.py:176` harvests backticked tokens from
the body and `ANCHOR_RE` at `:49` requires a slash or a source extension. Run over this record, that
yields exactly `['lib-unattended.sh']`. Every other backticked token in it is an id, a short sha, or a
whitespace-bearing command line the regex cannot match. The front matter says `universal: false`.

Measured, on the commit that created the record:

```
$ python tools/memory-tree/gotchas.py --for-diff 6fcfe367..HEAD
# recurring-bug-class checklist for 6fcfe367..HEAD (10 changed file(s))
# 0 class(es) selected by an anchor + 3 universal
```

Ten changed files, three of them specs, and the record does not fire on its own creating commit. Same
result for `--for-paths` on spec 23 itself. `--for-paths tools/unattended/lib-unattended.sh` selects
it. So a class whose symptom, incident and both prescribed checks are entirely about SPEC authoring
and spec review reaches only a reviewer of one shell library.

Spec 25 §10 rests the whole retirement on "its existing `gotchas.py --for-diff` delivery, which
already hands a reviewer the classes their diff can hit". Measured, that delivery is inert for this
class. Hygiene check 19 (`gotchas.py:279-283`) is green regardless, because it only reds an EMPTY
anchor set or an INERT one, and `lib-unattended.sh` is a live tracked path — a green gate certifying
an unreachable record.

**Fix.** Either mark the record `universal: true`, which is what the class actually is — it is about
specs in any kit, not about the unattended kit — noting that `UNIVERSAL_BUDGET` in
`.memory-tree.conf` is 3 and three universals already exist, so the budget needs an owner decision;
or add a backticked token to the body that reaches the spec corpus (`memory/builds/` or the
spec-folder path shape) and re-run `gotchas.py --write`. Verify with `--for-paths` on a spec file
before landing. Then amend spec 25's AC1 from "recorded as a gotcha" to "recorded AND selected on a
spec diff, observed by `gotchas.py --for-paths <a spec>`" — existence is not delivery.

**Left-shift gate.** Extend hygiene check 19: a record's derived anchor set must SELECT at least one
file the record's own "Where it bit" section names. That converts "has an anchor" into "has the right
anchor", and it is exactly the charter's "a predicate that never matched its target population",
which this repo has now booked three times.

---

# HIGHS

## H1 — AC2 is satisfied by the existing nested `drows` fixture, so S2 ships unobserved

*(raw confirmed ids 6, 33)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:98-100`.

`drows` at `check-unattended.test.sh:1442-1447` parks both rows at one anchor, and every caller passes
a NESTED pair — arm A (`:1449-1454`) and arm B (`:1456-1462`) both use `work/one.txt` then
`work/one.txt work/two.txt`. Row 2 is a superset, so under the BASE last-wins fold the surviving row
already IS the union: arm A commits inside and is silent, arm B commits a stray and reports. Those
are AC2's two halves verbatim, satisfied with `row[k] = $0` untouched.

AC12's red-first ledger does not close the hole, because it binds "every arm ADDED by this unit" and
AC2 names no new arm. An implementer can cite the existing arms and S2 — the unit's central behaviour
— ships with nothing observing it. The only shape that distinguishes union from last-wins is the
NON-NESTED pair the spec's own §4 names at `:60-62` (`work/a` then `work/b`), and AC2 does not
require it. Round 2's H7 asked for exactly this and rev-3 did not take it.

This is `fixture-passes-by-finding-nothing`, which `gotchas.py` emits as a universal class for this
very diff.

**Fix.** Spell the fixture into AC2: row 1 `work/a`, row 2 `work/b` at one anchor; a commit touching
BOTH produces no report line (RED at base) and a commit touching `work/c` produces one naming it. Add
the sentence round 2 asked for: the existing nested `drows` callers cannot serve this criterion.

**Left-shift gate.** A review-time check, cheap and mechanical: for every AC claiming to observe new
behaviour, run the named observation against the PRE-fix tree and require it to fail. AC12 already
demands the artifact; what is missing is that the artifact be produced per-criterion rather than
claimed in aggregate.

## H2 — Converting `fail` to `report` breaks 7 existing arms and silently disarms 9 more, owned by no scope item

*(raw confirmed id 21)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:40-42` (S9) and
`:121-123` (AC12), both of which cover only arms this unit ADDS.

`fail()` at `check-unattended.sh:57` prints unconditionally. The suite's `run()` at
`check-unattended.test.sh:163` is a bare `bash "$SCRIPT" 2>&1` with no environment. So:

- **Seven arms go RED the moment S1 lands** — `:1434`, `:1462`, `:1472`, `:1495`, `:1522`, `:1543`,
  `:1560`, each asserting check-23 failure text through `run()`. This half is self-correcting via
  AC13.
- **Nine `miss "check 23 FAILED"` assertions become permanently unfalsifiable** — `:1427`, `:1454`,
  `:1484`, `:1515`, `:1529`, `:1537`, `:1571`, `:1580`, `:1607` — because no code path can emit that
  string any more. This half is NOT self-correcting. It is green-by-absence, the exact shape this leg
  has already redded for twice.
- The two DARK arms at `:1593-1612` and the fixture's `DISPATCH_GRADING=1` at `:79`, plus the two
  `sed -i '/^DISPATCH_GRADING=/d'` edits at `:1602` and `:1610`, become dead. AC1's grep enumeration
  excludes the test file, so no criterion names any of them.

**Fix.** Add a scope item: every existing check-23 arm is re-aimed at the report channel or retired;
the two DARK arms and the fixture key are deleted; and each `miss "check 23 FAILED"` is replaced with
a `miss` over the report line's own text so the negative controls stay falsifiable. Add an AC
asserting `grep -c 'check 23 FAILED' tools/unattended/check-unattended.test.sh` is 0 after the unit,
and state the arm count the unit converts so AC12's ledger can be checked against it.

**Left-shift gate.** A leg over the unattended suite: every `miss` assertion's needle must appear
somewhere in `check-unattended.sh`. A negative control whose needle no longer exists in the subject is
not a control, and this is mechanically checkable in one grep loop.

## H3 — S7 asserts "BOTH carriers" of the orphaned widening prose; there are five, and the two it omits are the binding contract and its installed twin

*(raw confirmed ids 8, 38)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:35-37`.

`tools/unattended/PROTOCOL.template.md:354-361` still states all three of:

- "A re-declaration of a pass that is still OPEN widens or no-ops; it never narrows"
- "a narrowing is a strict subset and always overlaps, so it is still refused"
- "A new pass whose set PARTLY overlaps its predecessor is read as a narrowing and refused"

All three are false at base. `unattended.sh:2407-2423` says so in capitals: "THE RE-DECLARATION AND
WIDENING MACHINERY IS GONE ... There is no narrowing refusal", and the code path is now an
unconditional `park`.

`memory/guides/UNATTENDED-PROTOCOL.md` carries the identical bytes — I diffed the pair and they are
identical modulo the path prefix — and check 10 (`check-unattended.sh:645-657`) byte-diffs them, so
the two move together or the bar reds. Check 10 is green whatever they SAY, as its own sibling
check-16 comment admits.

That is five carriers, not two: `unattended.sh:2397`, `check-unattended.sh:1090-1101`,
`PROTOCOL.template.md:354-361`, `memory/guides/UNATTENDED-PROTOCOL.md:354-361`, and
`check-unattended.test.sh:1431-1437`. §5's help/docs bullet reaches the protocol only for its KEY
TABLE, and §3 lists no exclusion covering stale prose, so the omission is not a recorded decision.

This matters beyond tidiness. AGENTS.md names the protocol the binding contract and forbids
paraphrasing it precisely so one answer exists. A run that obeys the stale paragraph declares only the
NEW paths at a new anchor — which under S2 and S3 is a row whose window excludes the commit that used
the old paths, producing a report line for doing what the contract said. Round 2's M2 raised this;
rev-3 did not take it.

**Fix.** Add the protocol pair and the test-file block to S7, and replace the paragraph with what is
true at base: rows are append-only, each stands on its own, nothing supersedes or retracts, a pass
needing more paths declares again at the current anchor, and the leg grades each row inside its own
window. Extend AC10 to observe it.

**Left-shift gate.** Wire the retired vocabulary into the leg's own phrase scan: a tree-wide
`! grep -q` over `RE-DECLARATION RULE`, `widening repair`, `supersedes an OPEN pass`, `never narrows`,
`is read as a narrowing`. This is the "delete the prose in the same commit as the machinery" half of
the new gotcha record, made mechanical for the one class that has now caused two spec revisions.

## H4 — AC10's second grep target is vacuous, and rev-3 dropped the live clause rev-2 had

*(raw confirmed ids 7, 34)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:116-117`.

Measured over the tracked tree: `RE-DECLARATION RULE` occurs **once**, at `unattended.sh:2397`, and
**zero** times in `check-unattended.sh`. So half of AC10 is already green at base and would stay green
if S7's second deletion were skipped entirely.

The prose S7 actually targets in that file is `check-unattended.sh:1090-1101` — "ONE ROW PER (group,
unit) — THE LAST. The driver's widening repair supersedes an OPEN pass's row and parks the replacement
AT THE SAME ANCHOR ... the later one is the one that binds" — which after S2's union fold would sit
directly above code contradicting it, the exact defect S7 exists to remove. That block contains no
occurrence of AC10's needle.

Worse, rev-2's AC8 also asserted "the library header no longer names a re-declaration caller". rev-3
deleted that clause. `lib-unattended.sh:69` still reads "condition 1, the driver's re-declaration
rule, and the leg's write-set grading" — and this diff's own gotcha record cites that exact line at
`:30-31` as one of the two carriers that produced rev-1's false mental model. A vacuous criterion
replaced a live one.

**Fix.** Restore `lib-unattended.sh:69` to S7 as a third carrier. Re-aim AC10 at each carrier's own
text: `! grep -q 'RE-DECLARATION RULE' tools/unattended/unattended.sh`,
`! grep -q "driver's re-declaration rule" tools/unattended/lib-unattended.sh`, and a string actually
present in `check-unattended.sh:1090-1101` such as `widening repair supersedes`.

**Left-shift gate.** Same phrase scan as H3 — one leg closes both, and it is the only form that gates
the CLASS rather than the three instances currently known.

## H5 — AC1's carrier list misses the two `DISPATCH_GRADING` carriers no gate can catch, and names the only reader by an undefined word

*(raw confirmed ids 4, 11, 24, 39, and the second half of 40)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:96-97` (AC1),
`:20-23` (S1), `:91-92` (§5 docs bullet) — all three enumerate the same four things.

`git grep DISPATCH_GRADING` over the tracked tree at `37abdf95` finds eight files:

| Carrier | Gated by |
|---|---|
| `.unattended.conf:132,144` | manifest `watch:` list, stamp only |
| `tools/unattended/.unattended.conf.example:113,125` | the leg's conf-parity checks |
| `tools/unattended/check-unattended.sh:1115,1117` | the sole READER |
| `tools/unattended/check-unattended.test.sh:79,1602,1610` | nothing (see H2) |
| `tools/unattended/PROTOCOL.template.md:387` | check 10 byte-diff |
| `memory/guides/UNATTENDED-PROTOCOL.md:387` | check 10 byte-diff |
| `tools/unattended/kit.toml:38` | **nothing** |
| `memory/guides/SESSION-KICKOFF.md:56` | **nothing** |

Two of the eight are gated by nothing at all, and both are omitted from all three enumerations.

- **`kit.toml:38`** lists `DISPATCH_GRADING` in `optional_keys`. Repo-wide, `optional_keys` is read at
  exactly one site — `tools/govkit/govkit.py:711` — and only to resolve `requires_if` condition keys.
  Nothing asserts a declared key still exists. The one arm over conf keys,
  `unattended.test.sh:1282-1288`, derives its population from `.unattended.conf.example` and `continue`s
  on any key the DRIVER does not reference; `DISPATCH_GRADING` is read only by the leg, so it is
  skipped there too. The kit descriptor — the declared population an adopter reads to learn the conf
  surface — would keep advertising a key the engine no longer reads, green forever. That is the
  charter's "an exemption naming a path that no longer exists reds too, because a stale one silently
  widens the surface it was written to narrow", landing in the descriptor that is supposed to BE the
  declaration.
- **`SESSION-KICKOFF.md:54-58`** is the manifest every session front-loads. It states the grading
  "ships DARK behind `DISPATCH_GRADING` ... and the leg says so on any run carrying dispatch rows"
  and closes "do not treat a green leg as a disjointness proof". After S1 all three sentences are
  false about a key that no longer exists. `.unattended.conf` IS in the manifest's `watch:` list
  (`SESSION-KICKOFF.md:6`), so §1's DoD forces a `last-audit` re-stamp — but `manifest-check.sh` C5
  is satisfied by the re-stamp alone and never reads the body, and C9 forces a body revision only
  after ten or more watched commits. The false prose survives a green ratchet.

Separately, `grep -c DISPATCH_GRADING tools/unattended/unattended.sh` is **0**, so AC1's "the engine"
cannot mean the driver — and the sole reader, `check-unattended.sh`, is named nowhere in S1, §5 or
AC1. Round 2's M2 caught the same shape as "the driver's own rationale block".

**Fix.** Replace the four-file list in all three places with one tree-wide observation:
`git grep -l DISPATCH_GRADING -- ':!memory/builds' ':!memory/backlog'` returns nothing. That covers
`kit.toml`, `SESSION-KICKOFF.md` and the test suite in a single predicate and cannot be enumerated
wrong. Replace "the engine" with `tools/unattended/check-unattended.sh`. Re-stamp the manifest's
`last-audit` with a delta line, and rewrite its paragraph to what will be true: declarations are
recorded, the comparison is a REPORT that never fails the bar, and the output channel is whatever B1
resolves.

**Left-shift gate.** A govkit leg asserting every key in a kit's `required_keys_*` / `optional_keys` /
`conditional_keys` is read by at least one tracked file in that kit. That is the declared-population
rule in both directions, and it currently runs in neither.

## H6 — Spec 25's AC2 is unmet, unowned, and names a generated file

*(raw confirmed ids 15, 25, 37)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:56-57`, against
`:22` (§2 Scope) and `:60` (§7 Gates).

Spec 25 retires on §4:46-48: "The repo's sanctioned answer for an ungateable class is a gotcha record
and a documented check, which is what replaces this unit." AC1's half landed —
`memory/gotchas/spec-names-code-its-base-lacks.md` is in this diff. **AC2's half did not.**
`git diff --name-only 6fcfe367..HEAD` does not list `memory/guides/BUILD-METHOD.md`, and grepping that
file for a base-verification instruction returns nothing.

Three problems compound:

1. **Nothing will ever land it.** A WONTDO unit owes nothing to the ledger —
   `check-memory-hygiene.test.sh` case 74 pins "WONTDO owes nothing — a retired unit built nothing" —
   so no future pass picks AC2 up. The README units table has 23 and 24 SPECCED and 25 WONTDO, and no
   other spec in the folder names this edit. Charter §7's left-shift is half-executed with the owning
   unit closed.
2. **The named file is generated.** `tools/memory-tree/adopt-memory-tree.sh:83` renders
   `memory/guides/BUILD-METHOD.md` from `tools/memory-tree/BUILD-METHOD.template.md`, and
   `tools/memory-tree/kit-dogfood-parity.test.sh:53` carries the pair in `PAIRS` and byte-compares it,
   wired as the "kit/dogfood doc parity" leg at `tools/gate-legs.json:232`. Editing only the file AC2
   names **reds the bar**.
3. **§2 says "Nothing. The unit is retired before any code" and §7 says Gates: "None".** With AC2
   live, all three cannot hold.

The hygiene gate cannot catch this: check 12 only requires each acceptance bullet to carry a
backticked witness, which AC2 does, so a witness path whose CONTENT is absent passes green.

Worth flagging as cost rather than as a defect: `BUILD-METHOD.md` is at 289 lines / 21062 B against
M1's stated 290 / 22528 — one line of headroom — and M3 veto 2 makes the budget an owner turn. The
unowned obligation is also the expensive one.

**Fix.** Land AC2 in this diff: one sentence in `tools/memory-tree/BUILD-METHOD.template.md`'s M2 spec
step — open the code at the BASE you are pinning, `git show <base>:<path>`, and read the function you
are scoping — plus the re-render, observed by `bash tools/memory-tree/kit-dogfood-parity.test.sh`.
Change §2 from "Nothing" to that one doc edit and §7 from "None" to the parity leg, so the
retirement's deliverable sits inside a gated scope. Otherwise delete AC2 and say in §4 that the
review-time delivery is the whole replacement — which then requires B3 to be fixed first, or the
replacement is nothing at all.

**Left-shift gate.** Extend hygiene check 12: for a `WONTDO` unit, every acceptance criterion must be
satisfied IN the retiring commit or explicitly reassigned to a named live unit. A retired unit that
leaves an open obligation has no owner by construction, and that is checkable from the status header
plus the diff.

---

# MEDIUMS

## M1 — §4's rationale for the inclusive upper bound states the opposite of what `pass_commit` does

*(raw confirmed id 9)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:66-69`.

The sentence reads: "the inclusive upper bound is chosen because a commit AT the next anchor is the
next pass's first commit under `pass_commit`'s exclusive lower bound, and the two must not both
disown it."

`pass_commit` opens `"$_pa..HEAD"` (`lib-unattended.sh:84`), which EXCLUDES `_pa`. A commit AT the
next anchor is therefore precisely **not** in the next row's window — which is exactly why the
previous row must own it. The sentence asserts the opposite. It is also self-contradictory: if the
next row owned that commit, there would be nothing for "the two must not both disown it" to guard
against, and disowning is the actual (correct) reason for the inclusive bound.

The RULE in S3 is right. Only its stated reason is inverted — but this spec has now lost two revisions
to false claims about this exact function's window, and a reviewer already traced the exclusive
reading flipping arm C from RED to green. A rationale that argues for the bound its own paragraph
rejects is not a harmless wording slip here.

**Fix.** Restate: `pass_commit`'s window excludes its own anchor, so the LATER row can never grade a
commit at that anchor; the earlier row must, or no row does — which is why the upper bound is
inclusive.

**Left-shift gate.** Not gateable; it is prose semantics. Route it into the new gotcha record's
review-time check, which already says to grep the co-named file at the declared base — extend it to
"and read the window/boundary of any function the spec's rationale characterises". This spec is three
for three on that class.

## M2 — S3's window re-attributes a pass that commits AFTER the next anchor, producing two false report lines

*(raw confirmed id 10)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:28-30`.

Condition 1 skips a unit's own rows on the unit token alone (`unattended.sh:2384`:
`case "$sib" in *" $unit · reason "*) continue`), so a unit can be dispatched into a second group while
its first pass is still open. `cross-component.test.sh:107-118` drives exactly that: `--writes work/spec`
then `--writes work/build` across a commit.

Now add the first pass's commit AFTER the second anchor, which is what AC11 requires of arm 3b ("arm
3b commits for at least one pass"). Trace:

- Row 1 anchor `A0`, row 2 anchor `A1`. Row 1's window under S3 is `(A0, A1]`, which holds only the
  declaration bookkeeping commit — and `pass_commit` skips run-state-only commits
  (`lib-unattended.sh:85-87`). So row 1 falls to the no-commit branch and reports "a pass that
  produced no change".
- The late commit lands in row 2's window `(A1, HEAD]`, names the same unit, and is graded against row
  2's `work/build` while it actually wrote `work/spec` — "committed a path outside the set it
  declared".

That is precisely the mis-attribution `check-unattended.sh:1094-1099` says the `(group, unit)` key
exists to prevent — "graded one pass's commit against another pass's declaration, and left the second
pass ungraded entirely" — re-introduced by the window rule. Under S1 it is a false REPORT rather than
a red, and the spec's own premise at §4:57 is that a wrong report is worse than none.

**Fix.** Say what happens when a row's window closes with no commit for that unit while a later commit
names it: either fall back to the unbounded search and report the ambiguity, or list the case in §3
with a reason. Add the arm to AC5's boundary pair. Do not let AC11's arm-3b change be the first place
this state appears.

**Left-shift gate.** An arm in `cross-component.test.sh` alongside 3b: one unit, two anchors, the first
pass committing after the second anchor, asserting whichever verdict the design chooses. The class is
"a windowing rule that partitions commits must be shown to partition them" — a boundary arm per edge,
which AC5 already half-asks for.

## M3 — S4 bounds the no-commit branch's WINDOW but never says which path SET it probes

*(raw confirmed id 14)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:31-32`.

The fold at `check-unattended.sh:1121-1125` feeds two consumers. The second is the no-commit branch at
`:1153-1160`, which iterates `for dsp in $dsdecl` and runs `GIT log "$dsgrp"..HEAD -- "$dsp"` looking
for a commit by ANY author.

S2 defines the reported set as the union of rows "whose window contains the commit" — a clause with no
referent when there is no commit. S4 fixes only the window. Both readings are broken:

- **Read as union**, merging same-anchor rows enlarges `$dsdecl`. The driver explicitly permits a
  narrowing re-declaration (`unattended.sh:2422`: "There is no narrowing refusal"), so under union that
  narrowing can no longer take effect: an unrelated commit touching the abandoned path fires "a
  declared path of a dispatched pass moved ... while no commit names that pass", naming a path the pass
  disowned.
- **Read as empty**, the branch scans nothing and is silently disabled.

Round 2's H8 asked for the path-set half; rev-3 answered only the window half.

**Fix.** State in S1 or S4 which set the no-commit branch uses and why. Add the arm: two same-anchor
rows narrowing from `work/a work/b` to `work/a`, an unrelated commit touching `work/b`, asserting the
intended verdict.

**Left-shift gate.** Fold into B2's fix — one sentence naming the fold shape settles both consumers.
The gateable form is an AC per CONSUMER of a shared derived value, which is generalisable: when a spec
changes how a value is computed, every reader of that value needs a criterion.

## M4 — The "what this unit does NOT buy" paragraph discloses a different evasion from the one the design blesses

*(raw confirmed id 13)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:74-76`.

Two `--dispatch` calls at an unmoved HEAD park two rows under one key, and the driver parks a fresh row
on every call with no narrowing refusal. So a pass that has ALREADY written outside its lane and not
yet committed can declare the path it wrote and have the union cover it — and AC2 requires exactly that
shape to produce no report line. A silent report therefore proves "declared before COMMIT", never
"declared before WRITE".

The disclosure paragraph, whose stated purpose is that "a green report is not over-read", names only
the up-front-wide declaration. Its closing sentence — "It tells a reader what a pass said versus what
it did" — asserts the ordering the design does not buy. The generic hedge "two artifacts the run itself
authored" gestures at it without disclosing it. S2 addresses only the later-anchor direction.

Because S1 makes this a report that is READ rather than enforced, this paragraph is the only control on
over-reading it. Round 1's D4 asked for the negative control by name and round 2's H1 repeated it.

**Fix.** Add one sentence to §4: a re-declaration at the SAME anchor widens the graded set
retroactively, so the report cannot distinguish a sanctioned repair from a write laundered before
commit. Then add the D4 arm beside AC2 in the same fixture — declare narrow, write out of lane,
re-declare wide at the unmoved anchor, commit — asserting whichever verdict the design chooses.

**Left-shift gate.** Not a code gate. The documented check is §8's own rule applied to spec prose: a
"what this does not buy" section must name every evasion the design's own acceptance criteria
explicitly permit. Add it to the review checklist beside the base-verification check.

## M5 — §5's "deleting `DISPATCH_GRADING` touches the adopter and its e2e arm" is false at the declared base

*(raw confirmed id 12, first half of 40)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:87-88`.

Measured: `grep -c DISPATCH_GRADING` returns **0** for `tools/unattended/adopt-unattended.sh`, **0**
for `tools/unattended/adopt-unattended.test.sh` and **0** for `tools/unattended/cross-component.test.sh`.
The adopter requires a pre-existing `.unattended.conf` (`adopt-unattended.sh:114-115`), renders the
Skill from `SKILL.template.md` and copies the protocol/playbook templates; `SKILL.template.md` carries
no such key. The e2e writes its own conf inline at `adopt-unattended.test.sh:32-48` with no
`DISPATCH_GRADING` line, and its protocol assertion pins an unrelated sentence.

So a builder sizing the change from this bullet hunts for an adopter edit that does not exist, while
the two carriers that DO need editing and are gated by nothing (H5) are named nowhere. This is a fresh
unverified base assertion in §5 — the same section round 2 already flagged for carrying this diff's
false base claims, and the exact class this diff's own new gotcha record describes.

**Fix.** Replace the bullet with the measured carrier set: the leg (`check-unattended.sh:1115-1120`)
and its arms (`check-unattended.test.sh:79,1593-1612`), both confs, the shipped example, `kit.toml:38`,
the protocol pair and `memory/guides/SESSION-KICKOFF.md`. Drop the adopter.

**Left-shift gate.** Same as B3's: the base-verification check, made reachable. This finding IS the
class the gotcha record describes, appearing in the same commit that files the record — which is the
strongest available argument that the record needs to be selectable on a spec diff.

## M6 — Spec 24 §5 and F2 both claim AC3 pins a state rev-3's own AC3 moved away from

*(raw confirmed ids 27, 42)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-24.md:70-71` (§5) and
`:106-108` (F2), against `:85-89` (AC3).

§5's error-states bullet enumerates three fall-backs — no other worktrees, a tree with no run-state
file for this slug, an unreadable one — and asserts "S3's negative arm pins the first". F2 repeats it:
"A single-tree run enumerates one worktree and falls straight to today's message, which AC3 pins."

AC3 as rewritten in this diff reads "tied to AC2's fixture, differing only in whether the second tree
holds `LANDING`" — which REQUIRES a second worktree and therefore pins the wrong-phase case, none of
the three listed states. The rewrite is correct and is round 2's M1 fix, properly taken; the two prose
sentences are the stale half. `git show 6fcfe367:...-24.md` confirms the §5 sentence is byte-identical
to rev-2's while AC3 moved.

A builder following §5 writes the zero-other-trees fixture, which passes on fixed and unfixed code
alike — this repo's own booked `fixture-passes-by-finding-nothing` class. And all three listed
fall-backs plus a fourth are now pinned by nothing: the fourth is a foreign worktree whose own
`.unattended.conf` declares a different `MEMORY_ROOT`, missed silently because `M` is read from THIS
tree (`unattended.sh:82,90`). Round 2 raised that fourth case and rev-3 did not add it.

In a single-tree run — the common case — the untested path is the one every ordinary invocation takes.

**Fix.** Rewrite the §5 bullet and F2 to match AC3: the negative arm is a second worktree present with
a non-`LANDING` phase. Add a third arm for zero other worktrees and a fourth for a second tree whose
run-state file is absent or unreadable, all asserting today's message verbatim. Add the differing-
`MEMORY_ROOT` case as a fifth fall-back. Three or four cheap arms over one fixture, differing by one
input each.

**Left-shift gate.** A spec-review check, mechanical enough to be worth writing down: every state a
production-readiness checklist ENUMERATES must be named by an acceptance criterion, or explicitly
listed as unpinned with a reason. §5 enumerating three and AC pinning one is the detectable shape.

---

# LOWS

## L1 — `grep -c` is named as the predicate twice, and it exits non-zero on the outcome both criteria assert

*(raw confirmed id 41)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:96` (AC1) and `:116`
(AC10).

Verified in this tree: `grep -c ZZZNOPE tools/unattended/kit.toml` prints `0` and exits rc=1. Both
criteria assert the count is 0, so in both the PASS outcome is the non-zero-exit case and fails any
`&&` chain an arm wires it into. That is charter §14's booked class verbatim: "a no-match grep exits
non-zero and fails `&&` chains — a PASSING zero-count check reads as failure."

The builder either sees a false red or defuses it with `|| true`, after which the assertion cannot fail
in either direction. rev-2 carried one instance (its AC8); rev-3 renumbered it to AC10 and added a
second at AC1, so the unaddressed finding doubled. Round 2's L1 said exactly this.

**Fix.** State both as `! grep -q ...`, or `git grep -q ... ; test $? -eq 1`, so the exit code and the
verdict agree.

**Left-shift gate.** A spec-lint one-liner over acceptance criteria: flag `grep -c` naming an expected
count of 0. Cheap, unambiguous, and it is the third time this exact shape has been filed in this build.

## L2 — The driver-side never-closing sibling row is in neither §2 nor §3 for a third revision

*(raw confirmed id 16)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:44-53` (§3, where it
is absent).

`sibrows` (`unattended.sh:2331-2352`) calls `pass_commit`, which returns only its FIRST candidate commit
(`lib-unattended.sh:82-88`), tests that one commit against the row's declared set, and keeps the row
OPEN when nothing overlaps. Condition 1 (`:2378-2391`) then refuses any other unit declaring an
overlapping path with `fail 49 ... also in <who>`, on an append-only record with no retraction and no
owner turn to clear it — terminal in an unattended run, which is the class this build exists to remove.

Concretely: unit A declares `work/one` at `A0`, declares `work/one work/two` later, then commits only
`work/two/y.txt`. Row 1 is OPEN forever and unit B declaring `work/one` is refused for the rest of the
run.

§3 waives condition 1's REFUSALS, `pass_commit`'s permissiveness and the overlap gate by name, but
never the OPENNESS computation that makes the refusal permanent. So a reader of the non-goals is not
told this known stall survives. The same trace is already recorded at
`reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-round3-fix.md:219-228` and in both prior spec
reviews. Round 1's D2, round 2's H6 and round 4's D5 all named it.

Low severity as scoped — it is a disclosure gap, not a wrong instruction — but unowned for a third
revision.

**Fix.** List it in §3 with a reason and the unit that will own it, or take it IN with a driver-only
scan-forward, set-filtered predicate and its own criterion. Silence is what has lost it three times.

**Left-shift gate.** Not a code gate; a spec-review rule. A known terminal-stall class named in a prior
review of the same build must appear in §2 or §3 of the next revision. That is checkable by a human in
one pass against the prior report and is the cheapest possible fix for a defect now on its fourth
appearance.

---

# Round 2 carry-forward

Nineteen findings in `2026-08-21-review-TOOL-dUnstalledConvoy-23-24-25-specs.md`. Disposition, verified
against rev-3 rather than against its revision log:

| R2 | Subject | Status in rev-3 |
|---|---|---|
| B1 | union does not deliver the in-band exit | **CLOSED.** Retracted by name in the Goal; the fork was resolved to REPORT instead |
| B2 | S2 states no window boundary; arm C flips | **CLOSED.** S3 states `(own, next]` and ordering by ancestry; arm C traced surviving |
| B3 | spec 25's predicate reds 151 of 225 | **CLOSED.** Unit retired on the measurement |
| B4 | spec 25's own Design violates its check | **CLOSED** by the retirement |
| B5 | AC6's motivating claim measured false | **CLOSED** by the retirement |
| H1 | union proves "declared before COMMIT", not "before WRITE" | **LIVE — decided the other way without saying so.** M4 |
| H2 | "co-named with a file" undefined | **CLOSED** by the retirement |
| H3 | spec 24's fixture precedent false about the base | **CLOSED.** rev-3 corrects it to `recall-opened.test.sh` and says so |
| H4 | AC3 green at base, wrong measurement for union | **LIVE and worse.** rev-3 dropped the scoping qualifier; the criterion is now unsatisfiable. B2 |
| H5 | no AC observes S8's flip | **CLOSED** — there is no flip any more |
| H6 | driver-side never-closing row neither IN nor OUT | **LIVE, third revision.** L2 |
| H7 | AC1/AC2 satisfied by existing green arms; `drows` is NESTED | **LIVE, unaddressed.** H1 |
| H8 | union widens the no-commit branch's path probe | **HALF-CLOSED.** S4 fixes the window, not the path set. M3 |
| H9 | orphaned widening prose live in the leg and its suite | **HALF-CLOSED.** S7 names two carriers; five exist. H3, H4 |
| M1 | spec 24's AC3 pins the vacuous negative | **CLOSED in the AC, broken in the prose.** M6 |
| M2 | docs item misses the manifest, cites a carrier that does not exist | **LIVE, both halves.** H5, M5 |
| M3 | `pop_guard` does not reach S2's vacuity mode | **CLOSED** by the retirement |
| M4 | spec 25 states its population two ways | **CLOSED** by the retirement |
| L1 | AC8's observation exits non-zero on the outcome it asserts | **LIVE and doubled.** L1 |

**Nine closed, two half-closed, one closed-in-the-AC-only, seven live.** Of the live ones, six are
oversights — nothing in §3 or the revision log records a decision to leave them — and one (H1) is
decided the other way without disclosure, which is M4's whole content.

---

# What this revision got right

Worth stating, because the list above is long and rev-3 is a genuine improvement on rev-2.

- **The owner's resolution is the correct call and it dissolves more than it was asked to.** Round 2's
  B1 and B2 were both consequences of trying to keep a hard gate in a run with no owner turn. Making
  check 23 a report removes the stall, the flip, the rollback key and the retraction vector in one
  move, and the spec says so plainly rather than reframing.
- **The false claim is retracted by name, in the Goal, with the evidence.** "`pass_commit` opens its
  window as `"$_pa..HEAD"`, which EXCLUDES the anchor" is exactly right, and it is stated as a
  verification rather than an argument. That is the second revision in a row where the retraction is
  the best-written part of the document.
- **S3 is the right rule.** I traced arm C under it and the finding survives; under the exclusive
  reading round 2 flagged, it does not. Only the rationale is inverted (M1), not the boundary.
- **Spec 25's retirement is exemplary.** Two predicates written, both RUN over the real corpus, both
  rejected on measured false-positive rate, with the numbers in the document. The charter asks for
  "run a candidate gate predicate over the real tree before wiring it" and this is what that looks
  like when the answer is no.
- **Spec 24's rev-3 fixes both of round 2's defects properly** — the fixture precedent is corrected
  with the reason ("rev-2 named it from memory"), and AC3 is relabelled a negative control and tied to
  AC2's fixture so the pair discriminates. Only the surrounding prose was left behind (M6).
- **The forks-as-bullets conversion works.** Both specs' §8 entries now parse as list items.

# Coverage and limits of this review

- Every code claim was re-verified at `37abdf95` by reading or running, not inherited from the finder
  pass. The `gotchas.py` reachability claims (B3) were **measured by running the tool**, not traced.
  `grep -c`'s exit code (L1) was measured. Every `DISPATCH_GRADING` and `GOV_UNATTENDED_REPORT`
  carrier came from `git grep` over the tracked tree.
- **Not run:** the full bar, the unattended suites, and any fixture. The diff is records-and-spec only
  and touches no gated artifact, so every arm-level claim above is traced by reading rather than by
  execution. In particular, arm C's survival under S3 (hunt item 4) is TRACED, not reproduced —
  reproducing it requires implementing S2 and S3 first.
- **Not assessed:** whether REPORT is the right resolution of F1 at all, as opposed to whether the
  spec's design under that resolution holds. The owner resolved it; B1 argues the delivery is unfunded,
  not that the decision is wrong.
- **Not assessed:** spec 24's S1, which is small, correct about the flow, and uncontested across three
  rounds.
- **One finding's citation was corrected during verification:** raw id 15 anchors on spec 24 while its
  substance is spec 25's AC1/AC2 at the same line offsets. Re-anchored to spec 25 in H6. The substance
  checked out; the pointer did not.

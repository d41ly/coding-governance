**Serves:** diff-review TOOL-dUnstalledConvoy-23 TOOL-dUnstalledConvoy-24

# Design review — two specs written from four rounds of evidence, against a tree that moved

**Reviewed range:** `d9728f89...HEAD` (HEAD = `de766cb3`, 1 commit, 2 files, spec only). **ROUND: 1.**

## Verdict: BLOCKED

**Five blockers, eight highs, seven mediums, one low.** This diff is two specs and no code, so every
finding below is a design defect: a scope item that cannot be built, an acceptance criterion a wrong
implementation also satisfies, a non-goal that is false about the base, or a decision the spec
resolves on a mechanism it contradicts itself about.

The headline is one sentence, and spec 23's own revision log says it first: it was **written against
the four review records rather than against the code**, and the code moved between round 4 and this
spec's own pinned base. Commit `e42cb5a` ("the widening branch is gone") is an ancestor of base
`d9728f89` and deleted the re-declaration and widening machinery outright. Spec 23's S2, S3 and two
of S5's four one-liners edit that machinery, and AC3, AC5 and AC7 observe its behaviour. Four of
seven scope items and three of eleven acceptance criteria therefore have no subject, and a builder
following them literally re-introduces the forty lines rounds 1 through 4 each damaged — with the
design pass skipped and `DISPATCH_GRADING` flipped ON over the result.

Spec 24 has the same shape in miniature and it is not a wording slip either. Its Goal says check 31
reports "the COMMITTED phase". It does not: `fact()` reads the file on disk, so check 31 reports the
WORKING-TREE phase. Both of the unit's scope halves that depend on that premise are dead on arrival,
including in the incident the spec was written from, which is in this repo's own revision log.

## Review shape

- **raw 46 · confirmed 40 · refuted 6 · unverified 0 · precision 0.87.**
- After dedupe the 40 confirmed collapse to **21 distinct defects: 5 BLOCKER, 8 HIGH, 7 MEDIUM, 1
  LOW.** Each section names the raw confirmed ids that reached it. Five lenses reached the spec-24
  index-read defect independently and four reached the stale-base defect, which is what a spec
  written from records rather than from source produces.
- Every code claim below was re-verified against the tree at `de766cb3` before this report was
  written: ancestry by `git merge-base --is-ancestor`, the leg's awk fold by piping rows through it,
  `normpath` by sourcing the library, the leg's own output by running it, and the merge that carried
  `BUILDING` by `git cat-file`.
- **Not covered:** the full bar was not re-run for this review; the diff is spec-only and touches no
  gated artifact. That is an assumption, not an observation.

---

# BLOCKERS

## D1 — Spec 23 edits code its own base deleted: four scope items and three ACs have no subject

*(raw ids 1, 15, 28, 36)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:17-27`, `:95`,
`:100`, `:103`

`git merge-base --is-ancestor e42cb5a d9728f8` succeeds, so the spec's own BASE carries the deletion.
At that base `verb_dispatch` ends at `tools/unattended/unattended.sh:2407-2428` with the removal
rationale in capitals — "THE RE-DECLARATION AND WIDENING MACHINERY IS GONE", "A declaration is now
APPEND-ONLY" — and falls straight through to `park` and an unconditional `dispatch declared` echo.
Grepping the file for `WIDENED`, `_shares`, `curgrp` and `curpaths` returns only the dead locals in
the `local` line at `unattended.sh:2263`. There is no `cur` selection, no `tail -1`, no narrowing
test, and no re-declaration lookup anywhere in the verb.

So:

- **S2** ("the re-declaration lookup keys on raw `pass_commit` openness") names a lookup that does not
  exist.
- **S3** ("`cur` is selected by best match, not `tail -1`") names a selection that does not exist.
- **S5 item 1** ("the narrowing test compares normalised paths") names a test that does not exist.
- **S5 item 4** ("the re-declaration gate drops its `curgrp != grp` nesting") names a gate that does
  not exist.
- **AC3**, **AC5** and **AC7** observe behaviour no code path at base can produce, and **AC10**'s
  red-first discipline is unsatisfiable for those arms: you cannot observe an arm RED against a
  branch that is not there.

Section 4 compounds it by discussing `tail -1` in the past tense as though it were live code, so this
is not a stale sentence — the whole design paragraph is written against a pre-`e42cb5a` tree. The
library's own header at `tools/unattended/lib-unattended.sh:68-69` still advertises "the driver's
re-declaration rule" as one of `pass_commit`'s three callers, which is where the spec's mental model
came from and which is itself now wrong.

The consequence is not merely unbuildable scope. A builder taking S2/S3/S5 literally must first
RE-INTRODUCE the branch `e42cb5a` removed with the recorded verdict that "every version of it was
wrong in a different direction", and the spec carries no design for the re-introduced form, no
statement of what a widening is against append-only rows, and no argument for why D1's retraction
vector does not come back with it. That is round 5 re-opening the exact forty lines with the design
pass skipped.

**Fix.** Re-ground section 2 and section 4 on `verb_dispatch` as it stands at `d9728f89`. Either
(a) drop S2, S3, S5 items 1 and 4, AC3, AC5 and AC7, leaving S1, S4, S5 items 2 and 3, S6 and S7 as
the real scope and building the redesign on the append-only record; or (b) add an explicit S0 that
re-introduces a re-declaration path, with its full semantics against append-only rows (what a
widening is, what anchor the replacement takes, what a fold by group and unit does) and its own
statement of why D1 does not return. Silently presupposing the branch is the one option that must not
survive review.

**Left-shift gate.** A spec-hygiene arm that every `file:line` and every code identifier a spec names
in its Scope section resolves at the spec's own declared BASE. This is one grep per backticked
identifier against `git show <base>:<path>`, it is cheap, and it would have caught all four items and
all three ACs before the spec was committed. Same class as the memory-tree hygiene checks already
running.

## D2 — S4 gives one helper to two callers whose correct answers differ, which is the root cause the spec itself names

*(raw ids 2, 32)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:22-23`, design at
`:63-66`

Section 4 says the four rounds failed because "one predicate served three callers whose edges
disagree". S4 then states the helper exists "so S1 and S2 read the same history the same way", and
section 4 line 64 says outright that the helper "answers which commits belong to this row once, and
both the driver and the leg call it". That is the same shape one caller shorter.

Round 4's D5 fix says the opposite in as many words, at
`reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-round3-fix.md:243-245`: "Keep `pass_commit`
unchanged — it is check 23's attribution oracle. Add a second library helper, e.g.
`pass_commit_in_set <anchor> <unit> <rel> <declared…>`, and call that from the filter." Driver-side
only.

The two callers genuinely want different answers, and section 3 already commits to one of them:

- The **leg's** oracle (S1, check 23's grading window) must stay PERMISSIVE. Section 3 lists
  de-permissifying `pass_commit` as OUT precisely because an intersection filter makes check 23
  report an out-of-lane pass as "a pass that produced no change".
- The **driver's** openness filter (`unattended.sh:2337-2351`) must be SET-FILTERED and scan forward
  unbounded, closing a row only on a commit intersecting that row's declared set.

One helper is either set-filtered or it is not. Verified the regressive arm end to end in the leg: if
`dshit` is empty, `check-unattended.sh:1153-1169` takes the no-change branch, and a pass that
committed ENTIRELY outside its lane moves none of its declared paths, so `dsmoved` is empty and the
code emits `report "check 23 observed ... a pass that produced no change"` — silent unless
`GOV_UNATTENDED_REPORT=1`. That is verbatim the regression section 3's own OUT list forbids, arriving
through the helper instead of through `pass_commit`, and S6 ships it as a live gate that cannot fail
on out-of-lane writes.

**Fix.** Split S4 into two named helpers, each with a header stating what it does NOT answer.
`pass_commit` stays untouched — first qualifying commit, unbounded, permissive — and remains check
23's oracle. `pass_commit_in_set <anchor> <unit> <rel> <declared…>` serves the driver's `sibrows`
filter and nothing else. Say in S4 that S1's windowing lives in the leg, where the anchor list lives,
not in a shared helper. Update `pass_commit`'s header at `lib-unattended.sh:66-78` to name its real
callers, since one of the three it advertises no longer exists.

**Left-shift gate.** An acceptance criterion, and a driver arm behind it, asserting that a commit made
entirely outside the declared lane still REDS check 23 rather than reporting no change. That single
arm distinguishes the set-filtered helper from the permissive one at the only place the difference
matters, and it is the arm round 3 and round 4 both wished existed.

## D3 — Nothing in the spec says what a unit's GRADED SET is when it has several rows, and the leg's fold silently drops all but the last

*(raw id 16)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:14-16`

Empirically reproduced the fold: piping two rows with identical group-and-unit keys through the awk
at `tools/unattended/check-unattended.sh:1121-1125` prints only the SECOND, because `row[k] = $0`
overwrites unconditionally. Reachability verified in the driver: two `--dispatch` calls at an unmoved
HEAD both key on `grp=$(GIT rev-parse --short=8 HEAD)` (`unattended.sh:2318`), condition 1 skips the
unit's own rows at `:2384`, and with the re-declaration branch gone nothing else refuses a second
row, so `park` appends at the same anchor.

That is precisely the repair `unattended.sh:2421` documents in place of widening — "A pass that needs
more paths declares again; both rows are on the record" — and the leg silently discards one of them.
Concretely: unit U declares `--writes work/a`, writes nothing yet, then declares `--writes work/b`
for the extra lane. Both rows carry the same key. The pass then commits `work/a/x` and `work/b/y`,
and check 23 grades both against `work/b` alone and reds on `work/a/x`.

S1 does not reach this — the row is discarded before any window opens. And once S6 flips the grading
ON, this is a terminal merge-bar red at the push boundary with no owner turn and **no in-band exit**:
a corrective declaration lands at a NEW anchor, so under S1 the surviving bad row's window still
contains the offending commit. That is the "refusal no run can clear in band" the backlog row for
this very unit names as one of the two failure modes to design AGAINST. Note also that
`tools/unattended/unattended.test.sh:2718-2720` asserts the driver parks 2 rows, so the driver-side
arm cannot see the leg dropping one either.

**Fix.** Add a scope item stating the graded set explicitly. Either the UNION of a unit's rows whose
window contains the commit, or last-wins with the driver ECHOING the effective set and the protocol
telling a run to re-declare CUMULATIVELY. Whichever is chosen, write it in section 2 and in the
protocol, because the driver's comment and the leg's fold currently give two answers to one question.

**Left-shift gate.** An arm over the shape "declare, declare again with only the new path, commit both
lanes", asserting the leg is silent — or, if the design chooses refusal, that the driver refuses at
DECLARATION time, which is at least clearable. Plus a leg-side assertion that the number of rows the
fold emits equals the number of rows in the file for a unit with rows at distinct anchors.

## D4 — S6 flips the grading ON over a same-anchor supersession hole, so D1's retraction survives one step earlier

*(raw id 29)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:28-29`

`park` appends unconditionally (`unattended.sh:2070`) and nothing in `verb_dispatch` refuses a second
declaration for the same unit — condition 1 skips the unit's own rows at `:2384`. Two `--dispatch`
calls with no commit between them therefore share the short-HEAD group key, and check 23 still folds
one row per group-and-unit keeping the LAST (`check-unattended.sh:1121-1127`).

The leg suite's arm A at `tools/unattended/check-unattended.test.sh:1449-1454` explicitly blesses
that supersession: `drows` writes two rows at the SAME anchor and the arm asserts no check-23
failure. So the sequence — declare `work/a`, write `work/b/x` without committing, re-declare
`work/a work/b` at the same anchor, then commit — drops the narrow row from the fold and grades the
wide one GREEN. Nothing refuses it: section 3 lists the narrowing refusal OUT and the driver no
longer has one.

That reopens round 4's D1 one step earlier than the branch that was deleted to close it. S1 does not
help — with a single shared anchor there is no later anchor to bound against. The driver's own
comment at `unattended.sh:2422` ("nothing rewrites, supersedes or retracts an earlier one") is false
as check 23 reads the file, which is the two-answers-to-one-question class the kit library was
created to end. **A disjointness proof that can be talked out of a finding is worth less than no
proof, because it is believed** — that is round 4's verdict, and S6 turns exactly that on.

**Fix.** Before S6, make every appended row graded: key the fold on the row itself (anchor plus
ordinal) rather than on group-and-unit, or restore a driver-side refusal so a same-anchor
re-declaration cannot shrink the record. Make S6 conditional on the negative-control arm below being
green.

**Left-shift gate.** A leg arm as a negative control: declare narrow, write out of lane WITHOUT
committing, re-declare wide at the SAME anchor, commit, assert the leg still REDS. Arm A at
`check-unattended.test.sh:1449-1454` currently asserts the opposite verdict over the same row shape,
so this arm and that one together pin the boundary the design has to choose.

## D5 — Spec 24's S1 reads the wrong source and cannot fire in either tree of the incident it was written from

*(raw ids 6, 17, 20, 27, 37)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-24.md:8-9`, `:14-16`,
`:73-74`

The Goal's premise is wrong about the code. `fact()` at `tools/unattended/unattended.sh:246-256`
reads the file on disk (`done < "$1"`), and `verb_landed` grades `cur=$(fact "$rel" phase)` at
`:1324-1326`. **Check 31 reports the WORKING-TREE phase, never the committed one.** Both trees of the
recorded flow then defeat S1:

- **In the tree where `--close` ran**, `set_fact` at `:1870` rewrites the working file to `LANDING`
  before `stage_or_fail` at `:1875` stages it, so tree and index agree, check 31 PASSES, and the
  refusal actually met is `check_clean`'s `fail 2 — the working tree is dirty ... N path(s)`
  (`:622-632`), a bare count naming neither the file nor the fix. The code already documents this at
  `:1871-1874`. This unit does not touch that message.
- **In the merged tree where check 31 DID fire**, nothing is staged. Verified against this repo's own
  history: merge `c5da884` has parents `cac2915` and `38d0b09`, and `git show
  c5da884:memory/builds/dUnstalledConvoy/RUN.md` carries `phase: BUILDING`; `LANDING` first appears
  as a COMMIT at `8e1a81b`. A tracked file in a clean tree has an index entry equal to HEAD, so
  `git show :<run-state>` returns the same `BUILDING` the refusal already printed, and the new branch
  falls through to today's message.

So the discriminator is empty on both the reachable path and the reported one. **AC1**'s state —
`LANDING` staged over a `BUILDING` worktree — is producible by no verb in the kit; reaching it needs
a hand `git restore --source=HEAD --worktree`. An arm pinning a state the kit cannot enter goes green
while the trap stays, which is the D6/D9 shape this build has already shipped twice. **AC5** then
quantifies over that synthetic population. Section 3 compounds it with "A run still reaches `LANDED`
only from a committed `LANDING`", which is false — check 31 requires a WORKING-TREE `LANDING`.

S2 (the `--close` message) is the only item in this unit that reaches the reported flow.

**Fix.** Correct the Goal to say check 31 reports the working-tree phase. Then promote S2 to the
primary fix and re-aim S1 at a state that actually occurs. In the merged tree the run-state file is
at `BUILDING` with a clean index, and the only evidence a `LANDING` was ever evaluated is that it was
never committed — so either have check 31 name the re-close path and its cost, or enumerate
`git worktree list` and name the tree whose run-state file reads `LANDING`. If the index read is kept
anyway, say in section 2 that it covers no driver-reachable state and label AC1's fixture hand-built,
so a green arm is not read as coverage.

**Left-shift gate.** An arm that drives the ACTUAL cross-tree sequence end to end — `--close` in a
linked worktree, merge into the primary, `--landed` there — and asserts on the refusal text. Any arm
that has to desync index from worktree by hand should be refused at review as a fixture the kit
cannot produce; that rule is worth writing into the build method, since this is its third instance.

---

# HIGHS

## D6 — S1's window has neither a boundary rule nor an ordering rule, and the wrong choice on the boundary restores D1

*(raw ids 3, 45)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:14-16`

S1 says only "the commits between its own anchor and the NEXT anchor for the same unit". Two rules
are missing and both are decisive.

**Inclusivity.** Anchors are `GIT rev-parse --short=8 HEAD` at declaration time
(`unattended.sh:2318`), so a re-declaration made AFTER a pass commit anchors ON that commit, and
`pass_commit` opens the exclusive range `$_pa..HEAD` (`lib-unattended.sh:82`). The existing fixture
proves the stakes: arm C at `check-unattended.test.sh:1464-1472` puts the out-of-lane commit exactly
at row 2's anchor. Read exclusively, that commit leaves row 1's window and is already outside row
2's, so it is graded by nobody — rc=1 to rc=0, D1 restored by the very change meant to bound the
window.

**Ordering and ancestry.** Rows are appended in call order and check 23 emits keys in FIRST-appearance
order (`check-unattended.sh:1121-1125`); the only anchor validation is the per-row
`merge-base --is-ancestor "$dsgrp" HEAD` at `:1139`, and the PAIR is never validated. Under M6's
concurrent shape, passes sit in separate worktrees at different HEADs, so `next_anchor` need not
descend from `anchor` and `git log anchor..next_anchor` may be empty or name another line entirely.
There is also a plainly reachable case on the append-only code as it stands: a run that widens BEFORE
its pass commits leaves row 1's window holding only bookkeeping commits, `pass_commit` returns
nothing, `dsmoved` is empty because the window closed before the pass wrote, and the row takes the
silent no-change `report`. S1 as written converts a red into a silence — the "less able to fail"
class round 4 was told to hunt, arriving inside the fix for it.

**Fix.** State both rules in S1. The window is `<this anchor>..<next anchor>` INCLUSIVE of the next
anchor's commit, so a commit that is itself an anchor is graded by the row it closes. "Next" is the
next anchor that is a DESCENDANT of this one; a row whose successor is not a descendant falls back to
`<anchor>..HEAD` and emits a named report saying the pair is unordered, never an empty window.

**Left-shift gate.** Two arms: the anchor-is-the-offending-commit case (arm C's shape, asserted to stay
RED after S1), and the unordered-pair case asserting the named refusal rather than silence.

## D7 — S1 bounds one window and leaves check 23's second one running to HEAD, and AC2 cannot see it

*(raw id 19)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:93-94`

Check 23 has TWO windows. S1 and AC2 name only the first. The second is the no-commit branch's
moved-path probe at `check-unattended.sh:1161`, which is
`GIT log --format=%H "$dsgrp"..HEAD -- "$dsp"` — all the way to HEAD.

With only the `pass_commit` window bounded, a row whose window holds no pass commit takes the
no-change branch, and that branch then asks whether its declared paths moved over `anchor..HEAD`,
which includes the NEXT pass's commits. Wherever the two rows' declared sets overlap — the ordinary
shape when a unit re-declares — the result is not the "no-change branch reports" AC2 promises but
`fail 23 — a declared path of a dispatched pass moved after the group anchor while no commit names
that pass`, while the later row grades clean.

AC2's arm cannot detect this, because round 4's D2 reproduction used DISJOINT lanes (`work/spec` then
`work/build`), so the probe stays silent there and an arm built from it passes over the unbounded
second window. A careful builder might bound both from S1's wording; the defect is that AC2 cannot
tell whether they did.

**Fix.** Say in S1 that BOTH windows are bounded above — the `pass_commit` call and the moved-path
probe — and rewrite AC2's arm so the two rows' declared sets OVERLAP, which is the only case where an
unbounded second window is visible.

**Left-shift gate.** The overlapping-lane variant of AC2's fixture, asserting the no-change REPORT and
explicitly asserting the absence of the `moved after the group anchor` failure.

## D8 — Section 4's claim that a bounded window grades "its own pass's commits and nothing else" is unsupported, and S1 can turn a red green

*(raw id 31)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:53-56`

The only attribution check 23 has is the unit id in the commit subject, via `id_in` at
`lib-unattended.sh:83`. That is identical for every pass of one unit, so bounding by anchor time adds
no pass identity — S1 MOVES the mis-attribution rather than removing it, and it can move it in the
wrong direction.

Traced against the live append-only driver: declare `work/one` at A0, commit a run-state park moving
HEAD to A1, re-declare at A1, then commit writing only `work/two`. Today row `(A0, work/one)` has
window `A0..HEAD`, `pass_commit` finds the `work/two` commit, and the subset test REDS. With S1 the
window is `A0..A1`, empty, so the no-change branch runs; `dsmoved` finds `work/one` unmoved and emits
the silent report; the commit is then graded only against the later row and PASSES. The same result
follows for the concurrent two-lane shape where pass 1's commit lands after pass 2's anchor.

That is red-to-green on the exact defect the check exists to catch. Neither AC1 nor AC2 covers this
direction — both pin the no-change reporting, never the cross-pass attribution.

**Fix.** Either put a pass discriminator into the row key AND into the commit-subject rule so the join
can tell one unit's passes apart, or state plainly in section 4 that S1 buys only the no-change case
and leaves cross-pass attribution unresolved. Do not let the current sentence stand: it claims a
property the change does not deliver, and section 4 is what a builder reads for intent.

**Left-shift gate.** An arm for the cross-pass case asserting the leg still REDS when a pass writes
into a sibling pass's lane, with the sibling's own row present and clean — the control that
distinguishes "red because attributed" from "red because everything reds".

## D9 — S4 has no acceptance criterion at all, and it silently drops the second half of round 4's D5 fix

*(raw ids 4, 39)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:22-23`, AC set at
`:91-111`

Mapping the criteria to the scope: S1 has AC1 and AC2, S2 has AC3, S3 has AC5, S5's first three items
have AC6, AC7 and AC8, S6 has AC9, S7 has AC10, and the bar has AC11. **S4 and S5's fourth item have
none.** S4 is the unit's only library change and the fix for D5 — the terminal-stall class, which in
a run with no owner turn ENDS the unit, and which is this build's entire subject.

The class is live at base. `pass_commit` returns only the FIRST qualifying commit, so the filter at
`unattended.sh:2337-2351` tests that one commit's diff against the row's declared set, and a row
whose first candidate missed the lane never closes. Traced concretely: unit A declares `work/one`
(row 1), later declares `work/one work/two` (row 2), the pass writes only `work/two/y.txt`. No commit
ever intersects `work/one`, row 1 stays open forever, and unit B declaring `work/one` hits condition
1's `fail 49 ... also in <who>` at `unattended.sh:2382-2392`. The scan-forward helper alone does not
close row 1 either.

And S4 carries only the scan-forward half of D5. The second half — `round3-fix.md:245-247`,
"Additionally fold `sibrows` by `(group, unit)` keeping the last row, as check 23 already does, so a
superseded narrow row cannot outlive its widening" — appears nowhere in the spec, neither IN nor OUT.
Existing arms do not reach it: `unattended.test.sh:2683-2690` stops at the `git add -A` declaration
commit where refusing is correct, and `:2655-2660` uses a commit that DOES intersect the lane. AC11's
full bar passes over the whole class because no fixture exercises it.

**Fix.** Add the fold of `sibrows` by group-and-unit to S4, or list it in section 3 with a reason and
the unit that owns it. Add the two acceptance criteria D5's left-shift already specifies.

**Left-shift gate.** Round 4 wrote the gate; adopt it verbatim. Two driver arms — the `git add -A`
declaration commit carrying one extra tracked file, and widen-then-write-only-the-new-lane — each
asserting a later sibling declaration is ADMITTED, and each with its control (a clean declaration
commit admitted) beside it, or the arm cannot tell "admitted because correct" from "admitted because
nothing was checked".

## D10 — AC3 is not observable and has no positive control, so an implementation that does nothing for S2 satisfies it

*(raw ids 5, 40)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:95-97`

AC3 asks an arm to distinguish condition 1's openness set from "the re-declaration lookup's". Two
problems, either of which is fatal.

**There is no second consumer.** `sibrows` has exactly three readers in `verb_dispatch` — the
empty-set announcement at `:2359-2361`, the condition-1 loop, and `sibpaths` feeding the
generated-index pairing refusal — all fed by the single intersection-filtered set. The re-declaration
lookup AC3 names no longer exists. No output, message or exit code can differ between the two sets,
so an implementation that computes a second set and never wires it satisfies AC3 exactly as well as
one that does.

**There is no positive control.** The only observable for "closed to the re-declaration lookup" is
that a re-declaration was NOT treated as a widening. At base, every re-declaration prints
`dispatch declared` and parks a row unconditionally (`unattended.sh:2425-2427`), so the arm passes
without any lookup existing and without the two openness sets ever being distinct. **The criterion
the spec calls its spine is satisfied by not doing S2.** Round 4 booked this exact shape twice: an
arm that "passes by containing no instance of what it names" (D9) and a repair "held by nothing"
(D6).

**Fix.** Name the observable: the exact driver stdout and exit code, for one fixed sequence, in each of
the two membership states. Pair the negative half with its control — an OPEN pass (no commit yet)
re-declaring a strict superset IS recognised as a widening and reuses the original anchor, while the
committed-out-of-lane pass is not — one arm asserting the DIFFERENCE, both spellings in the same
fixture. If no such observation pair exists once S2 is re-based on the current code, delete AC3 with
S2 rather than restating it.

**Left-shift gate.** A review rule worth a checklist entry, since this is its third appearance in this
build: **an acceptance criterion whose only observable is an ABSENCE must ship with the presence arm
beside it, in the same fixture.**

## D11 — AC5 arms a new refusal and nothing arms its in-band exit

*(raw id 8)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:100-101`, design at
`:58-61`

S3 converts a path that today parks a row and continues into a refusal. In a run with no owner turn a
refusal that cannot be cleared is TERMINAL — the backlog row for this unit names "a refusal no run
can clear in band (round 3, terminal in an unattended run)" as one of the two reproduced failure
modes to design against, and it is precisely what round 3 shipped and `e42cb5a` removed.

Section 4 asserts two exits ("the run declares narrower, or commits the pass it already has"). AC5
asserts only that the refusal fires and names both rows. Neither exit is observed. Worse, the first
exit is in tension with section 3's own claim that "a new pass partly overlapping its predecessor is
refused as a narrowing": declaring narrower is a strict subset, always overlaps, and under that
boundary is itself refused.

**Fix.** Add an acceptance criterion that DRIVES the escape: after the two-overlap refusal, a narrower
re-declaration (or a commit closing one of the two rows) is ADMITTED and prints a success line, in
the same fixture, so the refusal is proven clearable rather than asserted clearable. Resolve the
tension with section 3 explicitly.

**Left-shift gate.** A standing rule for this kit: **every new driver refusal lands with an arm that
clears it in band.** One grep over the driver's `fail` sites versus the suite's admitted-after-refusal
arms would keep it honest, and it is the single cheapest guard against the failure mode this build
exists to remove.

## D12 — The DISPATCH_GRADING rollback that F1 leans on does not exist; section 5, AC9 and the shipped confs contradict each other

*(raw ids 9, 18, 33, 41)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:84-85`, `:107-108`,
`:120-123`

Verified byte for byte. `check-unattended.sh:1115` is `if [ -z "${DISPATCH_GRADING:-}" ]; then`
followed by the DARK report and `continue`; both `.unattended.conf:144` and
`tools/unattended/.unattended.conf.example:125` are `DISPATCH_GRADING=""` under comments reading
"non-blank turns ON ... BLANK, and blank is the default". The `:-` idiom collapses blank and absent
into one state, and the sibling key `LANDED_ANCHOR_CUTOFF` uses the same idiom, so a
presence-versus-blank reading that would reconcile the spec contradicts the kit's own semantics.

AC9 requires the key UNSET in both files AND the grading RUNNING, which is only satisfiable by
inverting that test. After the inversion, **blank is the ON state** — so section 5's "a project that
hits trouble sets it blank and is back to today's behaviour without a code change" names a value that
turns it on. F1 resolves the only open fork on exactly that mechanism: "The rollback is one conf key,
which is what makes flipping it the reversible choice rather than the brave one." As specified there
is no value a project can set to get today's behaviour back, and the only rollback left is a code
revert — in a gate whose wrong red lands at the push boundary of a run with no owner turn.

Two collateral items the scope never names. The leg SOURCES the conf (`check-unattended.sh:70`), so
every project whose conf was rendered before the flip keeps `DISPATCH_GRADING=""` and stays DARK
under a presence-reading, or flips ON unasked under a blank-reading — "this unit flips it" is true
for this repo and not for adopters either way. And the two arms that pin the dark path assert it by
DELETING the key (`check-unattended.test.sh:1602` and `:1610`), so both invert under the flip and
neither is in scope.

**Fix.** Pick the OFF spelling and make section 5, S6, AC9 and both conf comments say the same one —
either keep the key positive-sense and have S6 write `DISPATCH_GRADING="1"` into both confs (default
ON by declaration, blank still OFF, adopters unaffected until they re-render), or introduce an
explicit `DISPATCH_GRADING="off"` sentinel tested as `[ "${DISPATCH_GRADING:-on}" = off ]`. Decide
blank-versus-unset explicitly. Name the whole declared population in S6: both confs,
`tools/unattended/kit.toml:38`, both protocol copies at line 387, and the two dark arms. State what a
pre-flip adopter conf gets.

**Left-shift gate.** An acceptance criterion that the disabling value RESTORES the dark announcement,
observed on a fixture — the rollback observed rather than asserted. Plus an arm for each of the three
states (unset, blank, set), since the spec cannot currently say which two are the same.

## D13 — Spec 24's S3 has no refusal site to attach to, and AC4 names a reading `--close` does not perform

*(raw ids 7, 34, 44)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-24.md:19-21`, `:79-80`

`verb_abort` at `unattended.sh:1441-1482` writes `phase ABORTED`, writes the witness, parks the
reason and calls `stage_or_fail`. **It contains no phase-reporting refusal at all**, so S3's "the same
reading for `--abort`" has nothing to edit — and `--landed`, where check 31 lives, is never the verb
that follows an abort.

The polarity is also opposite. Every ABORTED consumer was checked — `refuse_if_terminal` at
`:1038-1045`, `verb_preflight`'s rotation test at `:1499`, `verb_phase` at `:1272`, `verb_resume` at
`:1756`, `check_single_live` at `:781` — and **none refuses because a phase is not ABORTED**. What a
lost ABORTED actually produces is a record that stays non-terminal to every later reader, surfacing
much later as `check_single_live`'s check 5 on the NEXT run's preflight, in a different verb with a
different message that reading the index cannot repair either, since `check_single_live` also reads
the working tree through `fact`.

And S1's own condition excludes `--abort` by construction twice over: S1 keys on a staged phase of
`LANDING`, which a staged `ABORTED` does not match; and `verb_landed` calls `refuse_if_terminal` at
`:1323`, one line BEFORE `cur=$(fact ...)` at `:1324`, with `PHASES_TERMINAL="LANDED ABORTED"` at
`:106` — so an ABORTED record is refused by check 26 and never reaches check 31 at all.

AC4's wording is worse than underspecified: "`--abort` carries the same staged-phase reading as
`--close`", and `--close` performs no staged-phase reading in this spec or in the code — it is the
verb that STAGES. No implementation can be judged against it, so any implementation satisfies it.

**Fix.** Name the function S3 changes. The buildable half is the `--abort` sibling of S2: an abort
success message that names committing the run-state file as the next step, pinned by an acceptance
criterion on its exact text. If the abort-side loss is in scope at all, name the real consequence — a
record that stays non-terminal and later trips check 5 — and pin that, or scope S3 to
`refuse_if_terminal` and say why. Delete AC4 as written either way.

**Left-shift gate.** An arm asserting the check-5 consequence end to end: abort without committing,
start the next run, assert the preflight refusal names the un-committed terminal record. That is the
observable that exists, and it is the one an operator actually meets.

---

# MEDIUMS

## D14 — Round 4's D6 and D9 are neither IN nor OUT, and S6 turns the leg ON over the unarmed line D6 names

*(raw ids 14, 24)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:34-44`

D6 was rated HIGH and is mutation-verified: replacing the leg's `covers` call with the original
literal `case` left both suites PASS at byte-identical assertion counts. That call now sits at
`check-unattended.sh:1198` (round 4 cited `:1141`, stale after `e42cb5a`). Grepping
`check-unattended.test.sh`, `cross-component.test.sh` and `unattended.test.sh` for `covers`,
`overlaps` and a `work/sub` fixture returns only comment prose and the driver-side arm at
`unattended.test.sh:2729-2735` — neither the hand-written `drow ARCH-tRun-1 "work/sub/"` arm nor the
class-level call-site assertion round 4 demanded exists. Since the driver parks normalised spellings,
no fixture can present the leg with a row it must normalise, so the half that repairs rows written by
an OLDER driver is held by nothing — and S6 makes it load-bearing for every such project.

D9 is worse than round 4 recorded. Cross-component arm 3b at `cross-component.test.sh:107-122`
inherits `DISPATCH_GRADING=""` from the repo conf it copies at `:51`, so check 23 hits the dark
`continue` at `check-unattended.sh:1119` and the DARK `report` is silent without
`GOV_UNATTENDED_REPORT=1`. The assertion "the leg is silent" **cannot fail at all**, behind
`FLOOR_ASSERTIONS=19` at `cross-component.test.sh:176`. AC11's green bar is exactly what both defects
produce.

Section 3 does name arm 3b, but only in round 4's do-not-undo sense, not as a decision about its
vacuity; and section 10's "`covers`/`overlaps`/`normpath`/`id_in` are all reused unchanged" is a reuse
note, not a scope decision. **A HIGH from the evidence base must not be left unclassified.**

**Fix.** Add D6's two arms and D9's missing commit to section 2 as an explicit item, or list both in
section 3 with the reason and the unit that owns them.

**Left-shift gate.** A hand-written `drow ARCH-tRun-1 "work/sub/"` leg arm (the spelling only an older
driver produces), plus a class-level assertion that the leg script contains at least one
`covers`/`overlaps` call site. For arm 3b, a real write commit inside the arm and an explicit
`DISPATCH_GRADING=1` in that fixture, keeping the rc=0 and empty-output assertions.

## D15 — Section 3 lists as a settled boundary a refusal the base deleted and the suite pins the ABSENCE of

*(raw id 12)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:42-43`

The OUT list's second KNOWN boundary — "a new pass partly overlapping its predecessor is refused as a
narrowing ... Both are documented and pinned" — is false about the code at base.
`unattended.sh:2419-2424` states there is no narrowing refusal, "because with grading dark there is
nothing for a narrowing to hide from — and a refusal nobody can clear is the stall this build exists
to remove", and `unattended.test.sh:2721-2727` asserts the ABSENCE with `miss ... "narrowing is not"`
under a comment saying it is pinned as an absence so its return is visible. It is "documented" only
in the STALE protocol prose that D16 covers.

Listing the refusal OUT rather than IN quietly mandates restoring what `e42cb5a` deleted as a terminal
stall, presents it as settled rather than as a decision anyone weighed, and puts it beyond review by
putting it in the non-goals. The pinned-absence arm will red on this unit's first commit, which is the
signal that the OUT list describes a different tree. The first boundary in that same bullet IS real
and pinned (`unattended.test.sh:2696-2701`), which is what makes the false half hard to spot.

**Fix.** Rewrite the bullet against the base: declarations are append-only today; if S2 and S3
re-introduce a re-declaration branch, the narrowing refusal moves into section 2 as an IN item with
its in-band exit specified. Otherwise leave it deleted and drop AC7.

**Left-shift gate.** Extend the spec-hygiene arm from D1: every behaviour a spec's OUT list calls
"pinned" must name the arm that pins it, and that arm must exist. A pinned ABSENCE and a pinned
PRESENCE are opposite claims, and a spec that confuses them is describing another tree.

## D16 — The docs item reaches two of at least six carriers, and none of the prose that already mis-describes the driver

*(raw ids 13, 26)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:86-87`

The claim S6 falsifies is carried by six sites, all verified: `.unattended.conf:132-144`,
`tools/unattended/.unattended.conf.example:113-125`, `tools/unattended/PROTOCOL.template.md:387`,
`memory/guides/UNATTENDED-PROTOCOL.md:387`, `memory/guides/SESSION-KICKOFF.md:54-58`, and the DARK
report text at `check-unattended.sh:1117`. The docs item names two.

`SESSION-KICKOFF.md:58` is the one that matters most: it is the manifest every session front-loads
and it currently ends "do not treat a green leg as a disjointness proof". Left stale after S6, it is
a governing doc actively lying about the gate's meaning.

Separately, `PROTOCOL.template.md:354-361` and its installed twin
`memory/guides/UNATTENDED-PROTOCOL.md:354-361` still say a re-declaration of an OPEN pass "widens or
no-ops; it never narrows" and that a partly overlapping set "is read as a narrowing and refused".
Both are already false at base — round 4's D10 doc half, unrepaired — and the docs item as scoped
does not reach either. **A run that reads the protocol will believe declaring only the NEW paths
widens its set, which is exactly the shape that reds check 23 once S6 flips grading ON.**

**Fix.** Enumerate all six carriers in the help/docs item, add the two protocol copies' dispatch
paragraph, and state what replaces it: append-only rows, what the graded set is (D3), and what a pass
does when it needs more paths.

**Left-shift gate.** An acceptance criterion asserting no tracked file still claims the grading is dark
once S6 lands — one grep over the tracked tree, run as part of the unit. This is the claims-registry
class already booked as `TOOL-dUnstalledConvoy-16`; the grep is the cheap instance of it.

## D17 — AC4 is already green at HEAD, so it cannot be observed RED and it contradicts AC10

*(raw ids 35, 42)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:98-99`

The D1 sequence already reds at base, two ways verified. The driver is append-only
(`unattended.sh:2420-2425`), so the second declaration parks at a NEW anchor and the fold holds two
distinct keys; row 1's unbounded window still finds the out-of-lane commit and the subset test at
`check-unattended.sh:1202` still fails it. And the sequence is ALREADY an arm: arm C at
`check-unattended.test.sh:1464-1472` is exactly it, and the suite passes (ran shard 2/2: PASS, 187
assertions).

So AC4 passes against the code this unit exists to change. AC10 states without qualification that
"every arm added by this unit was observed RED against the pre-fix code" and names a red-first record
that would have to lie about this one. A green-from-the-start arm in a red-first ledger is the
self-certifying shape round 4 booked as D6 and D9. It stays green post-S1 as well, since the
out-of-lane commit IS the second row's anchor — so the arm is inert in both directions, not merely
redundant, which is also how D6 above got in.

**Fix.** Either drop AC4 as already-held and say so in section 3 (D1 is closed by the REMOVAL, not by
this unit), or re-aim it at the case that is not held: the same sequence with the re-declaration made
at the SAME anchor and no commit between, which is D4's hole. Whichever survives must have an
observed-RED staged break, or AC10 is unmeetable.

**Left-shift gate.** Make the red-first record machine-checkable: each arm it lists names the staged
break and the assertion that failed. An arm that cannot be broken cannot produce that pair, so the
record itself becomes the gate against inert arms.

## D18 — AC4 names the wrong observation site: the leg suite hand-writes every dispatch row

*(raw id 11)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:98-99`

`check-unattended.test.sh` contains no `--dispatch` invocation — the only match is a comment at
`:1437` — and every dispatch fixture is a hand-written row via `drow` (`:1416`) or `drows` (`:1442`).
AC4's sequence (declare narrow, commit out of lane, re-declare wide) is three DRIVER calls, and the
retraction it pins is a driver decision about which anchor to re-park at.

Round 4 named `cross-component.test.sh` as the left-shift site for D1, D2 and D9 for exactly this
reason; that file's own comment at `:104-106` says a fixture hand-writing its rows with `drow`
"cannot see it". No acceptance criterion in this spec observes anything in `cross-component.test.sh`,
so the driver/leg seam — the only place the retraction defect is visible — has no criterion at all.

The site is mis-aimed rather than impossible: the leg suite does invoke the driver elsewhere (`drive`
at `:843`, five `--preflight` calls at `:848-891`), so real `--dispatch` arms could be added there.
The defect is that the seam has no owner.

**Fix.** Move AC4 to `cross-component.test.sh` and add the D9 edit to scope: pass 2 writes inside its
declared lane and commits with a subject naming the unit before the leg runs, keeping the rc=0 and
empty-output assertions.

**Left-shift gate.** A rule worth a checklist entry: **an acceptance criterion that names a driver
sequence must name a fixture that drives the driver.** One grep per criterion — does the named file
invoke the verbs the sequence needs — catches this class without judgement.

## D19 — S5 and AC6 cover half of round 4's normpath class; the trailing `/.` spelling is broken identically

*(raw id 25)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:24-27`, `:102`

Measured by sourcing the library at base: `normpath work/sub/.` returns `work/sub/.` unchanged, and
`covers work/sub/. work/sub/f` is FALSE — identical to the interior `/./` case that S5 and AC6 do
name. `verb_dispatch`'s refusals all pass it: not absolute, `*..*` needs two consecutive dots,
`is_repo_root` is FALSE on `work/sub/.`, no glob metacharacter, no whitespace. So
`--dispatch --writes work/sub/.` parks verbatim at `unattended.sh:2405`, and once S6 turns grading ON
the leg's subset test at `check-unattended.sh:1198` reds on a pass that wrote **exactly where it
declared**.

Round 4's D7 fix said explicitly "and strip a trailing `/.`", and its left-shift gate named
`work/sub/.` alongside `work/./sub`. S5's second one-liner and AC6 name only the interior spelling, so
the arm again contains no instance of the spelling it leaves broken.

**Fix.** Extend S5's `normpath` item to strip a trailing `/.` after the interior collapse, and extend
AC6 to all three spellings round 4's gate named — `work/./sub`, `./work/./sub/` and `work/sub/.` —
with a matching leg-side arm.

**Left-shift gate.** The systematic spelling sweep round 4 left uncovered: one table-driven arm over
the `--writes` spellings, asserting `normpath` is idempotent and that `covers <spelling> <child>` is
TRUE for every spelling of the same directory. `normpath` is on the write path into the record, so
this is one arm's cost for the whole class.

## D20 — AC9's named observation cannot distinguish the flip from no flip

*(raw id 43)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:107-108`

AC9 observes "the dark announcement is gone" by `bash tools/unattended/check-unattended.sh`. Ran it
at base: **0 bytes, exit 0** — and 0 bytes again under `GOV_UNATTENDED_REPORT=1`. The dark
announcement goes through `report()` (`check-unattended.sh:218`), which prints only when `REPORT=1`,
and it fires only for a run-state file carrying `dispatch · item` rows. No tracked RUN.md carries
one; the only matches in `memory/` are review prose and one spec's grammar block.

So AC9's named observation is already true before S6 and stays true if S6 is implemented wrongly,
botched, or skipped entirely. The fixture arms at `check-unattended.test.sh:1600-1612` do
discriminate, but AC9 names the repo-level command, not the suite.

**Fix.** Observe the flip where it is visible: `GOV_UNATTENDED_REPORT=1` over a fixture whose
run-state file carries a dispatch row, asserting the DARK line is ABSENT and a grading verdict is
PRESENT. State the fixture, since the repo's own records supply no dispatch rows.

**Left-shift gate.** A general rule for this leg's criteria: **an observation naming a command must
name a population that command can see.** A one-line probe — does the named command emit any bytes on
this tree — turns a vacuous observation into a visible one before it is written into a spec.

---

# LOW

## D21 — Section 10's reuse audit calls `normpath` "reused unchanged" while S5 and AC6 modify it

*(raw id 46)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:133`

Section 10 lists `covers`, `overlaps`, `normpath` and `id_in` as "all reused unchanged". S5's second
one-liner and AC6 both change `normpath`, which at `lib-unattended.sh:38-47` currently collapses
repeated slashes, a leading `./` and a trailing `/` and nothing else. It is also the shared base of
`covers` (`:52-56`), `overlaps` (`:57`) and `is_repo_root` (`:61-64`), and it is on the write path
into the record (`unattended.sh:2405`), so the audit understates the blast radius of the one change
every other predicate depends on. Low severity precisely because the contradiction sits inside the
section written to catch it.

**Fix.** List `normpath` as MODIFIED with its three dependent predicates named; keep `covers`,
`overlaps` and `id_in` in the unchanged list.

**Left-shift gate.** A hygiene arm that no identifier appears in a spec's Scope section and in its
reuse audit's unchanged list at once. One comparison of two sets, and it fails closed.

---

# Fix order

The five blockers are not independent, and the ordering matters more than usual, because four rounds
have each repaired the previous round's damage in the same forty lines.

1. **Re-ground spec 23 on its own base (D1).** Nothing else in that spec can be judged until section 2
   and section 4 describe code that exists. This is a spec revision, not a code change, and it decides
   whether S2, S3 and S5 survive at all.
2. **Decide the graded set (D3) and the same-anchor hole (D4) together.** They are one question — what
   a unit's several rows mean — asked from the leg side and the driver side. Deciding one without the
   other is what produced the disagreement the library was created to end.
3. **Split S4 into two helpers (D2)**, with headers stating what each does NOT answer, and give the
   driver-side one its acceptance criteria (D9). This is round 4's D5 fix as written, and it is the
   only one of the four that adds a library function.
4. **Then S1's boundary and ordering rules (D6, D7, D8)**, which are the window's actual semantics and
   which currently exist only as a phrase.
5. **S6 last, and conditional.** Flip the default only after D4's negative control is green and D12's
   rollback is a value a project can actually set. F1's resolution — that the flip is reversible — is
   currently resting on a mechanism the spec contradicts itself about. Make the rollback real and F1
   stands; leave it, and F1 is an unsupported argument for shipping a gate four rounds could not make
   correct.

For spec 24: **ship S2 (and its `--abort` sibling) and re-spec S1 against a verified reproduction.**
S2 is the only item in that unit which reaches the flow in this repo's own revision log. S1 and S3 as
written are dead branches, and an arm that goes green over a state the kit cannot enter is worse than
no arm.

**Every one of these lands with its arm in the same commit, and every arm is observed RED before the
fix goes in.** That was round 4's closing instruction, and it is repeated here because AC10 already
promises it while AC4 (D17) cannot deliver it.

## What these specs got right

Stating this is not politeness; it matters for what the next revision should not throw away.

- **Section 4's diagnosis is correct and is the most valuable sentence in either spec.** One predicate
  serving callers whose edges disagree IS what produced four rounds of defects. D2 is that the design
  then does it again one caller shorter, not that the diagnosis is wrong.
- **S1 is the right change.** An unbounded grading window is a real defect, and bounding it is the only
  thing that makes a multi-pass unit gradeable. D6, D7 and D8 are missing rules INSIDE S1, not
  arguments against it.
- **S7 — the red-first discipline as scope rather than as a note — is the correct response to three
  rounds of unarmed repairs**, and it should survive every revision below.
- **Spec 24's S2 is right, cheap, and reaches the recorded incident.** It is the half that works.
- **Both specs pin a BASE and both carry a revision log saying what they were written from.** Spec 23's
  section 9 is what made D1 diagnosable in minutes rather than by bisection, and a spec that admits
  its own provenance is doing the thing this repo asks for.

## Coverage and limits of this review

- Scope was the two spec files at `d9728f89...de766cb3` plus the code they name: `verb_dispatch`,
  `verb_close`, `verb_landed`, `verb_abort`, `refuse_if_terminal`, `check_clean`, `fact`, `set_fact`,
  check 23, check 31, and the whole of `lib-unattended.sh`, read at the specs' own declared base.
- Reproductions ran against the tree at `de766cb3`: ancestry by `git merge-base`, the leg's awk fold
  by piping rows through it, `normpath` and `covers` by sourcing the library, the leg's output by
  running it, `check-unattended.test.sh` shard 2/2 by running it, and the merge that carried
  `BUILDING` by `git cat-file` on this build's own history.
- **Not covered:** the full merge bar was not re-run — the diff is spec-only and touches no gated
  artifact. That is an assumption, not an observation.
- **Not covered:** the adopter suite and the memory-tree leg were not exercised, and no fuzzing of
  `--writes` spellings beyond the four round 4 named plus the trailing `/.` measured here.
- Six raw findings were refuted by the skeptic and are not carried; nothing is outstanding or
  unverified. Three carried findings had one clause each partly refuted, and each refutation is
  written into its section rather than dropped.

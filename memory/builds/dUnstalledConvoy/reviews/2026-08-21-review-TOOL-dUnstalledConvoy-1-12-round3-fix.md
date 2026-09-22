**Serves:** diff-review PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12

# Diff review — round 3's repair, and the five regressions it shipped

**Reviewed range:** `a8bd64a...HEAD` (HEAD = `77d40fc4`, 1 commit, 9 files, +639/-18). **ROUND: 1.**

## Verdict: BLOCKED

**Three blockers, four highs, three mediums.** All ten sit in `verb_dispatch`, in the `sibrows`
filter and the re-declaration branch it feeds, plus one in check 23 and three in the arms that were
supposed to hold them.

The headline is not the count. It is that **five of the ten are regressions from base `a8bd64a`,
verified by running the same sequence against the base commit**, and that **two of them make a check
strictly less able to fail than it was before this diff**. Round 3 was asked to close a stall; it
closed that stall and opened two more, one of which lets an unattended run erase its own check-23
failure with a single extra driver call and no owner turn.

## Review shape

- **raw 22 · confirmed 20 · refuted 2 · unverified 0 · precision 0.91.**
- After dedupe the 20 confirmed collapse to **10 distinct defects: 3 BLOCKER, 4 HIGH, 3 MEDIUM.**
  Four of the ten were reached independently by four lenses each, which is what a 54-line hunk with
  three load-bearing branches produces. Each section names the raw ids that reached it.
- **One merge carried a downgrade and it is recorded in bold at that section (D4, blocker to high).**
  One merge kept the higher of two ratings (D7, low and high, merged high). Nothing else moved.
- Every defect below was reproduced against the tree — most on the kits' own fixtures, one by
  mutation. Two impact narratives were partly refuted by their own verifiers, and both refutations
  are written into the sections rather than dropped.

### Where round 3 stands against its predecessors

Round 1 fixed 16 and introduced 5. Round 2 fixed 10 and introduced 3, one of them a terminal stall.
Round 3 fixed 8 and introduced 5, one of them a self-certifying proof. **The introduction rate is not
falling.** Every round has repaired the previous round's damage in the same forty lines and produced
new damage there, which is what a single function carrying three disagreeing predicates does to
anyone who edits it. That is a design observation, not a scolding, and it is the argument for the
sequencing note at the end of this report.

### The class this review was told to hunt, and found

Three defects made a check less able to fail than it was at base:

- **D1** lets a driver call retract a check-23 red that had already been emitted. The check goes from
  rc=1 to rc=0 over the same violating tree.
- **D6** left round 3's own leg-side repair unarmed: reverting it leaves both suites green at
  byte-identical assertion counts.
- **D9** added an arm named for the driver/leg disagreement seam in which neither pass ever commits,
  so the seam is never entered — and `FLOOR_ASSERTIONS` was ratcheted 13 to 19 on the strength of it.

---

## D1 — BLOCKER · the post-hoc widening rewrite, re-opened

`tools/unattended/unattended.sh:2261` (with `:2322` and `:2371`) · raw ids 1, 11

Round 3's intersection filter drops a row from `sibrows` only when the pass's commit **overlapped the
row's declared set**. A pass that committed entirely **outside** its lane therefore stays open — which
is precisely the pass that just produced a check-23 failure. `cur` at line 2322 reads that same
filtered set, finds the row, `_shares` matches on the path the declaration already carried, and `park`
at line 2371 re-parks the widened row **at the original anchor**. check 23 folds rows last-wins per
`(group, unit)` (`check-unattended.sh:1064-1068`), so the narrow declaration stops being graded.

**Reproduced end to end.** Declare `--writes work/a` at anchor `4c388f25`; commit `work/b/x.txt` under
a subject naming `ARCH-tRun-1`. The leg reds: `check 23 FAILED — ... ARCH-tRun-1 ... wrote
work/b/x.txt`, rc=1. Then issue `--dispatch --pass ARCH-tRun-1 --writes work/a --writes work/b`. The
driver prints `dispatch WIDENED`, parks a second row under the same key at the same anchor, and the
leg goes **rc=0 with empty output**. The same sequence against base `a8bd64a` prints `dispatch
declared` at a **new** anchor and stays RED at both points, because there `pass_commit` alone closed
the row and `cur` was empty.

**Sharpest form, also reproduced:** pass P1 declares `work/a` and writes into sibling P2's declared
`work/b`. Once P2 commits inside its own lane, P2's row closes; condition 1 only sees OPEN siblings,
so it no longer refuses; P1 then widens into `work/b`. The cross-lane collision the verb exists to
prevent is laundered green.

**Three artefacts now assert something false in exactly the violating case:** the comment at
`unattended.sh:2352-2363` ("once the pass has COMMITTED, `sibrows` no longer carries its row, `cur` is
empty, and this branch is not reached at all"), the comment at `check-unattended.sh:1058-1062`, and
the paragraph this diff added to both `PROTOCOL.template.md:354-358` and
`memory/guides/UNATTENDED-PROTOCOL.md:354-358` ("Once that pass has COMMITTED ... is recorded as its
own row rather than judged against the previous one"). The disjointness proof is self-certifying.

**Fix.** Do not let one predicate serve both consumers. Keep the intersection-filtered set for
condition 1's conservative disjointness, and key the re-declaration lookup on RAW openness — the
leg's own reading of "has this pass committed". Emit two streams from the `sibrows` loop (or a marker
column): a row is a condition-1 sibling when the filter says its work has not landed, but it is
RE-DECLARABLE only while `pass_commit` returns nothing at all. Minimal form, immediately before line
2350: `[ -n "$cur" ] && pass_commit "$curgrp" "$unit" "$rel" >/dev/null && cur=""`. Do **not** move
the filter into `pass_commit` — check 23 needs it permissive as an attribution oracle.

**Left-shift gate.** `cross-component.test.sh`: drive the out-of-lane commit, assert the leg reds;
drive the widening; assert the leg **still** reds and that the second row parked at a **different**
anchor. This is a negative control on a gate's ability to fail, which is the one arm shape this build
keeps discovering it lacks (§7, "a gate you have only ever seen pass is an assertion about nothing").

---

## D2 — BLOCKER · check 23 grades a row against the NEXT pass's commit

`tools/unattended/unattended.sh:2347` (with check 23's window in `check-unattended.sh`) · raw ids 5, 16

Round 3's overlap gate deliberately lets one unit park a second row at a new anchor when the sets are
disjoint — that is B2's repair and it is correct. But check 23 opens each row's window as
`anchor..HEAD` and takes the FIRST commit naming the unit (`lib-unattended.sh:79`). So when pass 1
produced no change — the case M6 explicitly sanctions and check 23's own no-change branch exists for —
row 1 is graded against **pass 2's** commit, which is outside row 1's declared set.

**Reproduced verbatim from arm 3b's own sequence.** Declare `ARCH-tRun-1 --writes work/spec`, commit;
declare `ARCH-tRun-1 --writes work/build`, commit (both accepted, two rows as intended); then let the
pass write inside its **own second lane**, `work/build/x.txt`, committed as `ARCH-tRun-1 builds its
lane`. The leg reds: `UNATTENDED check 23 FAILED — a dispatched pass committed a path outside the set
it declared before dispatch ... ARCH-tRun-1 at e616cfd8 wrote work/build/x.txt`. The `(group, unit)`
key does not disambiguate overlapping windows.

**Round 3 traded a terminal driver refusal for a terminal merge-bar red.** Both end an unattended run.
This one ends it *after the work is already committed*, and it is discovered at the push boundary
with no owner turn to clear it.

**This defect and D1 currently hold each other up.** The only in-band escape from D2 that I could find
is D1's post-hoc widening — widening row 1 to cover `work/build` clears the red, confirmed. So fixing
D1 alone makes D2 unconditionally terminal. They must land together; see "Fix order" below.

**Fix.** Bound each row's grading window above by the NEXT anchor recorded for the same unit. In check
23, instead of `pass_commit "$dsgrp" "$dsunit" "$f"` over `<anchor>..HEAD`, stop at the anchor of the
next `(group, unit)` row for that unit — `dsrows` is already folded and ordered — so a row whose pass
produced no change is graded over an empty window and takes the existing no-change branch. Until that
lands, the driver must not park a second row for a unit whose predecessor row is still open.

**Left-shift gate.** Extend `cross-component.test.sh` arm 3b past line 122 with a real write commit
for the second pass and keep the `rc=0` / empty-output assertions. That arm reds today, which is the
arm doing its job. This is the same edit D9 requires, so one change arms both.

---

## D3 — BLOCKER · `cur` is `tail -1`, so a widening of the older row parks a third row silently

`tools/unattended/unattended.sh:2326` · raw id 8

Once the overlap gate permits two open rows for one unit (D2's precondition, and B2's intended
behaviour), `cur` selects by recency, not by match. Widening the **older** row is therefore neither
recognised nor refused: `cur` picks the newer row, `_shares` finds no overlap, `cur` is blanked at
line 2347, and the call falls through to `park` at the current anchor.

**Reproduced from arm 3b's own state.** With rows `74cdd778 ARCH-tRun-1 · reason work/spec` and
`30e2784f ARCH-tRun-1 · reason work/build` both open, `--dispatch tRun --pass ARCH-tRun-1 --writes
work/spec --writes work/spec-extra` prints `unattended: dispatch declared — 0ea58ec7 ARCH-tRun-1 ·
work/spec work/spec-extra` — **not** `WIDENED` — rc=0, and RUN.md now holds three rows with the narrow
`work/spec` row untouched at its original anchor.

The operator is told the declaration landed. The anchor-reuse invariant the whole widening design
rests on — the widened row keeps the superseded row's anchor — is silently skipped, and check 23 goes
on grading the stale narrow row. After the pass commits both declared paths the leg reds terminally
with two `check 23 FAILED ... wrote work/spec-extra/b.txt` lines, rc=1. This reaches the same terminal
leg red as D2 **without any no-change pass**.

**Fix.** Select `cur` by best match rather than by recency: among the unit's open rows, pick the one
whose declared set overlaps the incoming set, preferring a row already at `$grp`. Refuse rather than
park when two open rows of the same unit both overlap the incoming set — which one is being widened
is then undecidable, and a guess there is a mis-grading nobody can see.

**Left-shift gate.** A fixture that opens two disjoint rows for one unit and widens the FIRST,
asserting `dispatch WIDENED` and a row count of 2. Note that a row-count assertion is what caught
this: B2's existing `grep -c ... = 2` check is the right shape and simply is not run on this path.

---

## D4 — HIGH · the narrowing test compares raw argv against a now-normalised record

`tools/unattended/unattended.sh:2368` · raw ids 2, 6, 12, 17

Round 3 normalised `want` at lines 2313-2316 and parks the normalised spelling — B3's repair, and
correct. It left the read-back comparison at line 2368 on the raw `"$@"`:

```
for q in $curpaths; do
  for p in "$@"; do [ "$p" = "$q" ] && continue 2; done
  fail 49 "--dispatch re-declares a pass with a path the earlier declaration carried and this one drops ..."
```

`$curpaths` is now normalised; `"$@"` is not. So a **widening that repeats the same literal argument
it originally declared** is refused as a narrowing, naming a path the caller never dropped and never
spelled that way.

**Reproduced.** `--writes work/sub/` parks `work/sub`. The legal widening `--writes work/sub/ --writes
work/other` — the same literal argument, plus one — exits 1 with `check 49 FAILED — ... widening is
the repair, narrowing is not: work/sub for ARCH-tRun-1`. The canonical spelling `--writes work/sub
--writes work/other` prints `dispatch WIDENED`. `./work/one` fails identically. Against base
`a8bd64a` the respelled widening printed `dispatch WIDENED`, because both sides were raw.

The adjacent no-op test at line 2364 (`[ "$curpaths" = "$want" ]`) correctly compares the normalised
`want`, which is why this fires **only** on the widening path — and why B3 (parks a spelling, never
re-declares) and B2 (declares only bare `work/one work/two`) both miss it.

**Raised as BLOCKER by one lens and downgraded to HIGH here, on evidence from two of its own
verifiers:** re-declaring with the normalised spelling repairs it in band, and the refusal text even
prints the normalised form, so a run that reads its own error can recover. That is a real difference
from round 2's stall, which had no in-band exit. It is still HIGH and not lower: an autonomous loop
re-issues the argument it holds, it has no canonicalisation step, and the message actively
misdiagnoses the failure as a narrowing the caller did not perform.

**Fix.** Compare normalised to normalised: `for p in $want; do [ "$p" = "$q" ] && continue 2; done`.
`want` already holds exactly the normalised tokens and whitespace paths are refused upstream, so
word-splitting is safe here.

**Left-shift gate.** Extend B3 past its parked-spelling assertion: re-declare `--writes work/sub/
--writes work/other` and require `dispatch WIDENED` plus `miss` on `narrowing is not`. The existing
narrowing arm cannot catch this because every path in it is already canonical — the arm passes by
containing no instance of the shape it would need.

---

## D5 — HIGH · the openness filter examines only the FIRST candidate commit

`tools/unattended/unattended.sh:2248` · raw id 7

`pass_commit` returns the first qualifying commit only, and round 3's filter tests **that one commit's
diff** against the row's declared set. If that first commit missed the lane, no later in-lane commit
is ever examined, so the row never closes — even after the pass has committed its entire declared
set. Every later declaration overlapping that lane is then refused, terminally, while the leg is
entirely silent about it.

**Two reproduced triggers, neither exotic, with a control.**

(a) **The documented widening repair.** Declare `work/one`, widen to `work/one work/two` — both rows
sit at the same anchor and BOTH stay in `sibrows`, because the driver does not fold by `(group, unit)`
the way check 23's awk does. The pass then writes only `work/two/y.txt`. The superseded narrow row
never overlaps that commit and stays open forever; `--dispatch tRun --pass ARCH-tRun-2 --writes
work/one` is refused with `check 49 FAILED — ... work/one also in 6c2a30c5 ARCH-tRun-1`, legrc=0.

(b) **The `git add -A` declaration commit that B1 itself calls "the ordinary commit shape".** Declare
`work/shared`, commit RUN.md plus `work/unrelated.txt`, then write `work/shared/y.txt` and commit.
Pass 1 is complete and entirely in-lane, yet `ARCH-tRun-2 --writes work/shared` is refused
identically. **Control:** with a clean declaration commit the same sequence is admitted (`dispatch
declared — ... ARCH-tRun-2 · work/shared`), so the extra file is the whole difference.

This is the driver refusing what its own leg calls legal — the direction the kit's own protocol calls
terminal. Stale open rows also leak into `sibpaths`, so the generated-index refusal fires against
long-finished passes too.

**Fix.** Make the openness question scan forward rather than stopping at the first candidate: iterate
every commit in `<anchor>..HEAD` whose subject names the unit and whose diff, minus the run-state
file, intersects the row's declared set; close the row on the first such commit. Keep `pass_commit`
unchanged — it is check 23's attribution oracle. Add a second library helper, e.g.
`pass_commit_in_set <anchor> <unit> <rel> <declared…>`, and call that from the filter. Additionally
fold `sibrows` by `(group, unit)` keeping the last row, as check 23 already does, so a superseded
narrow row cannot outlive its widening.

**Left-shift gate.** Two driver arms: the `git add -A` declaration commit carrying one extra tracked
file, and the widen-then-write-only-the-new-lane sequence — each asserting a later sibling
declaration is ADMITTED. Both need the control (clean declaration commit admitted) beside them, or
the arm cannot distinguish "admitted because correct" from "admitted because nothing was checked".

---

## D6 — HIGH · round 3's own leg-side repair is unarmed, mutation-verified

`tools/unattended/check-unattended.sh:1141` · raw id 18

The `case` to `covers` change is held by nothing. **Mutation-verified in the repo:** replacing line
1141's `covers "$dsp" "$dsq" && { dsok=1; break; }` with the original `case "$dsq" in
"$dsp"|"$dsp"/*) dsok=1; break ;; esac` leaves `check-unattended.test.sh` at PASS (259 assertions)
and `cross-component.test.sh` at PASS (19 assertions) — byte-identical to the baselines taken before
mutating. File restored, `git status` clean.

Round 3's own driver-side fix is what disarmed it: the driver now parks normalised spellings, so no
fixture in either suite ever presents the leg with a row it must normalise. The leg change is the
half that also repairs rows written by an OLDER driver, which is the half that cannot be reached
through the driver at all.

The record's stated left-shift for this blocker was "arms on BOTH sides" plus a class-level assertion
that `check-unattended.sh` has at least one `covers`/`overlaps` call site. **Neither exists.**
Grepping both across all three suites returns comment prose and the driver-side M1 arm
(`unattended.test.sh:2565-2571`), and nothing asserting the leg has such a call site.

**Fix and left-shift gate (the same edit).** Add a `check-unattended.test.sh` arm using `drow
ARCH-tRun-1 "work/sub/"` — hand-written, bypassing the driver — with a commit writing
`work/sub/f.txt`, asserting the leg is silent. Add the class-level arm the record asked for: assert
the leg script contains at least one `covers` or `overlaps` call site, mirroring the two-arm GIT-pin
discipline at `unattended.test.sh:1567`.

---

## D7 — HIGH · `normpath` does not collapse an interior `/./`, and B3's arm covers two spellings of three

`tools/unattended/lib-unattended.sh:43` (arm at `tools/unattended/unattended.test.sh:2560`) · raw ids 14, 19

`normpath` collapses repeated slashes, a leading `./` and a trailing `/`, and nothing else. So
`--dispatch --pass ARCH-tRun-2 --writes work/./sub` clears every driver refusal — not absolute, no
`..`, no glob metachar, no whitespace, `is_repo_root` false — and parks **verbatim**: `reason
work/./sub`. Verified by sourcing the library directly: `normpath work/./sub` returns it unchanged,
and `covers work/./sub work/sub/f.md` is false. The pass then writes exactly where it declared and
the leg reds: `check 23 FAILED ... wrote work/sub/f.md`.

This is the same permanent-red that round 3's `covers` fix was written to remove, surviving in the
one spelling the normaliser does not reach — and it now sits on the **write path into the record**,
which is new in this diff.

B3's arm asserts only `reason work/sub work/other$`, so it **contains no instance of the spelling it
leaves broken**, and the fix's own class claim ("THE RECORD CARRIES ONE SPELLING") is false as
written.

**Merged at the higher of the two ratings (low and high). One impact claim is refuted and recorded
here:** an in-band repair does exist — re-declaring `--writes work/./sub --writes work/sub` is
accepted as a widening, reuses the anchor, and the leg then goes quiet. "No in-band repair" was
wrong. The accepted-spelling-that-reds-the-leg defect and the unarmed class both stand.

**Fix.** Add an interior-`.` pass to `normpath` after the slash collapse and before the trailing-slash
strip: loop while the path matches `*/./*`, replacing `/./` with `/`, and strip a trailing `/.`.
Order it after the `//` collapse so `.//./x` reduces correctly.

**Left-shift gate.** Extend the normpath unit arm with `work/./sub`, `./work/./sub/` and `work/sub/.`,
and add `work/./sub` to B3 **and** to a matching leg-side arm — the class here spans both components,
which is the lesson D6 already paid for.

---

## D8 — MEDIUM · the empty-proof announcement measures a different population than the proof

`tools/unattended/unattended.sh:2270-2271` · raw ids 4, 9, 13, 22

The new liveness line fires when `sibrows` is empty. Condition 1's loop then discards the declaring
unit's OWN rows at line 2295 (`case "$sib" in *" $unit · reason "*) continue`). So whenever the unit's
own open row is the only open row, the loop iterates **zero** siblings and the announcement stays
silent — the guard tests a strict superset of the population it claims to be asserting liveness for.

**Reproduced with stderr isolated.** The first `--dispatch ... --writes work/one` prints `unattended:
dispatch — no sibling pass is open, so condition 1 is a proof over an empty set for ARCH-tRun-1`. The
follow-up `--writes work/one --writes work/two` prints `dispatch WIDENED` on stdout and **nothing on
stderr**, having compared against zero rows. Declaring the same unit with a disjoint set behaves the
same way.

This is not an exotic state: **every re-declaration and every widening in a single-unit run reaches
it**, and arm 3b's own second declaration hits it too. A proof over nobody stays byte-indistinguishable
from a proof over somebody, which is the exact property the announcement was added to remove, and the
§7 class the hunk's own comment cites as its justification.

Severity is MEDIUM because the refusal logic itself is correct — only the probe is blind — and the
narrower openness-regression class the comment also names (where `sibrows` empties entirely) is still
covered.

**Fix.** Derive the announcement from the population condition 1 actually iterates. Compute the
sibling set once with the own-row exclusion applied — e.g. `sibs=$(printf '%s\n' "$sibrows" | grep -v
-F -- " $unit · reason ")` — announce on **that** being empty, and feed the condition-1 loop from the
same variable so the message and the proof cannot disagree.

**Left-shift gate.** The existing announcement arm asserts only the first-declaration case. Add a
re-declaration/widening arm asserting the announcement is still emitted. A probe's arm must cover the
states the probe is supposed to be watching, not the one state where it happens to work.

---

## D9 — MEDIUM · arm 3b passes by containing no instance of what it names

`tools/unattended/cross-component.test.sh:121-122` · raw ids 10, 21

Arm 3b's header says it exists because the driver/leg disagreement "is invisible to either suite
alone". Both of its commits touch **RUN.md only** (`ARCH-tRun-1 declare dispatch`, `... declare second
dispatch`), and `pass_commit` filters the run-state path — so neither row ever has a pass commit,
check 23 takes the `no commit names this pass and none of its declared paths moved` branch for both,
and that branch is a `report`, silent unless `GOV_UNATTENDED_REPORT=1`. **The attribution and subset
path at `check-unattended.sh:1112-1145` — the only place driver and leg can disagree — is never
entered.** The arm's two `same ... "$rc" "0"` / `"$out" ""` assertions hold regardless of how the leg
grades.

Confirmed by instrumenting the arm with `GOV_UNATTENDED_REPORT=1` and reading both report lines. Not
merely vacuous: adding `mkdir -p work/build && printf 'x\n' > work/build/x.txt` plus a commit naming
the unit before `leg` reds immediately — `check 23 FAILED ... wrote work/build/x.txt` — which is D2.
The arm is green over a seam that is actually broken, which is the precise class its own header claims
to close.

`FLOOR_ASSERTIONS` was raised 13 to 19 in the same commit that added the arm (confirmed in git
history), so the floor was ratcheted on six assertions of which the two load-bearing ones cannot fail.

**Fix and left-shift gate (the same edit).** After line 118, have pass 2 write inside its declared
lane, commit with a subject naming `ARCH-tRun-1`, push, and only then run the leg — keeping the `rc=0`
and empty-output assertions. Once D1 and D2 are fixed the arm passes; today it reds, which is the
point. Consider also making the arm assert it entered the subset path at all (run it once under
`GOV_UNATTENDED_REPORT=1` and `miss` on the no-change report line), so a future change cannot quietly
route it back into the silent branch.

---

## D10 — MEDIUM · the re-declaration gate is nested inside "did HEAD move", and both protocol docs now describe a discriminator the code does not use

`tools/unattended/unattended.sh:2342` · raw id 20

The disjointness escape at line 2342 sits inside `if [ "$curgrp" != "$grp" ]`, so it only runs once
HEAD has moved. A legal disjoint second pass declared **before any intervening commit** is still
refused as a narrowing.

**Reproduced.** With no commit between the two calls, `--dispatch tRun --pass ARCH-tRun-6 --writes
work/spec` then `--writes work/build` yields `check 49 FAILED — ... narrowing is not: work/spec for
ARCH-tRun-6`. Inserting `git add -A && git commit` between them makes the same pair print `dispatch
declared`. `--dispatch` only STAGES the run-state file, so a run that batches its declarations — or
whose first pass produced no change and therefore committed nothing — hits this.

**Both existing arms step around it.** B2 at `unattended.test.sh:2543` and cross-component arm 3b both
insert `git add -A && git commit` between the two declarations, which is exactly the condition that
hides the residual.

**And the binding documents now positively mis-describe the code.** `PROTOCOL.template.md:354-361` and
`memory/guides/UNATTENDED-PROTOCOL.md:354-361`, both amended in this diff, say the driver distinguishes
the two cases by set overlap and mention no HEAD condition. The code's own adjacent comment states it
unconditionally too. That is the two-answers-to-one-question class the library was created to end,
reintroduced in prose in the same commit that removed it from code.

**Fix.** Drop the `curgrp != grp` guard and gate on overlap alone: a disjoint set is a new pass whether
or not HEAD moved. A narrowing is a strict subset and still overlaps, so the refusal is preserved
untouched. If the guard is kept instead, both documents and the comment must be corrected to describe
the actual discriminator — but the code change is smaller than the doc change and removes the
divergence rather than documenting it.

**Left-shift gate.** An arm for the no-commit-between shape asserting `dispatch declared` and two
parked rows. Refusal is the conservative direction, but in a run with no owner turn it is still a
stall, and this build's whole subject is stalls.

---

## Fix order for round 5

The two blockers D1 and D2 are coupled and **must land in one commit**. D1's escape is currently the
only in-band exit from D2, so repairing D1 alone converts D2 from "recoverable by an illegal widening"
into an unconditional terminal red at the push boundary. Suggested order inside that commit:

1. **check 23's window** — bound each row above by the next anchor for the same unit (D2). This is the
   change that makes multi-pass units gradeable at all, and every driver-side fix below assumes it.
2. **Split the two predicates** — condition 1 keeps the intersection-filtered set; the re-declaration
   lookup keys on raw `pass_commit` openness (D1). Leave `pass_commit` itself alone.
3. **`cur` selection by best match, not `tail -1`**, refusing the undecidable two-overlap case (D3).
4. **The scan-forward openness helper** (D5), which is the only one of the four that adds a library
   function.

Then the three one-liners, in any order: normalised comparison at 2368 (D4), interior-`.` in
`normpath` (D7), the announcement's population (D8), and dropping the `curgrp != grp` nesting (D10).

**Every one of these lands with its arm in the same commit, and every arm is observed RED before the
fix goes in.** Three rounds have now each shipped a repair that nothing held — round 3 proved it for
its own three by reverting each with the suite still green, and then shipped a fourth (D6) with the
same property. That is the pattern to break, and it is cheaper to break with a red-first discipline
than with another round.

## What round 3 got right

Stating this is not politeness; it matters for what the next round should not undo.

- **The call-site tightening was the correct call.** Pushing the intersection filter into
  `pass_commit` would have made check 23 report an out-of-lane pass as "a pass that produced no
  change" — the check going green on the exact defect it exists to catch. The commit message's design
  verdict on that is right, and D1's fix must preserve it.
- **`normpath` collapsing repeated slashes before stripping the leading `./` is correct** and was found
  by the arm written for the function, which is the argument for writing arms for library functions.
  D7 is a missing case in it, not a reversal.
- **B2's overlap gate genuinely closed round 2's stall.** The legal second pass of one unit now
  declares. D2 and D3 are consequences of that being correct while check 23 and `cur` were not updated
  to match, not arguments for reverting it.
- **Arm 3b is the right idea in the right file.** It is the only place the driver/leg disagreement is
  visible at all. D9 is one missing commit inside it, not a case against the arm.

## Coverage and limits of this review

- Scope was the diff at `a8bd64a...HEAD` plus the callers and callees of every hunk in it: the whole
  of `verb_dispatch`, `lib-unattended.sh`, check 23, and the three suites' affected arms.
- Reproductions ran on the kits' own fixtures and on scratch fixtures built from the cross-component
  scaffolding. Base comparisons ran the identical sequence against `a8bd64a` in a separate tree.
- **Not covered:** the adopter suite, the memory-tree leg, and the rest of the merge bar were not
  re-run for this review — the diff does not touch them, and that is an assumption, not an
  observation.
- **Not covered:** no fuzzing of `--writes` spellings beyond the four this report names
  (`work/sub/`, `./work/one`, `work/./sub`, `.//x`). `normpath` is now on the write path into the
  record, so a systematic spelling sweep is worth one arm's cost and does not exist yet.
- Two raw findings were refuted by the skeptic and are not carried here; nothing is outstanding or
  unverified.

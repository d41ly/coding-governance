**Serves:** spec-audit TOOL-aBatchedArm-3

# Tier-2 spec audit — TOOL-aBatchedArm-3, ROUND 4

*The third fold audit, and the first SCOPED one. Round 3 (BLOCKED, eight blocker rows over nine
defects, precision 0.42) graded rev-4; rev-5 is the fold of round 3's two blockers and one high, and
this round grades THAT fold only. Because round 3's precision fell below the ~0.5 line `AGENTS.md`
§8 sets, the lenses were primed on the sections the fold touched and nothing else: §2 S5 and S6, §6
AC4, AC8 and AC9, and the base bump. The rest of the spec was read three times by rounds 1 to 3 and
was NOT re-read for new findings here; a zero against any section outside that scope is not a
measured zero. Node `a`, 2026-09-13, ROUND 4. Every finding below survived a skeptic prompted to
REFUTE it, and every suite line cited was re-read at the spec's declared base `0422ea2e` by the
author of this report rather than transcribed from a lens: the three helpers at `:57-59`, the `ahead`
push at `:1243` and the absence of any deletion of it, `reset_tree`'s body at `:240-246`, the `trunk`
push at `:3046-3047`, the check-16 block from `:1404` to its control at `:1513` (thirteen
`reset_tree` lines, twelve cycles, zero `mutate()` calls), the floor grade at `:3167`, the sharded
epilogue at `:3227` and the PASS line at `:3228`, the `ls-remote --heads` at
`check-unattended.sh:912` and the `ADV_TIPS` comment at `:1026`, `SHARD_ARITY=2` at `:29`, the
`reset_tree` call-line count, two shared-needle counts, and the cited rulings in
`TOOL-aShardedFloor-3` (§3, §5, AC2), `memory/gotchas/ab-arm-never-did-the-work.md` and
`memory/guides/BUILD-METHOD.md:140`.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md`@`51c5645bf24f3a05decb3631aa5b860758f6968f` — rev-5, the fold of round 3. ROUND 4. Scoped to §2 S5, §2 S6, §6 AC4, AC8, AC9, and the base line.

Facts this round rests on, each checked in the tree rather than in the spec: `refs/heads/ahead` is
pushed at `check-unattended.test.sh:1243` and `reset_tree` clears only `refs/remotes/` and
`refs/replace/`; the `still clean after nine mutations` control is at `:1513` and its block starts at
`Nine branches, nine arms` at `:1404`; `check-unattended.sh` reads every remote head via
`ls-remote --heads` on every run; `TOOL-aBatchedArm-4` is CLOSED at `0422ea2e` with `--pooled` and
the substring `--kit` filter; at that base `SHARD_ARITY` is 2, so `--shard 1/2` and `2/2` are valid
direct invocations there.

## Verdict: BLOCKED

Four rows at BLOCKER, three at HIGH, five at MEDIUM. Those twelve rows collapse to **seven distinct
defects**; the table below names which rows share one, so a fold that repairs a defect repairs every
row under it. Severity here is adjudicated by this report, not carried from the pipeline: BLOCKER
means that built or graded exactly as written the spec yields a wrong verdict, or a Definition of
Done that cannot be met without breaking one of its own binding non-goals; HIGH means a measurement
or observation the spec relies on cannot distinguish the case it exists to catch; MEDIUM is
placement, anchors, records and cost. Two rows the pipeline confirmed at HIGH (id=2, id=8) are
BLOCKER under that definition, and B2 says why.

Two defects are blockers, both inside the S5/AC8 pair the fold rewrote. **The KEPT/DROPPED oracle is
blind** (D-1): S5 decides whether a boundary owes a replay by comparing the shard's `FAIL` SET with
and without it, and forbids the state scan from deciding. But the suite's helpers print ONLY on
failure and only the needle text (`:57-59`), so an arm already red at BASE, a green arm whose needle
a red sibling already prints, a `miss` or `same` control gone vacuous, and a failure that moved
between two fixtures sharing one needle all leave the set byte-identical — and a needed replay is
DROPPED with a verdict that reads as derived. `TOOL-aShardedFloor-3` AC2 rejected verdict comparison
for this exact file and this exact question, and §10 does not dispose of it. **AC8's third clause
cannot pass** (D-2): it asks each `--shard <i>/8` to run GREEN with the kept set, while §3 says the
suite is RED at BASE, the reds belong to `aQuenchedHarness-9` and `aHoistedPass-38`, and this unit
must not move a verdict; every index carrying a red arm exits 1 and the only way to green it is
forbidden. That is round 3's B1 shape again — a criterion with no satisfiable outcome — written into
the clause the fold added.

Two defects are HIGH. **AC4's ten timed arms carry no completion witness** (D-3): at BASE every run
exits 1 whether it finished or aborted, the count prints only on a PASS line, and the two direct
`--shard i/2` invocations are graded by `date +%s` alone — the class
`memory/gotchas/ab-arm-never-did-the-work.md` records, on the reading that decides the owner's arity
ruling. **§3's "must not change any arm's verdict" has no observation for the delete** (D-4): the
origin-side delete changes what `ls-remote --heads` advertises to every arm after `:1249` in the
UNSHARDED run, AC6 compares sharded against unsharded at one commit where both sides carry it, and
`TOOL-aShardedFloor-3` §3 ruled this fix OUT of a split unit without §10 superseding that ruling.

The medium rows: the delete's placement inside `reset_tree` is one spawn per call, roughly three
hundred per unsharded run, on the unit whose deliverable is wall, and it loads the eight-shard side
of AC4's ratio and not the two-shard side (D-5); `trunk` at `:3046-3047` is a second leak of the
class S5 calls "one real leak", and AC8's `names no refs/heads/ahead` stays green with it open (D-6);
and §1, §4, §5 and F2 still say the two readings are taken "at the same commit", the design AC4 and
the rev-5 log reject (D-7).

S6 and AC9 drew no confirmed finding: the block's own `MUT_EXPECTED`, the per-cycle increment, and
the assertion BEFORE `run` match the file (twelve cycles, zero `mutate()` calls, control at `:1513`).
The base bump to `0422ea2e` drew none: `TOOL-aBatchedArm-4` is CLOSED there with `--pooled` and the
substring `--kit` filter. Both are measured zeros under a run where nothing died, for the lenses that
ran.

**Convergence.** Under `memory/guides/BUILD-METHOD.md` (`:140`) the loop re-arms only on a STRICTLY
SMALLER confirmed-blocker count. Round 3 stood at eight blocker rows; this round stands at four. By
the rule's letter the loop RE-ARMS. Read by defect it is flat — two blocker defects in round 3, two
here — but not the same two. Round 3's B2 (the typed nine) is CLOSED by rev-5 and stays closed;
round 3's B1 (AC8 unsatisfiable under a read-keyed rule) was folded into a verdict-keyed rule that is
unsatisfiable for a different reason and blind for a third. The distance left is one oracle and one
clause. **Disposition of both standing blockers: FOLD.** Each fix lies inside S5 or AC8, each is a
rule the build already has the artifacts to apply, and neither needs a mechanism this build lacks.
Nothing here needs a PROMOTE.

## Review shape

- raw 30 · confirmed 12 · refuted 18 · unverified 0 · precision 0.40

Precision fell from 0.42 to 0.40 despite the scoping, so narrowing the SECTIONS did not lift it. The
refuted eighteen were not handed to the author of this report and are not characterised here. Read
the confirmed count with the table in hand: the pipeline reports zero duplicates because each row
addresses a different clause, but two lenses hit the S5 oracle (two rows), two hit the AC8 green
clause (two rows), two hit AC4's missing witness (two rows), two hit the missing §3 observation (two
rows), and two hit the delete's placement (two rows). Twelve rows is seven defects.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete FOR THE SCOPE THE LENSES WERE PRIMED ON, and a fold may treat the UNVERIFIED
bucket as genuinely empty. Sections outside the scope were not graded this round and carry no zero
of any kind from it.

## The seven defects, and which rows carry each

| Defect | Rows (severity as adjudicated here) | Section |
|---|---|---|
| D-1 · S5's KEPT/DROPPED oracle compares `FAIL`-line SETS printed only on failure, so a needed replay is DROPPED with a verdict that reads as derived; `aShardedFloor-3` AC2 already rejected this comparison for this file | id=1 blocker · id=23 blocker | B1 |
| D-2 · AC8's "runs green at each index" is unsatisfiable at the landing commit under §3 | id=2 blocker · id=8 blocker | B2 |
| D-3 · AC4's ten timed arms carry no completion witness; a truncated arm is a short wall that decides the arity | id=5 high · id=25 high | H1 |
| D-4 · the delete lands with the re-cut, §3's "must not change any arm's verdict" has no observation for it, and `aShardedFloor-3` §3 is undisposed | id=24 high · id=6 medium | H2 |
| D-5 · the delete inside `reset_tree` is one spawn per call on ~296 call lines, and loads only the eight-shard side of AC4's ratio | id=19 medium · id=28 medium | M1 |
| D-6 · `trunk` at `:3046-3047` is a second leak of the same class; "one real leak" is wrong by one and AC8's clause is instance-shaped | id=18 medium | M2 |
| D-7 · §1, §4 (twice), §5 and F2 still say "at the same commit"; round 3's H1 fix reached AC4 only | id=12 medium | M3 |

## Round 3 against the fold, item by item (scoped)

- **B1 (AC8 unsatisfiable: `ahead` and `trunk` leaks; read-keyed rule non-empty everywhere)** —
  rev-5 moved the rule from "which refs are read" to "which replays change the verdict", conceded
  that the read scan cannot decide (the checker reads every head by `ls-remote`), and closed the
  `ahead` leak in `reset_tree`. RIGHT that the read scan cannot decide. WRONG on the oracle it chose
  instead (B1 here), WRONG on the green clause it added (B2), INCOMPLETE on the leak class (`trunk`,
  M2), and the delete's placement and observation are defects the fold created (M1, H2).
- **B2 (S6 types 9 against 12 cycles)** — folded: the block declares `MUT_EXPECTED` beside its first
  cycle, every `reset_tree`-led cycle increments `MUT`, the control asserts before `run`, and "nine"
  is named as the arm count. Verified against the block at `:1404-1513`. RIGHT. Not re-graded; no
  confirmed finding on S6 or AC9.
- **H1 (AC4's two readings "at the same commit" cannot coexist)** — folded in AC4: the two-shard
  reading is two concurrent direct `--shard i/2` invocations at BASE on the same frozen clone, which
  is valid there (`SHARD_ARITY=2` at `:29`). RIGHT on AC4. INCOMPLETE: the other sites round 3 named
  still say "same commit" (M3), and neither reading carries a witness that it ran (H1 here).
- **M5 (base predates the runner)** — folded: base bumped to `0422ea2e`, where `TOOL-aBatchedArm-4`
  is CLOSED with `--pooled` and the substring `--kit` filter. RIGHT. Not re-graded.

Round 3's M1, M2, M3, M4 and M6 are outside this round's scope and are not graded here; the rev-5
log does not claim them folded, and nothing in this report says whether they are.

---

# BLOCKERS

## B1 · id=1, id=23 — S5's KEPT/DROPPED oracle compares `FAIL`-line sets printed only on failure, so a needed replay is DROPPED with a verdict that reads as derived

**Address:** section 2 S5 (`:56-69`, the rule "KEPT at every boundary where removing it changes the
shard's `FAIL` set, DROPPED where it does not", and "the scan ... never decides whether one is
owed"); section 6 AC8 (`:214-222`, "every DROPPED one is one whose removal did not"); section 10
(`:304-305`, `aShardedFloor-2` and `-3` "REUSED (the contract and the block-edge cut rule)").

The oracle. S5 runs each boundary's shard WITH and WITHOUT its replay and compares the two `FAIL`
sets; identical sets mean DROPPED, and the ref/variable/function scan is explicitly demoted to
informing the replay's CONTENT. The comparison is therefore the only thing standing between a bare
shard and a green-by-absence pass. What it can see is bounded by what the helpers print, and at BASE
they print this and nothing else:

- `hit()` — `FAIL missing: <needle>` (`:57`); `miss()` — `FAIL unexpected: <needle>` (`:58`);
  `same()` — `FAIL <label>: expected [..], got [..]` (`:59`). No line number, no arm index, no
  output. A green arm prints nothing.

Four cases leave the set byte-identical whatever the replay does, and each exists in the file today:

1. **An arm red on both sides.** §3 declares the suite RED at BASE and forbids repairing it
   (`TOOL-aHoistedPass-38` has three causes OPEN at `memory/backlog/TOOL.md:415`; the
   verb-documentation arm's own comment at `:510` says it "reds on a tree nobody has touched"). An
   arm that fails with and without the replay contributes the same line to both sets. If the replay
   is what that arm NEEDS — its BASE failure masking a second, replay-shaped one — the set does not
   move, the replay is DROPPED, and the shard reds "correctly" until `aQuenchedHarness-9` or
   `aHoistedPass-38` repairs the first cause, when it reds again as THEIR regression.
2. **A green arm whose needle a red sibling already prints.** Needles are shared: this report's two
   greps over the base file count 22 and 31 texts asserted by more than one arm (the sibling review
   measured 38 with a broader pattern; the exact figure is not load-bearing, any count above zero
   is). A set of texts cannot tell "arm A failed on `<needle>`" from "arm B failed on `<needle>`".
3. **A `miss` or `same` control gone vacuous.** 101 `miss` arms and 27 `same` arms at BASE, all
   silent when green. A bare-shard state that makes the checker refuse EARLIER than the arm expects
   turns a `miss` into a pass for the wrong reason — `TOOL-aHoistedPass-38` cause 1 records exactly
   this suite's `miss` arms already "asserting absence against a tree that already talks" — and both
   sets stay identical. The replay whose absence caused it is DROPPED. This is the green-by-absence
   class §7 names, and AC6 and AC8 are both blind to it because the shard is green on both sides.
4. **A failure that moves between fixtures sharing one needle.** Arm 6b's three fixtures
   (`:1482-1494`) assert one text; a set collapses them, so a removal that shifts the failure from
   fixture 2 to fixture 3 is a no-op to the oracle.

And this was already ruled on, for this file, for this question. `TOOL-aShardedFloor-3` AC2 (rev-2,
F7): rev-1's per-arm PASS/FAIL vector "has the SAME blindness to an arm passing for the wrong reason
(PASS in both runs)", "this suite's helpers print only on failure", therefore "compare STATE, not
verdicts", plus `aShardedFloor-2` AC9's per-arm byte comparison. rev-5 S5 makes the verdict
comparison the SOLE decider and demotes the state scan, and §10 disposes `-2`/`-3` as REUSED for the
contract and cut rule only — AC2 is neither reused nor superseded. A spec that reverses a sibling's
ruling has to say so and say why; this one does not know it did.

**Fix.** Three changes, all inside S5/AC8/§10 and none needing a RED repair:

- Make the FAIL comparison the KEEP trigger, never the sole DROP trigger. A DROP additionally
  requires the shard's per-arm OUTPUT to be byte-identical with and without the replay — every
  `$(run)` capture, written by a `run()` that appends to a per-invocation log under an env var, the
  artifact `aShardedFloor-2` AC9 and `-3` AC2 already prescribe. Identical output vectors mean the
  replay changed nothing an arm saw; identical FAIL sets mean only that nothing it saw was printed.
- Compare the ordered FAIL SEQUENCE keyed on arm identity, not a set of texts: add
  `${BASH_LINENO[0]}` to the three helpers' FAIL lines (one word each at `:57-59`), or at minimum
  compare the multiset (`sort | uniq -c`). State in AC8's red-when that a verdict taken over a set
  containing the needle of an arm red at BASE is VOID, and that the arms red at BASE are listed in
  the build log from the BASE run so a reader can see which boundaries the oracle could not vote on.
- Dispose of `aShardedFloor-3` AC2 in §10 — SUPERSEDED-in-part, with the reason: the read scan was
  found undecidable because the checker reads every head, so the verdict comparison is ADDED to the
  state comparison, not substituted for it.

**Left-shift gate.** The per-invocation output log is the gate: a staged bare-shard run whose output
vector equals the whole run's for the same arms proves the boundary needs no replay, and a diff names
the arm and the line. It reds on case 3 today (the `miss` that passes for the wrong reason prints
nothing, but the checker output it grepped differs) and on case 4 (the fixture that failed is in the
log). Record it per boundary in the build log as a table — boundary, FAIL-sequence delta,
output-vector delta, verdict — so a reader can see an empty FAIL delta beside a non-empty output
delta and know the replay was KEPT for the right reason.

## B2 · id=2, id=8 — AC8's "runs green at each index" is unsatisfiable at the landing commit under §3

**Address:** section 6 AC8 third clause (`:217`, "`check-unattended.test.sh --shard <i>/8` at each
index runs green with the kept set in place"); section 3 (`:87-88`, "Repairing the suite's
pre-existing RED ... This unit must not change any arm's verdict"); section 6 AC6 (`:206-210`).

The clause reads literally: each of the eight shards, with its kept replays, exits 0. §3 says the
suite is RED at BASE, that the reds belong to `TOOL-aQuenchedHarness-9` and `TOOL-aHoistedPass-38`,
and that this unit must not move any arm's verdict. Verified at BASE `0422ea2e`: the suite exits
`$st` (`:3229`), set to 1 by any `FAIL`; the verb-documentation arm at `:510` "reds on a tree nobody
has touched" and assigns its fix to `aQuenchedHarness-9`; the two
`pedit 's/^Ten kit-owned core items\./…'` fixtures at `:1961` and `:1966` no-op against a protocol
that says "Twelve" at BASE (`UNATTENDED-PROTOCOL.md:324`, `aHoistedPass-38` cause 3, OPEN). Each of
those arms lands in SOME shard on every candidate cut, and that shard exits 1. So the clause fails at
one or more indices at every landing commit this unit can produce, and the only way to make it pass
is the repair §3 forbids. AC6, two criteria up, already presumes a non-empty `FAIL` set —
"identical to the unsharded `FAIL` set at the same commit" — so the spec states both that the shards
carry FAILs and that they exit 0.

The consequence is not a wrong build but a DoD with no satisfiable outcome: the builder either
strikes the clause at build time, a spec edit no review saw, or reads every pre-existing FAIL as
this unit's defect and starts repairing arms it does not own. Round 3's B1 was the same shape — a
criterion that could only fail — and the fold wrote a new one into the clause it added. Severity is
BLOCKER by this report's definition (a DoD that cannot be met without breaking a binding non-goal)
rather than the HIGH the pipeline carried; the fix is one clause, but severity prices the impact,
not the edit.

**Fix.** Replace "runs green with the kept set in place" with "reproduces, for its region, the
unsharded run's `FAIL` sequence at the same commit, with the kept set in place" and point at AC6 as
the owner of that observation. Green is not the reference; the unsharded run's FAIL sequence
restricted to the shard is. Add to AC8's red-when: "a shard whose FAIL sequence differs from the
unsharded run's for its arms".

**Left-shift gate.** The same per-invocation log as B1: the shard's FAIL sequence, filtered to its
region's arms, diffed against the unsharded run's. One `diff` per index in the build log, and it
cannot be satisfied by repairing a RED, because a repaired arm changes the unsharded side too and
AC6 catches it.

---

# HIGH

## H1 · id=5, id=25 — AC4's ten timed arms carry no completion witness; a truncated arm is a short wall that decides the arity

**Address:** section 6 AC4 (`:186-201`; the two direct invocations "timed with `date +%s`", the
record carrying "all eight shard walls", the red-when on the 0.5 ratio); section 4 (`:113-116`, "The
ratio of eight's longest shard to two's longest decides the arity"); F2 (`:252-254`).

AC4 is a comparison: two walls at BASE, eight after S1, and the ratio of the longest to the longest
reverses the owner's arity ruling at 0.5. Every arm records seconds and nothing else. At BASE the
suite is RED (§3), so every run exits 1 whether it completed or aborted — a `set -u` unbound, an
`exit 2` refusal, a mid-run `exit 1` — and the assertion count prints only on the PASS line
(`:3228`) or on a floor breach (`:3167`). The two direct `--shard i/2` invocations are graded by
`date +%s` alone; the eight pooled rows by the runner's `SWEEP of N` line, which proves dispatch and
not completion, and its per-row rc-plus-seconds. The pooled runner does name bound-kills and
wall-kills, so a killed row is visible; an aborted one is not.

The failure mode is directional. A refusal at BASE — `--shard 1/8` mistyped where the arity is 2
refuses in milliseconds, before `mktemp -d` — or an early abort on the two-shard side reads as a
tiny "two-shard longest", eight's ratio lands at or above 0.5 by construction, and F2's fallback
lowers the arity on a measurement of how long it took to fail.
`memory/gotchas/ab-arm-never-did-the-work.md` records this class with a documented check — "every
arm of a comparison asserts the WORK it did, not only the time it took", to be run "over any diff
that adds a measurement" — and AC4 is that diff. The verified per-process `mktemp` of `TMP`,
`ORIGIN_DIR` and `TMPBIN` means the two concurrent BASE invocations do not collide, so the missing
witness is the only liveness gap here; but it is the whole gap.

**Fix.** AC4 requires a positive artifact per arm beside its seconds. For each direct invocation:
the log ends with the unconditional sharded epilogue `(this leg ran shard i/2 only; the other region
was NOT exercised here)` at `:3227`, AND its FAIL sequence equals that shard's BASE baseline. For
each pooled row: the runner's own per-row verdict line, the same epilogue in the row's log, and the
same FAIL-sequence match. A wall without its artifact is recorded as NO READING, never as a number,
and AC4 is red on any missing artifact. State whether the AC1 count runs and the AC4 timed runs are
the SAME invocations, or say why not.

**Left-shift gate.** A `tail -1` over each arm's log grepped for the epilogue, in the build's own
measurement script, red on absence. It is the gotcha's documented check made mechanical for this
unit; the gotcha file is where a reader will look for it, so name the script there when it exists.

## H2 · id=24 (high), id=6 (medium) — the delete lands with the re-cut, §3's "must not change any arm's verdict" has no observation for it, and `aShardedFloor-3` §3 is undisposed

**Address:** section 2 S5 (`:66-69`, "One real leak is fixed on the way ... `reset_tree` gains the
origin-side delete"); section 4 Rollout (`:138-139`, "S1, S3, S5 and S6 land together"); section 6
AC6 (`:206-210`) and AC8 second half (`:218-219`); section 3 (`:88`); section 10 (`:304`).

The delete is a behaviour change to the UNSHARDED run. `check-unattended.sh:912` runs
`ls-remote --heads` on every `run()` and fixes `ADV_TIPS` from it for the whole run (`:1026`), so
after the delete every arm from `:1249` to exit sees an advertisement without `refs/heads/ahead`
where at BASE it saw one with it. §3 binds "must not change any arm's verdict". Nothing observes
that for the delete: AC6 compares sharded against unsharded at ONE commit, where both sides carry
the delete; AC6's second clause reads only the pre-split COUNT; AC8's second half checks only that
the ref is gone. A verdict flip with an unchanged count — the class the count clause cannot see —
lands silently. By reading, no arm after `:1244` references `$ahead` and the ref's only non-`main`
ancestor is itself, so the flip is unlikely; that is an assertion, and `aShardedFloor-3` §5 rules
for this exact suite that such a question is settled "by RUNNING both shards, never by reasoning
about it".

And the placement was ruled on. `aShardedFloor-3` §3: "No fix to the leaked `refs/heads/ahead`"
inside a split unit, because touching the fixture while splitting it makes the split unreviewable;
its AC2 asked for a named negative showing some arm READS the leak before treating it as more than a
risk, and that negative was never produced. rev-5 folds the delete into the same landing as the
re-cut (Rollout: S1, S3, S5, S6 together) and §10 disposes `-3` as REUSED for the cut rule only.
Round 3's B1 itself proposed the delete, so the delete is not the defect; landing it unobserved and
unseparated, against a ruling the spec cites and does not supersede, is. id=6 is the observation
half of this on its own and sits at MEDIUM; id=24 carries the rollout coupling and the undisposed
ruling and sits at HIGH.

**Fix.** Land the delete as its own commit BEFORE S1's re-cut, so the split is reviewed against a
fixture that already has it. Add one line to AC6 (or AC8): the multiset of FAIL texts from the
unsharded run at the landing commit equals the multiset from the unsharded run at BASE — red when
any text appears, disappears or changes count. The BASE side is free: AC4's two-shard BASE reading
already produces it, and sibling `TOOL-aBatchedArm-1` AC3 already diffs against a recorded red
baseline in this shape. Supersede `aShardedFloor-3` §3 explicitly in §10, with the reason (the
verdict-keyed rule needs a bare shard to start from whole-run state, and the leak is the one
difference that cannot be replayed away).

**Left-shift gate.** The BASE-vs-landing unsharded FAIL diff, recorded once in the build log. With
B1's per-invocation output log in place it is the same diff over the output vector, which also
catches a flip the FAIL text cannot show.

---

# MEDIUM

## M1 · id=19, id=28 — the delete inside `reset_tree` is one spawn per call on roughly three hundred call lines, and loads only the eight-shard side of AC4's ratio

**Address:** section 2 S5 (`:68`, "`reset_tree` gains the origin-side delete"); section 6 AC4
(`:199-201`, the ratio) and AC8 (`:218-219`).

`reset_tree` (`:240-246`) is four git spawns with the ref work batched through ONE
`update-ref --stdin`, and its own header says why: "a git process per ref per arm dominates this
suite's wall time". The origin is a separate bare git-dir (`$ORIGIN`, `:177`), so an origin-side
delete cannot ride that batch and is one more process per call. This report counts 296 `reset_tree`
call lines at BASE (`grep -cE '^\s*reset_tree(\s|;|$)'`), two of them inside `anchor_break` and
`anchor_restore`, which are themselves called many times more. One site creates the ref (`:1243`).
At the spec's own ~190 ms per fork that is about a minute per unsharded run; at the 751 ms per git
spawn this node's own memory records for node `a`, it is nearer four
(`memory/gotchas/process-creation-is-the-suite-cost.md` records the suite's cost AS spawn count). And
it is asymmetric: AC4's two-shard reading is taken at BASE, before the delete exists, while the
eight-shard reading carries roughly forty extra spawns per shard — so the placement pushes eight's
longest wall UP against a two-shard wall that does not carry it, toward the 0.5 line that lowers the
arity. One row's "every S3 floor moves with it" is wrong — floors are assertion counts, not timings
— but S2's serial readings are timings and do.

**Fix.** Delete once, where the ref is made: `git push -q origin :refs/heads/ahead` (or
`git --git-dir="$ORIGIN" update-ref -d refs/heads/ahead`) immediately after the `hit` at the text
`is not an ancestor of HEAD` (`:1245`). One spawn per run, the identical "a bare shard starts from
the state the whole run would have" property, and AC8's `ls-remote` observation holds unchanged. If
`reset_tree` must own it, guard the spawn with a builtin test — `[ -e "$ORIGIN/refs/heads/ahead" ]`
— so it costs a process exactly once. Say which was chosen and why in S5.

**Left-shift gate.** S2 itself: a serial reading taken before and after the delete lands, recorded
beside the placement. A placement that moves a serial reading by more than one spawn's worth is in
the wrong place, and the reading is already owed.

## M2 · id=18 — `trunk` at `:3046-3047` is a second leak of the same class; "one real leak" is wrong by one and AC8's clause is instance-shaped

**Address:** section 2 S5 (`:66`, "One real leak is fixed on the way"); section 6 AC8 (`:218-219`,
"names no `refs/heads/ahead`").

At `:3046-3047`, `git branch -f trunk main` and `git push -q origin trunk` leave `refs/heads/trunk`
on the origin AND a local `refs/heads/trunk`; `reset_tree` clears neither (local `refs/remotes/` and
`refs/replace/` only, and `reset --hard` moves HEAD's branch). Every arm after `:3047` sees `trunk`
in the checker's `ls-remote --heads`, and a boundary after `:3047` inherits it on both sides — the
same class as `ahead`, which round 3's B1 named alongside it. S5's count is therefore wrong by one,
and AC8's observable is written for the instance: `names no refs/heads/ahead` stays green with
`trunk` on the origin, and a third push of this shape lands unseen. The row's other half — that
local `refs/heads/main` is "un-reset the same way" — is wrong: `main` is deliberately stateful, it
is the carrier the existing `SH_I = 2` replay exists for, and it is not a leak. The `trunk` instance
stands on its own.

**Fix.** State the CLASS in S5 — every `refs/heads/` ref on either side that its own block does not
restore — and name both instances. Make AC8's clause class-shaped: after a reset, `ls-remote --heads`
on the fixture origin names exactly `refs/heads/main`, and `for-each-ref refs/heads/` locally names
exactly `main` and `unit`. That reds on `trunk` today, which is the point. Close `trunk` the same way
as `ahead`: one delete after `:3047`'s block, at its producing site (M1).

**Left-shift gate.** The class-shaped AC8 clause IS the gate, staged and observed RED on `trunk`
before the delete lands. A new origin-side push then reds it the day it is written.

## M3 · id=12 — §1, §4 (twice), §5 and F2 still say "at the same commit"; round 3's H1 fix reached AC4 only

**Address:** section 1 (`:19`, "a two-shard reading taken at the same commit"); section 4
(`:112-113`, "AC4 takes TWO readings at the same commit: the two-shard pooled wall BEFORE S1
lands"); section 4 Alternatives (`:148`, "AC4 measures it at the same commit"); section 5 perf
(`:159`, "measured twice at one commit"); F2 (`:253`, "AC4's two-shard reading at the same commit");
against section 6 AC4 (`:190-193`) and the rev-5 log (`:266-268`).

AC4 and the rev-5 log say the two readings CANNOT coexist across the arity change, and that the
two-shard reading is two direct invocations at BASE, the eight-shard reading after S1 — two commits,
one frozen clone. Five sites still state the design the fold rejected, and §4 still calls the
two-shard reading a POOLED wall, which the spec itself says the runner cannot take at BASE because
no shard row exists there. Round 3's H1 named those sites and its fix was to replace "the SAME
commit" everywhere; the fold changed AC4 only. A builder following §4 or F2 takes a reading that
cannot exist, or reads AC4 as the typo.

**Fix.** At the five sites, replace "at the same commit" with "on the same frozen clone, at BASE for
two and at the landing commit for eight" — the clone is the like-with-like guarantee, not the
commit — and in §4 replace "the two-shard pooled wall" with "the two-shard direct pair".

**Left-shift gate.** None mechanical for prose agreeing with prose; the §6 rule ("a value stated
beside the source that owns it rots") and a fold checklist line — "every site round N named, not
only the AC" — which would have caught this one.

---

## What a fold should do first

B1 and B2 are one artifact and one clause. The artifact is the per-invocation output log
`aShardedFloor-2` AC9 already prescribes: with it, DROPPED means "the output vector did not move",
KEPT means "the FAIL sequence did", and the sequence is keyed on arm identity by one word in each of
three helpers. The clause is AC8's "runs green", which becomes "reproduces the unsharded FAIL
sequence for its region" and stops contradicting §3. Do the §10 disposition of `aShardedFloor-3`
AC2 and §3 in the same edit, because the next round will look for it.

H1 is a `tail -1 | grep` per arm and the sentence "a wall without its artifact is no reading". H2 is
a commit boundary — the delete before the re-cut — and one AC6 line diffing the unsharded FAIL
multiset at landing against BASE, which AC4's BASE reading already produces.

The medium rows land in one records commit: the delete moved to its producing site with a `trunk`
sibling (M1, M2), AC8's clause made class-shaped (M2), and the five "same commit" sites (M3).
Precision this round was 0.40 against 0.42, so narrowing the sections did not lift it; the next fan
should be primed with rev-5's S6, AC9 and base bump as CLOSED and by-design, and with this report's
seven defects as the only open surface, so it hunts the fold and not the history.

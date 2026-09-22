**Serves:** spec-audit DEPL-dSealedTally-1 DEPL-dSealedTally-5 TOOL-dSealedTally-1

# Spec audit round 2 — dSealedTally

Tier-2 · node d · 2026-09-04 · a re-audit of the three units the rev-2 fold amended, before any of
them opened for building.

**ROUND 2** over three subjects, each pinned at the blob it was read at:
[DEPL-dSealedTally-1](../spec/2026-09-04-spec-DEPL-dSealedTally-1.md)@`61b0e5743490` ·
[DEPL-dSealedTally-5](../spec/2026-09-04-spec-DEPL-dSealedTally-5.md)@`67c50b2cc0ed` ·
[TOOL-dSealedTally-1](../spec/2026-09-04-spec-TOOL-dSealedTally-1.md)@`ddf9c2f4af36`.

## Verdict: BLOCKED

Three blockers stand, and all three are in text the rev-2 fold added. `DEPL-dSealedTally-1`'s fix
for round 1's B2 sources its widened baseline from a call site that a `--write` run never reaches,
so the mechanism cannot execute in the only mode where a baseline exists. `DEPL-dSealedTally-5`'s
fix for round 1's B5 pins `apply` to a vintage that `apply` has no parameter for and silently
discards, while §4 Files touched still names only the self-test — the fix is unimplementable at the
declared scope. `TOOL-dSealedTally-1`'s fix for round 1's B4 asserts a closed population of four
backlog rows and misses a fifth OPEN one, whose decided second half no acceptance criterion grades.

Each is the round-1 finding it was written to close, one level over. That is the shape of the whole
round: the fold rewrote prose against the round-1 report rather than against the code the prose now
names, so five of the ten findings below are defects in sentences that did not exist at rev-1. The
repairs are all cheap and none of them changes what a unit is for.

## Review shape

| Raw | Confirmed | Refuted | Unverified | Precision |
|---|---|---|---|---|
| 43 | 18 | 25 | 0 | 0.42 |

Precision 0.42 is still under the ~0.5 floor §8 sets, and barely moved from round 1's 0.40 despite a
narrower subject set. The refuted 25 again clustered on reachability guesses about `govkit.py`
internals. The lesson round 1 drew — prime the finders with the structure of the file, not only with
the prose that describes it — was not applied, so it carries forward to round 3 unchanged.

Nothing came back unverified. Every finding here survived a skeptic asked to refute it, and I
re-checked the load-bearing address of every one against the working tree before writing it up.

## The 18 confirmed collapse to 10 distinct defects

Five clusters re-reported one defect each from different lenses. They are merged below rather than
listed separately, because a report that counts one defect three times misprices the set.

| Merged into | Confirmed ids folded in |
|---|---|
| B1 | 12, 26, 41 |
| B3 | 38 |
| H1 | 2, 14 |
| H4 | 22, 31 |
| M1 | 24, 35 |
| M2 | 23, 25, 34, 40 |

The remaining four — B2 (28), H2 (19), H3 (20), L1 (37) — each came back once.

## Severity as adjudicated here

The counts in the table below are this report's, not the review fan's. One finding carries a
severity different from the one the fan assigned, for a stated reason.

- **Raised to HIGH — H3, the real-root invocation outside `run()`.** The fan called it medium. It
  makes `DEPL-dSealedTally-5`'s AC1 unreachable by S1's own stated mechanism, which is the class
  round 1 graded at high in H4 and H12. Not a blocker, because the arm reds visibly during
  implementation rather than shipping green — round 1's own rule when it lowered H9.

Two merges deserve a note. M2 absorbs a finding the fan graded low (the `2427`/`2428` off-by-one)
into a medium, because in the merged form it is not a stylistic mis-address: taken literally it
inserts a statement inside another statement's line continuation. H1 stays high rather than rising
to blocker even though it is round 1's H10 returning unchanged, because it has a stated cheap fix
and needs no design decision — the bar round 1 used to separate its blockers from its highs.

| Severity | Count |
|---|---|
| BLOCKER | 3 |
| HIGH | 4 |
| MEDIUM | 2 |
| LOW | 1 |

## The findings at a glance

| # | Sev | Unit | Address | The defect |
|---|---|---|---|---|
| B1 | blocker | `DEPL-dSealedTally-1` | §2 S1, §4 Inventory row 1, §10 | the widened baseline is sourced from a call a `--write` run never reaches |
| B2 | blocker | `DEPL-dSealedTally-5` | §2 S4, §6 AC6, §4 Files touched | `apply` has no vintage argument, so the pin is parsed and discarded |
| B3 | blocker | `TOOL-dSealedTally-1` | §10 backlog paragraph, §6 AC1 | a fifth OPEN row exists, and its decided second half is ungraded |
| H1 | high | `DEPL-dSealedTally-1` | §6 AC5 | the containment mutation still cannot fail |
| H2 | high | `DEPL-dSealedTally-5` | §3, §4 Inventory row 2, §6 AC5 | the declared population is a `grep -c` line count, wrong by ~2.5x |
| H3 | high | `DEPL-dSealedTally-5` | §2 S1, §4 Inventory row 4 | a real-root `update` runs outside `run()` and stays unpinned |
| H4 | high | `TOOL-dSealedTally-1` | §2 S3, §4 Inventory row 3 | the guard S3 hoists already precedes every write in that verb |
| M1 | medium | `TOOL-dSealedTally-1` | §2 S1, §5, §6 | `stage_or_fail` still returns non-zero after the terminal write |
| M2 | medium | `TOOL-dSealedTally-1` | §4 Inventory, §2 S1 | two wrong addresses in the table rev-2 added to fix addressing |
| L1 | low | `DEPL-dSealedTally-1` | §5 observability | a deleted landing prints as `restored` in the rollback order |

---

## Blockers

### B1 — the widened baseline is sourced from a call a `--write` run never reaches

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §2 S1 ("from
the existing `derive_unclaimed_candidates` call at `govkit.py:6276`"), §4 Inventory row 1
("`derive_unclaimed_candidates` preview | 6276 | before the snapshot — supplies S1") and the §4
Design paragraph that reasons from that call's printed output, plus §10's reuse claim.

**Defect.** `govkit.py:6276` sits inside `if not write:` at 6275, a branch that ends `return
r.emit()` at 6285. A `--write` run never executes it. It is also the only call site of the function
in the file. So on the only path where a snapshot, a baseline or a rollback exists, nothing widens
`touched_kits`, a landed-only kit still gets no pre-write baseline, and round 1's B2 returns.

**Why it is real.** Verified three ways. `grep -n derive_unclaimed_candidates tools/govkit/govkit.py`
returns the definition at 6203, the stale comment at 6270 and exactly one call, at 6276. Reading
6275-6285 confirms the branch returns. And the function returns `[x[0] for x in _land], _ref` at
6260 — destination paths with the `_eid` discarded — while `touched_kits` at 6347 is a list of kit
ids, so even a reachable call could not supply what S1 asks of it. Three supporting sentences fall
with it. §4's "it says so in its own output today" cites the caveat printed at 6277-6279, which only
a read-only run emits. §10's "reuses the classifier rather than deriving the landed set twice" is
false already: the write path at 7020-7185 re-inlines the whole classifier — the same `for _eid in
(kits or claimed)` walk, the same four skips, the same containment call — rather than calling it.
And the code's own comment at 6270, "ONE IMPLEMENTATION, TWO CALLS", is the trap the author fell
into; grep says one call. The spec was written from that comment.

**Fix.** Rewrite S1 to say the write path ADDS a `derive_unclaimed_candidates(set())` call between
6286 and the snapshot at 6319, and that the function's return shape changes to `(dest, eid)` pairs
so it can feed `touched_kits`. Correct the §4 Inventory row to name that new site rather than 6276.
Strike the "it says so in its own output today" clause. Decide and state whether the inline copy at
7020-7185 is refactored onto the shared function or left as a second implementation, and correct
§10 accordingly — the two answers have different merge bars. Add both the new call and the
return-shape change to §4 Files touched, which currently budgets ~80 lines for a widening rather
than for a new call plus a signature change with a second consumer.

**Left-shift.** Round 1 already named the regression arm — a fixture whose only change is a landed
source, kit check forced red, asserting the run reaches its rollback report — and that arm is the
gate here too, provided it runs under `--write`. The generalisable half is a `gotchas/` class
record: *a spec that sources a value from an existing call site states the MODE that call site runs
in, and greps for its call count rather than trusting a comment.* That record puts both halves of
this defect on every future reviewer's checklist via
`python tools/memory-tree/gotchas.py --for-diff`. Independently, correct or delete the 6270 comment
in the same commit — it is a stale prose claim beside the source that owns it, the class §6 names.

### B2 — `apply` has no vintage argument, so the pin is parsed and discarded

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §2 S4 ("the
fixtures that `apply` at gov HEAD apply at the PIN instead, so each receipt's `gov_commit` IS the
pin"), §6 AC6, against §4 Files touched.

**Defect.** `apply` takes no vintage. `main` dispatches `cmd_apply(root, target, mode, kits,
resume=RESUME)` at `govkit.py:8358` with no `TO_REV`; neither `cmd_apply` at 4169 nor `_cmd_apply`
at 4184 has such a parameter; and `_cmd_apply` hardcodes `commit = git(root, "rev-parse",
"HEAD").strip()` at 4199, which is the value written as the receipt's `"gov_commit"` at 5061.
`parse_args` accepts `--to` at 7986, so `apply --to <pin>` parses cleanly and is thrown away.

**Why it is real.** Verified at every one of those lines. The consequence is exact: no harness change
can make a receipt's `gov_commit` equal the pin, so in the detached-merge case the pin stays an
ancestor of `gov_commit`, `demand_forward_vintage` at 4129 tests `merge-base --is-ancestor HEAD pin`,
that is false, and the run refuses — which is precisely what round 1's B5 said. Meanwhile §4 Files
touched names only `tools/govkit/selftest.py` and §3 lists no product change as out of scope. The
spec therefore contradicts itself: S4 and AC6 require a product capability that does not exist,
inside a unit declared to touch no product code.

**Fix.** Pick one and say which, because the two have different merge bars. Either scope the product
change in: `cmd_apply`/`_cmd_apply` take `TO_REV`, stamp it as `gov_commit`, and the change gets its
own AC and its own gate leg, with `tools/govkit/govkit.py` added to §4 Files touched and the unit's
tier re-checked. Or restate S4 as the fixture writing `gov_commit` into the receipt directly after
`apply` returns, which keeps the unit inside `selftest.py` and makes AC6 constructible as written.

**Left-shift.** The enabling defect is gateable and worth gating: a flag that parses but is never
read. An arm over `parse_args` asserting that each verb's accepted-flag set is consumed on that
verb's own path would have caught `apply --to` before any spec relied on it. If the dispatch table
is too dynamic for a static check, the cheap version is a `gotchas/` record — *a flag that parses is
not a flag that is honoured; grep the verb's implementation for the variable before designing around
it* — which costs one file and reaches every reviewer.

### B3 — a fifth OPEN backlog row, and its decided second half is ungraded

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` §10, the
backlog-rows paragraph added by the rev-2 fold, and §6 AC1.

**Defect.** §10 asserts a closed population — "`memory/backlog/TOOL.md` carries FOUR rows on this
defect" — and misses `TOOL-dTieredTribunal-28`, OPEN at `memory/backlog/TOOL.md:262`. That row is
squarely on this defect and decides a fix in two halves; the spec adopts the first and not the
second. The unadopted half is "add an arm asserting that a refused `--landed` leaves `RUN.md`
byte-identical".

**Why it is real.** The row exists at line 262 and reads, in part, that `unattended.sh --landed`
mutates before it validates, observed 2026-08-27 — five rows, not four. The unadopted half bites,
because S1 deliberately keeps the phase write AFTER every other fact write: `landed-anchor` at
`unattended.sh:2405`, `unpushed-at-landing` at 2409 and `units-at-landing` at 2425 all still land
before it, each with its own `|| return 1`. A refusal at any of those sites leaves `RUN.md`
materially changed, while AC1 and AC4 grade only the `phase:` value and the absence of
`landed-anchor` — so the spec passes its own acceptance set while failing the criterion the corpus
decided. §10 also tells the next reader which rows close, so `-28` would stay OPEN, uncounted and
invisible. Its instance also makes §5's "four instances across three nodes" and §4's "the four
wedged records" undercounts. This is round 1's B4 repeating: the unit lands narrower than the
corpus already decided.

**Fix.** Cite `TOOL-dTieredTribunal-28` in §10 and place it in the closes/stays-OPEN list. Strengthen
AC1 to the criterion that row decided — the run-state file is BYTE-IDENTICAL after a refused
`--landed`, not merely `phase: LANDING` with no anchor — which forces the other three fact writes
below the checks as well, or forces the spec to say in §3 why they stay above. Re-derive §4's and
§5's instance and node counts from five rows.

**Left-shift.** This one is mechanically gateable and would have caught round 1's B4 too. A spec-lint
leg that, for each path in a spec's §4 Files touched, greps `memory/backlog/<FAMILY>.md` for OPEN
rows naming that path, and reds when §10 cites none of them. The rows already carry file paths and
the specs already carry a Files-touched list, so the check is a join over two files that exist. Pair
it with the stronger AC as the regression arm: a forced refusal at each of the four write sites,
asserting `RUN.md` is byte-identical.

---

## High

### H1 — the containment mutation still cannot fail

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §6 AC5,
against §2 S5 and §4 Migration.

**Defect.** AC5 asserts that deleting the `demand_contained_dest` call from the landed restore branch
makes the AC1 arm FAIL. It does not. The function is pure validation: it raises on an escaping path
and otherwise returns `dest`, and the rollback call site at `govkit.py:6869` discards the return
value. For a contained destination — which AC5 itself concedes is the only kind the arm can carry,
because the landing refuses an escaping one at 7085-7114 before writing — removing the call changes
no observable outcome. The arm passes with and without it.

**Why it is real.** Verified at `govkit.py:748` (definition) and 6868-6872 (the bare call inside a
`try`, return discarded). This is round 1's H10 returning: that finding said AC5 was unconstructible,
the fold rewrote it, and the rewrite has the same shape. A criterion that cannot fail records the
containment guard as reached while proving nothing about whether the DELETE path into a foreign
repository is guarded — the exact false-confidence class this build exists to drain, and a direct
breach of §7's "a new gate is not landed until its failing case has been observed".

**Fix.** Rewrite AC5 around an observation rather than around code deletion. Two workable shapes: the
arm monkeypatches `demand_contained_dest` to record its `where` string and asserts a call carrying
the landing's reason string from S5; or the fixture stages a `snap_rows` entry whose landed path
escapes — built directly in the fixture rather than through the landing, which refuses one — and
asserts the run emits the `rolling back kit ... refusing to touch` refusal, with the mutation turning
that refusal into a delete outside the target.

**Left-shift.** A documented §10 checklist entry, since the class is not gateable in general: *an
acceptance criterion whose kill is "delete the call" names what OBSERVES the call, and a criterion
over a function whose return value every caller discards is a criterion over nothing.* Round 1
raised the same class once already; a checklist entry is what stops it coming back a third time.

### H2 — the declared population is a line count, wrong by roughly 2.5x

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §4 Inventory
row 2 and the §3 sentence "32 of the 74 do", against §6 AC5.

**Defect.** The Inventory declares that 32 of the 74 `update` invocations already carry an explicit
`--to`. The 74 is right; the 32 is a `grep -c -- '--to'` line count that includes comment and
check-description lines. The real figure is 13 `--to` argument occurrences, of which 11 sit on a line
also carrying `"update"`.

**Why it is real.** Measured on the tree. `"update"` occurs exactly 74 times in
`tools/govkit/selftest.py`; `"--to"` occurs exactly 13 times; 32 is the count of LINES matching
`--to`. Of the 13, 11 are `update` invocations (2721, 2736, 2739, 2745, 2751 via `gov_run`; 3685,
3716, 3728, 3747 via `run`; 6213 and 6251 via `run_in_gov`), one is an `adopt` at 6249 and one a
continuation at 6287. So the real-root, already-pinned population AC5 is meant to protect is 4, not
32. AC5 grades "an arm counting explicitly-pinned invocations against a declared number", and the
only declared number in the spec is the wrong one — so the arm reds against a correct implementation,
or the implementer quietly rewrites the constant and the arm stops asserting anything.

**Fix.** Re-derive the row from the tree and state which quantity AC5's arm computes. The counted
quantity must be the one the arm can compute from the file — "`run()` invocations carrying their own
`--to` = 4" is the honest one, with the 13 and the 11 stated beside it so a reader can reproduce the
split.

**Left-shift.** Round 1's B3 already proposed exactly this arm, and this finding is that arm's
declared constant being wrong. So the arm is not the left-shift; the discipline around the constant
is. Make it a documented §10 check: *a count in a spec is a number the acceptance arm computes, never
a prose constant, and any spec claiming "every X" or "N of M X" states the command that produced the
figure so a reviewer can re-run it.* A `grep -c` over a source file is not that command, and saying
so in the checklist is the whole fix.

### H3 — a real-root `update` runs outside `run()` and stays unpinned

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §2 S1 ("the
real-root invocations — those going through the `run(*args)` helper") and §4 Inventory row 4, against
§6 AC1.

**Defect.** S1 scopes the pin to invocations reached through `run()`, and the Inventory asserts that
real-root equals via-`run()`. The file has a real-root invocation that is neither: `selftest.py:2627`
runs `[sys.executable, str(GOVKIT), "update", "--target", str(cc), "--write"]` through a bare
`subprocess.Popen`, carrying no `--to`.

**Why it is real.** `str(GOVKIT)` appears at exactly two sites in the file — line 72, inside `run()`,
and line 2627, the lock-contention pair. The second is real-root, carries no `--to`, and does not go
through `run()`. `govkit.py:5724` runs `demand_published_vintage` on every update run, so that arm
still defaults to `--to HEAD` and still refuses on a detached head. AC1's "exits 0" is therefore
unreachable by S1's stated mechanism, and §4 asserts an equivalence the file does not hold.

**Fix.** Extend S1 to name the direct-`Popen` invocation at `selftest.py:2627` as a second threading
site, and change the Inventory row to "real-root, via `run()` plus the direct `Popen` at 2627".

**Left-shift.** Make the population structural rather than nominal, and it is one line: an arm
asserting that every occurrence of `str(GOVKIT)` in `tools/govkit/selftest.py` is either inside
`run()` or carries an explicit `--to`. That is the real definition of "real-root invocation", it
cannot drift as the suite grows, and it reds the day someone adds a third `Popen`. It also composes
with H2's arm — one counts, this one classifies.

### H4 — the guard S3 hoists already precedes every write in that verb

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` §2 S3, and §4
Inventory row 3 ("check 26 idempotence guard | after the write").

**Defect.** S3 requires the check-26 idempotence guard to be "evaluated before any write, not after",
and the Inventory row states it currently runs after the verb's own write. Both are false of the
tree. `verb_landed()` opens at `unattended.sh:2250` and calls `refuse_if_terminal "$rel" --landed ||
return 1` at 2255 — 102 lines before the phase write at 2357.

**Why it is real.** Verified: between 2250 and 2255 there are only `check_slug`, `runmd_of` and an
`-f` test, no writes. `fail 26` occurs exactly once in the file, at 1611, inside `refuse_if_terminal`
(1606-1613), and the only `refuse_if_terminal` call inside `verb_landed` is the one at 2255 — the
next occurrence is 2459, in `--abort`. Dispatch runs one verb per invocation, so no path evaluates
check 26 after a write in this verb. S3 therefore scopes work that does not exist: an implementer
either no-ops it or relocates a call that is already correct. The `TOOL-dUnstalledConvoy-38`
observation the row rests on must have come from a SECOND invocation reading a record the first one
wedged — which is the defect S1 already fixes — so rev-2's claim to have folded that row's
"guard-ordering half" is unearned.

**Fix.** Delete S3 and its Inventory row, and say in §3 that the `-38` guard-ordering observation is
already satisfied at 2255 — or, if something is genuinely wrong, name the verb and line where the
guard actually runs after a write (it is not `verb_landed`) and give it its own AC. Either way,
re-derive what `-38` observed before claiming its half is closed.

**Left-shift.** Cheap and mechanical, because the spec supplies both numbers: a spec-lint leg that
reds when an Inventory row asserts an ordering ("after the write", "before the snapshot") that the
line numbers in the same table contradict. Here the table itself carries 2357 for the write, and 2255
for the guard would have made the row self-refuting. The same leg catches B1's row.

---

## Medium

### M1 — `stage_or_fail` still returns non-zero after the terminal write

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` §2 S1 ("so no
statement that can return non-zero runs after it"), §5 observability, and §6 AC4.

**Defect.** S1 places the phase write immediately before the staging call and claims that establishes
the invariant. It does not: `stage_or_fail "$rel" || return 1` at `unattended.sh:2428` is exactly such
a statement, and `stage_or_fail` (1564-1572) does `fail 9` and returns 1 whenever `stage_runmd`
fails.

**Why it is real.** The residual is structural rather than hypothetical — the write must precede the
stage or it would not be staged. A staging failure leaves a record whose `phase:` reads LANDED,
unstaged and therefore outside the leg's per-run population, with the verb exiting 1. §5's
"a refused `--landed` leaves a record whose phase matches its exit code" is untrue on that path, and
nothing in §6 grades it: AC4 is scoped to "a fact write LATER than the marker gate", and after the
move every fact write precedes the phase. So the residual instance of the class this unit exists to
close is both unstated and ungraded. It is medium rather than high because the record left behind is
COMPLETE — both facts present, so hygiene check 15 is satisfied — which is a far smaller wound than
the one the unit closes.

**Fix.** State the residual in S1 and §5: a staging failure leaves a complete terminal record that is
unstaged. Then either accept it explicitly with that reasoning, or move both writes after the staging
call and add an AC for a forced `stage_or_fail` failure leaving `phase: LANDING`.

**Left-shift.** A `gotchas/` class record: *the last statement in a verb is still a statement that can
fail; a "nothing after this can fail" invariant is checked against the function's last line, not
against its last interesting line.* If the AC is added, it doubles as the regression arm.

### M2 — two wrong addresses in the table rev-2 added to fix addressing

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` §4 Inventory
row 2 ("`set_fact landed-anchor` | ~1890 region") and §2 S1 plus §4 Files touched ("the staging call
at 2427").

**Defect.** Both addresses are wrong at base `0f19429a`. `set_fact "$rel" landed-anchor "$akind"` is
at `unattended.sh:2405`, not the "~1890 region" — off by 515 lines, and pointing into a different
function entirely. And the staging call is at 2428; line 2427 is the third line of the multi-line
`set_fact "$rel" units-at-landing` statement that spans 2425-2427.

**Why it is real.** Verified byte-exactly. 2425-2427 is one continued statement ending `| sed 's/ $//'
)" || return 1`, and `stage_or_fail "$rel" || return 1` is on 2428. The 1890 figure is inherited
verbatim from `TOOL-dScaffoldedMirror-22`, written 2026-08-25 against an older tree, while the
table's other rows (2357, 2373) carry current numbers — so the one table the fold added to inventory
the write sites mixes a stale coordinate with fresh ones and gives the implementer no way to tell
which is which. Row 2's line and its own consequence column are mutually exclusive: a statement at
1890 would run before both the phase write at 2357 and the marker gate. Taking "immediately before
2427" literally inserts the phase write inside another statement's line continuation, which is a
shell syntax break rather than a misplacement.

**Fix.** Correct row 2 to "`set_fact landed-anchor` | 2405 | after the marker gate, so a refusal at
2373-2400 leaves phase written and anchor not". Correct 2427 to 2428 in both S1 and §4, phrased as
"immediately before `stage_or_fail` at 2428, i.e. after the `units-at-landing` write that ends at
2427". Add the `unpushed-at-landing` write at 2409 as its own row — S1's "after every other fact
write" has to clear it too. And state that the numbers were re-verified at `0f19429a` rather than
carried from the cited backlog rows; §9's rev-1 note claims verification of 2357 and 2373 only, which
is exactly the gap.

**Left-shift.** Genuinely mechanical and worth building, because it would have caught every address
defect in this round and in round 1's B1. A spec-lint leg that, for each `<file>:<line>` in a §4
Inventory row, resolves `git show <base-sha>:<file>` and asserts the row's named symbol appears on
that line. The specs already carry a `base` in their status header and the rows already carry both
the symbol and the number, so the check has every input it needs and no new authored data.

---

## Low

### L1 — a deleted landing prints as `restored` in the rollback order

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §5
observability, the claim that "a deleted landing appears in the same list, distinguished by its
origin".

**Defect.** The rollback order's path list is a single origin-free join at `govkit.py:6945` —
`"".join(f"restored  {p}\n" for p in restored)` — and the paragraph above it at 6941-6942 asserts
that every path below "was restored to the index entry it had before the first byte moved". Both are
false of a landed path whose restore is a DELETE plus a receipt-row removal. Nothing in the spec
delivers the promised distinction: no scope item mentions the report, no AC grades its text, and §4's
Files touched enumerates six `govkit.py` items with no report writer among them.

**Why it is real.** Verified at 6941-6950. No non-goal withholds this — the three non-goals cover
which sources land, moving the block earlier, and the receipt re-stamp. So §5 asserts an observable
the design does not produce, in a unit whose stated risk is data loss in a repository gov does not
own. An operator reading `restored  <path>` for a path that was removed is told bytes were put back
when they were taken away. Low because it is a report-text defect with no data consequence, and
because the fix is a few lines inside a change the unit is already making.

**Fix.** Add the report change to S3 and to §4 Files touched: a landed entry prints under its own
verb — `removed  <path>` — and the paragraph's "was restored to the index entry it had" sentence is
conditioned on whether any landed entry is present.

**Left-shift.** Free once the fix lands, because the fixture already exists: the AC1 arm asserts the
rollback order's verb column distinguishes a deleted landed path from a restored claimed one. That is
one string assertion on output the arm already captures.

---

## What the round says about the set

Every blocker in this round is a defect in text that did not exist at rev-1, and each one is the
round-1 finding it was written to close, re-committed one level up. B1 is round 1's B2 grounded on a
call site nobody re-read. B2 is round 1's B5 answered with a capability the product does not have.
B3 is round 1's B4 with a population declared closed and counted wrong. H1 is round 1's H10, rewritten
and still unfailable. Four of ten findings are the same fold, which matches the corpus's own
`fold-text-is-unreviewed-surface` gotcha precisely: the fold is new surface, and it was reviewed by
nobody before this round.

The specific mechanism is worth naming, because it is one habit rather than four. The fold answered
each finding by writing a sentence that satisfies the finding's text, then addressed that sentence by
citing a line number found in the report, in a comment, or in a backlog row — without opening the
file at the declared base. Every one of the ten findings below blocker level is an instance: a count
taken from `grep -c`, an equivalence assumed between "real-root" and "via `run()`", a guard assumed
to be after a write because a backlog row said the write happened first, an address carried from a
row written ten days earlier. The tree was not consulted, and the tree disagrees in every case.

Two of the left-shifts above would have caught most of this on their own, and both are joins over
files that already exist: resolving each Inventory `file:line` against the spec's own declared base,
and reding an Inventory row whose asserted ordering contradicts its own line numbers. Neither needs
authored data and neither can rot. If only one thing lands from this report before round 3, it should
be the first of those.

## Round 3 scope

Narrower again, and code-first rather than prose-first. The three amended sections only — S1 and AC5
on `DEPL-dSealedTally-1`, S1/S4 and the Inventory on `DEPL-dSealedTally-5`, S1/S3 and the Inventory
on `TOOL-dSealedTally-1` — with the finders primed on the structure of `govkit.py`,
`selftest.py` and `unattended.sh` at base `0f19429a`, not only on the prose that describes them.
Precision has now sat under the §8 floor for two consecutive rounds on the same priming defect, so
round 3 fixes the priming or stops adding lenses.

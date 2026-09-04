**Serves:** spec-audit DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1

# Spec audit round 1 — dSealedTally

Tier-2 · node d · 2026-09-04 · a pre-code pass over the whole six-unit spec set at rev-1, before any unit opened.

**ROUND 1** over six subjects, each pinned at the blob it was read at: [DEPL-dSealedTally-1](../spec/2026-09-04-spec-DEPL-dSealedTally-1.md)@`4bd6f17d00b1` · [DEPL-dSealedTally-2](../spec/2026-09-04-spec-DEPL-dSealedTally-2.md)@`08f6150a2707` · [DEPL-dSealedTally-3](../spec/2026-09-04-spec-DEPL-dSealedTally-3.md)@`9159773ea574` · [DEPL-dSealedTally-4](../spec/2026-09-04-spec-DEPL-dSealedTally-4.md)@`0e607b65cdc7` · [DEPL-dSealedTally-5](../spec/2026-09-04-spec-DEPL-dSealedTally-5.md)@`b8dd7d6af7ba` · [TOOL-dSealedTally-1](../spec/2026-09-04-spec-TOOL-dSealedTally-1.md)@`6009fd149be2`.

## Verdict: BLOCKED

Five findings say a unit cannot be built as its own design section describes it, and three of those
five are against one spec. `DEPL-dSealedTally-1` names a mechanism that runs after its only reader
has finished, on a code path that excludes the very files it is written to cover.
`DEPL-dSealedTally-5` names a pin that two separate guards refuse, one of which the spec never
mentions. `TOOL-dSealedTally-1` was written without three OPEN backlog rows that already priced its
defect and decided a wider remedy. None of that is fixable during a pass — each needs a design
decision the spec has not made — so the set does not open for building at rev-1.

The good news is that every blocker has a stated and cheap fix, and none is a rethink of what the
build is for. The problems this build exists to close are real and correctly identified. What is
wrong is where the specs put the code, and what they did not read first.

## Review shape

| Raw | Confirmed | Refuted | Unverified | Precision |
|---|---|---|---|---|
| 55 | 22 | 33 | 0 | 0.40 |

Precision 0.40 sits below the ~0.5 floor §8 sets. That rule says tighten scope and priming before
adding agents, so a round 2 over the amended specs should be narrower rather than larger. The 33
refuted clustered on speculative reachability claims about `govkit` internals that the skeptic
disproved by reading one function — a priming problem, not a lens problem. The finders were handed
the specs and not the structure of the file the specs describe, so they reconstructed that structure
from prose and guessed wrong.

Nothing came back unverified. Every finding below survived a skeptic asked to refute it, so none of
them is an open question about whether it is true.

## Severity as adjudicated here

Three findings carry a severity in this report different from the one the review fan assigned, each
for a stated reason. The counts in this section and the table below are this report's.

- **Raised to BLOCKER — B5, the second vintage guard.** The fan called it high. It belongs with the
  blockers because it makes `DEPL-dSealedTally-5`'s AC1 unsatisfiable by any implementation of the
  design as written, which is the same class as the blocker already standing against that unit.
- **Lowered to HIGH — H9, the composition of `excused`.** The fan called it a blocker and its own
  skeptic said the severity was overstated. The design paragraph is genuinely wrong, but it REDS at
  AC2 during implementation rather than shipping green. This corpus's own rule is that a visible
  refusal outranks a silent pass, so a spec defect that the unit's own acceptance set catches is not
  a blocker.
- **Raised to HIGH — H10, the containment arm.** The fan called it medium. It is the same
  could-not-fail-acceptance class as two findings already at high, inside the spec set of a build
  whose stated purpose is draining that class. Grading one instance of a class below another
  instance of the same class is how the class survives.

| Severity | Count |
|---|---|
| BLOCKER | 5 |
| HIGH | 13 |
| MEDIUM | 3 |
| LOW | 1 |

## The findings at a glance

| # | Sev | Unit | Address | The defect |
|---|---|---|---|---|
| B1 | blocker | `DEPL-dSealedTally-1` | §4 Design, §3 Non-goals | the landing block runs after the pass meant to read it |
| B2 | blocker | `DEPL-dSealedTally-1` | §2 S1 | a landed-only kit has no pre-write baseline and cannot get one later |
| B3 | blocker | `DEPL-dSealedTally-5` | §4 Design | the pin is threaded into repositories whose object databases lack it |
| B4 | blocker | `TOOL-dSealedTally-1` | §10 Reuse audit, §2 | three OPEN rows decided a wider fix and the spec cites none |
| B5 | blocker | `DEPL-dSealedTally-5` | §2 S4, §3 Non-goals | a second vintage guard the spec never names refuses the pin |
| H1 | high | `DEPL-dSealedTally-1` | §2 S2, §6 | the index half of the restore is resolved by F1 and graded by nothing |
| H2 | high | `DEPL-dSealedTally-3` | §2 S1, §6 | no criterion observes an assertion site calling the new predicate |
| H3 | high | build order | `DEPL-dSealedTally-4` header, §4 | step 1 is a parallel pair with identical write sets |
| H4 | high | `DEPL-dSealedTally-5` | §2 S2 against §4, §5 | the fallback grades an ancestor's tree, not the tree under test |
| H5 | high | four specs | `DEPL-dSealedTally-1` §6 AC5 and siblings | one arm-count constant pinned by four units that land in sequence |
| H6 | high | `DEPL-dSealedTally-1` | §2 S2, §4 Data model | a landed path is classified untouched, so the DELETE never runs |
| H7 | high | `DEPL-dSealedTally-1` | §4 Data model, the `origin` switch | the per-entry field restore runs for landed entries too |
| H8 | high | `DEPL-dSealedTally-1` | §4 Design, the minted receipt row | a rolled-back landing leaves its receipt row behind |
| H9 | high | `DEPL-dSealedTally-3` | §4 Data model, §2 S2 | `excused` is specified as the wrong end of the rename |
| H10 | high | `DEPL-dSealedTally-1` | §2 S3, §6 AC4 | the containment arm cannot be constructed against shipped code |
| H11 | high | `DEPL-dSealedTally-4` | §4 Rollout, §8 F1 | one call site is mid-write, so raise-always aborts a part-written target |
| H12 | high | `DEPL-dSealedTally-5` | §2 S2 and S3, §4 | the named mitigation does not cover the risk it is named for |
| H13 | high | `TOOL-dSealedTally-1` | §2 S1 | five more failure sites follow the check the write moves below |
| M1 | medium | build order | `DEPL-dSealedTally-3` header, §4 | step 2 is a parallel pair sharing one test file |
| M2 | medium | `DEPL-dSealedTally-5` | §4 Data model | neither candidate command is runnable as written |
| M3 | medium | `DEPL-dSealedTally-2` | §4 Design, §5 risks | an unwrapped `Refusal` moves onto every kit's path |
| L1 | low | `DEPL-dSealedTally-4` | §5 error and empty states | the guard named as load-bearing is unreachable for every input |

---

## Blockers

### B1 — the landing block runs after the pass that is supposed to read it

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §4 Design
("Files touched") and §3 Non-goals, second bullet.

**Defect.** The design has the landing block append its own `snap_rows` entries so the
verify-and-rollback pass picks them up. The landing block sits at `tools/govkit/govkit.py:6983-7185`,
strictly after the whole verify-and-rollback pass at `6806-6980`. Entries appended there are read by
nothing.

**Why it is real.** `snap_rows` appears in `tools/govkit/govkit.py` at lines 6319, 6326, 6336, 6340,
6347, 6348 and 6858, and nowhere below. Its readers are `touched_kits` and `orphan_kits` at
6347-6348 and the restore loop at 6858, all finished before the landing block starts. S1, S2 and S4
therefore cannot be delivered by the stated mechanism. The obvious repair is closed by the spec's own
§3 non-goal, and that non-goal misattributes the move to `DEPL-dSealedTally-2`, whose scope is
hoisting the `rename_dests` fill and does not include it.

**Fix.** Add a Design sub-section stating the ordering. The landing block moves to sit between the
write loop's end and `written_paths = ...` at `tools/govkit/govkit.py:6806`. It needs
`withdrawn_rows`, built in the write loop, and `rename_dests`; both are complete by that point, so
the position is available. Delete the second §3 non-goal, or restate it as "moved to just before
line 6806, and no earlier than the write loop's end".

**Left-shift.** A spec-lint leg that resolves every `file:line` anchor a §4 Design section names and
reds when a mechanism's producer line sits below its consumer's. Both numbers are already in the
spec and the reader is a grep. If that is too clever for one leg, the cheap version is a
`gotchas/` class record for "a design that appends to a structure already consumed upstream", so
`python tools/memory-tree/gotchas.py --for-diff` puts it on every reviewer's checklist for this file.

### B2 — a landed-only kit has no pre-write baseline, and cannot get one afterwards

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §2 S1.

**Defect.** S1 requires a kit whose only change is a landed source to appear in `touched_kits` and
therefore receive a baseline and an after-check. `touched_kits` is computed at
`tools/govkit/govkit.py:6347` from `snap_rows` membership and the baseline loop runs at 6350-6352,
both before the write loop. The verify pass then reads `baseline[eid]` unguarded at 6811. A
landed-only kit has no acted row, so no snapshot entry, so no baseline — and the landing that would
create one runs at 6983.

**Why it is real.** Adding such a kit to `touched_kits` raises `KeyError` at 6811 and aborts the run
mid-write, inside a repository gov does not own. Recomputing `touched_kits` after the landing does
not rescue it: a baseline taken after the landing writes grades post-write state as the baseline,
which makes `was == now` for every such kit and silently disables the rollback this unit exists to
add. The spec states the property and proposes no mechanism for it, and budgets nothing for one.

**Fix.** State in §4 that the landed destinations are derived BEFORE the snapshot, using the
`derive_unclaimed_candidates` preview call already made at `tools/govkit/govkit.py:6276`, and that
`touched_kits` and `baseline` at 6347-6352 widen from that preview so a landed-only kit is baselined
pre-write like every other kit.

**Left-shift.** A regression arm rather than a gate, and it is free once the fix lands because it is
the AC1 arm this finding makes possible: a fixture whose only change is a landed source, run with
its kit check forced red, asserting the run reaches its own rollback report instead of exiting on a
traceback. Alongside it, `baseline[eid]` at 6811 becomes `baseline.get(eid)` with a named refusal, so
the next unit that widens `touched_kits` gets a message rather than a `KeyError`.

### B3 — the pin is threaded into repositories whose object databases do not hold it

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §4 Design, the
sentence "The value is passed to every `update` invocation as an explicit `--to`".

**Defect.** 28 of the 74 `update` invocations in `tools/govkit/selftest.py` run against scratch gov
repositories built by `git init -q -b main` plus one commit, at `selftest.py:1772-1776` and
`1811-1815`, reached through the helpers at 1781 and 2681. A sha derived from the real checkout's
refs does not exist in those object databases at all.

**Why it is real.** Threading one module-level pin through every invocation makes `rev-parse
--verify` fail in every scratch gov, converting a 46-arm failure into a near-total one. Eleven or
more call sites also pass a deliberate per-fixture vintage taken from the scratch repo's own history
(`tools/govkit/selftest.py:2721-2751`, `3685-3747`, `6213-6251`), which a blanket pin would clobber
and silently change what those arms grade. §4's "every `update` invocation" and §10's "every
`update` invocation in it relies on the `--to HEAD` default" are both false of the actual
population.

**Fix.** Scope the pin in §4 to the real-root invocations only, meaning the `run(*args)` helper at
`tools/govkit/selftest.py:69` that executes govkit in place, and state that the scratch-gov helpers
and any call already carrying its own `--to` are untouched. Add an AC asserting the scratch-gov
arms' `--to` values are unchanged from base.

**Left-shift.** An arm that counts explicitly-pinned `update` invocations in the suite against a
declared number, so a future edit that widens the pin reds instead of quietly re-pointing fixtures.
The general class — a change described as universal, measured against a population nobody counted —
belongs in §10 as a documented check: a spec claiming "every X" states the count of X it measured.

### B4 — three OPEN backlog rows decided a wider fix and the spec cites none of them

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` §10 Reuse
audit, and §2.

**Defect.** `memory/backlog/TOOL.md` carries three OPEN rows recording this exact defect across four
measured instances, with a wider decided fix. The row at line 231 states that fix as "compute and
validate, then write both facts together, so a refusal leaves the record untouched", and records
that the resulting LANDED-with-no-anchor record reds hygiene check 15 forever while check 26 then
refuses `--park` and `--phase`, so no verb can repair it. The row at line 273 is a fourth instance on
node `a`, offering a `--landed --repair` candidate. The row at line 212 is the same
write-before-check family. A grep of the entire `memory/builds/dSealedTally/` tree returns zero hits
for any of the three ids.

**Why it is real.** §1's Definition of Ready requires reading the stream's backlog before touching
code, and the spec's §10 claims a reuse audit happened. As specced the unit lands a strictly narrower
fix than the corpus already decided, ships nothing for the four records already wedged
LANDED-with-no-anchor, and would leave three OPEN rows describing a defect it partly closed. That is
the accumulation `DEPL-dGaugedVintage-2` had to sweep by hand.

**Fix.** Cite the three rows in §10. Then either widen §2 to the recorded fix of writing the phase
and `landed-anchor` together after validation, or state in §3 which of their asks are deliberately
out of scope — the repair path, the no-ff predicate — and file the residue as a fresh row before the
unit opens.

**Left-shift.** This is the most valuable gate in the report and it is genuinely buildable. For each
spec, read the `→ <path>` target of every OPEN row in that spec's own backlog family, and red when a
row's target is a file the spec's §4 "Files touched" names while the spec cites neither the row id
nor a waiver. It converts "did you read the backlog" from a DoR item people remember into a leg that
fails, and everything it needs is already structured text in two files.

### B5 — a second vintage guard the spec never names refuses the derived pin

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §2 S4 and §3
Non-goals.

**Defect.** S4 names only `demand_published_vintage`. The guard `demand_forward_vintage` at
`tools/govkit/govkit.py:4129` refuses any `--to` that is not a descendant of the receipt's
`gov_commit`, on the grounds that a downgrade is not an update — and it runs first, at
`tools/govkit/govkit.py:5723-5724`, on every run including read-only ones. The design's pin is by
construction an ANCESTOR of HEAD whenever the derivation fires.

**Why it is real.** Apply stamps the receipt's `gov_commit` from `git rev-parse HEAD`
(`tools/govkit/govkit.py:4199`, written at 5061), and many suite fixtures are applied at gov HEAD and
then updated. On a detached merge commit those receipts record the merge, so the pin — a
ref-reachable ancestor of it — is refused as a downgrade where the same arm previously refused on
published vintage. Those arms stay red, so AC1, "exits 0 on a detached merge commit", cannot hold for
any implementation of §4 as written. The stale-target fixtures at `tools/govkit/selftest.py:540-564`
survive because they re-pin `gov_commit` to an ancient sha; the apply-at-HEAD fixtures do not.

**Fix.** Add `demand_forward_vintage` to S4. Then either add an AC that the derived pin still
descends from every fixture receipt's `gov_commit`, or derive a pin only for the invocations
`demand_published_vintage` would actually refuse and leave the rest on the `HEAD` default.

**Left-shift.** A documented §10 checklist entry, because the general case is not gateable: when a
unit changes an argument that guards read, enumerate every guard on that argument's path and name
each one in scope, not only the guard whose failure motivated the unit. The mechanical half is cheap
though — a comment at `tools/govkit/govkit.py:5723` naming both vintage guards as one ordered pair
would have put the second one in front of this spec's author.

---

## High

### H1 — the index half of the restore is resolved by F1 and graded by nothing

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §2 S2, with no
matching criterion in §6.

**Defect.** S2 says the restore is a DELETE plus an index removal, and F1 resolves that removal to
`git rm --cached`. No AC in §6 observes the index after a rollback. AC1 checks only that the
destination is absent; AC2 uses the word "staged" on the success path.

**Why it is real.** That AC2 says "staged" and AC1 does not is meaningful rather than accidental —
the spec distinguishes worktree presence from index state where it wants to. An arm asserting only
that the destination does not exist passes AC1 through AC5 while leaving a stage-0 entry for a path
the worktree no longer holds, and an adopter's next commit then commits the file the rollback
removed. The half of S2 that F1 exists to answer is ungraded.

**Fix.** Add an AC: when a landed file is rolled back, `git ls-files -s <dest>` in the target reports
no entry, proved by the AC1 arm asserting index state alongside its `lexists` check.

**Left-shift.** A structural spec check with wide reach: every S-item in §2 is named by at least one
AC in §6, reported per unit. It catches H1 and H2 together and would have caught both before either
spec left SPECCED. The mapping can be as crude as requiring each AC to cite an S-item id, which makes
the coverage derivable rather than judged.

### H2 — no criterion observes an assertion site calling the new predicate

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-3.md` §2 S1, with no
matching criterion in §6.

**Defect.** S1 requires the new predicate to replace the count comparison at its assertion sites.
AC1 through AC3 assert only the two predicates' return values, AC4 mutates the predicate's own
`excused` subtraction, and AC5 counts arms. None observes any existing assertion site now grading
paths.

**Why it is real.** §3 keeps `count_never_falls` alive "where a count is what is meant" without
saying where that is, so an implementation that adds the predicate, its truth table and its mutation
control while leaving every real update arm on the old predicate passes AC1 through AC5 with the
delete-one-land-one swap still undetected. The acceptance set cannot distinguish wired from unwired,
which is the defect the unit exists to close, one level up.

**Fix.** Add an AC naming the sites: when the delete-one-land-one fixture is driven through the
update arm at a named site, that arm REDS where at base `0f19429a` it passes. Name in S1 which sites
convert, since §3's non-goal keeps the old predicate without saying where.

**Left-shift.** Same leg as H1 — every S-item is named by an AC. Beyond that, an arm asserting the
count of `count_never_falls` call sites has fallen from its base value, so a predicate that ships
unwired reds on arithmetic rather than on judgement.

### H3 — step 1 is a parallel pair with identical write sets

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-4.md` status header
`order 1` and §4 "Files touched", against the build's generated step-1 group.

**Defect.** This spec declares `order 1` and names `tools/govkit/govkit.py` plus
`tools/govkit/selftest.py`. `DEPL-dSealedTally-2` declares the same `order 1` and the identical two
files. The generated build order prints step 1 as `Parallel: yes`, while `memory/guides/BUILD-METHOD.md`
M6 permits concurrency only when the two write sets, written down before dispatch, do not intersect.

**Why it is real.** Verified in both status headers and both Files-touched sections, and in the
generated order table in the build README. `memory/TEMPLATE-SPEC.md` states that units sharing an
order value are the parallel group. Here the two write sets are not merely intersecting, they are
identical — on the file whose data-loss guard this build exists to close. Either the two passes
collide on `govkit.py`, or the run silently sequences them and the order table stops describing what
happened.

**Fix.** Move one of the two units to `order 2` so the generated table sequences them, or add a line
to §4 of both stating the disjoint line ranges each will write and why M6's first clause is
satisfied.

**Left-shift.** A leg in the build-index renderer: for each order group with more than one unit,
intersect the backticked paths in each member's "Files touched" section and red on a non-empty
intersection unless both members carry a disjoint-range note. It catches H3 and M1 in the same pass,
and it runs on data the renderer already parses.

### H4 — the fallback grades an ancestor's tree, not the tree under test

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §2 S2, against
§4 Design and §5 risks.

**Defect.** S2 requires the pin to be the ref-reachable commit that describes the tree under test.
§4's fallback for the detached-merge case walks to the first ancestor that IS ref-reachable, whose
tree is by construction not the merge commit's tree. §5 concedes the derivation could silently pick a
wrong ancestor and grade an older tree.

**Why it is real.** The fallback is the path taken in exactly the motivating case, since a
`for-each-ref --contains` query returns nothing for a detached merge. The mechanism therefore defeats
§1's stated goal of making the suite's verdict a function of the tree it grades: on the case the unit
exists for, the suite grades an ancestor's tree and reports green for a tree it never examined. A
false green is a worse outcome than the refusal it replaces, because the refusal is visible.

**Fix.** Either restrict the derivation to a ref-reachable commit whose `rev-parse HEAD^{tree}`
equals the working tree, refusing by name when none exists per S2's own refusal clause, or amend S2
and §1 to say the pin names the vintage `update` is asked to deploy rather than the tree under test —
and say plainly which of the two the suite grades.

**Left-shift.** Not a repo gate but a suite arm, and it is the same arm H12 asks for: assert
`pin^{tree}` equals `HEAD^{tree}` and refuse otherwise, so the wrong-ancestor case is a named refusal
rather than a silent regrade. The class belongs in §10 as "a derivation whose fallback answers a
different question than its primary path".

### H5 — one arm-count constant pinned by four units that land in sequence

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §6 AC5, and the
matching criteria in `-2` §6 AC4, `-3` §6 AC5 and `-5` §6 AC2, against the build's step order.

**Defect.** Four units each require the suite's arm count to be strictly greater than the 1074 it
reports at base `0f19429a`, while the generated order lands them across steps 1, 2 and 3 on one
branch. From the second unit onward the comparison is already satisfied by a sibling's arms.

**Why it is real.** Verified in all four specs and in the generated order table. `DEPL-dSealedTally-5`,
ordered last, passes its AC2 having added zero arms. The charitable reading — that the criterion
means "adds coverage rather than removing arms" — fails too, since a unit that deletes arms stays
above the constant on a sibling's surplus. This is a could-not-fail acceptance criterion in four
specs at once, reporting coverage nobody has, in the build opened to drain that shape.

**Fix.** Re-pin each unit's arm-count AC to the count observed at the head of the PRECEDING step,
captured in that unit's own revision log when its pass opens, or state the exact number of arms the
unit adds and assert the delta.

**Left-shift.** A spec-lint leg: no two specs in one build may pin the same numeric acceptance
constant against the same base sha. It is a duplicate-detection pass over backticked numbers beside a
base reference, and it names the class precisely — a shared constant is only a valid criterion for
whichever unit reaches it first.

### H6 — a landed path is classified untouched, so the DELETE never runs

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §2 S2 and §4
Design ("Data model").

**Defect.** The restore loop gates every path on a `written_paths` membership test at
`tools/govkit/govkit.py:6873`, and `written_paths` is built at 6806 from `changed`, `renamed` and
`deleted`. A landed path goes into `_landed_new`, which is none of those three.

**Why it is real.** The gate at 6873 sits ahead of the entry-is-None branch the spec's data model
depends on, and a scan of the whole landing block finds no mutation of `changed`, `renamed` or
`deleted` — it appends only to `_landed_new` and `_claimed_paths`. So even with B1's ordering fixed
and an origin-tagged entry present, every landed path takes the untouched arm and the DELETE never
runs. The rollback report then prints that it left the path alone because this run never wrote it,
about a file this run did write, which is a false statement in the operator-facing order.

**Fix.** State in §4 that the landing block appends its destinations to `changed`, or that
`written_paths` is widened by `_landed_new`, and that the closing tally loop at
`tools/govkit/govkit.py:6925-6928` removes a rolled-back landing from `_landed_new` so the summary
does not report a landing that was undone.

**Left-shift.** An arm asserting the rollback report's own text: for a rolled-back landing, the
operator order names the path as deleted and never as untouched. That is the liveness assertion §7
asks for, applied to a report rather than a probe — a rollback that silently classifies its subject
as out of scope currently reports a reassuring sentence.

### H7 — the per-entry field restore runs for landed entries too

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §4 Design
("Data model"), the `origin` switch.

**Defect.** §4 switches only the byte-restore branch on `origin`. The per-entry block at
`tools/govkit/govkit.py:6915-6924` sits outside the paths loop and runs for every snapshot entry: it
writes or pops each of the six `ROLLBACK_FIELDS` on the entry's row, then removes that row from
`withdrawn_rows`.

**Why it is real.** `ROLLBACK_FIELDS` is defined at `tools/govkit/govkit.py:5125` and includes
`path`. The spec's data model pins exactly the combination that breaks this block: an empty `fields`
map, and no receipt row for a landed file. With a `None` row that block raises `AttributeError`
mid-rollback in a foreign repository. With the minted receipt row it strips that row's `path`,
`sha256`, `commit`, `gov_oid` and `oid`, leaving a row the next run's receipt-integrity preamble
cannot attribute. The design's only stated switch does not reach this block.

**Fix.** State that the landed branch skips the `ROLLBACK_FIELDS` restore and the `withdrawn_rows`
removal entirely, and say explicitly what a landed entry's `row` key holds — the minted receipt row,
or a sentinel — rather than leaving it as "no receipt row".

**Left-shift.** A gotcha class record with an anchor on this file: "a per-entry block outside the
per-path loop runs for entry shapes the new branch never considered". The general lesson is that
adding a fourth shape to a structure obliges you to walk every consumer of that structure, not only
the one you are extending, and `gotchas.py --for-diff` is the delivery mechanism.

### H8 — a rolled-back landing leaves its receipt row behind

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §4 Design,
which carries no bullet for the minted receipt row.

**Defect.** The landing block appends a nine-field receipt row at `tools/govkit/govkit.py:7134`. The
rollback path calls `r.fail`, and the receipt is written on a failed run — the branch at
`tools/govkit/govkit.py:7203-7208` writes both `install.json` and `install.sums` whenever the run has
problems, withholding only the gov-commit re-stamp.

**Why it is real.** A rolled-back landing therefore deletes the file from the target and leaves its
row in both the receipt and the sums file. The next `update` reads a row naming a path the target
does not hold, which is the wedged-adopter state the landing block's own comment records paying for
once already. §3's non-goal covers the receipt re-stamp, not row minting, so it does not withhold
this.

**Fix.** Add an S-item and a Design bullet: on rollback of a landed entry, the row appended at 7134
is removed from the receipt's file list in the same branch that deletes the file, with an AC
asserting the post-rollback receipt names no landed path.

**Left-shift.** An invariant arm rather than a case arm, which is the stronger shape: after any run
that rolls back, every path in the receipt exists in the target. It covers this defect and every
future one of its kind, and it is the lockstep-invariant guard §7 asks for on a pair that must move
together.

### H9 — `excused` is specified as the wrong end of the rename

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-3.md` §4 Design
("Data model"), and §2 S2, which carries the same wording.

**Defect.** `excused` is specified as the rename destinations the run reported. The predicate grades
the paths that LEFT, which are the rename SOURCES. A destination is in the after set by construction
and can never appear in the difference being graded.

**Why it is real.** The arithmetic holds against the fixture: the rename moves one demo path to
another, so the difference is the old path. With `excused` holding destinations, the predicate
degenerates to the rejected subset assertion for renames, AC2's required `True` is unobtainable, and
the unit ships the predicate it was filed to avoid. The run does report both ends, so the fix is one
clause — but as written, the paragraph the spec itself calls the whole design names the wrong set.

**Fix.** Change §4 and S2 to say `excused` holds the pre-rename paths, meaning each renamed receipt
row's path as it stood before the run, plus the withdrawn rows' paths. Name the observable channel:
the receipt read before the run, or the run's own rename verdict lines, since the post-run receipt
carries only the destination and withdrawn rows are stripped from it.

**Left-shift.** The truth table AC3 already asks for is the right instrument, extended by one row: a
rename case with `excused` holding the destination must return `False`, so the wrong composition is
distinguishable from the right one by an arm rather than by reading. That is the mutation-control
discipline S4 already commits to, applied to the argument instead of to the subtraction.

### H10 — the containment arm cannot be constructed against shipped code

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-1.md` §2 S3 and §6
AC4.

**Defect.** The landing block already refuses any destination outside the target at
`tools/govkit/govkit.py:7062-7070` and any destination inside `.git` at 7072-7078, both before a byte
is written. No landed path can reach the rollback uncontained.

**Why it is real.** AC4's stated method is an arm giving the landing a destination outside the
target. That arm exercises the landing refusal, not the rollback's containment call, and cannot fail
on the thing the criterion names. The code's own comment beside that call says the class is narrow
and not reproduced, which is the same admission from the other side. An arm that cannot fail, reading
as coverage, written into an acceptance criterion — in this build.

**Fix.** Either restate AC4 as "the rollback branch calls `demand_contained_dest` for a landed path,
proved by a mutation that removes the call", or say in §4 that the arm requires the landing block's
own containment check to be stubbed, and name that stub as the arm's second mutation.

**Left-shift.** The rule already in §7 — a new gate is not landed until its failing case has been
observed — extended to acceptance criteria: an AC whose arm has never been seen to fail is an
assertion about nothing. As a documented §10 check it reads "for each AC, name the mutation that
makes it red", which is exactly what AC3 and AC4 do elsewhere in this same spec and what AC4 does
not.

### H11 — one call site is mid-write, so raise-always aborts a part-written target

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-4.md` §4 Design
("Rollout") and §8 F1's resolution.

**Defect.** One of the seven `index_read` call sites — the rename-destination lookup at
`tools/govkit/govkit.py:6460` — sits inside the write loop, after earlier rows have already moved
bytes. `Refusal` is caught only at the command boundary.

**Why it is real.** A failed chunk at 6460 aborts before `written_paths` at 6806, before the verify
pass and before the rollback pass, leaving a foreign repository part-written with no outbox order, no
rollback and no report of what stands. That is the precise class `DEPL-dSealedTally-1` is being
written to close, reintroduced by its sibling. Every other failure inside that loop uses a fail-and-
continue, and the rollback path catches `Refusal` explicitly to avoid exactly this — so F1's
raise-always resolution, whose stated rationale is snapshot truth, was never weighed against this
call site's position.

**Fix.** State in Rollout which call sites are pre-write and which is mid-write, and say what a
mid-write refusal owes: either the refusal at 6460 becomes a fail-and-continue so the run reaches its
own rollback pass, or the spec declares the part-written abort acceptable and says so in the risks
bullet.

**Left-shift.** A gotcha class record anchored on this file: "a refusal introduced inside a write
loop escapes to the boundary and skips the rollback pass". The mechanical companion is a grep-shaped
check that no `raise Refusal` appears between the write loop's opening line and `written_paths`
without an accompanying comment, which is crude but would have surfaced this call site during the
design pass.

### H12 — the named mitigation does not cover the risk it is named for

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §2 S2 and S3,
and §4's ancestor fallback.

**Defect.** The fallback pins a ref-reachable ancestor whose tree differs from the merge commit's
tree. The arms then read gov's blobs at the pinned commit while descriptors come from the working
tree, so they grade the ancestor's bytes mixed with this tree's descriptors, while §1 promises the
suite's verdict is a function of the tree it grades.

**Why it is real.** §5 names this risk and assigns it to S3, but S3 as scoped only proves the pin
took effect — that it is not HEAD's default. It asserts nothing about tree equality, which is
directly checkable and is not asked for anywhere in the spec. A green run on a detached merge commit
would certify the pre-merge tree, and AC1 would pass on a merge that broke something the ancestor did
not have. The mitigation and the risk are about different properties.

**Fix.** Make S2's derivation assert tree identity: accept the pin only when `rev-parse
<pin>^{tree}` equals `rev-parse HEAD^{tree}`, and fire the named refusal when no ref-reachable commit
has this tree. Restate S3's liveness arm as proving that equality rather than proving a pin was
printed.

**Left-shift.** Generalize the liveness rule §7 already carries: a mitigation names the property it
establishes, and a risk names the property it needs, and they are compared as text during the audit.
As a §10 checklist entry — "for each risk in §5, state which AC would fail if the risk materialized"
— it is a two-minute pass that catches this whole family.

### H13 — five more failure sites follow the check the write moves below

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-TOOL-dSealedTally-1.md` §2 S1, the
phrase "below the lander-marker gate".

**Defect.** Five more failure sites follow that gate in the landing verb of
`tools/unattended/unattended.sh`: three further fact writes at lines 2402, 2405 and 2408, a fourth at
2425, and the staging call at 2427, each returning non-zero on failure. A fact write returns 1
whenever the record carries neither the key nor the run-facts heading.

**Why it is real.** S1's stated property — that no check which can return non-zero runs after the
terminal phase is written — is false of its own placement, and §1's goal sentence says "below every
check". A `--landed` that fails on the roster freeze or on staging still exits non-zero with the
terminal phase written, and the finished-record guard then refuses every retry. The run is wedged
exactly as it is today, on a narrower trigger. The ordering is genuinely constrained, since the phase
must be written before staging stages the file — which is an argument for saying so in the spec, not
for S1's current claim.

**Fix.** Change S1 to place the phase write immediately before the staging call at line 2427, after
every other fact write, and add an AC covering a `--landed` refused by a LATER fact write rather than
by the marker gate, leaving the phase at LANDING.

**Left-shift.** An arm per refusal site rather than one arm for the motivating site: for each way the
landing verb can return non-zero, the record's phase is unchanged. Enumerating the sites is what
makes the arm a class check instead of an instance check, and §7 already names that distinction as
the rule this build is dogfooding.

---

## Medium

### M1 — step 2 is a parallel pair sharing one test file

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-3.md` status header
`order 2` and §4 "Files touched", against the build's generated step-2 group.

**Defect.** This spec declares `order 2` and lives entirely in `tools/govkit/selftest.py`.
`DEPL-dSealedTally-1` declares the same `order 2` and writes roughly 45 lines of the same file, so
the generated order prints step 2 as `Parallel: yes` over an intersecting write set, which
`memory/guides/BUILD-METHOD.md` M6 forbids.

**Why it is real.** Two concurrent passes appending arms to one test file lose the loser's arms in
the reconcile — and because both units' arm-count criteria only require a total above 1074, the loss
is undetectable by either criterion once the sibling's arms have landed. H5 and M1 compound: the
weak criterion is what makes the collision silent.

**Fix.** Give `DEPL-dSealedTally-3` `order 3` and push `DEPL-dSealedTally-5` to `order 4`, or record
in §4 of both units the disjoint regions of `tools/govkit/selftest.py` each will write.

**Left-shift.** The same order-group intersection leg proposed under H3 covers this case; it is one
leg for both findings.

### M2 — neither candidate command is runnable as written

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-5.md` §4 Design
("Data model"), against §2 S2.

**Defect.** S2 requires a derived pin with a named refusal. §4 offers two alternative mechanisms and
neither is runnable. The first, described as an inverted `rev-list` against branches and remotes,
enumerates commits that are NOT ref-reachable — the opposite end of the range — and "inverted" names
no flag. The second, a `rev-parse` peel of HEAD to a commit, resolves to HEAD itself and not to any
ancestor.

**Why it is real.** The fallback is the branch actually taken in the motivating detached-merge case,
so the unit's central mechanism is undecided at SPECCED and the builder invents it. The two
candidates disagree about which commit is chosen and one of them returns the wrong end, which is the
silent-wrong-ancestor failure §5 already names as the unit's main risk.

**Fix.** Spell one command and its expected output in §4, and state what the suite does when that
command returns empty.

**Left-shift.** A documented §10 entry: a §4 Data model that offers alternatives has not made a
decision, and a spec reaches SPECCED with one mechanism named, not a menu. Mechanical proxy — red a
spec whose §4 contains "or" between two backticked commands, which is crude but catches the shape.

### M3 — an unwrapped `Refusal` moves onto every kit's path

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-2.md` §4 Design and
§5 risks.

**Defect.** The descriptor resolver raises `Refusal`, which is why the landing block wraps its call
in a try/except at `tools/govkit/govkit.py:7027-7032`. The call inside the rename resolver at 5961 is
unwrapped, because today it is reached only for kits that actually have a rename. Filling eagerly for
every kit puts that unwrapped call on the path of kits whose descriptor cannot resolve for this
target.

**Why it is real.** An unhandled `Refusal` propagates to the command boundary and aborts the run,
turning a descriptor that is merely irrelevant to this target into a hard refusal of the whole verb.
Both the preview and the landing block already wrap the identical call, so the codebase treats an
unresolvable descriptor as a live case. §5's claim that the only new failure direction is
over-exclusion, and §4's claim that the change can only widen the decided set, are both wrong about
this second direction.

**Fix.** Add a Design line: the eager fill wraps the resolver in a try/except that continues on
`Refusal`, copying the landing block's own handling and its stated reason. Correct the §5 risks
bullet to name the second direction.

**Left-shift.** A gotcha class record with anchors on this file: "hoisting a lazily-reached call
widens the population it can raise on". The general form is that moving a call earlier changes which
inputs reach it, and the audit question is what the new inputs do — which belongs in §10 for every
hoist, since this build contains two of them.

---

## Low

### L1 — the guard named as load-bearing is unreachable for every input

**Address.** `memory/builds/dSealedTally/spec/2026-09-04-spec-DEPL-dSealedTally-4.md` §5, "error /
empty / loading states".

**Defect.** §5 claims the existing empty-chunk guard already handles an empty path list. With no
paths, the batching range is empty and the loop body never executes; with any paths, every slice
taken at a range index is non-empty. The guard at `tools/govkit/govkit.py:3767-3771` cannot fire for
any input.

**Why it is real.** AC4's behaviour still holds, so nothing breaks. But the spec names the wrong
mechanism as the thing the change must not disturb, so an implementer preserving the named guard
preserves dead code, and one removing it is told they broke something they did not. That is the
assertion-about-nothing class this file elsewhere deletes on purpose.

**Fix.** Restate as: the empty case is handled by the loop not executing at all, the empty-chunk
guard is unreachable, and the returncode check sits inside the loop body so an empty list still
spawns nothing.

**Left-shift.** No gate; this is a review-reading finding. It joins §10 as a documented check —
"a §5 claim that an existing guard handles a case names a branch that some input reaches" — which is
the same discipline as the liveness assertion §7 requires of a probe, applied to a spec's prose.

---

## What the round says about the set

Three patterns account for eighteen of the twenty-two findings, and each has a cheaper fix at the
spec level than at the code level.

**Design sections written against remembered code rather than read code.** B1, B2, H6, H7, H8, H11
and M3 are all one failure: the spec describes a mechanism whose position, gating or fan-out in
`tools/govkit/govkit.py` is not what the file actually does. Six of the seven are in one spec. The
remedy is not more review; it is that a §4 Design section citing a mechanism cites the line range it
will sit in and the line range of each consumer it depends on, so the ordering is checkable while
the spec is being written.

**Acceptance criteria that cannot fail.** H1, H2, H5 and H10 are four instances, in a build whose
README says its purpose is draining that class from the deployer. H5 alone puts one could-not-fail
criterion into four specs. The single highest-value left-shift in this report is the S-item coverage
leg proposed under H1 — every scope item named by at least one criterion — because it catches two of
the four mechanically, and the constant-duplication leg under H5 catches the third.

**Concurrency declared without the write sets it requires.** H3 and M1 are the build's own generated
order table authorizing two parallel pairs whose write sets intersect, one of them identically, on
the two files this build spends its whole diff in. The renderer already parses both halves of what
the check needs.

The fourth pattern has one instance and it is a blocker: B4, a spec whose reuse audit missed three
OPEN rows in its own family that had already priced its defect across four measured instances. That
is worth a leg of its own, and the leg is buildable today.

## Round 2 scope

Round 2 should read the amended specs only, with the fan primed on the actual structure of
`tools/govkit/govkit.py` around lines 6200 to 7200 rather than on the specs' description of it —
that priming gap produced most of the 33 refuted findings and cost more than the round returned. The
narrower fan §8 prescribes below 0.5 precision applies.

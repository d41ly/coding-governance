**Serves:** spec-audit TOOL-aBoundedVerdict-1..5  <!-- inferred: round 2 of 2 over the same set, per its own header -->

## Verdict: CLEAN WITH FIXES

*Review shape: raw 30, confirmed 30, refuted 0, unverified 0, precision 1.00, lenses 3/3. Round 2 of
2 — the last round the cap this build proposes would allow, applied to itself.*

**Degraded run, stated first because it changes how this record should be read.** All three lenses
returned. Every skeptic batch and the synthesis agent then died on a session limit — five refute
agents and one synth, six of nine. The harness scored all 30 findings UNVERIFIED, which is correct
and is not "clean": a finding nobody judged is outstanding, never refuted.

Rather than record a clean round over an unjudged set, the orchestrator adjudicated all 30 by hand
against source. Five needed measurement and were measured; the rest name folds made in round 1 and
were checkable by reading the fold. **All 30 hold.** They collapse to 15 distinct defects, listed
below. Precision 1.00 is therefore the orchestrator's own verdict rather than an independent
skeptic's, and it should be read with that discount — the honest limit, stated rather than implied.

**The dominant finding is that round 1's fold did not reach the whole of the specs it changed.**
Nine of the fifteen are fold-induced: a scope item left describing a data model the same fold
deleted, a taxonomy contradicted by every place its own counter is spelled, two claims of having
done something the fold asserted without doing. This is the class round 2 exists for, and it is the
argument for the cap being two rather than one.

## Round 1's findings: did the folds hold?

| Round 1 | Held? |
|---|---|
| S1 blocker — three new facts against a seven-fact pin | **Partly.** The shape split is sound and verified: the halt code is a singleton read by key, the review rounds are append-only history. But the fold did not reach the review cap's own gate scope item, which still specified a leg parsing a fact that no longer exists. Fixed in this round |
| S2 high — the method file's line-cap premise | Held. Both size paragraphs and both criteria now measure against the gated cap and the read-path ceiling |
| S3 medium — the kickoff manifest re-stamp | **Partly.** The rule was added and asserts it is in every affected unit's files list; it was in three of five. Fixed |
| S4 medium — the floor-key rationale | Held. Restated in both specs on grounds that reproduce |
| S5 low — the arms rule on the wrong instrument | Held. Restated on the pin-or-arm refusal |
| 4-B1 blocker — the predicate stated two ways | Held. One statement, conditions ordered |
| 4-B2 blocker — the item boundary | Held. Block reading, with the convention measured |
| 4-B3 blocker — the floor raise against the green bar | Held |
| 4-H1 high — a waiver mechanism that does not exist | Held. Replaced by a dated cutoff |
| 4-H2 high — the method's M3 sentence | Held. Added as a carrier |
| 4-H3 high — the kit-version marker files | Held |
| 4-M1 medium — two anti-drift artifacts | **Partly.** The case table is named consistently now, but the harness it cites works by slicing a named function and the hygiene predicate has none. Fixed in this round as a new scope item |
| 4-M2 medium — the open question's population | Held |
| 4-M3 medium — the reuse probe's real output | Held |
| 5-H1 high — the unnamed observable and the shared evaluator | **Partly.** The observable was named and the placement stated, but the count was left unqualified in four places while the taxonomy added in the same fold scoped it to one class. Fixed |
| 5-L1 low — the criterion read as a claim | Held |
| 2-H1 high — three call sites, no joining gate | Held |
| 2-H2 high — the kickoff engine's size budget | Held |
| 2-M1 medium — name both conf keys | **NOT FIXED.** The fold replaced the defect with a sentence asserting both keys were named, and named neither. Fixed in this round |
| 2-M2 medium — the criterion's prefix grep | Held |
| 3-H1 high — a gotchas run that resolves nothing | Held |
| 3-H2 high — a gate that cannot witness the claim | Held |
| 3-M1 medium — the wrong halt code for a blocked unit | Held. A member was added — and adding it stranded another, which is finding 12 below |

Four of round 1's twenty-three were not fully closed, and one was closed with an assertion rather
than a change. That is the round-2 result worth carrying forward.

## Round 2 findings, all folded in this round

| # | sev | unit | the defect |
|---|---|---|---|
| 1 | high | `TOOL-aBoundedVerdict-1` | The gate scope item still specified a leg parsing a round-count FACT after the same fold made the count derived from park lines. Two scope items describing mutually exclusive on-disk shapes — the class round 1 filed against the predicate unit. Four further sites still described the fact shape: the migration paragraph, the perf line, the observability line, and the reuse audit's named seam |
| 2 | high | `TOOL-aBoundedVerdict-5` | The taxonomy added in round 1's fold scopes the surfaced count to DECISION kinds; the scope item, the inventory row, the status line and the acceptance criterion all said parked lines unqualified. The unqualified reading is the exact failure the taxonomy exists to prevent |
| 3 | high | `TOOL-aBoundedVerdict-5` | The taxonomy had no machine home, no pin and no reader — declared in prose only, unlike the halt vocabulary, which gets a driver constant, a shrink-only floor and a leg reader. The decoration this kit already names as a defect in its own phase writer |
| 4 | high | `TOOL-aBoundedVerdict-5` | The taxonomy had no arm that could FAIL: at this unit's landing every existing kind is a decision kind, so a fixture built from today's kinds passes under a count of all lines. Vacuity by construction |
| 5 | high | SET | Both halves of the taxonomy interface asserted the method's wrap-up derivation counts decision kinds only, and no unit scoped that edit. The row demands question, options and reason — three fields a review line does not carry |
| 6 | medium | `TOOL-aBoundedVerdict-5` | Measured: the close verb appends its own override line AFTER the Definition-of-Done loop, so a count including it can never be satisfied. The acceptance fixture carried no override and passed either way |
| 7 | medium | `TOOL-aBoundedVerdict-2` | The fold asserted "Both keys are NAMED in the design" and named neither. The spec asserted a false thing about its own content |
| 8 | medium | `TOOL-aBoundedVerdict-2` | Measured: both tracked run-state files claim the landed terminal, so the population the migration's exemption, registry and enumeration serve is ZERO — and the recording it would have registered them in is read by no gate |
| 9 | medium | `TOOL-aBoundedVerdict-2` | The pin's dossier statement is TWO statements, not one, and the completeness grep as written matches only one of them |
| 10 | medium | `TOOL-aBoundedVerdict-2` | The wrap-up scope item still pointed at the build method after the same fold dropped the method from the files list on this spec's own recommendation |
| 11 | medium | `TOOL-aBoundedVerdict-2` | The gate list omitted the hygiene gate although the unit edits two files under the memory root and grows a read-path member |
| 12 | medium | `TOOL-aBoundedVerdict-2` | Adding the external-prerequisite member left the awaiting-approval member with no routing site at all: the stall unit's three cases dispose every such unit elsewhere. A vocabulary member invented ahead of its callers, in the spec that forbids exactly that |
| 13 | medium | SET | Two units each add a check to the unattended leg, and neither named the leg's header count or the charter's matching count. No gate observes either |
| 14 | medium | `TOOL-aBoundedVerdict-4` | The non-goal "no new gate leg" sat beside a files list offering a new sibling test as an alternative. The two carry different costs — a leg row, the run-gates canary, and a codebase-map key whose baseline is closed to new ones |
| 15 | medium | `TOOL-aBoundedVerdict-4` | The case-table precedent does not transfer: that harness slices a NAMED function out of shipped bytes, the hygiene predicate is inline in one long awk program with no function boundary, the two readers grade disjoint status populations, and the new cutoff makes their answers legitimately differ |

Three lows are folded without separate rows: the class named `non-decision` in one spec and `record`
in the spec that owns it, under a sentence claiming the two were spelled identically; the read-path
spender list naming two units when four spend it; and a revision log omitting the largest change in
its own revision — the taxonomy another unit depends on.

## Per-unit disposition — final

- **`TOOL-aBoundedVerdict-4` — buildable.** Round 1's three blockers held. This round added the case
  table's mechanism, which was the last thing a builder could not have derived.
- **`TOOL-aBoundedVerdict-5` — buildable.** Four findings, all on the taxonomy the previous fold
  introduced. It now has a home, a reader, a pin and an arm that can fail.
- **`TOOL-aBoundedVerdict-2` — buildable.** Six findings, all foldable; the set-level pin question
  round 1 blocked on is settled and the unit moves the pin explicitly.
- **`TOOL-aBoundedVerdict-1` — buildable.** One high, and it was the largest single gap in the set:
  the unit's only gate work described a data model that no longer existed.
- **`TOOL-aBoundedVerdict-3` — buildable.** No finding landed against its rules in either round.

## What remains for the implementing build

Not defects — work the specs deliberately leave to the pass that builds them.

- Fourteen open forks across the five specs — three, three, four, two, two, in the roster's order —
  each with a recommendation. Two are owner turns and say so: whether committing a build folder
  should be read as approving the scope of every spec inside it, and whether the vacuous-selector
  class record gains a build-method anchor. Derive the count with
  `awk '/^## 8\./,/^## 9\./' memory/builds/aBoundedVerdict/spec/*.md | grep -cE '^- \*\*F[0-9]'`
  rather than reading it here; this line said twelve until that command was run.
- Six unknowns carried from the research record, chiefly whether any producer-verb change keeps the
  driver's sibling test green — every candidate that adds a verb is unmeasured against a leg that
  took eighteen minutes on the probe host — and whether the two legs red at baseline in a clone are
  green in a real worktree.
- The corpus measurement the predicate unit's cutoff must be chosen against, which is evidence to
  record in the conf rather than a repair worklist.

## The cap, applied to this build

This is round 2, and under the rule `TOOL-aBoundedVerdict-1` proposes there is no round 3. The
verdict is CLEAN WITH FIXES and the fixes are folded, so the disposition is to build — not to review
again. Had this round returned BLOCKED, the disposition would have been the review-budget halt code
and a park, which is the rule the same unit writes.

Worth recording plainly: **round 2 found fifteen real defects, nine of them created by round 1's own
fold.** A one-round cap would have shipped all fifteen. That is the strongest evidence in this build
for the number being two, and it was produced by the build reviewing itself rather than by argument.

# TOOL-dScriptedRepeat-7 — SET-scoped checks, and where they run

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling

## 1. Goal

Give a playbook a second check population that runs over ALL N pieces at once, because every
composition failure in the reference corpus was found by measuring the set and none by measuring a
piece — and a Definition of Done that verifies each piece individually ships a monoculture green.

## 2. Scope (IN)

- **S1.** A `set_checks` population in the playbook's declaration block, parallel to the per-piece one,
  each entry tagged `GATE <leg>` or `CHECK <why>` by the same grammar unit 3 already enforces. One
  grammar, two populations — not two grammars.
- **S2.** Template section 8 (unit 2's canon) is where they are WRITTEN in prose, with the declaration
  block naming the machine half. A playbook that genuinely has none declares `none — <why>`, and unit 3
  distinguishes that from an empty section.
- **S3.** The RUN POSITION. Set-scoped checks run at `--close`, over the set unit 5's reader
  enumerates, after `pieces-complete` has established the set is non-empty and each piece is verified.
  They need no new phase: the protocol already carries `RUNNING` as "a run between named passes", and
  `RESEARCHING`/`TESTING` already establish the precedent that a position is not a pass kind.
- **S4.** The SET RECORD: one tracked record per RUN, hash-joined to the SET — the ordered list of
  piece content hashes — so a set verdict cannot survive a piece changing under it. Same four states as
  unit 5's per-piece record, for the same reason.
- **S5.** A tenth DoD item, `set-checks-recorded:machine`, asserting that a set record exists for this
  run's set and that every declared set-scoped `GATE` has a verdict in it. It asserts a verdict EXISTS
  and is bound to this set; it does not assert what the verdict concluded — the same honest limit
  `closing-review-recorded` already states about itself.
- **S6.** Arms: a set record bound to a stale set reds; a declared set-scoped `GATE` with no verdict
  blocks the close; `none — <why>` passes; the single-piece case (N=1) runs set checks rather than
  skipping them.

## 3. Non-goals (OUT)

- No new PHASE. S3's whole point. Adding one would need `CORE_FLOOR`'s phase half to move and would
  claim a pass kind the build method's closed set does not contain.
- The kit ships no set-scoped check of its own. What counts as monoculture is domain knowledge and
  belongs to the playbook, per fork 7. The kit gates that the population is DECLARED and VERDICTED.
- No averaging, no scores. A set check's verdict is binary and anchored, for the reason the reference
  corpus records: an undecided reviewer writes the midpoint, and a composite lets eight cheap passes
  drown the one failure that mattered.

## 4. Design

### The evidence this unit exists for

In the reference corpus nine articles were each reviewed carefully and each passed, and the nine
together were a monoculture no single review could have caught. The mechanism is not reviewer laziness
— it is structural: a reviewer who has just spent an hour inside one piece cannot see that its shape is
the previous piece's shape. The corpus's own repairs were all set-scoped: a byte-level repetition
invariant, a heading-level one, a register share ceiling, and a read-the-previous-piece pass. Three of
those four are machine checks, which is why this unit is not merely a documented CHECK.

A second, sharper instance is in the template's own exemplar rule: one checklist's example phrase
reached 8 of 9 bodies verbatim. Every one of those nine pieces passed every per-piece check.

### Why a share ceiling must measure the SHIPPED population

The reference's own register census counted all planned rows and reported healthy variety across
articles nobody had written, while every published row carried one value. A set-scoped check that
measures the planned set rather than the produced set is green-by-absence with extra steps. The set
this unit's checks run over is therefore unit 5's ENUMERATION of pieces that exist, never a declared
plan.

### N=1

A set of one is still a set, and it is the case where a skip is most tempting and most wrong: piece one
of a corpus is the piece every later piece will be compared against. Set checks run at N=1; a check
that is meaningless at N=1 says so in its own `<why>` rather than being skipped by the engine.

### Alternatives rejected

**A new phase, `COMPOSING`.** Rejected by S3: the position vocabulary already covers it and a new phase
member costs a floor move for no new information.

**Folding set checks into the closing review.** Rejected: `closing-review-recorded` asserts a review of
the DIFF exists. A set check is a measurement over artifacts, is machine-runnable, and would be
invisible inside a prose review record.

**Making it a documented CHECK only.** The owner considered and declined this at fork 10, and the
evidence supports the decline: three of the reference's four set-level repairs are machine invariants.

## 5. Production-readiness checklist

- security — no new execution surface beyond unit 3's registry membership.
- perf / scale — set checks are O(N) at minimum and some are O(N²) by nature, since comparing every
  piece against every other is what a repetition check does. At large N this is the expensive part of
  the close, and the playbook's own declaration is where a cheaper predicate is chosen.
- a11y — N/A.
- i18n — a repetition predicate over non-ASCII text must compare bytes or normalise deliberately; the
  kit does not choose, the playbook's leg does.
- error / empty / loading states — a set record absent, stale, orphaned or verdict-incomplete are four
  states with four messages. `none — <why>` is a fifth and distinct from all of them.
- observability — the close prints the set size, the declared set-check count and the verdict count.
- risks — the largest is that this unit gates the EXISTENCE of set checks while their QUALITY is the
  thing that matters, and a playbook can satisfy it with one trivial check. Stated in the leg header;
  the compensating control is that section 8's prose is read at every playbook review.
- testing + left-shift gates — S6, with the N=1 arm as the one most likely to be wrongly optimised away
  later.
- migration / rollback — a tenth core DoD item; `CORE_FLOOR`'s DoD half moves with unit 6's in one
  commit, and an arm asserts the INSTALLED conf.
- user docs — protocol §4 gains a row; template section 8 is the author-facing documentation.

## 6. Acceptance criteria

- **AC1** — When a playbook declares set-scoped checks and the run records a verdict for each,
  `--close` reports `set-checks-recorded` met.
- **AC2** — When a declared set-scoped `GATE` has NO verdict in the set record, `--close` BLOCKS naming
  that check. Staged and observed.
- **AC3** — When a piece is edited after the set record is written, the set record is STALE and
  `--close` blocks with a message distinct from AC2's. Observed via the ordered-hash join.
- **AC4** — When the playbook declares `set_checks` as `none — <why>`,
  `bash tools/unattended/check-playbook.sh` passes and `--close` does not block. When it declares an
  EMPTY section instead, the gate REDS. Two arms.
- **AC5** — When N is 1, set checks RUN, observed through `bash tools/unattended/check-playbook.sh`.
  Not assumed — the engine must not special-case it.
- **AC6** — When `DOD_CORE` reaches ten items, `CORE_FLOOR` moves in the same commit and an arm reads
  the INSTALLED `.unattended.conf`, not only the shipped example.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — should a set-scoped check run against pieces from PREVIOUS runs of the same playbook?** The
  monoculture the reference measured was across nine articles produced over months, not within one
  run — so a set scoped to one run's output would not have caught it. Against that: a run cannot be
  blocked by a corpus it did not produce, and unit 6 deliberately counts only the run's own pieces.
  Recommendation: the set-check population is declared per check as `run` or `corpus`, the playbook
  chooses, and a `corpus`-scoped check WARNS rather than blocks. **This is the sharpest question in the
  unit and it is genuinely open — owner input welcome, but it is mechanism, so I will resolve it at the
  first pass if you would rather not spend a turn on it.**
- **F2 — whether `set-checks-recorded` collapses into `pieces-complete`.** They read different
  populations and fail for different reasons, and this repo's own DoD history is one long argument for
  splitting terms rather than ANDing them. Recommendation: keep them separate. Deferred, not open.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. The unit exists because of the research's single strongest
  finding, which no kickoff fork covered; S3's use of an existing position rather than a new phase comes
  from the protocol's own `RESEARCHING`/`TESTING` precedent, which the contradiction hunt surfaced.

## 10. Reuse audit

The POSITION-not-a-pass-kind precedent is reused wholesale from the protocol's phase vocabulary, which
already carries two positions and a stated rule that the build method's pass set is closed — so this
unit needs no vocabulary change at all, which was not obvious before the research found it. The
ORDERED-HASH set join extends unit 5's per-piece join by the same argument, one level up. The
`closing-review-recorded` item is the model for S5's honest limit: it asserts a bound review EXISTS and
explicitly not what it concluded, and copying that phrasing is what stops this item overclaiming. The
BINARY ANCHORED VERDICT rule and the ban on averaging are the reference corpus's, adopted with its
measured reason rather than as a style preference. Recall terms used: set scope corpus monoculture
repetition census population shipped planned verdict binary anchored close position phase pass kind
definition of done record join stale.

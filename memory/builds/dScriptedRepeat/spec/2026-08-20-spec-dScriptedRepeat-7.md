# TOOL-dScriptedRepeat-7 — SET-scoped checks, and where they run

**Status:** CLOSED · rev-9 · 2026-08-22 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Give a playbook a second check population that runs over ALL N pieces at once, because every
composition failure in the reference corpus was found by measuring the set and none by measuring a
piece — and make its Definition-of-Done item read the verdicts rather than merely their existence.

## 2. Scope (IN)

- **S1.** A `set_checks` key in the playbook's declaration block, parallel to the per-piece checks key,
  each entry tagged `GATE <leg>` or `CHECK <why>` by the same grammar unit 3 already enforces. One
  grammar, two populations. Unit 2's declaration-block key list carries both keys with this unit named
  as their owner.
- **S2.** Template section 8 is where they are WRITTEN in prose, with the declaration block naming the
  machine half. A playbook with none declares `none — <why>`, and unit 3 distinguishes that from an
  empty section.
- **S3.** The RUN POSITION. Set-scoped checks run at `--close`, over `enumerate_run` as unit 5 defines
  it, after `pieces-complete` has established the set is non-empty and each piece is `verified`. No new
  phase: the protocol already carries `RUNNING` as "a run between named passes", and
  `RESEARCHING`/`TESTING` establish that a position is not a pass kind.
- **S4.** The SET RECORD: one tracked record per RUN, carrying a RUN IDENTITY and the ordered list of
  piece content hashes, written by unit 5's writer function through a set-scoped caller. The run
  identity is what makes a later run's larger set read `superseded` rather than `stale` — without it,
  run 2 makes run 1's record stale by construction and unit 6 blocks a close it has nothing to do with.
- **S5.** `set-checks-recorded:machine`, a tenth core item, with THREE terms:
  0. the recorded mode is `recipe` mode, else MET-and-announced with the `skipped` shape — the same
     term zero unit 6 carries, and for the same reason: `verb_close` evaluates `DOD_CORE` for every run
     with no mode branch, so an item only this mode can satisfy would wedge the fleet;
  1. a set record exists for THIS run's set, joined by run identity and ordered hashes;
  2. every declared `GATE`-tagged set check records a PASS. A recorded FAIL BLOCKS, naming the check.
     A `CHECK`-tagged entry keeps the existence-only limit, and the leg header states which half is
     which.
- **S6.** The `CORE_FLOOR` slack arm is unit 6's S7 and is not duplicated here. Units 6 and 7 CO-LAND
  as one commit-per-pair so the DoD half of `CORE_FLOOR` moves once, from eight to ten, with both arms
  observing the RED before it moves.
- **S7.** Arms: a set record bound to a superseded set is named as such and does not block; a declared
  `GATE` set check with no verdict blocks; a declared `GATE` set check recording FAIL blocks with a
  distinct message; a `CHECK`-tagged entry with a recorded FAIL does not block; `none — <why>` passes;
  a `slug`-mode run closes GREEN with this item present; the single-piece case runs set checks.

## 3. Non-goals (OUT)

- No new PHASE. Adding one would move `CORE_FLOOR`'s phase half and claim a pass kind the build
  method's closed set does not contain.
- The kit ships no set-scoped check of its own. What counts as monoculture is domain knowledge and
  belongs to the playbook, per fork 7. The kit gates that the population is DECLARED and VERDICTED.
- No averaging, no scores. A set check's verdict is binary and anchored, for the reason the reference
  corpus records: an undecided reviewer writes the midpoint, and a composite lets eight cheap passes
  drown the one failure that mattered.

## 4. Design

### The evidence this unit exists for

In the reference corpus nine articles were each reviewed carefully and each passed, and the nine
together were a monoculture no single review could have caught. The mechanism is structural rather than
a reviewer failing: somebody who has just spent an hour inside one piece cannot see that its shape is
the previous piece's shape. The corpus's own repairs were all set-scoped — a byte-level repetition
invariant, a heading-level one, a share ceiling, and a read-the-previous-piece pass. Three of the four
are machine checks, which is why this is not merely a documented CHECK.

### Why term 2 reads the verdict

The previous revision borrowed `closing-review-recorded`'s honest limit — assert a record EXISTS, not
what it concluded — and the audit showed the borrowing does not transfer. That item's own source
comment says a verdict grammar cannot be anchored over prose review records, which is a limitation of
prose. Here S1 makes set checks `GATE <leg>` entries and §3 makes every verdict binary and anchored, so
the stronger reading is available and declining it produced the exact failure this unit exists to
prevent: a run ships N monocultured pieces, records the repetition check FAIL, and `--close` reports
both DoD items met. The `CHECK` half keeps the existence-only limit because there the limit is real.

### Why a share ceiling must measure the SHIPPED population

The reference's own register census counted all planned rows and reported healthy variety across
articles nobody had written, while every published row carried one value. A set-scoped check measuring
the planned set rather than the produced set is green-by-absence with extra steps. The set here is
unit 5's `enumerate_run`, never a declared plan.

### N=1

A set of one is still a set, and it is where a skip is most tempting and most wrong: piece one is what
every later piece will be compared against. Set checks run at N=1; a check meaningless at N=1 says so
in its own `<why>` rather than being skipped by the engine.

### Alternatives rejected

**A new phase, `COMPOSING`.** The position vocabulary already covers it and a new member costs a floor
move for no new information.

**Folding set checks into the closing review.** `closing-review-recorded` asserts a review of the DIFF
exists. A set check is a machine-runnable measurement over artifacts and would be invisible inside a
prose record.

**Making it a documented CHECK only.** Declined at fork 10, and the evidence supports the decline.

## 5. Production-readiness checklist

- security — no new execution surface beyond unit 3's registry membership.
- perf / scale — set checks are O(N) at minimum and some are O(N²) by nature, since comparing every
  piece against every other is what a repetition check does. At large N this is the expensive part of
  the close, and the playbook's own declaration is where a cheaper predicate is chosen.
- a11y — N/A.
- i18n — a repetition predicate over non-ASCII text must compare bytes or normalise deliberately; the
  kit does not choose, the playbook's leg does.
- error / empty / loading states — set record absent, superseded, orphaned, verdict-incomplete, and
  verdict-failing are five states with five messages. `none — <why>` is a sixth and distinct.
- observability — the close prints the set size, the declared set-check count, the verdict count and
  the pass count.
- risks — this unit gates the EXISTENCE and now the VERDICTS of set checks, while their QUALITY is what
  matters, and a playbook can still satisfy it with one trivial check. Stated in the leg header; the
  compensating control is that section 8's prose is read at every playbook review.
- testing + left-shift gates — S7, with the recorded-FAIL arm and the N=1 arm as the two most likely to
  be wrongly optimised away later.
- migration / rollback — a tenth core item, inert for every run of another mode via term zero. It
  co-lands with unit 6 so `CORE_FLOOR`'s DoD half moves once.
- user docs — protocol §4 gains a row naming the mode branch and the GATE/CHECK split; template section
  8 is the author-facing documentation.

## 6. Acceptance criteria

- **AC0** — When a `slug`-mode run reaches `--close` with `set-checks-recorded` present, the item is MET
  and announces itself with the `skipped` shape naming the mode. Observed via
  `bash tools/unattended/unattended.sh --close`.
- **AC1** — When every declared `GATE`-tagged set check records a PASS, `--close` reports
  `set-checks-recorded` met.
- **AC2** — When a declared `GATE`-tagged set check has NO verdict, `--close` BLOCKS naming that check.
- **AC3** — When a declared `GATE`-tagged set check records a FAIL, `--close` BLOCKS with a message
  distinct from AC2's. Staged and observed — this is the arm that stops the monoculture green.
- **AC4** — When a `CHECK`-tagged entry records a FAIL, `--close` does NOT block, and the leg header
  states that limit. Observed, because the asymmetry is deliberate and reads like a bug otherwise.
- **AC5** — When a piece is edited after the set record is written, the set record is stale and
  `--close` blocks; when a LATER run's set is larger, run 1's record reads `superseded` and blocks
  nothing. Two arms, and the second is the one the previous revision got wrong.
- **AC6** — When the playbook declares `set_checks` as `none — <why>`,
  `bash tools/unattended/check-playbook.sh` passes and `--close` does not block. When it declares an
  EMPTY section instead, the gate REDS. Two arms.
- **AC7** — When N is 1, set checks RUN, observed through `bash tools/unattended/check-playbook.sh`.
  Not assumed — the engine must not special-case it.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — should a set-scoped check run against pieces from PREVIOUS runs of the same playbook?**
  RE-RESOLVED (agent, 2026-08-20, delegated): `enumerate_run` ONLY, which is what S3, S5 term 2 and §4
  already say. The earlier resolution invented a per-check scope field that S1's grammar does not carry,
  unit 2's key table does not own and unit 3's tag grammar does not enforce, and it shipped a
  non-blocking corpus path with no arm and no acceptance criterion — so a `GATE`-tagged corpus check
  recording FAIL both blocked and never blocked. Taking the narrow reading contradicts nothing and adds
  no unarmed behaviour. The corpus question is real and survives as a follow-up rather than as an
  unbuilt clause: a run cannot be blocked by a corpus it did not produce, and unit 6 already reports the
  `enumerate_corpus` census without blocking, which is where a later build would extend.
- **F2 — whether `set-checks-recorded` collapses into `pieces-complete`.** RESOLVED (agent,
  2026-08-20, delegated): keep them SEPARATE. They read different populations and fail for different
  reasons, and this repo's Definition-of-Done history is one long argument for splitting terms rather
  than ANDing them into a verdict that cannot say which half failed.

## 9. Revision log

- rev-9 · 2026-08-22 · the round-3 fold. `set_checks` inherits the parser refusal on a multi-line array — one parser
  meant one fix, which is what the rev-8 consolidation bought and what rev-8 itself did not spend. The declared-null
  escape on `set-checks-recorded` is an exact match rather than a prefix match, so a declared check whose name merely
  begins `none` no longer returns MET with no record; and the set writer's separator refusal names the offending
  field instead of two it cannot have come from.
- rev-8 · 2026-08-22 · the round-2 fold. The leg's `set_checks` reader gained the declared-null escape and the trim its driver sibling had, so the two readers of one field give one answer; and the idempotent path in both writers now stages what its re-stamp changed.
- rev-6 · 2026-08-21 · BUILT. The set record and its Definition-of-Done item, with term zero and
  a verdict-reading term 2. `CORE_FLOOR` moved 12:8 to 12:10 once for the co-landing pair, and the
  SLACK arm both CORE halves were missing landed with it.
- rev-5 · 2026-08-20 · folded the round-2 spec audit, which returned BLOCKED at precision 0.625 over
  the fold range. Every change here repairs a place where two sentences in this build ordered opposite
  implementations and neither was marked the loser.
- rev-4 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-3 · 2026-08-20 · owner ratified `recipe` as the authorization mode value; every reference to
  the mode (never to the playbook DOCUMENT, which keeps its name) renamed. Unit 1 S3b states the
  distinction once.
- rev-1 · 2026-08-20 · initial draft. The unit exists because of the research's single strongest
  finding, which no kickoff fork covered.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F1 added term zero, the mode branch. F4 made term 2
  read the VERDICT rather than its existence — as written, this unit closed green on a failed set check,
  which is verbatim the outcome it exists to prevent. F2 gave the set record a run identity so a later
  run supersedes rather than staling. F6 named unit 5's writer as the set record's writer too. F3 moved
  the `CORE_FLOOR` arm to unit 6 and made 6 and 7 an explicit co-landing pair, removing the
  contradiction between this spec's §5 and unit 6's S1 about which commit moves the floor. F1 of §8 is
  now resolved against unit 5's two named scopes.

## 10. Reuse audit

The POSITION-not-a-pass-kind precedent is reused wholesale from the protocol's phase vocabulary, which
already carries two positions and a stated rule that the build method's pass set is closed — so this
unit needs no vocabulary change at all, which was not obvious before the research found it. The SET
RECORD's writer is unit 5's, through a set-scoped caller rather than a second implementation. The
ORDERED-HASH join extends unit 5's per-piece join one level up, now with a run identity the audit showed
it needed. What is deliberately NOT reused any more is `closing-review-recorded`'s existence-only limit:
§4 records why the borrowing failed, and that is the more useful half of a reuse audit — a seam
correctly identified and then correctly rejected. The BINARY ANCHORED VERDICT rule and the ban on
averaging are the reference corpus's, adopted with its measured reason. Recall terms used: set scope
corpus run monoculture repetition census population shipped planned verdict binary anchored close
position phase pass kind definition of done mode branch record join superseded stale identity.

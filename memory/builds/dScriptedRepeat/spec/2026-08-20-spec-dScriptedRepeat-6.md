# TOOL-dScriptedRepeat-6 — `pieces-complete`, the ninth core Definition-of-Done item

**Status:** CLOSED · rev-8 · 2026-08-22 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Add the DoD item that means "the run made what was asked": the requested N, read from the build README
at the pinned BASE, matched against the pieces the RUN ITSELF produced and verified — mode-branched so
it cannot touch a run of another mode, with a vacuity guard, a declared grain, and a stated answer on
whether it may be overridden.

## 2. Scope (IN)

- **S1.** `pieces-complete:machine` joins `DOD_CORE` as a ninth core item. Units 6 and 7 CO-LAND, so
  the PAIR adds two items and `CORE_FLOOR`'s DoD half moves from eight to TEN in that one commit, per
  unit 7 S6. The previous revision said "rises by one in the SAME commit", which followed literally in
  the co-landing commit writes nine against ten core items and reds the bar through this unit's own new
  S7 slack arm — the arm working, on the instruction its own spec gave — the research found a recorded
  failure where a core set grew in the shipped example and not in the dogfood conf, leaving the pin
  slack while the file still looked configured. S7 is what makes that failure visible.
- **S2.** THE MODE BRANCH, and it is term ZERO because everything else depends on it. `verb_close`
  evaluates `DOD_CORE` for EVERY run with no mode branch anywhere, so an item only a playbook run can
  satisfy would block `--close` on every `slug`- and `prompt`-mode run in the fleet, on a
  non-overridable item whose only exit is `--abort`. When the recorded mode is not `recipe` mode
  this item is MET, and it ANNOUNCES that with the `skipped` shape naming the mode — never a silent
  pass, because a skip that looks like a pass is indistinguishable from coverage.
  Implemented as a branch in `dod_met`, NOT as a third `DOD_CORE` field: `checker_of` uses
  shortest-prefix removal and both consumers route a three-field entry silently down the machine path.
- **S3.** TWO NAMED ENUMERATION SCOPES, taken from unit 5: `enumerate_run` (the grain intersected with
  the paths this run introduced) and `enumerate_corpus` (the grain over the whole tree). Every term
  below names which it uses. The previous revision mixed them inside one predicate, which blocked every
  close over a tree that already held pieces — for a mode aimed at a growing corpus, that is the
  ordinary tree.
- **S4.** THE PREDICATE, evaluated in `dod_met` as SEQUENTIAL terms each with its own message:
  0. the recorded mode is `recipe` mode, else MET-and-announced (S2);
  1. `enumerate_run` resolves and yields at least one piece — the vacuity guard, and it guards term 2
     in whatever scope term 2 lands in;
  2. every piece in `enumerate_run` is `verified` in unit 5's narrowed sense — hash-joined AND every
     declared per-piece leg verdict recorded PASS. `stale`, `unrecorded`, `orphan-record` and `failed`
     each name themselves;
  3. the count of `enumerate_run` equals `pieces:` read from the README at BASE.
  The `enumerate_corpus` census is REPORTED beside these and never blocks.
- **S5.** THE RUN'S OWN PIECES. Term 3 counts pieces the run's own diff introduced under the output
  globs, using unit 8's diff population, not files present at those paths. A presence count is
  satisfied by a previous run's output, so a run producing ZERO new pieces passes whenever N or more
  already exist. The research reproduced that exact shape scoring green.
- **S6.** OVERRIDABILITY: `pieces-complete` is NOT overridable at close. §4 states why, because both
  answers are bad and the reasoning has to be on the record.
- **S7.** THE `CORE_FLOOR` SLACK ARM, which does not exist today. `check-unattended.sh:131` reds only
  when the effective DoD count is BELOW the declared floor, so growing `DOD_CORE` and leaving the conf
  untouched leaves the leg GREEN — the floor goes slack silently. This unit adds the mirror arm to
  BOTH halves, redding when a declared floor sits below the kit's own core count and naming both
  numbers, the way `DIRECTIVES_FLOOR` is already armed at `check-unattended.sh:743`.
- **S8.** Arms: the mode branch (a `slug`-mode run closes GREEN with this item present); the vacuity
  case; a stale piece; a piece whose leg verdict is FAIL; a second run over a tree already holding the
  first run's pieces; a run producing zero new pieces over a full tree; the `--override` refusal; the
  `CORE_FLOOR` slack RED.

## 3. Non-goals (OUT)

- Not a `DOD_EXTRA` item. The research reproduced that a project-declared `:machine` extra is satisfied
  by a line the run itself writes, while `--attest` refuses that same key as self-certification — a
  live driver contradiction worth filing separately, and a reason not to build on that path.
- Not an agent-attested item. The whole point is that a machine can count this. The strongest available
  evidence about attestation in this kit is a warning: an attestable-but-not-checkable item is only as
  true as the agent's model of a subsystem it cannot see, and it was wrong in good faith twice.
- No opinion on piece QUALITY beyond the recorded leg verdicts term 2 now reads. Unit 7 owns the
  set-scoped checks; unit 5 owns the per-piece record and its states.

## 4. Design

### The mode branch is the load-bearing part

`verb_close` at `unattended.sh:1650` loops `for item in $(dod)` and calls `dod_met` per item, with no
mode branch anywhere in `verb_close` (1602-1700). `DOD_CORE` at `:93` is a flat `<item>:<checker>`
grammar with no scope field, unlike `DIRECTIVES_CORE` at `:112` whose third field is exactly what makes
a directive mode-conditional. So a core item that needs `playbook:`, a grain and `pieces:` — none of
which exist under another mode — fails term 1 for every run in the fleet, on a non-overridable item.

That is not a narrow bug. It reaches runs that have nothing to do with this mode, which is why it is
term zero and why it is a branch in `dod_met` rather than a grammar change. The previous revision
asserted the opposite property without establishing it, and the audit caught it.

### Why it is not overridable, when every other machine item is

An OVERRIDABLE piece count is a run certifying its own output — the single item meaning "the build made
what was asked" becomes the one the run can wave through. A NON-overridable one can wedge a run with
nobody to interpret the block.

The wedge is the smaller cost and it is bounded by an exit that already exists: `--abort` is the
documented sole exit from a wedged run, it records a reason, and it reaches a terminal phase. With term
zero in place the wedge can only reach a run of this mode, which is the run that owes the count.

### The vacuity guard is copied deliberately

`build-complete`'s own comment records why it needs a non-empty region term: "no unit row is
non-terminal" is vacuously true over no rows at all. The identical hazard is here one level over, and
the identical repair applies. Term 1 guards term 2 and must keep doing so after the rescope in S3.

### Where the numbers come from

`pieces:` from the README blob at BASE and the grain from the playbook blob at BASE, both via unit 4's
seam. The enumeration, the four-plus-one states and the leg verdicts from unit 5. The diff population
from unit 8. This item COMPARES; it derives no population of its own, which is what keeps it from being
a second implementation confirming the first.

### Alternatives rejected

**Counting commits.** The build method's "commit at the end of every pass" does not yield one commit
per piece, and commit counting is the wrong oracle for N.

**Counting files at the output paths.** S5's whole reason.

**A third `DOD_CORE` field carrying a mode scope.** Rejected by S2: `checker_of`'s shortest-prefix
removal sends a three-field entry silently down the machine path in both consumers. The audit's own
erratum on this is worth keeping: the literal example `${p#*:}` returns `machine:recipe`, so the
misclassification is real but arrives by a different route than the previous revision described.

## 5. Production-readiness checklist

- security — the item compares a run-authored count against a run-authored README under the published
  anchor. Protocol §9's reduction applies; this is an integrity check against accident, not a proof
  against a hostile run, and the spec says so rather than implying more.
- perf / scale — one diff enumeration and one corpus enumeration per close.
- a11y — N/A.
- i18n — piece paths may be non-ASCII; the count is on paths, not on names.
- error / empty / loading states — five sequential messages, one per term including the mode
  announcement, plus the refusal on `--override`. A single verdict would send a reader to check a count
  when the grain was the problem.
- observability — the close prints the mode, the run enumeration, the corpus census, the verified count
  and the requested N, so a shortfall is legible without re-running anything.
- risks — the diff population is the risk. Naive `BASE..HEAD` was measured wrong by a large factor and
  `--no-merges` is not the repair. Unit 8 owns the population and this item consumes it, so 6 and 8
  CO-LAND; the build README's predecessor list carries that constraint.
- testing + left-shift gates — S8. The mode-branch arm and the zero-new-pieces-over-a-full-tree arm are
  the two that matter most, because both PASS today under the obvious implementation.
- migration / rollback — a ninth core item that, with term zero, is inert for every run of another
  mode. Nothing in flight is affected and the arm in S8 observes that rather than asserting it.
- user docs — protocol §4's DoD table gains a row naming the mode branch; the Skill documents the
  shortfall message.

## 6. Acceptance criteria

- **AC0** — When a `slug`-mode run reaches `--close` with `pieces-complete` present in `DOD_CORE`, the
  item is MET and the output carries the `skipped` shape naming the mode. Observed via
  `bash tools/unattended/unattended.sh --close`, and staged BEFORE the branch lands to see it block.
- **AC1** — When `enumerate_run` yields zero pieces on a `recipe`-mode run, `--close` BLOCKS with the
  vacuity message, not with a count mismatch. Staged and observed.
- **AC2** — When one piece is `stale`, `--close` blocks with a message naming staleness and the piece.
- **AC3** — When the tree already holds N pieces and the run produced NONE, `--close` BLOCKS. Staged
  against a pre-populated output tree; this is the case a presence count passes.
- **AC4** — When the run produced exactly `pieces:` pieces, each hash-joined AND each declared per-piece
  leg recorded PASS, `--close` reports `pieces-complete` met.
- **AC5** — When a piece is hash-fresh but records a FAILING leg verdict, `--close` BLOCKS with a
  message distinct from AC2's. Staged and observed — this is the arm that makes fork 5 real.
- **AC6** — When a SECOND run of the same playbook closes over a tree already holding run 1's pieces,
  `--close` reports met, and the `enumerate_corpus` census is printed and does not block. Observed.
- **AC7** — When `--override pieces-complete` is passed, `bash tools/unattended/unattended.sh` REFUSES
  with a message stating the item is not overridable and naming `--abort` as the honest exit.
- **AC8** — When `DOD_CORE` holds ten items and the installed `.unattended.conf` still declares a DoD
  floor of eight, `bash tools/unattended/check-unattended.sh` REDS naming both numbers. Staged and
  observed; today this passes GREEN, which is the whole reason S7 exists.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/unattended.test.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — does `pieces:` mean "at least N" or "exactly N"?** RESOLVED (agent, 2026-08-20, delegated):
  exactly N. The playbook declares the grain, so a surprise extra is a grain bug more often than a
  bonus, and an owner who wanted a range can declare one in a later revision of this item rather than
  inherit an unstated tolerance.
- **F2 — the moment `stale` is judged.** RESOLVED (agent, 2026-08-20, delegated): the RULING lives in
  unit 5 S9, where the reader lives. This fork is a POINTER at that ruling and not its owner.

## 9. Revision log

- rev-8 · 2026-08-22 · the round-2 fold. `--counts` takes the pinned BASE sha and reads the playbook from the blob, so `pieces-complete` can no longer be moved by an uncommitted edit — the round-1 fix pinned `grain` and `records` and left `piece_checks` on the working tree, which defeated the item this same build had made non-overridable.
- rev-6 · 2026-08-21 · BUILT, with one divergence recorded rather than made silently. S5 said term 3
  counts pieces using unit 8's diff population; it counts them through unit 5's `enumerate_run`
  instead, which derives the run's own pieces from the run identity each RECORD carries. That is the
  direction the round-2 fold pushed for (D11): the diff population needs a live remote observation
  and a run-state file, and the reader that owns this enumeration has neither on the merge bar.
  Unit 8 is not landed, so consuming it was not available either.
- rev-5 · 2026-08-20 · folded the round-2 spec audit, which returned BLOCKED at precision 0.625 over
  the fold range. Every change here repairs a place where two sentences in this build ordered opposite
  implementations and neither was marked the loser.
- rev-4 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-3 · 2026-08-20 · owner ratified `recipe` as the authorization mode value; every reference to
  the mode (never to the playbook DOCUMENT, which keeps its name) renamed. Unit 1 S3b states the
  distinction once.
- rev-1 · 2026-08-20 · initial draft. S5 comes from a reproduced false green in the research; the
  vacuity guard and the sequential-message shape are both copied from `build-complete`'s own recorded
  repairs.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F1 added term zero, the mode branch, after the audit
  established that `verb_close` evaluates `DOD_CORE` for every run — the previous revision would have
  wedged every non-playbook unattended run in the fleet. F2 split the enumeration into two named scopes.
  F3 added S7's missing `CORE_FLOOR` slack arm, which is why AC8 is now a RED observation rather than a
  green one. F5 narrowed term 2 to require recorded leg PASSes. F7 moved the `stale` ruling to unit 5.

## 10. Reuse audit

`build-complete` is the seam and this item is deliberately its sibling rather than its generalisation:
same evaluation site in `dod_met`, same sequential-terms-with-own-messages shape, same non-empty
vacuity guard, same `checker_of` two-field grammar. Every one of those properties exists because
`build-complete` was built wrong first and repaired. Inheriting a repaired shape is the cheapest
correctness available here — and the audit demonstrated the converse, since the one place this unit
did NOT inherit an existing shape (the mode branch, which `DIRECTIVES_CORE` solves with a third field
and `DOD_CORE` cannot) is exactly where it broke. The `CORE_FLOOR` slack arm in S7 is not a new
mechanism either: it is the mirror of `DIRECTIVES_FLOOR`'s arm at `check-unattended.sh:743`, which
already reds a floor declared below the kit's own core count. Recall terms used: definition of done
item machine checker core floor slack vacuous region term override budget abort wedged run mode branch
diff population enumeration grain count skipped announcement.

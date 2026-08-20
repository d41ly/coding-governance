# TOOL-dScriptedRepeat-6 — `pieces-complete`, the ninth core Definition-of-Done item

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling

## 1. Goal

Add the DoD item that means "the run made what was asked": the requested N, read from the build README
at the pinned BASE, matched against the pieces the RUN ITSELF produced and verified — with a vacuity
guard, a declared grain, and a stated answer on whether it may be overridden.

## 2. Scope (IN)

- **S1.** `pieces-complete:machine` joins `DOD_CORE` as a ninth core item, and `CORE_FLOOR`'s DoD half
  rises by one in this repo's `.unattended.conf` in the SAME commit — the research found a recorded
  failure where a core set grew in the shipped example and not in the dogfood conf, leaving the pin
  slack while the file still looked configured.
- **S2.** The PREDICATE, evaluated in `dod_met` as SEQUENTIAL terms each with its own message, never
  one ANDed verdict. The terms, in order, structure before content:
  1. the declared grain resolves and ENUMERATES at least one piece — the vacuity guard;
  2. every enumerated piece is `verified` by unit 5's reader, with `stale`, `unrecorded` and
     `orphan-record` each naming themselves;
  3. the count of pieces THIS RUN produced equals `pieces:` read from the README at BASE.
- **S3.** The RUN'S OWN PIECES. Term 3 counts pieces the run's own diff introduced under the output
  globs, not files present at those paths. A presence count is satisfied by a previous run's output,
  so a run producing ZERO new pieces passes whenever N or more already exist — which for a mode
  explicitly aimed at a growing corpus is the ordinary tree, not an edge case. The research reproduced
  this exact shape scoring a green.
- **S4.** OVERRIDABILITY: `pieces-complete` is NOT overridable at close. §4 states why, because both
  answers are bad and the reasoning has to be on the record.
- **S5.** `checker_of` must not misclassify. It uses shortest-prefix removal, so a hypothetical
  three-field item would silently parse as `machine`; this item stays two-field for that reason and the
  constraint is recorded here rather than rediscovered.
- **S6.** Arms: the vacuity case (zero pieces enumerated) BLOCKS; a stale piece blocks with its own
  message; a run producing zero new pieces over a tree that already has N blocks; the happy path
  passes; the `--override` attempt is refused.

## 3. Non-goals (OUT)

- Not a `DOD_EXTRA` item. The research reproduced that a project-declared `:machine` extra is satisfied
  by a line the run itself writes, while `--attest` refuses that same key as self-certification —
  a live driver contradiction worth filing separately, and a reason not to build on that path.
- Not an agent-attested item. The whole point is that a machine can count this. The strongest available
  evidence about attestation in this kit is a warning: an attestable-but-not-checkable item is only as
  true as the agent's model of a subsystem it cannot see, and it was wrong in good faith twice.
- No opinion on piece QUALITY. Unit 7 owns the set-scoped checks and unit 5 owns per-piece verdicts.

## 4. Design

### Why it is not overridable, when every other machine item is

Both answers are bad and the choice is between two costs. An OVERRIDABLE piece count is a run
certifying its own output — the single item that means "the build made what was asked" becomes the one
the run can wave through, which is the shape the DoD's own comments already warn about for
`build-complete`. A NON-overridable one can wedge a run with nobody to interpret the block.

The wedge is the smaller cost, and it is bounded by an exit that already exists: `--abort` is the
documented sole exit from a wedged run, it records a reason, and it reaches a terminal phase. So a run
that genuinely cannot meet its piece count stops honestly rather than landing a shortfall with an
override that reads like a check that failed. Recorded as a decision rather than a default, because the
override budget's whole design is that an item names its escape.

### The vacuity guard is copied deliberately

`build-complete`'s own comment records why it needs a non-empty region term: "no unit row is
non-terminal" is vacuously true over no rows at all. The identical hazard is here one level over —
"every piece is verified" is vacuously true over no pieces — and the identical repair applies. Copying
a term whose failing case is already recorded is cheaper and more trustworthy than inventing one.

### Where the numbers come from

`pieces:` comes from the README blob at BASE (unit 4). The grain comes from the playbook blob at BASE
(unit 4). The enumeration and verdicts come from unit 5's reader. This item COMPARES; it derives no
population of its own, which is what keeps it from being a second implementation confirming the first.

### Alternatives rejected

**Counting commits.** The build method's "commit at the end of every pass" does not yield one commit
per piece, and commit counting is the wrong oracle for N. Only one research lens noticed.

**Counting files at the output paths.** S3's whole reason.

**A third `DOD_CORE` field carrying a mode scope.** Rejected by S5: `checker_of`'s shortest-prefix
removal would read the scope as the checker.

## 5. Production-readiness checklist

- security — the item compares a run-authored count against a run-authored README under the published
  anchor. §9's reduction applies; this is an integrity check against accident, not a proof against a
  hostile run, and the spec says so rather than implying more.
- perf / scale — one diff enumeration per close.
- a11y — N/A.
- i18n — piece paths may be non-ASCII; the count is on paths, not on names.
- error / empty / loading states — three sequential messages, one per term, plus the refusal on
  `--override`. A single verdict would send a reader to check a count when the grain was the problem.
- observability — the close path prints enumerated, verified and requested as three numbers, so a
  shortfall is legible without re-running anything.
- risks — the diff population is the risk. Naive `BASE..HEAD` was measured wrong by up to a factor of
  22 on a real build, and `--no-merges` is not the repair because merges carry combined-diff changes.
  Unit 8 owns the diff population and this item consumes it; the two must land together or this term
  counts the wrong thing.
- testing + left-shift gates — S6, with the zero-new-pieces-over-a-full-tree arm as the one that
  matters most, because it is the case that passes today under the obvious implementation.
- migration / rollback — a ninth core item reds any in-flight run of the new mode until met; no
  existing run has the mode, so nothing in flight is affected.
- user docs — protocol §4's DoD table gains a row; the Skill documents the shortfall message.

## 6. Acceptance criteria

- **AC1** — When the grain enumerates zero pieces, `--close` BLOCKS on `pieces-complete` with the
  vacuity message, not with a count mismatch. Staged and observed.
- **AC2** — When one piece is `stale`, `--close` blocks with a message naming staleness and the piece.
- **AC3** — When the tree already holds N pieces and the run produced NONE, `--close` BLOCKS. Staged
  by running against a pre-populated output tree; this is the case a presence count passes.
- **AC4** — When the run produced exactly `pieces:` verified pieces, `--close` reports
  `pieces-complete` met.
- **AC5** — When `--override pieces-complete` is passed, the driver REFUSES with a message stating the
  item is not overridable and naming `--abort` as the honest exit. Observed.
- **AC6** — When `DOD_CORE` grows, `CORE_FLOOR` in `.unattended.conf` rises in the same commit and
  `bash tools/unattended/check-unattended.sh` is green; an arm asserts the INSTALLED conf, not only
  the shipped example — the research found the installed one graded by nothing.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/unattended.test.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — does `pieces:` mean "at least N" or "exactly N"?** An owner asking for ten articles who gets
  eleven has not been wronged; an owner asking for one hero image who gets three has. Recommendation:
  exactly N, because the playbook declares the grain and a surprise extra is a grain bug more often
  than a bonus. **Agent-resolvable, recorded because the opposite reading is defensible.**
- **F2 — the moment `stale` is judged.** Unit 5 F2 deferred this here. Recommendation: `--close`
  evaluates staleness strictly; a run mid-fold has not closed yet, so the distinction resolves by
  WHEN the item is evaluated rather than by a severity knob. RESOLVED (agent, 2026-08-20, delegated):
  evaluate at close only.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. S3 comes from a reproduced false green in the research; the
  vacuity guard and the sequential-message shape are both copied from `build-complete`'s own recorded
  repairs; F2 resolves unit 5's deferred question.

## 10. Reuse audit

`build-complete` is the seam and this item is deliberately its sibling rather than its generalisation:
same evaluation site in `dod_met`, same sequential-terms-with-own-messages shape, same non-empty-region
vacuity guard, same `checker_of` two-field grammar. Every one of those properties exists because
`build-complete` was built wrong first and repaired — the units region term replaced an authored roster
term that only four of forty-nine build folders carried, and the ANDed verdict was split after readers
could not tell a missing spec from an unfinished unit. Inheriting a repaired shape is the cheapest
correctness available here. The one thing NOT reused is its population: `build-complete` reads the
generated units region and this item reads a filesystem enumeration joined to unit 5's records, because
pieces are passes and never units. Recall terms used: definition of done item machine checker core
floor vacuous region term override budget abort wedged run diff population enumeration grain count.

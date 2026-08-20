# TOOL-dUnstalledConvoy-10 — the leg compares a declared write set against the paths the pass actually committed

**Status:** CLOSED · rev-5 · 2026-08-21 · node d · Tier-2 · base 2dc9df35 · streams tooling · ratified 2026-08-20

## 1. Goal

`TOOL-dUnstalledConvoy-9` records what a concurrently dispatched pass SAID it would write. This unit
adds one check comparing that declaration against what the pass actually committed, joined by the
unit id M6 already requires in a pass's commit subject. It is what turns the declaration from a
formality into a claim that can be caught out.

## 2. Scope (IN)

- **S1** — a new check inside `tools/unattended/check-unattended.sh`, not a new gate leg, for the
  reason units 6 and 13 give.
- **S2** — for each `dispatch` row, the check selects the FIRST commit after the row's recorded group
  anchor whose subject names the row's unit id, and grades that one alone. Later commits naming the
  same unit are outside the group BY CONSTRUCTION. Review fold: H7, whose second disposition this is.
  An open-topped range graded every later commit against a window that had closed — and M6's pass set
  includes a spec reviewed and a review's fixes folded in, both of which routinely happen after a
  concurrent group ends, so an ordinary sequential fold would have redded the bar with no in-band
  repair. **Amended at rev-3, before any code:** H7's FIRST disposition was a recorded CLOSE anchor,
  and it needs a verb and a row type the sibling unit never built. A first-commit rule needs neither,
  bounds the window just as tightly, and cannot drift out of step with a close nobody remembered to
  record. The cost is stated rather than hidden: a pass that legitimately commits TWICE inside its own
  group has only its first commit graded, which is a narrower check than a close anchor would give.
- **S3** — the union of paths those commits touched must be a SUBSET of the row's declared set. A
  path outside it is a refusal naming the unit id, the path, and the commit that carried it.
- **S4** — the no-commit case is SPLIT, because one line was covering two very different states, and
  the split keys on the DECLARED PATHS rather than on subject-naming. Review fold: M2, refined at
  rev-4. An empty outcome is an announced observation: a declared pass that produced no change is
  legal and M6 says so. But if any commit after the group anchor TOUCHES A PATH IN THAT PASS'S
  DECLARED SET while no commit names the unit, that is the evasion — the declared work happened and
  the join was dodged — and it is a REFUSAL. The first draft keyed the refusal on a commit whose
  subject named no unit id at all, which would red on every ordinary witness or bookkeeping commit a
  run makes between passes, so it was a check that reds on correct behaviour. Keying on the declared
  paths catches exactly the case the finding was about and nothing else.
- **S5** — a commit whose subject names TWO unit ids from the same group is a refusal, because the
  join becomes ambiguous and a subset test over an ambiguous attribution proves nothing.
- **S6** — every case the check cannot compare ANNOUNCES itself: an unresolvable group anchor, a run
  with no `dispatch` rows, or a tip that is not a descendant of the anchor.
- **S7** — the check's header states what it does not buy, and specifically that both of its inputs
  are inside the run's reach.

## 3. Non-goals (OUT)

- Re-deciding M6's conditions 1 and 3. `TOOL-dUnstalledConvoy-9` refuses those at declaration time,
  and repeating them here would recompute the driver's answer from the driver's inputs.
- Deciding M6's condition 2. Neither the verb nor this check can decide whether a file is a contract
  the sibling reads, and both say so.
- Refusing a declared path the pass did NOT write. Declaring more than you use is conservative and
  safe; the subset direction is the one that matters.
- Grading sequential passes. A pass with no `dispatch` row was not dispatched concurrently and has
  nothing here to compare.
- Terminal records, which are frozen.

## 4. Design

### The join, and why it exists already

M6 requires the unit id in every pass's commit subject. `TOOL-dUnstalledConvoy-9` requires `--pass`
to be a unit id rather than a free label for exactly this reason. So the join between a declaration
and a commit is a rule the method already enforces for its own reasons, and this check consumes it
rather than inventing an attribution mechanism.

That is also why S5 refuses an ambiguous subject. The join is a substring match on a distinctive id,
and two ids from one group in one subject makes the subset test unattributable — the same defect as
an arm that cannot fire, one level up.

### Inventory

| Case | Verdict |
|---|---|
| committed paths are a subset of declared | pass |
| a committed path is outside the declared set | refusal naming id, path and commit |
| no commit names the unit id | announced observation, not a refusal |
| one commit names two ids from the same group | refusal, ambiguous attribution |
| group anchor unresolvable, or tip not a descendant | announced skip |
| run has no `dispatch` rows | announced skip, so a green row is not read as coverage |

### Why this is a second opinion

The declaration is written before the dispatch. The commits are written after it. They are two
artifacts produced by two acts at two times, and the check compares them rather than re-deriving
either. A pass that quietly wrote outside its lane is caught by exactly this and by nothing else in
the tree.

What it cannot buy, stated in the header: both artifacts are authored by the run, so a run determined
to hide a collision can declare the wider set up front. That is a more expensive lie than the failure
this catches, and the check does not claim to reach it. This is the repo's `inputs-inside-the-
subjects-reach` class, and naming it in the header is what stops a green row reading as proof of
disjointness.

### The vacuity risk, which is the main one

Every row in the inventory above except the first two can produce a green verdict over nothing. A run
with no dispatch rows, an unresolvable anchor, or a group whose passes made no commits all yield an
empty comparison. S4 and S6 exist so each announces itself; without them this check would be green on
every run in the tree today and would look like coverage of a mechanism nobody has used yet.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | one check, three refusals, three announced skips |
| `tools/unattended/check-unattended.test.sh` | the cases in §6 and the `ARMS_FLOORS` bump |
| `.memory-tree.conf` | the `ARMS_FLOORS` entry this unit moves — a BUILD-WIDE shared write, review fold M7 |

### Alternatives rejected

- **Attributing commits by author or timestamp.** Rejected: sidechain passes commit as the same
  author, and timestamps do not partition a group whose passes overlap by design.
- **Requiring a trailer rather than a subject substring.** Rejected: M6 already mandates the subject,
  and a second attribution channel would be a second answer to one question. If the subject join
  proves too weak in practice, a trailer is the follow-up, recorded as such.

## 5. Production-readiness checklist

- security — the check grades a claim the run made against commits the run authored, and the header
  says what that buys.
- perf / scale — one `rev-list` and one `diff-tree` per dispatch row.
- a11y — N/A — a shell gate with no user surface.
- i18n — N/A — the same.
- error / empty / loading states — S4 and S6 are this item, and §4 names them as the main correctness
  risk rather than a tidiness one.
- observability — three distinct refusals and three announced skips.
- risks (concurrency, data-loss, rollback hazards) — read-only.
- testing + left-shift gates — the cases in §6, each arm carrying the entire literal signature of its
  branch. Adding branches renumbers the ordinals below the insertion point.
- migration / rollback — no run in this tree has a `dispatch` row, so the check announces a skip
  everywhere until the first concurrent dispatch lands. That is the correct initial state and AC7
  asserts it rather than letting it read as green.
- user docs — the check's OWN SOURCE HEADER, which is how all twenty-one existing checks in this leg
  are documented and which S7 already requires. Review fold: M8. The protocol section this first
  pointed at does not exist, and the unit it was delegated to never creates one.

## 6. Acceptance criteria

- **AC1** — A fixture whose pass commits a path inside its declared set passes, observed in `tools/unattended/check-unattended.test.sh`.
- **AC2** — A fixture whose pass commits a path outside its declared set reds, naming the unit id,
  the path and the commit, observed in `tools/unattended/check-unattended.test.sh`.
- **AC3** — A fixture whose range between the anchors is EMPTY produces an announced observation and
  does NOT red; a fixture whose range holds a commit with an id-less subject REDS. Both observed in
  `tools/unattended/check-unattended.test.sh`. Review fold: M2, one criterion per branch.
- **AC9** — A fixture whose pass commits, and then commits AGAIN later naming the same unit id with a
  path outside the declared set, PASSES — the second commit is outside the group by construction.
  Observed in `tools/unattended/check-unattended.test.sh`. Review fold: H7.
- **AC10** — The header of the new check STATES what it cannot buy, observed by `grep` over
  `tools/unattended/check-unattended.sh`. Review fold: L1.
- **AC4** — A fixture with one commit naming two unit ids from the same group reds on ambiguous
  attribution, observed in `tools/unattended/check-unattended.test.sh`.
- **AC5** — A fixture whose group anchor cannot be resolved prints an announced skip and does not
  red, observed in `tools/unattended/check-unattended.test.sh`.
- **AC6** — A fixture declaring three paths and committing one passes, confirming the subset
  direction, observed in `tools/unattended/check-unattended.test.sh`.
- **AC7** — Run against this repo as it stands today, the check prints its no-dispatch-rows skip, and
  `bash tools/unattended/check-unattended.sh` exits 0 with that line present.
- **AC8** — Each refusal is observed RED against a fixture before the unit lands, observed in `tools/unattended/check-unattended.test.sh`.

## 7. Gates

`unattended kit gate` · `unattended kit selftest` · `harness arms` · the full bar at the push
boundary.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): RED, with the widening repair. A report-only check is the toothless state the directive is already in and which the owner's report is about. The repair keeps it from becoming a wedge: `--dispatch` may be re-run with a widened set before the commit, and re-declaring before committing is the honest act the rule wants. The sibling verb's idempotence rule already admits a widening, folded at its rev-3.**

  The question this settles: should a path outside the declared set RED, or be reported? Redding is the point of the
  unit, but it means a run that legitimately discovers a needed file mid-pass has its bar go red with
  no in-band repair, which is the wedge shape this build exists to remove. Options: red, and give the
  run a repair by letting `--dispatch` be re-run with a widened set before the commit; or report
  only. **Recommendation: red, WITH the widening repair.** A report-only check is the toothless state
  the directive is already in. The repair keeps it from becoming a wedge, and re-declaring before
  committing is exactly the honest act the rule wants. This changes `TOOL-dUnstalledConvoy-9`'s
  idempotence rule to admit a widening of an existing row, so it must be resolved before either unit
  builds.

## 9. Revision log

- rev-5 · 2026-08-21 · built, and ONE defect the spec could not have predicted: `--dispatch` STAGES
  the run-state file, so the run commits the DECLARATION itself — and that commit's subject names the
  unit, being about it. The join therefore read the declaration as the pass's own commit, ran the
  subset test against a diff touching only the run-state file, and redded every correctly declared
  pass. A run-state bookkeeping commit is not a pass commit, and the check now says so and skips it.
  Caught by the fixture, like every other defect this build has found in its own checks.
- rev-4 · 2026-08-21 · S2 amended before any code, per M2. rev-3 folded H7 as a recorded group CLOSE
  anchor, and that needs a verb and a row type `TOOL-dUnstalledConvoy-9` never built — the same
  cross-spec interface gap the widening rule was, caught the same way, by reading the pair together at
  the pass boundary. H7's SECOND disposition needs neither: the FIRST commit after the anchor naming
  the unit is the pass's commit, and later ones are outside the group by construction. It bounds the
  window just as tightly and cannot drift out of step with a close nobody remembered to record. The
  narrower coverage it buys — a pass that commits twice inside its own group has only its first commit
  graded — is stated in S2 rather than left implicit. S4 is refined in the same pass: its refusal keys
  on the DECLARED PATHS being touched without the unit being named, because the drafted version keyed
  on a subject naming no unit id and would have redded on every witness commit a run makes between
  passes — a check that reds on correct behaviour.
- rev-3 · 2026-08-20 · folded the spec audit: H7 (the commit range gains a recorded CLOSE anchor, so a
  later sequential fold is not graded against a window that has closed), M2 (the no-commit case splits
  — an empty range announces, an id-less subject reds), M8 (documentation is the check's own source
  header), M14 (§10 corrected: the leg holds no id pattern at all), L1. Three new criteria.
- rev-2 · 2026-08-20 · §10 corrected: the `id_pattern` seam is unreachable from a shell leg in a
  standalone-installed kit; the id shape comes from `_ids_of`. Same correction as unit 5 rev-2.
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "compare what a commit touched against what was declared"`
returns the `unattended` affordance seam and the `row-grammar` dossier. The `id_pattern` seam in that
dossier is REJECTED for the same reason `TOOL-dUnstalledConvoy-5` rejects it: it is Python in a
separately-installed kit and this leg is shell. **And the leg does not mirror the driver's `_ids_of`
either — grepping it for that helper returns nothing and it carries no id pattern of any kind.**
Review fold: M14. The seam that exists is the leg's parse of the driver's core sets out of the driver
SOURCE, which its own header defends on the ground that a second spelling is the drift the leg exists
to catch. The id pattern rides that parse or becomes a named driver constant, and either way this is a
driver-side edit as well as a leg edit, which `TOOL-dUnstalledConvoy-6` now carries in its
Files-touched table. The check reuses the leg's existing anchor loop and the same
region reader every sibling check uses.

`python tools/memory-recall/query.py "how does a gate attribute a commit to the pass that made it"
--terms "commit subject unit id pass attribution join declared write set subset dispatch group anchor
rev-list"` returns M6's commit rule, the parallelism verdict, and the record on arms whose fixtures
never fire. Verified at source at writing time: M6 states the unit id in the subject as a commit
rule, and the parked-region grammar parses line-wise, which is why `TOOL-dUnstalledConvoy-9` refuses
newlines in the fields this check reads.

Recall terms used: commit subject unit id pass attribution join declared write set subset dispatch
group anchor rev-list.

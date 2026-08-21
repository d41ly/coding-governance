# TOOL-dUnstalledConvoy-23 — the dispatch write-set comparison becomes a REPORT, and is made accurate enough to be worth reading

**Status:** SPECCED · rev-3 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

## 1. Goal

check 23 compares what a dispatched pass DECLARED against what it COMMITTED. It ships dark today
because no version of it could be trusted as a merge-bar failure. This unit makes the comparison
accurate and ships it as a REPORT that always runs and never fails the bar.

The owner resolved the fork this rests on. Two review rounds established that a hard gate and a
stall-free run are incompatible here, and the argument is short: an in-band exit for a mis-declared
pass requires a later declaration to cover an earlier commit, and that is retraction — the defect that
turned this dark. Verified rather than reasoned: `pass_commit` opens its window as `"$_pa..HEAD"`,
which EXCLUDES the anchor, so a corrective declaration anchored at or after the offending commit can
never contain it. rev-2 claimed union supplied that exit. It does not, and the claim is retracted.

## 2. Scope (IN)

- **S1 — the comparison is a REPORT.** check 23 emits on the report channel and never sets the leg's
  status. `DISPATCH_GRADING` and the dark announcement are both DELETED, in the engine, both confs, the
  shipped example and the protocol's key table — with a report there is no failure to gate, so there is
  nothing to flip and no rollback key to keep.
- **S2 — the reported set for a unit is the UNION of its rows whose window contains the commit.** The
  record is append-only and the driver tells a run needing more paths to declare again; the leg's fold
  keeps only the LAST row per `(group, unit)` and discards the rest. Union does not rescue a post-hoc
  widening, and must not: a row anchored after the commit has a window that excludes it.
- **S3 — a row's window is stated, not implied.** It opens AFTER the row's own anchor and closes AT the
  next anchor for the same unit, inclusive of that anchor's commit. Rows are ordered by ANCESTRY, not
  by file order. A row whose anchor is not an ancestor of HEAD is an announced skip.
- **S4 — the no-commit branch's path scan takes the same upper bound.** It scans `anchor..HEAD` today
  and S3 does not reach it.
- **S5 — `normpath` handles an interior `/./` and a trailing `/.`**, both broken by one missing case.
- **S6 — the empty-proof announcement measures condition 1's own population**, not `sibrows`.
- **S7 — the orphaned widening prose is deleted from BOTH carriers**: `unattended.sh`'s
  re-declaration-rule comment sitting above the code that replaced it, and the matching block in
  `check-unattended.sh`. One of them is where rev-1 of this spec got its false mental model.
- **S8 — the two arms round 4 named as missing:** the `case`-to-`covers` leg fix reverts green today,
  and cross-component arm 3b never lets either pass commit.
- **S9 — every change lands with its arm in the same commit.** An arm over a REPORT asserts the text
  AND a negative control asserting silence, because a report cannot be observed RED the way a failure
  can and "it printed nothing" is what a broken report also does.

## 3. Non-goals (OUT)

- **Any re-declaration, widening, narrowing or retraction machinery.** `e42cb5a` removed it with a
  recorded verdict; arm C pins the absence, and a later declaration rescuing an earlier finding is the
  exact vector that turned this dark.
- **Any reading in which check 23 can fail the bar.** That is the owner's resolution, not an
  implementation detail, and a later unit that re-arms it owes the stall argument an answer.
- `pass_commit`'s permissiveness; `normpath`'s collapse-then-strip ordering; condition 1 and condition
  3's refusals; the overlap gate; arm 3b's existence.
- The declaration grammar, the recording verb, the acceptance ledger, the landing anchors.

## 4. Design

S1 is the whole shape and everything else serves it. A report that is wrong is worse than no report,
because it will be read; so S2–S6 are the accuracy work, and S9 is what makes them checkable.

S2 is the finding rev-1 missed and rev-2 got half right. Two `--dispatch` calls at an unmoved HEAD park
two rows under one key and the leg's `row[k] = $0` overwrites, so a pass that declared `work/a` then
`work/b` and wrote both is reported against `work/b` alone. Union over WINDOWED rows fixes that without
touching arm C: the post-hoc row's window starts after the offending commit, so it contributes nothing
to the set that commit is compared against.

S3 exists because rev-2 stated a bound and left its boundary and ordering undefined, and a reviewer
traced the exclusive reading flipping arm C from RED to green. Writing the rule down is the fix; the
inclusive upper bound is chosen because a commit AT the next anchor is the next pass's first commit
under `pass_commit`'s exclusive lower bound, and the two must not both disown it.

S7 is not tidying. Two files carry prose describing machinery a third commit deleted, and one of them
taught rev-1 of this spec a rule that no longer existed. That cost two revisions.

What this unit does NOT buy, stated here so a green report is not over-read: it compares two artifacts
the run itself authored, it cannot see a wide declaration made up front, and it never fails. It tells a
reader what a pass said versus what it did.

## 5. Production-readiness checklist

- **security** — unchanged, and weaker by design: a report cannot block. The disjointness REFUSALS at
  declaration time (conditions 1 and 3) are untouched and remain the enforcing half.
- **perf/scale** — S3 and S4 narrow both windows; S2 reads more rows per unit. Net work falls.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — S6 is exactly this, and S3's non-ancestor case is an announced skip.
- **observability** — this unit IS the observability change; the report channel already exists and is
  read by `GOV_UNATTENDED_REPORT`.
- **testing/gates** — the driver, leg and cross-component suites, plus the full bar. Deleting
  `DISPATCH_GRADING` touches the adopter and its e2e arm.
- **migration/rollback** — a report cannot wedge a run, so the rollback the conf key existed to provide
  is no longer needed. Rollback is a revert.
- **help/ docs** — `PROTOCOL.template.md`'s key table loses `DISPATCH_GRADING`; both confs and the
  shipped example lose the key; S7 deletes two stale prose blocks.

## 6. Acceptance criteria

- **AC1** — `grep -c DISPATCH_GRADING` returns 0 across the engine, both confs, the shipped example and
  the protocol template, observed by `grep`.
- **AC2** — a unit with two rows at ONE anchor committing inside the union of both produces NO report
  line, and committing outside it produces one naming the path, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC3** — arm C still reports: a widened row at a LATER anchor does not clear the earlier finding,
  observed in `tools/unattended/check-unattended.test.sh`.
- **AC4** — the fold emits one row per `(group, unit)` per distinct anchor and discards none, asserted
  by comparing the fold's row count against the file's, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC5** — a row whose unit has a later anchor is compared only against commits in `(own, next]`, with
  an arm on each boundary, observed in `tools/unattended/check-unattended.test.sh`.
- **AC6** — the no-commit branch's scan takes the same upper bound, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC7** — `normpath` returns `a/b` for `a/./b`, `a/b/.`, `a/b/./` and `./a/./b/.`, observed in
  `tools/unattended/unattended.test.sh`.
- **AC8** — the empty-proof announcement fires when condition 1's population is empty and is silent
  otherwise, observed in `tools/unattended/unattended.test.sh`.
- **AC9** — the leg's exit status is 0 for every check-23 discrepancy, asserted directly, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC10** — `grep -c 'RE-DECLARATION RULE'` returns 0 in both `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh`, observed by `grep`.
- **AC11** — round 4's `case`-to-`covers` fix reverts to a changed report, and arm 3b commits for at
  least one pass, observed in `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/cross-component.test.sh`.
- **AC12** — every arm added by this unit was observed failing against the pre-fix code, and each
  report-shaped arm has a negative control, observed in
  `2026-08-21-build-TOOL-dUnstalledConvoy-23-1-red-first.md`.
- **AC13** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with the unattended driver, leg, cross-component and adopter
self-tests as the exercising legs. `GATE_FULL=1` for the Definition of Done.

## 8. Open questions

- **F1 — gate or report?** RESOLVED by the owner, 2026-08-21: report. The alternatives were a hard gate
that wedges an unattended run with no in-band exit, staying dark indefinitely, or re-admitting
retraction. A report is the only one that leaves the mechanism doing something it can actually do.

- **F2 — does `DISPATCH_GRADING` survive as an off switch for the report?** RESOLVED: no. It existed to
gate a failure; a report that always runs has nothing to gate, and a key that only silences output is a
way to make a check dark without saying so.

## 9. Revision log

- rev-3 · 2026-08-21 · a second spec review returned BLOCKED. rev-2's central claim — that union gives a
  corrective declaration an in-band exit — is FALSE: `pass_commit`'s window excludes its anchor, so a
  later row cannot cover an earlier commit. The owner then resolved the underlying fork: the comparison
  becomes a REPORT, which dissolves the stall, the flip, the rollback key and F1's whole dependency on
  a sentence that was not true. S3 now states the window's boundary and ordering, which rev-2 left
  implied and a reviewer traced to arm C flipping green.
- rev-2 · 2026-08-21 · re-grounded on the code after the first spec review; dropped four scope items
  naming machinery `e42cb5a` deleted.
- rev-1 · 2026-08-21 · written against the review records rather than the code. That was the defect.

## 10. Reuse audit

Every predicate this needs is already in `lib-unattended.sh`; S5 edits one rather than adding a sibling.
The report channel already exists. Net this unit DELETES a conf key, two prose blocks and a branch, and
adds no file, no kit and no helper.

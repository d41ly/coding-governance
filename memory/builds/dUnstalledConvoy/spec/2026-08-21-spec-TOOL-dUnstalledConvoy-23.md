# TOOL-dUnstalledConvoy-23 — the dispatch write-set grading, re-grounded on the append-only record, and the conditions for turning it on

**Status:** SPECCED · rev-2 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

## 1. Goal

Make check 23's grading of a dispatch declaration against what the pass committed correct enough to
ship ON. Today it is inert behind `DISPATCH_GRADING` and the leg announces the dark state on every run
carrying dispatch rows.

**rev-1 of this spec was written against the four review records instead of against the code, and the
commit that deleted the widening branch is an ancestor of this spec's own BASE.** Four scope items and
three acceptance criteria named machinery that no longer exists. This revision is written against
`verb_dispatch`, `check 23` and `lib-unattended.sh` as they stand at `d9728f89`.

## 2. Scope (IN)

- **S1 — the GRADED SET of a unit is the UNION of its rows whose window contains the commit.** The
  record is append-only and the driver's own rationale tells a run that needs more paths to declare
  again; the leg's fold at `tools/unattended/check-unattended.sh` keeps only the LAST row per
  `(group, unit)` and silently discards the rest. Those are two answers to one question and the
  driver's is the one the protocol published.
- **S2 — each row's window is bounded above** by the next anchor for the same unit, so a row is graded
  against its own pass's commits rather than every commit to HEAD.
- **S3 — check 23's second window is bounded too.** The no-commit branch scans declared paths over
  `anchor..HEAD` and is not covered by S2.
- **S4 — `normpath` handles an interior `/./` and a trailing `/.`.** Both spellings are broken by the
  same missing case, and fixing one is how a class becomes an instance.
- **S5 — the empty-proof announcement measures condition 1's own population**, not `sibrows`.
- **S6 — the orphaned re-declaration comment block is deleted.** `unattended.sh` still carries "THE
  RE-DECLARATION RULE, keyed on GROUP plus UNIT … a strict SUPERSET REPLACES" immediately above the
  code that replaced it, describing a rule the same file then says in capitals is gone.
- **S7 — two arms round 4 named as missing:** the `case`-to-`covers` leg fix has no arm and reverts
  green, and cross-component arm 3b never lets either pass commit, so the seam it is named for is never
  entered.
- **S8 — `DISPATCH_GRADING` flips to ON only if S1–S7 land with their arms AND the two-rows-at-one-
  anchor case is closed.** The flip is a scope item with a precondition, not an outcome.
- **S9 — every change lands with its arm in the same commit, and every arm is observed RED first.**

## 3. Non-goals (OUT)

- **Re-introducing any re-declaration, widening or narrowing machinery.** `e42cb5a` removed it with a
  recorded verdict that every version was wrong in a different direction, and the record is append-only
  by design. A redesign that starts by putting the branch back has skipped the argument for removing it.
- `pass_commit`'s permissiveness. Filtering inside it makes check 23 report an out-of-lane pass as "a
  pass that produced no change" — the check going green on the defect it exists to catch.
- `normpath`'s collapse-then-strip ordering, condition 1 and condition 3's refusals, the overlap gate,
  and cross-component arm 3b's existence. Round 4 named these correct; S7 adds to 3b, it does not undo it.
- The declaration grammar and the recording verb.
- The acceptance ledger, the landing anchors, and the rescope verbs.

## 4. Design

S1 is the foundation and everything else is downstream of it. Two `--dispatch` calls at an unmoved HEAD
park two rows under one key, which is exactly the repair the driver documents in place of widening. The
leg's `row[k] = $0` overwrites, so the first declaration is discarded and a pass that declared
`work/a` then `work/b` and wrote both is graded against `work/b` alone. Union is the reading that
matches the record: each row is a declaration, and a pass's lane is everything it declared.

Union also removes the reason S8 needs care. Under last-wins the flip creates a terminal red with no
in-band exit — a corrective declaration lands at a new anchor and the surviving bad row's window still
contains the offending commit. Under union a corrective declaration WIDENS the graded set, which is the
in-band exit, and it does so without any code that rewrites or retracts a row.

S2 and S3 are the two windows. S2 is round 4's D2 and is still live at this base; S3 is its sibling that
round 4 found and no revision has addressed. Both narrow what a row is graded against; neither changes
what a row means.

S6 is not tidying. A comment describing deleted behaviour, sitting above the code that deleted it, is
where rev-1 of this spec got its mental model — the library header still advertises "the driver's
re-declaration rule" as a caller. Deleting it is the cheapest possible fix for a defect that has already
cost one spec revision.

## 5. Production-readiness checklist

- **security** — unchanged. Every check runs under the run's own uid and a determined run can declare a
  wide set up front. What this restores is catching a run that is WRONG.
- **perf/scale** — S1 reads more rows per unit; S2 and S3 narrow each window. Net work per row falls.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — S5 is exactly this: a proof over an empty population must say so.
- **observability** — S8 replaces the dark announcement with ordinary grading output.
- **testing/gates** — the full bar plus the driver, leg and cross-component suites, every arm RED-first.
- **migration/rollback** — `DISPATCH_GRADING` stays a declared key and blank keeps the dark path, so a
  project that hits trouble sets it blank. AC9 asserts the rollback rather than assuming it.
- **help/ docs** — `PROTOCOL.template.md`'s conf table, the key's comment in both confs, and the
  driver's own rationale block all describe the current default; S8 updates every carrier it changes,
  and S6 removes one that is already wrong.

## 6. Acceptance criteria

- **AC1** — a unit with two rows at ONE anchor that commits inside the union of both is GREEN, observed
  in `tools/unattended/check-unattended.test.sh`.
- **AC2** — the same unit committing outside that union still REDS, so union widened the set without
  disarming the check, observed in `tools/unattended/check-unattended.test.sh`.
- **AC3** — the fold emits one row per `(group, unit)` per distinct anchor and discards none, asserted
  by comparing the fold's row count against the file's for a unit with rows at two anchors, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC4** — a row whose unit has a LATER anchor is graded only against commits before that anchor,
  observed in `tools/unattended/check-unattended.test.sh`.
- **AC5** — the no-commit branch's path scan is bounded by the same upper anchor, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC6** — `normpath` returns `a/b` for `a/./b`, `a/b/.`, `a/b/./` and `./a/./b/.`, observed in
  `tools/unattended/unattended.test.sh`.
- **AC7** — the empty-proof announcement fires when condition 1's population is empty and stays silent
  when it is not, observed in `tools/unattended/unattended.test.sh`.
- **AC8** — `grep -c 'RE-DECLARATION RULE' tools/unattended/unattended.sh` returns 0 and the library
  header no longer names a re-declaration caller, observed by `grep`.
- **AC9** — with `DISPATCH_GRADING` blank the leg announces DARK and grades nothing; with it set the
  leg grades. Both arms present, so the rollback is observed rather than asserted, observed in
  `tools/unattended/check-unattended.test.sh`.
- **AC10** — round 4's `case`-to-`covers` fix reverts RED, and cross-component arm 3b commits for at
  least one pass, observed in `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/cross-component.test.sh`.
- **AC11** — every arm added by this unit was observed RED against the pre-fix code, observed in
  `2026-08-21-build-TOOL-dUnstalledConvoy-23-1-red-first.md`, which names the staged break per arm.
- **AC12** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with the unattended driver, leg, cross-component and adopter
self-tests as the legs that exercise this. `GATE_FULL=1` for the Definition of Done.

## 8. Open questions

**F1 — union or last-wins for a unit's graded set?** RESOLVED: union. Last-wins contradicts the
driver's published repair and creates a terminal red with no in-band exit, which is one of the two
failure modes the backlog row for this unit names as things to design against.

**F2 — does S8 flip the default in this unit?** RESOLVED: yes, but as a gated scope item. rev-1 made
the flip unconditional and a reviewer was right to attack it. The precondition is S1–S7 landed with
arms, and AC9 pins the rollback in both directions so the flip is reversible by one conf value.

## 9. Revision log

- rev-2 · 2026-08-21 · re-grounded on the code at BASE after a spec review returned BLOCKED with five
  blockers. rev-1 named a re-declaration lookup, a `cur` selection, a narrowing test and a `curgrp`
  gate, none of which exist at `d9728f89` — `e42cb5a` deleted all four and is an ancestor of that base.
  S1 is new and is the finding rev-1 missed entirely: the leg's fold discards all but the last row per
  key, so the driver's own append-again repair loses a declaration. The flip is now conditional.
- rev-1 · 2026-08-21 · initial draft, written against the four review records rather than against the
  code. That is the defect, not the method: the records describe a tree three commits older than the
  spec's own base.

## 10. Reuse audit

`lib-unattended.sh` already holds every predicate this unit needs and S4 edits one of them rather than
adding a sibling. No new library function is proposed — rev-1's scan-forward helper is dropped, because
its two callers wanted different answers and that is the defect this whole build has been repeating. No
new file, no new kit, no new conf key.

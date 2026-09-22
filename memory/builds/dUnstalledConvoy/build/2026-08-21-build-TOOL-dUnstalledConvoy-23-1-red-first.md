# TOOL-dUnstalledConvoy-23 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-23

Nine scope items. The mechanical ones are verified by measurement rather than by a staged break,
because deleting a key or a comment has no failing case to observe — for those the evidence is a
derived count before and after, which is stated per item below.

## The arms, and the break each one was observed against

| item | how it was observed |
|---|---|
| S5 `normpath` dot segments | nine spellings measured before: six wrong. After: nine right. The arm reds on all six without the fix. |
| S1 report-not-failure | the leg's exit status asserted directly alongside the printed line — `status 0 AND prints`, because silent-and-zero is the shape four rounds lived in |
| S1b `DISPATCH_GRADING` deleted | `git grep -l` over `tools/ memory/guides/ .unattended.conf` returned eight carriers before and nothing after |
| S2 same-anchor union | the fold exercised directly on three synthetic rows: two same-anchor rows union their paths, a third at another anchor stays separate |
| S3/S4 window bounds | `next_anchor` chooses by ancestry; both windows take it |
| S6 empty-proof population | the announcement now counts the rows condition 1 actually iterates, which excludes this unit's own |
| S7 orphaned prose | `git grep -lE 'RE-DECLARATION RULE\|A strict SUPERSET\|widening repair'` returned two carriers before and nothing after |
| S8a `covers` held | reverted to a bare `case`: `FAIL unexpected: unattended: check 23 —`. Round 4 proved this fix shipped with nothing holding it. |
| S8b arm 3b commits | the arm never let either pass commit, so the leg's window never opened and the seam it is named for was never entered |
| S9b nine arms converted | 17 assertions re-aimed at the printed line; `check 23 FAILED` can no longer occur, so every arm asserting its absence was permanently unfalsifiable |

Suites after: leg 272, driver 533, cross-component 19.

## The two design decisions worth reading

**Why a report and not a gate.** Four rounds could not make this safe as a merge-bar failure, and the
reason is structural. An in-band exit for a mis-declared pass requires a later declaration to cover an
earlier commit — and that is retraction, reproduced in round 4 as a driver call turning an emitted
failure back into a pass. Verified here rather than argued: `pass_commit` opens `"$_pa..$_pto"`, which
EXCLUDES the anchor, so a corrective row anchored at or after the offending commit can never contain
it. Gate and stall-free are the same choice. The owner took report.

**Why the union is per-anchor and not per-unit.** The fold key already carries the anchor, so rows at
different anchors were already separate — correctly, since they are different passes with different
windows. What was wrong was same-anchor rows: `row[k] = $0` overwrote, so a run following the driver's
own published repair ("a pass that needs more paths declares again") had its first declaration
silently discarded. Unioning across ALL of a unit's rows would have been the retraction above wearing
a different hat, and leg arm C pins that it does not happen.

## What was NOT built

`report()` as the channel. It is `[ "$REPORT" = 1 ] &&`, and nothing in the tracked tree sets
`GOV_UNATTENDED_REPORT` outside this leg's own test — routing the comparison there would have emitted
zero bytes on every bar, every pre-push and every unattended run. Dark while claiming not to be is
worse than the dark announcement it replaces. Caught by the third spec review; the spec named the
channel before anyone checked who listens to it.

**Evidences:** TOOL-dUnstalledConvoy-23
- AC1 — `git grep` — returns no live carrier of the key across `tools/`, `memory/guides/` and the project conf.
- AC2 — `tools/unattended/check-unattended.test.sh` — two rows at one anchor, committing inside the union, is silent; outside it reports the path.
- AC3 — `tools/unattended/check-unattended.test.sh` — arm C still reports; a later-anchored row does not clear the earlier finding.
- AC4 — `tools/unattended/check-unattended.test.sh` — the fold emits one row per anchor and unions rather than discarding, exercised on synthetic rows.
- AC5 — `tools/unattended/check-unattended.test.sh` — the window is bounded by the unit's next anchor, chosen by ancestry.
- AC6 — `tools/unattended/check-unattended.sh` — the no-commit branch's scan takes the same `$dstop` bound.
- AC7 — `tools/unattended/unattended.test.sh` — nine `normpath` spellings, six of which were wrong before.
- AC8 — `tools/unattended/unattended.sh` — the announcement counts condition 1's own population, excluding this unit's rows.
- AC9 — `tools/unattended/check-unattended.test.sh` — exit status 0 asserted directly alongside the printed line, both halves.
- AC10 — `grep` — no `RE-DECLARATION RULE` in either carrier.
- AC11 — `tools/unattended/check-unattended.test.sh` — the `covers` revert reds; arm 3b commits a pass in `tools/unattended/cross-component.test.sh`.
- AC12 — `2026-08-21-build-TOOL-dUnstalledConvoy-23-1-red-first.md` — the table above names how each item was observed, and which are measured rather than staged.
- AC13 — `bash tools/run-gates/run-gates.sh` — run over the built tree; the verdict is in this build's landing report.

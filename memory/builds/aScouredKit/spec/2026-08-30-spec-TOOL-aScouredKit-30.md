# TOOL-aScouredKit-30 — one derivation everywhere, and the dead pointer REPORTED

**Status:** CLOSED · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-31 TOOL-aScouredKit-32 |

<!-- /gen:spec-records -->

## 1. Goal

Withdraw `TOOL-aScouredKit-15`'s persistence mechanism, which three review rounds could not make
work, and reduce that unit to the half that does: the dead sibling pointer becomes LOUD instead of
silent, without becoming a red an adopter cannot clear.

## 2. Scope (IN)

- S1. `{kit}/.workflows-rel` — the store, its write and its read — is removed entirely.
- S2. The positional leaves `[adopt]` too, so `adopt` and `--check` resolve the sibling by ONE
  derivation and cannot disagree.
- S3. `_wf_absent_kit` and its exit-0 branch go. The distinction it claimed cannot be made.
- S4. `--check` REPORTS a dead pointer at exit 0, naming both paths, the cause, and the backlog row
  that blocks the real fix. It does not red.
- S5. `DRIFT_WORKFLOWS_REL` survives as the hand-install escape hatch, and its use is confined to
  people who run both invocations themselves.

## 3. Non-goals (OUT)

- Fixing the underlying defect. It needs a cross-entry destination token govkit does not have, which
  is `TOOL-aScouredKit-26`; this unit stops making it worse.
- Any change to `tools/workflows/`, the review-harness kit, or the registry.

## 4. Design

Three rounds each produced a fix whose next round refuted it, and the reason is one constraint the
first design missed: **`adopt` and `--check` must resolve the same value, and `--check` cannot be
given one.** `govkit selfcheck` refuses a gate-leg argv naming a path the entry does not ship — an
adopter may install drift-audit alone — so the leg carries nothing. Every channel that carries an
answer to `adopt` alone therefore makes the two DISAGREE, and the diff arm reds with a message that
misdiagnoses the cause and a remedy that overwrites the correct Skill with the wrong one. That is a
red converted into a green over a broken artifact, which is worse than the silence this all started
from.

The file-based store was the attempt to bridge that gap and it fails for a separate reason: it is
untracked, claimed by no `[[files]]` rule, and in no receipt, so it does not survive a fresh
checkout — where the leg re-derives, disagrees with the committed Skill, and reds.

So the answer is to stop carrying an answer. One derivation, both invocations, always equal. The
pointer is then WRONG in a govkit-deployed tree, exactly as it was before this build — but it is no
longer SILENT, which was the actual finding, and the remaining gap has a row.

### Alternatives rejected

Making the missing sibling RED. It taxes every adopter who legitimately installed drift-audit alone,
and this kit does not require review-harness. Round 3 also proved the "is the kit installed at all"
test cannot be written here: it inspects the DERIVED path, so "not installed" and "installed
elsewhere" are one answer, and the branch restored the silence it was added to remove.

## 5. Production-readiness checklist

- security — N/A; this removes a file write and two reads.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the dead-pointer report IS the state, and it is now the only one.
- observability — the report is the whole deliverable of the surviving half.
- risks — a reader may take exit 0 as "fine". Mitigated by the wording: it names the two files that
  do not exist and says the Skill's commands will not run.
- testing + left-shift gates — `bash tools/drift-audit/adopt-drift-audit.sh --check` on this tree,
  plus the same run in a scratch copy whose sibling directory is renamed.
- migration / rollback — an adopter carrying a `.workflows-rel` from the intermediate state is
  unaffected: nothing reads it, and it is one file to delete.
- user docs — the printed report is the operator-facing text.

## 6. Acceptance criteria

- **AC1** — When `tools/drift-audit/adopt-drift-audit.sh` is read, no line READS OR WRITES a
  `.workflows-rel` file, and no `[adopt]` or `[check]` argv in `tools/drift-audit/kit.toml` carries
  a positional path. Graded on the MECHANISM, not on the token: one comment names the retired store
  so nobody re-adds it, and a `grep -c … == 0` criterion would have forced that warning out of the
  file. The first draft of this bullet said exactly that and was wrong.
- **AC2** — When `bash tools/drift-audit/adopt-drift-audit.sh` and then
  `bash tools/drift-audit/adopt-drift-audit.sh --check` run in that order on a tree whose sibling
  directory has been renamed away, `--check` exits 0, does NOT report template drift, and its
  output names both absent files.
- **AC3** — When the same pair runs on this repo unchanged, `--check` exits 0 and reports the
  harnesses present, with the rendered Skill byte-identical to the committed one.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0.

## 7. Gates

`drift-audit wiring` · `drift-audit selftest` · `govkit selfcheck` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft. PROMOTED, not folded: the closing review went 4 → 3 → 4
  standing, so the loop was NON-CONVERGENT and its blockers became units. This spec exists because
  three consecutive folds each introduced the next round's blocker in this one file, which is the
  signal to change the design rather than patch it again.

## 10. Reuse audit

No new seam; this REMOVES one. The reuse finding that matters is negative and is recorded so the
next author does not re-attempt it: there is no existing channel that carries a per-target answer to
a gate leg's own invocation, and inventing one per kit is what this unit is undoing.
`TOOL-aScouredKit-26` holds the shape of the real one.

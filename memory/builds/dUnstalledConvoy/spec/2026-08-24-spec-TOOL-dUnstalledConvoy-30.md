# TOOL-dUnstalledConvoy-30 — the boundary self-tests are subject `repo`, and the criterion says why

**Status:** CLOSED · rev-1 · 2026-08-24 · node d · Tier-1 · base b164a296 · streams tooling

## 1. Goal

`TOOL-dUnstalledConvoy-26`'s criterion — a leg testing the kit's own source is `kit` — read literally
puts gov's push- and commit-boundary self-tests on the on-demand side. Those legs verify the hook and
guard INSTALLED IN THIS REPOSITORY, so taking them off the automatic bar would remove the checks that
watch the boundary, in the same change that alters what the boundary trusts.

## 2. Scope (IN)

- **S1 — the criterion is sharpened to what a leg READS WHEN IT FAILS.** A leg whose failure means
  "the kit's source is broken" is `kit`; a leg whose failure means "this repository is misconfigured"
  is `repo`. That distinction decides the boundary legs, and the parent's wording did not.
- **S2 — the boundary self-tests are assigned `repo`**, with the sharpened criterion as the reason,
  and the parent spec's repo-subject list is corrected to name them.
- **S3 — the assignment is recorded where the pin lives**, so `TOOL-dUnstalledConvoy-29`'s ratchet
  carries it from the first commit.

## 3. Non-goals (OUT)

- The `subject` field itself, the runner skip, or the cross-check — the parent unit and `-29`.
- Re-subjecting any leg not named here.

## 4. Design

The parent's criterion asked WHAT a leg tests. That is ambiguous for a self-test of a kit whose
product is a repository's configuration: the pre-push self-test tests the push-main kit's source AND
the hook installed here, and the two readings give opposite answers.

Asking what a FAILURE means resolves it without a new vocabulary. A broken kit source is the kit's
problem and can wait for the owner to ask; a misconfigured boundary in this repository is this
repository's problem and belongs on its bar.

## 5. Production-readiness checklist

- **security** — the boundary checks stay on the automatic bar, which is the point.
- **perf/scale** — no change; these legs already run.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — N/A; this is an assignment.
- **observability** — the criterion is stated where the field is declared.
- **testing/gates** — the full bar.
- **migration/rollback** — a value in a descriptor; rollback is a revert.
- **help/ docs** — the parent spec's §3 list is corrected as part of this unit.

## 6. Acceptance criteria

- **AC1** — the boundary self-tests carry `subject = "repo"`, observed by `grep`.
- **AC2** — they RUN on a default bar with the switch off, observed by
  `bash tools/run-gates/run-gates.sh`.
- **AC3** — the sharpened criterion is stated where `subject` is declared, observed by `grep`.
- **AC4** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 bash tools/run-gates/run-gates.sh`. Tier 1: gates plus one focused self-review.

## 8. Open questions

- **F1 — sharpen the criterion, or list the exceptions?** RESOLVED (agent, 2026-08-24): sharpen. A
  list of exceptions is a second population to keep, and the ambiguity would recur at the next leg.

## 9. Revision log

- rev-1 · 2026-08-24 · promoted from round 2's NON-CONVERGENT spec audit, which found four
  repo-subject legs missing from the parent's list and the criterion deciding them the wrong way.

## 10. Reuse audit

No code. A criterion sentence and a set of descriptor values.

# Acceptance ledger — TOOL-dRatifiedSeam-1

**Serves:** journal TOOL-dRatifiedSeam-1

Tier-2 · node d · 2026-09-03

## What the fix actually is, which is not what the spec recommended

F1 asked whether the AUDIT stage belongs in the harness at all, and rev-1 recommended keeping it
with the caller supplying the result. Reading the code produced a better answer: **the harness IS a
workflow script**, and the script runtime provides `workflow({scriptPath}, args)` for running
another workflow inline. The spawn never needed to leave the harness — it needed to stop being
delegated to an agent that cannot hold the tool. No harness in this repo had called `workflow()`
before this unit.

**But it does not collapse to one call, and assuming it would have been wrong.** `tier2-review.js`
REFUSES a spec-audit whose `subjects` is not a non-empty array of `{path, blob}` with 7-40 hex per
subject, and a workflow script has no filesystem and no git, so it cannot resolve a blob. So the
split is forced rather than chosen: an AGENT does what only an agent can — read the tree and pin
each spec at its blob — and the SCRIPT does what only the script can, which is hold `Workflow`. The
old code gave the agent both jobs, and the second is the one it could not do.

## Acceptance criteria

**Evidences:** TOOL-dRatifiedSeam-1

- AC1 — MET IN ITS MECHANISM via `bash tools/workflows/unattended-build.test.sh`, not end to end,
  and the distinction is stated rather than blurred.
  `bash tools/workflows/unattended-build.test.sh` reaches `phase:Build` through the fixed AUDIT
  stage in every terminal-verdict arm, and an arm asserts the trace carries
  `workflow:tools/workflows/tier2-review.js`, so the sub-workflow is invoked BY THE SCRIPT. What is
  NOT claimed is a full SPEC → AUDIT → BUILD run against a real build: that would author specs and
  build units in a live repository, which is a destructive way to answer a narrow question. AC1's
  residue is closed by S4 below instead.
- AC2 — MET — `bash tools/workflows/unattended-build.test.sh` arms the absent verdict, the
  non-integer blocker count and the impossible pairing, each as its own refusal. `AUDIT_SCHEMA` no
  longer binds this path because there is no agent in it; the obligation became an explicit check,
  which is stronger — a schema on an agent is a retry prompt, and this is a refusal.
- AC3 — MET, OBSERVED BY MUTATION — replacing the pairing guard with `if (false)` reds
  `S3 CONVERGING with 0 blockers THROWS` and `S3 ...and the refusal names the pairing` by name, and
  restoring returns 28 arms green.
- AC4 — MET — `grep -nE "as a Workflow|scriptPath: tools"` over
  `tools/workflows/unattended-build.js` returns exactly one line, and it is inside the comment
  explaining the defect. No instruction ordering a sidechain agent to invoke a tool it cannot hold
  survives in any `agent()` prompt.
- AC5 — MET — `bash tools/workflows/unattended-build.test.sh` exits 0 at **28 arms**, up from the
  21 it reported before this unit. rev-2 corrected this criterion precisely because the suite
  already exited 0 at 21, so the original wording was satisfied by building nothing.
- AC6 — MET — the `agent-cap` hook did not deny the changed script: the S4 probe below invoked a
  workflow whose script carries no fan-out primitive at all, and a `workflow()` call is not a
  spawn. The changed harness adds one `agent()` call for the subject resolver, which is a single
  spawn and needs no marker.
- AC7 — pending — `bash tools/run-gates/run-gates.sh` runs at the closing bar; recorded there.

## S4 — the one thing 28 mocked arms cannot buy

The suite grades the harness against a runtime double whose `workflow` I wrote myself. That proves
the harness CALLS it correctly and proves nothing about whether the real runtime provides it. The
whole fix rests on that assumption, so it was measured rather than assumed:

    workflowIsAFunction: true
    childReturn: {verdict: "CONVERGED", blockers: 0, reportPath: "probe.md", from: "child"}
    threw: null
    returnsTheShapeTheHarnessReads: true

`workflow()` is available to a script and returns the child's value intact, in the exact shape the
harness reads. 0 agents, 0 subagent tokens, 55 ms — confirming it is a script-level call and not a
delegated spawn, which is the entire point of the change.

## Two suite arms were re-pointed, and neither was a defect

- One grepped for `kind: "spec-audit"` inside the audit PROMPT. The kind moved into the
  sub-workflow's args object, where it is single-quoted. The arm now accepts either quoting, because
  what is graded is that `tier2-review` is TOLD the kind — an arm pinning one spelling is grading
  punctuation.
- One asserted the absent-verdict throw carries the sentence about CONVERGED never being a default.
  My split moved that sentence onto a different branch; the sentence was restored to the branch the
  arm grades, rather than the arm being loosened.

Both graded the right property in the wrong place. Loosening either would have been the cheaper fix
and the wrong one.

## What is still owed

`dRatifiedSeam`'s M4 spec audit was SELF-review — five cold reviewers died on server 529s. A cold
pass on both specs remains unpaid, and this unit does not claim one.

# TOOL-dRatifiedSeam-1 — the harness AUDIT stage runs where Workflow exists

**Status:** CLOSED · rev-2 · 2026-09-03 · node d · Tier-2 · base 7c6f3eb7 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-dRatifiedSeam-1-1-acceptance-ledger.md](../build/2026-09-03-build-TOOL-dRatifiedSeam-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-03-prompt-TOOL-dRatifiedSeam-1-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRatifiedSeam-1-1-build-brief.md) | journal | — |
| [2026-09-03-review-DEPL-dRatifiedSeam-1-closing-diff.md](../reviews/2026-09-03-review-DEPL-dRatifiedSeam-1-closing-diff.md) | diff-review | DEPL-dRatifiedSeam-1 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-build.js` drives a build SPEC → AUDIT → BUILD as ordered stages, and
its AUDIT stage orders a sidechain agent to invoke the Workflow tool. A sidechain holds neither
Workflow nor Agent — the capability is ABSENT, not policed — so that stage can never complete and
BUILD is unreachable through the harness. The owner ruled (`TOOL-dRetiredFork-41`) to fix the
harness rather than drop or waive the directive.

## 2. Scope (IN)

- **S1** — Move the work that requires `Workflow` out of the sidechain. The AUDIT stage's *decision*
  stays in the harness; the *spawn* moves to where the tool exists, which is the main loop.
- **S2** — Keep the stage's verdict REQUIRED. `AUDIT_SCHEMA` demands a verdict for a stated reason:
  an absent verdict would otherwise read as a pass. Whatever shape S1 takes must preserve that, or
  it trades a stage that cannot complete for one that cannot fail.
- **S3** — The impossible pairing becomes a REFUSAL by name. The stage agent returned
  CONVERGING-with-0-blockers, which is this repo's own signature for a record no verb produced. The
  harness must refuse that pairing rather than emit it, so the next failure of this kind is loud.
- **S4** — Observe the fixed route completing end to end: SPEC → AUDIT → BUILD on a fixture build,
  with a real verdict the AUDIT stage produced.
- **S5** — `tools/workflows/unattended-build.test.sh` grades the fix. It is currently registered in
  no manifest and run by no bar (`TOOL-dBriefedPass-7`); this unit does not have to fix that, but
  its arms must at minimum be run and reported here.

## 3. Non-goals (OUT)

- Making the harness ENFORCE anything. `TOOL-dBriefedPass-4` ratified that a Workflow harness buys
  pass ORDER and never enforcement: it has no filesystem, so every observation is its own agent's
  claim. This unit restores the ORDER guarantee and claims nothing more.
- Registering the suite as a bar leg. That is `TOOL-dBriefedPass-7` and it is the five-declaration
  act `TOOL-dBriefedPass-3` describes.
- Rewriting the SPEC or BUILD stages, which complete today.
- Raising any concurrency bound. The cap stays whatever `tools/hooks/agent-cap.js` resolves.

## 4. Design

### The constraint that shapes everything

A sidechain agent holds neither tool, and that is measured rather than assumed — `AGENTS.md` §8
states it, and the stage agent's own behaviour confirmed it: it searched the deferred registry three
times, found neither, refused to fabricate a verdict, and wrote nothing. It was right on every
count. So the fix cannot be "ask the sidechain harder"; the spawn has to happen where the tool is.

### What is newly possible

`tools/hooks/agent-cap.js` carries a third marker, `gov:sequential-agents(5)`, spelling ratified by
the owner 2026-09-01, and it is the ONLY marker that admits a loop. It exists because
`TOOL-cBriefedPilot-21` ratified `parallelism route: none` while the hook denied `agent()` in any
loop body — bounded-parallel permitted by the hook and forbidden by the verdict, strictly sequential
required by the verdict and forbidden by the hook. A harness iterating a build's units sat in that
gap and could not be written at all. It can now, which widens the option set this unit chooses from.

The marker is a CLAIM, never a permission: every clause must hold, and the two carrying weight are
that the loop iterates a bare identifier the hook already proves bounded, and that a one-call sweep
after the scan makes the number a SPAWN count rather than an ITERATION count.

### Rollout

The harness is not on any bar, so this lands without a gate moving. S4's end-to-end observation is
the evidence, and it is the acceptance rather than a demonstration.

### Alternatives rejected

Dropping the directive, and standing a default waiver on it. Both were offered to the owner and
declined; a standing waiver on a directive nobody can satisfy tends to become permanent.

### Files touched (estimate)

`tools/workflows/unattended-build.js` (364 lines; stage 2 begins at line 229, `AUDIT_SCHEMA` at 173)
and `tools/workflows/unattended-build.test.sh`.

## 5. Production-readiness checklist

- security — no new write path; the harness orchestrates and writes nothing itself.
- perf / scale — one stage's spawn moves; agent count is unchanged and stays under the cap.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3 is this line: the impossible verdict pairing becomes a named
  refusal instead of an emitted record.
- observability — the AUDIT stage must name which agent produced its verdict, so a future absent
  capability is attributable rather than mysterious.
- risks — the real one is S2's inverse: a stage that cannot complete is at least loud, and a stage
  that completes with a fabricated verdict is silent. The fix must not trade one for the other.
- testing + left-shift gates — `bash tools/workflows/unattended-build.test.sh` (21 arms), run by
  hand because the suite is on no bar.
- migration / rollback — a harness script; revert is the rollback.
- user docs — `memory/guides/BUILD-METHOD.md` M6 mentions the driven route; update only if the
  invocation changes.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/unattended-build.js` runs against a fixture build, the AUDIT
  stage COMPLETES and BUILD is reached, which neither does today.
- **AC2** — When the AUDIT stage completes, its verdict is a real one from the closed set, and
  `AUDIT_SCHEMA` still refuses a run that omits it.
- **AC3** — When a stage returns CONVERGING paired with 0 blockers, `unattended-build.js`
  REFUSES by name rather than emitting the record. Observed by staging that pairing.
- **AC4** — When the AUDIT stage runs, the agent that invokes `Workflow` is one that HOLDS it,
  demonstrated by that invocation succeeding in AC1's run. rev-1 graded this as the ABSENCE of a
  `grep -n "Workflow"` hit inside the stage prompt, which deleting the prompt would satisfy and
  which rewording without fixing would also satisfy — an absence over a scope no machine
  defines.
- **AC5** — `bash tools/workflows/unattended-build.test.sh` exits 0 AND its arm count is HIGHER
  than the 21 it reports today, because this unit adds the arms for S3's refusal and S4's
  end-to-end route. Measured before authoring: that suite already exits 0 at 21 arms, so rev-1's
  criterion was satisfied by doing nothing.
- **AC6** — When the changed harness is invoked through the `Workflow` tool, the `agent-cap`
  PreToolUse hook does not deny it. rev-1 said `node tools/hooks/agent-cap.js` grades a script
  FILE, and that is not its interface: it reads a PreToolUse payload from stdin
  (`readFileSync(0)`), uses `process.argv` only for `--only=`, and given a path it hangs. The
  observation is the tool call being permitted, not a command that cannot make it.
- **AC7** — `bash tools/run-gates/run-gates.sh` is green, AND its `workflow script syntax`,
  `verifier fan-out` and `agent-cap self-test` legs are among the legs that RAN rather than
  being skipped by a guard. A bare green bar proves nothing about this change. rev-2 named two
  legs that DO NOT EXIST — `workflow syntax` and `review-protocol parity`, both missing their
  real suffixes — which the spec-tokens gate caught and which would have sent a builder looking
  for legs no manifest declares.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `agent-cap self-test`

## 8. Open questions

- **F1 — does the AUDIT stage still belong in the harness at all?** If its spawn must happen in the
  main loop, the harness may be sequencing a stage it cannot run. Recommendation: keep it, and have
  the harness sequence a stage the CALLER supplies the result for — order is what the harness buys
  and it can still buy that. Resolve before writing code; it decides the whole shape.
- **F2 — does the fix need the `gov:sequential-agents(5)` marker, or is the AUDIT stage a single
  spawn?** Recommendation: single spawn, no marker. Reach for the marker only if the stage genuinely
  iterates units, and a marker taken without need is a claim nobody checked.
- **F3 — should S3's refusal live in the harness or in the driver that reads its record?**
  Recommendation: the harness, because it is the thing that can emit the pairing; a reader-side
  check would grade a record already written.

**RESOLVED (agent, 2026-09-03): all three forks settled, and F1 against its own stated Recommendation.** F1 — the stage STAYS in the harness, but not with the caller supplying the result: the harness is a workflow script, so it calls `workflow({scriptPath})` itself. The recommendation was written before reading the runtime. F2 — no `gov:sequential-agents(5)` marker; the resolver is a single spawn, and a marker taken without need is a claim nobody checked. F3 — the refusal lives in the harness, which is the thing that can emit the pairing.

## 9. Revision log

- rev-1 · 2026-09-03 · initial draft. Written against `TOOL-dRetiredFork-41` and grounded on
  `TOOL-dBriefedPass-4`'s order-not-enforcement ruling, plus the discovery that `agent-cap.js`'s
  loop denial is superseded by `gov:sequential-agents(5)`.
- rev-2 · 2026-09-03 · folded four M4 findings against this spec's own acceptance, each verified
  against the tree. AC5 was ALREADY TRUE before the unit starts — the suite exits 0 at 21 arms
  today, measured — so it was satisfied by building nothing. AC6 named a witness that is not an
  interface: the hook reads stdin, and invoked with a path it hangs (`rc=124`, measured). AC4
  graded an ABSENCE over a scope no machine defines. AC7 was a bare green bar. The audit was
  self-review, the cold reviewers having died on server 529s, so a cold M4 pass is still owed.

## 10. Reuse audit

**Probe result.** No existing seam fits. The evidence: `tools/workflows/` holds three harnesses
(`tier2-review.js`, the two `drift-audit-*.js`) and none of them runs a stage whose spawn must
escape the sidechain — they are invoked FROM the main loop and fan out from there, which is exactly
the shape this unit has to adopt. So the reuse here is a PATTERN the siblings already demonstrate
rather than a symbol to extend, and `tier2-review.js` is the file to read before writing.

**Recall terms used:** `sidechain agent Workflow tool absent capability measured harness fan-out
main loop agent-cap hook PreToolUse`. It returned `TOOL-dRetiredFork-41` (the ruling),
`memory/guides/REVIEW-PROTOCOL.md`, `TOOL-dRetiredFork-22`, and `TOOL-dBriefedPass-4` — the last
being the ratified limit on what any Workflow harness can buy, which §3 takes as a non-goal rather
than rediscovering.

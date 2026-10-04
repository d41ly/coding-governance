# TOOL-aWardedAudit-6 — the closing review's batched minors, round 1

**Status:** OPEN · rev-1 · 2026-10-05 · node a · Tier-2 · base 8cfe5678 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aWardedAudit-6-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aWardedAudit-6-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review, round 1: its four MEDIUM and seven LOW items (17 raw confirmed
findings), batched into one unit as the method requires. Each item below is closed by the mechanism
named beside it; the review record carries the full findings.

## 2. Scope (IN)

- **S1** — M1 (ids 2, 9, 19): a harness call that names a `slug` is placed in that slug's build: a
  `reviewDir` under another build, or a `units[].specPath` outside `builds/<slug>/`, is denied by
  name. A unit with no `specPath` is skipped. Observed by AC1.
- **S2** — M2 (id 3) and L5 (id 13): the hook reads `phase:` and `spec-audit:` inside the run-state
  file's `## Run facts` section only, as the driver's `fact()` does, and treats LANDING, LANDED and
  ABORTED as no live run, since no pre-code audit is owed past the close. Observed by AC2.
- **S3** — M3 (id 15) and L7 (id 17): arms for a harness call with no run-state file, for an
  ABORTED and a LANDING record, and for a prompt README with no key beside a dated conf default.
  Observed by AC3.
- **S4** — M4 (id 16): an arm that runs `--close` over a record whose BASE README carries a
  prompt-mode `spec-audit:` line, and reads `specs-audited — not gradable`. Observed by AC4.
- **S5** — L6 (ids 14, 18): the hook defaults an EMPTY `reviewDir` as the harness does. Observed by AC1.
- **S6** — L1 (ids 6, 12, 23): the driver's fail 53, 54, 55 messages and the not-owed line name the
  conf read at the default-branch side, not "at BASE". Observed by AC5.
- **S7** — L2 (ids 11, 20), L3 (id 21), L4 (id 22): the hooks README limits paragraph and the rule-0
  header, the Skill's "both keys are read at BASE", the protocol's `specs-audited` row and the
  method's M4 state the default-branch-side read and name both owner routes. Observed by AC6.

## 3. Non-goals (OUT)

- A parity gate between the hook's no-live-run set and the driver's terminal set: the hook's set
  is a superset by design, LANDING included, so an equality would be wrong.

### Edges

none

## 4. Design

### Evidence

The closing review record for this build, round 1, and the code at base `8cfe5678`. The harness
reads `reviewDir` as `a.reviewDir || 'memory/builds/' + slug + '/reviews'` and carries unit spec
paths as `units[].specPath`. The driver's `fact()` reads only under `## Run facts`.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/memory-tree/BUILD-METHOD.template.md`

### Alternatives rejected

- **Two units.** The items split into a hook half and a driver-and-carriers half, but they are built
  inline in sequence, so a second unit buys no concurrency.

## 5. Production-readiness checklist

- perf / scale — none beyond a section scan of one small file.
- security — S1 narrows an admission; S2 narrows a refusal to the phases it was meant for.
- error / empty / loading states — every new deny names its field.
- observability — messages name the read they made.
- testing — each changed verdict is observed against the base code first.
- migration — none.
- user docs — S7.
- risks — the message edits strand the arms quoting them; those arms move in this unit.

## 6. Acceptance criteria

- **AC1** — When a harness call names `slug: tSA` with `reviewDir` under another build, or a
  `units[].specPath` outside `builds/tSA/`, rule 0 denies naming the field; with `reviewDir: ""` it
  places the call in `builds/tSA/`.
  Red when: the base hook admits on the other build's README.
- **AC2** — When the run-state file carries a `phase: BUILDING` line above `## Run facts` and
  `phase: LANDING` inside it, rule 0 admits a slug README's dated key.
  Red when: the whole-file read takes the stray line, or LANDING reads as live.
- **AC3** — When a harness call meets no run-state file, rule 0 admits on a slug README's `spec-audit: 2026-10-05`
  and denies a prompt README's; an ABORTED record admits; a prompt README with no key beside a dated
  conf default admits.
  Red when: any of these verdicts moves under a one-token mutation of the S2 condition.
- **AC4** — When `--close` runs over a record whose BASE README carries a prompt-mode `spec-audit:`
  line, it prints `specs-audited — not gradable`.
  Red when: the clear in check 89's branch is deleted.
- **AC5** — When the BASE conf cannot be evaluated, the refusal names `the default-branch side`.
  Red when: the message still says the pinned BASE.
- **AC6** — When `grep -n 'both keys are read at BASE' tools/unattended/SKILL.template.md` runs, it
  prints nothing, and the `kit/dogfood doc parity` and `unattended skill wiring` legs are green.
  Red when: a carrier still states the at-BASE read.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `unattended kit gate` · `unattended skill wiring` · `kit/dogfood doc parity` · `build-method size` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · the base hook, which places a harness call by reviewDir alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the closing review's round-1 minors.

## 10. Reuse audit

No new seam: `python tools/codebase-map/reuse_lookup.py` ranked scratch-guard's `readFrontMatterKey`,
already reused. Each item extends the code its finding names; the run-state reader follows the driver's `fact()`
section scope. `python tools/memory-recall/query.py` returned `TOOL-aBatchedMinors-5`, the batching
rule this unit follows.

Recall terms used: spec-audit SPEC_AUDIT_DEFAULT opt-in owner self-grant second anchor published prompt mode README front matter may grant D12-j

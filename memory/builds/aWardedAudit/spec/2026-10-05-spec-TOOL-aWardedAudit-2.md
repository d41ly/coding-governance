# TOOL-aWardedAudit-2 — the fan-out hook admits a spec audit only on an owner opt-in

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-2 · base 35438ba0 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aWardedAudit-2-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aWardedAudit-2-1-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aWardedAudit-1-closing-diff-round1.md](../reviews/2026-10-05-review-TOOL-aWardedAudit-1-closing-diff-round1.md) | diff-review | TOOL-aWardedAudit-1 TOOL-aWardedAudit-3 |

<!-- /gen:spec-records -->

## 1. Goal

Rule 0 of the fan-out hook denies a `kind: spec-audit` Workflow call unless the build README in the
WORKTREE carries a dated `spec-audit:` key or the worktree conf a dated `SPEC_AUDIT_DEFAULT`. A run
can write either line a second before the call, so the hook admits exactly the self-opt-in the
driver now refuses. This unit makes the hook agree with the driver before any audit token is spent.

## 2. Scope (IN)

- **S1** — When the build folder holds a run-state file whose `phase:` is not `LANDED` or
  `ABORTED`, rule 0 admits only on that file's `spec-audit:` fact, which the driver pinned from the
  owner's side. The worktree README and conf are not read on that path. Observed by AC1 and AC2.
- **S2** — With no live run-state file, a README whose front matter declares `authorized-by:` other
  than `slug` admits nothing by its own `spec-audit:` key; the deny names the mode. The worktree
  conf default still admits on that path, as it does today. Observed by AC3 and AC4.
- **S3** — Every existing rule 0 arm keeps its verdict. Observed by AC5.
- **S4** — A Workflow call whose args carry `specAudit` is judged by the same predicate as a
  `kind: spec-audit` one: the build harness runs its audit through a runtime `workflow()` call no
  hook sees, so the call carrying `specAudit` is the only one to judge. It is placed by the
  harness's own `reviewDir` default when none is passed, and in a live run the value must equal
  the pinned fact. Observed by AC6 and AC7.

## 3. Non-goals (OUT)

- The driver's derivation, which is `TOOL-aWardedAudit-1`.
- An attended session's worktree conf. With an owner present the hook is a guard against drift,
  not forgery, and the BASE read is the one that binds an unattended run.
- A hand-edited run-state fact. The driver's `--close` refuses a fact that disagrees with BASE
  (check 53).

### Edges

- **consumes-from** `TOOL-aWardedAudit-1` — the `spec-audit` fact S1 reads is the one that unit decides.
- **hands-off** `TOOL-aWardedAudit-3` — the hooks README states the rule this unit enforces.

## 4. Design

### Evidence

Read at base `35438ba0`. `checkSpecAuditDeclared` in `tools/hooks/agent-cap.js` places the README at
`<repo>/<parent of reviewDir>/README.md`, reads `spec-audit` through scratch-guard's
`readFrontMatterKey`, then the conf through `readSpecAuditDefault`. The run-state file is
`RUN.md` beside the README; the driver writes `phase: <PHASE>` and `spec-audit: <date>` as
column-1 fact lines under `## Run facts`.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`

### Alternatives rejected

- **Have the hook run `git show` at the default branch.** It would need the remote's tip to mean
  anything, which is a network call inside a PreToolUse hook; the driver already made that
  observation and pinned its answer.
- **A refusal in `--review` instead.** It fires after the audit's agents have run, so the tokens
  this build exists to save are already spent; and 37 existing arms record spec-subject rounds
  with no fact.

## 5. Production-readiness checklist

- perf / scale — one extra file read per spec-audit Workflow call.
- security — narrows an admission; every throw is still a deny.
- error / empty / loading states — an unreadable run-state file is a deny by name.
- observability — each deny names the file and the fact or mode it read.
- testing — each new deny is observed against the base hook first.
- migration — none.
- user docs — the hooks README, in `TOOL-aWardedAudit-3`.
- risks — a run that pinned no fact cannot audit even if the owner edits the README mid-run; the
  owner's route is a fresh preflight.

## 6. Acceptance criteria

- **AC1** — When a live run-state file pins no `spec-audit` fact and the worktree README carries a
  dated key, rule 0 denies naming the run-state file.
  Red when: the base hook admits on the worktree key.
- **AC2** — When a live run-state file pins `spec-audit: 2026-10-05` and the README carries no key,
  rule 0 admits.
  Red when: S1 reads the fact but ignores its value.
- **AC3** — When no run-state file exists and a prompt-mode README carries a dated key, rule 0 denies
  naming `authorized-by: prompt`.
  Red when: the base hook admits.
- **AC4** — When a `LANDED` run-state file sits beside a slug README carrying a dated key, rule 0
  admits.
  Red when: a finished run's file still decides, so an attended audit after landing is denied.
- **AC5** — When rule 0 judges a slug README carrying `spec-audit: 2026-09-20` beside no run-state
  file, it admits, as at base.
  Red when: a rule 0 verdict at base moved.
- **AC6** — When a harness call passes `specAudit: 2026-10-05` beside a live run-state file pinning
  no fact, rule 0 denies naming the run-state file; pinning `2026-10-05`, it admits.
  Red when: the base hook admits, because it judged `kind` alone.
- **AC7** — When the pinned fact is `2026-09-01` and the call passes `2026-10-05`, rule 0 denies
  naming both dates.
  Red when: any dated fact admits any `specAudit`.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · the base hook, which admits on a worktree key the run wrote · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from rule 0 at base and `TOOL-aWardedAudit-1`.
- rev-2 · 2026-10-05 · S4 · AC6 · AC7 · building found the build harness's `specAudit` argument is a
  second self-opt-in route rule 0 never judged: the hooks README says its nested audit is a runtime
  call, so the S1 predicate alone left the main unattended path open.

## 10. Reuse audit

The seam extended is rule 0 itself, `checkSpecAuditDeclared`, and scratch-guard's
`readFrontMatterKey`, which already reads `authorized-by:` for that hook's own exemption.
`python tools/codebase-map/reuse_lookup.py "refuse a front-matter key the run could have written
under a second-anchor mode"` ranked `readFrontMatterKey` among its candidates. `python
tools/memory-recall/query.py` returned `TOOL-dDerivedDocket-19`, whose mode-keyed refusal this
unit mirrors at the tool call.

Recall terms used: spec-audit SPEC_AUDIT_DEFAULT opt-in owner self-grant second anchor published prompt mode README front matter may grant D12-j

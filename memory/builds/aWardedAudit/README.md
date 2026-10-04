---
slug: aWardedAudit
node: a
opened: 2026-10-05
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aWardedAudit-1 TOOL-aWardedAudit-2 TOOL-aWardedAudit-3 TOOL-aWardedAudit-4 TOOL-aWardedAudit-5 TOOL-aWardedAudit-6
---

# aWardedAudit — only the owner can opt a build into the spec audit

## The problem this build exists to solve

The pre-code spec audit is opt-in, but the opt-in is a line any run can write. A prompt-mode run
authors its own build README, so a `spec-audit:` key there is the run opting itself in, and the
driver's not-owed line even recommends writing one. Two runs did; one spent five hours auditing
before any code. The owner rules that only the owner opts in. The prompt is in `prompts/`.

## Expected improvements

- A `spec-audit:` key in a README the run could have written is refused, not honoured.
- A project default counts only from the default branch, never from the run's own pushed tip.
- The fan-out hook denies an audit the driver would not have admitted.
- No carrier tells a run to declare the key; the owner is told instead.

## Detriments if this is not built

- Runs keep opting themselves into multi-hour audit chains the owner never asked for.
- The owner's opt-in ruling stays a memory note one session wrote, enforced by nothing.

## Build-level rules

- Owner provenance has one meaning, the one D12-a and D12-j already use for `asks:` and `may:`.
- Reuse first: `check_authorization`'s mode refusals, rule 0 in `tools/hooks/agent-cap.js`.
- Every new refusal is observed RED on a staged break before it lands.
- No spec audit: none is owed, and none may be self-declared; the closing review is the first.
- Classified at kickoff (M2): every unit MISSING; authored and built inline, in order.

## Parked decisions

- P1 — the owner's per-build opt-in for a prompt-mode run: as built, only `SPEC_AUDIT_DEFAULT` or a
  slug README the owner lands. An invocation flag or a prompt-recording hook was refused.
- P2 — `aEvidencedLens`, live on another branch, carries a prompt-mode `spec-audit:` line its owner
  asked for; after it merges check 89, its close refuses. Land it first, or re-home its opt-in.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWardedAudit-1` | 2 | the driver refuses `spec-audit:` under a second-anchor mode and reads the project default at the default-branch side |
| 2 | `TOOL-aWardedAudit-2` | 2 | the fan-out hook's rule 0 denies a non-slug README key and, in a live run, admits only on the driver's pinned fact |
| 3 | `TOOL-aWardedAudit-3` | 1 | the method, Skill, protocol, conf and hook docs state the owner-only rule, and a decision records it |
| 5 | `TOOL-aWardedAudit-5` | 2 | promoted from the closing review's H1: check 19 refuses a run commit writing `spec-audit:` or `SPEC_AUDIT_DEFAULT` |
| 6 | `TOOL-aWardedAudit-6` | 2 | promoted from the closing review: round 1's four mediums and seven lows, batched |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 5 unit(s) · node a · opened 2026-10-05 · streams tooling
ids TOOL-aWardedAudit-1 TOOL-aWardedAudit-2 TOOL-aWardedAudit-3 TOOL-aWardedAudit-4 TOOL-aWardedAudit-5 TOOL-aWardedAudit-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWardedAudit-1 — the driver honours a spec-audit opt-in only from the owner's side](spec/2026-10-05-spec-TOOL-aWardedAudit-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-aWardedAudit-2 — the fan-out hook admits a spec audit only on an owner opt-in](spec/2026-10-05-spec-TOOL-aWardedAudit-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-aWardedAudit-3 — the carriers state that only the owner opts a build into the spec audit](spec/2026-10-05-spec-TOOL-aWardedAudit-3.md) | 3 | 1 | CLOSED | rev-1 | 2026-10-05 |
| [TOOL-aWardedAudit-5 — the bar refuses a run commit that writes a spec-audit opt-in](spec/2026-10-05-spec-TOOL-aWardedAudit-5.md) | 5 | 2 | OPEN | rev-1 | 2026-10-05 |
| [TOOL-aWardedAudit-6 — the closing review's batched minors, round 1](spec/2026-10-05-spec-TOOL-aWardedAudit-6.md) | 6 | 2 | OPEN | rev-1 | 2026-10-05 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aWardedAudit-1 TOOL-aWardedAudit-2 TOOL-aWardedAudit-3 TOOL-aWardedAudit-5 TOOL-aWardedAudit-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWardedAudit-1` | no |
| 2 | `TOOL-aWardedAudit-2` | no |
| 3 | `TOOL-aWardedAudit-3` | no |
| 5 | `TOOL-aWardedAudit-5` | no |
| 6 | `TOOL-aWardedAudit-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

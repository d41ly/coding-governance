# TOOL-aWardedAudit-1 — the driver honours a spec-audit opt-in only from the owner's side

**Status:** OPEN · rev-1 · 2026-10-05 · node a · Tier-2 · base 35438ba0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aWardedAudit-1-0-run-mandate.md](../prompts/2026-10-05-prompt-TOOL-aWardedAudit-1-0-run-mandate.md) | journal | — |
| [2026-10-05-prompt-TOOL-aWardedAudit-1-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aWardedAudit-1-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The pre-code spec audit is opt-in (TOOL-aBlindedTrial-6), and the opt-in is a `spec-audit: <date>`
line in the build README or a `SPEC_AUDIT_DEFAULT` in `.unattended.conf`, both read at BASE. Under
`authorized-by: prompt` or `recipe` the README is one the run writes, and on the second anchor BASE
is a tip the run pushed, so both reads can return bytes the run authored. Two runs opted themselves
in that way. This unit makes the driver honour the opt-in only from a record the owner landed, the
reading rulings D12-a and D12-j already give `asks:` and `may:`.

## 2. Scope (IN)

- **S1** — `check_authorization` refuses a build README that carries a `spec-audit:` line under a
  mode other than `slug`, as a new numbered refusal, check 89, beside checks 71 and 78. The refusal
  names the mode and the two owner routes: a `slug` README landed on the default branch, or
  `SPEC_AUDIT_DEFAULT` on the default branch. It leaves the specs-audited grader not gradable, as
  every other refused spec-audit read does. Observed by AC1 and AC2.
- **S2** — `SPEC_AUDIT_DEFAULT` is read from `.unattended.conf` at the DEFAULT-BRANCH side: the
  pinned BASE on the first anchor, unchanged, and the merge-base of the observed default-branch tip
  and BASE on the second. A merge-base that cannot be computed reads as no default. Observed by AC3
  and AC4.
- **S3** — The `not owed` preflight line stops telling the run to write the key. Its clause becomes
  a note for the owner's wrap-up, saying the opt-in is the owner's and never the run's. Observed by
  AC5.

## 3. Non-goals (OUT)

- A `slug` README's key on the first anchor: that README was on the default branch before the run
  branched, which is the owner provenance this unit keys on. Unchanged.
- The fan-out hook's own read of the opt-in, which is `TOOL-aWardedAudit-2`.
- The carriers that describe the rule, which are `TOOL-aWardedAudit-3`.
- A run forging the run-state file or the default branch. A run with full shell access can still
  defeat any local check; the control that binds lives on the remote (protocol §9).

### Edges

- **hands-off** `TOOL-aWardedAudit-2` — the hook reads the run-state `spec-audit` fact S1 and S2 decide.
- **hands-off** `TOOL-aWardedAudit-3` — the carriers state the rule this unit enforces.

## 4. Design

### Evidence

Read at base `35438ba0`. `check_authorization` in `tools/unattended/unattended.sh` reads
`spec-audit:` out of the same front-matter scan as `authorized-by:`, then reads the conf blob at
`$base`. Checks 71 and 78 already refuse `asks:` and `may:` when `AUTH_MODE != slug`, after the mode
membership test and check 50. `resolve_base` sets `ANCHOR_KIND` to `run-branch` when BASE is the
pushed branch tip, and `ASHA` holds the observed default-branch tip; every caller of
`check_authorization` runs `trusted_base` first, so both are set. `print_spec_audit_line` ends its
not-owed line with a clause telling the run to write the key into its README front matter, and
`aGraftedHelix` followed it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Ignore a self-written key instead of refusing it.** Ruling D12-j rejected that shape for `may:`:
  ignoring pins `none` and leaves the self-grant attempt invisible in every record.
- **An owner token, such as a flag on the invocation line confirmed by one question.** The driver
  cannot tell the owner's answer from the run's, so the token would be the run's claim with extra
  steps. The default branch is the one record the charter already makes owner-gated.
- **Refuse by anchor rather than by mode.** A prompt README landed on the default branch would then
  carry an opt-in while the same README's `may:` is refused; one rule per key is the simpler reading.

## 5. Production-readiness checklist

- perf / scale — one `merge-base` on the second anchor only; no new process otherwise.
- security — narrows an authorization surface; no new write path.
- error / empty / loading states — the refusal writes nothing, and the grader reads not gradable.
- observability — the refusal names the mode and the two owner routes.
- testing — each refusal is observed against the base driver first.
- migration — none. No live build carries the key under a non-`slug` mode.
- user docs — the Skill, protocol and method, in `TOOL-aWardedAudit-3`.
- risks — an in-flight prompt-mode run that pinned a self-written opt-in refuses at its next resume.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs over a prompt-mode README carrying `spec-audit: 2026-10-05` on
  the second anchor, it refuses at check 89 naming mode `prompt`, and no run-state file is created.
  Red when: the base driver opts the run in by README.
- **AC2** — When the same README declares `recipe`, check 89 refuses before the playbook refusal.
  Red when: the recipe run reaches the playbook check first, or opts in.
- **AC3** — When a prompt-mode run's conf declares `SPEC_AUDIT_DEFAULT` only on its pushed branch,
  preflight prints `not owed` and pins no `spec-audit` fact.
  Red when: the base driver opts the run in by project default.
- **AC4** — When the default is on the default branch and the prompt README is on the run branch,
  preflight prints `opted in by project default`.
  Red when: S2 read the default away from the owner's side too.
- **AC5** — When a two-unit build declares no opt-in, the not-owed line names the owner and carries
  no `recommend spec-audit:` clause.
  Red when: the base line's recommendation still prints.
- **AC6** — When `--preflight` runs over a slug README carrying `spec-audit: 2026-09-20` landed on the
  default branch, it prints `opted in by README spec-audit: 2026-09-20`, as at base.
  Red when: the first anchor's reading moved.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the base driver, which opts a prompt run in by its own README · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the owner's prompt and `check_authorization` at base.

## 10. Reuse audit

The seam extended is `check_authorization`'s mode-keyed refusal, the shape checks 71 and 78 already
take for `asks:` and `may:`, and its existing conf read, moved to the default-branch side.
`python tools/codebase-map/reuse_lookup.py "refuse a front-matter key the run could have written
under a second-anchor mode"` printed `unscanned layers: .sh`, so it cannot see this seam; the seam
was found by reading `unattended.sh`. `python tools/memory-recall/query.py` returned
`TOOL-dDerivedDocket-19` (D12-j) and `TOOL-aBlindedTrial-6`, the ruling and the opt-in this unit
narrows.

Recall terms used: spec-audit SPEC_AUDIT_DEFAULT opt-in owner self-grant second anchor published prompt mode README front matter may grant D12-j
